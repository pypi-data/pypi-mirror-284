from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr, VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

    from databricks.bundles.jobs.models.task import Task, TaskParam

__all__ = ["ForEachTask", "ForEachTaskParam"]


@dataclass(kw_only=True)
class ForEachTask:
    """"""

    """
    Array for task to iterate on. This can be a JSON string or a reference to
    an array parameter.
    """
    inputs: VariableOr[str]

    """
    Configuration for the task that will be run for each element in the array
    """
    task: "VariableOr[Task]"

    """
    Controls the number of active iterations task runs. Default is 20,
    maximum allowed is 100.
    """
    concurrency: VariableOrOptional[int] = None

    @classmethod
    def create(
        cls,
        /,
        *,
        inputs: VariableOr[str],
        task: "VariableOr[TaskParam]",
        concurrency: VariableOrOptional[int] = None,
    ) -> "Self":
        return _transform(cls, locals())


class ForEachTaskDict(TypedDict, total=False):
    """"""

    """
    Array for task to iterate on. This can be a JSON string or a reference to
    an array parameter.
    """
    inputs: VariableOr[str]

    """
    Configuration for the task that will be run for each element in the array
    """
    task: "VariableOr[TaskParam]"

    """
    Controls the number of active iterations task runs. Default is 20,
    maximum allowed is 100.
    """
    concurrency: VariableOrOptional[int]


ForEachTaskParam = ForEachTaskDict | ForEachTask
