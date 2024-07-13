from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["WorkspaceStorageInfo", "WorkspaceStorageInfoParam"]


@dataclass(kw_only=True)
class WorkspaceStorageInfo:
    """"""

    """
    workspace files destination, e.g. `/Users/user1@databricks.com/my-init.sh`
    """
    destination: VariableOr[str]

    @classmethod
    def create(
        cls,
        /,
        *,
        destination: VariableOr[str],
    ) -> "Self":
        return _transform(cls, locals())


class WorkspaceStorageInfoDict(TypedDict, total=False):
    """"""

    """
    workspace files destination, e.g. `/Users/user1@databricks.com/my-init.sh`
    """
    destination: VariableOr[str]


WorkspaceStorageInfoParam = WorkspaceStorageInfoDict | WorkspaceStorageInfo
