# Official setup and access paths for review

Open the current official documentation before presenting commands. Respect the repository's pinned versions, package manager, SDK, and CI. Setup that adds dependencies, creates deployments, uploads builds, instruments production, accesses sensitive sessions, contacts people, or spends money requires explicit authorization.

These are instructions for the owner or a separately authorized setup action. The read-only review worker presents the tailored steps and stops before executing any mutating step, even when the owner chooses setup. After setup is completed outside review, start a new review run, re-probe capabilities, and freeze the target identity again before collecting evidence. Do not add dependencies or tests, change project configuration, connect services, publish, upload, instrument, recruit, or spend from the review worker.

## Git and target identity

1. Install Git through [Git's official downloads](https://git-scm.com/downloads).
2. Verify `git --version`, repository root, HEAD, and dirty status.
3. For GitHub checks/artifacts only, follow the [GitHub CLI quickstart](https://docs.github.com/en/github-cli/github-cli/quickstart) and verify `gh auth status` without exposing credentials.

## Web runtime, screenshots, and accessibility

1. Inspect existing Playwright config/scripts and use the pinned package manager.
2. If absent, review [Playwright installation](https://playwright.dev/docs/intro), propose the development dependency, and obtain dependency approval.
3. Install only required browser binaries using the current [browser guide](https://playwright.dev/docs/browsers); verify version and list/run one smoke test.
4. Add or run state-specific screenshot assertions following [Playwright snapshots](https://playwright.dev/docs/test-snapshots). Never invoke update mode during review.
5. Add/run `@axe-core/playwright` using [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing), then plan keyboard, zoom/reflow, focus, and applicable screen-reader checks.
6. Playwright MCP from the [official guide](https://playwright.dev/docs/getting-started-mcp) is optional for live exploration; normal tests and artifacts remain authoritative.

## Web component workbench

1. Look for an existing `.storybook`, catalog route, or component fixtures.
2. Add Storybook only if repeated component-state review justifies a dependency; follow [Storybook installation](https://storybook.js.org/docs/get-started/install).
3. Verify stories for the required states and build the workbench. An image exported from it is capture-only unless an active test compares it.

## Mobile runtime with Maestro

1. Follow the current OS-specific [Maestro quickstart](https://docs.maestro.dev/get-started/quickstart); verify `maestro --version`.
2. Configure/boot the target simulator or emulator, install the exact candidate build, and verify device/app identity.
3. Run a checked-in deterministic flow. [`assertScreenshot`](https://docs.maestro.dev/reference/commands-available/assertscreenshot) can protect an accepted image; `takeScreenshot` is capture-only.
4. For useful live inspection, configure the CLI's MCP server through [Maestro MCP](https://docs.maestro.dev/getting-started/maestro-mcp) and verify `list_devices`. MCP remains optional when the CLI evidence path works.

## Apple runtime and accessibility

1. Install a project-supported [Xcode](https://developer.apple.com/xcode/) and select command-line tools.
2. Verify `xcodebuild -version`, workspace/project, scheme, simulator, and candidate build identity.
3. Use [Swift previews](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode) only as component-state evidence; run the actual app for acceptance.
4. Run existing XCTest/XCUITest without record/update modes.
5. Open Xcode > Open Developer Tool > Accessibility Inspector, target the running app, and follow [Apple accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app). Add/currently run automated audits where supported and manually use VoiceOver and required system settings.

## Android runtime and accessibility

1. Install the project-supported Android Studio/SDK using [Android Studio setup](https://developer.android.com/studio/install).
2. Verify the project's Gradle wrapper, list tasks, boot a supported emulator, and bind the installed candidate to its build/ref.
3. Run Compose UI or instrumentation/Espresso tests without golden-update modes.
4. Follow [Android accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing), including current [Compose accessibility checks](https://developer.android.com/develop/ui/compose/accessibility/testing) or Espresso AccessibilityChecks.
5. Manually exercise TalkBack, font/display scaling, orientation/window size, and relevant input methods.

## React Native and Flutter

For React Native/Expo, verify Metro/Expo/native build tools and both claimed platform builds. Use an existing Storybook or follow [React Native Storybook](https://storybookjs.github.io/react-native/docs/intro/getting-started/) only if a state catalog is genuinely needed. Run Maestro plus native accessibility tools on each claimed platform.

For Flutter, install the project-supported SDK through [Flutter installation](https://docs.flutter.dev/get-started/install), run `flutter doctor`, existing tests, and actual target builds. Follow [Flutter accessibility testing](https://docs.flutter.dev/ui/accessibility/accessibility-testing). Add Widgetbook only if justified, using the [Widgetbook quick start](https://docs.widgetbook.io/quick-start).

## Penpot and token compilers

For exact editable source context, request an approved export or configure read-only access via the [official Penpot MCP](https://help.penpot.app/mcp/). Verify the intended file/layer. Never edit or accept from review.

If multi-platform tokens are generated, install the repository's pinned compiler and run check/read-only comparison. For a new justified setup, review [Style Dictionary installation](https://styledictionary.com/getting-started/installation/) and route the dependency decision outside review.

## Conditional share/device services

### Cloudflare preview

Prefer an existing preview. Otherwise choose an approach from [Cloudflare Pages getting started](https://developers.cloudflare.com/pages/get-started/) only after upload/deployment approval. Configure the documented build/output through Git integration or [Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/), deploy to preview rather than production, and bind its URL to the reviewed ref.

### Firebase Test Lab

Create/select and register the exact app, install/authenticate the Google Cloud CLI, define a small approved device matrix, and follow [Firebase Test Lab](https://firebase.google.com/docs/test-lab). Start with one virtual target before consuming physical-device quota. Results are device evidence, not user validation.

### Firebase App Distribution

Follow [Firebase App Distribution](https://firebase.google.com/docs/app-distribution) after explicit build-upload and tester authorization. Register the exact app, build/sign the candidate, authenticate the Firebase CLI, invite only approved groups, upload, and pair the build with a named task/feedback protocol. Distribution itself proves only access.

## User and post-launch evidence

### Microsoft Clarity

Do not instrument production during review. First resolve the decision question, consent/legal basis, population restrictions, masking/redaction, retention, sensitive-data boundaries, and performance budget. Then an authorized owner can follow [Clarity setup](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup) or the applicable mobile SDK guide. Verify masking using non-sensitive test data before collection. The reviewer should receive scoped read-only access or sanitized observations.

### Lyssna or moderated research

Do not create studies, recruit, contact, or purchase participants during review. First approve the research question, target population, method/tasks, sample, recruitment, consent/data handling, and budget. Use the current [Lyssna help center](https://help.lyssna.com/en/) or an equivalent moderated process. Recheck free-plan visibility limits before promising sample capacity. Store only consented, minimized findings.
