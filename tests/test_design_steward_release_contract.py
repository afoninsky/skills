from __future__ import annotations

import json
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DESIGN_STEWARD = REPOSITORY_ROOT / "deprecated" / "design-steward"


class DesignStewardReleaseContractTests(unittest.TestCase):
    def test_skill_declares_release_version_and_response_contract(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")

        for required in (
            'metadata: {version: "4.1.0"}',
            "## Preflight the required grilling skill",
            "## Check every gate response",
            "Blocking Unknowns",
            "Working Assumptions",
            "Write **None** for an empty category",
            "obtain the named System Owner's reapproval before affected work continues",
            "owner-originated input",
            "preference as stakeholder input",
            "content/data rules",
            "semantic structure, focus, keyboard",
            "Unassigned — Blocking Unknown",
            "record one status for every applicable gate",
            "one approval cannot substitute for another",
        ):
            self.assertIn(required, skill)

    def test_g4_requires_professional_quality_not_process_compliance(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        quality = DESIGN_STEWARD.joinpath(
            "references", "design-quality.md"
        ).read_text(encoding="utf-8")
        combined = skill + quality

        for required in (
            "professional design quality",
            "product-specific",
            "screenshot-first",
            "Relabel test",
            "Default-cluster test",
            "Core-act test",
            "First-ten-seconds test",
            "review harness",
            "Strong",
            "E0 generated design judgment",
            "Avoid 100-point scoring by a single model",
        ):
            self.assertIn(required, combined)

    def test_direction_workflow_is_staged_and_budgeted(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        directions = DESIGN_STEWARD.joinpath(
            "references", "directions-and-artifacts.md"
        ).read_text(encoding="utf-8")
        combined = skill + directions

        for required in (
            "12–15 raw concepts",
            "six materially distinct territories",
            "three developed directions",
            "one backbone",
            "representative frame",
            "six-up contact sheet",
            "Build only surviving proof",
            "artifact, iteration, time, and delegation budget",
            "living delegation ledger",
            "Do not build six prototypes",
            "Do not increase direction count",
        ):
            self.assertIn(required, combined)

    def test_operating_plan_output_has_a_token_budget(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        rapid_loop = DESIGN_STEWARD.joinpath(
            "references", "rapid-design-loop.md"
        ).read_text(encoding="utf-8")
        combined = skill + rapid_loop

        for required in (
            "at most 600 words by default",
            "Do not recite every gate",
            "Do not replay the complete gate or assurance catalog",
            "exact next action",
        ):
            self.assertIn(required, combined)

    def test_gate_review_preserves_status_semantics_and_traceability(self) -> None:
        gate_review = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "records", "gate-review.md"
        ).read_text(encoding="utf-8")

        for required in (
            "Status: Pass / Fail / Not yet evidenced",
            "Impact review and System Owner reapproval",
            "Evidence contradictions and gaps",
            "Requirement / evidence / assumption / artifact / delta trace links",
        ):
            self.assertIn(required, gate_review)

    def test_design_brief_schema_enforces_outcome_quality_and_coverage(self) -> None:
        brief = json.loads(
            DESIGN_STEWARD.joinpath(
                "assets", "engagement-starter", "design-brief.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(brief["schema_version"], "4.0.0")
        self.assertEqual(brief["operating_mode"], "Design-intent grilling")
        self.assertIn("engagement_type", brief)
        self.assertIn("grilling", brief)
        self.assertIn("dependency_preflight", brief)
        self.assertEqual(
            brief["dependency_preflight"]["required_skill"], "grilling or grill-me"
        )
        self.assertIn("owner_design_intent", brief)
        self.assertIn("shared_understanding", brief)
        self.assertIn("system_owner", brief["authority"])
        for required in (
            "product_experience_thesis",
            "complete_experience_scope",
            "product_idea_to_make_obvious",
            "professional_quality_bar",
            "artifact_iteration_delegation_budget",
            "first_visible_artifact_target",
            "max_preselection_revision_loops_per_direction",
            "feedback_checkpoint_plan",
            "deferred_assurance_plan",
            "stopping_point",
        ):
            self.assertIn(required, brief["success_contract"])

        self.assertIn("roles_and_domains", brief["users_and_contexts"])
        self.assertIn("priority_handoffs", brief["users_and_contexts"])
        self.assertIn(
            "professional_quality_criteria", brief["comparison_contract"]
        )
        self.assertIn("numeric_scoring_policy", brief["comparison_contract"])

    def test_grilling_composes_base_skill_without_copying_it(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        wrapper = DESIGN_STEWARD.joinpath(
            "references", "design-intent-grilling.md"
        ).read_text(encoding="utf-8")
        owner_brief = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "owner-design-brief.md"
        ).read_text(encoding="utf-8")
        combined = skill + wrapper + owner_brief

        for required in (
            "Design-intent grilling",
            "Autonomous design",
            "installed `grilling` or `grill-me` skill",
            "does not replace or restate",
            "Ask one neutral question",
            "Owner's unaided response",
            "no more than three materially distinct",
            "Does this brief represent our shared understanding, and may Design Steward enter autonomous design mode?",
        ):
            self.assertIn(required, combined)

    def test_owner_design_brief_contains_required_authority_and_intent(self) -> None:
        template = DESIGN_STEWARD.joinpath(
            "assets", "engagement-starter", "owner-design-brief.md"
        ).read_text(encoding="utf-8")

        for required in (
            "System Owner name and role",
            "Core user act or transformation",
            "Intended first-ten-seconds hierarchy",
            "Accepted trade-offs and risk tolerance",
            "Unacceptable outcomes",
            "Rejection criteria",
            "Owner-originated preferences",
            "Steward recommendations",
            "Material disagreements and resolutions",
            "Authorization boundaries",
            "Consequential decision provenance",
        ):
            self.assertIn(required, template)

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
            "System Owner G5/release decision record ID",
            "State-fixture and coverage manifest",
            "Matched implementation fidelity",
            "Engineering source acceptance",
            "Design-integration acceptance",
            "Preview or deployed fidelity",
            "Non-implementing fidelity reviewer",
        ):
            self.assertIn(required, contract)

    def test_recovery_state_is_required_and_roadmap_ready(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        state_reference = DESIGN_STEWARD.joinpath(
            "references", "state-and-roadmap.md"
        ).read_text(encoding="utf-8")
        state = json.loads(
            DESIGN_STEWARD.joinpath(
                "assets", "engagement-starter", "steward-state.json"
            ).read_text(encoding="utf-8")
        )
        combined = skill + state_reference

        for required in (
            "canonical recovery spine",
            "read it completely first",
            "exact next action",
            "every material decision",
            "generate_engagement_roadmap.py",
            "single-page roadmap",
        ):
            self.assertIn(required, combined)

        self.assertEqual(state["schema_version"], "1.0.0")
        self.assertEqual(state["record_type"], "design-steward-state")
        for required in (
            "dependency_preflight",
            "resume",
            "decisions",
            "research_and_materials",
            "funnel",
            "artifacts",
            "coverage",
            "implementation",
            "roadmap",
        ):
            self.assertIn(required, state)

        self.assertEqual(
            [item["gate"] for item in state["roadmap"]],
            ["G0", "G1", "G2", "G3", "G4", "G5", "G6"],
        )
        for item in state["roadmap"]:
            for required in (
                "status",
                "decision_or_result",
                "evidence_ids",
                "artifact_ids",
                "open_items",
            ):
                self.assertIn(required, item)

    def test_g5_fidelity_rejects_semantic_only_acceptance(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        quality = DESIGN_STEWARD.joinpath(
            "references", "design-quality.md"
        ).read_text(encoding="utf-8")
        combined = skill + quality

        for required in (
            "paired captures",
            "identical state",
            "central working width",
            "legacy-shell reuse",
            "Engineering source acceptance",
            "design-integration acceptance",
            "preview or deployed fidelity",
            "non-implementing fidelity review",
            "A source-only pass cannot establish design integration",
        ):
            self.assertIn(required, combined)

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

    def test_delegation_is_bounded_and_not_a_funnel_default(self) -> None:
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
            "Do not delegate to increase concept count",
            "does not require 12–15 agents, six agents, or even three agents",
            "one fresh, history-free sub-agent per developed direction only when",
            "no claim that their authorship was independent",
            "fresh critic only when",
            "Not yet evidenced",
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
            "Keeps raw concepts, six-territory formation, narrowing, and synthesis with the Steward",
            "Does not create one agent per concept or territory",
            "Uses isolated direction authors only when a named decision risk requires independence",
            "Keeps gate recommendation, direction selection, and human approval with the Steward",
        ):
            self.assertIn(required, expectations)

    def test_real_failure_modes_have_behavioral_evals(self) -> None:
        benchmark = json.loads(
            DESIGN_STEWARD.joinpath("evals", "benchmark.json").read_text(
                encoding="utf-8"
            )
        )
        cases = {case["id"]: case for case in benchmark["evals"]}
        self.assertTrue({12, 13, 14, 15, 16, 17, 18, 19}.issubset(cases))

        expectations = " ".join(
            expectation
            for case_id in (12, 13, 14, 15, 16, 17, 18, 19)
            for expectation in cases[case_id]["expectations"]
        )
        for required in (
            "generic rendered work",
            "end to end",
            "reviewer controls and provenance chrome",
            "living ledger",
            "direction multiplication",
            "first useful visible artifact within 15 active minutes of generation authorization",
            "Defers mobile, exhaustive accessibility, browser, history, portability, migration, telemetry, and implementation checks",
            "Does not create pairwise critics, remediation agents, or deterministic recheck agents",
        ):
            self.assertIn(required, expectations)

    def test_recovery_dependency_and_fidelity_failures_have_behavioral_evals(self) -> None:
        benchmark = json.loads(
            DESIGN_STEWARD.joinpath("evals", "benchmark.json").read_text(
                encoding="utf-8"
            )
        )
        cases = {case["id"]: case for case in benchmark["evals"]}
        self.assertTrue({26, 27, 28, 29, 30}.issubset(cases))

        expectations = " ".join(
            expectation
            for case_id in (26, 27, 28, 29, 30)
            for expectation in cases[case_id]["expectations"]
        )
        for required in (
            "installed and readable grilling or grill-me skill",
            "canonical recovery spine",
            "central working width",
            "visible global destinations",
            "exact nested clean URL",
        ):
            self.assertIn(required, expectations)

    def test_rapid_design_loop_is_latency_budgeted_and_fidelity_aware(self) -> None:
        rapid_loop = DESIGN_STEWARD.joinpath(
            "references", "rapid-design-loop.md"
        ).read_text(encoding="utf-8")
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        combined = skill + rapid_loop

        for required in (
            "within 15 minutes of active work",
            "No-blocker readiness overhead",
            "target no more than 25 active minutes from task start",
            "before 25%",
            "at least 50%",
            "at most two bounded revision loops",
            "A visible checkpoint is not an extra approval gate",
            "Checks by fidelity",
            "no delegation for raw concepts or territories",
            "one isolated author per developed direction and one non-author critic only when",
            "A check that cannot change the current promote/pivot/reject decision is premature",
            "Do not create routine G1 auditors",
            "once per generation wave",
        ):
            self.assertIn(required, combined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
