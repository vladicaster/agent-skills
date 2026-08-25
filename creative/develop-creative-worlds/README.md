# Develop Creative Worlds

Develop fictional worlds that generate stories instead of merely accumulating lore. The skill supports open-ended exploration, connected world development, living world-bible creation, continuity auditing, and controlled canon revision.

## Purpose

Use this skill to:

- turn a premise into a distinctive creative engine;
- explore genuinely different world directions and their tradeoffs;
- develop cultures, systems, institutions, histories, locations, factions, and characters;
- trace first-, second-, and third-order consequences;
- connect lore to ordinary life, power, identity, relationships, and conflict;
- create and maintain a structured world bible;
- preserve original creator material while distinguishing later stewardship and editorial development;
- distinguish canon from proposals, possibilities, disputed accounts, mysteries, and deprecated material;
- track provenance independently from canon status;
- create or manage an optional GitHub-backed world repository and creative harness;
- audit continuity, causality, narrative usefulness, distinctiveness, and complexity;
- propagate approved canon changes across affected timelines, characters, institutions, and stories.

The skill is genre- and medium-neutral. It can support novels, film, television, games, RPG campaigns, interactive experiences, and transmedia projects.

## When to use it

Recognizable requests include:

- "Help me explore three versions of this fictional world."
- "Turn these notes into a living world bible."
- "Develop the cultures and institutions implied by this premise."
- "Check this timeline and character history for contradictions."
- "If we change this rule, what else in the world must change?"
- "Adapt this story world for a game without losing its thematic identity."
- "Memorialize these creator notes in a revisable GitHub world repository."
- "Create or audit the creative harness that governs this world bible."

Do not use it as the primary workflow for writing a complete screenplay or novel, implementing a game, conducting historical research, or managing a software-delivery lifecycle. It can provide setting, canon, continuity, and narrative-system inputs to those activities.

## Operating modes

| Mode | Primary outcome |
| --- | --- |
| Explore | Distinct possibilities, consequences, tradeoffs, and a recommended direction when justified |
| Develop | Deeper, interconnected systems that create lived experience and story pressure |
| Document | A navigable world bible scaled to the project |
| Audit | Classified continuity, causality, distinctiveness, and narrative-yield findings |
| Revise | Approved canon changes with downstream impact traced and reconciled |

Repository-backed work may additionally Bootstrap, Create, Audit, Update, Repair, Validate, or Reconcile a proportionate creative harness.

Modes may be combined, but transitions should remain explicit.

## Canon discipline

The workflow does not silently turn brainstorming into canon.

| Status | Meaning |
| --- | --- |
| Canon | Established and authoritative |
| Proposed | Recommended but awaiting approval |
| Possibility | An exploratory alternative |
| Disputed | Conflicting accounts within the world or source material |
| Unknown | Intentionally unresolved |
| Deprecated | Replaced but retained when change history matters |

Casual brainstorming remains conversational. Formal status tracking becomes useful when choices affect later work.

Canon status answers whether a claim is authoritative. **Provenance** answers where it came from. Formal projects should track both so original creator material, steward-directed development, editorial normalization, later proposals, adaptation-specific material, and in-world artifacts remain distinguishable.

## Workflow

1. Establish medium, genre, tone, audience, scale, objective, and existing material.
2. Identify the premise, thematic tension, emotional promise, defining pressure, and important constraints.
3. Trace who benefits, who pays, who resists, and what consequences emerge.
4. Develop only the world domains relevant to the current creative decision.
5. Connect the resulting lore to ordinary behavior, character desire, institutions, dilemmas, and mysteries.
6. Record consequential decisions with appropriate canon status when formal continuity matters.
7. Audit or revise the world when requested, preserving intentional ambiguity and unreliable accounts.

## Repository-backed memorialization

GitHub is optional. Use a repository when the user wants durable, collaborative, revision-controlled world maintenance—not merely because one is available.

When authorized, the skill can organize a scalable repository with only the useful portions of a root overview, `bible/`, `characters/`, `locations/`, story or episode catalogs, mythology or history, `continuity/`, `source-material/`, and `templates/`. Original notes remain separate from normalized canon and later proposals.

Repository creation, owner, visibility, initialization, world-file writes, harness changes, publication, and merging retain their own approval and permission boundaries. Empty repositories require an initial commit before a normal feature branch can exist. The skill follows repository instructions and can coordinate with **GitHub Issue to Draft PR** for gated delivery.

## Creative repository harness

A proportionate harness can govern authorship, stewardship, canon authority, provenance, source preservation, file routing, revision impact, and contribution workflow. Depending on the project, it may include `AGENTS.md`, a harness manifest, entry and canon-decision templates, GitHub issue and PR templates, and deterministic checks for mechanical invariants.

The skill supports harness Bootstrap, Create, Audit, Update, Repair, Validate, and Reconcile behavior. Substantial harness work can coordinate with **Manage Coding-Agent Harness**. The worldbuilding skill owns creative governance; the harness skill owns general instruction architecture and enforcement structure.

## Included resources

- [`references/creative-lenses.md`](references/creative-lenses.md) provides targeted prompts for premise, rules, culture, power, history, character, distinctiveness, and continuity.
- [`references/world-bible-schema.md`](references/world-bible-schema.md) provides a scalable structure for project direction, canon, systems, people, power, history, places, characters, story engines, language, continuity, and adaptation.
- [`references/world-repository-harness.md`](references/world-repository-harness.md) defines optional repository structure, provenance, source preservation, GitHub readiness, and harness lifecycle.
- [`assets/world-repository-harness/`](assets/world-repository-harness/) provides an adaptable `AGENTS.md`, harness manifest, canon-decision form, and GitHub contribution templates.

## Worked example

[`examples/the-fabulous-unknown/`](examples/the-fabulous-unknown/) follows a one-sentence premise through Explore, Develop, and Document modes into a canon-controlled 20-page graphic-novel script, cover, splash page, and character sheets. The example also distinguishes the worldbuilding workflow from optional image-generation and connected-document capabilities.

## Approval and execution boundaries

Conversational exploration, read-only analysis, and portable draft generation do not authorize repository or connected-document writes, publication, external sharing, collaborator outreach, purchases, or production changes. Each requires separate authorization and any relevant connector or repository permission.

The workflow preserves private, licensed, client, and unpublished material within the requested scope. A request to brainstorm or audit a world does not authorize adding it to a public repository or replacing an existing world bible.

## Validation

From the repository root, run:

```bash
python scripts/validate_repository.py
```

The validator checks required skill structure, frontmatter, catalog links, Python syntax, and visible escaped-newline errors. Creative coherence, originality, sensitivity, and continuity still require human review.

## Installation

Install the complete `creative/develop-creative-worlds` directory so `SKILL.md`, `agents/openai.yaml`, references, assets, and examples remain together.

Source:

```text
https://github.com/vladicaster/agent-skills/tree/main/creative/develop-creative-worlds
```

### ChatGPT Work


For immediate use in the current ChatGPT Work conversation, paste the complete skill-directory URL into the chat:

```text
Use the develop-creative-worlds skill from this directory for this task:
https://github.com/vladicaster/agent-skills/tree/main/creative/develop-creative-worlds
```

ChatGPT should retrieve and follow the complete directory, including `SKILL.md` and its supporting files. Referencing the directory this way applies to the current conversation or task; it does not permanently install the skill. Use a supported Skills workflow or plugin separately when reusable installation is desired.

Ask ChatGPT Work:

```text
Install the develop-creative-worlds skill from:
https://github.com/vladicaster/agent-skills/tree/main/creative/develop-creative-worlds
```

ChatGPT should retrieve and validate the complete skill directory before installing it. Installing the skill does not grant GitHub or other connector permissions. If it is not immediately visible after a confirmed installation, refresh or reopen the Skills page.

### Codex

Personal installation:

```bash
mkdir -p ~/.agents/skills
cp -R creative/develop-creative-worlds ~/.agents/skills/develop-creative-worlds
```

Project-scoped installation, run from the target project's root:

```bash
mkdir -p .agents/skills
cp -R /path/to/agent-skills/creative/develop-creative-worlds .agents/skills/develop-creative-worlds
```

As with Claude, a copied installation is a snapshot. An absolute symbolic link can be used when the installation should follow a maintained source checkout.

### Claude

Clone or update this repository, then either copy or symbolically link the complete skill directory.

Personal installation:

```bash
mkdir -p ~/.claude/skills
cp -R creative/develop-creative-worlds ~/.claude/skills/develop-creative-worlds
```

Project-scoped installation, run from the target project's root:

```bash
mkdir -p .claude/skills
cp -R /path/to/agent-skills/creative/develop-creative-worlds .claude/skills/develop-creative-worlds
```

For a symbolic-link installation, replace the copy command with `ln -s` and use an absolute path to the source directory. A symbolic link follows updates in the source checkout. A copied installation is a snapshot and must be copied again after source updates. Remove or move an existing destination before replacing it; do not overwrite local customizations without reviewing them.

## Invocation

Invoke explicitly with a request such as:

```text
Use @develop-creative-worlds to explore three distinct versions of a society where memories are currency. Keep every option as a possibility until I approve one as canon.
```

The skill may also trigger automatically when its description closely matches the request and the host supports implicit invocation.

## Updating this skill

For ChatGPT Work, ask:

```text
Update my installed develop-creative-worlds skill from:
https://github.com/vladicaster/agent-skills/tree/main/creative/develop-creative-worlds
```

ChatGPT should compare the installed copy, validate the complete source, identify meaningful changes or local conflicts, and replace the installed copy only through the supported Skills workflow.

For Codex or Claude, pull the source checkout. Symbolic-link installations use the updated source immediately. Copied installations must be replaced by copying the complete directory again after reviewing local changes.

For a reproducible installation, check out a repository release tag or commit before copying or linking the directory. Record that revision with the consuming project. The `main` branch represents the latest stable source, not a permanent version pin.

## Limitations

- The workflow cannot determine creative intent that the user has not expressed.
- Internal coherence does not guarantee audience comprehension or emotional impact.
- Sensitivity review benefits from relevant lived experience and qualified human readers.
- Large worlds require a durable storage location to preserve canon across separate sessions.
- Repository and harness generation require separately authorized access and do not make GitHub mandatory.
- Deliberate mysteries and unreliable accounts should not be mistaken for continuity errors.
- Installing the skill grants no repository, document, publishing, or external-sharing permissions.
