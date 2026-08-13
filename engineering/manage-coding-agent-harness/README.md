# Manage Coding-Agent Harness

A technology-neutral Agent Skill for creating and managing coding-agent harnesses from either an existing repository or a greenfield PRD.

## Capabilities

- Bootstrap a provisional architecture, stack decision, and harness from a PRD.
- Create a repository-grounded harness.
- Audit, explain, validate, update, repair, and reconcile existing harnesses.
- Preserve an explicit approval gate before any harness files are written.
- Adapt to ChatGPT/Codex, Claude Code, GitHub Copilot, and shared repository instruction surfaces.

## Installation

Keep this directory intact so `SKILL.md`, `references/`, `scripts/`, and `assets/` remain together.

- **ChatGPT Work:** Install through a supported Skills workflow or package it in an OpenAI plugin for distribution.
- **Codex personal:** Place or link it at `~/.agents/skills/manage-coding-agent-harness/`.
- **Codex project:** Place it at `.agents/skills/manage-coding-agent-harness/`.
- **Claude Code personal:** Place or link it at `~/.claude/skills/manage-coding-agent-harness/`.
- **Claude Code project:** Place it at `.claude/skills/manage-coding-agent-harness/`.

Invoke it as `@manage-coding-agent-harness` in ChatGPT Work, `$manage-coding-agent-harness` in Codex, or `/manage-coding-agent-harness` in Claude Code.

## Safety boundary

Audit, Validate, and Explain are read-only. Bootstrap, Create, Update, Repair, and Reconcile must stop for approval after presenting decisions and exact proposed file changes.

Installing this skill does not grant repository, filesystem, GitHub, deployment, or secrets access.
