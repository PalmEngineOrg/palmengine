from __future__ import annotations

from pathlib import Path

from palm.common.transforms._apps import INSTALLED_TRANSFORMS
from palm.common.transforms.catalog import TRANSFORM_CATALOG

ROOT = Path(__file__).resolve().parents[2]
L0 = ROOT / "src/palm/runtimes/mcp/assist/tools.py"


def test_honest_transform_count_is_24() -> None:
    assert len(INSTALLED_TRANSFORMS) == 24
    assert set(TRANSFORM_CATALOG) == set(INSTALLED_TRANSFORMS)
    assert "parquet_load" not in INSTALLED_TRANSFORMS
    assert "parquet_load" not in TRANSFORM_CATALOG


def test_l0_continue_uses_instance_id_not_session() -> None:
    text = L0.read_text(encoding="utf-8")
    assert "{instance_id, flow_id, value}" in text
    assert '"instance_id": "inst-1"' in text
    assert "{session_id, flow_id, value}" not in text
    assert '"session_id": "inst-1"' not in text
