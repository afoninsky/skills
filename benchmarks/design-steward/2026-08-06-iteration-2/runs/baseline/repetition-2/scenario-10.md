Do not scale this design globally yet. The headline conversion result is not sufficient evidence of a win: the denominator excludes failed sessions, so the reported lift may be biased, while screen-reader completion and subgroup support incidents indicate material harm.

Treat the current launch as a conditional or failed decision pending investigation. Immediately:

1. Pause further rollout and preserve the current control or a safe fallback. If the affected subgroup faces severe or irreversible harm, roll back their exposure now.
2. Recalculate conversion using an intent-to-treat denominator that includes every eligible assigned session, including failures, timeouts, crashes, and abandonment. Report absolute counts, rates, confidence intervals, missingness, and exposure by variant.
3. Break outcomes down by assistive-technology use and the subgroup with elevated incidents. Measure task completion, error and abandonment rates, time to complete, support contacts, and incident severity—not conversion alone.
4. Audit the end-to-end screen-reader journey with representative users and common browser/assistive-technology combinations. Review focus order, announcements, labels, validation, error recovery, dynamic updates, and keyboard operation.
5. Triage subgroup incidents to identify a shared failure mode, quantify impact, and establish whether the experiment caused the increase.

Before resuming expansion, define explicit guardrails: no meaningful regression in screen-reader completion, no increase in severe incidents for any material subgroup, complete session accounting, and an independently reviewed accessibility pass. Re-run or continue the experiment only after instrumentation and design defects are corrected, with predeclared success and stop criteria.

The decision should be based on the full outcome set. A conversion gain that depends on excluding failures or shifts costs onto disabled users or a vulnerable subgroup is not a globally scalable product improvement.
