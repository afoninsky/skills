# Web implementation adapter

## Detect ownership

Identify the actual framework and rendering mode from package/workspace manifests and imports: React/Next/Remix, Vue/Nuxt, Svelte/SvelteKit, Angular, Web Components, server templates, or mixed islands. Detect SSR/CSR/static rendering, PWA/service-worker behavior, shared packages, CSS/token authority, route ownership, and existing test scripts. Follow the repository; do not replace its stack with a preferred framework.

## Implement

- Reuse the existing component, styling, state, form, routing, localization, and data-loading patterns.
- Prefer semantic HTML and framework primitives over div-based replicas or positioned screenshot tracing.
- Keep tokens semantic. Inventory cascade layers, root/theme declarations, CSS import order, CSS-in-JS providers, and generated token outputs before touching shared style.
- Exercise real copy extremes, loading/empty/error/retry, permissions, disabled/selected/focus/hover/pressed, and navigation states from deterministic fixtures.
- Preserve SSR/hydration, caching, deep links, back/forward behavior, and service-worker semantics when relevant.

## Workbench and runtime

Use an existing Storybook/catalog or checked-in component fixture. Add Storybook only when a reusable system and repeated hard-to-reach states justify the dependency.

Use Playwright against the normal app command for required desktop/tablet/phone widths and browser projects. Browser device emulation is web evidence, not proof of a packaged/native app. Capture console, network, and trace evidence when the change touches loading or integration.

Pair Playwright with axe for automated findings, then cover keyboard-only operation, visible focus, zoom/reflow, text spacing/scaling, reduced motion, forced colors/high contrast, and an applicable screen reader manually. Do not call a clean axe scan accessibility validation.

## Baselines

`expect(...).toHaveScreenshot(...)` is an asserted golden. `page.screenshot(...)`, a browser-tool screenshot, or a CI artifact without comparison is capture-only. Never run Playwright with snapshot-update flags in this worker.

