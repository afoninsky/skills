# Platform adapters

Load only the row matching the detected implementation architecture. Prefer the repository's current stack and state harness.

| Architecture | Canonical UI/state source | Runtime evidence | Adaptive and accessibility checks |
| --- | --- | --- | --- |
| Web framework | Existing components plus stories/fixture route | Playwright browser projects and asserted screenshots | Breakpoints, intermediate widths, zoom/reflow, pointer/keyboard/touch, axe plus manual keyboard/screen reader |
| React Native | RN components plus RN Storybook or fixtures | Maestro plus native tests | Phone/tablet, orientation, safe areas, software keyboard, font scaling, TalkBack/VoiceOver |
| Flutter | Widgets plus Widgetbook or widget tests | Maestro plus Flutter/native tests | Constraints, orientation, text scaling, semantics/guideline checks, TalkBack/VoiceOver |
| SwiftUI/UIKit | App source plus Xcode previews/configurations | XCTest/XCUITest and Maestro simulator flow | Size classes, Dynamic Type, safe areas, keyboard/input, Accessibility Inspector, VoiceOver/reduced motion |
| Compose/Android Views | Source plus Compose previews/UI checks or layout fixtures | Instrumentation/native tests and Maestro | Window classes, font/display scaling, insets, input, semantics/accessibility checks, TalkBack |
| PWA/Capacitor/web wrapper | One web component source plus native shell configuration | Playwright for UI; Maestro/device smoke for packaged app | Web reflow plus safe areas, keyboard, WebView/runtime differences, platform accessibility smoke |

## Detection rules

- Inspect build files, workspace layout, app entrypoints, package metadata, native project folders, and actual imports.
- Do not infer a separate native UI tree from an iOS/Android wrapper directory.
- If several applications share a token/component package, map every consumer before accepting a shared change.
- Do not introduce a preferred framework, workbench, or token compiler when the repository already has a viable equivalent.

## Baseline matrix

Each accepted entry needs a stable surface, state, target, environment/configuration, path, hash, and assertion or approval source. Examples of targets include desktop browser, compact phone browser, Android compact device, iPad size class, large-text mode, or a packaged WebView smoke. Select the smallest matrix that protects the actual contract; do not pretend one screenshot covers a platform family.
