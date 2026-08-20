# Dependency contract

## `develop-go-to-market-strategy`

Required semantics: evidence classification; market readiness; segmentation and ICP; positioning and messaging; offer and pricing hypotheses; channels and sales motion; launch plan and experiments; readiness gaps; explicit approve, revise, or cancel gate.

## `develop-product-requirements`

Required semantics: product hierarchy; stable requirement identifiers; evidence and decision traceability; journeys; scope; functional and nonfunctional requirements; acceptance criteria; validation; explicit PRD approval; separate approval before issue-plan creation.

## Change handling

At runtime, prefer the current installed dependency. Treat renamed fields as compatible when semantics remain intact. Preserve additive outputs. Treat removed gates, lost traceability, incompatible identifier rules, or changed approval semantics as breaking changes and stop for reconciliation.

General methodology fixes should be contributed to the owning dependency. This skill should contain only orchestration, compatibility mapping, repository governance, readiness, and handoff logic.
