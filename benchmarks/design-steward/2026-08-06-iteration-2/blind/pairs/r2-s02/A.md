# Evolution redesign recommendation

I would not treat every legacy convention as permanently fixed. With no source or decision owner, “fixed” is an unverified assumption—not a product requirement—and it prevents meaningful modernization. The fast, safe interpretation is: preserve users’ learned workflows and outcomes while allowing presentation and implementation details to evolve.

## Guardrails

Keep fixed for the first release:

- Information architecture, core task order, terminology, and feature availability
- Existing data, permissions, shortcuts, URLs, and back-button behavior
- Placement of high-frequency or high-risk actions unless evidence supports a move
- Accessibility and platform conventions at least at their current level

Allow to change:

- Typography, spacing, color, icon treatment, elevation, and component consistency
- Responsive behavior, empty/loading/error states, and visual hierarchy
- Redundant decoration and inconsistent one-off styling

## Fast execution

1. Create a one-page convention inventory from the current product, classifying each item as **workflow**, **meaning**, or **presentation**. Record unknowns explicitly; do not silently convert them into requirements.
2. Define a small visual system and apply it to one representative, high-traffic journey. Preserve labels, task sequence, and action locations in this pilot.
3. Compare old and new versions using task completion, time on task, error/reversal rate, accessibility checks, and qualitative “where did you expect this?” feedback.
4. Ship behind a reversible rollout with analytics and support monitoring. Expand only if the pilot meets the agreed thresholds.

## Decision rule

If a convention affects recognition, task sequence, data meaning, or recovery from mistakes, preserve it until validated. If it is purely visual and does not change comprehension or behavior, modernize it now. Ambiguous cases go into a short decision log with a temporary owner and review date.

The first release is complete when the representative journey retains functional parity, introduces no critical accessibility regressions, and does not materially worsen completion, errors, or support contacts. This keeps the redesign evolutionary without preserving accidental complexity forever.
