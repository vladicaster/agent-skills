# Validation scenarios

Select the applicable scenarios and adapt domain nouns without weakening the invariant. Verify observable behavior and artifacts, not exact generated wording.

| Scenario | Required evidence |
| --- | --- |
| Greenfield cooperative game | Design identifies server authority, contracts, persistence, solo rules, phases, risks, and approval boundaries without requiring a repository. |
| Multiplayer and solo sessions | Two-player behavior works; solo mode replaces or disables quorum, corroboration, voting, trading, and role-diversity requirements without deadlock or fake players. |
| Simultaneous commands | Only one command at the same expected revision commits; the loser receives `stale_revision`; retrying a completed idempotency key does not duplicate effects. |
| Private information | Player A, unauthenticated callers, ordinary hosts, logs, errors, snapshots, and realtime messages cannot reveal Player B’s secrets. |
| Interrupted generation | A job resumes from its last valid checkpoint; bounded repair, timeout, cancellation, retry exhaustion, and budget exhaustion each reach a specific terminal or resumable state. |
| Live schema upgrade | A retained old-state fixture upcasts deterministically or continues on its compatible ruleset; unsupported newer versions fail safely; the campaign is not regenerated. |
| WebSocket disconnect and migration | Reconnect from a known revision produces missed authorized updates or a safe snapshot without polling; a later SignalR adapter preserves commands, revisions, authorization, clocks, and projections. |
| TypeScript-to-C# migration | Both implementations accept the same normalized fixtures and produce equivalent outcomes, error categories, revisions, events, and viewer projections. |

## Required focused checks

### Continuous simulation scenarios

Use these in addition to the applicable foundation scenarios. Design review establishes whether the agent chose a defensible architecture; only executable target-runtime tests establish deployed behavior.

| Scenario | Required evidence |
| --- | --- |
| Two-player native simulation with only a socket echo demo | Agent marks continuous runtime/coordination evidence missing, identifies the exact verification needed, and does not claim reliability, add polling, or provision a service. |
| Native lightweight room with verified target-runtime evidence | Agent selects the native profile within measured limits and records ownership, lifetime, recovery, load evidence, and migration triggers rather than requiring Ably or an external server by default. |
| Latency-sensitive physics game without native execution guarantees | Agent proposes Sites frontend plus an external authoritative simulator, preserves approval gates, and separates WSS delivery from simulation and storage ownership. |
| Replayed, late, out-of-order, and forged movement inputs | Duplicate controls have no repeated effect; sequence gaps follow the declared bounded policy; actor/time/position claims cannot bypass rules; discrete stale revisions still reject as before. |
| Tick overrun and slow client | Queues and catch-up work remain bounded; superseded updates may coalesce without invalid deltas or lost durable results; overload is observable and follows the declared pause/disconnect policy. |
| Reconnect after checkpoint recovery | Authorized snapshot and new epoch replace incompatible client history without polling; loss stays within the declared bound; acknowledged durable purchases/rewards survive without duplication. |
| Competing room owners after lease expiry | Stale owner is fenced from both commits and authoritative delivery; only the active owner advances accepted truth, and revocation still blocks inputs. |
| TypeScript/C# simulation replay and private deltas | Same fixture inputs, ticks, RNG state, and versions produce equivalent outcomes and recovery; snapshots and deltas contain only viewer-authorized data, including after visibility changes. |

### Implementation checks

Add tests appropriate to the implementation for:

- unauthenticated, nonmember, member, host, former member, and administrative access
- host transfer, leave/disconnect, reconnect, expired presence lease, and abandoned session recovery
- duplicate, missing, delayed, and out-of-order WebSocket messages; slow clients; reconnect from old and current revisions
- invalid commands, phase closure, deadline equality, clock skew attempts, and worker races
- nested, cached, logged, traced, error, object-storage, and generated-prompt information leaks
- duplicate commands in progress and after completion
- failed transactions between state, event, and command-receipt writes
- invalid references, duplicate IDs, unsupported rule types, and structurally valid but unsolvable generated content
- generation attempt, token, cost, time, and artifact-size ceilings
- every rule that assumes more than one participant
- state, command, event, projection, and generation-checkpoint version changes

Use injected clocks and deterministic IDs. Run concurrency checks repeatedly or under controlled scheduling. Property tests are useful for invariants such as conservation of resources, monotonic revisions, one terminal outcome, and absence of secrets from unauthorized projections.

Manual playtesting remains necessary for clarity, pacing, fun, and many forms of solvability. Report it as **manual**, not as a deterministic pass.
