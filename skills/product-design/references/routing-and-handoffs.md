# Routing and handoffs

Use this protocol for a durable multi-worker engagement, automation that needs machine-readable state, resuming across context loss, or an accepted-baseline transition. Ordinary atomic requests need only a concise working scope and handoff.

## Routing model

Route by the unresolved decision:

- users, jobs, flows, content, or consequential domain knowledge → discovery;
- visual or interaction grammar → direction;
- durable tokens, components, source ownership, or accepted identity → contract;
- an isolated proof of a design question → prototype;
- a clear new product surface → implementation;
- a bounded delta to existing or accepted UI → change;
- quality, fidelity, accessibility, drift, or release evidence → review.

Choose the smallest route that can deliver the requested outcome. The user's request supplies authority for its stated exploration and mutation scope. Continue through a sequence when decisions are clear, tools are adequate, and writes stay within that scope. Pause only for a material unknown, scope expansion, consequential external action, or protected acceptance decision.

Workers may be used atomically or in combinations such as:

```text
discovery → direction → prototype → implementation → review
direction → contract → implementation
review → bounded change → review
reviewed candidate → contract:accept-freeze
```

These are useful paths, not mandatory pipelines. Skip resolved phases and do not create a worker handoff solely because a phase exists.

## Preserve identity proportionally

For simple work, keep the objective, intended delta, must-preserve list, assumptions, and exact next action in working context.

Use a durable routing record when compaction, automation, multiple agents, protected artifacts, or resumability makes identity important. In the project's existing format, include only relevant fields:

- request or decision ID;
- original objective and, when useful, its digest;
- exploration and mutation scope;
- accepted inputs or comparison state;
- fixed constraints, assumptions, and material unknowns;
- affected targets and shared ownership;
- allowed writes and protected artifacts;
- evidence needed for the next claim;
- current worker and exact stopping condition.

Do not create envelope, toolchain, or project-state files for a routine request merely to satisfy this suite.

## Handoffs

A useful handoff states:

- outcome and status;
- artifacts or production files changed;
- explored alternatives not committed;
- evidence run and missing evidence;
- scope preservation and baseline status;
- assumptions and limitations;
- next decision or action.

The router validates that a successor does not broaden authority, hide missing evidence, or mutate a protected baseline.

Formal projects already using the suite's legacy A–F envelope schema may adapt the legacy [routing-envelope](../assets/routing-envelope.json) and [worker-handoff](../assets/worker-handoff.json) assets and use the bundled route and toolchain validators. Those assets intentionally default to Gate A and a `design/toolchain.json` record for compatibility; do not copy those defaults into a new proportional engagement. The schema records some decisions in separate envelopes and applies stricter execution preflight than ordinary routing; a single clear user instruction may still supply multiple explicit decisions without a duplicate conversation turn. The validators preserve compatibility for those projects and do not prove design quality:

```text
python3 <product-design-skill-directory>/scripts/validate_route.py <routing-envelope> --toolchain <toolchain> --for-execution
python3 <product-design-skill-directory>/scripts/validate_route.py <routing-envelope> --toolchain <toolchain> --handoff <worker-handoff>
```

## Ambiguous requests

- **Discovery or review:** unresolved product definition routes to discovery; assessment of an existing experience routes to review.
- **Direction or prototype:** visual/interaction language routes to direction; feasibility or behavior proof routes to prototype.
- **Implementation or change:** a clear new surface routes to implementation; modifying current or accepted behavior/design routes to change.
- **Review and fix:** review first. Apply only findings already covered by a clear mutation scope; confirm material redesign, shared impact, dependencies, or baseline changes.
- **Vague improvement:** inspect the current product and rationale before mutation, then form bounded findings and useful direction alternatives.
- **Shared dependency:** expand analysis and verification to real consumers. Ask before mutation when that expands the user's scope.
- **Approved design to code:** implement directly when the design and states are clear enough; use direction, contract, or prototype only for material unresolved decisions.
- **Autonomous design:** a broad or greenfield request may delegate reversible design choices. Explore proportionally, select a working direction, and implement only within the named scope.

## Protected acceptance

Implementation and change never update accepted references or baselines. Snapshot regeneration, passing tests, agent judgment, and implied enthusiasm are not acceptance.

Route to `product-design-contract` accept-freeze only when the human explicitly identifies the reviewed candidate and authorizes that identity and covered conditions as the accepted baseline. A single clear instruction may both dispose the reviewed candidate and authorize its freeze; do not force a duplicate approval turn. Deployment, instrumentation, participant contact, external publication, and spend remain separate decisions.

## Failure and recovery

When a worker, target, or necessary capability is unavailable:

1. preserve current accepted and user-owned state;
2. state which artifact, edit, evidence, or claim is affected;
3. complete unrelated safe work when useful;
4. offer the smallest existing-tool, supplied-evidence, setup, or reduced-scope path;
5. resume from the recorded next action rather than restarting resolved design work.
