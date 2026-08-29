# Operating contract

## Contents

- Design Brief schema
- Operating modes and grilling composition
- Unknowns and constraints
- Mode contract
- Authority model
- Capability registry
- Delegation and returns
- Lifecycle gates
- Consequential-change rule

## Design Brief schema

Require a versioned, System Owner-confirmed Owner Design Brief before direction generation. Normalize it into `design-brief.json` for deterministic readiness checks. Include:

1. explicit operating mode, Evolution/From-scratch engagement type, authority, objective, desired outcomes, and non-goals;
2. base grilling skill identity, whether grilling was completed or validly skipped, preserved owner-originated decision records, exact shared-understanding confirmation, and autonomous authorization;
3. product experience thesis, core user act, first-ten-seconds hierarchy, experiential qualities, complete experience scope, product idea to make obvious, professional quality bar, work budget, first-visible-artifact target, feedback checkpoints, preselection revision cap, deferred-assurance plan, rejection criteria, and stopping point;
4. target users, contexts, roles/domains, priority journeys, cross-boundary handoffs, and important exclusions;
5. evidence with source, recency, provenance, confidence, and access class;
6. representative content, canonical terminology, data conditions, and critical edge, error, and empty states;
7. accessibility, inclusion, ethical, privacy, legal, and safety constraints;
8. constraint ledger plus technical, operational, platform, budget, timing, localization, and asset-rights constraints;
9. precommitted professional-quality criteria, comparison rubric, baselines, evidence thresholds, numeric-scoring policy, and validation claim rule;
10. decision owners, human gates, participant-contact authority, permitted tools, data, sources, and product access;
11. change-control and clean-room boundaries.

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

## Operating modes and grilling composition

Resolve and read an installed `grilling` or `grill-me` skill before intake or workspace creation. After the preflight passes, create the engagement workspace and record the resolved name, version or content hash, verification time, and `Available` status in `steward-state.json`, the Owner Design Brief, and `design-brief.json` before the first intake question. If neither skill is exposed and readable, stop before intake; the missing dependency is a Blocking Unknown, not permission to improvise the base workflow.

Start in **Design-intent grilling** for new, ambiguous, or consequential work. Use the resolved skill as the base decision-tree interaction and apply [design-intent-grilling.md](design-intent-grilling.md) as the wrapper. The portable skill format has no supported nested-dependency metadata, so composition is an explicit name-based invocation. Do not copy the base skill's general logic into this package.

Enter **Autonomous design** only after the System Owner confirms the Owner Design Brief. A narrow change may skip grilling only when an existing confirmed brief resolves the decision, no material objective/constraint/evidence/risk changed, and the System Owner explicitly authorizes autonomy; record all three conditions.

Do not ask routine professional design questions in grilling. After autonomy starts, reopen only the affected consequential decision branch and reconfirm the brief before dependent work resumes.

## Engagement type contract

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

For both engagement types, when users, outcomes, engagement type, Fixed constraints, evidence, permissions, or evaluation criteria materially change, create a new brief version, complete an impact review, and obtain the named System Owner's reapproval before generation or continuation.

## Authority model

Keep one accountable Design Steward. Permit it to draft, transform, compare, challenge, maintain records, and recommend.

Reserve these decisions for the System Owner or service owner:

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

The composed `grilling` or `grill-me` skill is the required base interaction for design-intent grilling. The optional `frontend-design` and `web-design-guidelines` skills are bounded specialist mechanisms. Invoke all of them only through the lifecycle, authority, availability, and fallback contracts in [design-intent-grilling.md](design-intent-grilling.md) and [specialist-capabilities.md](specialist-capabilities.md). Their instructions cannot override this operating contract, the confirmed brief, Fixed constraints, hard gates, or reserved human authority.

## Delegation and returns

### Orchestration rule

The Steward owns orchestration, record integrity, synthesis, gate recommendations, and interaction with reserved human authorities. Do not delegate those responsibilities.

Classify work before execution:

| Class | Trigger | Execution |
| --- | --- | --- |
| Required sub-agent | A bounded specialist inspection or a commission/benchmark that explicitly requires independent authorship or adversarial review | Use a fresh, history-free sub-agent with an isolated context. Do not substitute Steward self-work while claiming independence or specialist review. |
| Useful parallel work | Two or more bounded read-only questions share frozen inputs, have no mutable shared state, and can be joined without ordering | Dispatch together when capacity allows; otherwise use fresh agents sequentially. |
| Keep with Steward | Deterministic check, mutable shared record, dependent sequence, synthesis, disposition, gate recommendation, approval, participant operation, or consequential write | Execute serially under the Steward or route to the reserved human owner. |

Raw concepts, six-territory formation, narrowing, synthesis, and gate decisions remain with the Steward. Do not delegate to increase concept count or simulate a design team. The maximum justified preselection topology is one isolated author per developed direction plus one critic who authored none of them, and only when a named risk makes independence material. Do not create an independent G1 auditor, pairwise critics, remediation agents, or deterministic recheck agents by default.

The minimum required topology is:

| Lifecycle point | Fresh sub-agent requirement | Join condition |
| --- | --- | --- |
| G3–G4 direction development | Optional: one agent per developed direction when isolated authorship is decision-relevant; no agent authors more than one direction | Every delegated direction return is frozen and dispositioned before sibling exposure |
| Post-freeze critique | Optional: one critic who authored none of the directions when adversarial independence is decision-relevant | All direction artifacts and their screenshot contact sheet are frozen |
| G5 source audit | One read-only, path-bounded agent using `web-design-guidelines` when inspectable UI source and the verified skill are available | Findings are tied to the frozen implementation state and dispositioned |

Treat concurrency as a scheduling optimization, not a quality strategy. Dispatch justified independent work in parallel only after inputs freeze. Record intended scheduling separately from observed execution and call work parallel only when task state or timestamps prove overlap. If a specifically required independent author or specialist is unavailable, record the limitation and mark only the affected independence or specialist claim **Not yet evidenced**; continue unrelated Steward-owned funnel work when safe. Never fabricate a specialist result, reuse one agent across sibling directions, or label Steward self-review independent.

Use one living delegation ledger for routine direction authoring, research, critique, and bounded revisions. Add a concise row or section for each dispatch and return. Create a standalone packet only when sensitivity, complexity, external handoff, or consequential authority makes it materially safer. Keep a direction's original isolated author for revisions; do not create a fresh sub-agent for every remediation or recheck.

Give each delegation:

- stable ID, question, success condition, and due point;
- necessity class, fresh agent/session ID, and proof that it did not inherit sibling outputs;
- start dependencies, planned schedule, observed dispatch/completion/join order, concurrency evidence, safe parallel group, join condition, and disposition owner;
- approved brief version and minimum authorized slice;
- evidence and artifact IDs with provenance, confidence, recency, and access controls;
- applicable constraints, assumptions, and risks;
- output schema, fidelity, rubric dimensions, and definition of done;
- first-visible-artifact target, current fidelity, preselection revision cap, checks required now, and checks explicitly deferred until promotion;
- allowed tools, data, external actions, and write scope;
- forbidden actions, human gates, and escalation conditions.

Require each return to state:

- result or options;
- actual skill names and versions or content hashes read, or **Not confirmed**;
- actual instruction/reference and product sources accessed, plus files written or **None**;
- requirement, coverage, quality-criterion, and evidence trace links;
- material assumptions, uncertainty, confidence, and method limitations;
- alternatives considered and rejection rationale;
- constraint conflicts and accessibility, ethics, privacy, safety, technical, and operational risks;
- specialist review still needed;
- source and artifact provenance;
- direct visible checkpoint, current fidelity, revision-loop count, checks run now, checks deferred, and the decision gained from the return;
- recommended gate outcome.

Treat a return without the material parts of this envelope as a draft. An instruction to use a skill does not prove that the agent read or applied it; require explicit return evidence before making that claim. Record **Accepted**, **Revision requested**, **Escalated**, or **Rejected** with rationale. Preserve dissent. Do not turn every return, retry, or deterministic recheck into a separate file when the living ledger and artifact manifest preserve the evidence.

## Lifecycle gates

Use seven risk-proportionate gates:

- **G0 Commission and intake readiness** — establish accountable ownership, problem, affected people, harms, boundaries, access, and safe workspace.
- **G1 Confirmed brief and discovery readiness** — confirm the Owner Design Brief and autonomous authorization, zero Blocking Unknowns, constraints, assumptions, evidence inventory, rejection criteria, rubric, and permissions.
- **G2 Research and problem-framing readiness** — obtain method, recruitment, consent, safeguarding, retention, accessibility, and analysis approval before participant contact.
- **G3 Structure, content, quality, and funnel readiness** — establish realistic content and states, solution-neutral structure, experience coverage, professional-quality criteria, frozen baseline, six distinct territory definitions, rubric, evidence thresholds, budget, first-visible target, feedback checkpoints, revision cap, fidelity-aware assurance plan, and hard gates.
- **G4 Direction selection** — admit only directions that pass screenshot-first professional quality, then compare frozen independent survivors using appropriate evidence, specialist review, the rubric, dissent, and residual risks.
- **G5 Implementation-contract and release-candidate readiness** — trace intent into integrated behavior, acceptance criteria, semantics, responsive states, focus and keyboard behavior, instrumentation, and implementation deltas.
- **G6 Launch and live-learning readiness** — verify critical journeys, assurance domains, measurement, feedback and harm routes, rollback, and residual-risk ownership.

At each gate propose **Proceed**, **Iterate**, **Pivot**, or **Stop**. Artifacts are instruments, not mandatory phase theater.

## Consequential-change rule

Allow autonomous read-only analysis, approved deterministic checks, record maintenance, and option drafting inside the authorized workspace.

Require exact human approval before participant operations, sensitive-data joins or exposure, procurement, product instrumentation, replay, experiments, feature flags, external publication, production changes, deployment, launch, rollback, or destructive record changes. Record the action, exact target, approver, time, scope, and rollback path before execution.

## Recovery-state contract

Maintain `steward-state.json` as the canonical current recovery spine from engagement creation through handoff. Every material decision, evidence disposition, constraint change, artifact verdict, approval, gate result, implementation delta, and exact next action must appear there even when a detailed immutable record also exists.

On context compaction, session transfer, or resumed work, read the state file completely before relying on a conversation summary. Reconcile it with changes newer than its timestamp and stop consequential work when authority, artifact identity, or the next action cannot be recovered confidently. Generate the owner roadmap only from this file so the visual history cannot drift into a second manually maintained narrative.
