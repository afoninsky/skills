#!/usr/bin/env python3
"""Verify optional Design Steward specialists against recorded content hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PROVENANCE = Path(__file__).resolve().parents[1] / "references" / "specialist-provenance.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(project_root: Path) -> dict[str, object]:
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    ok = True

    for name, record in provenance["skills"].items():
        skill_path = project_root / ".agents" / "skills" / name / "SKILL.md"
        expected = record["installed_sha256"]
        actual = sha256(skill_path) if skill_path.is_file() else None
        skill_ok = actual == expected
        errors = [] if skill_ok else ["missing skill" if actual is None else "skill hash mismatch"]

        license_path_value = record.get("license_path")
        if license_path_value:
            license_path = project_root / license_path_value
            license_actual = sha256(license_path) if license_path.is_file() else None
            if license_actual != record.get("license_sha256"):
                skill_ok = False
                errors.append(
                    "missing license" if license_actual is None else "license hash mismatch"
                )

        ok = ok and skill_ok
        results.append(
            {
                "name": name,
                "ok": skill_ok,
                "actual_sha256": actual,
                "expected_sha256": expected,
                "errors": errors,
            }
        )

    return {"ok": ok, "project_root": str(project_root), "skills": results}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify repository-local Design Steward specialist skills."
    )
    parser.add_argument("project_root", type=Path, nargs="?", default=Path.cwd())
    args = parser.parse_args()
    result = verify(args.project_root.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
