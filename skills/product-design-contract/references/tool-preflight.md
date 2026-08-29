# Capability preflight

Preflight only capabilities relevant to this invocation. The absence of an irrelevant tool is not degradation; the absence of a tool needed for a promised artifact or evidence class is.

## Requirement and status

Requirement (`required`, `conditional`, or `optional`) explains when the capability matters. Status uses the suite's exact vocabulary:

| Status | Meaning | Action |
| --- | --- | --- |
| `available` | A safe probe proved the tool, configuration, and needed target | Continue |
| `missing-blocking` | The phase cannot produce required identity or evidence | Stop; provide setup steps; ask whether to perform or await setup |
| `missing-degradable` | Useful reduced work can continue, but fidelity or evidence is lost | Explain impact; offer setup or a bounded degraded mode; wait for confirmation |
| `unknown` | Presence or correctness was not verified | Probe safely or treat as missing |
| `not-applicable` | Capability is not selected for this phase/platform | Do not install or warn |

User confirmation can authorize reduced contract planning. It cannot turn missing evidence into a pass. Persist durable results in `design/toolchain.json` with tool/version/evidence, degradation, and `confirmation_id`; never store credentials. Set `checked_at` only after all applicable probes run: execution requires a timezone-aware ISO-8601 value no older than four hours and no more than five minutes in the future, with an earlier re-probe when phase, platform, claim, target/build, access, version, or status changes.

## Representative platform matrix

Contract and accept-freeze profiles use a non-empty platform set whenever targets exist. The detailed matrix contains at least one configuration per materially distinct implementation/adaptation class, not every device: name runtime/device or viewport/window class, state/fixture, input, text/display scale, theme/locale, and evidence or explicit exclusion. For `shared-web-wrapper`, record the shared browser UI and packaged native shell separately. Planning may mark rows unverified; Gate E and accept-freeze are limited to the exact reviewed rows and cannot infer unlisted coverage.

## Capability classification

| Capability | Requirement | When it applies | Probe |
| --- | --- | --- | --- |
| Repository filesystem + Python 3.10+ | Required | Every authoritative contract operation | Read project; `python3 --version`; run validator help |
| Git | Required | Accepted identity, rollback, or freeze; strongly preferred for drafts | `git rev-parse --show-toplevel`; `git status --short`; resolve accepted ref |
| CSS variables | Conditional | Simple web contract with an existing CSS source | Inspect actual imports/root/theme scopes and rendered values |
| DTCG + Style Dictionary | Conditional | Multiple outputs/themes/platforms or an established compiler | Locate canonical token JSON/config; run existing validation/build; inspect clean generated diff |
| Penpot + official MCP | Optional adapter | Exact selected frame/layer/component/token context is needed and Penpot is the source | Verify authenticated project/file read and selected object; keep exports in Git |
| Framework workbench/preview | Conditional | Reusable components require executable states | Run an existing story/preview/fixture and render the named state |
| Playwright | Conditional | Web/PWA/wrapped-web runtime or web goldens | Run configured project and one representative screenshot assertion |
| Maestro/native tests | Conditional | iOS/Android/RN/Flutter/packaged app target | List a usable simulator/device; validate and run one named flow |
| Accessibility tools | Conditional hard-gate evidence | Contract claims semantics/a11y readiness | Run axe for web or the relevant native audit/semantics checks; retain manual plan |
| Cloudflare Pages | Optional | A reviewer needs a remote web candidate | Verify project/build/preview access; local runtime remains canonical |
| Firebase App Distribution/Test Lab | Optional | Physical-device or remote tester evidence is required | Verify authenticated project, target app, quota, and exact matrix |

MCP presence alone is not a successful probe. Test the needed resource and operation. Treat MCP as a replaceable live adapter; exports, tests, manifests, and hashes in Git remain authoritative.

## Missing-capability response

Before continuing, report:

```text
Capability: <name>
Requirement: required | conditional | optional
Status: available | missing-blocking | missing-degradable | unknown | not-applicable
Impact: <specific artifact/check/evidence that cannot be produced>
Safe degraded mode: <exact reduced scope, or “none”>
Evidence status if degraded: Not evidenced
Confirmation ID: <record only after explicit approval>
```

Then provide setup steps appropriate to the repository. Do not install dependencies, create accounts, enable analytics, spend money, expose ports, or mutate CI without authorization.

### Git

1. Install Git from the operating-system package source or official Git distribution.
2. Verify with `git --version`.
3. Initialize only if the user wants this directory to become a repository: `git init`.
4. Establish an accepted commit/ref before freeze; do not use an unresolved dirty tree as baseline identity.

### Python validator

1. Install Python 3.10 or newer from the platform package manager or official Python distribution.
2. Verify with `python3 --version`.
3. Run `python3 scripts/validate_design_contract.py --help` from this skill package.

### Style Dictionary

1. Confirm multi-output/theme generation is actually needed.
2. Prefer the project's package manager and pin Style Dictionary as a development dependency after approval.
3. Define one checked-in DTCG source and explicit generated outputs.
4. Run the configured build twice and verify the second run is clean.

Do not add it for a single-output site where committed CSS variables are sufficient.

### Penpot MCP

1. Use a supported Penpot release and an existing Free/self-hosted workspace.
2. Configure the official Penpot MCP using Penpot's current client instructions.
3. Authenticate with the minimum project access needed.
4. Verify exact file/page/frame or selected-layer read before relying on it.
5. Export the approved reference/project to the repository after a gate; never expose an unauthenticated local MCP port.

If Penpot is unavailable, an approved export plus explicit human confirmation of its identity may be a safe reduced input. Selection metadata and live structured-source checks remain `Not evidenced`.

### Playwright and web accessibility

1. Prefer the repository's existing package manager and Playwright configuration.
2. With approval, add the pinned development dependencies `@playwright/test` and, when accessibility automation is needed, `@axe-core/playwright`.
3. Install the configured browsers and OS dependencies using Playwright's documented command.
4. Verify with the repository's smallest existing screenshot assertion and accessibility test.

Browser-control or Playwright MCP may assist exploration but does not replace checked-in assertions.

### Maestro and native tools

1. Install Maestro CLI using the current official Maestro instructions and verify `maestro --version`.
2. Install/start the platform SDK, emulator, or simulator required by the project.
3. Verify a usable target (`maestro test` on a smoke flow; `adb devices` for Android; Xcode simulator tooling for Apple).
4. Keep YAML flows and asserted screenshots in Git. Use Maestro MCP only for live inspection.
5. Pair device flows with platform semantics/accessibility tests and manual assistive-technology checks.

Maestro's normal Apple path is simulator evidence. Use the project's native/XCTest and physical-device route when physical iOS evidence is required.

### Framework workbench

Use an existing Storybook, React Native Storybook, Widgetbook, Xcode Preview, Compose Preview, or ordinary fixture route. If none exists, first ask whether the component/state reuse and review value justifies a new development dependency. A deterministic fixture can be the lower-cost alternative.

## Degradation boundaries

- A draft may continue without a live design MCP when an identified approved export exists and the user accepts the limitation.
- A planning-only contract audit may continue without runtime tools when the user accepts that states and baselines remain unverified. It produces contract proposals only, never production source or accepted identity.
- Accept-freeze may not continue without the runtime/hash/assertion capabilities needed for the declared target matrix.
- Missing accessibility tooling never becomes “passed”; it stays `Not evidenced` and blocks any accessibility or release-readiness claim.

## Official setup sources

Verify commands against current official documentation for the detected environment before presenting or running them:

- Git and GitHub rulesets: <https://git-scm.com/downloads>, <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- Penpot MCP: <https://help.penpot.app/mcp/>
- Style Dictionary: <https://www.styledictionary.org/getting-started/installation/>
- Storybook and Widgetbook: <https://storybook.js.org/docs/get-started/install>, <https://docs.widgetbook.io/>
- Playwright and axe: <https://playwright.dev/docs/intro>, <https://playwright.dev/docs/accessibility-testing>
- Maestro: <https://docs.maestro.dev/getting-started/installing-maestro>
- Apple, Android, and Flutter accessibility: <https://developer.apple.com/documentation/accessibility/accessibility-testing>, <https://developer.android.com/guide/topics/ui/accessibility/testing>, <https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility>
