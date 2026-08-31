---
name: product-design-contract
description: Encode or repair durable design-system rules, semantic tokens, component states, adaptive behavior, source ownership, accepted design identity, and code-first maintenance guidance. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. This is the only worker that may record an explicitly approved baseline.
compatibility: Uses the repository's existing design-system and version-control conventions. Accept-freeze uses repository-native integrity checks; bundled validators are required only when the project uses their formal schemas.
metadata: {version: "1.2.0"}
---

# Product Design Contract

Create one small, inspectable source of design truth that makes future implementation and change safer. A contract records decisions; it does not invent approval or force a new design-system stack onto a project.

## Modes and authority

| Mode | Purpose | Allowed mutation |
| --- | --- | --- |
| Encode | Turn a selected direction or stable existing design into reusable rules | Design-contract artifacts only |
| Re-architect | Reconcile fragmented or duplicated authorities without intentional visual or behavioral change | Contract proposal and authorized design-system files only |
| Maintenance-handoff | Finalize a broad implemented and reviewed design for granular future changes | One repository-native routine design guide, its minimal discoverability pointer, an existing-style guidance integrity check when useful, and authorized stale-guidance cleanup; never product UI, behavior tests, or baseline identity |
| Accept-freeze | Record a named, reviewed candidate that a human explicitly approved as the accepted identity | The exact approved contract/reference/baseline artifacts and minimal acceptance metadata needed to bind their identity |

Outside explicit accept-freeze mode, never overwrite, regenerate, move, delete, or relabel accepted references, goldens, baseline manifests, or their hashes.

## Practice

1. **Inspect existing authority and rationale.** Locate tokens, themes, global styles, component libraries, generated outputs, platform variants, tests, accepted references, and ownership boundaries. Use history and dependent surfaces to understand apparent duplication or odd behavior before replacing it.
2. **Choose the smallest useful contract.** Extend the repository's existing source of truth when it is coherent. Do not create a second token root, component family, or design-document hierarchy merely to match this suite.
3. **Encode observable decisions.** Capture product-specific principles, semantic tokens, component anatomy and relevant states, content and accessibility rules, responsive or adaptive behavior, intentional platform/brand/theme variants, and a lightweight map from shared rules to their consumers.
4. **Use complexity only when earned.** CSS variables may be enough for one web output. Structured tokens and a mature compiler are useful when aliases, multiple themes, platforms, or generated formats make deterministic generation valuable. Reuse existing previews, fixtures, stories, and native workbenches instead of installing new ones by default.
5. **Preserve behavior during re-architecture.** Separate authority cleanup from design change. Compare the current and candidate outputs across affected consumers; if reconciliation would alter appearance, behavior, public API, or a fixed product decision, stop and route that delta through direction or change work.
6. **Make updates idempotent.** If the requested contract already exists and matches the product, make no edit. Update canonical entries in place, avoid duplicate declarations and records, and ensure deterministic generation so a second run produces no diff.
7. **Leave a maintenance path after durable finalization.** For a broad design that is implemented, reviewed, and explicitly being finalized for future work, use maintenance-handoff to create or update one discoverable code-first guide. Skip this mode for ordinary local changes.

Read [contract protocol](references/contract-protocol.md) for multi-platform generation, source-map work, or a substantial authority re-architecture. Read [platform adapters](references/platform-adapters.md) only for the actual targets. Use [tool preflight](references/tool-preflight.md) only when a needed compiler, runtime, design source, or evidence path is uncertain.

Read [maintenance handoff](references/maintenance-handoff.md) before maintenance-handoff mode. Keep production code and behavior-focused tests authoritative for exact styling and interaction. Record only stable product consequences, canonical owners, preservation boundaries, representative verification, and truthful reference status. Reconcile competing agent-facing guidance within the authorized cleanup scope; do not copy prototype implementation or session history into the routine guide. Do not declare a no-op from the routine guide alone: classify retained design records and verify every source-map consumer and current-authority claim. Maintenance-handoff does not imply human acceptance, baseline authorization, or release readiness.

When the repository uses the bundled formal contract schema, run:

```text
python3 <product-design-contract-skill-directory>/scripts/validate_design_contract.py --project-root <repository> --mode draft
```

### Accept-freeze

Read [accept and freeze](references/accept-and-freeze.md) before any accepted-identity mutation. Require all of the following:

- the human explicitly names or unambiguously identifies the reviewed candidate and the target/state matrix being accepted;
- the candidate identity still matches what was reviewed;
- material before/candidate differences and missing evidence are visible;
- every protected image is an active deterministic golden or an explicitly approved reference, never a capture mislabeled as protection;
- only the named accepted artifacts and disclosed repository-native acceptance metadata will change.

An instruction to update snapshots, a passing regenerated test, agent preference, or general enthusiasm is not acceptance. When the formal schema is in use, validate the completed freeze with the exact approval identity:

```text
python3 <product-design-contract-skill-directory>/scripts/validate_design_contract.py --project-root <repository> --mode freeze --approval-id <approval-id>
```

## Definition of done

- Each semantic decision has one clear canonical owner; intentional variants and generated outputs are explicit.
- Contract rules are observable and product-specific, with the relevant component states, content extremes, accessibility semantics, and target adaptations represented.
- Shared tokens and components can be traced far enough to understand the real impact of a future change.
- Re-architecture introduces no unintended visual, behavioral, accessibility, API, or platform regression.
- Maintenance-handoff leaves one discoverable routine guide that traces stable intent to current code and tests, removes or disconnects competing active guidance within scope, and creates no UI or baseline change.
- The same request and inputs produce no duplicate authority, artifact, or diff on a second run.
- Baselines changed only in a completed accept-freeze operation for the exact human-approved candidate; otherwise they remain untouched.
- The handoff names the contract changes, validation performed, consumers affected, remaining uncertainty, and the smallest authorized next worker and scope.
