---
name: product-design-change
description: Make a precise, idempotent change to an existing or accepted UI while proving that unrelated behavior and design remain intact. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. Never update accepted baselines or broaden a local request silently.
compatibility: Works with an inspectable current state and the repository's normal build, runtime, and test tools. Formal source maps, manifests, and bundled guards are used when the project already has protected design artifacts or the risk justifies them.
metadata: {version: "1.2.0"}
---

# Product Design Change

Treat “change only this” as a closed-world delta. Derive the requested final state, apply the smallest coherent patch, and preserve everything outside its real dependency boundary.

## Invariants

- Never update, regenerate, delete, rename, or approve an accepted reference, golden, baseline manifest, or hash. A candidate may differ intentionally; acceptance is a separate human decision recorded by `product-design-contract`.
- Do not run snapshot-update modes or make visual tests pass by replacing expected images.
- Do not use a local override to conceal a shared design decision or an unexpected impact.
- Before changing geometry inside an existing layout, inspect its grid/flex sizing, stretch and alignment, intrinsic size, wrapping, overflow, and positioned descendants. Hidden layout coupling is part of the protected dependency boundary.
- Do not require suite-specific metadata for an ordinary repository. Use existing project records and guards when they exist; introduce a durable manifest only when protection, collaboration, or risk makes it useful.

## Practice

1. **Check the current result first.** Use the smallest reliable canonical-source, cascade/binding, or runtime evidence that can establish the requested final condition. If it is already satisfied, make no edit and report the no-op. Expand the investigation only when an edit or unexplained behavior remains.
2. **Establish the comparison state.** Before editing, inspect the relevant runtime, source and tests, Git status, accepted references when present, and any existing design contract or source map. Read enough history and dependent journeys to understand why the current behavior exists. Preserve unrelated user changes. On later turns, keep the original protected state and the immediately previous working candidate as separate anchors. Carry forward earlier explicit requirements and prior intentional changes as protected constraints. A later request supersedes only an earlier requirement it explicitly contradicts; naming an element authorizes only the stated delta and does not reopen its other accepted decisions.
3. **Define the final delta.** State one observable outcome, allowed surfaces/states/components/tokens/files, and important must-not-change behavior. For a relative instruction, translate it into a verifiable final condition so a second run cannot compound the change.
4. **Resolve real impact.** Trace the named element through its implementation component, semantic tokens and shared files, dependent states and surfaces, and target platforms. A shared dependency expands the evidence needed. If it materially expands mutation scope, changes behavior or navigation, reopens a fixed design decision, or needs a new dependency, obtain approval for that expansion before editing.
5. **Apply the smallest patch.** Extend existing components, tokens, and framework conventions. Prefer a local semantic correction when the intent is local and a canonical shared change when the intent is truly shared. Do not perform unrelated cleanup or modify project records merely to legitimize an unexpected dependency.
6. **Verify change and preservation.** Run affected functional, state, accessibility, responsive/adaptive, and visual checks in the real runtime. Compare like-for-like conditions and inspect actual output. Check every actual consumer of a changed shared component or token, plus the highest-risk must-not-change paths. Any non-uniform structure, style, local geometry, wrapping, or rendered change outside the authorized delta and its proven necessary dependency closure is a regression; fix it rather than relabeling it incidental reflow.
7. **Report a candidate.** Separate the intended delta from regressions, skipped evidence, and accepted-state changes. Do not call the candidate accepted or update its baselines.

Read [change protocol](references/change-protocol.md) for protected, cross-surface, or collaborative changes. Read [platform adapters](references/platform-adapters.md) only for affected targets. Use [tool preflight](references/tool-preflight.md) when a required comparison, runtime, accessibility, or scope capability is uncertain.

When a project already uses the suite's contract, source map, and change manifest, adapt the existing manifest and use the bundled guard:

```text
python3 <product-design-change-skill-directory>/scripts/change_guard.py validate --project-root <repository> --manifest <manifest>
python3 <product-design-change-skill-directory>/scripts/change_guard.py verify --project-root <repository> --manifest <manifest>
```

For high-risk visual changes, project-native tools may export deterministic protected evidence for the bundled comparison guard:

```text
python3 <product-design-change-skill-directory>/scripts/preservation_guard.py --candidate <candidate.json> --expected-candidate-capture-id <current-capture-id> --against <original.json> [--against <previous.json>]
```

Read [preservation evidence](references/preservation-evidence.md) only when using this guard. Each reference names only evidence that must remain exact; bind an inserted, modified, or deleted authorized subtree with a stable locator and operation-specific counts, and express geometry relative to the protected component so allowed downstream translation cannot conceal internal reflow. The guards prove declared scope and equality of supplied protected evidence, not capture freshness, general visual quality, or usability. If a missing capability makes the protected edit unsafe, stop before production writes; otherwise complete only the safe bounded work and state what remains unverified.

## Definition of done

- The requested observable result holds and only its necessary dependency closure changed.
- Existing behavior and rationale were inspected before replacement; unexplained legacy behavior was preserved.
- Out-of-scope surfaces, accepted references, baseline files, and unrelated user changes remain intact.
- Shared-component or token impact is fully disclosed and verified across actual consumers.
- Relevant runtime, functional, visual, responsive/adaptive, and accessibility evidence passed, with limitations explicit.
- The final state is idempotent: repeating the same request would create no further change.
- The handoff lists the exact delta, changed files and design authorities, preservation evidence, missing evidence, and any human acceptance decision still required.
