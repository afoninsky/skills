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
ALLOWED_OPERATING_MODES = {"Design-intent grilling", "Autonomous design"}
ALLOWED_ENGAGEMENT_TYPES = {"Evolution", "From-scratch"}
ALLOWED_GRILLING_STATUSES = {"Required", "Completed", "Skipped"}
CONFIRMATION_QUESTION = (
    "Does this brief represent our shared understanding, and may Design Steward "
    "enter autonomous design mode?"
)
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
    "operating_mode",
    "engagement_type",
    "authority",
    "dependency_preflight",
    "grilling",
    "owner_design_intent",
    "shared_understanding",
    "objectives",
    "success_contract",
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
    "operating_mode",
    "engagement_type",
    "authority.system_owner",
    "authority.commissioned_decision",
    "dependency_preflight.required_skill",
    "grilling.base_skill",
    "grilling.required_or_skip_reason",
    "owner_design_intent.commission_and_desired_outcome",
    "owner_design_intent.product_thesis",
    "owner_design_intent.core_user_act",
    "owner_design_intent.first_ten_seconds_hierarchy",
    "success_contract.product_experience_thesis",
    "success_contract.product_idea_to_make_obvious",
    "success_contract.first_visible_artifact_target",
    "success_contract.stopping_point",
    "accessibility_ethics_privacy_legal_safety.accessibility_standard",
    "comparison_contract.validation_claim_rule",
    "comparison_contract.tie_and_uncertainty_handling",
    "comparison_contract.numeric_scoring_policy",
    "governance.participant_contact_authority",
    "governance.consequential_write_authority",
    "permissions.product_access",
    "clean_room.engagement_workspace",
    "clean_room.portable_core_writeback",
)

APPROVAL_STRINGS = (
    "shared_understanding.confirmed_by",
    "shared_understanding.confirmed_at",
    "shared_understanding.authorized_scope",
    "approval.system_owner",
    "approval.approved_at",
    "approval.approved_scope",
)

NON_EMPTY_LISTS = (
    "objectives.desired_outcomes",
    "objectives.non_goals",
    "owner_design_intent.priority_users_roles_and_situations",
    "owner_design_intent.desired_experiential_qualities",
    "owner_design_intent.business_priorities_and_constraints",
    "owner_design_intent.non_negotiables",
    "owner_design_intent.accepted_trade_offs",
    "owner_design_intent.unacceptable_outcomes",
    "owner_design_intent.rejection_criteria",
    "owner_design_intent.owner_originated_preferences",
    "owner_design_intent.steward_recommendations",
    "owner_design_intent.material_disagreements_and_resolutions",
    "owner_design_intent.evidence_assumptions_and_unresolved_uncertainty",
    "owner_design_intent.authorization_boundaries",
    "success_contract.complete_experience_scope",
    "success_contract.professional_quality_bar",
    "success_contract.artifact_iteration_delegation_budget",
    "success_contract.feedback_checkpoint_plan",
    "success_contract.deferred_assurance_plan",
    "users_and_contexts.target_users",
    "users_and_contexts.contexts",
    "users_and_contexts.roles_and_domains",
    "users_and_contexts.priority_journeys",
    "users_and_contexts.priority_handoffs",
    "representative_content.canonical_terminology",
    "representative_content.content_samples",
    "representative_content.data_conditions",
    "representative_content.critical_states",
    "constraint_ledger",
    "comparison_contract.rubric",
    "comparison_contract.professional_quality_criteria",
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

    if data.get("schema_version") != "4.0.0":
        errors.append("schema_version must be '4.0.0'")
    if data.get("record_type") != "design-brief":
        errors.append("record_type must be 'design-brief'")
    if data.get("operating_mode") not in ALLOWED_OPERATING_MODES:
        errors.append(
            "operating_mode must be 'Design-intent grilling' or 'Autonomous design'"
        )
    if data.get("engagement_type") not in ALLOWED_ENGAGEMENT_TYPES:
        errors.append("engagement_type must be 'Evolution' or 'From-scratch'")
    if not allow_draft and data.get("operating_mode") != "Autonomous design":
        errors.append(
            "operating_mode must be 'Autonomous design' before direction generation"
        )

    if not allow_draft and data.get("status") != "Accepted":
        errors.append("status must be 'Accepted' before direction generation")
    elif allow_draft and data.get("status") not in {"Draft", "Accepted", "Superseded"}:
        errors.append("status must be Draft, Accepted, or Superseded")

    for path in NON_EMPTY_STRINGS:
        value = get_path(data, path)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path} must be a non-empty string")

    dependency = data.get("dependency_preflight")
    if not isinstance(dependency, dict):
        errors.append("dependency_preflight must be an object")
    elif not allow_draft:
        if dependency.get("resolved_skill") not in {"grilling", "grill-me"}:
            errors.append(
                "dependency_preflight.resolved_skill must be 'grilling' or 'grill-me'"
            )
        for field in ("version_or_content_hash", "verified_at"):
            value = dependency.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"dependency_preflight.{field} must be a non-empty string"
                )
        if dependency.get("status") != "Available":
            errors.append(
                "dependency_preflight.status must be 'Available' before intake or direction generation"
            )

    if not allow_draft:
        for path in APPROVAL_STRINGS:
            value = get_path(data, path)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path} must be a non-empty string")

    for path in NON_EMPTY_LISTS:
        value = get_path(data, path)
        if not isinstance(value, list) or not value:
            errors.append(f"{path} must be a non-empty array")

    grilling = data.get("grilling")
    if not isinstance(grilling, dict):
        errors.append("grilling must be an object")
    else:
        grilling_status = grilling.get("status")
        if grilling_status not in ALLOWED_GRILLING_STATUSES:
            errors.append("grilling.status must be Required, Completed, or Skipped")
        if not allow_draft and grilling_status not in {"Completed", "Skipped"}:
            errors.append(
                "grilling.status must be Completed or Skipped before direction generation"
            )
        if grilling_status == "Completed":
            skill_identity = grilling.get("base_skill_version_or_hash")
            if not isinstance(skill_identity, str) or not skill_identity.strip():
                errors.append(
                    "grilling.base_skill_version_or_hash must be recorded when grilling is Completed"
                )
            decisions = grilling.get("decision_records")
            if not allow_draft and (not isinstance(decisions, list) or not decisions):
                errors.append(
                    "grilling.decision_records must be non-empty when grilling is Completed"
                )
            elif isinstance(decisions, list):
                require_record_fields(
                    decisions,
                    "grilling.decision_records",
                    (
                        "id",
                        "question",
                        "owner_original_response",
                        "input_class",
                        "steward_recommendation",
                        "agreement_disagreement_evidence_gaps_and_consequences",
                        "resolution",
                    ),
                    errors,
                )
        if grilling_status == "Skipped":
            existing_brief = grilling.get("existing_confirmed_owner_design_brief")
            if not isinstance(existing_brief, str) or not existing_brief.strip():
                errors.append(
                    "grilling.existing_confirmed_owner_design_brief is required when grilling is Skipped"
                )
            if grilling.get("no_material_change_confirmed") is not True:
                errors.append(
                    "grilling.no_material_change_confirmed must be true when grilling is Skipped"
                )
            if grilling.get("owner_explicit_autonomous_authorization") is not True:
                errors.append(
                    "grilling.owner_explicit_autonomous_authorization must be true when grilling is Skipped"
                )

    shared_understanding = data.get("shared_understanding")
    if not isinstance(shared_understanding, dict):
        errors.append("shared_understanding must be an object")
    else:
        if shared_understanding.get("confirmation_question") != CONFIRMATION_QUESTION:
            errors.append("shared_understanding.confirmation_question must use the canonical wording")
        if not allow_draft and shared_understanding.get("confirmed") is not True:
            errors.append(
                "shared_understanding.confirmed must be true before direction generation"
            )

    preselection_revision_cap = get_path(
        data, "success_contract.max_preselection_revision_loops_per_direction"
    )
    if (
        not isinstance(preselection_revision_cap, int)
        or isinstance(preselection_revision_cap, bool)
        or not 1 <= preselection_revision_cap <= 3
    ):
        errors.append(
            "success_contract.max_preselection_revision_loops_per_direction "
            "must be an integer from 1 to 3"
        )

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

    approval_owner = get_path(data, "approval.system_owner")
    authority_owner = get_path(data, "authority.system_owner")
    confirmation_owner = get_path(data, "shared_understanding.confirmed_by")
    if (
        isinstance(approval_owner, str)
        and isinstance(authority_owner, str)
        and approval_owner.strip()
        and authority_owner.strip()
        and approval_owner.strip() != authority_owner.strip()
    ):
        errors.append("approval.system_owner must match authority.system_owner")
    if (
        isinstance(confirmation_owner, str)
        and isinstance(authority_owner, str)
        and confirmation_owner.strip()
        and authority_owner.strip()
        and confirmation_owner.strip() != authority_owner.strip()
    ):
        errors.append(
            "shared_understanding.confirmed_by must match authority.system_owner"
        )

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
        print(
            "Design Brief draft structure is valid; System Owner confirmation is still required."
        )
    else:
        print(
            "Design Brief is structurally generation-ready; recorded System Owner confirmation "
            "must still be verified."
        )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
