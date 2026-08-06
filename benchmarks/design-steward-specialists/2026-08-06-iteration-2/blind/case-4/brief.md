# Case 4: Equipment checkout decision queue

**Charter:** A comparison-first workbench for quick keyboard scanning, contextual inspection, and deliberate reversible decisions before final confirmation.

**Priority journey:** A coordinator compares requests, inspects dates, conflicts and condition, drafts Approve or Decline with a reason when required, reviews the result, confirms, and sees the supplied audit entry.

**Representative content:** Requester; equipment; checkout and return dates; conflict; condition; decision status; reason; actor and timestamp where supplied; concurrent-change and failed-confirmation states.

## Fixed constraints

- Responsive from 320 to 1440 CSS pixels
- System font and native text or CSS-drawn symbols only
- No charts, bulk actions, external packages, or hover-only controls
- WCAG 2.2 AA intent, keyboard-first interaction, visible focus, and reduced-motion support
- Do not invent permissions, conflict logic, reason policy, concurrency semantics, reversibility after confirmation, or audit retention

## Open axes

- palette
- density
- layout
- provisional-decision marker treatment
