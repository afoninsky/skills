# Design Steward specialist-capability benchmark — corrected matched run

## Status and boundary

Precommitted before sampling on 2026-08-06. This run corrects the first specialist comparison's agent-count confound: the original baseline used one agent for four cases while the candidate used one fresh agent per case. Here, **both conditions use exactly one fresh, history-free agent per case**.

The run evaluates the frozen portable package at commit `94aad78cb9cfa3922dc68552c6e61b916d3d08ba`. It is synthetic, product-neutral, text-only evidence. It does not inspect a target product, contact participants, render an interface, or make an external product change.

## Frozen inputs

- Candidate commit: `94aad78cb9cfa3922dc68552c6e61b916d3d08ba`
- Design Steward tree: `d3eb76eeff710eb195d700f3232bf3c6343e71ba`
- `frontend-design` tree: `0d5b74a14bdf3ebcd64f352d06376a2ef05ed296`
- Cases: four synthetic approved G1/G3-ready briefs in `fixtures.json`
- Conditions: Design Steward with its installed visual specialist, and a matched generic senior product-design baseline
- Raw samples: eight, one fresh agent per condition and case
- Output budget: 450–700 words, one response, no follow-up turn
- External sources, product context, participant access, sibling outputs, and consequential actions: none

## Matched conditions

Every sample inherits the same Codex model, reasoning configuration, output budget, case, workspace permissions, and clean-room constraints. Do not override model or reasoning effort.

### Candidate wrapper

> Use the frozen Design Steward at `skills/design-steward/SKILL.md` and its installed `frontend-design` specialist at `.agents/skills/frontend-design/SKILL.md`. Read only those two skills, their directly routed references required for visual direction generation, and your assigned case in `fixtures.json`. Treat the fixture as an approved G1/G3-ready brief. Produce one visual-direction specification in the required sections. Do not read sibling cases or outputs, benchmark expectations, grades, product repositories, or unrelated files. Do not invent facts outside the brief; make uncertainty and limitations explicit. Return 450–700 words and write only the assigned output file.

### Baseline wrapper

> Act as a capable senior product and visual designer. Read only your assigned case in `fixtures.json`. Treat it as an approved design brief and produce one visual-direction specification in the required sections. Do not read specialized skills, sibling cases or outputs, benchmark expectations, grades, product repositories, or unrelated files. Do not invent facts outside the brief; make uncertainty and limitations explicit. Return 450–700 words and write only the assigned output file.

Required output sections for both conditions: Visual thesis; Palette; Type roles; Layout rhythm; Signature element; States and responsive behavior; Accessibility intent; Traceability; Limitations.

## Blind grading

Deterministically alternate A/B order by case and withhold the key. Give each pair to two independent fresh graders. Each grader scores both outputs from 1–5 for brief fidelity, traceability, visual coherence, brief-specific distinctiveness, and realistic state/responsive/accessibility coverage; records Tier 1 evidence; and selects A, B, or tie. Tier 1 means invented context, breach of a Fixed constraint, unauthorized source/dependency/action, or a positive validation/certification claim.

## Precommitted thresholds

- Candidate Tier 1 failures: zero, with no Tier 1 regression from baseline.
- Candidate preferred in at least 70% of non-tie grader judgments.
- Candidate improves the mean of visual coherence and brief-specific distinctiveness by at least 0.5 on the five-point rubric.
- Every output stays within 450–700 words.
- Limitations, model-grader status, and the corrected matched sampling design remain visible.

## Verdict rules

Any failed threshold yields **Fail — specialist integration needs iteration**. If all thresholds pass, the verdict is **Pass — bounded specialist integration evidence**. Neither verdict is qualified-human visual review, usability validation, accessibility certification, runtime assurance, or proof of product outcomes. This corrected run supersedes the first comparison for release-readiness claims; the first run remains preserved as historical ticket evidence.
