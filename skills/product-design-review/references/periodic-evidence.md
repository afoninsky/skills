# Periodic and post-launch evidence

## Begin with a decision

Do not browse dashboards for generic “insights.” Name the pending decision, affected population, behavior/task, target release, time window, and what evidence would change the decision.

Examples:

- whether first-time phone users locate the primary action;
- whether a revised error state improves recovery;
- whether tablet navigation causes repeated reversals;
- whether target participants interpret a new label as intended.

## Evidence types are not interchangeable

| Evidence | Supports | Does not establish alone |
|---|---|---|
| Heuristic/agent review | hypotheses, known principle conflicts | actual user behavior or validation |
| Automated/runtime tests | deterministic correctness in covered states | comprehension, preference, real-world success |
| Session replay/heatmaps | observed interaction patterns for recorded traffic | motivation, intent, representativeness, causality |
| Product analytics | event/funnel incidence for instrumented population | why behavior occurred or visual quality |
| Support reports | reported problems and language | prevalence in the full population |
| Lyssna/unmoderated study | sampled task outcomes/responses under that method | all users or production behavior |
| Moderated observation/interview | rich task behavior and explanations in sample | prevalence without suitable sampling |
| Distribution/install data | candidate reached a device/tester | task completion, comprehension, or usability |

Triangulate when claims matter. Record contradictions instead of averaging them away.

Use the suite labels consistently: agent hypotheses E0, specialist/heuristic review E1, deterministic runtime E2, internal non-representative task observation E3, representative-user evidence E4, and consented live-product outcomes E5.

## Privacy and welfare gate

Before viewing or proposing collection, establish:

- consent/legal basis and age/population restrictions;
- masking/redaction and sensitive fields/screens;
- retention, access, export, and deletion boundaries;
- whether recordings or build uploads cross organizational boundaries;
- participant contact/recruitment authority and compensation/spend;
- the minimum data required for the named decision.

If these are unresolved, do not access or instrument. Request authorized, sanitized evidence or propose a privacy-reviewed plan.

## Analysis discipline

- Bind observations to release, platform/device, locale, time window, and population.
- Check instrumentation coverage, missing data, bot/internal traffic, sampling, and changes during the window.
- Distinguish counts from rates and define denominators.
- Treat rage/dead clicks, heat, and repeated actions as signals requiring contextual inspection.
- Preserve outliers and failure/recovery paths when they affect vulnerable or high-impact users.
- State whether a finding is hypothesis, observed behavior, representative-user evidence, or production outcome.

## Output

Turn evidence into ranked change briefs, each with decision question, observed facts, uncertainty, affected surfaces, smallest proposed scope, success/failure signals, and a verification/research plan. Review remains read-only.

When the requested outcome is a release/rollout or a named research/learning action, assemble the decision packet and stop at Gate F. The owner releases/holds or approves/revises/rejects the action. Leave the next worker unset until that decision. If claim-required evidence or privacy/authority is missing, stop blocked before Gate F and request setup, access, equivalent evidence, or a narrower question.
