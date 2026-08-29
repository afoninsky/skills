# Review evidence and findings

## Target-bound evidence

Every evidence item records:

- target state/build/deployment identity;
- observation time and environment;
- surface, state, content fixture, target/device/viewport, locale/theme, text/display scale, and relevant permissions;
- producer/tool and version;
- exact artifact, test, trace, or observation locator;
- coverage boundary and refresh trigger.

Evidence becomes stale when source/build, contract, baseline, state fixture, target runtime, or relevant tool version changes.

## Evidence labels

- **E0 — agent judgment:** generated analysis or visual critique.
- **E1 — specialist/heuristic review:** structured review by a relevant expert or tool.
- **E2 — deterministic artifact/runtime evidence:** tests, goldens, traces, semantics, and device output bound to the target.
- **E3 — internal human task evidence:** observed tasks by non-representative reviewers.
- **E4 — representative-user evidence:** appropriately recruited target users.
- **E5 — live product evidence:** consented, correctly interpreted production behavior/outcomes.

Higher labels do not automatically invalidate lower evidence, and quantity does not upgrade a label. Agent or synthetic-user review remains E0. Label each evidence item, then state the claim it can support.

## Screenshot taxonomy

**Asserted golden** requires all of:

1. named accepted reference identity;
2. deterministic state/configuration;
3. active comparison assertion in the executed path;
4. defined comparison method/tolerance;
5. failure/diff evidence;
6. human authority for baseline changes.

**Approved reference** has human authority and identity but may not run as a regression assertion.

**Capture-only** records a render without active comparison. It is useful evidence, but cannot fail when pixels drift.

**Unknown/stale** lacks producer, active execution, matched state, or current target identity.

Inspect code and execution. A snapshot directory, hash, filename containing “golden,” or committed PNG is insufficient.

## Quality lenses

Use these as professional heuristics, never automated acceptance:

- **First ten seconds:** can the intended user locate and understand the core act?
- **Silhouette:** are main regions, proportions, and reading path coherent before details?
- **Core act:** does visual weight serve the primary task rather than brand chrome?
- **Relabel:** would the interface still look specific if product names were replaced?
- **Default cluster:** does it collapse into common model defaults—generic cards, pills, gradients, centered heroes, excessive rounded containers?
- **Craft:** are spacing rhythm, typography, alignment, wrapping, control states, and transitions resolved?
- **Family/system:** do related surfaces/components share grammar unless a variant is explicitly justified?

Also challenge hostile content, localization, failure/recovery, reduced motion, and input/accessibility settings. Label agent judgment as heuristic.

## Finding contract

Each finding contains:

- stable ID and priority `P0`–`P3`;
- concise observed problem, not a solution title;
- user/product consequence;
- evidence locators and matched configuration;
- evidence label E0–E5;
- affected surfaces/states/targets and source-map dependents;
- contract rule/reference or `contract unavailable`;
- confidence separately from impact;
- evidence limitations and alternate explanations;
- smallest bounded change brief, including what must not change;
- verification matrix if the change is accepted.

Do not emit a finding solely because the reviewer prefers another aesthetic. Tie it to approved intent, task comprehension, system coherence, robust states, or established design/accessibility principles.

## Acceptance language

Say what was observed:

- “This Playwright test actively asserts the desktop default state; the mobile error image is capture-only.”
- “No automated accessibility findings were observed in these states; VoiceOver was not exercised.”
- “The candidate differs materially from the accepted reference in shell proportion; intent requires owner disposition.”

Avoid “accessible,” “compliant,” “usable,” “validated,” “pixel perfect,” “all platforms,” or “no regressions” unless the evidence scope genuinely supports the exact claim.

## Decision boundaries

- Gate D is the owner's accept/reject/revise disposition of the named reviewed candidate and representative matrix.
- Gate E is a later, separate router request for explicit approval of that exact identity as the accepted baseline; review does not perform it.
- Gate F is the owner's release/hold or research/learning decision from a review-owned evidence packet. Review does not execute the decision.

If the required matrix or claim evidence is incomplete, label it `Not evidenced` and block before the corresponding gate rather than implying “all platforms” or asking the owner to waive evidence.
