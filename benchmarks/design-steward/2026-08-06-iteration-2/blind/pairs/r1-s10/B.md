# G6 live-learning decision: do not scale globally

**Proposed outcome: Stop.** The headline conversion increase does not justify global scaling. The accountable Product Owner/service owner is **Unassigned — Blocking Unknown**; only that named human may record the release decision after the failed gates are resolved.

## Evidence assessment

- The overall-conversion claim is **not valid E4 experimental evidence for scaling** because failed sessions were excluded from its denominator. Report the observed increase only as a method-limited signal; recompute it with an intent-to-treat or otherwise pre-specified eligible-session denominator, segmented by completion outcome, assistive-technology use, and affected subgroup, with uncertainty.
- The screen-reader completion decline is a production accessibility contradiction. Its precise magnitude and uncertainty still need verification, but the supplied direction of effect establishes an **Accessibility: Fail**, not an average that the aggregate gain can offset.
- Increased support incidents for one subgroup are adverse **E5 field evidence** for that population and journey. Severity, causal attribution, and exposure need triage, but the signal cannot be hidden by the aggregate conversion result.

## Hard gates

- Accessibility: **Fail** — screen-reader completion fell.
- Content truth: **Not yet evidenced** — incident causes, instructions, states, consequences, and recovery have not been reviewed.
- Privacy and participant welfare: **Not yet evidenced** — subgroup analysis permissions, minimization, and access controls are unspecified.
- Ethical UX and safety: **Fail** — a subgroup has an observed increase in adverse support outcomes; severity and recovery remain unresolved.
- Provenance and AI use: **Not yet evidenced** — metric definitions, event provenance, exclusions, and analysis lineage are absent.

## Required recovery action

Pause further expansion and preserve the current allocation and logs. If exposure may cause serious or irreversible harm, the service owner should limit or roll back the affected route under the existing incident process. Assign an accessibility specialist, measurement owner, support/operations owner, and subgroup-harm owner to:

1. audit screen-reader journeys with relevant disabled users and integrated manual/automated assurance;
2. triage incident severity and recovery by subgroup;
3. repair and independently verify denominator and instrumentation;
4. record dissent, limitations, and residual risks against stable evidence IDs.

Return to G6 only after the failed gates pass and a named accountable owner explicitly approves a bounded launch or scale decision. The safe default is no global scale.
