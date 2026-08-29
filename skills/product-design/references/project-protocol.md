# Project design protocol

## Default layout

Adapt to an existing repository rather than duplicating established files. When no equivalent exists, use:

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
    README.md
  baselines/
    manifest.json
```

Tests and goldens may remain in framework-native locations. The baseline manifest points to them.

## Recovery spine

Use [the project state template](../assets/project-design.json). Keep it concise and referential:

- current phase and mode;
- original-prompt SHA-256 and objective summary;
- accepted artifact paths and hashes;
- selected direction and superseded decisions;
- target platforms and source-sharing model;
- active request/change/review;
- capability preflight record;
- approvals;
- exact next action and blockers.

Read it first when resuming. Never overwrite accepted hashes while creating a candidate.

## Design source map

Map:

- tokens to generated outputs;
- components to source files, state fixtures, and token dependencies;
- surfaces/routes/screens to components and baseline states;
- shared implementations across web/mobile;
- intentional themes, brands, or platform variants.

This is an impact graph, not a complete AST. Keep it only as detailed as needed to protect shared decisions.

## Artifact states

- **Exploration:** disposable and isolated; cannot drive production automatically.
- **Candidate:** under review; does not replace accepted identity.
- **Accepted:** named human approval plus immutable path/hash/ref.
- **Archived:** retained for provenance but excluded from active context.
- **Superseded:** replaced by a named later decision; cannot silently re-enter.

## Baselines

The manifest distinguishes:

- approved visual goldens with deterministic assertion commands;
- approved structured references;
- review captures that are not assertions;
- environment identity such as OS, browser/runtime, viewport/device, fonts, locale, theme, scale, and data fixture.

Only `product-design-contract` in explicit `accept-freeze` mode may change accepted baseline identity. Candidate image generation remains outside approved baseline paths whenever practical.

The approval sequence is durable state: Gate D records the candidate disposition, Gate E separately records explicit approval of the exact immutable candidate and reviewed representative matrix, and accept-freeze records that approved identity in contract/baseline manifests. A later Gate F release or research/learning decision is a review-owned packet and remains separate from visual baseline acceptance.

## Existing repositories

Before initializing:

1. locate existing design docs and tests;
2. identify canonical and duplicate authorities;
3. preserve repository conventions;
4. create mapping files rather than moving large artifact sets without approval;
5. record unresolved conflicts as blockers or contract-rearchitecture findings.
