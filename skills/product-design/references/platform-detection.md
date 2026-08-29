# Platform detection

Load this reference only for a real repository or specified target.

## Inspect first

Identify:

- app/workspace boundaries and build graph;
- framework and UI rendering layer;
- package manager and test runner;
- design token authorities and generated outputs;
- web-to-mobile wrappers or shared component packages;
- existing component workbench/previews;
- browser, simulator/emulator, and device tests;
- supported OS versions, window classes, orientation, input, theme, locale, and accessibility settings.

Do not infer separate UI trees from separate deployable apps.

## Adapter map

| Architecture | State workbench | Runtime evidence | Adaptive/accessibility concerns |
|---|---|---|---|
| React/Vue/Svelte/Angular/Web Components | existing state route or Storybook | Playwright | browsers, reflow/zoom, keyboard/pointer/touch, forced colors |
| React Native | RN Storybook when justified | Maestro plus native tests | safe areas, keyboard, font scale, orientation, platform behavior |
| Flutter | Widgetbook or widget tests | Maestro plus Flutter/native tests | constraints, text scale, semantics, orientation, platform adaptation |
| SwiftUI/UIKit | Xcode previews and XCTest | Maestro simulator plus XCTest/XCUITest | size classes, Dynamic Type, VoiceOver, safe areas, input |
| Compose/Android Views | Compose previews/UI Check or layout fixtures | Maestro plus instrumentation | window classes, insets, font/display scale, TalkBack, input |
| PWA/Capacitor/other web wrapper | one web component source plus shell fixtures | Playwright for UI; Maestro/device smoke for packaged app | responsive web plus WebView, safe area, keyboard, native bridge |

If the repository has an equivalent established tool, compare its evidence with the approved capability before proposing a new dependency.

