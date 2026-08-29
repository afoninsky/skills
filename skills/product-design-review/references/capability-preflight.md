# Capability preflight for review

Before recommending setup or changing a tool, read the relevant sections of the suite's canonical tool selection baseline from the sibling `product-design/references/tool-selection-baseline.md` skill resource. It explains why the free-first defaults were chosen and what an alternative must prove. If that resource is unavailable, stop any toolchain-change proposal and request installation of the complete `product-design` suite; do not recreate the comparison from memory.

Run this before accepting substitutions. The reviewer must disclose whether it can inspect the real target and support each requested conclusion.

## Canonical statuses

- `available` — verified now with a safe version, list, runtime, device, or access probe.
- `missing-blocking` — absent/inaccessible and the requested conclusion has no honest evidence route.
- `missing-degradable` — absent/inaccessible but a named partial review remains useful after owner confirmation.
- `unknown` — presence, identity, or access cannot be established safely. Treat the affected conclusion as blocked.
- `not-applicable` — current architecture or review question does not require the capability; explain why.

Do not invent additional statuses. Configuration without a successful probe is `unknown`.

Capability status and evidence disposition are separate. Label every gate or conclusion that lacks sufficient evidence exactly `Not evidenced` while retaining the capability's canonical status.

## Keep the request stage-local

Build the capability table from the current review question and its conclusions. A likely later change or implementation may need additional tooling, but that future need is a forecast until the router selects that worker. It must not block review or appear in the current exact next action.

When a tool spans stages, state why it is needed now. For example, Maestro or an equivalent may be a current review requirement when repeatable native-flow evidence is part of the review; it is not a current requirement merely because a later protected change will need regression evidence. This distinction must be visible in the user-facing request.

## Discover and verify

1. Read `design/toolchain.json` when present as intended configuration, never as freshness proof.
2. Inspect manifests, lockfiles, test/CI configs, stories/previews, wrapper/native projects, analytics notes, baseline manifests, and producer code.
3. Inspect callable tools/MCPs and use harmless live probes. A listed MCP that cannot read its target is `unknown`.
4. Probe local tools read-only: Git identity/status, package-manager scripts, Playwright/browser list, `maestro --version`/device list, `xcodebuild -version`/schemes, Gradle tasks/devices, `flutter doctor`, and existing test listing.
5. Bind a running target to the frozen Git/build/deployment identity.
6. Probe external evidence read-only and minimally; never print credentials, private URLs, participant data, session content, or account identifiers.

Review does not modify `design/toolchain.json`. Include proposed observations in the handoff with observation time, version, access scope, target, probe, and refresh trigger. The router's execution profile uses `checked_at` only after all applicable probes ran; it must be timezone-aware, no older than four hours, and no more than five minutes in the future. Re-probe sooner whenever phase, platform, claim, target/build, environment/access, version, or observed status changes.

Candidate and Gate F review questions use a non-empty representative platform matrix: at least one configuration for every materially distinct implementation/adaptation class in the claim, with explicit exclusions. For `shared-web-wrapper`, inspect both browser and packaged shell while keeping their common source ownership clear.

## Capability matrix

| Capability | Active when | Missing result |
|---|---|---|
| Git or equivalent target-state fingerprint | Always | `missing-blocking` |
| Accepted contract/reference/baseline identity | Fidelity/drift review | `missing-blocking` for drift claims; current-state inventory may be `missing-degradable` |
| Real browser/app runtime and representative capture | Visual, UX, or release review | `missing-blocking` for acceptance; source-only audit may be `missing-degradable` |
| Platform accessibility automation/inspection and manual plan | Accessibility or release review | `missing-blocking` for acceptance |
| Playwright + axe | Web/PWA runtime/accessibility | `missing-blocking` for web acceptance unless an equivalent real-browser path is proven |
| Maestro/native UI execution | Mobile runtime | `missing-blocking` for mobile acceptance unless equivalent device execution is proven |
| Native accessibility tools | Apple/Android/RN/Flutter mobile | `missing-blocking` for accessibility acceptance |
| Existing component workbench/previews | Component-state/system audit | `missing-degradable` only when equivalent deterministic fixtures are absent |
| Physical device/Test Lab | Device-specific or release-matrix claim | `missing-blocking` for that claim; otherwise `not-applicable` or `missing-degradable` |
| Cloudflare/existing preview | Reviewer cannot run a web target locally | `missing-degradable`; local runtime may make it `not-applicable` |
| Firebase App Distribution/existing signed build | Reviewers/testers need a mobile candidate | `missing-degradable`; installed local build may make it `not-applicable` |
| Clarity/telemetry evidence | Post-launch behavior question names it | `missing-blocking` for that behavior claim; heuristic review remains separate |
| Lyssna/moderated representative-user evidence | Usability/comprehension/preference/validation claim | `missing-blocking` for that claim |
| Penpot exact design source | Fidelity detail absent from exports/contract | `missing-degradable` or `missing-blocking` depending on the decision |

Hard gates cannot be waived. The owner may confirm a narrower review question, not convert missing evidence into a pass.

## Missing-capability response

Before running a partial review, state:

1. capability and canonical status;
2. probe performed and observed result;
3. exact claim/surface/configuration lost;
4. setup or access steps from [tool-setup.md](tool-setup.md);
5. verification probe after setup;
6. one specific choice: set up, grant read access, provide equivalent evidence, or confirm the named partial review.

The exact next action asks only for the current review's missing capability. Put later-stage requirements under a separate forecast heading without installation instructions unless the user explicitly asks to prepare the later stage too.

Do not ask about irrelevant tools. If an underlying deterministic capability is available, an absent MCP is normally `not-applicable` rather than degradation.

## MCP boundary

- Penpot MCP can read exact design context; contract/export remains authority.
- Playwright MCP can explore a browser; checked-in tests/traces/captures remain evidence.
- Maestro MCP can inspect a device; YAML/native flows and captures remain evidence.
- Storybook MCP can discover states; story source and real render remain evidence.
- Clarity MCP is not required; authorized read-only dashboard access or sanitized exports can supply behavioral signals.

MCP access never accepts a baseline, proves usability, or authorizes an external write.
