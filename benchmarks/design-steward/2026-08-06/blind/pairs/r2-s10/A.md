Do not scale globally.

**G6 Live learning — proposed outcome: Pivot.** Pivot from expansion to containment, corrected measurement, and targeted investigation. The accountable Product Owner/launch owner must approve the next production decision; their name is missing and must be recorded. Accessibility, experimentation/analytics, and subgroup-risk claims need named specialist owners.

The headline conversion result is not decision-grade E4 evidence for the claimed population. Excluding failed sessions creates survivorship/attrition bias and can make conversion appear better precisely by omitting people harmed by the experience. It cannot compensate for a non-passing hard gate.

Current signals:

- Screen-reader completion fell: treat this as an accessibility **Fail** if the production measure is reliable; otherwise it is **Not yet evidenced**, which is still non-passing. Either state blocks scale.
- Support incidents increased for a subgroup: ethical UX/safety is **Not yet evidenced** until severity, affected journey, exposure, and causality are triaged. Preserve this dissent rather than averaging it into the overall metric.
- Content truth, privacy/welfare, and provenance were not assessed in the supplied evidence and must not be presumed to pass.

Before another scale decision:

1. Freeze expansion and define owner-approved containment or rollback thresholds for the affected journeys.
2. Recalculate outcomes using all randomized/eligible sessions, including failures and dropouts. Report absolute completion and conversion by assignment, screen-reader status, and relevant subgroup, with missingness, sample sizes, uncertainty, and incident severity.
3. Have an accessibility specialist investigate the completion drop with manual assistive-technology testing and representative screen-reader users, including error and recovery states.
4. Triage subgroup incidents with support and the accountable safety/ethics owner; minimize sensitive data and avoid unauthorized identity joins.
5. Correct the design or instrumentation, then run a bounded re-test with accessibility and subgroup-harm guardrails specified in advance.

Global scaling can be reconsidered only when the inclusive analysis still supports benefit, accessibility and safety gates pass, residual risks have owners, and the named human approver explicitly authorizes scale.
