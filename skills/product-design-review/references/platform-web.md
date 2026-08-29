# Web review adapter

## Identify the real surface

Inspect manifests and runtime to determine framework/rendering mode, route ownership, shared packages, CSS/token providers, PWA/service worker, workbench/fixtures, Playwright projects, and deployed-build identity. Follow existing architecture; do not interpret framework preference as a finding.

## Runtime matrix

Use Playwright or an equivalent real browser against the normal app command/deployment. Cover required Chromium/WebKit/Firefox or supported browser policy, representative desktop/tablet/phone widths, zoom/reflow, light/dark/forced-colors, reduced motion, keyboard/touch/pointer, locale/long content, and the contract states.

Inspect console/network/hydration and service-worker/offline behavior when relevant. Responsive emulation is web evidence, not packaged/native evidence.

Run axe on the reached states, then exercise keyboard-only operation, visible focus, zoom/reflow, text spacing/scaling, and applicable VoiceOver/NVDA/TalkBack. Static semantics or axe alone cannot support “accessible.”

## Drift signals

Look for competing `:root`/theme providers, literal values, import/cascade precedence, global overrides, duplicate component implementations, page-local token systems, SSR/client divergence, and missing state stories/fixtures. Distinguish intentional brand/theme variants from accidental override order.

## Screenshot classification

Playwright `expect(...).toHaveScreenshot(...)` in an executed test may be asserted. `page.screenshot(...)`, browser screenshots, trace attachments, or image artifacts without comparison are capture-only. Confirm the test did not run with update mode and that the baseline identity is accepted.

