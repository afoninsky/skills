# Implementation capability preflight

Use this when an implementation outcome depends on a capability whose availability is uncertain. Inspect the project's real toolchain first and evaluate only the implemented surface and claims.

## Minimum capabilities

Production implementation normally needs:

- access to the target source and current working state;
- the project's build or static-check path;
- a real browser or app runtime for visual and interaction claims;
- platform-appropriate accessibility evidence for accessibility claims;
- affected functional and regression checks;
- deterministic generation only when the repository already has generated design outputs.

Component workbenches, Playwright, Maestro, axe, native inspectors, design tools, hosted previews, and device labs are examples, not mandatory brands. Reuse an established equivalent that produces the needed evidence.

## Check proportionally

1. Bind the intended surface, states, targets, and claims.
2. Inspect manifests, scripts, tests, previews, wrappers, and existing design records.
3. Probe only the selected build, runtime, target, and evidence paths with safe version/list/build/smoke commands.
4. Continue with safe implementation work that does not depend on a missing capability; label unsupported conclusions.
5. Stop before a production edit when the missing capability makes that edit unsafe, prevents preservation of a high-risk path, or is essential to the user's requested acceptance.

A formal suite toolchain may use `available`, `missing-blocking`, `missing-degradable`, `unknown`, and `not-applicable`. Do not create or update the record unless the repository already uses it and design-record writes are authorized.

## Missing evidence

- No real runtime means no verified visual or interaction result.
- No accessibility path means no accessibility acceptance.
- No representative participants means no usability-validation claim.
- No deterministic generator for an affected canonical output means do not hand-edit generated copies.
- No packaged-app run for a shared web wrapper means shell-specific behavior remains unverified, even if browser behavior passes.

If setup is necessary, consult current official documentation, use the existing package manager and architecture, explain files/dependencies/permissions/rollback, obtain authorization, and verify with the smallest real affected case. An MCP may accelerate inspection but does not replace repository source, tests, runtime output, or accepted evidence.
