from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr, VariableOrDict

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["RunJobTask", "RunJobTaskParam"]


@dataclass(kw_only=True)
class RunJobTask:
    """"""

    """
    ID of the job to trigger.
    """
    job_id: VariableOr[int]

    """
    Job-level parameters used to trigger the job.
    """
    job_parameters: VariableOrDict[str] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        /,
        *,
        job_id: VariableOr[int],
        job_parameters: Optional[VariableOrDict[str]] = None,
    ) -> "Self":
        return _transform(cls, locals())


class RunJobTaskDict(TypedDict, total=False):
    """"""

    """
    ID of the job to trigger.
    """
    job_id: VariableOr[int]

    """
    Job-level parameters used to trigger the job.
    """
    job_parameters: VariableOrDict[str]


RunJobTaskParam = RunJobTaskDict | RunJobTask
