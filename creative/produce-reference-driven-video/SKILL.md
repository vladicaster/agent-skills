---
name: produce-reference-driven-video
description: Plan, generate, adapt, review, and finish short reference-driven AI videos. Use for promotional, narrative, product, or social video work that needs explicit story causality, image/video/audio reference roles, character and location continuity, landscape or vertical variants, provider capability and credit preflight, generation-job tracking, quality review, or deterministic captions and end cards. Supports a provider-neutral core with a first-class Higgsfield and Seedance adapter.
---

# Produce Reference-Driven Video

Turn a video objective and reference media into a controlled production package and, when authorized, a finished short video. Prefer a small number of legible story beats over a visually dense prompt.

## Select the operating mode

- **Concept:** Define the audience, promise, emotional tone, story, platform, and call to action.
- **Reference Plan:** Design or inspect frames and assign each image, video, or audio asset one explicit role.
- **Generate:** Preflight a provider, obtain any required spending approval, submit a generation, and track it to a verified result.
- **Adapt:** Recompose an approved story natively for another aspect ratio, duration, or platform.
- **Review:** Inspect the rendered media for story, physics, continuity, audio, typography, and delivery defects.
- **Finish:** Add or repair exact captions, end cards, and simple timing outside the generative model.

Combine modes when requested, but do not silently turn planning into paid generation or publication.

## Establish the production contract

Record the objective, audience, platform, aspect ratio, resolution, duration, audio expectations, required exact text, brand constraints, available references, provider preference, delivery destination, and known budget or credit limit. Infer low-risk creative details; ask only about choices that materially alter the result or authorize cost.

Write a beat sheet before a multi-shot prompt. For every beat, state:

1. what the viewer sees;
2. what changes;
3. why that change follows from the prior beat;
4. which reference establishes the visual truth;
5. what must remain invariant.

Make causal geography explicit. If a character discovers a place remotely, establish a visually distinct starting location before showing travel or arrival. Do not rely on narration to repair contradictory staging.

## Build the reference and continuity contracts

Assign each asset one or more named roles: identity, wardrobe, location, prop, start frame, end frame, motion, composition, style, or audio. Do not assume the provider interprets upload order as intent.

Record continuity invariants for recurring people, wardrobe, storefront geometry, interior layout, lighting progression, props, logos, and permitted sign text. Separate exact requirements from flexible attributes. Use the patterns in [references/prompt-patterns.md](references/prompt-patterns.md).

For a fragile interaction such as opening a door, exchanging an object, or using a phone:

- reduce simultaneous body and camera motion;
- keep hands, hinges, contact points, and object paths visible;
- describe the physical sequence in temporal order;
- avoid impossible occlusion or large spatial jumps;
- prefer a cut between actions when one continuous move is not essential.

## Preflight the provider

Use live provider evidence when generation is requested. Verify the selected account or workspace, available models, supported aspect ratios, resolutions, durations, audio behavior, reference limits, current credit balance, and estimated cost. Treat model names and capabilities as time-sensitive.

If Higgsfield is selected or available, follow [references/higgsfield-seedance.md](references/higgsfield-seedance.md). For another provider, preserve the same preflight, reference-role, approval, job-tracking, and delivery contracts.

Before a chargeable submission, show the selected model/settings and expected cost. Obtain explicit approval unless the user's current request already clearly authorizes that exact generation within a known budget. Never purchase credits, change a subscription, or choose a paid path over an available unlimited path without authorization.

Uploading media, spending credits, publishing, and sharing externally are separate permission boundaries.

## Generate and track without losing state

Translate the beat sheet into the provider's supported reference and prompt structure. Include positive action, continuity constraints, camera behavior, audio direction, and high-value exclusions. Do not ask the model to render exact captions, URLs, product names, or end-card copy when deterministic finishing is available.

After submission:

- preserve the provider, workspace, model, settings, reference roles, job identifier, cost, and submission time;
- distinguish queued, running, failed, and completed states;
- report status only from provider evidence;
- reuse a completed result or provider asset identifier when making an approved variant;
- never imply a result is visible in an app widget without confirming it;
- return the actual media artifact or direct supported media presentation when complete.

Do not resubmit merely because status is slow or a widget did not render. Diagnose delivery separately from generation.

## Adapt for another format

Treat vertical and landscape as separate compositions, not crops. Preserve story function and continuity while changing blocking, negative space, subject scale, camera distance, title-safe areas, and caption placement. Confirm that the first beat remains immediately understandable on the target platform.

## Review before accepting the render

Use [references/quality-checklist.md](references/quality-checklist.md). Review the video itself, including representative frames and audio when tools permit. Check causal clarity, starting geography, identity, wardrobe, location, object permanence, hand/object contact, door and hinge physics, camera motion, pronunciation, exact spelling, caption timing, end-card legibility, safe zones, resolution, duration, and file accessibility.

Classify each defect:

- **Regenerate:** story causality, identity, location, severe geometry, broken physics, or missing essential action.
- **Finish deterministically:** captions, spelling, end-card copy, simple overlays, timing trims, or audio replacement that does not require new visual action.
- **Accept:** harmless variation that does not weaken meaning, continuity, brand, or platform fit.

Prefer the least expensive repair that fixes the actual defect. Never spend additional credits without renewed authorization when cost was not already approved.

## Finish exact text deterministically

Use `scripts/finish_video.py` to build an FFmpeg command for timed captions and an optional end card. Run it first with `--dry-run`, verify exact spelling and timing, then execute only when the local files and FFmpeg are available and the requested write is authorized.

Keep exact product names, URLs, calls to action, and captions out of model-rendered scenery. Generated signs may be blank, generic, or non-readable unless readable environmental text is itself essential and will be reviewed.

## Respect boundaries

Do not expose credentials, account identifiers, private media URLs, customer assets, or proprietary prompts in reusable output. Do not publish, message collaborators, license likenesses or music, or represent brand/legal approval without separate evidence and authorization. GitHub is unnecessary unless the user requests repository-backed storage or delivery.

## Complete the assignment

Return the requested combination of concept, beat sheet, reference-role map, continuity contract, provider preflight, generation record, review findings, repaired media, and delivery link or file. State which checks passed, failed, remain manual, or were not run.

The work is complete only when the requested artifact is accessible, the target format is verified, consequential defects are resolved or disclosed, exact text has been checked deterministically, and no paid generation or external action is represented as completed without evidence.
