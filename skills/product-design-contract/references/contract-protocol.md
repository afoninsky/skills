# Contract protocol

Use this protocol in Encode or Re-architect mode. Its purpose is to make the selected design durable and change-impact-aware without turning every small product into a token-platform project.

## Inspect before defining

Inventory existing sources in this order:

1. repository/project state and accepted Git ref;
2. selected direction and approved references;
3. root/theme/style variables and import/override order;
4. token source, aliases, generated outputs, and build commands;
5. component libraries, variants, state fixtures, and preview/workbench entries;
6. routes/screens/surfaces and their component dependencies;
7. responsive rules, native adaptation, safe areas, text scaling, and input modes;
8. visual assertions versus ordinary screenshots;
9. multiple apps, themes, brands, native targets, or shared-code wrappers.

Do not infer that the newest or most specific stylesheet is authoritative. Record competing authorities and ask for direction when repository evidence cannot resolve intentional variation.

## Minimum durable contract

### Principles

Write rules with consequences. “Calm” is weak. “One primary action per task region; recovery remains visible without competing color” is inspectable. Pair principles with an avoid-list of known failure modes.

### Semantic tokens

Prefer semantic names such as `color.action.primary` or `space.component.compact` over page-specific names. Record canonical source, aliases, generated outputs, theme ownership, and affected components.

- Single web output: committed CSS custom properties are normally enough.
- Multiple outputs/themes/platforms: DTCG token JSON plus a deterministic compiler may be justified.
- Existing compiler: extend it rather than creating a second source.
- Penpot: synchronize only the reviewed interoperable subset; Git remains canonical.

### Components and states

For each shared component record source files, semantic token dependencies, surfaces, and relevant states. Include behavior, content extremes, focus/semantics, and platform differences. Do not invent unused component variants to complete a matrix.

### Responsive and adaptive behavior

Distinguish:

- **Responsive:** same product behavior reflows or scales across available space.
- **Adaptive:** input, navigation, safe area, platform convention, or information density intentionally changes.

Record breakpoints only when they correspond to an observable layout transition. Include narrow widths, intermediate widths, text scaling, zoom/reflow, orientation, safe areas, software keyboard, touch/pointer/keyboard, and motion preferences as relevant.

Record a non-empty representative platform matrix whenever the contract has targets. Include at least one configuration for every materially distinct source/runtime/adaptation class and make exclusions explicit. This is proportional coverage, not an exhaustive device list. A shared web wrapper has one web UI source but still needs browser and packaged-shell rows because shell behavior can diverge.

### Source map

Use `source-map.json` to express:

```text
token → component → surface → target → baseline entry
```

Model shared-code wrappers explicitly. A packaged web application usually has one UI source plus an additional native-shell verification target, not a duplicate native component tree.

### Baseline classes

- **Asserted golden:** a test runner compares current runtime output with the image and fails on material change.
- **Approved reference:** a human explicitly accepted an artifact as design authority; it may not itself be executable.
- **Capture-only:** useful evidence, but not a baseline and must not appear as an accepted baseline entry.

## Proportionality

Do not add unused infrastructure. A small site may need principles, CSS variables, a component/state inventory, two responsive targets, Playwright, and a small source map. A multi-platform system may need DTCG, generated Swift/Kotlin/Dart/CSS outputs, native previews, and a larger target matrix.

## Re-architecture output

When authorities are fragmented, first produce:

- current-authority inventory;
- conflicts and runtime precedence;
- proposed canonical source and explicit variants;
- migration stages and rollback points;
- impact matrix and verification needs;
- decisions requiring human approval.

Do not rewrite production styles in this skill. Route approved production migration through implementation/change work.
