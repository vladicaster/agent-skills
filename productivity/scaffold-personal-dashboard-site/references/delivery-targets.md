# Delivery targets

Select a target independently of Blueprint, Scaffold, or Extend mode. Shared module contracts survive a target change; credentials, persistence, hosting, and execution APIs do not automatically transfer.

## GPT Sites

Use the current installed Sites building and hosting skills. Preserve the existing project identity and configuration. Pass through the user's publishing intent; do not deploy a preview-only request. Missing Sites tooling blocks native execution, not an otherwise useful portable blueprint.

## Claude Code

1. Inspect CLAUDE.md, AGENTS.md, framework, package manager, and existing commands. Preserve an existing app. In an empty workspace, use a small React/TypeScript app when suitable; choose a server-capable framework only when selected sources require it.
2. Implement the shared shell, typed module registry, source adapters, and local or verified live modules. Keep provider-specific code outside views.
3. For authenticated sources, use an authorized backend or verified runtime service. Claude Code's own MCP tools and terminal credentials are development capabilities, not credentials to bundle into the dashboard.
4. Document install, development, build, and validation commands; provide a safe environment-variable example containing names and empty values only.
5. Run the app's build and selected failure/configuration scenarios. Start a local preview when available. A build alone does not prove deployed authentication.
6. Deliver source plus a short DASHBOARD.md with module configuration, data/storage scope, extension instructions, and remaining setup.
7. If deployment is requested, resolve provider, project, audience, runtime support, and credentials. Use the provider's current supported workflow. A static host cannot run secret-bearing server routes; select a compatible backend or report that module blocked.
8. Verify deployment success before reporting a URL. Do not create a hosting account or choose public visibility merely because the user requested Claude Code.

Claude Code's native session artifacts are a separate optional output. Do not substitute them for the requested standalone application or assume their sharing rules match Claude chat Artifacts.

## Claude Artifacts in chat

1. Verify the native Artifact creation surface and current supported HTML/React format. Produce a self-contained interactive dashboard that can be edited in the Artifact pane. Do not assume a Node server, filesystem, or arbitrary browser networking.
2. Begin with the requested modules. Local focus items, bookmarks, and supplied data can make a useful first version. Label imported snapshots and sample data; do not claim automatic live refresh.
3. For live modules, verify runtime MCP availability and user authorization separately from chat tool access. Use documented host APIs, not invented bridge calls. If unavailable, keep the module disconnected and finish the usable remainder.
4. Choose transient, personal, or shared storage explicitly. Prefer personal data scope for personal dashboards. Verify persistence in the actual host before claiming it works.
5. Preview controls, module failures, configuration, and data scope. If persistence cannot run before publication, test with a clearly labeled in-memory substitute and report durable storage as unverified. Do not publish solely to make a test pass.
6. For sharing, determine the actual audience and plan behavior first. Explain a public/private mismatch and obtain a compatible target rather than exposing a private dashboard. Remove embedded private snapshots and credentials from shareable source.
7. Perform publication only with the user's authorization and available host controls. When the final action is user-only, provide the precise native step and report publication pending.
8. Hand off editable source, configuration guidance, persistence limitations, and publication status. If running outside Claude, provide an import prompt and source; mark native preview, MCP, storage, and publishing not run.

## Current capability evidence

Verify these documents again when implementing a target; capabilities and plan rules can change.

- [Artifacts capabilities](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them), checked September 8, 2026: supported plans can use runtime MCP with per-user authorization and personal/shared persistence. Persistence requires publication; unpublishing deletes associated stored data. Never assume author connections are inherited by viewers.
- [Artifact publication](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts), checked September 8, 2026: consumer publication is public; Team/Enterprise sharing is organization-scoped. Check current behavior before promising a private link or changing visibility.
- [Claude Code overview](https://code.claude.com/docs/en/overview): repository authoring, commands, and development tools.
- [Claude Code skills](https://code.claude.com/docs/en/skills): current skill loading and invocation guidance.

## Target changes

Map existing module IDs, configuration, and visible behavior first. Revalidate authentication, storage ownership, data export, and deployment. Never copy tokens or silently replace durable data with transient state. A request for both Claude targets produces two delivery paths or artifacts, not an assumption that one runtime executes the other's code.
