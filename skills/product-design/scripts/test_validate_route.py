from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_route", ROOT / "scripts" / "validate_route.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RouteValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.contract = json.loads(
            (ROOT / "assets" / "route-contract.json").read_text(encoding="utf-8")
        )
        self.envelope = json.loads(
            (ROOT / "assets" / "routing-envelope.json").read_text(encoding="utf-8")
        )
        self.handoff = json.loads(
            (ROOT / "assets" / "worker-handoff.json").read_text(encoding="utf-8")
        )

    def assert_has_error(self, errors: list[str], fragment: str) -> None:
        self.assertTrue(
            any(fragment in error for error in errors),
            f"expected {fragment!r} in {errors!r}",
        )

    @staticmethod
    def toolchain_context(
        phase: str,
        *,
        platforms: list[str] | None = None,
        claims: list[str] | None = None,
    ) -> dict[str, object]:
        return {
            "schema_version": "1.0.0",
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "profile": {
                "phase": phase,
                "platforms": platforms or [],
                "claims": claims or [],
            },
            "capabilities": [
                {
                    "id": "project-artifact-access",
                    "requirement": "required",
                    "status": "available",
                    "selected_tool": "project files",
                    "version": "test",
                    "evidence": "verified test fixture access",
                    "degradation": None,
                    "confirmation_id": None,
                }
            ],
        }

    @staticmethod
    def run_cli(
        envelope: dict[str, object],
        *,
        toolchain: dict[str, object] | None = None,
        for_execution: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp_directory:
            temp_root = Path(temp_directory)
            envelope_path = temp_root / "routing-envelope.json"
            envelope_path.write_text(json.dumps(envelope), encoding="utf-8")
            command = [sys.executable, str(ROOT / "scripts" / "validate_route.py"), str(envelope_path)]
            if toolchain is not None:
                toolchain_path = temp_root / "toolchain.json"
                toolchain_path.write_text(json.dumps(toolchain), encoding="utf-8")
                command.extend(["--toolchain", str(toolchain_path)])
            if for_execution:
                command.append("--for-execution")
            return subprocess.run(command, capture_output=True, text=True, check=False)

    def test_starter_envelope_and_handoff_are_valid(self) -> None:
        self.assertEqual(MODULE.validate_envelope(self.envelope, self.contract), [])
        self.assertEqual(MODULE.validate_handoff(self.handoff, self.envelope, self.contract), [])

    def test_invalid_transition_is_rejected(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope["route"] = ["product-design-discovery", "product-design-change"]
        self.assert_has_error(
            MODULE.validate_envelope(envelope, self.contract), "invalid transition"
        )

    def test_change_worker_cannot_update_baseline(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope["route"] = ["product-design-change"]
        handoff = copy.deepcopy(self.handoff)
        handoff["worker"] = "product-design-change"
        handoff["baseline_changed"] = True
        self.assert_has_error(
            MODULE.validate_handoff(handoff, envelope, self.contract),
            "outside explicit accept-freeze",
        )

    def test_accept_freeze_requires_contract_authority_and_approval(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope.update(
            {
                "route": ["product-design-contract"],
                "current_phase": "accept-freeze",
                "mutation_authority": "accept-freeze",
                "owner_gate": "E",
                "baseline_updates_allowed": True,
            }
        )
        self.assert_has_error(
            MODULE.validate_envelope(envelope, self.contract),
            "accept_freeze_approval_id",
        )
        envelope["accept_freeze_approval_id"] = "APPROVAL-001"
        self.assertEqual(MODULE.validate_envelope(envelope, self.contract), [])

        envelope["mutation_authority"] = "design-artifacts-only"
        self.assert_has_error(
            MODULE.validate_envelope(envelope, self.contract),
            "accept-freeze mutation authority",
        )

    def test_prompt_and_accepted_input_hashes_must_survive_handoff(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["input_hashes"]["original_prompt"] = "0" * 64
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "original_prompt",
        )

        envelope = copy.deepcopy(self.envelope)
        envelope["accepted_inputs"] = [
            {"id": "brief", "path": "design/brief.md", "sha256": "1" * 64}
        ]
        handoff = copy.deepcopy(self.handoff)
        self.assert_has_error(
            MODULE.validate_handoff(handoff, envelope, self.contract), "'brief'"
        )
        handoff["input_hashes"]["brief"] = "1" * 64
        self.assertEqual(MODULE.validate_handoff(handoff, envelope, self.contract), [])

    def test_gate_must_match_owner_gate_and_needs_owner_status(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["gate"] = "F"
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "does not match",
        )
        handoff["gate"] = "A"
        handoff["status"] = "complete"
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "requires needs-owner",
        )

    def test_non_null_gate_requires_handoff_evidence(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["evidence"] = []
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "requires non-empty evidence",
        )

    def test_recommendation_must_be_known_allowed_and_declared(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["recommended_next_worker"] = "product-design-change"
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "invalid recommended transition",
        )

        envelope = copy.deepcopy(self.envelope)
        envelope["route"] = [
            "product-design-discovery",
            "product-design-direction",
        ]
        handoff["recommended_next_worker"] = None
        self.assert_has_error(
            MODULE.validate_handoff(handoff, envelope, self.contract),
            "declared next route item",
        )

    def test_blocked_or_failed_handoff_cannot_advance(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["status"] = "blocked"
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "cannot recommend a successor",
        )
        envelope = copy.deepcopy(self.envelope)
        envelope["route"] = ["product-design-discovery", "product-design-direction"]
        handoff["gate"] = None
        handoff["recommended_next_worker"] = None
        self.assertEqual(MODULE.validate_handoff(handoff, envelope, self.contract), [])

    def test_implementation_requires_explicit_gate_c_or_bounded_slice_basis(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope.update(
            {
                "route": ["product-design-implementation"],
                "current_phase": "implementation",
                "mutation_authority": "production-bounded",
                "writes_allowed": ["src/"],
                "owner_gate": "D",
            }
        )
        self.assert_has_error(
            MODULE.validate_envelope(envelope, self.contract),
            "implementation requires gate-c-approved",
        )
        envelope["implementation_entry_basis"] = "gate-c-approved"
        envelope["implementation_entry_approval_id"] = "GATE-C-001"
        self.assertEqual(MODULE.validate_envelope(envelope, self.contract), [])

    def test_review_requires_read_only_authority_and_no_writes(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope.update(
            {
                "route": ["product-design-review"],
                "current_phase": "review",
                "owner_gate": None,
            }
        )
        self.assert_has_error(
            MODULE.validate_envelope(envelope, self.contract), "review requires read-only"
        )
        envelope["mutation_authority"] = "read-only"
        envelope["writes_allowed"] = []
        self.assertEqual(MODULE.validate_envelope(envelope, self.contract), [])

    def test_degraded_handoff_requires_router_confirmation(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["degraded_capabilities"] = [
            {
                "id": "structured-visual-context",
                "confirmation_id": "CONF-1",
                "limitation": "Annotated export only.",
            }
        ]
        self.assert_has_error(
            MODULE.validate_handoff(handoff, self.envelope, self.contract),
            "not authorized",
        )
        envelope = copy.deepcopy(self.envelope)
        envelope["degradation_confirmation_ids"] = ["CONF-1"]
        self.assertEqual(MODULE.validate_handoff(handoff, envelope, self.contract), [])

    def test_candidate_review_and_freeze_are_separate_gate_envelopes(self) -> None:
        review_envelope = copy.deepcopy(self.envelope)
        review_envelope.update(
            {
                "route": ["product-design-review"],
                "current_phase": "review",
                "mutation_authority": "read-only",
                "writes_allowed": [],
                "owner_gate": "D",
            }
        )
        review_handoff = copy.deepcopy(self.handoff)
        review_handoff.update(
            {
                "worker": "product-design-review",
                "status": "needs-owner",
                "gate": "D",
                "recommended_next_worker": None,
            }
        )
        self.assertEqual(MODULE.validate_envelope(review_envelope, self.contract), [])
        self.assertEqual(
            MODULE.validate_handoff(review_handoff, review_envelope, self.contract), []
        )

        freeze_envelope = copy.deepcopy(self.envelope)
        freeze_envelope.update(
            {
                "route": ["product-design-contract"],
                "current_phase": "accept-freeze",
                "mutation_authority": "accept-freeze",
                "owner_gate": "E",
                "baseline_updates_allowed": True,
                "accept_freeze_approval_id": "FREEZE-001",
            }
        )
        freeze_handoff = copy.deepcopy(self.handoff)
        freeze_handoff.update(
            {
                "worker": "product-design-contract",
                "status": "complete",
                "baseline_changed": True,
                "gate": None,
                "recommended_next_worker": None,
            }
        )
        self.assertEqual(MODULE.validate_envelope(freeze_envelope, self.contract), [])
        self.assertEqual(
            MODULE.validate_handoff(freeze_handoff, freeze_envelope, self.contract), []
        )

    def test_execution_context_requires_exact_phase_and_platform_match(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope["platforms"] = ["web"]
        matching = self.toolchain_context("discovery", platforms=["web"])
        self.assertEqual(
            MODULE.validate_route_context(envelope, matching, for_execution=True), []
        )

        wrong_phase = self.toolchain_context("direction", platforms=["web"])
        self.assert_has_error(
            MODULE.validate_route_context(envelope, wrong_phase, for_execution=True),
            "phase must exactly match",
        )

        wrong_platform = self.toolchain_context(
            "discovery", platforms=["native-mobile"]
        )
        self.assert_has_error(
            MODULE.validate_route_context(envelope, wrong_platform, for_execution=True),
            "platforms must exactly match",
        )

    def test_gate_b_and_c_require_non_empty_platforms(self) -> None:
        for gate, worker, phase in (
            ("B", "product-design-direction", "direction"),
            ("C", "product-design-prototype", "prototype"),
        ):
            with self.subTest(gate=gate):
                envelope = copy.deepcopy(self.envelope)
                envelope.update(
                    {
                        "route": [worker],
                        "current_phase": phase,
                        "owner_gate": gate,
                        "platforms": [],
                    }
                )
                toolchain = self.toolchain_context(phase)
                self.assert_has_error(
                    MODULE.validate_route_context(
                        envelope, toolchain, for_execution=True
                    ),
                    f"Gate {gate} requires at least one platform",
                )

                envelope["platforms"] = ["web"]
                toolchain["profile"]["platforms"] = ["web"]
                self.assertEqual(
                    MODULE.validate_route_context(
                        envelope, toolchain, for_execution=True
                    ),
                    [],
                )

    def test_gate_d_requires_review_and_both_acceptance_claims(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope.update(
            {
                "route": ["product-design-review"],
                "current_phase": "review",
                "owner_gate": "D",
                "platforms": ["web"],
            }
        )
        incomplete = self.toolchain_context(
            "review", platforms=["web"], claims=["visual-acceptance"]
        )
        self.assert_has_error(
            MODULE.validate_route_context(envelope, incomplete, for_execution=True),
            "accessibility-acceptance",
        )

        complete = self.toolchain_context(
            "review",
            platforms=["web"],
            claims=["visual-acceptance", "accessibility-acceptance"],
        )
        self.assertEqual(
            MODULE.validate_route_context(envelope, complete, for_execution=True), []
        )

        envelope["current_phase"] = "implementation"
        wrong_phase = self.toolchain_context(
            "implementation",
            platforms=["web"],
            claims=["visual-acceptance", "accessibility-acceptance"],
        )
        self.assert_has_error(
            MODULE.validate_route_context(envelope, wrong_phase, for_execution=True),
            "Gate D is valid only for phase 'review'",
        )

    def test_gate_e_requires_accept_freeze_context(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope.update(
            {
                "route": ["product-design-contract"],
                "current_phase": "accept-freeze",
                "owner_gate": "E",
                "platforms": ["web"],
            }
        )
        toolchain = self.toolchain_context("accept-freeze", platforms=["web"])
        self.assertEqual(
            MODULE.validate_route_context(envelope, toolchain, for_execution=True), []
        )

        envelope["current_phase"] = "contract"
        toolchain["profile"]["phase"] = "contract"
        self.assert_has_error(
            MODULE.validate_route_context(envelope, toolchain, for_execution=True),
            "Gate E is valid only for phase 'accept-freeze'",
        )

    def test_gate_f_requires_review_and_release_or_representative_user_claim(self) -> None:
        envelope = copy.deepcopy(self.envelope)
        envelope.update(
            {
                "route": ["product-design-review"],
                "current_phase": "review",
                "owner_gate": "F",
                "platforms": ["web"],
            }
        )
        no_decision_claim = self.toolchain_context("review", platforms=["web"])
        self.assert_has_error(
            MODULE.validate_route_context(
                envelope, no_decision_claim, for_execution=True
            ),
            "release or representative-user",
        )

        for claim in ("release", "representative-user"):
            with self.subTest(claim=claim):
                toolchain = self.toolchain_context(
                    "review", platforms=["web"], claims=[claim]
                )
                self.assertEqual(
                    MODULE.validate_route_context(
                        envelope, toolchain, for_execution=True
                    ),
                    [],
                )

        envelope["current_phase"] = "direction"
        wrong_phase = self.toolchain_context(
            "direction", platforms=["web"], claims=["representative-user"]
        )
        self.assert_has_error(
            MODULE.validate_route_context(envelope, wrong_phase, for_execution=True),
            "Gate F is valid only for phase 'review'",
        )

    def test_cli_structural_validation_does_not_require_toolchain(self) -> None:
        result = self.run_cli(self.envelope)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_cli_execution_requires_explicit_toolchain(self) -> None:
        result = self.run_cli(self.envelope, for_execution=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("--toolchain is required with --for-execution", result.stderr)

    def test_cli_execution_loads_and_binds_toolchain(self) -> None:
        matching = self.toolchain_context("discovery")
        result = self.run_cli(
            self.envelope, toolchain=matching, for_execution=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)

        mismatched = self.toolchain_context("direction")
        result = self.run_cli(
            self.envelope, toolchain=mismatched, for_execution=True
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("phase must exactly match", result.stderr)

    def test_cli_execution_rejects_blocked_bound_toolchain(self) -> None:
        blocked = self.toolchain_context("discovery")
        blocked["capabilities"][0].update(
            {
                "status": "missing-blocking",
                "evidence": None,
                "degradation": "Project artifacts are inaccessible.",
            }
        )
        result = self.run_cli(self.envelope, toolchain=blocked, for_execution=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not permit execution", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
