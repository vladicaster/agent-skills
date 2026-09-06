# Real-time graphical simulation

Read this when a game needs continuous movement, physics, or simulation between player actions. Animated graphics alone do not require a continuous server loop. Preserve the distinction between browser rendering, message transport, authoritative simulation, and durable recovery.

## Select an execution profile

| Profile | Appropriate starting point | Required evidence |
| --- | --- | --- |
| Sites-native lightweight rooms | Bounded session simulations whose runtime requirements can be met in the target Sites environment | Verified room routing/ownership, server execution lifetime, timer behavior, reconnect delivery, recovery, and load results |
| Sites frontend with external authoritative simulator | Continuous or latency-sensitive simulation whose requirements are unsupported or unverified in Sites | Approved external hosting boundary, authenticated WSS access, single-owner room execution, persistence/recovery, and measured capacity |

Do not select by genre alone. A graphical strategy game can be event-driven; a two-player physics game can require a demanding continuous loop. Ably or another shared delivery service may supply fan-out and presence, but does not execute authoritative simulation or solve room ownership. Keep it optional and separately approved.

Before committing to Sites-native continuous execution, record sources, dates, target configuration, and test evidence for:

- inbound WebSocket handling and any external WSS connectivity needed by the chosen profile
- how all inputs for a room reach one authoritative owner, including across instances
- timer scheduling, request/connection lifetime, idle suspension, process restart, and execution limits
- ownership transfer and prevention of stale owners publishing or committing state
- authorized fan-out, reconnect/resynchronization, and membership revocation
- latency, jitter, tick overruns, room/player limits, message bandwidth, queue depth, and recovery time under target load

Use current official runtime documentation and authorized deployed tests. A local socket echo test or small player count does not establish these guarantees. State undocumented capabilities as unknown, not unsupported facts. If essential evidence is unavailable, mark native continuous execution **blocked** or **deferred**, name the missing verification, and offer an external-server design or an explicitly approved event-driven simplification. Do not silently provision services, relax requirements, or introduce polling.

## Four independent rates and responsibilities

- **Rendering:** The browser draws and interpolates locally. Its frame rate is not the server's tick or network update rate.
- **Simulation:** Deterministic server code advances a documented time step and applies validated inputs. Inject the clock, seed randomness, and define numerical precision and update order.
- **Delivery:** Send viewer-scoped snapshots or deltas at a bounded rate selected for latency and bandwidth targets. WebSockets carry inputs and updates; they are not gameplay authority.
- **Persistence:** Checkpoint recoverable simulation state at an explicit cadence and persist critical durable actions according to their stronger guarantees. Do not require a database write per render frame or per tick by default.

Treat any proposed frequency as a target to measure, not a Sites or SignalR guarantee. Bound catch-up steps after stalls; choose and disclose pause, slow-down, resynchronization, or termination behavior instead of an unlimited catch-up loop. Keep model calls outside the simulation loop. Consume only bounded, validated, versioned content at deterministic activation boundaries.

## Input and snapshot contract

Keep revision-protected discrete commands in [game-state-contract.md](game-state-contract.md). Buying an item, joining, or making a durable choice must not lose its atomicity/idempotency guarantees because movement was added.

For continuous inputs, define a separate versioned envelope and processing policy:

- session ID, server-issued input-stream epoch, monotonically increasing per-player input sequence, input type/version, and bounded payload; derive the actor from authenticated membership
- desired controls, not trusted positions, velocities, hit results, elapsed time, or client outcomes
- deterministic handling of duplicate, old, missing, late, future, and out-of-order sequences; bound reorder windows and queues, and define whether missing controls hold briefly or become neutral
- a server-issued mapping to application tick, with bounded client time hints only if the rules need them; constrain input frequency and per-tick effects to prevent speed cheats
- acknowledgments distinguishing received, applied, rejected, and durable state; report the last processed sequence plus rejected/skipped ranges when a cumulative acknowledgment would otherwise be ambiguous

Do not demand the latest global session revision on every movement sample: other players and server ticks advance independently. The room owner serializes accepted inputs and discrete commands with a defined ordering at the authoritative boundary. Keep one shared authority for interactions between durable inventory and simulated combat; do not create independent conflicting writers.

Snapshots/deltas identify the room, owner epoch, server tick/time, state/projection version, snapshot sequence, durable revision/checkpoint reference, and applicable input acknowledgments. Deltas identify their exact baseline. Define tick and durable revision separately; do not overload one field with incompatible meanings. Preserve viewer-specific filtering for deltas as well as full snapshots, including visibility removals.

Client interpolation smooths authorized snapshots. Optional client prediction may replay unacknowledged local controls after reconciling with authoritative state; it cannot grant inventory, reveal hidden entities, or decide outcomes. Bound prediction history and extrapolation. Reject obsolete epochs/baselines and resynchronize when history is missing or incompatible.

## Ownership, overload, and recovery

Use one active authoritative writer per room. A verified single-instance arrangement can suffice within its declared availability limits; failover or multiple instances require ownership arbitration. A lease alone is insufficient if an expired owner can still write: use a monotonically increasing fencing token/owner epoch enforced at persistence and delivery boundaries. Validate ownership before durable effects and stop stale execution. A process-local lock is not a cross-instance guarantee.

Authenticate subscriptions and inputs, enforce membership revocation, and bound per-player inbound and outbound work. Coalesce superseded replaceable snapshots; never silently drop discrete command results or emit a delta whose baseline was discarded. Disconnect slow clients with a recovery path when necessary. Record privacy-safe tick lag, queue pressure, dropped/coalesced updates, reconnects, ownership changes, and checkpoint age without logging private payloads.

Define the recovery contract before claiming persistence:

1. Checkpoint simulation state, tick, rules/content/schema versions, deterministic RNG state when used, input high-water marks, and durable command/event references consistently.
2. State the maximum acceptable lost simulation progress and recovery time. Applied input acknowledgment is not a durability promise. Critical rewards, purchases, and terminal outcomes need durable atomic receipts before a durable success acknowledgment.
3. On failure, fence the old owner, load a compatible checkpoint, and replay only a retained authoritative input/event log when exact replay is supported. If replay is unavailable, explicitly roll back to the checkpoint within the approved loss bound or pause for recovery; never invent missing history.
4. Start a new recovery/input epoch and send a fresh authorized snapshot. Discard or explicitly revalidate old pending inputs. Durable command retries use preserved receipts and must not duplicate rewards. If acknowledged durable effects cannot be reconciled with the checkpoint, stop rather than overwrite them.

Reconnect uses authenticated resume and bounded history or a snapshot, with backoff on failures and no recurring state polling. Heartbeats and reconnect attempts are connection maintenance, not a substitute polling loop. Neither D1 checkpoints nor a pub/sub channel alone establish continuous execution reliability.

## Portable behavior and delivery scope

Record normalized fixtures for input order, application ticks, duplicate rejection, snapshot baselines, prediction correction, clock stalls, owner changes, and checkpoint replay. Preserve time-step, arithmetic, RNG, and collision/rule behavior across TypeScript and C#; document precision tolerances only where they cannot change outcomes. See [aspnet-portability.md](aspnet-portability.md).

This reference is design guidance, not an included simulation engine. The foundation template remains a discrete-command starting point. New wire envelopes, runtime adapters, deployment, paid infrastructure, and live testing belong to a separately scoped and approved target-game implementation. Validate with [validation-scenarios.md](validation-scenarios.md) and report actual evidence, not assumed runtime capacity.
