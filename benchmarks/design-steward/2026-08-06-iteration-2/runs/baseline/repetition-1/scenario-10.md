# Recommendation: Do not scale globally yet

The headline conversion result is not sufficient evidence for a global rollout. The experiment denominator excludes failed sessions, so the reported lift may be biased upward precisely by omitting users who could not complete the flow. At the same time, screen-reader completion declined and support incidents increased for a subgroup. Those are material regressions, not secondary metrics to average away.

Pause expansion and keep exposure at the smallest safely reversible level. If the affected experience creates a serious accessibility or customer-harm risk, roll it back for the impacted paths immediately.

Before making a launch decision:

1. Recalculate conversion using all eligible sessions assigned at exposure, including failures, timeouts, crashes, and abandonment. Report absolute counts, confidence intervals, and missing-data rates.
2. Segment outcomes by assistive-technology use and by the subgroup with elevated incidents. Check both completion and error rates; aggregate improvement does not compensate for concentrated harm.
3. Audit the screen-reader journey end to end with representative browser and screen-reader combinations. Identify the failing step, repair semantics, focus order, announcements, labels, validation, and recovery behavior, then test with disabled users where feasible.
4. Classify the support incidents by severity and root cause. Confirm whether the design caused them, whether users can recover, and whether any data, financial, or access consequences occurred.
5. Rerun a corrected experiment with an intention-to-treat denominator and predeclared guardrails. Accessibility completion and subgroup incident rates should be release-blocking guardrails, not merely monitored diagnostics.

Proceed to global rollout only if the inclusive conversion result remains positive, screen-reader completion is restored to at least baseline, the subgroup incident increase is resolved, and no severe harm signal remains. Document the decision and maintain a rollback trigger during staged expansion.

The current decision is **no-go for global scale**: the metric is incomplete, and the observed harms outweigh confidence in the headline win.
