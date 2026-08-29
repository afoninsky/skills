# Rendering, quality, and platform coverage

## Matched render contract

Every compared render records:

- direction ID and source hash;
- surface and deterministic fixture/state;
- exact pixel dimensions, scale, orientation, theme, locale, and text scale;
- renderer/editor and version;
- fonts/assets loaded and any substitutions;
- crop rule and output path;
- capture timestamp only when needed for traceability.

Use one manifest for the contact sheet. Do not compare a polished desktop success state with another direction's mobile error state.

## Platform adapters

Load only the applicable row:

| Architecture | Candidate medium | Required direction checks |
| --- | --- | --- |
| Responsive web | Penpot or disposable HTML/CSS in a real browser | small/large reflow, zoom risk, keyboard/pointer/touch hierarchy, long copy |
| React Native | RN preview/Storybook or structured design frames | phone/tablet, platform conventions, safe areas, keyboard, font scale |
| Flutter | Widgetbook/widget preview or structured design frames | constraints, phone/tablet, text scale, orientation, Material/Cupertino adaptation |
| SwiftUI/UIKit | Xcode preview or structured design frames | size classes, Dynamic Type, safe areas, native control/gesture expectations |
| Compose/Views | Compose preview/layout fixture or structured design frames | window classes, font/display scale, insets, native control/gesture expectations |
| PWA/web wrapper | one responsive web direction plus shell captures | WebView/safe-area/keyboard/native-back implications; do not invent a second UI source |

At Gate B these may be design renders rather than production runtime, but they must be actual pixels at the named targets. Record which platform behaviors remain prototype risks.

The matrix is representative rather than exhaustive: one or more rows must cover every materially distinct implementation/adaptation class named by the route, while explicit exclusions bound the claim. All finalists use the same rows. A shared web wrapper has one design source but separate browser and shell rows; those rows do not imply separate visual directions.

## Quality lenses

Use qualitative evidence, not a composite score:

- **First ten seconds:** is the core act and current state immediately legible?
- **Silhouette:** does the composition have a purposeful recognizable shape at thumbnail scale?
- **Relabel:** after replacing product words, does the design still have a coherent product-specific grammar rather than a template?
- **Default cluster:** is it distinguishable from framework defaults and fashionable generic patterns for a reason?
- **Core-act emphasis:** does visual hierarchy favor the actual job rather than branding or chrome?
- **Craft:** are spacing, type, alignment, optical balance, state transitions, and details resolved consistently?
- **Family/system:** can related states and surfaces plausibly belong to this backbone without one-off styling?
- **Content truth:** does real long/empty/error content preserve hierarchy and dignity?
- **Adaptive truth:** does the grammar transform intentionally rather than merely shrink?

Name observable evidence and remaining risk. Avoid self-awarded “9/10” scores.

## Accessibility risk review

Direction work cannot prove full accessibility, but it must expose risks before selection:

- color contrast and non-color state cues;
- type sizes, line length, text zoom/scaling, and truncation;
- focus/order and visible focus concept;
- touch targets and gesture alternatives;
- motion/reduced-motion concept;
- semantics implied by custom controls;
- reading order after responsive rearrangement.

A beautiful candidate that depends on inaccessible contrast, tiny type, hidden state, or gesture-only control is not a viable finalist unless the issue is corrected and re-rendered.

## Asset provenance

Record creator/source, license, allowed transformations, download date, and local Git path for fonts, icons, photography, illustration, or generated imagery. Mark generated assets as generated and retain the prompt/reference provenance permitted by the tool. Do not copy identifiable product UI as an asset.
