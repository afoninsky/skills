# Evidence and optional human gates

Use evidence in proportion to the decision. Formal gates are useful for durable, high-impact, regulated, collaborative, release, or accepted-baseline work; they are not mandatory pauses for ordinary clear requests. The user's explicit request may already authorize the stated exploration and mutation scope.

## Evidence labels

Use the strongest truthful label:

- **E0 — agent judgment:** generated analysis or visual critique.
- **E1 — specialist/heuristic review:** structured review by a relevant expert or tool.
- **E2 — deterministic artifact/runtime evidence:** tests, goldens, traces, semantics, device output.
- **E3 — internal human task evidence:** observed task completion by non-representative reviewers.
- **E4 — representative-user evidence:** appropriately recruited target users.
- **E5 — live product evidence:** consented, correctly interpreted production behavior/outcomes.

Higher labels do not automatically invalidate lower evidence, and quantity does not upgrade a label. Agent or synthetic-user review remains E0.

## Gates

| Gate | Human decision | Minimum supporting evidence |
|---|---|---|
| A — UX brief | Confirm user, task, structure, content hierarchy, states, platforms when a material decision remains | grounded brief; unresolved assumptions visible |
| B — direction | Select one visual backbone when selection was not delegated | matched renders and comparison; agent may select a working direction when the user delegated judgment |
| C — representative slice | Approve contract expression on representative targets | real renders/prototype states; accessibility risks visible |
| D — candidate decision | Accept, reject, or request bounded revision | real runtime, deterministic checks, review report, representative matrix |
| E — baseline authorization | Explicitly approve the exact named reviewed candidate and covered conditions as the accepted identity | reviewed diffs, exact identity, baseline environment, approval record |
| F — release/learning | Release/hold, or approve/revise/reject a named research or learning action | review-owned packet with applicable accessibility, device, user, safety, privacy, and operational evidence |

Missing evidence limits the decision it supports. A user may authorize further exploratory work but cannot turn absent evidence into a pass.

Candidate acceptance does not imply baseline authority unless the user explicitly says the named reviewed candidate should become the accepted identity. One clear instruction may contain both decisions when it identifies the candidate and evidence; do not force a duplicate confirmation turn. Only then does `product-design-contract` in `accept-freeze` mode record the approved identity.

In a formal engagement, `product-design-review` owns the Gate F evidence packet. The reviewer may recommend release, hold, or further research, but the accountable human makes and executes the consequential decision. Missing evidence prevents an unsupported recommendation, and review never deploys, instruments, recruits, or contacts participants.

For consequential Gates B–F, use representative configurations for every materially distinct implementation or adaptation class included in the claim, with explicit exclusions. Approval language is limited to what was actually reviewed; it never means “all platforms” by implication.

## Separate decisions

Do not infer one of these decisions from another:

- selecting visual direction;
- approving a prototype;
- accepting source implementation;
- approving visual/system integration;
- accepting new baselines;
- releasing/deploying;
- instrumenting analytics or contacting participants.

A single instruction may authorize more than one only when it clearly identifies each decision and its scope.

## Baseline acceptance

Require an explicit instruction that identifies the candidate and acknowledges its observed diffs. “Update snapshots,” a green test after regeneration, or the agent's recommendation is not acceptance.
