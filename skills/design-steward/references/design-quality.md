# Professional design quality

Use this reference to decide whether a direction is good enough to show, compare, or recommend. This is a craft floor, not representative-user validation or a claim that taste is objective.

## Contents

- Principal-level standard
- Required direction foundations
- Staged artifact funnel
- Screenshot-first review
- Counterfactual tests
- Ecosystem coverage
- Prototype presentation
- Review verdicts

## Principal-level standard

A professional direction must do more than satisfy requirements and render without bugs. It must turn the product's idea into a clear experience with an authored point of view. The product should be recognizable from the interaction, hierarchy, content, and system—not only from its logo or nouns.

Judge the direction on seven inseparable qualities:

1. **Product specificity:** the form grows from this product's users, domain objects, promises, and constraints.
2. **Experience clarity:** the first meaningful action, consequence, navigation, and recovery are immediately understandable.
3. **Interaction authorship:** behavior expresses a coherent mental model instead of assembling standard components.
4. **Visual authorship:** composition, type, color, imagery, material, and motion form a distinctive and disciplined system.
5. **Content voice:** interface language is concrete, age- and context-appropriate, consistent, and useful.
6. **Ecosystem coherence:** priority roles, domains, states, and handoffs feel related without pretending they are the same surface.
7. **Execution finish:** the requested fidelity is resolved across responsive layouts, states, controls, spacing, alignment, and detail.

Do not award professional quality because a rationale is sophisticated, many states exist, CSS is long, or the direction is technically different from siblings.

## Required direction foundations

Freeze these before visual authoring:

- **Experience promise:** one sentence describing what becomes simpler or more powerful for the user.
- **Core act:** the behavior that makes the product itself visible.
- **First-ten-seconds hierarchy:** what the user notices, understands, and can do first.
- **Mental model and interaction grammar:** the repeated rules by which the experience behaves.
- **Visual territory:** a subject-grounded compositional and material idea, not a palette label.
- **Content voice:** tone, vocabulary, density, and example-content rules.
- **Ownable constellation:** two or three mutually reinforcing choices across interaction, structure, content, and visuals. Do not rely on one decorative signature.
- **Anti-goals:** the specific generic patterns, product misunderstandings, and emotional failures this direction must avoid.
- **Decisive journey slice:** the smallest sequence that proves the thesis, including consequence and recovery.

If these read as interchangeable with another product or direction, the charter is not ready.

## Staged artifact funnel

Spend fidelity only after a direction earns it:

1. Generate 12–15 one-paragraph experience concepts in private. Remove clichés, cosmetic variants, and ideas that do not change the user's mental model, structure, interaction, or value proposition.
2. Form six materially distinct territories and create one matched low-fidelity visual or interaction sketch per territory. Show the six-up contact sheet early; do not turn it into six polished direction packages.
3. Select three territories through professional judgment and create one realistic desktop concept frame for each. Include the experience promise, layout silhouette, interaction grammar, type/material territory, and one decisive moment.
4. Show the frames side by side and inspect them before rationales or code. This is progress, not an approval gate. Do not wait for mobile, every state, provenance packaging, or exhaustive assurance.
5. Kill or replace weak directions before detailed journeys. Build one decisive thin slice per survivor: core act plus visible consequence. Revise within the same thesis and author context for no more than two preselection loops by default.
6. Converge on one coherent backbone. Expand it to mobile behavior, the comparison journey, one material recovery state, G4 evidence, and—only after selection—implementation depth.

An explicit request for a fixed number of final directions means replace failed candidates until that count meets the floor. It does not mean ship weak filler.

Use the fidelity-aware check matrix in [rapid-design-loop.md](rapid-design-loop.md). A concept frame does not need to pass selected-direction assurance, and a technically complete prototype does not earn promotion when the frame already fails the relabel, default-cluster, core-act, or first-ten-seconds test.

## Screenshot-first review

Inspect representative rendered output before reading the rationale or source. Use a contact sheet when comparing several directions. For the first visible checkpoint, one representative desktop frame per direction is enough. For final G4 readiness, include:

- the first meaningful entry or return state;
- the core action at its decisive moment;
- the consequence, result, or recovery state;
- one narrow/mobile state for each decisive moment;
- one cross-role or cross-domain handoff when the commissioned scope includes it.

For each direction, record concrete observations—not adjectives—for:

- attention order and competing elements;
- composition, density, rhythm, balance, and whitespace;
- typography roles, line lengths, hierarchy, and tone;
- color, contrast, imagery/material, icons, and motion;
- control affordance, feedback, navigation, and recovery;
- whether responsive behavior preserves the thesis rather than merely stacking blocks;
- whether realistic content strengthens or breaks the design;
- unfinished, inconsistent, awkward, or debug-like details.

At the requested fidelity, obvious placeholder styling, raw native controls without intentional integration, accidental overflow, arbitrary type jumps, inconsistent spacing, unexplained empty space, decorative lines, and state drawers over the product are quality failures.

## Counterfactual tests

Run all tests before G4 readiness:

### Relabel test

Replace the logo and product nouns mentally with an adjacent product. If the direction still works almost unchanged, it is too generic. Identify which structural, behavioral, content, or visual choices must become more product-specific.

### Default-cluster test

Check whether convenience—not the brief—produced a familiar AI cluster. Recurring symptoms include oversized display headlines on sparse fields, condensed or high-contrast type plus monospace eyebrows, off-white or cool-gray surfaces with blue/teal accents, hairline-heavy editorial layouts, interchangeable cards, gradients, floating pills, arbitrary blobs, and one loud accent on otherwise default components. These are not banned. Require a brief-specific reason and execution that could not be swapped into another direction unchanged.

### Silhouette test

Blur the copy and compare page silhouettes. Directions that differ only in type, palette, labels, or decorative marks are siblings, not alternatives. Conversely, visibly different silhouettes are insufficient when the interaction and mental model are the same.

### Core-act test

Hide the product logo and ask what the user is doing and why this product exists. The answer should be clear from the action, object, feedback, and consequence.

### First-ten-seconds test

Name the first three things attention encounters. If reviewer controls, provenance, navigation clutter, status prose, or a giant slogan precedes the user's real job without a deliberate reason, revise.

### Craft test

Zoom into ordinary details: labels, buttons, field states, alignment, spacing, empty areas, icons, focus, long copy, and narrow layouts. A concept is not allowed to use novelty to excuse unfinished fundamentals.

### Family-system test

For multi-role or multi-domain products, verify shared principles and identity without forcing one shell onto different jobs. The relationship should be legible through vocabulary, behavior, and system decisions, not merely the same header and colors.

## Ecosystem coverage

Create a matrix of priority journeys by role, domain, stage, and handoff. Mark each cell as represented, deliberately out of scope, or missing.

An end-to-end direction must show:

- where each priority role enters and orients;
- the core act for each priority role;
- the cross-role or cross-domain object and handoff;
- waiting, failure, consent/authority, and recovery where material;
- how shipped, concept-only, and unavailable capabilities are communicated;
- how the visual and interaction system remains coherent across different jobs.

Do not defer a commissioned role or domain to a future phase and still call the current artifacts end to end. Either represent it at the fidelity needed for the decision or explicitly narrow the decision and obtain approval.

## Art direction and precedent

Use authorized research to escape model defaults. Curate a small visual territory from the subject's materials, cultural context, physical artifacts, editorial forms, tools, or adjacent professional practice. Abstract principles from several sources; do not reproduce a single surface.

Choose fonts, imagery, icons, and motion for a reason. Do not default to system fonts or no imagery solely because they are convenient. When external assets are authorized, prefer rights-clear and durable sources and record provenance. When they are not authorized, build a deliberate code-native or system-native language and name the limitation.

Art direction is more than styling. It coordinates composition, interaction, content, and emotional tone. One novel component on a conventional page is not an authored direction.

## Prototype presentation

Separate the product from the review harness:

- keep state selectors, scenario navigation, artifact IDs, prototype warnings, provenance, hashes, rationale links, and audit controls outside the product viewport;
- make the first-open state a credible product experience, not a review dashboard;
- provide a separate review index or browser frame for switching directions and states;
- show rationale after the artifact, not as a substitute for it;
- ensure direct-file or documented local-server opening works before handoff.

Never let disclaimers and evidence labels dominate the user experience being judged. Preserve them in the surrounding review artifact.

## Review verdicts

Use one verdict per direction:

- **Strong:** product-specific, coherent, complete at the requested fidelity, and worth comparing or converging.
- **Promising — Iterate:** the thesis is valuable, but one or more concrete quality failures must be fixed before comparison.
- **Pivot:** the thesis or mental model is wrong; surface polish will not save it.
- **Reject:** generic, redundant, incoherent, misleading, or materially below the requested fidelity.

G4 readiness requires **Strong** from the Steward's screenshot-first review and no unresolved blocker from any qualified or independently commissioned review that the brief requires. A generated author or critic remains **E0 generated design judgment**, not qualified-human assurance. Preserve disagreements and show the System Owner the artifacts, concrete findings, and trade-offs.

Avoid 100-point scoring by a single model. If numeric scoring is necessary, use a small anchored scale, calibrate it on examples before judging, include multiple independent evaluators where stakes justify it, and report disagreement. Never use a number to rescue a direction that fails the quality floor.
