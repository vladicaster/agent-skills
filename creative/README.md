# Creative Agent Skills

Reusable agent skills for imaginative development, narrative systems, fictional-world design, canon management, and creative continuity.

Each subdirectory is independently installable. You do not need to install the complete `agent-skills` repository.

## Available skills

| Skill | Status | Purpose |
| --- | --- | --- |
| [Develop Creative Worlds](develop-creative-worlds/) | Available | Creates, expands, documents, audits, and revises coherent fictional worlds and living world bibles. |

## Creative skill conventions

Creative skills should:

- Preserve the creator's voice, themes, constraints, ambiguity, and unusual choices.
- Distinguish established canon from proposals, possibilities, disputed accounts, unknowns, and deprecated material.
- Generate meaningful alternatives whose consequences differ, not cosmetic variations.
- Connect lore to lived experience, power, character desire, conflict, and story generation.
- Trace downstream consequences before resolving creative choices.
- Treat unexplained or contradictory material as potentially intentional before classifying it as an error.
- Scale outputs to the project rather than producing exhaustive questionnaires or generic lore dumps.
- Preserve approval boundaries before publication, repository writes, external sharing, or other consequential actions.

## Updating installed skills

Installed copies do not automatically follow source changes. Use the repository's [versioning and update policy](../README.md#versioning-and-updates), then follow the selected skill's README for ChatGPT Work, Claude, symbolic-link, or copied-installation instructions.

## Planned areas

Future creative skills may cover:

- Character and relationship development
- Story architecture and narrative systems
- Writers' room collaboration
- Fictional languages and naming systems
- Interactive narrative and branching continuity
- Cross-medium adaptation

A planned area should become a separate skill only when it has a distinct trigger, workflow, and expected output.

## Installation

Open the desired skill directory and follow its README.

| Host | Typical location or distribution |
| --- | --- |
| ChatGPT Work | Supported Skills workflow using the skill's GitHub source URL |
| Codex, personal | `~/.agents/skills/<skill-name>/` |
| Codex, project | `.agents/skills/<skill-name>/` |
| Claude, personal | `~/.claude/skills/<skill-name>/` |
| Claude, project | `.claude/skills/<skill-name>/` |

GitHub is not required for conversational worldbuilding or portable artifacts. Repository access is required only when the user explicitly asks to read or write repository-backed world material.
