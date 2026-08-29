---
name: product-design-implementation
description: Implement a clear or approved UI design in the product's real web or mobile architecture with production-quality states, accessibility, and verification. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. Do not redesign accepted UI or overwrite baselines.
compatibility: Uses the target project's existing build and test toolchain. Runtime, accessibility, and visual-comparison tools are selected in proportion to the implemented surface and claims.
license: MIT
metadata: {version: "1.1.0"}
---

# Product Design Implementation

Translate a clear design decision into maintainable production UI without changing its intent or the surrounding product by accident.

## Authority

The user's request may itself authorize implementation when it identifies the desired outcome and mutation scope clearly. An approved mock or contract is useful but not mandatory for a small, well-defined design. For a greenfield or broad redesign, resolve material structural and visual choices through direction or prototype work before committing them; those phases may occur in the same task when the request delegates the choices.

Use professional judgment for small reversible details that follow the existing system. Stop for a decision only when a gap would materially change behavior, information architecture, brand direction, shared surfaces, dependencies, or the user's stated scope.

Never update accepted references or visual baselines, disguise a new design decision as implementation, or treat passing tests as acceptance.

## Practice

1. **Inspect before editing.** Read project instructions, Git status, relevant source and tests, routes, component and token ownership, design records, current runtime, and platform packaging. Understand why existing behavior and boundaries exist. Preserve unrelated user changes.
2. **Bind the intended result.** Name the surfaces, states, targets, files or packages likely to change, the observable outcome, and what must remain unchanged. If the requested result already holds, verify it and report a no-op.
3. **Use the real architecture.** Extend existing components, semantic tokens, navigation, state, localization, responsive/adaptive patterns, and test fixtures. For a shared web wrapper, improve the shared UI and verify shell-specific behavior rather than creating a duplicate native interface.
4. **Prefer proven mechanisms.** Use platform-native semantic controls and the repository's mature libraries before custom widgets, layout engines, or infrastructure. When no repository or architecture exists, choose the simplest dependency-free platform-appropriate implementation that satisfies the request; introduce a stack only when a material requirement justifies it. Do not add a production dependency, replace a working toolchain, or create a parallel design system unless the request genuinely requires it and authority covers the change.
5. **Implement the smallest coherent slice.** Cover the entry context, core action, consequence, and relevant loading, empty, error, disabled, focus/selected, permission, long-content, localization, and recovery states. Include only states that belong to the requested surface or are necessary to preserve dependent behavior.
6. **Make the result idempotent.** Express the desired final state rather than stacking relative tweaks, wrappers, overrides, generated records, or duplicate tokens. Running the same request again against the finished product should make no further change.
7. **Verify the real output.** Run the smallest relevant build, type/static, functional, visual, responsive/adaptive, and accessibility checks. Inspect representative browser or app renders and the critical interactions at affected targets. Check dependent surfaces when a shared component or token changed.

Read [implementation evidence](references/implementation-evidence.md) for consequential or multi-target production work. Detect the architecture and read only the applicable platform adapter in `references/platform-*.md`. Use [capability preflight](references/capability-preflight.md) when a required renderer, runtime, accessibility, or comparison path is uncertain; use [tool setup](references/tool-setup.md) only after deciding a missing capability is necessary.

A missing capability blocks only the work or claim that depends on it. If its absence makes a production edit unsafe or prevents the requested acceptance, stop before that edit and offer the smallest setup or reduced-scope option. Otherwise complete the safe portion and label the unverified result honestly; do not call source inspection runtime, visual, accessibility, or usability evidence.

Before handoff, protect established baseline paths. When the repository uses the suite manifest or another known protected layout, run:

```text
python3 <product-design-implementation-skill-directory>/scripts/check_protected_paths.py --root <repository> --base-ref <comparison-ref> --manifest <baseline-manifest>
```

## Definition of done

- Only the requested surfaces, states, components, tokens, and necessary tests or fixtures changed; unrelated behavior and user work are preserved.
- The implementation follows existing architecture and conventions and introduces no unrequested dependency, parallel design authority, or prototype shortcut.
- The result is coherent with the intended design and robust for the relevant content, states, targets, inputs, responsiveness/adaptation, and accessibility needs.
- Shared changes were checked against their actual consumers.
- The smallest relevant checks and real-output inspection passed; skipped or unavailable evidence and its consequence are explicit.
- Accepted references and baselines are unchanged.
- A second run of the same request would produce no diff.
- The handoff states the implementation delta, evidence, preservation checks, limitations, and any bounded review or decision still needed.
