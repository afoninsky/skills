# Agent-operable visualization and prototyping services

_Research date: 2026-08-06_

## Executive answer

No single current service is the best agent-operated environment for information architecture, journey mapping, high-fidelity UI, interaction, motion, collaboration, accessibility, and portable delivery. The practical choice is a small portfolio whose handoffs are explicit:

1. **Mermaid or Excalidraw for structure and alternatives.** Mermaid is the most deterministic option for architecture, flows, states, and journeys because an agent edits reviewable text and renders it locally to SVG, PNG, or PDF. Excalidraw is better when the result should remain an informal, spatially arranged, human-editable canvas.
2. **Penpot or Figma for an editable design canvas.** Penpot is the strongest open, self-hostable option and now has an official MCP path. Figma has the deepest agent-facing canvas toolset, including editable capture from running UI and native canvas mutation, but its writes depend on seat, permission, beta tooling, and a proprietary file format.
3. **Code-native HTML/CSS/JavaScript (often React) for the decisive prototype.** It produces the highest-fidelity responsive, clickable, animated, and testable artifact. Storybook, Playwright, and Motion make component states, interaction, visual regression, accessibility checks, and reduced-motion behavior agent-operable. It is also the most portable result, though it costs more engineering effort than arranging a canvas.
4. **Webflow when the prototype is intended to become a visual production website.** Its official MCP is now largely headless, its Designer API covers visual primitives, its animation system is strong, and code/component export offers a partial exit. Publishing and several product features remain platform-dependent.
5. **Miro for collaborative discovery and early click-throughs; Framer for fast, motion-rich marketing experiences.** Miro combines journeys, diagrams, comments, workshops, wireframes, and early multi-screen prototypes. Framer combines a headless Server API with a strong motion model, but has the highest delivery lock-in because published sites cannot be exported as HTML for self-hosting.

The default recommendation is therefore **Mermaid/Excalidraw → Penpot/Figma → code-native**, with Miro, Webflow, or Framer selected when their collaboration or publishing model is the actual requirement. Browser automation should be a fallback, not the primary interface: official MCP, API, CLI, SDK, or structured-file writes are more observable and less vulnerable to layout changes, authentication dialogs, focus problems, and canvas coordinates.

## Evaluation method

“Agent-operable” here means that an agent can create or materially edit an artifact through a documented interface—not merely describe what a human should draw. The interfaces were ranked in this order:

1. structured source or file format that can be diffed and validated;
2. CLI or headless SDK/API;
3. official MCP server;
4. plugin or bridge that requires a live editor session;
5. browser automation over the product UI.

The first four paths have product-defined semantics. Browser automation is still useful for preview, acceptance, and gaps in an API, but is a fragile authoring substrate and often stops at OAuth, CAPTCHA, administrator consent, file permissions, font dialogs, or publishing confirmation.

Capability ratings below are an author assessment based on the documented primitives and outputs, not vendor benchmarks:

- **●** strong fit with a supported agent write path;
- **◐** possible, but constrained, indirect, or dependent on an add-on/custom implementation;
- **—** not a realistic primary use.

## Capability matrix

| Path | IA / flows | Journeys | Wireframes | High-fidelity responsive UI | Click-through | Motion / storytelling | Comparable alternatives | Best agent interface |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Mermaid CLI | ● | ● | ◐ | — | — | ◐ | ● | Text + CLI |
| Excalidraw + official MCP | ● | ● | ● | ◐ | — | — | ● | MCP or open JSON scene |
| Miro | ● | ● | ● | ◐ | ● | ◐ | ● | Remote MCP / REST API |
| Penpot | ● | ◐ | ● | ● | ● | ◐ | ● | Remote/local MCP + plugin API |
| Figma / FigJam | ● | ● | ● | ● | ● | ● | ● | Remote MCP + Plugin API |
| tldraw SDK | ● | ◐ | ● | ◐ | ◐ | ◐ | ● | TypeScript SDK + validated store |
| Code-native + Storybook | ◐ | ◐ | ● | ● | ● | ● | ● | Source files + CLI/test runner |
| Webflow | ◐ | ◐ | ● | ● | ● | ● | ● | Remote MCP / Designer API |
| Framer | ◐ | ◐ | ● | ● | ● | ● | ● | Server API / Plugin API |

## Decision matrix

| Path | Output ceiling | Collaboration | Accessibility evidence | Portable formats and lock-in | Cost and operational gates |
|---|---|---|---|---|---|
| Mermaid | Precise diagrams; limited visual polish and interactivity | Git/review workflow rather than live canvas | Diagram source supports `accTitle` and `accDescr`, emitted as SVG title/description and ARIA metadata | `.mmd` text plus SVG/PNG/PDF; MIT; very low lock-in | Free local tooling; Node or container runtime |
| Excalidraw | Excellent sketch-like diagrams and wireframes; not a click-through system | Hosted app offers real-time collaboration; MCP App keeps output interactively editable | No verified claim that an exported scene is an accessible interactive artifact; provide a text alternative | Open `.excalidraw` JSON plus SVG/PNG; MIT; low lock-in | Free/open-source core; MCP-capable client or self-hosted server |
| Miro | Strong discovery canvas and early multi-screen prototype; moderate visual ceiling | Best-in-class workshop, comments, and shared-board flow | Board accessibility checker and assistive-technology guidance; prototype still needs artifact-level testing | Static JPG/PDF/SVG/CSV export; `.rtb` backup restores only to Miro; medium-high lock-in | Per-member cloud plans; MCP daily limits; Enterprise admin may need to enable MCP; prototype entitlement varies by plan/add-on |
| Penpot | Strong editable UI and prototype canvas; motion is basic relative to web-native output | Real-time collaboration and shareable prototype view | Design-time plugins/checklists help; no evidence that a visual prototype itself satisfies WCAG | Inspectable ZIP+JSON `.penpot`, SVG/PNG/JPEG/WebP/PDF; MPL-2.0 and self-hostable; low-medium lock-in | Cloud or free self-hosted Professional edition; remote token or a browser file/plugin kept open for local MCP |
| Figma | Strongest general-purpose design canvas; editable code-to-canvas capture and prototype animation | Mature shared files, components, comments, branches and prototype links | Accessible-prototype mode maps selected layers to HTML-like roles; unavailable on mobile and still requires deliberate semantics | Static PNG/JPG/SVG/PDF; local `.fig` is proprietary and explicitly not a stable third-party interchange format; medium-high lock-in | Seat/plan-dependent limits; Full seat plus edit permission for many writes; some tools are beta; custom fonts and some assets require human handling |
| tldraw | Strong custom infinite-canvas foundation; product prototype behavior must be built | Sync primitives exist, but the adopter owns integration | SDK documents WCAG 2.2 AA, keyboard, screen-reader, focus, reduced-motion, and ARIA support | Typed JSON-like records plus SVG/PNG/JPEG/WebP; source available but production use requires a tldraw license; medium lock-in | Development is free; production needs trial, commercial, or approved hobby key |
| Code-native | Highest: real responsive behavior, data states, navigation, gestures, and production-grade motion | Git/PR collaboration; Storybook share/hosting optional; weaker synchronous spatial editing | Semantic HTML plus automated axe checks, browser tests, keyboard testing, and manual assistive-tech evaluation | HTML/CSS/JS/source and standard assets; major tools cited here are permissively licensed; lowest artifact lock-in | Tooling is free; engineering, review, hosting, and maintenance are the cost |
| Webflow | High for responsive marketing/content sites and sophisticated GSAP/Rive motion | Cloud Designer collaboration, comments, roles, branches on applicable plans | Audit panel covers common alt, heading, contrast, and ID issues; manual evaluation remains necessary | Paid code export yields HTML/CSS/JS/assets, but excludes CMS, ecommerce, accounts, localization and other platform functions; medium lock-in | Free entry tier and paid site/workspace plans; OAuth role gate; some bridge actions require an open Designer session |
| Framer | High for responsive, motion-rich marketing prototypes/sites | Live collaboration, preview links, branches, review and merge | Semantic tags, alt text, tab order and reduced-motion controls are available; authors must configure them | No HTML export or self-hosting; production delivery remains on Framer; very high lock-in | Free entry tier and paid site/editor plans; project API key and deploy permission; Server API is still beta |

## Detailed findings

### 1. Mermaid: the deterministic baseline

The Mermaid CLI accepts Mermaid text and renders SVG, PNG, or PDF through a local command, Docker image, or Node API. Its source is MIT-licensed. Mermaid covers flowcharts, state and sequence diagrams, timelines, user journeys, and architecture diagrams, making it the cleanest way for an agent to produce multiple comparable structural alternatives that can be reviewed as text and regenerated deterministically. [[Mermaid CLI](https://github.com/mermaid-js/mermaid-cli)] [[Mermaid syntax index](https://mermaid.js.org/intro/syntax-reference.html)]

Accessibility metadata is unusually explicit for a diagram tool: `accTitle` and `accDescr` are supported across diagram types and are emitted into SVG title/description elements with ARIA metadata. This improves the exported diagram, but does not turn a diagram into an operable product prototype. [[Mermaid accessibility](https://mermaid.js.org/config/accessibility.html)]

Use Mermaid for IA, service blueprints that fit a graph, user journeys, storyboards expressed as sequence/state/timeline diagrams, and alternative flow comparisons. Move to a spatial canvas when freeform composition matters, and to code when interaction is the question under test.

### 2. Excalidraw: open, editable low-fidelity visual thinking

Excalidraw is an MIT-licensed React canvas for hand-drawn diagrams and wireframes. The project documents open `.excalidraw` JSON scenes, SVG/PNG export, a local-first PWA, end-to-end encrypted real-time collaboration in the hosted product, and embeddable React components. Its export utilities can produce SVG, canvas, or blobs; an exported image can embed the scene so it remains editable. [[Excalidraw repository](https://github.com/excalidraw/excalidraw)] [[Excalidraw export and persistence guidance](https://github.com/excalidraw/excalidraw/discussions/3778)]

The official Excalidraw MCP server can be used remotely or self-hosted. In MCP Apps-capable clients it streams the generated diagram into an interactive viewport so the human can keep editing it rather than receiving only a screenshot. That makes Excalidraw a realistic agent/human co-editing surface for wireframes, journeys, system maps, and side-by-side concepts. [[Official Excalidraw MCP](https://github.com/excalidraw/excalidraw-mcp)]

Its limit is equally useful: Excalidraw is not a native click-through or motion prototype. Treat it as a visual thinking artifact. Because no primary source reviewed here establishes an accessible interactive export, accompany important canvases with structured text and do not use a canvas image as the only specification.

### 3. Miro: collaborative discovery with early prototype capability

Miro's official remote MCP server uses OAuth 2.1 and can create boards, layouts, diagrams, tables, images, documents and comments, as well as search and read boards. Its diagram tool accepts a documented DSL, which gives an agent a more stable surface than UI clicks. The REST API remains available for board and item CRUD. [[Miro MCP introduction](https://developers.miro.com/docs/mcp-intro)] [[Miro MCP versus REST](https://developers.miro.com/docs/mcp-server-vs-rest-api)]

This combination is well suited to journeys, workshop boards, IA, service maps, and parallel alternatives. Miro Prototypes adds editable multi-screen prototypes, hotspots, preview, AI refinement, and screenshot-to-editable conversion. The feature is aimed at early-stage product exploration rather than production fidelity, and current entitlement depends on the account's Business/Enterprise plan or add-on. The older wireframe library remains available for basic UI composition. [[Miro Prototypes](https://help.miro.com/hc/en-us/articles/26654269713682-Miro-Prototypes)] [[Miro Prototypes overview](https://help.miro.com/hc/en-us/articles/26654102601874-Miro-Prototypes-overview)] [[Wireframe library](https://help.miro.com/hc/en-us/articles/28149231434514-Wireframe-library-LEGACY)]

The collaboration advantage comes with gates. A user authorizes the MCP to a specific team; Enterprise administrators can disable it. Daily tool-call allowances are plan-dependent, currently ranging from 100 on Free to 10,000 on Enterprise. [[Connecting Miro MCP](https://developers.miro.com/docs/connecting-to-miro-mcp)] [[Miro MCP limits](https://developers.miro.com/docs/mcp-usage-and-daily-limits)]

Miro exports JPG, PDF, SVG, and CSV, but CSV loses most spatial relationships. A native `.rtb` backup is paid-plan functionality and can only be restored into Miro. That creates more lock-in than the visual exports suggest. [[Miro board export](https://help.miro.com/hc/en-us/articles/360017572754-How-to-export-your-board)] [[Miro board backup](https://help.miro.com/hc/en-us/articles/360017572774-How-to-save-board-backup)]

Miro provides an accessibility checker for contrast, image descriptions, and container titles, and documents keyboard, screen-reader, and voice-control use. Those checks make a well-structured board easier to consume; they are not evidence that a click-through accurately models accessible production behavior. [[Accessible Miro boards](https://help.miro.com/hc/en-us/articles/4403828924306-How-to-make-your-Miro-boards-more-accessible)] [[Assistive technologies](https://help.miro.com/hc/en-us/articles/4403828752274-How-to-access-Miro-boards-with-assistive-technologies)]

### 4. Penpot: the strongest open design-canvas option

Penpot is an MPL-2.0 design and prototyping platform with real-time collaboration, a plugin system, cloud hosting, and supported self-hosting. Its `.penpot` v3 file is a ZIP containing inspectable JSON and binary assets; layers can also export as SVG, PNG, JPEG, WebP, or PDF. This is a meaningfully better portability story than proprietary local backup files, although semantic round-tripping across design products is never lossless. [[Penpot repository](https://github.com/penpot/penpot)] [[Penpot file format](https://help.penpot.app/technical-guide/developer/data-model/penpot-file-format/)] [[Exporting layers](https://help.penpot.app/user-guide/export-import/exporting-layers/)] [[Self-hosting guide](https://help.penpot.app/technical-guide/getting-started/)]

The official MCP can run remotely with a user token or locally through `@penpot/mcp`. It can read and modify components, styles, tokens, pages, and layers. The local architecture connects the server to a Penpot plugin over WebSocket; the relevant Penpot file and plugin UI must remain open and connected. The agent can execute code in the Penpot plugin environment, so the setup should be treated as a privileged design-file write channel. [[Penpot MCP guide](https://help.penpot.app/mcp/)] [[Official Penpot MCP repository](https://github.com/penpot/penpot-mcp)]

Penpot prototypes connect boards/screens through triggers, actions, overlays, navigation, and transition animations, and can be shared in View mode. This supports credible responsive screen and click-flow validation, but the animation vocabulary is less suitable for rich web storytelling than Framer, Webflow, or code. [[Penpot prototyping](https://help.penpot.app/user-guide/prototyping-testing/prototyping/)]

The self-hosted Professional edition is advertised as free with unlimited users, files, and core features; paid Enterprise self-hosting adds governance such as SSO, audit and plugin controls. Cloud and commercial terms should still be rechecked at adoption time. [[Penpot self-host pricing](https://penpot.app/pricing/self-host)]

Penpot publishes accessibility-oriented design guidance and plugins for contrast/checklists. These are useful design-time aids, not a claim that a visual prototype exposes production semantics. Validate the implemented HTML separately. [[Penpot accessible-design checklist](https://penpot.app/blog/accessible-design-checklist/)]

### 5. Figma: the deepest general-purpose agent canvas

Figma's official remote MCP is the broadest native design-canvas interface reviewed. It can generate editable FigJam diagrams from Mermaid, capture a live web UI into standard editable Figma layers, create new files, and use a general `use_figma` tool to inspect, create, edit, move, and delete pages, frames, components, variants, variables, styles, text, and images. Code Connect can link design components to implementation. [[Figma MCP overview](https://developers.figma.com/docs/figma-mcp-server/)] [[Figma MCP tools](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)] [[Code to canvas](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/)]

The general canvas tool executes JavaScript through Figma's Plugin API. It currently carries practical limits: writing requires a Full seat and edit permission, the tool is beta, output per call is limited, custom fonts are unsupported, and some asset/component publication tasks require manual handling or review. Access and read-call limits vary by seat and plan, and only catalogued MCP clients are supported. [[Writing to the Figma canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)] [[Figma MCP access and limits](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/)]

Figma prototypes support triggers, navigation and other actions, overlays, Smart Animate, easing/spring transitions, and responsive presentation using constraints and auto layout. This makes it strong for comparing alternatives and testing screen-level flow before implementation. [[Prototype interactions](https://help.figma.com/hc/en-us/articles/360040315773-Create-interactions)] [[Playing responsive prototypes](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes)]

Accessible-prototype mode can map layers to HTML-like roles: click targets can appear as buttons/links, list links as lists, image layer names as alt text, frames as sections, and layer order as tab order. It is limited to desktop browser/app presentation and depends on deliberate authoring, so it should be treated as an accessibility review aid rather than conformance proof. [[Accessible prototypes](https://help.figma.com/hc/en-us/articles/7810391964695-Accessible-prototypes-in-Figma)]

Static export covers PNG, JPG, SVG, and PDF. A local `.fig` backup is proprietary, may change, omits comments/history, and reimports as a disconnected new file; Figma explicitly warns third parties not to parse it. This is the central lock-in cost. [[Figma export formats](https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings)] [[Figma local copies](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files)]

### 6. tldraw: an agent-programmable canvas substrate

tldraw is best evaluated as a TypeScript/React SDK, not as a turnkey prototype service. An agent can manipulate a validated record store without the renderer, persist JSON-like snapshots locally or remotely, integrate sync, and export self-contained SVG, PNG, JPEG, or WebP with embedded fonts and media. This is a strong base for a domain-specific diagramming or comparison tool when generic canvases are insufficient. [[tldraw store](https://tldraw.dev/sdk-features/store)] [[tldraw persistence](https://tldraw.dev/sdk-features/persistence)] [[tldraw image export](https://tldraw.dev/sdk-features/image-export)]

The SDK documents keyboard navigation, focus management, screen-reader support, reduced motion, ARIA attributes, and a WCAG 2.2 AA target. That is stronger substrate-level accessibility evidence than most infinite canvases provide, but custom shapes and interactions still inherit responsibility from the implementer. [[tldraw accessibility](https://tldraw.dev/features/composable-primitives/accessibility)]

tldraw's source is available under its own license, not a permissive open-source license. Default use is for development; production requires a time-limited trial, commercial key, or approved hobby license, and the hobby license carries a watermark. There is no official MCP required for agent operation: the agent writes against the SDK and store. The adopter also owns the product-specific click-through, hosting, data model, and collaboration integration. [[tldraw license](https://tldraw.dev/community/license)] [[tldraw repository](https://github.com/tldraw/tldraw)]

### 7. Code-native: the fidelity, testing, and portability winner

A code-native prototype is an actual web application: responsive layout, focus behavior, validation, data states, URL navigation, device input, and animation can all be real rather than simulated. Vite and React are MIT-licensed foundations; Motion is an MIT-licensed animation library with gestures, layout and scroll animation, and an explicit reduced-motion hook. [[Vite repository](https://github.com/vitejs/vite)] [[React repository](https://github.com/facebook/react)] [[Motion repository](https://github.com/motiondivision/motion)] [[Motion for React](https://motion.dev/docs/react)] [[Reduced-motion hook](https://motion.dev/docs/react-use-reduced-motion)]

Storybook isolates component states and supports scripted interaction in stories. Its accessibility addon runs axe checks locally and in CI; Storybook notes that automated checks find only a portion of WCAG issues. Playwright drives Chromium, Firefox, and WebKit in headless or headed mode, emulates devices, records screenshot baselines, and integrates axe for page-level scans. [[Storybook interaction testing](https://storybook.js.org/docs/9/writing-tests/interaction-testing)] [[Storybook accessibility testing](https://storybook.js.org/docs/writing-tests/accessibility-testing)] [[Playwright introduction](https://playwright.dev/docs/intro)] [[Playwright visual comparisons](https://playwright.dev/docs/test-snapshots)] [[Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing)]

This path is naturally agent-operable through source edits, CLI commands, screenshots, browser inspection, tests, and version control. It is the best way to produce several comparable alternatives because variants can share components, fixtures, and tests while differing in layout or interaction. Its trade-off is engineering cost: design decisions become implementation decisions earlier, and synchronous nontechnical co-editing is weaker than a canvas. The Web Accessibility Initiative is explicit that tools alone cannot determine accessibility; knowledgeable human evaluation remains required. [[W3C evaluating tools overview](https://www.w3.org/WAI/test-evaluate/)]

### 8. Webflow: visual production with a growing headless surface

Webflow's official remote MCP v2 uses OAuth and is now largely headless. It exposes site, page, component, style, variable, CMS, asset, font, comment, and branch operations. The live Designer bridge is still used for selected visual context such as the current selection, page, mode, viewport, breakpoints, and visual snapshots. This separation makes API/MCP writes practical while preserving an optional human-in-the-loop canvas. [[Webflow MCP architecture](https://developers.webflow.com/mcp/reference/how-it-works)] [[Webflow MCP changelog](https://developers.webflow.com/home/changelog)] [[Webflow Designer tools](https://developers.webflow.com/mcp/tools/designer-tools)]

Authorization is a human gate: only owners, administrators, or site managers can connect an AI tool, and Webflow applies the user's permissions and logs agent activity. The Designer API provides another JavaScript route to pages, elements, styles, variables, components, and assets through a Designer extension. [[Connecting Webflow MCP](https://help.webflow.com/hc/en-us/articles/52536616701971-Connect-your-AI-tools-to-the-Webflow-MCP-server)] [[Designer API](https://developers.webflow.com/designer/reference/introduction)]

Webflow's Interactions with GSAP supports timelines, staggers, SplitText, ScrollTrigger, advanced easing, responsive previews, collaboration, and `prefers-reduced-motion`; Rive animations can also be driven by interactions. This is the best cloud visual-builder choice in the set for scroll-led storytelling and motion that may proceed to a production site. [[GSAP interactions](https://help.webflow.com/hc/en-us/articles/46300264646803-Interactions-with-GSAP-vs-Classic-Interactions)] [[Rive interactions](https://help.webflow.com/hc/en-us/articles/50272089911059-Control-Rive-animations-with-Interactions-with-GSAP)]

The Audit panel detects several common alt-text, heading, contrast, duplicate-ID, and content issues, but its documented scope has exceptions and cannot replace manual testing. [[Webflow Audit panel](https://help.webflow.com/hc/en-us/articles/33961313088531-Intro-to-the-Audit-panel)]

Portability is partial. Paid code export produces HTML, CSS, JavaScript, and assets without required Webflow attribution, but excludes CMS content/functionality, ecommerce, user accounts, localized content, code components, forms/search processing, and other hosted behavior. DevLink can export selected Webflow components as generated React/CSS and preserve interactions, but generated files are overwritten on re-export and should not be hand-edited. [[Webflow code export](https://help.webflow.com/hc/en-us/articles/33961386739347-How-do-I-export-my-Webflow-site-code)] [[DevLink component export](https://developers.webflow.com/devlink/docs/component-export)] [[What DevLink exports](https://developers.webflow.com/devlink/docs/component-export/whats-exported)]

Webflow has a free entry plan and paid site/workspace plans; MCP is included on the Starter tier, while publishing, collaboration and export capabilities vary. Recheck current pricing and entitlements before choosing it for delivery. [[Webflow pricing](https://webflow.com/pricing)]

### 9. Framer: fast motion-rich sites with the strongest lock-in

Framer's official Server API is a headless JavaScript/TypeScript interface that can update a project, manage canvas/CMS/settings, create a preview deployment, and deploy to production. It shares most capabilities with the Plugin API and uses a project-bound API key. Framer's own documentation shows building a custom MCP on top of this API; there is not an official hosted Framer MCP in the sources reviewed. [[Framer Server API](https://www.framer.com/developers/server-api-introduction)] [[Server API reference](https://www.framer.com/developers/server-api-reference)] [[Server API quick start](https://www.framer.com/developers/server-api-quick-start)]

The Plugin API can create and edit canvas nodes, components, styles, assets, code files, and CMS data. UI-less plugins still require Framer to be open, whereas the Server API is headless. The Server API is currently an open beta, so production automation should pin versions, preview first, and retain a human deploy gate. [[Framer Plugin API reference](https://www.framer.com/developers/reference)] [[Server API announcement](https://www.framer.com/updates/server-api)]

Framer's animation model is built on Motion and exposes hover, tap, drag, layout, scroll and loop effects, with Code Components/Overrides available for deeper behavior. Live collaboration, preview links, and branches support human review and parallel agent work before merge. [[Framer animations](https://www.framer.com/help/articles/how-animations-and-effects-work-in-framer/)] [[Live collaboration](https://www.framer.com/help/articles/live-collaboration-in-framer/)] [[Framer branches](https://www.framer.com/help/articles/how-to-use-branches-in-framer/)]

Accessibility controls include semantic tags, alt text, tab order and reduced-motion settings, but the author must configure the design and content correctly. [[Framer accessibility guide](https://www.framer.com/help/articles/guide-to-web-accessibility-in-framer/)]

The decisive constraint is portability: Framer states that sites cannot be exported as HTML or self-hosted and require Framer hosting. It has a free entry tier and paid site/editor plans; external agent access is currently promoted during preview, but pricing and beta terms can change. [[Framer HTML export policy](https://www.framer.com/help/articles/can-i-export-my-website-to-html-and-self-host-it/)] [[Framer pricing](https://www.framer.com/pricing)]

## Data handling, licensing, and browser automation

### Data handling

Agent access adds another disclosure path to the ordinary product relationship: the selected board, design, screenshot, code, or metadata can pass through the agent client and its model provider. This is an inference from the MCP/API architectures, not a claim that every tool sends an entire file. Scope tokens and permissions narrowly, separate sensitive workspaces, avoid personal/sensitive data in prompts, and review each vendor's current retention, residency, subprocessors, and AI-training controls before organizational adoption.

There are material product-specific differences:

- Penpot, Excalidraw, Mermaid, tldraw, and code-native paths can be run locally; Penpot and Excalidraw can also be self-hosted. This permits stronger data-boundary control, although any connected model may still receive selected context.
- Miro documents regional data residency choices, while noting that some AI processing, previews, beta features, or third-party integrations can fall outside the primary region. Miro also documents AI-quality-improvement controls and says selected Free-plan interaction data is not used to train/fine-tune underlying models. [[Miro data residency](https://help.miro.com/hc/en-us/articles/23084283851026-Data-residency-at-Miro)] [[Miro AI quality improvements](https://help.miro.com/hc/en-us/articles/22874000865554-Miro-AI-quality-improvements)]
- Figma documents encryption and model-provider restrictions for its AI features, while customer training settings depend on plan/account controls. [[Figma approach to AI](https://www.figma.com/ai/our-approach/)] [[Figma privacy policy](https://www.figma.com/legal/privacy/)]
- Framer hosts data in the United States and explicitly warns users to assess AI outputs and not provide personal or sensitive data to AI features. [[Framer security](https://www.framer.com/legal/security)] [[Framer AI notice](https://www.framer.com/legal/ai-notice)]

### Licensing and cost

Open-source labels need precision. Mermaid, Excalidraw, React, Vite, Motion, and Storybook use permissive MIT licenses; Playwright uses Apache-2.0; Penpot uses MPL-2.0. tldraw is source-available under a production license, not permissive open source. Cloud canvases and builders are proprietary and price access by plan, seat/member/editor, site, usage, or add-on. [[Storybook repository](https://github.com/storybookjs/storybook)] [[Playwright repository](https://github.com/microsoft/playwright)]

For a durable cost comparison, budget five categories rather than only the advertised subscription: editor seats, agent/API usage, hosting/publishing, export or governance entitlements, and the engineering time required to make outputs production-ready. Prices and beta allowances are volatile; the linked vendor pricing pages are authoritative at procurement time.

### When browser automation is justified

Browser automation is justified for acceptance checks, screenshots, flows not exposed through an official interface, and products whose agent bridge deliberately depends on a live file. It should not be the default write path where the product offers MCP/API/CLI/SDK access. In particular:

- use Figma, Miro, Webflow, Penpot, and Excalidraw's official MCP/API surfaces for semantic creation;
- use Mermaid and code-native CLI/source operations for deterministic creation;
- use tldraw and Framer's SDK/API directly;
- use browser control to open the file, establish a bridge, inspect rendering, compare responsive states, or complete a human-authorized publish—not to simulate hundreds of coordinate clicks.

## Unavoidable human-in-the-loop gates

Even the strongest agent interfaces leave work that should not be automated away:

1. **Authorization and scope:** OAuth consent, API keys, administrator enablement, paid/full seats, file edit rights, plugin approval, and selection of the correct workspace/team/site.
2. **Sensitive-data approval:** decide whether a board, design, customer journey, screenshot, or production dataset may be exposed to the selected vendor and model provider.
3. **Design judgment:** choose which alternative best communicates the intended hierarchy, brand, emotional tone, and product strategy; remove visually plausible but semantically incoherent output.
4. **Usability evidence:** observe representative users. A clickable prototype and an agent's simulated walkthrough do not establish comprehension or task success.
5. **Accessibility evaluation:** set semantics and text alternatives, test keyboard and zoom/reflow, inspect reduced motion and contrast, and include manual screen-reader/assistive-technology testing. Automated checks are necessary but insufficient.
6. **Asset and rights review:** approve custom fonts, photography, icons, trademarks, generated visuals, licenses, and any missing alt/caption copy.
7. **Release control:** review preview deployments, analytics/privacy behavior, forms and integrations, responsive states, performance, security headers, and production-domain publishing.

## Recommended operating model

### Default, portability-first workflow

1. Generate two or three IA/journey alternatives in Mermaid and render SVG for review.
2. Move the chosen structure to Excalidraw for low-fidelity spatial exploration when needed.
3. Build the decisive responsive/clickable alternative in code, with shared fixtures and Storybook stories so variants remain comparable.
4. Use Playwright for screenshots, cross-browser interaction, and repeatable acceptance; use axe plus manual accessibility evaluation.
5. Keep source, structured diagram files, decision notes, and test evidence in version control. Export static review artifacts, but do not treat screenshots as source.

### Canvas-first workflow

Choose Penpot when self-hosting, open data, and low lock-in dominate. Choose Figma when its component ecosystem, editable code capture, canvas depth, and organizational adoption justify the seat and file-format dependency. In both cases, implement the accepted interaction in code before claiming production behavior or accessibility.

### Collaboration-first workflow

Choose Miro when the central event is a workshop or discovery process involving journeys, comments, clustering, diagrams, and quick click-throughs. Export key results into durable structured notes/diagrams rather than leaving the decision record only on the board.

### Visual-site workflow

Choose Webflow when visual authoring, sophisticated scroll/motion, CMS/content workflows, and a partial code exit are valuable. Choose Framer when maximum speed and motion polish outweigh the inability to export and self-host. In either product, have a human approve OAuth, preview, responsive/accessibility review, and production deploy.

## Conclusion

The practical frontier has shifted: agents can now make semantic writes to major design tools, not merely drive their browsers. Figma, Penpot, Miro, Webflow, and Excalidraw all expose official MCP surfaces; Framer and tldraw expose programmable SDKs; Mermaid and code-native workflows remain the most deterministic and portable.

The strongest general strategy is therefore not to standardize on one canvas. Use the cheapest, most structured artifact that can answer the current question, preserve an exit format at every handoff, and escalate to a cloud visual builder only when its collaboration or publishing capability is the point. For most teams that means Mermaid/Excalidraw for thinking, Penpot/Figma for shared visual design, and code-native prototypes for the final interaction, motion, accessibility, and delivery decision.
