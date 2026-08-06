Do not scale this design globally.

**G6 Live learning — proposed outcome: Stop the global rollout.** The accountable Product Owner must approve any rollout, limitation, or rollback; the accessibility specialist owns accessibility claims, the experimentation/analytics owner owns metric validity, and the support or safety owner owns the subgroup-harm assessment.

The headline result does not support the requested conclusion. Because failed sessions are excluded, the conversion uplift describes only the included population, not end-to-end performance for everyone assigned or exposed. It is not adequate E4 evidence for a global-scale claim until the denominator, exclusions, segmentation, and uncertainty are corrected.

The other production signals cannot be averaged away:

- **Accessibility: Fail.** Screen-reader completion worsened. This is a non-compensable gate; higher aggregate conversion cannot turn it into a pass.
- **Ethical UX/safety: Not yet evidenced.** Increased support incidents for one subgroup are a potential harm signal requiring severity, journey, and causality triage. If investigation confirms harm or blocked recovery, mark this gate Fail.
- **Global benefit claim: Not validated.** The current evidence is scoped, internally inconsistent, and affected by denominator bias.

Immediately pause expansion and preserve these results, exclusions, objections, and affected-population definitions in the design record. If the accessibility regression or subgroup incidents are severe, the Product Owner should limit exposure or approve rollback while investigation proceeds.

Before reconsidering scale:

1. Recalculate outcomes on an assignment/exposure denominator that includes failed and abandoned sessions; publish exclusions, sample sizes, confidence intervals, and segmented results.
2. Diagnose the screen-reader journey with qualified accessibility review and representative screen-reader users, then verify the integrated fix across relevant assistive-technology/browser combinations.
3. Triage subgroup incidents with support and safety owners using minimized, authorized data; identify severity, mechanism, recovery path, and residual-risk owner.
4. Define non-inferiority guardrails for screen-reader completion and subgroup incident rates, then run a staged, monitored test with automatic pause criteria.

Reopen G6 only when accessibility passes, the harm route is resolved or acceptably bounded, instrumentation is valid, and the named human approver explicitly authorizes the next stage.
