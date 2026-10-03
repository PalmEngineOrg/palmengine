"""System supervisor — continuous system services for one SystemInstance.

Planes carry reactive traffic. The supervisor owns **lifecycle** for long-running
loops and worker sets (work drain, outbox poll, inbound workers, …).

Install law lives on continuous **definitions**; the supervisor walks them.
"""

from __future__ import annotations

from palm.system.subsystems.supervisor.definition import (
    DEFAULT_CONTINUOUS_DEFINITIONS,
    ContinuousServiceDefinition,
    ContinuousWireContext,
)
from palm.system.subsystems.supervisor.outbox_loop import OutboxLoopService
from palm.system.subsystems.supervisor.service import (
    CallableSystemService,
    ServiceStartContext,
    SystemService,
)
from palm.system.subsystems.supervisor.supervisor import SystemSupervisor

__all__ = [
    "CallableSystemService",
    "ContinuousServiceDefinition",
    "ContinuousWireContext",
    "DEFAULT_CONTINUOUS_DEFINITIONS",
    "OutboxLoopService",
    "ServiceStartContext",
    "SystemService",
    "SystemSupervisor",
]
