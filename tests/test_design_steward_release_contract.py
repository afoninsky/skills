from __future__ import annotations

import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DESIGN_STEWARD = REPOSITORY_ROOT / "skills" / "design-steward"


class DesignStewardReleaseContractTests(unittest.TestCase):
    def test_skill_declares_release_version_and_response_contract(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")

        for required in (
            'metadata: {version: "1.0.0"}',
            "## Check every gate response",
            "Blocking Unknowns",
            "Working Assumptions",
            "Write **None** for an empty category",
            "obtain the named Product Owner's reapproval before generation or continuation",
            "information architecture, navigation, interaction, content structure, and visual language",
            "domain meaning, evidence, duties, platform realities, and explicit Fixed constraints",
            "original context, abstracted principle, rights, transformation, and transfer limitations",
            "content rules, data rules",
            "semantic structure",
            "focus behavior, keyboard operation",
            "Unassigned — Blocking Unknown",
            "record exactly one status for each applicable gate",
            "one approval cannot substitute for another",
        ):
            self.assertIn(required, skill)

    def test_gate_review_preserves_status_semantics_and_traceability(self) -> None:
        gate_review = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "gate-review.md"
        ).read_text(encoding="utf-8")

        for required in (
            "Status: Pass / Fail / Not yet evidenced",
            "Impact review and Product Owner reapproval",
            "Evidence contradictions and gaps",
            "Requirement / evidence / assumption / artifact / delta trace links",
        ):
            self.assertIn(required, gate_review)

    def test_direction_charter_captures_mode_and_precedent_contract(self) -> None:
        charter = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "direction-charter.md"
        ).read_text(encoding="utf-8")

        for required in (
            "From-scratch Open-by-default set",
            "From-scratch binding IDs",
            "Original context",
            "Abstracted principle",
            "Rights/permission",
            "Transfer limitations",
        ):
            self.assertIn(required, charter)

    def test_implementation_contract_has_complete_g5_trace(self) -> None:
        contract = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "implementation-contract.md"
        ).read_text(encoding="utf-8")

        for required in (
            "Content and data rules mapped to integrated behavior",
            "Semantic structure mapped and inspected",
            "Focus order, focus restoration, and keyboard operation",
            "Responsive, error, empty, loading, partial-permission",
            "Recovery behavior and truthful persistence/loss handling",
            "Instrumentation and denominator/segmentation rules",
            "Engineering acceptance record ID",
            "Specialist claim-owner dispositions and evidence IDs",
            "Product Owner G5/release decision record ID",
        ):
            self.assertIn(required, contract)

    def test_record_graph_has_atomic_requirement_and_evidence_links(self) -> None:
        requirement_register = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "requirement-register.md"
        ).read_text(encoding="utf-8")
        evidence_register = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "evidence-register.md"
        ).read_text(encoding="utf-8")
        contract = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "implementation-contract.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Requirement ID", requirement_register)
        self.assertIn("Evidence IDs", requirement_register)
        self.assertIn("Assumption IDs", requirement_register)
        self.assertIn("Claim ID and scoped claim", evidence_register)
        self.assertIn("Artifact/release", evidence_register)
        self.assertIn("Acceptance evidence IDs", contract)


if __name__ == "__main__":
    unittest.main(verbosity=2)
