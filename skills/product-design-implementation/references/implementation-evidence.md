# Implementation evidence contract

## Match before comparing

A visual comparison is meaningful only when approved reference and candidate share:

- surface and state;
- representative content and data fixture;
- viewport/device, orientation, safe-area/inset behavior, and text/display scale;
- locale, theme, motion setting, permissions, and authentication state;
- browser/OS/runtime version, fonts, and crop.

Record mismatches. Do not interpret them as design deltas.

## Evidence levels

- **E0 — agent judgment:** generated analysis or visual critique.
- **E1 — specialist/heuristic review:** structured review by a relevant expert or tool.
- **E2 — deterministic artifact/runtime evidence:** source checks, workbench fixtures, tests, goldens, traces, semantics, or device output bound to the target.
- **E3 — internal human task evidence:** observed task completion by non-representative reviewers.
- **E4 — representative-user evidence:** appropriately recruited target users under a documented method.
- **E5 — live product evidence:** consented, correctly interpreted production behavior/outcomes.

Higher labels do not automatically override lower evidence and quantity does not upgrade a label. Each supports different claims. Source evidence cannot prove rendering; a screenshot cannot prove semantics or interaction; automation cannot prove usability; distribution cannot prove that a tester completed a task.

## Visual acceptance dimensions

Compare both fidelity and quality:

- shell silhouette and region proportions;
- hierarchy, core act, density, spacing rhythm, and whitespace;
- typography metrics, wrapping, truncation, and content extremes;
- semantic color, shape, elevation, imagery, iconography, and motion;
- component states and family/system consistency;
- responsive/adaptive behavior rather than one frozen viewport;
- focus, hover, pressed, selected, disabled, loading, empty, error, permission, and recovery states.

Passing semantic or functional tests cannot compensate for a material visual mismatch. Conversely, exact pixels cannot compensate for broken behavior or inaccessible semantics.

## Baseline protection

Before editing, inventory:

- manifest-declared approved references;
- Playwright `toHaveScreenshot` snapshot directories;
- Maestro `assertScreenshot` references;
- native snapshot-test goldens;
- repository-defined approved reference paths.

After implementation, compare their Git status against the accepted base. New candidate captures must have a distinct path and label. `page.screenshot`, Maestro `takeScreenshot`, simulator captures, and exported images are capture-only unless an assertion and human-approved baseline identity protect them.

Do not run update-snapshot/re-record/rebaseline modes. If a test requests an update, fail the implementation handoff and send the candidate to review.

## Acceptance wording

Use scoped claims:

- “The authorized slice builds and was exercised in Chromium and WebKit at these configurations.”
- “No automated axe findings were observed in these states; keyboard and screen-reader checks remain listed.”
- “No protected baseline paths changed relative to the accepted ref.”

Avoid:

- “pixel perfect” without a defined tolerance and matched captures;
- “accessible,” “compliant,” or “usable” from automation;
- “mobile tested” when only responsive browser emulation ran;
- “no regressions” beyond the actual preservation matrix.
