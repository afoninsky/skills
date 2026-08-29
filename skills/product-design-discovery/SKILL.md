---
name: product-design-discovery
description: Clarify users, jobs, journeys, information architecture, content, states, and platform constraints before visual or production work. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. Do not choose visual direction or edit production UI.
compatibility: Uses repository and product evidence already available. Web research, participant research, and runtime inspection are conditional on the question being answered; no particular SaaS or MCP server is required.
---

# Product Design Discovery

Create the smallest trustworthy understanding that lets design proceed without guessing. Focus on what people need to accomplish, the conditions around that work, and the decisions later design must honor.

## Scope

Discovery may inspect the existing product and create or update research, brief, flow, content, and state artifacts within the authorized design-artifact scope. It does not select an aesthetic, edit production UI, recruit participants, enable analytics, spend money, or claim human acceptance.

If existing evidence already answers the question, reuse it. Update only gaps that matter to the request; do not create a parallel brief, repeat settled research, or reopen fixed decisions without evidence.

## Practice

1. **Frame the decision.** Name the outcome this work must enable, affected people, product stage, target platforms, fixed constraints, and failure costs. Separate fixed decisions, evidence-backed challengeable decisions, open questions, and reversible working assumptions.
2. **Inspect before asking or researching.** Read the supplied material, product language, source, tests, prior research, support signals, and current runtime when available. Understand why current behavior exists before labeling it accidental. Ask only for missing information that could materially change the design.
3. **Research relevant gaps.** Browse when the work involves an unfamiliar audience or domain, safety, culture, accessibility, law, current platform behavior, or another consequential unknown. Prefer primary research, standards, official platform guidance, and authoritative domain organizations. Record the design implication, date when relevant, confidence, and limitation. Stakeholder opinion, analytics, participant observation, and agent inference remain distinct evidence types.
4. **Model the experience.** Define the primary and secondary roles, priority situations and jobs, core act, entry and completion, alternate and recovery paths, navigation relationships, content hierarchy, and applicable loading, empty, error, offline, permission, interrupted, destructive, and success states.
5. **Cover real conditions.** Consider representative screen or window sizes, orientation, safe areas, keyboard/pointer/touch, text scaling, localization, assistive technology, privacy, and content extremes when they can affect the experience. Use a text flow or rough wireframe when structure—not visual style—is the question.
6. **Synthesize the minimum useful artifact.** Adapt the repository's conventions. A concise brief and experience map are usually enough; use the templates in `assets/` only when they help. State assumptions and exclusions instead of filling sections with invented detail.

Participant research requires representative people and appropriate consent. Synthetic personas, agent critique, or simulated interviews can generate hypotheses but never count as user validation. External writes, participant contact, or paid research require explicit authority.

Read [discovery method](references/discovery-method.md) for substantial research or synthesis. Read [evidence and platform coverage](references/evidence-and-platform-coverage.md) for multi-platform, runtime, participant, or consequential evidence claims. Use [tool preflight](references/tool-preflight.md) only when a needed research, runtime, or artifact capability is uncertain.

## Definition of done

- The brief states the intended outcome, people and context, core task, priority journey, important states, constraints, and rejection criteria at useful fidelity.
- Fixed decisions, evidence, assumptions, inferences, contradictions, and unresolved questions remain distinguishable.
- Audience- or domain-specific claims are supported by credible sources or clearly labeled as assumptions.
- Every material role, surface, state, and target is covered, explicitly excluded, or recorded as a gap.
- Existing visual direction, production behavior, accepted references, and baselines are unchanged.
- The handoff says what decision is now possible, what remains uncertain, and whether direction, contract, prototype, implementation, or review is the smallest useful next step.
