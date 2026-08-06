# Steward + frontend-design outputs

## Case 1

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

## Case 2

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

## Case 4

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
