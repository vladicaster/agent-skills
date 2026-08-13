# Capability Matrix

Use this as an applicability checklist, not as mandatory boilerplate.

| Capability | Evaluate | Typical evidence |
| --- | --- | --- |
| Workflow | Branching, approvals, issue/PR boundaries | Git config, templates, branch rules |
| Scope control | Unrelated changes and requirement expansion | Agent instructions, review policy |
| Architecture | Boundaries, dependency direction, decision ownership | Source layout, ADRs, diagrams |
| Coding standards | Language and framework conventions | Linters, formatters, docs |
| Testing | Appropriate test levels and ownership | Test projects, runners, CI |
| Build validation | Restore, build, lint, format, analysis | Manifests, scripts, workflows |
| Security | Secrets, auth, input handling, dependencies | Config, scanners, threat guidance |
| Resiliency | Timeouts, retry policy, fallback, degradation | Client configuration, runbooks |
| Observability | Logs, metrics, traces, correlation | Telemetry setup, dashboards |
| Technical debt | In-scope handling and out-of-scope recording | Issue policy, review checklist |
| UI quality | Accessibility, responsive behavior, themes | UI stack, design system, tests |
| Data changes | Compatibility, migration, rollback | Migration tooling, data policy |
| APIs | Contracts, errors, compatibility, versioning | Schemas, API docs, tests |
| Configuration | Environments, secrets, safe defaults | Config providers, deployment files |
| Documentation | Behavior and operational updates | Docs tree, PR requirements |
| Validation reporting | Passed, failed, blocked, manual, not run | PR template, agent output rules |
| Release readiness | Diff review, deployment and rollback | Release workflows, runbooks |

Classify each applicable capability as **covered**, **partial**, **missing**, **conflicting**, or **not applicable**, and cite repository evidence.
