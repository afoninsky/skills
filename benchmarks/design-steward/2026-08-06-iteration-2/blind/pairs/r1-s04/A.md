# Three provisional information architectures

These are concept models for testing, not implementation-ready site maps. The missing object model, vocabulary, real content, and access rules could materially change every option. I would not use lorem ipsum: it hides label length, hierarchy, and comprehension problems. Use clearly marked representative placeholders instead.

## 1. Object-first

Best when users primarily find, manage, and relate durable records.

- Home
- [Primary object plural]
  - All [objects]
  - My [objects]
  - Create [object]
  - [Object detail]
    - Overview
    - Activity
    - Related [secondary objects]
    - Access
- [Secondary object plural]
- Reports
- Administration
- Help

Risk: premature object names and boundaries become embedded in navigation. Test ambiguous ownership, cross-object relationships, and whether users recognize the proposed nouns.

## 2. Task-first

Best when users arrive with a small set of recurring goals and do not need to understand the underlying data model.

- Home
- Start [core task]
- Review work
  - Assigned to me
  - Waiting on others
  - Completed
- Find and manage records
- Monitor outcomes
- Team settings
- Help

Risk: tasks overlap or change by role, creating duplicate pathways. Test novice versus expert expectations, task frequency, interrupted work, and handoffs.

## 3. Lifecycle-first

Best when work progresses through a stable, shared sequence.

- Home
- Intake
- In progress
- Review
- Approved / completed
- Archive
- Insights
- Administration
- Help

Each stage contains filtered [work items], with a detail view for status, ownership, history, related records, and next actions.

Risk: real work may skip, repeat, or branch between stages. Test exceptions, bulk work, reopened items, and parallel review.

## Required validation before choosing

For each option, prototype the same five scenarios using real terminology and content: first-time creation, finding an existing item, a long translated label, an empty result, and a failed or unauthorized action. Include three permission states: full access, partial visibility, and no access. Show whether inaccessible destinations are hidden, disabled, or visible with an explanation.

Choose only after agreeing on primary objects, canonical labels, representative records, lifecycle rules, and role/permission behavior. The decision should be based on task success and comprehension, not stakeholder preference.
