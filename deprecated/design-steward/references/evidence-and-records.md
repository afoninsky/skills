# Evidence and records

## Evidence ladder

Label every material claim with the strongest supporting level:

- **E0 — Assumption or generated hypothesis:** stakeholder belief, agent analysis, generated direction, generated specialist or critic review, ungrounded heuristic inspection, synthetic user, generated persona, or simulated journey.
- **E1 — Indicative or expert input:** qualified-human specialist review, inspectable established-practice audit, analogous precedent, or exploratory signal without representative context. A model adopting a specialist role does not become E1 by naming itself an expert.
- **E2 — Contextual qualitative:** observed or reported evidence from relevant contexts with documented recruitment and limitations, but not yet representative enough for an evaluative claim.
- **E3 — Representative-user evaluative:** task or comprehension evidence from a justified representative sample, including relevant disabled users where applicable.
- **E4 — Quantitative or experimental:** appropriately instrumented behavior, experiment, or statistical evidence with population, denominator, segmentation, and uncertainty.
- **E5 — Assurance or field evidence:** production-like or live integrated assurance across relevant journeys and specialist domains.

Evidence levels are not a universal ranking of value. Match the method to the claim. Do not upgrade a claim because several weak sources agree.

A static `web-design-guidelines` review is E1 specialist/heuristic input. Record the inspected implementation revision, authorized paths and exclusions, immutable guideline revision when available, retrieval URL and time, SHA-256 content hash, findings, limitations, and remediation status. It cannot establish representative usability, accessibility certification, runtime behavior, engineering approval, or release readiness. If current rules cannot be retrieved and verified, record the audit as not run and required coverage as **Not yet evidenced**.

## Claim language

Record a stable claim ID, linked requirement and applicable assumption IDs, claim owner, population, context, task, artifact or release, method, date, limitations, and evidence ID. Use language such as:

- “E0 generated design review judged…”
- “E1 qualified specialist review found…”
- “E2 interviews suggest a hypothesis that…”
- “E3 task evidence supports this journey for the recruited population…”
- “E4 production analysis observed…”

Use “validated” only for a narrow claim supported by representative-user or production evidence. Never say that a whole design, product, or population is validated without matching evidence.

## Non-compensable gates

Track each as Pass, Fail, or Not yet evidenced:

1. **Accessibility:** default to WCAG 2.2 AA unless the brief requires stricter; include automated and manual evaluation, keyboard operation, semantics, zoom/reflow, contrast, motion, and relevant disabled-user evidence.
2. **Content truth:** verify terminology, instructions, states, consequences, error recovery, and domain claims with accountable content or domain owners.
3. **Privacy and participant welfare:** minimize collection, authorize access, protect consent and withdrawal, restrict raw data, and prevent inappropriate joins or reuse.
4. **Ethical UX and safety:** reject deception, coercion, hidden consequences, exploitative engagement, unsafe defaults, or blocked appeal and recovery.
5. **Provenance and AI use:** identify sources, tools, generated content, transformations, rights, limitations, and human review.

Do not permit a score, preference, schedule, or System Owner decision to convert a failure into a pass. Preserve the objection and escalate or stop.

Record exactly one status for each applicable hard gate. Use **Fail** when supplied or collected evidence demonstrates a violation, even when approval or review is also missing. Use **Not yet evidenced** only for the separate absent or incomplete method, reviewer, artifact, or result. Neither state passes, but preserve both facts without relabeling the observed violation as missing assurance.

## Design record graph and evidence diet

Maintain engagement-local records with stable typed IDs and explicit links, but default to the smallest set that preserves authority and decisions:

- one required `steward-state.json` recovery spine containing every material decision and exact resumption state;
- engagement header and record index;
- confirmed Owner Design Brief, normalized brief versions, and requirement records;
- evidence register and research records;
- assumptions, risks, and constraints;
- experience structures, direction charters, artifacts, and prototypes;
- one living delegation ledger with bounded return envelopes; use standalone packets only when sensitivity, complexity, or handoff risk warrants them;
- gate reviews, decisions, dissent, and supersession;
- implementation contract and delta log;
- live-learning hypotheses, changes, measures, and closure.

Use **Draft**, **Reviewed**, **Accepted**, **Superseded**, or **Retired**. Never overwrite an accepted decision; supersede it and link both records.

IDs are immutable. Link records by stable IDs, not headings or row positions. Supersession creates a new ID plus forward and backward links; it never mutates the accepted record.

Do not create a separate record for status commentary, every retry, repeated successful checks, each screenshot, a hash already present in the artifact manifest, or an agent correction that does not change authority, evidence, the frozen artifact, a gate decision, or an implementation delta. Artifact count is not traceability. Preserve the decision path without burying it.

The state file is current and append-aware rather than immutable: update current fields, preserve superseded decisions through links and statuses, and point to accepted detailed records. No other record may be the sole location of a decision required to resume. Regenerate `steward-roadmap.html` from the state file at completion or on Owner request; never edit the generated roadmap as evidence.

## Sensitive data boundary

Keep raw recordings, transcripts, contact details, screeners, identifiers, sensitive analytics, and regulated material in an authorized restricted system. Put only minimized findings, opaque evidence IDs, access classification, retention rule, provenance, and approved excerpts in the design record.

Do not copy product or participant data into this skill, agent memory, public branches, or generic service prompts.

## Live learning loop

For each post-launch signal:

1. collect through an approved route;
2. classify population, journey, severity, evidence level, and potential harm;
3. triage with accountable owners;
4. create a falsifiable hypothesis and guardrails;
5. record the decision and approved change;
6. verify instrumentation and measure;
7. close, iterate, pivot, roll back, or retire with evidence.

Link every change back to the affected brief, decision, requirement, direction, and residual-risk owner. Keep engagement learning local; update the portable core only through an explicit public, product-neutral release decision.
