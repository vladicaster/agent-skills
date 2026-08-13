---
name: develop-product-requirements
description: Discover, develop, audit, refine, change, decompose, validate, and reconcile product requirements documents with stable identifiers and end-to-end traceability. Use when a user wants to turn an idea, product evidence, existing PRD, platform, product, subproduct, feature, or change request into decision-ready requirements, journeys, scope, functional and nonfunctional requirements, acceptance criteria, product hierarchy, change impact, or a proposed mapping from one PRD to multiple GitHub issues and pull requests.
---

# Develop Product Requirements

Create decision-ready product requirements that state what must be true and why without silently prescribing implementation. Support platforms containing multiple products and subproducts, multiple PRDs at each appropriate level, and many-to-many traceability across requirements, GitHub issues, pull requests, tests, and acceptance evidence.

## Select the mode

- **Discover:** Structure a product idea, problem, and missing decisions.
- **Develop:** Produce a complete PRD.
- **Audit:** Evaluate an existing PRD without changing it.
- **Refine:** Improve requirements using feedback or new evidence.
- **Change:** Analyze and apply an approved change to an existing PRD.
- **Decompose:** Propose epics, capabilities, delivery slices, and GitHub issues from an approved PRD.
- **Reconcile:** Align requirements with research, implementation, issue, or validation evidence.
- **Validate:** Check readiness, hierarchy, identifiers, and traceability without changing artifacts.

## Phase 1: Establish context and hierarchy

1. Confirm the platform, product, subproduct, feature, owners, business objective, target users, maturity, constraints, and definition of success.
2. Read `references/product-hierarchy.md`. Discover existing catalogs and PRDs before assigning identifiers.
3. Assign stable identifiers for platform, product, subproduct, PRD, requirements, nonfunctional requirements, metrics, and acceptance criteria.
4. Record parent relationships and inherited requirements. Do not duplicate platform policy into every product or PRD.
5. Gather available product evidence and read `references/evidence-and-assumptions.md`. Separate verified evidence, company-provided facts, stakeholder decisions, inference, assumptions, and open questions.

## Phase 2: Define the product requirements

1. Define the problem, affected users, current alternatives, importance, evidence, outcomes, and success measures.
2. Read `references/journeys-and-scenarios.md` and model primary, alternate, failure, recovery, permission, and operational paths.
3. Establish must-have, should-have, optional, out-of-scope, deferred, and open-decision boundaries using `references/prioritization-and-scope.md`.
4. Write traceable functional requirements using `references/functional-requirements.md`.
5. Evaluate applicable quality attributes using `references/nonfunctional-requirements.md`.
6. Write testable acceptance criteria using `references/acceptance-criteria.md`.
7. Address applicable UX, accessibility, data, integrations, security, privacy, analytics, observability, dependencies, risks, rollout, support, migration, compatibility, and operational readiness.
8. Build evidence-to-objective-to-requirement-to-acceptance traceability.

## Phase 3: Present for approval

Present:

- product hierarchy and document ownership
- problem and evidence
- users, journeys, and outcomes
- scope and priorities
- requirements and acceptance criteria
- quality attributes
- data, integration, UX, analytics, security, and operational implications
- dependencies, risks, assumptions, and open decisions
- traceability coverage and readiness gaps
- exact artifacts to create or update

Ask the user to **approve**, **revise**, **defer**, or **cancel**. Do not treat a PRD as authoritative until approval is unambiguous.

## Phase 4: Decompose an approved PRD

1. Read `references/issue-decomposition.md` and `references/traceability.md`.
2. Split work into independently valuable and verifiable slices rather than technical layers alone.
3. Map every requirement and acceptance criterion to proposed issues. Allow one requirement to map to many issues and one issue to cover multiple related requirements.
4. Support multiple repositories and identify dependencies, sequencing, validation, migration, documentation, and operational work.
5. Check for orphaned requirements, unapproved scope, oversized issues, and missing acceptance evidence.
6. Present the complete issue plan and ask for separate approval before creating GitHub issues.
7. After approval, hand each issue to an authorized GitHub workflow. Do not begin implementation.

## Phase 5: Manage change and reconciliation

1. Read `references/change-management.md`.
2. Record the proposed change, reason, evidence, decision owner, affected requirements, and effective version.
3. Determine affected products, subproducts, PRDs, issues, PRs, tests, documentation, analytics, releases, and inherited requirements.
4. Preserve stable identifiers. Mark removed requirements superseded or retired instead of silently reusing IDs.
5. Revalidate traceability and acceptance coverage after the change.

## Validation

Use:

- `scripts/validate_prd.py` for required PRD sections and stable requirement identifiers.
- `scripts/validate_hierarchy.py` for catalog identifiers, parent references, and PRD placement.
- `scripts/build_traceability.py` for requirement-to-issue coverage and a human-readable traceability report.

Report validation as **passed**, **failed**, **blocked**, **manual**, or **not run**.

## Boundaries

- Do not invent customer evidence, numerical targets, market facts, or stakeholder approval.
- Do not disguise assumptions as requirements.
- Do not silently expand scope or rewrite approved requirements.
- Do not select frameworks, databases, deployment topology, service boundaries, or internal implementation unless they are hard constraints supplied by the user.
- Do not create GitHub issues, modify code, start implementation, contact stakeholders, or approve the PRD without separate authorization.
- Keep requirement statements testable and solution-neutral where practical.
- Preserve lineage across platform, product, subproduct, PRD, requirement, issue, PR, test, and acceptance evidence.
