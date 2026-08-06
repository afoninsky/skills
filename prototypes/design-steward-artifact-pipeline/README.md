# Design Steward artifact-pipeline prototype

> **THROWAWAY PROTOTYPE — never production code.**

## Question

Can one service-independent artifact set carry a design decision from journey and information structure through wireframe, three distinct responsive directions, interactive behavior, and a decision review—while remaining inspectable when preferred cloud tools are unavailable?

## Representative scenario

- **Subject:** rescheduling a community repair-session booking.
- **Audience:** residents bringing an item to volunteer repairers, including keyboard and reduced-motion users.
- **Single job:** choose a viable replacement time and understand what changes before confirming.
- **Why this scenario:** it exercises time comparison, realistic constraints, content hierarchy, destructive/change consequences, error states, responsive behavior, and accessible interaction without importing a target product.

## Run

From this directory:

```sh
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173/` and switch with the floating bar or URL:

- `?variant=A` — Workbench board
- `?variant=B` — Guided route
- `?variant=C` — Parts ledger

Use Left/Right Arrow outside form controls to cycle variants. The prototype is read-only; confirmation only exposes the resulting in-memory state.

## Visual plan

- **Palette:** Workshop blue `#16324f`, safety orange `#e4572e`, cool enamel `#e8eff1`, graphite `#20252b`, bench green `#2d6a4f`, chalk `#ffffff`.
- **Type:** Rockwell/Georgia for restrained workshop headings, Avenir Next/system sans for task copy, SFMono/Menlo for status and artifact labels.
- **Layout thesis:** the same decision should survive a spatial board, a linear guided flow, and a dense comparison ledger.
- **Signature:** a perforated repair-ticket summary that makes the reservation and its consequences the stable object across all three directions.
- **Aesthetic risk:** visible workshop registration marks and an asymmetric board composition; retained because they encode assembly and sequence rather than acting as decoration.

### Self-critique

The first plan paired warm paper, a slab-serif heading, and rust-orange accents. That sat too close to a common generated-design formula. The ground shifted to cool workshop enamel, while orange is restricted to registration, warning, and active-selection cues. The subject still reads as a repair bench without borrowing a fashionable editorial palette.

## Artifact ladder

| Fidelity | Source artifact | Portable review/export | Question answered |
| --- | --- | --- | --- |
| Journey | `journey.mmd` | `journey.svg` | Where does rescheduling begin and what must remain visible? |
| Structure | `ia.mmd` | `ia.svg` | Which content and actions belong together? |
| Wireframe | `wireframe.excalidraw` | `wireframe.svg` | Can the critical information fit before visual styling? |
| Directions | `index.html`, `styles.css` | browser, screenshot, print/PDF | Which hierarchy and comparison model deserves testing? |
| Interaction | `app.js` | browser plus visible state ledger | Do selection, errors, and confirmation behave coherently? |
| Decision | `decision-review.md`, `artifact-manifest.json` | Markdown/JSON | Can a reviewer trace the recommendation and fallbacks? |

Every stage keeps an editable source and an open, static review surface. A cloud canvas may replace or complement a source artifact during a real engagement, but never becomes the only inspectable record.
