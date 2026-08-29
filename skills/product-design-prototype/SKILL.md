---
name: product-design-prototype
description: Build an isolated wireframe, mock, interaction proof, or representative product slice that answers a design question. Use when routed by product-design or explicitly requested; otherwise use product-design for unqualified UI/UX work. Prototypes remain separate from production and accepted baselines.
compatibility: Requires only the renderer or runtime needed to answer the design question. Existing project tools are preferred; browser, native, design-canvas, hosting, and tester tools are conditional.
---

# Product Design Prototype

Build the least expensive real artifact that resolves a design uncertainty. A prototype is decision evidence, not production architecture or an accepted baseline.

## Scope

Define one decision question, observable success or failure, target conditions, and the source location before building. Write only to an isolated prototype, preview, worktree, design page, or other disposable area. Production may be inspected or imported read-only; production must not depend on prototype code.

Use either:

- **Evidence mode:** follow the clear or accepted product, direction, and contract inputs needed for the question.
- **Exploration mode:** when the user delegates a greenfield, broad redesign, sandbox, or concept decision, make reasonable reversible assumptions, explore distinct theses proportionally, and select a working direction inside the isolated artifact.

Exploration mode does not authorize production writes, acceptance claims, deployment, account connections, participant contact, or spend.

## Practice

1. **Inspect the context.** Understand current architecture, design conventions, shared web/native ownership, accepted decisions, and the behavior the prototype must preserve. Do not duplicate a native UI when the real product uses one shared web interface in a wrapper.
2. **Choose the lowest useful fidelity.** Use flows or wireframes for structure, clickable schematics for sequence, rendered mocks for visual composition, and framework/native previews when layout, input, safe areas, text scaling, motion, or platform behavior matters.
3. **Keep inputs and shortcuts explicit.** Record material assumptions, synthetic facts, accepted inputs, allowed dependencies, run instructions, and what the prototype cannot prove. Reuse existing tools; do not add production infrastructure for a disposable question.
4. **Use deterministic realistic fixtures.** Cover the smallest set of content extremes, relevant states, transitions, and recovery paths that can expose a bad decision. Do not build exhaustive machinery unrelated to the question.
5. **Build the decision slice.** Include enough entry context, core action, consequence, failure or recovery, and return state to make the experience believable. Prefer semantic controls and real layout behavior.
6. **Verify in the real medium.** Exercise the relevant browser, device runtime, or design canvas at representative targets. Inspect the rendered composition and critical path for comprehension, product specificity, responsiveness/adaptation, interaction integrity, accessibility risk, content extremes, and runtime errors.
7. **Conclude the question.** State what the prototype supports, contradicts, or leaves unresolved. Do not copy it into production by momentum; implementation should translate the decision into the product's actual architecture.

If the requested outcome already exists in a suitable prototype and still matches the inputs, verify and report it rather than creating another version. Re-running the same request should not duplicate artifacts or compound state.

Read [prototype method](references/prototype-method.md) for a substantial interaction proof or representative slice. Read [platform adapters and verification](references/platform-adapters-and-verification.md) only for the actual target. Read [autonomous exploration quality](references/autonomous-exploration.md) for a broad self-directed prototype. Use [tool preflight](references/tool-preflight.md) only for capabilities the selected medium needs.

## Definition of done

- One named question and stop condition govern the artifact.
- Prototype source and dependencies are isolated and production does not import them.
- The artifact uses realistic content and the relevant default, edge, failure, and recovery states without unnecessary breadth.
- The named target conditions render or run in the actual medium, and critical interactions are repeatable at the fidelity claimed.
- Accessibility, responsive/adaptive behavior, platform risks, assumptions, shortcuts, and untested conditions are explicit.
- Captures remain prototype evidence rather than accepted visual baselines.
- The handoff includes the runnable artifact, concise run instructions, evidence, answered decision, limitations, and the implementation-neutral behavior or design decisions worth carrying forward.
