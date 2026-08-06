# Evolution redesign direction

Preserve familiarity, but do not treat every undocumented legacy convention as permanently fixed. That would make the redesign cosmetic, preserve accidental complexity, and transfer unresolved decisions into the new UI. Instead, use legacy behavior as the default hypothesis: retain it unless evidence shows that it harms comprehension, accessibility, consistency, or task completion.

## Product principle

Modernize the visual system and interaction quality while keeping users’ mental model, terminology, information architecture, and core workflows recognizable. Changes should feel like the same product becoming clearer and faster—not a different product users must relearn.

## What stays stable

- Core navigation destinations and major task sequences
- User-facing terminology unless it is demonstrably ambiguous
- Location of high-frequency actions where muscle memory matters
- Existing data, permissions, saved states, and keyboard workflows
- Expected outcomes, including validation and recovery behavior

## What can evolve

- Typography, spacing, color, iconography, and component consistency
- Visual hierarchy, density controls, responsive behavior, and accessibility
- Feedback states, error guidance, progressive disclosure, and empty states
- Redundant steps, unclear labels, and inconsistent patterns—after validation

## Decision framework

Create a lightweight convention register during discovery. For each legacy pattern, record its purpose, affected users and workflows, observed evidence, risk of change, and provisional owner. Classify it as:

1. **Preserve** — familiar, effective, or operationally critical.
2. **Modernize in place** — behavior stays; presentation or feedback improves.
3. **Validate** — intent is unclear or evidence conflicts.
4. **Retire** — demonstrably harmful, redundant, or inaccessible.

Absence of a source or owner is not evidence that a convention is sacred. For speed, assign a product owner and design owner for the redesign, maintain a short decision log, and time-box disputed items rather than silently freezing them.

## Delivery approach

Start with a representative end-to-end workflow and establish the updated design system around it. Prototype both common and failure states, test with experienced and newer users, and compare completion, errors, confidence, and time-on-task against the current product. Release incrementally behind a reversible rollout, monitor support signals and behavioral metrics, then expand only after the pilot meets agreed thresholds.

Success means users can complete familiar work without retraining while experiencing clearer hierarchy, stronger accessibility, fewer inconsistencies, and faster recovery from mistakes.
