# Generic baseline outputs

## Case 1

### Visual thesis

“Calm ledger” treats shifts as comparable records rather than promotional cards. The first view should expose the finite set, availability, timing, venue, and requirements together, letting volunteers scan before committing. Hierarchy comes from alignment, spacing, weight, and restrained color—not urgency cues. The experience should feel orderly and factual: a dependable register in which every place count and requirement is easy to find.

### Palette

Use a warm off-white page, white record surfaces, charcoal text, cool gray rules, and one muted blue for links, focus, and selected controls. Reserve a subdued green for confirmed claims and a restrained amber for requirements needing attention. A no-longer-available shift should use neutral gray plus explicit text, not red or reduced opacity alone. All semantic colors need a paired label or symbol and contrast suitable for the WCAG 2.2 AA intent.

### Type roles

Use the system font throughout. A compact page title establishes the task; shift titles use a semibold record heading; date and time receive the strongest metadata emphasis. Venue, accessibility notes, certification, and remaining places use regular body text with short, plain labels. Tabular numerals, where the system font supports them, improve alignment of times and counts. Avoid oversized display type: density and comparison are primary.

### Layout rhythm

At wide widths, present a ledger-like list with a persistent header row and consistently aligned columns for shift, date/time, venue, requirements, and places/action. Each row can expand in place for full accessibility notes without losing its location in the set. Use an 8-pixel-derived spacing rhythm: tight within a field group, moderate between groups, and a clear rule between records. At narrow widths, transform each row into a compact stacked record, preserving the same information order. Put comparison filters or availability controls above the list, not in a detached sidebar.

### Signature element

The signature element is an “availability rail”: a narrow, consistently positioned strip within every record combining the plain-text remaining-place count and claim action. It creates a stable scan line across the list. The rail never pulses, counts down, or uses scarcity language; it simply states, for example, “2 places remaining” or “No places remaining.”

### States and responsive behavior

Default, hover, keyboard focus, selected, expanded-detail, submitting, confirmed, and unavailable states should preserve record dimensions where practical to prevent reorientation. Claiming opens a focused confirmation area that repeats shift title, date/time, venue, requirements, and accessibility notes. If another person has just claimed the final place, keep the record visible, mark it “No longer available,” explain what happened, and return focus to a useful recovery choice such as viewing the next available shift. At 320 px, actions become full-width beneath metadata; from medium widths upward, aligned columns return. Reduced space should cause wrapping, never horizontal page scrolling.

### Accessibility intent

Use native controls, visible focus indicators, semantic headings, and a real list or table structure chosen to match interaction behavior. Do not encode availability through color alone. Announce claim results and availability changes without unexpectedly moving focus. Touch targets should remain comfortably operable, labels should stay visible, and expanded content should expose its state programmatically. Plain-language error text should identify the failed claim and the next action.

### Traceability

The overview-first ledger directly supports comparing finite shifts. Strong date/time and aligned requirement fields reflect the representative content. The stable availability rail supports remaining-place scanning without urgency manipulation. In-place expansion preserves the charter’s object-first approach, while explicit conflict recovery covers the just-claimed-slot journey. System type, responsive stacking, and contrast-conscious semantics reflect the fixed constraints.

### Limitations

This direction does not define final color values, filtering rules, sorting logic, content length limits, or backend concurrency behavior. It assumes the supplied shift fields are available but does not prescribe non-essential imagery; the direction would likely work best without it. WCAG 2.2 AA is an intent here, not a validation or certification claim.

## Case 2

### Visual thesis

“Guided checkpoint” makes booking feel like a short sequence of deliberate confirmations. Each view foregrounds one consequential choice while keeping completed choices visible as concise, editable summaries. The visual tone is neutral and supportive: clear progress, limited simultaneous controls, and enough context to understand the consequence of the next action without exposing the entire workflow at once.

### Palette

Use a white or very light neutral background, charcoal text, quiet gray borders, and a single medium-dark blue for primary actions, selected states, links, and focus. Use a restrained green only for completed booking confirmation and a dark amber or red-brown for connection errors, always paired with plain text and an icon or structural cue. No gradients are used. Color areas remain flat, with borders and spacing carrying most grouping duties.

### Type roles

Use the system font. A modest step label (“Topic,” “Time,” “Confirm”) provides orientation; the current decision uses a clear semibold heading. Topic names and local slot times are the dominant choice labels. Duration, facilitator, capacity, and timezone use regular supporting text. Completed checkpoints collapse into one-line summaries with an explicit “Change” action. Avoid decorative type treatments and keep numeric times easy to compare.

### Layout rhythm

Center the active checkpoint in a single-column task frame with a readable maximum width. Above it, show a compact progress list; below it, reserve a stable area for Back and Continue. Topic selection precedes the slot view. The three slots should appear as equal-structure choice rows, each aligning local time, timezone, facilitator, and capacity. Use generous separation between decisions but tighter spacing within each option. On wide screens the three slots may sit in a row only if their internal alignment remains consistent; otherwise retain the vertical comparison list.

### Signature element

The signature element is a “checkpoint receipt”: after each decision, its panel contracts into a bordered summary that states exactly what was chosen and offers a visible Change control. This creates progressive disclosure without making previous context disappear. The timezone receipt repeats the local timezone immediately before the final booking action, making it a conscious confirmation rather than incidental metadata.

### States and responsive behavior

Controls need default, hover, focus, selected, unavailable, loading, success, and error states. Selection should update instantly without animated travel; any transitions should be optional, brief, and removed under reduced-motion preferences. During booking, keep the confirmed topic, slot, timezone, facilitator, duration, and capacity visible. A connection error should retain all choices, replace the pending action with a clear explanation, and offer Retry plus a safe route back to time selection. At 320 px, choice rows stack their metadata and navigation buttons become full-width. At larger widths, content remains centered rather than stretching.

### Accessibility intent

Model topic and slot choices with appropriately labeled native radio controls or equivalent semantic groupings. Give every checkpoint a heading and instructions associated with its controls. Keep focus visible and move it only when advancing to a newly revealed checkpoint, with an announced heading. Error messaging should be programmatically associated with the booking action and should not rely on color. Maintain AA-intended text and control contrast, adequate target sizes, and full keyboard operation. Reduced-motion preferences should remove nonessential transitions.

### Traceability

The one-decision task frame and collapsing receipts implement task-first progressive disclosure. Equal slot structures support comparison of exactly three choices. The repeated timezone checkpoint addresses explicit timezone confirmation. Persistent selected details support booking confidence, while retained choices and Retry address connection-error recovery. Flat palette, system typography, absent photography, and reduced-motion behavior follow the fixed constraints.

### Limitations

This direction does not specify available topics, slot-generation logic, timezone detection, retry policy, or connection diagnostics. It does not determine whether capacity changes in real time. Exact colors, breakpoints, icon shapes, and copy require implementation testing. WCAG 2.2 AA remains a stated design intent rather than a validation or certification claim.

## Case 3

### Visual thesis

“Visible trail” frames a maintenance request as a traceable civic record from first description through later correction. The current status and provenance stay visible, while controls appear in the context where they matter. The interface should communicate continuity: what the resident supplied, what disclosure applied, what reference was issued, what changed, and how to correct information without obscuring previous events.

### Palette

Use a light neutral canvas, white content surfaces, near-black text, sturdy gray dividers, and a deep teal or blue for actions, links, current-step emphasis, and focus. Statuses use distinct but restrained semantic accents paired with text labels and simple shapes. Errors use a dark red accent; cautions use amber. High-contrast mode should replace decorative fills with system colors, strong outlines, and preserved labels rather than depending on custom palette relationships.

### Type roles

Use the system font. The current request status is the primary heading after submission; during entry, the current task step receives that role. Category and approximate location form a compact record title. Description, privacy disclosure, and correction guidance use comfortable body text. Reference IDs and timestamps should use a stable, highly legible treatment, with monospacing only if available through the system stack and beneficial. Status labels remain explicit words.

### Layout rhythm

During submission, use a broad main column for the active form and a narrower persistent summary column showing category, approximate location, description completion, optional photo state, and disclosure status. Without a map, location entry should be text-first and clearly labeled as approximate. At narrow widths, the summary becomes a collapsible block above the current controls. After submission, lead with a status header, then a vertical history, followed by the retained request details and correction route. Use consistent vertical spacing to separate events, fields, and actions.

### Signature element

The signature element is a “provenance spine”: a vertical line connecting labeled status events, each with actor context when available, timestamp, and a short description. The reference ID anchors the top of the spine. A correction does not silently overwrite the original record; it appears as another event and points to the corrected field, preserving a visible trail without inventing operational details.

### States and responsive behavior

Support empty, entered, validation-error, photo-attached, disclosure-unreviewed, ready-to-submit, submitting, submitted, status-updated, and correction-requested states. The review step repeats the category, approximate location, description, photo presence, and disclosure before submission. Submission failure should preserve entered content and focus the error summary. Successful submission should surface the reference ID and current status immediately. At 320 px, the provenance spine retains chronological order, metadata wraps below event labels, and actions occupy the full content width. At wider sizes, the status summary may remain sticky while the history scrolls, provided it does not hide content.

### Accessibility intent

Use explicit labels and instructions for every field, including acceptable location detail and optional photo status. Provide a semantic error summary linked to affected inputs. Ensure the privacy disclosure is readable before its acknowledgment control and that acknowledgment is not preselected. Status history should be a semantic ordered list, with color-independent labels and meaningful timestamps. High-contrast mode, visible keyboard focus, adequate control targets, and AA-intended contrast are core. Photo content needs an appropriate textual description route if it conveys report information.

### Traceability

Text-first approximate location follows the fixed absence of a map. Persistent summary and review support categorize-locate-describe-disclose-submit. The status header, provenance spine, reference ID, and correction events enact status-first presentation and persistent provenance. Preserved input on failure and a visible correction route address recovery. System type, high-contrast adaptation, and non-coercive disclosure behavior reflect the constraints.

### Limitations

This direction does not define categories, location precision, photo requirements, privacy-disclosure wording, agency actors, status vocabulary, correction eligibility, or response times. Illustration is intentionally unspecified and should not replace functional status information. Exact high-contrast behavior depends on platform and browser testing. WCAG 2.2 AA is an intent, not a validation or certification claim.

## Case 4

### Visual thesis

“Decision bench” presents requests as comparable work items with their constraints always close at hand. The interface favors rapid keyboard scanning, focused inspection, and deliberate decisions. A split context keeps the request set visible while one request’s dates, conflicts, condition, reason, and audit trail are inspected. Approval and decline remain reversible drafts until an explicit final confirmation.

### Palette

Use a pale neutral workspace, white request and detail surfaces, near-black text, medium gray rules, and one deep blue for focus, selection, and primary controls. Conflicts use a dark amber accent with a text label; approved and declined states use restrained green and burgundy respectively, paired with words and native symbols. Draft decisions use blue-gray. Avoid large saturated fills so dense comparison remains calm and legible.

### Type roles

Use the system font only. Requester and equipment form the primary row label; checkout dates are the strongest comparison metadata. Conflict, condition, and decision status use short semibold labels followed by regular text. The detail pane title identifies the selected request. Actor and timestamp in the audit trail use compact supporting text. Reason fields use normal body text rather than a decorative quote style. Native text symbols may supplement labels but never replace them.

### Layout rhythm

At desktop widths, use a two-pane workbench: a compact request list on the left and a flexible detail pane on the right. Align list columns for requester/equipment, dates, conflict, condition, and status. The detail pane groups constraints first, decision controls second, and audit trail third. Use tight row spacing for scanning, clear separators between requests, and more generous spacing around the consequential decision area. At narrower widths, the list becomes the first screen and selected details open as the next in-flow view with a persistent Back to requests control.

### Signature element

The signature element is a “decision tray” fixed within the selected request’s context. It shows Approve and Decline as peer actions, reveals a required reason field when applicable to the chosen route, and labels the result “Draft decision” until confirmation. Undo or Change decision remains available before final confirmation. The tray repeats the selected requester, equipment, and dates to prevent cross-request mistakes.

### States and responsive behavior

Request rows need default, hover, keyboard focus, selected, draft-approved, draft-declined, finalized, and conflict states. The detail pane needs empty selection, loading, ready, validation-error, confirmation, and final audit states. Keyboard users should move through requests predictably, open details, reach constraints, choose a decision, enter a reason, review, and confirm without pointer use. Before confirmation, changing requests should preserve or clearly surface any draft decision. At 320 px, columns become labeled stacked fields; audit events remain chronological; actions become full-width without changing their order. At large widths, pane sizes may adjust, but the selected row and detail identity must stay synchronized.

### Accessibility intent

Use semantic list or table structures matching the implemented interaction, with explicit column or field labels. Provide a strong visible focus ring and avoid focus traps in the split pane or confirmation view. Conflicts and statuses must be expressed in text, not color or icons alone. Decision controls require clear accessible names; validation explains what reason is needed. Confirmation should summarize the decision and return focus to the resulting status after completion. Target sizes, contrast, reading order, and keyboard sequences should support the WCAG 2.2 AA intent.

### Traceability

Aligned request rows directly support comparison-first scanning. The split workbench connects the set to one request’s constraints. The decision tray implements reversible approve/decline actions until final confirmation and keeps identity context visible. Conflict, condition, reason, status, actor, and timestamp each have an explicit placement. The audit section preserves the required trail. System type, native symbols, keyboard-first behavior, responsive transformation, and absence of charts or external packages reflect fixed constraints.

### Limitations

This direction does not define permission rules, conflict calculation, when reasons are mandatory, bulk actions, decision reversibility after confirmation, or audit retention. It avoids prescribing charts and external iconography as required, but exact native symbols will vary by platform. Pane behavior and keyboard patterns require implementation testing. WCAG 2.2 AA is an intent, not a validation or certification claim.
