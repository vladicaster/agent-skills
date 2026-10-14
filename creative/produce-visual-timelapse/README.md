# Produce Visual Timelapse

Create a coherent visual history or transformation with stable geography, dated milestones, camera choreography, and synchronized time overlays. Use it for miniature aerial city histories, building/site transformations, landscape evolution, or fictional-world growth.

## Use and modes

Choose Research, Blueprint, Prototype, Produce, Adapt, or Review. Start from a subject, source video, existing timeline, or editable scene. Ordinary footage speed changes and standalone image generation are outside this skill's scope.

Example: “Use $produce-visual-timelapse to plan a 25-second miniature 3D harbor-town history with five milestones, a moving year counter, and a final aerial reveal.”

## Workflow and outputs

1. Establish scope, factual or fictional intent, format, audio, tools, and budget.
2. Research dated milestones with traceable evidence and honest date precision.
3. Build stable world entities and explicit lifecycle intervals.
4. Map historical time to video time and choreograph the camera.
5. Choose persistent 3D, layered 2.5D, or an explicitly illustrative hybrid.
6. Render a small proof, review continuity, and then scale to the requested film.
7. Finish exact labels and audio, verify the actual video, and deliver the selected revision.

Research returns an evidence ledger. Blueprint returns a world/timeline manifest and shot plan. Production returns a playable video and requested editable assets. A scene preview alone is not production completion.

## Dependencies and boundaries

GitHub and an existing repository are unnecessary unless repository delivery is requested. Rendering requires an available renderer and export path; AI generation additionally requires a supported connected provider and authorization under its current spending rules.

The optional produce-reference-driven-video skill owns provider preflight, generation tracking, reference roles, and audiovisual finishing. Reuse compatible approved artifacts and invoke only missing stages. This skill owns temporal world continuity and historical mapping. Neither dependency is required for a planning-only task.

Publication, account creation, credit purchases, external communication, and private-media disclosure require applicable authorization. Historical research and automated video analysis do not establish music rights. Do not place private project material into the public skill source.

## Included resources

- references/reference-style.md: visual grammar derived from the supplied aerial evolution reference, with evidence limits.
- references/world-and-timeline.md: entity lifecycle, evidence, time mapping, camera, render record, and fictional proof example.
- agents/openai.yaml: OpenAI skill presentation.

## Validation

From the repository root run:

```bash
python scripts/validate_repository.py
```

Run the host skill creator's quick_validate.py on this directory when available. These checks validate structure, not historical truth, renderer capability, or final-film quality. Forward-test planning with a fictional town, conflicting historical dates, and a production request lacking a renderer; run an actual proof render separately before claiming production readiness.

## Installation

Install the complete directory, including references. In ChatGPT Work, use the supported Skills workflow or provide the GitHub directory URL for the current task. This does not imply every host automatically installs or refreshes a skill.

For Codex, copy this directory to ~/.agents/skills/produce-visual-timelapse or a project's .agents/skills/ directory. For Claude Code, use ~/.claude/skills/produce-visual-timelapse or a project's .claude/skills/ directory. Invoke by skill name or ask for a matching timelapse workflow.

## Updating this skill

Installed copies are snapshots. Pull the source checkout, compare local customizations, and explicitly replace the complete installed directory. A symlink follows its checkout. Pin a tag or commit for reproducible workflows and review permission changes before updating.

## Limitations

The skill is procedural guidance, not a bundled rendering engine or historical dataset. It does not guarantee documentary precision, asset availability, or arbitrary-length generation. Approximate geometry and illustrative animation must be identified. Verify current provider capabilities rather than relying on a fixed model list.
