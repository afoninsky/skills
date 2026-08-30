#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("preservation_guard.py")
SPEC = importlib.util.spec_from_file_location("preservation_guard", SCRIPT_PATH)
assert SPEC and SPEC.loader
GUARD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = GUARD
SPEC.loader.exec_module(GUARD)

CHANNELS = (
    "behavior",
    "local_geometry",
    "render",
    "side_effects",
    "structure",
    "style",
)


class BundleFixture:
    def __init__(
        self,
        root: Path,
        name: str,
        subject: str,
        capture_id: str | None = None,
    ) -> None:
        self.root = root / name
        self.root.mkdir(parents=True)
        self.path = self.root / "bundle.json"
        self.data = {
            "schema_version": 1,
            "subject": subject,
            "capture_id": capture_id or f"capture:{name}",
            "cases": [],
        }

    def add_case(
        self,
        target: str,
        turn: str,
        *,
        marker: str = "same",
        channels: tuple[str, ...] = CHANNELS,
        case_id: str = "kiln-card/loaded",
        state: str = "loaded",
    ) -> None:
        case_slug = case_id.replace("/", "-")
        prefix = f"{target.replace('/', '-')}-{turn}-{case_slug}"
        conditions = {
            "surface": "kiln-card",
            "state": state,
            "fixture": "kiln-fixture-v1",
            "viewport_or_device": target,
            "locale": "en-NL",
            "theme": "light",
            "scale": 1,
            "runtime": "test-runtime@1",
            "fonts": ["system-default"],
            "probe": "fixture-adapter@1",
        }
        evidence: dict[str, str] = {}
        for channel in channels:
            filename = f"{prefix}-{channel}.evidence"
            (self.root / filename).write_text(
                f"{channel}:{marker}\n",
                encoding="utf-8",
            )
            evidence[channel] = filename
        self.data["cases"].append(
            {
                "target": target,
                "turn": turn,
                "case_id": case_id,
                "conditions": conditions,
                "authorized_subtree": {
                    "locator": "[data-authorized-change]",
                    "operation": "modify",
                    "match_count": 1,
                },
                "evidence": evidence,
            }
        )

    def write(self) -> Path:
        self.path.write_text(json.dumps(self.data, indent=2) + "\n", encoding="utf-8")
        return self.path


class PreservationGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def load(self, fixture: BundleFixture):
        bundle, errors = GUARD.load_bundle(fixture.write())
        self.assertEqual(errors, [])
        self.assertIsNotNone(bundle)
        return bundle

    def matching_pair(self):
        reference = BundleFixture(self.root, "reference", "original")
        candidate = BundleFixture(self.root, "candidate", "candidate")
        reference.add_case("desktop", "original")
        candidate.add_case("desktop", "original")
        return reference, candidate

    def test_identical_evidence_passes_when_paths_and_subjects_differ(self) -> None:
        reference, candidate = self.matching_pair()
        differences = GUARD.compare_bundles([self.load(reference)], self.load(candidate))
        self.assertEqual(differences, [])

    def test_reordered_multi_target_and_turn_cases_pass(self) -> None:
        reference = BundleFixture(self.root, "reference", "previous")
        candidate = BundleFixture(self.root, "candidate", "candidate")
        reference.add_case("mobile", "turn-1")
        reference.add_case("desktop", "original")
        candidate.add_case("desktop", "original")
        candidate.add_case("mobile", "turn-1")
        self.assertEqual(
            GUARD.compare_bundles([self.load(reference)], self.load(candidate)),
            [],
        )

    def test_same_target_and_turn_support_distinct_state_cases(self) -> None:
        reference = BundleFixture(self.root, "reference", "original")
        candidate = BundleFixture(self.root, "candidate", "candidate")
        for fixture in (reference, candidate):
            fixture.add_case("desktop", "original")
            fixture.add_case(
                "desktop",
                "original",
                case_id="kiln-card/error",
                state="error",
            )
        self.assertEqual(
            GUARD.compare_bundles([self.load(reference)], self.load(candidate)),
            [],
        )

    def test_each_required_channel_is_compared(self) -> None:
        for channel in CHANNELS:
            with self.subTest(channel=channel):
                root = self.root / channel
                root.mkdir()
                reference = BundleFixture(root, "reference", "original")
                candidate = BundleFixture(root, "candidate", "candidate")
                reference.add_case("desktop", "original")
                candidate.add_case("desktop", "original")
                candidate_path = (
                    candidate.root
                    / f"desktop-original-kiln-card-loaded-{channel}.evidence"
                )
                candidate_path.write_text(f"{channel}:changed\n", encoding="utf-8")
                differences = GUARD.compare_bundles(
                    [self.load(reference)],
                    self.load(candidate),
                )
                self.assertTrue(any(f"channel='{channel}'" in item for item in differences))

    def test_conditions_mismatch_fails(self) -> None:
        reference, candidate = self.matching_pair()
        candidate.data["cases"][0]["conditions"]["theme"] = "dark"
        differences = GUARD.compare_bundles([self.load(reference)], self.load(candidate))
        self.assertTrue(any("conditions changed" in item for item in differences))

    def test_semantically_equal_reordered_conditions_pass(self) -> None:
        reference, candidate = self.matching_pair()
        conditions = candidate.data["cases"][0]["conditions"]
        candidate.data["cases"][0]["conditions"] = dict(
            reversed(list(conditions.items()))
        )
        self.assertEqual(
            GUARD.compare_bundles([self.load(reference)], self.load(candidate)),
            [],
        )

    def test_conditions_require_reproducible_capture_identity(self) -> None:
        reference, _ = self.matching_pair()
        valid_conditions = reference.data["cases"][0]["conditions"]
        reference.data["cases"][0]["conditions"] = {}
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("conditions is missing fields" in item for item in errors))

        reference.data["cases"][0]["conditions"] = valid_conditions
        valid_conditions["mask"] = "footer"
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("conditions has unsupported fields: mask" in item for item in errors))

        valid_conditions.pop("mask")
        valid_conditions["clip"] = "main"
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("conditions has unsupported fields: clip" in item for item in errors))

        valid_conditions.pop("clip")
        valid_conditions["scale"] = float("nan")
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("unsupported JSON numeric constant" in item for item in errors))

    def test_candidate_must_equal_union_of_original_and_previous_cases(self) -> None:
        original = BundleFixture(self.root, "original", "original")
        previous = BundleFixture(self.root, "previous", "previous")
        candidate = BundleFixture(self.root, "candidate", "candidate")
        original.add_case("desktop", "original")
        previous.add_case("desktop", "turn-1")
        candidate.add_case("desktop", "original")
        candidate.add_case("desktop", "turn-1")
        self.assertEqual(
            GUARD.compare_bundles(
                [self.load(original), self.load(previous)],
                self.load(candidate),
            ),
            [],
        )

    def test_missing_and_unexpected_cases_fail(self) -> None:
        reference, candidate = self.matching_pair()
        candidate.data["cases"] = []
        extra = BundleFixture(self.root, "extra", "candidate")
        extra.add_case("desktop", "original")
        extra.add_case("mobile", "original")
        candidate_bundle, candidate_errors = GUARD.load_bundle(candidate.write())
        self.assertIsNone(candidate_bundle)
        self.assertTrue(any("non-empty array" in item for item in candidate_errors))
        differences = GUARD.compare_bundles([self.load(reference)], self.load(extra))
        self.assertTrue(any("unexpected candidate case" in item for item in differences))

        two_cases = BundleFixture(self.root, "two-cases", "original-two")
        one_case = BundleFixture(self.root, "one-case", "candidate-one")
        two_cases.add_case("desktop", "original")
        two_cases.add_case("mobile", "original")
        one_case.add_case("desktop", "original")
        differences = GUARD.compare_bundles(
            [self.load(two_cases)],
            self.load(one_case),
        )
        self.assertTrue(any("missing candidate case" in item for item in differences))

    def test_unknown_fields_and_missing_required_channels_are_invalid(self) -> None:
        reference, _ = self.matching_pair()
        reference.data["schema_version"] = True
        reference.data["ignore"] = ["geometry"]
        reference.data["cases"][0]["evidence"].pop("render")
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("schema_version must equal 1" in item for item in errors))
        self.assertTrue(any("unsupported fields: ignore" in item for item in errors))
        self.assertTrue(any("missing required channels: render" in item for item in errors))

    def test_authorized_subtree_operation_controls_role_specific_counts(self) -> None:
        reference, candidate = self.matching_pair()
        reference.data["cases"][0]["authorized_subtree"] = {
            "locator": ".new-notice",
            "operation": "insert",
            "match_count": 0,
        }
        candidate.data["cases"][0]["authorized_subtree"] = {
            "locator": ".new-notice",
            "operation": "insert",
            "match_count": 1,
        }
        self.assertEqual(
            GUARD.compare_bundles(
                [self.load(reference)],
                self.load(candidate),
            ),
            [],
        )

        candidate.data["cases"][0]["authorized_subtree"]["match_count"] = 0
        differences = GUARD.compare_bundles(
            [self.load(reference)],
            self.load(candidate),
        )
        self.assertTrue(any("candidate match_count" in item for item in differences))

        candidate.data["cases"][0]["authorized_subtree"]["locator"] = "main"
        differences = GUARD.compare_bundles(
            [self.load(reference)],
            self.load(candidate),
        )
        self.assertTrue(any("authorized subtree changed" in item for item in differences))

        reference.data["cases"][0]["authorized_subtree"]["match_count"] = 2
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("match_count must be 0 or 1" in item for item in errors))

        reference.data["cases"][0]["authorized_subtree"] = {
            "locator": "main",
            "operation": "modify",
            "match_count": 1,
            "mask": "footer",
        }
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("unsupported fields: mask" in item for item in errors))

    def test_all_authorized_operations_and_null_transitions(self) -> None:
        counts = {
            "delete": (1, 0),
            "insert": (0, 1),
            "modify": (1, 1),
        }
        for operation, (reference_count, candidate_count) in counts.items():
            with self.subTest(operation=operation):
                root = self.root / operation
                reference = BundleFixture(root, "reference", "original")
                candidate = BundleFixture(root, "candidate", "candidate")
                reference.add_case("desktop", "original")
                candidate.add_case("desktop", "original")
                reference.data["cases"][0]["authorized_subtree"] = {
                    "locator": "[data-authorized-change]",
                    "operation": operation,
                    "match_count": reference_count,
                }
                candidate.data["cases"][0]["authorized_subtree"] = {
                    "locator": "[data-authorized-change]",
                    "operation": operation,
                    "match_count": candidate_count,
                }
                self.assertEqual(
                    GUARD.compare_bundles(
                        [self.load(reference)],
                        self.load(candidate),
                    ),
                    [],
                )

                candidate.data["cases"][0]["authorized_subtree"]["match_count"] = (
                    1 - candidate_count
                )
                differences = GUARD.compare_bundles(
                    [self.load(reference)],
                    self.load(candidate),
                )
                self.assertTrue(any("candidate match_count" in item for item in differences))

                candidate.data["cases"][0]["authorized_subtree"]["match_count"] = (
                    candidate_count
                )
                reference.data["cases"][0]["authorized_subtree"]["match_count"] = (
                    1 - reference_count
                )
                differences = GUARD.compare_bundles(
                    [self.load(reference)],
                    self.load(candidate),
                )
                self.assertTrue(any("reference match_count" in item for item in differences))

        reference = BundleFixture(self.root, "null-reference", "original-null")
        candidate = BundleFixture(self.root, "null-candidate", "candidate-null")
        reference.add_case("desktop", "original")
        candidate.add_case("desktop", "original")
        reference.data["cases"][0]["authorized_subtree"] = None
        differences = GUARD.compare_bundles(
            [self.load(reference)],
            self.load(candidate),
        )
        self.assertTrue(any("authorized subtree changed" in item for item in differences))

        reference.data["cases"][0]["authorized_subtree"] = {
            "locator": "[data-authorized-change]",
            "operation": "modify",
            "match_count": 1,
        }
        candidate.data["cases"][0]["authorized_subtree"] = None
        differences = GUARD.compare_bundles(
            [self.load(reference)],
            self.load(candidate),
        )
        self.assertTrue(any("authorized subtree changed" in item for item in differences))

    def test_artifacts_cannot_escape_or_use_symlinks(self) -> None:
        reference, _ = self.matching_pair()
        reference.data["cases"][0]["evidence"]["render"] = "../outside.json"
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("stay inside" in item for item in errors))

        symlink_fixture = BundleFixture(self.root, "symlink-reference", "original")
        symlink_fixture.add_case("desktop", "original")
        outside = self.root / "outside.json"
        outside.write_text("outside\n", encoding="utf-8")
        link = symlink_fixture.root / "linked.json"
        link.symlink_to(outside)
        symlink_fixture.data["cases"][0]["evidence"]["render"] = "linked.json"
        bundle, errors = GUARD.load_bundle(symlink_fixture.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("must not traverse a symlink" in item for item in errors))

    def test_evidence_channels_cannot_alias_or_use_empty_artifacts(self) -> None:
        reference, _ = self.matching_pair()
        evidence = reference.data["cases"][0]["evidence"]
        evidence["style"] = evidence["structure"]
        bundle, errors = GUARD.load_bundle(reference.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("reuses the artifact" in item for item in errors))

        empty_fixture = BundleFixture(self.root, "empty-reference", "original")
        empty_fixture.add_case("desktop", "original")
        render_path = (
            empty_fixture.root / "desktop-original-kiln-card-loaded-render.evidence"
        )
        render_path.write_text("", encoding="utf-8")
        bundle, errors = GUARD.load_bundle(empty_fixture.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("must not be empty" in item for item in errors))

        states = BundleFixture(self.root, "aliased-states", "original-states")
        states.add_case("desktop", "original")
        states.add_case(
            "desktop",
            "original",
            case_id="kiln-card/error",
            state="error",
        )
        first_structure = states.data["cases"][0]["evidence"]["structure"]
        states.data["cases"][1]["evidence"]["structure"] = first_structure
        bundle, errors = GUARD.load_bundle(states.write())
        self.assertIsNone(bundle)
        self.assertTrue(any("case_id='kiln-card/loaded'" in item for item in errors))

    def test_custom_channels_are_compared(self) -> None:
        channels = CHANNELS + ("accessibility_tree",)
        reference = BundleFixture(self.root, "reference", "original")
        candidate = BundleFixture(self.root, "candidate", "candidate")
        reference.add_case("desktop", "original", channels=channels)
        candidate.add_case("desktop", "original", channels=channels)
        (
            candidate.root
            / "desktop-original-kiln-card-loaded-accessibility_tree.evidence"
        ).write_text(
            "accessibility_tree:changed\n",
            encoding="utf-8",
        )
        differences = GUARD.compare_bundles([self.load(reference)], self.load(candidate))
        self.assertTrue(any("accessibility_tree" in item for item in differences))

    def test_cli_exit_codes_distinguish_invalid_and_changed_evidence(self) -> None:
        reference, candidate = self.matching_pair()
        output = io.StringIO()
        errors = io.StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            result = GUARD.main(
                [
                    "--candidate",
                    str(candidate.write()),
                    "--expected-candidate-capture-id",
                    "capture:candidate",
                    "--against",
                    str(reference.write()),
                ]
            )
        self.assertEqual(result, 0)
        (
            candidate.root / "desktop-original-kiln-card-loaded-render.evidence"
        ).write_text(
            "render:changed\n",
            encoding="utf-8",
        )
        with redirect_stdout(output), redirect_stderr(errors):
            result = GUARD.main(
                [
                    "--candidate",
                    str(candidate.write()),
                    "--expected-candidate-capture-id",
                    "capture:candidate",
                    "--against",
                    str(reference.write()),
                ]
            )
        self.assertEqual(result, 1)
        candidate.data["schema_version"] = 99
        with redirect_stdout(output), redirect_stderr(errors):
            result = GUARD.main(
                [
                    "--candidate",
                    str(candidate.write()),
                    "--expected-candidate-capture-id",
                    "capture:candidate",
                    "--against",
                    str(reference.write()),
                ]
            )
        self.assertEqual(result, 2)

    def test_cli_allows_noop_subject_but_rejects_reused_capture(self) -> None:
        reference, candidate = self.matching_pair()
        candidate.data["subject"] = "original"
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = GUARD.main(
                [
                    "--candidate",
                    str(candidate.write()),
                    "--expected-candidate-capture-id",
                    "capture:candidate",
                    "--against",
                    str(reference.write()),
                ]
            )
        self.assertEqual(result, 0)

        with redirect_stderr(io.StringIO()):
            result = GUARD.main(
                [
                    "--candidate",
                    str(candidate.write()),
                    "--expected-candidate-capture-id",
                    "different-capture",
                    "--against",
                    str(reference.write()),
                ]
            )
        self.assertEqual(result, 2)

        candidate.data["capture_id"] = "capture:reference"
        with redirect_stderr(io.StringIO()):
            result = GUARD.main(
                [
                    "--candidate",
                    str(candidate.write()),
                    "--expected-candidate-capture-id",
                    "capture:reference",
                    "--against",
                    str(reference.write()),
                ]
            )
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
