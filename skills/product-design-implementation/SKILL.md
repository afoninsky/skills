---
name: product-design-implementation
description: Internal production-implementation worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-implementation, or advanced automation supplies an immutable approved design input, bounded production-write authority, and equivalent routing context; for every other raw UI/UX request, use product-design. Convert an approved contract, mock, or representative reference into framework-native components and screens with real states, runtime evidence, accessibility checks, and strict baseline protection. Do not perform discovery, visual exploration, disposable prototyping, change an accepted UI, audit, or update baselines.
compatibility: Requires Git and the target project's existing build toolchain. Runtime and accessibility capabilities are hard acceptance gates. Playwright, axe, Maestro, native tests, previews, workbenches, and external services are conditional; the skill preflights them and never silently degrades.
license: MIT
metadata: {version: "1.0.0"}
---

# Product Design Implementation

Realize an approved design in the product's existing architecture. Treat design intent as an input contract, not an invitation to redesign. Production source, runtime behavior, and accessibility evidence are the output; a plausible code diff is not enough.

## Authority

- Preserve the user's original request and any routing envelope verbatim.
- If invoked directly, create the same compact handoff described below, but do not orchestrate another worker.
- Require an approved design contract or an equivalently explicit reference plus the authorized slice. If visual, interaction, state, or content decisions remain material and unresolved, stop and name the missing decision.
- Require one implementation entry basis: `gate-c-approved` with the named representative-slice approval, or `bounded-reviewed-slice` with a human approval identifying the immutable mock/reference and exact slice. New, multi-surface, or high-impact work cannot use the bounded-slice exception.
- Never select a direction, change a fixed design rule, broaden scope, accept a candidate, or update an approved reference or visual baseline.
- If implementation exposes a contract gap, report the smallest proposed contract decision and wait. Do not hide a new design decision in code.

## Load only what applies

Read [capability-preflight.md](references/capability-preflight.md) before acting and [implementation-evidence.md](references/implementation-evidence.md) before verification.

Detect the implementation architecture from manifests, build files, imports, source ownership, and packaging configuration. Then read only the relevant adapter:

- Browser UI, PWA, React, Vue, Svelte, Angular, or Web Components: [platform-web.md](references/platform-web.md)
- SwiftUI, UIKit, or mixed Apple UI: [platform-apple.md](references/platform-apple.md)
- Jetpack Compose, Android Views, or mixed Android UI: [platform-android.md](references/platform-android.md)
- React Native or Expo: [platform-react-native.md](references/platform-react-native.md)
- Flutter: [platform-flutter.md](references/platform-flutter.md)
- Capacitor, Cordova, Tauri mobile, or another web-to-native wrapper: read [platform-shared-web-wrapper.md](references/platform-shared-web-wrapper.md) plus the web adapter and the applicable shell adapter.

When architecture is mixed, load each adapter that owns part of the requested slice. Do not infer that a mobile directory owns UI: wrappers often package one web component tree.

## Workflow

### 1. Bind the accepted inputs

Locate and record:

- target Git ref and dirty-worktree state;
- accepted brief, direction/reference, contract, and their recorded hashes when present;
- component/state inventory and responsive/adaptive rules;
- source map from tokens and components to surfaces/platforms;
- existing visual-baseline manifest and protected paths;
- the authorized surface, states, targets, and files or packages;
- product behaviors and legacy journeys that must remain unchanged.

Prefer repository-owned artifacts. An editable design tool or MCP may supply exact selected-layer context, but is an adapter, not authority. If an approved artifact cannot be identified, stop with `needs-owner` rather than choosing one.

### 2. Detect the real implementation surface

Inspect before proposing dependencies:

- package, workspace, Xcode, Gradle, CocoaPods/SPM, and Flutter manifests;
- component conventions, token sources and generated outputs;
- CSS/import precedence, theme boundaries, and shared UI packages;
- routes/screens, native shells, plugins, and platform-sharing relationships;
- existing previews, stories, fixtures, unit/UI tests, screenshot assertions, and CI commands.

State the detected architecture and ownership in one paragraph. If evidence conflicts, treat ownership as a blocking unknown.

### 3. Run capability preflight

Publish the capability table before production writes. Read `design/toolchain.json` if present, then verify rather than trusting stale configuration. Classify only capabilities relevant now as `required`, `conditional`, or `optional`. Use exactly `available`, `missing-blocking`, `missing-degradable`, `unknown`, or `not-applicable` for status.

- Missing Git, target build toolchain, an executable runtime for every target in the authorized matrix, or a platform-appropriate accessibility path stops this worker before production writes.
- Do not offer a source-only production patch as degraded implementation. Return `blocked` with no production mutations. The router may offer setup/equivalent evidence or, after the owner confirms a reduced non-production goal, create a fresh envelope for read-only review, contract planning, or an isolated prototype artifact whose own preflight passes.
- User evidence is a hard gate only for a usability or validation claim. Implementation of already-approved behavior does not manufacture that claim.
- If a selected useful tool is unavailable or inaccessible, explain the lost evidence and provide the official setup steps from the preflight reference. A non-hard conditional capability may have a precisely reduced scope only when all implementation hard gates still pass; otherwise stop and ask the router to reroute. Never silently substitute an MCP, screenshot, or model judgment.
- Label every unavailable gate or unsupported evidence claim exactly `Not evidenced`; use capability statuses only for tool availability and worker status only for the handoff.

### 4. Freeze mutation and preservation scope

Before editing, write the implementation plan in working context:

- allowed source areas, components, tokens, surfaces, states, and targets;
- protected source areas and every approved-reference/baseline path;
- expected intentional runtime differences;
- preservation matrix for shared components/tokens and legacy journeys;
- checks that will prove the slice and catch regressions.

If a repository change manifest exists, obey it. If scope must expand, stop and request a revised manifest. Baseline updates are always forbidden in this worker, even if the manifest is malformed.

### 5. Implement one representative slice

- Extend existing components, themes, token bindings, navigation, state management, localization, and test architecture.
- Use real framework controls and semantics. Avoid screenshot tracing, giant positioned layers, duplicated page-local component systems, and prototype-only shortcuts.
- Represent loading, empty, error, disabled, focus/selected, long content, localization, permission, and recovery states required by the contract.
- Use realistic content extremes and deterministic fixtures. Do not let happy-path placeholder content conceal layout behavior.
- Bind semantic tokens at the established source of truth. If multiple outputs are already generated, change the canonical token input and verify generated diffs. Do not introduce Style Dictionary for a single-output system merely because it is available.
- Build and review the representative slice before repeating the pattern. Propagate only after the slice passes runtime and accessibility gates and matches the approved intent.
- Do not use technical checks as a substitute for Gate C. Propagation beyond an explicitly bounded reviewed slice requires the router's recorded Gate C approval ID.

### 6. Verify in the real runtime

Inspect representative screenshots or device renders before reading implementation rationale. Compare matched state, content, viewport/device, text scale, theme, locale, crop, and runtime version.

Run the smallest relevant set that proves:

- build/type/static correctness and affected functional behavior;
- component states in the existing workbench/preview or fixture route;
- runtime behavior at the required target matrix;
- accessibility automation plus the applicable manual/assistive-technology plan;
- responsive/adaptive behavior, text scaling, safe areas, input/keyboard, and orientation where applicable;
- preservation of dependent surfaces and legacy journeys;
- no approved baseline or reference changed.

Candidate captures go to temporary/test-output locations or an explicitly designated candidate directory. They never overwrite goldens. Resolve the bundled script relative to this skill package and use it before handoff:

```sh
python <skill-directory>/scripts/check_protected_paths.py --root <repository> --base-ref <accepted-ref> --manifest design/baselines/manifest.json
```

If the repository uses another baseline layout, pass each protected prefix with `--protected`. Read the script's help before use.

### 7. Report the delta without accepting it

Use [implementation-delta-report.md](assets/implementation-delta-report.md). Separate:

- implemented source behavior;
- observed runtime evidence;
- accessibility evidence and manual gaps;
- matched visual deltas from the approved reference;
- preservation results;
- missing tools, skipped configurations, and claims labeled `Not evidenced`.

Passing tests do not make a visual delta intentional. Return the candidate for independent review and human acceptance.

## Hard stops

Stop before consequential work when:

- the approved reference, contract, target state, or implementation authority is ambiguous;
- `implementation_entry_basis` or its human approval ID is absent, or a broad route attempts to bypass prototype/Gate C;
- the request is actually a change to an accepted surface/component/token rather than a new approved implementation;
- navigation, product behavior, content policy, or a fixed visual principle would change;
- the architecture owner cannot be identified;
- a required tool or access path is missing and the user has not chosen setup or a valid reduced scope;
- runtime or accessibility evidence needed for the claimed target cannot be produced;
- any protected baseline/reference changed;
- the representative slice fails and propagation would multiply the defect.

Runtime, accessibility, and claim-relevant user-evidence gates cannot be waived. When an implementation hard gate is missing, this worker performs no production mutation; reduced non-production work belongs to a newly validated review, contract-planning, or isolated-prototype route.

## Handoff

End with both a concise human summary and this JSON shape. Set `baseline_changed` to `false`; if it is not false, status is `failed` and restore only your own baseline mutation without touching pre-existing user work.

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-implementation",
  "status": "complete | needs-owner | blocked | failed",
  "input_hashes": {"original_prompt": "<sha256>"},
  "artifacts_created_or_changed": [],
  "production_mutations": [],
  "evidence": [],
  "missing_evidence": [],
  "degraded_capabilities": [],
  "baseline_changed": false,
  "gate": null,
  "recommended_next_worker": "product-design-review",
  "exact_next_action": "..."
}
```

Use `complete` only when the authorized implementation is exercised in every claimed runtime and the accessibility gate passes. If a hard gate failed preflight, use `blocked`, keep `production_mutations` empty, recommend no successor from this worker, and make the exact next action setup/equivalent evidence or a router-owned reduced-scope decision.
