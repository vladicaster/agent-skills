---
name: develop-creative-worlds
description: Create, expand, structure, audit, memorialize, and maintain imaginative fictional worlds for novels, films, television, games, role-playing campaigns, interactive experiences, and transmedia projects. Use when developing a premise, exploring alternate world concepts, building a world bible, preserving creator source material, defining authorship and stewardship, establishing canon and provenance, creating or governing a world repository and its creative harness, checking continuity, resolving contradictions, evaluating downstream consequences, or adapting one world across stories and media.
---

# Develop Creative Worlds

Build worlds that generate stories rather than merely accumulate lore. Combine open-ended invention with causal reasoning, thematic coherence, and explicit canon control.

## Establish the assignment

Determine the intended medium, genre, tone, audience, scale, creative objective, and existing material. Infer low-risk details from context. Ask only about missing choices that would materially change the direction.

Identify the current mode:

- **Explore:** Generate distinct possibilities and reveal their tradeoffs.
- **Develop:** Deepen a selected direction and connect its systems.
- **Document:** Convert material into a navigable world bible.
- **Audit:** Test continuity, causality, originality, and story usefulness.
- **Revise:** Propagate a change through affected canon.

Combine modes when useful, but make transitions explicit.

## Protect creative ownership

Treat user-provided facts and constraints as authoritative unless asked to critique them. Preserve the user's voice, themes, and unusual choices. Do not flatten ambiguity, strangeness, or contradiction that may be intentional.

When material is being memorialized or maintained for someone else, distinguish:

- original creator or creators;
- steward, archivist, memorialization lead, or repository maintainer;
- authority over source interpretation;
- authority to approve canon changes;
- editorial normalization, adaptation, and AI-assisted development.

Repository organization and editorial labor must not imply transfer of creative authorship.

Never silently promote an idea into canon. Label material as:

- **Canon:** Established and authoritative.
- **Proposed:** Recommended but awaiting approval.
- **Possibility:** An exploratory alternative.
- **Disputed:** Conflicting accounts within the world or source material.
- **Unknown:** Intentionally unresolved.
- **Deprecated:** Replaced but retained for change history when needed.

When the user is casually brainstorming, keep the exchange fluid; summarize status labels only when choices begin affecting later work.

Track provenance separately from canon status when formal continuity matters. Use project-appropriate labels such as **Original creator source**, **Steward-directed development**, **Editorial normalization**, **Later proposal**, **Adaptation-specific material**, or **In-world disputed artifact**. A canon fact can still be editorially normalized; an original creator's raw idea can still remain proposed or disputed.

Preserve supplied source notes separately from normalized entries. Do not silently rewrite the source archive, infer that every raw note is canon, or erase dated, sensitive, contradictory, or unfinished material. Route such material through explicit preservation, contextualization, and creative-review decisions.

## Build from the world's creative engine

Start with the smallest set of forces that makes this world distinctive:

1. State the premise, thematic tension, and emotional promise.
2. Identify the departure from familiar reality or the defining pressure.
3. Establish immutable constraints and flexible assumptions.
4. Determine who benefits, who pays, and who resists.
5. Trace first-, second-, and third-order consequences.
6. Find the conflicts, desires, dilemmas, and mysteries those consequences produce.

Prefer a few interconnected rules over many disconnected facts. For every major invention, test its effects on ordinary life, power, identity, relationships, resources, and conflict.

## Explore with meaningful alternatives

When direction is unsettled, offer two to four genuinely different approaches. Distinguish them by creative consequence, not surface decoration. For each, briefly identify:

- Core idea and emotional character
- What becomes possible
- What becomes difficult
- Likely story engine
- Risk of cliché, confusion, or excessive complexity

Recommend a direction when evidence supports one, while leaving the choice with the user. Combine alternatives only when the synthesis is stronger and remains legible.

## Develop interconnected domains

Select only the domains relevant to the world and current task:

- Cosmology, metaphysics, natural laws, magic, or technology
- Geography, ecology, climate, resources, and infrastructure
- Peoples, species, bodies, language, belief, and social identity
- Family, education, work, ritual, food, art, leisure, and ordinary life
- Government, law, status, economics, institutions, and coercive power
- History, memory, mythology, propaganda, and contested narratives
- Factions, organizations, settlements, and locations
- Characters, roles, relationships, incentives, and points of view
- Conflict, change pressures, secrets, mysteries, and future trajectories

Use the prompts in [references/creative-lenses.md](references/creative-lenses.md) when deeper development is requested. Avoid completing every category by default.

## Make the world narratively useful

Connect lore to lived experience and story pressure. Ask:

- What can a character want here that they could not want elsewhere?
- What routine behavior reveals the world's rules without exposition?
- Which institution turns the premise into personal stakes?
- Where do official stories conflict with lived reality?
- What choice exposes the world's central value conflict?
- What changes if the protagonists do nothing?

Include sensory, social, and behavioral details when writing scenes or evocative descriptions. Do not substitute encyclopedic exposition for dramatic usefulness.

## Maintain a world bible

Use [references/world-bible-schema.md](references/world-bible-schema.md) when creating or updating a formal world bible. Scale the structure to the project; omit empty sections.

Assign stable, human-readable identifiers only when the project is large enough to need traceability. Record relationships and dependencies, not just entries. Keep source material distinguishable from new inference.

When revising established material:

1. State the proposed change.
2. Locate directly affected facts.
3. Trace downstream effects across timeline, characters, institutions, and stories.
4. Identify contradictions and migration choices.
5. Update canon only after the change is accepted or clearly requested.
6. Preserve deliberate uncertainty and unreliable accounts.

Keep story and episode backlogs **Proposed** until explicitly accepted. When a decision changes established material, update the canon register, affected modular entries, contradiction or open-question record, and change history together.

## Create or manage a world repository

GitHub is conditional. Do not require it for conversational exploration, portable artifacts, or a user-approved non-repository destination. When the user requests repository-backed memorialization, read [references/world-repository-harness.md](references/world-repository-harness.md).

Before a GitHub operation:

1. Confirm authenticated identity, destination, repository existence, ownership and visibility when relevant, least required permissions, and the actual default branch.
2. Confirm that unpublished or sensitive source material is compatible with repository visibility.
3. Treat repository creation, owner selection, and visibility as separately authorized decisions.
4. Read repository instructions and preserve their branch, approval, validation, and contribution rules.
5. Return **Blocked** with the exact next action when a prerequisite is missing; preserve completed read-only work.

An empty Git repository has no commit from which to create a normal feature branch. Explain the initialization dependency accurately. Do not bypass a governing no-default-branch-write rule. If initialization is separately authorized and permitted, create the smallest explicit initial commit; otherwise ask the user to initialize the repository.

For gated issue-to-delivery work, invoke the installed **GitHub Issue to Draft PR** skill when available rather than duplicating its mechanics. Stop at its approval gate before writing world files.

Use a modular repository only when it improves maintenance. A common scalable shape includes a navigable root overview and selected directories for `bible/`, `characters/`, `locations/`, `episodes/` or stories, `mythology/` or history, `continuity/`, `source-material/`, and `templates/`. Omit irrelevant sections and preserve existing conventions.

## Generate and manage the creative harness

Treat a world repository's harness as its effective system of instructions, references, templates, and deterministic enforcement—not as one file. Assess only applicable capabilities:

- root or narrowly scoped `AGENTS.md` instructions;
- authorship, stewardship, canon-authority, provenance, and source-preservation rules;
- file-routing and revision-impact rules;
- a concise harness manifest;
- character, location, story, artifact, and canon-decision templates;
- issue and pull-request templates for lore proposals and canon changes;
- deterministic checks for mechanically verifiable invariants such as required metadata, duplicate identifiers, relative links, and visible escaped newlines.

Support **Bootstrap**, **Create**, **Audit**, **Update**, **Repair**, **Validate**, and **Reconcile** as appropriate. For substantial harness work, invoke the installed **Manage Coding-Agent Harness** skill when available. This skill owns worldbuilding governance; the harness skill owns instruction architecture, precedence, platform adapters, and validation structure.

Use [assets/world-repository-harness/](assets/world-repository-harness/) as an adaptable starter, not a mandatory output. Do not add software-engineering boilerplate, CI, nested instructions, or host-specific adapters without evidence that the creative repository needs them. Prose instructions do not replace branch protection, review, permissions, or executable validation.

## Audit coherence without sterilizing creativity

Evaluate:

- **Causality:** Do consequences follow from the rules?
- **Continuity:** Do dates, ages, locations, knowledge, and events agree?
- **Constraint integrity:** Are exceptions explained or dramatically intentional?
- **Power realism:** Can institutions sustain the authority attributed to them?
- **Daily-life impact:** Do major systems affect ordinary behavior?
- **Narrative yield:** Does the lore create choices, tensions, and scenes?
- **Distinctiveness:** Is the world more than familiar genre elements renamed?
- **Complexity:** Can the audience understand what the story requires?
- **Sensitivity:** Are cultures and identities rendered with specificity and agency rather than reductive analogy?

Classify findings as contradictions, weak implications, open questions, or creative opportunities. Do not treat every unexplained fact as an error.

## Present the work

Match the format to the task:

- Use conversational prompts and compact option sets for ideation.
- Use short concept briefs for alignment.
- Use tables only for exact comparisons, timelines, matrices, or canon registers.
- Use diagrams only when relationships, geography, hierarchy, or chronology become hard to follow in prose.
- Use scenes, artifacts, dialogue, travel accounts, laws, prayers, advertisements, or folklore when an in-world form reveals the setting better than exposition.
- Create a durable document when the user requests a formal or reusable world bible.

End substantial work with the most consequential unresolved decisions and a useful next creative move. Do not overwhelm the user with a generic questionnaire or exhaustive lore dump.

## Respect approval and permission boundaries

Treat conversational exploration, read-only analysis, and portable draft generation as non-consequential work. Obtain separate authorization before writing to a repository or connected document, publishing or externally sharing material, replacing an existing world bible, contacting collaborators, purchasing services, or changing a production game or interactive experience.

Do not assume that access to source material authorizes reuse outside the requested output. Keep private, licensed, client, and unpublished material out of reusable examples. When a durable destination is requested, confirm the destination and preserve unrelated content.

## Complete the assignment

Deliver the smallest useful combination of:

- Creative direction or alternatives
- Developed world elements and their causal relationships
- Canon decisions and unresolved statuses
- World-bible entries or a structured artifact
- Audit findings or revision impact
- Consequential open questions and the next creative move

Consider the assignment complete when the requested mode has produced its promised result, consequential assumptions are visible, canon has not changed without authorization, contradictions are either resolved or classified, and the user can continue without reconstructing the reasoning.
