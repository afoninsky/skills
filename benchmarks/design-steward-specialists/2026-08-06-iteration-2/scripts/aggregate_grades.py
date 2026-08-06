#!/usr/bin/env python3
"""Aggregate the two blind grades for the corrected specialist benchmark."""

from __future__ import annotations

import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
METRICS = ("brief_fidelity", "traceability", "coherence", "distinctiveness", "coverage")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    key = load_json(ROOT / "condition-key.json")["pairs"]
    grade_paths = sorted((ROOT / "grades").glob("grader-*.json"))
    if len(grade_paths) != 2:
        raise SystemExit(f"Expected 2 grader files, found {len(grade_paths)}")

    scores: dict[str, dict[str, list[int]]] = {
        condition: defaultdict(list) for condition in ("candidate", "baseline")
    }
    tier1_cases: dict[str, set[int]] = {"candidate": set(), "baseline": set()}
    preferences = defaultdict(int)
    non_ties = 0
    pair_results: list[dict[str, Any]] = []

    grades_by_case: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for path in grade_paths:
        data = load_json(path)
        for case in data.get("cases", []):
            case_value = str(case["case"])
            case_id = int(case_value.removeprefix("case-"))
            grades_by_case[case_id].append(case)

    for pair_id, mapping in sorted(key.items()):
        case_id = int(mapping["case_id"])
        case_grades = grades_by_case[case_id]
        if len(case_grades) != 2:
            raise SystemExit(f"Expected 2 grades for case {case_id}, found {len(case_grades)}")
        result: dict[str, Any] = {"pair_id": pair_id, "case_id": case_id, "graders": []}

        for grade in case_grades:
            grader_result: dict[str, Any] = {"grader_id": grade.get("grader_id", "unknown")}
            for label in ("A", "B"):
                condition = mapping[label]
                output = grade[label]
                for metric in METRICS:
                    value = int(output[metric])
                    if not 1 <= value <= 5:
                        raise SystemExit(f"Invalid {metric} score for case {case_id} {label}: {value}")
                    scores[condition][metric].append(value)
                if output.get("tier1_failures"):
                    tier1_cases[condition].add(case_id)

            preference = grade["preference"]
            if preference in {"A", "B"}:
                preferred_condition = mapping[preference]
                preferences[preferred_condition] += 1
                non_ties += 1
                grader_result["preference"] = preferred_condition
            else:
                grader_result["preference"] = "tie"
            result["graders"].append(grader_result)
        pair_results.append(result)

    summary: dict[str, Any] = {}
    for condition in ("candidate", "baseline"):
        means = {metric: statistics.fmean(values) for metric, values in scores[condition].items()}
        means["coherence_distinctiveness_mean"] = statistics.fmean(
            [means["coherence"], means["distinctiveness"]]
        )
        word_counts = [
            len(path.read_text(encoding="utf-8").split())
            for path in sorted((ROOT / "runs" / condition).glob("case-*.md"))
        ]
        summary[condition] = {
            "mean_scores": means,
            "tier1_failure_cases": sorted(tier1_cases[condition]),
            "preferences": preferences[condition],
            "preference_rate_among_non_ties": preferences[condition] / non_ties if non_ties else 0.0,
            "word_counts": word_counts,
            "word_count_minimum": min(word_counts),
            "word_count_maximum": max(word_counts),
        }

    summary["candidate"]["coherence_distinctiveness_gain"] = (
        summary["candidate"]["mean_scores"]["coherence_distinctiveness_mean"]
        - summary["baseline"]["mean_scores"]["coherence_distinctiveness_mean"]
    )

    output = {
        "schema_version": "1.0.0",
        "status": "model-graded-results-before-release-interpretation",
        "grader_files": [str(path.relative_to(ROOT)) for path in grade_paths],
        "non_tie_preferences": non_ties,
        "summary": summary,
        "pairs": pair_results,
        "limitations": [
            "The outputs and blind reviews are textual model evidence, not rendered-interface or qualified-human evidence.",
            "Four synthetic cases do not estimate population-level variance.",
            "The exact service-side model identifier and sampling parameters were not exposed.",
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
