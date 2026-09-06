# ASP.NET portability

Migration preserves behavior at the command/projection boundary. It is not a line-by-line TypeScript rewrite.

## Concept mapping

| Portable concept | Sites prototype | Mature C# implementation |
| --- | --- | --- |
| HTTP application | Sites server handlers | ASP.NET Core endpoints/controllers |
| Deterministic domain | TypeScript functions/modules | C# domain/application services |
| Authentication | ChatGPT-authenticated subject | OIDC claims principal |
| Membership/permissions | D1-backed application records | SQL-backed application records/policies |
| Optimistic concurrency | Conditional D1 update | Row version/revision checked transaction |
| Initial/recovery state | HTTP or WebSocket snapshot | HTTP or SignalR resynchronization |
| Realtime session | Authenticated Sites WebSocket | SignalR hub with authorized groups |
| Continuous simulation, when selected | Verified room owner and time-step runtime, or external simulator | Dedicated room execution service with bounded scheduling; SignalR remains delivery only |
| Continuous input/recovery | Sequenced controls, tick snapshots, fenced checkpoints | Equivalent input ordering, owner epochs, checkpoint/replay and durability semantics |
| Relational storage | D1 | PostgreSQL or Azure SQL |
| Large artifacts | R2 | Blob Storage |
| Generated content | Bounded model call behind server code | OpenAI API behind application service |
| Background generation | Durable job/checkpoints available to Sites | Hosted service or approved durable worker |

OIDC identity does not replace session membership. SignalR group membership does not replace command authorization. Blob URLs do not replace artifact authorization.

## External simulator with Sites frontend

This is an optional prototype profile, not a requirement to migrate the entire application. Keep Sites rendering/UI while an approved ASP.NET Core service owns simulation. Verify authentication handoff and external WSS connectivity in the target environment. Hub connections feed the room owner; do not start competing game loops per connection or assume a hosted service runs exactly once across replicas. Define room routing, fencing, load limits, shutdown checkpoints, and recovery using [realtime-simulation.md](realtime-simulation.md).

Before migrating continuous behavior, freeze fixtures covering ticks, input sequences/epochs, late/duplicate controls, RNG state, numeric precision, snapshots/delta baselines, durable receipts, and checkpoint recovery. Compare authoritative outcomes across TypeScript and C#; rendering FPS and transport throughput are separate measurements. A SignalR adapter or managed backplane alone does not prove simulation capacity.

## Migration sequence

1. Freeze and document the wire contract and time/serialization conventions.
2. Capture cross-player projection, command-result, old-version, and clock-boundary fixtures.
3. Implement C# readers and deterministic transitions against the same fixtures.
4. Implement SQL persistence with equivalent uniqueness, revision, and atomicity guarantees.
5. Run both implementations against normalized contract tests.
6. Shadow or replay sanitized recorded commands when authorized.
7. Cut over only after recovery, observability, rollback, and data migration are approved.
8. Replace the Sites WebSocket adapter with SignalR after command parity; do not combine transport migration with gameplay-rule changes.

## Compatibility rules

- Preserve stable IDs, command type/version names, error categories, revision semantics, and projection visibility.
- Normalize JSON field naming, enum strings, decimals, timestamps, nulls, unknown fields, and collection ordering.
- Inject clocks and ID generators in both implementations.
- Keep old-version upcasters until retained sessions and events no longer require them.
- Compare semantic outcomes rather than language-specific exception text or property order.

Document intentional behavior changes separately and obtain approval; do not hide them inside “migration.”
