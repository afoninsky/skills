# Design-intent grilling wrapper

Use this wrapper only in **Design-intent grilling** mode. It narrows the installed `grilling` or `grill-me` skill to consequential product and design-intent decisions; it does not replace or restate that skill's general one-question-at-a-time decision-tree workflow.

## Composition contract

The public `SKILL.md` package format does not provide portable nested-skill calls or dependency metadata. Compose the base skill through explicit runtime invocation:

1. Discover an installed skill named `grilling` or `grill-me` through the runtime's skill registry.
2. Read and follow that skill as the base interaction loop.
3. Apply this reference as the design-specific scope, provenance, visual-elicitation, and transition wrapper.
4. Record the resolved base skill name, version or content hash, verification time, and availability in `steward-state.json`, the Owner Design Brief, and `design-brief.json` before asking the first question.

In the first user-facing grilling response, name the resolved base skill once. Do not repeat this status on every turn.

Do not vendor, paraphrase, or evolve a private copy of the base decision-tree logic here. If neither base skill is available, report that composed grilling is unavailable and ask the System Owner to install or expose it. Do not silently substitute a new general interview workflow or enter autonomous design.

## Decision frontier

Start with consequential decisions whose answers constrain later branches:

1. commission and desired outcome;
2. priority users, roles, and situations;
3. product thesis and reason for existing;
4. behavior or transformation the product should enable;
5. first-ten-seconds hierarchy;
6. experiential qualities and intended emotional effect;
7. business priorities and material constraints;
8. acceptable trade-offs and risk tolerance;
9. non-negotiables and unacceptable outcomes;
10. rejection criteria and owner-specific taste reactions;
11. owner beliefs that remain unsupported;
12. authorization boundaries and stopping point.

Ask only decisions that remain open and consequential. Do not ask the System Owner for discoverable facts; use authorized workspace inspection, research, and tools. Do not grill typography, spacing, control styling, navigation mechanics, layout mechanics, icons, implementation details, or other routine professional decisions unless they expose an unresolved product decision.

## Preserve original owner judgment

For each material decision:

1. Ask one neutral question without revealing the Steward's answer.
2. Wait for the System Owner's unaided response.
3. Record its substance as owner-originated input without polishing it into the recommendation.
4. Give the Steward's recommended answer and reasoning.
5. Distinguish owner preference, evidence, assumption, and Steward inference.
6. Identify agreement, disagreement, evidence gaps, consequences, and any harmful or contradictory premise.
7. Resolve the decision or mark it unresolved before moving to a dependent question.

Challenge vague, contradictory, unsupported, or harmful answers. Agreement is a decision state, not proof. Never cite repeated owner agreement as user evidence or confidence calibration.

## Visual elicitation

Some owner judgments cannot be obtained verbally. When the same consequential question remains unresolved because it needs something visible:

- stop rephrasing the question;
- create the smallest disposable contrast that isolates the decision;
- show no more than three materially distinct visual or interaction alternatives;
- keep them low fidelity and clearly label them as elicitation aids;
- ask for the owner's immediate reaction and reasoning before recommending;
- record the reaction as owner-originated input and return to the unresolved decision.

Do not reuse an elicitation aid as a funnel finalist by default. It may enter the later raw-concept pool only after confirmation, where it competes on equal terms and receives no preference for having been shown during grilling. Do not build production code, a polished prototype, a design system, or a direction package during grilling.

## Owner Design Brief and transition

When the decision frontier is empty, complete the concise Owner Design Brief template. It must contain:

- commission and desired outcome;
- priority users, roles, and situations;
- product thesis and core user act;
- intended first-ten-seconds hierarchy;
- desired experiential qualities;
- business priorities and constraints;
- non-negotiables, accepted trade-offs, and unacceptable outcomes;
- rejection criteria;
- owner-originated preferences;
- Steward recommendations;
- material disagreements and resolutions;
- evidence, assumptions, and unresolved uncertainty;
- authorization boundaries.

Label owner preference as stakeholder input, not user, market, accessibility, technical, or production evidence. Preserve the original owner response and the Steward recommendation as separate fields in each consequential decision record.

Ask exactly:

> Does this brief represent our shared understanding, and may Design Steward enter autonomous design mode?

Remain in grilling mode until the named System Owner answers affirmatively. Record who confirmed, when, the brief version, and the exact scope authorized. A file status, validator pass, previous approval, or inferred consent cannot substitute.

## Bounded re-entry

After autonomous design begins, reopen only the branch affected by a material objective or constraint change, a rejection that reveals an unstated consequential preference, missing authority or information that would materially change the result, or a safety/privacy/accessibility/ethics/provenance/content-truth decision reserved for the owner.

Do not reopen resolved branches or ask for routine design approval. Supersede the Owner Design Brief only when the bounded pass changes shared understanding or authorization, then reconfirm before affected autonomous work resumes.
