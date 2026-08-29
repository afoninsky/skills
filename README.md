# AI Agent Skills

[![Verify skills](https://github.com/afoninsky/skills/actions/workflows/verify.yml/badge.svg)](https://github.com/afoninsky/skills/actions/workflows/verify.yml)
[![skills.sh](https://skills.sh/b/afoninsky/skills)](https://skills.sh/afoninsky/skills)

Public, installable skills for AI coding agents. Each skill follows the open `SKILL.md` format and can be discovered by the [`skills` CLI](https://github.com/vercel-labs/skills).

## Install

Install all skills from this repository:

```bash
npx skills add afoninsky/skills
```

Install one skill:

```bash
npx skills add afoninsky/skills --skill agent-work-auditor
npx skills add afoninsky/skills --skill marktplaats-ad-creator
```

`product-design` is a router over seven focused worker skills. Install the suite together for normal use:

```bash
npx skills add afoninsky/skills \
  --skill product-design \
  --skill product-design-discovery \
  --skill product-design-direction \
  --skill product-design-contract \
  --skill product-design-prototype \
  --skill product-design-implementation \
  --skill product-design-change \
  --skill product-design-review
```

Installing an individual worker is supported only for explicit advanced or automated use. A router with a missing selected worker stops and provides suite-installation instructions instead of impersonating it.

Add `-g` to install globally instead of into the current project:

```bash
npx skills add afoninsky/skills --skill agent-work-auditor -g
```

Review a repository's available skills before installing:

```bash
npx skills add afoninsky/skills --list
```

## Skills

### Product Design suite

Use `$product-design` as the common entrypoint for UI/UX work across responsive web, iOS, Android, React Native, Flutter, and shared web/mobile wrappers. It preserves the original request, inspects current project state, checks applicable tool capabilities, and routes the earliest missing prerequisite through one or more focused workers:

- `product-design-discovery`
- `product-design-direction`
- `product-design-contract`
- `product-design-prototype`
- `product-design-implementation`
- `product-design-change`
- `product-design-review`

The suite keeps accepted design decisions in versioned contracts, source maps, framework-native component states, and deterministic browser/app-runtime baselines. A change worker cannot update approved screenshots. Gate D disposes a reviewed candidate, Gate E separately authorizes the exact named candidate and matrix as the new accepted identity, and only the following contract `accept-freeze` records that identity. Review also owns release and research/learning evidence packets and stops for the owner's Gate F decision.

Tool dependencies are capability-based. Git, Penpot, CSS variables or DTCG/Style Dictionary, framework workbenches, Playwright, Maestro, accessibility tools, preview/distribution services, and user-evidence tools are selected only when the phase and platform need them. Missing applicable capabilities are never hidden: the skill explains the loss, provides current official setup steps, and stops for setup or explicit confirmation of a limited degraded route. Missing hard runtime or accessibility evidence stops implementation and change before production writes; confirmed reduced work moves to read-only review, contract planning, or an isolated prototype with its own valid preflight. Missing evidence still cannot pass its gate.

The suite includes a dated [tool-selection baseline](skills/product-design/references/tool-selection-baseline.md) describing where each recommendation belongs, why it passed the maturity/free-capacity/functionality filters, its limits and alternatives, and the representative comparison and rollback proof required before replacement.

Executable preflight records use a non-empty representative platform set for direction, contract, prototype, implementation, protected change, and acceptance. `checked_at` certifies that every applicable status was actually probed within the previous four hours and is no more than five minutes ahead of the current clock; changing phase, platform, claim, target, build, access, or tool state requires an earlier re-probe.

[Read the entrypoint](skills/product-design/SKILL.md)

[Use the Product Design suite](docs/product-design.md)

### Agent Work Auditor

An evidence-first audit of completed agent work. It checks requirement fidelity, completion and causal claims, test validity, regressions, process integrity, privacy and security risk, and delivery readiness.

The skill freezes the exact target state, reconstructs requirement and claim ledgers, runs independent empirical checks, challenges tests and generated artifacts, and produces validated JSON plus a standalone HTML report. Use it explicitly after material work when an unsupported completion claim, synthetic evidence, wrong-environment verification, or costly regression would affect acceptance.

The workflow was created from the testing and agent-workflow lessons described in Dan Luu's ["Agentic test processes, LLM benchmarks, and other notes on agentic coding from Galapagos Island"](https://danluu.com/ai-coding/). The article is the conceptual source, not an endorsement of this implementation.

Requirements: Python 3.10 or newer for the bundled report generator. Other verification tools depend on the work being audited.

[Read the skill](skills/agent-work-auditor/SKILL.md)

### Marktplaats Ad Creator

Creates Dutch Marktplaats.nl listings from product images and seller details. It researches current comparables when pricing is needed, adapts recommendations to the seller's goal, drafts accurate listing copy, and can prepare the listing in a browser.

The skill supports quick-sale, balanced, maximum-value, fixed-price, and seller-defined strategies. Bidding, Direct Kopen, negotiation, trade language, delivery, and paid promotion are explicit user choices rather than inherited defaults. Browser actions stop at the final review screen for approval before publishing.

This is an unofficial automation aid and is not affiliated with or endorsed by Marktplaats. It does not bypass CAPTCHA, access controls, or platform limits.

Requirements: image input and browser control for the complete workflow. Without browser control, the skill can still research and draft a listing for manual posting.

[Read the skill](skills/marktplaats-ad-creator/SKILL.md)

## Verification

Pull requests and pushes to `main` run:

- skill metadata, link, JSON, Python syntax, symlink, private-path, and sensitive-data checks;
- Python linting and tests on Python 3.10 and 3.14;
- deterministic regeneration of the auditor's standalone HTML example;
- discovery and clean installation of every skill with a pinned `skills` CLI version;
- full-history secret scanning with Gitleaks.

Run the local checks:

```bash
python3 scripts/verify_skills.py --repository .
python3 -m unittest tests/test_verify_skills.py -v
python3 -m unittest tests/test_product_design_suite.py -v
python3 skills/product-design/scripts/test_validate_route.py
python3 skills/product-design/scripts/test_validate_toolchain.py
python3 skills/product-design-contract/scripts/test_validate_design_contract.py
python3 skills/product-design-change/scripts/test_change_guard.py
python3 skills/product-design-implementation/scripts/test_check_protected_paths.py
python3 skills/product-design-review/scripts/test_classify_visual_evidence.py
python3 skills/agent-work-auditor/scripts/test_generate_report.py
npx --yes skills@1.5.16 add . --list
```

## License

[MIT](LICENSE)
