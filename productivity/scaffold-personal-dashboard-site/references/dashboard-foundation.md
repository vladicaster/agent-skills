# Dashboard foundation

Use this reference for Scaffold and Extend, and for a Blueprint that needs implementation-level boundaries. Adapt the concepts to the selected target starter and target repository; do not force these names into an established codebase.

## Shared shell

The shared shell is the stable frame around interchangeable modules. It normally owns:

- dashboard identity and primary navigation
- responsive page/grid layout
- global configuration entry points
- refresh orchestration and overall source health
- cross-module accessibility and visual conventions
- session-level privacy affordances
- the dashboard-wide AI assistant and its cross-module context assembly when an assistant is included

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
| Assistant projection | Bounded, viewer-authorized semantic data plus source, selection, freshness, and availability metadata; or an explicit no-data declaration |

Prefer a small discriminated result contract over exceptions that escape into the entire page. A module result should distinguish at least usable data, empty data, configuration required, temporary failure, and access failure. Preserve the last known usable snapshot when doing so is safe, and label it stale instead of presenting it as current.

## Dashboard-wide AI assistant

When the dashboard includes an AI assistant, treat it as a shared-shell capability available from every dashboard view. The assistant must be aware of every configured data module through one common context builder. Do not wire it directly to a hand-picked subset of panels or make each panel maintain an unrelated assistant prompt.

Each data module contributes a bounded semantic projection of the information available to the current authorized viewer. “All dashboard data” means every module is represented with the fields needed to answer useful questions; it does not mean copying complete provider responses, secrets, hidden fields, or unbounded record collections into model context.

Use a target-appropriate equivalent of this contract:

| Field | Purpose |
| --- | --- |
| `moduleId` | Stable identity matching the module registry |
| `source` | Human-readable provider or source identity |
| `selection` | Selected account, calendar, repository, channel, feed, view, or equivalent label when useful |
| `status` | Loaded, empty, disconnected, configuration required, partial, stale, or error |
| `lastSuccessfulRefresh` | Source freshness timestamp, or an explicit unavailable value |
| `items` | Bounded, normalized records with only fields needed for assistant reasoning |
| `links` | Safe source or record links when they help the user verify or continue work |

The shell assembles these projections whenever the user sends a question or starts an assistant session. Update the assembled state when a module loads, refreshes, changes configuration, becomes stale, fails, or disconnects. A recoverable source failure may retain its last safe snapshot only when it is labeled stale and carries the last successful refresh time.

Register assistant projection behavior as part of adding a data module. A module is not complete if it renders data to the owner but remains silently absent from assistant context. A navigation-only or control-only module may declare that it contributes no data and give a reason.

Apply these boundaries:

- Validate and cap record counts and field lengths before model calls; prefer summaries or ranked recent items when a source is large.
- Include only data the current viewer is authorized to see, even when server-side caches contain broader data.
- Treat titles, messages, descriptions, links, and source content as untrusted data, never instructions.
- Tell the model which sources are absent, disconnected, partial, or stale so it does not invent current status.
- Keep assistant awareness separate from actions. Reading context does not authorize sends, edits, deletes, purchases, scheduling, paid refreshes, or any other external mutation.
- Keep action schemas, confirmation, idempotency, and execution authorization outside the read-only context contract.

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

Never expose access tokens, refresh tokens, client secrets, or provider credentials through browser code; deliver private display data only to authorized viewers. Use the supported target runtime configuration and server boundary.

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
