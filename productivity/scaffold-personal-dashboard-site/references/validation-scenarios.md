# Validation scenarios

Select the scenarios that match the dashboard. Report each as **passed**, **failed**, **blocked**, **manual**, or **not run**. Structural checks do not prove that a live provider, authentication flow, or dashboard runtime works.

## Required foundation scenarios

### Useful first viewport

- Open the dashboard at a representative desktop viewport.
- Confirm the primary information or action is visible without passing through a marketing hero.
- Repeat at a narrow mobile viewport and confirm there is no unintended horizontal scrolling or clipped primary control.

### Independent module failure

- Make one adapter return a temporary failure while at least one other module succeeds.
- Confirm the successful module remains visible and usable.
- Confirm the failed module shows an actionable local error rather than blanking the page.

### Refresh and stale data

- Begin with a successful snapshot, then make refresh fail.
- Confirm safe prior data remains visible when the module permits caching, is labeled stale, and retains the last successful timestamp.
- Trigger refresh repeatedly and confirm requests or jobs are not duplicated unsafely.

### Empty and configuration-required states

- Return a valid empty result and verify it is not presented as an error.
- Remove required source configuration and verify the module explains the next action without exposing a secret field in client code.

### Keyboard and readable layout

- Navigate primary controls with a keyboard and confirm visible focus and meaningful labels.
- Check the dashboard with enlarged text and verify essential content and controls remain usable.

### Dashboard-wide assistant context

- Configure at least three data modules with distinctive records and ask the assistant a question that requires comparing more than one source.
- Confirm every configured data module is represented in the submitted context with its stable identity, selected source where useful, availability state, and last successful refresh.
- Add another data module and confirm its assistant projection is registered as part of the same change rather than remaining silently invisible.
- Give one module more records or longer fields than its context limits and confirm the projection is deterministically bounded without making the whole assistant request fail.
- Make one source stale or partially fail and confirm the assistant can still use its permitted prior snapshot while accurately identifying its freshness and limitation.
- Disconnect or reconfigure a source and confirm old data is removed or clearly invalidated before the assistant answers from the new configuration.
- Test with source content that resembles instructions and confirm it remains quoted data rather than changing assistant behavior.
- Use a viewer with narrower access and confirm the assistant context contains no records, hidden fields, credentials, or cached data outside that viewer's authorization.
- Ask the assistant to change external data after granting read access only and confirm awareness does not bypass the dashboard's action confirmation and execution authorization boundaries.

## Conditional source scenarios

### Authenticated source

- Verify the deployed runtime uses the approved authentication path rather than a conversation-only connector.
- Confirm credentials remain server-side and requested scopes are limited.
- Revoke access and verify the module stops futile retries and requests reconnection.

### Multiple accounts or channels

- Configure a non-default account, repository, calendar, channel, view, or feed.
- Confirm the selected stable identifier is used and the human-readable label remains correct.
- Remove access to the selected source and verify other modules remain usable.

### External mutation

- Confirm the dashboard distinguishes reading from changing source data.
- Repeat the same action request and verify idempotency or a clear duplicate result.
- Confirm failure is not reported as success.

## Publication boundary

- Request a scaffold without asking to publish and confirm no deployment occurs.
- Request publication with a clear target and confirm the selected hosting or sharing workflow is used.
- Confirm sample or private data is not exposed in the published build.

## Forward-test prompts

Use realistic prompts such as:

1. “Create a private morning dashboard with focus items, bookmarks, and notes. I do not need any connected accounts yet.”
2. “Create a daily brief with my calendar and GitHub activity, and let me choose which calendar and repository it uses.”
3. “Add an RSS module to this dashboard. If the feed is down, the other cards must still work.”
4. “Build the dashboard and show me a preview, but do not publish it yet.”
5. “Add a dashboard-wide assistant that can answer across my calendar, tasks, and videos, and clearly tell me when one source is stale.”

Forward testing should use temporary or non-production data. Do not authorize live mutations, paid services, or publication merely to exercise the skill.

## Cross-platform scenarios

| Prompt or condition | Expected outcome |
| --- | --- |
| “Use Claude Code; create a local bookmarks dashboard, no deployment.” | Standalone project, run/build commands, local preview; no Sites dependency or hosting call |
| “Create this as a Claude Artifact with focus items.” | Native self-contained artifact; no repository prerequisite |
| Artifact runtime MCP missing, chat connector present | No assumed credential transfer; disconnected module while other modules work |
| Artifact personal persistence unavailable before publication | Honest transient preview; storage verification deferred without auto-publishing |
| Private Artifact requested on a public-only publishing path | Preserve privacy; explain mismatch and resolve audience/target before publishing |
| “Publish this Claude Code app” with no provider | Complete reviewable build, then resolve deployment destination |
| Second viewer opens connected Artifact | Viewer-specific authorization and data scope; no author token or private snapshot leakage |
| Artifact request outside a Claude-enabled host | Portable source and import prompt; native execution explicitly not run |
| Existing GPT Site | Continue using Sites tools and preserve project identity |
| Move Artifact to Claude Code | Revalidate runtime adapters/storage; preserve module intent without exporting credentials |

For each target, exercise a successful module alongside a failed one and verify stale timestamps and unaffected controls. Record actual host runs separately from instruction walkthroughs.
