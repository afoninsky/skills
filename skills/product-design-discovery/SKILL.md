---
name: product-design-discovery
description: Internal discovery worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-discovery, or advanced automation supplies equivalent accepted inputs and authority; for every other raw UI/UX request, use product-design. Establish evidence-backed users, jobs, journeys, information architecture, content hierarchy, required states, and web/mobile constraints before visual styling. Do not choose art direction, build polished mocks or production UI, change an accepted design, or perform a visual-quality audit.
compatibility: Requires project-file read/write access; durable versioning is required before Gate A acceptance or pipeline continuation. Web research, participant research, app-runtime inspection, and Penpot are conditional or optional capabilities selected by preflight; no particular SaaS or MCP server is mandatory.
---

# Product Design Discovery

Create the smallest trustworthy UX contract that lets later design work proceed without guessing. Discovery determines what the product must help people do, not how the interface should look.

## Start here

1. Read [tool preflight](references/tool-preflight.md) completely before research or file writes. Run it visibly. If it pauses work, tell the user which capability is missing and why.
2. Read [discovery method](references/discovery-method.md) before interviewing, researching, or synthesizing.
3. Read [evidence and platform coverage](references/evidence-and-platform-coverage.md) when the request needs current facts, participant evidence, an existing runtime, or more than one platform/input model.
4. Use the templates in `assets/` without overwriting accepted project artifacts.

If invoked by `product-design`, accept the unchanged original prompt and routing envelope as inputs. Do not reinterpret or expand the router's mutation authority. If invoked directly, construct the same minimum envelope in working context: scope, authority, accepted inputs, fixed constraints, assumptions, blocking unknowns, and stop condition.

## Preconditions

- Inspect `design/project-design.json` when present. Treat accepted paths and hashes as authoritative; never infer approval from chat summaries or draft filenames.
- Inspect the repository, product documentation, existing implementation, and research records before asking questions they already answer.
- Confirm the discovery boundary. This phase may create discovery artifacts; it does not choose a visual direction, edit production UI, recruit participants, spend money, enable analytics, or accept a baseline without separate authority.
- If a reliable accepted brief already answers the request, stop and recommend the appropriate next worker rather than rewriting it.

## Workflow

### 1. Frame the decision

State the decision this discovery must enable, affected people, product stage, target platforms, and the evidence threshold. Classify each known decision as:

- **Fixed:** preserve unless the owner explicitly reopens it.
- **Challengeable:** question only with evidence and show the consequence.
- **Open:** resolve in this phase or record as an assumption.

Separate a **blocking unknown** from a reversible **working assumption**. Ask only questions whose answers would materially change users, flows, content, safety, scope, or target coverage. Prefer one compact batch over an open-ended interview.

### 2. Inspect before researching

Build an evidence inventory from supplied material and the repository. Trace current routes/screens, domain vocabulary, data and permission states, existing tests, accessibility constraints, platform sharing, and known support failures. Do not treat implementation accidents as product requirements.

Research externally only for a named knowledge gap. Prefer primary sources for standards, platform behavior, law, safety, and technical constraints. For user attitudes or comprehension, use representative people; an agent critique is not user research.

### 3. Model the experience

Define:

- primary and secondary users or roles;
- priority situations, jobs, desired outcomes, and failure costs;
- the core act and the information/action needed in the first ten seconds;
- entry, happy path, alternate path, recovery, completion, and return journeys;
- surfaces/screens and navigation relationships;
- real content hierarchy and content extremes;
- loading, empty, error, offline, permission, destructive, interrupted, and success states as applicable;
- phone, tablet, desktop, orientation, safe-area, keyboard, pointer, touch, large-text, locale, and assistive-technology constraints as applicable.

Keep the fidelity appropriate: a text flow or simple wireframe is enough when structure is the question. Do not introduce color, typography, decoration, or a component aesthetic.

### 4. Reconcile evidence and assumptions

For every consequential claim, record its source, evidence level, date when time-sensitive, confidence, affected decision, and limitation. Resolve contradictions explicitly. Do not flatten stakeholder preference, repository behavior, market fact, platform rule, and participant observation into one undifferentiated “finding.”

If participant evidence is required but unavailable, offer setup or a precisely named assumption-only continuation. The latter may produce a candidate brief, but it cannot be called user-validated or satisfy a representative-user evidence gate.

### 5. Write the discovery contract

Adapt the project layout; default outputs are:

- `design/brief.md`
- `design/experience-map.md`
- `design/research/evidence-register.md`
- a screen/surface and state inventory inside the brief or experience map
- an update to `design/project-design.json` that references paths and hashes rather than duplicating prose

Use [brief template](assets/brief.md), [experience-map template](assets/experience-map.md), and [evidence-register template](assets/evidence-register.md). Preserve unknowns honestly; do not fill unused sections with invented detail.

### 6. Stop at Gate A

Present the concise brief, material assumptions, evidence limitations, target/state coverage, and recommendation. Ask the owner to approve or amend the UX brief and structure. Approval must name the artifact/version or observable candidate; silence, prior enthusiasm, or agent confidence is not approval.

Do not begin art direction or production work in this skill.

## Completion checks

- The brief defines one observable product outcome, core act, rejection criteria, and priority journey.
- Fixed, challengeable, and open decisions remain distinguishable.
- Every commissioned role, state, surface, and target is covered, excluded with a reason, or visible as a gap.
- Factual and user claims are traceable; inference and preference are labeled.
- No visual direction, production code, approved reference, or baseline changed.
- Missing hard evidence remains a blocker for the claim it supports and the affected gate is reported as `Not evidenced`.

## Handoff

End with a short human summary followed by this machine-readable object:

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-discovery",
  "status": "complete | needs-owner | blocked | failed",
  "input_hashes": {"original_prompt": "<sha256>"},
  "artifacts_created_or_changed": [],
  "production_mutations": [],
  "evidence": [],
  "missing_evidence": [],
  "degraded_capabilities": [],
  "baseline_changed": false,
  "gate": "A | null",
  "recommended_next_worker": "product-design-direction | product-design-prototype | null",
  "exact_next_action": "..."
}
```

Normally the status is `needs-owner` at Gate A. A worker may recommend a next phase, but only the `product-design` router advances a series.
