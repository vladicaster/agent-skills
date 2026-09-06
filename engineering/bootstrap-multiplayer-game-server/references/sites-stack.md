# Sites prototype stack

Use this adapter only for Prototype mode or when the user explicitly chooses Sites.

## Recommended shape

- React/TypeScript renders viewer-scoped projections and submits commands.
- Sites server code authenticates the caller, resolves membership, validates commands, owns clocks, applies transitions, and returns projections.
- D1 stores relational session state, revisions, command receipts, events/audit records, and generation checkpoints.
- R2 stores large immutable generated artifacts or media when justified.
- ChatGPT authentication supplies the authenticated subject; game membership and host permissions remain application data.

Do not move authoritative rules into React merely for responsiveness. Optional client prediction must be cosmetic and reconciled with the returned revision.

## Initial endpoints

Adapt names to host conventions while preserving semantics:

- `POST /sessions` — create a session and host membership
- `POST /sessions/{id}/memberships` — join or accept an invitation
- `GET /sessions/{id}/view?afterRevision=n` — return the viewer projection or unchanged status
- `POST /sessions/{id}/commands` — submit a versioned command envelope
- `POST /sessions/{id}/generation-jobs` — start an authorized bounded job
- `GET /generation-jobs/{id}` — return stage, checkpoints, usage, and terminal state

Long polling is optional. Ordinary revision polling is acceptable first when intervals use backoff/jitter, pause in background tabs, and do not query heavy joined state unnecessarily.

## D1 practices

- Use foreign keys and uniqueness constraints for membership and idempotency.
- Apply revision updates conditionally inside a transaction.
- Store timestamps as normalized UTC strings or integer epochs consistently.
- Keep migrations additive where possible and record state schema separately from database migration version.
- Verify the actual D1 transaction and migration capabilities available in the target Sites environment before relying on them.

## Realtime seam

The server response remains the authoritative projection. Later SignalR/WebSocket messages should normally carry `sessionId`, `newRevision`, and a reason to refresh, or the same already-authorized projection shape. A connection ID never becomes player identity.

## Prototype boundaries

The prototype should prove contracts, recovery, privacy, and playability. It need not prove massive concurrency, global distribution, service decomposition, or production operations. Record the measurements and requirements that would trigger migration or infrastructure changes.
