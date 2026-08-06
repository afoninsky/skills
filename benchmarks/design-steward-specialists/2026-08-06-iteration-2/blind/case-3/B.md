## Visual thesis

Treat the service as a civic record before it is a form. The page should make the request’s present status, source, and amendment path immediately legible. A narrow “record spine” carries the reference, current state, and supplied history; form content attaches to it as clearly labeled evidence. Visual character comes from registration marks, ruled fields, and explicit provenance labels, not ornamental polish.

## Palette

Use warm paper (`#F7F5EF`) for the canvas, near-black ink (`#171A1C`) for text, and white for task surfaces. Deep municipal blue (`#164E63`) supports primary actions and strong rules; a muted ochre (`#8A5A00`) flags attention; dark red (`#8B1E2D`) identifies errors. Every status also has a text label and distinct border or shape treatment. High-contrast modes retain meaningful borders, controls, and status markers without fills.

## Type roles

Use the system sans-serif stack only. The page title is 32/38 at large widths and 26/32 on small screens. Section headings are 20/26, field labels 16/22 semibold, body and controls 16/24, and metadata 14/20 with sufficient contrast. Reference IDs use a system monospace stack for character distinction and wrapping. Sentence case and plain verbs keep the voice administrative but humane.

## Layout rhythm

At 960–1440 CSS pixels, use a centered 1120-pixel maximum grid: an approximately two-thirds task column and one-third record spine, separated by a 32-pixel gutter. Below 960, the spine becomes a full-width summary before the active task. At 320, all content is single-column with 16-pixel margins. Spacing follows an 8-pixel rhythm, with 24 pixels between related groups and 40 between stages. Category choices, approximate text location, description, photo-presence indication, and privacy disclosure each occupy bounded sections. No map surrogate is introduced.

## Signature element

The “record edge” is a continuous left rule interrupted by labeled notches for submitted material, supplied history, current status, and correction route. It evokes a maintained public ledger while remaining functional: each notch marks a provenance change. The rule never carries meaning alone; adjacent headings and plain-language labels do. A restrained line illustration of a garden fixture may appear only in an outer margin on wide screens, never between fields, actions, status, or recovery guidance.

## States and responsive behavior

Categorization precedes location and description; privacy review precedes submission. The review surface repeats entered information, explicitly states whether a photo is present, and provides edit links. After submission, the reference ID and current status lead, followed by the supplied history and correction route. Upload and submission failures appear next to the affected action and in a focusable summary, with the failed item, known consequence, and available retry or return path stated only when the system can establish them. The interface must not imply that unsent work persisted. On narrow screens, history remains ordered vertically; long IDs and descriptions wrap rather than scroll horizontally.

## Accessibility intent

Controls target at least 44 by 44 CSS pixels where feasible, with persistent labels, programmatic descriptions, and a clearly visible two-pixel focus indicator offset from component edges. Keyboard order follows the visual journey. Errors identify the field and corrective action in text; live announcements are reserved for meaningful status changes. Headings, landmarks, disclosure structure, and history lists expose hierarchy to assistive technology. Motion is unnecessary. These choices express WCAG 2.2 AA intent, not a claim of conformance or testing.

## Traceability

Category, approximate location, description, and optional photo presence map to the intake sections. Privacy disclosure maps to the mandatory review gate. Reference ID, current status, and supplied history map to the record spine and post-submit view. The correction route is a persistent labeled action beside the record. Upload and submission failures map to contextual recovery plus the summary. Responsive, system-font, no-map, focus, contrast, and non-color status constraints shape every component rather than appearing as afterthoughts.

## Limitations

The brief does not define categories, actors, status vocabulary, history entries, timestamps, retention, correction permissions, service-level timing, or persistence behavior. The design therefore shows structural slots and conditional language only; production copy and enabled actions must be derived from authoritative service rules. Palette contrast is specified by intent and candidate values but still requires implementation-level measurement, zoom, forced-colors, keyboard, screen-reader, and failure-path evaluation before release.
