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
| Polling | Revision-based HTTP GET | Same HTTP contract |
| Realtime notification | Later WebSocket adapter | SignalR hub notifying authorized groups |
| Relational storage | D1 | PostgreSQL or Azure SQL |
| Large artifacts | R2 | Blob Storage |
| Generated content | Bounded model call behind server code | OpenAI API behind application service |
| Background generation | Durable job/checkpoints available to Sites | Hosted service or approved durable worker |

OIDC identity does not replace session membership. SignalR group membership does not replace command authorization. Blob URLs do not replace artifact authorization.

## Migration sequence

1. Freeze and document the wire contract and time/serialization conventions.
2. Capture cross-player projection, command-result, old-version, and clock-boundary fixtures.
3. Implement C# readers and deterministic transitions against the same fixtures.
4. Implement SQL persistence with equivalent uniqueness, revision, and atomicity guarantees.
5. Run both implementations against normalized contract tests.
6. Shadow or replay sanitized recorded commands when authorized.
7. Cut over only after recovery, observability, rollback, and data migration are approved.
8. Add SignalR as a transport adapter after command parity; do not combine it with gameplay-rule changes.

## Compatibility rules

- Preserve stable IDs, command type/version names, error categories, revision semantics, and projection visibility.
- Normalize JSON field naming, enum strings, decimals, timestamps, nulls, unknown fields, and collection ordering.
- Inject clocks and ID generators in both implementations.
- Keep old-version upcasters until retained sessions and events no longer require them.
- Compare semantic outcomes rather than language-specific exception text or property order.

Document intentional behavior changes separately and obtain approval; do not hide them inside “migration.”
