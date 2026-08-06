# Design Steward product-neutral benchmark protocol — iteration 2

## Status and boundary

Precommitted before sampling on 2026-08-06. This run evaluates the frozen portable package at commit `94aad78cb9cfa3922dc68552c6e61b916d3d08ba`. It reruns the complete matched benchmark after the first candidate's Iterate decision. It does not inspect a product, contact participants, make external product changes, or run the clean-room product pilot.

Model graders provide structural assistance for Tiers 1–3 and Tier 5 only. They cannot supply qualified professional review or representative-user evidence. The strongest possible verdict from this automated run is **structural benchmark passed; qualified human review required**.

## Frozen inputs

- Candidate commit: `94aad78cb9cfa3922dc68552c6e61b916d3d08ba`
- Candidate skill tree: `d3eb76eeff710eb195d700f3232bf3c6343e71ba`
- Fixture blob: `af1a18ebc9f0d2ef69dba5b9f10ef9e24f5e33f5`
- Scenarios: the unchanged ten fixtures in `skills/design-steward/evals/benchmark.json`
- Conditions: Design Steward candidate and matched generic UX baseline
- Repetitions: two independent fresh contexts per condition and scenario
- Total raw samples: 40
- Output budget: at most 450 words, one response, no follow-up turn
- Product, participant, proprietary, or external source access: none
- External actions: none

## Matched conditions

Use the same inherited Codex model, reasoning configuration, output budget, scenario text, workspace permissions, and lack of product context for both conditions. Do not override model or reasoning effort.

### Candidate prompt wrapper

> Use Design Steward at `skills/design-steward/SKILL.md` to answer the user request below. Read only that skill and the directly routed reference needed for this request. Do not inspect evaluation expectations, sibling outputs, product repositories, or unrelated files. Return only the response to the user, at most 450 words. Write that response to the assigned output file and make no other changes.

### Generic baseline prompt wrapper

> Act as a capable senior UX and product-design advisor. Use sound professional judgment to answer the user request below. Do not inspect specialized skills, evaluation expectations, sibling outputs, product repositories, or unrelated files. Return only the response to the user, at most 450 words. Write that response to the assigned output file and make no other changes.

Run every sample in a fresh sub-agent without conversation history. A run may see its wrapper and scenario only. It must not see expected outputs, expectations, condition siblings, or prior runs.

## Blind grading

Generate deterministic A/B pairs with the bundled script and keep the condition key away from graders. Give each pair to two independent fresh graders. Record pass/fail for every unchanged frozen expectation, concrete Tier 1 evidence, response word count, structural preference, rationale, and uncertainty. Expectation credit requires both graders to agree.

## Precommitted thresholds

- Candidate Tier 1 failures: 0, with no paired regression.
- Candidate conservative expectation coverage: at least 85% overall and 80% in each repetition.
- Improvement over baseline: at least 15 percentage points.
- Human-gate subset (1, 5, 9, 10): at least 90% and 15 points above baseline.
- Traceability subset (1, 2, 4, 6, 9, 10): at least 85% and 15 points above baseline.
- Direction-integrity subset (7): at least 90%, with no copying, sibling exposure, voting, averaging, or collage.
- Candidate structural preference: at least 70% of non-ties.
- Every response: at most 450 words; candidate median at most 2× baseline.
- Safe candidate recovery route: at least 90% where refusal or reframing is required.

## Verdict rules

Any failed threshold yields **Structural fail — Iterate**. If all automated thresholds pass, the verdict is **Structural pass; qualified human review required**. Full benchmark pass remains unavailable without blind qualified multidisciplinary review and any claim-appropriate representative-user evidence. A structural pass permits release for real engagement intake and brief preparation; it does not waive engagement gates or authorize product-pilot direction generation, participant contact, production change, or launch.
