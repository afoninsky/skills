# Design Steward product-neutral benchmark protocol

## Status and boundary

Precommitted before sampling on 2026-08-06. This run evaluates the frozen portable package at commit `fca00ad2c3e25be38169f5ab03913ddf9c7e6ae1`. It does not inspect a product, contact participants, make external product changes, or run the clean-room product pilot.

Model graders provide structural assistance for Tiers 1–3 and Tier 5 only. They cannot supply qualified professional review or representative-user evidence. The strongest possible verdict from this automated run is **structural benchmark passed; qualified human review required**.

## Frozen inputs

- Candidate commit: `fca00ad2c3e25be38169f5ab03913ddf9c7e6ae1`
- Candidate skill tree: `f1a7359de1e2e342f1c01a2f1ae50bc2e30ae7b4`
- Fixture blob: `af1a18ebc9f0d2ef69dba5b9f10ef9e24f5e33f5`
- Scenarios: the ten fixtures in `skills/design-steward/evals/benchmark.json`
- Conditions: Design Steward candidate and matched generic UX baseline
- Repetitions: two independent fresh contexts per condition and scenario
- Total raw samples: 40
- Output budget: at most 450 words, one response, no follow-up turn
- Product, participant, proprietary, or external source access: none
- External actions: none

## Matched conditions

Use the same inherited Codex model, reasoning configuration, output budget, scenario text, workspace permissions, and lack of product context for both conditions. Do not override the model or reasoning effort.

### Candidate prompt wrapper

> Use `$design-steward` at `skills/design-steward/SKILL.md` to answer the user request below. Read only that skill and the directly routed reference needed for this request. Do not inspect evaluation fixtures, sibling outputs, product repositories, or unrelated files. Return only the response to the user, at most 450 words. Write that response to the assigned output file and make no other changes.

### Generic baseline prompt wrapper

> Act as a capable senior UX and product-design advisor. Use sound professional judgment to answer the user request below. Do not inspect specialized skills, evaluation fixtures, sibling outputs, product repositories, or unrelated files. Return only the response to the user, at most 450 words. Write that response to the assigned output file and make no other changes.

Run every sample in a fresh sub-agent without conversation history. A run may see its wrapper and scenario only. It must not see expected outputs, expectations, condition siblings, or prior runs.

## Blind grading

After all outputs exist, generate deterministic A/B pairs using SHA-256 of `design-steward-2026-08-06|repetition|scenario`. Keep the condition key away from graders. Give each pair to two independent fresh model graders. Each grader records:

- pass/fail for every frozen expectation;
- any Tier 1 violation and its evidence;
- response word count;
- structural preference: A, B, or tie;
- concise rationale and uncertainty.

Resolve expectation coverage conservatively: an expectation passes only when both graders mark it true. Count a Tier 1 failure when either grader identifies a concrete violation, then adjudicate that evidence against the raw output before reporting. Record grader disagreement rather than averaging it away.

## Precommitted thresholds

### Tier 1 — hard gates

- Candidate: zero adjudicated Tier 1 failures across all 20 samples.
- Regression rule: candidate may not fail a hard gate that the paired generic baseline passes.

### Tier 2/3 — protocol and direction quality

- Candidate conservative expectation coverage: at least 85% overall.
- Repeatability: at least 80% candidate coverage in each repetition.
- Material improvement: candidate overall coverage at least 15 percentage points above the generic baseline.
- Human-gate subset (scenarios 1, 5, 9, 10): candidate at least 90% and at least 15 points above baseline.
- Traceability/evidence subset (scenarios 1, 2, 4, 6, 9, 10): candidate at least 85% and at least 15 points above baseline.
- Direction-integrity subset (scenario 7): candidate at least 90%, with no copying, sibling-exposure, voting, averaging, or collage violation.
- Structural preference: candidate preferred in at least 70% of pairs that are not grader ties.

### Tier 5 — efficiency and recoverability

- Every response stays within 450 words.
- Candidate median word count is no more than 2.0 times the baseline median.
- Candidate provides a safe next action or recovery route in at least 90% of scenarios where the requested action must be refused or reframed.

## Verdict rules

- **Structural fail:** any candidate Tier 1 failure or any precommitted Tier 2/3/5 threshold fails.
- **Structural pass; qualified human review required:** every automated threshold passes, raw outputs and variance are preserved, and no claim exceeds the model-graded conditions.
- **Full benchmark pass:** unavailable in this run. It additionally requires blind qualified multidisciplinary review of the frozen outputs and any claim-appropriate representative-user task evidence. A later human review must use the same frozen candidate, fixtures, rubric, raw samples, and condition masking.

Do not start the product pilot from a structural pass alone.
