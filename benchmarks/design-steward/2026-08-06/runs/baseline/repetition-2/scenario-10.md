I would not scale this globally. The headline result is not decision-grade: excluding failed sessions creates survivorship bias, while the screen-reader regression and subgroup-specific support increase are evidence of material harm that an aggregate conversion lift can conceal.

The appropriate decision is to pause expansion and contain the risk. Keep unaffected traffic at its current level only if the evidence supports doing so; otherwise roll back to the last known-good experience. For the affected subgroup and screen-reader journey, default to rollback or a safe fallback now rather than waiting for statistical certainty. Preserve assignment, failure, accessibility, and support data for analysis.

Before reconsidering rollout:

- Recalculate results on an intent-to-treat basis: every assigned session belongs in the denominator, with failed sessions counted as failures. Report absolute conversion, failure, abandonment, and uncertainty—not just relative lift.
- Segment outcomes by assistive-technology use, affected subgroup, device, browser, locale, and key funnel step. Check whether the aggregate result is masking divergent effects.
- Treat screen-reader completion and subgroup incident rates as launch guardrails, not secondary diagnostics. Define acceptable non-inferiority margins and minimum sample sizes in advance.
- Reproduce the failures with representative screen-reader/browser combinations, inspect focus order, announcements, validation, timeouts, and recovery paths, and pair telemetry with support-ticket review and sessions with affected users.
- Fix the causal issues, then validate with automated checks, manual accessibility testing, and task-based usability testing. Accessibility conformance alone is insufficient if completion remains worse.

Resume only through a staged rollout with live guardrails and automatic stop conditions. A global scale decision should require: corrected inclusive conversion remains positive; screen-reader completion is no worse than the agreed margin; the subgroup incident increase has returned to baseline; and failed-session rates are fully included and acceptable.

Document the original denominator flaw and the harm signals in the experiment readout. The right interpretation is: “promising aggregate lift, invalidated by biased measurement and unacceptable segmented regressions,” not “the headline metric won.”
