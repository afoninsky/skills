# Third-party skill notices

Design Steward can compose two optional repository-local skills. Their instructions are subordinate to Design Steward's clean-room, authority, and evidence contracts.

## grilling / grill-me runtime composition

Design Steward also composes an existing installed skill named `grilling` or `grill-me` for the general one-question-at-a-time decision-tree interaction used during design-intent grilling. The public `SKILL.md` package format has no supported nested-skill dependency metadata, and this repository does not vendor or rewrite that skill. Design Steward therefore invokes it by name through the runtime skill registry and applies `references/design-intent-grilling.md` only as a design-specific wrapper. If neither name is available, the Steward stops before grilling instead of substituting a divergent copy.

## frontend-design

- Source: [Anthropic frontend-design](https://github.com/anthropics/skills/blob/2235be7c60b551f5de82ade908fd3816455afcda/skills/frontend-design/SKILL.md)
- Local SHA-256: `1608ea77fbb6fc30d13a97d12cfa8ebf31358d40f0dd97beed24829d6b3f45dd`
- License: [Apache License 2.0](https://github.com/anthropics/skills/blob/ef740771ac901e03fbca3ce4e1c453a96010f30a/skills/frontend-design/LICENSE.txt) (SPDX: Apache-2.0)
- Local license copy: `.agents/skills/frontend-design/LICENSE.txt`

The installed skill and license are unmodified copies of the linked upstream files.

## web-design-guidelines

- Source: [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/ba46938889d4e58635362fb8f618e1178ac3ec46/skills/web-design-guidelines/SKILL.md)
- Local SHA-256: `f4647ca866a3accf763777f83e7682954f0187cd6bea7eea0399796652414e8f`
- License: MIT, as declared in the upstream [repository README](https://github.com/vercel-labs/agent-skills/blob/7c180d9044c9ae2b442b567aad4e42a28dd5ed62/README.md#license)

The upstream skill directory does not contain a separate license file. This notice preserves the upstream repository's license declaration and exact source revision. The installed skill is an unmodified copy.

Machine-readable provenance is in `skills/design-steward/references/specialist-provenance.json`.
