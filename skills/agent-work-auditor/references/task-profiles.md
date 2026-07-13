# Task Verification Profiles

Always apply the cross-cutting profile, then read only the task-specific sections relevant to the work being audited. These are prompts for risk-based verification, not exhaustive checklists.

## Always apply: provenance, safety, and cost

Verify:

- Every material evidence item is bound to the audited state ID, environment, observation time, source/version, and coverage boundary.
- State-dependent evidence postdates the last relevant change and the running target matches the claimed revision or artifact digest.
- Missing, partial, stale, conflicting, or untrusted inputs remain visible and cannot be promoted to `found` without resolution.
- Unfamiliar scripts and generated code are inspected before execution; verification defaults to sandboxed, read-only, no-network operation without production credentials.
- Production access, external writes, paid calls, sensitive-data transfer, and budget escalation have explicit authorization.
- Logs and report excerpts exclude secrets and unnecessary private or proprietary data.
- Targeted checks run before broad suites, fuzzing, or multiple reviewers, with stopping and escalation conditions recorded.

Challenge:

- Could the evidence come from a stale server, cached build, different deployment, or changed workspace?
- Could the verification itself alter external state, expose data, consume unexpected budget, or execute untrusted code?
- Does a broad negative claim exceed the observed surfaces and checks?
- Did a post-hoc rerun get used to “prove” a historical process claim that required contemporaneous logs?

## Coding and feature work

Verify:

- Each user-visible requirement through the public interface or normal execution path.
- Error paths, empty states, boundaries, invalid input, and important combinations.
- Compatibility with established APIs, schemas, and project conventions.
- Targeted tests plus the relevant broader regression suite.
- Build, type, lint, packaging, and migration checks when the change can affect them.
- No unrelated changes or generated-file churn.

Challenge:

- Could the implementation be hard-coded to the shown example?
- Do mocks duplicate the implementation instead of representing an independent dependency?
- Does the test assert behavior or merely that code executed?
- Could hidden state, ordering, locale, timezone, concurrency, or retries change the result?

## Debugging and root-cause claims

Require an observable reproduction. A plausible causal explanation is not proof.

Verify:

- The original failing behavior exists in the relevant baseline when reproducible.
- The proposed change removes that behavior under equivalent conditions.
- Reverting or disabling the relevant fix restores the failure in an isolated environment.
- The explanation matches execution traces, logs, bisect results, or other direct evidence.
- Nearby symptoms that share the suspected cause are covered.

Challenge:

- Was a fake or simplified environment constructed to produce the desired result?
- Did multiple changes occur between the working and failing states?
- Does the patch hide the symptom while preserving corrupted state or incorrect behavior?
- Is the alleged cause merely correlated with the failure?

## UI and browser work

Use the normal development or production-like stack and a real browser whenever possible.

Verify:

- The primary workflow at relevant desktop and mobile dimensions.
- Loading, empty, error, long-content, and keyboard states where applicable.
- No overlap, clipping, unexpected layout shift, inaccessible controls, or broken navigation.
- Browser console and network failures.
- The screenshot or video actually comes from the target application and test path.

Inspect both the artifact and the automation that produced it. A convincing video of a synthetic page is not evidence about the real application.

## Data analysis and benchmarks

Recompute decisive values independently when practical.

Verify:

- Units, bounds, denominators, joins, filters, missing values, duplicates, and sampling.
- Invariants such as percentages not exceeding meaningful limits unless definitions permit it.
- Conclusions against the complete relevant data, not only selected examples.
- Plots have meaningful axes, scales, labels, and denominators.
- Outliers and surprising results reproduce under controlled conditions.
- Compared runs use equivalent inputs, hardware, warm-up, seeds, deadlines, and stopping rules.
- Multiple runs reveal variation when the process is stochastic.

Challenge:

- Is the chosen metric only a proxy for the user's actual outcome?
- Would another reasonable task distribution reverse the conclusion?
- Are easy and impossible cases hiding the few cases that determine a summary score?
- Was an interpretation invented after seeing a favorable subset?

Report distributions and uncertainty rather than a single high-precision number when variance is material.

## Research and factual synthesis

Verify material claims against primary or authoritative sources.

Check:

- Each citation opens and supports the nearby claim.
- Dates, versions, prices, policies, and current officeholders are still current.
- Quotes are accurate, short, and not stripped of important context.
- Inferences are labeled separately from sourced facts.
- Conflicting credible sources are represented rather than silently resolved.
- The final recommendation follows the user's constraints rather than generic popularity.

Classify unsourced checkable claims as unsupported until verified. Do not call them false unless contradictory evidence exists.

## Documents, spreadsheets, presentations, PDFs, and images

Inspect both structure and rendered output.

Verify:

- Requested content, ordering, formatting, formulas, links, and metadata.
- Page, slide, sheet, and viewport rendering at the intended size.
- No clipping, overflow, unreadable text, broken references, or blank media.
- Formulas recalculate and totals reconcile with source data.
- Generated visuals show the requested subject and do not add unsupported factual details.
- Output filenames and formats match the user's delivery requirement.

Use the domain-specific artifact skill or renderer when available. A structurally valid file can still be unusable when rendered.

## Infrastructure, security, privacy, and destructive operations

Treat these as high risk unless the context clearly proves otherwise.

Require:

- Least-privilege review and explicit identification of secrets and data exposure paths.
- Dry-run or isolated-environment evidence before destructive execution.
- Rollback or recovery validation.
- Failure-mode checks for partial completion, retries, and concurrent execution.
- Authoritative documentation for security-sensitive configuration.
- Human approval for consequential external actions that cannot be safely reversed.

Passing a happy-path test is not enough for a high-risk verdict.
