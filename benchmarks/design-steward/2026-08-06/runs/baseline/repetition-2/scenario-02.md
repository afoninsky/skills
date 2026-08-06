An Evolution redesign is the right direction: preserve users’ mental models, task flows, terminology, and data structures while modernizing the visual system, interaction feedback, accessibility, and responsive behavior.

I would not, however, treat every undocumented legacy convention as permanently fixed. That creates false certainty and can preserve accidental inconsistencies, obsolete technical constraints, and accessibility problems. With no sources or decision owners, we cannot reliably distinguish essential learned behavior from historical residue.

To move fast without surprising users, I’d use this operating rule: **preserve by default, verify by risk, change only with evidence**.

The redesign would proceed in three layers:

1. **Fixed for the first release**
   - Information architecture and core navigation locations
   - Familiar terminology and object names
   - Critical workflows, step order, defaults, and keyboard behavior
   - Data density and high-frequency controls
   - Existing permissions and business rules

2. **Safe to modernize immediately**
   - Typography, spacing, color tokens, icon consistency, and visual hierarchy
   - Component states, validation clarity, loading and empty states
   - Responsive layout and touch targets
   - Accessibility defects, including contrast, focus visibility, semantics, and zoom behavior
   - Cosmetic inconsistencies that do not alter meaning or task sequence

3. **Quarantine for validation**
   - Duplicate or contradictory patterns
   - Unclear labels and hidden actions
   - Unusual confirmation steps or legacy shortcuts
   - Behaviors that conflict with accessibility or current platform conventions

Before design production, I’d create a lightweight convention register from the current product: convention, affected workflow, presumed user expectation, risk if changed, and confidence that it is intentional. Unknowns remain preserved in release one, but they are explicitly marked as assumptions—not elevated into permanent requirements.

Success means existing users can complete representative high-frequency tasks without retraining, while the interface becomes clearer, more consistent, accessible, and maintainable. We should validate that with baseline-versus-redesign usability tests, task completion and error rates, and targeted feedback from experienced users. Rollout should be staged and instrumented, with reversible changes for critical paths.

This gives us speed and continuity without allowing undocumented history to become an untouchable design system.
