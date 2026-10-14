# World and timeline contract

Use a JSON manifest, a database, or an equivalent explicit structure. The following fields define the minimum production contract; adapt the storage format without losing traceability.

## Project

Record project ID, subject, factual/fictional/illustrative status, coordinate system, units, extent, time range, date precision, duration_seconds, fps, dimensions, renderer, scene version, and artifact destination.

## Evidence and milestones

For each milestone record id, entity_ids, event type, historical date or range, precision, source_ids, evidence status, animation interpretation, video_start_seconds, video_end_seconds, and dependencies.

Event types include construct, open, expand, demolish, replace, terrain_change, and infrastructure_change. An opening does not imply a fully researched construction schedule. Mark accelerated construction animation as schematic unless evidence supports the stages.

## Entities

Record id, label, world position, rotation, footprint, height/scale, asset ID and version, present_from, present_until (exclusive or null), predecessor/successor IDs, source_ids, and geometry confidence. Store lifecycle stages separately when assets change without entity identity changing.

Evaluate presence at historical time t as present_from <= t and (present_until is null or t < present_until). Distinguish site identity from building identity. Preserve unchanged entities; update or replace only those affected by a milestone.

## Time mapping

Record ordered segments:
- video start/end in seconds;
- historical start/end with explicit units or date representation;
- mapping (linear, eased, or hold);
- active event IDs.

Use nondecreasing historical time for the main sequence. Model an optional rewind hook as a separate segment with an explicit direction and cut into the main sequence. Require contiguous video coverage unless a deliberate cut/hold is specified. Resolve simultaneous events explicitly.

For a linear segment, map fraction u = (video_time - video_start) / (video_end - video_start) into historical_start + u * (historical_end - historical_start). Use the same mapped date to evaluate world state and text. Record rounding rules so a displayed year cannot imply the wrong event state.

## Camera and overlays

Record shot ID, video interval, camera position/target keyframes, lens, interpolation, geographic anchors, event focus, transition, and safe regions. Record exact overlay text or date formatter, timing, typography, and screen placement.

## Render and review

Record revision, scene/manifest hashes if available, renderer/settings, job IDs, status, cost, output file, metadata verification, sampled frames, playback review, failures, and superseded revisions. Check start/end and frames around every state boundary. Keep the approved master separate from candidates.

## Worked miniature (fictional)

A 25-second harbor-town proof may map:
- 0–4 seconds: 1800, coastline and dock established;
- 4–9: 1800–1850, warehouse and road added;
- 9–14: 1850–1900, railway and housing added;
- 14–19: 1900–1950, warehouse removed then replaced on its site;
- 19–25: 1950–2000, expansion and final reveal.

Assign five evidence/canon milestones and stable IDs; specify exact event dates within these spans. This example is fictional and supplies no real-world historical claims.
