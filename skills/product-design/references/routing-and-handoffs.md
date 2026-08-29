# Routing and handoffs

## Routing model

Treat routing as a state transition, not keyword matching. Consider:

- requested outcome;
- repository readiness;
- accepted artifact identity;
- design uncertainty;
- mutation authority;
- scope and affected surfaces;
- target platforms and shared implementation;
- applicable capability evidence;
- next human gate.

The original prompt always accompanies the routing envelope. The envelope carries its UTF-8 SHA-256, and every handoff repeats that digest so compaction or resume cannot silently replace the request.

## Modes

- **Atomic:** one bounded worker, such as discovery research, read-only review, or a protected local change.
- **Pipeline:** an ordered series for a broad objective, executed only as far as the next gate.
- **Resume:** continue from accepted hashes and `exact_next_action`.
- **Reroute:** new instruction changes the sequence; record what it supersedes.

## Entry-point precedence

A raw end-user UI/UX request belongs to `product-design` unless the user explicitly names a worker or the invocation includes a valid router-issued routing envelope. Worker-domain words such as “audit,” “prototype,” “implement,” “tokens,” or “change spacing” do not bypass the router. The router may choose an atomic one-worker route, but it still owns preflight, accepted-state inspection, authority, gates, and handoff validation.

## Allowed transitions

Normal transitions are:

```text
discovery → direction | prototype
direction → contract
contract → prototype | implementation | review | change
prototype → review | implementation
implementation → review
change → review
review → change | contract
reviewed candidate → stop at Gate D for owner accept/reject/revise
Gate D acceptance → router stops at Gate E for explicit approval of the exact candidate and reviewed matrix
Gate E approval → contract:accept-freeze
contract:accept-freeze → stop after recording the approved identity; any later work starts in a fresh router envelope
review release/research/learning packet → stop at Gate F for the owner decision
```

A worker may run alone when its prerequisites already exist. Gate D acceptance cannot be reused as Gate E approval unless the user subsequently makes the separate, explicit Gate E decision naming the reviewed candidate and matrix. After accept-freeze records Gate E, the router may select any worker whose prerequisites and authority fit the next request, but that selection is a new route rather than a successor inside the baseline-mutating envelope. Gate F is review-owned and has no preselected successor. A transition outside this list requires a recorded reroute reason and must not bypass an owner gate.

## Routing envelope

Use [the routing-envelope template](../assets/routing-envelope.json). Required concepts:

- stable request ID;
- ordered remaining route and reason; the first item is always the current worker;
- current phase and mode;
- requested scope and mutation authority;
- original-prompt digest plus accepted input IDs, paths, and SHA-256 hashes;
- fixed constraints, assumptions, and unknowns;
- applicable platforms;
- capability-preflight record and any explicit degradation confirmation IDs;
- writes allowed and protected paths;
- stop condition and owner gate;
- implementation entry basis and approval ID when implementation is current;
- baseline updates fixed to false except explicit `accept-freeze`.

## Worker handoff

Use [the worker-handoff template](../assets/worker-handoff.json). Every worker reports:

- `complete`, `needs-owner`, `blocked`, or `failed`;
- exact input identity;
- artifacts created or changed;
- production mutations;
- evidence and missing evidence;
- tool degradation accepted for this run;
- baseline-change status;
- current gate;
- recommended next worker;
- exact next action.

The router independently validates the recommendation. A worker does not authorize its successor.

Before launch, validate and bind the envelope to its fresh capability record:

```text
python3 <product-design-skill-directory>/scripts/validate_route.py <routing-envelope-path> --toolchain <toolchain-path> --for-execution
```

This execution mode runs the capability validator as well as the phase/platform/gate binding checks. After the worker returns, validate envelope and handoff together with `--handoff <worker-handoff-path>`; the next worker must receive a newly probed profile and execution-bound envelope. Enforce:

- `input_hashes.original_prompt` and every accepted input hash match the envelope;
- review is read-only, production mutations have bounded authority, and non-production workers report none;
- a handoff gate is null or A–F, matches `owner_gate`, and uses `needs-owner`;
- blocked or failed work recommends no successor;
- a recommendation is a known allowed transition and matches the declared next route item;
- every degraded capability names a confirmation ID authorized by the envelope;
- baseline mutation occurs only in a completed contract `accept-freeze` handoff.

A gate prevents advancement. After explicit approval, create a new envelope with the approved successor as its first route item, bind the approval ID, rebuild capability preflight, and validate again. Gate E is a router boundary: once the owner approves the exact Gate D-reviewed identity, the new envelope contains only contract `accept-freeze`. Gate F remains at review with `recommended_next_worker: null` until the owner decides.

## Ambiguous requests

### Discovery or review

- Users, jobs, product flow, information architecture, content needs, and required states → discovery.
- Quality, consistency, fidelity, accessibility, or performance of an existing candidate/runtime → review.

### Direction or prototype

- Aesthetic language, brand fit, hierarchy grammar, visual references, and distinct options → direction.
- Interaction behavior, layout feasibility, state transitions, or a representative proof → prototype.

### Implementation or change

- New approved component/surface following the existing contract → implementation.
- Any edit that may alter an accepted component, token, surface, behavior, or golden → change.

### Review and fix

Run review first. If findings are local and mutation authority is explicit, route each approved finding through change. If a finding reopens visual direction, content hierarchy, navigation, or shared system rules, stop for the relevant gate.

### Existing product with a vague improvement request

“Make it prettier,” “improve the UX,” or “fix the design” starts with read-only review. Treat blanket fix intent as mutation authority in principle, not approval for unknown deltas. Produce bounded change briefs and obtain owner confirmation before change. Reopen discovery or direction only when findings show foundational decisions are unresolved.

### Shared token or component

Changing the value or behavior of an accepted shared token or component routes to change and expands to every mapped consumer. Replacing or consolidating the source of truth without an intended visual or behavioral delta routes to contract re-architecture.

### Approved design to code

An approved mock may route directly to implementation only when it is immutable and named, covers required states and target adaptations, can be mapped unambiguously to the existing component system, and has a recorded `bounded-reviewed-slice` approval ID. If those rules or mappings are missing, route to contract first. New, multi-surface, or high-impact work goes through a representative prototype and Gate C; the later implementation envelope records `gate-c-approved` and its approval ID.

### Visual baseline requests

Any request to regenerate, update, accept, or freeze screenshots or goldens routes through `product-design`. Without a completed Gate D candidate decision, route to review. Gate D acceptance then stops at Gate E for separate explicit approval of the exact candidate, reviewed matrix, and observed diffs. Only that Gate E approval routes to contract accept-freeze. Passing CI, an agent preference, or a snapshot-update request is not acceptance.

### Update snapshots

Updating files is not acceptance. Route to `accept-freeze` only after Gate D and when the human then explicitly approves the named candidate, reviewed matrix, diffs, and limitations at Gate E.

## Failure and recovery

On missing worker, tool failure, invalid handoff, or interrupted work:

1. preserve existing accepted state;
2. mark the active route `blocked` or `failed` without changing the accepted artifact hashes;
3. record the exact error/evidence;
4. give one recovery action;
5. do not launch a later worker.
