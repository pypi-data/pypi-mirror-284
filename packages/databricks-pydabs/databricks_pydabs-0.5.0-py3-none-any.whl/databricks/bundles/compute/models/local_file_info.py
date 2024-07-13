from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["LocalFileInfo", "LocalFileInfoParam"]


@dataclass(kw_only=True)
class LocalFileInfo:
    """"""

    """
    local file destination, e.g. `file:/my/local/file.sh`
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


class LocalFileInfoDict(TypedDict, total=False):
    """"""

    """
    local file destination, e.g. `file:/my/local/file.sh`
    """
    destination: VariableOr[str]


LocalFileInfoParam = LocalFileInfoDict | LocalFileInfo
