# Protected-change platform adapters

Load only the applicable row and reuse the project's established harness.

| Architecture | Implement in | Required preservation loop |
| --- | --- | --- |
| Web React/Vue/Svelte/Angular/Web Components | Existing components/tokens/styles | Playwright affected and protected projects; breakpoints/intermediate widths; keyboard/touch/pointer; axe/manual checks |
| React Native | Existing RN component/token tree | RN state fixtures when present; Maestro and native tests; phone/tablet, orientation, safe areas, keyboard, font scaling, TalkBack/VoiceOver |
| Flutter | Existing widget/theme tree | Widget tests/Widgetbook when present; Maestro/native tests; constraints, text scaling, orientation, semantics/guidelines |
| SwiftUI/UIKit | Existing view/style source | Previews plus XCTest/XCUITest/Maestro simulator; size classes, Dynamic Type, insets, input, Accessibility Inspector/VoiceOver |
| Compose/Android Views | Existing composable/view/resource source | Preview/UI checks plus instrumentation/Maestro; window classes, font/display scaling, insets, semantics/TalkBack |
| PWA/Capacitor/web wrapper | Shared web source, not a duplicate native view | Playwright for UI plus packaged-app Maestro/device smoke for safe-area, keyboard, WebView, plugin/runtime differences |

For a semantic token or shared component, union all mapped adapters. The required matrix follows the impact graph, not the platform named in the prompt.
