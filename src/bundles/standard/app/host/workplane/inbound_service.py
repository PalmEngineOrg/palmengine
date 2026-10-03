"""Compatibility re-export — inbound lives on the system work plane."""

from __future__ import annotations

from palm.system.subsystems.planes.work.inbound import InboundBinding, InboundBindingService

__all__ = ["InboundBinding", "InboundBindingService"]
