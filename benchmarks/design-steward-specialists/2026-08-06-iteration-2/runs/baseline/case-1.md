## Visual thesis

Design the board as a calm comparison surface where the tool is the anchor and appointment windows are equally weighted choices. Use a quiet, civic character: generous space, crisp borders, and restrained color. Each tool card should answer “What is it?”, “What do I need?”, and “When can I collect it?” Treat availability as information, not a sales cue.

## Palette

Use warm off-white `#F7F6F2` for the page, white `#FFFFFF` for cards, near-black `#202522` for primary text, and muted green `#315D4F` for actions and selected borders. Secondary text can use `#59615D`; dividers `#CDD2CE`. Reserve amber `#8A5A00` on `#FFF4D6` for caution and red `#9A2D2D` on `#FDECEC` for failed states. Pair every status color with text and, where useful, a native or CSS-drawn icon. These colors require implementation testing.

## Type roles

Use the system font stack throughout. Set the page title at 28–36 px, tool names at 20–24 px, section labels at 14–16 px semibold, and body and controls at 16 px. Supporting details may use 14 px but should not carry essential instructions alone. Use sentence case and tabular numerals where supported. Weight and spacing establish hierarchy.

## Layout rhythm

Build on an 8 px unit. A centered container reaches approximately 1200 px, with 16 px gutters on narrow screens and 24–32 px on wider screens. Tool identity and requirements occupy the card header; pickup windows follow in a grid. Keep date, time, depot, remaining reservations, and state aligned across options. Deposit, ID requirement, and accessibility note remain visible before reservation.

## Signature element

The signature element is a “window rail”: bordered 30-minute window buttons connected by a fine neutral rule. Each option contains date, time, depot, remaining reservations, and a written state. Selection adds a green inset border, check mark, and “Selected”; it does not imply that the slot is held. The rail keeps comparison orderly and the tool visually primary.

## States and responsive behavior

Available windows use neutral surfaces; hover darkens the border. Keyboard focus uses a 3 px high-contrast outline with offset. Selected, unavailable, confirming, confirmed, and error states have explicit labels. If a window becomes unavailable during confirmation, retain entered context where technically possible, explain that it could not be reserved, return focus to the message, and present remaining options without claiming they are locked. Show retry only if supported.

At 320–639 px, cards and window options stack, with requirements preceding the rail and actions spanning the content width. From 640 px, options may form two columns. At wider widths, use a two-region card: stable tool requirements beside a flexible window grid. Do not reorder content in a way that changes keyboard or reading sequence.

## Accessibility intent

Target WCAG 2.2 AA through semantic headings, real buttons and form controls, persistent labels, visible focus, sufficient target size, and status announcements appropriate to the implementation. Associate deposit, ID, and accessibility information with the tool and chosen window. Errors should identify what changed and what the resident can do next. Respect `prefers-reduced-motion`; transitions, if any, should be brief opacity or border changes and nonessential. Verify zoom, reflow, contrast, keyboard operation, and screen-reader announcements during implementation; this brief is not certification.

## Traceability

The object-first card answers the charter’s calm hierarchy. The window rail supports the priority comparison and reservation journey. Requirements remain before the action so deposit and ID conditions are not hidden. Explicit selection, confirmation, unavailability, and recovery states cover the representative reservation states without relying on color. Neutral remaining-count treatment and the absence of countdowns, scarcity language, photography, gradients, and external icons follow the fixed constraints.

## Limitations

The brief does not define whether reservations are held, persisted, synchronized across residents, or recoverable after navigation; those behaviors require product and technical confirmation. Exact depot naming, tool imagery or identifiers, deposit currency, ID wording, accessibility accommodations, and remaining-count semantics are also unspecified. Content design, interaction timing, contrast, assistive-technology behavior, and responsive fit must be tested with the implemented system and representative users before release.
