## Visual thesis

Treat the queue as a calm, comparison-first instrument panel: dense enough to scan, restrained enough that a consequential choice never feels casual. Favor request facts before controls, with dates, conflicts, and condition readable in one horizontal sweep on wide screens. Decisions remain visibly provisional until confirmation. Crisp alignment and spacing distinguish evidence, draft intent, and recorded outcome.

## Palette

Use off-white `#F7F8FA`, white surfaces, ink `#18212B`, and muted text `#586573`. Deep blue `#2457A6` supports links, focus, and confirmation. Reserve amber `#8A4B08` for conflicts, green `#176B45` for approved outcomes, and brick `#A3342F` for declines and failures, each on a pale tonal background. Pair color with text and a native or CSS-drawn symbol. Draft treatments remain quieter than final statuses.

## Type roles

Use the system font stack. Requester and equipment names are the strongest row labels at 15–16 px, semibold. Column labels and metadata are 12–13 px, never all caps. Dates, condition, and status use 14 px text with consistently aligned date ranges. Decision labels use explicit verbs. Reasons use sentence case and wrap rather than truncate.

## Layout rhythm

At 1024–1440 px, use a narrow queue rail, comparison table, and contextual inspection panel. The rail indicates current request and nearby position without suggesting bulk selection. The table uses sticky headers, 44–52 px rows, subtle rules, and visually anchored requester and equipment columns. Selecting a row opens its full facts and supplied audit details. An 8 px spacing base supports 16 px cell padding, 24 px section gaps, and 32 px page margins. Review and confirmation follow the inspected evidence.

## Signature element

A “decision ribbon” connects each inspected request to its draft choice. This bordered inset band contains a CSS-drawn open circle, “Draft,” the proposed Approve or Decline action, and a reason field only when required by supplied policy. Its incomplete outline signals provisional state without implying persistence or undo. In review, the circle becomes a check-shaped mark while “Not yet confirmed” remains explicit, preserving the boundary between consideration and commitment.

## States and responsive behavior

Rows expose comparable facts and textual status. The selected row receives a persistent border and current-item label. Conflict and condition remain visible in inspection; nothing depends on hover. A concurrent-change warning interrupts review, summarizes only supplied changed fields, and assumes no resolution semantics. Failed confirmation keeps the draft visible and places failure beside the confirm control without implying automatic retry. After success, replace the ribbon with the supplied audit entry, including actor and timestamp only when provided.

From 600–1023 px, stack inspection beneath a horizontally scrollable comparison region with preserved headers and a visible scroll affordance. At 320–599 px, transform requests into compact fact cards in source order; selection reveals inline details, then draft and review controls. Critical fields remain present. Controls use at least 44 px targets. Optional disclosure motion is brief and removed under reduced-motion preferences.

## Accessibility intent

Use semantic headings, table markup on wide layouts, labeled regions, and equivalent card reading order. Provide a keyboard path from queue through inspection, drafting, review, and confirmation. Every control has a visible two-pixel focus indicator with sufficient contrast and no obscuring. Announce errors and concurrent changes with appropriate urgency; move focus only to reach newly relevant content. Labels and symbols carry meaning independent of color. Contrast, zoom, reflow, target size, and error association require implementation testing; this is not a conformance claim.

## Traceability

The comparison surface maps to requester, equipment, checkout and return dates, conflict, condition, and status. Inspection preserves context while drafting Approve or Decline. The ribbon maps draft, conditionally required reason, review, and confirmation into a deliberate sequence. Supplied actor and timestamp appear only in the audit treatment. Responsive transformations preserve facts and sequence; dedicated panels cover concurrent change and failed confirmation.

## Limitations

The design does not define permissions, conflict calculation, reason policy, concurrent-update resolution, draft persistence, reversibility after confirmation, retry behavior, or audit retention. Those rules require product and engineering decisions before interaction copy and edge behavior can be finalized. Content lengths, localization, and assistive-technology behavior are also unknown; prototypes and implementation should be tested with representative supplied data and users.
