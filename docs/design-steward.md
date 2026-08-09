# Using Design Steward

Design Steward is an autonomous principal product designer for responsive websites and web applications. It first establishes original intent with the System Owner, then explores broadly, exposes visual thinking early, narrows through professional judgment, rejects generic work, and invests implementation effort only in concepts that survive.

Current package version: **4.0.0**.

Version 4.0 makes the composed `grilling` or `grill-me` skill a verified runtime dependency, introduces required `steward-state.json` recovery state, generates an owner-facing single-page roadmap from that state, and strengthens G5 with matched-state visual fidelity, selected-backbone coverage closure, non-implementing review, and separate engineering-source, design-integration, and preview/deployed acceptance claims.

Earlier records remain governed by the package version that created them. To migrate active work, preserve accepted records, create `steward-state.json` from the current decision path, record the resolved grilling dependency, migrate and revalidate the v4 Design Brief, obtain System Owner confirmation for any unrecoverable material decision, and repeat only affected gates.

## Install

Install the portable core:

```bash
npx --yes skills@1.5.16 add afoninsky/skills \
  --skill design-steward \
  --agent codex \
  --copy \
  --yes
```

Design-intent grilling composes a separately installed skill named `grilling` or `grill-me`. Before intake or workspace creation, Design Steward resolves the skill through the runtime registry and reads it completely. After that preflight passes, it creates the engagement workspace and records the dependency name and version/content hash before the first intake question. If neither skill is exposed and readable, Design Steward stops before intake instead of inventing a divergent decision-tree workflow.

Optional visual-design and UI-audit specialists can be installed in the same project:

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

Verify the optional specialists against the evaluated revisions:

```bash
python3 <skill-directory>/scripts/verify_specialists.py <project-root>
```

The portable core has no required MCP, browser, design framework, paid service, or proprietary runtime. It does require an installed and readable `grilling` or `grill-me` skill. Python 3.10 or newer is needed for Design Brief validation, specialist-integrity checks, and roadmap generation. A renderer is strongly preferred for screenshot-first review.

## Start in the correct operating mode

For new, ambiguous, or consequential work:

```text
$design-steward

Start a new responsive product commission. System Owner: <name and role>.
Use design-intent grilling to establish our shared understanding before
autonomous design. Do not begin the concept funnel until I confirm the brief.
```

Design Steward asks one neutral consequential question at a time. It waits for the System Owner's unaided answer, records that answer as owner-originated input, then gives its recommendation and reasoning, identifies evidence gaps and disagreements, and resolves the branch before continuing. Facts available through authorized tools or files are discovered rather than asked.

Routine typography, spacing, controls, navigation mechanics, layout, icon, and implementation choices remain Design Steward's professional responsibility unless they reveal a deeper unresolved product decision.

When a design-intent decision genuinely needs something visual, Design Steward creates no more than three disposable low-fidelity contrasts, captures the immediate reaction and reasoning, and returns to the unresolved question. Those contrasts are elicitation aids, not finalists.

## Confirm the Owner Design Brief

The engagement starter includes `owner-design-brief.md`. It records:

- commission and desired outcome;
- priority users, roles, and situations;
- product thesis, core user act, and first-ten-seconds hierarchy;
- desired experiential qualities;
- business priorities, constraints, non-negotiables, accepted trade-offs, and risk tolerance;
- unacceptable outcomes and rejection criteria;
- owner-originated preferences and Steward recommendations;
- material disagreements and resolutions;
- evidence, assumptions, unresolved uncertainty, and authorization boundaries;
- a decision-provenance table that keeps owner answers separate from Steward judgment.

Design Steward then asks:

> Does this brief represent our shared understanding, and may Design Steward enter autonomous design mode?

No autonomous concept generation begins until the named System Owner answers affirmatively. Silence, a validator pass, or a completed document is not approval.

A narrow change may skip grilling only when an existing confirmed Owner Design Brief resolves the relevant decision, no material objective, constraint, evidence, or risk changed, and the System Owner explicitly authorizes autonomous execution. The skip record must contain all three conditions and the reason.

## Create and validate the engagement workspace

Copy the starter outside the installed skill:

```bash
cp -R .agents/skills/design-steward/assets/engagement-starter \
  ./design-steward-engagement
```

Keep product context, approvals, evidence, and artifacts in that engagement workspace. The installed package remains immutable reference material.

The starter includes `steward-state.json`. Resolve it immediately after the grilling dependency preflight. It is the engagement recovery spine: every material decision, evidence disposition, artifact verdict, approval, gate result, implementation delta, and exact next action must appear there. After context compaction or a session handoff, read it completely before relying on conversation history.

After the Owner Design Brief is confirmed, normalize the detailed readiness contract into `design-brief.json` and run:

```bash
python3 .agents/skills/design-steward/scripts/validate_design_brief.py \
  ./design-steward-engagement/design-brief.json
```

The v4 validator requires:

- a verified and available `grilling` or `grill-me` dependency;
- operating mode `Autonomous design` and Evolution/From-scratch engagement type;
- completed composed grilling, or all three valid skip conditions;
- preserved owner-original decision records when grilling was completed;
- the canonical shared-understanding question, named confirmation, time, and authorized scope;
- owner intent, success contract, coverage, content, evidence, constraints, permissions, hard gates, and zero Blocking Unknowns;
- matching System Owner authority, confirmation, and approval records.

A successful result checks structure. Verify that confirmation is real before autonomous work.

## Generate the owner roadmap

At engagement completion, and whenever the System Owner asks to see the path taken, generate a self-contained roadmap from the canonical state:

```bash
python3 .agents/skills/design-steward/scripts/generate_engagement_roadmap.py \
  ./design-steward-engagement/steward-state.json \
  --output ./design-steward-engagement/steward-roadmap.html
```

The page opens with an infographic G0–G6 timeline. Every gate is labeled **Completed**, **In progress**, **Blocked**, or **Not done**, then shows its decision/result, evidence, outputs, and remaining closure condition. Supporting sections cover research and materials, material decisions and approvals, the concept funnel, mocks, selected direction, coverage, implementation fidelity, unresolved risks, and the exact next action. Regenerate it after later material decisions; do not maintain it separately from `steward-state.json`.

## Autonomous concept funnel

For substantial work, Design Steward uses:

**12–15 raw concepts → 6 territories → 3 developed directions → 1 backbone**

The stages control investment:

1. Raw concepts are one short paragraph each, materially different in thesis, core act, mental model, structure, interaction, or value proposition. They contain no code or detailed UI.
2. Six territories receive a promise, first-ten-seconds hierarchy, mental model, interaction grammar, content voice, and subject-grounded visual idea. Design Steward shows a matched six-up low-fidelity contact sheet early; these are not six prototypes.
3. Three territories survive into developed directions. Design Steward renders realistic representative frames, judges screenshots before rationale or code, and builds the core act plus immediate consequence only for Promising or Strong work.
4. One coherent backbone survives into responsive behavior, recovery, G4 evidence, and deeper implementation. Synthesis may import only compatible, evidenced elements and must be retested.

The first useful visual defaults to within 15 active minutes or 15% of the generation budget, and the six-territory contact sheet appears before 25%. Visual checkpoints are progress, not routine approval gates. After confirmation, Design Steward keeps making reversible design decisions autonomously.

A narrow commission may use a smaller funnel when Design Steward records why the default would add cost without changing the decision.

## Quality and evidence

Design Steward rejects work that fails product specificity, core-act clarity, first-ten-seconds hierarchy, interaction authorship, visual authorship, content voice, ecosystem coverage, responsive composition, or finish. It applies relabel, default-cluster, silhouette, core-act, first-ten-seconds, craft, and family-system counterfactuals to rendered output. Numeric self-scoring, polished rationale, traceability, state count, and code volume cannot rescue generic or under-resolved work.

Generated authors, specialists, and critics are E0 design judgment. Static guideline audits are E1 heuristic input. Representative-user or production evidence is required for scoped validation claims. Accessibility, content truth, privacy/participant welfare, ethical UX/safety, and provenance remain non-compensable hard gates.

## Delegation and specialist behavior

Design Steward owns raw concepts, six-territory formation, narrowing, synthesis, gate recommendations, and owner interaction. It does not create agents merely to increase idea count or simulate a design team.

When isolated authorship is materially important, it may use at most one fresh author per developed direction. When adversarial independence is materially important, it may add one non-author critic after freeze. Otherwise, Design Steward authors and judges the directions directly and makes no claim of independent authorship. A verified `frontend-design` specialist can be composed for bounded visual development; a fresh read-only `web-design-guidelines` specialist can inspect frozen authorized source at G5. Missing specialist work is never fabricated.

Routine retries and returns remain in one delegation ledger. The original author handles bounded revision. Routine G1 auditors, pairwise critics, remediation agents, and recheck agents are not defaults.

## Re-enter grilling only when needed

After autonomous design begins, Design Steward does not ask for routine approvals. It reopens only the affected decision branch when the System Owner changes objectives or material constraints, rejection reveals an unstated consequential preference, missing authority/information would materially alter the result, or a safety/privacy/accessibility/ethics/provenance/content-truth issue requires an owner decision.

The changed Owner Design Brief must be reconfirmed before dependent autonomous work resumes.

## Completion handoff

The handoff leads with the rendered backbone and decision. It includes the confirmed Owner Design Brief version and System Owner, representative product artifacts, screenshot-based quality verdict, funnel and experience-coverage result, evidence scope and hard-gate status, assumptions and dissent, residual-risk owners, the smallest supporting record links, and the exact next approval or specialist action.

Design Steward never contacts participants, spends money, publishes, changes production, deploys, launches, or rolls back without exact approval for the target action.
