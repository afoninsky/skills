# Maintenance handoff

Use this mode to finalize a broad implemented and reviewed design for future
maintenance. Its output is a compact navigation and preservation aid, not a
second visual specification. Do not run it after an ordinary local change, and
do not treat implementation completion as human acceptance or baseline
authority.

## Required outcome

Leave the repository with:

- one routine design guide reachable from an existing agent, contributor, or
  documentation entrypoint;
- current production code and behavior-focused tests as the exact visual and
  interaction authority;
- a small set of stable product and design consequences that future work must
  preserve;
- direct mappings from surfaces and shared decisions to their canonical code
  and verification owners; and
- no competing active guidance that can silently revive superseded design.

Keep detailed approval identities, hashes, capture environments, and retirement
history in the repository's existing protected provenance record. The routine
guide should link to that record only when a future change needs it.

Prefer an existing guide and entrypoint. Do not create parallel guides for
different agents or tools. If no discoverable entrypoint exists and the user
specifically requested future-agent continuity, create one minimal
repository-native entrypoint that links to the guide instead of copying its
contents.

## Establish the current authority

Inspect the implemented product, project and agent instructions, product and
domain decisions, design-system sources, routes, components, styles, tests,
accepted references, prototypes, historical mocks, and design documentation.
Use version history when needed to distinguish current intent from residue.

Before declaring a no-op, inventory retained design files reachable from the
routine guide, agent or contributor entrypoint, provenance records, contract
manifests, source maps, validators, and repository search. Classify each as
routine authority, protected provenance, clearly archived/superseded history,
or unresolved. A current routine guide does not prove that retained contract or
machine-readable records are truthful.

Verify every retained artifact that still claims current, accepted, active, or
implementation-authoritative status against current code, tests, and acceptance
records. A disconnected historical artifact may keep old content only when its
archived status is unambiguous and no routine tool or validator presents it as
current.

Record status precisely: current implementation, selected direction, approved
reference, asserted golden, and human-accepted baseline are different states.
Do not upgrade one into another during handoff.

Extract only the decisions whose rationale or cross-surface consequence is not
obvious from code. The guide should tell a new agent where to look and what not
to shift; it should not recreate the design from prose.

## Minimum guide contents

Adapt the repository's existing format, but cover the applicable information:

1. **Authority order.** Put the current task and product/domain decisions
   before implementation details; make production code and tests authoritative
   for exact behavior and styling. Use accepted references only for intent that
   code does not make clear.
2. **Experience pattern.** State the small set of observable hierarchy,
   navigation, interaction, content, progress, recovery, or trust consequences
   that define the finalized design. Include the reason only when it prevents a
   plausible regression.
3. **Code ownership map.** Map each important surface or shared decision to
   stable relative paths, components, symbols, token sources, style entrypoints,
   and relevant tests. Avoid line numbers and copied implementation.
4. **Responsive and accessibility contract.** Name meaningful layout
   transitions, input/adaptation differences, content extremes, and the
   representative target matrix. Keep exact values in code unless the value is
   itself an intentional cross-surface decision.
5. **Granular change protocol.** Require an intended delta, must-preserve list,
   shared-impact check, smallest owner-local patch, representative unaffected
   surface, and baseline immutability. Route existing accepted surfaces to
   `product-design-change`; do not restart direction for a bounded fix.
6. **Verification.** Provide the smallest current commands and runtime states
   that prove visual, responsive, interaction, and accessibility preservation,
   with explicit evidence limits.
7. **Reference and legacy boundaries.** Identify protected references and their
   provenance, capture-only evidence, compatibility code that is not precedent,
   and superseded artifacts that must not return as design authority.
8. **Maintenance rule.** Update the guide only when an approved, implemented
   cross-surface decision changes a stable invariant, canonical owner, target
   matrix, or verification path. Ordinary local changes and routine UI details
   remain in code and tests.

Do not include a session transcript, exhaustive style inventory, copied CSS or
token values, rejected-direction gallery, speculative roadmap, duplicate
component documentation, or instructions to implement from prototype source.

## Reconcile stale guidance

When the finalization scope explicitly includes design-document cleanup, remove
or update obsolete agent-facing guides, intermediate implementation handoffs,
mocks, source maps, and references that compete with the current design. Do not
retain completed authorization language or machine-readable ownership entries
that no longer resolve to current consumers. Preserve required history,
licenses, rollback material, and accepted-reference provenance. An accepted
baseline or protected reference can be moved, removed, or relabelled only under
the same explicit acceptance or retirement authority required by accept-freeze.

If deletion is not authorized or provenance is still required, label the
artifact superseded and disconnect it from the routine agent path. Do not leave
two documents claiming to be current.

## Verify the handoff

- Resolve every local link and confirm each named source, source-map consumer,
  test, and command is current.
- Check that the routine agent path reaches one guide and no superseded guide.
- Check that prototypes, capture-only evidence, and compatibility styles are
  not described as production source.
- Treat a passing guide or link check as evidence, not as a substitute for the
  retained-artifact classification and source-consumer audit above.
- Run existing baseline-integrity checks without updating baselines.
- Add or update a lightweight repository-native guidance check when it provides
  durable protection without new infrastructure.
- Repeat the finalization inputs and confirm they produce no additional diff.

The final report names the guide and entrypoint, current code/test anchors,
stale artifacts removed or retained, validation performed, accepted-baseline
status, and any evidence limitation relevant to future changes.
