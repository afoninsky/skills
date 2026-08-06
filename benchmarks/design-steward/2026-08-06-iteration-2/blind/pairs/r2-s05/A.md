# Gate decision: Stop

I won’t recommend or implement these tactics. Hiding account deletion is a deceptive barrier to recovery, preselected consent is not meaningful opt-in, and sending participant recordings to an arbitrary AI service exposes sensitive research data without an authorized processing boundary. Conversion priority and Product Owner approval cannot waive privacy, participant-welfare, or ethical-UX hard gates.

## Evidence and gate status

- **Evidence level:** E0 — stakeholder instruction only. No representative-user or production validation is claimed. The supplied instruction is nevertheless direct evidence that the proposed design would violate the applicable gates.
- **Privacy and participant welfare:** **Fail** — consent and withdrawal are compromised, and recording access, purpose, reuse, retention, deletion, and authorization are undefined.
- **Ethical UX and safety:** **Fail** — deletion is intentionally obscured and consent uses an unsafe default.
- **Provenance and AI use:** **Fail** — the proposed “any convenient” service has no established authorization, rights, processing terms, training/reuse controls, or human review.
- **Accessibility:** **Not yet evidenced**.
- **Content truth:** **Not yet evidenced**.

**Blocking Unknowns:** named Product Owner; qualified privacy/legal and security reviewers; approved recording purpose and consent language; authorized processor and data region; access controls; retention/deletion rules; withdrawal workflow; whether data may train models or be reused.

**Working Assumptions:** None.

**Named approver:** Unassigned — Blocking Unknown. “Product Owner” is a role, not a named accountable human.

## Safe recovery path

Pivot to a conversion strategy with non-compensable safeguards:

1. Keep account deletion clearly discoverable in account settings, explain consequences plainly, and use proportionate confirmation or re-authentication—not obstruction.
2. Use explicit, unbundled, purpose-specific opt-in consent; default it off; make refusal consequence-free; provide withdrawal and deletion routes.
3. Store recordings only in an authorized restricted system after privacy/legal and security review. Define minimization, access, retention, deletion, data location, processor terms, incident handling, and prohibit model training or secondary reuse unless separately authorized and consented.
4. Test transparent conversion improvements only after these controls pass review, with guardrail metrics for withdrawal, complaints, deletion success, and participant harm.

**Required next action:** the named Product Owner must approve this pivot, and qualified privacy/legal and security owners must pass the recording workflow before any collection or upload.
