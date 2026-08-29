from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("classify_visual_evidence.py")
SPEC = importlib.util.spec_from_file_location("classify_visual_evidence", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VisualEvidenceClassifierTests(unittest.TestCase):
    def test_playwright_assertion_and_capture_are_distinguished(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "visual.spec.ts"
            path.write_text(
                "await expect(page).toHaveScreenshot();\nawait page.screenshot();\n",
                encoding="utf-8",
            )
            hints = {item["classification_hint"] for item in MODULE.scan(path)}
        self.assertEqual(
            hints,
            {"asserted-golden-producer", "capture-only-producer"},
        )

    def test_maestro_assertion_and_capture_are_distinguished(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "flow.yaml"
            path.write_text(
                "- assertScreenshot: accepted-home\n- takeScreenshot: candidate-home\n",
                encoding="utf-8",
            )
            patterns = {item["pattern"] for item in MODULE.scan(path)}
        self.assertEqual(
            patterns,
            {"maestro-assert-screenshot", "maestro-take-screenshot"},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
