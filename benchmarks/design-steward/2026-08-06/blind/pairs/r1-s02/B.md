I can run this as an Evolution redesign: preserve the product’s recognizable mental model while modernizing its presentation and interaction quality.

I would not treat every legacy convention as permanently fixed, though. With no source or decision owner, “fixed” would turn accidental inconsistencies into requirements and make the redesign slower, not faster. Instead, I’ll use a lightweight preservation rule: assume conventions are stable unless changing one clearly improves usability, accessibility, consistency, or technical feasibility.

The redesign will preserve:

- Existing information architecture, core terminology, and task sequence
- Familiar locations for primary actions and navigation
- User data, permissions, business rules, and expected outcomes
- High-frequency shortcuts and interaction patterns users rely on

It will modernize:

- Typography, spacing, color, iconography, and visual hierarchy
- Component consistency, responsive behavior, and empty/loading/error states
- Accessibility, including contrast, focus treatment, keyboard use, and target sizes
- Feedback, validation, content clarity, and progressive disclosure

Before design work, I’ll create a short convention inventory and label each item:

1. **Preserve** — essential to recognition or workflow continuity.
2. **Restyle** — behavior remains intact; presentation improves.
3. **Normalize** — inconsistent variants become one standard pattern.
4. **Escalate** — a convention creates meaningful usability, accessibility, or product risk.

No formal provenance exercise is needed. For any escalated item, I’ll document the observed behavior, proposed change, reason, and migration risk in one line. If no owner can be found quickly, the product lead becomes the temporary decision owner. That keeps decisions reversible and prevents anonymous legacy behavior from silently becoming policy.

Success means existing users can complete their core tasks without relearning the product, while the interface feels more coherent, accessible, and current. I’d validate that with side-by-side task walkthroughs, targeted usability checks on the highest-traffic flows, accessibility checks, and regression coverage for preserved behavior.

The stopping point is a modernized design system and updated priority flows, with all preserved conventions mapped and every intentional change explicitly recorded.
