# Source integrations

Read this reference before implementing any live or authenticated dashboard source.

## Classify the runtime path

| Source class | Evidence required | Typical handling |
| --- | --- | --- |
| Local/static | Data is intentionally bundled or entered locally | Keep examples generic and label sample data |
| Platform storage | The current target runtime supports the required persistence and access pattern | Use the Platform storage guidance and server boundary |
| Public HTTP | The deployed runtime can reach the endpoint and its terms permit the use | Validate response, caching, rate limits, and attribution |
| Authenticated runtime API | A supported server-side credential or OAuth flow exists for the dashboard runtime | Keep secrets server-side and scope permissions narrowly |
| Verified Artifact MCP | Artifact runtime tools, user authorization, and plan/admin access have been verified | Use the host-mediated connection; never export author credentials |
| Blocked | No verified safe runtime path exists | Explain the exact missing capability; do not fake live data |

A connector available to the agent during the conversation is evidence that the agent may be able to read that service for the current task. It is not evidence that generated Site code can reuse the connector, credential, or session.

## Source feasibility record

For each requested source, establish:

- what the module needs to read or change
- the account, tenant, channel, repository, view, feed, or equivalent selection
- authentication method and where credentials live
- server or client execution boundary
- scopes and least required permissions
- refresh trigger and expected freshness
- pagination, rate limits, caching, and cost constraints
- normal empty behavior
- transient, permanent, disconnected, and revoked-access behavior
- privacy classification and who may see the result

If these facts cannot be established, implement only an honest configuration-required state or mark the source **Blocked**.

## Read and mutation separation

Keep source reads distinct from external actions. Loading email does not authorize sending email. Loading tasks does not authorize completing or deleting them. Loading repository data does not authorize creating issues or merging pull requests.

Before an external mutation:

1. resolve the exact target and acting identity,
2. show or describe the proposed effect when material,
3. obtain the authorization required by the relevant connector or workflow,
4. execute once with idempotency where applicable,
5. surface a trustworthy result without inventing success.

## Account and source selection

When a provider supports multiple sources, expose a configuration choice instead of hard-coding the first accessible account. Store stable provider identifiers separately from human-readable labels. Revalidate access when configuration changes, and handle renamed or revoked sources without breaking unrelated modules.

## Failure and stale-data behavior

- **Disconnected:** Explain that connection or runtime configuration is required.
- **Access revoked:** Stop retries and prompt for reconnection.
- **Rate limited:** Preserve safe cached data, show staleness, and honor retry guidance.
- **Temporary dependency failure:** Keep other modules usable and allow a bounded retry.
- **Invalid response:** Reject malformed data at the adapter boundary and avoid rendering it as trusted content.
- **No results:** Show a normal empty state rather than an error.

Never transform an HTML error page, authentication redirect, or provider error into application data. Validate response status and content type before parsing JSON.

## Secrets and observability

Do not log tokens, authorization headers, private payloads, or unnecessary personal content. Log enough structured context to identify the module, source class, attempt, duration, outcome, and safe provider error category. Keep user-facing errors actionable without revealing secrets or internal stack traces.
