# Product Design skill suite

The Product Design suite gives an agent one stable entrypoint for creating and evolving web and mobile interfaces without relying on chat memory for visual consistency.

Use:

```text
$product-design <your original request>
```

The entrypoint inspects the repository and current design state, checks the applicable tool capabilities, and routes one focused worker or a gated series. You do not need to choose the worker yourself.

## Skills

| Skill | Responsibility |
|---|---|
| `product-design` | Common entrypoint, router, dependency preflight, state transitions, and human gates |
| `product-design-discovery` | Users, jobs, flows, content hierarchy, requirements, states, and research |
| `product-design-direction` | Visual reference research, distinct directions, comparison, and selection evidence |
| `product-design-contract` | Principles, semantic tokens, components, adaptive rules, source map, and explicit baseline freeze |
| `product-design-prototype` | Isolated wireframes, mocks, interaction proofs, and representative slices |
| `product-design-implementation` | Approved design to real framework-native components and screens |
| `product-design-change` | Baseline-protected, impact-mapped, surgical iteration |
| `product-design-review` | Read-only visual, UX, system-drift, accessibility, and periodic review |

Workers are directly invokable for advanced or automated use, but the normal interface is `$product-design`.

## Install

Install the complete repository so the router can find every worker:

```bash
npx skills add afoninsky/skills
```

For a local checkout:

```bash
npx skills add /path/to/skills
```

Review what will be installed first when required by your runtime:

```bash
npx skills add afoninsky/skills --list
```

The portable skill format does not declare nested dependencies. The `product-design` entrypoint therefore preflights the selected worker and stops with installation instructions if it is missing.

## Typical requests

### Start from an idea

```text
$product-design Design and build a responsive booking product for independent music teachers. Start from scratch.
```

The router records the whole objective but begins with discovery. It will stop at the UX brief gate before visual direction, at direction selection before freezing rules, and at representative-slice approval before production propagation.

### Implement an approved design

```text
$product-design Convert the approved phone and tablet mock into reusable Flutter widgets. Preserve its hierarchy and use the existing app architecture.
```

The router verifies the approved reference and contract, detects the Flutter implementation, checks the available preview/runtime/accessibility capabilities, and launches implementation only when prerequisites exist.

### Make a local change

```text
$product-design Reduce vertical spacing in the checkout summary only. Do not change typography, colors, ordering, other components, or approved baselines.
```

The router selects the change worker. It resolves the affected component and tokens, writes an allowed-change manifest, renders the accepted base, applies the smallest patch, and rejects undeclared files or visual diffs.

### Audit without modifying

```text
$product-design Review the current web and mobile UI for design-system drift and accessibility risks. Do not fix anything.
```

The router launches the read-only review worker. Findings can become later change requests only after authorization.

### Resume

```text
$product-design Direction B is approved. Continue.
```

The router reads `design/project-design.json`, verifies the recorded candidate and approval, and advances to contract work instead of reconstructing the direction from conversation.

## Pipeline and gates

```text
Original request
  → product-design router
  → discovery
  → Gate A: approve UX brief and structure
  → direction
  → Gate B: select one visual direction
  → contract
  → prototype representative slice
  → Gate C: approve the slice on representative targets
  → implementation
  → review
  → Gate D: accept, reject, or revise the named reviewed candidate
  → Gate E: explicitly approve that exact candidate and reviewed matrix as the new accepted identity
  → contract `accept-freeze`: record the approved identity and baseline hashes
```

When release readiness or a research/learning action is in scope, `product-design-review` owns the evidence packet and stops separately:

```text
review release or learning evidence
  → Gate F: owner releases/holds, or approves/revises/rejects the named research or learning action
```

Gate D acceptance is not Gate E authorization. Gate E must identify the immutable reviewed candidate, its exact representative matrix and material diffs, and an approval ID. `accept-freeze` records that already-made decision; it does not ask for or manufacture approval. Gate F is not implied by visual acceptance or a freeze, and review never deploys, instruments, or contacts participants on the owner's behalf.

Later changes use:

```text
change impact and manifest
  → surgical patch
  → deterministic review
  → human approval or rejection
  → explicit `accept-freeze` only when the approved baseline intentionally changes
```

Not every request uses every phase. The router chooses the earliest missing prerequisite and the shortest valid route. New, multi-surface, or high-impact production work requires the representative prototype and Gate C. A direct implementation route is reserved for an immutable, named, explicitly bounded reviewed slice with an approval ID.

### Representative platform matrices

Direction, contract, and prototype profiles always name at least one applicable platform class: `web`, `native-mobile`, or `shared-web-wrapper`. This is not a demand to test every device. It means the route includes at least one representative configuration for every materially distinct implementation or adaptive-behavior class it claims, with explicit exclusions. A matrix row records the target/runtime, surface and state, viewport or device/window class, input, text/display scale, theme/locale, and required evidence.

Use `shared-web-wrapper` when one responsive web UI is packaged in a native shell. Its matrix contains both a real-browser row for the shared UI and a packaged-app row for WebView, safe-area, keyboard, lifecycle, bridge/permission, and native-back behavior. Use `web` plus `native-mobile` when the UI implementations are genuinely independent.

Gate B compares every direction on the same representative matrix. Gate C exercises the named slice on that matrix. Gates D and E bind their decision and approval to the reviewed matrix, and Gate F binds release or learning claims to the actual release, population, platform, and configuration coverage. A narrower matrix supports only a narrower claim.

## Tool dependency behavior

The suite knows the approved free-first tool stack, but depends on capabilities rather than brands. It reuses an established project alternative when that alternative produces equivalent durable evidence.

### Core and conditional tools

| Capability | Approved default | Typical use |
|---|---|---|
| Versioning and rollback | Git and optional GitHub protected checks | contracts, implementation, changes, acceptance |
| Structured visual source | Penpot Free; MCP on demand | direction, prototype, selected-layer context |
| Semantic styles | CSS variables or DTCG JSON | accepted design rules |
| Multiple token outputs | Style Dictionary | multi-platform, multi-theme, or generated formats |
| Component states | Existing state route, Storybook, RN Storybook, Widgetbook, Xcode or Compose previews | representative components and edge states |
| Web runtime/goldens | Playwright Test | browser behavior, responsive matrix, visual regression |
| Mobile runtime/goldens | Maestro CLI and native tests where needed | installed app flows and screenshots |
| Accessibility | axe/Playwright and platform-native inspection/tests | automated and assisted evidence |
| Web review build | Existing preview host or Cloudflare Pages Free | human candidate review |
| Mobile review build | Firebase App Distribution or existing beta channel | real-device tester access |
| Physical-device sample | Firebase Test Lab or existing device lab | significant mobile candidate evidence |
| Pre-release users | Moderated testing or Lyssna Free | comprehension and task evidence |
| Post-launch behavior | Microsoft Clarity | consented behavior evidence for a named decision |
| Live agent access | Penpot, Maestro, Storybook, Playwright, or Chrome DevTools MCP | optional scoped interaction only |

MCP servers are adapters. Losing one must not lose the design: exports, token source, stories/previews, test flows, screenshots, and approvals remain in Git.

### Preflight statuses

Before a worker uses an applicable capability, it records one of:

- `available`
- `missing-blocking`
- `missing-degradable`
- `unknown`
- `not-applicable`

The suite never silently falls back.

For execution, `design/toolchain.json.checked_at` is a timezone-aware ISO-8601 timestamp certifying that all applicable statuses were actually probed no more than four hours ago and no more than five minutes in the future. Do not refresh the timestamp without rechecking the selected capabilities. Re-probe sooner whenever phase, platform, claim, scope, target/build identity, credentials/access, tool version, or observed status changes.

For a missing capability it explains:

1. what is missing;
2. why the selected phase needs it;
3. what work remains possible;
4. what evidence and claims become unavailable;
5. step-by-step setup instructions tailored to the project and checked against current official documentation;
6. whether it needs setup authorization or confirmation of a precisely bounded degraded mode.

The agent waits for the answer. It does not install dependencies, connect an account, change CI, expose a server, or add analytics without permission.

### Degraded mode

A confirmed degraded route may still produce useful read-only review, contract planning, or an isolated lower-fidelity prototype when that new route has its own valid capability profile. It is not a way to pass a gate or to let implementation/change write unverified production source.

Examples:

- No Penpot: the user may approve an isolated code-rendered mock or annotated-reference workflow when its renderer/capture path is proven, but structured selected-layer editing is unavailable.
- No Playwright for a protected web implementation/change: that production worker stops before writing. The router offers setup or a fresh read-only review, contract-planning, or isolated-prototype route; protected web acceptance remains `Not evidenced`.
- No Maestro/simulator or native accessibility path for a mobile implementation/change: that production worker stops before writing. A confirmed non-production route remains explicitly separate; installed-app and accessibility evidence remain `Not evidenced`.
- No representative users: agent critique remains heuristic and cannot be called usability validation.
- No consent/masking decision: session replay is not installed.

## Project artifacts

The default structure is:

```text
design/
  project-design.json
  toolchain.json
  brief.md
  experience-map.md
  contract/
    principles.md
    components.md
    content.md
    responsive-and-adaptive.md
    source-map.json
    tokens/
  decisions/
    selected-direction.md
    changes/
    reviews/
  references/
    approved/
    archive/
  prototypes/
  baselines/
    manifest.json
```

Existing repository conventions take precedence. Tests and screenshots may remain beside their framework tests; the manifest points to them.

`project-design.json` is the compact recovery spine. It records the original-prompt digest, paths, and hashes rather than repeating long briefs. `source-map.json` maps tokens and components to affected surfaces and platforms. Per-change manifests declare what may and must not change.

## Strict baseline rule

Only `product-design-contract` in explicit `accept-freeze` mode may update accepted baseline identity.

Acceptance requires:

- a named candidate;
- reviewed before/after/diff evidence;
- a Gate D candidate decision;
- separate Gate E human approval of the exact named candidate and reviewed matrix;
- exact Git ref and environment identity;
- a following freeze operation that records, but does not create, that approval.

Implementation and change workers cannot update approved screenshots. “Update snapshots” alone is not approval.

## Platform behavior

The suite detects the implementation rather than imposing one:

- Web frameworks use their existing components/state route or Storybook plus Playwright.
- React Native uses framework states plus Maestro/native tests.
- Flutter uses Widgetbook/widget tests when useful plus Maestro/native tests.
- Apple UI uses Xcode previews, XCTest/XCUITest, and platform accessibility tools.
- Android UI uses Compose previews/UI Check or layout fixtures plus instrumentation and TalkBack checks.
- A PWA or Capacitor-style wrapper keeps one web UI source and adds packaged-app verification; it does not create a duplicate native component system.

## Recovering from drift

When unexpected diffs appear:

1. stop the active change;
2. preserve actual/diff artifacts;
3. compare with the accepted Git ref and source map;
4. restore or reproduce the accepted base in an isolated branch/worktree;
5. revise the change manifest if the true dependency surface is broader;
6. reapply only the intended change;
7. never repair drift by asking the model to remember the old design.
