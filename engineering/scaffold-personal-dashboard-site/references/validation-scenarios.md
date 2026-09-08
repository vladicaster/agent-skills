# Validation scenarios

Select the scenarios that match the dashboard. Report each as **passed**, **failed**, **blocked**, **manual**, or **not run**. Structural checks do not prove that a live provider, authentication flow, or deployed Site works.

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
- Request publication with a clear target and confirm the Sites hosting workflow is used.
- Confirm sample or private data is not exposed in the published build.

## Forward-test prompts

Use realistic prompts such as:

1. “Create a private morning dashboard with focus items, bookmarks, and notes. I do not need any connected accounts yet.”
2. “Create a daily brief with my calendar and GitHub activity, and let me choose which calendar and repository it uses.”
3. “Add an RSS module to this dashboard. If the feed is down, the other cards must still work.”
4. “Build the dashboard and show me a preview, but do not publish it yet.”

Forward testing should use temporary or non-production data. Do not authorize live mutations, paid services, or publication merely to exercise the skill.
