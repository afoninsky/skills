# Android review adapter

## Identify the real surface

Inspect Gradle modules/source sets, Compose/View ownership, resources/themes, navigation, previews/layout fixtures, instrumentation/Compose UI tests, snapshot tests, and candidate build identity. A Compose preview or layout editor is not the installed app.

## Runtime matrix

Run the exact candidate on supported emulator/device configurations. Cover window size classes, orientation/multi-window, font/display scaling, insets/cutouts and edge-to-edge, IME/keyboard, light/dark/high contrast, locale/RTL where required, loading/errors/permissions/recovery, and TalkBack/focus traversal.

Use previews/UI Check for component-state inspection, then verify the installed app. Run Compose UI or instrumentation/Espresso and relevant Maestro flows without golden-update modes.

Use current Compose accessibility checks or Espresso AccessibilityChecks as applicable, then manually exercise TalkBack, font/display scaling, and relevant switch/voice/keyboard input. Record coverage limits.

## Drift and screenshots

Look for competing Material/themes/resources, literals bypassing token generation, duplicate Compose/View component families, undocumented platform variants, and missing adaptive/state coverage.

An active screenshot assertion with accepted reference may be asserted. Compose preview images, emulator screenshots, test attachments, and Maestro `takeScreenshot` are capture-only without active comparison.

