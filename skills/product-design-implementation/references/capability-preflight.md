# Capability preflight for implementation

Before recommending setup or changing a tool, read the relevant sections of the suite's canonical tool selection baseline from the sibling `product-design/references/tool-selection-baseline.md` skill resource. It explains why the free-first defaults were chosen and what an alternative must prove. If that resource is unavailable, stop any toolchain-change proposal and request installation of the complete `product-design` suite; do not recreate the comparison from memory.

Run this before production writes. The purpose is to expose whether the agent can obtain the evidence the requested implementation needs, rather than pretending that source inspection or an MCP is equivalent to a real runtime.

## Status vocabulary

Use exactly one status per relevant capability:

- `available` — verified now with a read-only version, help, list, build, device, or access probe.
- `missing-blocking` — absent or inaccessible, and no honest implementation/acceptance route remains.
- `missing-degradable` — absent or inaccessible, but a specifically reduced, reversible task could still produce value after owner confirmation.
- `unknown` — evidence conflicts or a safe probe cannot establish availability. Treat as blocking until resolved.
- `not-applicable` — the current architecture, target, or claim does not need it. State why.

Do not add synonyms such as “probably installed” or “configured.” A config file without successful access is `unknown`.

Capability status and evidence disposition are separate. Label every gate or claim that lacks sufficient evidence exactly `Not evidenced`, while retaining its canonical capability status.

## Capability classes

Classify the capability before assigning status:

- **Required now:** Git/state identity, target build toolchain, approved input identity, and the real runtime/accessibility path needed for every claimed target.
- **Conditional now:** Playwright, axe, Maestro, native UI tests, workbench/previews, token generation, physical devices, distribution, or user evidence when the target or claim activates them.
- **Optional accelerator:** an MCP or hosted service that saves interaction but does not replace repository artifacts or deterministic execution.

Do not list an irrelevant catalog of absent tools. Evaluate the minimum tool set that materially improves this task. Once a tool is selected as useful, its absence must be visible.

## Discovery order

1. Read `design/toolchain.json` if present. Treat it as a cache of intended capabilities, not current proof.
2. Inspect repository manifests, lockfiles, scripts, CI, test configs, stories/previews, native projects, wrapper configs, and baseline manifests.
3. Inspect the agent's callable tools and MCP servers. An MCP is available only after a harmless live probe; a configured name is not proof.
4. Use read-only local probes such as `git --version`, the repository's package-manager version, framework `--version`/doctor commands, `xcodebuild -version`, `./gradlew tasks`, `flutter doctor`, `maestro --version`, or a device/browser list.
5. Verify authentication/access with a read-only list or status call. Never print tokens or secrets.
6. Verify the smallest target runtime: build/list first, then one representative render or test before broad execution.

Record the observation time, command/tool, version, access scope, target, and evidence location. Set the record-level `checked_at` only after every applicable capability has been probed; for execution it must be no older than four hours and no more than five minutes in the future. A phase, platform, claim, target/build, access, version, or status change requires a new probe sooner. Implementation may update `design/toolchain.json` only when design-record writes are authorized; otherwise return proposed entries in the handoff. Never store credentials, account identifiers, participant data, or private URLs.

## Minimum implementation matrix

| Capability | When active | Missing result |
|---|---|---|
| Git and exact target-state identity | Always | `missing-blocking` |
| Approved contract/reference and authorized slice | Always | `missing-blocking` |
| Project's existing build/runtime toolchain | Always for production implementation | `missing-blocking`; reduced non-production work requires a new worker route |
| Browser execution and capture | Claimed web/PWA UI | `missing-blocking`; stop before production writes |
| Web automated accessibility plus manual plan | Claimed web/PWA UI | `missing-blocking` for acceptance |
| Simulator/emulator/app execution and capture | Claimed mobile UI | `missing-blocking`; stop before production writes |
| Platform accessibility automation/inspection plus assistive-tech plan | Claimed mobile UI | `missing-blocking` for acceptance |
| Workbench/preview | Existing reusable system or hard-to-reach states | `missing-degradable` only if no equivalent checked-in fixture exists |
| Style Dictionary/token compiler | Repository already generates multiple outputs | `missing-blocking` if canonical outputs cannot be regenerated; otherwise `not-applicable` |
| Penpot exact layer/export | Contract depends on an unavailable design detail | `missing-degradable` if approved exports are sufficient; otherwise `missing-blocking` |
| Physical-device service | Release/device-specific claim | `missing-degradable` for ordinary implementation; `missing-blocking` for that claim |
| Review distribution | Human reviewer cannot run target | `missing-degradable` |
| Representative-user evidence | User asks to call behavior usable/validated | `missing-blocking` for that claim; implementation may still follow an approved contract |

For a shared web wrapper, browser execution and packaged-app execution are both active: Playwright proves the shared UI and a simulator/device smoke proves the wrapper, safe areas, keyboard, plugins, and WebView behavior.

## Response when something is missing

Before continuing, state:

1. capability and status;
2. how it was checked;
3. which target, evidence, or claim is lost;
4. smallest setup path from [tool-setup.md](tool-setup.md), adapted to the existing project;
5. exact verification probe after setup;
6. one specific choice: set it up, grant access, supply equivalent evidence, or confirm a named degraded scope.

Do not ask for degraded implementation when the missing item is a hard gate. Stop this worker with no production mutation. Offer setup/equivalent evidence, or ask the router to obtain explicit confirmation for a fresh read-only review, contract-planning, or isolated-prototype route. The new route must use its own authority, platform matrix, current preflight, and truthful evidence boundary.

## MCP rule

MCP servers are adapters only:

- Penpot MCP may expose a selected layer; exported reference plus contract stays authoritative.
- Playwright MCP may help explore; Playwright tests, traces, and screenshots are the evidence.
- Maestro MCP may inspect a live device; Maestro YAML/native tests and captures are durable.
- Storybook MCP may discover states; story source and actual render are durable.
- Clarity MCP is not required; consented observations or exported evidence are the input.

If an MCP is missing but the underlying durable capability is verified, mark the MCP `not-applicable` unless interactive access is specifically needed. Never call the workflow degraded merely because an adapter is absent.
