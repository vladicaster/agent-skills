# Product Agent Skills

Reusable agent skills for product strategy, market selection, positioning, commercialization, launch planning, adoption, and evidence-based product decisions.

Each subdirectory is independently installable. You do not need to install the complete `agent-skills` repository.

## Available skills

| Skill | Status | Purpose |
| --- | --- | --- |
| [Develop Go-to-Market Strategy](develop-go-to-market-strategy/) | Available | Develops, audits, refines, diagnoses, launch-plans, and reconciles evidence-based GTM strategies from product inputs and market results. |

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

## Planned areas

Future product skills may cover:

- Product requirements development
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
