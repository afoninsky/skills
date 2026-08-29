# Product-design tool selection baseline

Choose tools for the work they enable, not their novelty, brand, AI features, or integration surface. These principles govern new setup and replacement; they do not require migration of a working project.

## Selection order

1. Reuse the repository's established tool or platform-native capability.
2. Prefer a mature, maintained package or service with a strong fit.
3. Build a custom solution only when existing choices cannot satisfy a concrete requirement.

Use the smallest tool set that can produce the artifact and evidence the request needs.

## Admission criteria

Evaluate a candidate against the capability it must provide:

- **Fit:** resolves the actual design, implementation, collaboration, or evidence gap.
- **Maturity:** maintained, documented, stable enough for the project's risk, and supported by a credible ecosystem.
- **Compatibility:** works with the current architecture, platforms, accessibility needs, source ownership, and CI.
- **Evidence quality:** produces inspectable, repeatable output appropriate to the claim.
- **Portability:** important state can be exported or kept in durable project artifacts; lock-in and exit are understood.
- **Security and privacy:** permissions, data handling, hosting, and participant impact are acceptable.
- **Cost and operations:** sustainable for the intended duration and team, including maintenance and quotas.
- **Reversibility:** migration and rollback are practical and tested in proportion to risk.

A built-in AI generator or MCP endpoint can improve speed, but it does not replace these criteria or make the service canonical.

## Capability examples

These are illustrations, not mandatory defaults:

| Need | Prefer |
| --- | --- |
| Versioning and rollback | Existing version control, commonly Git |
| Structured visual source | The team's current editable design tool or portable code-native study |
| Semantic styling | Existing framework tokens or CSS variables; structured token formats when multiple outputs justify them |
| Component states | Existing fixtures, stories, previews, or native workbenches |
| Web behavior and visual comparison | Existing browser test stack; Playwright is a common mature option |
| Mobile behavior | Existing platform tests or cross-platform flow runner plus native checks where needed |
| Accessibility | Platform semantics, automated checks, and relevant manual assistive-technology inspection |
| Human review | Existing preview, distribution, or artifact-sharing path |
| User research | Authorized moderated or unmoderated research with representative participants |
| Product behavior | Existing consented analytics or research system tied to a named decision |

Do not install every example. A small product may need only repository source, its normal runtime, browser or device inspection, and focused tests.

## AI division of labor

Use models to synthesize evidence, generate divergent concepts, draft realistic content and edge cases, critique, and assist implementation. Use editable source and deterministic tools for structure and behavior, real runtimes for rendered results, and representative people or appropriately interpreted product data for user claims.

Image generation is suitable for raster assets when the design needs them. It is not a substitute for semantic, editable UI structure.

## Replacement test

Before replacing an established tool:

1. Understand why it exists, who uses it, what state it owns, and which workflows depend on it.
2. Identify the concrete deficiency; conformity or novelty is not a reason.
3. Compare the current and proposed tool on the same representative artifact or workflow.
4. Evaluate lost fidelity, history, permissions, accessibility, automation, exports, migration effort, and rollback.
5. Obtain approval when the change affects canonical source, production dependencies, CI, external services, research, analytics, spend, or team workflow.
6. Migrate only after the replacement proves a net benefit without degrading required behavior or evidence.

For a durable high-impact replacement, record the decision and rollback in the repository's existing decision format. Do not create a new governance hierarchy for a small or reversible adapter change.

## Time-sensitive setup

Versions, pricing, quotas, ownership, permissions, and features change. Verify them against current official documentation at the moment of setup or replacement. Prefer primary product documentation and release notes; do not freeze installation commands or commercial assumptions in this skill.
