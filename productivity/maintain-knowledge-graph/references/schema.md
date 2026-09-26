# Classified graph v1

Required envelope:

```json
{
  "schema_version": "classified-graph/1",
  "graph_id": "12345678-1234-4234-8234-123456789abc",
  "revision": 1,
  "fields": {"title": {"visibility": "private", "value": "My graph"}},
  "nodes": [{
    "id": "12345678-1234-4234-8234-123456789abd",
    "visibility": "private",
    "fields": {
      "label": {"visibility": "private", "value": "Example person"},
      "type": {"visibility": "private", "value": "Person"},
      "biography": {"visibility": "unclassified", "value": "Supported description"},
      "evidence": {"visibility": "private", "value": {"basis": "user_reported", "source": "Provided conversation", "reported_on": "2026-01-01"}}
    }
  }],
  "edges": []
}
```

An edge has exactly `id`, `visibility`, `source`, `target`, `fields`. Endpoints refer to existing node UUIDs. Its required `relation` field is a visibility/value wrapper with a nonempty string. Nodes require wrapped nonempty `label` and `type` strings. Optional attributes belong directly inside `fields`, individually classified.

Use unique canonical version-4 UUIDs. Never put names, URLs or other semantics in IDs. Field names use lowercase snake_case. Extra envelope keys are rejected to prevent metadata bypasses.

| Visibility | Meaning |
| --- | --- |
| public | Explicitly reviewed for public eligibility; scoped publication approval still required. |
| private | Authorized private readers only. |
| unclassified | No disclosure decision; excluded from public output. |

Effective disclosure is the intersection of record and field visibility. A private node's public field stays private. A public node's private salary is omitted. Public nodes require public label/type; public edges require surviving endpoints and a public relation. Omit nonpublic graph fields. Recompute public counts from the sanitized result.

Nested arrays/objects are atomic: the classification covers every contained value. Split `profile` into `job_title`, `contact_email`, etc. for finer control. Semantic references in field values require human review; only structural edge references are automatically filtered. Keep evidence private independently of its public claim.

Suggested fields: `evidence`, `observed_on`, `valid_from`, `valid_to`, `status`, `uncertainty`, `inference_basis`, `correction_note`. Storage manifests and consent records belong in private fields or private sidecars.

Public export resets revision to 1 to avoid disclosing private edit counts, but preserves opaque IDs across releases. If the user requests unlinkable exports, remap IDs and all semantic ID references in a staged copy and validate again; never silently change canonical identities.

## Legacy migration

The migrate command accepts only `personal_property_graph`. It generates new UUIDs once, preserves node/edge connectivity, stores each full original record in a classified `legacy_record` field, and retains metadata and a private old/new ID map. Known private-context records stay private; all other imported records are unclassified. It rejects duplicate identities, dangling edges, missing labels/types/relations and unsupported formats. Do not migrate the same graph repeatedly; subsequent updates use the resulting canonical master.

Legacy properties and evidence remain intact in atomic classified fields. Split them into independently classified fields before selectively approving public content. Merely setting a migrated node public will not release an unclassified label/type or its legacy record.
