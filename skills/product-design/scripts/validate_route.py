#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "assets" / "route-contract.json"
VALID_MODES = {"atomic", "pipeline", "resume", "reroute"}
VALID_HANDOFF_STATUSES = {"complete", "needs-owner", "blocked", "failed"}
VALID_MUTATION_AUTHORITIES = {
    "read-only",
    "design-artifacts-only",
    "production-bounded",
    "accept-freeze",
}
VALID_CONTEXT_PLATFORMS = {"web", "native-mobile", "shared-web-wrapper"}
VALID_CONTEXT_CLAIMS = {
    "visual-acceptance",
    "accessibility-acceptance",
    "release",
    "physical-device",
    "representative-user",
}
GATE_PHASES = {
    "A": "discovery",
    "B": "direction",
    "C": "prototype",
    "D": "review",
    "E": "accept-freeze",
    "F": "review",
}
IMPLEMENTATION_ENTRY_BASES = {"gate-c-approved", "bounded-reviewed-slice"}
PRODUCTION_WORKERS = {"product-design-implementation", "product-design-change"}
NO_PRODUCTION_MUTATION_WORKERS = {
    "product-design-discovery",
    "product-design-direction",
    "product-design-contract",
    "product-design-prototype",
    "product-design-review",
}
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"missing file: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}:{error.lineno}: invalid JSON: {error.msg}") from error


def validate_toolchain_for_execution(toolchain: dict[str, Any]) -> list[str]:
    """Run the sibling capability validator without relying on caller import paths."""

    validator_path = ROOT / "scripts" / "validate_toolchain.py"
    spec = importlib.util.spec_from_file_location("product_design_validate_toolchain", validator_path)
    if spec is None or spec.loader is None:
        return [f"route context: cannot load toolchain validator at {validator_path}"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_toolchain(toolchain, for_execution=True)


def require_fields(record: dict[str, Any], fields: tuple[str, ...], label: str) -> list[str]:
    return [f"{label}: missing field {field!r}" for field in fields if field not in record]


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_sha256(value: object) -> bool:
    return isinstance(value, str) and bool(SHA256_RE.fullmatch(value))


def validate_string_array(value: object, location: str, *, allow_empty: bool = True) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, list) or not all(non_empty_string(item) for item in value):
        return [f"{location} must be an array of non-empty strings"]
    if not allow_empty and not value:
        errors.append(f"{location} must not be empty")
    if len(value) != len(set(value)):
        errors.append(f"{location} must not contain duplicates")
    return errors


def validate_accepted_inputs(value: object) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    expected: dict[str, str] = {}
    if not isinstance(value, list):
        return ["routing envelope: accepted_inputs must be an array"], expected
    for index, item in enumerate(value):
        location = f"routing envelope: accepted_inputs[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{location} must be an object")
            continue
        input_id = item.get("id")
        if not non_empty_string(input_id):
            errors.append(f"{location}.id must be a non-empty string")
            continue
        if input_id in expected or input_id == "original_prompt":
            errors.append(f"{location}.id is duplicated or reserved: {input_id!r}")
        if not non_empty_string(item.get("path")):
            errors.append(f"{location}.path must be a non-empty string")
        digest = item.get("sha256")
        if not valid_sha256(digest):
            errors.append(f"{location}.sha256 must be a lowercase SHA-256 digest")
        else:
            expected[str(input_id)] = str(digest)
    return errors, expected


def phase_for_worker(worker: str, *, accept_freeze: bool) -> str:
    if worker == "product-design-contract" and accept_freeze:
        return "accept-freeze"
    return worker.removeprefix("product-design-")


def validate_route_context(
    envelope: dict[str, Any], toolchain: dict[str, Any], *, for_execution: bool = False
) -> list[str]:
    """Bind a routed worker and owner gate to the exact preflight profile used for it."""

    errors: list[str] = []
    profile = toolchain.get("profile")
    if not isinstance(profile, dict):
        return ["route context: toolchain.profile must be an object"]

    phase = profile.get("phase")
    if not non_empty_string(phase):
        errors.append("route context: toolchain.profile.phase must be a non-empty string")

    envelope_platform_values = envelope.get("platforms")
    profile_platform_values = profile.get("platforms")
    envelope_platform_errors = validate_string_array(
        envelope_platform_values, "route context: envelope.platforms"
    )
    profile_platform_errors = validate_string_array(
        profile_platform_values, "route context: toolchain.profile.platforms"
    )
    errors.extend(envelope_platform_errors)
    errors.extend(profile_platform_errors)

    envelope_platforms = (
        set(envelope_platform_values) if not envelope_platform_errors else set()
    )
    profile_platforms = set(profile_platform_values) if not profile_platform_errors else set()
    invalid_envelope_platforms = sorted(envelope_platforms - VALID_CONTEXT_PLATFORMS)
    if invalid_envelope_platforms:
        errors.append(
            "route context: envelope.platforms contains unsupported values: "
            + ", ".join(invalid_envelope_platforms)
        )
    invalid_profile_platforms = sorted(profile_platforms - VALID_CONTEXT_PLATFORMS)
    if invalid_profile_platforms:
        errors.append(
            "route context: toolchain.profile.platforms contains unsupported values: "
            + ", ".join(invalid_profile_platforms)
        )

    claim_values = profile.get("claims")
    claim_errors = validate_string_array(
        claim_values, "route context: toolchain.profile.claims"
    )
    errors.extend(claim_errors)
    claims = set(claim_values) if not claim_errors else set()
    invalid_claims = sorted(claims - VALID_CONTEXT_CLAIMS)
    if invalid_claims:
        errors.append(
            "route context: toolchain.profile.claims contains unsupported values: "
            + ", ".join(invalid_claims)
        )

    if not for_execution:
        return errors

    envelope_phase = envelope.get("current_phase")
    if phase != envelope_phase:
        errors.append(
            "route context: toolchain.profile.phase must exactly match "
            f"envelope.current_phase {envelope_phase!r}"
        )
    if profile_platforms != envelope_platforms:
        errors.append(
            "route context: toolchain.profile.platforms must exactly match envelope.platforms"
        )

    gate = envelope.get("owner_gate")
    expected_gate_phase = GATE_PHASES.get(gate)
    if expected_gate_phase is not None and envelope_phase != expected_gate_phase:
        errors.append(
            f"route context: Gate {gate} is valid only for phase {expected_gate_phase!r}"
        )
    if gate in {"B", "C"} and not envelope_platforms:
        errors.append(f"route context: Gate {gate} requires at least one platform")
    if gate == "D":
        required_claims = {"visual-acceptance", "accessibility-acceptance"}
        missing_claims = sorted(required_claims - claims)
        if missing_claims:
            errors.append(
                "route context: Gate D requires toolchain claims "
                + ", ".join(missing_claims)
            )
    if gate == "F" and not claims.intersection({"release", "representative-user"}):
        errors.append(
            "route context: Gate F requires a release or representative-user claim"
        )
    return errors


def validate_envelope(envelope: dict[str, Any], contract: dict[str, Any]) -> list[str]:
    errors = require_fields(
        envelope,
        (
            "schema_version",
            "request_id",
            "original_prompt_sha256",
            "route",
            "route_reason",
            "mode",
            "current_phase",
            "platforms",
            "mutation_authority",
            "accepted_inputs",
            "toolchain_record",
            "degradation_confirmation_ids",
            "writes_allowed",
            "protected_paths",
            "stop_condition",
            "owner_gate",
            "implementation_entry_basis",
            "implementation_entry_approval_id",
            "baseline_updates_allowed",
            "accept_freeze_approval_id",
        ),
        "routing envelope",
    )
    if envelope.get("schema_version") != "1.0.0":
        errors.append("routing envelope: schema_version must equal '1.0.0'")
    if not non_empty_string(envelope.get("request_id")):
        errors.append("routing envelope: request_id must be a non-empty string")
    if not valid_sha256(envelope.get("original_prompt_sha256")):
        errors.append("routing envelope: original_prompt_sha256 must be a lowercase SHA-256 digest")
    if not non_empty_string(envelope.get("route_reason")):
        errors.append("routing envelope: route_reason must be a non-empty string")
    if not non_empty_string(envelope.get("stop_condition")):
        errors.append("routing envelope: stop_condition must be a non-empty string")
    if not non_empty_string(envelope.get("toolchain_record")):
        errors.append("routing envelope: toolchain_record must be a non-empty path")

    workers = set(contract.get("workers", []))
    transitions = contract.get("allowed_transitions", {})
    route = envelope.get("route")
    if not isinstance(route, list) or not route:
        errors.append("routing envelope: route must be a non-empty array")
        route = []
    for worker in route:
        if worker not in workers:
            errors.append(f"routing envelope: unknown worker {worker!r}")
    for current, following in zip(route, route[1:]):
        if following not in transitions.get(current, []):
            errors.append(f"routing envelope: invalid transition {current!r} -> {following!r}")

    if envelope.get("mode") not in VALID_MODES:
        errors.append(f"routing envelope: mode must be one of {sorted(VALID_MODES)}")
    authority = envelope.get("mutation_authority")
    if authority not in VALID_MUTATION_AUTHORITIES:
        errors.append(
            "routing envelope: mutation_authority must be one of "
            + str(sorted(VALID_MUTATION_AUTHORITIES))
        )
    errors.extend(
        validate_string_array(envelope.get("writes_allowed"), "routing envelope: writes_allowed")
    )
    errors.extend(
        validate_string_array(envelope.get("protected_paths"), "routing envelope: protected_paths")
    )
    errors.extend(
        validate_string_array(envelope.get("platforms"), "routing envelope: platforms")
    )
    errors.extend(
        validate_string_array(
            envelope.get("degradation_confirmation_ids"),
            "routing envelope: degradation_confirmation_ids",
        )
    )
    accepted_errors, _ = validate_accepted_inputs(envelope.get("accepted_inputs"))
    errors.extend(accepted_errors)

    baseline_updates = envelope.get("baseline_updates_allowed")
    if not isinstance(baseline_updates, bool):
        errors.append("routing envelope: baseline_updates_allowed must be boolean")
        baseline_updates = False
    if baseline_updates:
        if route != ["product-design-contract"]:
            errors.append("routing envelope: baseline updates require contract-only accept-freeze route")
        if authority != "accept-freeze":
            errors.append("routing envelope: baseline updates require accept-freeze mutation authority")
        if not non_empty_string(envelope.get("accept_freeze_approval_id")):
            errors.append("routing envelope: baseline updates require accept_freeze_approval_id")
    else:
        if envelope.get("accept_freeze_approval_id") is not None:
            errors.append("routing envelope: approval ID is only valid when baseline updates are allowed")
        if authority == "accept-freeze":
            errors.append("routing envelope: accept-freeze authority requires baseline updates")

    gate = envelope.get("owner_gate")
    if gate is not None and gate not in set(contract.get("human_gates", [])):
        errors.append(f"routing envelope: unknown owner gate {gate!r}")

    if route:
        current_worker = route[0]
        expected_phase = phase_for_worker(current_worker, accept_freeze=bool(baseline_updates))
        if envelope.get("current_phase") != expected_phase:
            errors.append(
                f"routing envelope: current_phase must be {expected_phase!r} for {current_worker!r}"
            )
        if current_worker == "product-design-review":
            if authority != "read-only":
                errors.append("routing envelope: review requires read-only mutation authority")
            if envelope.get("writes_allowed") != []:
                errors.append("routing envelope: review writes_allowed must be empty")
        elif current_worker in PRODUCTION_WORKERS and authority != "production-bounded":
            errors.append(
                f"routing envelope: {current_worker} requires production-bounded mutation authority"
            )
        elif current_worker in NO_PRODUCTION_MUTATION_WORKERS and not baseline_updates:
            if authority not in {"read-only", "design-artifacts-only"}:
                errors.append(
                    f"routing envelope: {current_worker} cannot use {authority!r} mutation authority"
                )

        basis = envelope.get("implementation_entry_basis")
        approval_id = envelope.get("implementation_entry_approval_id")
        if current_worker == "product-design-implementation":
            if basis not in IMPLEMENTATION_ENTRY_BASES:
                errors.append(
                    "routing envelope: implementation requires gate-c-approved or "
                    "bounded-reviewed-slice entry basis"
                )
            if not non_empty_string(approval_id):
                errors.append(
                    "routing envelope: implementation requires implementation_entry_approval_id"
                )
        elif basis is not None or approval_id is not None:
            errors.append(
                "routing envelope: implementation entry fields are only valid when implementation is current"
            )
    return errors


def validate_handoff(
    handoff: dict[str, Any], envelope: dict[str, Any], contract: dict[str, Any] | None = None
) -> list[str]:
    if contract is None:
        contract = load_json(DEFAULT_CONTRACT)
    errors = require_fields(
        handoff,
        (
            "schema_version",
            "request_id",
            "worker",
            "status",
            "input_hashes",
            "artifacts_created_or_changed",
            "production_mutations",
            "evidence",
            "missing_evidence",
            "degraded_capabilities",
            "baseline_changed",
            "gate",
            "recommended_next_worker",
            "exact_next_action",
        ),
        "worker handoff",
    )
    if handoff.get("schema_version") != "1.0.0":
        errors.append("worker handoff: schema_version must equal '1.0.0'")
    if handoff.get("request_id") != envelope.get("request_id"):
        errors.append("worker handoff: request_id does not match routing envelope")

    workers = set(contract.get("workers", []))
    transitions = contract.get("allowed_transitions", {})
    route = envelope.get("route", [])
    worker = handoff.get("worker")
    if worker not in workers:
        errors.append(f"worker handoff: unknown worker {worker!r}")
    if route and worker != route[0]:
        errors.append("worker handoff: worker is not the current routed worker")

    status = handoff.get("status")
    if status not in VALID_HANDOFF_STATUSES:
        errors.append(f"worker handoff: status must be one of {sorted(VALID_HANDOFF_STATUSES)}")
    for field in (
        "artifacts_created_or_changed",
        "production_mutations",
        "evidence",
        "missing_evidence",
        "degraded_capabilities",
    ):
        if not isinstance(handoff.get(field), list):
            errors.append(f"worker handoff: {field} must be an array")
    if not non_empty_string(handoff.get("exact_next_action")):
        errors.append("worker handoff: exact_next_action must be a non-empty string")

    input_hashes = handoff.get("input_hashes")
    if not isinstance(input_hashes, dict):
        errors.append("worker handoff: input_hashes must be an object")
        input_hashes = {}
    else:
        for input_id, digest in input_hashes.items():
            if not non_empty_string(input_id) or not valid_sha256(digest):
                errors.append(
                    f"worker handoff: input_hashes[{input_id!r}] must be a lowercase SHA-256 digest"
                )
    expected_hashes = {"original_prompt": envelope.get("original_prompt_sha256")}
    accepted_errors, accepted_hashes = validate_accepted_inputs(envelope.get("accepted_inputs", []))
    errors.extend(accepted_errors)
    expected_hashes.update(accepted_hashes)
    for input_id, expected in expected_hashes.items():
        if input_hashes.get(input_id) != expected:
            errors.append(
                f"worker handoff: input hash does not match routing envelope for {input_id!r}"
            )

    baseline_changed = handoff.get("baseline_changed")
    if not isinstance(baseline_changed, bool):
        errors.append("worker handoff: baseline_changed must be boolean")
    if baseline_changed and not envelope.get("baseline_updates_allowed"):
        errors.append("worker handoff: baseline changed outside explicit accept-freeze authority")
    if baseline_changed and worker != "product-design-contract":
        errors.append("worker handoff: only product-design-contract may freeze baselines")
    if baseline_changed and status != "complete":
        errors.append("worker handoff: baseline change is valid only for a completed accept-freeze")

    production_mutations = handoff.get("production_mutations", [])
    if worker in NO_PRODUCTION_MUTATION_WORKERS and production_mutations:
        errors.append(f"worker handoff: {worker} must not report production mutations")
    if production_mutations and envelope.get("mutation_authority") != "production-bounded":
        errors.append("worker handoff: production mutations exceed routing authority")

    gate = handoff.get("gate")
    known_gates = set(contract.get("human_gates", []))
    if gate is not None and gate not in known_gates:
        errors.append(f"worker handoff: unknown gate {gate!r}")
    if gate is not None and gate != envelope.get("owner_gate"):
        errors.append("worker handoff: gate does not match routing envelope owner_gate")
    if gate is not None and status != "needs-owner":
        errors.append("worker handoff: a non-null gate requires needs-owner status")
    if gate is not None and isinstance(handoff.get("evidence"), list) and not handoff["evidence"]:
        errors.append("worker handoff: a non-null gate requires non-empty evidence")

    recommendation = handoff.get("recommended_next_worker")
    if recommendation is not None:
        if recommendation not in workers:
            errors.append(f"worker handoff: unknown recommended_next_worker {recommendation!r}")
        elif recommendation not in transitions.get(worker, []):
            errors.append(
                f"worker handoff: invalid recommended transition {worker!r} -> {recommendation!r}"
            )
    if status in {"blocked", "failed"} and recommendation is not None:
        errors.append("worker handoff: blocked or failed work cannot recommend a successor")
    if len(route) > 1 and status not in {"blocked", "failed"}:
        expected_next = route[1]
        if recommendation != expected_next:
            errors.append(
                "worker handoff: recommended_next_worker must match declared next route item "
                f"{expected_next!r}"
            )

    confirmations = set(envelope.get("degradation_confirmation_ids", []))
    degraded = handoff.get("degraded_capabilities", [])
    if isinstance(degraded, list):
        for index, item in enumerate(degraded):
            location = f"worker handoff: degraded_capabilities[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{location} must be an object")
                continue
            for field in ("id", "confirmation_id", "limitation"):
                if not non_empty_string(item.get(field)):
                    errors.append(f"{location}.{field} must be a non-empty string")
            if item.get("confirmation_id") not in confirmations:
                errors.append(f"{location}.confirmation_id is not authorized by the routing envelope")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate product-design routing and worker handoffs.")
    parser.add_argument("envelope", type=Path)
    parser.add_argument("--handoff", type=Path)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--toolchain", type=Path)
    parser.add_argument("--for-execution", action="store_true")
    args = parser.parse_args()
    try:
        contract = load_json(args.contract)
        envelope = load_json(args.envelope)
        errors = validate_envelope(envelope, contract)
        if args.for_execution and args.toolchain is None:
            errors.append("route context: --toolchain is required with --for-execution")
        elif args.toolchain is not None:
            toolchain = load_json(args.toolchain)
            errors.extend(
                validate_route_context(
                    envelope,
                    toolchain,
                    for_execution=args.for_execution,
                )
            )
            if args.for_execution:
                errors.extend(validate_toolchain_for_execution(toolchain))
        if args.handoff:
            errors.extend(validate_handoff(load_json(args.handoff), envelope, contract))
    except ValueError as error:
        errors = [str(error)]
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, "route": envelope["route"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
