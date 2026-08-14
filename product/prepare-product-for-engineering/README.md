# Prepare Product for Engineering

An orchestration skill for converting a product concept or partial plan into an approved, traceable engineering-readiness package before solution design begins.

It coordinates [`develop-go-to-market-strategy`](../develop-go-to-market-strategy/) and [`develop-product-requirements`](../develop-product-requirements/), then adds planning-repository governance, readiness classification, dependency compatibility, and a controlled handoff.

## What it produces

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
