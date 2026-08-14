---
name: manage-coding-agent-harness
description: Create, bootstrap, audit, update, repair, validate, explain, and reconcile repository-specific coding-agent harnesses. Use when a user wants to establish or manage agent instructions, engineering standards, workflow templates, architecture guidance, stack decisions, or validation requirements for an existing repository or a greenfield project described by a PRD.
---

# Manage Coding-Agent Harness

Build and maintain the effective instruction system that governs coding agents. Treat the harness as the combination of agent instructions, engineering references, workflow templates, and executable enforcement—not as one file.

## Select the mode

- **Bootstrap:** Start from a PRD or project brief when no repository exists.
- **Create:** Establish a harness for an existing repository.
- **Audit:** Report coverage, gaps, duplication, and contradictions without writing.
- **Update:** Make an approved targeted policy change.
- **Repair:** Reconcile broken, stale, or conflicting instructions.
- **Validate:** Assess completeness and internal consistency without writing.
- **Explain:** Describe the effective policy without writing.
- **Reconcile:** Align a provisional greenfield harness with a newly created repository.

Default to read-only Audit or Explain when the user asks a question rather than requesting changes.

## Phase 1: Discover and propose

1. Confirm the requested mode and whether a repository exists.
2. For an existing repository:
   - Identify the repository location and required access. If it is remote, verify the authenticated identity, repository existence, and least read or write permissions needed for the selected mode.
   - If required access is missing, report **Blocked** with the exact setup action; do not request pasted credentials.
   - Read repository and directory-scoped instruction files before acting.
   - Run `scripts/inventory_harness.py` when filesystem access is available.
   - Inspect the actual stack, project layout, build files, tests, CI, documentation, and contribution templates.
   - Determine which instructions apply to which files and identify contradictions or stale paths.
3. For a greenfield project:
   - Do not require GitHub. Confirm the approved portable output destination.
   - Read `references/greenfield-bootstrap.md` and `references/stack-selection.md`.
   - Extract functional requirements, nonfunctional requirements, constraints, assumptions, and open decisions from the supplied PRD.
   - Recommend the simplest system shape and stack that satisfy the evidence. Do not select technology by popularity alone.
4. Read `references/capability-matrix.md` and evaluate only applicable capabilities. Do not add irrelevant boilerplate.
5. Read `references/instruction-precedence.md` when multiple instruction surfaces exist. Read `references/platform-files.md` when choosing host-specific files.
6. Present:
   - current or proposed harness inventory
   - known requirements and constraints
   - assumptions and open questions
   - gaps, duplication, and conflicts
   - proposed architecture and stack when relevant
   - exact files to create, update, retain, or supersede
   - implementation and validation plan
7. For Bootstrap, Create, Update, Repair, or Reconcile, stop and ask the user to **approve**, **revise**, or **cancel**. Do not write harness files before unambiguous approval.

Audit, Validate, and Explain remain read-only unless the user separately approves changes.

## Phase 2: Apply after approval

1. Reconfirm the approved decisions and file scope.
2. Preserve useful existing guidance, project terminology, and repository conventions.
3. Generate only applicable files. Prefer concise root instructions that link to detailed references over duplicated policies.
4. Keep platform-neutral engineering policy in shared documents. Add platform-specific adapter files only when that platform is used.
5. Use templates in `assets/` as modular starting points, not mandatory complete outputs.
6. Verify that commands, paths, links, precedence statements, and ownership boundaries match the repository.
7. Review the diff for contradictions, duplication, excessive prescription, secrets, personal data, proprietary content, and obsolete instructions.
8. Run relevant validation. Distinguish **passed**, **failed**, **blocked**, **manual**, and **not run**.
9. Report decisions, files changed, meaningful policy changes, validation results, provisional assumptions, and remaining risks.

Repository creation is outside this skill unless separately authorized. Before creating one, confirm the personal or organization owner, public or private visibility, confidentiality compatibility, and required access.

## Harness design rules

- Make the harness technology-neutral until repository or PRD evidence supports a technology-specific rule.
- Favor the simplest architecture that satisfies the requirements.
- Never add microservices, Kubernetes, messaging, caching, vector storage, or other infrastructure without a requirement and stated tradeoff.
- Separate behavioral instructions from detailed engineering documentation and deterministic enforcement.
- Never claim prose guarantees behavior that should be enforced by CI, permissions, tests, linters, or branch rules.
- Do not silently overwrite contradictory policies. Explain the conflict and obtain approval for the resolution.
- Do not remove or weaken approval, security, validation, or release safeguards without explicit authorization.
- Never embed credentials, tokens, private keys, or environment-specific secrets.
- Treat generated greenfield guidance as provisional until reconciled with the actual repository.

## Typical output locations

Choose only those that apply:

- `AGENTS.md` for shared repository instructions.
- Nested `AGENTS.md` files for genuinely different subtree rules.
- `CLAUDE.md`, `.github/copilot-instructions.md`, or host-specific adapters when needed.
- `docs/architecture/` for system shape, boundaries, and approved decisions.
- `docs/engineering/` for detailed policies.
- `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md` for contribution workflow.
- `harness-manifest.yaml` for concise status, decisions, and provisional assumptions.

Do not create a `project-harness/` wrapper inside an existing repository. Use it only as a portable deliverable when no repository exists.
