# Direction tool preflight

Run before visual research or any local/remote write. Record results in `design/toolchain.json` when a project workspace exists. Depend on capabilities, not brands.

## Status vocabulary

Use exactly:

- `available` — proven by a version check, project configuration, read-only connection probe, or rendered artifact;
- `missing-blocking` — required evidence cannot be produced; stop;
- `missing-degradable` — scoped work can continue with reduced fidelity after explicit confirmation;
- `unknown` — not verified; probe safely or treat as missing;
- `not-applicable` — not selected for this direction/target.

## Phase capability matrix

| Capability | Requirement | Approved default or existing equivalent | Durable evidence / degradation |
| --- | --- | --- | --- |
| Read/write isolated artifacts | Required | Workspace filesystem | No fallback |
| Version, diff, and recover candidates | Required | Git; GitHub review optional | Another established VCS only if it provides immutable refs, diffs, rollback |
| Render/export and capture matched visual candidates | Required | Penpot export, real browser capture, or native/framework preview capture | Text-only directions are `missing-blocking` for Gate B |
| Inspect approved structured design source | Conditional | Penpot Free with official MCP on demand | Exported source + annotated references can be `missing-degradable` when they contain equivalent context |
| Research current visual references, fonts, or platform guidance | Conditional | Web access to first-party/original sources | Supplied sources; otherwise the named research question remains blocked |
| Generate bespoke raster imagery | Optional | Available image-generation capability | Licensed supplied/stock asset or direction without bespoke imagery |
| Obtain representative-user direction evidence | Conditional | Moderated test or Lyssna when a named decision requires it | No synthetic substitute; heuristic comparison cannot pass that evidence gate |
| Share a live web candidate with remote reviewers | Conditional | Existing preview host; Cloudflare Pages when appropriate | Local capture if every required reviewer can inspect it; otherwise review is blocked |
| Put a mobile candidate on tester devices | Conditional | Existing beta channel or Firebase App Distribution | Simulator capture is not equivalent to required physical human review |

Penpot is useful but not mandatory. If it is unavailable, disclose the loss of structured human-editable source and ask before using a code-rendered or annotated-reference fallback. Always export accepted evidence to Git.

## Safe probes

1. Inspect available tools, skills, repository manifests, design files, test/workbench configuration, and target SDKs.
2. Verify Git and cleanly identify unrelated changes; do not modify them.
3. Prove the chosen renderer by producing or opening one disposable frame at an exact target size and capturing it.
4. For Penpot MCP, list the focused file/page/layers read-only before requesting scoped write access. Do not assume an account or configured server is connected.
5. For browser/native previews, verify fonts/assets and exact target dimensions; a source file that cannot render is not available.
6. For participant or remote-review tools, verify authorization, access, consent/privacy, and the actual review surface.
7. Store tool, version, environment, evidence, status, degradation, and confirmation ID in `design/toolchain.json`; never store credentials.

Set `checked_at` only after every applicable probe ran. Execution requires a timezone-aware ISO-8601 timestamp no older than four hours and no more than five minutes in the future; re-probe sooner whenever phase, platform, claim, target/build, environment/access, version, or observed status changes.

Direction uses a non-empty representative platform matrix. Include at least one target/configuration for each materially distinct implementation/adaptation class and state exclusions. `shared-web-wrapper` keeps one visual direction but requires both browser and packaged-shell rows; independent web and native implementations use separate classes.

Report capability, requirement, adapter, exact status, probe evidence, impact, and action.

## Missing-capability protocol

Never silently replace a structured design source, renderer, real participant, or review surface.

1. Explain the missing capability and which output/evidence it affects.
2. Mark it `missing-blocking` or `missing-degradable`.
3. Offer setup and, only if safe, a precisely bounded degraded mode.
4. Ask for an explicit choice. Confirmation may authorize degraded work but cannot upgrade its evidence or pass a hard gate.
5. When setup is requested, inspect OS/framework/package manager and browse current official documentation. Give exact steps, least-privilege/read-only configuration first, files/accounts changed, verification probe, Git export path, and rollback/disconnect steps. Ask before installing, connecting an account, publishing, spending, or adding a project dependency.
6. Re-run the probe and update `design/toolchain.json`.

Keep MCP tokens out of prompts, logs, screenshots, and Git. Do not expose a local MCP listener beyond its trusted local boundary.

Official starting points to verify live:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Penpot MCP](https://help.penpot.app/mcp/)
- [Playwright browsers](https://playwright.dev/docs/browsers)
- [Storybook install](https://storybook.js.org/docs/get-started/install)
- [Widgetbook quick start](https://docs.widgetbook.io/quick-start)
- [Xcode previews](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode)
- [Compose previews](https://developer.android.com/develop/ui/compose/tooling/previews)
- [Cloudflare review hosting](https://developers.cloudflare.com/pages/get-started/)
- [Firebase App Distribution](https://firebase.google.com/docs/app-distribution)
- [Lyssna study setup](https://help.lyssna.com/en/collections/9546028-setting-up-your-study)

## Hard evidence boundaries

- no actual render/export and capture means no Gate B candidate comparison;
- no matched content/state/target means no defensible comparative claim;
- no representative participants means no user-validation claim;
- no durable isolated source/export means no selectable continuing-pipeline artifact;
- no required remote/device access means the affected reviewer or target remains `Not evidenced`.

Optional structured-source access may be degraded only when another actual matched render/capture path is proven and explicitly confirmed. If render/capture itself is missing, stop direction; an unrendered source draft is not executable direction work and cannot advance to Gate B. The router may instead offer research/read-only work or an isolated prototype using an alternative renderer whose own preflight passes.
