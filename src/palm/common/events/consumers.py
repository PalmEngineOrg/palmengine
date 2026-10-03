"""
Named journal consumers.

Doctor / control-plane lag snapshot over :meth:`EventJournal.status`.
No default consumer names remain. Work drain is the WorkIntent organ.
"""

from __future__ import annotations

from typing import Any

from palm.common.events.journal import EventJournal

DEFAULT_JOURNAL_CONSUMERS: tuple[str, ...] = ()


def journal_consumer_status(
    journal: EventJournal,
    *,
    consumers: list[str] | tuple[str, ...] | None = None,
) -> dict[str, Any]:
    """Lag snapshot for doctor / control_plane."""
    names = list(consumers) if consumers is not None else list(DEFAULT_JOURNAL_CONSUMERS)
    return journal.status(consumers=names)


__all__ = [
    "DEFAULT_JOURNAL_CONSUMERS",
    "journal_consumer_status",
]
