from dataclasses import dataclass
from typing import Any, Callable, Generic, Iterator, Optional, Type, TypeVar, overload

from databricks.bundles.internal._transform import _transient_field

T = TypeVar("T")

__all__ = [
    "Resource",
    "ResourceGenerator",
    "ResourceMutator",
    "resource_generator",
]


@dataclass
class Resource:
    resource_name: Optional[str] = _transient_field()  # type:ignore


class ResourceGenerator:
    def __init__(self, function: Callable[[], Iterator[Resource]]):
        self.function = function


@dataclass
class ResourceMutator(Generic[T]):
    """
    Mutators defined within a single Python module are applied in the order they are defined.
    The relative order of mutators defined in different modules is not guaranteed.
    """

    resource_type: Type[T]
    function: Callable[[T], T]


@overload
def resource_generator() -> (
    Callable[[Callable[[], Iterator[Resource]]], ResourceGenerator]
):
    ...


@overload
def resource_generator(function: Callable[[], Iterator[Resource]]) -> ResourceGenerator:
    ...


def resource_generator(*args: Any, **kwargs: Any) -> Any:
    # using `@resource_generator` is equivalent to `@resource_generator()`
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return resource_generator()(args[0])

    if len(args) != 0:
        raise ValueError("Only keyword args are supported")

    def wrapper(function: Callable[[], Iterator[Resource]]) -> ResourceGenerator:
        return ResourceGenerator(function)

    return wrapper
