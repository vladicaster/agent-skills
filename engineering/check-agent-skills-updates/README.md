# Check Agent Skills Updates

Checks the installed Vladicaster Agent Skills plugin version against the latest release manifest and returns accurate host-specific upgrade instructions. Failure to reach the manifest never blocks another skill's workflow.

## Installation

This skill is automatically included in the full plugin. Install and update that package using the explicit [plugin instructions](../../docs/plugin-installation-and-updates.md).

Install the full ChatGPT/Codex plugin with:

```bash
codex plugin marketplace add vladicaster/agent-skills --ref main
```

Install **Vladicaster Agent Skills** from **Vladicaster Tools**. Update it with:

```bash
codex plugin marketplace upgrade vladicaster-tools
```

For Claude Code:

```bash
claude plugin marketplace add vladicaster/agent-skills
claude plugin install vladicaster-agent-skills@vladicaster-tools
```

Enable marketplace auto-update or update explicitly:

```text
/plugin marketplace update vladicaster-tools
/reload-plugins
```

For standalone use in ChatGPT Work, import this complete directory through the available Skills workflow and invoke `@check-agent-skills-updates`.

For standalone Codex installation:

```bash
mkdir -p ~/.agents/skills
cp -R /path/to/agent-skills/engineering/check-agent-skills-updates \
  ~/.agents/skills/check-agent-skills-updates
```

For standalone Claude Code installation:

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/agent-skills/engineering/check-agent-skills-updates \
  ~/.claude/skills/check-agent-skills-updates
```

Standalone use requires the installed plugin version to be provided or otherwise available. The checker does not infer an arbitrary standalone skill's version.

## Updating this skill

- **Full plugin:** Follow the [ChatGPT/Codex or Claude plugin update steps](../../docs/plugin-installation-and-updates.md). Claude can auto-update when enabled; ChatGPT/Codex repository-marketplace updates require the documented marketplace refresh.
- **Copied standalone skill:** Pull the source repository, compare local customizations, and replace the complete directory.
- **Symbolic-link installation:** Run `git -C /path/to/agent-skills pull`.
- **Pinned installation:** Advance to a newer Git tag deliberately.

## Deterministic check

Run:

```bash
python scripts/check_update.py --platform chatgpt-codex
```

Use `--manifest-url` to test against a specific manifest and `--installed-version` for standalone use.

The script compares semantic versions and returns JSON. It does not install or remove anything.

## Boundaries

- Network failure is non-blocking.
- Update availability does not authorize installation.
- Duplicate standalone skills are preserved until the user approves a migration.
- ChatGPT background updates and native update notices are not claimed.
