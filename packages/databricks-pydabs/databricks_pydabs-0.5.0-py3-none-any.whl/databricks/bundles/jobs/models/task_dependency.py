from dataclasses import dataclass, field
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr, VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["TaskDependency", "TaskDependencyParam"]


@dataclass
class TaskDependency:
    """"""

    """
    The name of the task this task depends on.
    """
    task_key: VariableOr[str]

    """
    Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run.
    """
    outcome: VariableOrOptional[str] = field(default=None, kw_only=True)

    @classmethod
    def create(
        cls,
        /,
        *,
        task_key: VariableOr[str],
        outcome: VariableOrOptional[str] = None,
    ) -> "Self":
        return _transform(cls, locals())


class TaskDependencyDict(TypedDict, total=False):
    """"""

    """
    The name of the task this task depends on.
    """
    task_key: VariableOr[str]

    """
    Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run.
    """
    outcome: VariableOrOptional[str]


TaskDependencyParam = TaskDependencyDict | TaskDependency
