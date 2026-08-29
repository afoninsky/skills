# Disposable contract/change fixture

This fixture models one Vue web UI packaged by a Capacitor-style Android wrapper. It is generic and contains no TeachRelay source.

It is a structural validator fixture, not a runnable application or visual-acceptance fixture. `design/baselines/home-default.png` contains placeholder bytes and `tests/visual.spec.ts` records the intended check name but cannot run standalone. The contract validator proves schema, hashes, authority, and approval identity. The change guard proves declared scope and protected-path/hash behavior; it does not execute the manifest's Playwright or Maestro checks.

To reproduce the change-guard exercise in an isolated copy:

1. Initialize a Git repository in this directory, disable signing locally if required, commit all fixture files, and tag that commit `fixture-base`.
2. From this fixture directory, validate the accepted contract structurally:

   ```bash
   python3 /path/to/skills/skills/product-design-contract/scripts/validate_design_contract.py \
     --project-root . \
     --mode freeze \
     --contract-manifest design/contract/manifest.json \
     --source-map design/contract/source-map.json \
     --baseline-manifest design/baselines/manifest.json \
     --approval-id FREEZE-APPROVAL-PILOT
   ```

3. Change `src/Card.vue` padding from `var(--space-card-compact)` to `calc(var(--space-card-compact) + 4px)`.
4. Verify the declared change scope and protected hashes:

   ```bash
   python3 /path/to/skills/skills/product-design-change/scripts/change_guard.py verify \
     --project-root . \
     --manifest design/decisions/changes/CHG-001.json
   ```

5. Mutating `design/baselines/home-default.png` must make verification fail; restore the fixture bytes afterward.

The pilot's temporary nested Git metadata was removed after verification so this directory remains ordinary content in the parent skills repository.
