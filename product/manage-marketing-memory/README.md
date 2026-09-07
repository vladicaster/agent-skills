# Manage Marketing Memory

Create a durable `growth-os` in GitHub so future marketing work can reuse customer evidence, voice, objections, approved messaging, experiments, results and human corrections. The skill both initializes the structure and maintains it as new information arrives.

## When to use

Use this skill to create a marketing memory, record new customer feedback, preserve a messaging decision, incorporate campaign measurements, retrieve prior learning or reconcile contradictory records. It works across businesses; the installed skill contains only generic methodology and starter assets.

It does not send campaigns, operate an ad account, deploy autonomous agents or replace a full go-to-market strategy workflow. For a one-off copy draft with no persistent memory requirement, a writing workflow is sufficient.

## Modes and inputs

| Mode | Inputs | Output |
| --- | --- | --- |
| Bootstrap | Business scope, destination, repository creation authorization if needed | Six-area memory with navigation and agent guidance |
| Capture/update | Existing memory and authorized new evidence or decisions | Traceable additions and scoped revisions |
| Retrieve | Question and accessible memory | Referenced answer or brief, without writes |
| Reconcile/audit | Existing memory and requested review scope | Prioritized findings and authorized repairs |

Example requests:

- “Use $manage-marketing-memory to create growth-os in this existing repository.”
- “Record these customer objections and link them to the messaging they affect.”
- “Which hooks have supporting results for this audience?”
- “This tone correction applies only to outbound messages; preserve it for future sessions.”
- “Reconcile these experiment results with our approved angles.”

## Workflow

1. Establish the business, memory root and requested mode. Inspect existing repository instructions, content and pending work.
2. Confirm GitHub identity, access, destination visibility, permissions and actual default branch for repository delivery. Resolve only missing material choices.
3. On bootstrap, add missing starter files. On subsequent runs, read the index and affected records first. Preserve populated files and map equivalent existing structures.
4. Record evidence, sources, dates and scope using stable identifiers. Keep human approval separate from whether a claim is supported by measurements.
5. Link customer observations to content, exact content versions to experiments, and measurements to learning. Preserve conflicts, negative results and superseded decisions.
6. Apply human corrections within their stated scope. Update navigation and dependent records together.
7. Review the diff and deliver authorized changes on a feature branch through a draft PR. Report unresolved decisions and the next useful action.

The skill is session-driven. Its `agents/` area stores role guidance and corrections; installing it does not start services or recurring maintenance.

## Memory areas

| Directory | Starting file | What it remembers |
| --- | --- | --- |
| `customer-truth/` | `evidence.md` | Customer language, needs, objections and counterevidence |
| `content-engine/` | `messaging.md` | Voice, hooks, angles, versions and approval decisions |
| `outbound-engine/` | `playbooks.md` | Audiences, qualification rules and message sequences |
| `creative-testing/` | `experiments.md` | Hypotheses, variants, metrics and predeclared decision rules |
| `agents/` | `guidance.md` | Roles, boundaries and scoped human corrections |
| `results/` | `learning.md` | Measurements, limitations and changes informed by results |

The root index links all six areas. Start with small registries; split records into separate files as needed while preserving IDs and repairing links. Unknown facts stay unknown. Starter instructions are not customer evidence or approval records.

## Approval and GitHub boundaries

GitHub is required to deliver a GitHub memory. An existing repository is optional: the user can authorize creation with a specific owner/name and visibility. A read-only review or portable scaffold does not require GitHub. Installing the skill grants no account or repository access.

The skill includes the runtime checks from the shared [repository readiness guide](../../docs/github-repository-readiness.md). It verifies identity, source/destination access, ownership, visibility, permissions, default branch and applicable capabilities. When blocked, it identifies the exact failed operation and next setup action. The leaf skill remains usable when installed alone.

Creation authorization must cover initialization of an empty repository. Existing rules against default-branch writes remain binding. Ongoing edits use feature branches and reviewable PRs; merges require separate authorization. Existing session approval is reused within its scope.

Permission to store a draft does not approve the draft's claims. Content approval does not authorize sending, publication or spending. A merged record is not proof that a hook worked. The skill requires linked measurement evidence before calling something a supported winner, and retains the tested audience/channel/window.

Customer data must fit destination visibility. The skill source stays generic; private business memory belongs in the selected destination. Raw personal data and private transcripts are not seeded into public repositories.

## Relationship to other skills

[Develop Go-to-Market Strategy](../develop-go-to-market-strategy/) is optional. It owns strategy development; this skill preserves and maintains the evidence, approved outputs and subsequent learning. Existing approved strategy can be referenced without rerunning that workflow. Installation does not require another skill.

When the user invokes an issue-to-draft-PR workflow, its approval gate and branch conventions apply. Marketing-memory maintenance does not silently change those boundaries or become an engineering implementation task.

## Included resources

- [SKILL.md](SKILL.md): mode selection, runtime checks and operational workflow.
- [Memory model](references/memory-model.md): records, approval/lifecycle fields, experiments, results and corrections.
- [Maintenance guidance](references/maintenance.md): repeat-run behavior, audits, scenario checks and handoffs.
- [Starter memory](assets/growth-os/README.md): index, scoped instructions and six usable area documents.
- `agents/openai.yaml`: skill discovery metadata.

No executable helper is necessary for this initial version. The agent inspects and adds missing starter files individually, avoiding destructive bulk copying. It never assumes that an existing destination can be replaced by a fresh template.

## Validation

From the source repository root:

```bash
python scripts/validate_repository.py
```

This checks skill structure, frontmatter, catalog propagation and Markdown hygiene. Use the scenario table in [maintenance guidance](references/maintenance.md) to review bootstrap, repeat updates, conflicting evidence, approval changes, missing denominators and scoped corrections. Check relative links and actual diffs as part of delivery.

Structural validation cannot establish marketing truth, source permissions, statistical reliability, human approval or correct behavior in every host. No live campaign or customer repository needs to be created to validate the generic skill.

## Installation

Install only this leaf directory, including its references and assets.

| Host | Installation |
| --- | --- |
| ChatGPT Work | Add this skill directory through the supported Skills workflow; configure GitHub separately |
| Codex personal | Copy to `~/.agents/skills/manage-marketing-memory/` |
| Codex project | Copy to `.agents/skills/manage-marketing-memory/` |
| Claude Code personal | Copy to `~/.claude/skills/manage-marketing-memory/` |
| Claude Code project | Copy to `.claude/skills/manage-marketing-memory/` |

For a deliberate linked Codex installation from a local checkout:

```bash
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/agent-skills/product/manage-marketing-memory ~/.agents/skills/manage-marketing-memory
```

If the destination already exists, inspect it before replacing or relinking it. In Codex or Work invoke `$manage-marketing-memory`; in Claude Code use the installed skill invocation supported by the host, for example `/manage-marketing-memory`. Provide the destination and intended task. Authenticate GitHub through the host's supported flow, never by embedding tokens in memory files.

## Updating this skill

Installed copies are snapshots. Review source changes and deliberately update the full leaf directory; do not overwrite business memory with new starter assets. For reproducibility, install from a known tag or commit and record that revision. A symlink follows its checkout, so changes to that checkout change the installed instructions. Merging a source PR does not automatically update copied installations.

## Limitations and completion

The skill can only use sources and measurements available to the session. It does not collect analytics, research private customer data or create a schedule merely by being installed. Inaccessible evidence remains a documented limitation. New research, publication, communication and spending require appropriate tools and task authorization.

A GitHub task is complete when its authorized changes are pushed and its review link is verified. A portable scaffold is useful progress but is explicitly reported as such if GitHub delivery is blocked. The handoff includes changed records, checks, unresolved decisions and the next action.
