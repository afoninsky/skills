#!/usr/bin/env python3
"""Validate protected design-change scope, impact closure, and baseline identity."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
BASELINE_KINDS = {"approved-reference", "asserted-golden"}
REQUIRED_HARD_GATES = {
    "accessibility",
    "content_truth",
    "privacy_and_safety",
    "representative_user_evidence",
}
NON_HUMAN_APPROVERS = {
    "agent",
    "ai",
    "assistant",
    "automation",
    "codex",
    "llm",
    "model",
    "system",
}
LIST_FIELDS = (
    "allowed_files",
    "allowed_components",
    "allowed_tokens",
    "surfaces_may_change",
    "surfaces_must_not_change",
    "required_states",
    "required_targets",
    "required_checks",
    "protected_paths",
    "capability_confirmation_ids",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_timestamp(value: object) -> bool:
    if not non_empty_string(value):
        return False
    try:
        datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def human_approver(value: object) -> bool:
    if not non_empty_string(value):
        return False
    normalized = re.sub(r"[^a-z]+", " ", str(value).lower()).strip()
    return not bool(set(normalized.split()) & NON_HUMAN_APPROVERS)


def load_json(path: Path, errors: list[str], label: str) -> dict[str, Any] | None:
    if not path.is_file():
        errors.append(f"{label} does not exist: {path}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{label} is not valid JSON: {error}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{label} must be a JSON object")
        return None
    return data


def relative_path(
    project_root: Path,
    raw_path: object,
    errors: list[str],
    location: str,
    *,
    must_exist: bool = False,
) -> tuple[str, Path] | None:
    if not isinstance(raw_path, str) or not raw_path.strip():
        errors.append(f"{location} must be a non-empty project-relative path")
        return None
    candidate = Path(raw_path)
    if candidate.is_absolute():
        errors.append(f"{location} must not be absolute")
        return None
    resolved = (project_root / candidate).resolve()
    try:
        normalized = resolved.relative_to(project_root).as_posix()
    except ValueError:
        errors.append(f"{location} leaves the project root")
        return None
    if must_exist and not resolved.is_file():
        errors.append(f"{location} does not identify an existing file: {raw_path}")
    return normalized, resolved


def string_list(data: dict[str, Any], field: str, errors: list[str]) -> list[str]:
    value = data.get(field)
    if not isinstance(value, list) or not all(non_empty_string(item) for item in value):
        errors.append(f"change-manifest.{field} must be an array of non-empty strings")
        return []
    return [str(item) for item in value]


def valid_glob(pattern: str, errors: list[str], location: str) -> bool:
    if Path(pattern).is_absolute() or ".." in Path(pattern).parts:
        errors.append(f"{location} must stay inside the project root")
        return False
    normalized = pattern.replace("\\", "/").lstrip("./")
    if normalized in {"", "*", "**", "**/*"}:
        errors.append(f"{location} is too broad")
        return False
    return True


def path_matches(path: str, patterns: Iterable[str]) -> bool:
    normalized = path.replace("\\", "/").lstrip("./")
    return any(fnmatch.fnmatchcase(normalized, pattern.replace("\\", "/").lstrip("./")) for pattern in patterns)


def literal_prefix(pattern: str) -> str:
    normalized = pattern.replace("\\", "/").lstrip("./")
    wildcard_positions = [position for mark in "*?[" if (position := normalized.find(mark)) >= 0]
    if wildcard_positions:
        normalized = normalized[: min(wildcard_positions)]
    return normalized.rstrip("/")


def patterns_may_overlap(first: str, second: str) -> bool:
    first_prefix = literal_prefix(first)
    second_prefix = literal_prefix(second)
    if not first_prefix or not second_prefix:
        return True
    return (
        first_prefix == second_prefix
        or first_prefix.startswith(second_prefix + "/")
        or second_prefix.startswith(first_prefix + "/")
        or path_matches(first_prefix, [second])
        or path_matches(second_prefix, [first])
    )


def source_map_impact(
    source_map: dict[str, Any],
    component_ids: Iterable[str],
    token_ids: Iterable[str],
) -> tuple[dict[str, set[str]], list[str]]:
    errors: list[str] = []
    tokens = source_map.get("tokens", {})
    components = source_map.get("components", {})
    surfaces = source_map.get("surfaces", {})
    if not isinstance(tokens, dict) or not isinstance(components, dict) or not isinstance(surfaces, dict):
        return {}, ["source map tokens, components, and surfaces must be objects"]

    impacted_tokens = set(token_ids)
    impacted_components = set(component_ids)
    source_files: set[str] = set()

    for token_id in sorted(impacted_tokens):
        token = tokens.get(token_id)
        if not isinstance(token, dict):
            errors.append(f"allowed token is missing from source map: {token_id}")
            continue
        canonical = token.get("canonical_path")
        if non_empty_string(canonical):
            source_files.add(str(canonical))
        outputs = token.get("generated_outputs", [])
        if isinstance(outputs, list):
            source_files.update(str(output) for output in outputs if non_empty_string(output))
        direct_components = token.get("components", [])
        if isinstance(direct_components, list):
            impacted_components.update(
                str(component) for component in direct_components if non_empty_string(component)
            )

    for component_id, component in components.items():
        if not isinstance(component, dict):
            continue
        dependencies = component.get("token_dependencies", [])
        if isinstance(dependencies, list) and impacted_tokens.intersection(dependencies):
            impacted_components.add(str(component_id))

    impacted_surfaces: set[str] = set()
    impacted_states: set[str] = set()
    for component_id in sorted(impacted_components):
        component = components.get(component_id)
        if not isinstance(component, dict):
            errors.append(f"allowed component is missing from source map: {component_id}")
            continue
        files = component.get("source_files", [])
        states = component.get("states", [])
        mapped_surfaces = component.get("surfaces", [])
        if isinstance(files, list):
            source_files.update(str(path) for path in files if non_empty_string(path))
        if not isinstance(files, list) or not any(non_empty_string(path) for path in files):
            errors.append(f"mapped component has no concrete source_files: {component_id}")
        if isinstance(states, list):
            impacted_states.update(str(state) for state in states if non_empty_string(state))
        if isinstance(mapped_surfaces, list):
            impacted_surfaces.update(
                str(surface) for surface in mapped_surfaces if non_empty_string(surface)
            )

    for surface_id, surface in surfaces.items():
        if not isinstance(surface, dict):
            continue
        mapped_components = surface.get("components", [])
        if isinstance(mapped_components, list) and impacted_components.intersection(mapped_components):
            impacted_surfaces.add(str(surface_id))

    targets: set[str] = set()
    baseline_entries: set[str] = set()
    platforms: set[str] = set()
    for surface_id in sorted(impacted_surfaces):
        surface = surfaces.get(surface_id)
        if not isinstance(surface, dict):
            errors.append(f"impacted surface is missing from source map: {surface_id}")
            continue
        for field, destination in (
            ("targets", targets),
            ("baseline_entry_ids", baseline_entries),
            ("platforms", platforms),
        ):
            values = surface.get(field, [])
            if isinstance(values, list):
                destination.update(str(value) for value in values if non_empty_string(value))

    return {
        "tokens": impacted_tokens,
        "components": impacted_components,
        "surfaces": impacted_surfaces,
        "states": impacted_states,
        "targets": targets,
        "platforms": platforms,
        "source_files": source_files,
        "baseline_entry_ids": baseline_entries,
    }, errors


def baseline_protected_paths(
    baseline: dict[str, Any],
    contract_manifest_path: str,
    baseline_manifest_path: str,
    source_map_path: str,
    manifest: dict[str, Any],
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    protected = [
        contract_manifest_path,
        baseline_manifest_path,
        source_map_path,
        "design/baselines/**",
        "design/references/approved/**",
    ]
    protected.extend(str(path) for path in manifest.get("protected_paths", []))
    entries = baseline.get("entries", [])
    if not isinstance(entries, list):
        errors.append("baseline manifest entries must be an array")
        return protected, errors
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"baseline manifest entries[{index}] must be an object")
            continue
        path = entry.get("path")
        if non_empty_string(path):
            protected.append(str(path))
    return sorted(set(protected)), errors


def validate_baseline_identity(
    project_root: Path,
    baseline: dict[str, Any],
    baseline_path: Path,
    expected_manifest_hash: object,
    errors: list[str],
) -> None:
    if baseline.get("status") != "accepted":
        errors.append("baseline manifest status must be accepted before a protected change")
    if not human_approver(baseline.get("accepted_by")):
        errors.append("baseline manifest accepted_by must identify the human approver")
    if not valid_timestamp(baseline.get("accepted_at")):
        errors.append("baseline manifest accepted_at must be an ISO-8601 timestamp")
    for field in ("candidate_id", "approval_id", "accepted_ref"):
        if not non_empty_string(baseline.get(field)):
            errors.append(f"baseline manifest {field} is required")
    relative_path(
        project_root,
        baseline.get("approval_record"),
        errors,
        "baseline manifest approval_record",
        must_exist=True,
    )
    if not isinstance(expected_manifest_hash, str) or not SHA256_RE.fullmatch(expected_manifest_hash):
        errors.append("change-manifest.baseline_manifest_sha256 must be a lowercase SHA-256 digest")
    elif sha256_file(baseline_path) != expected_manifest_hash:
        errors.append("baseline manifest hash differs from the accepted identity")
    entries = baseline.get("entries", [])
    if not isinstance(entries, list):
        errors.append("baseline manifest entries must be an array")
        return
    for index, entry in enumerate(entries):
        location = f"baseline manifest entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{location} must be an object")
            continue
        kind = entry.get("kind")
        if kind not in BASELINE_KINDS:
            errors.append(
                f"{location}.kind must be approved-reference or asserted-golden; capture-only is not protected"
            )
        result = relative_path(
            project_root,
            entry.get("path"),
            errors,
            f"{location}.path",
            must_exist=True,
        )
        expected = entry.get("sha256")
        if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
            errors.append(f"{location}.sha256 must be a lowercase SHA-256 digest")
        elif result is not None and result[1].is_file() and sha256_file(result[1]) != expected:
            errors.append(f"protected baseline hash changed: {result[0]}")
        if kind == "asserted-golden":
            relative_path(
                project_root,
                entry.get("assertion_source"),
                errors,
                f"{location}.assertion_source",
                must_exist=True,
            )

    hard_gates = baseline.get("hard_gates")
    if not isinstance(hard_gates, dict):
        errors.append("baseline manifest hard_gates must be an object")
    else:
        missing = sorted(REQUIRED_HARD_GATES - set(hard_gates))
        if missing:
            errors.append(
                "baseline manifest hard_gates is missing required dispositions: "
                + ", ".join(missing)
            )


def validate_contract_identity(
    project_root: Path,
    contract: dict[str, Any],
    contract_path: Path,
    expected_manifest_hash: object,
    expected_source_map_path: str,
    errors: list[str],
) -> None:
    if contract.get("status") != "accepted":
        errors.append("contract manifest status must be accepted before a protected change")
    if not human_approver(contract.get("accepted_by")):
        errors.append("contract manifest accepted_by must identify the human approver")
    if not valid_timestamp(contract.get("accepted_at")):
        errors.append("contract manifest accepted_at must be an ISO-8601 timestamp")
    for field in ("candidate_id", "approval_id", "accepted_ref"):
        if not non_empty_string(contract.get(field)):
            errors.append(f"contract manifest {field} is required")
    relative_path(
        project_root,
        contract.get("approval_record"),
        errors,
        "contract manifest approval_record",
        must_exist=True,
    )
    if not isinstance(expected_manifest_hash, str) or not SHA256_RE.fullmatch(expected_manifest_hash):
        errors.append("change-manifest.contract_manifest_sha256 must be a lowercase SHA-256 digest")
    elif sha256_file(contract_path) != expected_manifest_hash:
        errors.append("contract manifest hash differs from the accepted identity")

    files = contract.get("files")
    if not isinstance(files, list) or not files:
        errors.append("accepted contract manifest files must be a non-empty array")
        return
    mapped_source = False
    for index, entry in enumerate(files):
        location = f"contract manifest files[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{location} must be an object")
            continue
        result = relative_path(
            project_root,
            entry.get("path"),
            errors,
            f"{location}.path",
            must_exist=True,
        )
        expected = entry.get("sha256")
        if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
            errors.append(f"{location}.sha256 must be a lowercase SHA-256 digest")
        elif result is not None and result[1].is_file() and sha256_file(result[1]) != expected:
            errors.append(f"accepted contract file hash changed: {result[0]}")
        if result is not None and result[0] == expected_source_map_path and entry.get("role") == "source-map":
            mapped_source = True
    if not mapped_source:
        errors.append("accepted contract manifest must map the selected source map with role 'source-map'")


def validate_manifest(
    project_root: Path,
    manifest_path: Path,
    *,
    require_approved: bool = True,
) -> tuple[list[str], dict[str, Any] | None, list[str]]:
    project_root = project_root.resolve()
    errors: list[str] = []
    manifest = load_json(manifest_path, errors, "change manifest")
    if manifest is None:
        return errors, None, []
    if manifest.get("schema_version") != 1:
        errors.append("change-manifest.schema_version must equal 1")
    for field in ("change_id", "base_ref", "intent", "change_kind"):
        if not non_empty_string(manifest.get(field)):
            errors.append(f"change-manifest.{field} is required")
    status = manifest.get("status")
    if status not in {"draft", "approved"}:
        errors.append("change-manifest.status must be draft or approved")
    if require_approved and status != "approved":
        errors.append("change-manifest.status must be approved before production writes or verification")
    approval = manifest.get("approval")
    if status == "approved":
        if not isinstance(approval, dict):
            errors.append("change-manifest.approval must be an object for approved status")
        else:
            if not non_empty_string(approval.get("approval_id")):
                errors.append("change-manifest.approval.approval_id is required")
            if not human_approver(approval.get("approved_by")):
                errors.append("change-manifest.approval.approved_by must identify the human approver")
            if not valid_timestamp(approval.get("approved_at")):
                errors.append("change-manifest.approval.approved_at must be an ISO-8601 timestamp")
            relative_path(
                project_root,
                approval.get("approval_record"),
                errors,
                "change-manifest.approval.approval_record",
                must_exist=True,
            )
    if manifest.get("baseline_updates_allowed") is not False:
        errors.append("change-manifest.baseline_updates_allowed must be false")

    lists = {field: string_list(manifest, field, errors) for field in LIST_FIELDS}
    if not lists["allowed_files"]:
        errors.append("change-manifest.allowed_files must not be empty")
    if not lists["surfaces_may_change"]:
        errors.append("change-manifest.surfaces_may_change must not be empty")
    if not lists["required_targets"]:
        errors.append("change-manifest.required_targets must not be empty")
    if not lists["required_checks"]:
        errors.append("change-manifest.required_checks must not be empty")
    for field in ("allowed_files", "protected_paths"):
        for index, pattern in enumerate(lists[field]):
            valid_glob(pattern, errors, f"change-manifest.{field}[{index}]")

    contract_result = relative_path(
        project_root,
        manifest.get("contract_manifest"),
        errors,
        "change-manifest.contract_manifest",
        must_exist=True,
    )
    source_result = relative_path(
        project_root,
        manifest.get("source_map"),
        errors,
        "change-manifest.source_map",
        must_exist=True,
    )
    baseline_result = relative_path(
        project_root,
        manifest.get("baseline_manifest"),
        errors,
        "change-manifest.baseline_manifest",
        must_exist=True,
    )
    if contract_result is None or source_result is None or baseline_result is None:
        return errors, manifest, []
    contract_path_text, contract_path = contract_result
    source_path_text, source_path = source_result
    baseline_path_text, baseline_path = baseline_result
    contract = load_json(contract_path, errors, "contract manifest")
    source_map = load_json(source_path, errors, "source map")
    baseline = load_json(baseline_path, errors, "baseline manifest")
    if contract is None or source_map is None or baseline is None:
        return errors, manifest, []

    validate_contract_identity(
        project_root,
        contract,
        contract_path,
        manifest.get("contract_manifest_sha256"),
        source_path_text,
        errors,
    )
    source_hash = manifest.get("source_map_sha256")
    if not isinstance(source_hash, str) or not SHA256_RE.fullmatch(source_hash):
        errors.append("change-manifest.source_map_sha256 must be a lowercase SHA-256 digest")
    elif sha256_file(source_path) != source_hash:
        errors.append("source map hash differs from the accepted identity")

    validate_baseline_identity(
        project_root,
        baseline,
        baseline_path,
        manifest.get("baseline_manifest_sha256"),
        errors,
    )
    protected, protected_errors = baseline_protected_paths(
        baseline,
        contract_path_text,
        baseline_path_text,
        source_path_text,
        manifest,
    )
    errors.extend(protected_errors)
    for allowed in lists["allowed_files"]:
        for protected_pattern in protected:
            if patterns_may_overlap(allowed, protected_pattern):
                errors.append(
                    f"allowed file pattern overlaps protected design/baseline path: {allowed!r} vs {protected_pattern!r}"
                )

    impact, impact_errors = source_map_impact(
        source_map,
        lists["allowed_components"],
        lists["allowed_tokens"],
    )
    errors.extend(impact_errors)
    surfaces = source_map.get("surfaces", {})
    if not isinstance(surfaces, dict):
        surfaces = {}
    known_surfaces = set(str(surface) for surface in surfaces)
    may_change = set(lists["surfaces_may_change"])
    must_not_change = set(lists["surfaces_must_not_change"])
    unknown_surfaces = (may_change | must_not_change) - known_surfaces
    if unknown_surfaces:
        errors.append("change manifest references unknown surfaces: " + ", ".join(sorted(unknown_surfaces)))
    overlap = may_change & must_not_change
    if overlap:
        errors.append("surfaces cannot both change and remain protected: " + ", ".join(sorted(overlap)))
    unclassified = known_surfaces - may_change - must_not_change
    if unclassified:
        errors.append("every known surface must be classified; missing: " + ", ".join(sorted(unclassified)))
    missing_impacted_surfaces = impact.get("surfaces", set()) - may_change
    if missing_impacted_surfaces:
        errors.append(
            "shared impact requires additional surfaces_may_change: "
            + ", ".join(sorted(missing_impacted_surfaces))
        )

    required_targets_from_surfaces: set[str] = set()
    for surface_id in may_change:
        surface = surfaces.get(surface_id)
        if isinstance(surface, dict) and isinstance(surface.get("targets"), list):
            required_targets_from_surfaces.update(
                str(target) for target in surface["targets"] if non_empty_string(target)
            )
    missing_targets = (impact.get("targets", set()) | required_targets_from_surfaces) - set(
        lists["required_targets"]
    )
    if missing_targets:
        errors.append("required_targets does not close impact: " + ", ".join(sorted(missing_targets)))
    missing_states = impact.get("states", set()) - set(lists["required_states"])
    if missing_states:
        errors.append("required_states does not close component impact: " + ", ".join(sorted(missing_states)))
    for source_file in sorted(impact.get("source_files", set())):
        if not path_matches(source_file, lists["allowed_files"]):
            errors.append(f"mapped impacted source file is not allowed: {source_file}")
    return errors, manifest, protected


def git_changed_files(project_root: Path, base_ref: str, errors: list[str]) -> list[str]:
    try:
        subprocess.run(
            ["git", "rev-parse", "--verify", f"{base_ref}^{{commit}}"],
            cwd=project_root,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        diff = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACDMRTUXB", base_ref, "--"],
            cwd=project_root,
            check=True,
            capture_output=True,
            text=True,
        )
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=project_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        errors.append("Git is unavailable")
        return []
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() if error.stderr else str(error)
        errors.append(f"Git could not compute change scope: {detail}")
        return []
    return sorted(set(filter(None, diff.stdout.splitlines() + untracked.stdout.splitlines())))


def verify_changed_files(
    changed_files: Iterable[str],
    allowed_files: Iterable[str],
    protected_paths: Iterable[str],
    manifest_relative: str,
    administrative_paths: Iterable[str] = (),
) -> list[str]:
    errors: list[str] = []
    allowed = list(allowed_files)
    protected = list(protected_paths)
    administrative = {path.replace("\\", "/").lstrip("./") for path in administrative_paths}
    administrative.add(manifest_relative)
    for raw_path in changed_files:
        path = raw_path.replace("\\", "/").lstrip("./")
        if path in administrative:
            continue
        if path_matches(path, protected):
            errors.append(f"protected baseline/contract path changed: {path}")
        elif not path_matches(path, allowed):
            errors.append(f"changed file is outside manifest scope: {path}")
    return errors


def resolve_manifest_path(project_root: Path, raw_path: Path) -> tuple[Path | None, str | None, str | None]:
    project_root = project_root.resolve()
    resolved = raw_path.resolve() if raw_path.is_absolute() else (project_root / raw_path).resolve()
    try:
        relative = resolved.relative_to(project_root).as_posix()
    except ValueError:
        return None, None, "manifest path leaves the project root"
    return resolved, relative, None


def print_errors(errors: list[str]) -> int:
    if not errors:
        return 0
    print("Design change guard failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate or verify a protected product-design change."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("validate", "verify"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--project-root", type=Path, default=Path.cwd())
        subparser.add_argument("--manifest", type=Path, required=True)

    impact_parser = subparsers.add_parser("impact")
    impact_parser.add_argument("--project-root", type=Path, default=Path.cwd())
    impact_parser.add_argument(
        "--source-map", type=Path, default=Path("design/contract/source-map.json")
    )
    impact_parser.add_argument("--component", action="append", default=[])
    impact_parser.add_argument("--token", action="append", default=[])
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    if args.command == "impact":
        source_result = resolve_manifest_path(project_root, args.source_map)
        source_path, _, path_error = source_result
        errors = [path_error] if path_error else []
        source_map = load_json(source_path, errors, "source map") if source_path else None
        if source_map is None:
            return print_errors(errors)
        impact, impact_errors = source_map_impact(source_map, args.component, args.token)
        errors.extend(impact_errors)
        if errors:
            return print_errors(errors)
        print(json.dumps({key: sorted(value) for key, value in impact.items()}, indent=2))
        return 0

    manifest_path, manifest_relative, path_error = resolve_manifest_path(project_root, args.manifest)
    if path_error or manifest_path is None or manifest_relative is None:
        return print_errors([path_error or "invalid manifest path"])
    errors, manifest, protected = validate_manifest(project_root, manifest_path)
    if manifest is not None:
        changed = git_changed_files(project_root, str(manifest.get("base_ref", "")), errors)
        approval = manifest.get("approval", {})
        administrative_paths = []
        if isinstance(approval, dict) and non_empty_string(approval.get("approval_record")):
            administrative_paths.append(str(approval["approval_record"]))
        errors.extend(
            verify_changed_files(
                changed,
                manifest.get("allowed_files", []),
                protected,
                manifest_relative,
                administrative_paths,
            )
        )
    if errors:
        return print_errors(errors)
    if args.command == "verify":
        print("Protected design change verified; accepted baselines are unchanged.")
    else:
        print("Protected design change manifest is valid and approved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
