"""Shared, transport-agnostic surface helpers.

Cross-surface presentation primitives (pagination envelopes, serializers) live here so that every
runtime surface — REST, MCP, SSR, WebSocket — depends *down* on `common` rather than sideways on
another surface.

Add new cross-surface helpers here, not under a single surface.
"""
