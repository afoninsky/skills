#!/usr/bin/env python3
"""Build deterministic A/B pairs for the corrected specialist benchmark."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
BLIND = ROOT / "blind"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def render_brief(case: dict[str, Any]) -> str:
    brief = case["brief"]
    lines = [
        f"# Case {case['id']}: {case['title']}",
        "",
        f"**Charter:** {brief['charter']}",
        "",
        f"**Priority journey:** {brief['priority_journey']}",
        "",
        f"**Representative content:** {brief['representative_content']}",
        "",
        "## Fixed constraints",
        "",
        *[f"- {item}" for item in brief["fixed_constraints"]],
        "",
        "## Open axes",
        "",
        *[f"- {item}" for item in brief["open_axes"]],
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    cases = load_json(ROOT / "fixtures.json")["cases"]
    key: dict[str, dict[str, str | int]] = {}
    index: list[dict[str, str | int]] = []

    for case in cases:
        case_id = int(case["id"])
        pair_id = f"case-{case_id}"
        sources = {
            condition: RUNS / condition / f"case-{case_id}.md"
            for condition in ("candidate", "baseline")
        }
        missing = [str(path.relative_to(ROOT)) for path in sources.values() if not path.is_file()]
        if missing:
            raise SystemExit("Missing raw outputs:\n- " + "\n- ".join(missing))

        labels = ("candidate", "baseline") if case_id % 2 else ("baseline", "candidate")
        pair_directory = BLIND / pair_id
        pair_directory.mkdir(parents=True, exist_ok=True)
        (pair_directory / "brief.md").write_text(render_brief(case), encoding="utf-8")
        for label, condition in zip(("A", "B"), labels, strict=True):
            content = sources[condition].read_text(encoding="utf-8").strip() + "\n"
            (pair_directory / f"{label}.md").write_text(content, encoding="utf-8")

        key[pair_id] = {"case_id": case_id, "A": labels[0], "B": labels[1]}
        index.append(
            {
                "pair_id": pair_id,
                "case_id": case_id,
                "brief_path": f"blind/{pair_id}/brief.md",
                "a_path": f"blind/{pair_id}/A.md",
                "b_path": f"blind/{pair_id}/B.md",
            }
        )

    BLIND.mkdir(parents=True, exist_ok=True)
    (BLIND / "index.json").write_text(
        json.dumps({"pairs": index}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (ROOT / "condition-key.json").write_text(
        json.dumps({"method": "candidate is A for odd cases and B for even cases", "pairs": key}, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(index)} blind pairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
