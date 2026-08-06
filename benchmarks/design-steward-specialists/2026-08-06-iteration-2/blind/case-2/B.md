## Visual thesis

Treat booking as a calm scheduling ledger: one active decision occupies the main stage, while a compact facts ledger keeps already confirmed details continuously visible. This supports the task-first charter without implying that any choice is final before confirmation.

## Palette

Use Paper `#F7F9FC` for the canvas, White `#FFFFFF` for decision surfaces, Midnight `#17263B` for text and rules, Meeting Blue `#175AA8` for actions and focus, Mist Blue `#DCEAF8` for selected backgrounds, and Fault Red `#A12F35` for interruption messaging. Blue is functional rather than decorative; selection also receives a border and explicit label. Fault Red is reserved for connection errors. Exact contrast must be checked in implementation.

## Type roles

Use only the platform system stack. A 28–36px semibold heading names the current decision; 17–18px regular text explains it. Slot dates use 20–24px semibold, while times, duration, capacity, timezone, facilitator, and confirmation reference use 14–16px with tabular numerals where the system font supports them. Small labels remain at least 13px and use weight, not uppercase letter-spacing, for hierarchy.

## Layout rhythm

Build on an 8px base with 12px internal gaps, 20px card padding, and 32–48px sectional separation. At wide widths, place the facts ledger in a four-column-width left rail and the active decision in an eight-column-width main area. The ledger lists topic, selected option, IANA timezone, facilitator, and duration; unknown or unconfirmed values are stated as such rather than filled. Progress is a plain sequence—Topic, Time, Confirm, Booked—with the current step named in text.

## Signature element

The “three-window rail” is a CSS-drawn rule passing behind exactly three slot panels. Each window contains local date and time, duration, remaining capacity, and facilitator when confirmed by the provided data. Selecting a window thickens its Midnight outline, adds a Meeting Blue inset bar, and displays “Selected.” The rail expresses comparison across three moments without borrowed iconography. On narrow screens it rotates into a vertical spine, preserving the same reading order.

## States and responsive behavior

Topic choice precedes the three-slot comparison. Confirmation gives timezone and facilitator their own explicit review rows before the booking action. The booked state replaces the action with the confirmation reference while retaining the fact ledger. A connection interruption receives a bordered Fault Red panel near the active task: booking status and selection persistence are described as unknown until the service confirms them, with reconnect/retry and review paths kept visible.

From 320px, content is one column, the fact ledger becomes a collapsible summary headed by the currently confirmed facts, and slot panels stack without horizontal scrolling. At larger widths the ledger becomes sticky only when doing so does not obscure content. Controls keep a minimum 44px target, wrapping labels grow vertically, and no essential content is truncated.

## Accessibility intent

Implement the slots as one keyboard-operable native radio group with a visible legend; keep DOM and visual order aligned. Provide a high-contrast, non-obscured focus ring, text labels for current step and selected state, and an announced interruption status that does not repeatedly seize focus. Motion is unnecessary; any optional state transition is brief and removed under reduced-motion preferences. Semantic headings, error association, zoom/reflow, and contrast target WCAG 2.2 AA, but require implementation review and testing.

## Traceability

The single active stage traces to “one consequential choice at a time”; the facts ledger to confirmed facts staying visible; the three-window rail to exactly three remote slots; and explicit review rows to timezone and facilitator confirmation. Responsive reflow, keyboard behavior, focus, reduced motion, system type, CSS-only motifs, and the candid interruption state trace directly to Fixed constraints. Palette, rhythm, progress treatment, and the rail use only Open axes. No external precedent or asset is used.

## Limitations

No audience, topic values, dates, facilitator names, capacities, brand language, or persistence behavior were supplied, so none are assumed. This is a visual-direction rationale, not a prototype, usability finding, accessibility certification, engineering feasibility result, or selection recommendation. Long localized content, real data extremes, focus behavior, live-region timing, sticky behavior, and color contrast remain to be verified with implementation and appropriate specialist review.
