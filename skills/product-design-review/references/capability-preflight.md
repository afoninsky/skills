# Review capability preflight

Use this only when a requested review conclusion depends on uncertain access or evidence. A review can still report bounded heuristic or source findings when stronger evidence is unavailable, provided the limits are explicit.

## Select capabilities from the question

- Visual, interaction, fidelity, or release conclusions need the real target at representative conditions.
- Accessibility conclusions need platform-appropriate automated or manual inspection.
- Drift claims need an identifiable accepted reference or contract.
- Usability, comprehension, or preference claims need representative people.
- Post-launch behavior claims need authorized, correctly scoped product evidence.
- A source-only architecture or token audit needs repository read access, not a browser by default.

Use existing project tests, previews, browsers, device tools, accessibility inspectors, analytics access, and research records. Named tools and MCPs are optional adapters unless the project itself depends on them.

## Check proportionally

1. Freeze or identify the target and list the conclusions requested.
2. Inspect existing evidence and probe only the capabilities those conclusions require.
3. Bind runtime evidence to the actual build or working state.
4. Complete useful narrower findings when a capability is missing, while withholding the unsupported conclusion.
5. Ask for setup, access, or equivalent evidence only when it would materially improve the requested decision.

Formal suite projects may record `available`, `missing-blocking`, `missing-degradable`, `unknown`, and `not-applicable`. Review remains read-only and should not update `design/toolchain.json`; return any material observation instead.

## Evidence boundaries

- No real runtime means no runtime fidelity or interaction acceptance.
- No accessibility inspection means no accessibility acceptance.
- No accepted identity means current-state consistency can be reviewed, but not drift from an accepted design.
- No representative participants means no usability validation.
- No consent, provenance, or direct trustworthy access means telemetry remains an unverified signal.
- A screenshot is capture evidence unless an active assertion or explicit approval gives it another role.

If setup or access is necessary, consult current official documentation, request least privilege, identify data/privacy implications and rollback, and obtain authorization before connecting accounts, installing tools, instrumenting, contacting participants, publishing, or spending.
