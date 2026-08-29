#!/usr/bin/env python3
"""Find likely asserted-golden and capture-only producers without changing files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TEXT_SUFFIXES = {
    ".dart",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".kts",
    ".mjs",
    ".swift",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}
ASSERTION_PATTERNS = {
    "playwright-to-have-screenshot": re.compile(r"\btoHaveScreenshot\s*\("),
    "maestro-assert-screenshot": re.compile(r"\bassertScreenshot\s*:"),
    "flutter-golden": re.compile(r"\bmatchesGoldenFile\s*\("),
    "native-snapshot-assertion": re.compile(
        r"\b(?:assertSnapshot|assertViewSnapshot|verifySnapshot|verifyScreenshot|compareSnapshot)\s*\("
    ),
}
CAPTURE_PATTERNS = {
    "playwright-page-screenshot": re.compile(r"\b(?:page|locator)\.screenshot\s*\("),
    "maestro-take-screenshot": re.compile(r"\btakeScreenshot\s*:"),
    "apple-screen-capture": re.compile(r"\bXCUIScreen\.main\.screenshot\s*\("),
    "android-compose-capture": re.compile(r"\bcaptureToImage\s*\("),
    "generic-test-screenshot": re.compile(r"\b(?:takeSnapshot|captureScreenshot)\s*\("),
}


def iter_files(inputs: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for item in inputs:
        if item.is_file() and item.suffix.lower() in TEXT_SUFFIXES:
            files.add(item)
        elif item.is_dir():
            files.update(
                path for path in item.rglob("*") if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
            )
    return sorted(files)


def scan(path: Path) -> list[dict[str, object]]:
    if path.stat().st_size > 2 * 1024 * 1024:
        return []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return []
    occurrences: list[dict[str, object]] = []
    for number, line in enumerate(lines, start=1):
        for name, pattern in ASSERTION_PATTERNS.items():
            if pattern.search(line):
                occurrences.append(
                    {
                        "line": number,
                        "pattern": name,
                        "classification_hint": "asserted-golden-producer",
                    }
                )
        for name, pattern in CAPTURE_PATTERNS.items():
            if pattern.search(line):
                occurrences.append(
                    {
                        "line": number,
                        "pattern": name,
                        "classification_hint": "capture-only-producer",
                    }
                )
    return occurrences


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Test/flow files or directories to scan")
    args = parser.parse_args()

    missing = [str(path) for path in args.paths if not path.exists()]
    if missing:
        print(json.dumps({"error": "input path not found", "paths": missing}, indent=2), file=sys.stderr)
        return 2

    results = []
    for path in iter_files(args.paths):
        occurrences = scan(path)
        if occurrences:
            results.append({"file": str(path), "occurrences": occurrences})

    payload = {
        "files_with_visual_producers": results,
        "notice": (
            "Hints only. Inspect active execution, deterministic state, comparison tolerance, accepted baseline "
            "identity, and failure artifacts before classifying evidence."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

