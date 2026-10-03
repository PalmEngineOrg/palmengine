"""Runner ready() doctor register composted."""

from __future__ import annotations

import importlib.util

from plugins.kits.server.diagnostics import build_doctor_report


def test_doctor_contributor_registry_is_gone() -> None:
    # Dropped the doctor registry.
    assert importlib.util.find_spec("palm.common.runtimes") is None
    assert importlib.util.find_spec("drivers.runners.host.doctor") is None
    assert importlib.util.find_spec("drivers.runners.neonroot.doctor") is None


def test_host_and_neonroot_ready_are_not_doctor_registers() -> None:
    # Dropped the doctor ready() hooks.
    assert importlib.util.find_spec("drivers.runners.host.app") is None
    assert importlib.util.find_spec("drivers.runners.neonroot.app") is None
    assert importlib.util.find_spec("drivers.runners.host.doctor") is None
    assert importlib.util.find_spec("drivers.runners.neonroot.doctor") is None


def test_anatomy_doctor_has_no_contributor_bags() -> None:
    import drivers.runners  # noqa: F401

    class _RT:
        runtime_name = "test"
        storage = None
        orchestration = None
        repository = None
        auth_enforce = False

    report = build_doctor_report(_RT())
    assert "neonroot" not in report
    assert "workload_host" not in report
    assert "neonroot" in report["workloads"]["registered_runtimes"]
    assert "host" in report["workloads"]["registered_runtimes"]
