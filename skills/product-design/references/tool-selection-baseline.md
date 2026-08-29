# Product-design tool selection baseline

**Baseline ID:** `PD-TOOLS-2026-08-29`
**Research reviewed:** 29 August 2026
**Scope:** responsive web, native iOS and Android, React Native, Flutter, and shared web/mobile wrappers

Use this reference when creating a toolchain, proposing setup, accepting an existing project alternative, or replacing a recommended tool. It records why the suite recommends each capability provider and what a replacement must preserve.

This is a decision baseline, not an instruction to install everything. Select the smallest set activated by the current phase, platform matrix, and evidence claims. Current official documentation overrides time-sensitive prices, quotas, versions, and setup commands; recheck it before promising capacity or changing configuration.

## Contents

1. [Selection policy](#selection-policy)
2. [Phase map](#phase-map)
3. [Recommended tools](#recommended-tools)
4. [MCP policy](#mcp-policy)
5. [Comparison baseline for replacements](#comparison-baseline-for-replacements)
6. [Previously assessed alternatives](#previously-assessed-alternatives)
7. [Source register](#source-register)

## Selection policy

Recommend a tool only when it passes all five tests:

1. **Sustainable capacity:** its indefinite free use supports approximately three to five new small projects per month while older projects continue to run. A trial, one-project portfolio limit, or quota that predictably stops routine checks fails. A paid GitHub plan is the accepted exception.
2. **Maturity:** it has established stewardship, active maintenance, documented releases, and a credible migration path.
3. **Portability:** accepted decisions live in Git, open formats, ordinary source, or normal test artifacts. Losing a SaaS account or MCP server must not erase the design contract.
4. **Material function:** it strengthens a workflow gate through an editable artifact, deterministic enforcement, real runtime, human access, physical-device evidence, or representative-user evidence.
5. **Non-replaceability by a strong model:** it obtains or enforces facts the agent cannot reliably synthesize. Generic UI generation, prompt packs, inspiration feeds, documentation wrappers, and thin CLI wrappers do not qualify by themselves.

Prefer an established project alternative when it produces equivalent durable evidence. Do not migrate a working toolchain merely to match this list. Conversely, familiarity, an MCP interface, or attractive generated output is not enough to replace a proven evidence layer.

### Evidence roles

Do not compare unlike roles:

| Role | What must survive |
|---|---|
| Canonical source | Editable design or semantic rules, stable identity, export, history, and an exit path |
| Runtime/evidence engine | Repeatable execution against the real target, deterministic assertions, diagnostics, and CI-readable artifacts |
| Human access/distribution | A named candidate tied to a build/ref that an authorized reviewer or tester can actually reach |
| User evidence | Known population, task, method, consent, limitations, and decision-linked findings |
| MCP adapter | Scoped live access only; removing it leaves the canonical source and evidence path intact |

## Phase map

| Phase | Use by default | Add only when triggered |
|---|---|---|
| Discovery | Git-owned brief/evidence register; web research from primary sources | Penpot for editable flows; Lyssna or moderated sessions for a named participant question |
| Direction | Git isolation plus Penpot or a real code/native renderer and matched captures | Image generation for necessary raster assets; preview hosting or tester distribution when decision makers need remote access |
| Contract | CSS variables for one web output; DTCG JSON for multiple outputs | Style Dictionary for multiple targets/themes/formats; framework workbench when reusable component states justify it |
| Prototype | Real renderer for the chosen medium | Playwright for web interaction; Maestro/native tests for installed apps; Cloudflare/App Distribution for remote human review |
| Implementation/change | Git, real target runtime, deterministic comparison, applicable accessibility path | Workbench, token compiler, MCP live inspection, physical devices, or distribution as activated by scope and claims |
| Review/accept-freeze | Immutable target identity, matched runtime evidence, accessibility evidence, Git-owned acceptance record | Test Lab, representative-user research, Clarity, preview hosting, or distribution only for a named conclusion |

## Recommended tools

### 1. Git and GitHub review controls

**Use:** Store briefs, contracts, tokens, source maps, stories/previews, test flows, approvals, and accepted baseline manifests in the repository. Use Git refs/diffs for isolation and rollback. Use GitHub protected checks and review when remote enforcement is needed.

**Why recommended:** Git provides portable history and recovery; GitHub adds mature collaboration and protected-check enforcement. These prevent an agent from silently redefining accepted state. GitHub paid plans are allowed by the suite's cost policy.

**Durable evidence:** committed files, immutable refs, diffs, review records, and required-check results.

**Limits:** Git records identity; it does not prove visual quality, runtime behavior, accessibility, or usability.

**Replacement baseline:** another VCS/forge must provide immutable identity, human review, rollback, protected paths/checks, artifact retention, and a documented migration/export path. Do not require GitHub when an existing GitLab, Bitbucket, or other established forge already satisfies those functions.

### 2. Penpot Free; official MCP on demand

**Use:** Create editable flows, wireframes, direction frames, prototypes, components, and reviewed visual references. Use MCP read-only first for exact selected-layer/file context; request scoped write access only for isolated design artifacts. Export reviewed source/reference artifacts to Git at gates.

**Why recommended:** Penpot combines a capable no-subscription visual editor, unlimited project creation suitable for this portfolio scale, open-source/self-hosting escape, structured components/styles/tokens, and an official bidirectional agent interface. It contributes editable visual state that a model cannot reconstruct reliably from prose.

**Durable evidence:** Penpot export, reference images, layer/frame identity, and the Git-owned design contract. MCP state is never canonical.

**Limits:** Hosted recovery/history is not the long-term archive. Penpot token interchange is not assumed to be a lossless round trip with every DTCG 2025.10 feature. Keep Git tokens canonical and sync only a reviewed compatible subset. Never expose a local MCP port beyond its trusted boundary.

**Replacement baseline:** compare structured editing, components/variants, responsive layout, tokens, prototype interaction, reliable export, collaboration, agent read/write depth, security, free portfolio capacity, and an exit path. Lunacy is a credible offline fallback but currently offers less bidirectional agent control. Figma is acceptable only as an already-funded project tool with sufficient access; it is not the free-first default.

### 3. CSS variables, DTCG JSON, and Style Dictionary

**Use:** Keep plain committed CSS custom properties for a single web target. Use DTCG JSON when rules must cross platforms, themes, aliases, or output formats. Add Style Dictionary only to compile multiple deterministic outputs such as CSS/TypeScript, Swift, Kotlin/XML, or Dart.

**Why recommended:** Text sources are diffable and portable; DTCG provides an interoperable vocabulary; Style Dictionary is mature, open source, extensible, and quota-free. Together they prevent hand-copied values from drifting across implementations.

**Durable evidence:** canonical token source, pinned transform configuration, generated outputs, clean regeneration diff, and golden/unit checks for transforms.

**Limits:** Do not add a compiler to a one-theme microsite that needs only CSS variables. Support for newer or complex DTCG types varies by compiler; use the smallest proven subset and test every configured output.

**Replacement baseline:** the candidate must validate the required DTCG subset, generate every required target deterministically, preserve aliases and metadata needed by the project, support custom transforms, run locally and in CI without restrictive quotas, and offer a low-risk migration. Terrazzo may supplement validation but has a smaller ecosystem. Tokens Studio is not the default because the required Variables/MCP workflow introduces a recurring paid dependency.

### 4. Framework-native component workbenches

**Use:** Prefer an existing component/state route. Otherwise use Storybook for web, React Native Storybook for RN, Widgetbook OSS for Flutter, Xcode previews for Apple UI, or Compose previews/UI Check for Android. Capture loading, error, empty, selected, focus, long-copy, large-text, theme, locale, and responsive/adaptive states.

**Why recommended:** These tools render real framework components with deterministic fixtures. They turn a prose component inventory into executable states and reduce the chance that an agent fixes one screen by creating an incompatible local component.

**Durable evidence:** story/preview/catalog source, fixtures, build output, test results, and captures produced by the real renderer.

**Limits:** Add a workbench only when repeated component-state work justifies its maintenance. Storybook MCP surfaces remain optional and framework-limited; Widgetbook Cloud quotas are not part of the foundation.

**Replacement baseline:** it must render production components rather than imitations, isolate all required states, build repeatably, support accessibility inspection and target themes/viewports, and remain useful without a hosted paid snapshot service.

### 5. Playwright Test for web runtime and visual regression

**Use:** Exercise browser journeys, responsive matrices, component/state routes, screenshot assertions, console/network checks, and traces. Pair it with `@axe-core/playwright` for automated web accessibility checks. Pin browser, OS, fonts, scale, data, animation, and time inputs for baselines.

**Why recommended:** Playwright is mature, actively maintained, open source, cross-browser, quota-free, and combines runtime interaction with deterministic visual evidence. Ordinary checked-in tests and artifacts remain usable without an MCP or hosted visual-regression subscription.

**Durable evidence:** tests, fixtures, baseline images, actual/diff images, traces, and CI results tied to a Git ref.

**Limits:** screenshot similarity is not a quality judgment. An implementation worker must not update accepted baselines. Playwright MCP is optional for persistent exploration, not required for normal execution.

**Replacement baseline:** prove equivalent browser coverage, stable locators, screenshot assertions and diffs, traces/diagnostics, parallel CI operation, accessibility integration, local reproducibility, and no portfolio-wide quota. Existing Cypress/WebdriverIO suites may qualify; do not add a second runner without a measured gap. BackstopJS and hosted snapshot services add duplicate configuration or quota risk for a new setup.

### 6. Maestro CLI for mobile runtime and visual regression

**Use:** Drive installed iOS/Android, React Native, and Flutter apps through readable YAML flows; inspect the accessibility hierarchy; run taps, typing, swipes, assertions, and screenshot comparisons. Use MCP only for live device inspection; keep flows and screenshots in Git. Combine with native tests where platform coverage or integration depth requires them.

**Why recommended:** Maestro supplies a concise architecture-independent black-box loop across the major mobile stacks, includes deterministic screenshot assertions, is open source and quota-free locally, and exposes an official live agent adapter.

**Durable evidence:** YAML flows, native tests where needed, asserted reference images, actual/diff captures, logs, and build/device identity.

**Limits:** iOS Maestro execution is simulator-oriented; physical iOS evidence needs an appropriate native/Test Lab path. Do not use experimental model-based assertions as blocking acceptance. Maestro Cloud is paid and excluded from the foundation.

**Replacement baseline:** compare iOS/Android and framework coverage, accessibility-tree interaction, concise maintainable flows, deterministic screenshots, CI/local execution, diagnostics, device management, and total maintenance. Appium is the preferred fallback for unusual platforms or an established WebDriver estate, not the new-project default.

### 7. Platform accessibility tools

**Use:** Web uses axe with Playwright plus keyboard, zoom/reflow, focus, and relevant screen-reader checks. Apple uses Accessibility Inspector/XCTest audits plus VoiceOver and system settings. Android uses Compose semantics/UI checks or Espresso AccessibilityChecks plus TalkBack and display/font settings. Flutter uses semantics/guideline tests plus both platform assistive technologies.

**Why recommended:** accessibility lives partly in semantics trees, focus order, assistive technology, text scaling, and platform settings—facts invisible in ordinary screenshots. The selected tools are open source or included with platform SDKs and produce repeatable evidence.

**Durable evidence:** source tests, reports, audit recordings/notes, manual checklist, target configuration, and accepted exceptions.

**Limits:** no automated scanner proves accessibility. Manual assistive-technology work remains required in proportion to the claim. A paid axe MCP does not add foundational value over deterministic test output.

**Replacement baseline:** cover the same rendered semantics, roles/labels, focus/order, contrast, target sizes, scaling/reflow, motion, and assistive-technology behavior on every claimed platform. Report automation and manual evidence separately.

### 8. Cloudflare Pages Free for conditional web review

**Use:** Publish a commit-bound preview only when required reviewers cannot run the web candidate locally and the existing host provides no suitable preview. Deploy a preview, not production.

**Why recommended:** it offers mature, straightforward pull-request previews and, at the research date, enough free build/project capacity for several small projects. It provides independent human access, which a local dev server cannot.

**Durable evidence:** build configuration in Git, candidate ref, preview URL/identity, and review record.

**Limits:** hosting is conditional and externally stateful. Recheck current limits before adoption. Skip it when an existing host already produces safe previews or local review is sufficient.

**Replacement baseline:** secure per-candidate previews, immutable commit linkage, adequate build/project limits, logs, access control, teardown, custom build support, and easy migration. GitHub Pages or the project's normal host may be equivalent.

### 9. Firebase Test Lab Free for conditional physical-device sampling

**Use:** Sample a small, risk-based real-device/OS matrix for significant mobile candidates or device-specific defects after local simulator/emulator checks pass. Start with virtual targets, then consume approved physical quota.

**Why recommended:** it provides mature Android and iOS device infrastructure and artifacts without building a private device lab. At the research date, the Spark allowance was suitable for selective release sampling, not per-commit execution.

**Durable evidence:** matrix configuration, native test artifacts, exact app/build identity, device/OS identity, logs, screenshots/video, and result links or exports.

**Limits:** quotas and supported harnesses vary and must be rechecked. Test Lab proves device behavior, not usability. Cross-platform flows may need native wrappers, especially on iOS.

**Replacement baseline:** required physical platforms/models/OS versions, supported harnesses, quota for the planned cadence, artifact quality, CI/API access, privacy/location, and reproducibility. An existing owned-device lab is equivalent when it records the same evidence.

### 10. Firebase App Distribution Free for conditional tester delivery

**Use:** Deliver an exact signed mobile candidate to approved internal or target testers when real-device human use is required. Pair every distribution with a named task and feedback method.

**Why recommended:** it is mature, supports iOS and Android, integrates with common build/CI paths, and provides ample no-cost tester/release capacity for small products at the research date.

**Durable evidence:** signed build identity, release notes, approved tester/group scope, distribution record, task protocol, and consented findings.

**Limits:** uploading a build changes external state and requires authorization. Distribution proves access only—not installation, successful use, or usability.

**Replacement baseline:** both target platforms, tester/group controls, signing and retention behavior, CLI/API/CI support, auditability, free capacity, privacy, and export/migration. An existing TestFlight/Play internal-testing or beta channel may be preferable.

### 11. Lyssna Free or moderated testing for conditional pre-release evidence

**Use:** Use a small study for a named comprehension, navigation, preference, or task question when representative participants are required. Prefer direct moderated sessions when recruitment and observation are already available.

**Why recommended:** Lyssna supplies structured prototype, tree, card-sort, preference, and quick-study mechanics; its free self-recruited response visibility was sufficient for focused small studies at the research date. The actual participants and research method—not the dashboard—are the irreplaceable capability.

**Durable evidence:** approved research question, population, recruitment/consent, tasks, observations, limitations, findings, and resulting decisions in Git.

**Limits:** recheck free-plan response visibility and never promise a paid panel without approval. Synthetic users and agent critique cannot replace participant evidence.

**Replacement baseline:** method fit, representative recruitment, usable free sample size, prototype/live-target support, consent/privacy, observation depth, accessible exports, and durable decision capture. Moderated research is an equal or stronger replacement when run rigorously.

### 12. Microsoft Clarity Free for conditional post-launch behavior

**Use:** Add only after launch when a named decision requires session/heatmap/friction evidence and consent, masking, retention, population, and performance have been approved. Use scoped read-only access or sanitized summaries during review.

**Why recommended:** Clarity provides no-cost web and mobile behavioral observation at portfolio scale and covers native Apple/Android, React Native, Flutter, and web. It obtains real behavior signals that a model cannot invent.

**Durable evidence:** decision question, instrumentation/masking decision, release/population context, minimized observations, limitations, and accepted findings—not raw session replay as the only record.

**Limits:** behavioral signals do not explain motives or validate usability. Mobile SDK performance and platform limits require target testing. Do not instrument production or inspect sensitive sessions without explicit authority. Its MCP/query allowance is not the reason for selection.

**Replacement baseline:** platform coverage, free portfolio capacity, consent/masking controls, data retention/location, performance cost, session/heatmap fidelity, read-only access, export, and ability to connect observations to a decision. PostHog may be an explicit single-product exception when structured funnels justify its project/pricing model.

## MCP policy

MCP servers are replaceable adapters. Declare or configure one only when live state materially improves the selected phase; prefer read-only access until a scoped write is authorized.

| MCP | Default posture | Canonical evidence if unavailable |
|---|---|---|
| Penpot | On demand for exact design context; isolated writes only | Penpot export, reviewed images, contract |
| Maestro | On demand for live device inspection | YAML/native flows, captures, normal CLI output |
| Storybook/RN Storybook | Optional state discovery; current APIs may be limited | Story/preview source, fixtures, real render |
| Playwright | Optional persistent browser exploration | Tests, traces, screenshots, CLI output |
| Chrome DevTools | Specialist performance/runtime diagnosis only | trace/Lighthouse artifacts and source fixes |
| Clarity analytics | No default install | sanitized observations and accepted findings |
| Framework/component registry MCPs | No default install | repository components, registry docs/CLI, lockfile |

An MCP outage is `not-applicable` when an equivalent deterministic path remains available and the adapter was not selected. It is degradable only when losing live context reduces a named output. It is blocking only when no equivalent evidence path can support the requested claim.

## Comparison baseline for replacements

Do not replace a recommended or established project tool from memory or preference. Copy [tool-substitution-record.md](../assets/tool-substitution-record.md) to `design/decisions/tool-substitutions/<date>-<capability>.md` for a durable engagement and record:

1. **Trigger:** deprecation, security issue, quota/cost failure, missing platform, maintenance burden, or measured evidence gap.
2. **Current role and artifacts:** what is canonical, what evidence it produces, integrations, protected baselines, and exit format.
3. **Candidate facts:** current stable version, stewardship, license, release activity, security posture, free-tier limits across the whole portfolio, authentication/data handling, and official migration/export path.
4. **Functional comparison:** every current required capability plus the specific new gap. Treat an MCP or AI-generation feature as an accelerator, not automatic superiority.
5. **Representative pilot:** run the same real workflow and matrix with pinned inputs. For web, include two viewport classes, a stressed state, interaction, accessibility output, and an unchanged-surface preservation check. For mobile, include each claimed platform class, one stressed state, runtime interaction, accessibility evidence, and deterministic visual comparison.
6. **Artifact comparison:** confirm source, baselines, logs/diffs, approval identity, and CI results remain human-inspectable and exportable.
7. **Migration and rollback:** list files/services changed, conversion loss, dual-run period if needed, rollback steps, and the old tool's removal condition.
8. **Decision:** `keep`, `pilot`, `adopt`, or `exception`, with owner approval for a canonical-source, evidence-engine, external-service, CI, analytics, or production-dependency change.

Minimum acceptance table:

| Criterion | Required result |
|---|---|
| Sustainable free capacity | Pass at three to five new small projects/month plus maintained-project checks, or an explicitly approved cost |
| Maturity and maintenance | Equal/better stewardship and a credible multi-year path |
| Functional coverage | No loss in an activated capability or gate |
| Evidence quality | Equal/better deterministic, target-bound artifacts |
| Portability and exit | Git/open export; no SaaS-only accepted identity |
| Security/privacy | No material regression; auth/data boundaries documented |
| Agent value | Obtains/enforces facts rather than duplicating strong-model work |
| Migration safety | Tested conversion, rollback, and preservation proof |

Changing only an optional MCP adapter may use a shorter record, but it still must prove that canonical artifacts and authorization boundaries remain unchanged. Never edit accepted baselines merely to make a replacement pilot pass.

## Previously assessed alternatives

This table is a comparison starting point, not a permanent ban. Reopen a decision when official facts materially change and run the replacement protocol.

| Candidate | Baseline decision | Reason at review date |
|---|---|---|
| Figma Professional + MCP | Not portfolio default | Subscription required; free MCP capacity was insufficient for sustained agent design. Use if already funded and it passes current access/capacity checks. |
| Tokens Studio Variables/MCP | Reject as foundation | Recurring paid dependency; DTCG JSON plus Style Dictionary covers the durable cross-platform function. |
| Supernova Free | Reject as portfolio default | One-system/context constraints did not fit several ongoing projects. |
| Chromatic, Argos, Percy | Reject as foundation | Hosted snapshot quotas/retention add portfolio risk over Playwright/Maestro plus Git. An existing paid project setup may remain. |
| Lost Pixel | Reject | Product sunset made it unsuitable for multi-year adoption. |
| BackstopJS | Do not add for new work | Duplicates Playwright's browser/screenshot layer; preserve an existing working suite until migration has measured value. |
| Paper | Reject as foundation | Agent-call quota and maturity were insufficient for sustained iteration. |
| OpenPencil, pen.dev | Watch | Attractive open/Git-native ideas, but maturity, openness, or migration confidence was insufficient. Re-evaluate after stable adoption evidence. |
| Lunacy | Offline fallback | Mature and free, but less bidirectional agent control than Penpot at review time. |
| Motiff | Reject | Service closure demonstrates the risk of SaaS-owned canonical artifacts. |
| Canva MCP | Asset-only tool | Useful for communication assets, not a portable application UI component/prototype source. |
| Maestro Cloud, Widgetbook Cloud | Reject as foundation | Paid or restrictive hosted quotas; local OSS layers provide the required evidence. |
| Maze MCP, paid axe MCP, Builder/Fusion, Anima MCP | Reject as foundation | Paid/restrictive agent access or generation focus; deterministic OSS/runtime layers cover the required function. |
| Generic UI generators, prompt packs, inspiration services | Reject | A strong model already generates and researches; these add no canonical artifact, enforcement, runtime truth, distribution, or real-user evidence. |
| PostHog Free | Explicit exception | Strong event/funnel capability, but the free portfolio model was less suitable than Clarity. Use when one product's structured analytics value justifies it. |

## Source register

Revalidate the relevant official source before setup or replacement:

- GitHub rulesets and protected checks: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- Penpot pricing and MCP: <https://penpot.app/pricing>, <https://help.penpot.app/mcp/>
- DTCG format and Style Dictionary: <https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/>, <https://www.styledictionary.org/>
- Storybook, React Native Storybook, and Widgetbook: <https://storybook.js.org/docs/get-started/install>, <https://storybookjs.github.io/react-native/>, <https://docs.widgetbook.io/>
- Playwright screenshots and accessibility: <https://playwright.dev/docs/test-snapshots>, <https://playwright.dev/docs/accessibility-testing>
- Maestro CLI/MCP: <https://docs.maestro.dev/get-started/quickstart>, <https://docs.maestro.dev/getting-started/maestro-mcp>
- Apple, Android, and Flutter accessibility: <https://developer.apple.com/documentation/accessibility/accessibility-testing>, <https://developer.android.com/guide/topics/ui/accessibility/testing>, <https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility>
- Cloudflare Pages: <https://developers.cloudflare.com/pages/get-started/>
- Firebase Test Lab and App Distribution: <https://firebase.google.com/docs/test-lab>, <https://firebase.google.com/docs/app-distribution>
- Lyssna help: <https://help.lyssna.com/>
- Microsoft Clarity: <https://learn.microsoft.com/en-us/clarity/>

Review the baseline immediately when a recommended tool is deprecated, changes ownership/license, has a material security incident, loses a required platform/capability, or changes its free capacity enough to fail the admission test. Otherwise, conduct a source revalidation at least annually before treating the recommendation as current.
