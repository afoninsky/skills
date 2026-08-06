# Design Steward specialist-capability evaluation — corrected matched run

Date: 2026-08-06

## Decision

**Pass — bounded specialist integration evidence.**

With agent count matched exactly, the Design Steward plus `frontend-design` condition cleared every precommitted threshold: zero candidate Tier 1 failures, 6 of 7 non-tie blind preferences (85.7%), and a +0.6875 improvement in mean visual coherence plus brief-specific distinctiveness on the five-point rubric.

This corrected comparison supersedes the first run's comparative release-readiness claim. The first run remains preserved as historical evidence for the specialist-capability ticket, but its baseline used one agent for all four cases while the candidate used one fresh agent per case.

## Frozen state and method

- Candidate: `94aad78cb9cfa3922dc68552c6e61b916d3d08ba`
- Design Steward tree: `d3eb76eeff710eb195d700f3232bf3c6343e71ba`
- `frontend-design` tree: `0d5b74a14bdf3ebcd64f352d06376a2ef05ed296`
- Protocol committed before sampling: `ed04316`
- Cases: four new synthetic, fully approved G1/G3-ready visual briefs
- Samples: four candidate and four generic baseline outputs
- Matching: one fresh history-free agent per condition and case; inherited model/configuration; same brief, sections, word budget, permissions, and clean-room boundary
- Grading: deterministic alternating A/B mask; two fresh independent blind model graders per pair
- External sources, product access, participants, rendered artifacts, and consequential actions: none

## Results

| Measure | Candidate | Baseline | Frozen threshold | Result |
| --- | ---: | ---: | ---: | --- |
| Tier 1 failure cases | 0 | 1 flagged by one grader | Candidate 0; no regression | Pass |
| Blind preferences | 6/7 non-ties (85.7%) | 1/7 (14.3%) | Candidate ≥70% | Pass |
| Brief fidelity | 4.750 | 4.875 | descriptive | — |
| Traceability | 5.000 | 4.375 | descriptive | — |
| Visual coherence | 5.000 | 4.375 | combined gain ≥0.5 | Pass |
| Brief-specific distinctiveness | 5.000 | 4.250 | combined gain ≥0.5 | Pass |
| State/responsive/accessibility coverage | 5.000 | 5.000 | descriptive | — |
| Coherence + distinctiveness mean | 5.000 | 4.3125 | gain ≥0.5 | **+0.6875; Pass** |
| Output range | 671–687 words | 597–687 words | every output 450–700 | Pass |

Across eight grader judgments, six preferred the candidate, one preferred the baseline, and one was a tie. The baseline preference concerned a workshop-booking direction one grader found more restrained; the tie concerned two strong civic-record directions. Both are retained in the raw grades.

One grader classified baseline case 4's promise to preserve a draft after failed confirmation as invented behavior; the other did not raise Tier 1. No grader raised a candidate Tier 1 issue.

## Interpretation

The corrected evidence supports the narrow claim that the installed visual specialist, when bounded by Design Steward's approved brief and hard gates, improves the specificity and coherence of text direction specifications without weakening the clean-room constraints. It also shows that the gain is not an artifact of giving the candidate more fresh agents than the baseline.

It does not establish rendered visual quality, professional review, usability, accessibility conformance, implementation feasibility, runtime behavior, brand fit, or product outcomes. Those claims require engagement-scoped artifacts and the named human, specialist, implementation, and representative-user evidence appropriate to the claim.

## Evidence files

- `protocol.md`, `manifest.json`, and `fixtures.json` — frozen method and cases
- `runs/` — eight raw outputs
- `scripts/build_blind_pairs.py`, `blind/`, and `condition-key.json` — deterministic masking
- `grades/grader-*.json` — two independent blind grades
- `scripts/aggregate_grades.py` and `aggregate.json` — deterministic summary
- `result.json` — threshold decisions and limitations
