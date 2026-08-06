from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DESIGN_STEWARD = REPOSITORY_ROOT / "skills" / "design-steward"
PROVENANCE_PATH = DESIGN_STEWARD / "references" / "specialist-provenance.json"
VERIFY_SPECIALISTS = DESIGN_STEWARD / "scripts" / "verify_specialists.py"


class DesignStewardSpecialistTests(unittest.TestCase):
    def setUp(self) -> None:
        self.provenance = json.loads(PROVENANCE_PATH.read_text(encoding="utf-8"))
        self.lock = json.loads(REPOSITORY_ROOT.joinpath("skills-lock.json").read_text(encoding="utf-8"))

    def test_optional_specialists_are_locked_to_expected_sources(self) -> None:
        expected = {
            "frontend-design": ("anthropics/skills", "skills/frontend-design/SKILL.md"),
            "web-design-guidelines": (
                "vercel-labs/agent-skills",
                "skills/web-design-guidelines/SKILL.md",
            ),
        }

        self.assertEqual(set(self.lock["skills"]), set(expected))
        for name, (source, skill_path) in expected.items():
            entry = self.lock["skills"][name]
            self.assertEqual(entry["source"], source)
            self.assertEqual(entry["skillPath"], skill_path)
            self.assertNotIn("/Users/", json.dumps(entry))
            self.assertNotIn("/home/", json.dumps(entry))

    def test_installed_specialists_match_recorded_hashes(self) -> None:
        for name, record in self.provenance["skills"].items():
            skill_path = REPOSITORY_ROOT / ".agents" / "skills" / name / "SKILL.md"
            digest = hashlib.sha256(skill_path.read_bytes()).hexdigest()
            self.assertEqual(digest, record["installed_sha256"])

        frontend = self.provenance["skills"]["frontend-design"]
        license_path = REPOSITORY_ROOT / frontend["license_path"]
        license_digest = hashlib.sha256(license_path.read_bytes()).hexdigest()
        self.assertEqual(license_digest, frontend["license_sha256"])

    def test_specialist_contract_is_integrated_into_steward(self) -> None:
        skill = DESIGN_STEWARD.joinpath("SKILL.md").read_text(encoding="utf-8")
        contract = DESIGN_STEWARD.joinpath(
            "references", "specialist-capabilities.md"
        ).read_text(encoding="utf-8")

        for required in (
            "frontend-design",
            "web-design-guidelines",
            "fresh isolated sub-agent",
            "Not yet evidenced",
            "E1 specialist/heuristic input",
            "not representative-user validation",
        ):
            self.assertIn(required, skill + contract)

    def test_license_evidence_is_stable_and_documented(self) -> None:
        notice = REPOSITORY_ROOT.joinpath("THIRD_PARTY_SKILLS.md").read_text(encoding="utf-8")
        for record in self.provenance["skills"].values():
            self.assertRegex(record["license_evidence"], r"github\.com/.+/blob/[0-9a-f]{40}/")
            self.assertIn(record["license"], notice)

    def test_installed_specialist_verifier_passes_repository_copy(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VERIFY_SPECIALISTS), str(REPOSITORY_ROOT)],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["ok"])

    def test_installed_specialist_verifier_fails_missing_copy(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(VERIFY_SPECIALISTS), directory],
                capture_output=True,
                check=False,
                text=True,
            )

        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)["ok"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
