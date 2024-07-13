import copy
from dataclasses import dataclass, replace
from datetime import timedelta
from typing import TYPE_CHECKING, Callable, Generic, ParamSpec, TypeVar

from databricks.bundles.internal._transform import (
    _transform,
    _transform_optional,
    _transient_field,
)
from databricks.bundles.jobs.functions._signature import Signature
from databricks.bundles.jobs.functions._task_parameters import _TaskParameters
from databricks.bundles.jobs.models.email_notifications import (
    TaskEmailNotifications,
    TaskEmailNotificationsParam,
    TaskNotificationSettings,
    TaskNotificationSettingsParam,
)
from databricks.bundles.jobs.models.run_if import RunIf, RunIfParam
from databricks.bundles.jobs.models.task import Task
from databricks.bundles.jobs.models.task_dependency import TaskDependency
from databricks.bundles.jobs.models.webhook_notifications import (
    WebhookNotifications,
    WebhookNotificationsParam,
)
from databricks.bundles.variables import Variable, VariableOrOptional, resolve_variable

if TYPE_CHECKING:
    from typing_extensions import Self


R = TypeVar("R")
P = ParamSpec("P")


@dataclass(kw_only=True)
class TaskWithOutput(Generic[R], Task):
    return_type: dict[str, type] = _transient_field()  # type:ignore

    def with_task_key(self, value: str):
        return replace(self, task_key=value)

    def add_depends_on(self, task: Task) -> "Self":
        if not task.task_key:
            raise ValueError("Specified task doesn't have task_key")

        task_dependency = TaskDependency(task.task_key)
        depends_on = resolve_variable(self.depends_on)

        # FIXME test it
        if task_dependency in depends_on:
            return self

        return replace(self, depends_on=[*depends_on, task_dependency])

    def with_run_if(self, run_if: RunIfParam) -> "Self":
        return replace(self, run_if=_transform(RunIf, run_if))

    @property
    def result(self) -> R:
        """
        Returns task result. For functions decorated with @task, it's
        their return value.
        """

        raise Exception(
            "Accessing task result outside of @job decorator isn't supported"
        )

    @property
    def output(self) -> R:
        """
        Returns task output.

        Deprecated: use 'result' instead
        """

        raise Exception(
            "Accessing task output outside of @job decorator isn't supported"
        )


@dataclass(kw_only=True)
class TaskFunction(Generic[P, R]):
    function: Callable[P, R]
    base_task: TaskWithOutput[R]

    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> TaskWithOutput[R]:
        task_parameters = _TaskParameters.parse_call(self.function, args, kwargs)
        # deep copy to avoid mutating shared instance
        base_task_copy = copy.deepcopy(self.base_task)
        base_task_with_parameters = task_parameters.inject(base_task_copy)
        signature = Signature.from_function(self.function)

        return replace(base_task_with_parameters, return_type=signature.return_type)


def _transform_min_retry_interval_millis(
    min_retry_interval_millis: VariableOrOptional[timedelta],
) -> VariableOrOptional[int]:
    if not min_retry_interval_millis:
        return None

    if isinstance(min_retry_interval_millis, Variable):
        # FIXME specified variable should be an int with milliseconds, not timedelta
        # we should allow to specify timedelta as well
        return Variable(path=min_retry_interval_millis.path, type=int)

    if min_retry_interval_millis.microseconds:
        raise ValueError("Microseconds are not supported for 'min_retry_interval'")

    return min_retry_interval_millis // timedelta(milliseconds=1)


def _create_task_with_output(
    max_retries: VariableOrOptional[int],
    min_retry_interval_millis: VariableOrOptional[timedelta],
    retry_on_timeout: VariableOrOptional[bool],
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam],
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam],
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam],
    timeout_seconds: VariableOrOptional[int],
    return_type: dict[str, type],
) -> TaskWithOutput:
    return TaskWithOutput(
        task_key="",
        max_retries=max_retries,
        min_retry_interval_millis=_transform_min_retry_interval_millis(
            min_retry_interval_millis
        ),
        retry_on_timeout=retry_on_timeout,
        email_notifications=_transform_optional(
            TaskEmailNotifications, email_notifications
        ),
        webhook_notifications=_transform_optional(
            WebhookNotifications, webhook_notifications
        ),
        notification_settings=_transform_optional(
            TaskNotificationSettings, notification_settings
        ),
        timeout_seconds=timeout_seconds,
        return_type=return_type,
    )
