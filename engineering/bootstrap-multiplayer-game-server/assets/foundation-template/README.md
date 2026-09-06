# Foundation template

These files are an adaptable contract seed, not a complete game server.

- `domain-contracts.ts` defines stable state, membership, clocks, events, and projection envelopes.
- `commands.ts` defines mutation and result envelopes with revision and idempotency semantics.
- `projections.ts` demonstrates allowlisted viewer-scoped projections.
- `persistence-schema.sql` provides a D1-compatible starting schema for sessions, membership, snapshots, accepted events, command receipts, generation checkpoints, and audit history.
- `contract-fixture.json` seeds cross-language checks for accepted, repeated, stale, and viewer-private behavior.

Before use, define the game-specific payloads and commands, remove unused structures, and add deterministic transition and projection tests. Keep authenticated actor identity out of client-controlled payloads. Execute a command in one transaction: claim/check idempotency, load and authorize membership, compare revision, apply the deterministic transition, conditionally update state, append event/audit data, and store the result receipt.

The SQL is intentionally generic. Review the target host’s current migration, transaction, foreign-key, JSON, and timestamp behavior before applying it. Repository writes and database migrations require approval under the skill workflow.
