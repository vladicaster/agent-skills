# Diagram quality checklist

Report each applicable check as **Passed**, **Failed**, **Blocked**, **Manual**, or **Not run**.

## Purpose and scope

- Audience and supported decision are stated.
- System of interest and boundary are explicit.
- Current, target, or mixed state is labeled.
- Diagram title identifies C4 level or supplemental view type.

## Evidence integrity

- Material claims are classified Observed, Inferred, Proposed, or Unknown.
- Important Observed claims cite an inspected source.
- Inferred claims state their basis and do not masquerade as facts.
- Proposed elements are visually or textually distinct from current state.
- Conflicting sources and material unknowns are surfaced.

## C4 consistency

- Elements appear at the appropriate abstraction level.
- Names and responsibilities remain consistent across views.
- Container boundaries reflect runnable or deployable responsibilities.
- Component views stay inside one named container.
- Context relationships reconcile with lower-level views where expanded.

## Relationship quality

- Arrows have a meaningful direction.
- Relationship labels use concise verbs and explain purpose.
- Protocol or mechanism appears only when known and useful.
- Asynchronous, scheduled, or event-driven behavior is not misleadingly shown as a synchronous call.
- Sensitive data or trust-boundary crossings are visible when relevant.

## Readability

- The diagram has a clear reading order and avoids unnecessary crossings.
- Labels are readable at the intended size.
- Color is not the only carrier of meaning.
- Legends explain status or evidence encodings.
- The view contains only detail needed by its audience.
- Large models are divided into scoped views rather than one dense diagram.

## Artifact verification

- Source syntax parses with an available compatible renderer or validator.
- The rendered result is inspected when rendering is available.
- Relative links and referenced files resolve.
- No credentials, private data, or proprietary evidence are exposed in a reusable or public artifact.
- Generated output contains actual line breaks rather than visible escaped newline sequences.

## Review result

Summarize:

| Check | Status | Evidence or limitation |
| --- | --- | --- |
| Syntax | Passed | Compatible parser completed successfully |
| Visual layout | Manual | Renderer unavailable; inspect in destination |
| Evidence traceability | Failed | Two current-state relationships lack sources |

Never report the overall model as fully validated when material checks failed, are blocked, or require manual review.
