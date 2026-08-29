# Android implementation adapter

## Detect ownership

Inspect Gradle modules, manifests, source sets, themes/resources, navigation, and imports. Determine whether the slice uses Jetpack Compose, Android Views/XML, a deliberate mixture, or a wrapped web view. Do not migrate UI systems as part of realizing a design.

## Implement

- Extend established composables/views, navigation, state holders, resources, localization, and token generation.
- Prefer Material/platform primitives when they fit the approved contract; customize through the existing theme rather than duplicating a page-local system.
- Model loading, empty, error, offline/retry, permissions, disabled/selected/focus/pressed, and long/localized content.
- Support window size classes or existing adaptive layout rules, orientation/multi-window, font and display scaling, insets/cutouts, edge-to-edge, IME/keyboard, dark/high-contrast modes, and right-to-left layout where required.
- Expose meaningful semantics/content descriptions, roles/state descriptions, traversal order, actions, and target sizes. Avoid duplicate announcements and descriptions on decorative imagery.

## Workbench and runtime

Use Compose previews with deterministic parameters or existing View layout fixtures. UI Check/previews accelerate state inspection but do not replace an installed app.

Run the project's Compose UI tests or instrumentation/Espresso suite on a supported emulator. Maestro may cover shared black-box journeys; retain native checks for semantics and platform behavior.

Enable the current Compose accessibility checks or Espresso AccessibilityChecks as applicable. Manually exercise TalkBack, font/display scaling, switch/voice access when relevant, orientation/window changes, and keyboard/focus behavior. Automated checks are incomplete.

## Baselines

Protect screenshot-test goldens and approved device images. A screenshot attachment or Maestro `takeScreenshot` remains capture-only without a deterministic assertion. Never re-record references here.

