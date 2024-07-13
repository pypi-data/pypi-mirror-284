import dataclasses
from dataclasses import dataclass
from typing import Any, ParamSpec, TypeVar

from databricks.bundles.jobs.functions.task import TaskFunction, TaskWithOutput

__all__ = [
    "ComputeTask",
    "ComputeTaskFunction",
]

R = TypeVar("R")
P = ParamSpec("P")


@dataclass(kw_only=True)
class ComputeTask(TaskWithOutput[R]):
    class TaskValues:
        def __getattribute__(self, item) -> Any:
            pass

    def with_existing_cluster_id(self, value: str):
        return dataclasses.replace(self, existing_cluster_id=value)

    def with_job_cluster_key(self, value: str):
        return dataclasses.replace(self, job_cluster_key=value)

    def with_environment_key(self, value: str):
        return dataclasses.replace(self, environment_key=value)

    @property
    def values(self) -> TaskValues:
        raise Exception(
            "Accessing task values outside of @job decorator isn't supported"
        )


@dataclass(kw_only=True)
class ComputeTaskFunction(TaskFunction[P, R]):
    base_task: ComputeTask[R]

    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> ComputeTask[R]:
        return super().__call__(*args, **kwargs)  # type:ignore
