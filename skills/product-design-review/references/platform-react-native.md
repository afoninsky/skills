# React Native review adapter

## Identify the real surface

Inspect React Native/Expo version, Metro/Re.Pack, router/navigation, shared components/tokens, platform extension files, native directories/modules, Storybook/fixtures, tests, build profiles, and candidate identity. Determine what is shared versus intentionally platform-specific.

## Runtime matrix

Run both claimed native platforms. Cover phone/tablet constraints, orientation, safe areas, text/display scaling, keyboard open, light/dark/high contrast, reduced motion, locale/RTL where required, focus/pointer/hardware keyboard, permissions/offline/recovery, and platform control differences.

Use existing React Native Storybook for deterministic component states but verify the installed app. Run Maestro shared journeys and existing native/unit/component tests. A React Native Web render does not prove iOS/Android.

Inspect accessibility separately with Apple and Android tools and manually exercise VoiceOver/TalkBack. Compare accessible name/role/state/value, traversal/grouping, target sizes, and text scaling on both platforms.

## Drift and screenshots

Look for inconsistent shared/platform overrides, duplicated native screens, token copies diverging between JavaScript and native code, safe-area/keyboard workarounds, and one-platform-only state coverage.

Maestro `assertScreenshot` or active native snapshot assertions may be asserted. `takeScreenshot`, simulator captures, workbench exports, and attachments are capture-only.

