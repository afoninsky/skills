# Protected change protocol

## Define one observable delta

A useful intent says what a user will observe and what remains fixed. Examples:

- “Reduce vertical padding in compact notification cards while typography, horizontal alignment, interaction, and every non-notification surface remain unchanged.”
- “Increase the semantic primary-action contrast across every mapped consumer, preserving layout and behavior.”

“Polish the card” or “make it modern” is unresolved direction, not a protected change.

## Accepted-base reproduction

Before editing:

1. resolve the accepted Git ref;
2. verify baseline manifest and entry hashes;
3. identify environment, viewport/device, theme, locale, data fixture, fonts, and runtime configuration;
4. run the asserted baseline path or explain why the base is not reproducible;
5. capture the exact affected states;
6. isolate from unrelated dirty work.

Do not rewrite or update a failed baseline to make reproduction succeed.

## Impact resolution

Start from the smallest known selector—annotated crop, selected design layer, component name, route/screen, or source symbol. Resolve against `source-map.json` and actual imports.

### Local source edit

The component source, its relevant states, all surfaces using the component, and each corresponding target are affected unless implementation proves the edited path is a separately contracted variant.

### Shared component edit

Expand to every mapped consumer surface and component state. A story/preview is useful but cannot replace journey preservation where behavior is involved.

### Semantic token edit

Expand to each component referencing the token, each dependent surface, every generated platform output, and all relevant themes/targets. Run the compiler deterministically if one is canonical.

### Responsive/adaptive edit

Include widths/configurations on both sides of the layout transition plus intermediate space, text scaling, input, orientation, safe areas, and software keyboard as applicable.

### Shared-code wrapper

Edit the actual shared UI source once. Verify in its normal web runtime and add a packaged-app smoke for native shell, safe-area, keyboard, WebView, or plugin differences. Do not create a parallel native component.

## Scope escalation triggers

Stop for a revised manifest or earlier design phase when work would:

- change navigation, information architecture, product behavior, or fixed content hierarchy;
- alter a design principle, semantic meaning, shared token, shared component, or intentional variant not named by the request;
- add a dependency or second token/style authority;
- touch an unmapped consumer or reveal an incorrect source map;
- revive an archived/rejected direction;
- modify a protected baseline/reference or ask a change worker to accept itself.

## Evidence matrix

For every `surfaces_may_change`, show matched before/candidate/diff evidence. For representative `surfaces_must_not_change`, run deterministic preservation. Include functional and accessibility checks appropriate to the actual delta.

Capture-only images are useful debugging evidence but do not protect preservation. Keep accepted goldens unchanged until a separate human-approved freeze.

## Failure and rollback

If the scope guard fails:

1. stop further writes;
2. list unexpected paths or baseline identity changes;
3. determine whether they belong to this worker or pre-existing user work;
4. restore only worker-owned accidental changes with a recoverable, targeted edit;
5. rerun the guard;
6. propose manifest expansion only when product impact genuinely requires it.

Never use a broad destructive reset to clean a shared working tree.
