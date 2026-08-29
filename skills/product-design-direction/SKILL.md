---
name: product-design-direction
description: Explore, compare, and resolve product-specific visual and interaction direction from a clear product brief. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. Keep exploration isolated and do not edit production UI or accepted baselines.
compatibility: Requires enough product context to judge fit and a renderable medium appropriate to the question. Design tools, image generation, participant studies, and preview hosting are optional and selected only when useful.
---

# Product Design Direction

Turn product intent into a coherent visual and interaction backbone. Use creative judgment, not trend imitation, and spend exploration effort in proportion to the decision.

## Scope

Direction work may create isolated sketches, mocks, design files, code studies, references, and comparison artifacts. It does not mutate production source or accepted baselines.

Preserve fixed product, content, behavior, accessibility, brand, and platform constraints. A broad or greenfield request permits substantial creative interpretation inside those constraints. A narrow styling question does not.

When the design question, inputs, and constraints are unchanged, reuse an equivalent completed direction set and its stable candidate identities instead of generating duplicates. If nothing needs to change, report a no-op.

## Practice

1. **Understand the product and current design.** Read the brief, real content, priority journey, state inventory, current runtime and design system, and prior decisions. In an existing product, identify which visual patterns are intentional and why before proposing their replacement.
2. **Name the design problem.** State the qualities the direction must produce as observable consequences: hierarchy, comprehension, interaction grammar, tone, density, responsiveness, accessibility, and product specificity. Avoid adjective-only goals.
3. **Research with intent.** For unfamiliar audiences, cultural contexts, domain conventions, accessibility needs, or platform behavior, use credible primary or authoritative sources. Reference products may reveal patterns, but are not permission to copy. Track asset and font provenance.
4. **Explore proportionally.** Generate a small range of structurally and visually distinct theses when alternatives can reveal a meaningful tradeoff. Vary information hierarchy, composition, navigation treatment, typography, density, color/material logic, imagery, motion, and state expression as coherent systems. Do not manufacture extra options or present palette swaps as separate directions.
5. **Use the lowest useful medium.** Work in an isolated design page, disposable code study, native preview, or other renderable artifact. Use image generation for raster imagery when it improves the result, not as a substitute for editable interface structure. Prefer existing project tools and portable source.
6. **Compare matched evidence.** Judge alternatives with the same representative content, states, targets, and constraints. Inspect actual renders for hierarchy, rhythm, legibility, responsiveness, accessibility risk, product fit, and implementation implications.
7. **Converge deliberately.** When the user delegates design judgment, recommend and select the strongest coherent direction within scope. Surface alternatives when their tradeoffs are useful. Ask before production implementation only when the alternatives imply materially different product behavior, information architecture, cost, cross-surface impact, or a brand commitment outside the delegated brief.

Agent selection chooses a working direction; it does not create an accepted baseline or claim representative-user preference. Keep discarded exploration separate from the committed design path.

Read [direction method](references/direction-method.md) for a substantial comparison exercise. Read [rendering, quality, and platform coverage](references/rendering-quality-and-platforms.md) when the work spans target classes or requires formal comparison evidence. Use [tool preflight](references/tool-preflight.md) only for capabilities the selected medium actually needs.

## Definition of done

- The chosen direction follows the product's real content, task, audience, and constraints rather than a generic template.
- Exploration was broad enough to test the meaningful design space, but no unnecessary options or artifacts were produced.
- Any compared directions use matched inputs and differ in structural or interaction logic, not decoration alone.
- The working direction defines a coherent hierarchy, type, color, shape, imagery, motion, responsive/adaptive, state, and accessibility approach at the fidelity the request needs.
- Existing production files, accepted design authorities, references, and baselines are unchanged.
- Repeating the same direction request with unchanged inputs would not create duplicate candidates or artifacts.
- The handoff identifies the chosen or recommended direction, explored alternatives, evidence, tradeoffs, unresolved decisions, and the scope that may proceed to contract, prototype, or implementation.
