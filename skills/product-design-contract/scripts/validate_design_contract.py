#!/usr/bin/env python3
"""Validate a Git-owned product design contract and accepted baseline identity."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

REQUIRED_CONTRACT_ROLES = {
    "principles",
    "components",
    "content",
    "responsive-adaptive",
    "source-map",
}
BASELINE_KINDS = {"approved-reference", "asserted-golden"}
HARD_GATE_STATUSES = {"evidenced", "not-evidenced", "not-applicable"}
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
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def project_file(
    project_root: Path,
    raw_path: object,
    errors: list[str],
    location: str,
    *,
    must_exist: bool = True,
) -> Path | None:
    if not isinstance(raw_path, str) or not raw_path.strip():
        errors.append(f"{location} must be a non-empty project-relative path")
        return None
    relative = Path(raw_path)
    if relative.is_absolute():
        errors.append(f"{location} must not be absolute")
        return None
    resolved = (project_root / relative).resolve()
    try:
        resolved.relative_to(project_root)
    except ValueError:
        errors.append(f"{location} leaves the project root")
        return None
    if must_exist and not resolved.is_file():
        errors.append(f"{location} does not identify an existing file: {raw_path}")
    return resolved


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


def string_list(value: object, location: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not all(non_empty_string(item) for item in value):
        errors.append(f"{location} must be an array of non-empty strings")
        return []
    return [str(item) for item in value]


def validate_acceptance_identity(
    data: dict[str, Any],
    project_root: Path,
    location: str,
    errors: list[str],
) -> None:
    for field in ("candidate_id", "approval_id", "accepted_ref"):
        if not non_empty_string(data.get(field)):
            errors.append(f"{location}.{field} is required for accepted state")
    if not human_approver(data.get("accepted_by")):
        errors.append(
            f"{location}.accepted_by must identify the human approver, not an agent or automation"
        )
    if not valid_timestamp(data.get("accepted_at")):
        errors.append(f"{location}.accepted_at must be an ISO-8601 timestamp")
    project_file(
        project_root,
        data.get("approval_record"),
        errors,
        f"{location}.approval_record",
    )


def validate_source_map(
    data: dict[str, Any],
    project_root: Path,
    errors: list[str],
    *,
    accepted: bool,
) -> tuple[set[str], set[str]]:
    if data.get("schema_version") != 1:
        errors.append("source-map.schema_version must equal 1")

    platforms = data.get("platform_architecture")
    if not isinstance(platforms, list):
        errors.append("source-map.platform_architecture must be an array")
        platforms = []
    if accepted and not platforms:
        errors.append("source-map.platform_architecture must not be empty for an accepted contract")

    platform_ids: set[str] = set()
    for index, platform in enumerate(platforms):
        location = f"source-map.platform_architecture[{index}]"
        if not isinstance(platform, dict):
            errors.append(f"{location} must be an object")
            continue
        platform_id = platform.get("id")
        if not non_empty_string(platform_id):
            errors.append(f"{location}.id is required")
            continue
        if platform_id in platform_ids:
            errors.append(f"{location}.id is duplicated: {platform_id}")
        platform_ids.add(str(platform_id))
        if not non_empty_string(platform.get("kind")):
            errors.append(f"{location}.kind is required")
        roots = string_list(platform.get("source_roots", []), f"{location}.source_roots", errors)
        for root_index, root in enumerate(roots):
            resolved = (project_root / root).resolve()
            try:
                resolved.relative_to(project_root)
            except ValueError:
                errors.append(f"{location}.source_roots[{root_index}] leaves the project root")
        shares = string_list(platform.get("shares_ui_with", []), f"{location}.shares_ui_with", errors)
        for shared in shares:
            if shared == platform_id:
                errors.append(f"{location}.shares_ui_with cannot reference itself")

    for index, platform in enumerate(platforms):
        if not isinstance(platform, dict):
            continue
        for shared in platform.get("shares_ui_with", []):
            if shared not in platform_ids:
                errors.append(
                    f"source-map.platform_architecture[{index}].shares_ui_with references unknown platform {shared!r}"
                )

    tokens = data.get("tokens")
    components = data.get("components")
    surfaces = data.get("surfaces")
    if not isinstance(tokens, dict):
        errors.append("source-map.tokens must be an object")
        tokens = {}
    if not isinstance(components, dict):
        errors.append("source-map.components must be an object")
        components = {}
    if not isinstance(surfaces, dict):
        errors.append("source-map.surfaces must be an object")
        surfaces = {}
    if accepted and not surfaces:
        errors.append("source-map.surfaces must not be empty for an accepted contract")

    for token_id, token in tokens.items():
        location = f"source-map.tokens[{token_id!r}]"
        if not non_empty_string(token_id) or not isinstance(token, dict):
            errors.append(f"{location} must be a named object")
            continue
        canonical = project_file(
            project_root,
            token.get("canonical_path"),
            errors,
            f"{location}.canonical_path",
        )
        if canonical is None:
            continue
        generated = string_list(token.get("generated_outputs", []), f"{location}.generated_outputs", errors)
        for output_index, output in enumerate(generated):
            project_file(
                project_root,
                output,
                errors,
                f"{location}.generated_outputs[{output_index}]",
            )
        refs = string_list(token.get("components", []), f"{location}.components", errors)
        for component_id in refs:
            if component_id not in components:
                errors.append(f"{location}.components references unknown component {component_id!r}")

    for component_id, component in components.items():
        location = f"source-map.components[{component_id!r}]"
        if not non_empty_string(component_id) or not isinstance(component, dict):
            errors.append(f"{location} must be a named object")
            continue
        source_files = string_list(component.get("source_files", []), f"{location}.source_files", errors)
        for file_index, source_file in enumerate(source_files):
            project_file(
                project_root,
                source_file,
                errors,
                f"{location}.source_files[{file_index}]",
            )
        for token_id in string_list(
            component.get("token_dependencies", []),
            f"{location}.token_dependencies",
            errors,
        ):
            if token_id not in tokens:
                errors.append(f"{location}.token_dependencies references unknown token {token_id!r}")
        string_list(component.get("states", []), f"{location}.states", errors)
        for surface_id in string_list(component.get("surfaces", []), f"{location}.surfaces", errors):
            if surface_id not in surfaces:
                errors.append(f"{location}.surfaces references unknown surface {surface_id!r}")

    baseline_ids: set[str] = set()
    for surface_id, surface in surfaces.items():
        location = f"source-map.surfaces[{surface_id!r}]"
        if not non_empty_string(surface_id) or not isinstance(surface, dict):
            errors.append(f"{location} must be a named object")
            continue
        for platform_id in string_list(surface.get("platforms", []), f"{location}.platforms", errors):
            if platform_id not in platform_ids:
                errors.append(f"{location}.platforms references unknown platform {platform_id!r}")
        for component_id in string_list(surface.get("components", []), f"{location}.components", errors):
            if component_id not in components:
                errors.append(f"{location}.components references unknown component {component_id!r}")
        string_list(surface.get("targets", []), f"{location}.targets", errors)
        for baseline_id in string_list(
            surface.get("baseline_entry_ids", []), f"{location}.baseline_entry_ids", errors
        ):
            baseline_ids.add(baseline_id)

    variants = data.get("intentional_variants")
    if not isinstance(variants, list):
        errors.append("source-map.intentional_variants must be an array")

    return set(surfaces), baseline_ids


def validate_contract_manifest(
    data: dict[str, Any],
    project_root: Path,
    errors: list[str],
    *,
    freeze: bool,
) -> tuple[bool, Path | None]:
    if data.get("schema_version") != 1:
        errors.append("contract-manifest.schema_version must equal 1")
    status = data.get("status")
    if status not in {"draft", "accepted"}:
        errors.append("contract-manifest.status must be 'draft' or 'accepted'")
    accepted = status == "accepted"
    if freeze and not accepted:
        errors.append("contract-manifest.status must be 'accepted' in freeze mode")
    if accepted:
        validate_acceptance_identity(data, project_root, "contract-manifest", errors)

    files = data.get("files")
    if not isinstance(files, list):
        errors.append("contract-manifest.files must be an array")
        files = []
    if accepted and not files:
        errors.append("contract-manifest.files must not be empty for accepted state")

    roles: set[str] = set()
    paths: set[str] = set()
    source_map_path: Path | None = None
    for index, entry in enumerate(files):
        location = f"contract-manifest.files[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{location} must be an object")
            continue
        role = entry.get("role")
        if not non_empty_string(role):
            errors.append(f"{location}.role is required")
        elif role in roles:
            errors.append(f"{location}.role is duplicated: {role}")
        else:
            roles.add(str(role))
        raw_path = entry.get("path")
        path = project_file(project_root, raw_path, errors, f"{location}.path")
        if isinstance(raw_path, str):
            if raw_path in paths:
                errors.append(f"{location}.path is duplicated: {raw_path}")
            paths.add(raw_path)
        if path is not None and role == "source-map":
            source_map_path = path
        expected_hash = entry.get("sha256")
        if accepted or expected_hash:
            if not isinstance(expected_hash, str) or not SHA256_RE.fullmatch(expected_hash):
                errors.append(f"{location}.sha256 must be a lowercase SHA-256 digest")
            elif path is not None and path.is_file() and sha256_file(path) != expected_hash:
                errors.append(f"{location}.sha256 does not match {raw_path}")

    if accepted:
        missing = sorted(REQUIRED_CONTRACT_ROLES - roles)
        if missing:
            errors.append(f"contract-manifest.files is missing required roles: {', '.join(missing)}")
    return accepted, source_map_path


def validate_baseline_manifest(
    data: dict[str, Any],
    project_root: Path,
    errors: list[str],
    *,
    freeze: bool,
    surface_ids: set[str],
    mapped_baseline_ids: set[str],
    approval_id: str | None,
) -> None:
    if data.get("schema_version") != 1:
        errors.append("baseline-manifest.schema_version must equal 1")
    status = data.get("status")
    if status not in {"draft", "accepted"}:
        errors.append("baseline-manifest.status must be 'draft' or 'accepted'")
    accepted = status == "accepted"
    if freeze and not accepted:
        errors.append("baseline-manifest.status must be 'accepted' in freeze mode")
    if accepted:
        validate_acceptance_identity(data, project_root, "baseline-manifest", errors)
    if freeze:
        if not non_empty_string(approval_id):
            errors.append("freeze mode requires the router's explicit approval ID")
        elif data.get("approval_id") != approval_id:
            errors.append("baseline-manifest.approval_id does not match the authorized freeze approval")

    hard_gates = data.get("hard_gates")
    if not isinstance(hard_gates, dict):
        errors.append("baseline-manifest.hard_gates must be an object")
        hard_gates = {}
    if accepted:
        missing_hard_gates = sorted(REQUIRED_HARD_GATES - set(hard_gates))
        if missing_hard_gates:
            errors.append(
                "baseline-manifest.hard_gates is missing required dispositions: "
                + ", ".join(missing_hard_gates)
            )
    for gate_id, gate in hard_gates.items():
        location = f"baseline-manifest.hard_gates[{gate_id!r}]"
        if not isinstance(gate, dict) or gate.get("status") not in HARD_GATE_STATUSES:
            errors.append(f"{location}.status must be evidenced, not-evidenced, or not-applicable")
            continue
        evidence = string_list(gate.get("evidence", []), f"{location}.evidence", errors)
        if gate.get("status") == "evidenced" and not evidence:
            errors.append(f"{location}.evidence must not be empty when status is evidenced")
        if gate.get("status") == "not-applicable" and not non_empty_string(gate.get("rationale")):
            errors.append(f"{location}.rationale is required when status is not-applicable")

    entries = data.get("entries")
    if not isinstance(entries, list):
        errors.append("baseline-manifest.entries must be an array")
        entries = []
    if accepted and not entries:
        errors.append("baseline-manifest.entries must not be empty for accepted state")

    ids: set[str] = set()
    for index, entry in enumerate(entries):
        location = f"baseline-manifest.entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{location} must be an object")
            continue
        entry_id = entry.get("id")
        if not non_empty_string(entry_id):
            errors.append(f"{location}.id is required")
        elif entry_id in ids:
            errors.append(f"{location}.id is duplicated: {entry_id}")
        else:
            ids.add(str(entry_id))
        if entry.get("kind") not in BASELINE_KINDS:
            errors.append(
                f"{location}.kind must be approved-reference or asserted-golden; capture-only is not a baseline"
            )
        for field in ("surface_id", "state", "target"):
            if not non_empty_string(entry.get(field)):
                errors.append(f"{location}.{field} is required")
        surface_id = entry.get("surface_id")
        if non_empty_string(surface_id) and surface_id not in surface_ids:
            errors.append(f"{location}.surface_id references unknown surface {surface_id!r}")
        if not isinstance(entry.get("viewport"), dict) and not isinstance(
            entry.get("device_config"), dict
        ):
            errors.append(f"{location} requires viewport or device_config")
        path = project_file(project_root, entry.get("path"), errors, f"{location}.path")
        expected_hash = entry.get("sha256")
        if not isinstance(expected_hash, str) or not SHA256_RE.fullmatch(expected_hash):
            errors.append(f"{location}.sha256 must be a lowercase SHA-256 digest")
        elif path is not None and path.is_file() and sha256_file(path) != expected_hash:
            errors.append(f"{location}.sha256 does not match {entry.get('path')}")
        if entry.get("kind") == "asserted-golden":
            project_file(
                project_root,
                entry.get("assertion_source"),
                errors,
                f"{location}.assertion_source",
            )

    unknown_mapped = mapped_baseline_ids - ids
    if unknown_mapped:
        errors.append(
            "source-map references baseline IDs missing from baseline manifest: "
            + ", ".join(sorted(unknown_mapped))
        )
    unmapped = ids - mapped_baseline_ids
    if accepted and unmapped:
        errors.append(
            "accepted baseline entries are not mapped to a surface: " + ", ".join(sorted(unmapped))
        )


def validate_project(
    project_root: Path,
    mode: str,
    contract_manifest_relative: str,
    source_map_relative: str,
    baseline_manifest_relative: str,
    approval_id: str | None = None,
) -> list[str]:
    project_root = project_root.resolve()
    errors: list[str] = []
    contract_path = project_file(
        project_root,
        contract_manifest_relative,
        errors,
        "contract manifest path",
    )
    baseline_path = project_file(
        project_root,
        baseline_manifest_relative,
        errors,
        "baseline manifest path",
    )
    if contract_path is None or baseline_path is None:
        return errors
    contract = load_json(contract_path, errors, "contract manifest")
    baseline = load_json(baseline_path, errors, "baseline manifest")
    if contract is None or baseline is None:
        return errors

    accepted, mapped_source_path = validate_contract_manifest(
        contract,
        project_root,
        errors,
        freeze=mode == "freeze",
    )
    source_path = mapped_source_path or project_file(
        project_root,
        source_map_relative,
        errors,
        "source map path",
    )
    if source_path is None:
        return errors
    source_map = load_json(source_path, errors, "source map")
    if source_map is None:
        return errors
    surfaces, mapped_baselines = validate_source_map(
        source_map,
        project_root,
        errors,
        accepted=accepted or mode == "freeze",
    )
    validate_baseline_manifest(
        baseline,
        project_root,
        errors,
        freeze=mode == "freeze",
        surface_ids=surfaces,
        mapped_baseline_ids=mapped_baselines,
        approval_id=approval_id,
    )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate product design contract, source-map, and baseline manifests."
    )
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--mode", choices=("draft", "freeze"), default="draft")
    parser.add_argument(
        "--contract-manifest", default="design/contract/manifest.json"
    )
    parser.add_argument("--source-map", default="design/contract/source-map.json")
    parser.add_argument(
        "--baseline-manifest", default="design/baselines/manifest.json"
    )
    parser.add_argument(
        "--approval-id",
        help="Explicit human approval ID authorized by the router; required in freeze mode",
    )
    args = parser.parse_args()

    errors = validate_project(
        args.project_root,
        args.mode,
        args.contract_manifest,
        args.source_map,
        args.baseline_manifest,
        args.approval_id,
    )
    if errors:
        print("Design contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Design contract validation passed ({args.mode} mode).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
