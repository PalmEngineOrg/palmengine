"""Product inspect door — present operator views over system facts.

Home for :class:`InspectService`. Formerly
``services.system`` / ``SystemService`` — that package remains a thin
import shim.

:meth:`InspectService.top` / :meth:`InspectService.vitality` present
system vitality projection only.

:meth:`InspectService.doctor` is demoted anatomy packaging.

:meth:`InspectService.benchmark` presents vitality tool (opt-in).
"""

from services.inspect.present import (
    present_benchmark,
    present_doctor,
    present_top,
    present_vitality,
)
from services.inspect.service import InspectService

__all__ = [
    "InspectService",
    "present_benchmark",
    "present_doctor",
    "present_top",
    "present_vitality",
]
