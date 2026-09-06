# AI generation pipeline

Generated content is untrusted input. The pipeline may create narrative, maps, characters, objectives, encounters, clue graphs, or simulation parameters, but deterministic code decides whether that content is safe and playable.

## Staged pipeline

Use explicit stages appropriate to the game, for example:

1. Normalize the approved generation brief.
2. Generate a compact structural outline.
3. Validate structure, identifiers, counts, and references.
4. Generate bounded detail by section.
5. Validate safety, semantic consistency, rule compatibility, and solvability.
6. Assemble and freeze a versioned campaign artifact.
7. Initialize canonical game state deterministically from that artifact.

Persist each completed checkpoint with the prompt/template version, model identifier, schema version, input hash, output hash, token use, estimated cost, attempt number, timestamps, and validation result. Resumption must start from the latest compatible checkpoint rather than repeating successful stages.

## Strict outputs

- Use a strict structured-output schema with bounded strings and arrays.
- Reject unknown identifiers, broken references, duplicate stable IDs, impossible counts, and unsupported rule types.
- Separate syntactic schema validation from semantic and solvability validation.
- Treat model explanations as diagnostic text, never executable rules.
- Never execute generated code, queries, HTML, URLs, or tool instructions.

## Retry and repair policy

For every stage define a timeout, maximum attempts, repair limit, backoff, and terminal outcome. Repairs receive only the necessary validation failures and must return the complete required stage output. Do not allow recursive “try until it works” behavior.

Recommended terminal outcomes:

- Use validated deterministic fallback content when the game can remain meaningful.
- Preserve checkpoints and return a resumable failure when fallback would misrepresent the requested experience.
- Cancel safely when authorization, budget, or policy prevents continuation.

Never leave a session indefinitely in a generic `Generating` state. Store a specific stage, heartbeat, lease/owner, next action, and failure category. Expired work must be reclaimable without duplicating completed stages.

## Budgets

Set limits before execution:

- maximum input and output tokens per stage
- maximum attempts and repairs
- maximum estimated and actual cost per job/session/account
- maximum wall-clock duration
- maximum artifact size and retention

Reserve enough budget for validation and one bounded repair rather than spending the entire allowance on the first generation. Stop before the next call if its worst-case cost would exceed the remaining budget. Report estimates separately from provider-confirmed usage.

## Solvability

Define deterministic validators for the game’s structure. Examples include reachability of required locations, a path from evidence to conclusions, sufficient resources to complete objectives, legal role distributions, and at least one valid terminal path. Property-based or exhaustive checks are preferable when the state space is small.

Model self-critique may supplement but never replace deterministic validation. When no general proof is possible, state the limitation and add simulation plus manual review.
