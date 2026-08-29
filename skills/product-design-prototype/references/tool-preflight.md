# Prototype capability preflight

Use this only when the prototype's chosen fidelity or evidence depends on an uncertain capability. The question determines the tools, not the reverse.

## Minimum capabilities

A prototype may need:

- an isolated writable location;
- a renderer or runtime appropriate to the question;
- repeatable interaction control for behavior claims;
- visual capture for composition claims;
- platform or accessibility inspection for claims that depend on them;
- sharing or device distribution only when the intended reviewer cannot inspect locally.

Use the project's existing browser, design canvas, native preview, test runner, fixtures, and package manager when suitable. Do not add a production dependency or new infrastructure for a disposable artifact.

## Check proportionally

1. State the question, fidelity, target conditions, and evidence needed.
2. Inspect existing tools and prove the selected renderer with the smallest disposable output.
3. Verify interaction, capture, or accessibility paths only when the claim activates them.
4. Use an equivalent established tool when it preserves the necessary evidence.
5. If a capability is missing, lower fidelity or narrow the claim when that still answers the question; otherwise explain the blocker.

Formal suite projects may record `available`, `missing-blocking`, `missing-degradable`, `unknown`, or `not-applicable`. Do not create toolchain metadata for an ordinary prototype.

## Evidence boundaries

- Source or pseudocode without a working render is not high-fidelity prototype evidence.
- A static image does not prove interaction behavior.
- Simulator output does not become physical-device evidence.
- Agent or synthetic-persona feedback is not representative-user validation.
- A prototype capture is not an accepted baseline.

When setup, hosting, account connection, device distribution, participant contact, or spend is necessary, consult current official guidance, describe the exact external effect and rollback, and obtain authorization before acting.
