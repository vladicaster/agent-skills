# Architecture discovery

Use the section matching the selected starting mode. Preserve evidence classifications throughout discovery.

## Shared intake

Capture:

- audience and decision to support;
- system of interest and boundary;
- current state, target state, or both;
- available repositories, documents, diagrams, and subject-matter expertise;
- operational, regulatory, security, data, cost, and delivery constraints;
- requested notation and artifact destination.

Prefer a small number of material questions. Continue with explicit Unknown or Proposed entries when answers are unavailable.

## Brainstorm mode

1. Extract actors, goals, capabilities, constraints, and quality attributes from the idea or requirements.
2. Propose the system boundary and external dependencies.
3. Propose containers by independently deployable or runnable responsibility, not by arbitrary technical layers.
4. Describe alternatives for consequential choices rather than prematurely selecting one.
5. Mark all unapproved architecture as Proposed.
6. Surface decisions that merit ADRs and questions requiring product, security, operations, or domain input.

Expected evidence is usually user statements and approved requirements. Do not imply that proposed technology already exists.

## Repository-discovery mode

Inspect applicable repository instructions first. Build evidence from the most authoritative available sources, typically:

1. deployment and infrastructure configuration;
2. executable entry points and project manifests;
3. application configuration and dependency wiring;
4. API, messaging, persistence, and external-client code;
5. tests and operational scripts;
6. maintained architecture documentation;
7. general README prose and filenames.

Search for solution and project boundaries, deployables, processes, databases, queues, caches, object stores, identity providers, external APIs, protocols, scheduled jobs, event handlers, and observability paths.

Cross-check documentation against implementation. Record conflicts as Unknown or explicitly describe the current implementation versus intended design. A referenced repository or service that was not inspected is not Observed merely because its name appears elsewhere.

For each important relationship, capture source, destination, purpose, protocol or mechanism when known, and evidence location. Avoid deriving production topology solely from development configuration.

## Existing-system refinement mode

1. Identify the diagram's claimed scope, level, audience, date, and source of truth.
2. Inventory elements and relationships before editing.
3. Compare them with current evidence and list stale, missing, ambiguous, duplicated, or incorrectly leveled items.
4. Preserve stable identifiers and names where practical.
5. Separate corrections to current state from proposed improvements.
6. Explain material removals or boundary changes.

If the diagram cannot be edited in its native format, provide a corrected replacement or a precise change list and mark visual verification Manual.

## Change-impact mode

1. Establish a verified current-state baseline.
2. Trace the change through people, systems, containers, data, integrations, trust boundaries, deployment, and operations.
3. Produce separate current and target views when a combined view would be ambiguous.
4. Mark unchanged, modified, new, deprecated, and removed elements consistently.
5. Record migration, compatibility, rollout, telemetry, rollback, data-conversion, and ownership implications when material.
6. Identify decisions and implementation increments without authorizing them.

## Evidence table

Use a compact record such as:

| Claim or element | Classification | Evidence or basis | Confidence | Impact if wrong |
| --- | --- | --- | --- | --- |
| Public API calls worker | Observed | `src/api/...` and client configuration | High | Incorrect request flow |
| Queue is production transport | Inferred | Local configuration and handler code | Medium | Wrong container relationship |
| Add cache for read path | Proposed | Latency requirement | N/A | Target design changes |
| Production scaling policy | Unknown | No deployment evidence found | N/A | Deployment view incomplete |

Keep the record proportional to the decision. Do not enumerate trivial implementation facts.
