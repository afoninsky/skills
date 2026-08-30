# Evidence and platform coverage

## Evidence labels

Use the lowest accurate level for each claim:

| Label | Meaning | Appropriate claim |
| --- | --- | --- |
| E0 | Agent judgment, inference, or generated hypothesis | “Candidate assumption” |
| E1 | Specialist or structured heuristic review | “Expert/heuristic finding under stated limits” |
| E2 | Deterministic artifact/runtime evidence, including tests, traces, or verified first-party constraints | “Observed or deterministically supported in this scope” |
| E3 | Internal human task evidence from non-representative reviewers | “Observed with these internal reviewers” |
| E4 | Representative participant evidence | “Observed with this sample and method” |
| E5 | Post-launch behavior/outcome evidence with appropriate consent | “Observed in released use under stated limitations” |

Higher is not automatically better; it answers a different question. Supplied facts, stakeholder preferences, and source documents retain their explicit provenance rather than receiving an inflated evidence label. Runtime evidence does not establish desirability, and participant preference does not establish accessibility or technical feasibility.

Every evidence record needs an ID, claim/finding, level, source or artifact path, date when time-sensitive, scope, affected decision, limitation, and disposition. Do not retain raw sensitive participant data in a public design directory.

## Research rules

- Search only after naming the decision and knowledge gap.
- Reuse evidence only when its audience, decision, business model, geography, platform, and material conditions still apply; refresh only changed or time-sensitive gaps.
- Prefer standards bodies, platform owners, regulators, first-party product documentation, and original research.
- When facts may have changed, verify them live and cite the supporting page near the claim.
- Distinguish observed product patterns, research or standards, what people do or say, and what we recommend; one does not prove another.
- Select comparison products for a named decision. Verify “top” or “leader” claims or call them representative, and inspect the relevant journey rather than only a homepage; use direct, adjacent, or counterexamples only when they clarify a tradeoff.
- Stop when each activated gap yields a bounded design implication or an explicit unresolved question; more sources without decision value add noise.
- Do not use generated personas, synthetic interviews, generic critique services, or a model's taste as representative-user evidence.
- Contacting people, ordering panel responses, spending credits, recording sessions, or accessing sensitive data requires explicit authority.

## Representative target considerations

Choose only relevant rows, then state exclusions:

| Concern | Web | Native/cross-platform mobile | Shared web wrapper |
| --- | --- | --- | --- |
| Form factors | phone, tablet, desktop, wide desktop | phone, tablet/foldable where supported | responsive web sizes plus packaged shell |
| Inputs | touch, pointer, keyboard | touch, hardware keyboard, assistive input | web inputs plus native back/keyboard behavior |
| Layout | reflow, zoom, browser chrome | orientation, window classes/size classes, safe areas | reflow plus safe areas/WebView insets |
| Text | zoom, locale expansion, RTL | Dynamic Type/font scaling, locale, RTL | both web text behavior and OS scaling effects |
| System states | network, permissions, browser storage | permissions, background/foreground, interruptions | web state plus native shell lifecycle |
| Accessibility | semantics, keyboard, focus, screen reader | platform semantics, screen reader, target size, motion | both layers, without duplicating the UI source |

Detect architecture before describing screens. A PWA or Capacitor-style wrapper often has one UI source plus a native-shell verification layer; it is not two separately designed component systems. React Native and Flutter share cross-platform code but still need platform-adaptive checks. SwiftUI/UIKit and Compose/Views use native preview and semantics conventions.

## Coverage closure

Before calling the discovery question complete, map each material role, journey branch, state, destination, and target to one of:

- covered by a named brief/experience-map section;
- intentionally excluded with owner-visible rationale;
- unresolved gap with an owner or evidence action.

Do not hide missing coverage behind “existing behavior,” “standard mobile behavior,” or a polished central flow.
