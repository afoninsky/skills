# Change capability preflight

Use this for a bounded change only when the safety or evidence of that change depends on an uncertain capability. Do not require formal suite tooling for an ordinary repository.

## Minimum capabilities

Select from the real impact:

- a trustworthy current or accepted comparison state;
- source and history inspection sufficient to understand the existing behavior;
- a way to trace shared components, tokens, generated outputs, and platform consumers;
- the project's affected build, runtime, test, accessibility, and visual-comparison paths;
- deterministic generation when a canonical source feeds generated outputs;
- formal source-map, manifest, hashes, or guard only when the repository already protects design state that way or the risk justifies adding them.

## Check proportionally

1. Name the final observable delta and must-not-change behavior.
2. Inspect existing tools and protection before proposing setup.
3. Probe only capabilities that support the actual affected consumers and preservation claims.
4. Use established equivalents; an absent optional MCP or preferred brand is normally not a gap.
5. Stop before mutation if missing comparison, generation, runtime, or scope evidence makes this particular change unsafe. Otherwise complete the bounded safe work and state the evidence limit.

Formal suite projects may retain `available`, `missing-blocking`, `missing-degradable`, `unknown`, and `not-applicable`. Do not create `design/toolchain.json` solely for a small change.

## Evidence boundaries

- A local selector does not prove a shared token change is local.
- A captured screenshot is not a deterministic preservation assertion.
- Browser verification does not prove packaged-shell or independent native consumers.
- Missing accessibility evidence limits accessibility conclusions.
- An unchanged baseline file plus a matched runtime comparison supports preservation; regenerating the baseline does not.

When a necessary tool or target is unavailable, explain the exact consumer or claim affected. Offer an existing equivalent, current-official setup, or a non-production impact plan. Obtain authorization before installing tools, adding dependencies, connecting accounts, modifying CI, publishing, or spending.
