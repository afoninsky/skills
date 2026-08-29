# Capability preflight for protected changes

Before recommending setup or changing a tool, read the relevant sections of the suite's canonical tool selection baseline from the sibling `product-design/references/tool-selection-baseline.md` skill resource. It explains why the free-first defaults were chosen and what an alternative must prove. If that resource is unavailable, stop any toolchain-change proposal and request installation of the complete `product-design` suite; do not recreate the comparison from memory.

Record applicable capabilities in `design/toolchain.json` using the suite status vocabulary.

| Status | Meaning | Action |
| --- | --- | --- |
| `available` | A safe probe proved the tool, configuration, and needed target | Continue |
| `missing-blocking` | The protected change cannot preserve scope or produce required evidence | Stop; give setup steps; ask whether to set up or await setup |
| `missing-degradable` | A selected non-hard capability is absent, but the bounded change can still satisfy every production hard gate | Explain exact limitation; offer setup or bounded confirmation; wait for confirmation |
| `unknown` | Presence/correctness was not verified | Probe safely or treat as missing |
| `not-applicable` | The capability is not selected for this phase/target | Do not install or warn |

User confirmation cannot waive a production hard gate. If the useful reduced goal is planning, read-only analysis, or an isolated proof, stop this worker and let the router create a contract, review, or prototype envelope with its own preflight and authority.

## Capability map

| Capability ID | Default | Requirement for this skill |
| --- | --- | --- |
| `versioning-and-rollback` | Git | Required: accepted ref, isolated diff, rollback, and changed-file inventory |
| `scope-and-hash-validation` | Python 3.10+ bundled guard | Required: manifest, source-map closure, and baseline hashes |
| `structured-visual-context` | Penpot official MCP on demand | Optional; becomes degradable when exact element identity depends on a selected layer and no annotated export exists |
| `semantic-style-source` | Existing CSS variables or DTCG | Required when the change touches a semantic token |
| `token-compilation` | Existing Style Dictionary | Conditional when multiple generated outputs/themes are affected |
| `component-state-runtime` | Existing fixture/workbench/native preview | Conditional for reusable component/state changes |
| `web-runtime-and-visual-regression` | Playwright | Required for protected web/PWA/wrapped-web changes |
| `mobile-runtime-and-visual-regression` | Maestro plus native tests | Required for protected native/RN/Flutter/packaged-app changes |
| `web-accessibility` | axe Playwright or established equivalent | Required evidence for applicable web candidate gate |
| `native-accessibility` | Platform semantics/audit tools | Required evidence for applicable mobile candidate gate |
| `remote-review` | Existing preview host/Cloudflare Pages or mobile beta channel | Conditional only when the reviewer cannot run the candidate locally |
| `physical-device-sampling` | Firebase Test Lab/existing lab | Conditional for significant/device-specific release claims |

MCP is a replaceable adapter. The source map, manifest, tests, flows, exports, and evidence in Git remain authoritative.

## Required probes

- Git: `git rev-parse --show-toplevel`, resolve `base_ref`, and inspect `git status --short`.
- Python: `python3 --version` and `python3 scripts/change_guard.py --help`.
- Baselines: run guard validation and hash every protected entry before edits.
- Playwright: run one configured affected test/project and prove an asserted screenshot path, not a capture-only output.
- Maestro/native: list a usable target, validate the named flow, and execute the smallest affected state.
- Token compiler: run the established build twice and verify the second run produces no diff.
- Accessibility: execute the existing automation and preserve a concrete manual assistive-technology plan.

## Missing-capability response

Report capability, requirement, exact status, impact, safe bounded continuation, `Not evidenced` claims, and `confirmation_id` if the user approves a non-hard degradation. Record `checked_at` only after every applicable status was actually probed; execution accepts a timezone-aware timestamp no older than four hours and no more than five minutes in the future, with an earlier re-probe on any phase, platform, claim, target/build, access, version, or status change.

Then provide environment-specific setup using current official documentation. Do not install a package/system tool, connect an account, expose an MCP port, add analytics, alter CI, or add a development dependency without authorization.

### Git and Python

1. Install Git and Python 3.10+ from the platform's official/package-manager route.
2. Verify `git --version` and `python3 --version`.
3. Ensure the accepted ref exists locally; fetch only with authorization/network access already in scope.
4. Run `python3 scripts/change_guard.py --help`.

There is no safe protected-change degradation without these capabilities. Return only the preflight blocker and reroute options; advisory impact analysis belongs to a fresh read-only review or contract-planning route after confirmation.

### Playwright and axe

1. Reuse the repository's package manager and existing Playwright configuration.
2. With approval, add pinned development dependencies for `@playwright/test` and, when needed, `@axe-core/playwright`.
3. Install configured browsers through Playwright's documented command.
4. Add/run a real assertion for the affected state and a representative protected state.

Browser-control or MCP exploration cannot substitute for checked-in assertions.

### Maestro and platform tools

1. Install Maestro CLI using its current official instructions; verify `maestro --version`.
2. Start the required emulator/simulator and verify it is usable.
3. Keep Maestro YAML and asserted screenshots in Git; use MCP only for live inspection.
4. Run the relevant native semantics/accessibility tests and manual TalkBack/VoiceOver plan.

For physical iOS evidence use the project's XCTest/device distribution path; simulator evidence must remain labeled as such.

### Style Dictionary

1. Confirm a multi-output/theme token change actually requires compilation.
2. Reuse and pin the existing project configuration; ask before adding it as a development dependency.
3. Generate every mapped output and verify a second generation is clean.

Do not add a compiler for a local single-output CSS change.

### Penpot MCP

1. Configure the official Penpot MCP for the existing project with minimum access.
2. Verify a read-only exact file/page/frame/selected-layer probe.
3. Export relevant approved context to Git.
4. Never expose an unauthenticated local MCP port.

An annotated crop plus confirmed source selector can be an explicitly approved fallback; live layer identity remains `Not evidenced`.

## Hard boundaries

- No accepted ref/hash guard → no production write.
- No applicable browser/app runtime → no interaction or visual-preservation claim.
- No deterministic comparison → no “everything else unchanged” claim.
- No applicable accessibility path → no production write in this worker; accessibility remains `Not evidenced`.
- No physical-device run when required → simulator-only evidence.

## Official setup sources

Verify commands against current official documentation for the detected environment before presenting or running them:

- Git: <https://git-scm.com/downloads>
- Penpot MCP: <https://help.penpot.app/mcp/>
- Style Dictionary: <https://www.styledictionary.org/getting-started/installation/>
- Storybook and Widgetbook: <https://storybook.js.org/docs/get-started/install>, <https://docs.widgetbook.io/>
- Playwright and axe: <https://playwright.dev/docs/intro>, <https://playwright.dev/docs/accessibility-testing>
- Maestro: <https://docs.maestro.dev/getting-started/installing-maestro>
- Apple, Android, and Flutter accessibility: <https://developer.apple.com/documentation/accessibility/accessibility-testing>, <https://developer.android.com/guide/topics/ui/accessibility/testing>, <https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility>
