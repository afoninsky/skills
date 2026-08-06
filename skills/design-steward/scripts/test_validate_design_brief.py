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
            "status": "Approved",
            "mode": "From-scratch",
            "evidence_gap_rationale": "No prior evidence exists; research questions are recorded at G2.",
        }
    )
    brief["authority"] = {
        "product_owner": "Product Owner",
        "commissioned_decision": "Select a direction for an approved priority journey.",
        "accountable_specialists": ["Research owner", "Accessibility owner"],
    }
    brief["objectives"] = {
        "desired_outcomes": ["Users can complete the priority journey."],
        "non_goals": ["Production implementation is out of scope."],
    }
    brief["users_and_contexts"] = {
        "target_users": ["Representative intended users"],
        "contexts": ["Responsive web use"],
        "priority_journeys": ["Complete the priority task"],
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
            "decision_owner": "Product Owner",
        }
    ]
    brief["comparison_contract"]["rubric"] = ["Task success", "Comprehension"]
    brief["comparison_contract"]["evidence_thresholds"] = ["E3 for usability claims"]
    brief["comparison_contract"]["tie_and_uncertainty_handling"] = "Iterate when evidence is inconclusive."
    brief["governance"] = {
        "human_gates": ["Product Owner approves G1 and G4"],
        "decision_owners": ["Product Owner"],
        "participant_contact_authority": "Product Owner after qualified research approval",
        "consequential_write_authority": "Exact Product Owner approval",
    }
    brief["clean_room"]["engagement_workspace"] = "engagement-local-workspace"
    brief["approval"] = {
        "product_owner": "Product Owner",
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
        self.assertIn("status must be 'Approved' before direction generation", errors)
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
        brief["approval"]["product_owner"] = "Different owner"
        errors = VALIDATOR.validate_brief(brief)
        self.assertIn("approval.product_owner must match authority.product_owner", errors)

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
