# Audit Report Schema

Use this contract for `agent-work-audit.json`. The bundled renderer validates the record and produces a standalone HTML report. All strings are plain text; never place HTML or Markdown in a field.

## Contents

- [Top-level structure](#top-level-structure)
- [Audit metadata](#audit-metadata)
- [Verdict dimensions](#verdict-dimensions)
- [Executive summary](#executive-summary)
- [Preflight inputs](#preflight-inputs)
- [Requirement ledger](#requirement-ledger)
- [Claim ledger](#claim-ledger)
- [Verification checks](#verification-checks)
- [Findings](#findings)
- [Evidence register](#evidence-register)
- [Process, quality, and residual risk](#process-quality-and-residual-risk)
- [Recommendation and corrections](#recommendation-and-corrections)
- [Integrity rules](#integrity-rules)

## Top-level structure

```json
{
  "schemaVersion": "1.0",
  "audit": {},
  "verdicts": {},
  "summary": {},
  "inputs": [],
  "requirements": [],
  "claims": [],
  "checks": [],
  "processChecks": [],
  "findings": [],
  "evidence": [],
  "processSummary": "",
  "evidenceQuality": "",
  "residualRisks": [],
  "recommendation": {},
  "corrections": []
}
```

Do not supply derived totals or an overall verdict. The renderer calculates them so the headline cannot disagree with the underlying records.

## Audit metadata

```json
{
  "audit": {
    "id": "audit-2026-07-10-001",
    "title": "Agent Work Audit",
    "generatedAt": "2026-07-10T16:30:00+02:00",
    "generatorVersion": "1.0.0",
    "phase": "pre_delivery",
    "gateState": "blocked",
    "iteration": 1,
    "independence": "fresh_review",
    "confidence": "high",
    "risk": "medium",
    "humanConfirmation": "not_required",
    "subject": {
      "summary": "Checkout validation change",
      "claimedState": "HEAD abc123 plus diff sha256:...",
      "auditedState": "HEAD abc123 plus diff sha256:...",
      "targetEnvironment": "Local production build in Chromium"
    },
    "redactionStatus": "reviewed"
  }
}
```

Allowed values:

- `phase`: `pre_delivery`, `post_hoc`
- `gateState`: `ready`, `blocked`, `not_applicable`
- `independence`: `fresh_review`, `self_audit`
- `confidence`: `high`, `medium`, `low`
- `risk`: `low`, `medium`, `high`
- `humanConfirmation`: `not_required`, `obtained`, `unavailable`
- `redactionStatus`: `reviewed`, `redacted`, `not_reviewed`

Use `gateState: not_applicable` for post-hoc audits. `iteration` is a positive integer and increases after every remediation.

`claimedState` identifies what the implementer intended to hand off. `auditedState` identifies what the evidence actually observed. A mismatch must remain prominent and ordinarily blocks readiness.

## Verdict dimensions

```json
{
  "verdicts": {
    "outcome": "fail",
    "process": "pass_with_risks",
    "claims": "fail"
  }
}
```

Each dimension uses `pass`, `pass_with_risks`, `fail`, or `indeterminate`. The renderer derives overall severity in this order:

1. `fail`
2. `indeterminate`
3. `pass_with_risks`
4. `pass`

The renderer rejects inconsistent combinations such as a stop-ship finding with a passing overall result, `self_audit` with high confidence, or a material unavailable input with a passing result.

## Executive summary

```json
{
  "summary": {
    "text": "The primary workflow works, but rollback behavior was not available for verification.",
    "mainLimitation": "No staging access for the rollback path.",
    "decisiveEvidenceIds": ["E1", "E2"]
  }
}
```

Keep the summary concise. Every decisive evidence ID must exist in the evidence register.

## Preflight inputs

```json
{
  "inputs": [
    {
      "id": "I1",
      "name": "user_contract",
      "material": true,
      "status": "found",
      "location": "Current conversation",
      "why": "Defines required behavior"
    }
  ]
}
```

Final reports permit only `found`, `unavailable`, and `not_applicable`. Resolve `partial`, `stale`, `conflicting`, `untrusted`, and `requested` before report generation. A material unavailable input requires `fail` or `indeterminate` overall.

## Requirement ledger

```json
{
  "requirements": [
    {
      "id": "R1",
      "text": "Reject an expired checkout session",
      "priority": "critical",
      "status": "contradicted",
      "evidenceNeeded": "Expired-session response from the public API",
      "evidenceIds": ["E1"],
      "gap": "API returns 200 instead of 401"
    }
  ]
}
```

Allowed `priority`: `critical`, `non_critical`.

Allowed `status`: `satisfied`, `partial`, `missing`, `contradicted`, `uncheckable`.

## Claim ledger

```json
{
  "claims": [
    {
      "id": "C1",
      "text": "The expired-session case passes in the public API test.",
      "materiality": "material",
      "classification": "contradicted",
      "evidenceIds": ["E1"]
    }
  ]
}
```

Allowed `materiality`: `critical`, `material`, `minor`.

Allowed `classification`: `verified`, `contradicted`, `unsupported`, `uncheckable`.

Split claims by independently checkable proposition. Scope negative claims to the checks and surfaces actually observed.

Claim-verdict consistency is fail-closed:

- A critical or material contradicted claim requires `verdicts.claims: fail`.
- A critical or material uncheckable claim requires `verdicts.claims` to be `fail` or `indeterminate`.
- `verdicts.claims: pass` requires every critical and material claim to be verified.
- `verdicts.claims: pass_with_risks` permits only minor unsupported or uncheckable non-verified claims. Any contradicted claim or non-verified critical/material claim invalidates it.

## Verification checks

```json
{
  "checks": [
    {
      "id": "K1",
      "name": "Expired-session API check",
      "oracle": "The user contract requires HTTP 401",
      "oracleProvenance": "Requirement R1",
      "environment": "Local production build",
      "result": "failed",
      "requirementIds": ["R1"],
      "evidenceIds": ["E1"]
    }
  ],
  "processChecks": [
    {
      "id": "P1",
      "name": "Fresh test evidence",
      "status": "passed",
      "notes": "The command ran after the audited diff was created.",
      "evidenceIds": ["E1"]
    }
  ]
}
```

Allowed check `result`: `passed`, `failed`, `error`, `not_run`, `uncheckable`.

Every empirical check must reference at least one requirement. A check linked to a critical requirement is a critical acceptance check and directly constrains the outcome verdict.

Allowed process-check `status`: `passed`, `failed`, `warning`, `uncheckable`.

## Findings

```json
{
  "findings": [
    {
      "id": "F1",
      "severity": "critical",
      "stopShip": true,
      "iteration": 1,
      "status": "open",
      "resolvedInIteration": null,
      "title": "Expired sessions are accepted",
      "detail": "The public API returns a successful response for an expired session.",
      "consequence": "Unauthorized checkout state can continue.",
      "correctiveAction": "Reject expired sessions before processing checkout.",
      "evidenceIds": ["E1"]
    }
  ]
}
```

Allowed `severity`: `critical`, `high`, `medium`, `low`.

Allowed `status`: `open`, `resolved`, `accepted_risk`.

Use a stable ID, introduction iteration, resolution state, concrete consequence, causal correction, and evidence references. `resolvedInIteration` is required for resolved findings and must be later than `iteration`. A resolved finding must be referenced by a correction record. Stop-ship findings cannot be accepted as risk. Only current open findings constrain the current verdict, but resolved findings remain visible in history.

## Evidence register

```json
{
  "evidence": [
    {
      "id": "E1",
      "kind": "command",
      "label": "Expired-session regression test",
      "summary": "One targeted check failed.",
      "locator": "work/audit/test-output.txt",
      "observedAt": "2026-07-10T16:15:00+02:00",
      "stateId": "HEAD abc123 plus diff sha256:...",
      "environment": "Local production build",
      "sourceVersion": "pytest 9.0 / lockfile sha256:...",
      "coverage": "Expired session through public checkout API",
      "refreshTrigger": "Any code, dependency, configuration, or test change",
      "excerpt": "1 failed, 42 passed",
      "command": {
        "display": "pytest tests/test_checkout.py",
        "exitCode": 1
      },
      "sourceUrl": "https://example.com/authoritative-source"
    }
  ]
}
```

Allowed `kind`: `command`, `artifact`, `browser`, `source`, `observation`, `log`, `data`.

All evidence strings are bounded and escaped by the renderer. `sourceUrl` is optional and must be an explicit valid HTTPS URL. Never infer links from evidence text. Do not include credentials, tokens, personal data, or raw untrusted HTML.

Every evidence reference must resolve. State-dependent evidence must use the audited state ID and postdate its last relevant change. Use `coverage` to prevent bounded checks from supporting unrestricted claims.

All timestamps must be ISO-8601 values with an explicit timezone offset. Evidence cannot be observed after the report generation time.

## Process, quality, and residual risk

```json
{
  "processSummary": "The agent followed repository instructions but initially relied on a unit test instead of the public API.",
  "evidenceQuality": "The targeted test has a contract-derived oracle and demonstrated failure sensitivity. The staging rollback path was not observed.",
  "residualRisks": [
    {
      "id": "U1",
      "text": "Rollback behavior is unverified.",
      "reason": "Staging access was unavailable.",
      "resolution": "Run rollback rehearsal in staging.",
      "evidenceIds": []
    }
  ]
}
```

Residual risks remain visible even when non-blocking.

## Recommendation and corrections

```json
{
  "recommendation": {
    "decision": "correct",
    "summary": "Correct F1 and re-run K1 before handoff.",
    "items": ["Fix expired-session validation", "Re-run the public API check"]
  },
  "corrections": [
    {
      "iteration": 1,
      "priorState": "HEAD abc123 plus diff sha256:old",
      "newState": "HEAD abc123 plus diff sha256:new",
      "summary": "Added expired-session validation.",
      "findingIds": ["F1"],
      "evidenceIds": ["E2"]
    }
  ]
}
```

Allowed recommendation `decision`: `accept`, `correct`, `reverify`, `obtain_evidence`, `reject`.

Corrections are optional but required when a pre-delivery remediation occurred. Each correction creates a new state and therefore a new audit iteration.

## Integrity rules

The renderer fails without writing HTML when:

- Required fields or allowed values are invalid.
- IDs are duplicated or references dangle.
- A material input remains unresolved or is unavailable under a passing verdict.
- A critical or material contradicted claim is paired with a non-failing claim verdict.
- A critical or material uncheckable claim is paired with a passing claim verdict.
- A claim `pass` has a non-verified critical or material claim, or `pass_with_risks` has anything other than minor unsupported/uncheckable non-verified claims.
- An open stop-ship finding is paired with a non-failing overall verdict.
- A passing or ready report has no preflight inputs, requirements, claims, empirical checks, process checks, decisive evidence, or evidence register.
- A critical check fails, errors, is not run, or is uncheckable under an incompatible outcome verdict.
- A self-audit claims high confidence or overall pass.
- Overall pass is paired with anything other than high confidence.
- A ready verdict uses different claimed and audited state IDs, or current requirement, claim, check, open-finding, or decisive evidence is bound to another state.
- A low-confidence report attempts `pass` or `pass_with_risks`.
- A high-risk ready report lacks obtained human or authoritative confirmation.
- A failed, warning, or uncheckable process check is hidden under an incompatible process verdict.
- A medium- or high-severity finding is hidden under overall pass.
- A resolved finding lacks a correction record and new-state evidence.
- `generatorVersion` does not match the bundled renderer.
- The JSON exceeds the renderer's size limits or contains unsafe control characters beyond what can be normalized safely.

Fix the source record or the audit itself. Never weaken a verdict merely to satisfy validation.

The renderer's first viewport shows gate state and iteration, overall plus all three dimension verdicts, and claimed versus audited state. The bundled [post-hoc sample](../examples/post-hoc-audit.json) uses `gateState: not_applicable`.
