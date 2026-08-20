# C4 model guidance

## Model elements

- **Person:** a human role or persona interacting with a software system.
- **Software system:** the highest-level system of interest or an external software system.
- **Container:** an independently runnable or deployable application, service, data store, job, or client application with a distinct responsibility.
- **Component:** a significant structural unit inside one container, described at a stable architectural level.
- **Relationship:** a directional interaction with a concise purpose and, when useful, technology or protocol.

Do not treat infrastructure nodes, source folders, namespaces, or generic technical layers as containers without evidence that they represent independently runnable or deployable responsibilities.

## View selection

### System Context

Use when the audience needs scope, users, business-facing purpose, or external dependencies. Keep internal containers out of this view.

### Container

Use when the audience needs major runtime responsibilities, data ownership, integration paths, or deployment-unit boundaries. Include technologies only when they improve the decision or explanation.

### Component

Use only when all are true:

- one container is clearly selected;
- the audience needs its internal structure;
- components have meaningful, stable responsibilities;
- relationships are supported by evidence or labeled Proposed;
- the view will not merely reproduce folders or classes.

### Code

Generate only on explicit request. State the revision or evidence basis because code structure changes quickly. Prefer class, module, or dependency tooling native to the implementation ecosystem.

## Supplemental views

- **Dynamic:** show an important multi-step interaction or failure path.
- **Deployment:** map containers to runtime environments or infrastructure nodes when topology evidence exists.
- **Data flow:** emphasize data classification, transformation, ownership, or movement.
- **Trust boundary:** emphasize identity, authorization, network zones, or sensitive data crossings.
- **Current versus target:** explain architectural change without presenting proposals as existing behavior.

Supplemental views do not replace the core C4 hierarchy when that hierarchy is needed.

## Modeling rules

1. Give every element a concise name, type, and responsibility.
2. Use role names for people rather than individual names.
3. Name relationships with verbs that explain purpose; avoid unlabeled arrows.
4. Keep direction consistent with the primary interaction, and explain important asynchronous or bidirectional behavior.
5. Use the same name for the same element across every view.
6. Show the system boundary explicitly.
7. Avoid mixing Context, Container, and Component elements in one view unless the exception is necessary and explained.
8. Prefer fewer readable elements over exhaustive low-value detail.
9. Add technology labels only when observed or proposed and decision-relevant.
10. Use legends for evidence status, lifecycle status, or other visual encodings.

## Notation selection

### Mermaid

Choose for Markdown portability, conversational rendering, and repositories without established architecture tooling. Standard Mermaid flowcharts may express C4 concepts more reliably across renderers than implementation-specific C4 extensions. Label element types and boundaries explicitly.

### C4-PlantUML

Choose when the destination already renders PlantUML, the user requests C4-PlantUML, or consistent C4 macros are valuable. Verify include policy and renderer availability before depending on remote includes.

### Structurizr DSL

Choose when the architecture should be maintained as a reusable model with multiple views, relationships, styles, and workspace-level consistency. Validate with the destination's Structurizr tooling when available.

Syntax validation confirms parsability only. Semantic and visual review remain separate checks.
