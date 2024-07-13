from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["Adlsgen2Info", "Adlsgen2InfoParam"]


@dataclass(kw_only=True)
class Adlsgen2Info:
    """"""

    """
    abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`.
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


class Adlsgen2InfoDict(TypedDict, total=False):
    """"""

    """
    abfss destination, e.g. `abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<directory-name>`.
    """
    destination: VariableOr[str]


Adlsgen2InfoParam = Adlsgen2InfoDict | Adlsgen2Info
