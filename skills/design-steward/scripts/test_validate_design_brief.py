from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import ModuleType

SCRIPT_PATH = Path(__file__).with_name("validate_design_brief.py")
TEMPLATE_PATH = SCRIPT_PATH.parents[1] / "assets" / "engagement-starter" / "design-brief.json"


def load_validator() -> ModuleType:
    spec = importlib.util.spec_from_file_location("validate_design_brief", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load validate_design_brief.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


def ready_brief() -> dict[str, object]:
    brief = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
    brief.update(
        {
            "brief_id": "BRIEF-001",
            "status": "Accepted",
            "operating_mode": "Autonomous design",
            "engagement_type": "From-scratch",
            "evidence_gap_rationale": "No prior evidence exists; research questions are recorded at G2.",
        }
    )
    brief["authority"] = {
        "system_owner": "System Owner",
        "commissioned_decision": "Select a direction for an approved priority journey.",
        "accountable_specialists": ["Research owner", "Accessibility owner"],
    }
    brief["grilling"] = {
        "base_skill": "grilling",
        "base_skill_version_or_hash": "sha256:example",
        "status": "Completed",
        "required_or_skip_reason": "A consequential new commission required design-intent grilling.",
        "existing_confirmed_owner_design_brief": "",
        "no_material_change_confirmed": False,
        "owner_explicit_autonomous_authorization": True,
        "decision_records": [
            {
                "id": "OWNER-DECISION-001",
                "question": "What transformation should the product enable?",
                "owner_original_response": "Make the priority action feel obvious and trustworthy.",
                "input_class": "Owner preference and product thesis",
                "steward_recommendation": "Make the core act and consequence dominate the first interaction.",
                "agreement_disagreement_evidence_gaps_and_consequences": "Agreement; representative-user evidence remains absent.",
                "resolution": "Use this thesis for autonomous exploration and test it later.",
            }
        ],
    }
    brief["owner_design_intent"] = {
        "commission_and_desired_outcome": "Select a direction for a trustworthy priority journey.",
        "priority_users_roles_and_situations": ["Primary user completing the priority task"],
        "product_thesis": "The product guides one meaningful action to a clear result.",
        "core_user_act": "Complete the priority task and understand its consequence.",
        "first_ten_seconds_hierarchy": "Priority action, expected result, then supporting context.",
        "desired_experiential_qualities": ["Obvious", "Trustworthy", "Calm"],
        "business_priorities_and_constraints": ["Responsive web within the commissioned scope"],
        "non_negotiables": ["Content truth and safe recovery"],
        "accepted_trade_offs": ["Depth may follow clarity at first use"],
        "unacceptable_outcomes": ["Generic dashboard treatment"],
        "rejection_criteria": ["Core act is not clear in ten seconds"],
        "owner_originated_preferences": ["Calm is stakeholder input, not user evidence"],
        "steward_recommendations": ["Explore materially different mental models before rendering"],
        "material_disagreements_and_resolutions": ["None; agreement is not evidence"],
        "evidence_assumptions_and_unresolved_uncertainty": ["No prior user evidence; test after direction selection"],
        "authorization_boundaries": ["Autonomous reversible design through G4 only"],
    }
    brief["shared_understanding"] = {
        "confirmation_question": (
            "Does this brief represent our shared understanding, and may Design Steward "
            "enter autonomous design mode?"
        ),
        "confirmed": True,
        "confirmed_by": "System Owner",
        "confirmed_at": "2030-01-01T00:00:00Z",
        "authorized_scope": "Autonomous direction exploration through G4",
    }
    brief["objectives"] = {
        "desired_outcomes": ["Users can complete the priority journey."],
        "non_goals": ["Production implementation is out of scope."],
    }
    brief["success_contract"] = {
        "product_experience_thesis": "The priority task is obvious and trustworthy.",
        "complete_experience_scope": ["Entry, core action, consequence, and recovery"],
        "product_idea_to_make_obvious": "The product guides one meaningful action to a clear result.",
        "professional_quality_bar": [
            "Product-specific interaction and visual authorship",
            "Strong screenshot-first verdict at desktop and mobile",
        ],
        "artifact_iteration_delegation_budget": [
            "12–15 raw concepts, six territories, three developed directions, and one backbone",
            "One thin-slice revision wave before G4",
        ],
        "first_visible_artifact_target": (
            "Within 15 active minutes after G1/G3 authorize generation or before 15% of the generation budget."
        ),
        "max_preselection_revision_loops_per_direction": 2,
        "feedback_checkpoint_plan": [
            "Show six matched low-fidelity territory sketches before 25% of the budget.",
            "Show revised decisive thin slices after one bounded iteration.",
        ],
        "deferred_assurance_plan": [
            "Defer mobile, recovery, exhaustive accessibility, and browser assurance until promotion."
        ],
        "stopping_point": "Stop at System Owner G4 selection.",
    }
    brief["users_and_contexts"] = {
        "target_users": ["Representative intended users"],
        "contexts": ["Responsive web use"],
        "roles_and_domains": ["Primary user in the responsive web product"],
        "priority_journeys": ["Complete the priority task"],
        "priority_handoffs": ["User action to system result and recovery"],
        "important_exclusions": ["Native mobile"],
    }
    brief["representative_content"] = {
        "canonical_terminology": ["Priority task"],
        "content_samples": ["Representative long-form label"],
        "data_conditions": ["Typical and boundary values"],
        "critical_states": ["Loading, empty, error, success, and partial permission"],
    }
    brief["constraint_ledger"] = [
        {
            "id": "CONSTRAINT-001",
            "statement": "Responsive web is required.",
            "classification": "Fixed",
            "rationale": "Commissioned scope.",
            "source": "Approved brief",
            "decision_owner": "System Owner",
        }
    ]
    brief["comparison_contract"]["rubric"] = ["Task success", "Comprehension"]
    brief["comparison_contract"]["professional_quality_criteria"] = [
        "Product specificity",
        "Interaction and visual authorship",
        "Content voice, ecosystem coverage, responsive composition, and finish",
    ]
    brief["comparison_contract"]["evidence_thresholds"] = ["E3 for usability claims"]
    brief["comparison_contract"]["tie_and_uncertainty_handling"] = "Iterate when evidence is inconclusive."
    brief["governance"] = {
        "human_gates": ["System Owner confirms G1 and approves G4"],
        "decision_owners": ["System Owner"],
        "participant_contact_authority": "System Owner after qualified research approval",
        "consequential_write_authority": "Exact System Owner approval",
    }
    brief["clean_room"]["engagement_workspace"] = "engagement-local-workspace"
    brief["approval"] = {
        "system_owner": "System Owner",
        "approved_at": "2030-01-01T00:00:00Z",
        "approved_scope": "Direction exploration through G4",
    }
    return brief


class ValidateDesignBriefTests(unittest.TestCase):
    def test_ready_brief_passes(self) -> None:
        self.assertEqual(VALIDATOR.validate_brief(ready_brief()), [])

    def test_template_is_not_ready(self) -> None:
        template = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
        errors = VALIDATOR.validate_brief(template)
        self.assertIn("status must be 'Accepted' before direction generation", errors)
        self.assertTrue(any("must be a non-empty" in error for error in errors))

    def test_blocking_unknown_stops_generation(self) -> None:
        brief = ready_brief()
        brief["blocking_unknowns"] = [{"id": "UNKNOWN-001", "question": "Who is affected?"}]
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn("blocking_unknowns must be empty before direction generation", errors)

    def test_blocking_constraint_stops_generation(self) -> None:
        brief = ready_brief()
        brief["constraint_ledger"][0]["classification"] = "Blocking Unknown"
        errors = VALIDATOR.validate_brief(brief)
        self.assertTrue(any("prevents generation" in error for error in errors))

    def test_approval_owner_must_match_authority(self) -> None:
        brief = ready_brief()
        brief["approval"]["system_owner"] = "Different owner"
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn("approval.system_owner must match authority.system_owner", errors)

    def test_unconfirmed_shared_understanding_stops_generation(self) -> None:
        brief = ready_brief()
        brief["shared_understanding"]["confirmed"] = False
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "shared_understanding.confirmed must be true before direction generation",
            errors,
        )

    def test_required_grilling_cannot_enter_autonomous_generation(self) -> None:
        brief = ready_brief()
        brief["operating_mode"] = "Design-intent grilling"
        brief["grilling"]["status"] = "Required"
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "operating_mode must be 'Autonomous design' before direction generation",
            errors,
        )
        self.assertIn(
            "grilling.status must be Completed or Skipped before direction generation",
            errors,
        )

    def test_completed_grilling_preserves_original_owner_input(self) -> None:
        brief = ready_brief()
        del brief["grilling"]["decision_records"][0]["owner_original_response"]
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "grilling.decision_records[0].owner_original_response must be a non-empty string",
            errors,
        )

    def test_skipped_grilling_requires_all_three_conditions(self) -> None:
        brief = ready_brief()
        brief["grilling"] = {
            "base_skill": "grilling",
            "base_skill_version_or_hash": "",
            "status": "Skipped",
            "required_or_skip_reason": "Narrow label correction under an existing brief.",
            "existing_confirmed_owner_design_brief": "",
            "no_material_change_confirmed": False,
            "owner_explicit_autonomous_authorization": False,
            "decision_records": [],
        }
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "grilling.existing_confirmed_owner_design_brief is required when grilling is Skipped",
            errors,
        )
        self.assertIn(
            "grilling.no_material_change_confirmed must be true when grilling is Skipped",
            errors,
        )
        self.assertIn(
            "grilling.owner_explicit_autonomous_authorization must be true when grilling is Skipped",
            errors,
        )

    def test_valid_narrow_change_skip_passes(self) -> None:
        brief = ready_brief()
        brief["grilling"] = {
            "base_skill": "grilling",
            "base_skill_version_or_hash": "",
            "status": "Skipped",
            "required_or_skip_reason": "Narrow copy correction under the existing brief.",
            "existing_confirmed_owner_design_brief": "OWNER-BRIEF-007@1.2.0",
            "no_material_change_confirmed": True,
            "owner_explicit_autonomous_authorization": True,
            "decision_records": [],
        }
        self.assertEqual(VALIDATOR.validate_brief(brief), [])

    def test_missing_quality_contract_stops_generation(self) -> None:
        brief = ready_brief()
        brief["success_contract"]["professional_quality_bar"] = []
        brief["comparison_contract"]["professional_quality_criteria"] = []
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "success_contract.professional_quality_bar must be a non-empty array",
            errors,
        )
        self.assertIn(
            "comparison_contract.professional_quality_criteria must be a non-empty array",
            errors,
        )

    def test_preselection_revision_cap_is_bounded(self) -> None:
        brief = ready_brief()
        brief["success_contract"]["max_preselection_revision_loops_per_direction"] = 4
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "success_contract.max_preselection_revision_loops_per_direction must be an integer from 1 to 3",
            errors,
        )

    def test_feedback_and_deferred_assurance_plans_are_required(self) -> None:
        brief = ready_brief()
        brief["success_contract"]["feedback_checkpoint_plan"] = []
        brief["success_contract"]["deferred_assurance_plan"] = []
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn(
            "success_contract.feedback_checkpoint_plan must be a non-empty array",
            errors,
        )
        self.assertIn(
            "success_contract.deferred_assurance_plan must be a non-empty array",
            errors,
        )

    def test_schema_must_be_current(self) -> None:
        brief = ready_brief()
        brief["schema_version"] = "2.0.0"
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn("schema_version must be '3.0.0'", errors)

    def test_cli_emits_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            brief_path = Path(directory) / "brief.json"
            brief_path.write_text(json.dumps(ready_brief()), encoding="utf-8")
            original_argv = list(VALIDATOR.sys.argv)
            try:
                VALIDATOR.sys.argv = [str(SCRIPT_PATH), str(brief_path), "--json"]
                self.assertEqual(VALIDATOR.main(), 0)
            finally:
                VALIDATOR.sys.argv = original_argv


if __name__ == "__main__":
    unittest.main(verbosity=2)
