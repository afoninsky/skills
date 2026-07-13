---
name: agent-work-auditor
# Trigger mode: MANUAL. To restore automatic audits, comment out the active
# description below and uncomment every line in the AUTOMATIC MODE block.
# Keep exactly one description active.
description: Evidence-first audit of completed agent work for requirement fidelity, hallucinated or unsupported claims, test validity, regressions, process quality, and delivery readiness. Use only when the user explicitly invokes `$agent-work-auditor`, names the Agent Work Auditor skill, or directly asks to run this skill. Do not invoke it automatically when another task finishes or before a handoff, commit, PR, publish, deploy, or completion claim. When invoked, bind evidence to the exact target state and claims, request missing material evidence, and produce validated JSON plus standalone HTML.
# AUTOMATIC MODE (disabled)
# description: >-
#   Final evidence-first audit for completed agent work. Invoke automatically
#   before final handoff, commit, PR, publish, deploy, or a completion claim when
#   an agent materially changed a deliverable or external state and work affects
#   user-visible or shared behavior, spans components or agents, makes material
#   causal, numerical, source, integration, or environment claims, or carries
#   meaningful regression, security, privacy, financial, destructive, or
#   operational risk. Also invoke when the user asks to audit or verify agent
#   compliance, claims, tests, hallucinations, root cause, regressions, or
#   readiness. Run after artifact, review, and verification skills; audit
#   integrated subagent output once; never recursively audit the audit. Skip
#   simple Q&A, unexecuted planning, ordinary review of pre-existing work, status
#   checks, lookups, and tiny low-risk read-only, cosmetic, or metadata changes.
#   Bind evidence to exact target state and claims, request missing material
#   evidence, and produce validated JSON plus standalone HTML.
# END AUTOMATIC MODE
compatibility: Requires Python 3.10+ for the bundled standalone HTML report generator. Verification tools otherwise depend on the audited task.
license: MIT
---

# Agent Work Auditor

## Purpose

Treat completed agent work as an untrusted hypothesis until observable evidence supports it. Plausible explanations, self-written tests, screenshots, videos, and confident completion summaries can all be wrong while looking convincing.

Audit the work using evidence that does not merely repeat the implementation's assumptions. Prefer execution, inspection, and externally observable behavior over another round of reasoning about whether the work ought to be correct.

Operate as an auditor rather than another source of plausible explanations:

- Preserve findings before any correction so the audit trail remains visible.
- Do not accept the implementing agent's narrative or test suite as sufficient proof.
- Do not turn missing evidence into assumptions.
- Do not reduce a multidimensional result to one quality score.
- Never recursively invoke this skill to audit its own generated audit report.

In an automatic pre-delivery gate, the auditor stays read-only but may hand fixable findings back to the implementing role within the user's already-authorized scope; re-audit every corrected state. In a post-hoc or explicit audit-only review, do not modify the subject unless the user asks. Temporary verification artifacts are allowed only when isolated from the user's work.

## Required audit inputs

First choose the audit mode:

- **Pre-delivery gate:** the implementing agent has finished a qualifying task but has not sent its final response. Require a draft claims manifest containing every completion, verification, causal, numerical, scope, and negative claim it intends to make. A completed gate report records `audit.gateState` as `ready` or `blocked`; remediation is a lifecycle action while the gate remains blocked.
- **Post-hoc audit:** a completed response or handoff already exists. Audit its claims directly, record `audit.gateState` as `not_applicable`, and remain audit-only unless the user authorizes remediation.

Record independence separately from mode:

- `fresh_review`: a reviewer context that did not implement the audited state.
- `self_audit`: the implementing context performs the audit. Shared assumptions lower confidence.

Collect enough information to determine both what was requested and what actually happened:

1. The original user request and all later clarifications or corrections.
2. The resulting code changes, files, generated artifacts, or other work product.
3. The available action transcript, contemporaneous tool and command history, implementing agent's final response or draft claims manifest, and other material factual or completion claims.
4. The intended runtime or review environment and any relevant project instructions.
5. Existing acceptance criteria, test commands, logs, screenshots, videos, source citations, or other verification records.
6. An exact target-state identity: commit plus dirty-diff digest, artifact digest, dependency/configuration version, deployed revision, or another reproducible fingerprint appropriate to the subject.
7. The audit budget and whether evidence has been reviewed for secrets or private data before reporting.

First discover these inputs from the current conversation, workspace, version-control history, project instructions, and available tool output. Do not ask the user to repeat information that is already available.

### Missing evidence gate

Create a preflight table before auditing:

| Input | Material | Status | Location or request | Why it matters |
|---|---|---|---|---|
| User contract | yes/no | found/partial/stale/conflicting/untrusted/requested/unavailable/not applicable | Conversation, path, or question | Requirement fidelity |
| Work product | yes/no | found/partial/stale/conflicting/untrusted/requested/unavailable/not applicable | Diff, files, or artifact | Actual outcome |
| Process and claims record | yes/no | found/partial/stale/conflicting/untrusted/requested/unavailable/not applicable | Transcript, response, or manifest | Process and claim integrity |
| Target state and environment | yes/no | found/partial/stale/conflicting/untrusted/requested/unavailable/not applicable | Fingerprint, project docs, or user answer | Correct target and reproduction |
| Verification evidence | yes/no | found/partial/stale/conflicting/untrusted/requested/unavailable/not applicable | Commands or artifacts | Completion proof |

Treat `partial`, `stale`, `conflicting`, and `untrusted` as unresolved, not as found. Justify every `not applicable` classification.

If a material input cannot be found, pause the affected part of the audit and request it from the user. Ask only for the missing information that could change the verdict, state why it is needed, and prefer one concise request containing no more than three questions. Use another concise round when more material gaps remain; do not silently omit them.

Examples:

- Ask for the original request when only a final implementation is available.
- Ask for the changed files, repository, or artifact when only a completion summary is available.
- Ask for the available transcript, command history, or handoff when the user wants the work process evaluated but only the artifact is available.
- Ask how the software is normally run when the target environment cannot be inferred safely.
- Ask for access or a user-provided reproduction when correctness depends on a private service or physical observation.
- Ask which outcome is authoritative when later instructions conflict.

Never invent the missing information or quietly narrow the requirement. Do not issue a final verdict while a material request is unanswered; user silence is not confirmation that evidence is unavailable. If the user explicitly says material evidence cannot be provided, classify it `unavailable`, complete only the checks that remain valid, and return `INDETERMINATE` unless a separate proven defect already requires `FAIL`. List exactly what could not be established and what evidence would resolve it. A non-material omission may permit `PASS WITH RISKS` when every critical requirement and material claim has target-bound support.

## Audit workflow

### 1. Freeze the work and classify risk

Record the exact claimed state and audit state before running checks. Include relevant files, version-control status and diff, generated artifacts, dependency/configuration versions, deployed revision, and available verification evidence. Use a reproducible state ID such as `HEAD + dirty diff hash`, artifact digests, or an external revision identifier.

Bind every evidence item to the state ID and environment it observed. Prove that a running server, browser, deployment, dataset, or generated artifact corresponds to that state rather than a stale build or cache. If the relevant state changes, invalidate affected evidence and restart from this step. In a post-hoc audit, current behavior cannot prove a historical delivered state when that state is unavailable.

Choose a risk level that controls verification depth:

- **Low:** reversible, local, narrow impact.
- **Medium:** shared behavior, user-visible workflow, migration, integration, or meaningful regression risk.
- **High:** security, privacy, money, destructive operations, production data, legal or medical implications, or difficult rollback.

Set a proportional audit budget for wall time, compute, tokens, paid calls, traffic, and data volume:

- **Low:** contract and claims trace, fresh targeted checks, and a scoped adversarial pass.
- **Medium:** low-risk checks plus relevant broader regression or rendered-artifact verification and a fresh reviewer when available.
- **High:** medium-risk checks plus failure/rollback paths, a fresh reviewer, and human or authoritative external confirmation for consequential behavior.

Stage targeted checks before broad suites or fuzzing. Define stopping and escalation conditions. Ask before paid calls, production access, external writes, sensitive-data transfer, or exceeding the agreed budget. A budget-skipped material check makes the verdict `INDETERMINATE`; disclose non-material skipped checks as residual risk.

### 1a. Safe-execution gate

Verification can itself cause harm. Before executing unfamiliar scripts or generated code, inspect what will run and prefer sandboxed, read-only, no-network execution without production credentials. Obtain approval before production access, external side effects, privileged operations, or transmitting proprietary material to another service or reviewer.

Never include secret values or unnecessary private data in commands, logs, JSON, or HTML. Redact evidence, bound excerpts, use restricted temporary-file permissions when relevant, and remove temporary sensitive material when the audit is complete.

### 2. Reconstruct the user contract

Translate the conversation into atomic requirements. Include:

- Explicit requested behavior and deliverables.
- Later corrections, priorities, and exclusions.
- Relevant project conventions and compatibility constraints.
- User-visible success conditions.
- Important implied behavior only when the repository or task context supports it.

Mark each requirement as `critical` or `non-critical`. User-stated musts, requested deliverables, acceptance criteria, and safety, privacy, money, data-loss, and irreversible-operation constraints default to critical unless the user explicitly says otherwise. Do not allow many minor successes to average away a missing critical requirement.

Build a requirement ledger:

| Requirement | Priority | Evidence needed | Status | Evidence or gap |
|---|---|---|---|---|
| Concrete requested outcome | critical/non-critical | Observable proof | satisfied/partial/missing/contradicted/uncheckable | Path, command output, artifact, or explanation |

If intent remains materially ambiguous after reading all available context, invoke the missing evidence gate.

### 3. Build a claim ledger

Extract objective claims from the final response, comments, documentation, and verification summary. Include claims such as:

- A feature was implemented or a bug was fixed.
- Tests, builds, linters, migrations, or benchmarks passed.
- A real environment or integration was exercised.
- No regressions or unrelated changes were introduced.
- A particular cause explains an observed failure.
- Numerical, performance, factual, or source-based statements are correct.

Split claims into atomic, independently checkable propositions and classify each:

- `verified`: fresh, relevant evidence directly supports it.
- `contradicted`: evidence directly conflicts with it.
- `unsupported`: checkable, but adequate evidence was not produced or found.
- `uncheckable`: necessary access or observation is unavailable.

Mark materiality as `critical`, `material`, or `minor`. A claim is material when falsity could change acceptance, remediation, risk, or the user's decision. Unsupported is not automatically false, and uncheckable is not automatically unsupported.

Rewrite universal negatives to the scope evidence can support. Prefer “no regressions observed in checks X across surfaces Y at state Z” over “no regressions,” and “no unrelated tracked changes relative to baseline Z” over an unrestricted claim. Leave a broader negative unsupported unless exhaustive proof genuinely exists.

Each evidence item must record `observedAt`, `stateId`, `environment`, `sourceVersion`, `coverage`, and `refreshTrigger` in addition to its identity, kind, label, summary, locator, and excerpt. State-dependent evidence must postdate the last relevant state change. Historical process claims require contemporaneous logs; rerunning now only establishes current behavior. Volatile facts require an explicit “as of” time and current authoritative source.

### 4. Inspect the work product

Read the actual changes and artifacts. Check for:

- Missing or only partially implemented requirements.
- Hard-coded examples, fake fixtures, or behavior that only satisfies the demonstrated case.
- Scope drift, accidental requirements, unrelated changes, or ignored exclusions.
- Unnecessary complexity and duplicated or dead logic.
- Violations of established project patterns or ownership boundaries.
- A patch to the visible symptom that leaves the systemic cause intact.
- Documentation or final prose that overstates what the implementation does.

Code inspection identifies hypotheses and risk areas. It does not replace behavioral verification.

### 5. Audit process integrity

Use the available transcript and command history to evaluate how the result was produced. Check whether the agent:

- Read the relevant instructions and existing implementation before changing it.
- Preserved user scope, exclusions, and unrelated work.
- Used the real target where it claimed to do so.
- Ran the commands it later claimed passed and read their complete results.
- Responded honestly to failures, access limits, and missing evidence.
- Avoided destructive actions, fabricated artifacts, and unexplained substitutions.
- Investigated the underlying cause instead of repeatedly masking visible symptoms.

Separate process quality from outcome quality. A sound outcome can come from a weak process, and a careful process can still produce a failed outcome. If the process record is unavailable, invoke the missing evidence gate before making claims about how the agent worked.

### 6. Design evidence-backed acceptance checks

Derive checks from the user contract before relying on the implementing agent's tests. Favor the intended external behavior and real execution path.

For every critical check, name an oracle and its provenance. Valid oracles include the user specification, an authoritative example, a separately implemented reference, a domain invariant, a differential comparison with a trusted system, or direct human observation. Do not calculate an expected answer with the implementation under test and then use that answer to validate the same implementation. If no trustworthy oracle is available, request one or classify the requirement as uncheckable.

- For a bug fix, reproduce the original symptom and show that the changed implementation removes it.
- For a feature, exercise the primary workflow and each critical constraint.
- For UI behavior, run the normal application stack in a real browser. Inspect both the visual artifact and the code or test that produced it.
- For an integration, use the most production-like environment available. State clearly when mocks or substitutes were necessary.
- For performance work, compare equivalent conditions, inspect outliers, and report distributions rather than one favorable run.
- For data analysis, verify units, denominators, joins, bounds, missing data, sample selection, and whether the conclusion follows from the complete dataset.
- For research, open the cited primary sources and verify that each material claim is actually supported.
- For documents, spreadsheets, presentations, PDFs, images, or other artifacts, inspect the rendered result as well as its source structure.

Read [references/task-profiles.md](references/task-profiles.md) for the relevant task type before designing checks.

### 7. Execute fresh verification

Run the full approved and budgeted commands now and record their exit status, state ID, environment, observation time, coverage boundary, and important output. Do not cite a previous agent's statement that a command passed as fresh evidence.

Use an appropriate combination of:

- Targeted acceptance or regression tests.
- The project's broader regression suite.
- Build, type, lint, migration, or schema checks.
- Browser or end-to-end interaction in the intended stack.
- Property-based, randomized, fuzz, or cross-product testing for risky input spaces.
- Independent source or data calculations.

Save random seeds and minimized failures so discovered cases can become regression tests. Scale the effort to risk and avoid claiming exhaustive coverage.

For randomized or fuzz checks, record the dimensions varied, important combinations covered, generator constraints, seed, and stopping condition. A large input count does not compensate for a generator that omits the relevant combinations.

### 8. Challenge the tests and artifacts

Determine whether the evidence could pass while the requested behavior is still broken.

Inspect tests for meaningful inputs, observable assertions, negative cases, and coverage of the actual requirement. Watch for tautological assertions, mocks that implement the desired answer, snapshots that were blindly updated, swallowed errors, skipped tests, and tests that never reach the claimed path.

When safe and useful, perform a red-green or mutation check in an isolated temporary copy or disposable worktree:

1. Confirm the check passes with the proposed implementation.
2. Remove or perturb the relevant behavior.
3. Confirm the check fails for the expected reason.
4. Restore the isolated copy and confirm it passes again.

Never perform this experiment destructively in the user's working tree. If test sensitivity cannot be demonstrated, report that limitation.

For screenshots, videos, benchmark charts, and generated reports, inspect both the artifact and its producer independently. Confirm that the producer exercises the real target rather than a fabricated or simplified environment.

### 9. Run an adversarial pass

Ask: "How could every current check pass while the user's actual objective remains unmet?"

Probe the most plausible alternatives rather than generating a long generic checklist. Look for proxy metrics, narrow samples, hidden state, different user behavior, recovery paths, boundary combinations, and implementation-specific tests.

For medium- and high-risk work, use a fresh reviewer context or independent subagents when available and permitted. Use separate perspectives for:

- Requirement fidelity and scope.
- Empirical reproduction and evidence integrity.
- Contrarian failure analysis.

Have them inspect evidence independently before reconvening. Consensus without fresh execution is still weak evidence, so forced checking remains primary. For subjective quality or inaccessible external behavior, request human observation instead of manufacturing certainty.

If the implementing agent must audit its own work in the same context, label the result `self_audit`, never describe it as independent, cap confidence at `medium`, and cap the overall verdict at `PASS WITH RISKS`. High-risk work cannot pass on self-audit alone; obtain human or authoritative external confirmation or return `INDETERMINATE`.

### 10. Determine claim integrity

Split claims atomically by independently checkable proposition. Do not inflate the denominator with stylistic statements, repeated claims, or minor paraphrases.

Report raw counts before any ratios:

- Verified claims.
- Contradicted claims.
- Unsupported claims.
- Uncheckable claims.

When useful, calculate:

- **Contradicted-claim share:** contradicted checkable claims / all checkable claims.
- **Unsupported-claim share:** unsupported claims / all claims.
- **Uncheckable-claim share:** uncheckable claims / all claims.

Headline the critical and material counts; do not let numerous minor claims dilute them. Never label unsupported or uncheckable claims as confirmed hallucinations. These ratios describe only the claims extracted from this audit; they do not estimate hidden hallucination frequency and must not be used to compare agents or audits with different claim segmentation. Avoid false precision when there are few claims or subjective classifications.

Freeze the audited claims manifest after classification. Before handoff, compare the proposed final response against it. Verify or remove every new material claim; any new completion, causal, numerical, environment, or broad negative claim invalidates claim-integrity evidence until audited.

### 11. Assign verdicts

Assign separate verdicts for the outcome, process, and claim integrity, then derive the overall verdict. Use the same four labels for each dimension.

For the **outcome verdict**:

- `FAIL`: use when evidence proves that a critical requirement or deliverable is absent, partial, or contradicted, important behavior fails, or the change creates a stop-ship regression.
- `INDETERMINATE`: use when no failure is proved but critical correctness or a material outcome claim depends on evidence the user explicitly said is unavailable or on unresolved ambiguity. State what must be supplied or observed.
- `PASS WITH RISKS`: use only when every critical requirement and material outcome claim is verified, no critical or material claim is contradicted, and remaining outcome gaps are non-critical and non-blocking.
- `PASS`: use only when every critical requirement and every critical or material outcome claim has trustworthy support, meaningful verification passes, and no nontrivial outcome evidence gap remains.

For the **process-integrity verdict**:

- `FAIL`: use for fabricated evidence, concealed command failures, unauthorized or destructive actions, or a severe violation of a critical user instruction.
- `INDETERMINATE`: use when material process history is unavailable and the user explicitly says it cannot be provided.
- `PASS WITH RISKS`: use for material but non-severe process defects such as incomplete command capture, weak environment fidelity, avoidable scope drift, or unreliable handling that did not invalidate the result.
- `PASS`: use only when the available record supports the material process claims and no material process defect remains.

For the **claim-integrity verdict**:

- `FAIL`: use when a critical or material claim is contradicted or fabricated, regardless of whether intent can be proved.
- `INDETERMINATE`: use when no contradiction requires `FAIL`, but a critical or material claim is unsupported or uncheckable because required evidence is unavailable. A critical or material uncheckable claim permits only `FAIL` or `INDETERMINATE`.
- `PASS WITH RISKS`: use only when all critical and material claims are verified and every remaining non-verified claim is a minor unsupported or uncheckable claim. A contradicted claim is incompatible with this verdict.
- `PASS`: use only when every critical and material claim is verified and no nontrivial claim-evidence gap remains.

Derive the **overall verdict** from the most severe dimension, using this precedence: `FAIL`, then `INDETERMINATE`, then `PASS WITH RISKS`, then `PASS`. A proven defect is `FAIL`; inability to observe a required dimension is `INDETERMINATE`. Reserve overall `PASS` for three passing dimensions, `fresh_review`, high confidence, complete material process coverage, and no unresolved material evidence gap.

Confidence describes certainty in the verdict, not the probability that the work is correct:

- `high`: critical oracles are trustworthy, evidence is fresh and target-bound, the intended environment was exercised, material process history is complete, and a fresh reviewer or authoritative human/external confirmation supports the result.
- `medium`: evidence is sufficient for the stated bounded verdict, but self-audit, production-like substitutes, or limited non-critical coverage remain.
- `low`: the verdict relies mainly on static inspection, mocks, stale evidence, or substantial inaccessible context. A low-confidence audit cannot produce `PASS` or `PASS WITH RISKS`; absent a proven failure, use `INDETERMINATE`.

Do not issue `PASS` solely because existing tests pass. Do not issue `FAIL` solely because evidence is absent; distinguish failure from inability to verify.

## Correction and re-audit lifecycle

For an automatic pre-delivery gate:

1. Preserve the claims manifest, state ID, evidence, verdict, and findings for the current iteration. Give every finding an introduction iteration and status: `open`, `resolved`, or `accepted_risk`.
2. A `FAIL` or `INDETERMINATE` sets `audit.gateState` to `blocked`; do not claim completion, commit, publish, deploy, or hand off.
3. Fixable findings within the user's authorized implementation scope may enter remediation while the gate remains `blocked`. Keep the auditor read-only and hand findings to the implementing role.
4. After any correction, compute a new state ID, rerun fresh verification, and perform a new audit iteration. Mark a finding `resolved` only when a correction record and new-state evidence prove it; old evidence does not transfer unless it is demonstrably state-independent. Never mark a stop-ship finding `accepted_risk`.
5. Run at most two automatic remediation cycles by default. Stop earlier for repeated failures, missing user input, permissions, external side effects, or budget escalation; present the blocked report and request a decision.
6. `PASS WITH RISKS` may set `audit.gateState` to `ready` only when every remaining risk is explicitly non-blocking. `PASS` sets it to `ready`.
7. Immediately before the final response, recheck the state ID and claims manifest. Any relevant mutation or new material claim invalidates `ready` and requires another audit.

Record every remediation iteration in the final report. Post-hoc audits remain read-only until the user authorizes a separate correction cycle.

## Structured report artifacts

Produce two user-facing artifacts for every completed audit when the filesystem is available:

1. `agent-work-audit.json`: the validated source record.
2. `agent-work-audit.html`: a standalone, offline, accessible report generated from that JSON.

Read [references/report-schema.md](references/report-schema.md) before writing the JSON. Use stable IDs and evidence references instead of duplicating untraceable prose. Record audit phase and reviewer independence as separate fields. Require `audit.gateState` and a positive `audit.iteration`. Describe `audit.subject` with separate required `summary`, `claimedState`, `auditedState`, and `targetEnvironment` fields; never collapse claimed and audited state into an ambiguous snapshot. Include generated time, redaction status, preflight inputs, the required outcome, process, and claims verdicts, requirements, claims, checks, process checks, findings, corrections, evidence, residual risks, and recommendation.

Before writing the source JSON, remove secrets and unnecessary private data. Use bounded plain-text evidence excerpts and set redaction status honestly. Never place raw HTML or Markdown in the data.

Generate the report with the bundled fail-closed renderer:

```bash
python3 <skill-directory>/scripts/generate_report.py \
  --input <output-directory>/agent-work-audit.json \
  --output <output-directory>/agent-work-audit.html
```

The renderer derives the overall verdict from outcome, process, and claims; it also derives counts, ratios, and the stop-ship total and rejects inconsistent or unsafe input. The HTML must show the overall and all three dimension verdicts, claimed versus audited state, and gate iteration/state prominently. If validation fails, correct the JSON; do not handwrite substitute HTML or weaken the verdict to make generation pass.

Open the generated HTML with the available browser or renderer and inspect its first viewport, critical findings, evidence references, narrow-screen layout, and print behavior. If visual inspection is impossible, validate the file structurally and disclose that limitation.

In the final response, state the overall verdict and highest-priority next action in one short paragraph, then link the HTML report and JSON evidence record. If the environment cannot create files, provide the same structure inline and state why HTML was not generated.

## Evidence hierarchy

Prefer evidence in roughly this order:

1. Reproduction of the requested behavior in the intended external environment.
2. Independent acceptance checks derived from the user contract.
3. Meaningful project tests with demonstrated sensitivity to the target failure.
4. Direct inspection of code, data, artifacts, and authoritative sources.
5. Implementing-agent-authored tests and generated artifacts that were independently inspected.
6. Agent explanations, confidence, or repeated agreement without execution.

Lower-ranked evidence can identify where to investigate but should not overrule contradictory higher-ranked evidence.

## Background and intended use

This skill was created from the testing and agent-workflow lessons described in Dan Luu's article, ["Agentic test processes, LLM benchmarks, and other notes on agentic coding from Galapagos Island"](https://danluu.com/ai-coding/). It turns those lessons into a reusable completion audit; the article is the conceptual source, not an endorsement of this implementation.

- **What it does:** independently checks completed agent work, its material claims, and its delivery readiness against the user's actual requirements.
- **How it works:** freezes the exact target state, reconstructs requirement and claim ledgers, prefers empirical checks over agent explanations, challenges tests and generated artifacts, uses independent or adversarial perspectives where risk warrants them, and emits validated JSON plus standalone HTML.
- **When to use it:** invoke it explicitly after material agent work when incorrect completion claims, synthetic evidence, regressions, security or privacy impact, costly mistakes, or a wrong-target verification would affect acceptance. Do not use it as a substitute for implementation tests or for routine low-risk work.

The durable principles are empirical verification over plausible reasoning, independent perspectives for false-positive reduction, randomized testing where input spaces are large, systematic fixes over symptom patches, task-relevant evaluation rather than proxy metrics, and explicit uncertainty when outside feedback is still required.
