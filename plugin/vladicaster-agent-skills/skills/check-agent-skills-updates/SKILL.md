---
name: check-agent-skills-updates
description: Check whether a newer Vladicaster Agent Skills plugin release exists and report non-blocking, platform-specific update instructions. Use when a user asks to check for plugin updates or when a bundled workflow is configured to check at most once per conversation.
---

# Check Agent Skills Updates

Check for a newer plugin release without blocking the user's primary workflow.

1. Determine the current host: ChatGPT/Codex, Claude Code, or unknown.
2. Run `scripts/check_update.py --platform <chatgpt-codex|claude-code>` when scripts and network access are available. The script discovers the installed version from the surrounding plugin manifest. For a standalone installation, also pass `--installed-version <version>` when known.
3. If the check reports no update, do not add a disruptive notice.
4. If a newer version exists, report the installed and available versions, newly added skills, release-notes URL, and the returned host-specific update instruction.
5. If the check cannot run, continue the user's primary workflow and mention the limitation only when the user explicitly asked for an update check.
6. Never claim that ChatGPT repository marketplaces update automatically.
7. Never disable, uninstall, overwrite, or migrate a standalone skill without explicit approval.
8. Do not repeat an update notice after it has already been presented in the same conversation.

For full installation, update, duplicate-skill, and rollback guidance, read `README.md`.
