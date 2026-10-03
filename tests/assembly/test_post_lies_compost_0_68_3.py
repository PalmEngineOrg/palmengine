"""0.68.3 — living POST lies composted."""

from __future__ import annotations

from palm.system.runtime.job_hooks.outbox_drain import OutboxDrainHook
from palm.system.subsystems.supervisor.outbox_loop import OutboxLoopService


def test_production_drain_does_not_pass_on_before_publish() -> None:
    import inspect

    loop_src = inspect.getsource(OutboxLoopService)
    hook_src = inspect.getsource(OutboxDrainHook)
    assert "on_before_publish" not in loop_src
    assert "on_before_publish" not in hook_src
    assert "process_batch" in loop_src
    assert "process_batch" in hook_src
