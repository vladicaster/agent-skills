---
name: scaffold-personal-dashboard-site
description: Design, scaffold, or extend a modular personal dashboard for ChatGPT Sites. Use for personal command centers, daily briefs, or configurable dashboard workspaces; do not use for generic websites, enterprise BI systems, or static reports.
---

# Scaffold Personal Dashboard Site

Create the smallest useful personal dashboard foundation, then leave clear seams for the owner to personalize it. Build a working surface, not a page that advertises a dashboard.

Preserve this boundary:

> A configured module may display or act on a source only through a verified path available to the deployed Site. A ChatGPT connector is not automatically a Site runtime API.

## Select the mode

- **Blueprint:** Produce a read-only dashboard concept, module map, source-feasibility assessment, and implementation plan.
- **Scaffold:** Create a new dashboard Site using the current installed Sites building workflow.
- **Extend:** Add or revise modules in an existing dashboard while preserving its established architecture, design, and working behavior.

If the user asks to create, build, or scaffold the dashboard, select Scaffold. If they provide an existing Site or repository, select Extend. Otherwise prefer Blueprint when implementation intent is unclear.

## Discover the useful first version

Infer what is already clear. Ask at most three concise questions only when the answers materially change functionality, privacy, or runtime feasibility.

Determine:

- who uses the dashboard and the primary decision or action it supports
- what the first viewport must show
- timezone and freshness expectations
- requested modules and which actions, if any, can change external data
- privacy expectations and whether publishing is requested now
- existing Site, repository, design system, and source configuration

Avoid a generic module checklist when the user's purpose already implies a coherent first version. Do not copy another person's dashboard, prompts, accounts, private URLs, or source-specific rules.

## Classify every requested source

For Scaffold or Extend, read [source-integrations.md](references/source-integrations.md). Classify each source as local/static, Sites storage, public HTTP, authenticated runtime API, or blocked. Verify the actual runtime path before promising live data.

Treat authentication, authorization, configuration, and data access as separate facts. Never imply that installing this skill, connecting an app to ChatGPT, or viewing data in the current conversation makes that data available to deployed Site code.

When a source is not ready, either:

- scaffold a clearly labeled disconnected/configuration-required state when that still provides a useful result; or
- return **Blocked** with the exact capability, connection, or user choice needed.

Never place credentials, tokens, private source payloads, or personal identifiers in client code, committed files, examples, screenshots, or generated documentation.

## Blueprint workflow

1. Describe the dashboard's primary job and first viewport.
2. Propose only the modules required for a coherent first version.
3. For each module, record its purpose, source class, configuration, freshness, actions, privacy, and failure behavior.
4. Define the shared shell and module boundaries using [dashboard-foundation.md](references/dashboard-foundation.md).
5. Identify assumptions, blocked sources, approval boundaries, validation scenarios, and deferred modules.
6. Deliver the blueprint without creating files, connections, accounts, or deployments.

## Scaffold or Extend workflow

1. Inspect applicable repository instructions and the existing Site when present. Preserve its package manager, lockfile, architecture, hosting configuration, and design conventions.
2. Read [dashboard-foundation.md](references/dashboard-foundation.md) and select the relevant scenarios from [validation-scenarios.md](references/validation-scenarios.md).
3. Present a compact scope when a material product, privacy, or source-feasibility decision is unresolved. Do not add a separate approval gate for ordinary visual choices.
4. Use the current installed Sites building skill for project initialization, implementation, preview, build, and platform-specific decisions. For a new project, tell that workflow to save without deploying unless publication is already explicit and authorized.
5. Implement the dashboard as a modular working surface:
   - make the primary information or control visible in the first viewport
   - separate the shared shell, module registry, display components, source adapters, configuration, and secrets
   - give each module independent loading, empty, disconnected, stale, refreshing, success, and error behavior as applicable
   - keep one failed source from blanking or disabling unrelated modules
   - make refresh idempotent where repeated requests could otherwise duplicate effects
   - show source status and last successful refresh when they help the owner judge trustworthiness
   - support mobile and desktop layouts, keyboard use, readable text, and meaningful focus states
6. Use realistic generic sample data only when live data is unavailable and examples are needed to understand the starter. Label it clearly and keep it easy to replace.
7. Show the first meaningful preview using the Sites workflow, then complete the approved scope.
8. Exercise the selected validation scenarios. Report checks as **passed**, **failed**, **blocked**, **manual**, or **not run**.
9. If publication is requested and authorized, use the current installed Sites hosting skill. Otherwise stop with the completed preview or source and explain that publishing remains a separate action.

## Module selection rules

Email, calendar, tasks, GitHub, Notion, YouTube, RSS, weather, jobs, bookmarks, and custom APIs are examples, not a mandatory inventory.

- Include a module only when it advances the dashboard's primary job.
- Prefer a small complete dashboard to a large collection of placeholders.
- Keep account, view, repository, channel, feed, or equivalent source selection configurable when the provider supports it.
- Separate read actions from writes. A read connection never authorizes sending, editing, deleting, purchasing, scheduling, or otherwise mutating external state.
- Do not provision accounts, enable APIs, incur paid usage, or create repositories without separate authorization.
- Use browser storage only for device-local preferences or explicitly local data. Use supported server-side storage for durable or shared state.

## Approval and execution boundaries

Blueprint is read-only. A request to scaffold or extend authorizes only the named workspace or repository changes. It does not automatically authorize GitHub writes, connector authorization, credential creation, infrastructure provisioning, paid services, third-party mutations, destructive migrations, exposure of private data, or publication.

Treat an explicit request such as “publish,” “deploy,” or “make it available on Sites” as publication authorization when the target is clear. Otherwise ask immediately before invoking the hosting workflow. Never treat silence as approval.

## Completion criteria

Blueprint is complete when it identifies the first useful version, module/source contracts, feasibility, privacy, approvals, validation, and deferred work.

Scaffold or Extend is complete when the dashboard opens on a useful working surface; requested modules have verified live paths or honest disconnected states; module failures remain isolated; refresh and freshness are understandable; responsive and keyboard behavior are usable; secrets and private data are protected; applicable scenarios are reported honestly; and publication either completed through the Sites hosting workflow or remains clearly unperformed.
