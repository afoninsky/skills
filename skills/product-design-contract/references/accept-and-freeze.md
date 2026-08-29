# Human acceptance and freeze protocol

Accept-freeze is the only operation in the suite that may change approved references or visual baselines. Gate D first disposes the reviewed candidate. Gate E then explicitly approves the exact named candidate and reviewed matrix as the new accepted identity. Accept-freeze records that Gate E decision; it does not manufacture or replace it.

## Qualifying instruction

A qualifying Gate E instruction follows Gate D, identifies the reviewed candidate and exact matrix, and intentionally authorizes its observed changes as the accepted identity. Examples:

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
2. Verify the Gate D disposition and separate Gate E approval ID name that identity and reviewed matrix.
3. Confirm the working tree/candidate has not changed since human review.
4. Inventory every proposed baseline/reference mutation.
5. Compare matched content, state, target, viewport/device, theme, locale, and crop.
6. Ensure asserted goldens name their real assertion source. A screenshot-writing call is not an assertion.
7. Show material visual, behavioral, accessibility, and target-coverage deltas.
8. Keep unavailable hard-gate evidence labeled `Not evidenced`; visual acceptance alone does not imply release readiness or Gate F.
9. Confirm no rejected or archived direction is being revived implicitly.

## Freeze transaction

Treat the update as one reviewable transaction:

- update only the approved golden/reference files;
- update baseline manifest identities and SHA-256 hashes;
- update contract manifest hashes only if the accepted contract itself changed;
- write the human approval record with candidate/ref, scope, accepted deltas, known limitations, and timestamp;
- update compact project state to the accepted ref and exact next action;
- run the bundled validator in `freeze` mode;
- review the final diff and report every baseline/reference path changed.

If validation fails or the candidate moves, stop. Do not leave manifests saying `accepted` while hashes or files disagree.

## Evidence language

Use “human accepted visual baseline” only for the exact named matrix. Keep separate statuses for accessibility, content truth, privacy/safety, runtime behavior, physical-device coverage, and representative-user evidence.
