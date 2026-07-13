#!/usr/bin/env python3
"""Validate an agent-work audit record and render a standalone HTML report."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlparse

SCHEMA_VERSION = "1.0"
GENERATOR_VERSION = "1.0.0"
MAX_INPUT_BYTES = 2 * 1024 * 1024
MAX_ITEMS = 500
MAX_TEXT = 12_000
MAX_EXCERPT = 4_000
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,63}$")

VERDICTS = {"pass", "pass_with_risks", "fail", "indeterminate"}
VERDICT_RANK = {"pass": 0, "pass_with_risks": 1, "indeterminate": 2, "fail": 3}
INPUT_STATUSES = {"found", "unavailable", "not_applicable"}
REQUIREMENT_PRIORITIES = {"critical", "non_critical"}
REQUIREMENT_STATUSES = {"satisfied", "partial", "missing", "contradicted", "uncheckable"}
MATERIALITIES = {"critical", "material", "minor"}
CLAIM_CLASSIFICATIONS = {"verified", "contradicted", "unsupported", "uncheckable"}
CHECK_RESULTS = {"passed", "failed", "error", "not_run", "uncheckable"}
PROCESS_RESULTS = {"passed", "failed", "warning", "uncheckable"}
SEVERITIES = {"critical", "high", "medium", "low"}
FINDING_STATUSES = {"open", "resolved", "accepted_risk"}
EVIDENCE_KINDS = {"command", "artifact", "browser", "source", "observation", "log", "data"}
DECISIONS = {"accept", "correct", "reverify", "obtain_evidence", "reject"}
BIDI_CONTROLS = {
    "\u061c",
    "\u200e",
    "\u200f",
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",
    "\u2066",
    "\u2067",
    "\u2068",
    "\u2069",
}


class ValidationError(ValueError):
    """Raised when an audit source record is unsafe or internally inconsistent."""


def _add(errors: list[str], path: str, message: str) -> None:
    if len(errors) < 50:
        errors.append(f"{path}: {message}")


def _plain_text(value: str) -> str:
    chars: list[str] = []
    for char in value.replace("\r\n", "\n").replace("\r", "\n"):
        code = ord(char)
        if char in BIDI_CONTROLS or (code < 32 and char not in {"\n", "\t"}) or code == 127:
            chars.append("\ufffd")
        else:
            chars.append(char)
    return "".join(chars)


def _escaped(value: Any) -> str:
    return html.escape(_plain_text(str(value)), quote=True)


def _require_mapping(value: Any, path: str, errors: list[str]) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        _add(errors, path, "must be an object")
        return {}
    return value


def _require_list(value: Any, path: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        _add(errors, path, "must be an array")
        return []
    if len(value) > MAX_ITEMS:
        _add(errors, path, f"must contain at most {MAX_ITEMS} items")
    return value[:MAX_ITEMS]


def _require_str(
    obj: Mapping[str, Any],
    key: str,
    path: str,
    errors: list[str],
    *,
    max_len: int = MAX_TEXT,
    allow_empty: bool = False,
) -> str:
    value = obj.get(key)
    child = f"{path}.{key}"
    if not isinstance(value, str):
        _add(errors, child, "must be a string")
        return ""
    if not allow_empty and not value.strip():
        _add(errors, child, "must not be empty")
    if len(value) > max_len:
        _add(errors, child, f"must be at most {max_len} characters")
    return value


def _optional_str(
    obj: Mapping[str, Any], key: str, path: str, errors: list[str], *, max_len: int = MAX_TEXT
) -> str:
    if key not in obj or obj.get(key) is None:
        return ""
    return _require_str(obj, key, path, errors, max_len=max_len, allow_empty=True)


def _enum(value: Any, allowed: set[str], path: str, errors: list[str]) -> str:
    if not isinstance(value, str) or value not in allowed:
        _add(errors, path, "must be one of " + ", ".join(sorted(allowed)))
        return ""
    return value


def _parse_timestamp(value: str, path: str, errors: list[str]) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        _add(errors, path, "must be an ISO-8601 timestamp")
        return None
    if parsed.tzinfo is None:
        _add(errors, path, "must include a timezone offset")
        return None
    return parsed


def _validate_id(value: str, path: str, errors: list[str]) -> None:
    if value and not ID_RE.fullmatch(value):
        _add(errors, path, "must start with a letter and contain only letters, digits, dot, underscore, or hyphen")


def _item_id(item: Mapping[str, Any], path: str, errors: list[str]) -> str:
    value = _require_str(item, "id", path, errors, max_len=64)
    _validate_id(value, f"{path}.id", errors)
    return value


def _unique_ids(items: Sequence[Mapping[str, Any]], path: str, errors: list[str]) -> set[str]:
    seen: set[str] = set()
    for index, item in enumerate(items):
        item_id = _item_id(item, f"{path}[{index}]", errors)
        if item_id in seen:
            _add(errors, f"{path}[{index}].id", f"duplicates {item_id}")
        if item_id:
            seen.add(item_id)
    return seen


def _evidence_refs(item: Mapping[str, Any], path: str, errors: list[str]) -> list[str]:
    refs = _require_list(item.get("evidenceIds"), f"{path}.evidenceIds", errors)
    result: list[str] = []
    for index, value in enumerate(refs):
        if not isinstance(value, str):
            _add(errors, f"{path}.evidenceIds[{index}]", "must be a string")
            continue
        _validate_id(value, f"{path}.evidenceIds[{index}]", errors)
        result.append(value)
    return result


def _derive_overall(verdicts: Iterable[str]) -> str:
    return max(verdicts, key=lambda value: VERDICT_RANK[value])


def _collection(data: Mapping[str, Any], name: str, errors: list[str]) -> list[Mapping[str, Any]]:
    raw = _require_list(data.get(name), name, errors)
    result: list[Mapping[str, Any]] = []
    for index, item in enumerate(raw):
        result.append(_require_mapping(item, f"{name}[{index}]", errors))
    _unique_ids(result, name, errors)
    return result


def validate_record(data: Any) -> str:
    errors: list[str] = []
    root = _require_mapping(data, "$", errors)
    if root.get("schemaVersion") != SCHEMA_VERSION:
        _add(errors, "schemaVersion", f"must equal {SCHEMA_VERSION}")

    audit = _require_mapping(root.get("audit"), "audit", errors)
    _validate_id(_require_str(audit, "id", "audit", errors, max_len=64), "audit.id", errors)
    _require_str(audit, "title", "audit", errors)
    generated_at = _require_str(audit, "generatedAt", "audit", errors, max_len=64)
    generated_timestamp = _parse_timestamp(generated_at, "audit.generatedAt", errors)
    generator_version = _require_str(audit, "generatorVersion", "audit", errors, max_len=64)
    if generator_version and generator_version != GENERATOR_VERSION:
        _add(errors, "audit.generatorVersion", f"must equal {GENERATOR_VERSION}")
    phase = _enum(audit.get("phase"), {"pre_delivery", "post_hoc"}, "audit.phase", errors)
    gate_state = _enum(audit.get("gateState"), {"ready", "blocked", "not_applicable"}, "audit.gateState", errors)
    iteration = audit.get("iteration")
    if isinstance(iteration, bool) or not isinstance(iteration, int) or iteration < 1:
        _add(errors, "audit.iteration", "must be a positive integer")
    independence = _enum(audit.get("independence"), {"fresh_review", "self_audit"}, "audit.independence", errors)
    confidence = _enum(audit.get("confidence"), {"high", "medium", "low"}, "audit.confidence", errors)
    risk = _enum(audit.get("risk"), {"low", "medium", "high"}, "audit.risk", errors)
    human_confirmation = _enum(
        audit.get("humanConfirmation"),
        {"not_required", "obtained", "unavailable"},
        "audit.humanConfirmation",
        errors,
    )
    redaction = _enum(
        audit.get("redactionStatus"), {"reviewed", "redacted", "not_reviewed"}, "audit.redactionStatus", errors
    )
    subject = _require_mapping(audit.get("subject"), "audit.subject", errors)
    _require_str(subject, "summary", "audit.subject", errors)
    claimed_state = _require_str(subject, "claimedState", "audit.subject", errors)
    audited_state = _require_str(subject, "auditedState", "audit.subject", errors)
    _require_str(subject, "targetEnvironment", "audit.subject", errors)

    verdict_obj = _require_mapping(root.get("verdicts"), "verdicts", errors)
    outcome = _enum(verdict_obj.get("outcome"), VERDICTS, "verdicts.outcome", errors)
    process = _enum(verdict_obj.get("process"), VERDICTS, "verdicts.process", errors)
    claims_verdict = _enum(verdict_obj.get("claims"), VERDICTS, "verdicts.claims", errors)
    verdict_values = [outcome, process, claims_verdict]
    overall = _derive_overall(verdict_values) if all(value in VERDICTS for value in verdict_values) else "fail"

    summary = _require_mapping(root.get("summary"), "summary", errors)
    _require_str(summary, "text", "summary", errors)
    _require_str(summary, "mainLimitation", "summary", errors, allow_empty=True)
    decisive_refs = _require_list(summary.get("decisiveEvidenceIds"), "summary.decisiveEvidenceIds", errors)
    for index, value in enumerate(decisive_refs):
        if not isinstance(value, str):
            _add(errors, f"summary.decisiveEvidenceIds[{index}]", "must be a string")
        else:
            _validate_id(value, f"summary.decisiveEvidenceIds[{index}]", errors)

    inputs = _collection(root, "inputs", errors)
    requirements = _collection(root, "requirements", errors)
    claims = _collection(root, "claims", errors)
    checks = _collection(root, "checks", errors)
    process_checks = _collection(root, "processChecks", errors)
    findings = _collection(root, "findings", errors)
    evidence = _collection(root, "evidence", errors)
    residual_risks = _collection(root, "residualRisks", errors)

    for index, item in enumerate(inputs):
        path = f"inputs[{index}]"
        _require_str(item, "name", path, errors)
        material = item.get("material")
        if not isinstance(material, bool):
            _add(errors, f"{path}.material", "must be a boolean")
        status = _enum(item.get("status"), INPUT_STATUSES, f"{path}.status", errors)
        _require_str(item, "location", path, errors)
        _require_str(item, "why", path, errors)
        if material is True and status == "unavailable" and overall not in {"fail", "indeterminate"}:
            _add(errors, path, "material unavailable input requires overall fail or indeterminate")

    requirement_ids = {item.get("id") for item in requirements if isinstance(item.get("id"), str)}
    requirement_priority = {
        item.get("id"): item.get("priority") for item in requirements if isinstance(item.get("id"), str)
    }
    for index, item in enumerate(requirements):
        path = f"requirements[{index}]"
        _require_str(item, "text", path, errors)
        priority = _enum(item.get("priority"), REQUIREMENT_PRIORITIES, f"{path}.priority", errors)
        status = _enum(item.get("status"), REQUIREMENT_STATUSES, f"{path}.status", errors)
        _require_str(item, "evidenceNeeded", path, errors)
        _optional_str(item, "gap", path, errors)
        requirement_evidence = _evidence_refs(item, path, errors)
        if status == "satisfied" and not requirement_evidence:
            _add(errors, path, "satisfied requirement requires evidence")
        if priority == "critical" and status in {"partial", "missing", "contradicted"} and outcome != "fail":
            _add(errors, path, "critical unmet requirement requires outcome fail")
        if priority == "critical" and status == "uncheckable" and outcome not in {"fail", "indeterminate"}:
            _add(errors, path, "critical uncheckable requirement requires outcome fail or indeterminate")

    for index, item in enumerate(claims):
        path = f"claims[{index}]"
        _require_str(item, "text", path, errors)
        materiality = _enum(item.get("materiality"), MATERIALITIES, f"{path}.materiality", errors)
        classification = _enum(
            item.get("classification"), CLAIM_CLASSIFICATIONS, f"{path}.classification", errors
        )
        refs = _evidence_refs(item, path, errors)
        if classification == "verified" and not refs:
            _add(errors, path, "verified claim requires evidence")
        if materiality in {"critical", "material"}:
            if classification == "contradicted" and claims_verdict != "fail":
                _add(errors, path, "critical/material contradicted claim requires claims verdict fail")
            if classification in {"unsupported", "uncheckable"} and claims_verdict not in {"fail", "indeterminate"}:
                _add(errors, path, "critical/material unsupported or uncheckable claim requires fail or indeterminate")
            if classification != "verified" and claims_verdict in {"pass", "pass_with_risks"}:
                _add(errors, path, "passing claims verdict requires critical/material claims to be verified")

    critical_check_results: list[str] = []
    for index, item in enumerate(checks):
        path = f"checks[{index}]"
        _require_str(item, "name", path, errors)
        _require_str(item, "oracle", path, errors)
        _require_str(item, "oracleProvenance", path, errors)
        _require_str(item, "environment", path, errors)
        result = _enum(item.get("result"), CHECK_RESULTS, f"{path}.result", errors)
        requirement_refs = _require_list(item.get("requirementIds"), f"{path}.requirementIds", errors)
        if not requirement_refs:
            _add(errors, f"{path}.requirementIds", "must reference at least one requirement")
        linked_critical = False
        for ref_index, value in enumerate(requirement_refs):
            if not isinstance(value, str) or value not in requirement_ids:
                _add(errors, f"{path}.requirementIds[{ref_index}]", "must reference an existing requirement")
            elif requirement_priority.get(value) == "critical":
                linked_critical = True
        check_evidence = _evidence_refs(item, path, errors)
        if result == "passed" and not check_evidence:
            _add(errors, path, "passed check requires evidence")
        if linked_critical:
            critical_check_results.append(result)
            if result in {"failed", "error"} and outcome != "fail":
                _add(errors, path, "failed/error critical check requires outcome fail")
            if result in {"not_run", "uncheckable"} and outcome not in {"fail", "indeterminate"}:
                _add(errors, path, "unrun/uncheckable critical check requires outcome fail or indeterminate")

    process_statuses: list[str] = []
    for index, item in enumerate(process_checks):
        path = f"processChecks[{index}]"
        _require_str(item, "name", path, errors)
        process_statuses.append(_enum(item.get("status"), PROCESS_RESULTS, f"{path}.status", errors))
        _require_str(item, "notes", path, errors, allow_empty=True)
        process_evidence = _evidence_refs(item, path, errors)
        if item.get("status") == "passed" and not process_evidence:
            _add(errors, path, "passed process check requires evidence")

    open_stop_ship_count = 0
    finding_status_by_id: dict[str, str] = {}
    resolved_iteration_by_id: dict[str, int] = {}
    for index, item in enumerate(findings):
        path = f"findings[{index}]"
        severity = _enum(item.get("severity"), SEVERITIES, f"{path}.severity", errors)
        status = _enum(item.get("status"), FINDING_STATUSES, f"{path}.status", errors)
        finding_id = item.get("id") if isinstance(item.get("id"), str) else ""
        if finding_id:
            finding_status_by_id[finding_id] = status
        introduced = item.get("iteration")
        if isinstance(introduced, bool) or not isinstance(introduced, int) or introduced < 1:
            _add(errors, f"{path}.iteration", "must be a positive integer")
        stop_ship = item.get("stopShip")
        if not isinstance(stop_ship, bool):
            _add(errors, f"{path}.stopShip", "must be a boolean")
        elif stop_ship and status == "open":
            open_stop_ship_count += 1
        resolved_in = item.get("resolvedInIteration")
        if status == "resolved":
            if isinstance(resolved_in, bool) or not isinstance(resolved_in, int) or resolved_in < 1:
                _add(errors, f"{path}.resolvedInIteration", "resolved finding requires a positive integer")
            elif isinstance(introduced, int) and resolved_in <= introduced:
                _add(errors, f"{path}.resolvedInIteration", "must be later than the introduction iteration")
            else:
                resolved_iteration_by_id[finding_id] = resolved_in
        elif resolved_in is not None:
            _add(errors, f"{path}.resolvedInIteration", "must be null unless status is resolved")
        if status == "accepted_risk" and stop_ship is True:
            _add(errors, path, "stop-ship finding cannot be accepted as risk")
        _require_str(item, "title", path, errors)
        _require_str(item, "detail", path, errors)
        _require_str(item, "consequence", path, errors)
        _require_str(item, "correctiveAction", path, errors)
        _evidence_refs(item, path, errors)
        if severity == "critical" and stop_ship is not True:
            _add(errors, path, "critical finding must be stop-ship")

    evidence_ids = {item.get("id") for item in evidence if isinstance(item.get("id"), str)}
    evidence_by_id = {item.get("id"): item for item in evidence if isinstance(item.get("id"), str)}
    for index, item in enumerate(evidence):
        path = f"evidence[{index}]"
        _enum(item.get("kind"), EVIDENCE_KINDS, f"{path}.kind", errors)
        for key in (
            "label",
            "summary",
            "locator",
            "stateId",
            "environment",
            "sourceVersion",
            "coverage",
            "refreshTrigger",
        ):
            _require_str(item, key, path, errors)
        observed_at = _require_str(item, "observedAt", path, errors, max_len=64)
        observed_timestamp = _parse_timestamp(observed_at, f"{path}.observedAt", errors)
        if generated_timestamp and observed_timestamp and observed_timestamp > generated_timestamp:
            _add(errors, f"{path}.observedAt", "cannot be later than audit.generatedAt")
        _require_str(item, "excerpt", path, errors, max_len=MAX_EXCERPT, allow_empty=True)
        if "sourceUrl" in item:
            source_url = _require_str(item, "sourceUrl", path, errors, max_len=2048)
            parsed = urlparse(source_url)
            if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                _add(errors, f"{path}.sourceUrl", "must be an explicit credential-free HTTPS URL")
        if "command" in item:
            command = _require_mapping(item.get("command"), f"{path}.command", errors)
            _require_str(command, "display", f"{path}.command", errors)
            exit_code = command.get("exitCode")
            if isinstance(exit_code, bool) or not isinstance(exit_code, int):
                _add(errors, f"{path}.command.exitCode", "must be an integer")

    def check_refs(owner: str, refs: Iterable[Any]) -> None:
        for index, value in enumerate(refs):
            if isinstance(value, str) and value not in evidence_ids:
                _add(errors, f"{owner}[{index}]", f"references missing evidence ID {value}")

    check_refs("summary.decisiveEvidenceIds", decisive_refs)
    for name, items in (
        ("requirements", requirements),
        ("claims", claims),
        ("checks", checks),
        ("processChecks", process_checks),
        ("findings", findings),
        ("residualRisks", residual_risks),
    ):
        for index, item in enumerate(items):
            check_refs(f"{name}[{index}].evidenceIds", item.get("evidenceIds", []))

    if overall in {"pass", "pass_with_risks"}:
        for name, collection in (
            ("inputs", inputs),
            ("requirements", requirements),
            ("claims", claims),
            ("checks", checks),
            ("processChecks", process_checks),
            ("evidence", evidence),
        ):
            if not collection:
                _add(errors, name, "ready verdict requires at least one item")
        if not any(item.get("priority") == "critical" for item in requirements):
            _add(errors, "requirements", "ready verdict requires at least one critical requirement")
        if not decisive_refs:
            _add(errors, "summary.decisiveEvidenceIds", "ready verdict requires decisive evidence")
        if not critical_check_results:
            _add(errors, "checks", "ready verdict requires at least one check linked to a critical requirement")
        elif any(result != "passed" for result in critical_check_results):
            _add(errors, "checks", "ready verdict requires all critical checks to pass")

        def check_state_refs(owner: str, refs: Iterable[Any]) -> None:
            for ref_index, value in enumerate(refs):
                if isinstance(value, str) and value in evidence_by_id:
                    if evidence_by_id[value].get("stateId") != audited_state:
                        _add(errors, f"{owner}[{ref_index}]", "ready verdict requires evidence bound to auditedState")

        check_state_refs("summary.decisiveEvidenceIds", decisive_refs)
        for name, items in (("requirements", requirements), ("claims", claims), ("checks", checks)):
            for index, item in enumerate(items):
                check_state_refs(f"{name}[{index}].evidenceIds", item.get("evidenceIds", []))
        for index, item in enumerate(findings):
            if item.get("status") != "resolved":
                check_state_refs(f"findings[{index}].evidenceIds", item.get("evidenceIds", []))

    for index, item in enumerate(residual_risks):
        path = f"residualRisks[{index}]"
        _require_str(item, "text", path, errors)
        _require_str(item, "reason", path, errors)
        _require_str(item, "resolution", path, errors)
        _evidence_refs(item, path, errors)

    _require_str(root, "processSummary", "$", errors)
    _require_str(root, "evidenceQuality", "$", errors)
    recommendation = _require_mapping(root.get("recommendation"), "recommendation", errors)
    _enum(recommendation.get("decision"), DECISIONS, "recommendation.decision", errors)
    _require_str(recommendation, "summary", "recommendation", errors)
    recommendation_items = _require_list(recommendation.get("items"), "recommendation.items", errors)
    for index, value in enumerate(recommendation_items):
        if not isinstance(value, str) or not value.strip():
            _add(errors, f"recommendation.items[{index}]", "must be a non-empty string")
        elif len(value) > MAX_TEXT:
            _add(errors, f"recommendation.items[{index}]", f"must be at most {MAX_TEXT} characters")

    corrections = _require_list(root.get("corrections"), "corrections", errors)
    finding_ids = {item.get("id") for item in findings if isinstance(item.get("id"), str)}
    correction_iteration_by_finding: dict[str, int] = {}
    for index, raw in enumerate(corrections):
        path = f"corrections[{index}]"
        item = _require_mapping(raw, path, errors)
        number = item.get("iteration")
        if isinstance(number, bool) or not isinstance(number, int) or number < 1:
            _add(errors, f"{path}.iteration", "must be a positive integer")
        elif isinstance(iteration, int) and number > iteration:
            _add(errors, f"{path}.iteration", "cannot exceed audit.iteration")
        for key in ("priorState", "newState", "summary"):
            _require_str(item, key, path, errors)
        finding_refs = _require_list(item.get("findingIds"), f"{path}.findingIds", errors)
        for ref_index, value in enumerate(finding_refs):
            if not isinstance(value, str) or value not in finding_ids:
                _add(errors, f"{path}.findingIds[{ref_index}]", "must reference an existing finding")
            elif isinstance(number, int):
                correction_iteration_by_finding[value] = number
        refs = _require_list(item.get("evidenceIds"), f"{path}.evidenceIds", errors)
        if not refs:
            _add(errors, f"{path}.evidenceIds", "correction requires new-state evidence")
        check_refs(f"{path}.evidenceIds", refs)
        if refs and not any(
            isinstance(value, str)
            and value in evidence_by_id
            and evidence_by_id[value].get("stateId") == item.get("newState")
            for value in refs
        ):
            _add(errors, f"{path}.evidenceIds", "must include evidence bound to newState")

    for finding_id, resolved_iteration in resolved_iteration_by_id.items():
        if finding_id not in correction_iteration_by_finding:
            _add(errors, f"findings.{finding_id}", "resolved finding must be referenced by a correction")
        elif correction_iteration_by_finding[finding_id] != resolved_iteration:
            _add(errors, f"findings.{finding_id}", "resolvedInIteration must match its correction iteration")

    if open_stop_ship_count and overall != "fail":
        _add(errors, "verdicts", "open stop-ship findings require overall fail")
    if any(
        item.get("status") != "resolved" and item.get("severity") in {"high", "medium"} for item in findings
    ) and overall == "pass":
        _add(errors, "verdicts", "open/accepted medium or high findings require at least pass_with_risks")
    if any(status == "failed" for status in process_statuses) and process != "fail":
        _add(errors, "verdicts.process", "failed process check requires process fail")
    if any(status == "uncheckable" for status in process_statuses) and process not in {"fail", "indeterminate"}:
        _add(errors, "verdicts.process", "uncheckable process check requires fail or indeterminate")
    if any(status == "warning" for status in process_statuses) and process == "pass":
        _add(errors, "verdicts.process", "warning process check cannot produce process pass")
    if independence == "self_audit" and confidence == "high":
        _add(errors, "audit.confidence", "self-audit cannot claim high confidence")
    if independence == "self_audit" and overall == "pass":
        _add(errors, "verdicts", "self-audit cannot produce overall pass")
    if overall in {"pass", "pass_with_risks"} and confidence == "low":
        _add(errors, "verdicts", "low-confidence audit cannot produce a ready verdict")
    if overall == "pass" and confidence != "high":
        _add(errors, "verdicts", "overall pass requires high confidence")
    if risk == "high" and overall in {"pass", "pass_with_risks"} and human_confirmation != "obtained":
        _add(errors, "audit.humanConfirmation", "high-risk ready verdict requires obtained confirmation")
    if overall not in {"fail", "indeterminate"} and claimed_state != audited_state:
        _add(errors, "audit.subject", "ready verdict requires claimedState to equal auditedState")
    if phase == "post_hoc" and gate_state != "not_applicable":
        _add(errors, "audit.gateState", "post-hoc audit requires not_applicable")
    if phase == "pre_delivery":
        expected_gate = "blocked" if overall in {"fail", "indeterminate"} else "ready"
        if gate_state != expected_gate:
            _add(errors, "audit.gateState", f"pre-delivery overall {overall} requires {expected_gate}")
    if redaction == "not_reviewed" and overall in {"pass", "pass_with_risks"} and risk == "high":
        _add(errors, "audit.redactionStatus", "high-risk ready verdict requires redaction review")

    if errors:
        suffix = "" if len(errors) < 50 else "\n- additional errors omitted"
        raise ValidationError("Audit source validation failed:\n- " + "\n- ".join(errors) + suffix)
    return overall


def load_record(path: Path) -> Any:
    size = path.stat().st_size
    if size > MAX_INPUT_BYTES:
        raise ValidationError(f"Input exceeds {MAX_INPUT_BYTES} bytes")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read audit JSON: {exc}") from exc


def _pretty(value: str) -> str:
    return value.replace("_", " ").title()


def _tone(value: str) -> str:
    if value in {"fail", "failed", "error", "contradicted", "missing", "critical", "reject"}:
        return "bad"
    if value in {
        "indeterminate",
        "pass_with_risks",
        "warning",
        "uncheckable",
        "unsupported",
        "partial",
        "high",
        "blocked",
        "unavailable",
        "not_reviewed",
        "correct",
        "obtain_evidence",
        "open",
        "accepted_risk",
    }:
        return "warn"
    if value in {
        "pass",
        "passed",
        "verified",
        "satisfied",
        "found",
        "reviewed",
        "redacted",
        "ready",
        "accept",
        "resolved",
    }:
        return "good"
    return "info"


def _badge(value: str, tone: str | None = None) -> str:
    return f'<span class="badge badge--{tone or _tone(value)}">{_escaped(_pretty(value))}</span>'


def _evidence_links(ids: Sequence[str]) -> str:
    if not ids:
        return '<span class="muted">None recorded</span>'
    return " ".join(f'<a class="evidence-ref" href="#evidence-{_escaped(item_id)}">{_escaped(item_id)}</a>' for item_id in ids)


def _dl(rows: Sequence[tuple[str, str]]) -> str:
    return '<dl class="facts">' + "".join(
        f"<div><dt>{_escaped(label)}</dt><dd>{value}</dd></div>" for label, value in rows
    ) + "</dl>"


def _section(section_id: str, title: str, body: str, count: int | None = None) -> str:
    count_html = f'<span class="section-count">{count}</span>' if count is not None else ""
    return f'<section id="{_escaped(section_id)}" class="report-section"><h2>{_escaped(title)}{count_html}</h2>{body}</section>'


def render_report(data: Mapping[str, Any], overall: str, css: str, source_name: str) -> str:
    audit = data["audit"]
    subject = audit["subject"]
    verdicts = data["verdicts"]
    summary = data["summary"]
    inputs = data["inputs"]
    requirements = data["requirements"]
    claims = data["claims"]
    checks = data["checks"]
    process_checks = data["processChecks"]
    findings = data["findings"]
    evidence = data["evidence"]
    residual_risks = data["residualRisks"]
    corrections = data["corrections"]
    recommendation = data["recommendation"]

    stop_ship = [item for item in findings if item["stopShip"] and item["status"] == "open"]
    unavailable_inputs = [item for item in inputs if item["material"] and item["status"] == "unavailable"]
    unresolved_requirements = [
        item for item in requirements if item["priority"] == "critical" and item["status"] != "satisfied"
    ]
    material_claim_gaps = [
        item
        for item in claims
        if item["materiality"] in {"critical", "material"} and item["classification"] != "verified"
    ]
    failed_checks = [item for item in checks if item["result"] in {"failed", "error", "uncheckable", "not_run"}]

    alerts: list[str] = []
    if overall in {"fail", "indeterminate"}:
        alerts.append(
            f'<div class="notice notice--{_tone(overall)}"><strong>{_escaped(_pretty(overall))}:</strong> '
            f'{_escaped(summary["mainLimitation"] or recommendation["summary"])}</div>'
        )
    if audit["independence"] == "self_audit":
        alerts.append('<div class="notice notice--warn"><strong>Self-audit:</strong> shared assumptions cap confidence and readiness.</div>')
    if audit["redactionStatus"] == "not_reviewed":
        alerts.append('<div class="notice notice--warn"><strong>Redaction not reviewed:</strong> inspect evidence before sharing this report.</div>')
    if subject["claimedState"] != subject["auditedState"]:
        alerts.append('<div class="notice notice--warn"><strong>State mismatch:</strong> claimed and audited target states differ.</div>')

    headline = f"""
    <header class="report-header">
      <div class="shell">
        <p class="eyebrow">Evidence-first completion gate</p>
        <div class="headline">
          <div>
            <h1>{_escaped(audit['title'])}</h1>
            <p class="subject">{_escaped(subject['summary'])}</p>
          </div>
          <div class="overall overall--{_tone(overall)}"><span>Overall</span><strong>{_escaped(_pretty(overall))}</strong></div>
        </div>
        <div class="verdict-grid" aria-label="Audit verdicts">
          <div><span>Outcome</span>{_badge(verdicts['outcome'])}</div>
          <div><span>Process</span>{_badge(verdicts['process'])}</div>
          <div><span>Claims</span>{_badge(verdicts['claims'])}</div>
          <div><span>Confidence</span>{_badge(audit['confidence'], {'high': 'good', 'medium': 'info', 'low': 'warn'}[audit['confidence']])}</div>
          <div><span>Risk</span>{_badge(audit['risk'], {'low': 'good', 'medium': 'warn', 'high': 'bad'}[audit['risk']])}</div>
          <div><span>Gate</span>{_badge(audit['gateState'])}</div>
        </div>
        {''.join(alerts)}
      </div>
    </header>
    """

    target_body = _dl(
        [
            ("Claimed state", f"<code>{_escaped(subject['claimedState'])}</code>"),
            ("Audited state", f"<code>{_escaped(subject['auditedState'])}</code>"),
            ("Target environment", _escaped(subject["targetEnvironment"])),
            ("Phase", _badge(audit["phase"])),
            ("Independence", _badge(audit["independence"])),
            ("Iteration", _escaped(audit["iteration"])),
            ("Generated", _escaped(audit["generatedAt"])),
            ("Redaction", _badge(audit["redactionStatus"])),
        ]
    )

    summary_body = f"""
      <p class="summary-text">{_escaped(summary['text'])}</p>
      <div class="limitation"><strong>Main limitation</strong><p>{_escaped(summary['mainLimitation'] or 'None recorded')}</p></div>
      <p class="evidence-line"><strong>Decisive evidence</strong> {_evidence_links(summary['decisiveEvidenceIds'])}</p>
    """

    attention_items: list[str] = []
    for item in stop_ship:
        attention_items.append(
            f'<article class="attention attention--bad"><h3>{_escaped(item["id"])} · {_escaped(item["title"])}</h3>'
            f'<p>{_escaped(item["consequence"])}</p><p><strong>Action:</strong> {_escaped(item["correctiveAction"])}</p></article>'
        )
    for item in findings:
        if item not in stop_ship and item["status"] != "resolved" and item["severity"] in {"critical", "high"}:
            attention_items.append(
                f'<article class="attention attention--warn"><h3>{_escaped(item["id"])} · {_escaped(item["title"])}</h3>'
                f'<p>{_escaped(item["consequence"])}</p><p><strong>Status:</strong> {_escaped(_pretty(item["status"]))}</p></article>'
            )
    for item in unavailable_inputs:
        attention_items.append(
            f'<article class="attention attention--warn"><h3>{_escaped(item["id"])} · Missing material input</h3>'
            f'<p>{_escaped(item["name"])}: {_escaped(item["why"])}</p></article>'
        )
    for item in unresolved_requirements:
        attention_items.append(
            f'<article class="attention attention--warn"><h3>{_escaped(item["id"])} · Critical requirement {_pretty(item["status"])}</h3>'
            f'<p>{_escaped(item["text"])}</p></article>'
        )
    for item in material_claim_gaps:
        attention_items.append(
            f'<article class="attention attention--warn"><h3>{_escaped(item["id"])} · Material claim {_pretty(item["classification"])}</h3>'
            f'<p>{_escaped(item["text"])}</p></article>'
        )
    for item in failed_checks:
        attention_items.append(
            f'<article class="attention attention--warn"><h3>{_escaped(item["id"])} · Check {_pretty(item["result"])}</h3>'
            f'<p>{_escaped(item["name"])}</p></article>'
        )
    attention_body = "".join(attention_items) or '<p class="empty">No blocking or material attention items.</p>'

    input_body = '<div class="ledger">' + "".join(
        f'<article class="ledger-item"><div class="ledger-head"><h3>{_escaped(item["id"])} · {_escaped(item["name"])}</h3>{_badge(item["status"])}</div>'
        + _dl(
            [
                ("Material", _escaped("Yes" if item["material"] else "No")),
                ("Location", _escaped(item["location"])),
                ("Why", _escaped(item["why"])),
            ]
        )
        + "</article>"
        for item in inputs
    ) + "</div>"

    requirement_body = '<div class="ledger">' + "".join(
        f'<article class="ledger-item"><div class="ledger-head"><h3>{_escaped(item["id"])} · {_escaped(item["text"])}</h3>{_badge(item["status"])}</div>'
        + _dl(
            [
                ("Priority", _badge(item["priority"])),
                ("Evidence needed", _escaped(item["evidenceNeeded"])),
                ("Evidence", _evidence_links(item["evidenceIds"])),
                ("Gap", _escaped(item.get("gap") or "None recorded")),
            ]
        )
        + "</article>"
        for item in requirements
    ) + "</div>"

    checkable_claims = [item for item in claims if item["classification"] != "uncheckable"]
    contradicted = len([item for item in checkable_claims if item["classification"] == "contradicted"])
    unsupported = len([item for item in claims if item["classification"] == "unsupported"])
    uncheckable = len([item for item in claims if item["classification"] == "uncheckable"])
    claim_metrics = _dl(
        [
            ("Contradicted share", _escaped(f"{contradicted}/{len(checkable_claims)}" if checkable_claims else "Not meaningful")),
            ("Unsupported", _escaped(f"{unsupported}/{len(claims)}" if claims else "0/0")),
            ("Uncheckable", _escaped(f"{uncheckable}/{len(claims)}" if claims else "0/0")),
        ]
    )
    claim_body = claim_metrics + '<div class="ledger">' + "".join(
        f'<article class="ledger-item"><div class="ledger-head"><h3>{_escaped(item["id"])} · {_escaped(item["text"])}</h3>{_badge(item["classification"])}</div>'
        + _dl(
            [
                ("Materiality", _badge(item["materiality"])),
                ("Evidence", _evidence_links(item["evidenceIds"])),
            ]
        )
        + "</article>"
        for item in claims
    ) + "</div>"

    check_body = '<div class="ledger">' + "".join(
        f'<article class="ledger-item"><div class="ledger-head"><h3>{_escaped(item["id"])} · {_escaped(item["name"])}</h3>{_badge(item["result"])}</div>'
        + _dl(
            [
                ("Oracle", _escaped(item["oracle"])),
                ("Oracle provenance", _escaped(item["oracleProvenance"])),
                ("Requirements", _escaped(", ".join(item["requirementIds"]))),
                ("Environment", _escaped(item["environment"])),
                ("Evidence", _evidence_links(item["evidenceIds"])),
            ]
        )
        + "</article>"
        for item in checks
    ) + "</div>"

    process_body = f'<p class="summary-text">{_escaped(data["processSummary"])}</p><div class="ledger">' + "".join(
        f'<article class="ledger-item"><div class="ledger-head"><h3>{_escaped(item["id"])} · {_escaped(item["name"])}</h3>{_badge(item["status"])}</div>'
        + _dl([("Notes", _escaped(item["notes"] or "None recorded")), ("Evidence", _evidence_links(item["evidenceIds"]))])
        + "</article>"
        for item in process_checks
    ) + "</div>"

    finding_body = '<div class="ledger">' + "".join(
        f'<article class="ledger-item ledger-item--{_tone(item["status"] if item["status"] == "resolved" else item["severity"])}"><div class="ledger-head"><h3>{_escaped(item["id"])} · {_escaped(item["title"])}</h3><div class="badge-group">{_badge(item["severity"])} {_badge(item["status"])}</div></div>'
        + _dl(
            [
                ("Stop ship", _escaped("Yes" if item["stopShip"] else "No")),
                ("Introduced", _escaped(f"Iteration {item['iteration']}")),
                (
                    "Resolved",
                    _escaped(
                        f"Iteration {item['resolvedInIteration']}"
                        if item.get("resolvedInIteration") is not None
                        else "Not resolved"
                    ),
                ),
                ("Finding", _escaped(item["detail"])),
                ("Consequence", _escaped(item["consequence"])),
                ("Corrective action", _escaped(item["correctiveAction"])),
                ("Evidence", _evidence_links(item["evidenceIds"])),
            ]
        )
        + "</article>"
        for item in findings
    ) + "</div>"
    if not findings:
        finding_body = '<p class="empty">No findings recorded.</p>'

    risk_body = '<div class="ledger">' + "".join(
        f'<article class="ledger-item"><h3>{_escaped(item["id"])} · {_escaped(item["text"])}</h3>'
        + _dl(
            [
                ("Reason", _escaped(item["reason"])),
                ("Resolution", _escaped(item["resolution"])),
                ("Evidence", _evidence_links(item["evidenceIds"])),
            ]
        )
        + "</article>"
        for item in residual_risks
    ) + "</div>"
    if not residual_risks:
        risk_body = '<p class="empty">No residual risks recorded.</p>'

    correction_body = '<div class="ledger">' + "".join(
        f'<article class="ledger-item"><h3>Iteration {_escaped(item["iteration"])} · {_escaped(item["summary"])}</h3>'
        + _dl(
            [
                ("Prior state", f"<code>{_escaped(item['priorState'])}</code>"),
                ("New state", f"<code>{_escaped(item['newState'])}</code>"),
                ("Findings", _escaped(", ".join(item["findingIds"]) or "None")),
                ("Evidence", _evidence_links(item["evidenceIds"])),
            ]
        )
        + "</article>"
        for item in corrections
    ) + "</div>"
    if not corrections:
        correction_body = '<p class="empty">No remediation iterations recorded.</p>'

    evidence_body = '<div class="evidence-list">' + "".join(
        _render_evidence(item) for item in evidence
    ) + "</div>"

    recommendation_items = "".join(f"<li>{_escaped(item)}</li>" for item in recommendation["items"])
    recommendation_body = f"""
      <div class="recommendation recommendation--{_tone(recommendation['decision'])}">
        <div>{_badge(recommendation['decision'])}</div>
        <p>{_escaped(recommendation['summary'])}</p>
        <ul>{recommendation_items}</ul>
      </div>
    """

    main = "".join(
        [
            _section("summary", "Executive Summary", summary_body),
            _section("attention", "Needs Attention", attention_body, len(attention_items)),
            _section("target", "Audited Target", target_body),
            _section("inputs", "Input Completeness", input_body, len(inputs)),
            _section("requirements", "Requirement Fidelity", requirement_body, len(requirements)),
            _section("claims", "Claim Integrity", claim_body, len(claims)),
            _section("verification", "Empirical Verification", check_body, len(checks)),
            _section("process", "Process Integrity", process_body, len(process_checks)),
            _section("findings", "Findings", finding_body, len(findings)),
            _section("quality", "Test and Evidence Quality", f'<p class="summary-text">{_escaped(data["evidenceQuality"])}</p>'),
            _section("risks", "Residual Risk", risk_body, len(residual_risks)),
            _section("corrections", "Correction History", correction_body, len(corrections)),
            _section("recommendation", "Recommended Next Action", recommendation_body),
            _section("evidence", "Evidence Register", evidence_body, len(evidence)),
        ]
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; font-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
  <title>{_escaped(audit['title'])} · {_escaped(_pretty(overall))}</title>
  <style>{css}</style>
</head>
<body>
  <a class="skip-link" href="#report-main">Skip to report</a>
  {headline}
  <main id="report-main" class="shell">{main}</main>
  <footer class="report-footer"><div class="shell">Report {_escaped(audit['id'])} · schema {_escaped(data['schemaVersion'])} · generator {_escaped(GENERATOR_VERSION)} · source {_escaped(source_name)}</div></footer>
</body>
</html>
"""


def _render_evidence(item: Mapping[str, Any]) -> str:
    command_html = ""
    if "command" in item:
        command = item["command"]
        command_html = _dl(
            [
                ("Command", f"<code>{_escaped(command['display'])}</code>"),
                ("Exit code", _escaped(command["exitCode"])),
            ]
        )
    url_html = ""
    if item.get("sourceUrl"):
        url = _escaped(item["sourceUrl"])
        url_html = f'<p><a class="source-link" href="{url}" target="_blank" rel="noopener noreferrer">Open authoritative source</a></p>'
    return f"""
      <details id="evidence-{_escaped(item['id'])}" class="evidence-item" open>
        <summary><span>{_escaped(item['id'])} · {_escaped(item['label'])}</span>{_badge(item['kind'])}</summary>
        <div class="evidence-body">
          <p>{_escaped(item['summary'])}</p>
          {_dl([
              ('Locator', f'<code>{_escaped(item["locator"])}</code>'),
              ('Observed', _escaped(item['observedAt'])),
              ('State ID', f'<code>{_escaped(item["stateId"])}</code>'),
              ('Environment', _escaped(item['environment'])),
              ('Source version', _escaped(item['sourceVersion'])),
              ('Coverage', _escaped(item['coverage'])),
              ('Refresh trigger', _escaped(item['refreshTrigger'])),
          ])}
          {command_html}
          <pre>{_escaped(item['excerpt'] or 'No excerpt recorded')}</pre>
          {url_html}
        </div>
      </details>
    """


def generate_report(input_path: Path, output_path: Path) -> str:
    data = load_record(input_path)
    overall = validate_record(data)
    css_path = Path(__file__).resolve().parent.parent / "assets" / "report.css"
    try:
        css = css_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValidationError(f"Cannot read bundled CSS: {exc}") from exc
    document = render_report(data, overall, css, input_path.name)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=output_path.parent, prefix=f".{output_path.name}.", delete=False
        ) as handle:
            temp_name = handle.name
            handle.write(document)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, output_path)
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)
    return overall


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Path to agent-work-audit.json")
    parser.add_argument("--output", required=True, type=Path, help="Path for the standalone HTML report")
    args = parser.parse_args(argv)
    try:
        overall = generate_report(args.input, args.output)
    except (OSError, ValidationError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(f"Wrote {args.output} (overall: {overall})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
