# Evolution redesign — intake decision

**Decision in scope:** Whether to begin design direction generation for an Evolution redesign while preserving every legacy convention.

**Proposed gate outcome:** **Iterate at G1 (Brief)**. Direction generation must not begin yet.

**Named approver:** **Unassigned — Blocking Unknown**. A human Product Owner must be named and approve the Design Brief; the Steward can recommend but cannot supply that authority.

The goal—retain what users already know while modernizing the UI—is a useful intent, but “treat all legacy conventions as Fixed” is not an admissible shortcut. In Evolution mode, each Fixed constraint needs a source, rationale, and decision owner. An unspecified convention is **Open when safe**; when changing it could materially affect users, journeys, meaning, accessibility, safety, or the comparison rubric, it is a **Blocking Unknown**. Existing implementation alone is not evidence that a convention is binding.

## Unknowns

**Blocking Unknowns**

- Named Product Owner and exact approval authority.
- Inventory of legacy conventions, including which ones users rely on and for which tasks and contexts.
- Source, rationale, and owner for every proposed Fixed convention.
- Target users, priority journeys, desired outcomes, non-goals, and affected people or harms.
- Representative content, canonical terminology, data conditions, and critical, error, empty, permission, loading, and hostile states.
- Accessibility, content-truth, privacy, ethics, legal, safety, technical, platform, localization, asset-rights, and measurement constraints.
- Frozen comparison rubric, evidence thresholds, permissions, and clean-room boundary.

**Working Assumptions:** None. The missing facts could materially change the redesign and cannot safely be downgraded.

## Evidence and hard gates

**Evidence level:** **Not yet evidenced**. No source-backed or representative-user evidence supports the claim that every legacy convention must remain fixed. No validation claim can be made.

- Accessibility: **Not yet evidenced**
- Content truth: **Not yet evidenced**
- Privacy and participant welfare: **Not yet evidenced**
- Ethical UX and safety: **Not yet evidenced**
- Provenance and rights: **Not yet evidenced**

## Fastest safe next step

Name the Product Owner, create brief version 0.1, and run a short convention triage: classify each convention as **Fixed**, **Challengeable**, **Open**, or **Blocking Unknown**, recording source, rationale, owner, user/task impact, and evidence plan. Preserve confirmed Fixed items; keep Challengeable items in force until an evidence-backed alternative is approved; redesign Open areas. Then obtain exact Product Owner approval of the brief and frozen rubric before generating independent directions.

No direction, implementation, production change, or launch is authorized by this intake decision.
