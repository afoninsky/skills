#!/usr/bin/env python3
"""Compare deterministic protected evidence for a scoped product-design change."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

REQUIRED_CHANNELS = {
    "behavior",
    "local_geometry",
    "render",
    "side_effects",
    "structure",
    "style",
}
TOP_LEVEL_FIELDS = {"schema_version", "subject", "capture_id", "cases"}
CASE_FIELDS = {
    "authorized_subtree",
    "case_id",
    "conditions",
    "evidence",
    "target",
    "turn",
}
AUTHORIZED_SUBTREE_FIELDS = {"locator", "match_count", "operation"}
AUTHORIZED_OPERATIONS = {"delete", "insert", "modify"}
CONDITION_FIELDS = {
    "fixture",
    "fonts",
    "locale",
    "probe",
    "runtime",
    "scale",
    "state",
    "surface",
    "theme",
    "viewport_or_device",
}


@dataclass(frozen=True)
class EvidenceCase:
    target: str
    turn: str
    case_id: str
    conditions_sha256: str
    authorized_subtree: Optional[tuple[str, str, int]]
    evidence_sha256: dict[str, str]

    @property
    def key(self) -> tuple[str, str, str]:
        return self.target, self.turn, self.case_id


@dataclass(frozen=True)
class EvidenceBundle:
    path: Path
    subject: str
    capture_id: str
    cases: dict[tuple[str, str, str], EvidenceCase]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_json(value: object) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def reject_json_constant(value: str) -> None:
    raise ValueError(f"unsupported JSON numeric constant: {value}")


def resolve_artifact(
    bundle_path: Path,
    raw_path: object,
    errors: list[str],
    location: str,
) -> Optional[Path]:
    if not non_empty_string(raw_path):
        errors.append(f"{location} must be a non-empty bundle-relative path")
        return None

    relative = Path(str(raw_path))
    if relative.is_absolute() or ".." in relative.parts:
        errors.append(f"{location} must stay inside the evidence bundle")
        return None

    bundle_root = bundle_path.parent.resolve()
    unresolved = bundle_path.parent / relative
    cursor = bundle_path.parent
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            errors.append(f"{location} must not traverse a symlink: {raw_path}")
            return None

    resolved = unresolved.resolve()
    try:
        resolved.relative_to(bundle_root)
    except ValueError:
        errors.append(f"{location} leaves the evidence bundle")
        return None
    if not resolved.is_file():
        errors.append(f"{location} does not identify a file: {raw_path}")
        return None
    if resolved.stat().st_size == 0:
        errors.append(f"{location} must not be empty: {raw_path}")
        return None
    return resolved


def validate_conditions(
    value: object,
    errors: list[str],
    location: str,
) -> Optional[str]:
    if not isinstance(value, dict):
        errors.append(f"{location} must be an object")
        return None

    missing = sorted(CONDITION_FIELDS - set(value))
    if missing:
        errors.append(f"{location} is missing fields: " + ", ".join(missing))
    unknown = sorted(set(value) - CONDITION_FIELDS)
    if unknown:
        errors.append(f"{location} has unsupported fields: " + ", ".join(unknown))

    for field in (
        "surface",
        "state",
        "fixture",
        "theme",
        "locale",
        "runtime",
        "probe",
    ):
        if not non_empty_string(value.get(field)):
            errors.append(f"{location}.{field} must be a non-empty string")

    viewport_or_device = value.get("viewport_or_device")
    if not (
        non_empty_string(viewport_or_device)
        or isinstance(viewport_or_device, dict)
        and bool(viewport_or_device)
    ):
        errors.append(
            f"{location}.viewport_or_device must be a non-empty string or object"
        )

    scale = value.get("scale")
    if (
        isinstance(scale, bool)
        or not isinstance(scale, (int, float))
        or not math.isfinite(scale)
        or scale <= 0
    ):
        errors.append(f"{location}.scale must be positive")

    fonts = value.get("fonts")
    if not isinstance(fonts, list) or not fonts:
        errors.append(f"{location}.fonts must be a non-empty array")
    elif any(not non_empty_string(font) for font in fonts):
        errors.append(f"{location}.fonts entries must be non-empty strings")

    if errors:
        return None
    return sha256_json(value)


def load_bundle(path: Path) -> tuple[Optional[EvidenceBundle], list[str]]:
    path = path.resolve()
    errors: list[str] = []
    if not path.is_file():
        return None, [f"bundle does not exist: {path}"]
    try:
        data = json.loads(
            path.read_text(encoding="utf-8"),
            parse_constant=reject_json_constant,
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        return None, [f"bundle is not valid JSON: {path}: {error}"]
    if not isinstance(data, dict):
        return None, [f"bundle must be a JSON object: {path}"]

    unknown_top = sorted(set(data) - TOP_LEVEL_FIELDS)
    if unknown_top:
        errors.append("bundle has unsupported fields: " + ", ".join(unknown_top))
    if type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        errors.append("bundle.schema_version must equal 1")
    if not non_empty_string(data.get("subject")):
        errors.append("bundle.subject must be a non-empty string")
    if not non_empty_string(data.get("capture_id")):
        errors.append("bundle.capture_id must be a non-empty string")

    raw_cases = data.get("cases")
    if not isinstance(raw_cases, list) or not raw_cases:
        errors.append("bundle.cases must be a non-empty array")
        return None, errors

    cases: dict[tuple[str, str, str], EvidenceCase] = {}
    bundle_evidence_paths: dict[Path, str] = {}
    for index, raw_case in enumerate(raw_cases):
        location = f"bundle.cases[{index}]"
        if not isinstance(raw_case, dict):
            errors.append(f"{location} must be an object")
            continue
        missing_case = sorted(CASE_FIELDS - set(raw_case))
        unknown_case = sorted(set(raw_case) - CASE_FIELDS)
        if missing_case:
            errors.append(f"{location} is missing fields: " + ", ".join(missing_case))
        if unknown_case:
            errors.append(f"{location} has unsupported fields: " + ", ".join(unknown_case))

        target = raw_case.get("target")
        turn = raw_case.get("turn")
        case_id = raw_case.get("case_id")
        if not non_empty_string(target):
            errors.append(f"{location}.target must be a non-empty string")
        if not non_empty_string(turn):
            errors.append(f"{location}.turn must be a non-empty string")
        if not non_empty_string(case_id):
            errors.append(f"{location}.case_id must be a non-empty string")
        if not all(non_empty_string(value) for value in (target, turn, case_id)):
            continue
        key = str(target), str(turn), str(case_id)
        if key in cases:
            errors.append(
                "duplicate case: "
                f"target={key[0]!r}, turn={key[1]!r}, case_id={key[2]!r}"
            )
            continue

        conditions_sha256 = validate_conditions(
            raw_case.get("conditions"),
            errors,
            f"{location}.conditions",
        )
        authorized_subtree: Optional[tuple[str, str, int]] = None
        raw_authorized = raw_case.get("authorized_subtree")
        if raw_authorized is not None:
            if not isinstance(raw_authorized, dict):
                errors.append(f"{location}.authorized_subtree must be an object or null")
            else:
                missing_authorized = sorted(
                    AUTHORIZED_SUBTREE_FIELDS - set(raw_authorized)
                )
                unknown_authorized = sorted(
                    set(raw_authorized) - AUTHORIZED_SUBTREE_FIELDS
                )
                if missing_authorized:
                    errors.append(
                        f"{location}.authorized_subtree is missing fields: "
                        + ", ".join(missing_authorized)
                    )
                if unknown_authorized:
                    errors.append(
                        f"{location}.authorized_subtree has unsupported fields: "
                        + ", ".join(unknown_authorized)
                    )
                locator = raw_authorized.get("locator")
                operation = raw_authorized.get("operation")
                match_count = raw_authorized.get("match_count")
                if not non_empty_string(locator):
                    errors.append(
                        f"{location}.authorized_subtree.locator must be a non-empty string"
                    )
                if operation not in AUTHORIZED_OPERATIONS:
                    errors.append(
                        f"{location}.authorized_subtree.operation must be one of: "
                        + ", ".join(sorted(AUTHORIZED_OPERATIONS))
                    )
                if type(match_count) is not int or match_count not in {0, 1}:
                    errors.append(
                        f"{location}.authorized_subtree.match_count must be 0 or 1"
                    )
                if (
                    non_empty_string(locator)
                    and operation in AUTHORIZED_OPERATIONS
                    and type(match_count) is int
                ):
                    authorized_subtree = str(locator), str(operation), match_count

        raw_evidence = raw_case.get("evidence")
        if not isinstance(raw_evidence, dict):
            errors.append(f"{location}.evidence must be an object")
            continue
        invalid_channels = sorted(
            channel for channel in raw_evidence if not non_empty_string(channel)
        )
        if invalid_channels:
            errors.append(f"{location}.evidence channel names must be non-empty strings")
        missing_channels = sorted(REQUIRED_CHANNELS - set(raw_evidence))
        if missing_channels:
            errors.append(
                f"{location}.evidence is missing required channels: "
                + ", ".join(missing_channels)
            )

        evidence_hashes: dict[str, str] = {}
        evidence_paths: dict[Path, str] = {}
        for channel, artifact in sorted(raw_evidence.items()):
            if not non_empty_string(channel):
                continue
            artifact_path = resolve_artifact(
                path,
                artifact,
                errors,
                f"{location}.evidence.{channel}",
            )
            if artifact_path is not None:
                if artifact_path in evidence_paths:
                    errors.append(
                        f"{location}.evidence.{channel} reuses the artifact for "
                        f"channel {evidence_paths[artifact_path]!r}"
                    )
                    continue
                if artifact_path in bundle_evidence_paths:
                    errors.append(
                        f"{location}.evidence.{channel} reuses the artifact for "
                        f"{bundle_evidence_paths[artifact_path]}"
                    )
                    continue
                evidence_paths[artifact_path] = str(channel)
                bundle_evidence_paths[artifact_path] = (
                    f"case_id={key[2]!r}, channel={channel!r}"
                )
                evidence_hashes[str(channel)] = sha256_file(artifact_path)

        if conditions_sha256 is not None:
            cases[key] = EvidenceCase(
                target=key[0],
                turn=key[1],
                case_id=key[2],
                conditions_sha256=conditions_sha256,
                authorized_subtree=authorized_subtree,
                evidence_sha256=evidence_hashes,
            )

    if errors:
        return None, errors
    return EvidenceBundle(
        path=path,
        subject=str(data["subject"]),
        capture_id=str(data["capture_id"]),
        cases=cases,
    ), []


def case_label(key: tuple[str, str, str]) -> str:
    return f"target={key[0]!r}, turn={key[1]!r}, case_id={key[2]!r}"


def compare_bundles(
    references: Iterable[EvidenceBundle],
    candidate: EvidenceBundle,
) -> list[str]:
    references = list(references)
    differences: list[str] = []
    expected_keys: set[tuple[str, str, str]] = set()

    for reference in references:
        for key, expected in reference.cases.items():
            expected_keys.add(key)
            actual = candidate.cases.get(key)
            label = case_label(key)
            if actual is None:
                differences.append(f"missing candidate case: {label}")
                continue
            if actual.conditions_sha256 != expected.conditions_sha256:
                differences.append(
                    f"conditions changed for {label}: "
                    f"{expected.conditions_sha256} -> {actual.conditions_sha256}"
                )
            if expected.authorized_subtree is None:
                if actual.authorized_subtree is not None:
                    differences.append(f"authorized subtree changed for {label}")
            elif actual.authorized_subtree is None:
                differences.append(f"authorized subtree changed for {label}")
            else:
                expected_locator, expected_operation, expected_count = (
                    expected.authorized_subtree
                )
                actual_locator, actual_operation, actual_count = actual.authorized_subtree
                if (actual_locator, actual_operation) != (
                    expected_locator,
                    expected_operation,
                ):
                    differences.append(f"authorized subtree changed for {label}")
                reference_count, candidate_count = {
                    "delete": (1, 0),
                    "insert": (0, 1),
                    "modify": (1, 1),
                }[expected_operation]
                if expected_count != reference_count:
                    differences.append(
                        f"reference match_count for {label} must be {reference_count} "
                        f"for operation={expected_operation!r}"
                    )
                if actual_count != candidate_count:
                    differences.append(
                        f"candidate match_count for {label} must be {candidate_count} "
                        f"for operation={expected_operation!r}"
                    )
            expected_channels = set(expected.evidence_sha256)
            actual_channels = set(actual.evidence_sha256)
            for channel in sorted(expected_channels - actual_channels):
                differences.append(f"missing evidence channel {channel!r} for {label}")
            for channel in sorted(actual_channels - expected_channels):
                differences.append(f"unexpected evidence channel {channel!r} for {label}")
            for channel in sorted(expected_channels & actual_channels):
                expected_hash = expected.evidence_sha256[channel]
                actual_hash = actual.evidence_sha256[channel]
                if actual_hash != expected_hash:
                    differences.append(
                        f"protected evidence changed for {label}, channel={channel!r}: "
                        f"{expected_hash} -> {actual_hash}"
                    )

    for key in sorted(set(candidate.cases) - expected_keys):
        differences.append(f"unexpected candidate case: {case_label(key)}")
    return sorted(set(differences))


def print_invalid(label: str, errors: Iterable[str]) -> None:
    print(f"Invalid {label} preservation evidence:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fail when deterministic protected evidence changes across a scoped design edit.",
        epilog=(
            "Reference bundles contain only protected, normalized evidence. "
            "Omit the authorized subtree during project-native capture; do not use ignore masks."
        ),
    )
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--expected-candidate-capture-id", required=True)
    parser.add_argument("--against", type=Path, action="append", required=True)
    args = parser.parse_args(argv)

    candidate, candidate_errors = load_bundle(args.candidate)
    if candidate is None:
        print_invalid("candidate", candidate_errors)
        return 2

    references: list[EvidenceBundle] = []
    for index, reference_path in enumerate(args.against, start=1):
        reference, reference_errors = load_bundle(reference_path)
        if reference is None:
            print_invalid(f"reference {index}", reference_errors)
            return 2
        references.append(reference)

    identity_errors: list[str] = []
    if candidate.capture_id != args.expected_candidate_capture_id:
        identity_errors.append(
            "candidate capture_id does not match --expected-candidate-capture-id: "
            f"{candidate.capture_id!r} != {args.expected_candidate_capture_id!r}"
        )
    reference_capture_ids = [reference.capture_id for reference in references]
    if candidate.capture_id in reference_capture_ids:
        identity_errors.append("candidate capture_id duplicates a reference capture_id")
    duplicate_reference_capture_ids = sorted(
        capture_id
        for capture_id in set(reference_capture_ids)
        if reference_capture_ids.count(capture_id) > 1
    )
    if duplicate_reference_capture_ids:
        identity_errors.append(
            "reference capture_ids must be unique: "
            + ", ".join(duplicate_reference_capture_ids)
        )
    if identity_errors:
        print_invalid("bundle identities", identity_errors)
        return 2

    differences = compare_bundles(references, candidate)
    if differences:
        print("Protected preservation comparison failed:", file=sys.stderr)
        for difference in differences:
            print(f"- {difference}", file=sys.stderr)
        return 1

    names = ", ".join(reference.subject for reference in references)
    print(f"Protected evidence matches: {names}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
