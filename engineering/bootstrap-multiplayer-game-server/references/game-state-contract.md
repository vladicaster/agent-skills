# Game-state contract

The contract is the portability boundary. TypeScript and C# implementations must agree on serialized behavior, not class layout.

## Canonical envelope

Every persisted session state should include:

- stable `sessionId` and game-definition identifier
- `schemaVersion` for serialized state
- monotonically increasing `revision`
- lifecycle status
- server-owned `createdAt`, `updatedAt`, and relevant deadlines
- deterministic game payload
- generation/content version references

Use opaque stable identifiers. Do not derive authority from display names, array positions, connection IDs, or client-provided role claims.

## Command envelope

Every discrete mutating command should carry:

- `commandId` or idempotency key
- command type and version
- session identifier
- authenticated actor identity supplied by the server boundary
- `expectedRevision`
- client correlation identifier when useful
- command payload

Processing order:

1. Authenticate the subject.
2. Load membership and canonical session state.
3. Authorize the command type and target resources.
4. Return the stored result for a completed idempotency key.
5. Compare the expected and current revisions.
6. Validate deterministic game preconditions using the server clock.
7. Apply one atomic transition.
8. Persist state, accepted events/audit, and the command receipt together.
9. Return a viewer-scoped projection and the new revision.

Define stable error categories such as `unauthenticated`, `forbidden`, `not_member`, `invalid_command`, `stale_revision`, `duplicate_in_progress`, `phase_closed`, `budget_exhausted`, and `session_unavailable`. Do not expose private state in error details.

Continuous controls use the separate sequenced-input contract in [realtime-simulation.md](realtime-simulation.md), not a global expected revision per movement sample. Server-owned time steps are also authoritative transitions, not client commands. Preserve this discrete command contract and define how the room owner orders both paths. Distinguish simulation tick/snapshot sequence from durable revision; the included template implements only the discrete-command starting point.

## State and event evolution

- Never reinterpret an existing `schemaVersion` in place.
- Prefer additive changes and tolerant readers.
- Upcast old snapshots/events through explicit, tested steps.
- Keep a recorded fixture from each supported version.
- Reject a version newer than the server understands with a safe recoverable error.
- Separate serialized wire names from language-specific enum or property naming.
- Version commands, canonical state, events, generated content, and projections independently so one contract can evolve without forcing unrelated migrations.
- Specify UTC timestamp format, integer ranges, decimal handling, nullability, ordering, and unknown-field behavior.

Existing live sessions must either migrate deterministically, continue on a compatible ruleset, or enter an explicit recoverable state. Never silently regenerate their campaign.

## Projections

Build responses from canonical state through a projector with an explicit viewer context:

| Projection | May contain |
| --- | --- |
| Public | Join-safe metadata and intentionally public progress |
| Member | Shared game state visible to all session members |
| Player-private | That player’s hand, role, clues, inventory, or objectives |
| Host | Moderation controls, never other players’ secrets unless rules explicitly require it |
| Administrative | Operational data under separately authorized access |

Prefer allowlists. Test serialized output for forbidden paths and values, including nested debug fields and error payloads.

## Portability fixtures

Maintain language-neutral JSON fixtures for commands, accepted results, stale revisions, projections for different viewers, old state versions, and time-bound transitions. A migration passes when both implementations produce equivalent normalized outcomes for those fixtures.
