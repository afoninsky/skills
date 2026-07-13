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

Add `-g` to install globally instead of into the current project:

```bash
npx skills add afoninsky/skills --skill agent-work-auditor -g
```

Review a repository's available skills before installing:

```bash
npx skills add afoninsky/skills --list
```

## Skills

### Agent Work Auditor

An evidence-first audit of completed agent work. It checks requirement fidelity, completion and causal claims, test validity, regressions, process integrity, privacy and security risk, and delivery readiness.

The skill freezes the exact target state, reconstructs requirement and claim ledgers, runs independent empirical checks, challenges tests and generated artifacts, and produces validated JSON plus a standalone HTML report. Use it explicitly after material work when an unsupported completion claim, synthetic evidence, wrong-environment verification, or costly regression would affect acceptance.

The workflow was created from the testing and agent-workflow lessons described in Dan Luu's ["Agentic test processes, LLM benchmarks, and other notes on agentic coding from Galapagos Island"](https://danluu.com/ai-coding/). The article is the conceptual source, not an endorsement of this implementation.

Requirements: Python 3.10 or newer for the bundled report generator. Other verification tools depend on the work being audited.

[Read the skill](skills/agent-work-auditor/SKILL.md)

### Marktplaats Ad Creator

Creates Dutch Marktplaats.nl listings from product images and seller details. It researches comparable listings, recommends private floor and target prices plus a leverage-oriented public asking price, drafts honest listing copy, and can prepare the listing in a browser.

Browser actions are guarded: bidding stays disabled, paid promotion and account changes require explicit authorization, and the skill stops at the final review screen for approval before publishing.

This is an unofficial automation aid and is not affiliated with or endorsed by Marktplaats. It does not bypass CAPTCHA, access controls, or platform limits.

Requirements: image input and browser control for the complete workflow. Without browser control, the skill can still research and draft a listing for manual posting.

[Read the skill](skills/marktplaats-ad-creator/SKILL.md)

## Verification

Pull requests and pushes to `main` run:

- skill metadata, link, JSON, Python syntax, symlink, private-path, and sensitive-data checks;
- Python linting and tests on Python 3.10 and 3.14;
- deterministic regeneration of the auditor's standalone HTML example;
- discovery and clean installation of both skills with a pinned `skills` CLI version;
- full-history secret scanning with Gitleaks.

Run the local checks:

```bash
python3 scripts/verify_skills.py --repository .
python3 -m unittest tests/test_verify_skills.py -v
python3 skills/agent-work-auditor/scripts/test_generate_report.py
npx --yes skills@1.5.16 add . --list
```

## License

[MIT](LICENSE)
