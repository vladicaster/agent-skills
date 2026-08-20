# Platform Files

Keep engineering policy portable and host adapters thin.

| Surface | Use |
| --- | --- |
| `AGENTS.md` | Shared repository and subtree coding-agent instructions |
| `CLAUDE.md` | Claude-specific adapter when Claude Code is used |
| `.github/copilot-instructions.md` | GitHub Copilot repository adapter |
| `.github/instructions/*.instructions.md` | Path-specific Copilot guidance when justified |
| `.agents/skills/` | Repository-scoped Agent Skills for Codex-compatible hosts |
| `.claude/skills/` | Repository-scoped Claude Code skills |
| `.github/pull_request_template.md` | Validation and reporting expectations |
| `docs/architecture/` | Architecture decisions and boundaries |
| `docs/engineering/` | Detailed engineering and operational policy |

Avoid copying the same policy into multiple host files. Put shared rules in one canonical document and use adapters to point agents to it.
