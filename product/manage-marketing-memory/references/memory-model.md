# Memory model

Keep the canonical record in its owning area and link to it elsewhere. Start with the small Markdown registries supplied; split into one file per record when navigation benefits. Preserve IDs when moving records and repair links in the same change.

| Area | Owns | ID prefix |
| --- | --- | --- |
| customer-truth | Observations, quotations, objections, audience evidence | CUST |
| content-engine | Voice, hooks, angles and content versions | CONT |
| outbound-engine | Audience-specific playbooks and sequence drafts | OUT |
| creative-testing | Experiment plans and variants | EXP |
| agents | Scoped roles and human corrections | CORR for corrections |
| results | Measurements and derived learning | RES |

Use unused sequential identifiers such as `CUST-0001`; scan the current branch and reconcile collisions after concurrent edits. Link records with relative Markdown links and an explicit ID. Do not rely on an inaccessible chat as the only memory of a decision: capture an authorized concise summary plus its locator.

## Common fields

For each record capture:

- **ID, title, business/audience/channel scope.** Scope limits where the record applies.
- **Statement/artifact.** Exact quotation, paraphrase or asset text, clearly labeled.
- **Evidence type:** observed, user-provided, inferred, or hypothesis. User-provided claims are attributed, not automatically verified.
- **Sources:** locator, relevant excerpt or permitted summary, observed date, captured date and access restriction. Use ISO dates; unknown dates stay unknown.
- **Approval:** unreviewed, approved, rejected or withdrawn; approver, date, decision locator and exact approved version/scope. Changes outside that scope produce an unreviewed revision.
- **Lifecycle:** active, disputed, superseded or archived, independently of approval. Preserve prior statement/decision and link `supersedes`/`superseded-by` IDs or historical commit.
- **Related records, owner if known, last reviewed date, review trigger and open questions.** Do not invent an owner or review date.

These fields may be compact prose instead of YAML. Missing information is explicitly unknown, not a request to guess. A draft PR is proposed memory; a merge records the change but does not itself confer marketing approval.

## Experiments and results

An experiment records hypothesis, audience/channel, exact variant text or commit/asset version, baseline/control, primary metric and formula, planned window, sample/denominator, decision rule, status and related content IDs. Set the rule before execution; label a retrospective rule as exploratory. Record execution authorization separately from a draft plan.

A result records EXP ID, actual window, metric numerator/denominator and units, measurement source, exclusions, missing data, baseline comparison, limitations and outcome (supported, unsupported or inconclusive). Avoid percentages without denominators and causal claims from uncontrolled comparisons. A supported result applies only within its tested scope; it does not automatically authorize publication or spend.

A learning links evidence to a proposed or approved change and its affected CONT/OUT/CUST records. Negative and inconclusive results remain discoverable. If the window or audience differs, do not rank variants as if directly comparable.

## Corrections

A correction records the human's original instruction or authorized summary, observed agent behavior, corrected behavior, rationale, effective scope, date, source and affected records. Distinguish direct human correction from an agent's proposed improvement. Preserve superseded guidance and expose conflicts requiring a decision. Corrections cannot grant tools, publishing permission or authority over unrelated repositories.
