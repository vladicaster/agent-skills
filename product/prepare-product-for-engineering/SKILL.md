---
name: prepare-product-for-engineering
description: Prepare a product for engineering by orchestrating evidence intake, GTM validation, product requirements, approval gates, planning-repository governance, readiness assessment, and a controlled engineering handoff. Use when a product idea or product plan must become decision-ready before solution design or implementation begins.
---

# Prepare Product for Engineering

Move a product from concept or partial documentation to an approved, traceable, engineering-ready planning package. This skill coordinates existing GTM and PRD skills; it does not duplicate them.

## Modes

- **Assess**: inventory current evidence and report readiness gaps.
- **Prepare**: run the complete pre-engineering workflow.
- **Bootstrap**: create the governed planning-repository structure.
- **Reconcile**: align changed evidence, GTM, PRDs, and readiness decisions.
- **Handoff**: package approved inputs for engineering without starting the build.

## Select the dependency path

Use the smallest workflow that closes the readiness gaps:

- If neither GTM nor PRD work is approved, orchestrate both in order.
- If one is approved and compatible with current evidence, reuse it and invoke only the missing skill.
- If both are approved and compatible, do not rerun them; proceed to governance, readiness, reconciliation, or handoff.
- If the user requests only assessment or repository bootstrap, do not invoke either dependency unless the assessment shows it is necessary and the user authorizes the expanded scope.

Treat existing approval as valid unless provenance is missing, evidence materially changed, or GTM and PRD decisions conflict.

## Workflow

### 1. Establish scope and evidence

Record the product boundary, business objective, owners, decision deadline, and requested mode. Inventory source material with provenance and classify each item as fact, inference, assumption, decision, or unknown. Do not silently fill evidence gaps.

Use `assets/evidence-register-template.md` and `assets/decision-log-template.md` when equivalent records do not already exist.

### 2. Validate the go-to-market strategy

If approved, compatible GTM work does not exist, invoke the current `develop-go-to-market-strategy` skill. Preserve its evidence standards, segmentation, ICP, positioning, offer, pricing hypotheses, channels, launch plan, experiments, and readiness gaps.

Stop for explicit approval, revision, or cancellation of the GTM strategy. Do not treat silence as approval.

### 3. Develop product requirements

After GTM approval, if approved, compatible requirements do not exist, invoke the current `develop-product-requirements` skill. Preserve product hierarchy, stable identifiers, journeys, scope, functional and nonfunctional requirements, acceptance criteria, traceability, and validation.

Require explicit PRD approval. If issue decomposition is requested, preserve the PRD skill's separate issue-plan approval gate.

### 4. Govern the planning repository

Create or normalize the structure in `references/planning-repository.md`. Keep market, product, evidence, decisions, and readiness artifacts distinct. Confirm repository privacy before uploading confidential source material. Never place secrets in the repository.

### 5. Assess build readiness

Apply `references/readiness-model.md` and produce `planning/build-readiness.md` from the template. Classify each gate as **Ready**, **Conditionally ready**, **Blocked**, or **Not assessed**. Every conditional or blocked gate needs an owner and next action.

### 6. Produce the engineering handoff

Summarize approved product boundary, GTM decisions that constrain the solution, PRD hierarchy, unresolved risks, dependencies, nonfunctional constraints, validation expectations, and recommended next workflow.

Ask for separate authorization before creating a solution repository, choosing a stack, installing an engineering harness, creating issues, or writing code.

## Dependency compatibility

Read `references/dependency-contract.md` before orchestration. Always use the installed/current GTM and PRD skills. Compare their outputs and gates with the contract:

- **Compatible**: consume the new output directly.
- **Additive**: preserve the new fields and update this orchestrator's mapping when useful.
- **Breaking**: stop, identify the mismatch, and propose a migration before continuing.

When a reusable improvement belongs to GTM or PRD methodology, propose it upstream in that owning skill rather than embedding a divergent copy here. Keep product-specific adaptations in the product planning repository.

## Completion criteria

Complete only when evidence provenance exists, GTM and PRD approvals are explicit, readiness is classified with owners for gaps, and the handoff clearly distinguishes approved inputs from open decisions.

## Boundaries

- Do not fabricate research, customer evidence, approval, or readiness.
- Do not bypass approval gates inherited from dependency skills.
- Do not copy dependency skill bodies into this skill.
- Do not expose confidential material in a public repository.
- Do not begin solution design or implementation without explicit authorization.
