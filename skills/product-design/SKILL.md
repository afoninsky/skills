---
name: product-design
description: Sole automatic entrypoint and router for unqualified UI/UX and digital-product design work across responsive web, native iOS and Android, React Native, Flutter, and shared web/mobile wrappers. Trigger for new or redesigned sites and apps; UX research and structure; visual direction; wireframes, mocks, and prototypes; approved design-to-code work; design systems and semantic tokens; controlled changes to accepted UI; read-only or review-and-fix audits; periodic improvements; and acceptance or freezing of named UI candidates and visual baselines. Preserve the original request, inspect accepted state, preflight applicable capabilities, and route the earliest missing prerequisite or gated series. Use this before narrower styling, prototyping, implementation, or audit helpers unless the user explicitly names one. Do not use for standalone graphic or image assets, or non-visual code and architecture.
license: MIT
compatibility: Requires the selected product-design worker skills for routed execution. Works without MCP servers; Git and real browser or app-runtime evidence become required at acceptance and protected-change gates.
metadata: {version: "1.0.0"}
---

# Product Design

Be the single public entrypoint for the product-design suite. The user supplies the objective; you select and coordinate the specialist work.

Do not become a monolithic designer. Preserve authority, route focused workers, validate their handoffs, and stop at human gates.

## Read the operating protocol

Before routing, read completely:

1. [Routing and handoffs](references/routing-and-handoffs.md)
2. [Tool capability preflight](references/tool-capability-preflight.md)
3. [Project design protocol](references/project-protocol.md)
4. [Evidence and human gates](references/evidence-and-gates.md)

Load [platform detection](references/platform-detection.md) only when a repository or target platform exists.

## Preserve the request

Keep the user's original prompt and explicit constraints unchanged in working context. Compute its UTF-8 SHA-256 and put it in `original_prompt_sha256`; every worker returns that digest in `input_hashes.original_prompt`. Add a routing envelope; do not replace the request with a paraphrase.

For multi-turn work, persist the prompt digest, a concise objective, approvals, artifact paths and hashes, active route, and exact next action in `design/project-design.json`. Do not persist sensitive raw prompt content. On resume, hash the preserved prompt again and stop if identity cannot be reconciled.

## Discover before routing

Use read-only inspection first:

- find an existing project design state, brief, design system, tokens, components, references, prototypes, tests, and visual baselines;
- inspect repository instructions, framework, package manager, app boundaries, and web/mobile source sharing;
- distinguish asserted goldens from screenshots that are merely captured;
- identify accepted, candidate, archived, and superseded artifacts;
- classify the request's mutation authority: `read-only`, `design-artifacts-only`, `production-bounded`, or explicit `accept-freeze`.

If no repository exists, route using the user's product context and initialize project artifacts only when useful and authorized.

## Run capability preflight

Derive capabilities from the selected phase and platforms. Check each applicable capability as `available`, `missing-blocking`, `missing-degradable`, `unknown`, or `not-applicable`.

Never silently continue when an applicable tool or evidence capability is absent.

- For `missing-blocking`, stop. Explain the lost evidence, provide step-by-step setup instructions tailored to the environment and verified against current official documentation, and ask whether to perform or await setup.
- For `missing-degradable`, explain the exact limitation and claims that will remain `Not evidenced`. Offer setup or a specifically bounded degraded route, then wait for confirmation. If the current worker cannot honestly execute that reduced scope, create a new envelope for read-only review, contract planning, or an isolated prototype instead of continuing it in place.
- Missing applicable runtime or accessibility hard gates stop `product-design-implementation` and `product-design-change` before production writes. Never re-label a source-only production patch as degraded implementation.
- Do not install a package, connect an account, expose an MCP server, add analytics, or modify CI without authorization.
- An optional tool that is not selected for this route is `not-applicable`, not a hidden failure.

Record the result in `design/toolchain.json` for a durable engagement, excluding credentials and secrets.

Before executing a worker, set `toolchain.profile.phase`, `platforms`, and evidence `claims` to the selected route, then run:

```text
python3 <product-design-skill-directory>/scripts/validate_toolchain.py design/toolchain.json --for-execution
```

Execution requires a validator pass. Set `checked_at` only after every applicable status has been probed: it must be a timezone-aware ISO-8601 time no older than four hours and no more than five minutes in the future. Rebuild and revalidate the profile before every worker transition or whenever platform, claim, scope, target/build identity, access, tool state, or degraded-mode authority changes; those changes require a fresh probe even inside four hours. Do not refresh the timestamp alone, remove a required capability, or empty the platform set to make validation pass; narrow the routed work explicitly and keep the unavailable gate `Not evidenced`.

Use only the validator's canonical profile values:

- phase: `discovery`, `direction`, `contract`, `prototype`, `implementation`, `change`, `review`, or `accept-freeze`;
- platform: `web`, `native-mobile`, or `shared-web-wrapper` (combine web and native mobile for independent implementations);
- claim, when requested: `visual-acceptance`, `accessibility-acceptance`, `release`, `physical-device`, or `representative-user`.

Claims describe conclusions this run must support. Omit a claim only when the routed work explicitly excludes that conclusion, not because its evidence tool is missing.

For direction, contract, prototype, implementation, change, and accept-freeze, `platforms` is non-empty and represents every materially distinct implementation/adaptation class in scope. The detailed target matrix needs at least one representative configuration per class, not every device. `shared-web-wrapper` means one shared web UI with both browser and packaged-shell rows; independent web and native implementations use both `web` and `native-mobile`. Candidate decisions at Gates D–F are limited to the matrix actually reviewed.

## Select the earliest missing prerequisite

Route by objective and repository readiness:

| Condition | Worker |
|---|---|
| Users, jobs, flow, content, states, or platform requirements are unresolved | `product-design-discovery` |
| An approved brief exists and visual grammar/direction is unresolved | `product-design-direction` |
| A direction is selected but rules, tokens, components, source map, or accepted identity are absent | `product-design-contract` |
| A mock, interaction proof, or representative slice is requested before production | `product-design-prototype` |
| Approved design inputs exist and a new surface/component must be built in the real framework; Gate C is approved or the request is an explicitly bounded reviewed slice | `product-design-implementation` |
| An accepted surface, component, token, or baseline may change | `product-design-change` |
| The user asks to inspect, audit, diagnose, periodically assess, or review a candidate | `product-design-review` |
| A named reviewed candidate is explicitly approved as the new baseline | `product-design-contract` in `accept-freeze` mode |
| A release, rollout, periodic-learning, or research action needs an evidence-backed owner decision | `product-design-review`, stopping at Gate F |

For a broad request, plan the whole likely route but launch only the earliest prerequisite. New, multi-surface, or high-impact production work requires a representative prototype and Gate C before implementation. Direct implementation is allowed only for an immutable, named, explicitly bounded reviewed slice that already covers its required states, adaptations, and component mapping. Record `implementation_entry_basis` plus its human approval ID in the implementation envelope. Never skip a human gate merely because the prompt names the final output.

## Launch workers

Preflight the selected worker through the runtime's skill registry. The normal installation contains:

- `product-design-discovery`
- `product-design-direction`
- `product-design-contract`
- `product-design-prototype`
- `product-design-implementation`
- `product-design-change`
- `product-design-review`

If a selected worker is unavailable, name it, explain why it is required, provide suite-installation steps appropriate to the runtime, and stop. Do not imitate the missing worker with generic advice.

Pass the worker:

- the unchanged original prompt;
- the routing envelope;
- only relevant accepted project artifacts;
- capability-preflight results;
- the current human gate and stopping condition.

Announce the route concisely, for example: `product-design → change → review; stop at candidate acceptance`.

## Validate handoffs

Require every worker to return the handoff fields defined in [Routing and handoffs](references/routing-and-handoffs.md). Validate:

- inputs match accepted hashes;
- mutations match authority and declared scope;
- required evidence exists;
- baselines did not change outside explicit `accept-freeze` mode;
- missing capabilities remain visible;
- the recommended next worker is a valid transition.

Before launch, bind the envelope to the same fresh profile and re-run the capability validator through the route validator:

```text
python3 <product-design-skill-directory>/scripts/validate_route.py <routing-envelope-path> --toolchain design/toolchain.json --for-execution
```

After execution, run the route validator again with `--handoff <worker-handoff-path>` (without `--for-execution`; the next worker receives a new fresh preflight). Workers may recommend the next phase; only this router advances it.

## Continue or stop

Continue to the next worker in the same task only when:

- the transition is valid;
- no human gate intervenes;
- the capability preflight covers the next worker;
- authority already covers its writes;
- continuing does not broaden scope.

When advancing, create a new envelope whose first route item is the accepted successor and revalidate its toolchain profile. Do not reuse a stale envelope or let the worker invoke its successor. Otherwise update the exact next action and ask for the named decision. On resume, read project state first and reconcile the new prompt as continuation, reroute, or explicit supersession.

## Non-negotiable rules

- A human selects visual direction and approves every accepted baseline.
- A named candidate review stops at Gate D for accept/reject/revise. Gate D acceptance does not authorize baseline mutation: the router next stops at Gate E for explicit approval of the exact named reviewed candidate and matrix, then contract `accept-freeze` records that identity.
- `product-design-review` owns release and research/learning evidence packets. It stops at Gate F for the owner's release/hold or research/learning decision and never deploys, instruments, recruits, or contacts participants by itself.
- Implementation and change workers never update approved screenshots or accepted-reference hashes.
- A missing runtime, visual-comparison, accessibility, physical-device, or user-evidence capability cannot be converted into a pass by user waiver. Confirmed reduced work continues only through a valid non-production route; implementation/change stop when their runtime or accessibility hard gates are missing.
- MCP servers are replaceable adapters. Git artifacts, exports, tests, flows, and screenshots remain canonical.
- Use the smallest tool set and the smallest route that can answer the request.
- Do not restart discovery or direction for a bounded accepted-design change.
- Do not implement findings during a read-only review unless the router subsequently authorizes a change route.

## Response contract

At each router boundary report:

1. **Route** — current worker and likely series.
2. **Why** — evidence that made this the earliest prerequisite.
3. **Tool status** — applicable available and missing capabilities.
4. **Authority and scope** — allowed writes and protected artifacts.
5. **Gate** — exact stopping condition or decision required.
6. **Next action** — one concrete continuation.
