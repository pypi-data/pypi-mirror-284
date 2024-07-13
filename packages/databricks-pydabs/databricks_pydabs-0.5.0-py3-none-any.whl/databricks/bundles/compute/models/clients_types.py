from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["ClientsTypes", "ClientsTypesParam"]


@dataclass(kw_only=True)
class ClientsTypes:
    """"""

    """
    With notebooks set, this cluster can be used for notebooks
    """
    notebooks: VariableOrOptional[bool] = None

    """
    With jobs set, the cluster can be used for jobs
    """
    jobs: VariableOrOptional[bool] = None

    @classmethod
    def create(
        cls,
        /,
        *,
        notebooks: VariableOrOptional[bool] = None,
        jobs: VariableOrOptional[bool] = None,
    ) -> "Self":
        return _transform(cls, locals())


class ClientsTypesDict(TypedDict, total=False):
    """"""

    """
    With notebooks set, this cluster can be used for notebooks
    """
    notebooks: VariableOrOptional[bool]

    """
    With jobs set, the cluster can be used for jobs
    """
    jobs: VariableOrOptional[bool]


ClientsTypesParam = ClientsTypesDict | ClientsTypes
