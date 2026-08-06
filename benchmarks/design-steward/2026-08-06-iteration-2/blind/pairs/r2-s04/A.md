I can create three provisional information architectures now, but choosing one would be premature. Lorem ipsum is safe for body-copy volume; it is not safe for navigation labels, object names, permissions, errors, or empty states because those determine the structure itself.

## Working assumptions

- The product contains user-managed records, grouped into workspaces.
- Users commonly browse, create, search, review, and administer those records.
- “Record,” “workspace,” and “activity” are placeholders, not canonical product terms.
- Permissions may vary by workspace and record.

## IA 1: Object-first

Best when users repeatedly manage a small set of stable objects.

- Home
- Records
  - All records
  - My records
  - Recently viewed
  - Create record
- Workspaces
  - Workspace overview
  - Members
  - Activity
- Search
- Administration
  - People and access
  - Settings

Risk: this architecture will be misleading if “records” are actually several distinct objects with different lifecycles.

## IA 2: Workflow-first

Best when user intent and process stage matter more than object type.

- Home
- Create
- In progress
- Needs review
- Completed
- Archive
- Search
- Team
- Administration

Each workflow view can group items by workspace or object type. Risk: stages may not be universal, linear, or visible to every role.

## IA 3: Workspace-first

Best when access, ownership, and collaboration are primarily scoped to a workspace.

- Home
- Workspaces
  - Overview
  - Records
  - Activity
  - Members
  - Workspace settings
- Shared with me
- Search
- Personal settings
- Organization administration

Risk: users working across many workspaces may face excessive switching and fragmented search.

## Required states in every option

For each destination, prototype: representative populated content; realistic longest labels; first-use and filtered-empty states; loading; recoverable and blocking errors; read-only access; hidden fields; denied actions; and partial workspace access. Do not use lorem ipsum for these structural tests.

## Decision gate

Before selecting an IA, run a short object-and-language workshop, then test the three models with 5–8 representative tasks across at least two permission levels. The decision should be based on task completion, label comprehension, cross-scope navigation, and permission clarity. Until then, treat these as testable hypotheses, not approved navigation.
