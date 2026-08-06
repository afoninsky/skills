# Design Steward product-neutral benchmark result

## Outcome

**Structural benchmark: Fail — Iterate.**

The frozen Design Steward candidate materially outperformed the matched generic UX baseline and had no Tier 1 failures, but it missed three precommitted coverage thresholds. The clean-room product pilot must not start from this candidate.

This result is scoped to model-graded structural behavior on ten product-neutral adversarial advice scenarios. It is not qualified professional review, representative-user validation, or production evidence.

## Frozen state and method

- Candidate: `fca00ad2c3e25be38169f5ab03913ddf9c7e6ae1`
- Candidate skill tree: `f1a7359de1e2e342f1c01a2f1ae50bc2e30ae7b4`
- Fixture blob: `af1a18ebc9f0d2ef69dba5b9f10ef9e24f5e33f5`
- Protocol commit before sampling: `573d7ef6e55c33c680b74e7792b6975d6f804c34`
- Samples: 20 candidate and 20 matched generic baseline responses
- Repetitions: two independent fresh contexts for each condition and scenario
- Grading: deterministic A/B masking; two independent model graders per pair; expectation credit only on agreement
- Product context, external sources, participants, and consequential actions: none

The exact service-side model identifier was not exposed. All sample agents inherited the same Codex parent model and reasoning configuration without overrides.

## Results

| Metric | Candidate | Baseline | Frozen threshold | Result |
| --- | ---: | ---: | ---: | --- |
| Adjudicated Tier 1 failures | 0 | 4 | Candidate 0 | Pass |
| Conservative expectation coverage | 84.88% | 48.84% | Candidate ≥85%; +15 points | **Fail absolute; +36.05 points pass** |
| Repetition 1 coverage | 86.05% | 46.51% | Candidate ≥80% | Pass |
| Repetition 2 coverage | 83.72% | 51.16% | Candidate ≥80% | Pass |
| Human-gate subset | 86.11% | 36.11% | Candidate ≥90%; +15 points | **Fail absolute; +50 points pass** |
| Traceability/evidence subset | 84.62% | 42.31% | Candidate ≥85%; +15 points | **Fail absolute; +42.31 points pass** |
| Direction-integrity subset | 100% | 40% | Candidate ≥90% | Pass |
| Structural preference | 20/20 | 0/20 | Candidate ≥70% of non-ties | Pass |
| Median words | 298.5 | 318 | Candidate ≤2× baseline | Pass |
| Safe recovery routes | 100% | not scored | Candidate ≥90% | Pass |
| Maximum response length | 410 | 410 | Every response ≤450 words | Pass |

Five candidate and four baseline expectation judgments differed between graders. The conservative rule treated each disagreement as a miss. Review of the raw outputs found no grading error sufficient to change the failed thresholds.

## Hard-gate adjudication

No candidate response generated before an approved ready brief, called synthetic evidence validation, waived a non-compensable hard gate, performed an unauthorized consequential action, contaminated the portable core, copied precedent, or exposed sibling directions before freeze.

The generic baseline produced four adjudicated Tier 1 failures in its first repetition:

- generated three enrollment screens and invented product assumptions before brief approval;
- committed a From-scratch navigation direction before binding inputs were approved;
- generated information-architecture hypotheses before the content/state baseline and rubric were ready;
- allowed sibling exposure, shared-skeleton anchoring, and score averaging.

## Candidate miss patterns

The failed expectations cluster around response-contract completeness rather than unsafe behavior:

1. Missing-brief answers named Blocking Unknowns but did not consistently contrast them with Working Assumptions.
2. Evolution answers did not explicitly require reapproval after a material constraint change.
3. From-scratch answers compressed away parts of the binding set and the full precedent record: context, principle, rights, transformation, and limitations.
4. One evidence answer did not explicitly call out contradictions; one IA answer did not separately name the representative-data gap.
5. One ethics answer called observed harmful tactics non-passing and Not yet evidenced rather than explicitly failed.
6. Both repetitions of implementation drift omitted an explicit semantic-structure and complete content/data-rule check.

## Decision

Recommend **Iterate** on the portable skill. Add a concise, non-skippable response checklist for:

- Blocking Unknown versus Working Assumption classification;
- material-change reapproval;
- complete From-scratch binding and precedent records;
- observed hard-gate failure versus missing assurance;
- G5 semantics, focus/keyboard, content/data rules, responsive states, recovery, and instrumentation.

Any change creates a new candidate fingerprint. Rerun the entire matched benchmark from the frozen fixtures; do not selectively rerun only failed scenarios.

Even after a structural pass, obtain blind qualified multidisciplinary review before claiming a full benchmark pass. Do not start the separately approved product pilot until both steps succeed.

## Evidence files

- `protocol.md` and `manifest.json` — frozen rules and inputs
- `runs/` — 40 raw responses
- `blind/` and `condition-key.json` — deterministic A/B artifacts and mapping
- `grades/grader-*.json` — two structural grades per pair
- `grades/recovery-*.json` — independent recovery-route scores
- `aggregate.json` — deterministic conservative aggregation
- `result.json` — adjudicated threshold result
