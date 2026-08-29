# Tool capability preflight

Use [tool selection baseline](tool-selection-baseline.md) before choosing a default, proposing setup, accepting an equivalent, or replacing a tool. It records the phase fit, evidence role, selection rationale, limitations, rejected alternatives, and representative comparison required for a substitution. Do not reconstruct that decision from brand familiarity or current tool availability.

## Principle

Depend on capabilities, not brands. Prefer the approved mature free tool, but accept an established project alternative only when it produces equivalent durable evidence.

An existing alternative is equivalent only after a safe probe shows it satisfies the active capability and evidence claims. A new replacement also needs the baseline's capacity, maturity, portability, non-replaceability, pilot, migration, and rollback comparison. Missing MCP access alone does not justify replacing the underlying canonical or deterministic tool.

Never silently lose structured design context, framework rendering, deterministic comparison, accessibility evidence, physical-device evidence, or real-user evidence.

## Status vocabulary

| Status | Meaning | Action |
|---|---|---|
| `available` | Capability is proven by a version check, project configuration, connection probe, or existing artifact | Continue |
| `missing-blocking` | The phase cannot produce its required evidence | Stop; provide setup; ask for setup authorization |
| `missing-degradable` | Useful scoped work can continue, but fidelity or evidence is reduced | Explain impact; offer setup or bounded degraded mode; wait for confirmation |
| `unknown` | Presence or correctness was not verified | Run a safe probe or treat as missing |
| `not-applicable` | Capability is not selected for this phase/platform | Do not install or warn |

User confirmation can authorize degraded work. It cannot turn missing evidence into a pass.

## Executable profile

Before each worker, set `toolchain.profile` with one phase, applicable platforms, and only the claims the route is expected to support. Run the bundled validator with `--for-execution`. The profile derives the mandatory capability IDs; an omitted required capability, empty applicable platform set, unknown status, or confirmed degradation of a hard gate fails validation. Rebuild the profile at every transition instead of carrying a previous worker's pass forward.

Direction, contract, prototype, implementation, change, and accept-freeze require a non-empty platform set. Treat it as the list of materially distinct implementation/adaptation classes, then record at least one representative target configuration per class in the phase artifact. “Representative” is proportional coverage, not “all devices”: include configurations that exercise distinct layout/runtime/platform behavior and state explicit exclusions. `shared-web-wrapper` expands to both web and native layers, so verify the common UI in a browser and the packaged shell separately. Gates B–F apply only to the matrix actually evidenced.

For execution, `checked_at` certifies that every applicable capability status was actually probed. Use a timezone-aware ISO-8601 timestamp no older than four hours and no more than five minutes ahead of the current clock. Do not update the timestamp without re-running the selected probes. Re-probe earlier when phase, platform, claim, target/build identity, environment, access, version, or observed status changes.

Use `shared-web-wrapper` when one web UI is packaged in a native shell; the validator then requires both web and native runtime/accessibility layers. Use `web` plus `native-mobile` for genuinely independent implementations.

## Request capabilities just in time

Bind every capability request to the current phase and current evidence claim.

- A missing capability for the current worker can block now.
- A capability used only by a likely successor is a forecast, not a current blocker, and must not appear in the exact next action.
- Re-probe at the transition; do not carry a forecast forward as proof that the tool is still needed or missing.
- Ask for a capability first and name the approved default or an equivalent. Avoid forcing a brand when an established project tool produces the same durable evidence.
- Make the ask actionable: state what the user must install, connect, open, or provide; what read/write access is required; and the minimal verification probe that will prove readiness.

For example, a read-only native review may need the repository or installable build, a real simulator/device runtime, and the current review's accessibility/flow evidence path. A later protected change may require additional deterministic regression tooling. Do not require the later tool before the review unless the current review question itself depends on the repeatable evidence it produces; when it does, explain that current-stage relationship explicitly.

## Approved capability map

| Capability | Approved default | When required or conditional | Durable source |
|---|---|---|---|
| Versioning, rollback, protected acceptance | Git; GitHub checks when remote review is used | Required for accepted contracts, production implementation, protected changes, and freeze | repository files and history |
| Structured editable visual source | Penpot Free; official MCP on demand | Preferred for direction and visual prototypes; degradable to approved annotated references/code mock with confirmation | exported file, images, contract |
| Semantic style source | CSS variables for one web target; DTCG JSON for multiple outputs | Required once visual rules are frozen | committed source values |
| Token compilation | Style Dictionary | Conditional for multiple targets/themes/formats | config, generated outputs, golden checks |
| Component state workbench | Existing state route or Storybook; RN Storybook; Widgetbook; Xcode/Compose previews | Conditional when reusable components/states justify it | stories, fixtures, preview source |
| Web runtime and visual regression | Playwright Test | Required for protected web implementation/change/freeze | tests, goldens, traces |
| Mobile runtime and visual regression | Maestro CLI plus native tests where needed | Required for protected native/cross-platform mobile implementation/change/freeze | YAML flows, native tests, goldens |
| Web accessibility automation | `@axe-core/playwright` or equivalent | Required for applicable web candidate gates | test results |
| Native accessibility | Xcode Accessibility Inspector/XCTest; Android checks/Compose semantics; Flutter guideline tests | Required for applicable mobile candidate gates | source tests and recorded manual checks |
| Shareable web review | Existing preview host or Cloudflare Pages Free | Conditional when reviewers cannot run locally | candidate URL tied to commit |
| Mobile tester delivery | Firebase App Distribution or existing beta channel | Conditional when real-device human review is required | release/build identity |
| Physical-device sampling | Firebase Test Lab or existing device lab | Conditional for significant mobile release evidence | matrix configuration and artifacts |
| Pre-release user study | Moderated testing or Lyssna Free | Conditional when a named question requires participant evidence | research notes and decisions |
| Post-launch behavior | Microsoft Clarity | Conditional only after consent/masking/performance and a named decision | accepted findings, not raw-session dependency |
| Live agent adapter | Penpot, Maestro, Storybook, Playwright, or Chrome DevTools MCP | Optional and on demand | never canonical; normal exports/tests remain sufficient |

## Probe safely

1. Inspect lockfiles, manifests, project scripts, CI, test directories, and existing design exports.
2. Use non-mutating version/help commands where available.
3. For MCP or accounts, run a read-only capability probe; do not create or modify remote data.
4. For browser/device tools, run the smallest disposable smoke check.
5. Record tool, version, evidence, environment, and check time without credentials.

Do not treat a package name in a manifest as proof that its browser, simulator, fonts, or connection works.

## Missing-capability response

Report:

1. **Missing capability and selected tool**
2. **Why this phase needs it**
3. **What work can still be done**
4. **What evidence/claim remains unavailable**
5. **Setup steps**
6. **Specific user action** — the exact install/connect/open/provide action needed now
7. **Choice required** — set up now, provide an equivalent, or confirm the precisely bounded degraded mode

List likely later-stage capabilities separately as a forecast. They do not belong in the current exact next action and cannot block the current worker.

Do not continue until the choice is explicit.

For implementation or protected change, a missing applicable runtime or accessibility hard gate is `missing-blocking` and stops the worker before production writes. The choice is setup/equivalent evidence, or confirmation that the router should create a fresh reduced-scope envelope for read-only review, contract planning, or an isolated prototype whose own renderer and profile pass. It is never permission for a source-only production patch.

## Setup instructions

Tool installation and SaaS/MCP setup change over time. Before giving commands:

1. identify OS, architecture, framework, package manager, CI, and whether the project already has an equivalent;
2. consult current official documentation only;
3. show exact commands and files that would change;
4. ask before installing a production dependency, system tool, connecting an account, modifying CI, or exposing a server;
5. install only after authorization;
6. verify with a version check and minimal smoke test;
7. update `design/toolchain.json`.

Official starting points:

- GitHub protected checks: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- Penpot MCP: <https://help.penpot.app/mcp/>
- Style Dictionary: <https://www.styledictionary.org/getting-started/installation/>
- Storybook: <https://storybook.js.org/docs/get-started/install>
- React Native Storybook: <https://storybook.js.org/tutorials/intro-to-storybook/react-native/en/get-started/>
- Widgetbook: <https://docs.widgetbook.io/>
- Playwright: <https://playwright.dev/docs/intro>
- axe with Playwright: <https://playwright.dev/docs/accessibility-testing>
- Maestro: <https://docs.maestro.dev/getting-started/installing-maestro>
- Apple accessibility testing: <https://developer.apple.com/documentation/accessibility/accessibility-testing>
- Android accessibility testing: <https://developer.android.com/guide/topics/ui/accessibility/testing>
- Flutter accessibility testing: <https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility>
- Cloudflare Pages: <https://developers.cloudflare.com/pages/get-started/>
- Firebase Test Lab: <https://firebase.google.com/docs/test-lab>
- Firebase App Distribution: <https://firebase.google.com/docs/app-distribution>
- Lyssna: <https://help.lyssna.com/>
- Microsoft Clarity: <https://learn.microsoft.com/en-us/clarity/>

Never expose a local MCP port beyond its trusted local boundary. Keep MCP access read-only until a scoped write is approved.

## Hard evidence boundaries

- No working browser/app runtime → no visual or interaction acceptance.
- No deterministic baseline comparison → no preservation claim.
- No applicable accessibility automation/manual plan → no accessibility gate pass.
- No physical-device run when required → simulator evidence only.
- No representative participant evidence → heuristic or synthetic judgment only.
- No consent/masking decision → do not add session replay.
