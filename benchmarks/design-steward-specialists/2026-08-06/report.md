# Design Steward specialist-capability evaluation

Date: 2026-08-06

> **Release-readiness status:** superseded by the corrected matched run in `../2026-08-06-iteration-2/report.md`. This first run remains valid as historical ticket evidence, but its baseline used one agent for all four cases while the candidate used one fresh agent per case. Do not use its comparative effect size as release-readiness evidence.

Base Design Steward: `fca00ad2c3e25be38169f5ab03913ddf9c7e6ae1`

Skills CLI: `1.5.16`

## Decision

**Pass for the specialist-capability ticket.** The bounded `frontend-design` delegation produced a repeatable, measurable improvement over a matched generic-design baseline, with no candidate Tier 1 failure. The `web-design-guidelines` delegation produced reproducible, source-scoped E1 findings and preserved every required non-certification boundary.

This is product-neutral, model-graded forward-test evidence. It is not representative-user validation, qualified-human visual review, accessibility certification, runtime assurance, or proof of product outcomes.

## Precommitted visual threshold

- zero candidate Tier 1 failures and no Tier 1 regression from baseline;
- candidate preferred in at least 70% of blind review pairs;
- candidate improves mean brief-specific coherence and distinctiveness by at least 0.5 on a five-point rubric;
- limitations and disagreement remain visible.

## Method

Four synthetic, fully approved G1/G3-ready direction briefs were frozen. Each condition received the same brief, output sections, word range, and clean-room constraints.

- Baseline: one fresh generic design agent produced all four directions without Design Steward or `frontend-design`.
- Candidate: Design Steward created one fresh, isolated `frontend-design` sub-agent per direction; sibling cases and outputs were withheld.
- Blinding: A/B order alternated by case. Two fresh graders saw only `blind-pairs.md`, not condition filenames or provenance.
- Rubric: brief fidelity, traceability, visual coherence, brief-specific distinctiveness, and realistic state/responsive/accessibility coverage, each scored 1–5.
- Tier 1: invented context, Fixed-constraint breach, unauthorized source/dependency/action, or a positive validation/certification claim.

Raw baseline, candidate, blind pairs, and grader JSON are preserved beside this report.

## Visual results

| Measure | Candidate | Baseline | Difference |
| --- | ---: | ---: | ---: |
| Blind preferences | 8/8 (100%) | 0/8 (0%) | +100 percentage points |
| Brief fidelity | 5.000 | 4.750 | +0.250 |
| Traceability | 5.000 | 4.125 | +0.875 |
| Visual coherence | 5.000 | 4.000 | +1.000 |
| Brief-specific distinctiveness | 5.000 | 3.500 | +1.500 |
| State/responsive/accessibility coverage | 5.000 | 4.250 | +0.750 |
| Mean coherence + distinctiveness | 5.000 | 3.750 | **+1.250** |
| Tier 1 failures | 0 | 1 grader finding | No candidate regression |

Both graders made the same preference in every case. Candidate preference exceeded the 70% threshold by 30 percentage points; the +1.25 coherence/distinctiveness gain exceeded the +0.5 threshold by 0.75.

The baseline Tier 1 finding was one grader's scoped judgment that a failure-state persistence promise invented unconfirmed implementation behavior. The other grader described the same passage as overly categorical but did not classify it as Tier 1. This disagreement is preserved in the raw JSON.

## UI-audit result

A fresh `web-design-guidelines` sub-agent inspected only the frozen synthetic HTML fixture.

- Fixture SHA-256: `ac11654bba5549ca8e0217e8a92a90b05294d512cd9693fe9042341e1ad69890`
- Guideline commit: `4e799d45c17aec1498c269287a83b9dba22b966b`
- Guideline SHA-256: `eea73cb6dd46fee9faec9973e8e7fe198b5f07ec326f14d276a56e50287e1cab`
- Findings: 7 exact file-line findings with severity, remediation, provenance, exclusions, confidence, and limitations.
- Classification: E1 specialist/heuristic input.

The report explicitly rejects representative-user validation, accessibility certification, runtime/browser assurance, engineering approval, legal/regulatory compliance, and ship approval. It records that a clean static audit would mean only that the method found no issue in the inspected scope.

## Structural and portability evidence

- Both specialists are installed repository-locally and discoverable through `skills list --json`.
- Clean project installation succeeded for Design Steward and both companions.
- Design Steward's full assets, references, validator, frontend license, and UI-audit skill were present after installation.
- Provenance hashes match the installed files.
- Existing repository verifier, Design Brief tests, specialist integration tests, JSON checks, link checks, Python syntax checks, Ruff checks, and `git diff --check` passed.
- No required MCP, browser, design framework, paid service, or production/runtime dependency was added.

## Limitations

- The visual outputs were text specifications, not rendered interfaces or interactive prototypes.
- The graders were fresh model agents, not qualified human visual designers or representative users; their ratings are indicative E1 evidence.
- There were four briefs and two graders, so the evaluation does not estimate population-level variance.
- Exact model identifiers and sampling parameters were not exposed to the evaluation harness.
- The UI fixture was intentionally small and defective; the audit demonstrates correct scoping and evidence capture, not recall over a representative codebase.
- The canonical UI rules can change. Each future audit must resolve and hash a fresh immutable snapshot, or record the audit unavailable.

These limitations do not defeat the ticket's bounded capability claim. They do constrain any stronger claim about professional output quality, product usability, compliance, or release readiness.
