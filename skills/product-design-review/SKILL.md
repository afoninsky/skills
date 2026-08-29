---
name: product-design-review
description: Internal read-only review worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-review, or advanced automation supplies an immutable review target and equivalent scope; for every other raw UI/UX request, use product-design. Perform screenshot-and-runtime-first visual, UX, design-system, responsive/adaptive, accessibility, pre-release, or periodic review and return ranked findings plus bounded change briefs. Never implement findings, alter source or tests, approve a candidate, or update baselines.
compatibility: Requires Git/read access and a real target runtime for visual acceptance. Platform accessibility and claim-relevant user evidence are hard gates. Playwright, axe, Maestro, native tools, workbenches, Firebase, Cloudflare, Lyssna, Clarity, and MCPs are conditional and explicitly preflighted.
license: MIT
metadata: {version: "1.0.0"}
---

# Product Design Review

Review what users actually receive. Inspect runtime and representative captures before rationale or implementation prose. Remain independent and read-only: findings may recommend a change, but this worker never applies it, updates a baseline, or declares its own candidate accepted.

## Authority and read-only boundary

- Preserve the original request and any routing envelope unchanged.
- If invoked directly, produce the same handoff but do not invoke another worker.
- Do not edit production source, tests, tokens, contracts, approved references, baselines, analytics configuration, or external services.
- Use isolated temporary output for probes. By default, return the report in the response. Save a report only when the user explicitly names an output location, and never inside protected source/reference paths.
- Record target identity and Git status before and after review. If the target changed, invalidate affected evidence and restart or stop.
- A request to “review and fix” is review first. Recommend bounded change briefs; mutation requires separately authorized change work.

## Load only what applies

Read [capability-preflight.md](references/capability-preflight.md), then [review-evidence.md](references/review-evidence.md). For periodic/post-launch work also read [periodic-evidence.md](references/periodic-evidence.md).

Detect architecture and read only the applicable adapter:

- Browser UI/PWA/React/Vue/Svelte/Angular/Web Components: [platform-web.md](references/platform-web.md)
- SwiftUI/UIKit: [platform-apple.md](references/platform-apple.md)
- Jetpack Compose/Android Views: [platform-android.md](references/platform-android.md)
- React Native/Expo: [platform-react-native.md](references/platform-react-native.md)
- Flutter: [platform-flutter.md](references/platform-flutter.md)
- Capacitor/Cordova/Tauri mobile/another web wrapper: [platform-shared-web-wrapper.md](references/platform-shared-web-wrapper.md) plus the web and applicable shell adapters.

Load multiple adapters only when the target actually spans them.

## Workflow

### 1. Freeze the review target

Record:

- Git commit plus dirty-diff digest, or an equivalent immutable build/deployment identity;
- accepted contract/reference/baseline hashes when present;
- review surface, state, target matrix, and explicit exclusions;
- runtime URL/build/app ID without secrets;
- current design/source map and intentional themes/variants;
- review question: fidelity, quality, system drift, accessibility, release readiness, user behavior, or a combination.

If no trustworthy accepted contract exists, review can inventory current behavior and inconsistencies, but cannot label a difference “drift from accepted design.” State that limitation.

For candidate, release, or learning decisions, use a non-empty representative platform matrix with at least one configuration for every materially distinct implementation/adaptation class in the claim and explicit exclusions. For a shared web wrapper, include browser and packaged-shell rows while recognizing one shared UI source. A decision never implies unreviewed platforms or configurations.

### 2. Run capability preflight

Publish the capability table before substituting source review for runtime evidence. Read `design/toolchain.json` if present, then verify current availability with harmless probes. Review never writes the toolchain record; return proposed status updates in the handoff.

Use exactly: `available`, `missing-blocking`, `missing-degradable`, `unknown`, `not-applicable`.

Keep capability requests stage-local. Ask now only for tools, target access, and evidence needed to answer this review question. Forecast implementation/change dependencies separately and do not make them prerequisites for review. If a tool such as Maestro is required now for repeatable mobile-flow evidence, say that it serves the current review claim; do not describe it as later-stage evidence while requiring it in the current exact next action.

- Real runtime observation is a hard gate for visual/UX acceptance.
- Platform-appropriate accessibility automation/inspection plus a named manual/assistive-technology plan is a hard gate for accessibility acceptance.
- Representative-user evidence is a hard gate only for usability, comprehension, preference, or validation claims. It is `not-applicable` for a clearly labeled heuristic/system audit.
- If a useful conditional tool is missing, state what evidence is lost, provide official setup steps, and ask whether to set it up, grant access, provide equivalent evidence, or confirm a named source-only/partial review. Partial work remains blocked for the missing conclusion.
- Never silently replace runtime with screenshots, accessibility with agent inspection, or user evidence with analytics/synthetic personas.
- Label every unavailable gate or unsupported evidence conclusion exactly `Not evidenced`; capability status and worker status remain separate fields.

### 3. Inspect runtime first

Open the actual target at the agreed state and configuration. Capture or inspect the representative matrix before reading rationale. Verify the runtime corresponds to the frozen target, not a stale server, preview, cache, simulator build, or unrelated deployment.

Review at least:

- first-ten-seconds comprehension and core act;
- shell silhouette, hierarchy, proportions, density, rhythm, typography, color, shape, elevation, imagery, and motion;
- responsive/adaptive behavior, text scaling, safe areas, keyboard/input, orientation/window size, and relevant themes/locales;
- loading, empty, error, offline/retry, permissions, disabled, selected/focus/pressed, long content, and recovery;
- navigation/behavior preservation and console/runtime failures;
- accessibility semantics, focus/order, target sizes, contrast, motion, and assistive-technology behavior.

Keep two verdicts separate:

- **Fidelity:** does the candidate match the accepted contract/reference under matched conditions?
- **Quality:** is the realized experience coherent, legible, distinctive enough, robust, and fit for the intended task?

Pixel similarity does not prove quality; quality arguments do not waive an unapproved fidelity delta.

### 4. Classify every visual artifact

Inspect both each image and the source/test that produced it. Resolve the bundled script relative to this skill package and use it only as a lead generator:

```sh
python <skill-directory>/scripts/classify_visual_evidence.py <test-or-flow-path> ...
```

Classify evidence as:

- **asserted golden:** a running deterministic assertion compares the current render with a named accepted image and emits failure/diff evidence;
- **approved reference:** human-approved design/render identity, which may guide fidelity but is not automatically a regression test;
- **capture-only:** screenshot/export/attachment without an active comparison assertion;
- **unknown/stale:** producer, state identity, or current execution cannot be proven.

Examples: Playwright `toHaveScreenshot`, Maestro `assertScreenshot`, and an active native golden assertion may protect a baseline. `page.screenshot`, Maestro `takeScreenshot`, Xcode/emulator capture, a workbench image, or a file in test output is capture-only. A screenshot filename, hash, or committed status alone does not make it asserted.

Never update or re-record an image during review.

### 5. Audit contract and system drift

Trace rendered symptoms to source without editing:

- competing token roots/providers, literal values, generated/manual copies, and theme ownership;
- CSS/import/cascade order, unscoped overrides, appearance proxies, and duplicated component families;
- source-map gaps from shared tokens/components to surfaces/platforms;
- intentional platform/brand variants versus undocumented divergence;
- prototype code or local visual systems leaked into production;
- accepted states/configurations without runtime coverage;
- capture-only evidence presented as protection.

Run the applicable static, functional, visual, and accessibility checks read-only. Do not run update-snapshot, fix, format-write, code-generation-write, deployment, or analytics-instrumentation modes.

### 6. Assess periodic/post-launch evidence honestly

Start with a named decision question. Verify consent, masking/redaction, population, task/context, sampling, recency, device/platform, and target release. Treat:

- Clarity/session/heatmap events as behavioral signals, not explanations or validation;
- Firebase distribution as access to a build, not proof of use;
- Lyssna or moderated findings as user evidence only for the sampled population/tasks/method;
- support reports, analytics, and qualitative observations as separate evidence streams;
- agent or synthetic-persona critique as hypotheses only.

Do not install instrumentation, contact participants, order a panel, upload a build, or spend money during review. If claim-relevant evidence is absent, block the claim and propose the smallest study/observation plan.

### 7. Report actionable findings

Use [design-review-report.md](assets/design-review-report.md). Rank findings by user/product impact, not aesthetic preference:

- `P0` — safety, privacy, destructive/deceptive behavior, or critical accessibility blocker;
- `P1` — core task failure, severe fidelity/system break, or broad regression;
- `P2` — material inconsistency, adaptive/state gap, or recurring friction;
- `P3` — contained craft/polish issue.

For each finding include observed evidence, affected surfaces/targets/states, contract relationship, confidence, evidence limitations, and a bounded change brief. Separate fixed facts from professional judgment. Do not collapse the review into a numeric design score.

### 8. Verify read-only completion

Compare Git status/digest with the frozen start. Review-generated temporary files must remain outside the target or be removed. If the target changed, identify why; any unapproved product/baseline mutation makes the review `failed`.

### 9. Stop at Gate D for a named candidate

When the review target is an implementation or change candidate, present its exact identity, representative matrix, material deltas, preservation evidence, failures, and `Not evidenced` conclusions, then stop at Gate D. Ask the owner to accept for the next acceptance step, reject, or request a bounded revision of that named candidate. Do not preselect `product-design-change` or `product-design-contract`: the owner's decision determines the new router envelope.

Gate D acceptance is not baseline authority. After it, the router must stop separately at Gate E and ask the owner to explicitly approve the exact immutable candidate, reviewed matrix, observed diffs, and limitations as the new accepted identity. Only that Gate E approval creates an `accept_freeze_approval_id`; `product-design-contract` then records the identity in accept-freeze mode.

### 10. Stop at Gate F for release or research/learning decisions

This review worker owns the Gate F evidence packet. When the pending decision is release/hold, rollout scope, or approval/revision/rejection of a named research or learning action, present the target/release or population identity, representative matrix, applicable accessibility/device/user/safety/privacy/operational evidence, contradictions, and `Not evidenced` conclusions. Then stop with `needs-owner` at Gate F and no recommended successor.

The owner makes the decision. Review never deploys, instruments, recruits, contacts participants, orders a panel, or spends money. If evidence required for the requested decision is missing, return `blocked` before Gate F with setup/access/equivalent-evidence choices rather than asking the owner to guess.

An atomic heuristic or drift audit with no candidate, release, or research/learning decision may finish without Gate D or F and may recommend a valid next worker.

## Hard stops

Stop or narrow explicitly when:

- target/build/baseline identity is ambiguous or changed during review;
- a real runtime cannot be observed for a requested visual/UX acceptance claim;
- accessibility capability is unavailable for an accessibility/release claim;
- representative-user evidence is unavailable for a requested usability/validation conclusion;
- access would require external writes, production instrumentation, participant contact, sensitive data transfer, or spend without approval;
- an asserted golden would need updating to pass;
- requested fixes exceed read-only authority.

Runtime, accessibility, and claim-relevant user-evidence gates cannot be waived. A partial source or heuristic audit is useful only after explicit confirmation and remains limited.

## Handoff

End with a concise human summary and this JSON shape. `production_mutations` is empty and `baseline_changed` is false.

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-review",
  "status": "complete | needs-owner | blocked | failed",
  "input_hashes": {"original_prompt": "<sha256>"},
  "artifacts_created_or_changed": [],
  "production_mutations": [],
  "evidence": [],
  "missing_evidence": [],
  "degraded_capabilities": [],
  "baseline_changed": false,
  "gate": "D | F | null",
  "recommended_next_worker": null,
  "exact_next_action": "..."
}
```

For a named candidate review, use `needs-owner` at Gate D and leave `recommended_next_worker` null until the owner accepts, rejects, or requests a bounded revision. Gate E is a later router decision, not a review handoff. For a sufficiently evidenced release or research/learning packet, use `needs-owner` at Gate F and leave `recommended_next_worker` null. If its required evidence is absent, use `blocked` with no gate. For an atomic audit with no owner decision, `gate` may be null and a valid next worker may be recommended. Use `complete` only for review questions whose gates and target matrix were actually covered. A complete heuristic audit may still state that usability validation was not in scope.
