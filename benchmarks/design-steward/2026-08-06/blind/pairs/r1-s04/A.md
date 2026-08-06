I can create three structural hypotheses now, but they should not be mistaken for validated architectures. Lorem ipsum is fine for body-copy volume; it is unsafe for navigation labels, object names, permissions, and system states because it hides the decisions the IA needs to expose. I’ll use explicit placeholder tokens instead.

### 1. Object-centered IA

Best when people primarily find, inspect, and manage durable things.

- Home
- [Primary objects]
  - All [objects]
  - My [objects]
  - Create [object]
  - [Object detail]: Overview, Activity, Related [objects], Access
- [Secondary objects]
- Reports
- Administration

Risk: weak if users think in goals rather than objects. The relationship model and canonical object names must be settled before this can scale.

### 2. Task-centered IA

Best when users arrive to complete a small set of recurring jobs.

- Home
- [Start core task]
- [Review incoming work]
- [Track active work]
- [Resolve exceptions]
- History
- Reports
- Settings

Each task can use the same sequence: Start → Provide details → Review → Submit → Outcome.

Risk: the same object may appear in several tasks, creating duplication and unclear ownership. We need representative workflows, frequency, and role differences to rank tasks honestly.

### 3. Lifecycle-centered IA

Best when work moves through meaningful stages and handoffs.

- Overview
- Intake
- In progress
- Waiting / Blocked
- Review
- Completed
- Exceptions
- Administration

Within each stage: queue, filters, item detail, activity, and permitted actions.

Risk: stages often vary by object type or team. A universal lifecycle can become misleading unless status definitions and transition rules are shared.

### Required validation before choosing

Build one small content pack containing 8–12 realistic records, the longest plausible labels, one first-use empty state, one no-results state, two recoverable errors, and a permissions matrix for full, partial, and read-only access. Then test three representative find-and-act scenarios against all three hypotheses.

Until those inputs exist, my default starting hypothesis is **object-centered**, with task shortcuts on Home and lifecycle views inside each object collection. It is usually the least brittle combination—but that is a reversible assumption, not a recommendation.
