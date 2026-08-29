---
name: product-design-prototype
description: Internal prototyping worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-prototype, or advanced automation supplies equivalent accepted design inputs and authority; for every other raw UI/UX request, use product-design. Build an isolated disposable web or mobile wireframe, mock, interaction proof, state demonstration, or representative slice that answers one design question. Do not choose art direction, ship production components, alter an accepted design or baseline, or perform a read-only audit.
compatibility: Requires versioned isolated artifacts plus a working renderer/runtime and capture path appropriate to the question. Playwright, Maestro, native previews/tests, workbenches, Penpot, preview hosting, and tester distribution are selected conditionally; no single framework, SaaS, or MCP server is mandatory.
---

# Product Design Prototype

Build the least expensive real artifact that answers one design question. A prototype is evidence for a decision, not a shortcut into production.

## Start here

1. Read [tool preflight](references/tool-preflight.md) completely and run it before creating source or connecting a remote tool.
2. Read [prototype method](references/prototype-method.md) before choosing fidelity or scope.
3. Read [platform adapters and verification](references/platform-adapters-and-verification.md), then load only the row relevant to the detected architecture/target.
4. Use the templates in `assets/`; keep prototype source and dependencies isolated.

When routed, preserve the unchanged original prompt and obey the routing envelope. When invoked directly, establish a request ID, accepted artifact hashes, scope, mutation authority, target matrix, design question, and stop condition equivalent to Gate C when this is a representative slice.

The target matrix is non-empty and includes at least one representative configuration for every materially distinct implementation/adaptation class needed to answer the question. It is not an exhaustive device list. Make exclusions explicit. A shared web wrapper uses one shared UI prototype plus separate browser and packaged-shell evidence rows when shell behavior matters.

## Preconditions and authority

- Read `design/project-design.json` when present. Require an accepted brief for behavior/structure questions, a selected direction for visual-fidelity questions, and the current design contract when demonstrating a contracted system. Use only the prerequisites needed for the question; never invent a missing approval.
- Inspect repository architecture and platform sharing before selecting a prototype medium. A web-wrapper mobile app may have one UI source plus packaged-shell checks, not a second native UI prototype.
- Define one decision question and observable success/failure before building. If the question is “which aesthetic?”, route to `product-design-direction`. If the request is “ship this,” route the approved result to `product-design-implementation` later.
- Permit writes only to isolated prototype artifacts, fixtures, and verification output. Do not edit production components, accepted contracts/references, or baselines.
- Adding a dependency, publishing a preview, distributing a build, connecting an account, or contacting testers requires explicit authorization.

## Workflow

### 1. Choose the lowest useful fidelity

Use:

- a flow or low-fidelity wireframe for information order and navigation;
- a clickable schematic for sequence, disclosure, or role handoff;
- a high-fidelity visual mock for responsive/adaptive composition or expression of a selected direction;
- a framework/native preview when keyboard, safe area, text scaling, native controls, animation, or platform behavior is material;
- one representative vertical slice before system-wide implementation.

State what this fidelity can and cannot prove. Do not polish unresolved behavior or use a static image to claim interaction evidence.

### 2. Create an isolation contract

Assign a prototype ID. Record source location, build/run command, allowed dependencies, production-import boundary, teardown/archival plan, accepted input hashes, and expiration/status. Prefer a disposable directory/package or isolated worktree. Production may be imported read-only for an existing component-state question, but production must never import prototype code.

### 3. Create deterministic fixtures

Use real-shaped, deterministic content rather than lorem ipsum or live APIs. Include the minimum states needed to disprove the design, such as:

- default/success;
- long and short content;
- zero/one/many items;
- loading, empty, error, retry, offline, permission denied;
- destructive confirmation and recovery;
- interrupted/returning use;
- large text, locale expansion, dark/high-contrast mode where relevant.

Record fixture IDs and expected transitions. Keep personal/sensitive data synthetic and obviously fictional.

### 4. Build only the decision slice

Implement enough entry context, core act, consequence, recovery, and return state to answer the question. Reuse the accepted direction/contract; do not redesign around implementation convenience. Prefer semantic controls and real layout behavior so accessibility and adaptation can be inspected.

Avoid production-grade infrastructure, generalized data layers, analytics, authentication, migration logic, and abstractions unrelated to the question. If a shortcut could alter perceived behavior, disclose it.

### 5. Verify in a real render/runtime

Run the prototype at every representative configuration in the named matrix. Use a repeatable flow for interaction questions and capture matched renders for visual questions. Check relevant adaptive behavior, content extremes, keyboard/touch, safe areas, text scaling, orientation, focus/semantics, reduced motion, and recovery.

Use the repository's established tools when equivalent. For protected web evidence, prefer Playwright; for mobile app flows, prefer Maestro plus native checks where needed. Penpot click-through is adequate only for questions it can faithfully represent.

Record actual evidence and limitations. A source file, mocked screenshot, or agent description is not proof that the prototype runs.

### 6. Write an implementation-neutral behavior specification

Describe triggers, states, transitions, content/action contracts, platform adaptations, accessibility behavior, and unresolved risks without prescribing disposable source patterns as production architecture. Link every rule to a demonstrated fixture/evidence item.

### 7. Stop for the decision

For a representative slice, present the runnable prototype, matched renders, verification, and limitations at Gate C. Ask the owner to approve, amend, or reject the named prototype/ref/hash. Do not copy it into production or update baselines.

An atomic prototype answering a narrow question may finish without a pipeline gate, but must still state the answered decision and evidence boundary. A router-controlled pipeline advances only after its named human gate.

## Default outputs

- `design/prototypes/<prototype-id>/prototype-plan.md`
- isolated source/dependency files
- `design/prototypes/<prototype-id>/fixtures.json`
- `design/prototypes/<prototype-id>/behavior-spec.md`
- `design/prototypes/<prototype-id>/render-manifest.json`
- `design/prototypes/<prototype-id>/verification.md`
- an update to project state references/hashes when routed

Adapt an existing project convention without importing prototype code into production.

## Completion checks

- One named question and observable stop condition govern the prototype.
- Accepted UX/direction/contract inputs remain unchanged and traceable by hash.
- Source/dependencies are isolated and no production file imports the prototype.
- Required states use deterministic fixtures and real-shaped content.
- The named targets render in a real browser/app/editor runtime and critical interactions are repeatable.
- Accessibility/adaptive risks and untested targets are explicit.
- Captures are prototype evidence, not approved visual baselines.
- Missing runtime, accessibility, participant, or physical-device evidence leaves the affected gate `Not evidenced` and cannot be promoted to a pass.

## Handoff

End with a concise decision result and this suite-compatible object:

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-prototype",
  "status": "complete | needs-owner | blocked | failed",
  "input_hashes": {"original_prompt": "<sha256>"},
  "artifacts_created_or_changed": [],
  "production_mutations": [],
  "evidence": [],
  "missing_evidence": [],
  "degraded_capabilities": [],
  "baseline_changed": false,
  "gate": "C | null",
  "recommended_next_worker": "product-design-implementation | null",
  "exact_next_action": "..."
}
```

For a representative slice, the normal status is `needs-owner` at Gate C. Only the `product-design` router advances a worker series.
