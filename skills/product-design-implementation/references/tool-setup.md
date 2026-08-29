# Official setup paths

Use these only after repository discovery. Prefer the project's existing package manager, version policy, SDK, CI, and tool conventions. Adding a dependency or external service still requires the authority normally expected for that project.

Tool documentation changes. Open the official page before presenting commands, state the version observed, and adapt rather than blindly pasting a latest-version command into a pinned project.

## Git and GitHub

1. Install Git using the operating-system route listed by [Git](https://git-scm.com/downloads).
2. Verify `git --version`, then `git rev-parse --show-toplevel` and `git status --short` in the target repository.
3. For GitHub review/CI only, install and authenticate the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli/quickstart), then verify with `gh auth status` without exposing tokens.

GitHub is conditional; local Git is the canonical requirement.

## Web runtime: Playwright and axe

1. Read the project's lockfile and existing test setup. If Playwright exists, use its pinned package-manager script.
2. Otherwise review [Playwright installation](https://playwright.dev/docs/intro), propose the development dependency, and wait for dependency approval when required.
3. Install only the browser projects required by the target; verify with the repository package manager's `playwright --version` and browser-list/test command. See [browser installation](https://playwright.dev/docs/browsers).
4. Add a deterministic smoke test against the real app start command; verify one browser before expanding the matrix.
5. For automated accessibility, follow [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing): add `@axe-core/playwright`, scan the required states, and assert on results.
6. Record keyboard, zoom/reflow, focus, and assistive-technology checks separately; axe does not replace them.

Playwright MCP is optional. If interactive exploration materially helps, configure it from the [official MCP guide](https://playwright.dev/docs/getting-started-mcp), verify one harmless navigation, and keep normal tests authoritative.

## Web workbench: Storybook

1. First look for `.storybook`, story files, and existing scripts.
2. Add Storybook only when a reusable component system or hard-to-reach states justify it; a checked-in fixture route may be enough.
3. Follow [Storybook installation](https://storybook.js.org/docs/get-started/install) with the project's package manager and supported framework version.
4. Create stories for the contract states, run the local workbench, and build it in CI.
5. Treat Storybook MCP as optional discovery; story source and runtime renders remain canonical.

## Mobile runtime: Maestro

1. Install the current Maestro CLI using the OS-specific route in the [official quickstart](https://docs.maestro.dev/get-started/quickstart).
2. Verify `maestro --version`.
3. Configure and boot an Android emulator or iOS simulator, install the app, and verify the target appears in the device list.
4. Add one checked-in YAML flow that launches the app and asserts a stable element, then run it through the normal CLI.
5. Use [`assertScreenshot`](https://docs.maestro.dev/reference/commands-available/assertscreenshot) only against a human-approved reference; `takeScreenshot` alone is capture evidence, not a protected assertion.
6. If live agent interaction is useful, Maestro CLI already provides the MCP server. Follow the [Maestro MCP guide](https://docs.maestro.dev/getting-started/maestro-mcp), configure `maestro mcp`, and verify `list_devices`. The CLI flow remains authoritative.

## Apple: Xcode, previews, tests, and accessibility

1. Install a project-supported Xcode release from [Apple](https://developer.apple.com/xcode/) and select its command-line tools.
2. Verify `xcodebuild -version`, resolve the project/workspace, list schemes, and boot a supported simulator.
3. Use [Swift previews](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode) for representative UIKit/SwiftUI states and Dynamic Type/color-scheme/orientation variants.
4. Run the existing XCTest/XCUITest scheme in the simulator.
5. Open Xcode > Open Developer Tool > Accessibility Inspector, select the running app, inspect required states, and run audits following [Apple's audit guide](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app).
6. Add `XCUIApplication.performAccessibilityAudit` where supported, then manually exercise VoiceOver and required system settings. A clean automated audit is not accessibility certification.

## Android: Android Studio, UI tests, and accessibility

1. Install the project-supported Android Studio/SDK from [Android Developers](https://developer.android.com/studio/install).
2. Verify the JDK/SDK through the project's Gradle wrapper, list tasks, and boot a supported emulator.
3. Use existing Compose previews or View layout fixtures; do not migrate between UI systems as setup.
4. Run Compose UI tests or instrumentation/Espresso tests through the existing Gradle tasks.
5. Follow [Android accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing). For Compose, use the current [Compose accessibility-check guidance](https://developer.android.com/develop/ui/compose/accessibility/testing); for Views, enable Espresso AccessibilityChecks.
6. Manually exercise TalkBack, font/display scaling, orientation/window size, and applicable switch/voice input.

## React Native and Expo workbench

1. Verify the project's Node/package-manager, Metro/Expo or native CLI, iOS pods, and Android Gradle setup.
2. Use the existing device build scripts and Maestro/native tests.
3. If a state workbench is justified, follow [React Native Storybook getting started](https://storybookjs.github.io/react-native/docs/intro/getting-started/) and prefer its separate entry-point mode so Storybook code does not ship in production.
4. Verify iOS and Android workbench entry points and the same deterministic fixtures used by production components.

## Flutter and Widgetbook

1. Install a project-supported Flutter SDK using [Flutter installation](https://docs.flutter.dev/get-started/install), then run `flutter doctor` and resolve only target-relevant failures.
2. Run the existing analyze, widget, integration, and device commands.
3. Add semantics/guideline tests and manual platform inspection using [Flutter accessibility testing](https://docs.flutter.dev/ui/accessibility/accessibility-testing).
4. Add Widgetbook only for a real reusable catalog. Follow the current [Widgetbook quick start](https://docs.widgetbook.io/quick-start), keep the catalog separate from production entry points, and verify its build.

## Tokens and Penpot

1. If the repository already uses generated multi-platform tokens, install its pinned compiler and run the existing generation/check script.
2. For a new justified multi-output setup, review [Style Dictionary installation](https://styledictionary.com/getting-started/installation/) and obtain dependency approval before adding it.
3. Keep Git-owned token source canonical and review generated diffs.
4. For exact editable design context, use a human-supplied Penpot export or configure the [official Penpot MCP](https://help.penpot.app/mcp/). Verify read-only access to the intended file/layer before requesting write access. Never use it to accept a baseline.

## Conditional review and device services

These create external state, may expose proprietary builds, and may involve accounts or participants. Explain scope and obtain explicit authorization before setup or upload.

### Cloudflare review preview

1. Prefer an existing hosting preview. Otherwise choose Git integration or Direct Upload after reading [Cloudflare Pages getting started](https://developers.cloudflare.com/pages/get-started/); the choice has project-level consequences.
2. For Git integration, authorize the minimum repository and configure the documented build command/output directory.
3. For Direct Upload, follow [Wrangler setup](https://developers.cloudflare.com/pages/get-started/direct-upload/), authenticate, create a project, and deploy only a prebuilt candidate directory to a preview branch.
4. Verify the returned preview maps to the candidate Git ref. Do not deploy production as a design check.

### Firebase Test Lab

1. Create/select a Firebase project and register the exact app.
2. Install/authenticate the Google Cloud CLI, set the project, and inspect available devices.
3. Build a supported native test artifact and define a small matrix following [Firebase Test Lab](https://firebase.google.com/docs/test-lab).
4. Run one virtual target first, then approved physical targets; retain result links and state identity. Test Lab usage is evidence, not user validation.

### Firebase App Distribution

1. Register the exact app/package in Firebase and enable App Distribution.
2. Build and sign the intended pre-release artifact.
3. Install/authenticate the Firebase CLI and verify project/app access.
4. Follow the platform-specific [App Distribution documentation](https://firebase.google.com/docs/app-distribution), invite only approved testers/groups, and upload only after explicit authorization.
5. Pair distribution with a named task and consented feedback plan. Installation/download counts do not prove usability.

### Clarity and Lyssna

Do not install analytics or recruit/contact participants as an implementation convenience.

For Clarity, first approve the decision question, consent/legal basis, retention, masking, population restrictions, and performance budget. Then follow [Clarity setup](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup) or the applicable mobile SDK guide and verify masking with non-sensitive test data.

For Lyssna, first approve the research question, target participants, recruitment source, tasks, data handling, and spend. Create the smallest suitable study from the [Lyssna help center](https://help.lyssna.com/en/); the free plan and self-recruited limits must be rechecked before promising capacity.

