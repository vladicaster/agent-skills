# Skill authoring and maintenance

This document is the canonical repository standard for creating and maintaining reusable Agent Skills.

## Repository model

Each leaf directory under a professional category is independently installable. A skill should solve one recognizable workflow with a clear trigger, inputs, outputs, approval boundary, and completion condition. Do not couple installation of unrelated skills.

## Required structure

```text
category/skill-name/
├── README.md
├── SKILL.md
└── agents/
    └── openai.yaml
```

Add only what the workflow uses:

- `references/` for detailed methodology and decision rules
- `assets/` for templates and reusable starting material
- `scripts/` for deterministic validation or transformation

Use lowercase hyphenated directory names. The `SKILL.md` frontmatter name must exactly match the directory name.

## SKILL.md standard

Frontmatter contains only:

```yaml
---
name: skill-name
description: What the skill does and when it should be used.
---
```

The body should define the operating modes, workflow, evidence rules, approval gates, dependency behavior, completion criteria, and boundaries needed for reliable execution. Keep it focused; move optional depth to directly linked references.

Do not embed credentials, private URLs, personal data, client information, or product-specific assumptions in a generic skill.

## README standard

A skill README is user-facing documentation, not a short summary. Include applicable sections for:

1. Purpose and recognizable use cases.
2. When to use and when not to use the skill.
3. Modes or supported starting points.
4. A workflow diagram when it materially improves understanding.
5. Detailed step-by-step behavior.
6. Areas addressed and expected outputs.
7. Approval and execution boundaries.
8. Included references, assets, and scripts.
9. Validation commands and what they do not prove.
10. Installation and invocation for ChatGPT Work, Codex, and Claude Code.
11. Updating installed snapshots and pinned-version guidance.
12. Limitations, dependencies, and separately required permissions.

Use the GTM, PRD, coding-agent-harness, and product-preparation READMEs as depth references. Do not mechanically copy irrelevant sections.

## Dependencies and orchestration

Keep dependency ownership explicit. An orchestrator should call the current installed dependency rather than copying its methodology.

- Reuse approved compatible outputs.
- Invoke only missing or materially stale stages.
- Preserve additive upstream outputs.
- Stop and propose migration for breaking changes to approval semantics, identifiers, traceability, or required outputs.
- Contribute reusable methodology improvements to the owning skill; keep orchestration-specific compatibility logic in the orchestrator.

## Approval and permission boundaries

Planning and read-only analysis do not authorize consequential writes. State when separate authorization is required for repository changes, external communication, publication, spending, account creation, production changes, deployment, or implementation.

Never treat silence as approval. Never fabricate evidence, validation, ownership, or approval.

## GitHub and repository prerequisites

For every skill, state whether GitHub and an existing repository are required, conditional, or unnecessary. Repository-backed workflows must follow the shared [GitHub and repository readiness guide](../github-repository-readiness.md) and keep their runtime checks in `SKILL.md`.

Do not force GitHub on read-only, document-only, or portable-artifact workflows. Before a GitHub write, confirm the authenticated identity, source and destination repositories, repository existence, ownership and visibility when relevant, least required permissions, and required repository capabilities. Missing prerequisites must produce a **Blocked** result with an exact next action. Repository creation and visibility selection require separate authorization.

## Catalog and lifecycle propagation

When a skill is added, renamed, moved, or removed:

- update the category README skill table
- update the root README repository tree and skill table
- review lifecycle prose, diagrams, and tables
- review links from related skills
- describe whether the relationship is required, optional, or conditional

When only a skill's behavior changes, assess the same surfaces and update those whose claims became stale.

## Markdown and generated-text safety

- Use actual line breaks, not visible escaped sequences.
- Scan Markdown for a literal backslash followed by `n` before publishing.
- Keep Mermaid diagrams compact and make optional paths visually distinguishable.
- Use relative repository links and verify renamed paths.
- Do not commit `__pycache__`, compiled bytecode, temporary fixtures, or generated archives.

## Deterministic validation

Run the repository validator:

```bash
python scripts/validate_repository.py
```

Run changed skill utilities separately. A deterministic validator checks structure and syntax; it does not prove that research is true, strategy is sound, requirements are approved, or a workflow is safe in every environment.

## Versioning and updates

Source on `main` is the latest stable repository state. Installed copies are snapshots unless deliberately linked to a checkout. Updates must be explicit so users can review workflow and permission changes. Use tags for reproducible installations.
