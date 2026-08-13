# Product Agent Skills

Reusable agent skills for product strategy, market selection, positioning, commercialization, launch planning, adoption, and evidence-based product decisions.

Each subdirectory is independently installable. You do not need to install the complete `agent-skills` repository.

## Available skills

| Skill | Status | Purpose |
| --- | --- | --- |
| [Develop Go-to-Market Strategy](develop-go-to-market-strategy/) | Available | Develops, audits, refines, diagnoses, launch-plans, and reconciles evidence-based GTM strategies from product inputs and market results. |
| [Develop Product Requirements](develop-product-requirements/) | Available | Creates and manages hierarchical, traceable PRDs with stable requirements and many-to-many GitHub issue and PR relationships. |

## Product skill conventions

Product skills should:

- Separate verified evidence, company-provided facts, inference, and assumptions.
- Define the decision, target audience, inputs, outputs, and success criteria.
- Identify missing product, business, operational, and measurement capabilities.
- Prioritize rather than produce generic option lists.
- State tradeoffs, dependencies, risks, and reconsideration triggers.
- Use current cited research when external market facts matter.
- Preserve approval gates before external communication, publication, spending, production changes, or commercial commitments.
- Define measurable learning and decision criteria.

## Updating installed skills

Installed copies do not automatically follow source changes. Use the repository's [versioning and update policy](../README.md#versioning-and-updates), then follow the selected skill's README for ChatGPT Work, symbolic-link, or copied-installation instructions.

## Planned areas

Future product skills may cover:

- Customer-discovery synthesis
- Product positioning
- Pricing research and packaging
- Product and market readiness audits
- Product roadmap prioritization
- Launch retrospectives
- Adoption and retention diagnosis

A planned area should become a separate skill only when it has a distinct trigger, workflow, approval boundary, and expected output.

## Installation

Open the desired skill directory and follow its README.

| Host | Typical location or distribution |
| --- | --- |
| ChatGPT Work | Supported Skills workflow or an installable OpenAI plugin |
| Codex, personal | `~/.agents/skills/<skill-name>/` |
| Codex, project | `.agents/skills/<skill-name>/` |
| Claude Code, personal | `~/.claude/skills/<skill-name>/` |
| Claude Code, project | `.claude/skills/<skill-name>/` |

External research, analytics, CRM, email, advertising, website, and other permissions must be configured separately.
