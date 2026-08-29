# Prototype method

## Write the decision contract first

Complete this sentence before choosing a tool:

> We need to learn whether [role] can [observable task/understanding] in [situation/target], and we will reject the design if [observable failure].

Then name:

- relevant brief, direction, contract, or product-context inputs;
- fidelity necessary to answer the question;
- required states, content extremes, and targets;
- evidence needed and what remains out of scope;
- decision or stopping point at completion.

If no plausible observation could change the next action, a prototype is unnecessary.

## Fidelity selection

| Question | Lowest useful artifact | Cannot prove |
| --- | --- | --- |
| Is the flow/order coherent? | text flow or schematic wireframe | visual hierarchy, native behavior |
| Is progressive disclosure understandable? | clickable low-fidelity prototype | production performance, full semantics |
| Does selected direction adapt across sizes/states? | high-fidelity responsive/native renders | production architecture, live data |
| Does keyboard/safe-area/native-control behavior work? | framework preview or runnable app slice | full production integration |
| Can target users complete a critical task? | runnable prototype plus representative study | post-launch behavior at scale |

Do not use high fidelity to conceal unresolved interaction logic. Do not use low fidelity to claim visual or platform acceptance.

## Representative vertical slice

A useful slice includes enough of the product loop to expose system behavior:

1. entry/context;
2. the core act;
3. visible consequence or shared-state effect;
4. one failure/recovery path;
5. return or next-state behavior;
6. related component states demonstrating family consistency.

It is not necessarily one screen, and it is not the entire product.

## Isolation contract

For a durable, collaborative, or high-risk prototype record:

- prototype ID/status/owner;
- source root or worktree/branch;
- separate manifest and dependency boundary;
- permitted read-only imports from production;
- command to run and deterministic fixture source;
- outputs/evidence paths;
- teardown/archive policy;
- explicit rule that production cannot import prototype code.

For a small atomic prototype, an isolated source location, run command, and clear no-production-import boundary may be enough. Before handoff, inspect the dependency direction so production does not import prototype code.

## Fixture design

Fixtures should be stable, compact, and adversarial enough to reveal weakness. Avoid network timing and random data unless the question is specifically about them. Include:

- named fixture ID and seed/version;
- data, role, permissions, and environment assumptions;
- initial state;
- actions and expected transitions;
- content extremes and accessibility configurations;
- synthetic-data declaration.

Use realistic language and domain shapes. Lorem ipsum can make poor hierarchy look successful.

## Build discipline

- Prefer the existing project runtime when it can isolate a non-production route/state cleanly; otherwise use a disposable project.
- Preserve framework conventions only to the extent needed for faithful behavior.
- Use semantic controls before custom facsimiles.
- Hardcode fixture data rather than creating unnecessary services.
- Fake external effects visibly and document them.
- Keep analytics, persistence, authentication, migrations, and reusable architecture out unless directly tested by the question.
- Do not convert prototype shortcuts into implementation recommendations.

## Evidence packet

Show:

1. run/open instructions tied to a ref/hash;
2. representative target renders before rationale;
3. critical-flow result and state transitions;
4. adaptive/accessibility observations;
5. known shortcuts and untested targets;
6. implementation-neutral behavior spec;
7. the decision now supported and any material input still needed.

Prototype evidence is not an approved baseline. Do not update any golden/reference manifest in this phase.
