"""
Palm kits — shared surface infrastructure, exposed by name.

Kits are **not** the system layer and **not** product services.
They hold reusable transport and presentation glue (HTTP protocol, routes,
SSR helpers, …) so runtimes stay thin adapters.

Law:

- One implementation per kit (no dual trees).
- Named home: ``palm.kits.<name>`` — not anonymous bulk under ``common``.
- Install list is truth: :data:`INSTALLED_KITS`.
- Surfaces import kits; they do not invent private protocol copies.

Import the server kit as :mod:`palm.kits.server`.
Import the present kit as :mod:`palm.kits.present`.
Import the authoring kit as :mod:`palm.kits.authoring`.

``autoload`` does not import a kit. Import the kit module to register it.
"""

from __future__ import annotations

from plugins.kits._apps import INSTALLED_KITS, INTENTION_KITS, autoload
from plugins.kits.registry import (
    KitInfo,
    clear_kits,
    get_kit,
    installed_kit_names,
    list_kits,
    register_kit,
)

__all__ = [
    "INSTALLED_KITS",
    "INTENTION_KITS",
    "KitInfo",
    "autoload",
    "clear_kits",
    "get_kit",
    "installed_kit_names",
    "list_kits",
    "register_kit",
]
