# Validation scenarios

Select the applicable scenarios and adapt domain nouns without weakening the invariant. Verify observable behavior and artifacts, not exact generated wording.

| Scenario | Required evidence |
| --- | --- |
| Greenfield cooperative game | Design identifies server authority, contracts, persistence, solo rules, phases, risks, and approval boundaries without requiring a repository. |
| Multiplayer and solo sessions | Two-player behavior works; solo mode replaces or disables quorum, corroboration, voting, trading, and role-diversity requirements without deadlock or fake players. |
| Simultaneous commands | Only one command at the same expected revision commits; the loser receives `stale_revision`; retrying a completed idempotency key does not duplicate effects. |
| Private information | Player A, unauthenticated callers, ordinary hosts, logs, errors, polling, and realtime notifications cannot reveal Player B’s secrets. |
| Interrupted generation | A job resumes from its last valid checkpoint; bounded repair, timeout, cancellation, retry exhaustion, and budget exhaustion each reach a specific terminal or resumable state. |
| Live schema upgrade | A retained old-state fixture upcasts deterministically or continues on its compatible ruleset; unsupported newer versions fail safely; the campaign is not regenerated. |
| Polling-to-realtime upgrade | Commands, revisions, authorization, clocks, and projections remain unchanged; realtime delivery only notifies or transports an already-authorized view. |
| TypeScript-to-C# migration | Both implementations accept the same normalized fixtures and produce equivalent outcomes, error categories, revisions, events, and viewer projections. |

## Required focused checks

Add tests appropriate to the implementation for:

- unauthenticated, nonmember, member, host, former member, and administrative access
- host transfer, leave/disconnect, reconnect, expired presence lease, and abandoned session recovery
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
