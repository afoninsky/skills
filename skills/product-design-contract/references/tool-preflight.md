# Contract capability preflight

Use this reference when contract work depends on uncertain tooling. Ordinary contract editing needs only access to the existing design authority and a way to inspect the affected output.

## Select capabilities from the mode

- **Encode:** inspect the current design sources and write the authorized contract artifacts.
- **Re-architect:** trace every affected authority and deterministically compare outputs when the change claims no visual or behavioral delta.
- **Accept-freeze:** require versioned candidate identity, reviewed evidence, protected-file hashes, and the exact human approval.

Token compilation matters only when the repository already generates outputs or the requested contract genuinely needs multiple themes, platforms, aliases, or formats. Component workbenches, design editors, browser tests, native tests, and accessibility tools matter only for the states and claims they support.

## Check proportionally

1. Inspect existing token sources, generated outputs, build scripts, previews, tests, accepted references, and platform ownership.
2. Reuse the repository's canonical tools. Do not add Style Dictionary, Storybook, Penpot, or another named tool merely because it appears in examples.
3. Probe only selected capabilities with read-only version, list, validation, or representative render commands.
4. If a capability is missing, continue with contract work that does not depend on it and label unverified output or synchronization honestly.
5. Stop before a mutation when missing deterministic generation, runtime comparison, version identity, or approval would make that specific operation unsafe.

For projects already using the formal suite record, preserve the statuses `available`, `missing-blocking`, `missing-degradable`, `unknown`, and `not-applicable`. Do not introduce `design/toolchain.json` or refresh timestamps for an ordinary contract request.

## Setup and validation

When setup is necessary, prefer the project's package manager and current official documentation. State the dependency, files and generated outputs affected, migration and rollback, then obtain authorization before installing or connecting anything.

The bundled validator is required only when the project adopts its schema or performs formal accept-freeze:

```text
python3 <product-design-contract-skill-directory>/scripts/validate_design_contract.py --help
```

A validator pass proves structure and identity, not visual quality, accessibility, usability, or human acceptance.
