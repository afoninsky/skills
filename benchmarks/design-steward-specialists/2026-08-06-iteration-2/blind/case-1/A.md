## Visual thesis

Build the board like a carefully labelled community workshop bench: the tool is the anchor, and pickup windows are comparable facts beside it. Name the tool and category first, then show depot, deposit, ID, and accessibility details before reservation. The aesthetic risk is a time-bracket motif from physical measuring marks, used only to clarify each 30-minute span. It should feel civic and practical, never retail-like. No photography; restrained CSS lines and cut-corner tags provide object-world character.

## Palette

Use six flat colors: **Bench mist** `#F2F6F5` for the page, **Paper** `#FFFFFF` for records, **Toolbox navy** `#17324D` for primary text and actions, **Depot teal** `#286B68` for selection and links, **Washer gray** `#66747A` for secondary text and rules, and **Fault brick** `#9C3833` for errors. No gradients or overlays. Teal never carries state alone: selection also gains border weight and text. Remaining reservations stay navy or gray, without badges or enlarged numerals.

## Type roles

Use only `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. A 30/36 semibold tool name supplies the display role. Section labels use 13/18 bold, sentence case, with `0.04em` tracking. Body copy is 16/24; requirements are 15/22. Times and deposits use 17/24 semibold with tabular numerals when supported. Avoid all caps and oversized availability counts.

## Layout rhythm

An 8px rhythm produces 16px gaps, 24px record padding, and 32–48px section separation. At wide widths, a bounded 1180px board uses a 4/8 split: a sticky tool-and-requirements record at left and date-grouped windows at right. Each date is a heading; windows form a vertical list with aligned columns for time, depot, deposit, requirements, accessibility, remaining reservations, and state. Rules replace card clutter. The reserve action sits inside the selected window.

## Signature element

Each window begins with a CSS-drawn **workshop time bracket**: start and end times sit above two square ticks joined by a rule, with “30 min” beneath. It encodes duration, not progress, and never animates. Selection adds a thicker teal rule and “Selected window.” This is the sole expressive device; other controls and surfaces stay quiet. Plain text preserves meaning if the rule disappears.

## States and responsive behavior

Default, hover, focus, selected, confirming, reserved, unavailable-during-confirmation, and error states receive explicit labels. Confirming prevents duplicate submission and says “Confirming reservation”; it does not claim a hold. If availability changes, keep requirements visible, explain “This window is no longer available,” move focus to the message, and offer “Choose another window.” Do not promise persistence or locking. At 320–639px, metadata becomes labelled rows below the bracket and the action is full-width. From 640px, key facts align into columns; the split appears only with readable measures. Long notes wrap. No motion is required.

## Accessibility intent

Use semantic headings, native buttons, and a list or table matching final interaction semantics; use a fieldset and legend if windows are one choice set. Keyboard order follows visual order. Focus uses a 3px navy outline with a 2px Paper offset at every breakpoint. Check text/background pairs against WCAG 2.2 AA contrast targets during implementation; this is intent, not certification. Errors combine shape with text. Touch targets aim for at least 44 by 44 CSS pixels. Reduced-motion settings are honored by omitting movement.

## Traceability

The object-first hierarchy follows the charter. The comparison list maps to the representative tool, category, date, window, depot, deposit, ID, accessibility, remaining-reservations, and state fields. Neutral availability, static duration marks, and recovery copy trace to the bans on manufactured urgency and unconfirmed behavior. Responsive, focus, reduced-motion, and non-color rules trace to Fixed constraints. Palette, hierarchy, layout, and CSS marks use Open axes. No requirement IDs, evidence IDs, precedents, brand assets, or sibling directions were supplied or consulted.

## Limitations

This is an unvalidated visual-direction proposal, not usability evidence, accessibility certification, feasibility, or approval to implement. Content lengths, localization, latency, inventory semantics, persistence, and assistive-technology behavior remain unknown. Choosing table, list, or radio-group semantics requires interaction details and implementation review. Contrast, zoom, reflow, keyboard recovery, and unavailable-window behavior need browser checks and appropriate specialist or representative-user review. The generic-pattern self-critique rejected urgency badges, card grids, and decorative tool icons because they would compete with comparison or imply retail scarcity.
