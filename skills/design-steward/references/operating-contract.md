# Operating contract

## Contents

- Design Brief schema
- Unknowns and constraints
- Mode contract
- Authority model
- Capability registry
- Delegation and returns
- Lifecycle gates
- Consequential-change rule

## Design Brief schema

Require a versioned, Product Owner-approved Design Brief before direction generation. Include:

1. authority, objective, desired outcomes, and non-goals;
2. target users, contexts, priority journeys, and important exclusions;
3. evidence with source, recency, provenance, confidence, and access class;
4. representative content, canonical terminology, data conditions, and critical edge, error, and empty states;
5. accessibility, inclusion, ethical, privacy, legal, and safety constraints;
6. Evolution or From-scratch mode plus the constraint ledger;
7. technical, operational, platform, budget, timing, localization, and asset-rights constraints;
8. precommitted comparison criteria, baselines, evidence thresholds, and validation claim rule;
9. decision owners, human gates, participant-contact authority, permitted tools, data, sources, and product access;
10. change-control and clean-room boundaries.

Allow “not applicable” only with a recorded rationale.

## Unknowns and constraints

Classify a missing fact as:

- **Blocking Unknown** when it could materially change users, journeys, outcomes, representative content, constraints, safety, or the comparison rubric. Do not generate directions.
- **Working Assumption** when work can safely continue. Record rationale, risk, owner, planned test or evidence, and expiry or review trigger. Expose material assumption dependencies in every affected artifact.

Classify every relevant constraint as:

- **Fixed** — preserve it; record source, rationale, and decision owner.
- **Challengeable** — keep it in force until an evidence-backed alternative is approved.
- **Open** — deliberately available for exploration.
- **Blocking Unknown** — unsafe to classify yet.

Never infer a hidden constraint from an implementation, convention, or stakeholder preference.

## Mode contract

### Evolution

- Use only product context and constraints explicitly admitted by the approved brief.
- Preserve Fixed constraints.
- Challenge, but do not silently change, Challengeable constraints.
- Redesign Open areas.
- Treat an unspecified legacy convention as Open when safe; otherwise record a Blocking Unknown.
- Reapprove any consequential reopening of a Fixed constraint.

### From-scratch

- Default information architecture, navigation, interaction patterns, content structure, and visual language to Open.
- Keep users, outcomes, domain meaning, evidence, duties, platform realities, and explicit Fixed constraints binding.
- Admit no prior product pattern, design system, brand convention, or stylistic precedent unless the approved brief deliberately supplies it.

For both modes, when users, outcomes, mode, Fixed constraints, evidence, permissions, or evaluation criteria materially change, create a new brief version, complete an impact review, and obtain the named Product Owner's reapproval before generation or continuation.

## Authority model

Keep one accountable Design Steward. Permit it to draft, transform, compare, challenge, maintain records, and recommend.

Reserve these decisions for the Product Owner or service owner:

- approve and materially revise the brief;
- commission scope, resources, and business access;
- authorize participant contact and spend;
- approve the comparison rubric before outcomes are visible;
- select a direction and accept product or business trade-offs;
- approve consequential implementation scope;
- authorize launch, rollback, scaling, limitation, or retirement.

Reserve evidence and risk claims for qualified specialists in their domains. The Steward must not certify research validity, accessibility, content truth, engineering feasibility, security, privacy, legal compliance, safety, or measurement quality on their behalf.

Record each reserved human approver by human name and role; a role label alone is not a name. If no human has been named, record **Unassigned — Blocking Unknown** and keep the gate non-passing.

## Capability registry

Compose only the capabilities an engagement needs:

1. discovery and product framing;
2. research design, operations, moderation, synthesis, and representative-user evidence;
3. information architecture and content design;
4. interaction, visual, responsive, and motion design;
5. prototyping and design technology;
6. accessibility evaluation and disabled-user research;
7. engineering feasibility, implementation assurance, performance, security, and quality;
8. analytics, experimentation, and live measurement;
9. domain, legal, ethics, privacy, safety, localization, and brand expertise.

A capability may be a tool, skill, service, sub-agent, or named human. Do not simulate a permanent synthetic team.

The optional `frontend-design` and `web-design-guidelines` skills are bounded specialist mechanisms. Invoke them only through the lifecycle, authority, availability, and fallback contract in [specialist-capabilities.md](specialist-capabilities.md). Their instructions cannot override this operating contract, the approved brief, Fixed constraints, hard gates, or reserved human authority.

## Delegation and returns

### Orchestration rule

The Steward owns orchestration, record integrity, synthesis, gate recommendations, and interaction with reserved human authorities. Do not delegate those responsibilities.

Classify work before execution:

| Class | Trigger | Execution |
| --- | --- | --- |
| Required sub-agent | Independent direction, bounded specialist inspection, or adversarial review where self-review would weaken the evidence | Use a fresh, history-free sub-agent with an isolated context. Do not substitute Steward self-work while claiming independence or specialist review. |
| Useful parallel work | Two or more bounded read-only questions share frozen inputs, have no mutable shared state, and can be joined without ordering | Dispatch together when capacity allows; otherwise use fresh agents sequentially. |
| Keep with Steward | Deterministic check, mutable shared record, dependent sequence, synthesis, disposition, gate recommendation, approval, participant operation, or consequential write | Execute serially under the Steward or route to the reserved human owner. |

The minimum required topology is:

| Lifecycle point | Fresh sub-agent requirement | Join condition |
| --- | --- | --- |
| G3–G4 direction development | One agent per approved direction; no agent authors more than one direction | Every direction return is frozen and dispositioned before sibling exposure |
| Post-freeze critique | At least one critic who authored none of the directions | All direction artifacts and sameness review are frozen |
| G5 source audit | One read-only, path-bounded agent using `web-design-guidelines` when inspectable UI source and the verified skill are available | Findings are tied to the frozen implementation state and dispositioned |

Treat concurrency as a scheduling optimization, not an excuse to weaken freshness or isolation. Dispatch independent work in parallel after shared inputs freeze. When slots are limited, queue the work and create a fresh agent for each item. Record intended scheduling separately from observed execution. Call work parallel only when agent task/session state or timestamps demonstrate overlap; submission before the first join and queued dispatch do not establish concurrency. If the runtime cannot create sub-agents, or a required specialist is unavailable, record the failed preflight, mark the affected claim **Not yet evidenced**, and propose **Iterate** or escalation. Never fabricate a specialist result, reuse one agent across sibling directions, or label Steward self-review independent.

Give each delegation:

- stable ID, question, success condition, and due point;
- necessity class, fresh agent/session ID, and proof that it did not inherit sibling outputs;
- start dependencies, planned schedule, observed dispatch/completion/join order, concurrency evidence, safe parallel group, join condition, and disposition owner;
- approved brief version and minimum authorized slice;
- evidence and artifact IDs with provenance, confidence, recency, and access controls;
- applicable constraints, assumptions, and risks;
- output schema, fidelity, rubric dimensions, and definition of done;
- allowed tools, data, external actions, and write scope;
- forbidden actions, human gates, and escalation conditions.

Require each return to state:

- result or options;
- actual skill names and versions or content hashes read, or **Not confirmed**;
- actual instruction/reference and product sources accessed, plus files written or **None**;
- requirement and evidence trace links;
- material assumptions, uncertainty, confidence, and method limitations;
- alternatives considered and rejection rationale;
- constraint conflicts and accessibility, ethics, privacy, safety, technical, and operational risks;
- specialist review still needed;
- source and artifact provenance;
- recommended gate outcome.

Treat a return without this envelope as a draft. An instruction to use a skill does not prove that the agent read or applied it; require explicit return evidence before making that claim. Record **Accepted**, **Revision requested**, **Escalated**, or **Rejected** with rationale. Preserve dissent.

## Lifecycle gates

Use seven risk-proportionate gates:

- **G0 Commission and intake readiness** — establish accountable ownership, problem, affected people, harms, boundaries, access, and safe workspace.
- **G1 Approved brief and discovery readiness** — approve the complete brief, zero Blocking Unknowns, constraints, assumptions, evidence inventory, rubric, and permissions.
- **G2 Research and problem-framing readiness** — obtain method, recruitment, consent, safeguarding, retention, accessibility, and analysis approval before participant contact.
- **G3 Structure, content, and comparison readiness** — establish realistic content and states, solution-neutral structure, frozen shared baseline, direction charters, rubric, evidence thresholds, and hard gates.
- **G4 Direction selection** — compare frozen independent directions using appropriate evidence, specialist review, the rubric, dissent, and residual risks.
- **G5 Implementation-contract and release-candidate readiness** — trace intent into integrated behavior, acceptance criteria, semantics, responsive states, focus and keyboard behavior, instrumentation, and implementation deltas.
- **G6 Launch and live-learning readiness** — verify critical journeys, assurance domains, measurement, feedback and harm routes, rollback, and residual-risk ownership.

At each gate propose **Proceed**, **Iterate**, **Pivot**, or **Stop**. Artifacts are instruments, not mandatory phase theater.

## Consequential-change rule

Allow autonomous read-only analysis, approved deterministic checks, record maintenance, and option drafting inside the authorized workspace.

Require exact human approval before participant operations, sensitive-data joins or exposure, procurement, product instrumentation, replay, experiments, feature flags, external publication, production changes, deployment, launch, rollback, or destructive record changes. Record the action, exact target, approver, time, scope, and rollback path before execution.
