# Product Design suite — TeachRelay integration pilot

Date: 2026-08-29  
Target inspected read-only: `/Users/drago/Documents/teachrelay/teachrelay`  
Frozen target: `fe9c88d12f8f74bdada638b59409247c195d9a66` on `master`  
Suite under test: `/Users/drago/Documents/skills/skills/product-design*`

## Outcome

The common entrypoint routes the original request correctly, but the honest full review must stop at capability preflight:

```text
Original request
  → product-design-review (read-only system/current-state review)
  → product-design-contract (re-architect mode; contract proposal only)
  → owner approves the proposed authority and migration slices
  → product-design-change for each approved protected slice
  → product-design-review
  → explicit product-design-contract accept-freeze only after human approval
```

The first durable route `product-design-review → product-design-contract` passes the router validator. The active review cannot presently make a cross-platform visual-acceptance claim because the current web acceptance path does not reach its screenshot assertion and the packaged Android runtime is unavailable. A source-only authority inventory is a useful alternate route, but it requires explicit confirmation and must leave runtime, mobile, fidelity, and preservation conclusions `Not evidenced`.

No tracked TeachRelay source, test, design, baseline, or configuration file was changed. The tracked tree was clean before and after the live probes. The Playwright probe ran the existing Vite build, so ignored `apps/web/dist` output may have been refreshed; that generated output is not a source mutation or a proven clean artifact. No real product change, accepted design, accessibility result, packaged-app result, usability result, or release result was verified by this pilot.

## Router decision

Pilot prompt:

> Review and re-architect TeachRelay's visual consistency across the web app and packaged mobile experience without changing production files.

Why review is first:

- This is an existing product with an observable implementation, not a new-product discovery request.
- The request begins with inspection and diagnosis; `product-design-review` owns that read-only work.
- There is no Product Design suite contract, source map, baseline manifest, toolchain record, or recovery state in `design/`.
- Without accepted identity, review may describe competing authorities and current inconsistency risk, but it cannot label a difference “drift from the accepted design.”
- `product-design-contract` in re-architect mode follows review and may propose one authority, explicit variants, a source map, migration slices, and rollback points. It cannot rewrite production CSS.

The validated route envelope is [`fixtures/route/envelope.json`](fixtures/route/envelope.json). Because a blocked handoff cannot recommend or launch a successor, the blocked active-worker envelope is separately represented by [`fixtures/route/envelope-blocked-review.json`](fixtures/route/envelope-blocked-review.json) and [`fixtures/route/handoff-blocked.json`](fixtures/route/handoff-blocked.json). The explicitly narrowed synthetic reroute is bound separately by [`fixtures/route/envelope-source-audit-confirmed-example.json`](fixtures/route/envelope-source-audit-confirmed-example.json); it intentionally has no platform-acceptance claims.

## Architecture detected

TeachRelay is a Bun workspace. The relevant product surface is Vue 3.5.39 with Vite 8.1.4 and Playwright 1.61.1. `apps/mobile` is Capacitor 8.5.0 for Android.

The mobile project is not a second UI implementation:

- `apps/mobile/capacitor.config.ts` sets `webDir: "../web/dist"`.
- `apps/mobile/package.json` builds `apps/web`, runs `cap sync android`, and then records provenance.
- Android adds shell/plugin behavior around the shared web UI.
- The Android project targets API 36, supports API 24+, and compiles with Java 21.

Therefore the suite must model one UI source and two evidence layers:

1. Playwright covers the full shared browser UI, routes, states, reflow, keyboard, and browser semantics.
2. Maestro plus Android/native checks cover the packaged WebView: sync/build identity, launch, safe areas, keyboard/IME, system back, deep/external links, native bridges/plugins, font rendering, text/display scale, and TalkBack-relevant behavior.

A shared component or CSS-token change must expand to both targets. It must not create a duplicate native component. The disposable source map and change-guard probe confirmed that one mapped `Card` edit expands to:

```json
{
  "platforms": ["android-wrapper", "web-ui"],
  "targets": ["android-webview-smoke", "chromium-desktop"],
  "states": ["default", "loading"],
  "surfaces": ["home"]
}
```

## Current source-authority inventory

This is source evidence, not a visual-quality verdict.

- `apps/web/src/styles.css` imports eight layers in order: shared base, dashboard, learning, shared mentorship, responsive, family, guided-thread refinement, and Relay Board.
- `packages/cabinet-ui/base.css` defines the first global root token system, including `--field: #e8f0f3` and its display/body/utility typography.
- Later, `apps/web/src/styles/family.css` defines another global `:root`, changes `--field` to `#edf3f1`, and changes typography and shape language.
- Last, `apps/web/src/styles/relay-board.css` introduces a route-scoped `--relay-*` system with a different display/body stack and visual grammar under `.learner-shell--relay`.
- `/` and `/past-learning` set `route.meta.relayShell`; `App.vue` changes shell branding/header behavior for those routes.
- The inspected styling sources total 5,049 lines across shared base, web styles, mentor styles, and the home app. Size is not itself a defect; it increases the need for a declared canonical authority and impact map.
- Commit `c6b4e60` added the Relay Board, 1,048 lines of its stylesheet, four committed verification images, and broad learner behavior changes. Commit `4264b8f` immediately followed to restore legacy goals on Relay Home. This history proves a broad surface change and a subsequent behavior correction, not the cause or quality of the visual design.

These may be intentional product variants. The repository lacks a compact accepted contract that tells the reviewer which differences are deliberate, which source wins semantically, and which consumers a shared edit must protect. That is the precise reason to follow review with contract re-architecture.

## Capability preflight

The exact machine-readable records are:

- [`toolchain-blocked.json`](fixtures/route/toolchain-blocked.json) — requested shared-wrapper visual-acceptance review; execution must stop.
- [`toolchain-source-audit-confirmed-example.json`](fixtures/route/toolchain-source-audit-confirmed-example.json) — historical synthetic example of an owner-confirmed, source-only reroute; it passed execution validation at the recorded probe time and makes no visual-acceptance claim.
- [`toolchain-contract-blocked.json`](fixtures/route/toolchain-contract-blocked.json) — next contract phase; it stops because the supported Python validator runtime is absent.

| Capability | Status | Probe/evidence | Consequence |
| --- | --- | --- | --- |
| Git identity and rollback | `available` | Git 2.55.0; clean `fe9c88d…` target | Read-only target can be frozen and compared. |
| Bun/project configuration | `available` | Bun 1.3.13; manifests and 60 Playwright tests discovered | Framework and test graph are inspectable. |
| Browser engine | `available` | Headless Chromium 149.0.7827.55 launched and rendered a disposable page | The browser binary works. This alone is not app acceptance. |
| Accepted contract/baseline identity | `missing-degradable` | No suite contract/source map/baseline manifest found | A confirmed current-source inventory is possible; accepted-design drift and preservation remain `Not evidenced`. |
| Web runtime plus deterministic visual path | `missing-blocking` for visual acceptance | The selected accepted-Home test built and ran, but failed before `toHaveScreenshot`: expected `Explain why seasons differ around the world`; `/` rendered `Your goals` | Current web visual preservation cannot be claimed. Source-only work is a different, explicitly confirmed route. |
| Packaged Android runtime/visual path | `missing-blocking` | `maestro`, `adb`, Java, device target, and checked-in Maestro flow are absent | WebView/mobile-shell consistency, safe-area, IME, back, bridge, and mobile visual claims are `Not evidenced`. |
| Contract/change validator runtime | `missing-blocking` for contract/change | System `python3` is 3.9.6; suite requires 3.10+ | No authoritative contract freeze or protected production change may start. |
| Semantic style source | `available`, fragmented | Committed CSS variables and scoped tokens exist | Contract work can map existing values, but must resolve authority before migration. |
| Component state workbench | conditional | No Storybook; existing Playwright routes create many deterministic product states | Do not add Storybook automatically. First repair/use existing fixtures; add a workbench only if repeated isolated-state value justifies it. |
| Web accessibility automation | `not-applicable` to this visual-system-only pilot | `@axe-core/playwright` is not configured | No accessibility claim is made. It becomes a hard missing capability for accessibility/release work. |
| Penpot MCP | `not-applicable` | No exact selected-layer question is needed for the source inventory | If later layer identity is ambiguous and no approved annotated export exists, preflight must stop for setup or confirmed reduced context. |
| Style Dictionary | `not-applicable` | One CSS UI output is shared into Capacitor; no generated token pipeline exists | CSS variables remain the lower-cost authority unless future themes/outputs justify compilation. |
| Cloudflare, Firebase, Lyssna, Clarity | `not-applicable` | No remote reviewer, physical-device matrix, participant study, or post-launch behavior question is in this pilot | Do not connect accounts, upload builds, instrument production, recruit, or spend money. |

Capability records are intentionally time-bound. Execution validation now requires a timezone-aware probe no older than four hours and no more than five minutes ahead. These dated pilot fixtures therefore become stale by design; replay requires fresh probes and a new `checked_at`, never editing the historical record merely to force a pass.

### Required setup: supported Python

The current Python.org macOS page lists signed current stable installers; the suite only requires Python 3.10 or newer. Use a current supported stable release rather than the Apple-provided Python 3.9.6. See [Python releases for macOS](https://www.python.org/downloads/macos/).

1. Download and install the current signed universal macOS installer from Python.org.
2. Open a new terminal. Do not overwrite the Apple system interpreter; use the installed version explicitly or put its installer bin earlier in the shell path.
3. Verify, for example: `python3.14 --version` (or the installed supported version).
4. Verify the suite tools:
   - `python3.14 /Users/drago/Documents/skills/skills/product-design-contract/scripts/validate_design_contract.py --help`
   - `python3.14 /Users/drago/Documents/skills/skills/product-design-change/scripts/change_guard.py --help`
5. Re-run the contract-phase capability preflight. Only a successful supported-version probe changes the status to `available`.

No interpreter was installed during this pilot.

### Required setup: Android runtime and Maestro

TeachRelay requires Android API 36 and Java 21. Maestro itself requires Java 17 or newer. Current official starting points are [Android Studio installation](https://developer.android.com/studio/install) and [Maestro CLI installation](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli).

1. Install current stable Android Studio for Apple Silicon and complete its setup wizard.
2. In SDK Manager install Android SDK Platform 36, matching Build Tools, Platform-Tools, Android Emulator, and an ARM64 API 36 system image.
3. Create and start a representative Android Virtual Device.
4. Point the shell at Android Studio's Java 21 runtime and SDK for this machine, then verify:
   - `"/Applications/Android Studio.app/Contents/jbr/Contents/Home/bin/java" -version`
   - `/Users/drago/Library/Android/sdk/platform-tools/adb devices`
5. Install Maestro using one official macOS path. The official Homebrew path is:
   - `brew tap mobile-dev-inc/tap`
   - `brew install mobile-dev-inc/tap/maestro`
6. Verify `maestro --help` and confirm the running emulator is visible.
7. With explicit test-write authorization, add a deterministic checked-in smoke flow for `com.teachrelay.learner.dev`; do not rely on live MCP exploration alone.
8. Build with the existing project command: `bun run --filter @teachrelay/mobile build:android`.
9. Install the exact generated dev-debug APK, run the smoke flow, and record source commit, build identity, emulator/device, API, locale, scale, and evidence paths.
10. Re-run capability preflight. The status stays blocking until a named flow executes successfully against the exact packaged candidate.

No Android SDK, Java runtime, Maestro tool, emulator, flow, or build was installed/created by this pilot.

### Required decision: web accepted identity

This is not fixed by installing another tool.

1. The owner must decide whether the current Relay Board root, the previously accepted continuation workspace, or another named candidate is the intended authority.
2. Bind that decision to an exact Git ref and approved artifact identity.
3. Use contract re-architecture to map global/shared/family/Relay authorities and declare intentional variants.
4. Repair or replace the affected deterministic test through an approved change; do not update screenshots merely to make CI green.
5. Run the assertion without update mode and inspect the generated diff.
6. Only a later explicit accept-freeze operation may replace the accepted baseline.

## Screenshot evidence classification

The bundled classifier was run against the web and mentor Playwright sources. Its output was treated as a lead generator and checked against source and one live execution.

| Evidence set | Classification | Basis |
| --- | --- | --- |
| 16 files in `apps/web/tests/e2e/learning.spec.ts-snapshots/` | Assertion-backed producer; current status partly `unknown/stale` | `expectAcceptanceScreenshot` calls Playwright `toHaveScreenshot` with deterministic reset and tolerance. Nine files are explicitly named in the implementation-acceptance record. However, the selected Home acceptance test failed before reaching the assertion at current HEAD, so a committed PNG and assertion-capable helper do not prove a current passing golden. |
| Four `design/engagements/learner-relay-board/artifacts/verification/*.png` images | `capture-only` | Relay tests call `page.screenshot`; no active comparison assertion or accepted baseline manifest links these files. “Verification” in a path is not an assertion. |
| `apps/web/tests/e2e/shell.spec.ts` screenshot calls | `capture-only` | Five `page.screenshot` producer occurrences. |
| `apps/mentor/tests/e2e/mentor.spec.ts` screenshot calls | `capture-only` | Seven `page.screenshot` producer occurrences. |
| Non-acceptance screenshot calls in `learning.spec.ts` | `capture-only` | Seventeen `page.screenshot` producer occurrences. |
| Direction/contact-sheet and engagement captures | Approved reference only where a human record explicitly identifies them; otherwise `capture-only` or `unknown/stale` | They are useful design/review evidence but do not fail when production pixels change. |

Across the three inspected E2E sources there are 29 capture-only producer occurrences and one reusable asserted-screenshot producer. A filename, committed status, hash, `baseline` directory, or screenshot prose does not upgrade a capture to an asserted golden.

## Tool knowledge and dependency policy in the skills

The implemented suite explicitly covers all selected tool families: Git/GitHub checks, Penpot MCP and exports, CSS variables/DTCG/Style Dictionary, Storybook/RN Storybook/Widgetbook/native previews, Playwright, axe, Maestro, Apple/Android/Flutter native checks, Cloudflare Pages, Firebase App Distribution/Test Lab, Lyssna, and Clarity. No project-specific or ancestor-skill reference occurs under `skills/product-design*`.

The important behavior is capability-based rather than brand-based:

- A phase/platform/claim profile selects only applicable capabilities.
- A tool is useful only after a safe version/configuration/target probe; package presence or MCP registration is insufficient.
- Required capabilities and hard gates cannot be degraded by a confirmation ID.
- `shared-web-wrapper` expands runtime requirements to both web and native-mobile layers.
- A conditional non-hard degradation requires an explicit confirmation ID carried by the routing envelope and handoff.
- A source-only audit is a named reroute, not a waived visual-acceptance gate.
- MCPs improve exact context and live inspection; Git exports, manifests, tests, flows, and captures remain canonical.
- Setup instructions must be checked against current official documentation and no install, account connection, deployment, upload, instrumentation, participant contact, or spend occurs without authorization.

How the tools improve worker output:

- Penpot resolves exact frame/layer/component identity when source plus annotated evidence is ambiguous.
- Semantic tokens and conditional Style Dictionary compilation convert visual intent into an inspectable impact graph.
- Existing fixture routes or workbenches make component states executable instead of prose-only.
- Playwright and Maestro produce matched runtime evidence and protect preserved states across browser and packaged targets.
- axe and native accessibility tools prevent visual implementation from being mistaken for accessible implementation.
- Cloudflare/Firebase provide commit/build-bound review access only when local access is insufficient.
- Lyssna/moderated work and Clarity provide representative or live signals for named decisions; neither substitutes for visual craft or explanation.

## Validator and guard exercises

All mutations below occurred only in [`fixtures/contract-change`](fixtures/contract-change), a disposable generic fixture. Its temporary nested Git metadata was removed afterward so the parent skills repository can track the fixture normally.

| Exercise | Expected result | Observed result |
| --- | --- | --- |
| Validate `review → contract` series envelope | Pass | Pass |
| Validate blocked read-only review envelope + handoff | Pass; no successor recommended | Pass |
| Attempt baseline updates from a review pipeline | Reject | Rejected: contract-only accept-freeze route, authority, and approval ID required |
| Validate blocked capability record as an inventory | Pass schema | Pass |
| Validate blocked record `--for-execution` | Reject | Rejected missing/unconfirmed contract identity plus web and mobile hard gates |
| Validate synthetic owner-confirmed source-only route/profile | Pass only for narrowed non-acceptance review at the recorded probe time | Passed during the pilot; a replay must refresh probes and timestamp |
| Validate contract-phase record on Python 3.9.6 | Reject | Rejected required scope/hash capability |
| Validate the generic fixture's contract/baseline schema, hashes, authority, and approval ID in freeze mode | Pass structurally | Pass structurally; the placeholder PNG and non-runnable standalone visual test are not runtime or visual-acceptance evidence |
| Put a `capture-only` item in accepted baseline manifest | Reject | Rejected: only approved reference or asserted golden is allowed |
| Resolve shared `Card` impact | Expand to web + Android wrapper | Expanded to both platforms/targets and both mapped states |
| Validate approved bounded change manifest | Pass | Pass |
| Set `baseline_updates_allowed: true` in change manifest | Reject | Rejected |
| Verify one allowed fixture source edit | Pass with protected baseline bytes preserved | Pass structurally; required Playwright/Maestro checks were declared but not executed by the guard |
| Mutate protected baseline bytes | Reject | Rejected by hash and protected-path checks |
| Restore protected bytes and reverify | Pass | Pass |

Current bundled unit tests also passed after the integration fixtures were aligned with the final approval-ID schemas:

- router validation: 22/22;
- capability/toolchain validation: 16/16;
- contract validation: 9/9;
- change guard: 11/11;
- implementation protected-path checks: 2/2;
- review evidence-classification checks: 2/2;
- total: 62/62.

## Pilot conclusion

The suite handles the original failure mode as intended:

- It does not treat a long prompt as sufficient protection against visual drift.
- It finds the earliest worker, preserves the original prompt hash and target identity, and keeps review read-only.
- It detects the shared web/mobile architecture and expands target impact mechanically.
- It distinguishes assertion-backed images from captures and detects that a current acceptance path does not reach its assertion.
- It refuses execution when an applicable tool/evidence capability is missing.
- It offers a precise, explicitly confirmed narrower route where useful, while keeping unsupported conclusions `Not evidenced`.
- It prevents implementation/change workers from approving or changing accepted baselines.

The next honest action for TeachRelay is dependency setup or explicit confirmation of a source-only authority inventory. No production re-architecture should begin until a supported validator runtime exists, accepted visual authority is named, and the web plus packaged-mobile evidence paths required by the approved migration slice are working.
