# Flutter implementation adapter

## Detect ownership

Inspect `pubspec.yaml`, workspace/package structure, router, state-management conventions, themes/extensions, generated assets/tokens, platform folders, flavors, and supported targets. Determine whether UI is shared Flutter, intentionally platform-adaptive, Flutter web, or embedded in native shells.

## Implement

- Extend the established widgets, theme extensions, state/data model, navigation, localization, and platform adaptations.
- Prefer composable real widgets over custom painting or positioned screenshot tracing unless the contract truly requires custom rendering.
- Model loading, empty, error, offline/retry, permissions, disabled/selected/focus/pressed, keyboard open, and long/localized content.
- Support text scaling, constrained widths, orientation, safe areas/insets, keyboard, RTL where required, light/dark/high-contrast modes, reduced motion, focus traversal, mouse/keyboard/touch, and intentional Cupertino/Material adaptation.
- Build a correct Semantics tree with labels, values, roles/actions, grouping, sort order, live regions where appropriate, and platform target sizes.

## Workbench and runtime

Use existing Widgetbook or deterministic widget fixtures. Add Widgetbook only for a reusable catalog; keep its app separate from the production entry point.

Run analyze/widget tests, contract-state tests, and the actual target runtime. Use Maestro for shared mobile journeys and native platform tools for semantics/accessibility. Flutter web additionally requires the web adapter and browser checks.

Use Flutter's accessibility Guideline API for labels, contrast, and target sizes, then inspect on Android/iOS and manually exercise TalkBack/VoiceOver and text scaling. Automated guidelines are partial.

## Baselines

Protect golden-test images and approved runtime references. Do not invoke golden-update modes. Candidate captures must use separate paths and remain unaccepted.

