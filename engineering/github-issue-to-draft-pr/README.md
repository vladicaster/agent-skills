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

## Contents

- `SKILL.md` — workflow instructions and guardrails.
- `agents/openai.yaml` — display and invocation metadata.
- `assets/icon.svg` — skill icon.

## Installation

Install or import the `github-issue-to-draft-pr` directory as a complete skill. Keep `SKILL.md`, `agents/`, and `assets/` together so the instructions, metadata, and icon remain available.
