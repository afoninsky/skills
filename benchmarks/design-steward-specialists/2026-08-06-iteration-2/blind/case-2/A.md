## Visual thesis

The interface should feel like a calm booking ledger: direct, legible, and reassuring. Each screen presents one consequential decision, while a persistent fact rail keeps the topic, slot selection, timezone, facilitator, duration, and capacity visible whenever known. Progress describes the user’s place without implying completion. The active task leads the hierarchy; confirmed information is quieter but never hidden.

## Palette

Use deep ink (`#17212B`) on warm white (`#FCFCFA`), pale slate surfaces (`#F1F4F5`), and dark teal actions (`#006B66`). Selected states pair a teal border and pale teal fill (`#E6F5F3`) with an explicit label. Reserve muted amber (`#FFF4D6`) with dark brown text (`#5B3A00`) for interruptions. These are design targets; implementation-level contrast checking remains necessary.

## Type roles

Use the platform system stack. The page title is strongest, followed by the current task heading. Slot dates are prominent; times, timezone, facilitator, duration, and capacity use labeled body text. Helper and progress text is smaller but not faint. Confirmation references may use system-supported tabular numerals, without introducing another typeface.

## Layout rhythm

Use an 8-pixel rhythm, 24-pixel section spacing, and 12-pixel gaps within related facts. Wide layouts place the task panel beside a narrower sticky fact rail. Retain columns only while labels remain readable. On small screens, stack the summary above the active control and remove viewport-consuming stickiness. Slots remain three discrete full-width choices, never a calendar grid.

## Signature element

The signature element is a CSS-drawn “booking stitch”: a thin rule connecting markers for Topic, Time, Details, and Confirmed. The active marker is filled; completed steps use a CSS corner treatment plus text; future steps remain outlined. Beside it, the fact rail resembles a receipt assembled line by line, reinforcing sequence without imported icons.

## States and responsive behavior

Topic selection leads to exactly three remote slot cards. Each shows local date and time, IANA timezone, facilitator, duration, and supplied remaining capacity. Selection adds a visible “Selected” label and updates the summary; booking remains a separate action. Before booking, require explicit confirmation of timezone and facilitator. The booked state reveals the confirmation reference.

For a connection interruption, place the message by the affected action, explain that booking status is uncertain, and offer retry or status check. Never state that topic or slot survived unless the application confirms it. When retention is unknown, leave prior values unasserted and ask the user to verify them.

At 320 CSS pixels, cards stack, actions fill available width, and long IANA labels wrap. Toward 1440 pixels, cap line length and panel width. Motion is unnecessary; disable any added state motion under reduced-motion preferences.

## Accessibility intent

Use semantic headings, fieldsets and legends, native radio controls where feasible, and a real booking button. Preserve complete keyboard order, visible high-contrast focus, and target sizes aligned with WCAG 2.2 AA intent. Announce connection and booking outcomes without unexpected focus movement. Error copy names the problem and recovery action. Capacity, selection, progress, and confirmation never depend on color, shape, or position alone.

## Traceability

The one-decision task panel expresses the charter; the fact rail covers confirmed facts. Three cards provide the required comparison and labeled metadata. Separate selection, verification, booking, interruption, and confirmation treatments map to the journey. Responsive stacking, system type, CSS-only motifs, keyboard operation, visible focus, and reduced-motion handling address the fixed constraints.

## Limitations

No topic, dates, times, timezone, facilitator, duration, capacity counts, or confirmation format were provided; the interface must display supplied values rather than invented examples. Persistence after interruption is unknown and requires product logic before any retention claim. This direction describes accessibility intent only; it is not validation or certification.
