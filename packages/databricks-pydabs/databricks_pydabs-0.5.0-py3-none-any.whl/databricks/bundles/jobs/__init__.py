from dataclasses import replace
from datetime import timedelta
from typing import Any, Callable, Optional, ParamSpec, TypeVar, overload

from databricks.bundles.internal._diagnostics import Diagnostics
from databricks.bundles.jobs.models.job_environment import (
    JobEnvironment,
    JobEnvironmentParam,
)
from databricks.bundles.jobs.models.tasks.dbt_task import DbtTask
from databricks.bundles.jobs.models.tasks.spark_jar_task import SparkJarTask
from databricks.bundles.jobs.models.tasks.spark_python_task import SparkPythonTask
from databricks.bundles.jobs.models.tasks.sql_task_file import SqlTaskFile
from databricks.bundles.jobs.models.trigger import TriggerSettings, TriggerSettingsParam

__all__ = [
    "ClusterSpec",
    "ClusterSpecParam",
    "ComputeTask",
    "ComputeTaskFunction",
    "CronSchedule",
    "CronScheduleParam",
    "EmailNotifications",
    "EmailNotificationsParam",
    "Job",
    "JobCluster",
    "JobClusterParam",
    "JobEnvironment",
    "JobEnvironmentParam",
    "JobFunction",
    "JobNotificationSettings",
    "JobNotificationSettingsParam",
    "JobSyntaxError",
    "Library",
    "LibraryParam",
    "NotebookTask",
    "Permission",
    "PermissionLevel",
    "PermissionParam",
    "PipelineTask",
    "PythonWheelTask",
    "QueueSettings",
    "QueueSettingsParam",
    "ResourceMutator",
    "RunAs",
    "RunAsParam",
    "SparkJarTask",
    "SparkPythonTask",
    "SqlTask",
    "SqlTaskAlert",
    "SqlTaskDashboard",
    "SqlTaskFile",
    "SqlTaskQuery",
    "SqlTaskSubscription",
    "SqlTaskSubscriptionParam",
    "Task",
    "TaskEmailNotifications",
    "TaskEmailNotificationsParam",
    "TaskFunction",
    "TaskNotificationSettings",
    "TaskNotificationSettingsParam",
    "TaskWithOutput",
    "TriggerSettings",
    "TriggerSettingsParam",
    "WebhookNotifications",
    "WebhookNotificationsParam",
    "dbt_task",
    "jar_task",
    "job",
    "job_mutator",
    "notebook_task",
    "pipeline_task",
    "resource_generator",
    "sql_alert_task",
    "sql_dashboard_task",
    "sql_file_task",
    "sql_notebook_task",
    "sql_query_task",
    "task",
]

from databricks.bundles.compute.models.cluster_spec import ClusterSpec, ClusterSpecParam
from databricks.bundles.compute.models.library import (
    Library,
    LibraryParam,
    PythonPyPiLibrary,
)
from databricks.bundles.internal._transform import (
    _transform,
    _transform_optional,
    _transform_variable_or_dict,
    _transform_variable_or_list,
)
from databricks.bundles.jobs.functions._signature import Signature
from databricks.bundles.jobs.functions.compute import ComputeTask, ComputeTaskFunction
from databricks.bundles.jobs.functions.job import JobFunction
from databricks.bundles.jobs.functions.task import (
    TaskFunction,
    TaskWithOutput,
    _create_task_with_output,
    _transform_min_retry_interval_millis,
)
from databricks.bundles.jobs.internal.inspections import Inspections
from databricks.bundles.jobs.models.cron_schedule import CronSchedule, CronScheduleParam
from databricks.bundles.jobs.models.email_notifications import (
    EmailNotifications,
    EmailNotificationsParam,
    JobNotificationSettings,
    JobNotificationSettingsParam,
    TaskEmailNotifications,
    TaskEmailNotificationsParam,
    TaskNotificationSettings,
    TaskNotificationSettingsParam,
)
from databricks.bundles.jobs.models.job import Job
from databricks.bundles.jobs.models.job_cluster import JobCluster, JobClusterParam
from databricks.bundles.jobs.models.permission import (
    Permission,
    PermissionLevel,
    PermissionParam,
)
from databricks.bundles.jobs.models.queue_settings import (
    QueueSettings,
    QueueSettingsParam,
)
from databricks.bundles.jobs.models.run_as import RunAs, RunAsParam
from databricks.bundles.jobs.models.task import Task
from databricks.bundles.jobs.models.tasks.notebook_task import NotebookTask
from databricks.bundles.jobs.models.tasks.pipeline_task import PipelineTask
from databricks.bundles.jobs.models.tasks.python_wheel_task import PythonWheelTask
from databricks.bundles.jobs.models.tasks.sql_task import SqlTask
from databricks.bundles.jobs.models.tasks.sql_task_alert import SqlTaskAlert
from databricks.bundles.jobs.models.tasks.sql_task_dashboard import SqlTaskDashboard
from databricks.bundles.jobs.models.tasks.sql_task_query import SqlTaskQuery
from databricks.bundles.jobs.models.tasks.sql_task_subscription import (
    SqlTaskSubscription,
    SqlTaskSubscriptionParam,
)
from databricks.bundles.jobs.models.webhook_notifications import (
    WebhookNotifications,
    WebhookNotificationsParam,
)
from databricks.bundles.resource import ResourceMutator, resource_generator
from databricks.bundles.variables import (
    VariableOr,
    VariableOrDict,
    VariableOrList,
    VariableOrOptional,
    resolve_variable,
)

R = TypeVar("R")
P = ParamSpec("P")

TFunc = TypeVar("TFunc", bound=Callable[..., Any])


@overload
def job(
    *,
    name: VariableOrOptional[str] = None,
    description: VariableOrOptional[str] = None,
    resource_name: Optional[str] = None,
    default_job_cluster_spec: VariableOrOptional[ClusterSpecParam] = None,
    job_clusters: Optional[VariableOrList[JobClusterParam]] = None,
    max_concurrent_runs: VariableOrOptional[int] = None,
    tags: Optional[VariableOrDict[str]] = None,
    run_as: VariableOrOptional[RunAsParam] = None,
    environments: Optional[VariableOrList[JobEnvironmentParam]] = None,
    email_notifications: VariableOrOptional[EmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[JobNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
    schedule: VariableOrOptional[CronScheduleParam] = None,
    trigger: VariableOrOptional[TriggerSettingsParam] = None,
    permissions: Optional[VariableOrList[PermissionParam]] = None,
    queue: VariableOrOptional[QueueSettingsParam] = None,
    # deprecated parameters below
    # TODO mark as deprecated
    cron_schedule: Optional[CronScheduleParam] = None,
) -> Callable[[Callable[P, R]], JobFunction[P, R]]:
    ...


@overload
def job(function: Callable[P, R]) -> JobFunction[P, R]:
    ...


@overload
def task(
    *,
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
    libraries: Optional[VariableOrList[LibraryParam]] = None,
) -> Callable[[Callable[P, R]], ComputeTaskFunction[P, R]]:
    ...


@overload
def task(function: Callable[P, R]) -> ComputeTaskFunction[P, R]:
    ...


def job(*args: Any, **kwargs: Any) -> Any:
    # using `@job` is equivalent to `@job()`
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return job()(args[0])

    if len(args) != 0:
        raise ValueError("Only keyword args are supported")

    diagnostics = Diagnostics()

    if cron_schedule := kwargs.pop("cron_schedule", None):
        diagnostics = diagnostics.extend(
            Diagnostics.create_warning(
                "cron_schedule is deprecated, use schedule instead"
            )
        )

        kwargs["schedule"] = cron_schedule

    # FIXME needs to be in sync with overload
    def get_wrapper(
        name: VariableOrOptional[str] = None,
        description: VariableOrOptional[str] = None,
        resource_name: Optional[str] = None,
        default_job_cluster_spec: VariableOrOptional[ClusterSpecParam] = None,
        job_clusters: Optional[VariableOrList[JobClusterParam]] = None,
        max_concurrent_runs: VariableOrOptional[int] = None,
        tags: Optional[VariableOrDict[str]] = None,
        run_as: VariableOrOptional[RunAsParam] = None,
        email_notifications: VariableOrOptional[EmailNotificationsParam] = None,
        webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
        notification_settings: VariableOrOptional[JobNotificationSettingsParam] = None,
        timeout_seconds: VariableOrOptional[int] = None,
        schedule: VariableOrOptional[CronScheduleParam] = None,
        trigger: VariableOrOptional[TriggerSettingsParam] = None,
        environments: Optional[VariableOrList[JobEnvironmentParam]] = None,
        permissions: Optional[VariableOrList[PermissionParam]] = None,
        queue: VariableOrOptional[QueueSettingsParam] = None,
    ) -> Callable[[Callable[P, R]], JobFunction[P, R]]:
        if default_job_cluster_spec:
            default_job_cluster = JobCluster(
                job_cluster_key=JobCluster.DEFAULT_KEY,
                new_cluster=_transform(ClusterSpec, default_job_cluster_spec),
            )
            job_clusters = resolve_variable(job_clusters) or []
            job_clusters = [*job_clusters, default_job_cluster]

        def wrapper(function: Callable[P, R]) -> JobFunction[P, R]:
            obj = JobFunction.from_job_function(function)

            obj = replace(
                obj,
                _diagnostics=obj._diagnostics.extend(diagnostics),
                job_clusters=_transform_variable_or_list(
                    JobCluster, job_clusters or []
                ),
                max_concurrent_runs=max_concurrent_runs,
                schedule=_transform_optional(CronSchedule, schedule),
                trigger=_transform_optional(TriggerSettings, trigger),
                tags=_transform_variable_or_dict(str, tags or {}),
                run_as=_transform_optional(RunAs, run_as),
                environments=_transform_variable_or_list(
                    JobEnvironment, environments or []
                ),
                email_notifications=_transform_optional(
                    EmailNotifications, email_notifications
                ),
                webhook_notifications=_transform_optional(
                    WebhookNotifications, webhook_notifications
                ),
                notification_settings=_transform_optional(
                    JobNotificationSettings, notification_settings
                ),
                timeout_seconds=timeout_seconds,
                permissions=_transform_variable_or_list(Permission, permissions or []),
                queue=_transform_optional(QueueSettings, queue),
            )

            if name:
                obj = replace(obj, name=name)

            if description:
                obj = replace(obj, description=description)

            if resource_name:
                obj = replace(obj, resource_name=resource_name)

            return obj

        return wrapper

    return get_wrapper(**kwargs)


def task(*args: Any, **kwargs: Any) -> Any:
    # using `@task` is equivalent to `@task()`
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return task()(args[0])

    def get_wrapper(
        max_retries: VariableOrOptional[int] = None,
        min_retry_interval_millis: VariableOrOptional[timedelta] = None,
        retry_on_timeout: VariableOrOptional[bool] = None,
        email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
        webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
        notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
        timeout_seconds: VariableOrOptional[int] = None,
        libraries: Optional[VariableOrList[LibraryParam]] = None,
    ) -> Callable[[Callable[P, R]], ComputeTaskFunction[P, R]]:
        def wrapper(function: Callable[P, R]) -> ComputeTaskFunction[P, R]:
            task_func_name = Inspections.get_task_func_name(function)
            signature = Signature.from_function(function)

            base_task = _create_compute_task(
                max_retries=max_retries,
                min_retry_interval_millis=min_retry_interval_millis,
                retry_on_timeout=retry_on_timeout,
                email_notifications=email_notifications,
                webhook_notifications=webhook_notifications,
                notification_settings=notification_settings,
                timeout_seconds=timeout_seconds,
                return_type=signature.return_type,
                libraries=libraries,
            )

            from databricks.bundles import __version__

            updated_libraries = [
                *resolve_variable(base_task.libraries),
                Library.create(
                    pypi={
                        "package": "databricks-pydabs==" + __version__,
                        "repo": "https://databricks.github.io/workflows-authoring-toolkit",
                    },
                ),
                Library.create(whl="dist/*.whl"),
            ]

            base_task = replace(
                base_task,
                python_wheel_task=PythonWheelTask(
                    package_name="databricks-pydabs",
                    entry_point="entrypoint",
                    parameters=[f"--task_func={task_func_name}"],
                ),
                libraries=updated_libraries,
            )

            return ComputeTaskFunction(
                function=function,
                base_task=base_task,
            )

        return wrapper

    return get_wrapper(**kwargs)


def notebook_task(
    *,
    notebook_path: VariableOr[str],
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
    libraries: Optional[VariableOrList[LibraryParam]] = None,
) -> Callable[[Callable[P, None]], ComputeTaskFunction[P, None]]:
    def wrapper(function: Callable[P, None]) -> ComputeTaskFunction[P, None]:
        signature = Signature.from_function(function)

        base_task = _create_compute_task(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
            libraries=libraries,
        )

        base_task = replace(
            base_task,
            notebook_task=NotebookTask(
                notebook_path=notebook_path,
            ),
        )

        return ComputeTaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def sql_notebook_task(
    *,
    notebook_path: VariableOr[str],
    warehouse_id: VariableOr[str],
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
) -> Callable[[Callable[P, None]], TaskFunction[P, None]]:
    def wrapper(function: Callable[P, None]) -> TaskFunction[P, None]:
        signature = Signature.from_function(function)

        base_task = _create_task_with_output(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
        )

        base_task = replace(
            base_task,
            notebook_task=NotebookTask(
                notebook_path=notebook_path,
                warehouse_id=warehouse_id,
            ),
        )

        return TaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def jar_task(
    *,
    main_class_name: VariableOr[str],
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
    libraries: Optional[VariableOrList[LibraryParam]] = None,
) -> Callable[[Callable[P, None]], ComputeTaskFunction[P, None]]:
    def wrapper(function: Callable[P, None]) -> ComputeTaskFunction[P, None]:
        signature = Signature.from_function(function)

        base_task = _create_compute_task(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
            libraries=libraries,
        )

        base_task = replace(
            base_task,
            spark_jar_task=SparkJarTask(
                main_class_name=main_class_name,
            ),
        )

        return ComputeTaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def pipeline_task(
    *,
    pipeline_id: VariableOr[str],
    full_refresh: VariableOrOptional[bool] = None,
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
) -> Callable[[Callable[[], None]], TaskFunction[[], None]]:
    def wrapper(function: Callable[P, None]) -> TaskFunction[[], None]:
        signature = Signature.from_function(function)

        if signature.parameters:
            raise ValueError("Parameters are not supported for pipeline task")

        base_task = _create_task_with_output(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
        )

        base_task = replace(
            base_task,
            pipeline_task=PipelineTask(
                pipeline_id=pipeline_id,
                full_refresh=full_refresh,
            ),
        )

        return TaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def dbt_task(
    *,
    commands: VariableOrList[str],
    project_directory: VariableOr[str],
    schema: VariableOrOptional[str] = None,
    warehouse_id: VariableOrOptional[str] = None,
    profiles_directory: VariableOrOptional[str] = None,
    catalog: VariableOrOptional[str] = None,
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
    libraries: Optional[VariableOrList[LibraryParam]] = None,
) -> Callable[[Callable[[], None]], ComputeTaskFunction[[], None]]:
    if libraries is None:
        libraries = [
            Library(pypi=PythonPyPiLibrary(package="dbt-databricks>=1.0.0,<2.0.0"))
        ]

    def wrapper(function: Callable[P, None]) -> ComputeTaskFunction[P, None]:
        signature = Signature.from_function(function)

        if signature.parameters:
            raise ValueError("Parameters are not supported for dbt task")

        base_task = _create_compute_task(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
            libraries=libraries,
        )

        base_task = replace(
            base_task,
            dbt_task=DbtTask(
                commands=_transform_variable_or_list(str, commands),
                project_directory=project_directory,
                schema=schema,
                warehouse_id=warehouse_id,
                profiles_directory=profiles_directory,
                catalog=catalog,
            ),
        )

        return ComputeTaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def sql_dashboard_task(
    *,
    warehouse_id: VariableOr[str],
    dashboard_id: VariableOr[str],
    subscriptions: Optional[VariableOrList[SqlTaskSubscriptionParam]] = None,
    pause_subscriptions: VariableOrOptional[bool] = None,
    custom_subject: VariableOrOptional[str] = None,
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
) -> Callable[[Callable[P, None]], TaskFunction[P, None]]:
    def wrapper(function: Callable[P, None]) -> TaskFunction[P, None]:
        signature = Signature.from_function(function)

        base_task = _create_task_with_output(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
        )

        base_task = replace(
            base_task,
            sql_task=SqlTask(
                warehouse_id=warehouse_id,
                dashboard=SqlTaskDashboard(
                    dashboard_id=dashboard_id,
                    subscriptions=_transform_variable_or_list(
                        SqlTaskSubscription, subscriptions or []
                    ),
                    custom_subject=custom_subject,
                    pause_subscriptions=pause_subscriptions,
                ),
            ),
        )

        return TaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def sql_query_task(
    *,
    warehouse_id: VariableOr[str],
    query_id: VariableOr[str],
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
) -> Callable[[Callable[P, None]], TaskFunction[P, None]]:
    def wrapper(function: Callable[P, None]) -> TaskFunction[P, None]:
        signature = Signature.from_function(function)

        base_task = _create_task_with_output(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
        )

        base_task = replace(
            base_task,
            sql_task=SqlTask(
                warehouse_id=warehouse_id,
                query=SqlTaskQuery(
                    query_id=query_id,
                ),
            ),
        )

        return TaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def sql_alert_task(
    *,
    warehouse_id: VariableOr[str],
    alert_id: VariableOr[str],
    subscriptions: VariableOrList[SqlTaskSubscriptionParam],
    pause_subscriptions: VariableOrOptional[bool] = None,
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
) -> Callable[[Callable[[], None]], TaskFunction[[], None]]:
    def wrapper(function: Callable[P, None]) -> TaskFunction[[], None]:
        signature = Signature.from_function(function)

        if signature.parameters:
            raise ValueError("Parameters are not supported for SQL alert task")

        if not subscriptions:
            raise ValueError(
                "At least one subscription for SQL alert task must be specified"
            )

        base_task = _create_task_with_output(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
        )

        base_task = replace(
            base_task,
            sql_task=SqlTask(
                warehouse_id=warehouse_id,
                alert=SqlTaskAlert(
                    alert_id=alert_id,
                    subscriptions=_transform_variable_or_list(
                        SqlTaskSubscription, subscriptions
                    ),
                    pause_subscriptions=pause_subscriptions,
                ),
            ),
        )

        return TaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


def sql_file_task(
    *,
    warehouse_id: VariableOr[str],
    path: VariableOr[str],
    max_retries: VariableOrOptional[int] = None,
    min_retry_interval_millis: VariableOrOptional[timedelta] = None,
    retry_on_timeout: VariableOrOptional[bool] = None,
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam] = None,
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam] = None,
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam] = None,
    timeout_seconds: VariableOrOptional[int] = None,
) -> Callable[[Callable[P, None]], TaskFunction[P, None]]:
    def wrapper(function: Callable[P, None]) -> TaskFunction[P, None]:
        signature = Signature.from_function(function)

        base_task = _create_task_with_output(
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            retry_on_timeout=retry_on_timeout,
            email_notifications=email_notifications,
            webhook_notifications=webhook_notifications,
            notification_settings=notification_settings,
            timeout_seconds=timeout_seconds,
            return_type=signature.return_type,
        )

        base_task = replace(
            base_task,
            sql_task=SqlTask(
                warehouse_id=warehouse_id,
                file=SqlTaskFile(
                    path=path,
                ),
            ),
        )

        return TaskFunction(
            function=function,
            base_task=base_task,
        )

    return wrapper


class JobSyntaxError(SyntaxError):
    pass


def _create_compute_task(
    max_retries: VariableOrOptional[int],
    min_retry_interval_millis: VariableOrOptional[timedelta],
    retry_on_timeout: VariableOrOptional[bool],
    email_notifications: VariableOrOptional[TaskEmailNotificationsParam],
    webhook_notifications: VariableOrOptional[WebhookNotificationsParam],
    notification_settings: VariableOrOptional[TaskNotificationSettingsParam],
    timeout_seconds: VariableOrOptional[int],
    return_type: dict[str, type],
    libraries: Optional[VariableOrList[LibraryParam]],
) -> ComputeTask:
    return ComputeTask(
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
        libraries=_transform_variable_or_list(Library, libraries or []),
    )


def job_mutator(function: Callable[[Job], Job]) -> ResourceMutator[Job]:
    """
    Mutators defined within a single Python module are applied in the order they are defined.
    The relative order of mutators defined in different modules is not guaranteed.
    """

    return ResourceMutator(resource_type=Job, function=function)


def resolve_recursive_imports():
    import typing

    from databricks.bundles.jobs.models.tasks.for_each_task import ForEachTask

    ForEachTask.__annotations__ = typing.get_type_hints(
        ForEachTask,
        globalns={"Task": Task, "VariableOr": VariableOr},
    )


resolve_recursive_imports()
