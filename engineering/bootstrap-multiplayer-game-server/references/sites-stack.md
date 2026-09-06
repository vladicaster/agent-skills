# Sites prototype stack

Use this adapter only for Prototype mode or when the user explicitly chooses Sites.

## Recommended shape

- React/TypeScript renders viewer-scoped projections and submits commands over the selected authenticated transport.
- Sites server code authenticates the caller, resolves membership, validates commands, owns clocks, applies transitions, and publishes projections through a verified delivery path. Do not assume it can host sustained sockets merely because a handshake succeeds.
- D1 stores relational session state, revisions, command receipts, events/audit records, and generation checkpoints.
- R2 stores large immutable generated artifacts or media when justified.
- ChatGPT authentication supplies the authenticated subject; game membership and host permissions remain application data.

Do not move authoritative rules into React merely for responsiveness. Optional client prediction is speculative presentation, reconciled with authoritative revisions or simulation snapshots; it never commits gameplay outcomes.

## Real-time simulation profile

For continuous simulation, use [realtime-simulation.md](realtime-simulation.md) to choose Sites-native lightweight rooms or a Sites frontend connected to an approved external authoritative simulator. Verify the actual Sites runtime's WebSocket handling, execution lifetime, timer behavior, room routing/ownership, recovery, and multi-instance delivery before claiming native simulation reliability. WebSocket support alone does not establish a durable background game loop, even for two players.

In the external profile, Sites renders the game and may retain session/lobby APIs; the external server owns simulation truth. Define the trusted authentication handoff, audience/session scope, token expiry, revocation, and WSS origin policy. Do not assume an external server can directly trust browser-supplied ChatGPT identity or access D1. Give each state category one writer and use an approved authenticated service boundary where storage remains in Sites. Ably is optional delivery infrastructure, not the simulator.

## WebSocket-first protocol

For all interactive games, verify sustained idle/active delivery, token renewal, reconnect, and instance changes in the deployed environment. Classify short-lived connections as a failed deployment test until logs establish a cause; do not assume every Sites configuration has the same limitation.

Use authenticated `wss://` delivery at a verified native endpoint or an explicitly selected external provider. For Ably, follow [ably-setup.md](ably-setup.md): browser connections terminate at Ably; Sites accepts HTTPS commands and publishes via REST after durable commit. Ably is optional, not a gameplay authority. Adapt message names to host conventions while preserving semantics:

- `connection.resume` — identify the session and last known revision after the server authenticates the connection
- `connection.ready` — return connection metadata and the current authorized revision
- `command.submit` — carry the versioned command envelope
- `command.result` — return the stable accepted or rejected result
- `session.changed` — push an authorized projection or signal that a resynchronization snapshot is required
- `session.snapshot` — return a complete viewer-scoped projection for initial load or recovery
- `generation.status` — push stage, checkpoint, usage, and terminal-state changes to authorized viewers

Do not use periodic polling or silently enable SDK polling fallbacks. An HTTP surface may create sessions, accept invitations, issue/renew tokens, accept player commands, or return initial/recovery snapshots; it is not repeatedly called to discover changes. In the Ably profile, command submission/results use HTTPS, and authorized live events use Ably channels. Slower turn-based games may select polling explicitly when persistent connections add no useful experience.

## Connection and recovery rules

- A connection ID is never identity, membership, or authority.
- Authorize the session and viewer for every subscription and command.
- Tag server messages with session ID, revision, projection version, message ID, and server time.
- On reconnect, send the last applied revision and deduplicate message/command IDs.
- If missed updates are unavailable or incompatible, send a fresh authorized snapshot.
- Bound outbound queues and define slow-client behavior; never let one connection block canonical transitions.
- Verify routing and delivery across the actual deployment before relying on in-memory connection lists. Use a shared fan-out mechanism only when needed and approved; it does not replace authoritative room ownership or persistence.

## D1 practices

- Use foreign keys and uniqueness constraints for membership and idempotency.
- Apply revision updates conditionally inside a transaction.
- Store timestamps as normalized UTC strings or integer epochs consistently.
- Keep migrations additive where possible and record state schema separately from database migration version.
- Verify the actual D1 transaction and migration capabilities available in the target Sites environment before relying on them.
- For continuous simulation, separate live owner state from durable checkpoints and receipts. Declare recovery loss bounds and critical-action durability; do not assume every tick must be written to D1. Follow the ownership/fencing and recovery contract in [realtime-simulation.md](realtime-simulation.md).

## SignalR portability

The command/projection contract is the portability seam, independent of whether commands travel over HTTPS or WebSockets. A mature SignalR implementation may use hub methods and authorized groups, but it preserves command envelopes, revisions, idempotency, viewer-scoped projections, reconnect behavior, and server authority.

## Prototype boundaries

The prototype should prove contracts, recovery, privacy, and playability. It need not prove massive concurrency, global distribution, service decomposition, or production operations. Record the measurements and requirements that would trigger migration or infrastructure changes.
