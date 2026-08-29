# Apple review adapter

## Identify the real surface

Inspect Xcode projects/workspaces, schemes, deployment targets, SwiftUI/UIKit ownership, token/asset sources, previews, XCTest/XCUITest, snapshot tests, and build identity. A preview or design canvas is not the shipped app.

## Runtime matrix

Run the exact candidate on supported simulators/devices. Cover representative size classes, orientation/multitasking, safe areas, light/dark/high contrast, Dynamic Type through accessibility sizes, reduced motion/transparency, locale/RTL where required, hardware keyboard/pointer, loading/errors/permissions/recovery, and navigation state restoration.

Use Swift previews to inspect deterministic component states, then verify the actual app. Run existing XCTest/XCUITest and relevant Maestro flows without record/update modes.

Run Accessibility Inspector/current XCTest audits on each required screen. Manually exercise VoiceOver, Voice Control/Switch Control where relevant, Dynamic Type, reduced motion, and keyboard focus. Record audit limits.

## Drift and screenshots

Look for duplicated SwiftUI/UIKit components, hard-coded appearance values outside the canonical theme/tokens, inconsistent navigation/sheet conventions, platform variants with no contract, and missing large-text/error states.

An active native snapshot assertion may be asserted. Xcode preview images, simulator screenshots, XCTest attachments, or exported App Store images are capture-only unless an active deterministic comparison and accepted reference identity are proven.

