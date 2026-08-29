# Discovery tool preflight

Run this preflight before research, participant contact, workspace initialization, or artifact writes. Select capabilities from the requested evidence, not from a preferred tool brand.

## Capability classes

| Class | Meaning | Missing-capability response |
| --- | --- | --- |
| Required | Discovery cannot leave durable, inspectable results without it | Stop and request setup; no degraded completion |
| Conditional | Required only because the prompt, target, or evidence gate needs it | Stop that workstream; offer setup or an explicitly limited continuation when safe |
| Optional | Improves speed or fidelity but has a valid canonical fallback | Disclose the missing adapter and use the named fallback only after confirmation when output materially differs |

## Phase matrix

| Capability | Class | Preferred evidence/tool | Canonical fallback or limit |
| --- | --- | --- | --- |
| Read and write project artifacts | Required | Workspace filesystem | None |
| Version, diff, and recover accepted artifacts | Conditional; required for Gate A acceptance or pipeline continuation | Git; GitHub review is optional | An unversioned draft may be `missing-degradable`, but it cannot become an accepted continuing-pipeline artifact |
| Inspect an existing product repository | Conditional | Repository search, manifests, tests | User-provided architecture packet; otherwise existing-product claims are blocked |
| Research current external facts | Conditional | Web access to primary sources | User-provided authoritative sources; otherwise mark the factual question blocked |
| Observe an existing app flow | Conditional | Real browser, simulator/emulator, or device access | Supplied recordings/screenshots may support limited observations, never runtime claims |
| Gather representative-user evidence | Conditional | Moderated sessions or an existing research process; Lyssna may structure a study | No model-only substitute. Assumption-only continuation cannot satisfy a user-evidence gate |
| Edit structured flows/wireframes | Optional | Penpot Free; official MCP on demand | Git-owned Mermaid, SVG, or disposable HTML/text flow |
| Review/approve changes | Optional | GitHub protected review | Local Git diff plus explicit owner approval record |

Penpot is optional. Its MCP is a replaceable adapter to the currently open design file, not the source of truth. Export reviewed artifacts to Git. Lyssna is optional; relevant participants and a sound research question are the capability that matters.

## Availability checks

1. Inspect the runtime's callable tools and installed skills. Do not assume a named MCP exists because documentation mentions it.
2. Verify file read/write access with a non-destructive inspection; do not create the design workspace yet.
3. Run `git --version` and, when a repository exists, `git rev-parse --show-toplevel` and `git status --short`. Preserve unrelated user changes.
4. For a conditional web-research need, confirm a live search/open capability before promising current facts.
5. For an existing runtime, confirm that the browser/device can actually open the relevant target; a CLI installed without a runnable target is not available.
6. For Penpot MCP, first list/inspect the open file read-only. Write access is not needed for discovery unless the user requests editable flows.
7. For participant research, confirm recruitment authority, consent/privacy handling, target criteria, and access to the study—not merely an account.

Use exactly the suite status vocabulary:

- `available` — proven by a version/configuration/connection probe or existing artifact;
- `missing-blocking` — the phase cannot produce required evidence;
- `missing-degradable` — bounded work may continue with reduced evidence after confirmation;
- `unknown` — not verified; probe safely or treat as missing;
- `not-applicable` — not selected for this request.

Report a compact table with: capability, class for this request, selected adapter, exact status, evidence of the check, consequence, and next action. When a project workspace exists, persist tool, version, environment, evidence, degradation, and confirmation ID in `design/toolchain.json`; never store credentials.

## Missing capability protocol

Never omit the gap and continue as if evidence were equivalent.

1. Name the missing capability and the exact discovery output or claim it affects.
2. Mark it `missing-blocking` or `missing-degradable` and state whether it blocks the phase, blocks one workstream, or permits a safe degraded draft.
3. Offer **Set up** and, only when safe, **Continue in degraded mode**. Describe the precise limitation and the gate that will remain unpassed.
4. Ask the user to choose. Do not treat silence as consent.
5. If setup is requested, browse the current official documentation at that moment because commands, versions, account limits, and client configuration change. Provide:
   - why this is the smallest suitable tool;
   - OS/runtime prerequisites;
   - step-by-step installation or account configuration;
   - least-privilege/read-only configuration first;
   - a verification command or read-only probe;
   - where canonical exports will live in Git;
   - uninstall, disconnect, or rollback steps.
6. Re-run the availability check after setup and update `design/toolchain.json`. Do not accept “installed” without a working probe.

Keep MCP tokens out of prompts, logs, screenshots, and Git. Do not expose a local MCP listener beyond its trusted local boundary.

Useful official starting points to re-verify, not frozen installation instructions:

- [Git installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Penpot MCP](https://help.penpot.app/mcp/)
- [Lyssna study setup](https://help.lyssna.com/en/collections/9546028-setting-up-your-study)

## Hard evidence gates

These cannot be waived by “continue anyway”:

- no representative participants means no representative-user validation claim;
- no authoritative source means no high-stakes/current factual conclusion;
- no runnable product means no claim about actual interaction, accessibility tree, performance, or adaptive behavior;
- no durable versioned artifact means Gate A cannot be recorded as accepted for a continuing pipeline.

A degraded draft may still be useful. Mark it `unverified`, record the affected gate as `Not evidenced`, list the missing checks, set the handoff status to `blocked` or `needs-owner` as appropriate, and prevent the router from advancing through that gate.
