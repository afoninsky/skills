# Shared web-wrapper review adapter

Use this for Capacitor, Cordova, Tauri mobile, or another native shell packaging a web application.

## Prove the sharing model

Trace the configured web build directory, sync/copy command, native projects, plugins/bridges, and package identity. Identify the canonical web UI source and native-shell-only concerns. Do not count wrapper directories as separate UI implementations unless source proves that they are.

## Review both layers

1. Review the shared UI in real browsers with the full web adapter: components, responsive matrix, semantics, routes, offline/cache behavior, and asserted web goldens.
2. Review the exact packaged build on simulator/device: launch/splash, WebView/font rendering, safe areas/cutouts/status bars, IME/keyboard, back/deep/external links, plugins/permissions, cached assets, text/display scaling, and platform accessibility.

A browser mobile project cannot prove the packaged app. One device smoke cannot replace the browser/state matrix. Bind the packaged build to the same source ref and verify wrapper sync is current.

## Drift and screenshot evidence

Trace shared token/component changes to every browser route and packaged target. Look for shell-specific CSS or platform injection that creates an undocumented visual system.

Classify web and device images independently. A Playwright asserted golden does not automatically protect WebView output; a Maestro asserted golden does not protect responsive browser states. Capture-only images in either layer remain capture-only.
