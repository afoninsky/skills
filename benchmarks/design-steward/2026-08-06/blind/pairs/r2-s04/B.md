Below are three deliberately provisional information architectures. They are decision probes, not production-ready sitemaps. I would not use lorem ipsum for navigation or representative content: it hides label-length, hierarchy, and comprehension problems. Instead, I’ve used semantic placeholders and deliberately long test labels.

## 1. Object-centered

Best when people primarily return to find, inspect, and manage durable things.

- Home
- [Primary objects]
  - All [primary objects]
  - Recently viewed
  - Owned by me
  - Shared with me
  - Archived
- [Secondary objects]
- Collections
- Activity
- Administration
  - People and access
  - Policies
  - Integrations

Representative detail page: Overview, Related [objects], Activity, Access, Settings.

Risk: weak if users think in tasks rather than objects.

## 2. Workflow-centered

Best when progress through a repeatable process matters more than browsing a repository.

- Home
- Start new [workflow]
- My work
  - Needs my attention
  - In progress
  - Waiting on someone else
  - Completed
- Team queue
- All records
- Reports
- Administration

Representative workflow: Draft → Review → Approval → Completion, with exceptions visible rather than hidden in a generic “status.”

Risk: the same object may appear in several queues, so canonical location and URL behavior must be defined.

## 3. Goal- or audience-centered

Best when users have distinct responsibilities and rarely need the whole system.

- Home
- Create and submit
- Review and decide
- Monitor and resolve
- Explore records
- Reports and insights
- Help
- Administration

Each destination can expose role-relevant objects and actions without making internal data-model terms the top-level navigation.

Risk: overlapping roles can make destinations feel redundant or unpredictable.

## Required stress cases for all three

Prototype each architecture with these exact content conditions before choosing:

- Long label: “Items awaiting additional compliance documentation”
- Empty state: no records yet, with one meaningful next action
- Error: content failed to load, preserving navigation and retry
- Partial access: visible record, restricted section, explicit reason and access-request path
- Mixed ownership: mine, shared, unassigned, archived
- Representative volume: 3, 30, and 3,000 records

Decision criteria: first-click success on five common tasks, terminology comprehension, route predictability, and resilience under the stress cases above. Before detailed design, agree on a one-page vocabulary: candidate objects, their relationships, lifecycle states, ownership, and permission boundaries.
