#!/usr/bin/env python3

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("generate_report.py")
SPEC = importlib.util.spec_from_file_location("generate_report", MODULE_PATH)
assert SPEC and SPEC.loader
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


def valid_record() -> dict:
    state = "HEAD abc123 + diff sha256:audited"
    return {
        "schemaVersion": "1.0",
        "audit": {
            "id": "audit-001",
            "title": "Agent Work Audit",
            "generatedAt": "2026-07-10T16:30:00+02:00",
            "generatorVersion": "1.0.0",
            "phase": "post_hoc",
            "gateState": "not_applicable",
            "iteration": 1,
            "independence": "fresh_review",
            "confidence": "high",
            "risk": "low",
            "humanConfirmation": "not_required",
            "subject": {
                "summary": "Audit report renderer",
                "claimedState": state,
                "auditedState": state,
                "targetEnvironment": "Python and local browser",
            },
            "redactionStatus": "reviewed",
        },
        "verdicts": {"outcome": "pass", "process": "pass", "claims": "pass"},
        "summary": {
            "text": "The renderer validates and produces a standalone report.",
            "mainLimitation": "No external integration is required.",
            "decisiveEvidenceIds": ["E1"],
        },
        "inputs": [
            {
                "id": "I1",
                "name": "user_contract",
                "material": True,
                "status": "found",
                "location": "Current conversation",
                "why": "Defines expected output",
            }
        ],
        "requirements": [
            {
                "id": "R1",
                "text": "Generate offline HTML",
                "priority": "critical",
                "status": "satisfied",
                "evidenceNeeded": "A successful renderer run",
                "evidenceIds": ["E1"],
                "gap": "",
            }
        ],
        "claims": [
            {
                "id": "C1",
                "text": "The report renders successfully.",
                "materiality": "material",
                "classification": "verified",
                "evidenceIds": ["E1"],
            }
        ],
        "checks": [
            {
                "id": "K1",
                "name": "Generate report",
                "oracle": "Exit zero and output exists",
                "oracleProvenance": "Requirement R1",
                "environment": "Python standard library",
                "result": "passed",
                "requirementIds": ["R1"],
                "evidenceIds": ["E1"],
            }
        ],
        "processChecks": [
            {
                "id": "P1",
                "name": "Fresh evidence",
                "status": "passed",
                "notes": "Evidence follows the latest state change.",
                "evidenceIds": ["E1"],
            }
        ],
        "findings": [],
        "evidence": [
            {
                "id": "E1",
                "kind": "command",
                "label": "Renderer test",
                "summary": "The report was generated.",
                "locator": "scripts/test_generate_report.py",
                "observedAt": "2026-07-10T16:28:00+02:00",
                "stateId": state,
                "environment": "Python standard library",
                "sourceVersion": "schema 1.0",
                "coverage": "Validation and rendering",
                "refreshTrigger": "Any renderer, CSS, schema, or fixture change",
                "excerpt": "ok",
                "command": {"display": "python3 scripts/test_generate_report.py", "exitCode": 0},
                "sourceUrl": "https://example.com/audit-source",
            }
        ],
        "processSummary": "The renderer used fresh local evidence.",
        "evidenceQuality": "The test has a deterministic oracle and target-bound evidence.",
        "residualRisks": [],
        "recommendation": {"decision": "accept", "summary": "Accept the report.", "items": []},
        "corrections": [],
    }


class ReportGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def generate(self, record: dict) -> tuple[str, Path]:
        source = self.root / "audit.json"
        output = self.root / "audit.html"
        source.write_text(json.dumps(record), encoding="utf-8")
        overall = generator.generate_report(source, output)
        return overall, output

    def assert_invalid(self, record: dict) -> str:
        source = self.root / "invalid.json"
        output = self.root / "invalid.html"
        source.write_text(json.dumps(record), encoding="utf-8")
        with self.assertRaises(generator.ValidationError) as context:
            generator.generate_report(source, output)
        self.assertFalse(output.exists())
        return str(context.exception)

    def test_valid_report_is_standalone_responsive_and_printable(self) -> None:
        overall, output = self.generate(valid_record())
        document = output.read_text(encoding="utf-8")
        self.assertEqual(overall, "pass")
        self.assertIn("Content-Security-Policy", document)
        self.assertIn("default-src 'none'", document)
        self.assertIn("@media (max-width: 620px)", document)
        self.assertIn("@media print", document)
        self.assertIn("Audit report renderer", document)
        self.assertIn("Evidence Register", document)
        self.assertNotIn("https://cdn", document)

    def test_untrusted_text_is_escaped_and_bidi_is_neutralized(self) -> None:
        record = valid_record()
        record["summary"]["text"] = '<script>alert("x")</script>\u202eexe'
        _, output = self.generate(record)
        document = output.read_text(encoding="utf-8")
        self.assertNotIn('<script>alert("x")</script>', document)
        self.assertIn("&lt;script&gt;", document)
        self.assertNotIn("\u202e", document)

    def test_dangling_evidence_reference_fails_without_output(self) -> None:
        record = valid_record()
        record["claims"][0]["evidenceIds"] = ["E404"]
        message = self.assert_invalid(record)
        self.assertIn("missing evidence ID E404", message)

    def test_self_audit_cannot_claim_high_confidence_or_pass(self) -> None:
        record = valid_record()
        record["audit"]["independence"] = "self_audit"
        message = self.assert_invalid(record)
        self.assertIn("self-audit cannot claim high confidence", message)
        self.assertIn("self-audit cannot produce overall pass", message)

    def test_stop_ship_finding_requires_overall_fail(self) -> None:
        record = valid_record()
        record["findings"] = [
            {
                "id": "F1",
                "severity": "critical",
                "stopShip": True,
                "iteration": 1,
                "status": "open",
                "resolvedInIteration": None,
                "title": "Broken gate",
                "detail": "The gate is bypassed.",
                "consequence": "Invalid output can ship.",
                "correctiveAction": "Enforce the gate.",
                "evidenceIds": ["E1"],
            }
        ]
        message = self.assert_invalid(record)
        self.assertIn("open stop-ship findings require overall fail", message)

    def test_material_unavailable_input_cannot_pass(self) -> None:
        record = valid_record()
        record["inputs"][0]["status"] = "unavailable"
        message = self.assert_invalid(record)
        self.assertIn("material unavailable input requires overall fail or indeterminate", message)

    def test_claim_failure_drives_derived_overall(self) -> None:
        record = valid_record()
        record["verdicts"]["claims"] = "fail"
        record["claims"][0]["classification"] = "contradicted"
        overall, output = self.generate(record)
        self.assertEqual(overall, "fail")
        self.assertIn("Fail", output.read_text(encoding="utf-8"))

    def test_material_contradicted_claim_requires_claim_failure(self) -> None:
        record = valid_record()
        record["claims"][0]["classification"] = "contradicted"
        message = self.assert_invalid(record)
        self.assertIn("contradicted claim requires claims verdict fail", message)

    def test_passing_state_must_match(self) -> None:
        record = valid_record()
        record["audit"]["subject"]["claimedState"] = "different-state"
        message = self.assert_invalid(record)
        self.assertIn("claimedState to equal auditedState", message)

    def test_overall_pass_requires_high_confidence(self) -> None:
        record = valid_record()
        record["audit"]["confidence"] = "medium"
        message = self.assert_invalid(record)
        self.assertIn("overall pass requires high confidence", message)

    def test_ready_report_requires_minimum_evidence_basis(self) -> None:
        record = valid_record()
        record["summary"]["decisiveEvidenceIds"] = []
        record["requirements"] = []
        record["claims"] = []
        record["checks"] = []
        record["evidence"] = []
        record["processChecks"] = []
        message = self.assert_invalid(record)
        self.assertIn("ready verdict requires at least one item", message)
        self.assertIn("ready verdict requires decisive evidence", message)

    def test_failed_critical_check_requires_outcome_fail(self) -> None:
        record = valid_record()
        record["checks"][0]["result"] = "failed"
        message = self.assert_invalid(record)
        self.assertIn("failed/error critical check requires outcome fail", message)

    def test_current_ledger_evidence_must_match_audited_state(self) -> None:
        record = valid_record()
        stale = copy.deepcopy(record["evidence"][0])
        stale["id"] = "E2"
        stale["stateId"] = "stale-state"
        record["evidence"].append(stale)
        record["requirements"][0]["evidenceIds"] = ["E2"]
        message = self.assert_invalid(record)
        self.assertIn("evidence bound to auditedState", message)

    def test_low_confidence_pass_with_risks_cannot_be_ready(self) -> None:
        record = valid_record()
        record["verdicts"]["process"] = "pass_with_risks"
        record["audit"]["confidence"] = "low"
        message = self.assert_invalid(record)
        self.assertIn("low-confidence audit cannot produce a ready verdict", message)

    def test_high_risk_ready_verdict_requires_confirmation(self) -> None:
        record = valid_record()
        record["verdicts"]["process"] = "pass_with_risks"
        record["audit"]["independence"] = "self_audit"
        record["audit"]["confidence"] = "medium"
        record["audit"]["risk"] = "high"
        record["audit"]["humanConfirmation"] = "unavailable"
        message = self.assert_invalid(record)
        self.assertIn("high-risk ready verdict requires obtained confirmation", message)

    def test_resolved_stop_ship_finding_remains_in_history(self) -> None:
        record = valid_record()
        record["audit"]["iteration"] = 2
        record["findings"] = [
            {
                "id": "F1",
                "severity": "critical",
                "stopShip": True,
                "iteration": 1,
                "status": "resolved",
                "resolvedInIteration": 2,
                "title": "Prior renderer failure",
                "detail": "The first iteration failed to render.",
                "consequence": "No readable report was produced.",
                "correctiveAction": "Correct the renderer and regenerate.",
                "evidenceIds": ["E1"],
            }
        ]
        state = record["audit"]["subject"]["auditedState"]
        record["corrections"] = [
            {
                "iteration": 2,
                "priorState": "prior-state",
                "newState": state,
                "summary": "Corrected the renderer.",
                "findingIds": ["F1"],
                "evidenceIds": ["E1"],
            }
        ]
        overall, output = self.generate(record)
        self.assertEqual(overall, "pass")
        self.assertIn("Resolved", output.read_text(encoding="utf-8"))

    def test_process_warning_cannot_hide_under_process_pass(self) -> None:
        record = valid_record()
        record["processChecks"][0]["status"] = "warning"
        message = self.assert_invalid(record)
        self.assertIn("warning process check cannot produce process pass", message)

    def test_unsafe_source_url_is_rejected(self) -> None:
        record = valid_record()
        record["evidence"][0]["sourceUrl"] = "javascript:alert(1)"
        message = self.assert_invalid(record)
        self.assertIn("credential-free HTTPS URL", message)

    def test_evidence_cannot_postdate_report(self) -> None:
        record = valid_record()
        record["evidence"][0]["observedAt"] = "2026-07-10T16:31:00+02:00"
        message = self.assert_invalid(record)
        self.assertIn("cannot be later than audit.generatedAt", message)


if __name__ == "__main__":
    unittest.main(verbosity=2)
