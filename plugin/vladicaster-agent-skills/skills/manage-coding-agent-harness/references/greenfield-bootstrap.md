# Greenfield Bootstrap

Use when a PRD or project brief exists but a repository does not.

Separate functional requirements, quality attributes, constraints, preferences, assumptions, and open questions. Cover product shape, users, scale, interfaces, data, integrations, realtime work, security, compliance, operations, team capability, budget, delivery timeline, deployment, and AI requirements. Do not convert absent information into facts.

## Propose before generating

Present the requirement summary, missing decisions, assumptions, simplest suitable system shape, one recommended stack, at most one useful alternative, tradeoffs, proposed repository layout, and exact harness deliverables. Stop for approval.

## Portable output

When approved and no repository exists, create a `project-harness/` package containing only applicable files. Mark architecture, stack, commands, and paths as provisional. Include a manifest recording the PRD source, approval status, assumptions, and decisions requiring reconciliation.

When a repository becomes available, compare intent with actual manifests, source layout, tooling, CI, and implementation. Install files at their proper repository locations; do not retain the wrapper directory.
