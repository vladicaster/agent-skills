---
name: bootstrap-multiplayer-game-server
description: Design, scaffold, or migrate a production-minded server-authoritative foundation for session-based multiplayer games. Use for strategy, mystery, cooperative, simulation, or social-deduction concepts that need durable multiplayer state without prematurely building a full MMO; do not use for ordinary single-player games or generic networking questions.
---

# Bootstrap Multiplayer Game Server

Turn a game concept or existing prototype into the smallest credible multiplayer foundation. Preserve this invariant in every mode:

> Models generate bounded, validated game content; deterministic server code owns gameplay truth and state transitions.

Model output must never directly authorize a player, advance a clock, accept a command, mutate canonical state, expose private state, or decide a win or loss.

## Select the mode

- **Design:** Produce architecture, domain and command contracts, persistence, risks, tests, and implementation phases. Remain read-only unless the user separately requests implementation.
- **Prototype:** Scaffold a Sites-compatible React/TypeScript multiplayer foundation after approval.
- **Migration:** Translate an existing prototype into ASP.NET Core concepts while preserving observable game behavior and contract fixtures.

If the request is ambiguous, prefer Design. Do not interpret “multiplayer” as authorization to design a full MMO, microservice estate, or globally distributed system.

## Phase 1: Discover and propose

1. Confirm the mode, game concept, session shape, minimum and maximum players, solo behavior, hidden-information rules, host powers, time model, AI-generated content, persistence expectations, and repository status.
2. For repository-backed work, verify access and read all applicable instructions before proposing changes. Inspect the existing state model, server boundary, authentication, persistence, tests, deployment constraints, and generated-content flow.
3. Read [architecture.md](references/architecture.md) and [game-state-contract.md](references/game-state-contract.md). Read [ai-generation-pipeline.md](references/ai-generation-pipeline.md) when models generate content. Read [security-and-concurrency.md](references/security-and-concurrency.md) for any implementation or migration.
4. Use [sites-stack.md](references/sites-stack.md) for a Sites prototype. Use [aspnet-portability.md](references/aspnet-portability.md) for Migration or a mature C# design.
5. Read [validation-scenarios.md](references/validation-scenarios.md) and select the scenarios applicable to the concept.
6. Propose:
   - system boundary and trust model
   - domain entities, stable identifiers, schema versions, commands, projections, and clocks
   - persistence and recovery plan
   - AI pipeline, checkpoints, validation, budgets, and fallbacks when applicable
   - solo-safe rule adaptations
   - realtime connection, reconnect, and resynchronization contract
   - security, concurrency, leak-prevention, and compatibility tests
   - exact files and implementation phases
   - assumptions, risks, deferred scale triggers, and validation plan
7. For Prototype or Migration, stop and ask the user to **approve**, **revise**, or **cancel** before writing repository files. Design may return its read-only artifacts directly.

## Phase 2: Apply after approval

1. Reconfirm the approved repository, branch, files, behavior, and validation scope.
2. Start with the contracts in `assets/foundation-template/`, adapting them to the concept rather than copying unused structures.
3. Put authorization, validation, clocks, revision checks, idempotency, projections, and transitions behind the server boundary.
4. Persist enough canonical state, accepted commands/events, generation checkpoints, and audit data to recover or explain a session. Do not claim event sourcing unless events can actually rebuild state and the project accepts that operational cost.
5. For interactive Sites games, use authenticated WebSockets without periodic polling. Keep initial loading and reconnect recovery behind a snapshot/resynchronization contract, and keep transport separate from commands and projections. Use polling only when the user explicitly selects it for a slower turn-based experience.
6. Make solo behavior explicit for every rule involving quorum, voting, corroboration, role diversity, trading, or host intervention.
7. Validate applicable scenarios and review the diff for private-state leaks, client authority, nondeterministic transitions, unbounded model work, destructive migrations, secrets, and unrelated infrastructure.
   Run `scripts/validate_foundation.py` when the included template or its derived contracts are changed.
8. Report files changed, contract decisions, validation results, manual checks, remaining risks, and scale triggers.

## Approval and execution boundaries

Approval to scaffold or migrate authorizes only the named repository files. Obtain separate authorization before publishing, deploying, provisioning paid services, spending model budget, creating accounts or repositories, changing production data, running destructive migrations, or weakening security controls. Never treat silence as approval.

If access, credentials, a required product decision, or a safe migration path is missing, return **Blocked** with the exact next action. Do not request pasted secrets.

## Default stack profile

Use these as defaults only when user constraints and repository evidence do not indicate otherwise:

| Stage | Default |
| --- | --- |
| Sites prototype | React/TypeScript, Sites server code, WebSockets, D1, R2, ChatGPT authentication |
| Mature implementation | ASP.NET Core/C#, SignalR, PostgreSQL or Azure SQL, Blob Storage, OpenAI API, OIDC authentication |

Start with a modular monolith. Prefer WebSockets for interactive multiplayer in Sites and keep polling optional for slower turn-based games. Add caching, queues, sharding, or service decomposition only for a stated need and with an operational tradeoff.

## Completion criteria

Work is complete only when canonical state and projections are separated, every mutation is a server-validated command, stale and duplicate commands have defined results, clocks are server-owned, private state is viewer-scoped, persistence can recover an interrupted session, AI work is bounded and checkpointed, solo rules cannot deadlock, contract versions can evolve, and applicable validation is reported honestly as **passed**, **failed**, **blocked**, **manual**, or **not run**.
