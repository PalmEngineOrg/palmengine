"""Authoring resource provider package.

Working name ``authoring``. Duals the kit package. José may rename. Walks
``palm.kits.authoring.bound().commit``.
"""

from plugins.providers.authoring import registry as registry
from plugins.providers.authoring.provider import AuthoringProvider

__all__ = ["AuthoringProvider", "registry"]
