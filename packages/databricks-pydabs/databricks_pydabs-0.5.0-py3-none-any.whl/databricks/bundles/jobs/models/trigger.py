from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING, Literal, Optional, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.jobs.models.pause_status import PauseStatus, PauseStatusParam
from databricks.bundles.variables import VariableOr, VariableOrList, VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = [
    "Condition",
    "ConditionParam",
    "FileArrivalTriggerConfiguration",
    "FileArrivalTriggerConfigurationParam",
    "TableUpdateTriggerConfiguration",
    "TableUpdateTriggerConfigurationParam",
    "TriggerSettings",
    "TriggerSettingsParam",
]


class Condition(Enum):
    ANY_UPDATED = "ANY_UPDATED"
    ALL_UPDATED = "ALL_UPDATED"


ConditionParam = Literal["ANY_UPDATED", "ALL_UPDATED"] | Condition


@dataclass(kw_only=True)
class FileArrivalTriggerConfiguration:
    """"""

    """
    URL to be monitored for file arrivals. The path must point to the root or a subpath of the external location.
    """
    url: VariableOr[str]

    """
    If set, the trigger starts a run only after the specified amount of time passed since
    the last time the trigger fired. The minimum allowed value is 60 seconds
    """
    min_time_between_triggers_seconds: VariableOrOptional[int] = None

    """
    If set, the trigger starts a run only after no file activity has occurred for the specified amount of time.
    This makes it possible to wait for a batch of incoming files to arrive before triggering a run. The
    minimum allowed value is 60 seconds.
    """
    wait_after_last_change_seconds: VariableOrOptional[int] = None

    @classmethod
    def create(
        cls,
        /,
        *,
        url: VariableOr[str],
        min_time_between_triggers_seconds: VariableOrOptional[int] = None,
        wait_after_last_change_seconds: VariableOrOptional[int] = None,
    ) -> "Self":
        return _transform(cls, locals())


class FileArrivalTriggerConfigurationDict(TypedDict, total=False):
    """"""

    """
    URL to be monitored for file arrivals. The path must point to the root or a subpath of the external location.
    """
    url: VariableOr[str]

    """
    If set, the trigger starts a run only after the specified amount of time passed since
    the last time the trigger fired. The minimum allowed value is 60 seconds
    """
    min_time_between_triggers_seconds: VariableOrOptional[int]

    """
    If set, the trigger starts a run only after no file activity has occurred for the specified amount of time.
    This makes it possible to wait for a batch of incoming files to arrive before triggering a run. The
    minimum allowed value is 60 seconds.
    """
    wait_after_last_change_seconds: VariableOrOptional[int]


FileArrivalTriggerConfigurationParam = (
    FileArrivalTriggerConfigurationDict | FileArrivalTriggerConfiguration
)


@dataclass(kw_only=True)
class TableUpdateTriggerConfiguration:
    """"""

    """
    A list of Delta tables to monitor for changes. The table name must be in the format `catalog_name.schema_name.table_name`.
    """
    table_names: VariableOrList[str] = field(default_factory=list)

    """
    If set, the trigger starts a run only after the specified amount of time has passed since
    the last time the trigger fired. The minimum allowed value is 60 seconds.
    """
    min_time_between_triggers_seconds: VariableOrOptional[int] = None

    """
    If set, the trigger starts a run only after no table updates have occurred for the specified time
    and can be used to wait for a series of table updates before triggering a run. The
    minimum allowed value is 60 seconds.
    """
    wait_after_last_change_seconds: VariableOrOptional[int] = None

    """
    The table(s) condition based on which to trigger a job run.
    """
    condition: VariableOrOptional[Condition] = None

    @classmethod
    def create(
        cls,
        /,
        *,
        table_names: Optional[VariableOrList[str]] = None,
        min_time_between_triggers_seconds: VariableOrOptional[int] = None,
        wait_after_last_change_seconds: VariableOrOptional[int] = None,
        condition: VariableOrOptional[ConditionParam] = None,
    ) -> "Self":
        return _transform(cls, locals())


class TableUpdateTriggerConfigurationDict(TypedDict, total=False):
    """"""

    """
    A list of Delta tables to monitor for changes. The table name must be in the format `catalog_name.schema_name.table_name`.
    """
    table_names: VariableOrList[str]

    """
    If set, the trigger starts a run only after the specified amount of time has passed since
    the last time the trigger fired. The minimum allowed value is 60 seconds.
    """
    min_time_between_triggers_seconds: VariableOrOptional[int]

    """
    If set, the trigger starts a run only after no table updates have occurred for the specified time
    and can be used to wait for a series of table updates before triggering a run. The
    minimum allowed value is 60 seconds.
    """
    wait_after_last_change_seconds: VariableOrOptional[int]

    """
    The table(s) condition based on which to trigger a job run.
    """
    condition: VariableOrOptional[ConditionParam]


TableUpdateTriggerConfigurationParam = (
    TableUpdateTriggerConfigurationDict | TableUpdateTriggerConfiguration
)


@dataclass(kw_only=True)
class TriggerSettings:
    """"""

    """
    Whether this trigger is paused or not.
    """
    pause_status: VariableOrOptional[PauseStatus] = None

    """
    File arrival trigger settings.
    """
    file_arrival: VariableOrOptional[FileArrivalTriggerConfiguration] = None

    table_update: VariableOrOptional[TableUpdateTriggerConfiguration] = None

    def __post_init__(self):
        union_fields = [
            self.file_arrival,
            self.table_update,
        ]

        if sum(f is not None for f in union_fields) != 1:
            raise ValueError(
                "TriggerSettings must specify exactly one of 'file_arrival', 'table_update'"
            )

    @classmethod
    def create(
        cls,
        /,
        *,
        pause_status: VariableOrOptional[PauseStatusParam] = None,
        file_arrival: VariableOrOptional[FileArrivalTriggerConfigurationParam] = None,
        table_update: VariableOrOptional[TableUpdateTriggerConfigurationParam] = None,
    ) -> "Self":
        return _transform(cls, locals())


class TriggerSettingsDict(TypedDict, total=False):
    """"""

    """
    Whether this trigger is paused or not.
    """
    pause_status: VariableOrOptional[PauseStatusParam]

    """
    File arrival trigger settings.
    """
    file_arrival: VariableOrOptional[FileArrivalTriggerConfigurationParam]

    table_update: VariableOrOptional[TableUpdateTriggerConfigurationParam]


TriggerSettingsParam = TriggerSettingsDict | TriggerSettings
