# Directions and artifacts

## Independent direction protocol

Default to three directions. Reduce this only before generation with a Product Owner-approved rationale tied to scope, risk, or resources.

Freeze a shared baseline before work begins:

- approved brief version;
- evidence and requirement IDs;
- representative content and hostile states;
- Fixed and Challengeable constraints;
- hard gates and comparison rubric;
- evidence thresholds and uncertainty handling;
- one distinct structural charter per direction.

Give each direction the same baseline but an isolated context. Do not reveal sibling solution forms, layout, interaction, content framing, or visual choices before freeze. Route factual corrections through the Steward without leaking solutions.

When visual development is warranted, use one fresh `frontend-design` specialist sub-agent per direction under [specialist-capabilities.md](specialist-capabilities.md). Supply only that direction's authorized context and Open visual axes. Freeze its traced visual thesis and system before any sibling output or cross-critique is visible.

Make charters structurally distinct. Examples of structural differences include task-first versus object-first navigation, guided versus direct manipulation, progressive disclosure versus overview-first, or centralized versus contextual control. Color, typography, spacing, and ornament alone do not create distinct directions.

Use realistic content, error, empty, loading, partial-permission, long-text, localization, low-bandwidth, and keyboard-only states. Record which Working Assumptions each artifact depends on.

## Precedent protocol

Use high-trust primary or first-party sources when citing professional precedent. Record:

- stable source and observed date;
- original context and intended population;
- principle abstracted from the source;
- rights or license considerations;
- transformation into the current direction;
- limitations and reasons the precedent may not transfer.

Do not reproduce a surface, brand language, proprietary asset, or interaction merely because it is familiar.

## Fidelity ladder

Choose the lowest fidelity that can answer the current risk:

| Question | Preferred artifact | Portable review form |
| --- | --- | --- |
| Journey, dependency, state, or information structure | Mermaid source | SVG or PDF |
| Rough spatial or interaction alternative | Excalidraw JSON | SVG |
| Shared editable interface design | Penpot when open/self-hosted control matters; Figma when explicitly authorized and organizationally standard | Structured export plus static review |
| Responsive behavior, keyboard flow, semantics, motion, accessibility, or feasibility | Disposable HTML/CSS/JS; add Storybook or Playwright when useful | Runnable local artifact plus captures or test output |
| Decision and approval surface | Markdown or HTML | Stable Markdown, HTML, or PDF |

Every artifact must include:

- stable artifact ID and version;
- decision question and intended audience;
- linked brief, requirement, evidence, assumption, direction, and gate IDs;
- editable source;
- portable review/export;
- provenance, rights, and tool/AI disclosure;
- fidelity limitations and unsupported claims;
- open fallback or migration route.

Treat tool names as replaceable implementation choices. Never make a service account or proprietary format the sole durable record.

## Freeze, critique, and comparison

Before cross-critique:

1. freeze each direction's thesis, rationale, content, states, and artifacts;
2. verify baseline parity;
3. run a sameness review for shared layout skeletons, interaction logic, content hierarchy, and visual grammar;
4. revise or reject directions that are merely themed variants.

After freeze, obtain adversarial cross-critique from relevant specialists. Keep the original thesis visible when requesting revisions.

Evaluate hard gates before scoring. Disqualify unresolved critical failures in accessibility, content truth, privacy or participant welfare, ethical UX or safety, or provenance. Scores and Product Owner preference cannot compensate.

Compare surviving directions against the precommitted rubric. Separate observed evidence, specialist judgment, Product Owner preference, implementation estimate, and Steward inference.

## Synthesis

Choose one coherent structural backbone. Import an element from another direction only when:

- it addresses a documented weakness or requirement;
- it is compatible with the backbone's mental model and interaction grammar;
- evidence or specialist reasoning supports it;
- its dependencies and consequences are recorded;
- the resulting synthesis is retested against hard gates and the rubric.

Do not average, vote, collage, or include one element from each direction for representational fairness.

## Prototype boundary

Mark prototype code as disposable design evidence. Keep it outside production modules and credentials. Do not silently promote it into production. End design handoff with an implementation contract that describes intended behavior, semantics, content and data rules, responsive states, accessibility intent, instrumentation, acceptance criteria, and known limitations.
