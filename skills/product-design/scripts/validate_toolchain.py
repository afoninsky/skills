#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

VALID_REQUIREMENTS = {"required", "conditional", "optional"}
VALID_STATUSES = {
    "available",
    "missing-blocking",
    "missing-degradable",
    "unknown",
    "not-applicable",
}
VALID_PHASES = {
    "unselected",
    "discovery",
    "direction",
    "contract",
    "prototype",
    "implementation",
    "change",
    "review",
    "accept-freeze",
}
VALID_PLATFORMS = {"web", "native-mobile", "shared-web-wrapper"}
VALID_CLAIMS = {
    "visual-acceptance",
    "accessibility-acceptance",
    "release",
    "physical-device",
    "representative-user",
}

PHASE_REQUIRED_CAPABILITIES = {
    "discovery": {"project-artifact-access"},
    "direction": {"versioned-candidate-isolation", "matched-render-and-capture"},
    "contract": {
        "versioning-and-rollback",
        "scope-and-hash-validation",
        "semantic-style-source",
    },
    "prototype": {"versioned-prototype-isolation", "target-render-and-capture"},
    "implementation": {
        "versioning-and-rollback",
        "approved-input-identity",
        "target-build-toolchain",
    },
    "change": {"versioning-and-rollback", "scope-and-hash-validation"},
    "review": {"versioning-and-rollback"},
    "accept-freeze": {
        "versioning-and-rollback",
        "scope-and-hash-validation",
        "semantic-style-source",
    },
}

PLATFORM_CAPABILITIES = {
    "web": {
        "runtime": "web-runtime-and-visual-regression",
        "accessibility": "web-accessibility",
    },
    "native-mobile": {
        "runtime": "mobile-runtime-and-visual-regression",
        "accessibility": "native-accessibility",
    },
}

REPRESENTATIVE_USER_CAPABILITY = {
    "discovery": "representative-participant-research",
    "direction": "representative-participant-comparison",
    "prototype": "representative-participant-evidence",
}

HARD_GATE_CAPABILITIES = {
    "matched-render-and-capture",
    "target-render-and-capture",
    "web-runtime-and-visual-regression",
    "mobile-runtime-and-visual-regression",
    "web-accessibility",
    "native-accessibility",
    "physical-device-evidence",
    "representative-user-evidence",
    "representative-participant-research",
    "representative-participant-comparison",
    "representative-participant-evidence",
}

PLATFORM_SELECTION_REQUIRED_PHASES = {
    "direction",
    "contract",
    "prototype",
    "implementation",
    "change",
    "accept-freeze",
}
RUNTIME_AND_ACCESSIBILITY_REQUIRED_PHASES = {
    "implementation",
    "change",
    "accept-freeze",
}
MAX_PREFLIGHT_AGE = timedelta(hours=4)
MAX_FUTURE_CLOCK_SKEW = timedelta(minutes=5)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"missing file: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}:{error.lineno}: invalid JSON: {error.msg}") from error


def valid_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        checked_at = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    if checked_at.tzinfo is None or checked_at.utcoffset() is None:
        return False
    checked_at = checked_at.astimezone(timezone.utc)
    current_time = datetime.now(timezone.utc)
    return (
        current_time - MAX_PREFLIGHT_AGE
        <= checked_at
        <= current_time + MAX_FUTURE_CLOCK_SKEW
    )


def string_set(value: Any, label: str, valid_values: set[str], errors: list[str]) -> set[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        errors.append(f"toolchain.profile.{label} must be an array of strings")
        return set()
    if len(value) != len(set(value)):
        errors.append(f"toolchain.profile.{label} must not contain duplicates")
    invalid = sorted(set(value) - valid_values)
    if invalid:
        errors.append(
            f"toolchain.profile.{label} contains unsupported values: {', '.join(invalid)}"
        )
    return set(value) & valid_values


def expanded_platforms(platforms: set[str]) -> set[str]:
    expanded = set(platforms)
    if "shared-web-wrapper" in expanded:
        expanded.update({"web", "native-mobile"})
    return expanded


def profile_requirements(record: dict[str, Any], for_execution: bool) -> tuple[set[str], set[str], list[str]]:
    errors: list[str] = []
    profile = record.get("profile")
    if not isinstance(profile, dict):
        if for_execution:
            errors.append("toolchain.profile is required for execution")
        return set(), set(), errors

    phase = profile.get("phase")
    if not isinstance(phase, str) or phase not in VALID_PHASES:
        errors.append(f"toolchain.profile.phase must be one of {sorted(VALID_PHASES)}")
        phase = "unselected"
    if for_execution and phase == "unselected":
        errors.append("toolchain.profile.phase must select a worker phase before execution")

    platforms = string_set(profile.get("platforms"), "platforms", VALID_PLATFORMS, errors)
    claims = string_set(profile.get("claims"), "claims", VALID_CLAIMS, errors)
    platforms = expanded_platforms(platforms)

    if for_execution and phase in PLATFORM_SELECTION_REQUIRED_PHASES and not platforms:
        errors.append(f"toolchain.profile.platforms must not be empty for phase {phase!r}")
    if for_execution and claims.intersection(
        {"visual-acceptance", "accessibility-acceptance", "release"}
    ) and not platforms:
        errors.append("toolchain.profile.platforms is required for the selected acceptance claim")

    required = set(PHASE_REQUIRED_CAPABILITIES.get(str(phase), set()))
    hard_gates: set[str] = set()

    needs_runtime = phase in RUNTIME_AND_ACCESSIBILITY_REQUIRED_PHASES or bool(
        claims.intersection({"visual-acceptance", "release"})
    )
    needs_accessibility = phase in RUNTIME_AND_ACCESSIBILITY_REQUIRED_PHASES or bool(
        claims.intersection({"accessibility-acceptance", "release"})
    )
    for platform in platforms.intersection(PLATFORM_CAPABILITIES):
        if needs_runtime:
            capability_id = PLATFORM_CAPABILITIES[platform]["runtime"]
            required.add(capability_id)
            hard_gates.add(capability_id)
        if needs_accessibility:
            capability_id = PLATFORM_CAPABILITIES[platform]["accessibility"]
            required.add(capability_id)
            hard_gates.add(capability_id)

    if "physical-device" in claims:
        required.add("physical-device-evidence")
        hard_gates.add("physical-device-evidence")
    if "representative-user" in claims:
        capability_id = REPRESENTATIVE_USER_CAPABILITY.get(
            str(phase), "representative-user-evidence"
        )
        required.add(capability_id)
        hard_gates.add(capability_id)

    hard_gates.update(required.intersection(HARD_GATE_CAPABILITIES))
    return required, hard_gates, errors


def validate_toolchain(record: dict[str, Any], for_execution: bool = False) -> list[str]:
    required_capabilities, active_hard_gates, errors = profile_requirements(record, for_execution)
    if record.get("schema_version") != "1.0.0":
        errors.append("toolchain.schema_version must equal '1.0.0'")
    if for_execution and not valid_timestamp(record.get("checked_at")):
        errors.append(
            "toolchain.checked_at must be timezone-aware, no more than 4 hours old, "
            "and no more than 5 minutes ahead for execution"
        )
    capabilities = record.get("capabilities")
    if not isinstance(capabilities, list):
        return errors + ["toolchain: capabilities must be an array"]
    seen: set[str] = set()
    by_id: dict[str, dict[str, Any]] = {}
    for index, capability in enumerate(capabilities):
        label = f"toolchain.capabilities[{index}]"
        if not isinstance(capability, dict):
            errors.append(f"{label}: must be an object")
            continue
        capability_id = capability.get("id")
        if not isinstance(capability_id, str) or not capability_id.strip():
            errors.append(f"{label}: id is required")
        elif capability_id in seen:
            errors.append(f"{label}: duplicate id {capability_id!r}")
        else:
            seen.add(capability_id)
            by_id[capability_id] = capability
        requirement = capability.get("requirement")
        status = capability.get("status")
        if requirement not in VALID_REQUIREMENTS:
            errors.append(f"{label}: requirement must be one of {sorted(VALID_REQUIREMENTS)}")
        if status not in VALID_STATUSES:
            errors.append(f"{label}: status must be one of {sorted(VALID_STATUSES)}")
            continue
        if status == "available" and not capability.get("evidence"):
            errors.append(f"{label}: available capability requires evidence")
        if status in {"missing-blocking", "missing-degradable"} and not capability.get("degradation"):
            errors.append(f"{label}: missing capability requires a degradation description")
        if status == "not-applicable" and capability.get("confirmation_id"):
            errors.append(f"{label}: not-applicable capability cannot have confirmation_id")
        if status != "missing-degradable" and capability.get("confirmation_id"):
            errors.append(
                f"{label}: confirmation_id is valid only for missing-degradable capability"
            )
        if status == "missing-degradable" and requirement == "required":
            errors.append(f"{label}: required capability cannot be degraded by confirmation")
        if (
            status == "missing-degradable"
            and isinstance(capability_id, str)
            and capability_id in HARD_GATE_CAPABILITIES
        ):
            errors.append(f"{label}: hard-gate capability cannot be degraded by confirmation")
        if for_execution:
            if status in {"missing-blocking", "unknown"}:
                errors.append(f"{label}: status {status!r} does not permit execution")
            if status == "missing-degradable" and not capability.get("confirmation_id"):
                errors.append(f"{label}: degraded execution requires explicit confirmation_id")

    if for_execution:
        for capability_id in sorted(required_capabilities):
            capability = by_id.get(capability_id)
            if capability is None:
                errors.append(
                    f"toolchain profile requires capability {capability_id!r}, but it is omitted"
                )
                continue
            if capability.get("requirement") != "required":
                errors.append(
                    f"toolchain profile requires capability {capability_id!r} to be classified as required"
                )
            if capability.get("status") != "available":
                errors.append(
                    f"toolchain profile requires capability {capability_id!r} to be available for execution"
                )
        for capability_id in sorted(active_hard_gates):
            capability = by_id.get(capability_id)
            if capability is not None and capability.get("status") == "missing-degradable":
                errors.append(
                    f"toolchain profile hard gate {capability_id!r} cannot be waived by confirmation"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a product-design tool capability record.")
    parser.add_argument("toolchain", type=Path)
    parser.add_argument("--for-execution", action="store_true")
    args = parser.parse_args()
    try:
        errors = validate_toolchain(load_json(args.toolchain), for_execution=args.for_execution)
    except ValueError as error:
        errors = [str(error)]
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
