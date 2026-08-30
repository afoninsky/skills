# Product Design skill suite

`product-design` is the public entrypoint for designing, redesigning, prototyping, implementing, and reviewing web and mobile interfaces. It routes the request to the smallest useful specialist or sequence while keeping the user's objective and mutation scope authoritative.

```text
$product-design <your request>
```

## Working model

The suite is intentionally proportional:

- Inspect the current product, runtime, design system, source, tests, and project conventions before changing anything.
- Treat a narrow request as a closed-world change. Modify only the named element and the dependencies required to make it correct; a repeated run should be a no-op.
- For greenfield work or a broad redesign, explore a small range of genuinely different structural and visual approaches. Surface alternatives when they reveal a useful tradeoff; otherwise choose the strongest coherent direction and explain why.
- Keep exploration separate from mutation. Alternative concepts and prototypes stay isolated; only the selected approach enters the authorized product scope.
- Research concrete gaps when an unsupported audience, behavioral, domain, commercial, category, safety, cultural, regulatory, accessibility, platform, or current-fact premise could materially change the design. Reuse current matching evidence and pass only decision-relevant implications forward.
- Reuse the project's established framework, components, tokens, tests, and tools. Add a dependency or service only for a real unmet need and with the required authority.
- Inspect the result in its real medium and run checks proportional to the requested outcome. Missing evidence limits the claim; it does not prevent unrelated useful work.

Clear ordinary requests do not require a formal pipeline or approval at every phase. The router may continue across workers when the decisions are clear, the request authorizes the writes, and the mutation scope does not expand. It pauses when a material product decision, broader production impact, or separately protected action needs the user.

## Specialists

| Skill | Responsibility |
| --- | --- |
| `product-design` | Public entrypoint, proportional routing, shared scope and quality principles |
| `product-design-discovery` | Users, jobs, flows, content, states, constraints, and relevant research |
| `product-design-direction` | Distinct visual and interaction directions, comparison, and convergence |
| `product-design-contract` | Durable principles, tokens, component states, source maps, and accepted identities |
| `product-design-prototype` | Isolated wireframes, mocks, interaction proofs, and runnable decision slices |
| `product-design-implementation` | Clear or approved designs implemented in the real product architecture |
| `product-design-change` | Narrow, impact-aware changes that preserve everything outside the intended delta |
| `product-design-review` | Read-only visual, UX, accessibility, fidelity, and design-system review |

Workers can be invoked directly for focused or automated work, but `$product-design` is the normal interface.

## Typical requests

### Start from an idea

```text
$product-design Design and build a responsive booking product for independent music teachers. Choose a distinctive direction and make reasonable assumptions.
```

The router can move through discovery, direction, prototype, and implementation in one task when the brief is sufficiently clear. It explores proportionally, keeps alternatives isolated, and implements only the chosen approach.

### Make a local change

```text
$product-design Reduce vertical spacing in the checkout summary only. Preserve typography, color, order, behavior, and every other surface.
```

The change worker identifies the real component and shared dependencies, checks whether the requested result already exists, applies the smallest patch, and verifies the affected and protected behavior. Formal manifests and baseline guards are used when the project or risk warrants them, not as ceremony for every edit.

### Review without modifying

```text
$product-design Review the current web and mobile UI for design-system drift and accessibility risks. Do not fix anything.
```

Review stays read-only and separates observed facts, professional judgment, and unsupported claims. Findings become implementation or change work only when the request provides mutation authority for a bounded scope.

### Resume a formal engagement

```text
$product-design Direction B is approved. Continue from the recorded design state.
```

For a durable multi-stage engagement, the router resumes named artifacts and accepted identities rather than reconstructing decisions from chat. Formal routing envelopes, evidence gates, and source maps remain available when they protect resumability or high-risk decisions.

## Protected boundaries

- Review does not modify the product.
- Exploration, direction, and prototypes do not become production or accepted state by momentum.
- Implementation and change never overwrite accepted references or visual baselines to make a candidate pass.
- Only `product-design-contract` in explicit `accept-freeze` mode may record a named, reviewed, human-approved candidate as the accepted baseline. An updated snapshot, passing test, or agent recommendation is not acceptance.
- Deployment, analytics or instrumentation changes, participant contact, account connection, external publication, and spend require separate authority.
- Agent critique and synthetic personas may produce hypotheses; they are not representative-user research.

## Tools and evidence

Use repository-native and platform-native tools first. Mature tools such as existing browser tests, component previews, device tests, accessibility inspectors, and deterministic visual comparisons are valuable when the outcome depends on them, but the suite does not require a historical preferred brand merely because it is documented.

When introducing or replacing a tool, compare the capability it provides, maintenance, portability, evidence quality, migration risk, and rollback. Verify time-sensitive setup against current official documentation. MCP and SaaS integrations are optional adapters; accepted design state should remain in durable project artifacts.

## Install

Install the complete repository so the router can discover every specialist:

```bash
npx skills add afoninsky/skills
```

For a local checkout:

```bash
npx skills add /path/to/skills
```
