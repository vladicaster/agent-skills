# Agent Skills

A public collection of reusable skills that teach AI agents how to follow focused, repeatable professional workflows.

The repository organizes focused workflows by professional outcome without requiring every skill to be installed together.

## Repository structure

```text
agent-skills/
├── engineering/
│   ├── README.md
│   ├── github-issue-to-draft-pr/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── agents/
│   │   └── assets/
│   └── manage-coding-agent-harness/
│       ├── SKILL.md
│       ├── README.md
│       ├── agents/
│       ├── references/
│       ├── scripts/
│       └── assets/
└── README.md
```

Each leaf directory is a self-contained skill. Install only the skill directories you need.

## Available categories

| Category | Purpose |
| --- | --- |
| [Engineering](engineering/) | Software-delivery, repository-governance, coding-agent, testing, architecture, and spec-driven-development workflows. |\n| [Product](product/) | Product strategy, market selection, positioning, commercialization, launch, adoption, and evidence-based decision workflows. |

## Available skills

| Skill | Category | Purpose |
| --- | --- | --- |
| [GitHub Issue to Draft PR](engineering/github-issue-to-draft-pr/) | Engineering | Creates a GitHub issue and feature branch, pauses for approval, and then implements the approved work as a linked draft pull request. |
| [Manage Coding-Agent Harness](engineering/manage-coding-agent-harness/) | Engineering | Creates and manages technology-neutral coding-agent harnesses for existing repositories or greenfield projects described by a PRD. |\n| [Develop Go-to-Market Strategy](product/develop-go-to-market-strategy/) | Product | Develops evidence-based segmentation, positioning, offers, motions, channels, launch plans, experiments, and measurable GTM priorities. |

## Compatibility

Skills use a `SKILL.md` entry point and follow the open Agent Skills structure whenever practical.

- **ChatGPT Work:** Use the skill through a supported Skills workflow or an installable OpenAI plugin. GitHub access requires a separately authorized GitHub plugin.
- **Codex:** Install skills personally under `~/.agents/skills/` or within a project under `.agents/skills/`.
- **Claude Code:** Install skills personally under `~/.claude/skills/` or within a project under `.claude/skills/`.

A skill may also contain platform-specific metadata. For example, `agents/openai.yaml` configures its OpenAI presentation and invocation behavior without changing the shared `SKILL.md` workflow.

See each skill's README for exact prerequisites, installation commands, invocation syntax, and platform notes.

## Design principles

Every skill should:

- Solve one recognizable workflow.
- Define when it should and should not be used.
- Make required inputs and expected outputs explicit.
- Preserve human approval gates for consequential actions.
- State permission, authentication, and tool prerequisites without embedding credentials.
- Report checks and failures honestly.
- Keep `SKILL.md` focused and place optional supporting material in `references/`, `scripts/`, or `assets/`.
- Avoid organization-specific assumptions unless the skill is intentionally organization-specific.

## Using a skill

1. Open the desired category and skill directory.
2. Read its `README.md` for platform-specific installation instructions.
3. Install the complete skill directory, keeping `SKILL.md` and its supporting files together.
4. Configure any required connectors, command-line tools, or repository permissions separately.
5. Test the skill in a non-critical repository before relying on it for production work.

## Contributing

Contributions are welcome through GitHub issues and pull requests.

When proposing a skill:

1. Place it under the category that best describes its primary outcome.
2. Use a concise, lowercase, hyphenated directory name.
3. Include a valid `SKILL.md` with clear `name` and `description` frontmatter.
4. Include a skill-level `README.md` covering purpose, prerequisites, installation, invocation, and limitations.
5. Keep examples generic and remove credentials, personal data, client information, proprietary code, and private repository references.
6. Describe how the skill was tested.
7. Preserve explicit approval gates around writes, deployments, merges, external communications, and other consequential actions.

Repository maintainers review and merge contributions. Public visibility does not grant direct write access.
