# Shared web-to-native wrapper adapter

Use this for Capacitor, Cordova, Tauri mobile, or another architecture that packages a web application inside a native shell.

## Prove ownership first

Trace the wrapper's `webDir`/build output, sync/copy scripts, native entry points, plugin configuration, and route/deep-link handling. Identify:

- the one canonical web component/style tree;
- native shell code and assets;
- plugins/bridges and platform permissions;
- packaged build/version identity.

Do not create a parallel SwiftUI/Compose/Flutter/React Native UI because a mobile directory exists. Implement shared UI in the web owner. Touch native shell code only when the approved slice requires shell behavior.

## Two-layer verification

Both layers are active:

1. Use the web adapter and Playwright/axe to verify components, responsive behavior, browser semantics, and most visual states quickly.
2. Build/sync the real wrapper and use Maestro/native tooling to verify app launch, safe areas/cutouts, status/navigation bars, keyboard/IME, deep links, external links, back behavior, permissions/plugins, offline/cache behavior, WebView/font differences, text scaling, and platform accessibility.

Browser mobile emulation does not prove the packaged app. Conversely, one device smoke does not replace the browser matrix for a shared UI.

## Preservation

Record which web change affects both browser and packaged app surfaces. A shared token/component expands preservation checks to every dependent route and the packaged target. Keep browser and device candidate captures separate and protect both baseline families from updates.
