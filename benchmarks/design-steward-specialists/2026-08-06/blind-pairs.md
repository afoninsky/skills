# Blind visual-direction pairs

## Case 1

### Output A

### Visual thesis

The “calm ledger” becomes a quiet, object-first register of shifts: factual rows, stable alignment, and one distinctive availability notation make comparison feel dependable rather than promotional.

### Palette

Use Paper White `#F7F8F6` for the canvas, Ledger Ink `#202521` for primary text, Rule Grey `#C7CEC8` for structure, Registry Green `#286442` for available and confirmed states, Notice Blue `#245F82` for requirements and focus, and Closed Clay `#8A473A` for errors or unavailable states. These restrained choices serve the calm-ledger charter and the Open palette axis; green and clay never carry meaning without text or symbols.

### Type roles

Use the platform system stack throughout, respecting the Fixed system-font constraint. Shift titles use 18–20 px semibold; date and time use 16 px semibold; venue, accessibility notes, and certification use 14–16 px regular; remaining places use 14 px medium with tabular numerals where supported. Labels remain sentence case with modest letter spacing. Hierarchy comes from weight, size, alignment, and wording—not a second typeface.

### Layout rhythm

An overview header first states the number of available shifts and exposes plain-language filters; the shift objects follow immediately in a single register. At wider widths, each row aligns title, date/time, venue, requirements, remaining places, and action on a 12-column grid. Eight-pixel spacing increments, 16–24 px row padding, and continuous rules create density without crowding. At narrow widths, each row becomes a compact card in the same reading order. This serves overview-first comparison, representative content, and 320–1440 px support. Non-essential imagery is omitted because it would reduce scan density; that choice uses the Open imagery axis.

### Signature element

Each shift has a “place register”: a short ruled strip whose labeled cells correspond to remaining places, paired with explicit text such as “3 places remaining.” After claiming, one cell gains a check and the text becomes “Your place is claimed.” It translates finite capacity into ledger notation without urgency. I rejected countdowns, pulsing badges, and bright scarcity chips because they would manipulate urgency. The register is the single aesthetic risk; everything else stays quiet.

### States and responsive behavior

Available rows present “Claim this shift”; certification requirements appear before the action. Full shifts retain their comparison data but say “No places remaining” and disable claiming. If a place is taken during submission, the row remains in context, changes to “This shift was just claimed by someone else,” and offers “View available shifts,” returning focus to the next available row or overview. Long titles, long accessibility notes, missing optional notes, network failure, and zero results wrap or disclose without breaking alignment. On mobile, actions become full-width and metadata stacks; no horizontal scrolling is required. Motion is limited to a brief color transition that clarifies a status change and is removed under reduced-motion preferences.

### Accessibility intent

The direction targets WCAG 2.2 AA intent through semantic headings, lists or tables chosen to match implementation, persistent labels, minimum 44 px action targets, visible two-tone focus rings, logical DOM and keyboard order, and status messages announced without moving focus unexpectedly. Text and controls should be contrast-checked against every state. Color, cell fills, and motion remain redundant to explicit wording and icons.

### Traceability

Object-first rows, stable rules, density, and the place register derive from the charter. Overview counts, aligned metadata, preserved failed rows, and recovery navigation derive from the priority journey. Field order derives from the representative content. Plain labels, restrained status language, system type, accessibility intent, and responsive ranges derive from Fixed constraints. Palette, visual hierarchy, layout, and omitted imagery use the named Open axes. The brief color transition serves state feedback, while its reduced-motion treatment derives from accessibility intent.

### Limitations

This is a direction, not a selected or validated design. It assumes shifts can be meaningfully compared in one list and that remaining-place counts may be shown; product policy could invalidate either. Provenance is limited to the supplied brief, constraints, charter, and frontend-design skill. The ledger pattern risks resembling generic administrative tables; the place register and volunteer-specific field order counter that sameness, but should be challenged in critique. Accessibility, content-design, volunteer-operations, privacy, localization, and frontend-feasibility specialists still need review.

### Output B

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

### Output A

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

### Output B

### Visual thesis

“Guided checkpoint” becomes a calm, task-first sequence: one consequential choice per view, with a persistent evidence rail showing what the learner has confirmed.

### Palette

- Paper Mist `#F5F7F6` — background.
- Carbon `#17201E` — text and icons.
- Practice Teal `#176858` — actions, focus support, active checkpoint.
- Quiet Mint `#DDEDE8` — selected and confirmed surfaces.
- Signal Red `#A12D27` — errors and unavailable states.

No gradients. Neutral space provides hierarchy. Decorative imagery, including stock photography, is omitted. Consistent line icons may support timezone, facilitator, capacity, and connection labels, but never replace text.

### Type roles

Use only `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. Set checkpoint questions at 28–32 px semibold, body and choices at 16–18 px regular, and data labels at 13–14 px medium. Tabular numerals aid time comparison. Sentence case and plain verbs keep the tone instructional.

### Layout rhythm

Above 768 px, the current decision occupies roughly two-thirds of a two-column frame; the evidence rail summarizes topic, 25-minute duration, local time and timezone, facilitator, and capacity. Below that, the summary sits above the action. Use a 4/8 px spacing basis, with generous separation among the three slot cards. Cap content width at large viewports.

### Signature element

A bordered “checkpoint ticket” is the signature: its rows change from unresolved labels to confirmed facts as the journey advances. Restrained clipped corners suggest a reservation ticket, but every row must communicate state. This risks becoming ornamental, so surrounding surfaces remain plain. A numbered stepper was rejected because it shows position without preserving decision context; an all-controls dashboard was rejected because it conflicts with progressive disclosure.

### States and responsive behavior

Representative states cover topic selection, three comparable time slots, explicit timezone confirmation, booking review, confirmation, and connection state. Each slot shows local time, timezone, facilitator, and capacity; selection uses text, border, and icon rather than color alone. Hostile states include full or unavailable slots, no available slots, facilitator change, ambiguous timezone, booking conflict, and connection loss.

On connection failure, replace the action area with a precise explanation, primary “Try again,” and secondary “Review details.” Retain selections and say so only when implementation and policy confirm retention. Otherwise, disclose exactly what was lost and return the learner to review before another attempt. Never imply storage or auto-retry invisibly.

At 320 px, cards stack and actions retain document order; up to 1440 px, width remains controlled. Motion is limited to brief optional state transitions and removed when reduced motion is requested.

### Accessibility intent

WCAG 2.2 AA intent informs readable sizing, intended contrast pairings, semantic headings, persistent labels, descriptive errors, and a visible high-contrast focus indicator. Keyboard order follows topic, slots, timezone, then booking, without traps or hover-only disclosure. Status changes should be announced without stealing focus. Touch targets, zoom behavior, and narrow-width recovery require specialist review and measurement.

### Traceability

System type, no gradients or photography, reduced-motion support, accessibility intent, and the 320–1440 px range trace to Fixed constraints. Slot comparison, timezone confirmation, booking, and truthful conditional recovery trace to the priority journey. Ticket rows trace to representative content. Progressive disclosure, the evidence rail, and single-decision views trace to the charter. Hierarchy, layout, palette, and icon treatment use named Open axes.

Provenance is limited to the supplied case and required frontend-design skill. The direction avoids common cream/serif, dark/neon, and broadsheet defaults. However, cards and progress summaries remain familiar booking patterns; distinctiveness depends on the content-bearing ticket rail, not surface styling.

### Limitations

Brand attributes, locale conventions, timezone naming, persistence, storage policy, retry mechanics, and booking-service behavior are unspecified. Recovery must follow confirmed behavior. Accessibility, content-design, localization, privacy/policy, responsive implementation, and engineering reviews remain necessary; this direction does not establish compliance, usability, feasibility, or brand fit.

## Case 3

### Output A

### Visual thesis

“Visible trail” becomes a calm civic interface where every action leaves a legible record, making status, provenance, correction, and recovery more prominent than decoration.

### Palette

- **Civic Ink — `#17232B`:** primary text and history rules; charter.
- **Paper — `#F7F9F8`:** quiet page ground; Open palette axis.
- **Route Blue — `#075E8C`:** actions and correction links; contextual control.
- **Marker Amber — `#B85C00`:** warnings, always with text/icon; recovery.
- **Resolved Green — `#176B4D`:** completed status, never color-only; status history.
- **Fault Red — `#B42318`:** explicit errors and recovery guidance; AA intent.

Rejected: cream, serif, and terracotta styling would resemble a generic editorial template and weaken the service’s neutral, status-first character.

### Type roles

Use only the Fixed system stack: `system-ui, -apple-system, "Segoe UI", sans-serif`. A 28–36 px/700 title names the journey stage; 20–24 px/700 headings separate form sections; 16–18 px/400 body text carries instructions and disclosure; 14–16 px/600 utility text carries statuses, reference IDs, and available history details. Hierarchy and spacing, not an imported face, provide character.

### Layout rhythm

A 640–720 px task column works across the Fixed 320–1440 px range; wider screens add a 280 px contextual status rail instead of stretching inputs. Its order follows the priority journey: category → approximate location → description/photo → disclosure → review → submit. Tracking leads with reference ID and current status, then ordered history and correction route. An 8 px spacing base and strong rules express sequence. No map appears. Illustration is omitted from the task path; an optional small public-fixture line drawing may support an empty tracking state, using the Open illustration axis without competing with recovery copy.

### Signature element

The **Trail Ledger** is a continuous rule joining labeled checkpoints. It shows supplied information, surfaced status-history detail where available, and permitted corrections. It shifts from reporting progress to post-submission history, embodying “visible trail” and persistent provenance. The intentional aesthetic risk is making provenance, rather than a hero image, the memorable device.

### States and responsive behavior

Below 768 px, the ledger becomes a compact top summary with stacked checkpoints; above it, the ledger may occupy the rail. Current, complete, warning, and failed states combine words, icons/shapes, and color. Review keeps approximate-location uncertainty visible. “Correct location” returns focus to that field without promising that other entries persist. Photo failure states what remains and offers retry/remove. Submission interruption states what was retained or lost, whether a reference ID exists, and provides the appropriate correction or re-entry route; retention is claimed only when confirmed by implementation and policy. Motion is limited to checkpoint changes and removed under reduced-motion preference.

### Accessibility intent

The direction targets WCAG 2.2 AA intent through semantic headings, persistent labels, plain-language disclosure, logical source/tab order, keyboard-operable recovery, and a visible two-layer focus indicator. Text, controls, and states require implementation-time contrast measurement. At 200% zoom and narrow widths, content should reflow without page-level horizontal scrolling. High-contrast mode substitutes system colors, borders, text labels, and recognizable icons for fills, keeping the ledger meaningful without color. Errors receive both a summary and field guidance.

### Traceability

Ledger, reference prominence, provenance, history, and recovery derive from the **charter**. Ordered sections and edit routes derive from the **priority journey**. Location, photo, disclosure, reference ID, status history, and correction derive from **representative content**. System type, no map, AA intent, high contrast, and 320–1440 px behavior derive from **Fixed constraints**. Palette, hierarchy, layout, and restrained illustration use only named **Open axes**.

### Limitations

This direction is not validation, certification, compliance proof, feasibility proof, brand fit, usability evidence, or a selected solution. Status history is supplied, but timestamps, retention, correction permissions, upload limits, location format, and status vocabulary remain uncertain. The ledger risks becoming a generic stepper unless real provenance and recovery stay central. Specialist reviews still needed: accessibility, privacy/content, service operations, responsive interaction, and front-end feasibility.

### Output B

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

### Output A

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

### Output B

### Visual thesis

The “decision bench” is a calm equipment-room work surface where requests align for comparison, constraints remain adjacent, and decisions stay provisional until confirmation.

### Palette

Use **Workbench Navy #16242C** for text and focus anchors, **Instrument White #F7F8F6** for surfaces, **Gauge Gray #D8DEDC** for rules, **Inspection Blue #176B87** for selection and links, **Caution Amber #A65D00** for conflicts, and **Decision Red #A52A32** for decline actions. The equipment-inspired palette uses the Open color axis; words and shapes accompany every status to support the Fixed accessibility intent.

### Type roles

Use `ui-sans-serif, system-ui, sans-serif`: 20–24 px semibold for the active request, 14–16 px regular for evidence and reasons, and 12–13 px tabular numerals for dates, timestamps, and audit metadata. Native text symbols or CSS-drawn marks always retain visible labels. This honors the Fixed ban on external font and icon packages while supporting the representative content and priority journey.

### Layout rhythm

At 960–1440 px, a compact request queue takes two-fifths of the viewport and a sticky inspection pane three-fifths. Aligned rows expose requester, equipment, dates, conflicts, condition, and status; the pane places evidence, decision controls, then audit trail in reading order. An 8 px spacing base, 44 px controls, restrained corners, and inset rules suggest an equipment ledger (Open layout and hierarchy; charter).

A card grid was rejected because isolated cards weaken comparison and resemble a generic admin dashboard. The split pane is also familiar, so the constraint spine and provisional-action treatment must provide subject-specific character.

### Signature element

A vertical **constraint spine** joins dates, conflicts, condition, provisional choice, and confirmation. Short labels and native markers make reasoning scannable. Approve or Decline attaches a paper-tab-like marker that can be changed or cleared until “Confirm decision” records it (charter; journey). A single 120 ms marker shift provides feedback; reduced-motion preference removes it (accessibility intent).

### States and responsive behavior

Representative rows show requester, equipment, date range, conflict result, condition, and decision status. Detail exposes the reason before confirmation and actor, timestamp, and decision afterward.

Hostile states cover wrapped long names, individually listed date overlaps, “Not recorded” condition, missing decline reason, concurrent decisions, offline failure, empty queues, and long audit histories. Failed confirmation retains provisional input only when confirmed implementation and policy support reliable draft persistence. Otherwise, the interface warns that re-entry may be necessary, then states exactly what was lost and how to restore it.

At 600–959 px, inspection becomes a full-width drill-in with “Back to requests”; at 320–599 px, fields stack without changing reading order. Nothing is hover-only (Fixed range and keyboard-first operation).

### Accessibility intent

DOM order follows queue, evidence, provisional choice, confirmation, and audit trail. Provide a skip link, appropriate table/list semantics, explicit errors, announced status updates, and a visible 3 px focus outline. Tab and Enter remain sufficient even if arrow-key queue navigation is added. Text and controls target WCAG 2.2 AA contrast, 200% zoom resilience, and 44 px targets; color is never the sole signal. Reduced-motion preference removes transitions (Fixed accessibility intent, except motion treatment itself, which follows that intent).

### Traceability

Fixed constraints drive no charts, system typography, native/CSS icons, keyboard behavior, contrast targets, and 320–1440 px adaptation. Representative content determines the displayed fields and hostile states. The priority journey drives comparison, adjacent evidence, reasons, confirmation, and audit placement. The charter drives split context, the spine, and reversible provisional actions. Open axes authorize hierarchy, layout, palette, and native iconography; accessibility intent drives motion restraint.

### Limitations

This clean-room direction derives only from the supplied brief and required frontend-design guidance; no product, repository, research, brand system, or implementation was inspected. It assumes modest request volume and one final actor per decision; both are uncertain. Draft retention depends on unverified policy and implementation. The direction is neither selected nor validated. Accessibility, content-design, operations, responsive-implementation, and usability specialists should review conflict terminology, concurrency, audit retention, failure recovery, focus management, and production contrast.
