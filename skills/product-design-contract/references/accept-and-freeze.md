# Human acceptance and freeze protocol

Accept-freeze is the only operation in the suite that may change approved references or visual baselines. It records a human decision that explicitly approves an exact reviewed candidate and covered conditions as the new accepted identity; it does not manufacture or infer that decision.

## Qualifying instruction

A qualifying instruction identifies the reviewed candidate and covered matrix or conditions, and intentionally authorizes its observed changes as the accepted identity. It may follow an earlier review decision or state both candidate disposition and baseline authorization clearly in one instruction. Examples:

- “I reviewed candidate CHG-014 at commit `<ref>` and accept these diffs; freeze it.”
- “Direction B, build 37, is approved as the new phone and tablet baseline.”

These do not qualify:

- “Update snapshots.”
- “Make CI green.”
- “Looks good” when several candidates or unresolved diffs exist.
- an agent, automated grader, generated persona, or synthetic user recommending acceptance.

If identity or scope is ambiguous, stop and ask one precise confirmation question. Preserve the candidate unchanged while waiting.

## Pre-freeze checklist

1. Resolve the reviewed candidate to an immutable Git ref or content hashes.
2. Verify the review evidence and human approval identity name that candidate and covered matrix. The approval may come from one clear combined instruction or separate recorded decisions.
3. Confirm the working tree/candidate has not changed since human review.
4. Inventory every proposed baseline/reference mutation.
5. Compare matched content, state, target, viewport/device, theme, locale, and crop.
6. Ensure asserted goldens name their real assertion source. A screenshot-writing call is not an assertion.
7. Show material visual, behavioral, accessibility, and target-coverage deltas.
8. Keep unavailable evidence explicit; visual acceptance alone does not imply accessibility, usability, safety, or release readiness.
9. Confirm no rejected or archived direction is being revived implicitly.

## Freeze transaction

Treat the update as one reviewable transaction:

- update only the approved golden/reference files;
- update the repository's existing baseline manifest or integrity record when it has one;
- record the human approval identity, candidate/ref, scope, accepted deltas, and known limitations in the repository's established acceptance record, or a minimal adjacent record when no convention exists;
- run the repository's native golden, snapshot, or baseline-integrity checks;
- review the final diff and report every baseline/reference path changed.

When the project already uses the suite's formal contract schema, also update its SHA-256 identities, approval record, and compact project state, then run the bundled validator in `freeze` mode with the exact approval ID. These formal-schema writes are part of the disclosed acceptance metadata; do not introduce them into an ordinary repository merely to use this suite.

If validation fails or the candidate moves, stop. Do not leave manifests saying `accepted` while hashes or files disagree.

## Evidence language

Use “human accepted visual baseline” only for the exact named matrix. Keep separate statuses for accessibility, content truth, privacy/safety, runtime behavior, physical-device coverage, and representative-user evidence.
