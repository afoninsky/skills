from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VERIFY_SCRIPT = REPOSITORY_ROOT / "scripts" / "verify_skills.py"


class VerifySkillsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.repository = Path(self.temporary_directory.name)
        self.skills_directory = self.repository / "skills"
        self.skills_directory.mkdir()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def create_skill(self, name: str = "example-skill", body: str = "Use the bundled reference.") -> Path:
        skill_directory = self.skills_directory / name
        skill_directory.mkdir()
        skill_directory.joinpath("SKILL.md").write_text(
            "---\n"
            f"name: {name}\n"
            "description: Validate a public example skill when a user requests it.\n"
            "---\n\n"
            f"# Example Skill\n\n{body}\n",
            encoding="utf-8",
        )
        return skill_directory

    def run_verifier(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VERIFY_SCRIPT), "--repository", str(self.repository)],
            capture_output=True,
            check=False,
            text=True,
        )

    def test_valid_skill_repository_passes(self) -> None:
        self.create_skill()

        result = self.run_verifier()

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Verified 1 skill", result.stdout)

    def test_directory_and_frontmatter_names_must_match(self) -> None:
        skill_directory = self.create_skill()
        skill_file = skill_directory / "SKILL.md"
        skill_file.write_text(skill_file.read_text().replace("name: example-skill", "name: wrong-name"))

        result = self.run_verifier()

        self.assertEqual(result.returncode, 1)
        self.assertIn("must match its directory", result.stderr)

    def test_private_absolute_path_is_rejected(self) -> None:
        self.create_skill(body="Read /Users/example/private-notes.md before continuing.")

        result = self.run_verifier()

        self.assertEqual(result.returncode, 1)
        self.assertIn("private absolute path", result.stderr)

    def test_broken_relative_markdown_link_is_rejected(self) -> None:
        self.create_skill(body="Read [the reference](references/missing.md).")

        result = self.run_verifier()

        self.assertEqual(result.returncode, 1)
        self.assertIn("broken relative Markdown link", result.stderr)

    def test_evaluation_files_must_reference_existing_fixtures(self) -> None:
        skill_directory = self.create_skill()
        evaluations_directory = skill_directory / "evals"
        evaluations_directory.mkdir()
        evaluations_directory.joinpath("evals.json").write_text(
            '{"skill_name":"example-skill","evals":[{"id":1,"prompt":"Run it",'
            '"expected_output":"A result","files":["evals/files/missing.svg"]}]}',
            encoding="utf-8",
        )

        result = self.run_verifier()

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing evaluation fixture", result.stderr)

    def test_symlink_is_rejected(self) -> None:
        skill_directory = self.create_skill()
        external_file = self.repository / "private.txt"
        external_file.write_text("private")
        skill_directory.joinpath("linked.txt").symlink_to(external_file)

        result = self.run_verifier()

        self.assertEqual(result.returncode, 1)
        self.assertIn("symlink", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
