# World Bible Schema

Use this structure selectively. Omit sections that do not serve the project.

## Project compass

- Working title and logline
- Original creator or creators
- Steward, archivist, or memorialization lead when different
- Source-interpretation authority and canon-approval authority
- Medium, genre, tone, audience, and scope
- Thematic tension and emotional promise
- Defining premise or departure
- Creative principles and prohibited directions

## Canon register

For consequential facts, record:

| Field | Purpose |
|---|---|
| ID | Stable human-readable reference when needed |
| Fact | Concise claim |
| Status | Canon, proposed, possibility, disputed, unknown, or deprecated |
| Scope | Era, region, culture, story, or medium where it applies |
| Provenance | Original creator source, steward-directed development, editorial normalization, later proposal, adaptation-specific material, or in-world account |
| Source reference | Exact artifact, note, conversation decision, or approved inference |
| Dependencies | Facts or entries this relies on or affects |
| Notes | Exceptions, ambiguity, or revision history |

## Foundational systems

- Reality rules: cosmology, metaphysics, science, magic, technology
- Limits, costs, access, failure modes, and exceptions
- Geography, ecology, climate, resources, and infrastructure
- System interactions and major consequences

## People and daily life

- Peoples, species, cultures, languages, and identities
- Family, childhood, education, labor, health, food, housing, ritual, art, and leisure
- Status, belonging, taboo, etiquette, and social mobility
- Contrasts between official ideals and lived experience

## Power and exchange

- Governments, law, institutions, factions, and enforcement
- Economy, ownership, scarcity, trade, debt, and informal exchange
- Information, belief, propaganda, archives, and education
- Beneficiaries, excluded groups, resistance, and unstable bargains

## History and time

- Eras and dating system
- Turning points and causal chain
- Public history, suppressed history, myths, and disputed accounts
- Timeline with dates, locations, participants, and consequences

## Places and organizations

For each relevant entry: identity, function, inhabitants or members, sensory character, internal divisions, resources, relationships, secrets, and story uses.

## Characters and viewpoints

For each relevant character: role, desire, fear, contradiction, knowledge limits, relationships, dependence on world systems, and potential arc.

## Story engine

- Active conflicts and change pressures
- Recurring dilemmas and sources of escalation
- Mysteries and revelation boundaries
- Story seeds at personal, community, institutional, and world scale

## Language and style

- Naming principles and pronunciation notes
- Key terms, idioms, titles, and registers
- Visual, material, architectural, and sensory motifs
- Narrative voice or presentation constraints

## Continuity and change

- Canon register with status and provenance tracked independently
- Known contradictions and resolutions
- Open questions
- Deliberate mysteries
- Proposed changes and impact analysis
- Deprecated canon and replacement mapping
- Attribution-aware change history

## Source archive

- Original notes preserved without silent rewriting
- Confidentiality and destination-visibility decision
- Distinction between raw source, normalized entry, editorial inference, and later proposal
- Naming conflicts, alternatives, and unresolved source contradictions
- Contextualization or creative-review decisions for dated or sensitive material

## Modular repository projection

When a durable repository improves maintenance, project the useful sections into modular files rather than forcing one monolithic document. A common shape is:

- root overview, attribution, navigation, and revision guidance;
- `bible/` for premise, rules, tone, themes, and systems;
- `characters/`, `locations/`, and story- or medium-specific catalogs;
- `continuity/` for canon, contradictions, open questions, and change history;
- `source-material/` for preserved originals;
- `templates/` for repeatable entries and decisions.

Omit empty or irrelevant directories. Record relationships and dependencies so a revision can be propagated across files.

## Adaptation notes

- What every version must preserve
- What may vary by medium or storyline
- Audience knowledge by installment
- Spoiler and revelation sequencing
