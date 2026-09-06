# Security and concurrency

## Trust boundaries

Assume the client can alter requests, replay commands, forge displayed identifiers, inspect its traffic, disconnect strategically, and open multiple connections. Authentication establishes a subject; membership and permissions must still be loaded server-side for the target session.

Check permissions at the command boundary and again where sensitive records are queried. Scope every session-owned query by session ID plus the authorized membership/tenant boundary. A host is a game role, not an administrator by default.

## Concurrency contract

Use optimistic concurrency for the initial design:

- Clients submit `expectedRevision`.
- The persistence update succeeds only when the stored revision matches.
- State, event/audit record, and idempotency receipt commit atomically.
- A stale command returns the current revision and a safe refreshed projection; it is never silently replayed against new state unless the command contract explicitly defines safe rebasing.
- A repeated idempotency key returns the original completed result or an in-progress status.

Serialize commands per hot session through database concurrency or a narrow application lock if needed. Do not rely on one-process memory locks when multiple instances can handle the same session.

## Private-state protection

- Load only the secret records needed by the projector when practical.
- Construct shared and private DTOs separately from persistence/domain objects.
- Do not serialize canonical state and then delete secret fields.
- Scrub logs, traces, analytics, errors, realtime payloads, caches, and generation prompts.
- Authorize object-storage downloads and use short-lived access when private artifacts are externalized.

Test with two or more distinct identities. Snapshot tests should assert absence of forbidden names, identifiers, values, and nested paths—not merely presence of expected fields.

## Clocks and scheduled work

Commands evaluate time using a server clock in the same transaction or consistency boundary as the transition. Background workers should claim due work using leases and idempotent transitions. Multiple instances may race; exactly one durable state change should win.

## Recovery and audit

Recovery should distinguish transient infrastructure failure, invalid content, exhausted retry/budget, incompatible schema, and operator cancellation. Preserve correlation identifiers without logging secrets. Audit records should answer who attempted what, against which revision, when, and with what outcome.

Rate-limit joins, guesses, votes, messages, generation starts, and other abuse-prone commands. Define retention and deletion behavior for chat, evidence, model prompts/responses, and player identifiers.
