# React Native implementation adapter

## Detect ownership

Inspect React Native/Expo versions, Metro or Re.Pack config, router/navigation, native iOS/Android directories, design-system packages, platform extension files, and build profiles. Determine what is shared JavaScript/TypeScript, intentionally platform-specific, or a native module. Do not create duplicate native screens for shared UI unless the architecture already requires them.

## Implement

- Extend the established components, style/token layer, state/data model, navigation, localization, and platform overrides.
- Use React Native primitives or the project's accessible component library. Avoid web-only assumptions in native views.
- Model loading, empty, error, offline/retry, permissions, disabled/selected/focus/pressed, keyboard open, and long/localized content.
- Support safe areas, phone/tablet constraints, orientation, text and display scaling, RTL where required, light/dark/high-contrast settings, reduced motion, hardware keyboard/focus, and platform-specific control differences.
- Provide accessible names, roles, states, values, hints only where useful, and logical traversal/grouping on both platforms.

## Workbench and runtime

Use existing React Native Storybook or deterministic in-app fixture states. If adding Storybook is justified, prefer a development-only entry point that does not ship in production.

Build and run both claimed platforms. Use Maestro YAML for shared black-box journeys and screenshots; use existing native/unit/component tests for platform-specific behavior. A web-rendered React Native story does not prove the native runtime.

Run platform accessibility automation/inspection and manually exercise TalkBack/VoiceOver, text scaling, safe areas, keyboard behavior, and required input modes on each claimed platform.

## Baselines

Protect platform-specific goldens. `takeScreenshot` and simulator captures are evidence only; `assertScreenshot` or a native snapshot assertion identifies a protected golden. Never update either baseline set here.

