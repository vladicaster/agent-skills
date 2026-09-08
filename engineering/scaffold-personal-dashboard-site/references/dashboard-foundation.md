# Dashboard foundation

Use this reference for Scaffold and Extend, and for a Blueprint that needs implementation-level boundaries. Adapt the concepts to the current Sites starter and target repository; do not force these names into an established codebase.

## Shared shell

The shared shell is the stable frame around interchangeable modules. It normally owns:

- dashboard identity and primary navigation
- responsive page/grid layout
- global configuration entry points
- refresh orchestration and overall source health
- cross-module accessibility and visual conventions
- session-level privacy affordances

The shell does not own provider-specific fetching, parse source payloads, or erase a module's usable cached data because another source failed.

## Module boundary

Each module should declare enough information for the shell to compose it without knowing provider details.

| Concern | Expected behavior |
| --- | --- |
| Identity | Stable module ID and human-readable title |
| Purpose | The decision, information, or action the module supports |
| Placement | Default size/order that can adapt responsively |
| Source | Adapter identity and source configuration reference |
| Refresh | Manual, scheduled, event-driven, or static policy |
| State | Loading, empty, disconnected, stale, refreshing, success, or error |
| Freshness | Last attempted and last successful refresh when meaningful |
| Actions | Explicitly declared read or mutation capabilities |
| Privacy | Audience and sensitivity classification |

Prefer a small discriminated result contract over exceptions that escape into the entire page. A module result should distinguish at least usable data, empty data, configuration required, temporary failure, and access failure. Preserve the last known usable snapshot when doing so is safe, and label it stale instead of presenting it as current.

## Refresh behavior

- A dashboard-wide refresh coordinates independent module requests; it is not one all-or-nothing transaction.
- One module failure must not suppress successful results from others.
- Prevent overlapping refreshes for the same module unless the source explicitly supports them.
- Use idempotency for any refresh path that can enqueue work or create records.
- Show when data was last successfully refreshed, not merely when the user last clicked refresh.
- Keep previously usable data visible during a recoverable refresh when privacy and correctness permit it.
- Bound retries and stop repeating requests that fail for a permanent configuration or authorization reason.

## Configuration model

Keep safe display preferences separate from source secrets and server-owned configuration.

Examples of safe user-selectable configuration include module order, collapsed state, timezone, selected repository, selected calendar, feed URL, channel ID, or result limit. Whether a value is safe for client storage depends on its sensitivity and the target runtime.

Never expose access tokens, refresh tokens, client secrets, provider credentials, private API payloads, or administrative identifiers to browser code. Use the supported Sites runtime configuration and server boundary.

## First viewport

The first viewport should help the owner orient and act immediately. Prefer:

1. the highest-priority summary or status,
2. one or two primary controls,
3. the most important module results,
4. compact freshness or connection context.

Do not place a marketing hero, feature tour, or oversized greeting before the working surface. A greeting is useful only when it supports orientation and does not displace the dashboard's purpose.

## Evolution seams

Design the starter so another module can be added without rewriting the shell. Avoid premature plugin systems, dynamic code loading, universal schemas, or complex drag-and-drop builders. A typed registry and consistent adapter/view boundary are usually sufficient for the first version.

Add shared persistence, queues, caching, or background work only when a selected module needs them. Record why each capability exists so a generic starter does not quietly become an infrastructure platform.
