---
name: product-design-review
description: Perform a read-only UX/UI, visual-quality, design-system, responsive/adaptive, accessibility, fidelity, or release review and return evidence-backed prioritized findings. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. Do not implement findings or update baselines.
compatibility: Source inspection works with repository read access; visual, interaction, accessibility, fidelity, usability, and release claims additionally require evidence appropriate to those claims.
license: MIT
metadata: {version: "1.1.0"}
---

# Product Design Review

Review what people actually receive. Separate observable evidence from professional judgment, rank findings by impact, and keep the review itself read-only.

## Authority

Do not edit production source, tests, tokens, contracts, accepted references, baselines, analytics, or external services. Use temporary output for probes. Save a report only when the user requests an artifact and the location is within scope.

For “review and fix,” complete the review first. If the request clearly authorizes a bounded class of fixes, the router may then run implementation or change for only those findings. Blanket permission to “fix everything” does not silently authorize unknown product decisions, shared redesigns, new dependencies, or baseline changes; present those material deltas for scope confirmation.

## Practice

1. **Identify the target.** Record the reviewed commit/build/current working state, surfaces, states, targets, accepted references when present, review question, and explicit exclusions. If the target changes during review, invalidate affected evidence.
2. **Inspect the runtime before rationale.** When the claim is visual or interactive, open the real target and representative states before reading implementation explanations. Verify the target identity. If runtime evidence is unavailable, a source-only or heuristic review can still be useful but must be labeled accordingly.
3. **Review the experience.** Examine first-use comprehension, core task, hierarchy, information architecture, content, navigation, interaction affordances, visual system, responsive/adaptive behavior, relevant states and recovery, input methods, text scaling, motion, and accessibility semantics.
4. **Respect intentional behavior.** Trace suspicious patterns through source, tests, design records, history, platform conventions, and dependent journeys before calling them defects. Distinguish purposeful variants from drift and older constraints from accidental complexity.
5. **Use relevant guidance and research.** For unfamiliar audiences, domains, accessibility needs, safety, culture, regulation, or current platform conventions, consult credible primary research, standards, official platform guidance, and authoritative organizations. Best practice informs the review; it does not automatically override product context or legacy rationale.
6. **Separate verdicts.** Keep fidelity to an accepted design distinct from overall quality. Keep heuristic judgment, deterministic runtime evidence, representative-user evidence, and production signals distinct. Screenshots are captures unless an active assertion or explicit approval makes them protected evidence.
7. **Report actionable findings.** Rank by user and product impact, not aesthetic preference. For each finding give the observed evidence, affected surfaces/states/targets, likely cause, confidence and limitations, consequence, and the smallest bounded change brief. Include strengths and intentional patterns worth preserving when they affect prioritization.

Read [review evidence](references/review-evidence.md) for candidate, fidelity, baseline, or release reviews. Read [periodic evidence](references/periodic-evidence.md) only for post-launch behavior or research decisions. Detect the architecture and read only the applicable `references/platform-*.md` adapter. Use [capability preflight](references/capability-preflight.md) when a claim-relevant runtime, accessibility, user-evidence, or target capability is uncertain.

Missing evidence limits the conclusion it supports. No working runtime means no runtime fidelity or interaction claim; no representative participants means no usability validation; no accessibility inspection means no accessibility acceptance. Do not simulate these passes or block unrelated heuristic findings.

## Definition of done

- The target and review scope are stable and explicit, and the product remains unchanged.
- Actual runtime evidence was inspected for every runtime, fidelity, interaction, or release claim made; source-only conclusions are labeled.
- Existing rationale and intentional variants were investigated before recommending replacement.
- Relevant UX, visual-system, responsive/adaptive, state, behavior-preservation, and accessibility risks were covered in proportion to the question.
- Findings distinguish evidence from judgment, are prioritized by impact, and each maps to a bounded change brief rather than a vague redesign mandate.
- Accepted references and baselines remain unchanged; capture-only images are not mislabeled as goldens.
- The handoff states strengths, findings, evidence limits, and which changes—if any—are already within authorized scope versus awaiting a decision.
