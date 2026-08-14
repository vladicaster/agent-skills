# Repository Agent Instructions

## Scope

These instructions govern the entire `agent-skills` repository. This repository publishes reusable, independently installable Agent Skills; it is not an application runtime or a place for product-specific planning material.

Read [the skill-authoring standard](docs/engineering/skill-authoring.md) before creating or changing a skill.

## Working agreement

- Start from the current default branch and work on `agent/<description>`.
- Never commit directly to `main`. Publish changes through a draft pull request unless the user explicitly requests another review state.
- Keep changes within the approved skill, documentation, or harness scope. Surface materially new work before including it.
- Preserve existing approval, privacy, security, validation, and external-action boundaries. Never weaken them silently.
- Keep reusable methodology in the owning skill. Keep client, company, product, credential, and private-repository material out of this public repository.
- Treat installed skills as snapshots. Do not claim source changes automatically update installed copies.

## Skill changes

- A leaf skill directory must contain `SKILL.md`, a substantial `README.md`, and `agents/openai.yaml`.
- Keep `SKILL.md` frontmatter limited to `name` and `description`; the name must match the directory.
- Keep shared workflow logic in `SKILL.md`; place detailed guidance in `references/`, reusable starting material in `assets/`, and deterministic utilities in `scripts/`.
- Preserve optional orchestration: reuse approved compatible artifacts and invoke only missing dependencies.
- When adding, renaming, moving, or removing a skill, update its category README and the root README. Review lifecycle diagrams and cross-skill links for impact.
- Use real Markdown line breaks. Never commit visible escaped newline text such as a backslash followed by `n`.

## Validation

Run before publishing:

```bash
python scripts/validate_repository.py
```

Also run every changed skill's relevant deterministic scripts or fixtures. Report each check as **passed**, **failed**, **blocked**, **manual**, or **not run**. Do not describe a check as passed unless it ran successfully.

## Pull-request handoff

The pull request must explain the change, reason, user or agent impact, approval-boundary changes, catalog or lifecycle propagation, validation evidence, manual checks, remaining risks, and deferred work. Review the final diff for unrelated edits, secrets, personal data, proprietary content, broken links, generated artifacts, and visible escape sequences.
