# Prepare Product for Engineering

An orchestration skill for converting a product concept or partial plan into an approved, traceable engineering-readiness package before solution design begins.

It can optionally coordinate [`develop-go-to-market-strategy`](../develop-go-to-market-strategy/) and [`develop-product-requirements`](../develop-product-requirements/), then adds planning-repository governance, readiness classification, dependency compatibility, and a controlled handoff. The two dependency skills remain independently usable.

## Optional orchestration\n\nChoose the smallest path needed:\n\n- run both GTM and PRD workflows for a new concept\n- invoke only the missing GTM or PRD stage\n- consume already-approved GTM and PRD artifacts without recreating them\n- run only assessment, repository bootstrap, reconciliation, or handoff\n\nExisting approval remains valid unless new evidence or a material conflict requires reconsideration.\n\n## What it produces

- evidence register and decision log
- approved GTM and PRD artifacts, created by the owning skills
- governed planning-repository structure
- build-readiness assessment with owners and next actions
- engineering handoff that separates approved inputs from open decisions

## Modes

Assess, Prepare, Bootstrap, Reconcile, and Handoff.

## Safety and governance

The skill preserves the approval gates of its dependencies, verifies repository privacy before confidential uploads, and requires separate authorization before any solution repository, stack, harness, issue, or code work.

## Validation

Run:

```bash
python scripts/validate_planning_repo.py /path/to/planning-repository
```

The validator checks the minimum planning structure and canonical readiness states; it does not substitute for human approval.
