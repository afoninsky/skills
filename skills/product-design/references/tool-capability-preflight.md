# Tool capability preflight

Use this reference only when the requested result depends on a capability whose availability is uncertain, or when proposing to install, connect, or replace a tool. Do not preflight an irrelevant catalog.

## Capability-first rule

Start with the outcome and evidence:

1. Name the artifact, behavior, or conclusion to produce.
2. Identify the minimum capabilities it requires.
3. Inspect repository-native and already connected tools.
4. Probe only selected capabilities with harmless version, list, read, build, or smoke checks.
5. Continue, narrow the claim, request an input, or propose setup according to the actual consequence.

Prefer an established project tool when it produces equivalent results. An unavailable optional MCP, editor, hosting service, or preferred brand is not degradation when the underlying capability still exists.

## Missing capabilities

A gap blocks only the work or claim that depends on it.

- Missing runtime prevents verified visual or interaction conclusions, not source analysis.
- Missing deterministic comparison prevents a preservation claim, not all design judgment.
- Missing accessibility inspection prevents accessibility acceptance, not unrelated implementation checks.
- Missing representative participants prevents user-validation claims, not heuristic hypotheses.
- Missing physical-device evidence limits device-specific claims.
- Missing consent or provenance prevents use of sensitive product-behavior evidence.

Stop before mutation only when the missing capability makes that mutation unsafe, exceeds the requested evidence threshold, or prevents the explicit outcome. Otherwise complete the safe scope and state the limitation.

For an existing formal suite toolchain record, retain its statuses: `available`, `missing-blocking`, `missing-degradable`, `unknown`, and `not-applicable`. Do not create or update `design/toolchain.json` for routine work unless project protocol requires it and design-record writes are authorized.

## Setup or replacement

Before installing, connecting, or replacing anything:

- read [tool selection baseline](tool-selection-baseline.md);
- confirm no existing capability already solves the need;
- consult current official documentation for the actual OS, framework, package manager, and service;
- state files, dependencies, permissions, data exposure, ongoing cost, migration, rollback, and verification;
- obtain authorization for production dependencies, system tools, accounts, CI, external publication, participant operations, analytics, or spend;
- verify the smallest real use case after setup.

Keep secrets and sensitive data out of prompts, logs, screenshots, and Git. Request least privilege and prefer read-only probes.

## Durable evidence

MCPs and SaaS tools are adapters, not accepted state. Keep important source, exports, tokens, fixtures, tests, captures, decisions, and provenance in the repository or another user-approved durable system.
