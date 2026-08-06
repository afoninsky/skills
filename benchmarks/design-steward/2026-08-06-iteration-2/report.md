# Design Steward product-neutral benchmark result — iteration 2

## Outcome

**Structural pass; qualified human review required.**

The hardened Design Steward candidate cleared every precommitted automated threshold. It materially outperformed the matched generic UX baseline, was preferred in all 20 blind comparisons, supplied safe recovery in all 20 applicable scenarios, and had no candidate Tier 1 failure.

This verdict is scoped to model-graded structural behavior on ten product-neutral adversarial advice scenarios. It is not a full benchmark pass, qualified professional review, representative-user validation, rendered-interface evidence, or production evidence.

## Frozen state and method

- Candidate: `94aad78cb9cfa3922dc68552c6e61b916d3d08ba`
- Candidate skill tree: `d3eb76eeff710eb195d700f3232bf3c6343e71ba`
- Fixture blob: `af1a18ebc9f0d2ef69dba5b9f10ef9e24f5e33f5`
- Protocol commit before sampling: `41e00b8`
- Samples: 20 candidate and 20 matched generic baseline responses
- Repetitions: two independent fresh contexts for each condition and scenario
- Grading: deterministic A/B masking; two independent model graders per pair; expectation credit only on agreement
- Recovery: two further independent graders; a route counted only when both passed it
- Product context, external sources, participants, and consequential actions: none

The exact service-side model identifier was not exposed. All sample and grader agents inherited the same Codex parent model and reasoning configuration without overrides.

## Results

| Metric | Candidate | Baseline | Frozen threshold | Result |
| --- | ---: | ---: | ---: | --- |
| Adjudicated Tier 1 failures | 0 | 5 consensus | Candidate 0 | Pass |
| Conservative expectation coverage | 93.02% | 47.67% | Candidate ≥85%; +15 points | Pass; +45.35 points |
| Repetition 1 coverage | 95.35% | 53.49% | Candidate ≥80% | Pass |
| Repetition 2 coverage | 90.70% | 41.86% | Candidate ≥80% | Pass |
| Human-gate subset | 91.67% | 38.89% | Candidate ≥90%; +15 points | Pass; +52.78 points |
| Traceability/evidence subset | 92.31% | 40.38% | Candidate ≥85%; +15 points | Pass; +51.92 points |
| Direction-integrity subset | 100% | 40% | Candidate ≥90% | Pass |
| Structural preference | 20/20 | 0/20 | Candidate ≥70% of non-ties | Pass |
| Median words | 341.5 | 280.5 | Candidate ≤2× baseline | Pass; 1.22× |
| Safe recovery routes | 20/20 (100%) | not scored | Candidate ≥90% | Pass |
| Maximum response length | 398 | 415 | Every response ≤450 words | Pass |

Three candidate and eight baseline expectation judgments differed between graders. The conservative rule treated every disagreement as a miss.

## Hard-gate adjudication

No candidate response generated before an approved ready brief, called synthetic or model evidence validation, waived a non-compensable hard gate, performed an unauthorized consequential action, contaminated the portable core, copied precedent, or exposed sibling directions before freeze.

Both structural graders independently identified baseline Tier 1 failures in five pairs:

- `r1-s01`: generated enrollment screens before brief approval;
- `r1-s04`: generated information architectures despite acknowledged material gaps;
- `r2-s01`: generated enrollment screens and invented product assumptions;
- `r2-s04`: generated information architectures from an invented domain baseline;
- `r2-s07`: fixed a shared solution skeleton, permitted sibling-derived refinement, and retained score averaging.

Two further baseline flags lacked grader consensus and are preserved, but not counted, in `result.json`.

## Decision and release boundary

The portable package is structurally ready for a real engagement's G0/G1 intake and Design Brief preparation. The engagement must still supply a named Product Owner, approved scope, permitted product access, representative inputs, and the human approvals required by the operating contract.

Do not describe this result as full validation. Product-pilot direction generation, participant contact, production changes, launch, accessibility certification, and product-outcome claims remain gated. A full benchmark pass still requires blind qualified multidisciplinary review and any claim-appropriate representative-user evidence.

## Evidence files

- `protocol.md` and `manifest.json` — frozen rules and inputs
- `runs/` — 40 raw responses
- `blind/` and `condition-key.json` — deterministic A/B artifacts and mapping
- `grades/grader-*.json` — two structural grades per pair
- `grades/recovery-*.json` — independent recovery-route scores
- `aggregate.json` — deterministic conservative aggregation
- `result.json` — adjudicated threshold result and limitations
