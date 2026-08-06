# Artifact-pipeline prototype review

> **Prototype verdict, not product validation.** No representative users or future target product were involved.

## Question settled

A reusable Design Steward should not choose one universal canvas. The representative set remained inspectable only because each stage had an editable source, a portable review/export, a stated design question, and a traceable decision record.

## What the representative set exercised

- one realistic journey and structure model expressed as text plus SVG;
- one low-fidelity wireframe expressed as Excalidraw JSON plus SVG;
- three structurally distinct directions over identical content and state;
- responsive layouts, keyboard-visible controls, reduced-motion handling, unavailable and validation states, and visible in-memory state;
- one manifest connecting fidelity, source, review surface, preferred tools, fallbacks, permissions, and limitations.

It deliberately did not test participant collaboration, multiplayer editing, design-system libraries, proprietary imports, cloud authentication, production code generation, or handoff to a target engineering stack. Those require an approved engagement and, where material, a separate pilot.

## Recommended service-independent fidelity ladder

| Step | Smallest useful artifact | Preferred path | Required open fallback | Review surface | Exit question |
| --- | --- | --- | --- | --- | --- |
| Evidence and decision frame | approved Design Brief, evidence/assumption/risk register | Markdown/JSON in the authorized record system | Markdown/JSON/PDF | linked record | Is the question safe and specific enough to explore? |
| Journey and service structure | conditional journey, service map, IA or state flow | Mermaid for deterministic structure; Miro only for authorized facilitation | Mermaid source + SVG/PDF | static render plus source diff | Is the end-to-end task and boundary coherent? |
| Rough alternatives | sketches and wireframes with realistic content | Excalidraw for agent-operable open JSON; Penpot/Figma when team collaboration justifies them | Excalidraw JSON + SVG/PDF | canvas and static export | Are alternatives structurally distinct and complete enough to critique? |
| Editable high-fidelity directions | responsive frames, state/content model, rationale | Penpot as open/self-hostable shared default; Figma when it is the authorized organizational standard and its MCP/API path suffices | SVG/PDF/PNG plus token/content/state data and rationale | native canvas plus browser/static review | Is visual and interaction intent coherent without confusing polish for evidence? |
| Interactive responsive evidence | task-sized clickable behavior with realistic states | code-native HTML/CSS/JS, Storybook, Playwright, and deliberate motion; a design-canvas prototype may precede it | runnable local web artifact + static captures | browser, keyboard, assistive-technology and viewport review | Does the chosen fidelity answer the current behavior/accessibility/feasibility risk? |
| Decision comparison | direction theses, evidence, risks, dissent, rubric scores and recommendation | rendered Markdown/HTML in the decision system | Markdown + PDF | side-by-side presentation with stable links | Which direction, if any, should proceed, iterate, pivot, or stop? |
| Implementation contract | accepted behavior, state, semantics, content/data, responsive, accessibility and instrumentation intent | product-local code/design-system references after approval | Markdown/JSON plus static exports | browser review of the integrated build | Is implementation faithful and testable without promoting prototype code? |

## Tool decisions

### Default portfolio

1. **Mermaid plus SVG/PDF** for versionable journeys, IA, flows, and small diagrams.
2. **Excalidraw plus JSON/SVG** for rough collaborative diagrams and wireframes that an agent can create without a proprietary canvas.
3. **Penpot** as the preferred editable shared-design candidate where open format/self-hosting/control matter; **Figma** when an organization already authorizes and depends on it. Neither is the only decision record.
4. **Code-native HTML/CSS/JavaScript** for the decisive responsive, stateful, keyboard, motion, and implementation-feasibility prototype. Storybook/Playwright may structure and inspect it in a real engagement.
5. **Static HTML/Markdown/PDF with stable artifact links** for comparable decision presentations.

Miro, Webflow, Framer, and tldraw stay specialist options for facilitated discovery, visual publishing, motion-rich sites, or custom canvases—not default mandatory stages.

### Interchange contract

Every artifact record carries: stable identifier; brief/evidence version; question and fidelity; editable source; portable review/export; tool and version; owner; provenance; material assumptions; permissions/data classification; known omissions; and replacement/supersession links.

Preferred interchange formats are text/JSON where structure matters, SVG for editable vector review, PNG only for visual snapshots, PDF for fixed review packets, HTML/CSS/JS for runnable behavior, and documented tokens/content/state data rather than a screenshot-only handoff.

Do not claim round-trip fidelity between services unless tested for that artifact. Imports and exports are delivery paths, not proof that semantics, components, constraints, prototypes, variables, accessibility intent, or comments survived.

## Review surfaces and gates

- **Async inspection:** stable browser/static link plus source, brief version, rationale, limitations, and feedback deadline.
- **Structured critique:** directions remain independent until frozen; reviewers comment against the precommitted rubric and name evidence, risk, and proposed change.
- **Representative-user research:** uses task-sized prototypes, approved terms, realistic content/data, accessible materials, and a qualified researcher. It is the only review surface here that may support usability claims about representative users.
- **Accessibility review:** combines standards-based automated and manual evaluation with disabled-user research where relevant; a design canvas cannot establish conformance.
- **Decision review:** shows direction theses side by side, not as a blended mood board; the Steward recommends and preserves dissent, while the Product Owner decides.

## Cloud-unavailable fallback

The engagement continues locally with Mermaid source/SVG, Excalidraw JSON/SVG, code-native prototypes, and Markdown/HTML/PDF decision records. The fallback is considered workable only if reviewers can inspect the artifact, trace it to evidence and constraints, run or view it without proprietary credentials, and reconstruct the current decision even if they cannot round-trip it into the preferred cloud service.

## Verdict

Adopt the ladder and interchange contract above. Treat Penpot and Figma as interchangeable candidates only at the capability level—not as file-equivalent systems. Make code-native browser prototypes the decisive path when responsive behavior, state, keyboard interaction, accessibility, motion, or implementation feasibility matters. Require an open static or runnable review surface at every stage, and keep prototype code disposable by default.
