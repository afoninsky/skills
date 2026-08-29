---
name: product-design-change
description: Internal protected-change worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-change, or advanced automation supplies an accepted base, source map, baseline identity, and bounded mutation authority; for every other raw UI/UX request, use product-design. Make a controlled post-acceptance UI/UX iteration, expand shared-token and shared-component impact, enforce a machine-checkable change manifest, apply the smallest patch, and prove preservation outside the approved delta. Do not create an unapproved direction, implement a new unchanged surface, perform a read-only audit, accept a candidate, or update baselines.
compatibility: Python 3.10+ and Git are required for protected changes. Applicable browser/app runtime, visual-regression, and accessibility tools are preflighted per target. The skill works without MCP servers, but it never silently substitutes missing runtime evidence or changes approved baselines.
metadata: {version: "1.0.0"}
---

# Product Design Change

Treat “change only this” as an enforceable delta, not prompt advice. Start from the accepted identity, trace the request through shared design sources, authorize a precise manifest, apply the smallest patch, and prove that protected artifacts and out-of-scope surfaces did not move.

## Invariant

This skill never updates, re-records, regenerates, deletes, renames, or approves an accepted baseline/reference or its manifest/hash. Its candidate may intentionally differ from the accepted baseline; only a later explicit human-approved `product-design-contract` accept-freeze operation may replace that baseline.

Do not run snapshot update flags. Do not “fix” visual CI by accepting new images. A baseline change detected by the guard is a failure even when pixels look better or tests otherwise pass.

## Read only what the task needs

- Read [tool-preflight.md](references/tool-preflight.md) at the start of every invocation.
- Read [change-protocol.md](references/change-protocol.md) before impact analysis or mutation.
- Read [platform-adapters.md](references/platform-adapters.md) only for affected targets.

## Preconditions

Require:

- an accepted base Git ref;
- an accepted contract/source map or a trustworthy equivalent mapping;
- an accepted baseline manifest with verifiable hashes;
- a request that identifies an observable delta;
- production-write authority for the bounded patch;
- relevant runtime and preservation capabilities.

If contract identity or source mapping is missing, stop and recommend `product-design-contract`. If the visual grammar itself is unresolved or the request changes a fixed principle, stop and recommend `product-design-direction`. If the request is read-only, recommend `product-design-review`. Do not reconstruct accepted taste from chat or the newest stylesheet.

## Preflight before any production write

1. Detect repository, platform-sharing model, affected targets, existing state harness, and evidence needed to protect the request.
2. Classify each relevant capability as required, conditional, or optional.
3. Record status using the suite vocabulary: `available`, `missing-blocking`, `missing-degradable`, `unknown`, or `not-applicable`.
4. Probe the real CLI/configuration/connection/target. A package name or MCP registration is not enough.
5. For `missing-blocking`, stop with impact and step-by-step setup. A `missing-degradable` conditional capability may continue only after specific confirmation and only when deterministic scope/baseline protection plus every applicable runtime and accessibility hard gate still pass.
6. If deterministic baseline protection, applicable runtime reproduction, accessibility, or scope verification is missing, stop this worker before production writes. Do not offer source-only change work. The router may offer setup/equivalent evidence or, after the owner confirms a reduced non-production goal, create a fresh read-only review, contract-planning, or isolated-prototype envelope.
7. Record durable results in `design/toolchain.json` when that project protocol exists, without secrets.

## Workflow

### 1. Reproduce the accepted base

- Read project state, contract/source map, baseline manifest, and approval identities.
- Validate every protected baseline hash before work.
- Resolve the accepted `base_ref` in Git.
- Preserve unrelated user changes. Prefer an isolated branch/worktree from the accepted ref when the current tree is not a clean reproduction.
- Render affected accepted states before edits with their real content, targets, environment, fonts, and configuration.

If the accepted base cannot be reproduced, stop. A screenshot supplied from memory is not a substitute for baseline identity.

### 2. Resolve the impact graph

Trace:

```text
requested element or selected layer
  → implementation component
  → semantic tokens and shared source files
  → dependent states and surfaces
  → web/mobile targets and baseline entries
```

Penpot selected-layer context may improve element resolution, but is optional and never canonical. If unavailable and the element cannot be identified unambiguously from source plus annotated evidence, report `missing-degradable` and ask for setup or an annotated crop/selector confirmation.

Use the guard's `impact` command for mapped shared components/tokens. A shared token or component expands scope to every mapped consumer. Do not hide this expansion behind a local selector or platform-specific override.

### 3. Create and authorize the change manifest

Adapt `assets/change-starter/change-manifest.json` into a project decision such as `design/decisions/changes/CHG-014.json`. Declare:

- accepted base plus contract, source-map, and baseline-manifest hashes;
- one observable intent;
- allowed files, components, and semantic tokens;
- surfaces allowed to differ and surfaces that must remain unchanged;
- required component states, runtime targets, functional/accessibility/visual checks;
- protected references/manifests;
- `baseline_updates_allowed: false`.

Run `validate` before writes. If the manifest exactly restates a narrow implementation request and does not expand its scope, the user's instruction may be recorded as approval. If impact analysis adds a shared token, shared component, extra surface/target, changed navigation/behavior, fixed contract decision, or new dependency, stop and ask the human to approve the revised manifest.

```text
python3 scripts/change_guard.py validate --project-root <repository> --manifest <manifest>
```

### 4. Apply the smallest patch

- Extend existing tokens/components and framework conventions.
- Prefer a local semantic correction over a global override when the intent is local.
- Keep prototype shortcuts out of production.
- Do not edit the source map to legitimize an unexpected dependency; stop and route the mapping correction through contract work.
- Do not update baselines, approved references, contract/baseline manifests, or accepted hashes.
- If implementation reveals a necessary file/component/token/surface outside the manifest, stop before editing it and propose a revised impact analysis.

### 5. Verify candidate and preservation

Run the smallest complete matrix implied by impact:

- affected functional and state tests;
- applicable accessibility automation and manual plan;
- matched before/candidate/diff runtime captures;
- all mapped targets for a shared component/token;
- preservation assertions/captures for surfaces marked must-not-change;
- packaged-app smoke in addition to browser checks for a web UI wrapped as mobile.

Then run:

```text
python3 scripts/change_guard.py verify --project-root <repository> --manifest <manifest>
```

The guard verifies allowed files, source-map impact closure, baseline-manifest identity, and protected baseline hashes. A guard pass proves scope and file identity, not aesthetic quality or usability.

### 6. Present a candidate, not a new baseline

Report:

- before/candidate/diff evidence for identical configurations;
- files/components/tokens/surfaces/targets changed;
- checks passed, failed, skipped, or `Not evidenced`;
- remaining intentional delta from the old accepted baseline;
- preservation evidence and scope-guard result;
- the exact human decision required.

Recommend `product-design-review` for independent acceptance review. Only after human acceptance may the router invoke `product-design-contract` in accept-freeze mode.

## Handoff

Return the suite fields exactly:

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-change",
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

`baseline_changed` is always false for this skill. If it is not, return `failed`, identify the protected mutations, and restore only this worker's own baseline changes when that can be done without touching user-owned work.

When preflight stops on a hard gate, use `blocked`, keep `production_mutations` empty, leave `recommended_next_worker` null, and make the exact next action a setup/equivalent-evidence choice or a router-owned reduced-scope decision.

## Quality bar

- The accepted baseline is reproducible and hash-verified before mutation.
- The manifest partitions every known surface into may-change or must-not-change.
- Shared changes expand to every mapped state, surface, target, and baseline entry.
- The patch contains no unexplained production files and no baseline/reference mutation.
- Matched renders are inspected screenshot-first; prose does not override pixels.
- Missing tools/evidence remain visible and never become a pass by waiver.
- The candidate is reversible, reviewable, and clearly distinct from human acceptance.
