#!/usr/bin/env python3
"""Build deterministic condition-masked A/B files from benchmark outputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
BLIND = ROOT / "blind"
SEED = "design-steward-2026-08-06-iteration-2"


def main() -> int:
    missing: list[str] = []
    key: dict[str, dict[str, str | int]] = {}
    public_pairs: list[dict[str, str | int]] = []

    for repetition in (1, 2):
        for scenario in range(1, 11):
            pair_id = f"r{repetition}-s{scenario:02d}"
            candidate = RUNS / "candidate" / f"repetition-{repetition}" / f"scenario-{scenario:02d}.md"
            baseline = RUNS / "baseline" / f"repetition-{repetition}" / f"scenario-{scenario:02d}.md"
            for path in (candidate, baseline):
                if not path.is_file():
                    missing.append(str(path.relative_to(ROOT)))
            if missing:
                continue

            digest = hashlib.sha256(f"{SEED}|{repetition}|{scenario}".encode()).digest()
            labels = ("candidate", "baseline") if digest[0] % 2 == 0 else ("baseline", "candidate")
            sources = {"candidate": candidate, "baseline": baseline}
            pair_directory = BLIND / "pairs" / pair_id
            pair_directory.mkdir(parents=True, exist_ok=True)
            for label, condition in zip(("A", "B"), labels, strict=True):
                content = sources[condition].read_text(encoding="utf-8").strip() + "\n"
                (pair_directory / f"{label}.md").write_text(content, encoding="utf-8")

            key[pair_id] = {
                "scenario_id": scenario,
                "repetition": repetition,
                "A": labels[0],
                "B": labels[1],
            }
            public_pairs.append(
                {
                    "pair_id": pair_id,
                    "scenario_id": scenario,
                    "repetition": repetition,
                    "a_path": f"blind/pairs/{pair_id}/A.md",
                    "b_path": f"blind/pairs/{pair_id}/B.md",
                }
            )

    if missing:
        raise SystemExit("Missing raw outputs:\n- " + "\n- ".join(sorted(set(missing))))

    BLIND.mkdir(parents=True, exist_ok=True)
    (BLIND / "index.json").write_text(
        json.dumps({"pairs": public_pairs}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (ROOT / "condition-key.json").write_text(
        json.dumps({"seed": SEED, "pairs": key}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(public_pairs)} blind pairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
