from __future__ import annotations

import json
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
SUITE = (
    "product-design",
    "product-design-discovery",
    "product-design-direction",
    "product-design-contract",
    "product-design-prototype",
    "product-design-implementation",
    "product-design-change",
    "product-design-review",
)
WORKERS = SUITE[1:]
PREFLIGHT_STATUSES = (
    "available",
    "missing-blocking",
    "missing-degradable",
    "unknown",
    "not-applicable",
)


def skill_text(name: str) -> str:
    directory = SKILLS_ROOT / name
    return "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(directory.rglob("*"))
        if path.is_file() and path.suffix in {".md", ".json", ".py", ".yaml", ".yml"}
    )


class ProductDesignSuiteTests(unittest.TestCase):
    def test_complete_suite_has_skill_and_evals(self) -> None:
        for name in SUITE:
            directory = SKILLS_ROOT / name
            self.assertTrue(directory.joinpath("SKILL.md").is_file(), name)
            evals_path = directory / "evals" / "evals.json"
            self.assertTrue(evals_path.is_file(), name)
            evals = json.loads(evals_path.read_text(encoding="utf-8"))
            self.assertEqual(evals["skill_name"], name)
            self.assertGreaterEqual(len(evals["evals"]), 2)
            self.assertLessEqual(len(evals["evals"]), 3)

    def test_router_and_worker_trigger_boundaries_are_explicit(self) -> None:
        router_triggers = json.loads(
            (SKILLS_ROOT / "product-design" / "evals" / "trigger-evals.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(router_triggers), 15)
        self.assertTrue(any(item["should_trigger"] for item in router_triggers))
        self.assertTrue(any(not item["should_trigger"] for item in router_triggers))
        routing_cases = json.loads(
            (SKILLS_ROOT / "product-design" / "evals" / "routing-evals.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(routing_cases["evals"]), 15)

        for worker in WORKERS:
            description = (SKILLS_ROOT / worker / "SKILL.md").read_text(
                encoding="utf-8"
            ).split("---", 2)[1]
            self.assertIn("for every other raw UI/UX request, use product-design", description)
            triggers = json.loads(
                (SKILLS_ROOT / worker / "evals" / "trigger-evals.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                [item["should_trigger"] for item in triggers], [False, True, True], worker
            )

    def test_router_names_every_worker_and_owns_sequencing(self) -> None:
        router = skill_text("product-design")
        for worker in WORKERS:
            self.assertIn(worker, router)
        for required in (
            "single public entrypoint",
            "unchanged original prompt",
            "only this router advances",
            "earliest missing prerequisite",
            "accept-freeze",
        ):
            self.assertIn(required, router)

    def test_deprecated_design_steward_does_not_compete_for_new_work(self) -> None:
        steward_path = REPOSITORY_ROOT / "deprecated" / "design-steward" / "SKILL.md"
        steward = steward_path.read_text(encoding="utf-8")
        readme = REPOSITORY_ROOT.joinpath("README.md").read_text(encoding="utf-8")
        self.assertFalse((SKILLS_ROOT / "design-steward").exists())
        self.assertTrue(steward_path.is_file())
        self.assertIn("Legacy monolithic", steward)
        self.assertIn("Do not auto-route new design commissions here", steward)
        self.assertNotIn("### Design Steward", readme)
        self.assertNotIn("--skill design-steward", readme)

    def test_every_skill_uses_the_same_preflight_vocabulary(self) -> None:
        for name in SUITE:
            text = skill_text(name)
            for status in PREFLIGHT_STATUSES:
                self.assertIn(status, text, f"{name} missing {status}")

    def test_workers_forbid_silent_degradation_and_report_handoffs(self) -> None:
        for name in WORKERS:
            text = skill_text(name).lower()
            self.assertIn("silently", text, name)
            self.assertIn("setup", text, name)
            self.assertIn("confirmation", text, name)
            self.assertIn("handoff", text, name)
            self.assertIn("not evidenced", text, name)

    def test_approved_tool_stack_is_known_to_suite(self) -> None:
        combined = "\n".join(skill_text(name) for name in SUITE)
        for tool in (
            "Git",
            "Penpot",
            "CSS variables",
            "DTCG",
            "Style Dictionary",
            "Storybook",
            "Widgetbook",
            "Playwright",
            "Maestro",
            "axe",
            "Cloudflare Pages",
            "Firebase Test Lab",
            "Firebase App Distribution",
            "Lyssna",
            "Microsoft Clarity",
        ):
            self.assertIn(tool, combined, tool)

    def test_strict_baseline_authority_is_consistent(self) -> None:
        router = skill_text("product-design")
        contract = skill_text("product-design-contract")
        self.assertIn("Only `product-design-contract`", router)
        self.assertIn("accept-freeze", contract)
        for name in ("product-design-implementation", "product-design-change"):
            text = skill_text(name).lower()
            self.assertIn("baseline", text)
            self.assertTrue(
                "never update" in text or "must not update" in text or "do not update" in text,
                name,
            )

    def test_published_skills_are_generic_and_progressively_disclosed(self) -> None:
        for name in SUITE:
            skill = (SKILLS_ROOT / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertLess(len(skill.splitlines()), 500, name)
            self.assertNotIn("TeachRelay", skill)
            self.assertNotIn("/Users/", skill)

    def test_route_and_toolchain_validators_cover_strict_failures(self) -> None:
        route = (SKILLS_ROOT / "product-design" / "scripts" / "validate_route.py").read_text(encoding="utf-8")
        toolchain = (SKILLS_ROOT / "product-design" / "scripts" / "validate_toolchain.py").read_text(encoding="utf-8")
        self.assertIn("baseline changed outside explicit accept-freeze authority", route)
        self.assertIn("does not permit execution", toolchain)
        self.assertIn("degraded execution requires explicit confirmation_id", toolchain)
        self.assertIn("original_prompt_sha256", route)
        self.assertIn("invalid recommended transition", route)
        self.assertIn("implementation_entry_approval_id", route)

    def test_freeze_and_change_guards_require_human_approval_identity(self) -> None:
        contract_validator = (
            SKILLS_ROOT
            / "product-design-contract"
            / "scripts"
            / "validate_design_contract.py"
        ).read_text(encoding="utf-8")
        change_guard = (
            SKILLS_ROOT / "product-design-change" / "scripts" / "change_guard.py"
        ).read_text(encoding="utf-8")
        self.assertIn("--approval-id", contract_validator)
        self.assertIn("approval_id", change_guard)
        self.assertIn("capture-only is not protected", change_guard)


if __name__ == "__main__":
    unittest.main(verbosity=2)
