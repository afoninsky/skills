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
MUTATING_WORKERS = (
    "product-design-contract",
    "product-design-implementation",
    "product-design-change",
)


def entrypoint(name: str) -> str:
    return (SKILLS_ROOT / name / "SKILL.md").read_text(encoding="utf-8")


def package_text(name: str) -> str:
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
            self.assertLessEqual(len(evals["evals"]), 6)

    def test_router_and_worker_trigger_boundaries_are_explicit(self) -> None:
        router_triggers = json.loads(
            (SKILLS_ROOT / "product-design" / "evals" / "trigger-evals.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(router_triggers), 15)
        self.assertTrue(any(item["should_trigger"] for item in router_triggers))
        self.assertTrue(any(not item["should_trigger"] for item in router_triggers))

        for worker in WORKERS:
            frontmatter = entrypoint(worker).split("---", 2)[1]
            self.assertIn("otherwise use product-design", frontmatter, worker)
            triggers = json.loads(
                (SKILLS_ROOT / worker / "evals" / "trigger-evals.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                [item["should_trigger"] for item in triggers], [False, True, True], worker
            )

    def test_router_centralizes_requested_design_principles(self) -> None:
        router = entrypoint("product-design").lower()
        for worker in WORKERS:
            self.assertIn(worker, router)
        for principle in (
            "closed-world change",
            "exploration scope",
            "mutation scope",
            "understand why",
            "primary research",
            "authoritative domain",
            "not literal or exhaustive",
            "mature maintained",
            "real medium",
            "definition of done",
        ):
            self.assertIn(principle, router)

    def test_entrypoints_are_concise_and_progressively_disclosed(self) -> None:
        self.assertLessEqual(len(entrypoint("product-design").splitlines()), 120)
        for name in WORKERS:
            skill = entrypoint(name)
            self.assertLessEqual(len(skill.splitlines()), 90, name)
            self.assertNotIn("Read completely", skill, name)
            self.assertNotIn("at the start of every invocation", skill, name)
            self.assertNotIn("no older than four hours", skill, name)
            self.assertNotIn("/Users/", skill, name)

    def test_mutating_workers_require_idempotence_and_preservation(self) -> None:
        for name in MUTATING_WORKERS:
            text = entrypoint(name).lower()
            self.assertTrue(
                "idempotent" in text or "second run" in text,
                f"{name} lacks an idempotence rule",
            )
            self.assertIn("existing", text, name)
            self.assertIn("preserv", text, name)
            self.assertIn("baseline", text, name)

        change = entrypoint("product-design-change").lower()
        self.assertIn("already satisfied", change)
        self.assertIn("smallest patch", change)
        self.assertIn("shared dependency", change)

    def test_exploration_is_creative_but_separate_from_implementation(self) -> None:
        direction = entrypoint("product-design-direction").lower()
        prototype = entrypoint("product-design-prototype").lower()
        implementation = entrypoint("product-design-implementation").lower()
        self.assertIn("structurally and visually distinct", direction)
        self.assertIn("delegates design judgment", direction)
        self.assertIn("exploration mode", prototype)
        self.assertIn("isolated", prototype)
        self.assertIn("material structural and visual choices", implementation)
        self.assertIn("small reversible details", implementation)

    def test_research_rules_prioritize_credible_evidence(self) -> None:
        for name in (
            "product-design",
            "product-design-discovery",
            "product-design-direction",
            "product-design-review",
        ):
            text = entrypoint(name).lower()
            self.assertIn("primary", text, name)
            self.assertIn("authoritative", text, name)
        self.assertIn(
            "not user research", entrypoint("product-design").lower()
        )
        self.assertIn(
            "never count as user validation",
            entrypoint("product-design-discovery").lower(),
        )

    def test_review_and_acceptance_boundaries_remain_strict(self) -> None:
        review = entrypoint("product-design-review").lower()
        router = entrypoint("product-design")
        contract = entrypoint("product-design-contract").lower()
        default_prompt = SKILLS_ROOT.joinpath(
            "product-design", "agents", "openai.yaml"
        ).read_text(encoding="utf-8").lower()
        self.assertIn("read-only", review)
        self.assertIn("complete the review first", review)
        self.assertIn("Only `product-design-contract`", router)
        self.assertIn("accept-freeze", contract)
        self.assertIn("observed diffs as the new accepted baseline", default_prompt)
        self.assertIn("repository-native integrity checks", contract)
        self.assertIn("formal schemas", contract)
        for name in ("product-design-implementation", "product-design-change"):
            self.assertIn("never update", entrypoint(name).lower(), name)

    def test_optional_legacy_protocol_does_not_become_the_default(self) -> None:
        routing = SKILLS_ROOT.joinpath(
            "product-design", "references", "routing-and-handoffs.md"
        ).read_text(encoding="utf-8").lower()
        direction = entrypoint("product-design-direction").lower()
        prototype_evals = SKILLS_ROOT.joinpath(
            "product-design-prototype", "evals", "evals.json"
        ).read_text(encoding="utf-8").lower()
        self.assertIn("do not copy those defaults", routing)
        self.assertIn("legacy a–f envelope schema", routing)
        self.assertIn("stable candidate identities", direction)
        self.assertIn("report a no-op", direction)
        self.assertIn("all prototype writes outside production source", prototype_evals)

    def test_tools_are_capability_driven_and_existing_first(self) -> None:
        router = entrypoint("product-design").lower()
        implementation = entrypoint("product-design-implementation").lower()
        contract = entrypoint("product-design-contract").lower()
        self.assertIn("established project equivalent is preferred", router)
        self.assertIn("historical defaults", router)
        self.assertIn("repository's mature libraries", implementation)
        self.assertIn("complexity only when earned", contract)

    def test_deprecated_design_steward_does_not_compete_for_new_work(self) -> None:
        steward_path = REPOSITORY_ROOT / "deprecated" / "design-steward" / "SKILL.md"
        steward = steward_path.read_text(encoding="utf-8")
        readme = REPOSITORY_ROOT.joinpath("README.md").read_text(encoding="utf-8")
        self.assertFalse((SKILLS_ROOT / "design-steward").exists())
        self.assertTrue(steward_path.is_file())
        self.assertIn("Legacy monolithic", steward)
        self.assertIn("Do not auto-route new design commissions here", steward)
        self.assertNotIn("### Design Steward", readme)

    def test_optional_protection_tools_keep_strict_invariants(self) -> None:
        route = package_text("product-design")
        contract = package_text("product-design-contract")
        change = package_text("product-design-change")
        self.assertIn("baseline changed outside explicit accept-freeze authority", route)
        self.assertIn("--approval-id", contract)
        self.assertIn("capture-only is not protected", change)


if __name__ == "__main__":
    unittest.main(verbosity=2)
