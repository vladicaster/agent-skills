# Engineering Agent Skills

Reusable agent skills for software delivery, repository governance, coding-agent workflows, architecture, testing, and spec-driven development.

Each subdirectory is an independently installable skill. You do not need to install the entire `agent-skills` repository.

## Available skills

| Skill | Status | Purpose |
| --- | --- | --- |
| [Develop C4 Architecture](develop-c4-architecture/) | Available | Brainstorms, discovers, audits, refines, and validates evidence-backed C4 architecture models and diagrams. |
| [GitHub Issue to Draft PR](github-issue-to-draft-pr/) | Available | Creates a scoped issue and feature branch, waits for explicit approval, then implements, validates, commits, pushes, and opens a linked draft pull request. |
| [Manage Coding-Agent Harness](manage-coding-agent-harness/) | Available | Bootstraps, creates, audits, updates, repairs, validates, explains, and reconciles technology-neutral coding-agent harnesses from a repository or greenfield PRD. |

## Planned areas

Future engineering skills may cover:

- Product specification and acceptance-criteria development
- Spec-to-implementation planning
- Broader architecture and modernization reviews beyond C4 modeling
- Pull-request review and feedback resolution
- Test-strategy generation
- Observability and operational-readiness reviews
- Technical-debt identification and handling

A planned area should become its own skill only when it has a distinct trigger, workflow, approval boundary, and expected output.

## Engineering skill conventions

Engineering skills should:

- Inspect repository instructions such as `AGENTS.md` before making changes.
- Confirm the actual default branch instead of assuming `main` or `master`.
- Avoid direct commits to a protected or default branch.
- Separate planning from implementation when approval materially affects the outcome.
- Keep changes within the approved issue or specification.
- Respect existing architecture and coding conventions.
- Consider correctness, security, observability, accessibility, maintainability, and relevant technical debt.
- Run the checks supported by the target repository.
- Distinguish passed, failed, blocked, and not-run validation.
- Report the resulting issue, branch, commit, pull request, checks, and remaining risks clearly.
- Never embed credentials or assume that installing a skill grants access to GitHub or another service.

## Installation

Open the desired skill directory and follow its README. Installation differs by host:

| Host | Typical skill location or distribution |
| --- | --- |
| ChatGPT Work | Supported Skills workflow or an installable OpenAI plugin |
| Codex, personal | `~/.agents/skills/<skill-name>/` |
| Codex, project | `.agents/skills/<skill-name>/` |
| Claude Code, personal | `~/.claude/skills/<skill-name>/` |
| Claude Code, project | `.claude/skills/<skill-name>/` |

GitHub authentication, connector authorization, and repository permissions must be configured separately.

Use the repository-wide [GitHub and repository readiness guide](../docs/github-repository-readiness.md) before repository operations. `github-issue-to-draft-pr` requires an existing writable destination repository. `manage-coding-agent-harness` can instead bootstrap a portable greenfield package when no repository exists.

## Updating installed skills

Installed copies do not automatically follow source changes. Use the repository's [versioning and update policy](../README.md#versioning-and-updates), then follow the selected skill's README for ChatGPT Work, symbolic-link, or copied-installation instructions.

## Adding an engineering skill

Create a self-contained directory:

```text
engineering/
└── skill-name/
    ├── SKILL.md
    ├── README.md
    ├── agents/       # Optional host metadata
    ├── references/   # Optional detailed guidance
    ├── scripts/      # Optional deterministic utilities
    └── assets/       # Optional templates and visual assets
```

Only add optional directories when the skill actually uses them. Keep the main workflow concise, and reference supporting files directly from `SKILL.md` when the agent needs to load or execute them.
