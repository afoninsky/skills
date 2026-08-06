Do not scale this globally yet. The headline conversion result is not sufficient evidence of a win: the denominator excludes failed sessions, which can bias the result upward, while screen-reader completion and subgroup support incidents indicate plausible harm.

Treat the launch as a conditional hold and run three tracks immediately:

1. Correct the measurement. Recalculate conversion using all eligible assigned sessions, including failures, and report assignment-to-completion as the primary intention-to-treat metric. Audit how failures are classified, compare missingness by variant, device, assistive-technology use, geography, and relevant subgroup, and include confidence intervals rather than only point estimates.

2. Protect affected users. Pause expansion—and roll back the treatment for the affected subgroup or screen-reader users if targeting is reliable and rollback is safer. Review support incidents for severity, frequency, common task, and causal connection to the design. Escalate any issue that blocks access to an essential flow; provide a working fallback while fixes are developed.

3. Diagnose the experience. Reproduce the complete journey with major screen readers and browser combinations, including errors, timeouts, validation, focus order, announcements, and recovery. Pair telemetry with support evidence and sessions involving affected users; aggregate findings to protect privacy. Verify whether the increased conversion comes from a genuine usability improvement or from users being dropped before entering the denominator.

Define a new ship gate before resuming rollout:

- no material regression in end-to-end completion for screen-reader users;
- subgroup incident rate returns to baseline or an agreed safety threshold;
- the conversion lift remains credible under the corrected denominator;
- critical accessibility defects are fixed and independently retested;
- monitoring and a rapid rollback path are in place.

If the corrected analysis still shows an overall lift but harm remains concentrated, do not average it away. Redesign the problematic path, validate it with affected users, and rerun a staged experiment with explicit accessibility and subgroup guardrails. A global launch is justified only when the benefit survives valid measurement and the known harms are resolved or demonstrably controlled.
