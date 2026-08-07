from __future__ import annotations

import json
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DESIGN_STEWARD = REPOSITORY_ROOT / "skills" / "design-steward"


class DesignStewardReleaseContractTests(unittest.TestCase):
    def test_skill_declares_release_version_and_response_contract(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")

        for required in (
            'metadata: {version: "1.1.0"}',
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

    def test_required_subagent_orchestration_is_explicit(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        operating_contract = DESIGN_STEWARD.joinpath(
            "references", "operating-contract.md"
        ).read_text(encoding="utf-8")
        directions = DESIGN_STEWARD.joinpath(
            "references", "directions-and-artifacts.md"
        ).read_text(encoding="utf-8")
        delegation = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "delegation-packet.md"
        ).read_text(encoding="utf-8")

        combined = skill + operating_contract + directions
        for required in (
            "Required sub-agent",
            "one fresh, history-free sub-agent per approved direction",
            "never reuse one agent for sibling directions",
            "dispatch independent directions and research questions in parallel",
            "run required delegations sequentially as fresh agents",
            "fresh critic who authored none",
            "Claim parallel execution only when",
            "submission before the first join",
            "used a skill only when its return confirms",
            "Not yet evidenced",
            "do not silently perform the supposedly independent",
        ):
            self.assertIn(required, combined)

        for required in (
            "Necessity class",
            "Fresh agent/session ID",
            "No inherited sibling-output evidence",
            "Actual dispatch mode",
            "Concurrency evidence",
            "Actual skill names and versions/content hashes read",
            "Actual product sources accessed",
            "Files written",
            "Safe parallel group",
            "Join condition",
        ):
            self.assertIn(required, delegation)

    def test_orchestration_has_a_behavioral_eval(self) -> None:
        benchmark = json.loads(
            DESIGN_STEWARD.joinpath("evals", "benchmark.json").read_text(
                encoding="utf-8"
            )
        )
        orchestration = next(case for case in benchmark["evals"] if case["id"] == 11)
        expectations = " ".join(orchestration["expectations"])

        for required in (
            "one fresh history-free sub-agent per direction",
            "Claims parallel execution only",
            "fresh critic who authored none",
            "separates instruction/reference access, product-source access, and writes",
            "Keeps synthesis, gate recommendation, direction selection, and human approval",
        ):
            self.assertIn(required, expectations)


if __name__ == "__main__":
    unittest.main(verbosity=2)
