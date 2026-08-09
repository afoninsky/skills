# Steward state and owner roadmap

Use this reference when starting or resuming an engagement, after a material event, before a known context compaction or handoff, and when generating the owner-facing roadmap.

## The recovery spine

`steward-state.json` is the engagement's canonical current-state and recovery file. It answers three questions without relying on conversation memory:

1. What was decided, by whom, from what evidence, and with what authority?
2. What design path produced the current recommendation or selected backbone?
3. What is the exact safe next action?

Detailed accepted records remain immutable evidence and authority sources. Link them from the state file rather than copying their full contents. No material decision needed to resume may exist only in another record, a chat message, a sub-agent return, or the Steward's memory.

## Initialize and update

Copy the starter `steward-state.json` into the engagement workspace at creation. Resolve all starter placeholders before the first grilling question.

Update the state file immediately after:

- dependency preflight or dependency failure;
- a material owner answer, Steward recommendation, disagreement, resolution, or approval;
- a changed constraint, assumption, Blocking Unknown, authorization boundary, or scope decision;
- research return and Steward evidence disposition;
- concept rejection, territory promotion, direction verdict, synthesis, or selection;
- artifact creation, revision, freeze, supersession, or removal;
- coverage closure, gate result, implementation delta, or acceptance result;
- a check becoming completed or deliberately deferred;
- a new blocker, stopping condition, handoff, pause, or exact next action.

Do not update it for routine command output, unchanged progress, formatting, or repeated successful checks. One material event may update several related fields in one edit.

## Decision contract

Each material decision entry records:

- stable decision ID and timestamp;
- decision question;
- owner-original input or `None`;
- Steward recommendation and reasoning;
- evidence and assumption IDs used;
- agreement, disagreement, or unresolved consequence;
- resolution and status;
- named decision owner and approval evidence;
- affected artifacts, requirements, gates, and scope;
- `supersedes` and `superseded_by` links when the decision changes.

Never erase a superseded decision. Change its status and link the replacement so both recovery and the roadmap show the path honestly.

## Research and materials contract

Record only research or source material that influenced a design decision or remains an active limitation. Include source title and location, observed date, evidence level, material used, design implication, limitations, rights or provenance note, and disposition. A search result with no decision effect does not belong in the recovery spine.

## Funnel and artifact contract

Keep the funnel concise:

- raw concepts: ID, thesis, core act, disposition, and one-line reason;
- territories: promise, mental model, status, representative artifact, and verdict;
- developed directions: charter, decisive states, artifacts, screenshot verdict, and status;
- selected backbone: direction ID, Owner approval, imported elements, and rejected alternatives.

Each decision-bearing artifact records a stable ID, type, path or URL, direction, states, viewports, version or hash, status, limitations, and associated decision. Review-only controls remain outside the product viewport.

## Coverage and implementation fidelity

Coverage rows map every commissioned journey, role, domain, handoff, entry, empty, return, loading, failure, recovery, completion branch, and visible global destination to an artifact or explicit exclusion.

G5 fidelity rows pair one frozen reference with one implementation capture at the same state, fixture, viewport, and crop. Record composition constraints and observed deltas for shell silhouette, navigation and dock proportions, central working width, density, whitespace, hierarchy, visual tokens, and family identity. Keep these statuses distinct:

- **Engineering source acceptance:** source, tests, semantics, and scoped browser behavior passed.
- **Design-integration acceptance:** paired-state fidelity and complete in-scope branch coverage passed under a non-implementing reviewer.
- **Preview/deployed fidelity:** the authorized production-like or deployed target was inspected with representative account states.

One status never implies another. Missing access or fixtures produces `Not yet evidenced`, not a pass.

## Restore after compaction or handoff

On resume:

1. Read `steward-state.json` completely before reading chat summaries.
2. Confirm the package version, engagement workspace, resolved grilling dependency, brief version, mode, gate, selected artifact hash, and authorization boundary.
3. Read every path in `resume.read_first` in order.
4. Inspect repository or artifact changes newer than `engagement.last_updated_at` and reconcile them explicitly.
5. Update `resume.restored_at`, `resume.restored_by`, and any stale fields.
6. Continue from `resume.exact_next_action`; if reconciliation changes it materially, record a decision before proceeding.

If the state file is missing, invalid, or materially stale, stop consequential work. Reconstruct it from accepted records and current artifacts, mark the reconstruction and uncertainty, and obtain Owner confirmation when authority or a material decision cannot be recovered.

## Generate the owner roadmap

Run:

```bash
python3 <skill-directory>/scripts/generate_engagement_roadmap.py \
  <engagement-workspace>/steward-state.json \
  --output <engagement-workspace>/steward-roadmap.html
```

Generate it at completion and on System Owner request. Regenerate after any later material decision so the HTML never becomes a manually maintained second state source.

The page is self-contained and owner-facing. Its dominant visual is a G0–G6 gate timeline. Each gate uses one of four plain-language states—**Completed**, **In progress**, **Blocked**, or **Not done**—and answers four questions: what decision or result was gained, what evidence supports it, what artifact or output it produced, and what remains before closure. Keep `roadmap[].gate`, `status`, `decision_or_result`, `evidence_ids`, `artifact_ids`, and `open_items` current so this summary remains reliable.

Supporting sections show:

- current status, authority, mode, stage, and next action;
- research and materials that influenced the work;
- material decisions, disagreements, approvals, and supersession;
- the concept funnel and rejected/promoted alternatives;
- generated mocks and the selected backbone;
- commissioned coverage and explicit gaps;
- implementation fidelity, deltas, and acceptance level;
- remaining assumptions, blockers, risks, and deferred checks.

Inspect the HTML for correct content, links, layout, and absence of external dependencies. The roadmap explains the design journey; it does not replace the state file, accepted records, product artifact, or gate decision.
