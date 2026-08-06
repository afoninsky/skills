Do not pause indefinitely. The unavailable service may be the only way to preserve its native, fully editable source, but it is not the only way to preserve the design intent, review evidence, and implementation-ready work.

Declare a temporary “preservation mode” and create a tool-neutral release package containing:

- PDF exports of every key screen and flow, plus PNG/SVG exports of relevant assets
- A screen inventory with stable IDs, states, breakpoints, and flow order
- Design tokens for color, type, spacing, elevation, and motion in plain text or JSON
- Component specifications covering variants, states, behavior, accessibility, and responsive rules
- Interaction notes for transitions, validation, empty/loading/error states, and edge cases
- Annotated screenshots for details that exports cannot communicate reliably
- Content copy, asset provenance, known constraints, open questions, and decision history
- A short README explaining package structure, version, owner, date, and how to resume

Store the package in an approved, versioned repository or document system with access controls appropriate to the material. Ask engineering and product to review it for implementation completeness, and record any gaps explicitly rather than treating them as preserved.

Be precise about the limitation: native editability, prototype fidelity, comments, or certain metadata may be temporarily unavailable. Label those as recoverability risks. Preserve any existing native exports or backups without converting or overwriting them, and document the exact service, workspace, project identifiers, and last known version so restoration remains possible later.

Continue work that can safely proceed from the neutral package. Pause only activities that truly depend on unavailable proprietary behavior, and set a dated review point with a named owner for procurement or service recovery. An indefinite pause converts a tooling outage into an unmanaged product risk; a controlled preservation package keeps the work reviewable, transferable, and resumable.
