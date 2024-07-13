from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, TypedDict

from databricks.bundles.internal._transform import _transform
from databricks.bundles.jobs.models.tasks.sql_task_subscription import (
    SqlTaskSubscription,
    SqlTaskSubscriptionParam,
)
from databricks.bundles.variables import VariableOr, VariableOrList, VariableOrOptional

if TYPE_CHECKING:
    from typing_extensions import Self

__all__ = ["SqlTaskDashboard", "SqlTaskDashboardParam"]


@dataclass(kw_only=True)
class SqlTaskDashboard:
    """"""

    """
    The canonical identifier of the SQL dashboard.
    """
    dashboard_id: VariableOr[str]

    """
    If specified, dashboard snapshots are sent to subscriptions.
    """
    subscriptions: VariableOrList[SqlTaskSubscription] = field(default_factory=list)

    """
    Subject of the email sent to subscribers of this task.
    """
    custom_subject: VariableOrOptional[str] = None

    """
    If true, the dashboard snapshot is not taken, and emails are not sent to subscribers.
    """
    pause_subscriptions: VariableOrOptional[bool] = None

    @classmethod
    def create(
        cls,
        /,
        *,
        dashboard_id: VariableOr[str],
        subscriptions: Optional[VariableOrList[SqlTaskSubscriptionParam]] = None,
        custom_subject: VariableOrOptional[str] = None,
        pause_subscriptions: VariableOrOptional[bool] = None,
    ) -> "Self":
        return _transform(cls, locals())


class SqlTaskDashboardDict(TypedDict, total=False):
    """"""

    """
    The canonical identifier of the SQL dashboard.
    """
    dashboard_id: VariableOr[str]

    """
    If specified, dashboard snapshots are sent to subscriptions.
    """
    subscriptions: VariableOrList[SqlTaskSubscriptionParam]

    """
    Subject of the email sent to subscribers of this task.
    """
    custom_subject: VariableOrOptional[str]

    """
    If true, the dashboard snapshot is not taken, and emails are not sent to subscribers.
    """
    pause_subscriptions: VariableOrOptional[bool]


SqlTaskDashboardParam = SqlTaskDashboardDict | SqlTaskDashboard
