# GitHub and repository readiness

Installing a skill does not create a GitHub account, authorize a connector, create a repository, or grant repository permissions. Decide whether GitHub is part of the requested workflow before attempting repository operations.

## Requirements by skill

| Skill | GitHub requirement | Repository requirement |
| --- | --- | --- |
| GitHub Issue to Draft PR | Required | An existing accessible destination repository with issues and pull requests enabled |
| Manage Coding-Agent Harness | Conditional | Existing-repository modes need repository access; Bootstrap can produce a portable package without GitHub |
| Develop Product Requirements | Conditional | PRD authoring and issue planning can run without GitHub; approved issue creation needs confirmed destination repositories |
| Prepare Product for Engineering | Conditional | A local or document-based planning package is valid; GitHub repository creation or use is separately authorized |
| Develop Go-to-Market Strategy | Not inherently required | Outputs may be returned as documents or saved to an approved destination, including an optional repository |

## First-run readiness check

Before a GitHub read or write, determine the smallest applicable set of prerequisites:

1. Confirm that the user has a GitHub account and identify the authenticated GitHub identity without exposing credentials.
2. Confirm an authorized GitHub connector, MCP integration, or authenticated CLI is available.
3. Identify every required source and destination repository, or record that the workflow does not need one.
4. Verify that each required repository exists and is accessible.
5. Confirm personal or organization ownership. When repository creation is requested, separately confirm the owner and public or private visibility before creating it.
6. Verify the least permissions needed for the requested operations, such as reading contents, writing files, creating issues, creating branches, pushing commits, or opening pull requests.
7. For delivery work, discover the actual default branch and verify that issues, branches, and pull requests are available. Respect branch protections and required reviews; do not attempt to bypass them.
8. Confirm source-material confidentiality is compatible with the destination repository visibility before uploading it.

Read-only or document-only work should not be blocked merely because GitHub is unavailable. Keep the output local or use another user-approved destination.

## Missing prerequisites

When a required account, authorization, repository, capability, or permission is missing:

- stop before the affected repository operation
- report the result as **Blocked**
- name the missing prerequisite and the exact operation it prevents
- give the specific next action, such as authorizing the GitHub connector, signing in with the CLI, granting repository access, enabling issues, selecting an existing repository, or separately approving creation of a repository
- preserve any completed read-only analysis or portable artifacts

Never request that a user paste a token or credential into a repository, issue, prompt, document, or chat. Use the host's supported authorization flow.
