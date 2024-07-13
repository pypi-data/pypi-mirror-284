from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr, VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["PipelineTask", "PipelineTaskParam"]


@dataclass(kw_only=True)
class PipelineTask:
    """"""

    """
    The full name of the pipeline task to execute.
    """
    pipeline_id: VariableOr[str]

    """
    If true, triggers a full refresh on the delta live table.
    """
    full_refresh: VariableOrOptional[bool] = None

    @classmethod
    def create(
        cls,
        /,
        *,
        pipeline_id: VariableOr[str],
        full_refresh: VariableOrOptional[bool] = None,
    ) -> "Self":
        return _transform(cls, locals())


class PipelineTaskDict(TypedDict, total=False):
    """"""

    """
    The full name of the pipeline task to execute.
    """
    pipeline_id: VariableOr[str]

    """
    If true, triggers a full refresh on the delta live table.
    """
    full_refresh: VariableOrOptional[bool]


PipelineTaskParam = PipelineTaskDict | PipelineTask
