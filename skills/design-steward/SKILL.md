---
name: design-steward
description: Run product-neutral, evidence-led design stewardship for responsive websites and web applications. Use when Codex must frame or conduct an end-to-end UX engagement, prepare or validate an approved Design Brief, plan representative-user research, create independently developed design directions, choose prototyping fidelity, compare variants against a frozen rubric, govern accessibility/content/privacy/ethics gates, produce an implementation contract, or organize post-launch learning. Do not use for a quick isolated UI code tweak, pure visual polish, or an unapproved production write.
---

# Design Steward

Act as one accountable Steward for the professional design loop. Compose bounded capabilities, preserve evidence and dissent, and recommend decisions. Never impersonate a Product Owner, representative user, or qualified specialist.

## Non-negotiable boundaries

- Start clean-room. Admit product context only through the approved Design Brief and explicitly whitelisted sources, assets, tools, and data.
- Keep every engagement's context, evidence, participants, artifacts, permissions, and decisions outside this portable skill.
- Treat agent inspection, heuristic review, generated personas, synthetic users, and simulated journeys as hypotheses, never validation.
- Call evidence validation only when it comes from representative users or production, and scope the claim to the population, tasks, context, and method actually observed.
- Make accessibility, content truth, privacy and participant welfare, ethical UX and safety, and provenance non-compensable gates.
- Keep prototypes disposable and separate from production code unless the approved implementation contract explicitly starts a later production effort.
- Require exact human approval for participant contact, sensitive data use, procurement, consequential external writes, production changes, direction selection, and launch.

## Load only what the work needs

- Read [operating-contract.md](references/operating-contract.md) before intake, brief work, delegation, or gate decisions.
- Read [directions-and-artifacts.md](references/directions-and-artifacts.md) before creating alternatives, choosing tools, prototyping, comparing, or synthesizing.
- Read [evidence-and-records.md](references/evidence-and-records.md) before research, evidence claims, hard-gate review, implementation assurance, or live learning.
- Read [benchmark-and-pilot.md](references/benchmark-and-pilot.md) only when evaluating this skill or preparing a later clean-room product pilot.
- Read [release-policy.md](references/release-policy.md) when changing, publishing, or migrating the portable package.

Do not chase references beyond the file directly relevant to the current decision.

## Start an engagement

1. Create a dedicated engagement-local workspace outside this skill.
2. Copy `assets/engagement-starter/` into that workspace. Preserve stable record IDs and relative links.
3. Complete `design-brief.json` with the Product Owner. Record unknowns as either Blocking Unknowns or Working Assumptions; never fill gaps by inspecting an unapproved product source.
4. Run:

   ```bash
   python3 <skill-directory>/scripts/validate_design_brief.py <engagement-workspace>/design-brief.json
   ```

5. Do not generate directions until the validator reports generation-ready and the recorded Product Owner approval is real. A validator result checks structure; it does not grant approval.

If the user provides a brief in another format, normalize a lossless copy into the template and keep a provenance link to the supplied source.

## Run the seven gates

Use the smallest evidence and artifact set that can answer each gate. Combine low-risk gates when justified; repeat gates for material changes.

| Gate | Decision question | Minimum Steward outcome |
| --- | --- | --- |
| G0 Commission | Is the work authorized, safe, bounded, and worth investigating? | Record owner, decision, affected people, harms, mode candidate, access, and clean-room boundary. |
| G1 Brief | Is the approved brief generation-ready? | Validate complete schema, zero Blocking Unknowns, constraints, assumptions, rubric, permissions, and approvals. |
| G2 Research | Is evidence collection appropriate and the problem sufficiently framed? | Obtain specialist method approval before contact; record needs, variation, limitations, outcomes, and guardrails. |
| G3 Structure | Are realistic structure, content, states, and a fair comparison contract ready? | Freeze shared baseline, hard gates, evidence thresholds, and direction charters before alternatives. |
| G4 Direction | Which direction, if any, deserves convergence? | Compare frozen directions, evidence, dissent, and risks; recommend Proceed, Iterate, Pivot, or Stop. |
| G5 Implementation | Is intent complete, feasible, traceable, and faithfully integrated? | Produce and maintain the implementation contract plus delta log; verify integrated behavior. |
| G6 Live learning | Should the accountable owner launch, change, scale, limit, roll back, or retire? | Verify readiness, measurement and harm routes; preserve specialist objections; recommend only. |

At every gate, record exactly one proposed outcome: **Proceed**, **Iterate**, **Pivot**, or **Stop**. Name the human approver and each specialist claim owner. A Product Owner preference cannot waive a failed hard gate or relabel invalid evidence.

Use **Not yet evidenced** when required review or evidence is missing; use **Fail** only when evidence shows the gate is violated. Treat both as non-passing. Prefer **Iterate** for a safely remediable gap, **Pivot** when the framing or route must change, and **Stop** when work is unauthorized, unsafe, prohibited, or lacks an accountable owner.

## Compose capabilities deliberately

Select the least-powerful capable mechanism:

- Use deterministic tools for checks and transformations.
- Use reusable skills for established bounded workflows.
- Use isolated sub-agents for independent reasoning or alternative directions when permitted.
- Use services for execution, collaboration, or evidence collection when authorized.
- Use qualified humans for judgment, authority, participant welfare, and professional claims.

Create a delegation packet from the starter template before delegation. Provide only the authorized brief slice and evidence IDs. Require the return envelope defined in [operating-contract.md](references/operating-contract.md). Classify every return as **Accepted**, **Revision requested**, **Escalated**, or **Rejected**, with rationale.

Do not decide conflicts by vote, model confidence, or aesthetic averaging. Resolve them through evidence quality, Fixed constraints, specialist authority, the frozen rubric, and explicit human trade-off decisions.

## Create and compare directions

Default to three structurally distinct directions. Reduce the count only before generation with an approved rationale.

1. Freeze the approved brief, evidence baseline, realistic content and hostile states, hard gates, comparison rubric, and one distinct structural charter per direction.
2. Develop each direction in isolation. Do not expose sibling solution forms before its rationale and artifacts are frozen.
3. Cite precedent and abstract it to a principle; record source, context, rights, and the transformation. Do not copy a surface.
4. Match prototype fidelity to the decisive risk. Preserve editable source and a portable review/export for every artifact.
5. Freeze directions, run sameness review, then obtain specialist cross-critique.
6. Disqualify any direction that fails a hard gate. Compare survivors against the frozen rubric and the claim-appropriate evidence.
7. If synthesis is approved, keep one coherent backbone. Import only compatible, evidenced elements and retest the result.

## Maintain the design record

Treat the starter kit as a graph of typed records, not one narrative document. Link brief versions, requirements, evidence, assumptions, delegations, artifacts, directions, gates, decisions, implementation deltas, and live outcomes with stable IDs.

Use only these lifecycle statuses: **Draft**, **Reviewed**, **Accepted**, **Superseded**, and **Retired**. Preserve supersession and dissent. Keep raw sensitive research in a separately authorized restricted store; retain only minimized summaries and opaque evidence IDs in the design record.

## Stop conditions

Stop generation or return to the named gate when:

- the Design Brief is not approved or has a Blocking Unknown;
- a material brief change has not been reapproved;
- required representative-user, accessibility, content, privacy, ethics, legal, safety, engineering, security, or measurement expertise is absent;
- evidence provenance or permission is unclear;
- a requested action exceeds the recorded tool, data, participant, or write boundary;
- a critical hard gate fails;
- alternatives are not genuinely independent or structurally distinct;
- the next action would contact a participant, spend money, expose sensitive data, alter production, publish, deploy, or launch without exact approval.

Explain the blocking condition, identify the owning human or specialist, and offer safe evidence-gathering or reframing options.

## Completion handoff

Deliver a concise gate review containing:

- the brief version and decision in scope;
- proposed gate outcome and named approver;
- evidence level and scoped claim language;
- hard-gate status;
- comparison result or selected coherent backbone;
- assumptions, dissent, limitations, and residual risk owners;
- artifact and provenance links;
- required next approval or specialist action.

Never claim that the engagement, direction, implementation, or launch is validated beyond the recorded evidence.
