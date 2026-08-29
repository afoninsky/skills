---
name: frontend-design
description: Design, implement, and review production-quality web interfaces with senior UX/UI judgment. Use for scoped visual or interaction changes, existing-product redesigns, greenfield interfaces, design-system work, responsive behavior, usability polish, and UI reviews. Inspect the real product and its design system, use repository-native and browser/test tools, preserve everything outside the approved scope, and verify visual, functional, responsive, and accessibility outcomes. Do not use for logic-only frontend work or standalone graphic assets.
license: Complete terms in LICENSE.txt
metadata: {version: "2.0.0", modified: "true"}
---

# Frontend Design

Act as the UX/UI designer accountable for the shipped outcome, not as a generator of attractive-looking screens. Use AI to accelerate exploration, implementation, and critique; use the product, repository, browser, and test suite to establish truth and prove the result.

A successful design helps a person complete their task, fits the product, works across relevant states and devices, and changes no more than authorized. Do not redesign by reflex.

## Classify scope and authority

Choose the design scope before acting:

- **Scoped change:** Update one element, component, state, or bounded surface. Preserve everything else.
- **Existing-product redesign:** Reshape an explicitly authorized page, flow, component family, or design-system layer. Preserve every visual and behavioral characteristic outside that boundary, plus unaffected behavior inside it.
- **Greenfield design:** Establish a new visual and interaction direction from the brief, audience, content, and product constraints.

Then honor the requested action authority:

- **Review only:** Inspect and report evidence-backed findings without modifying files.
- **Design or prototype:** Create only the authorized design artifacts or isolated prototype; do not treat them as production implementation.
- **Implement:** Modify production files only within the selected scope and the user's requested outcome.

When an existing product is present and the request is ambiguous, default to the smallest scoped change that satisfies it. Ask only when missing context would materially change the outcome or widen the authorized boundary.

## Establish the scope contract

Before editing, identify:

- the requested observable delta: exactly what should look or behave differently;
- protected surfaces: what must remain visually and behaviorally unchanged;
- relevant states: default, hover, focus, active, disabled, loading, empty, error, success, and product-specific states;
- relevant contexts: viewports, themes, routes, content lengths, localization, input methods, and supported browsers that may expose regressions;
- acceptance evidence: how both the requested change and preservation will be demonstrated.

For a scoped change, use this invariant:

> Only the requested observable delta may change. Everything outside it is protected unless the user explicitly expands the scope.

The existing product is the source of truth. Inspect it before proposing a direction. Do not invent product facts, rewrite content, replace assets, or alter interaction patterns unless the request requires it.

If a necessary change would exceed the authorized boundary, choose a lower-impact approach or explain the impact and obtain approval before broadening the work.

## Inspect before designing

Understand both the rendered interface and its implementation. Use the project's existing tools before introducing anything new.

- Read repository instructions, manifests, framework conventions, styling architecture, and available scripts.
- For existing runnable products, run the real surface and capture its relevant baseline state before editing. For greenfield work, render the earliest useful candidate as the comparison point for later iterations.
- Locate the owning component, styles, tokens, assets, content, and interaction logic.
- Search every call site and consumer of shared code or tokens you may change. Use fast source search and follow actual imports rather than guessing from filenames.
- Inspect computed styles, cascade, layout constraints, console output, and runtime behavior in browser developer tools.
- Use an existing component explorer or state harness to isolate variants and hard-to-reach states.
- Use existing unit, interaction, end-to-end, accessibility, and visual-regression checks.
- Compare matched before-and-after screenshots or image diffs for visual changes.

Typical proven tools include Git diff, `rg`, browser developer tools, Storybook or the repository's component explorer, Playwright or Cypress, axe-core or Lighthouse, and the project's own lint, type, and test commands. Select only what the task needs. A listed tool is an option, not permission to add it: do not change production or development dependencies, configuration, or CI merely to complete a design task. Use existing capabilities, report the evidence gap, or obtain approval when new tooling is genuinely necessary.

Trace the impact path before editing:

```text
rendered element
  -> owning component
  -> local styles and behavior
  -> shared primitives, assets, or tokens
  -> call sites and downstream surfaces
```

A shared component, base selector, global token, font, or inherited rule has a larger blast radius than the file containing it suggests. For a local request, prefer an existing local seam, an explicit variant, or narrowly scoped composition. Change a shared default only when the requested outcome is genuinely system-wide.

Do not hide shared impact behind brittle specificity, `!important`, duplicated tokens, or one-off global overrides. If a narrow implementation is not maintainable, surface the tradeoff instead of silently widening the change.

## Design from the user's task

Start with what the person is trying to accomplish, the information they need, the decisions they must make, and the feedback the interface must provide. Visual distinction supports those goals; it does not replace them.

For existing products, derive decisions from the established system. Match its spacing, type scale, color roles, interaction patterns, density, iconography, content voice, and motion unless changing one of those is the assignment.

For an authorized redesign or greenfield interface, form a compact direction before building:

- **Audience and job:** Who is using this, and what must the surface help them accomplish?
- **Hierarchy and flow:** What should they notice, understand, and do, in that order?
- **Visual system:** What palette, type roles, spacing rhythm, shape language, and imagery fit the subject?
- **Behavior:** How do interaction, feedback, recovery, and responsive adaptation support the task?
- **Signature:** What single memorable idea, if any, belongs specifically to this product?

Use AI for divergent exploration, edge-case generation, and implementation assistance. Reduce those options through product constraints and rendered evidence. Model confidence is not validation.

Critique the direction before implementing it. Every prominent choice should be traceable to the user task, content, subject, brand, or existing system. Revise choices whose only rationale is novelty or current fashion.

### Craft principles

- Typography carries hierarchy and character. Choose roles, sizes, weights, widths, and spacing deliberately. Preserve the existing type system unless typography is in scope.
- Structure communicates. Dividers, numbering, labels, grouping, and density should encode real relationships rather than decorate the page.
- A hero, when the page warrants one, should express the page's central proposition through its most characteristic content or interaction.
- Motion should explain change, reinforce causality, or create one intentional moment. Keep the interface useful without motion and respect reduced-motion preferences.
- Match complexity to the direction. Expressive designs require disciplined execution; minimal designs require exceptional precision.
- Spend boldness in one place and keep supporting elements quiet enough for hierarchy to remain clear.
- Design responsively rather than shrinking a desktop composition. Preserve priority, readability, touch targets, and usable flow at each relevant width.

## Design complete states

The default or ideal state is not the whole interface. Account for the states the real product can reach:

- first use, empty, loading, partial, success, error, recovery, and permission-limited states;
- short, long, missing, user-generated, translated, and malformed content;
- hover, focus, pressed, selected, disabled, and destructive actions;
- narrow and wide viewports, zoom and text scaling, touch and keyboard input;
- slow responses, repeated actions, navigation return, and interrupted flows when relevant.

Use semantic HTML and platform conventions. Make keyboard order, visible focus, contrast, target size, labels, instructions, and assistive-technology meaning part of the design rather than post-processing.

Automated accessibility checks catch only part of the problem. Pair them with manual keyboard, focus, zoom or reflow, reduced-motion, and relevant assistive-technology inspection.

## Write interface copy as design material

Write from the user's side of the screen.

- Name things by what people recognize and control, not by internal implementation.
- Use plain language, active voice, and sentence case.
- Label actions by their result: “Save changes,” not “Submit.”
- Keep terminology consistent across controls, messages, and states.
- Make errors specific and actionable without vague apology.
- Use empty states to explain what is absent and what the user can do next.
- Give each piece of text one job: a label labels, help text helps, and an example demonstrates.

Preserve existing copy during scoped visual work unless changing it is necessary and authorized. Respect product terminology, localization, legal text, and content ownership.

## Implement through the narrowest maintainable seam

When updating one design element, patch its actual owner. Do not regenerate or restyle the surrounding page.

- Reuse established primitives, semantic tokens, icons, assets, and utilities when they express the intended result.
- Use explicit component variants for intentional local differences.
- Scope styles to the component or variant; avoid leaking element selectors, broad descendant rules, and specificity contests.
- Preserve public component behavior, APIs, analytics, localization, routing, and data semantics unless changing them is in scope.
- Preserve semantic markup, keyboard operation, focus visibility, contrast, target size, and assistive-technology meaning.
- Account for realistic content lengths and every relevant interaction state.
- Do not bundle unrelated cleanup, refactoring, token changes, copy edits, or dependency upgrades into the design change.
- Keep the diff small, readable, reversible, and consistent with repository conventions.

Do not update visual baselines merely to make a failing check pass. Inspect each changed image and confirm that it belongs to the authorized delta; baseline acceptance is separate from implementation.

## Verify the result and its containment

Do not call a scoped change complete until both the requested delta and the protected surfaces have evidence.

Use the smallest complete set of checks that proves the result:

1. Compare before and after under matched data, state, viewport, theme, locale, and browser conditions.
2. Verify the requested change in every relevant state and responsive context.
3. Inspect representative protected neighbors and downstream consumers. If shared code changed, cover every materially distinct consumer pattern.
4. Exercise interaction, keyboard navigation, focus, reduced motion, contrast, zoom or text scaling, overflow, truncation, and assistive semantics as relevant.
5. Run the repository's applicable tests, type checks, linting, formatting, accessibility checks, and visual-regression checks.
6. Inspect the final file list and diff for unintended selector, token, asset, dependency, snapshot, content, and behavior changes.
7. Review screenshots at useful sizes. Screenshots prove appearance, not behavior, so pair them with interaction checks where needed.

If the runtime, browser, representative data, or a required check is unavailable, use the strongest available evidence and report the exact verification gap. Do not claim that unaffected surfaces are preserved beyond what was actually inspected and tested.

## Critique and report

Review the rendered result, not only the source:

- Is the user's task clearer or easier?
- Does hierarchy still work in every relevant state and width?
- Does the change belong to the existing product?
- Did any shared decision drift outside the authorized delta?
- Is any decoration doing work that content, structure, or interaction should do instead?
- Does the implementation remain understandable and maintainable?

Lead the final response with the outcome. State concisely:

- what changed;
- what was intentionally preserved;
- which states, viewports, consumers, and checks were verified;
- any remaining uncertainty or skipped verification.

Avoid an aesthetic essay when the user asked for a production change. The final standard is a deliberate interface that works, fits its product, and changes no more than intended.
