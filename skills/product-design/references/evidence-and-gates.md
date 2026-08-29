# Evidence and human gates

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
| A — UX brief | Approve user, task, structure, content hierarchy, states, platforms | grounded brief; unresolved assumptions visible |
| B — direction | Select one visual backbone | matched renders and comparison; agent may recommend only |
| C — representative slice | Approve contract expression on representative targets | real renders/prototype states; accessibility risks visible |
| D — candidate decision | Accept for the next acceptance step, reject, or request bounded revision | real runtime, deterministic checks, review report, representative matrix |
| E — acceptance authorization | Explicitly approve the exact named reviewed candidate and matrix as the new accepted identity | Gate D disposition, reviewed diffs, exact ref/hash, baseline environment, approval ID |
| F — release/learning | Release/hold, or approve/revise/reject a named research or learning action | review-owned packet with applicable accessibility, device, user, safety, privacy, and operational evidence |

Missing tools may leave a gate `Not evidenced`. A user may authorize further exploratory work but cannot waive missing evidence into `Pass`.

Gate D acceptance is not Gate E approval. After Gate D, the router presents the immutable candidate, reviewed matrix, material diffs, and limitations again for a separate explicit Gate E decision. Only then does `product-design-contract` in `accept-freeze` mode record the already-approved identity and baseline hashes; the recording operation is not another human gate.

`product-design-review` owns the evidence packet for Gate F and stops with `needs-owner`. The owner makes the release/hold or research/learning decision. Missing required evidence blocks before Gate F rather than asking the owner to guess, and the reviewer never deploys, instruments, recruits, or contacts participants.

For Gates B–F, a representative platform matrix is non-empty whenever the product has a platform target. Include at least one configuration for every materially distinct implementation/adaptation class and name exclusions. Approval language is limited to that matrix; it never means “all platforms” by implication.

## Separate decisions

Do not collapse these into one approval:

- selecting visual direction;
- approving a prototype;
- accepting source implementation;
- approving visual/system integration;
- accepting new baselines;
- releasing/deploying;
- instrumenting analytics or contacting participants.

## Baseline acceptance

Require an explicit instruction that identifies the candidate and acknowledges its observed diffs. “Update snapshots,” a green test after regeneration, or the agent's recommendation is not acceptance.
