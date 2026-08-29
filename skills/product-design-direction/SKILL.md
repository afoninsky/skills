---
name: product-design-direction
description: Internal visual-direction worker in the Product Design suite. Invoke only when product-design selects it with a routing envelope, the user explicitly names $product-design-direction, or advanced automation supplies an accepted UX brief and equivalent authority; for every other raw UI/UX request, use product-design. Explore and compare genuinely distinct visual backbones with matched rendered evidence, recommend one, and stop for human selection. Do not perform discovery, interaction-only prototyping, production implementation, post-baseline changes, audits, or self-selection.
compatibility: Requires an accepted UX brief, versioned isolation, and a working visual render/export and capture path. Penpot Free/MCP, image generation, participant studies, and preview hosting are conditional or optional adapters; production source and accepted baselines remain out of scope.
---

# Product Design Direction

Turn an approved experience into two or three visually and structurally distinct candidates that a human can compare on equal evidence. The agent recommends; the owner selects.

## Start here

1. Read [tool preflight](references/tool-preflight.md) completely and run it before reference research, source creation, or remote design writes.
2. Read [direction method](references/direction-method.md) before generating territories or finalists.
3. Read [rendering, quality, and platform coverage](references/rendering-quality-and-platforms.md) before selecting the target matrix or judging candidates.
4. Use the templates in `assets/`; do not overwrite accepted references or contracts.

If routed, preserve the unchanged original prompt and obey the routing envelope. If invoked directly, establish the same request ID, accepted artifact hashes, scope, mutation authority, fixed constraints, target matrix, and Gate B stop condition.

## Preconditions and authority

- Read `design/project-design.json` when present. Require an accepted brief path/hash or explicit owner confirmation of an equivalent supplied brief. Draft requirements and chat recollection are insufficient.
- Read the real content, experience map, state inventory, platform map, existing contract, and current visual authorities when present.
- Confirm that visual grammar is genuinely unresolved. If the request is only about flow/behavior, recommend `product-design-prototype`; if an accepted baseline will change, recommend `product-design-change`.
- Permit writes only to isolated direction artifacts. Do not edit production source, canonical tokens, approved references, tests, or baselines.
- Never infer selection from the agent's recommendation, a stakeholder preference, or silence.

## Workflow

### 1. Freeze the comparison inputs

Record the same:

- priority journey and core act;
- real content and content extremes;
- representative states;
- viewport/device/input matrix;
- fixed/challengeable/open constraints;
- acceptance and rejection criteria.

Candidates are comparable only when these inputs remain matched. If a direction needs a different navigation model or product scope, stop and route that question back to discovery rather than hiding a UX redesign inside visual exploration.

The platform matrix is non-empty and contains at least one representative configuration for every materially distinct implementation/adaptation class in scope. It is not every device. Make excluded classes and configurations explicit. For a shared web wrapper, use one visual backbone but include browser and packaged-shell rows for the behaviors each can reveal.

### 2. Research with intent

Name the visual decision before gathering references. Seek principles and transferable patterns, not a collage of fashionable products. Record source, date, observed pattern, why it is relevant, what not to copy, and asset/license provenance.

Reference research is evidence about possibilities, not permission to imitate another product. Do not use inspiration-search services merely to produce volume when ordinary web research and a strong model suffice.

### 3. Explore breadth cheaply

Generate a proportional set of terse territories before rendering. For a normal small product, four to six territories and two or three finalists are enough. A narrow visual question may need only two finalists; a major high-stakes identity may justify more.

Each territory must have a different structural and visual hypothesis. Vary hierarchy, composition, navigation treatment, density, type system, shape/elevation, color logic, imagery, motion, and state expression as a coherent system. Palette swaps and minor card variations are one direction, not several.

Reject default clusters early: generic centered hero, interchangeable cards, familiar gradient, stock dashboard grid, or framework-default controls without a product reason.

### 4. Build finalists in isolation

Create each finalist in a separate design page/file, disposable source directory, branch, or worktree. Give each a stable direction ID. Keep prototype dependencies physically separate from production.

Use the lowest medium that resolves the question:

- Penpot frames for editable visual composition;
- disposable HTML/CSS for responsive web grammar;
- isolated Xcode/Compose/Flutter/RN preview source when native rendering materially affects the direction;
- image generation only for necessary raster imagery, never as a substitute for editable UI structure.

Export Git-owned source/references and record their hashes. MCP or SaaS state is never the sole artifact.

### 5. Produce matched evidence

Render every finalist with identical content, state, target size, scale, crop rule, and environment. Cover every listed platform class with its representative configuration; include at least one small target and one larger target when the same responsive class spans them, plus a state that stresses content or recovery.

Create a contact sheet and manifest linking every cell to direction, source, state, target, and hash. A text description without rendered evidence cannot pass Gate B.

### 6. Critique and recommend

Apply the quality lenses in the rendering reference. Describe strengths, risks, accessibility/adaptive concerns, implementation cost, and how each candidate advances the brief. Avoid numeric taste scores that imply false precision.

Recommend one candidate with reasons tied to the brief. Do not combine the “best parts” after comparison unless the owner explicitly asks for a new hybrid candidate; an unrendered hybrid is not selectable.

### 7. Stop at Gate B

Present two or three candidates and ask the owner to select, reject, or request one bounded refinement. Only after an explicit selection may this skill create/update `design/decisions/selected-direction.md`, identify the selected candidate hash, and archive rejected candidates without deleting their evidence.

Selection does not authorize production implementation or baseline updates. The next normal worker is `product-design-contract`.

## Default outputs

- `design/directions/<direction-id>/charter.md`
- isolated source and exported references under that candidate directory
- `design/directions/<direction-id>/render-manifest.json`
- `design/decisions/direction-comparison.md`
- a matched contact sheet
- after explicit selection only: `design/decisions/selected-direction.md` and archived rejected options
- `design/project-design.json` references/hashes when routed

Adapt an established project layout instead of duplicating it.

## Completion checks

- Inputs are matched across candidates and accepted brief constraints remain intact.
- Finalists differ in structure and visual grammar, not only styling tokens.
- Actual renders exist for the selected comparison matrix.
- Sources, assets, fonts, and references have provenance and Git-owned exports.
- Production files, accepted contract, approved references, and baselines are unchanged.
- The agent's recommendation is separate from the owner's selection.
- Missing render or required participant evidence leaves the affected gate `Not evidenced`, not merely caveated in prose.

## Handoff

End with a concise comparison summary and this object, matching the suite handoff schema:

```json
{
  "schema_version": "1.0.0",
  "request_id": "REQ-...",
  "worker": "product-design-direction",
  "status": "complete | needs-owner | blocked | failed",
  "input_hashes": {"original_prompt": "<sha256>"},
  "artifacts_created_or_changed": [],
  "production_mutations": [],
  "evidence": [],
  "missing_evidence": [],
  "degraded_capabilities": [],
  "baseline_changed": false,
  "gate": "B | null",
  "recommended_next_worker": "product-design-contract | null",
  "exact_next_action": "..."
}
```

Before selection, the normal status is `needs-owner` at Gate B. Workers recommend; only the `product-design` router advances a pipeline.
