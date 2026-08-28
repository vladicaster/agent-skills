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
- **Finish:** Add or repair exact captions, end cards, background music, and simple timing outside the generative model.

Combine modes when requested, but do not silently turn planning into paid generation or publication.

## Establish the production contract

Record the objective, audience, platform, aspect ratio, resolution, duration, audio expectations, required exact text, brand constraints, available references, provider preference, delivery destination, and known budget or credit limit. Determine whether burned-in captions or subtitles are required; if the user has not specified them, ask before including them in the production contract. Infer other low-risk creative details; ask only about choices that materially alter the result or authorize cost.

Write a beat sheet before a multi-shot prompt. For every beat, state:

1. what the viewer sees;
2. what changes;
3. why that change follows from the prior beat;
4. which reference establishes the visual truth;
5. what must remain invariant.

Make causal geography explicit. If a character discovers a place remotely, establish a visually distinct starting location before showing travel or arrival. Do not rely on narration to repair contradictory staging.

## Build the reference and continuity contracts

Assign each asset one or more named roles: identity, wardrobe, location, prop, start frame, end frame, motion, composition, style, or audio. Do not assume the provider interprets upload order as intent.

Treat a storyboard, contact sheet, or multi-panel concept board as a planning artifact. Do not upload it as the scene reference when a model needs a standalone start frame, end frame, or identity image. Before paid video generation, create or extract one independently usable keyframe per scene and verify that every keyframe is natively composed at the target aspect ratio. A tall canvas containing stacked landscape panels is not a set of 9:16 references.

When chronology matters, record an ordered scene manifest with a stable scene number, intended duration, reference roles, prompt, and transition responsibility. Preserve that scene index through submission, status polling, result display, review, and concatenation. If the selected model cannot guarantee that multiple uploaded references control a strict timeline, generate one controlled clip per scene and concatenate the completed clips deterministically in manifest order. Do not rely on filename order, upload order, or a composite board to communicate chronology.

Record continuity invariants for recurring people, wardrobe, storefront geometry, interior layout, lighting progression, props, logos, and permitted sign text. Separate exact requirements from flexible attributes. Use the patterns in [references/prompt-patterns.md](references/prompt-patterns.md).

For a fragile interaction such as opening a door, exchanging an object, or using a phone:

- reduce simultaneous body and camera motion;
- keep hands, hinges, contact points, and object paths visible;
- describe the physical sequence in temporal order;
- avoid impossible occlusion or large spatial jumps;
- prefer a cut between actions when one continuous move is not essential.

## Preflight the provider

Use live provider evidence when generation is requested. Verify the selected account or workspace, available models, supported aspect ratios, resolutions, durations, audio behavior, reference limits, current credit balance, and estimated cost. Treat model names and capabilities as time-sensitive. For a multi-scene batch, calculate the complete expected cost across all clips and other chargeable generations rather than quoting only the per-clip price.

If Higgsfield is selected or available, follow [references/higgsfield-seedance.md](references/higgsfield-seedance.md). For another provider, preserve the same preflight, reference-role, approval, job-tracking, and delivery contracts.

Before a chargeable submission, show the selected model/settings and expected cost. Obtain explicit approval unless the user's current request already clearly authorizes that exact generation within a known budget. Never purchase credits, change a subscription, or choose a paid path over an available unlimited path without authorization.

Treat voice auditions, full narration, replacement narration, and generated music cues as separate chargeable generations. Preflight and authorize each requested item at its actual scope; approval for the video or an earlier audio asset does not silently authorize later auditions or replacements. Confirm that a selected audio tool actually supports music; never substitute a speech-only generator for a music request.

Uploading media, spending credits, publishing, and sharing externally are separate permission boundaries.

## Generate and track without losing state

Translate the beat sheet into the provider's supported reference and prompt structure. Include positive action, continuity constraints, camera behavior, audio direction, and high-value exclusions. Do not ask the model to render exact captions, URLs, product names, or end-card copy when deterministic finishing is available.

When exact narration, a selected voice, subtitles, or later copy revision matters, generate the visual clips without embedded narration and create the voice track separately. Resolve the provider's exact voice identifier and voice type through live discovery or user selection; paginate the catalog until the requested voice is found or the catalog is exhausted. Never infer absence from the first page, invent an identifier, or silently substitute a voice.

A matching voice name proves catalog identity, not creative suitability. When tone is subjective or the user is uncertain, offer a short, low-cost audition using representative copy before generating the full narration. Preserve its exact identifier and settings if approved. Mark rejected or superseded narration assets as unusable for future assembly. A copy or voice change invalidates every downstream master containing the older narration, but normally reuses approved visual clips.

After narration completes, measure its actual duration before assembly. If it exceeds the visual runtime, first evaluate a visually acceptable deterministic repair such as modest uniform retiming and a brief final-frame hold. Regenerate paid visuals only when retiming would damage motion, causality, or quality. Rebuild captions and every downstream master from the final approved narration revision.

## Audition and mix background music

Treat cue selection and mix prominence as separate creative decisions. When the user is choosing a musical direction, describe a small set of materially different options and their tonal tradeoffs. Prefer a duration-matched music-only audition before mixing an undecided cue into the approved narrated master.

For every cue, record its identity, intended tone, duration, provenance, licensing state, cost, and approval state. Distinguish original or generated music, an already approved reusable asset, and third-party music that requires verified licensing. Do not represent a generated or discovered track as cleared for publication without evidence.

After cue approval, ask for or infer only when already established the desired prominence. Labels such as **subtle**, **balanced**, **prominent**, or a point between them are creative targets, not universal gain constants. Calibrate them against the actual narration and cue. Preserve the approved narrated master and create a separately named candidate for every mix; a soundtrack-only revision normally reuses visuals and narration without regeneration.

Mix deterministically when the visuals and narration are already approved:

- match the cue to the measured master duration and use intentional entrance and exit fades;
- use narration-aware ducking so music yields during speech and may rise naturally between phrases;
- limit the combined signal and retain headroom without making loudness claims from command success alone;
- mark rejected and superseded mixes so they cannot be confused with the selected master;
- compare candidates using the same source master whenever prominence is the only variable.

Use `scripts/mix_background_music.py` to construct or execute a source-preserving FFmpeg mix after duration and gain have been chosen. Run it with `--dry-run` first. Its numeric gain is an implementation parameter for the current assets, not a reusable definition of a prominence label.

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

When the approved production contract requires narration-driven subtitles, invoke an available dedicated subtitle workflow. Derive timings from transcription of the final approved audio or assembled video. Authored narration may correct recognized wording, brand names, numbers, and punctuation, but it must not supply estimated timestamps. Use word-level timestamps when a sentence boundary or phone-legible line break falls inside a larger transcription segment. Keep captions short, phone-legible, and inside platform safe zones; reserve a separate visual region for an overlapping end card. If the preferred caption font is unavailable, use a verified compatible fallback and rerun only the deterministic burn step. Do not add captions merely because narration exists.

Use `scripts/finish_video.py` to build an FFmpeg command for an optional end card or captions whose timings were already established by a valid external source. It is not a transcription or subtitle-timing tool. Use `scripts/mix_background_music.py` for an approved duration-matched music cue. Run either helper first with `--dry-run`, verify its parameters, then execute only when the local files and FFmpeg are available and the requested write is authorized.

Keep exact product names, URLs, calls to action, and captions out of model-rendered scenery. Generated signs may be blank, generic, or non-readable unless readable environmental text is itself essential and will be reviewed.

After deterministic assembly, verify the final file rather than only the command exit status. Confirm duration, dimensions, aspect ratio, frame rate, video and audio codecs/streams, exact narration and overlay copy, caption timing and safe zones, music provenance and approval, speech intelligibility, fade behavior, clipping or headroom, successful upload or save confirmation, and that the delivered artifact opens and corresponds to the reviewed revision. Present the final revision in a supported player and provide a direct download path when the host exposes one; do not confuse a generation result, audition, or superseded mix with the later assembled master.

## Respect boundaries

Do not expose credentials, account identifiers, private media URLs, customer assets, or proprietary prompts in reusable output. Do not publish, message collaborators, license likenesses or music, or represent brand/legal approval without separate evidence and authorization. GitHub is unnecessary unless the user requests repository-backed storage or delivery.

## Complete the assignment

Return the requested combination of concept, beat sheet, reference-role map, continuity contract, provider preflight, generation record, review findings, repaired media, and delivery link or file. State which checks passed, failed, remain manual, or were not run.

The work is complete only when the requested artifact is accessible, the target format is verified, consequential defects are resolved or disclosed, exact text has been checked deterministically, and no paid generation or external action is represented as completed without evidence.
