from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.compute.models.clients_types import (
    ClientsTypes,
    ClientsTypesParam,
)
from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["WorkloadType", "WorkloadTypeParam"]


@dataclass(kw_only=True)
class WorkloadType:
    """"""

    """
     defined what type of clients can use the cluster. E.g. Notebooks, Jobs
    """
    clients: VariableOr[ClientsTypes]

    @classmethod
    def create(
        cls,
        /,
        *,
        clients: VariableOr[ClientsTypesParam],
    ) -> "Self":
        return _transform(cls, locals())


class WorkloadTypeDict(TypedDict, total=False):
    """"""

    """
     defined what type of clients can use the cluster. E.g. Notebooks, Jobs
    """
    clients: VariableOr[ClientsTypesParam]


WorkloadTypeParam = WorkloadTypeDict | WorkloadType
