Do not approve this release as-is. Screenshot similarity verifies appearance, not the selected experience. Keyboard order, error recovery, responsive behavior, and instrumentation are all part of the product behavior; shipping known divergences would make the prototype—not the reviewed direction—the accidental specification.

Treat these as release criteria:

- Keyboard focus follows a logical order and all controls are operable without a pointer.
- Errors preserve user input, clearly explain the problem, focus or identify the affected field, and provide a reliable recovery path.
- The supported viewport range matches the approved responsive behavior, including content order, overflow, and touch targets.
- Required analytics events, properties, consent handling, and failure monitoring are verified in the production build.

Engineering should compare the production implementation against the selected interaction specification, not only screenshots, and record each mismatch as fixed, explicitly accepted, or deferred. Product, design, and engineering should jointly own any exception; design approval alone should not conceal accessibility, data-quality, or operational risk.

To minimize delay, run a short focused release review on the production candidate: keyboard-only traversal, one failed-and-recovered submission, representative narrow and wide viewports, and an instrumentation trace for the critical journey. If those checks pass after targeted fixes, approve immediately.

If the business must ship before all differences are resolved, use a documented exception rather than unconditional approval: limit exposure with a feature flag or staged rollout, identify an accountable owner, define rollback signals, and assign dated follow-up work. Keyboard traps, blocked error recovery, broken critical layouts, or missing critical instrumentation remain stop-ship issues.
