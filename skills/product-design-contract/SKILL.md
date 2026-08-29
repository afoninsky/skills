---
name: product-design-contract
description: Internal design-contract and accept-freeze worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-contract, or advanced automation supplies equivalent accepted inputs and authority; for every other raw UI/UX request, use product-design. Encode a selected direction into durable Git-owned principles, semantic tokens, component states, adaptive rules, and source mappings; re-architect fragmented design authorities without silently changing appearance; or freeze a named reviewed candidate only with explicit human approval. Do not explore directions, implement ordinary UI, change an accepted value, or treat a request to update screenshots as acceptance.
compatibility: Python 3.10+ runs the bundled validator. Authoritative contract and accept-freeze operations require Git. Runtime, token, design-source, workbench, and accessibility tools are selected and preflighted per target; unavailable capabilities are never silently ignored.
metadata: {version: "1.0.0"}
---

# Product Design Contract

Encode an approved design as a small, inspectable control plane. The contract describes what may vary, what must stay stable, where rules live in source, which states represent the product, and which rendered artifacts a human accepted. It does not choose a visual direction or grant itself approval.

## Invariant

Only enter **accept-freeze** mode after review has presented the named candidate for Gate D, the owner has disposed it at Gate D, and the owner has then explicitly approved that exact immutable candidate, reviewed representative matrix, and observed diffs as the new accepted identity at Gate E. Require the router's named `accept_freeze_approval_id` and record it in the acceptance/baseline identity. The contract operation records the already-made Gate E decision; it does not create another approval. “Update the screenshots,” Gate D acceptance alone, test update flags, an agent recommendation, passing tests, or silence are not Gate E acceptance. Outside that exact operation, do not create, overwrite, move, delete, or re-record approved references, baseline images, their manifests, or their hashes.

## Read only what the task needs

- Read [tool-preflight.md](references/tool-preflight.md) at the start of every invocation.
- Read [contract-protocol.md](references/contract-protocol.md) before encoding or re-architecting a contract.
- Read [accept-and-freeze.md](references/accept-and-freeze.md) before any acceptance or baseline operation.
- Read [platform-adapters.md](references/platform-adapters.md) only for the detected implementation targets.

## Choose the operating mode

| Mode | Use when | Mutation authority |
| --- | --- | --- |
| Encode | A human-selected direction must become tokens, rules, states, and mappings | Contract artifacts only; no baseline mutation |
| Re-architect | Existing style authorities or platform mappings are fragmented | Audit and proposed contract; production changes require a later worker/change manifest |
| Accept-freeze | The human explicitly accepts a named, reviewed candidate | Named contract/reference/baseline artifacts only |

If no approved direction or stable existing product intent exists, stop and recommend `product-design-direction`. If the request is to implement the contract, recommend `product-design-implementation`. If an accepted surface, token, component, or baseline must change, recommend `product-design-change` before a later freeze.

## Preflight capabilities before design work

1. Detect repository, platform-sharing model, relevant targets, existing tools, and the exact evidence required by this mode.
2. Classify each relevant capability as **required**, **conditional**, or **optional** using the preflight reference.
3. Probe the actual CLI, connection, authentication, project configuration, and usable target—not merely an installed package name.
4. Record one exact suite status: `available`, `missing-blocking`, `missing-degradable`, `unknown`, or `not-applicable`.
5. Report the result before work: capability, status, effect on output, evidence unavailable, and setup/recovery steps. Persist durable results in `design/toolchain.json` when that project protocol exists.
6. For `missing-blocking`, stop and provide step-by-step setup. For `missing-degradable`, either stop for setup or ask for specific approval to continue in a named safe degraded mode. Record its `confirmation_id` and state what will remain `Not evidenced`.
7. Never offer degraded mode when it would fabricate contract identity, runtime evidence, target coverage, accessibility evidence, or an accepted baseline. Irrelevant tools are `not-applicable` and do not need installation.

The skill may continue after an explicit degradation approval only within the stated reduced scope. Record that approval and limitation in the handoff; do not repeatedly ask once it is recorded and still applicable.

Set a non-empty representative platform matrix for encode, re-architect, and accept-freeze whenever a target platform exists. Include at least one configuration for every materially distinct implementation/adaptation class, with explicit exclusions. `shared-web-wrapper` means one shared UI authority plus separate browser and packaged-shell evidence rows; it does not mean a second native component system. Planning-only contract work may document an unverified matrix, but accept-freeze requires the exact reviewed matrix and its evidence.

## Workflow

### 1. Establish the accepted input

- Preserve the original request and explicit constraints.
- Locate the selected direction, approved references, brief, current contract, project state, and last accepted Git ref.
- Verify identities/hashes when present. Treat a missing or mismatched identity as a blocking unknown, not permission to reconstruct taste from chat.
- In an existing product, inventory every style authority, token source, global/theme scope, generated output, component library, import/override boundary, and platform sharing relationship before adding another one.
- Record the representative target/configuration matrix and explicit exclusions that the contract governs. A contract may cover several targets with one shared source, but each distinct adaptation/runtime class remains visible.

### 2. Model one coherent authority

Use the repository's established locations when clear; otherwise adapt the generic starter in `assets/contract-starter/` to `design/`.

Encode:

- principles plus a concrete avoid-list;
- semantic tokens and their canonical source;
- components, required states, content extremes, and accessibility semantics;
- responsive rules for fluid/reflow behavior and adaptive rules for platform-specific behavior;
- content, imagery, motion, and reduced-motion rules where relevant;
- intentional brands/themes/platform variants, with ownership and boundaries;
- a source map from tokens → components → surfaces → targets → evidence;
- draft contract and baseline manifests with no invented acceptance.

Prefer committed CSS variables for a single web output. Use DTCG JSON and Style Dictionary only when multiple themes, platforms, aliases, or generated formats make compilation valuable. Keep generated files labeled and verify regeneration is deterministic.

### 3. Make states executable

Use the existing framework workbench, preview, story, fixture route, widget test, or native preview when a reusable component system needs executable state coverage. Do not add Storybook, Widgetbook, Style Dictionary, analytics, or a SaaS simply because it appears in this skill. A small product may use ordinary checked-in fixtures.

Describe typical, empty, loading, error, disabled, selected, focus, permission, long-content/localization, large-text, reduced-motion, and recovery states only when applicable. Map each contracted state to its source fixture and target evidence rather than claiming prose is runtime proof.

### 4. Validate the draft

Run:

```text
python3 scripts/validate_design_contract.py --project-root <repository> --mode draft
```

Resolve structural errors. A draft validator pass proves schema/path consistency, not visual quality, usability, accessibility, or human acceptance.

### 5. Accept-freeze only on explicit instruction

Read the freeze reference and verify all of the following before mutation:

- the user names or unambiguously identifies the reviewed candidate;
- the Gate D decision and separate Gate E approval ID identify that same candidate and reviewed matrix;
- the candidate Git ref/content identity still matches what was reviewed;
- before/after evidence uses matched states, targets, content, and crops;
- every baseline entry is an asserted golden or explicitly approved reference, never a capture-only screenshot;
- relevant web/mobile runtime and preservation checks ran on the declared matrix;
- material deltas and missing hard-gate evidence are visible to the human;
- only the accepted files are touched.

Record the human identity supplied by the user, Gate E approval record, accepted ref, timestamps, exact matrix, file hashes, and assertion source. Do not describe an unavailable hard gate as passed; retain `Not evidenced` with its consequence (stored as `not-evidenced` where the JSON schema requires machine-readable lowercase values).

Then run:

```text
python3 scripts/validate_design_contract.py --project-root <repository> --mode freeze --approval-id <accept_freeze_approval_id>
```

If it fails, the freeze is incomplete. Do not partially relabel the candidate as accepted.

### 6. Handoff

End with a compact machine-readable handoff plus a plain-language summary:

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-contract",
  "status": "complete | needs-owner | blocked | failed",
  "input_hashes": {"original_prompt": "<sha256>"},
  "artifacts_created_or_changed": [],
  "production_mutations": [],
  "evidence": [],
  "missing_evidence": [],
  "degraded_capabilities": [],
  "baseline_changed": false,
  "gate": null,
  "recommended_next_worker": null,
  "exact_next_action": "..."
}
```

Set `baseline_changed` to true only for a completed explicit accept-freeze operation. Put every absent gate or claim in `missing_evidence` with the wording `Not evidenced`, and every specifically confirmed degraded mode in `degraded_capabilities`. Recommend a next worker; never launch one yourself.

## Quality bar

- Contract rules are product-specific and observable, not adjectives without consequences.
- One canonical token source exists for each semantic decision.
- Intentional variants are documented; selector scope alone does not prove intention.
- Platform sharing is explicit, including web UI wrapped by a mobile shell.
- The source map is sufficient to expand the verification matrix for a shared edit.
- Approved baselines have immutable paths, hashes, target/state identity, and an assertion or approval source.
- Screenshots that are merely captured remain evidence, never protected goldens.
- Agent judgment is never presented as human acceptance or representative-user validation.
