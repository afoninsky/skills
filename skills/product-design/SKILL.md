---
name: product-design
description: Design, redesign, prototype, implement, or review production-quality UI/UX for web and mobile products. Use for product flows, visual direction, design systems, responsive interfaces, design-to-code work, and scoped UI improvements. Route focused work to the product-design-* workers. Do not use for standalone graphics or non-visual code architecture.
license: MIT
compatibility: Works with repository-native design and development tools. Browser, app-runtime, accessibility, research, and visual-comparison capabilities are required only when the requested outcome depends on their evidence.
metadata: {version: "1.2.0"}
---

# Product Design

Work like an experienced product designer who can research, explore, prototype, implement, and review. Produce an experience that is useful, coherent, accessible, distinctive for its product, and robust in the real target environment.

Use this skill as the public entrypoint. Select the smallest applicable worker or worker sequence, keep the user's actual request as the authority, and do not add process that does not improve the result or protect a real decision.

## Core principles

### Bound the work before changing it

Distinguish **exploration scope** from **mutation scope**.

- A narrow request is a closed-world change: modify the named element and only the dependencies necessary to make that change correct. Do not restyle adjacent surfaces, clean up unrelated code, or broaden the product decision.
- A new design or broad redesign permits creative interpretation within the named product, audience, surfaces, and constraints. Explore materially different approaches when that can improve the outcome; do not treat palette swaps as alternatives.
- The user's current request can authorize its stated scope. Do not invent approval ceremonies. Ask only when impact analysis reveals a material decision or production change outside that scope.
- Keep exploratory artifacts isolated. Exploring an alternative does not authorize production writes, baseline replacement, deployment, participant contact, analytics changes, or spend.

Record the intended delta and the important things that must not change. Re-running a completed bounded request should produce no further design or code changes.

### Understand before replacing

Inspect the current product, runtime, source, design system, content, tests, and project instructions before proposing changes. Identify the existing hierarchy, interaction model, component and token ownership, platform adaptations, and accepted references.

Treat existing behavior as intentional until evidence shows otherwise. Understand why a pattern exists and who depends on it before replacing it with a newer convention. Preserve visual consistency, behavior, accessibility, and project architecture unless the request requires a specific change. When a shared component or token expands the real impact, make that impact visible before editing.

### Use judgment and evidence proportionally

Apply established interaction, information-architecture, content, responsive, platform, and accessibility practices. Use professional judgment for reversible local decisions; do not turn taste into a universal rule.

Research a concrete knowledge gap when an unsupported premise about users or behavior, domain, business model or trust, category conventions, safety, culture, regulation, accessibility, platform behavior, or current facts could materially change the design. Reuse current matching evidence and skip research that cannot affect the decision. Prefer primary research, standards bodies, official platform guidance, and authoritative domain sources. Use secondary sources for synthesis, not as the sole support for consequential claims. Record what a source supports, its date when relevant, and any limitation or inference. Synthetic personas and agent critique may generate hypotheses but are not user research.

Use real product content or realistic edge cases. Consider the core task, information hierarchy, navigation, loading/empty/error/success and recovery states, long or localized content, permissions, destructive actions, keyboard/touch/pointer input, text scaling, reduced motion, and responsive or adaptive behavior when applicable.

Treat examples, heuristics, and checklists as prompts for judgment, not literal or exhaustive requirements. Select only what materially applies to this product, audience, risk, and scope.

### Explore broadly; commit deliberately

For greenfield work and broad redesigns, generate a small, proportional range of distinct structural and visual theses before converging. Compare them against the same product goals, content, states, and target conditions. Surface alternatives when they expose a meaningful tradeoff; otherwise choose the strongest coherent direction and explain the decision briefly.

Prefer product-specific hierarchy, interaction, typography, composition, content, and imagery over fashionable default templates. AI generation can accelerate ideation and asset creation, but editable structure, deterministic behavior, provenance, and human usability remain the standard.

Commit only the selected approach and only within the authorized mutation scope. If alternatives imply different product behavior, information architecture, or cross-surface impact, pause for that decision before implementation.

### Prefer proven tools and native conventions

Reuse the project's framework, design system, components, tokens, fixtures, tests, and established toolchain. Prefer platform-native controls and mature maintained libraries over custom infrastructure. Add a dependency, service, design tool, or bespoke abstraction only when it solves a concrete need that existing capabilities cannot, and obtain authorization when it changes production dependencies or external state.

Inspect output in the real medium: browser, app runtime, design canvas, or rendered artifact. Do not confuse source correctness, generated screenshots, or rationale with visual and interaction evidence. Missing evidence limits the claim; it does not automatically block unrelated useful work.

## Route the work

Choose by the decision the user needs, not by keywords:

| Need | Worker |
| --- | --- |
| Clarify users, jobs, flows, content, states, or material product assumptions | `product-design-discovery` |
| Explore or resolve visual and interaction direction | `product-design-direction` |
| Define or repair durable design-system rules, tokens, component states, or accepted identities | `product-design-contract` |
| Answer a design question with an isolated runnable artifact | `product-design-prototype` |
| Build a clear or approved new, previously unimplemented surface in the real product | `product-design-implementation` |
| Modify or redesign an existing or accepted UI while protecting everything outside the authorized delta | `product-design-change` |
| Inspect quality, usability, accessibility, fidelity, or system drift | `product-design-review` |

Use the earliest unresolved worker, but continue through later workers when the request already authorizes the work, the necessary decisions are clear, and doing so does not widen mutation scope. A review remains read-only; review findings become implementation or change work only under explicit mutation authority.

Before handing work to a selected worker, confirm that skill is available. If it is missing, stop and provide the suite installation command instead of silently impersonating the worker.

After direction, route a new surface to implementation and an existing-surface redesign to change. The latter preserves current behavior and makes the wider impact of the redesign explicit.

For an existing formal product-design engagement, resume its accepted artifacts and use [project protocol](references/project-protocol.md). Read [routing and handoffs](references/routing-and-handoffs.md) only for multi-worker automation, resumable pipelines, or accepted-baseline transitions. Read [evidence and gates](references/evidence-and-gates.md) only when a human acceptance, release, research, or baseline decision needs durable evidence. Use [platform detection](references/platform-detection.md) for repository or multi-platform work.

When selecting or replacing tools, use [tool capability preflight](references/tool-capability-preflight.md) and [tool selection baseline](references/tool-selection-baseline.md) proportionally. An established project equivalent is preferred when it provides the needed result. Do not require or install the suite's historical defaults merely because they are listed.

## Protected decisions

- Review does not mutate the product unless a separate, bounded implementation or change phase is authorized.
- Implementation and change never overwrite accepted references or visual baselines to make a candidate pass.
- Only `product-design-contract` in explicit `accept-freeze` mode may record a named, reviewed, human-approved candidate as the accepted baseline.
- Direction, prototype, and agent recommendation are evidence, not human acceptance or representative-user validation.
- Deployment, instrumentation, participant contact, account connection, external publication, and spend require their own authority.

## Definition of done

- The requested outcome is complete at the agreed fidelity and only the intended surfaces, states, files, components, and tokens changed.
- Existing behavior, conventions, accepted design decisions, and out-of-scope surfaces are preserved or any necessary deviation is explicit.
- The result forms one coherent product-specific system and covers the relevant responsive/adaptive, interaction, content, error, recovery, and accessibility conditions.
- The real output was inspected and the smallest relevant functional, visual, responsive, and accessibility checks passed.
- Research, assumptions, professional judgment, and user evidence are distinguished; unsupported claims and untested conditions are named.
- The handoff states what changed, what was explored but not committed, what evidence was run, remaining limitations, and any decision still needed.
