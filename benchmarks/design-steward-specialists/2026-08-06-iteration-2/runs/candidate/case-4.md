## Visual thesis

Treat the queue as a calibrated equipment bench: cool, orderly, and comparison-first, with the selected request held under a focused inspection light. The aesthetic risk is a clipped-corner “checkout tag” used only for provisional decisions. Everything else stays rectilinear, quiet, and information-led. This is a proposed visual direction, not user-validated evidence.

## Palette

Use Alloy `#EEF2F3` for the page field, White `#FFFFFF` for working surfaces, Ink `#172126` for primary text, Cobalt `#2452B8` for focus and selected structure, Oxide `#9A3E23` for attention, and Lichen `#23645D` for resolved or affirmative accents. Status meaning must include text and a native or CSS-drawn symbol; color never carries meaning alone. Exact pairings and contrast need implementation verification.

## Type roles

Use the platform system sans stack throughout. Give it character through roles rather than imported faces: a 24/30 semibold workbench title, 15/22 regular reading text, 14/18 medium row labels, and 12/16 semibold utility labels with restrained letter spacing. Dates, timestamps, and compact identifiers use tabular numerals. Requester and equipment remain the strongest row anchors.

## Layout rhythm

Build on an 8px rhythm, with 4px for label-to-value relationships and 24–32px between regions. At wide sizes, an eight-column comparison queue sits beside a four-column sticky inspector. Queue columns prioritize requester, equipment, checkout/return dates, conflict, condition, and status; actions remain contextual, not bulk. The inspector follows the journey: request facts, condition and conflict context, draft decision, conditional reason, review, then confirm. Aligned hairlines connect queue and inspector rather than creating separate cards.

## Signature element

Attach a single clipped-corner decision tab to the selected row and repeat it at the inspector’s decision area. It reads `Draft — Approve` or `Draft — Decline`, never merely an icon, and its open outline distinguishes provisional intent from confirmed status. Before confirmation, changing the draft replaces the tab without suggesting an irreversible act. After a successful confirmation, the tab disappears; supplied status and audit information take its place. No post-confirmation reversibility is implied.

## States and responsive behavior

Selection, unselected, drafted, reviewing, confirmed, concurrent-change, and failed-confirmation states each receive a persistent text label and stable location. Where actor and timestamp are supplied, show them in a compact audit entry beneath the confirmed outcome. Because concurrency and failure semantics are unspecified, the interface should present system-provided facts and only the recovery actions defined by product rules; it must not promise merge, retry, draft retention, or reversal.

Below roughly 800px, the inspector becomes the next in-flow region rather than a squeezed sidebar. At 320px, each request becomes a compact comparison block with requester/equipment first, paired dates second, then labeled conflict, condition, and status; an explicit `Inspect` control opens the full detail sequence. No essential control appears only on hover, and no bulk affordance is introduced.

## Accessibility intent

Use semantic headings, a properly labeled table where the full table fits, and sequential grouped records at narrow widths. Preserve a logical reading and focus order. Every interactive element receives a high-visibility focus treatment using Cobalt plus a contrasting offset; selection is not communicated by focus alone. Keyboard users can reach each request, inspect it, set or revise a draft, review, and confirm. Any arrow-key enhancement must be announced and must not replace native Tab behavior. Motion is unnecessary; if a state transition is added, reduced-motion preference removes it. This expresses WCAG 2.2 AA intent, not conformance or certification.

## Traceability

The comparison queue traces to compare requests and the supplied requester, equipment, dates, conflict, condition, and status content. The inspector traces to contextual inspection and the approve/decline draft journey. The clipped tab traces to the open provisional-decision marker. Conditional reason presentation respects the supplied “when required” constraint without defining its policy. Review, confirmation, concurrent change, failed confirmation, and supplied audit entry each have an explicit surface.

## Limitations

No permissions, conflict calculation, reason requirement, concurrency resolution, failure recovery, post-confirmation reversibility, or audit retention behavior is defined here. Representative content, localization extremes, and qualified accessibility review were not supplied. Breakpoints, contrast pairings, table behavior, focus order, and assistive-technology output require implementation testing with realistic data and representative users before stronger claims are possible.
