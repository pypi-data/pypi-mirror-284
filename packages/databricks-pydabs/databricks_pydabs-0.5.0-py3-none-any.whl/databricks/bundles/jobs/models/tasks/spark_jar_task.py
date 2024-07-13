from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.variables import VariableOr, VariableOrList, VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["SparkJarTask", "SparkJarTaskParam"]


@dataclass(kw_only=True)
class SparkJarTask:
    """"""

    """
    The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library.
    
    The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail.
    """
    main_class_name: VariableOr[str]

    """
    Deprecated since 04/2016. Provide a `jar` through the `libraries` field instead. For an example, see :method:jobs/create.
    """
    jar_uri: VariableOrOptional[str] = None

    """
    Parameters passed to the main method.
    
    Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.
    """
    parameters: VariableOrList[str] = field(default_factory=list)

    @classmethod
    def create(
        cls,
        /,
        *,
        main_class_name: VariableOr[str],
        jar_uri: VariableOrOptional[str] = None,
        parameters: Optional[VariableOrList[str]] = None,
    ) -> "Self":
        return _transform(cls, locals())


class SparkJarTaskDict(TypedDict, total=False):
    """"""

    """
    The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library.
    
    The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail.
    """
    main_class_name: VariableOr[str]

    """
    Deprecated since 04/2016. Provide a `jar` through the `libraries` field instead. For an example, see :method:jobs/create.
    """
    jar_uri: VariableOrOptional[str]

    """
    Parameters passed to the main method.
    
    Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.
    """
    parameters: VariableOrList[str]


SparkJarTaskParam = SparkJarTaskDict | SparkJarTask
