# Deterministic preservation evidence

Use this only when a high-risk bounded change has project-native capture tooling that can produce normalized protected evidence. The guard compares supplied evidence; it does not replace the browser, app, test runner, or capture adapter.

## Bundle contract

```json
{
  "schema_version": 1,
  "subject": "worktree:8b31…",
  "capture_id": "capture:7f43…",
  "cases": [
    {
      "target": "web/chromium/1440x900",
      "turn": "original",
      "case_id": "kiln-card/loaded",
      "conditions": {
        "surface": "kiln-card",
        "state": "loaded",
        "viewport_or_device": {"width": 1440, "height": 900},
        "theme": "light",
        "locale": "en-NL",
        "fixture": "kiln-fixture-v1",
        "fonts": ["Georgia", "system-ui"],
        "runtime": "chromium@128",
        "probe": "kiln-capture@1",
        "scale": 1
      },
      "authorized_subtree": {
        "locator": "[data-maintenance-notice]",
        "operation": "insert",
        "match_count": 0
      },
      "evidence": {
        "structure": "original/structure.json",
        "style": "original/style.json",
        "local_geometry": "original/local-geometry.json",
        "render": "original/protected.rgba",
        "behavior": "original/behavior.json",
        "side_effects": "original/side-effects.json"
      }
    }
  ]
}
```

`subject` is the source, build, or working-tree fingerprint. It may equal a reference on a verified no-op. `capture_id` identifies the capture run; the candidate value must be fresh, differ from every reference capture, and match `--expected-candidate-capture-id`. A case key is `(target, turn, case_id)`; use stable `case_id` values to distinguish surfaces and states at the same target, while `turn` identifies the anchor comparison. For original and previous anchors, the candidate repeats every referenced case under matched conditions, so its case set is their exact union. Evidence artifacts must not be reused across cases.

The capture adapter must apply the stable authorized locator uniformly to every channel. Use `insert` for reference `match_count: 0` and candidate `1`, `modify` for `1` and `1`, or `delete` for `1` and `0`; use `null` when nothing is omitted. An inserted or deleted node is absent on one side and stripped on the other, while a modified node is replaced by the same deterministic sentinel on both. Produce six distinct, non-empty core artifacts. Geometry is relative to the protected component root; render evidence covers only protected pixels. Put platform detail inside `viewport_or_device` and bind adapter configuration through `probe`; other condition fields, ignore regions, masks, tolerances, and thresholds are invalid. Extra evidence channels are allowed and compared.

Run capture and comparison in the current project-native verification path. The guard canonicalizes and checks conditions, authorized operation/counts, capture-run identity, case/channel completeness, artifact paths, and artifact bytes. It cannot itself execute capture, resolve the locator, prove evidence provenance or completeness, or establish usability and visual quality. Treat locator counts, capture identity, and current-subject identity as adapter attestations; if those cannot be produced reliably, report the preservation claim as unverified instead of manufacturing a bundle.
