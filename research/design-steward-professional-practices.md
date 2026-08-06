# Professional practices a reusable Design Steward should operationalize

Research date: 2026-08-06
Scope: reusable professional practice for web products and services, not a prescription for a particular organization, design system, brand, or tool.

## Executive answer

A reusable Design Steward should be an **evidence-and-decision steward**, not a substitute product designer, researcher, content specialist, engineer, accessibility evaluator, domain expert, or product owner. Its durable job is to keep a multidisciplinary team anchored to real user needs, expose assumptions and risk, preserve traceability from evidence to decisions to shipped behavior, require the least expensive evidence that can retire the next material risk, and stop unsupported claims from crossing a decision gate.

This operating model is supported by four complementary source families:

1. [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) places human-centred design principles and activities across the whole lifecycle of interactive systems.
2. The [Design Council Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/) describes divergent and convergent work as nonlinear, people-centred, collaborative, and iterative; the [GOV.UK Service Manual](https://www.gov.uk/service-manual) makes those ideas operational through multidisciplinary roles, discovery/alpha/beta/live decisions, inclusive research, prototyping, and performance measurement.
3. [WCAG 2.2](https://www.w3.org/TR/WCAG22/), W3C's [accessibility evaluation guidance](https://www.w3.org/WAI/test-evaluate/), and [WCAG-EM](https://www.w3.org/TR/WCAG-EM/) establish testable requirements, human evaluation, representative sampling, complete-process coverage, and transparent reporting.
4. Original research provides narrower evidence for measurement and AI controls: Google's [HEART/Goals-Signals-Metrics paper](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) links product goals to user-centred measures, while Doshi and Hauser's [generative-AI creativity experiment](https://doi.org/10.1126/sciadv.adn5290) found more individually creative but more similar outputs in its story-writing setting. The latter is a risk signal about homogenization, not direct proof about web-interface design.

The Steward should therefore operationalize a loop, not a waterfall:

> frame the decision and risk -> gather proportionate evidence -> make and compare alternatives -> test with the right people and standards -> record the decision and limitations -> implement and inspect -> measure in use -> revisit

Every gate has four valid outcomes: **proceed, iterate, pivot, or stop**. Passing a gate means that named humans accepted the residual risk on documented evidence; it does not mean that a canvas was filled in or a polished mock-up exists.

## 1. Operating contract

The following rules are durable across team structures and toolchains.

### 1.1 Start with an evidenced problem, not a requested feature

Before solution work, record the people affected, the outcome they are trying to achieve, the current journey and context, observed barriers, organizational intent, constraints, and the decision the team must make. Separate observed facts from interpretation and assumptions. GOV.UK says discovery must understand the problem before committing to build and must cover users, goals, constraints, policy intent, and opportunities; it explicitly says not to start building in discovery ([discovery phase](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)). Its user-needs guidance says ungrounded opinions and suggestions are assumptions to prove through research, and user needs should express problems rather than proposed solutions ([learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)).

**Steward control:** reject feature-shaped needs such as "users need a dashboard" unless evidence establishes why that solution is necessary. Rewrite them as outcome hypotheses and attach evidence identifiers.

### 1.2 Make the process risk-led and nonlinear

Discovery, synthesis, architecture, content, interaction, visual design, prototyping, and evaluation overlap. Teams should diverge before converging and revisit earlier framing when new evidence changes the problem. The Design Council explicitly describes its Double Diamond as nonlinear and says early making can happen in discovery while feedback continues after delivery ([Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/)). GOV.UK alpha guidance says to prototype only enough to test the riskiest assumptions and expect to discard code and ideas ([alpha phase](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)).

**Steward control:** maintain a ranked assumption-and-risk register. Drive the next activity from the highest consequential uncertainty, not from a fixed ceremony or deliverable sequence.

### 1.3 Use a multidisciplinary team with explicit decision rights

The work is shared; authority is not. GOV.UK requires product, service ownership, delivery, research, content, design, and development capabilities, and defines specialist responsibilities ([service-team roles](https://www.gov.uk/service-manual/the-team/what-each-role-does-in-service-team)). Quality belongs to the whole team, with final responsibility held by the service owner. This prevents the Steward from becoming an unreviewed designer-of-everything.

**Steward control:** every material decision record names a recommender, consulted specialists, accountable approver, date, evidence, alternatives, residual risk, and review trigger.

### 1.4 Treat content, structure, behavior, and presentation as one experience

Information architecture and content are not decoration applied after interaction design. Content should meet valid task-based needs and record its evidence and acceptance criteria ([GOV.UK content guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/)). IA should organize, structure, and label content so people can find information and complete tasks; card sorting elicits how users group information, while tree testing evaluates findability in a proposed hierarchy ([Digital.gov IA case](https://digital.gov/2022/01/06/open-source-information-architecture-design-using-the-tools-you-have-to-conduct-card-sorting-and-tree-testing)).

**Steward control:** require real or representative content, data, terminology, and edge cases in flows and prototypes. Do not accept lorem ipsum, idealized happy paths, or a sitemap inferred only from organizational structure.

### 1.5 Reuse evidence-backed conventions, then adapt with evidence

Familiar patterns reduce relearning, but consistency is not uniformity. GOV.UK calls design patterns evidence-based solutions to common problems, tells teams to start from existing patterns, and permits adaptation or new patterns when research shows existing ones do not meet users' needs ([using, adapting and creating patterns](https://www.gov.uk/service-manual/design/using-adapting-and-creating-patterns)). Its current design principles say to "be consistent, not uniform" and to design with data ([Government Design Principles](https://www.gov.uk/guidance/government-design-principles)). W3C warns that its ARIA Authoring Practices examples are illustrative, not prescriptive or production-ready ([APG introduction](https://www.w3.org/WAI/ARIA/apg/about/introduction/)).

**Steward control:** for each novel or changed pattern, record the unmet need, alternatives examined, research evidence, accessibility behavior, and contribution/reuse decision. Novelty is not a goal by itself; neither is visual conformity.

### 1.6 Build accessibility in, then verify it in the implementation

Use the current applicable standard and organizational or legal target; for a reusable default, record WCAG 2.2 Level AA unless a stricter target applies. WCAG success criteria are technology-independent and testable, and conformance applies to full pages and complete processes ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)). W3C says no tool alone can establish accessibility and knowledgeable human evaluation is required ([Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/)). It also says user evaluation with disabled people and standards evaluation must be combined because neither establishes the other ([involving users in evaluation](https://www.w3.org/WAI/test-evaluate/involving-users/)).

**Steward control:** accessibility evidence must combine automated checks, keyboard and assistive-technology/manual evaluation by qualified people, standards-based scope and results, and research with relevant disabled users. A design-file contrast plugin or a single participant is not a conformance claim.

### 1.7 Measure outcomes, not output volume

Define a user outcome, signals that indicate it, metrics with baselines and guardrails, and a review cadence before launch. The HEART paper offers one adaptable vocabulary and, more durably, a Goals-Signals-Metrics mapping process ([Rodden, Hutchinson, and Fu](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/)). GOV.UK requires teams to define success and use performance data to decide whether a service meets needs and enables task completion ([performance data](https://www.gov.uk/service-manual/measuring-success/using-data-to-improve-your-service-an-introduction)).

**Steward control:** ban vanity metrics without a causal or decision link. Every metric must specify the decision it informs, population and segment, data source, calculation, baseline, expected direction, guardrail, owner, and interpretation limits.

### 1.8 Keep an inspectable evidence chain

The Home Office's engineering principle requires requirements and decisions to point back to current, valid, transparent evidence and recommends decision logs and useful design artifacts for assurance and maintenance ([Design from evidence](https://engineering.homeoffice.gov.uk/principles/design-from-evidence/)). W3C's accessibility evaluation methodology similarly requires scope, sample, methods, and outcomes to be documented for transparency and replicability ([WCAG-EM](https://www.w3.org/TR/WCAG-EM/)).

**Steward control:** no material insight, requirement, priority, or claim should exist only in a presentation. It must resolve to inspectable evidence or be labeled as an assumption.

## 2. Role boundaries and decision rights

The Design Steward facilitates, challenges, connects, and records. It may draft artifacts or alternatives, but it does not inherit specialist accountability. `A` below means the human who accepts the decision and residual risk; `R` means the specialist who leads the work. Titles can vary, but the capability must exist.

| Area | Accountable / responsible humans | Design Steward may | Design Steward must not |
| --- | --- | --- | --- |
| Product outcome, priority, scope, funding, launch | Product/service owner `A`; product manager `R` | expose evidence, options, dependencies, and residual risk; recommend gate outcome | silently prioritize, approve launch, or present a design preference as business authority |
| Research validity and participant welfare | Qualified user researcher `R`; appropriate ethics/privacy owner `A` | maintain questions, assumption links, evidence inventory, and decision consumption | fabricate or simulate participants; recruit, consent, moderate sensitive research, or generalize findings without qualified oversight |
| Synthesis and service framing | Researcher and relevant design lead `R`; multidisciplinary team consulted | preserve observation-to-finding traceability; surface contradictions and gaps | turn AI clusters or workshop votes into findings without returning to source evidence |
| Information architecture | IA/content/interaction design capability `R` | inventory content, draft models and test plans, compare structures | approve labels or hierarchy based only on stakeholder preference, analytics volume, or generated personas |
| Content | Content designer `R`; domain/legal/policy owner accountable for factual or regulated claims | draft variants, check traceability, identify terminology and comprehension risks | certify truth, legality, reading comprehension, localization, or tone outside human specialist review |
| Interaction and visual design | Interaction/product/visual designer `R` | generate alternatives, enforce state coverage, connect rationale to evidence and system constraints | become the sole taste-maker; claim usability or brand fit from a polished artifact alone |
| Technical feasibility and implementation | Engineering/technical architecture `R`; engineering owner `A` | make design intent testable, pair on prototypes, inspect built behavior | dictate architecture, security, performance, or semantic implementation without engineering authority |
| Accessibility | Whole team responsible; accessibility specialist/evaluator and engineering/design leads `R`; service owner `A` | keep target and test coverage visible; block unsupported conformance claims | equate automated checks, guidelines, or disabled-user research with a complete conformance evaluation |
| Measurement and experiments | Performance/data analyst `R`; product owner `A` | map goals to signals and decisions; require baselines, segments, and guardrails | make prevalence, causality, significance, or business-impact claims without appropriate analysis |
| Security, privacy, legal, and domain safety | Named specialists `R/A` | raise risks early and route decisions | approve specialist risk or use research/AI tools outside approved data handling |
| Quality and release | Whole team responsible; QA/engineering leads `R`; service owner `A` | trace acceptance evidence and unresolved issues | accept a design-file review as proof that production behavior works |

This boundary follows the GOV.UK role model: user researchers plan and conduct research, content designers own service content, developers advise on feasibility and build accessible software, performance analysts provide quantitative and qualitative performance evidence, and the service owner retains overall responsibility ([service-team roles](https://www.gov.uk/service-manual/the-team/what-each-role-does-in-service-team)).

## 3. Lifecycle playbook: practices, artifacts, and evidence

Artifacts are **conditional instruments**, not mandatory theater. Create the smallest artifact that lets the team inspect evidence, make the next decision, implement intent, or learn after launch. Merge artifacts when one representation can do several jobs without losing traceability.

### 3.1 Discovery

#### Discovery practices

- State the decision, problem boundary, affected people, desired outcomes, current behavior, end-to-end and cross-channel context, constraints, known evidence, unknowns, and harms.
- Review existing research, analytics, search and support logs, operational data, policy/domain material, competitor or analogous services, and the current service before commissioning new research.
- Observe and interview actual or likely users in relevant contexts. Include service staff and support roles where they form part of the experience.
- Recruit across meaningful behavior, context, access need, digital confidence, and exclusion risk rather than relying on an "average user."
- Convert feature requests and stakeholder opinions into assumptions or research questions.
- Rank assumptions by consequence and uncertainty; define what evidence would change the decision.

GOV.UK's discovery research guidance requires learning who likely users are, what they do now, their problems, and their needs before planning, designing, or building, using both direct research and existing data ([user research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery)).

#### Discovery artifacts

- problem-and-outcome brief;
- stakeholder/system map only where relationships or channels affect the problem;
- current journey or service blueprint only where sequence, backstage operations, or handoffs matter;
- evidence inventory;
- assumptions, constraints, dependencies, and risk register;
- research plan with questions, method rationale, recruitment matrix, consent/data handling, analysis plan, and decision linkage;
- initial Goals-Signals-Metrics map and guardrails.

#### Discovery exit evidence

- actual or likely users and relevant variation are identified;
- needs and barriers are evidenced and solution-neutral;
- end-to-end context and material constraints are understood enough to choose the next risk to test;
- success and unacceptable harm are defined;
- evidence gaps and limitations are explicit;
- the accountable owner chooses explore, reframe, pause, or stop.

### 3.2 Synthesis and framing

#### Synthesis practices

- Analyze close to each research round with observers and relevant specialists.
- Preserve atomic observations separately from interpretation. Link every finding to sessions, behavioral or quoted evidence, population/context, and contradictory cases.
- Distinguish a repeated pattern, a single critical incident, an unmet need, a preference, and a team hypothesis.
- Triangulate qualitative evidence with operational or behavioral data where available; disagreement is a prompt for more inquiry, not a reason to average incompatible evidence.
- Prioritize by user harm/value, frequency only when measured appropriately, strategic fit, feasibility, reversibility, and confidence.

GOV.UK advises recording what was seen or heard before interpretation, involving observers to reduce individual bias, then deriving findings and actions ([analyzing a research session](https://www.gov.uk/service-manual/user-research/analyse-a-research-session)).

#### Synthesis artifacts

- source-indexed observations and findings;
- opportunity/problem framing linked to evidence;
- updated needs, journey/system model, and risk register;
- decision log including rejected framings and contradictory evidence.

#### Synthesis exit evidence

- a reviewer can traverse finding -> observations/data -> participant or source context -> decision;
- the frame explains whom the problem affects, under what conditions, with what consequence;
- material gaps, dissent, and confidence are visible;
- generated personas or empathy maps, if used, are derived from research and cannot be mistaken for participants or evidence.

### 3.3 Information architecture

#### Information-architecture practices

- Inventory content, tasks, objects, relationships, metadata, ownership, lifecycle, and search/navigation routes before drawing a sitemap.
- Model the user's domain and language, not the organization chart.
- Separate generative methods from evaluative ones: open card sorting can reveal grouping and language; closed sorting can compare a proposed grouping; tree testing can evaluate whether people can find destinations in a hierarchy. None alone proves that the full interface works.
- Test critical findability tasks with representative users and realistic labels; include search, cross-links, alternate routes, permissions, and no-result/recovery behavior where relevant.
- Define governance for labels, metadata, redirects, archiving, and content ownership.

Digital.gov describes card sorting as a way to learn how users expect content to be organized and documents a government team combining card sorting with tree testing ([testing and assessment](https://digital.gov/guides/research-collaboration/testing/organization), [IA case](https://digital.gov/2022/01/06/open-source-information-architecture-design-using-the-tools-you-have-to-conduct-card-sorting-and-tree-testing)).

#### Information-architecture artifacts

- content/task/object inventory;
- proposed information model, taxonomy, navigation model, and critical-label glossary;
- redirect/migration and ownership plan when changing an existing service;
- task-based card-sort/tree-test or equivalent findability evidence, including method, participants, tasks, results, failures, and limitations.

#### Information-architecture exit evidence

- representative users can locate and correctly interpret critical content or actions at the fidelity being tested;
- high-risk labels are understood in users' language;
- alternate, error, empty, permission, and recovery routes are designed;
- unresolved findability risks have an owner and test plan.

### 3.4 Content design

#### Content-design practices

- Give every content item a valid user need, purpose, owner, source of truth, review/expiry rule, and acceptance criteria.
- Write content and interaction together from the earliest prototype. Use the language users use; prefer plain, direct, task-oriented language while preserving required domain accuracy.
- Design headings, labels, instructions, validation, errors, confirmations, help, notifications, privacy explanations, and recovery as functional parts of the interaction.
- Test comprehension and action, not preference for wording. Include people with relevant literacy, language, cognitive, stress, and access contexts.
- Have domain, policy, legal, localization, and safety owners approve the claims for which they are accountable; content design owns clarity and usefulness, not the underlying law or fact.
- Plan maintenance and removal as well as publication.

GOV.UK's current publishing guidance says every piece of content should meet a valid task-based need, distinguishes content design from user research, and recommends recording evidence and acceptance criteria ([Identify user needs](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/)).

#### Content-design artifacts

- content inventory/model and source/owner map;
- terminology and critical-copy matrix across states and channels;
- evidence-backed content acceptance criteria;
- factual/legal approval and content lifecycle record where relevant;
- comprehension/task evidence for high-risk content.

#### Content-design exit evidence

- content is complete enough to test realistic tasks;
- users can understand the purpose, required action, consequence, and recovery for critical flows;
- claims have accountable source owners;
- required alternatives and programmatic labels are specified against the accessibility target.

### 3.5 Interaction and visual design

#### Interaction and visual-design practices

- Start with tasks, state, sequence, feedback, and recovery before surface styling. Specify entry, progress, success, cancel, back, timeout, error, empty, loading, offline, permission, destructive, undo, and help states as applicable.
- Produce meaningfully different alternatives before convergence. Alternatives should vary the model, sequence, hierarchy, disclosure, or control strategy, not only color and decoration.
- Reuse a proven design-system component where it fits; document the evidence when adapting or creating a pattern.
- Use visual hierarchy, typography, spacing, color, imagery, and motion to express content importance, action, state, and identity. Require a rationale tied to user context, brand/system intent, evidence, or an accessibility constraint.
- Design responsive behavior and multiple input modes. WCAG 2.2 includes requirements covering reflow, text resize, contrast, visible and unobscured focus, target size, labels, errors, status messages, and programmatic name/role/value ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).
- Critique with multiple disciplines and evaluate in a browser; visual polish does not compensate for unclear structure or behavior.

#### Interaction and visual-design artifacts

- task flows and interaction/state model;
- a small set of structurally distinct directions with trade-offs;
- component/pattern reuse and deviation record;
- responsive, keyboard, focus, semantics, content, and motion annotations where intent cannot be inferred from code or shared components;
- visual rationale and tokens/variables only when they support coherent implementation and maintenance.

#### Interaction and visual-design exit evidence

- critical tasks and all material states are represented with real content and realistic data;
- the chosen direction has comparative rationale, not only stakeholder preference;
- keyboard, responsive, zoom/reflow, contrast, focus, error, and assistive-technology intent are testable;
- design-system departures and novel patterns have an evidence plan.

### 3.6 Prototyping

#### Prototyping practices

- State the question and required fidelity before making a prototype. Use the cheapest medium that can answer it.
- Use sketches or static representations to explore concepts and hierarchy; use interactive or coded prototypes for sequence, state, responsive behavior, keyboard interaction, realistic content/data, and technical feasibility.
- Build only enough of the end-to-end experience to make the target task believable, while not hiding dependencies that determine whether the task succeeds.
- Pair design, content, research, and engineering on higher-fidelity prototypes.
- Label prototypes clearly, protect access and participant data, and never ship prototype code as production merely because it looks complete.
- Discard or branch failed approaches; preserve what was learned, not every artifact.

GOV.UK requires prototypes before committing to build, recommends choosing the prototype type for the current need, says code prototypes are preferable for realistic interactions, and warns its prototype kit lacks production security and performance features ([Making prototypes](https://www.gov.uk/service-manual/design/making-prototypes)).

#### Prototyping artifacts

- prototype brief: question, risk, audience, fidelity, non-functional limits, and success/failure signal;
- prototype plus scenario, realistic data/content, and state coverage;
- result record linking observed evidence to the next decision.

#### Prototyping exit evidence

- the prototype was evaluated against its question;
- its fidelity and omissions are disclosed;
- the result changes or confirms a documented decision;
- no one can mistake prototype fidelity for production readiness.

### 3.7 Representative-user research

#### Representative-user research practices

- Begin with prioritized research questions and choose a method capable of answering them. Preference questions cannot establish usability; a usability session cannot establish prevalence; a survey cannot reveal unprompted in-context behavior by itself.
- Recruit actual or likely users against behavior and context criteria, including relevant disabled people, assistive-technology users, people with low digital confidence or literacy, and people who need support.
- Use realistic tasks and data. Avoid teaching the interface, leading questions, or asking participants to predict what others will do.
- Obtain informed, voluntary consent; disclose purpose, recording, observers, data use, retention, withdrawal, and controllers/processors; make materials accessible; minimize and protect participant data.
- Record the method, sample, context, tasks, evidence, analysis, limitations, and non-generalizability. Small qualitative studies can reveal severe problems but do not establish statistical prevalence.
- Analyze promptly with observers, preserve contradictory cases, and feed decisions and the backlog.
- Research continuously in small rounds from discovery through live, rather than relying on a single validation event.

GOV.UK says participants must be actual or likely users and recruitment must cover different kinds of users and access needs; its typical 4-8-person range for an interview or usability round is explicitly method-dependent, not a universal sample rule ([finding participants](https://www.gov.uk/service-manual/user-research/find-user-research-participants)). Its research introduction recommends small batches in every development phase ([how research improves service design](https://www.gov.uk/service-manual/user-research/how-user-research-improves-service-design)). Its consent guidance requires informed consent and careful data handling ([getting informed consent](https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research)).

#### Representative-user research artifacts

- research question and method rationale;
- recruitment criteria/matrix and disclosure of gaps;
- ethics, consent, safeguarding, incentives, and data-management record appropriate to risk;
- moderator/activity guide and realistic materials;
- source-indexed observations, findings, limitations, and actions.

#### Representative-user research exit evidence

- participants match the people and contexts implicated by the decision;
- the method can support the claim being made;
- important harms, task failures, accessibility barriers, and contradictory evidence are not averaged away;
- sample limitations are stated; no fixed participant count is used as a ritual gate.

### 3.8 Handoff and implementation assurance

Handoff should be a continuing collaboration and a testable **implementation contract**, not a file transfer.

#### Handoff and implementation practices

- Pair designers, content designers, researchers, and engineers before and during build. Resolve feasibility, data, semantics, responsive behavior, performance, privacy, security, and instrumentation while choices are still cheap to change.
- Define acceptance criteria for behavior and outcomes, not pixel imitation alone.
- Reuse coded components where appropriate and link design instances to their code, version, documented variants, and known limitations.
- Specify all states, content, data rules, focus order/management, keyboard behavior, accessible names and descriptions, status announcements, responsive changes, analytics events, and ownership not already guaranteed by the component or platform.
- Review implemented stories in the browser across relevant viewports, input modes, browsers, assistive technologies, network/data conditions, and realistic content.
- Track differences between intended and implemented behavior as decisions or defects; update the canonical source instead of allowing design and code to drift silently.

The role boundary is explicit: developers advise on feasibility and build accessible software, while the whole team collaborates on a user-centred service ([service-team roles](https://www.gov.uk/service-manual/the-team/what-each-role-does-in-service-team)). WCAG conformance applies to rendered full pages and complete processes, so source design files cannot prove it ([WCAG 2.2 conformance](https://www.w3.org/TR/WCAG22/#conformance-reqs)).

#### Handoff and implementation artifacts

- linked requirements/needs and behavioral acceptance criteria;
- component and pattern map with version and deviations;
- state/content/data/responsive/accessibility/instrumentation specification, preferably close to code;
- implementation decision/delta log;
- review evidence from the built experience.

#### Handoff and implementation exit evidence

- engineering, content, design, accessibility, and analytics owners have accepted their parts;
- critical flows are complete in the integrated implementation;
- design intent and changed decisions are synchronized with code and tests;
- unresolved issues are risk-rated, owned, and visible to the launch approver.

### 3.9 Launch and post-launch iteration

#### Launch and post-launch practices

- Evaluate the integrated service, not only isolated components. Cover complete critical processes and representative page/state/technology samples.
- Complete security, privacy, performance, reliability, content, analytics, accessibility, support, incident, migration, and rollback readiness with the responsible specialists.
- Establish baselines before interpreting change. Monitor task completion and quality, errors, drop-off, support demand, satisfaction or attitudinal signals, accessibility feedback, performance, reliability, and harms by meaningful segments where lawful and ethical.
- Combine behavioral analytics, operational/support evidence, surveys, and ongoing qualitative research. Each explains different aspects; none alone proves that needs are met.
- Keep a feedback and appeal route, triage cadence, experiment/iteration log, and owner for recurring research.
- Re-test changed critical flows and periodically revisit the original need, population, and success definition.

GOV.UK says live work remains based on user research, browser/device and accessibility testing, quality assurance, and performance metrics ([live phase](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works)). W3C recommends integrating accessibility throughout production, evaluating early and regularly, monitoring sites, and incorporating feedback ([Planning and Managing Web Accessibility](https://www.w3.org/WAI/planning-and-managing/)).

#### Launch and post-launch artifacts

- launch evidence pack and accountable risk acceptance;
- WCAG evaluation scope, sample, results, defects, and limitations;
- production dashboard with metric definitions, segments, baselines, guardrails, and owners;
- support/feedback and incident taxonomy;
- learning and decision log linked to the prioritized iteration backlog.

#### Launch and post-launch exit evidence

- complete critical journeys work in production-like conditions;
- the applicable accessibility target has documented evaluation and material issues are fixed or explicitly risk-accepted by authorized humans where legally permissible;
- measurement, feedback, support, incident response, and rollback are operational;
- the owner has reviewed residual risk and chosen launch, limited launch, remediate, or stop.

## 4. Decision gates

These are evidence gates, not phase ceremonies. A small low-risk change may combine several gates; a high-risk service may repeat them per journey, population, or release.

| Gate | Decision | Minimum evidence to pass | Must cause iterate, pivot, or stop |
| --- | --- | --- | --- |
| G0: commission and research readiness | Is the work safe, scoped, and worth investigating? | named owner; decision/problem brief; initial affected populations and harms; existing evidence review; constraints; research question; appropriate consent/privacy/ethics route | no accountable owner; prohibited or unsafe research; solution mandate with no inspectable problem; no access to needed users/evidence |
| G1: problem framing | Is there enough understanding to explore solutions? | evidence-backed, solution-neutral needs; current context/journey; relevant user variation; ranked assumptions; desired outcomes and guardrails; explicit gaps; discovery decision | needs are stakeholder opinions or generated personas; crucial groups/context absent; success undefined; evidence indicates no intervention or a different problem |
| G2: structure and content | Is the service model understandable enough to prototype realistically? | content/task/object inventory; tested or testable IA; real terminology and critical content; source owners; material states; findability/comprehension evidence proportionate to risk | hierarchy mirrors the organization; critical labels/content fail; source of truth or ownership missing; excluded users cannot complete the information task |
| G3: solution direction | Is an approach worth building? | multiple meaningful alternatives; prototype matched to risk; task-based research with representative users; accessibility and feasibility input; trade-off/decision record; no unresolved critical usability or harm issue | only one templated direction; preference voting replaces task evidence; research used proxies or synthetic users; critical task, comprehension, accessibility, feasibility, safety, or trust risk remains unexplained |
| G4: build readiness and implementation assurance | Is intent complete and the integrated build faithful enough to release-candidate test? | component reuse/deviation record; full state/content/responsive/accessibility/data/instrumentation acceptance criteria; engineering pairing; built-browser review; decisions/deltas synchronized | only a design file exists; happy path only; unknown data/content states; semantics/focus/error behavior unspecified; implementation diverges without decision record |
| G5: launch readiness | Should the accountable owner expose the service to its intended population? | complete critical journeys; relevant QA, security/privacy/performance/reliability checks; combined accessibility evaluation; production measurement and support; migration/rollback; residual-risk log and human approval | critical failure or harm; no representative evaluation; automated accessibility score presented as conformance; no support/monitoring/rollback; residual risk has no authorized owner |
| G6: live continuation | Continue, change, scale, limit, or retire? | field metrics against baselines/guardrails; feedback and support evidence; recurring representative-user research; segmented harm/accessibility review; learning log; next decision and owner | metrics are vanity measures; observed harm or exclusion lacks action; material context has changed; evidence no longer supports the original need or solution |

### Gate policy

- Gate evidence is **risk-proportionate**, not document-count-proportionate.
- A gate record must disclose what was not tested, who was not represented, and when the decision expires.
- Critical severity can outweigh frequency. One credible observation of irreversible harm or a complete blocker is not "only one data point."
- Conversely, a handful of sessions cannot establish prevalence, market size, or statistical superiority.
- Numerical thresholds must be specified before evaluation when they are used to make a go/no-go decision; changing them after seeing results requires a recorded rationale.
- Independence should rise with consequence: use specialist or independent review for high-risk accessibility, security, privacy, research ethics, regulated content, or safety claims.

## 5. Evidence standard

### 5.1 Evidence record schema

Every decision-bearing item should contain or link to:

- unique ID and concise claim;
- type: observation, user quote, behavioral/operational data, standard, domain fact, constraint, hypothesis, or decision;
- source/provenance, date, and owner;
- population, sample/recruitment, context, task, method, and materials where people were studied;
- analysis or calculation and versioned query where quantitative;
- supporting and contradictory evidence;
- scope, limitations, uncertainty/confidence, and expiry/review trigger;
- implicated need/risk/requirement;
- decision/action taken, accountable human, and outcome after implementation.

This makes a design rationale inspectable without turning raw personal research data into broadly accessible documentation. Identifiers should link to access-controlled source evidence; summaries should minimize personal data.

### 5.2 Evidence classes and allowed claims

The classes below are a governance vocabulary synthesized for the Steward; they are not a published universal scale.

| Class | Evidence | Claims it may support | Claims it must not support alone |
| --- | --- | --- | --- |
| E0 assumption | stakeholder statement, generated hypothesis, heuristic concern, analogy | what to investigate; a provisional risk | user need, usability, prevalence, conformance, or launch readiness |
| E1 indicative | existing support log, analytics signal, isolated observation, domain input, competitor/desk review | direction of inquiry; possible barrier/opportunity; known constraint or fact within source authority | general behavior/need without context; causal effect; representative preference |
| E2 contextual qualitative | source-indexed interviews/observation with relevant people and contexts; repeated pattern or critical incident; disclosed recruitment and limits | needs, mental models, language, context, mechanisms, severe failure modes | population prevalence, statistical difference, universal persona |
| E3 evaluative | realistic task-based study of prototype or service with representative participants; documented task, behavior, severity, context, and limits | whether and how a design works in tested conditions; iteration priorities | WCAG conformance; population-wide rate; untested users, devices, or conditions |
| E4 quantitative | defined population and metric; valid instrumentation or study design; baseline/comparator; adequate sample/power and uncertainty analysis appropriate to decision | magnitude, trend, segment difference, or causal effect to the extent supported by the design | why behavior occurred without complementary evidence; unmeasured long-term or excluded-population effects |
| E5 assurance/field | specialist evaluation against explicit standard and representative scope; integrated functional/non-functional tests; monitored production behavior | conformance/test result for the declared scope; operational performance in measured conditions | needs of unrepresented people; perfect accessibility or absence of all harm |

Use multiple classes for consequential decisions. For example, launch should join E3 representative task evidence, E5 accessibility/quality/security evidence, and a ready E4/field measurement plan. W3C explicitly says disabled-user evaluation and standards evaluation complement one another ([Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/)).

### 5.3 Accessibility evidence

Use WCAG-EM's durable reporting logic even when a full conformance claim is not being made:

1. define product scope and conformance target;
2. explore technologies, common pages/states, essential functions, page types, and relevant variations;
3. select and record a representative sample plus complete processes;
4. evaluate every applicable success criterion with automation and knowledgeable human methods;
5. report results, examples, methods, limitations, dates, tools/assistive technologies, and evaluator.

WCAG-EM requires documenting scope, exploration, representative sample, complete processes, evaluation, and findings for transparency and replicability ([WCAG-EM](https://www.w3.org/TR/WCAG-EM/)). No aggregate accessibility score should hide individual failures or coverage.

### 5.4 Research evidence

- There is no universal "five users" gate. Participant count follows the question, method, population diversity, consequence, expected incidence, and quantitative power needs.
- Recruit for the decision, not convenience. Disclose missing groups and likely bias.
- For qualitative work, report behaviors and mechanisms plus scope; do not convert counts in a small purposive sample into percentages.
- For quantitative work, define the population, hypothesis, metric, smallest decision-relevant effect where appropriate, sample/power approach, exclusions, multiple comparisons, uncertainty, and guardrails with a performance analyst or researcher.
- Do not use satisfaction alone as task success. Pair what people say with what they do and operational outcomes.
- Preserve negative, null, and contradictory findings. A decision log should show why evidence was accepted, rejected, or superseded.
- Consent is ongoing and withdrawable; research data use must remain within the consent and approved retention/access model ([GOV.UK informed consent](https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research)).

## 6. Controls against formulaic AI-generated work

AI can accelerate drafting, enumeration, comparison, prototyping, and checking. It must not lower the evidence bar or become a source of users, facts, taste, or accountability.

Doshi and Hauser found that generative-AI assistance improved individual story evaluations while making outputs more similar to one another in their experiment ([Science Advances, 2024](https://doi.org/10.1126/sciadv.adn5290)). Because that study concerned short stories, not web products, the correct response is a **precautionary control against convergence**, not a claim that every AI-assisted interface is homogeneous. NIST's AI RMF requires documented human-AI roles and oversight, context and limits, representative human-subject evaluation, testing in deployment-like conditions, independent or external input where appropriate, and production monitoring ([AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)).

The Steward should enforce these controls:

1. **AI output is a hypothesis, never evidence.** Generated personas, interviews, quotes, analytics, competitive claims, accessibility claims, and citations are marked synthetic until a human verifies them against owning sources or real participants. Synthetic users never count toward research coverage.
2. **Ground before generating.** Give approved tools an evidence pack containing the decision, real user language, content, domain constraints, accessibility target, existing system, brand principles where supplied, and known anti-patterns. Do not upload personal or confidential research data unless policy, consent, and tool terms permit it.
3. **Diverge structurally.** Require alternatives that change the information model, task sequence, disclosure, control model, or content strategy. Cosmetic variants do not satisfy divergence. Include a human-originated or non-AI baseline where feasible.
4. **Generate independently before showing exemplars.** Early exposure to one polished output can anchor subsequent work. Collect independent sketches or prompts, then compare. Preserve rejected directions and why they failed.
5. **Run a sameness review.** Compare alternatives for repeated layout skeletons, generic copy, fashionable surface treatments, stock imagery, uniform tone, default component combinations, and unsupported "best practice." For every major choice ask: which need, context, evidence, system rule, or deliberate identity principle makes this appropriate here?
6. **Use real content and hostile states.** Replace placeholder text and ideal data with actual terminology, long/short/localized content, errors, empty/loading/offline states, permissions, sensitive disclosures, destructive actions, and assistive-technology behavior before evaluation.
7. **Reuse patterns with provenance.** Record whether an output uses a standard, design-system component, observed competitor convention, model invention, or team decision. Verify licenses, provenance, accessibility, and production suitability. NIST calls for documenting third-party software/data and intellectual-property risks ([AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)).
8. **Keep a named human editor and decision owner.** A qualified designer/content specialist selects, combines, revises, and signs the rationale; the product/service owner accepts outcome and residual risk. "The model chose it" is not a rationale.
9. **Require independent critique on consequential work.** Review without the prompt or generation narrative where possible so polish and automation do not inflate confidence. Include research, content, engineering, accessibility, data, security/privacy, and domain perspectives as risk requires.
10. **Test with representative real users and the built system.** No prompt score, model self-critique, synthetic panel, aesthetic benchmark, heuristic checklist, or design-file plugin can establish need, comprehension, usability, accessibility, trust, or field performance.
11. **Record AI use and uncertainty.** Log model/tool/version where material, inputs and protected-data status, generated portions, human verification, sources, known limitations, and decisions changed. This supports later review when models or policies change.
12. **Monitor for convergence and harm after launch.** Track user language mismatch, exclusion, support demand, accessibility feedback, and performance by meaningful segment; create a route for users and impacted people to report problems. NIST explicitly calls for end-user feedback integrated into evaluation and production monitoring ([AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)).

## 7. What requires human judgment or real users

| Activity | AI/automation can assist | Required human judgment | Real users required? |
| --- | --- | --- | --- |
| Discovery and contextual inquiry | inventory sources, draft questions, summarize verified material | qualified researcher chooses method, recruits, consents, moderates, protects participants, interprets context | **Yes** for claims about needs, behavior, barriers, or context; actual/likely users, not synthetic personas |
| Synthesis | transcription, search, candidate clustering, trace links | researchers/team distinguish observation from interpretation, resolve contradictions, judge significance and harm | **Source evidence must come from real people/field data**; AI clustering cannot create a finding |
| IA | inventory, candidate taxonomies, test administration and calculations | IA/content judgment about domain model, labels, governance, and trade-offs | **Yes** for claims about user grouping, language, findability, or comprehension |
| Content | draft variants, consistency and known-rule checks | content designer owns clarity; domain/legal/policy/localization owners validate claims; accessibility specialist advises | **Yes when comprehension, trust, action, or risk is material**; always use real user language/evidence |
| Interaction design | enumerate states and alternatives, prototype routine behavior | designer owns model, sequence, feedback, recovery, and comparative rationale; engineer owns feasibility | **Yes** to claim usability or task success |
| Visual design | generate mood/direction candidates, token calculations, contrast pre-checks | skilled human owns hierarchy, identity, cultural meaning, craft, and appropriateness | **As risk requires** for comprehension, trust, inclusion, desirability, or task impact; user preference is not sole authority |
| Prototyping | draft screens/code/data and variations | designer/engineer chooses fidelity and ensures the prototype can answer the question safely | **Yes** when the prototype is used to claim user behavior, comprehension, or usability |
| Representative-user research | logistics, approved transcription, analysis aids | researcher owns ethics, sample, method, moderation, analysis, limitations | **Always**; a simulation can rehearse a plan but is not participant evidence |
| Accessibility | static linting, automated scans, calculations | knowledgeable human evaluates requirements and implementation; disabled people contribute lived-use evidence | **Yes, with relevant disabled users**, plus standards evaluation; each covers what the other cannot |
| Handoff/implementation | generate annotations/tests and detect drift | engineers decide architecture/semantics; designers/content specialists inspect fidelity; QA evaluates behavior | **Built-system testing with users is required** for usability claims; specialist tests are still required |
| Measurement/experiments | instrument, compute, visualize | analyst defines valid measures/design and uncertainty; owner interprets trade-offs and guardrails | **Yes in the field or study population**; simulated behavior is not a product outcome |
| Prioritization, risk acceptance, launch | summarize options and evidence | accountable product/service owner, advised by relevant specialists | User evidence informs the decision, but users do not carry organizational accountability |

W3C's accessibility guidance is especially clear about this boundary: knowledgeable human evaluation is required because tools cannot determine accessibility, while input from a limited set of disabled users cannot be generalized or treated as WCAG conformance ([evaluation overview](https://www.w3.org/WAI/test-evaluate/), [involving users](https://www.w3.org/WAI/test-evaluate/involving-users/)).

## 8. Durable practice versus adaptable methods and trends

### Durable invariants to encode

- human-centred work across the lifecycle;
- an evidenced, solution-neutral problem and outcome;
- continuous contact with representative real users;
- multidisciplinary specialist roles and named human accountability;
- explicit assumptions, risks, alternatives, decisions, and residual uncertainty;
- traceability from source evidence to need to requirement to implementation to outcome;
- divergent exploration followed by evidence-based convergence;
- realistic content, data, context, states, and complete journeys;
- accessibility integrated early and evaluated with standards, knowledgeable humans, tools, and disabled users;
- prototype fidelity selected by question and risk;
- collaboration through implementation and inspection of the built experience;
- outcome measurement, feedback, iteration, and retirement;
- ethical research, privacy, security, and data minimization.

These remain stable even when team titles, tools, phase names, or aesthetics change. They are consistent with lifecycle HCD in ISO 9241-210, nonlinear people-centred iteration in the Design Council framework, the multidisciplinary GOV.UK service model, and W3C's standards/evaluation model.

### Adaptable methods, useful only when they answer a question

- Double Diamond, discovery/alpha/beta/live, design sprints, or another phase vocabulary;
- interviews, contextual observation, diary studies, surveys, card sorting, tree testing, usability tests, experiments, or analytics;
- personas, jobs-to-be-done statements, journey maps, service blueprints, story maps, canvases, wireframes, or design histories;
- HEART or another metric taxonomy;
- low-, medium-, or high-fidelity prototypes;
- component libraries, design tokens, naming systems, design-file conventions, and handoff tools;
- a typical participant range for a qualitative round.

The Steward chooses among these based on the decision, risk, users, evidence already available, and cost. It must not mandate an artifact merely because a methodology diagram contains it.

### Trends that must never become evidence or defaults

- a fashionable visual treatment, layout archetype, animation style, or tone;
- a chat, assistant, copilot, personalization, or AI feature without a validated need and failure model;
- prompt-to-interface generation as a substitute for discovery, architecture, content, or research;
- AI-generated personas or synthetic panels represented as users;
- a tool-specific component structure treated as product architecture;
- a polished high-fidelity prototype treated as proof of feasibility, accessibility, or usability;
- a single score, benchmark, award, stakeholder vote, or social-media aesthetic treated as outcome evidence.

Trends may be explored as hypotheses. They pass only through the same user, accessibility, feasibility, identity, risk, and field-evidence gates as any other choice.

## 9. Minimal reusable artifact set

The reusable system should provide schemas, not force separate documents. A team can maintain these as linked records in its existing tools.

1. **Decision brief:** decision, problem/outcome, people/context, evidence, constraints, scope, owner, deadline.
2. **Evidence register:** the schema in section 5, with controlled links to raw data.
3. **Assumption/risk register:** consequence, uncertainty, affected groups, test, owner, status, residual risk.
4. **Research record:** questions, method, recruitment, ethics/consent/data handling, materials, observations, findings, limitations, actions.
5. **Experience model:** only the necessary current/future journey, service blueprint, system map, IA, content/object model, and ownership relationships.
6. **Design record:** meaningful alternatives, real content/data, state model, pattern reuse/deviation, accessibility and responsive intent, rationale.
7. **Prototype record:** question, fidelity, omissions, scenario, result, decision.
8. **Implementation contract:** needs/requirements, behavioral acceptance criteria, content/data/states, components, semantics, instrumentation, tests, deltas.
9. **Gate/decision log:** evidence reviewed, dissent, decision, accountable human, residual risk, expiry/revisit trigger.
10. **Live learning record:** metric definitions/baselines/guardrails, feedback and incident themes, research, changes, outcomes, next decision.

## 10. Recommended acceptance tests for the Design Steward itself

A future Design Steward should fail its own output unless all applicable statements are true:

- Every claimed user need resolves to research or field evidence; otherwise it is labeled an assumption.
- Every cited claim links to the source that owns it, not a secondary summary.
- The affected population, recruitment gaps, method, context, and limitations are visible.
- No synthetic participant, persona, quote, metric, or AI-generated citation is presented as real evidence.
- At least two meaningfully different approaches were considered for a material open-ended design decision, or the record explains why a proven pattern made divergence wasteful.
- Every major design choice has a user/context/evidence/system/accessibility/identity rationale, not "best practice" or model preference.
- Critical journeys contain realistic content/data and applicable error, recovery, responsive, keyboard, focus, assistive-technology, loading, permission, and destructive states.
- The current accessibility target is named; automated and human methods, disabled-user coverage, scope, complete processes, results, and limitations are recorded.
- Research and metric claims do not outrun their methods; small qualitative counts are not percentages and observational analytics are not causal proof.
- Named humans own research integrity, content truth, design judgment, engineering feasibility, specialist risk, metrics, and launch.
- The implemented experience was inspected; a design file is not release evidence.
- The launch has measurement, support/feedback, incident, rollback, and review ownership.
- AI assistance, protected-data handling, provenance verification, and human edits are disclosed when material.
- Gate outcomes can be proceed, iterate, pivot, or stop; the system does not reward artifact completion or predetermined launch.

## 11. Source assessment and limitations

### Primary-source inventory

| Source | Why it is authoritative here | Contribution | Limitation |
| --- | --- | --- | --- |
| [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) | international standard owned by ISO | human-centred design activities throughout an interactive system lifecycle | public page exposes the abstract, not the paid full text; this report does not attribute details beyond the public scope |
| [Design Council Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/) | first-party source from the creator of the Double Diamond | divergence/convergence, nonlinearity, people, collaboration, iteration | framework, not a conformance standard or empirical proof of a specific method |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) and [Government Design Principles](https://www.gov.uk/guidance/government-design-principles) | first-party operating guidance for professional government digital-service teams | role boundaries, discovery/alpha/live gates, continuous/inclusive research, prototyping, patterns, content, performance | government-specific "must" statements and phase labels are adapted here into reusable risk-based controls, not universal law |
| [GOV.UK content and publishing guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/) | current first-party publishing practice | task-based content needs, evidence, acceptance criteria, ownership | written for GOV.UK content; local voice, regulatory, and domain rules still apply |
| [Digital.gov research guidance](https://digital.gov/guides/research-collaboration/testing/organization) | first-party U.S. federal digital practice | operational card sorting and related evaluation methods | a method guide, not proof that a method is suitable for every IA decision |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | W3C Recommendation, normative web accessibility standard | testable success criteria and conformance requirements for full pages/processes | WCAG does not cover every need of every disabled person and is not a usability study |
| [W3C accessibility evaluation guidance](https://www.w3.org/WAI/test-evaluate/) and [user-involvement guidance](https://www.w3.org/WAI/test-evaluate/involving-users/) | first-party W3C/WAI guidance | tools require knowledgeable human evaluation; disabled users and standards evaluation complement each other | informative guidance; organizational legal obligations may add requirements |
| [WCAG-EM](https://www.w3.org/TR/WCAG-EM/) | W3C Working Group Note | evaluation scope, representative sample, complete processes, documented results | sampling evaluates a declared scope; it cannot justify broader claims than its coverage |
| [HEART paper](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) | original CHI 2010 publication by the framework authors | user-centred metrics and Goals-Signals-Metrics mapping | taxonomy and examples came from Google; metrics still require local validity and complementary qualitative evidence |
| [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | first-party U.S. standards-body framework | documented AI roles, human oversight, representative evaluation, deployment-like tests, feedback, and monitoring | voluntary general AI-risk framework, not a product-design method or legal opinion |
| [Doshi and Hauser, Science Advances 2024](https://doi.org/10.1126/sciadv.adn5290) | original peer-reviewed experiment | evidence that AI assistance can increase individual evaluations while reducing collective output diversity in the studied setting | story-writing task; it motivates convergence controls but does not establish an effect size for web design |

### Limits of this report

- The evidence base emphasizes formal web standards and public-sector digital-service practice because they publish unusually explicit first-party methods, roles, and gates. The transferable principles are separated from government-specific mandates, but commercial teams should map them to their own governance and risk.
- No universal artifact list, participant count, phase model, or metric set is evidence-backed for every product. This report deliberately makes them conditional on the question and risk.
- WCAG is a baseline for testable web accessibility, not a complete model of usability, disability inclusion, or applicable law. Teams must identify jurisdictional, contractual, organizational, and sector-specific requirements.
- Original evidence on AI-assisted professional web design remains emerging and tool-dependent. The anti-formula controls combine a narrow empirical homogenization signal with NIST governance requirements and durable HCD practice; they should be measured and updated rather than treated as settled effect estimates.

## Conclusion

The professional core of a Design Steward is disciplined humility: know what is evidence, what is inference, what is merely generated, who has authority, which risk the team is retiring, and what remains unknown. Operationalize user contact, specialist collaboration, standards, traceability, alternatives, realistic prototypes, implementation inspection, and live learning. Keep tools, artifacts, phase labels, visual styles, and AI techniques replaceable. Keep accountable humans and representative real users indispensable.
