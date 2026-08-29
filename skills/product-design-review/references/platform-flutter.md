# Flutter review adapter

## Identify the real surface

Inspect Flutter/workspace packages, router/state management, ThemeData/ThemeExtension/token generation, platform folders/flavors, Widgetbook/fixtures, widget/integration/golden tests, and candidate build identity. Determine shared Flutter, intentional adaptive widgets, Flutter web, and native shell ownership.

## Runtime matrix

Run every claimed target. Cover text scaling, phone/tablet constraints, orientation, safe areas/insets, keyboard, light/dark/high contrast, reduced motion, locale/RTL where required, focus/mouse/keyboard/touch, permissions/offline/recovery, and intentional Material/Cupertino differences.

Use Widgetbook or deterministic widget fixtures for states, then verify actual target builds. Run analyze/widget/integration tests and Maestro for mobile journeys. Flutter web also requires web runtime/accessibility review.

Run Flutter accessibility Guideline API tests, inspect semantics through platform tools, and manually exercise VoiceOver/TalkBack and text scaling. Automated guidelines cannot prove accessibility.

## Drift and screenshots

Look for duplicate ThemeExtensions, literals bypassing themes, custom-painted UI where semantics/state are lost, divergent platform copies, and missing constrained/text-scale states.

An active Flutter golden comparison may be asserted. Widgetbook images, emulator/simulator captures, Maestro `takeScreenshot`, and generic test attachments are capture-only.

