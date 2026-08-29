# Apple implementation adapter

## Detect ownership

Inspect Xcode projects/workspaces, schemes, package dependencies, deployment targets, and imports. Determine whether the requested UI is SwiftUI, UIKit, a deliberate mixture, or a wrapped web view. Do not migrate UIKit to SwiftUI, or the reverse, as a design implementation shortcut.

## Implement

- Extend established views/view controllers, navigation, dependency injection, localization, asset catalogs, and token generation.
- Prefer native controls and layout systems. Preserve state restoration, deep links, keyboard behavior, safe areas, sheets/popovers, and platform conventions.
- Model loading, empty, error, offline/retry, permissions, disabled/selected/focus, and long/localized content.
- Support Dynamic Type, right-to-left layout where required, light/dark/high-contrast appearances, reduced motion/transparency, orientation and size classes, pointer/keyboard on iPad, and safe-area changes.
- Give actionable elements stable accessibility labels, values, traits, hints only where useful, and logical focus order. Avoid flattening meaningful children or exposing decorative elements.

## Workbench and runtime

Use `#Preview` configurations for SwiftUI and UIKit states when the project supports them. Previews accelerate state craft but do not replace a built app.

Run the existing XCTest/XCUITest scheme on a supported simulator and exercise the normal app. Use Maestro for cross-platform black-box flows when established, but keep native tests for platform-specific semantics and physical Test Lab needs.

Run Accessibility Inspector/current XCTest accessibility audits on required screens and manually exercise VoiceOver, Dynamic Type accessibility sizes, Voice Control/Switch Control when relevant, reduced motion, and keyboard focus. A clean audit does not certify accessibility.

## Baselines

Treat native snapshot references and approved device images as protected. A simulator screenshot or attachment is capture-only unless a deterministic assertion compares it to an accepted golden. Never re-record snapshot references here.

