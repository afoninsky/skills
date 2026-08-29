# Platform adapters and verification

Detect the actual rendering architecture before loading one adapter. Prefer an established equivalent already in the project.

## Responsive web

- Use a disposable HTML/CSS/JS project for a stand-alone concept or an isolated route/workbench when existing components are part of the question.
- Use Storybook only when the project has or justifiably needs a reusable state catalog; do not add it for one small static page.
- Use Playwright for exact viewports, flow repetition, screenshots, console/network checks, keyboard/focus, zoom/reflow, and axe integration.
- Verify phone, intermediate/tablet, desktop, long/translated content, pointer/touch/keyboard, and reduced-motion/forced-color concerns as relevant.
- Use a preview host only when required reviewers cannot run locally; tie the URL to a commit and avoid exposing secrets/test data.

## React Native

- Use an isolated screen/dev entry or React Native Storybook when already appropriate.
- Run in the actual native app runtime; a browser-only React approximation cannot prove RN layout or behavior.
- Use Maestro for the critical device flow and native tests for semantics or platform-specific behavior where needed.
- Check phone/tablet, iOS/Android conventions, safe areas, keyboard, orientation, font scaling, screen-reader labels, and back behavior.

## Flutter

- Use an isolated route/widget test or Widgetbook when a reusable catalog adds value.
- Run with Flutter's real constraints and fonts; use Maestro for black-box flow plus Flutter tests for semantics/guideline checks.
- Check phone/tablet, orientation, text scaling, safe areas/insets, Material/Cupertino adaptation, platform back behavior, and localization.

## SwiftUI/UIKit

- Use `#Preview`/preview configurations for isolated states and Simulator for real navigation, keyboard, animation, permissions, or lifecycle.
- Use XCTest/XCUITest for deterministic behavior/semantics where needed and Maestro for cross-platform black-box flow when appropriate.
- Check size classes, Dynamic Type, VoiceOver labels/order, safe areas, keyboard, reduced motion, appearance, orientation, and native control expectations.

## Compose/Android Views

- Use Compose previews/UI Check or isolated layout fixtures; use emulator/device for navigation, keyboard, animation, permissions, or lifecycle.
- Use Compose/instrumentation accessibility checks and Maestro for the black-box flow when appropriate.
- Check window classes, font/display scale, TalkBack semantics/order, insets, keyboard, orientation, back behavior, and native controls.

## PWA and web-wrapper mobile apps

- Identify whether one responsive web UI is packaged in a native shell. Reuse that source rather than creating a parallel native prototype.
- Verify UI logic in the real browser with Playwright, then smoke the packaged app with Maestro/device tooling for WebView, safe-area, keyboard, lifecycle, bridge, permissions, and native-back differences.
- Keep browser and packaged-shell evidence separate; neither proves the other automatically.

## Verification record

For each check record target/configuration, fixture, command/tool/version, expected result, actual result, artifact path, evidence label, and limitation.

Useful evidence for a representative slice:

- runnable real render/runtime tied to a ref/hash;
- a non-empty platform matrix with at least one configuration per materially distinct implementation/adaptation class and explicit exclusions;
- matched captures for every agreed target/state row;
- repeatable core-act and recovery flow;
- relevant large-text/localization/adaptive evidence;
- applicable semantics/accessibility risk result and manual plan;
- no production imports from prototype source;
- missing physical-device or representative-user evidence explicitly labeled when it limits a claim.

An MCP session can accelerate inspection, but CLI tests, preview source, screenshots, and recorded results are the durable evidence.
