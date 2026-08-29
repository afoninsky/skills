#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("change_guard.py")
SPEC = importlib.util.spec_from_file_location("change_guard", SCRIPT_PATH)
assert SPEC and SPEC.loader
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ChangeFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        for relative, content in {
            "src/tokens.css": ":root { --action: blue; }\n",
            "src/Button.tsx": "export function Button() {}\n",
            "src/Checkout.tsx": "export function Checkout() {}\n",
            "src/Settings.tsx": "export function Settings() {}\n",
            "tests/checkout.png": "checkout golden\n",
            "tests/settings.png": "settings golden\n",
            "design/decisions/changes/CHG-1-approval.md": "Human approved the exact manifest.\n",
            "design/decisions/contract-acceptance.md": "Human accepted the contract.\n",
            "design/decisions/baseline-acceptance.md": "Human accepted the baseline.\n",
        }.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        self.source_map = {
            "schema_version": 1,
            "platform_architecture": [
                {"id": "web", "kind": "web", "source_roots": ["src"], "shares_ui_with": []}
            ],
            "tokens": {
                "color.action.primary": {
                    "canonical_path": "src/tokens.css",
                    "generated_outputs": [],
                    "components": ["Button"],
                }
            },
            "components": {
                "Button": {
                    "source_files": ["src/Button.tsx"],
                    "token_dependencies": ["color.action.primary"],
                    "states": ["default", "focus"],
                    "surfaces": ["checkout", "settings"],
                },
                "Checkout": {
                    "source_files": ["src/Checkout.tsx"],
                    "token_dependencies": [],
                    "states": ["default"],
                    "surfaces": ["checkout"],
                },
            },
            "surfaces": {
                "checkout": {
                    "platforms": ["web"],
                    "components": ["Button", "Checkout"],
                    "targets": ["desktop"],
                    "baseline_entry_ids": ["checkout-default"],
                },
                "settings": {
                    "platforms": ["web"],
                    "components": ["Button"],
                    "targets": ["desktop"],
                    "baseline_entry_ids": ["settings-default"],
                },
            },
            "intentional_variants": [],
        }
        self.write_json("design/contract/source-map.json", self.source_map)
        self.contract = {
            "schema_version": 1,
            "status": "accepted",
            "candidate_id": "CONTRACT-1",
            "approval_id": "CONTRACT-APPROVAL-1",
            "accepted_by": "Product owner",
            "accepted_at": "2030-01-01T09:00:00Z",
            "accepted_ref": "abc1234",
            "approval_record": "design/decisions/contract-acceptance.md",
            "files": [
                {
                    "role": "source-map",
                    "path": "design/contract/source-map.json",
                    "sha256": digest(root / "design/contract/source-map.json"),
                }
            ],
        }
        self.write_json("design/contract/manifest.json", self.contract)
        self.baseline = {
            "schema_version": 1,
            "status": "accepted",
            "candidate_id": "BASELINE-1",
            "approval_id": "BASELINE-APPROVAL-1",
            "accepted_by": "Product owner",
            "accepted_at": "2030-01-01T09:00:00Z",
            "accepted_ref": "abc1234",
            "approval_record": "design/decisions/baseline-acceptance.md",
            "hard_gates": {
                "accessibility": {"status": "not-evidenced", "evidence": []},
                "content_truth": {"status": "not-evidenced", "evidence": []},
                "privacy_and_safety": {"status": "not-evidenced", "evidence": []},
                "representative_user_evidence": {
                    "status": "not-evidenced",
                    "evidence": [],
                },
            },
            "entries": [
                {
                    "id": "checkout-default",
                    "kind": "approved-reference",
                    "path": "tests/checkout.png",
                    "sha256": digest(root / "tests/checkout.png"),
                },
                {
                    "id": "settings-default",
                    "kind": "approved-reference",
                    "path": "tests/settings.png",
                    "sha256": digest(root / "tests/settings.png"),
                },
            ],
        }
        self.write_json("design/baselines/manifest.json", self.baseline)
        contract_hash = digest(root / "design/contract/manifest.json")
        source_map_hash = digest(root / "design/contract/source-map.json")
        baseline_hash = digest(root / "design/baselines/manifest.json")
        self.manifest = {
            "schema_version": 1,
            "change_id": "CHG-1",
            "status": "approved",
            "base_ref": "abc1234",
            "intent": "Adjust checkout local composition only.",
            "change_kind": "local-component",
            "approval": {
                "approval_id": "CHANGE-APPROVAL-1",
                "approved_by": "Product owner",
                "approved_at": "2030-01-01T10:00:00Z",
                "approval_record": "design/decisions/changes/CHG-1-approval.md",
            },
            "contract_manifest": "design/contract/manifest.json",
            "contract_manifest_sha256": contract_hash,
            "source_map": "design/contract/source-map.json",
            "source_map_sha256": source_map_hash,
            "baseline_manifest": "design/baselines/manifest.json",
            "baseline_manifest_sha256": baseline_hash,
            "allowed_files": ["src/Checkout.tsx"],
            "allowed_components": ["Checkout"],
            "allowed_tokens": [],
            "surfaces_may_change": ["checkout"],
            "surfaces_must_not_change": ["settings"],
            "required_states": ["default"],
            "required_targets": ["desktop"],
            "required_checks": ["functional", "visual", "accessibility"],
            "protected_paths": [
                "design/baselines/**",
                "design/references/approved/**",
                "design/contract/manifest.json",
                "design/contract/source-map.json",
            ],
            "baseline_updates_allowed": False,
            "capability_confirmation_ids": [],
        }
        self.flush()

    def write_json(self, relative: str, data: object) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def flush(self) -> Path:
        path = self.root / "design/decisions/changes/CHG-1.json"
        self.write_json("design/decisions/changes/CHG-1.json", self.manifest)
        return path

    def validate(self) -> tuple[list[str], list[str]]:
        errors, _, protected = GUARD.validate_manifest(self.root, self.flush())
        return errors, protected


class ChangeGuardTests(unittest.TestCase):
    def make_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], ChangeFixture]:
        temporary = tempfile.TemporaryDirectory()
        return temporary, ChangeFixture(Path(temporary.name))

    def test_valid_local_component_manifest_passes(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        errors, _ = fixture.validate()
        self.assertEqual(errors, [])

    def test_shared_token_requires_all_consumers_and_source_files(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.manifest["allowed_tokens"] = ["color.action.primary"]
        fixture.manifest["allowed_components"] = []
        errors, _ = fixture.validate()
        self.assertTrue(any("additional surfaces_may_change" in error for error in errors))
        self.assertTrue(any("mapped impacted source file is not allowed" in error for error in errors))

    def test_baseline_updates_flag_is_never_allowed(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.manifest["baseline_updates_allowed"] = True
        errors, _ = fixture.validate()
        self.assertIn("change-manifest.baseline_updates_allowed must be false", errors)

    def test_changed_baseline_is_rejected(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        errors, protected = fixture.validate()
        self.assertEqual(errors, [])
        scope_errors = GUARD.verify_changed_files(
            ["tests/checkout.png"],
            fixture.manifest["allowed_files"],
            protected,
            "design/decisions/changes/CHG-1.json",
        )
        self.assertTrue(any("protected baseline" in error for error in scope_errors))

    def test_out_of_scope_source_file_is_rejected(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        errors, protected = fixture.validate()
        self.assertEqual(errors, [])
        scope_errors = GUARD.verify_changed_files(
            ["src/Settings.tsx"],
            fixture.manifest["allowed_files"],
            protected,
            "design/decisions/changes/CHG-1.json",
        )
        self.assertTrue(any("outside manifest scope" in error for error in scope_errors))

    def test_changed_baseline_hash_is_rejected_before_work(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        (fixture.root / "tests/checkout.png").write_text("changed pixels\n", encoding="utf-8")
        errors, _ = fixture.validate()
        self.assertTrue(any("protected baseline hash changed" in error for error in errors))

    def test_agent_cannot_approve_change_scope(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.manifest["approval"]["approved_by"] = "AI assistant"
        errors, _ = fixture.validate()
        self.assertTrue(any("human approver" in error for error in errors))

    def test_change_scope_requires_durable_approval_id(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.manifest["approval"]["approval_id"] = ""
        errors, _ = fixture.validate()
        self.assertTrue(any("approval_id is required" in error for error in errors))

    def test_capture_only_entry_is_not_a_protected_baseline(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.baseline["entries"][0]["kind"] = "capture-only"
        fixture.write_json("design/baselines/manifest.json", fixture.baseline)
        fixture.manifest["baseline_manifest_sha256"] = digest(
            fixture.root / "design/baselines/manifest.json"
        )
        errors, _ = fixture.validate()
        self.assertTrue(any("capture-only is not protected" in error for error in errors))

    def test_changed_contract_file_is_rejected_before_work(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        (fixture.root / "design/contract/source-map.json").write_text(
            "{}\n", encoding="utf-8"
        )
        fixture.manifest["source_map_sha256"] = digest(
            fixture.root / "design/contract/source-map.json"
        )
        errors, _ = fixture.validate()
        self.assertTrue(any("accepted contract file hash changed" in error for error in errors))

    def test_required_checks_cannot_be_omitted(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.manifest["required_checks"] = []
        errors, _ = fixture.validate()
        self.assertTrue(any("required_checks must not be empty" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
