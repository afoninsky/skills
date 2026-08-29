# Release and compatibility policy

## Compatibility

- Target agents that support the public `SKILL.md` format and relative bundled resources.
- Require an installed and readable `grilling` or `grill-me` skill before Design Steward intake.
- Require Python 3.10 or newer for `scripts/validate_design_brief.py` and `scripts/generate_engagement_roadmap.py`; the written workflow and templates remain inspectable without Python.
- Keep the portable core independent of any design, research, analytics, repository, browser, or collaboration service.
- Treat named services as replaceable examples selected per approved engagement.

## Versioning

Use semantic versioning for published package releases:

- **Patch:** clarification, typo, equivalent template improvement, or validator fix that does not change accepted records or gate meaning.
- **Minor:** backward-compatible capability, optional record type, benchmark fixture, or additional service-neutral guidance.
- **Major:** changed Design Brief schema, authority boundary, evidence level, hard gate, record status, lifecycle gate, validator contract, or required migration.

Record the package version and immutable commit in every engagement header. Fingerprint the exact package before a benchmark or product pilot.

## Change control

Require every portable-core change to state:

- product-neutral problem and public evidence;
- affected contract, template, validator, or fixture;
- backward compatibility and migration effect;
- benchmark scenarios affected;
- hard-gate and authority-boundary review;
- verification performed.

Never promote an engagement-specific pattern, product term, artifact, metric, participant finding, or credential into the portable core. Abstract a reusable change and review it independently.

## Migration

- Preserve accepted engagement records under the package version that created them.
- For a pre-3.0 engagement, create and confirm a v3 Owner Design Brief, migrate `mode` to separate `operating_mode` and `engagement_type` fields, migrate `product_owner` authority fields to `system_owner`, preserve owner-original answers where available, and explicitly record uncertainty where they were not captured.
- For a pre-4.0 engagement, preserve accepted records, create `steward-state.json` from current authority, decisions, evidence, funnel, artifacts, coverage, and exact next action, record a verified grilling dependency, migrate the Design Brief to schema 4.0.0, run an impact review and validator, and obtain System Owner confirmation when any material decision or authority boundary cannot be recovered.
- Migrate by creating a new record version with explicit `supersedes` links; do not rewrite accepted evidence or decisions.
- Revalidate the Design Brief after any schema migration.
- Repeat affected gates when a new version changes authority, constraints, evidence interpretation, hard gates, comparison logic, or artifact semantics.
- Keep old benchmark fixtures addressable for regression comparison.

## Deprecation

Deprecate a field, status, or workflow for at least one minor release before removal unless continued use creates a safety, privacy, legal, or evidence-integrity risk. Document the safe replacement and migration check. Use a major release for removal.
