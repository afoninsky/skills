from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_protected_paths.py")
SPEC = importlib.util.spec_from_file_location("check_protected_paths", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProtectedPathTests(unittest.TestCase):
    def test_manifest_paths_are_collected_but_urls_are_not(self) -> None:
        manifest = {
            "entries": [
                {"path": "tests/goldens/home.png"},
                {"assertion_source": "tests/home.spec.ts"},
            ],
            "documentation": {"path": "https://example.test/reference"},
        }
        self.assertEqual(
            MODULE.collect_manifest_paths(manifest),
            {"tests/goldens/home.png"},
        )

    def test_exact_files_and_directory_prefixes_are_protected(self) -> None:
        protected_files = {"custom/accepted.png", "design/baselines/manifest.json"}
        prefixes = {"design/baselines/", "design/references/approved/"}
        self.assertTrue(
            MODULE.is_protected("custom/accepted.png", protected_files, prefixes)
        )
        self.assertTrue(
            MODULE.is_protected(
                "design/references/approved/home.png", protected_files, prefixes
            )
        )
        self.assertFalse(MODULE.is_protected("artifacts/candidate.png", protected_files, prefixes))


if __name__ == "__main__":
    unittest.main(verbosity=2)
