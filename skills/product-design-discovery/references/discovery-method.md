# Discovery method

## Proportional depth

Match effort to uncertainty and consequence:

- **Local UX question:** inspect the affected flow, content, states, and target constraints; amend only the relevant brief sections.
- **New small product:** define primary users, one priority journey, surface/state inventory, content model, platform constraints, and explicit assumptions.
- **Consequential or multi-role product:** add failure/recovery paths, role handoffs, privacy/safety boundaries, representative research plan, and evidence thresholds.
- **Existing fragmented product:** discovery defines user/flow truth; visual inconsistency belongs to `product-design-review` and system authority to `product-design-contract`.

Do not use a fixed questionnaire or artifact count. A concise complete decision contract is better than a large form filled with guesses.

Activate only lenses that can change the decision: audience and development; behavior, attention, and ethics; domain and task; business model and trust; category patterns; or safety, culture, law, accessibility, and platform behavior. For minors, vulnerable people, or persuasive-attention requests, treat welfare and informed voluntary control as consequential; time spent or compulsion is not a default product outcome.

## Material-question test

Ask a question only when different plausible answers change one of:

- primary user or job;
- priority journey or navigation;
- information/content hierarchy;
- business model, trust, category convention, or differentiation;
- safety, privacy, legal, accessibility, or welfare handling;
- platform, input, device, or localization coverage;
- scope, authority, evidence threshold, or rejection criterion.

State a reversible assumption instead when the answer can be cheaply tested later. Stop on a blocking unknown when guessing could harm people, invalidate the product, or materially waste implementation effort.

## Core framing

Use plain product language:

- **Situation:** when and where the need occurs.
- **Job:** progress the person is trying to make.
- **Outcome:** observable result, not a feature list.
- **Core act:** the action the product must make unusually clear and trustworthy.
- **Early comprehension:** what must become clear, and at what point in the journey, for the task to proceed safely.
- **Rejection criterion:** visible condition proving the design failed.

Separate roles when their information, permissions, consequences, or mental models differ. Model the handoff between roles rather than merging them into a generic “user.”

## Flow and IA procedure

1. Start from an entry trigger, not a screen list.
2. Trace the shortest successful path to outcome.
3. Add decision points, role boundaries, prerequisites, and exits.
4. Add interruption, retry, cancellation, permission denial, and recovery where plausible.
5. Add return journeys: what the person sees tomorrow or after another role acts.
6. Convert the flow into surfaces only after the behavior is coherent.
7. Test every global destination and visible control against a real job; do not invent navigation to fill a shell.

## Content-first inventory

Use realistic nouns, labels, amounts, dates, names, statuses, errors, and actions. Capture extremes:

- shortest and longest plausible copy;
- zero, one, and many items;
- stale, partial, delayed, or conflicting data;
- first use and returning use;
- destructive or irreversible actions;
- unsupported/offline/permission states;
- translation expansion and right-to-left layout when relevant.

Content is part of the design contract. Placeholder prose can conceal hierarchy and state failures.

## UX quality lenses

Use these as critique questions, not automatic scores:

- Can a person identify the core act soon enough for this task and context?
- Does the structure still work if brand labels are replaced with generic terms?
- Does each role understand what happened and what happens next?
- Is recovery as clear as success?
- Does the experience preserve dignity and informed control?
- Can the same task survive small screens, large text, keyboard/touch input, localization, and assistive technology?
- Which assumption would most change the flow if false?

## Decision-ready handoff

Show only what the next design decision needs:

1. one-paragraph brief;
2. priority journey and surface/state coverage;
3. fixed/challengeable/open decisions;
4. top evidence, design implications, and material limitations;
5. blocking unknowns and working assumptions;
6. any material question that still needs the owner, or the smallest useful next design phase when none does.

The user's original request may already authorize continuation. Ask for approval only when an unresolved decision would materially change scope, behavior, safety, evidence, or production work. Discovery never selects visual style, mutates production, or approves a visual baseline.
