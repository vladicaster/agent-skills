---
name: github-issue-to-draft-pr
description: Manage a gated GitHub issue-to-draft-PR workflow for a referenced repository. Use when the user asks ChatGPT to draft or create a GitHub issue, create its feature branch, propose an implementation plan, wait for approval, then implement, test, commit, push, and open a linked draft pull request.
---

# GitHub Issue to Draft PR

Use GitHub tools for remote repository operations and the repository checkout for implementation and verification. Preserve repository instructions such as `AGENTS.md`.

## Phase 1: Issue and branch

1. Require an existing destination repository. Verify the authenticated GitHub identity, repository existence and access, issue and pull-request availability, permissions needed to create issues, branches, commits, and pull requests, and the actual default branch. Respect branch protections. Do not create a repository as part of this workflow.
2. Confirm the target repository and its actual default branch. Treat `master` as the user's normal preference, but do not assume it when repository metadata says otherwise or the user specifies another base.
3. If the repository, base branch, acceptance criteria, authorization, or other material requirements are unclear, ask only the concise questions needed before creating anything.
4. Inspect enough repository context to write an accurate, scoped issue and implementation plan. Do not modify code.
5. Draft or create the issue from the user's request, including clear acceptance criteria where appropriate.
6. Create a branch from the confirmed base branch only after obtaining the issue number. Name it `issue-<number>-<short-slug>` using a concise lowercase hyphenated slug.
7. Stop. Do not edit files, generate implementation changes, commit code, or open a pull request.
8. Report:
   - issue title
   - issue body
   - issue link
   - branch name
   - proposed implementation plan
9. Ask the user to **approve**, **edit**, or **cancel**. Treat only an unambiguous approval as authorization to begin Phase 2. If the user requests edits, update the issue or plan as requested and ask again.

If identity verification, authorization, repository access, required capabilities, permissions, issue creation, or branch creation fails, report **Blocked**, name the failed operation, and explain the exact setup action needed. Do not continue with implementation or request pasted credentials.

## Phase 2: Implementation after approval

1. Reconfirm that the working branch is the approved `issue-<number>-<short-slug>` branch and is based on the confirmed default branch. Never work directly on `master` or another default branch.
2. Implement only the approved issue scope. Surface materially new requirements instead of expanding the pull request silently.
3. Run relevant repository checks, tests, build, formatting, and static analysis as supported by the project. Record commands and results; never claim a check ran when it did not.
4. Review the diff for scope, correctness, security, observability, and repository conventions.
5. Commit the changes intentionally and push the approved branch.
6. Create a **draft** pull request targeting the confirmed base branch. Link it to the issue using a closing keyword such as `Closes #<number>` when appropriate.
7. Report:
   - issue link
   - branch name
   - draft pull request link
   - concise summary of changes
   - compact diff summary with the total files changed and additions/deletions, followed by a meaningful file-by-file description of what changed; group generated or mechanical files when that improves readability
   - a note that the draft pull request's **Files changed** tab contains the complete line-by-line diff
   - tests and checks with pass, fail, or not-run status

If implementation, checks, push, or draft pull request creation fails, stop at the safe boundary, preserve completed work, and explain what is needed next.

## Guardrails

- Never commit directly to the default branch.
- Never begin implementation before the explicit approval gate.
- Keep the issue and pull request narrowly scoped.
- Do not convert the draft pull request to ready-for-review or merge it unless the user separately asks.
- Do not message reviewers or assign people unless the user separately asks and the recipients are resolved.
