"""
Host wiring — projections + command/query bus handlers.

Parameter-based (root-agnostic) so the second composition root (``ServerContext``) can share it.
"""

from __future__ import annotations

from bundles.standard.app.host.wiring.cqrs import (
    collect_cqrs_command_types,
    collect_cqrs_query_types,
    wire_command_bus,
    wire_query_bus,
)
from bundles.standard.app.host.wiring.projections import (
    build_pattern_projections,
)

__all__ = [
    "build_pattern_projections",
    "collect_cqrs_command_types",
    "collect_cqrs_query_types",
    "wire_command_bus",
    "wire_query_bus",
]
