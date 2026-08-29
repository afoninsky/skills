# Tool substitution decision

## Identity

- Decision ID:
- Status: `keep | pilot | adopt | exception`
- Date:
- Owner/approval ID:
- Tool-selection baseline: `PD-TOOLS-2026-08-29`
- Capability and evidence role:
- Activated phase/platform/claim:

## Trigger

State the measured reason for reconsidering the current tool: deprecation, security, quota/cost, missing platform/capability, maintenance, or evidence-quality gap.

## Current tool and protected artifacts

- Current tool/version/access model:
- Canonical source and export format:
- Evidence and gates currently supported:
- Integrations and CI checks:
- Accepted baselines/identities that must not change during evaluation:

## Candidate

- Candidate/version/steward/license:
- Official documentation reviewed and date:
- Free-tier capacity for the whole maintained-project portfolio:
- Security, authentication, privacy, retention, and data-location notes:
- Export, migration, and exit path:
- Agent/MCP capability and why it adds non-replaceable value:

## Comparison

| Criterion | Current | Candidate | Evidence | Verdict |
|---|---|---|---|---|
| Sustainable capacity | | | | |
| Maturity and maintenance | | | | |
| Required functional/platform coverage | | | | |
| Deterministic evidence quality | | | | |
| Portability and exit | | | | |
| Security and privacy | | | | |
| Strong-model non-replaceability | | | | |
| Migration and rollback safety | | | | |

## Representative pilot

- Frozen input/ref/build:
- Matched target/state matrix:
- Current-tool artifacts:
- Candidate artifacts:
- Functional, visual, accessibility, and preservation results:
- Missing or non-equivalent evidence:
- Cost, latency, maintenance, and operator observations:

Do not update accepted baselines to make the candidate pass.

## Migration and rollback

- Files, dependencies, accounts, CI, or services changed:
- Conversion loss and mitigation:
- Dual-run period and success threshold:
- Rollback steps and verification:
- Old-tool removal condition:

## Decision

Record `keep`, `pilot`, `adopt`, or `exception`; the evidence supporting it; limitations; expiry/review trigger; exact owner approval; and the corresponding `design/toolchain.json` update. An MCP-only swap must confirm that canonical artifacts and authorization boundaries remain unchanged.
