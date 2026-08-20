---
name: develop-c4-architecture
description: Develop, discover, audit, refine, and communicate C4 architecture models from product ideas, requirements, repositories, existing diagrams, and proposed changes. Use when an agent should brainstorm system boundaries and responsibilities; generate System Context, Container, or evidence-supported Component diagrams; explain current or target architecture; assess change impact; or validate C4 diagrams and their supporting evidence.
---

# Develop C4 Architecture

Produce decision-useful architecture models without presenting assumptions as facts.

## Establish the engagement

1. Identify the audience, decision, scope, desired output location, and required notation.
2. Select a starting mode:
   - **Brainstorm:** propose architecture from an idea, conversation, or requirements.
   - **Repository discovery:** derive current state from repositories and documentation.
   - **Existing-system refinement:** audit, correct, or extend supplied diagrams.
   - **Change impact:** compare current and proposed states for a change.
3. Confirm whether the request authorizes analysis only, artifact creation, or repository writes. Do not infer permission to write, publish, adopt an ADR, implement, deploy, or alter production.
4. Reuse compatible approved requirements and architecture artifacts. Do not require another skill merely because its output could be useful.

Read [architecture discovery](references/architecture-discovery.md) for the selected mode. For repository-backed work, read applicable repository instructions before inspecting implementation evidence or proposing writes.

## Build the evidence model

Record every material statement in one of four classes:

- **Observed:** explicitly supported by inspected evidence.
- **Inferred:** strongly suggested by evidence but not explicitly confirmed.
- **Proposed:** recommended target-state design requiring a decision or approval.
- **Unknown:** unresolved information that may affect correctness or usefulness.

Attach a source path, document, URL, or user statement to important Observed claims. Explain the basis and confidence for important Inferred claims. Never relabel an inference as observed merely because it seems likely.

Determine people, software systems, system boundaries, external dependencies, containers, data stores, protocols, responsibilities, trust boundaries, and material operational constraints. Ask only questions whose answers materially change the model; otherwise continue with labeled assumptions.

## Select the smallest useful view

Read [C4 model guidance](references/c4-model-guidance.md), then select only the views needed for the audience and decision:

- Use **System Context** to explain scope, people, and external systems.
- Use **Container** to explain deployable or runnable units, data stores, responsibilities, and major communication paths.
- Use **Component** only for a selected container when evidence and the decision justify the additional detail.
- Use **Code** only when explicitly requested and source evidence is sufficiently stable; prefer native code-navigation artifacts for routine implementation detail.

Add deployment, dynamic/request-flow, data-flow, trust-boundary, or current-versus-target views only when they communicate an important relationship that the selected C4 views do not.

## Choose notation

- Default to Mermaid for portable Markdown and conversational output.
- Use C4-PlantUML when requested or already established by the destination.
- Use Structurizr DSL when requested, already established, or when a reusable model with multiple generated views is the desired artifact.
- Preserve an existing notation unless changing it has a clear user-approved benefit.

Use [C4 templates](assets/c4-templates.md) as starting material, not as a substitute for evidence or judgment.

## Generate the architecture package

Produce the applicable parts of this package:

1. **Purpose and scope:** audience, decision, system boundary, and mode.
2. **Diagram set:** the smallest useful set of consistently named views.
3. **Architecture narrative:** responsibilities, major interactions, constraints, and important tradeoffs.
4. **Evidence record:** Observed and Inferred claims with their basis.
5. **Proposal record:** Proposed elements, alternatives, and decisions still requiring approval.
6. **Unknowns:** unresolved questions ranked by architectural impact.
7. **Validation result:** Passed, Failed, Blocked, Manual, or Not run for each relevant check.

For change-impact work, label current and target states explicitly. Do not mix existing and proposed elements in one diagram unless the legend makes their status unmistakable.

## Validate

Apply the [diagram quality checklist](references/diagram-quality-checklist.md). Verify:

- audience and purpose are stated;
- scope and boundaries are unambiguous;
- names and responsibilities remain consistent across views;
- relationships are directional and meaningfully labeled;
- abstraction levels are not mixed without explanation;
- every material current-state claim is observed or labeled inferred;
- proposed elements and unresolved decisions are unmistakable;
- diagrams remain readable at the intended rendering size;
- notation parses or renders when a supported validator is available;
- repository links and artifact paths resolve when files are written.

Do not call visual inspection or semantic correctness passed merely because syntax validation succeeded.

## Handoffs and boundaries

- Identify ADR candidates, but do not adopt or publish ADRs without authorization.
- Identify coding-harness guidance affected by approved architecture, but do not update a harness unless requested.
- Identify implementable increments, but do not create issues or change code unless separately authorized.
- Treat architecture diagrams as models of evidence and decisions, not proof of runtime behavior, security, performance, or production topology.
- Report insufficient evidence as Blocked or Unknown rather than fabricating completeness.

## Completion

Finish when the requested architecture package is delivered, evidence status is visible, material unknowns are surfaced, relevant validation is reported honestly, and any authorized files are saved at the agreed destination.
