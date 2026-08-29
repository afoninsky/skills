from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_toolchain", ROOT / "scripts" / "validate_toolchain.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ToolchainValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads((ROOT / "assets" / "toolchain.json").read_text(encoding="utf-8"))

    @staticmethod
    def capability(
        capability_id: str,
        *,
        requirement: str = "required",
        status: str = "available",
        evidence: str | None = "verified probe",
        degradation: str | None = None,
        confirmation_id: str | None = None,
    ) -> dict[str, object]:
        return {
            "id": capability_id,
            "requirement": requirement,
            "status": status,
            "selected_tool": capability_id,
            "version": "test",
            "evidence": evidence,
            "degradation": degradation,
            "confirmation_id": confirmation_id,
        }

    def execution_record(
        self,
        phase: str,
        capabilities: list[dict[str, object]],
        *,
        platforms: list[str] | None = None,
        claims: list[str] | None = None,
    ) -> dict[str, object]:
        record = copy.deepcopy(self.record)
        record["profile"] = {
            "phase": phase,
            "platforms": platforms or [],
            "claims": claims or [],
        }
        record["checked_at"] = datetime.now(timezone.utc).isoformat()
        record["capabilities"] = capabilities
        return record

    def test_unknown_starter_is_valid_before_execution(self) -> None:
        self.assertEqual(MODULE.validate_toolchain(self.record), [])

    def test_unselected_profile_blocks_execution(self) -> None:
        self.assertTrue(
            any(
                "must select a worker phase" in error
                for error in MODULE.validate_toolchain(self.record, for_execution=True)
            )
        )

    def test_execution_requires_fresh_check_timestamp(self) -> None:
        record = self.execution_record(
            "discovery", [self.capability("project-artifact-access")]
        )
        record["checked_at"] = None
        self.assertTrue(
            any(
                "checked_at" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_execution_rejects_stale_check_timestamp(self) -> None:
        record = self.execution_record(
            "discovery", [self.capability("project-artifact-access")]
        )
        record["checked_at"] = (
            datetime.now(timezone.utc) - timedelta(hours=4, seconds=1)
        ).isoformat()
        self.assertTrue(
            any(
                "checked_at" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_execution_rejects_excessively_future_check_timestamp(self) -> None:
        record = self.execution_record(
            "discovery", [self.capability("project-artifact-access")]
        )
        record["checked_at"] = (
            datetime.now(timezone.utc) + timedelta(minutes=5, seconds=1)
        ).isoformat()
        self.assertTrue(
            any(
                "checked_at" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_execution_rejects_naive_check_timestamp(self) -> None:
        record = self.execution_record(
            "discovery", [self.capability("project-artifact-access")]
        )
        record["checked_at"] = datetime.now().isoformat()
        self.assertTrue(
            any(
                "checked_at" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_empty_capability_list_cannot_bypass_phase_profile(self) -> None:
        record = self.execution_record("discovery", [])
        self.assertTrue(
            any(
                "project-artifact-access" in error and "omitted" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_phase_profile_requires_every_capability(self) -> None:
        record = self.execution_record(
            "direction", [self.capability("versioned-candidate-isolation")]
        )
        self.assertTrue(
            any(
                "matched-render-and-capture" in error and "omitted" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_direction_and_prototype_require_platforms(self) -> None:
        cases = {
            "direction": [
                self.capability("versioned-candidate-isolation"),
                self.capability("matched-render-and-capture"),
            ],
            "prototype": [
                self.capability("versioned-prototype-isolation"),
                self.capability("target-render-and-capture"),
            ],
        }
        for phase, capabilities in cases.items():
            with self.subTest(phase=phase):
                record = self.execution_record(phase, capabilities)
                errors = MODULE.validate_toolchain(record, for_execution=True)
                self.assertTrue(
                    any("platforms must not be empty" in error for error in errors)
                )
                record["profile"]["platforms"] = ["web"]
                self.assertEqual(
                    MODULE.validate_toolchain(record, for_execution=True), []
                )

    def test_available_requires_evidence(self) -> None:
        record = self.execution_record(
            "discovery", [self.capability("project-artifact-access", evidence=None)]
        )
        self.assertTrue(
            any("requires evidence" in error for error in MODULE.validate_toolchain(record))
        )
        record["capabilities"][0]["evidence"] = "workspace read/write probe"
        self.assertEqual(MODULE.validate_toolchain(record, for_execution=True), [])

    def test_non_hard_conditional_degradation_requires_confirmation(self) -> None:
        record = self.execution_record(
            "discovery",
            [
                self.capability("project-artifact-access"),
                self.capability(
                    "structured-flow-source",
                    requirement="conditional",
                    status="missing-degradable",
                    evidence=None,
                    degradation="Use an approved text flow instead.",
                ),
            ],
        )
        self.assertTrue(
            any(
                "confirmation_id" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )
        record["capabilities"][1]["confirmation_id"] = "CONFIRM-001"
        self.assertEqual(MODULE.validate_toolchain(record, for_execution=True), [])

    def test_required_capability_cannot_be_degraded_by_confirmation(self) -> None:
        record = self.execution_record(
            "discovery",
            [
                self.capability(
                    "project-artifact-access",
                    status="missing-degradable",
                    evidence=None,
                    degradation="No durable artifact access.",
                    confirmation_id="CONFIRM-001",
                )
            ],
        )
        self.assertTrue(
            any(
                "required capability cannot be degraded" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_hard_gate_cannot_be_misclassified_as_conditional_degradation(self) -> None:
        record = self.execution_record(
            "discovery",
            [
                self.capability("project-artifact-access"),
                self.capability(
                    "web-runtime-and-visual-regression",
                    requirement="conditional",
                    status="missing-degradable",
                    evidence=None,
                    degradation="Source-only review.",
                    confirmation_id="CONFIRM-001",
                ),
            ],
        )
        self.assertTrue(
            any(
                "hard-gate capability cannot be degraded" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )

    def test_web_implementation_requires_runtime_and_accessibility(self) -> None:
        record = self.execution_record(
            "implementation",
            [
                self.capability("versioning-and-rollback"),
                self.capability("approved-input-identity"),
                self.capability("target-build-toolchain"),
                self.capability("web-runtime-and-visual-regression"),
            ],
            platforms=["web"],
        )
        errors = MODULE.validate_toolchain(record, for_execution=True)
        self.assertTrue(
            any("web-accessibility" in error and "omitted" in error for error in errors)
        )
        record["capabilities"].append(self.capability("web-accessibility"))
        self.assertEqual(MODULE.validate_toolchain(record, for_execution=True), [])

    def test_shared_wrapper_requires_both_runtime_layers(self) -> None:
        record = self.execution_record(
            "change",
            [
                self.capability("versioning-and-rollback"),
                self.capability("scope-and-hash-validation"),
                self.capability("web-runtime-and-visual-regression"),
                self.capability("web-accessibility"),
            ],
            platforms=["shared-web-wrapper"],
        )
        errors = MODULE.validate_toolchain(record, for_execution=True)
        self.assertTrue(any("mobile-runtime-and-visual-regression" in error for error in errors))
        self.assertTrue(any("native-accessibility" in error for error in errors))
        record["capabilities"].extend(
            [
                self.capability("mobile-runtime-and-visual-regression"),
                self.capability("native-accessibility"),
            ]
        )
        self.assertEqual(MODULE.validate_toolchain(record, for_execution=True), [])

    def test_blocking_capability_never_permits_execution(self) -> None:
        record = self.execution_record(
            "discovery",
            [
                self.capability(
                    "project-artifact-access",
                    status="missing-blocking",
                    evidence=None,
                    degradation="No durable artifact access.",
                    confirmation_id="CONFIRM-001",
                )
            ],
        )
        self.assertTrue(
            any(
                "does not permit execution" in error
                for error in MODULE.validate_toolchain(record, for_execution=True)
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
