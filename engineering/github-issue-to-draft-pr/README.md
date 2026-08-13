# GitHub Issue to Draft PR

A reusable agent skill for a gated GitHub issue-to-draft-pull-request workflow.

## What it does

The skill separates delivery into two explicit phases:

1. Create a well-scoped GitHub issue and an issue-numbered feature branch.
2. Stop and wait for human approval.
3. After approval, implement the issue, run relevant checks, review the diff, commit, push, and open a linked draft pull request.

## Key guardrails

- Never commits directly to the repository's default branch.
- Never starts implementation before explicit approval.
- Keeps implementation within the approved issue scope.
- Reports checks honestly as passed, failed, or not run.
- Creates a draft pull request and does not merge it or mark it ready for review without a separate request.

## Platform compatibility

The core `SKILL.md` follows the open Agent Skills structure and can be used by ChatGPT, Codex, and Claude Code.

- `agents/openai.yaml` supplies OpenAI-specific display and invocation metadata. Claude Code does not require it.
- Supporting files must remain with `SKILL.md`.
- GitHub authentication and repository permissions are supplied by the host environment; the skill does not contain credentials.
- Invocation syntax and installation locations differ by platform.

## Prerequisites

| Platform | GitHub access |
| --- | --- |
| ChatGPT Work | Install and authorize the GitHub plugin for the repositories the skill will manage. |
| Codex | Use an authorized GitHub integration or an authenticated GitHub CLI environment. |
| Claude Code | Use an authenticated GitHub CLI environment or a GitHub MCP integration. |

The authenticated identity must have permission to create issues, branches, commits, and pull requests in the target repository.

## Install for ChatGPT Work

For reusable distribution in ChatGPT Work across supported web, desktop, and mobile surfaces, package this skill in an OpenAI plugin. Installing the plugin makes its bundled skill available to ChatGPT Work.

Until a plugin package is published, the standalone directory can be used for local authoring and supported desktop workflows:

1. Download or clone this repository.
2. Keep the entire `engineering/github-issue-to-draft-pr/` directory intact.
3. Add or import the directory through the available Skills workflow.
4. Install and authorize the GitHub plugin separately.

Invoke the installed skill in ChatGPT Work with:

```text
@github-issue-to-draft-pr
```

> Installing the skill teaches ChatGPT the workflow. It does not independently grant GitHub access.

## Install for Codex

### Personal installation

Personal skills are available across repositories:

```bash
git clone https://github.com/vladicaster/agent-skills.git
mkdir -p ~/.agents/skills
ln -s "$(pwd)/agent-skills/engineering/github-issue-to-draft-pr" \
  ~/.agents/skills/github-issue-to-draft-pr
```

If the repository is already cloned, replace `$(pwd)/agent-skills` with the absolute path to that clone.

### Project installation

Project skills apply only to the repository in which they are installed:

```bash
mkdir -p .agents/skills
cp -R /path/to/agent-skills/engineering/github-issue-to-draft-pr \
  .agents/skills/github-issue-to-draft-pr
```

Invoke the skill in Codex with:

```text
$github-issue-to-draft-pr
```

## Install for Claude Code

### Personal installation

Personal skills are available across Claude Code projects:

```bash
git clone https://github.com/vladicaster/agent-skills.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/agent-skills/engineering/github-issue-to-draft-pr" \
  ~/.claude/skills/github-issue-to-draft-pr
```

If the repository is already cloned, replace `$(pwd)/agent-skills` with the absolute path to that clone.

### Project installation

Project skills apply only to the repository in which they are installed:

```bash
mkdir -p .claude/skills
cp -R /path/to/agent-skills/engineering/github-issue-to-draft-pr \
  .claude/skills/github-issue-to-draft-pr
```

Invoke the skill in Claude Code with:

```text
/github-issue-to-draft-pr
```

Claude Code reads `SKILL.md` and its referenced supporting resources. The OpenAI-specific `agents/openai.yaml` file can remain in the directory and does not need to be copied or modified separately.

## Contents

- `SKILL.md` — shared workflow instructions and guardrails.
- `agents/openai.yaml` — OpenAI display and invocation metadata.
- `assets/icon.svg` — OpenAI skill icon.
- `README.md` — platform-specific requirements and installation guidance.

## Updating this skill

Installed copies are snapshots and do not automatically follow source changes.

- **ChatGPT Work:** Ask ChatGPT: `Update my installed github-issue-to-draft-pr skill from https://github.com/vladicaster/agent-skills/tree/main/engineering/github-issue-to-draft-pr`. The update should retrieve and validate the complete directory, report meaningful changes or local conflicts, and replace the installed copy. Refresh or reopen the Skills page if necessary.
- **Codex or Claude Code, symbolic link:** Run `git -C /path/to/agent-skills pull`. The linked installation then uses the updated checkout.
- **Codex or Claude Code, copied directory:** Pull the source repository, compare any local customizations, and copy the complete skill directory into the personal or project skills location again.
- **Pinned installation:** Use a Git tag rather than `main` when reproducibility matters, and move to a newer tag deliberately.

See the repository's [versioning and update policy](../../README.md#versioning-and-updates) for release guidance.

