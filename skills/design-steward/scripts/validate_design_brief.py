#!/usr/bin/env python3
"""Validate a Design Steward Design Brief for direction-generation readiness."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ALLOWED_CONSTRAINTS = {"Fixed", "Challengeable", "Open", "Blocking Unknown"}
ALLOWED_MODES = {"Evolution", "From-scratch"}
REQUIRED_HARD_GATES = {
    "accessibility",
    "content truth",
    "privacy and participant welfare",
    "ethical ux and safety",
    "provenance and ai use",
}
PLACEHOLDER = re.compile(r"(?:\bTBD\b|\bTODO\b|\[\s*replace\b)", re.IGNORECASE)

REQUIRED_TOP_LEVEL = {
    "schema_version",
    "record_type",
    "brief_id",
    "version",
    "status",
    "mode",
    "authority",
    "objectives",
    "users_and_contexts",
    "evidence",
    "evidence_gap_rationale",
    "representative_content",
    "accessibility_ethics_privacy_legal_safety",
    "constraint_ledger",
    "delivery_constraints",
    "comparison_contract",
    "governance",
    "permissions",
    "working_assumptions",
    "blocking_unknowns",
    "clean_room",
    "change_control",
    "approval",
}

NON_EMPTY_STRINGS = (
    "schema_version",
    "brief_id",
    "version",
    "mode",
    "authority.product_owner",
    "authority.commissioned_decision",
    "accessibility_ethics_privacy_legal_safety.accessibility_standard",
    "comparison_contract.validation_claim_rule",
    "comparison_contract.tie_and_uncertainty_handling",
    "governance.participant_contact_authority",
    "governance.consequential_write_authority",
    "permissions.product_access",
    "clean_room.engagement_workspace",
    "clean_room.portable_core_writeback",
)

APPROVAL_STRINGS = (
    "approval.product_owner",
    "approval.approved_at",
    "approval.approved_scope",
)

NON_EMPTY_LISTS = (
    "objectives.desired_outcomes",
    "objectives.non_goals",
    "users_and_contexts.target_users",
    "users_and_contexts.contexts",
    "users_and_contexts.priority_journeys",
    "representative_content.canonical_terminology",
    "representative_content.content_samples",
    "representative_content.data_conditions",
    "representative_content.critical_states",
    "constraint_ledger",
    "comparison_contract.rubric",
    "comparison_contract.evidence_thresholds",
    "comparison_contract.hard_gates",
    "governance.human_gates",
    "governance.decision_owners",
    "clean_room.forbidden_context",
    "change_control.material_change_triggers",
)

REQUIRED_PERMISSION_LISTS = (
    "allowed_sources",
    "allowed_assets",
    "allowed_tools",
    "allowed_data",
    "external_writes",
)


def get_path(data: dict[str, Any], dotted_path: str) -> Any:
    value: Any = data
    for part in dotted_path.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def contains_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER.search(value))
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    return False


def require_record_fields(
    records: Any,
    label: str,
    fields: tuple[str, ...],
    errors: list[str],
) -> None:
    if not isinstance(records, list):
        errors.append(f"{label} must be an array")
        return
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"{label}[{index}] must be an object")
            continue
        for field in fields:
            value = record.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}[{index}].{field} must be a non-empty string")


def validate_brief(data: Any, allow_draft: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["brief root must be a JSON object"]

    for field in sorted(REQUIRED_TOP_LEVEL - data.keys()):
        errors.append(f"missing required field: {field}")

    if data.get("record_type") != "design-brief":
        errors.append("record_type must be 'design-brief'")
    if data.get("mode") not in ALLOWED_MODES:
        errors.append("mode must be 'Evolution' or 'From-scratch'")

    if not allow_draft and data.get("status") != "Approved":
        errors.append("status must be 'Approved' before direction generation")
    elif allow_draft and data.get("status") not in {"Draft", "Approved", "Superseded"}:
        errors.append("status must be Draft, Approved, or Superseded")

    for path in NON_EMPTY_STRINGS:
        value = get_path(data, path)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path} must be a non-empty string")

    if not allow_draft:
        for path in APPROVAL_STRINGS:
            value = get_path(data, path)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path} must be a non-empty string")

    for path in NON_EMPTY_LISTS:
        value = get_path(data, path)
        if not isinstance(value, list) or not value:
            errors.append(f"{path} must be a non-empty array")

    evidence = data.get("evidence")
    evidence_gap = data.get("evidence_gap_rationale")
    if not isinstance(evidence, list):
        errors.append("evidence must be an array")
    elif not evidence and (not isinstance(evidence_gap, str) or not evidence_gap.strip()):
        errors.append("supply evidence or a non-empty evidence_gap_rationale")
    elif evidence:
        require_record_fields(
            evidence,
            "evidence",
            (
                "id",
                "claim",
                "level",
                "source",
                "observed_at",
                "provenance",
                "confidence",
                "access_class",
                "limitations",
            ),
            errors,
        )

    permissions = data.get("permissions")
    if not isinstance(permissions, dict):
        errors.append("permissions must be an object")
    else:
        for field in REQUIRED_PERMISSION_LISTS:
            if not isinstance(permissions.get(field), list):
                errors.append(f"permissions.{field} must be an array")

    blockers = data.get("blocking_unknowns")
    if not isinstance(blockers, list):
        errors.append("blocking_unknowns must be an array")
    elif blockers and not allow_draft:
        errors.append("blocking_unknowns must be empty before direction generation")

    constraints = data.get("constraint_ledger")
    require_record_fields(
        constraints,
        "constraint_ledger",
        ("id", "statement", "classification", "rationale", "source", "decision_owner"),
        errors,
    )
    if isinstance(constraints, list):
        for index, constraint in enumerate(constraints):
            if not isinstance(constraint, dict):
                continue
            classification = constraint.get("classification")
            if classification not in ALLOWED_CONSTRAINTS:
                errors.append(
                    f"constraint_ledger[{index}].classification must be one of "
                    + ", ".join(sorted(ALLOWED_CONSTRAINTS))
                )
            elif classification == "Blocking Unknown" and not allow_draft:
                errors.append(
                    f"constraint_ledger[{index}] is a Blocking Unknown and prevents generation"
                )

    require_record_fields(
        data.get("working_assumptions"),
        "working_assumptions",
        ("id", "statement", "rationale", "risk", "owner", "evidence_plan", "review_or_expiry"),
        errors,
    )

    hard_gates = get_path(data, "comparison_contract.hard_gates")
    if isinstance(hard_gates, list):
        normalized = {item.strip().lower() for item in hard_gates if isinstance(item, str)}
        missing_gates = REQUIRED_HARD_GATES - normalized
        if missing_gates:
            errors.append("comparison_contract.hard_gates is missing: " + ", ".join(sorted(missing_gates)))

    approval_owner = get_path(data, "approval.product_owner")
    authority_owner = get_path(data, "authority.product_owner")
    if (
        isinstance(approval_owner, str)
        and isinstance(authority_owner, str)
        and approval_owner.strip()
        and authority_owner.strip()
        and approval_owner.strip() != authority_owner.strip()
    ):
        errors.append("approval.product_owner must match authority.product_owner")

    if contains_placeholder(data):
        errors.append("brief contains a TBD, TODO, or [replace ...] placeholder")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a Design Steward Design Brief for direction-generation readiness."
    )
    parser.add_argument("brief", type=Path, help="Path to design-brief.json")
    parser.add_argument(
        "--allow-draft",
        action="store_true",
        help="Validate draft structure without requiring Approved status or zero blockers.",
    )
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable result.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.brief.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Design Brief not found: {args.brief}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as error:
        print(f"Cannot read Design Brief: {error}", file=sys.stderr)
        return 2

    errors = validate_brief(data, allow_draft=args.allow_draft)
    result = {
        "brief": str(args.brief),
        "generation_ready": not errors and not args.allow_draft,
        "structurally_valid_draft": not errors if args.allow_draft else None,
        "errors": errors,
    }
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    elif errors:
        print("Design Brief is not generation-ready:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    elif args.allow_draft:
        print("Design Brief draft structure is valid; Product Owner approval is still required.")
    else:
        print("Design Brief is structurally generation-ready; recorded approval must still be verified.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
