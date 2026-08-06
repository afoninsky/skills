#!/usr/bin/env python3
"""Conservatively aggregate two blind structural graders per benchmark pair."""

from __future__ import annotations

import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT.parents[2] / "skills" / "design-steward" / "evals" / "benchmark.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    fixture_data = load_json(FIXTURES)
    expectations = {item["id"]: item["expectations"] for item in fixture_data["evals"]}
    key = load_json(ROOT / "condition-key.json")["pairs"]
    grade_paths = sorted((ROOT / "grades").glob("grader-*.json"))
    if len(grade_paths) != 4:
        raise SystemExit(f"Expected 4 grader files, found {len(grade_paths)}")

    by_pair: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in grade_paths:
        data = load_json(path)
        for pair in data.get("pairs", []):
            by_pair[pair["pair_id"]].append(pair)

    pair_results: list[dict[str, Any]] = []
    condition_totals = {
        "candidate": {"passed": 0, "possible": 0, "tier1": 0, "words": [], "preferred": 0},
        "baseline": {"passed": 0, "possible": 0, "tier1": 0, "words": [], "preferred": 0},
    }
    coverage_by_repetition = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    subset_totals = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    grader_disagreements = 0
    non_tie_preferences = 0

    for pair_id, mapping in sorted(key.items()):
        grades = by_pair.get(pair_id, [])
        if len(grades) != 2:
            raise SystemExit(f"Expected 2 grades for {pair_id}, found {len(grades)}")
        scenario = int(mapping["scenario_id"])
        expected_count = len(expectations[scenario])
        result: dict[str, Any] = {
            "pair_id": pair_id,
            "scenario_id": scenario,
            "repetition": mapping["repetition"],
            "conditions": {},
        }

        for label in ("A", "B"):
            condition = mapping[label]
            vectors = [grade["outputs"][label]["expectations"] for grade in grades]
            if any(len(vector) != expected_count for vector in vectors):
                raise SystemExit(f"Expectation length mismatch for {pair_id} {label}")
            conservative = [all(values) for values in zip(*vectors, strict=True)]
            disagreements = sum(a != b for a, b in zip(vectors[0], vectors[1], strict=True))
            grader_disagreements += disagreements
            tier1 = any(grade["outputs"][label]["tier1_failure"] for grade in grades)
            words = [int(grade["outputs"][label]["word_count"]) for grade in grades]
            word_count = max(words)

            passed = sum(conservative)
            condition_totals[condition]["passed"] += passed
            condition_totals[condition]["possible"] += expected_count
            condition_totals[condition]["tier1"] += int(tier1)
            condition_totals[condition]["words"].append(word_count)
            coverage_by_repetition[condition][int(mapping["repetition"])][0] += passed
            coverage_by_repetition[condition][int(mapping["repetition"])][1] += expected_count

            for subset, scenarios in {
                "human_gate": {1, 5, 9, 10},
                "traceability": {1, 2, 4, 6, 9, 10},
                "direction_integrity": {7},
            }.items():
                if scenario in scenarios:
                    subset_totals[condition][subset][0] += passed
                    subset_totals[condition][subset][1] += expected_count

            result["conditions"][condition] = {
                "label": label,
                "expectations_passed": passed,
                "expectations_possible": expected_count,
                "tier1_failure_flagged": tier1,
                "word_count": word_count,
                "grader_expectation_disagreements": disagreements,
            }

        preferences = [grade["structural_preference"] for grade in grades]
        if preferences[0] == preferences[1] and preferences[0] in {"A", "B"}:
            preferred_condition = mapping[preferences[0]]
            condition_totals[preferred_condition]["preferred"] += 1
            non_tie_preferences += 1
            result["structural_preference"] = preferred_condition
        else:
            result["structural_preference"] = "tie_or_disagreement"
        pair_results.append(result)

    def ratio(passed: int, possible: int) -> float:
        return passed / possible if possible else 0.0

    summary: dict[str, Any] = {}
    for condition, totals in condition_totals.items():
        summary[condition] = {
            "expectation_coverage": ratio(totals["passed"], totals["possible"]),
            "tier1_flags_before_adjudication": totals["tier1"],
            "median_word_count": statistics.median(totals["words"]),
            "structural_preferences": totals["preferred"],
            "per_repetition_coverage": {
                str(repetition): ratio(*values)
                for repetition, values in sorted(coverage_by_repetition[condition].items())
            },
            "subsets": {
                name: ratio(*values) for name, values in subset_totals[condition].items()
            },
        }

    summary["candidate"]["improvement_over_baseline"] = (
        summary["candidate"]["expectation_coverage"] - summary["baseline"]["expectation_coverage"]
    )
    summary["candidate"]["median_word_ratio_to_baseline"] = (
        summary["candidate"]["median_word_count"] / summary["baseline"]["median_word_count"]
        if summary["baseline"]["median_word_count"]
        else None
    )
    summary["candidate"]["preference_rate_among_non_ties"] = (
        summary["candidate"]["structural_preferences"] / non_tie_preferences
        if non_tie_preferences
        else 0.0
    )

    output = {
        "schema_version": "1.0.0",
        "status": "model-graded-structural-results-before-tier1-adjudication",
        "grader_files": [str(path.relative_to(ROOT)) for path in grade_paths],
        "grader_expectation_disagreements": grader_disagreements,
        "non_tie_preferences": non_tie_preferences,
        "summary": summary,
        "pairs": pair_results,
        "limitations": [
            "Model graders provide structural assistance only.",
            "Tier 1 flags require adjudication against raw outputs.",
            "Qualified multidisciplinary human review is not present.",
            "No representative-user or production evidence was collected or required for these product-neutral advice scenarios.",
        ],
    }
    (ROOT / "aggregate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Aggregated {len(pair_results)} pairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

