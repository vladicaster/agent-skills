# Productivity Agent Skills

Reusable skills for personal organization, daily workspaces, and tools that help people manage information and tasks. This category groups skills by the user's everyday outcome, even when implementation involves software.

Each skill directory is independently installable.

## Available skills

| Skill | Status | Purpose |
| --- | --- | --- |
| [Scaffold Personal Dashboard Site](scaffold-personal-dashboard-site/) | Available | Creates modular personal dashboards for GPT Sites, Claude Code, and Claude Artifacts with configurable sources and resilient module behavior. |

## Category boundaries

Use Productivity for personal workflows and workspaces. Use [Engineering](../engineering/) for software-delivery methodology and repository governance, and [Product](../product/) for strategy, requirements, and commercialization.

A new skill belongs here when it addresses a distinct workflow with clear inputs, outputs, and completion criteria. Do not require other productivity skills to be installed alongside it.

## Installation

Follow the selected skill's README and keep its complete directory together, including referenced resources.

- ChatGPT Work: use the supported Skills/plugin workflow or supply the complete skill directory for the current task.
- Codex: install under `~/.agents/skills/` or the project's `.agents/skills/`.
- Claude Code: install under `~/.claude/skills/` or the project's `.claude/skills/`.
- Claude chat: follow the selected skill's instructions for loading the skill and producing Artifacts.

Installation does not grant provider connections, runtime capabilities, or publishing permissions. GitHub is conditional on repository-backed delivery; consult the [repository readiness guide](../docs/github-repository-readiness.md) when applicable.

## Updating installed skills

Installed copies are snapshots. Compare local customizations and update deliberately from the current source directory. Repoint symbolic links when a skill moves. Pinned revisions retain their historical paths.

See the [repository update policy](../README.md#versioning-and-updates) and the selected skill's README for source URLs and host-specific instructions.
