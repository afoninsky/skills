# Source-scoped UI heuristic audit

## Classification and disposition

- Evidence class: **E1 specialist/heuristic input**.
- Disposition: findings require entry into the implementation contract and delta log by the Steward, followed by rerunning affected checks after remediation. Those artifacts were not in the authorized scope, so no disposition was written here.
- This audit is **not** representative-user validation, accessibility certification, runtime or browser assurance, engineering approval, legal or regulatory compliance, or ship approval.
- A clean static audit would mean only that no finding was produced within the recorded source scope and method. This audit is not clean.

## Specialist preflight

| Item | Record |
|---|---|
| Skill | `web-design-guidelines` |
| Availability | Available; repository-local skill read in full |
| Skill version | `1.0.0` |
| Skill SHA-256 | `f4647ca866a3accf763777f83e7682954f0187cd6bea7eea0399796652414e8f` |
| Steward wrapper | `skills/design-steward/references/specialist-capabilities.md`, read in full; SHA-256 `a6c8beacded209d401c85dd14ca90c07b9826c6034ffd81f2c29d75ad3b388d9` |
| Authorized inspection scope | `skills/design-steward/evals/files/ui-audit-fixture.html` only |
| Fixture/content SHA-256 | `ac11654bba5549ca8e0217e8a92a90b05294d512cd9693fe9042341e1ad69890` |
| Allowed tools | Read-only local file inspection; network retrieval limited to the canonical Vercel guideline repository/source; SHA-256 calculation; `apply_patch` for the report |
| Network access used | GitHub API to resolve the repository's current `main` commit; `raw.githubusercontent.com` to retrieve `command.md` at that immutable commit |
| Exact write scope | This report only: `benchmarks/design-steward-specialists/2026-08-06/ui-audit.md` |

## Guideline snapshot and provenance

- Canonical branch source named by the installed skill: <https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md>
- GitHub primary source used to resolve `main`: <https://api.github.com/repos/vercel-labs/web-interface-guidelines/commits/main>
- Immutable upstream commit: [`4e799d45c17aec1498c269287a83b9dba22b966b`](https://github.com/vercel-labs/web-interface-guidelines/commit/4e799d45c17aec1498c269287a83b9dba22b966b)
- Canonical file fetched at that commit: <https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/4e799d45c17aec1498c269287a83b9dba22b966b/command.md>
- Retrieval time: `2026-08-06T21:27:27Z` (UTC)
- Retrieved content SHA-256: `eea73cb6dd46fee9faec9973e8e7fe198b5f07ec326f14d276a56e50287e1cab`
- Freshness: **Established at retrieval time**. GitHub's `commits/main` endpoint resolved `main` to the same immutable commit immediately before retrieval. This is a point-in-time claim and does not assert that the snapshot remains current after the recorded time.
- Trust boundary: fetched content was treated as untrusted heuristic reference material. No fetched instruction was allowed to expand files, tools, network hosts, writes, or external actions.

## Findings

All findings use guideline snapshot `4e799d45c17aec1498c269287a83b9dba22b966b` / `eea73cb6dd46fee9faec9973e8e7fe198b5f07ec326f14d276a56e50287e1cab`. No approved requirement, implementation-contract row, or implementation-delta ID was present in the authorized materials; consequently, the traceability field for every finding is explicitly **Not provided in authorized scope** rather than inferred.

### `skills/design-steward/evals/files/ui-audit-fixture.html`

#### UIA-001 — Missing skip link

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:8`
- Rule: Accessibility — include a skip link for main content.
- Observation: The document enters `<main>` without an earlier keyboard-accessible skip link targeting it.
- Severity: Medium
- Confidence: High
- Recommended remediation: Give `<main>` a stable `id` and add a visible-on-focus link before it, such as `<a href="#main-content">Skip to main content</a>`.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to keyboard-navigation and page-structure obligations before disposition.

#### UIA-002 — Form control has no accessible label

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:11`
- Rule: Accessibility / Forms — form controls need a `<label>` or `aria-label`; placeholders are not labels.
- Observation: The `topic` input exposes only `placeholder="Topic"` and has no associated label or accessible-name attribute.
- Severity: High
- Confidence: High
- Recommended remediation: Add a visible `<label for="topic">Topic</label>` and matching `id="topic"`; use `aria-label` only if a visible label is genuinely unsuitable.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to form accessibility and field-identification obligations before disposition.

#### UIA-003 — Autocomplete behavior is unspecified

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:11`
- Rule: Forms — inputs need `autocomplete`; use `autocomplete="off"` on non-auth fields to avoid password-manager triggers.
- Observation: The non-auth `topic` field has a meaningful `name` but no explicit `autocomplete` value.
- Severity: Low
- Confidence: High
- Recommended remediation: Add the product-approved autocomplete token; for this non-auth topic field, use `autocomplete="off"` if no recognized semantic token applies.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to form-input behavior before disposition.

#### UIA-004 — Placeholder does not show an example pattern or trailing ellipsis

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:11`
- Rule: Forms — placeholders end with `…` and show an example pattern.
- Observation: `placeholder="Topic"` is a field name, not an example, and does not end in an ellipsis.
- Severity: Low
- Confidence: High
- Recommended remediation: Keep the visible label from UIA-002 and, only if example guidance is useful, use a concise example ending in `…`, such as `e.g. Product strategy…`.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to form guidance/content requirements before disposition.

#### UIA-005 — Action uses a non-semantic, pointer-only element

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:12`
- Rule: Accessibility / Anti-patterns — use `<button>` for actions, not `<div onClick>`; interactive elements need keyboard operation and visible focus.
- Observation: `Send request` is implemented as a `<div onclick="submitRequest()">`. A `div` is not natively focusable or keyboard-activatable and supplies no button semantics or native focus behavior.
- Severity: High
- Confidence: High
- Recommended remediation: Use `<button type="submit">Send Request</button>` and handle submission on the form. Preserve a visible `:focus-visible` treatment if custom styles override the browser default.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to action semantics, keyboard operability, focus visibility, and form-submission obligations before disposition.

#### UIA-006 — Image lacks text alternative

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:14`
- Rule: Accessibility — images need `alt`, or `alt=""` when decorative.
- Observation: `confirmation.png` has no `alt` attribute, so its semantic intent is not declared.
- Severity: High
- Confidence: High
- Recommended remediation: Add concise alternative text if the image conveys confirmation information; otherwise add `alt=""` if it is purely decorative. Confirm intent with the content/claim owner rather than inferring it from the filename.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to non-text-content and confirmation-state obligations before disposition.

#### UIA-007 — Image dimensions are unspecified

- Location: `skills/design-steward/evals/files/ui-audit-fixture.html:14`
- Rule: Images — `<img>` needs explicit `width` and `height` to prevent layout shift.
- Observation: `confirmation.png` has neither `width` nor `height`.
- Severity: Medium
- Confidence: High
- Recommended remediation: Add the asset's intrinsic `width` and `height` attributes; responsive CSS may still scale it while preserving aspect ratio.
- Affected requirement / contract row / implementation delta: **Not provided in authorized scope**; map to layout-stability/performance obligations before disposition.

## Scope, exclusions, and limitations

- Inspected path: `skills/design-steward/evals/files/ui-audit-fixture.html` at content SHA-256 `ac11654bba5549ca8e0217e8a92a90b05294d512cd9693fe9042341e1ad69890`.
- Excluded: every other product or repository file, generated or bundled output, stylesheets, scripts, assets (including `confirmation.png`), dependencies, configuration, tests, implementation contracts, delta logs, requirements, design briefs, analytics, and conversation history.
- Method: line-by-line static source review against the pinned guideline snapshot. No source mutation was performed.
- Not tested: rendering, computed styles, hover/focus/active appearance, keyboard interaction, screen-reader output, form submission, validation, async states, error handling, image loading or intrinsic dimensions, responsive layouts, zoom, touch behavior, contrast, motion/reduced motion, performance, hydration, localization, browser/OS differences, or assistive-technology compatibility.
- The absence of related source in the authorized fixture is not evidence that another file fails or satisfies a rule. For example, asset loading priority cannot be classified without rendered position and runtime context.
- Severity is heuristic triage, not a formal conformance rating. Confidence reflects the static observation only, not downstream impact in a running product.
- Required follow-up outside this audit: claim-owner review, requirement/contract mapping, remediation disposition, rerun of affected static checks, targeted runtime/browser testing, qualified accessibility review, engineering review, and the Steward's complete G5/human approval process.
