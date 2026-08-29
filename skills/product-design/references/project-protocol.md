# Project design protocol

Use durable project-design records only when they improve continuity, collaboration, impact analysis, or protection. Existing repository conventions take precedence. Do not initialize a `design/` hierarchy for a small atomic request that is already clear in source, tests, and the user prompt.

## Proportional records

A long-running or accepted-design engagement may benefit from:

```text
design/
  project-design.json
  brief.md
  experience-map.md
  contract/
  decisions/
  prototypes/
  references/
  baselines/
```

Create only the artifacts the work actually needs. Tests, fixtures, previews, and goldens should stay in their framework-native locations unless the project already centralizes them.

## Recovery spine

For resumable work, a compact `project-design.json` may link to:

- current objective and scope;
- accepted or selected artifact identities;
- target platforms and shared implementation ownership;
- active candidate, change, or review;
- material approvals and protected paths;
- assumptions, blockers, and exact next action.

Reference durable files rather than copying long prose. Update existing entries in place and avoid parallel records. If the same request and state recur, the record should remain unchanged.

## Source and impact map

Create a lightweight source map only when shared tokens, components, generated outputs, surfaces, or platforms make impact difficult to infer reliably. Map enough to answer:

```text
design decision → canonical source → consumers → representative evidence
```

Do not attempt to mirror the entire code graph. Existing imports, tests, stories, or documentation may already provide sufficient mapping.

## Artifact states

- **Exploration:** isolated and reversible; not production authority.
- **Candidate:** implemented or rendered for review; not accepted identity.
- **Accepted:** explicitly named and human-approved with durable identity.
- **Archived or superseded:** retained only when provenance or rollback matters.

Do not infer acceptance from filenames, chat enthusiasm, recency, green tests, or agent recommendation.

## Baselines

A baseline record distinguishes active deterministic goldens, explicitly approved references, capture-only evidence, and unknown or stale artifacts. Store the target/state/environment identity needed to reproduce each protected item.

Only `product-design-contract` accept-freeze may change accepted baseline identity, and only for the exact reviewed candidate the human approved. Candidate captures should remain outside protected paths. A later change derives a new candidate; it does not overwrite the accepted comparison state.

## Existing repositories

Before adding or replacing records:

1. inspect current design docs, source authority, tests, visual evidence, history, and ownership;
2. understand why duplicated or unusual behavior exists;
3. extend established conventions where they are coherent;
4. introduce mapping rather than moving large artifact sets;
5. make migrations reversible and verify no intended behavior or visual identity was lost.
