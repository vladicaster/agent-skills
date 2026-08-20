# Vladicaster Agent Skills plugin

The plugin installs every canonical skill in this repository as one versioned package while leaving individual-skill installation available.

## Install in ChatGPT and Codex

The review-free distribution path uses this GitHub repository as an OpenAI marketplace.

1. In Codex CLI, add the marketplace once:

   ```bash
   codex plugin marketplace add vladicaster/agent-skills --ref main
   ```

2. Open the ChatGPT desktop app's **Plugins** directory or run `/plugins` in Codex CLI.
3. Select the **Vladicaster Tools** source and install **Vladicaster Agent Skills**.
4. Start a new ChatGPT chat or Codex session before invoking a bundled skill.

Repository marketplaces are intended for local, repository, team, and direct distribution. This package is not listed in OpenAI's public Plugins Directory and does not depend on public-directory review.

### Update in ChatGPT and Codex

Refresh the Git-backed marketplace:

```bash
codex plugin marketplace upgrade vladicaster-tools
```

Then refresh or reopen ChatGPT, or start a new Codex session. Do not assume that a running ChatGPT conversation automatically reloads updated skill instructions. ChatGPT repository marketplaces do not provide a documented guarantee of background updates or native update notifications.

To check before upgrading, invoke `check-agent-skills-updates`. The check is advisory and non-blocking; it reports nothing disruptive when no newer release can be established.

## Install in Claude Code

Add the GitHub marketplace and install the plugin:

```bash
claude plugin marketplace add vladicaster/agent-skills
claude plugin install vladicaster-agent-skills@vladicaster-tools
```

In an interactive Claude Code session, the equivalent slash commands are:

```text
/plugin marketplace add vladicaster/agent-skills
/plugin install vladicaster-agent-skills@vladicaster-tools
```

Bundled skills use Claude's plugin namespace, for example:

```text
/vladicaster-agent-skills:github-issue-to-draft-pr
```

### Update in Claude Code

Third-party marketplace auto-update is disabled by default. Enable it from:

```text
/plugin → Marketplaces → vladicaster-tools → Enable auto-update
```

Or refresh manually:

```text
/plugin marketplace update vladicaster-tools
```

Claude Code checks an auto-updating marketplace after session startup. When it downloads a new plugin version, run:

```text
/reload-plugins
```

If no reload notice appears, the updated plugin loads on the next session. This behavior applies to supported Claude Code sessions, not every ordinary Claude web chat.

## New skills in an update

The bundle is generated from every valid canonical leaf skill. A newly added skill is included in the next minor or major plugin release and listed under **Added skills** in its release notes. After completing the update and reload steps above, the new skill becomes available through the plugin without a separate skill installation.

Standalone installations remain unchanged and do not independently acquire newly bundled skills.

## Existing standalone skills

Installing the plugin does not overwrite or remove separately installed skills.

- Claude plugin skills are namespaced, so `/skill-name` and `/vladicaster-agent-skills:skill-name` can coexist.
- ChatGPT and Codex may expose both copies; do not rely on undocumented implicit-selection precedence.
- Compare locally customized standalone copies before disabling them.
- Disable or uninstall a duplicate only after explicit user approval.

Only the plugin-bundled copy follows plugin releases.

## Roll back or uninstall

- For a reproducible rollback, configure the marketplace at a known Git tag and reinstall that plugin version.
- In ChatGPT or Codex, open the plugin manager and disable or uninstall **Vladicaster Agent Skills**.
- In Claude Code, run `/plugin uninstall vladicaster-agent-skills@vladicaster-tools`.
- Removing the plugin does not remove separately installed skills.

## Standalone installation and updates

Every leaf skill README includes standalone instructions for ChatGPT Work, Codex, and Claude Code.

- A copied standalone skill remains a snapshot until explicitly replaced.
- A symbolic link follows the linked repository checkout after `git pull`.
- A Git-tagged or otherwise pinned installation remains fixed until deliberately advanced.
- Installing instructions never grants GitHub, filesystem, deployment, email, or other external permissions.

## Maintainer release procedure

1. Change canonical skill sources under their category directories.
2. Add a new skill as a complete leaf directory; no plugin inventory edit is required.
3. Increment `release/version.json`. Adding a skill requires at least a minor increment.
4. Rebuild the committed plugin bundle:

   ```bash
   python scripts/build_plugin.py --sync
   ```

5. Validate source and package equivalence:

   ```bash
   python scripts/validate_repository.py
   python scripts/build_plugin.py --check
   ```

6. Tag the approved release. The release workflow publishes the plugin archive and update manifest.
