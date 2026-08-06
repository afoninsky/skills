# Using Design Steward

Design Steward runs a product-neutral, evidence-led design engagement for responsive websites and web applications. It helps frame the work, prepare an approved Design Brief, develop and compare independent directions, govern hard gates, create an implementation contract, and plan live learning. It recommends decisions; accountable humans approve them.

Current package version: **1.0.0**.

## Install

Install the portable core:

```bash
npx --yes skills@1.5.16 add afoninsky/skills \
  --skill design-steward \
  --agent codex \
  --copy \
  --yes
```

Install the optional visual-design and UI-audit specialists in the same project:

```bash
npx --yes skills@1.5.16 add anthropics/skills \
  --skill frontend-design \
  --agent codex \
  --copy \
  --yes

npx --yes skills@1.5.16 add vercel-labs/agent-skills \
  --skill web-design-guidelines \
  --agent codex \
  --copy \
  --yes
```

Verify that the installed companions match the revisions evaluated with this release:

```bash
python3 <skill-directory>/scripts/verify_specialists.py <project-root>
```

Stop if verification reports a missing skill or hash mismatch. Review and update provenance through a new Design Steward release instead of silently accepting upstream drift.

The core has no required MCP, browser, design framework, paid service, or runtime dependency. Python 3.10 or newer is needed only for the optional Design Brief and specialist-integrity validators. The UI-audit specialist needs network access to retrieve its current canonical rules; when that source cannot be verified, the Steward records the audit as unavailable instead of fabricating a result.

## Start an engagement

Invoke the skill explicitly and name the decision you need:

```text
$design-steward

Start a clean-room Evolution engagement for a responsive web application.
Help me prepare the Design Brief and stop before direction generation until
the Product Owner has approved it.
```

For a new product, choose From-scratch mode:

```text
$design-steward

Start a clean-room From-scratch engagement. Use only the context admitted
through the approved Design Brief. Prepare three structurally distinct
directions after the brief is generation-ready.
```

Create an engagement-local workspace outside the installed skill. Copy `assets/engagement-starter/` from the installed Design Steward directory into it. Complete `design-brief.json`; record missing material facts as Blocking Unknowns and safe temporary beliefs as Working Assumptions.

Use the starter requirement and evidence registers to assign immutable IDs before implementation handoff. Link every material claim and G5 contract row to requirement, evidence, and applicable assumption IDs; supersede accepted records instead of rewriting them.

Validate the structure:

```bash
python3 <skill-directory>/scripts/validate_design_brief.py \
  <engagement-workspace>/design-brief.json
```

A successful validator result does not create approval. The named Product Owner must approve the recorded brief, and direction generation requires zero Blocking Unknowns.

## What to provide

The approved Design Brief should identify:

- decision owner, objective, desired outcomes, and non-goals;
- target users, contexts, priority journeys, and exclusions;
- evidence, provenance, confidence, recency, and access class;
- representative content, canonical terminology, data conditions, and critical states;
- accessibility, content-truth, privacy, ethics, legal, safety, and inclusion constraints;
- Evolution or From-scratch mode and the constraint ledger;
- technical, operational, platform, budget, timing, localization, and asset-rights constraints;
- the comparison rubric, baselines, evidence thresholds, permissions, and human gates.

Do not give the Steward general permission to inspect a product repository, analytics, prior design system, brand book, or conversation history. Admit only the minimum approved sources needed for the current gate.

## Lifecycle

Design Steward uses seven gates:

1. G0 Commission: authorize and bound the engagement.
2. G1 Brief: approve a complete generation-ready brief.
3. G2 Research: approve methods and participant safeguards.
4. G3 Structure: freeze content, states, hard gates, rubric, and distinct direction charters.
5. G4 Direction: compare frozen directions and recommend Proceed, Iterate, Pivot, or Stop.
6. G5 Implementation: trace intent into integrated behavior and disposition source-scoped UI-audit findings.
7. G6 Live learning: verify measurement, harm routes, rollback, and residual-risk ownership.

At every gate, the Steward preserves evidence scope, assumptions, dissent, limitations, and the next human or specialist approval. **Fail** means evidence demonstrates a violation. **Not yet evidenced** means required assurance is absent. Neither passes.

Material changes to users, outcomes, mode, Fixed constraints, evidence, permissions, or evaluation criteria require an impact review, a new brief version, and Product Owner reapproval before affected work resumes.

## Specialist behavior

After G1 approval and G3 readiness, the Steward may give each direction to a fresh isolated `frontend-design` sub-agent. The specialist receives only that direction's authorized brief slice and may not invent users, content, brand rules, or product context. Its visual choices must trace to the brief, evidence, or explicitly Open axes.

At G5, the Steward may give a frozen, authorized file set to a fresh read-only `web-design-guidelines` sub-agent. Findings are E1 heuristic input tied to exact files, lines, implementation state, and a recorded guideline revision/hash. The audit is not user validation, accessibility certification, browser assurance, engineering approval, or ship approval.

The Steward's boundaries and hard gates, the approved brief and Fixed constraints, and reserved human authority always outrank specialist guidance.

## Expected handoff

A useful handoff includes:

- brief version and decision in scope;
- proposed gate outcome and named approver;
- evidence level and scoped claim language;
- hard-gate status;
- comparison result or selected coherent backbone;
- assumptions, dissent, limitations, and residual-risk owners;
- artifact, implementation, audit, and provenance links;
- the exact next approval or specialist action.

The Steward does not contact participants, spend money, publish, modify production, deploy, launch, or roll back without exact approval for the target action.

## First real-battle test

After the release's structural benchmark and integrity checks pass, start with one bounded journey and one named, accountable Product Owner. The released Steward is ready to accept real G0/G1 intake: keep the engagement local, choose Evolution or From-scratch explicitly, and admit context only through the approved brief.

Readiness to take an engagement is not blanket approval to generate, ship, or claim validation. Before direction generation or comparison, satisfy the brief, evidence, specialist, and human gates in the engagement and the pilot eligibility rule in `references/benchmark-and-pilot.md`. Stop the first engagement at an implementation contract; use the records to verify the workflow before authorizing participant contact, a production change, or launch.
