#!/usr/bin/env python3
"""Assembly coherence guard — run the fail-closed / single-truth suite."""

from __future__ import annotations

import subprocess
import sys


def main() -> int:
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "tests/assembly/",
        "tests/core/test_assembly_engine.py",
        "tests/test_assembly_system_0_63_2.py",
        "tests/test_assembly_gate_0_63_3.py",
        "--tb=short",
    ]
    # tests/assembly includes seed map and coherence gate
    print("🔒 Assembly coherence suite (fail-closed / single readiness)...")
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
