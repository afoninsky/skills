#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("validate_design_contract.py")
SPEC = importlib.util.spec_from_file_location("validate_design_contract", SCRIPT_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ContractFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        for relative, content in {
            "design/contract/principles.md": "# Principles\nOne action dominates.\n",
            "design/contract/components.md": "# Components\nButton states.\n",
            "design/contract/content.md": "# Content\nTruthful labels.\n",
            "design/contract/responsive-and-adaptive.md": "# Adaptive\nReflow.\n",
            "design/decisions/acceptance.md": "# Acceptance\nHuman accepted CAND-7.\n",
            "src/tokens.css": ":root { --action: blue; }\n",
            "src/Button.tsx": "export function Button() {}\n",
            "tests/button.spec.ts": "// screenshot assertion\n",
            "tests/button.png": "golden bytes\n",
        }.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        self.source_map = {
            "schema_version": 1,
            "platform_architecture": [
                {
                    "id": "web",
                    "kind": "web",
                    "source_roots": ["src"],
                    "shares_ui_with": [],
                }
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
                    "surfaces": ["checkout"],
                }
            },
            "surfaces": {
                "checkout": {
                    "platforms": ["web"],
                    "components": ["Button"],
                    "targets": ["desktop"],
                    "baseline_entry_ids": ["checkout-default-desktop"],
                }
            },
            "intentional_variants": [],
        }
        self.write_json("design/contract/source-map.json", self.source_map)

        contract_files = []
        for role, relative in {
            "principles": "design/contract/principles.md",
            "components": "design/contract/components.md",
            "content": "design/contract/content.md",
            "responsive-adaptive": "design/contract/responsive-and-adaptive.md",
            "source-map": "design/contract/source-map.json",
        }.items():
            contract_files.append(
                {"role": role, "path": relative, "sha256": digest(root / relative)}
            )
        self.contract = {
            "schema_version": 1,
            "status": "accepted",
            "candidate_id": "CAND-7",
            "approval_id": "CONTRACT-APPROVAL-7",
            "accepted_by": "Product owner",
            "accepted_at": "2030-01-01T10:00:00Z",
            "accepted_ref": "abc1234",
            "approval_record": "design/decisions/acceptance.md",
            "files": contract_files,
        }
        self.baseline = {
            "schema_version": 1,
            "status": "accepted",
            "candidate_id": "CAND-7",
            "approval_id": "FREEZE-APPROVAL-7",
            "accepted_by": "Product owner",
            "accepted_at": "2030-01-01T10:00:00Z",
            "accepted_ref": "abc1234",
            "approval_record": "design/decisions/acceptance.md",
            "hard_gates": {
                "accessibility": {
                    "status": "evidenced",
                    "evidence": ["tests/button.spec.ts"],
                },
                "representative_user_evidence": {
                    "status": "not-evidenced",
                    "evidence": [],
                },
                "content_truth": {
                    "status": "not-evidenced",
                    "evidence": [],
                },
                "privacy_and_safety": {
                    "status": "not-evidenced",
                    "evidence": [],
                },
            },
            "entries": [
                {
                    "id": "checkout-default-desktop",
                    "kind": "asserted-golden",
                    "surface_id": "checkout",
                    "state": "default",
                    "target": "desktop",
                    "viewport": {"width": 1440, "height": 900},
                    "path": "tests/button.png",
                    "sha256": digest(root / "tests/button.png"),
                    "assertion_source": "tests/button.spec.ts",
                }
            ],
        }
        self.flush()

    def write_json(self, relative: str, data: object) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def flush(self) -> None:
        self.write_json("design/contract/manifest.json", self.contract)
        self.write_json("design/baselines/manifest.json", self.baseline)

    def validate(self, mode: str = "freeze") -> list[str]:
        self.flush()
        return VALIDATOR.validate_project(
            self.root,
            mode,
            "design/contract/manifest.json",
            "design/contract/source-map.json",
            "design/baselines/manifest.json",
            self.baseline["approval_id"] if mode == "freeze" else None,
        )


class ValidateDesignContractTests(unittest.TestCase):
    def make_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], ContractFixture]:
        temporary = tempfile.TemporaryDirectory()
        return temporary, ContractFixture(Path(temporary.name))

    def test_valid_freeze_passes(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        self.assertEqual(fixture.validate(), [])

    def test_agent_cannot_be_recorded_as_human_approver(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.baseline["accepted_by"] = "Codex"
        errors = fixture.validate()
        self.assertTrue(any("human approver" in error for error in errors))

    def test_capture_only_is_not_an_accepted_baseline(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.baseline["entries"][0]["kind"] = "capture-only"
        errors = fixture.validate()
        self.assertTrue(any("capture-only is not a baseline" in error for error in errors))

    def test_changed_golden_hash_fails(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        (fixture.root / "tests/button.png").write_text("new pixels\n", encoding="utf-8")
        errors = fixture.validate()
        self.assertTrue(any("sha256 does not match" in error for error in errors))

    def test_asserted_golden_requires_assertion_source(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.baseline["entries"][0]["assertion_source"] = ""
        errors = fixture.validate()
        self.assertTrue(any("assertion_source" in error for error in errors))

    def test_project_path_cannot_escape_root(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.contract["approval_record"] = "../approval.md"
        errors = fixture.validate()
        self.assertTrue(any("leaves the project root" in error for error in errors))

    def test_not_evidenced_gate_does_not_become_passed(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.baseline["hard_gates"]["accessibility"] = {
            "status": "not-evidenced",
            "evidence": [],
        }
        self.assertEqual(fixture.validate(), [])

    def test_freeze_requires_matching_router_approval_id(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        fixture.flush()
        args = (
            fixture.root,
            "freeze",
            "design/contract/manifest.json",
            "design/contract/source-map.json",
            "design/baselines/manifest.json",
        )
        errors = VALIDATOR.validate_project(*args)
        self.assertTrue(any("explicit approval ID" in error for error in errors))
        errors = VALIDATOR.validate_project(*args, "WRONG-APPROVAL")
        self.assertTrue(any("does not match" in error for error in errors))

    def test_accepted_baseline_requires_every_hard_gate_disposition(self) -> None:
        temporary, fixture = self.make_fixture()
        self.addCleanup(temporary.cleanup)
        del fixture.baseline["hard_gates"]["privacy_and_safety"]
        errors = fixture.validate()
        self.assertTrue(any("missing required dispositions" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
