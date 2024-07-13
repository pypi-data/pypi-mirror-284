from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["SqlTaskQuery", "SqlTaskQueryParam"]


@dataclass(kw_only=True)
class SqlTaskQuery:
    """"""

    """
    The canonical identifier of the SQL query.
    """
    query_id: VariableOr[str]

    @classmethod
    def create(
        cls,
        /,
        *,
        query_id: VariableOr[str],
    ) -> "Self":
        return _transform(cls, locals())


class SqlTaskQueryDict(TypedDict, total=False):
    """"""

    """
    The canonical identifier of the SQL query.
    """
    query_id: VariableOr[str]


SqlTaskQueryParam = SqlTaskQueryDict | SqlTaskQuery
