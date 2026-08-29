from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("generate_engagement_roadmap.py")
STARTER_PATH = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "engagement-starter"
    / "steward-state.json"
)

SPEC = importlib.util.spec_from_file_location("generate_engagement_roadmap", SCRIPT_PATH)
assert SPEC and SPEC.loader
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


def populated_state() -> dict:
    state = json.loads(STARTER_PATH.read_text(encoding="utf-8"))
    state["engagement"].update(
        {
            "id": "ENG-001",
            "title": "Calm learner workspace",
            "workspace": "/tmp/design-engagement",
            "system_owner": "Mara Chen, VP Product",
            "last_updated_at": "2030-01-01T12:00:00Z",
        }
    )
    state["dependency_preflight"].update(
        {
            "resolved_skill": "grilling",
            "version_or_content_hash": "sha256:abc",
            "verified_at": "2030-01-01T09:00:00Z",
            "status": "Available",
        }
    )
    state["resume"].update(
        {
            "current_mode": "Autonomous design",
            "current_gate": "G4 Direction",
            "current_stage": "Direction selection",
            "latest_summary": "Three developed directions were compared.",
            "exact_next_action": "System Owner selects one direction.",
            "stopping_point": "Owner selection",
        }
    )
    state["authority"].update(
        {
            "owner_design_brief_id_and_version": "BRIEF-001 v1",
            "authorization_boundary": "Reversible design through G4",
        }
    )
    state["decisions"] = [
        {
            "id": "DEC-001",
            "decided_at": "2030-01-01T10:00:00Z",
            "question": "What should dominate the workspace?",
            "owner_original_input": "The current task.",
            "steward_recommendation": "Keep the current task visually dominant.",
            "resolution": "Accepted",
            "status": "Accepted",
            "decision_owner": "Mara Chen",
            "evidence_ids": ["E-001"],
            "supersedes": "",
            "superseded_by": "",
            "links": [],
        }
    ]
    state["research_and_materials"] = [
        {
            "id": "E-001",
            "title": "Primary task clarity guidance",
            "url_or_path": "https://example.com/guidance",
            "evidence_level": "E1",
            "material_used": "One prominent current action",
            "design_implication": "Reduce competing workspace chrome.",
            "limitations": "Guidance, not product validation.",
        }
    ]
    state["funnel"]["raw_concepts"] = [
        {"id": "RAW-001", "title": "Task stage", "thesis": "One task at a time", "status": "Promoted"}
    ]
    state["funnel"]["territories"] = [
        {"id": "TER-001", "title": "Calm stage", "promise": "Immediate focus", "status": "Promoted"}
    ]
    state["funnel"]["developed_directions"] = [
        {"id": "DIR-001", "title": "Guided workspace", "summary": "Task-first shell", "status": "Strong"}
    ]
    state["funnel"]["selected_backbone"].update(
        {
            "direction_id": "DIR-001",
            "title": "Guided workspace",
            "status": "Selected",
            "summary": "A task-first workspace with bounded support.",
        }
    )
    state["artifacts"] = [
        {
            "id": "ART-001",
            "title": "Guided workspace mock",
            "kind": "Interactive HTML",
            "path_or_url": "./artifacts/guided/index.html",
            "status": "Frozen",
            "direction_id": "DIR-001",
            "states": ["Entry", "Core task", "Recovery"],
            "viewports": ["1440×900", "390×844"],
            "limitations": "Fictional data",
        }
    ]
    state["coverage"] = [
        {
            "id": "COV-001",
            "journey_or_state": "First entry",
            "role_domain_or_destination": "Primary user / Home",
            "status": "Represented",
            "artifact_id": "ART-001",
        }
    ]
    state["implementation"].update(
        {
            "engineering_source_acceptance": "Pass",
            "design_integration_acceptance": "Not yet evidenced",
            "preview_or_deployed_fidelity": "Not started",
            "fidelity_pairs": [
                {
                    "id": "FID-001",
                    "state": "First entry",
                    "reference_capture": "./reference.png",
                    "implementation_capture": "./implementation.png",
                    "composition_constraints": "Task surface remains dominant",
                    "status": "Review",
                }
            ],
        }
    )
    state["checks"]["completed"] = ["Desktop mock rendered"]
    state["checks"]["deferred"] = ["Representative-user comprehension"]
    for index, gate in enumerate(state["roadmap"]):
        gate["status"] = "complete" if index < 5 else "pending"
        gate["decision_or_result"] = f"Gate {gate['gate']} produced a recorded decision."
        gate["evidence_ids"] = ["E-001"] if index < 5 else []
        gate["artifact_ids"] = ["ART-001"] if index == 4 else []
        gate["open_items"] = [] if index < 5 else ["Complete the gate review"]
    state["roadmap"][5]["status"] = "in_progress"
    return state


class GenerateEngagementRoadmapTests(unittest.TestCase):
    def test_starter_state_is_structurally_valid(self) -> None:
        state = json.loads(STARTER_PATH.read_text(encoding="utf-8"))
        self.assertEqual(GENERATOR.validate_state(state), [])

    def test_render_includes_owner_journey_and_separate_acceptance_levels(self) -> None:
        rendered = GENERATOR.render_page(populated_state(), Path("steward-state.json"))

        for expected in (
            "Calm learner workspace",
            "Mara Chen, VP Product",
            "Gates at a glance",
            'class="gate-timeline"',
            'class="gate-code">G0',
            'class="gate-code">G4',
            'class="gate-code">G6',
            "Completed",
            "In progress",
            "Not done",
            "Evidence",
            "Outputs",
            "Material decisions",
            "Primary task clarity guidance",
            "Guided workspace mock",
            "Engineering source acceptance",
            "Design-integration acceptance",
            "Preview/deployed fidelity",
            "System Owner selects one direction.",
        ):
            self.assertIn(expected, rendered)

        self.assertNotIn("fonts.googleapis.com", rendered)
        self.assertNotIn("<script src=", rendered)

    def test_gate_state_uses_four_plain_language_states(self) -> None:
        self.assertEqual(GENERATOR.gate_state("complete"), ("positive", "Completed", "✓"))
        self.assertEqual(GENERATOR.gate_state("in_progress"), ("active", "In progress", "→"))
        self.assertEqual(GENERATOR.gate_state("blocked"), ("negative", "Blocked", "!"))
        self.assertEqual(GENERATOR.gate_state("pending"), ("pending", "Not done", "○"))

    def test_unsafe_artifact_link_is_rendered_as_plain_text(self) -> None:
        state = populated_state()
        state["artifacts"][0]["path_or_url"] = "javascript:alert(1)"

        rendered = GENERATOR.render_page(state, Path("steward-state.json"))

        self.assertNotIn('href="javascript:', rendered)
        self.assertIn("Guided workspace mock", rendered)

    def test_cli_writes_self_contained_html(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state_path = root / "steward-state.json"
            output_path = root / "owner-roadmap.html"
            state_path.write_text(json.dumps(populated_state()), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    str(state_path),
                    "--output",
                    str(output_path),
                ],
                capture_output=True,
                check=False,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(output_path.exists())
            self.assertIn("The route to this design", output_path.read_text(encoding="utf-8"))
            self.assertTrue(json.loads(result.stdout)["ok"])

    def test_invalid_schema_fails_without_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state_path = root / "steward-state.json"
            output_path = root / "owner-roadmap.html"
            state = populated_state()
            state["schema_version"] = "0.0.0"
            state_path.write_text(json.dumps(state), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    str(state_path),
                    "--output",
                    str(output_path),
                ],
                capture_output=True,
                check=False,
                text=True,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("schema_version must be '1.0.0'", result.stderr)
            self.assertFalse(output_path.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
