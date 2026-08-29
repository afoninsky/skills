# Prototype tool preflight

Before recommending setup or changing a tool, read the relevant sections of the suite's canonical tool selection baseline from the sibling `product-design/references/tool-selection-baseline.md` skill resource. It explains why the free-first defaults were chosen and what an alternative must prove. If that resource is unavailable, stop any toolchain-change proposal and request installation of the complete `product-design` suite; do not recreate the comparison from memory.

Run before prototype source creation. Record results in `design/toolchain.json` when a project workspace exists. Select a capability because the design question needs its evidence, not because a tool is fashionable.

## Status vocabulary

Use exactly:

- `available` — proven with a version/configuration/connection probe and, for runtimes, a minimal render;
- `missing-blocking` — required evidence cannot be produced;
- `missing-degradable` — a bounded artifact can be created with reduced evidence after confirmation;
- `unknown` — not safely verified; probe or treat as missing;
- `not-applicable` — not selected for this question/target.

## Capability matrix

| Capability | Requirement | Approved default or equivalent | Evidence/degradation |
| --- | --- | --- | --- |
| Read/write isolated artifacts | Required | Workspace filesystem | No fallback |
| Version, diff, and recover prototype inputs/output | Required | Git; GitHub review optional | Another existing VCS with immutable refs/diff/rollback |
| Render and capture the chosen medium | Required | Penpot export, real browser, framework workbench, Xcode/Compose preview, simulator/emulator | Source-only work is `missing-blocking` for Gate C |
| Repeat the critical interaction | Conditional, required for interaction claims | Playwright for web; Maestro/native UI tests for apps; Penpot click-through for supported questions | Manual observation may be `missing-degradable` for an exploratory draft, never deterministic acceptance |
| Inspect structured design source | Conditional | Penpot Free with official MCP on demand | Exported approved references/contract may suffice with confirmation |
| Executable component-state workbench | Conditional | Existing state route/Storybook; RN Storybook; Widgetbook; Xcode/Compose previews | A disposable fixture route/preview; do not add a workbench for one small prototype without value |
| Applicable accessibility inspection | Conditional, required for Gate C risk closure | axe/browser semantics; native platform tools/tests | Manual risk inventory can support exploration, not an accessibility pass |
| Share web runtime with remote decision makers | Conditional | Existing preview host or current Cloudflare option | Local access only when every required reviewer can run it |
| Deliver mobile build to real testers | Conditional | Existing beta channel or Firebase App Distribution | Simulator evidence cannot replace required physical human use |
| Physical-device evidence | Conditional | Available device or Firebase Test Lab for supported harness | Simulator-only label; cannot pass a physical-device requirement |
| Representative participant evidence | Conditional | Moderated test or Lyssna | No synthetic substitute |
| Generate necessary raster imagery | Optional | Image-generation capability | Supplied/licensed asset or placeholder with disclosed fidelity limit |
| Live agent adapter | Optional | Penpot, Playwright, Maestro, or workbench MCP | Normal exports, CLI/tests, and screenshots are canonical |

The runtime capability is question-specific. A static Penpot prototype is not a valid fallback for native keyboard, offline recovery, screen-reader semantics, or real animation. A native simulator is unnecessary for an IA paper-flow question.

## Safe probes

1. Inspect available tools, lockfiles/manifests, SDKs, build scripts, existing previews/workbenches, test flows, and platform-sharing architecture.
2. Verify Git and preserve unrelated working-tree changes.
3. Run non-mutating version/help checks for the selected renderer and test runner.
4. Open/build one minimal isolated fixture at an exact target and capture it. Package installation alone does not prove runtime availability.
5. For Playwright, verify the project command and required browser binary; for Maestro, verify Java/tool plus an actual connected simulator/emulator/device and app build.
6. For Penpot or another MCP, run a read-only list/inspect probe before any scoped write.
7. For preview hosting, distribution, participants, or device labs, verify account/project access, authority, privacy, quotas, and candidate identity without publishing/uploading.
8. Record environment, versions, evidence, status, degradation, and confirmation ID in `design/toolchain.json`; never record credentials.

Set `checked_at` only after every applicable probe ran. Execution requires a timezone-aware ISO-8601 timestamp no older than four hours and no more than five minutes in the future; re-probe sooner on any phase, platform, claim, target/build, environment/access, version, or status change.

Prototype profiles use a non-empty representative platform matrix. Include at least one target/configuration for every materially distinct implementation/adaptation class needed by the design question, with explicit exclusions. For `shared-web-wrapper`, the browser UI and packaged shell are separate evidence rows even though source is shared.

Report capability, requirement, adapter, exact status, probe evidence, consequence, and next action.

## Missing-capability protocol

Do not quietly produce a lower-fidelity artifact.

1. Name the capability, why this question needs it, and which claim/gate becomes unavailable.
2. Assign `missing-blocking` or `missing-degradable`.
3. Offer setup and, only if safe, one precisely bounded degraded mode.
4. Ask for explicit confirmation. It authorizes the draft, not the missing evidence.
5. When setup is requested, inspect OS/architecture/framework/package manager/CI and browse current official documentation. Provide exact prerequisites and commands, files/accounts changed, least-privilege configuration, a minimal verification flow, Git artifact location, and uninstall/disconnect/rollback steps. Ask before adding dependencies, installing system tools, connecting accounts, changing CI, publishing, or distributing.
6. Re-probe and update `design/toolchain.json`.

Keep MCP tokens out of prompts, logs, screenshots, and Git. Do not expose a local MCP listener beyond its trusted local boundary.

Official starting points to verify live:

- [Playwright installation](https://playwright.dev/docs/intro)
- [Playwright browser installation](https://playwright.dev/docs/browsers)
- [Maestro CLI installation](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli)
- [Penpot MCP](https://help.penpot.app/mcp/)
- [Storybook installation](https://storybook.js.org/docs/get-started/install)
- [React Native Storybook](https://storybook.js.org/tutorials/intro-to-storybook/react-native/en/get-started/)
- [Widgetbook quick start](https://docs.widgetbook.io/quick-start)
- [Xcode previews](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode)
- [Compose previews](https://developer.android.com/develop/ui/compose/tooling/previews)
- [Web accessibility with Playwright](https://playwright.dev/docs/accessibility-testing)
- [Android accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing)
- [Flutter accessibility](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility)
- [Cloudflare web review hosting](https://developers.cloudflare.com/pages/get-started/)
- [Firebase App Distribution](https://firebase.google.com/docs/app-distribution)
- [Firebase Test Lab](https://firebase.google.com/docs/test-lab)

## Hard evidence boundaries

- no working render/runtime means no visual or interaction approval;
- no repeatable interaction evidence means no deterministic behavior claim;
- no applicable accessibility inspection/manual plan means no accessibility gate pass;
- no required physical-device run means simulator evidence only;
- no representative participants means heuristic/internal evidence only;
- no durable isolated artifact means no continuing-pipeline prototype;
- prototype captures cannot become approved baselines in this skill.

A confirmed degradation may change the prototype medium or narrow the question only when an alternative actual renderer/capture capability is proven and the rebuilt profile passes. The artifact remains isolated and its evidence boundary is explicit. If target render/capture is unavailable, stop; an unrendered setup-ready source tree is not executable prototype evidence and cannot advance through Gate C.
