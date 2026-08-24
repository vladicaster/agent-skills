# Higgsfield and Seedance adapter

Use this adapter when the user explicitly selects Higgsfield, when an available Higgsfield integration is the intended execution path, or when reviewing an existing Higgsfield job. The provider-neutral workflow in `SKILL.md` remains authoritative. Provider tools, model names, costs, and capabilities are time-sensitive: query them live.

## 1. Establish the workspace

Detect the installed Higgsfield plugin or callable tools. Confirm the selected workspace/account through the provider response without exposing internal identifiers. If multiple workspaces are possible and the choice changes balance, assets, or visibility, ask the user to select one.

Do not claim Higgsfield access merely because the skill is installed. A missing plugin, disconnected account, or unavailable tool is a blocked execution path, not permission to substitute another provider silently.

## 2. Discover current capabilities

Query the live model catalog and balance. For Seedance 2.0 and 2.5, record the exact capability data returned for:

- image-to-video, start/end frame, multi-reference, video reference, and audio reference modes;
- supported aspect ratios, resolutions, durations, and output audio;
- reference count, size, type, and ordering constraints;
- paid and unlimited-generation options;
- estimated or quoted credit cost.

Never infer that 2.5 exists in a workspace because it exists publicly, or assume that settings accepted by 2.0 are valid for 2.5. Present only currently available combinations.

## 3. Preflight cost and authorization

Before submission, summarize model, mode, duration, resolution, aspect ratio, audio choice, reference set, quoted cost, and remaining balance. If Higgsfield offers paid credits and an unlimited path, surface both with their relevant tradeoffs. Obtain explicit approval before a chargeable generation unless the current request already authorized that exact run and cost envelope.

Do not purchase credits, switch plans, or retry a failed paid job automatically.

## 4. Upload and assign references

Upload only media necessary for the authorized generation. Confirm each upload succeeded and map the returned asset to a declared role:

- start frame;
- end frame;
- identity/style image reference;
- motion/video reference;
- voice/music/audio reference.

Use the fewest references that establish the contract. Preserve provider asset identifiers privately for job reuse; never publish private storage URLs or customer media in reusable examples.

## 5. Submit and preserve the job record

Translate the approved beat sheet into Higgsfield's current parameter schema. Submit once, then store model/version, settings, asset-role map, prompt revision, cost, job ID, and submission time.

Poll or query the provider using the job ID. Report **queued**, **running**, **failed**, or **completed** only when the provider reports that state. A missing widget or delayed preview is a delivery problem, not proof of generation failure. Do not create a duplicate paid job while the original remains pending.

## 6. Reuse completed work

When creating an approved variant, use Higgsfield's completed job or asset identifiers if the provider supports them. Prefer reuse over downloading and re-uploading, and prefer a deterministic finish over a full regeneration when visuals are already acceptable.

## 7. Finish and deliver

If Higgsfield exposes a sandbox or FFmpeg execution path, use it for exact captions, spelling corrections, end cards, trims, and simple audio replacement. Verify the final output, not only the command status. Preserve the unmodified generated result unless replacement was explicitly requested.

Return the actual resulting media in the host's supported presentation or provide the provider-supported direct artifact. Do not say “you should see it” without evidence that the media was attached or displayed. If only a job ID is available, state that plainly and continue status tracking when requested.

## Seedance review emphasis

Regardless of version, inspect multi-shot causality, subject and location persistence, hand/object interactions, doors and hinges, readable generated text, brand pronunciation, audio continuity, and native 16:9 versus 9:16 composition. Version differences do not remove the need for human review.
