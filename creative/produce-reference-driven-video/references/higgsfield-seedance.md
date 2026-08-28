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

Voice catalogs may be paginated. When the user requests a named voice, continue through `next_cursor` pages until the exact name is found or the catalog is exhausted. A first page that omits the name is not evidence that the voice is unavailable. Preserve the returned `voice_id` and `voice_type` pair; do not reconstruct it from the display name.

## 3. Preflight cost and authorization

Before submission, summarize model, mode, duration, resolution, aspect ratio, audio choice, reference set, quoted cost, and remaining balance. If Higgsfield offers paid credits and an unlimited path, surface both with their relevant tradeoffs. Obtain explicit approval before a chargeable generation unless the current request already authorized that exact run and cost envelope.

For a batch, estimate every chargeable item and show the total. For example, three equal-cost scene clips require three cost units; a one-clip estimate is not the batch estimate. Include separately generated narration or other paid assets when they are known before authorization.

Price voice auditions independently from full narration. A request to hear a sample authorizes only that sample after its live cost is known; approval of a full video does not automatically cover additional auditions or replacement voices.

Do not purchase credits, switch plans, or retry a failed paid job automatically.

## 4. Upload and assign references

Upload only media necessary for the authorized generation. Confirm each upload succeeded and map the returned asset to a declared role:

- start frame;
- end frame;
- identity/style image reference;
- motion/video reference;
- voice/music/audio reference.

Use the fewest references that establish the contract. Preserve provider asset identifiers privately for job reuse; never publish private storage URLs or customer media in reusable examples.

Do not use a storyboard sheet as a start frame merely because it contains the desired scenes. Produce one standalone image per scene, inspect its actual pixel dimensions, and confirm it is a native composition for the requested aspect ratio before upload. Map every returned media identifier to its stable scene number and role.

## 5. Submit and preserve the job record

Translate the approved beat sheet into Higgsfield's current parameter schema. Submit once, then store model/version, settings, asset-role map, prompt revision, cost, job ID, and submission time.

Poll or query the provider using the job ID. Report **queued**, **running**, **failed**, or **completed** only when the provider reports that state. A missing widget or delayed preview is a delivery problem, not proof of generation failure. Do not create a duplicate paid job while the original remains pending.

When exact scene order is essential and the selected mode does not expose a guaranteed timeline contract, submit one image-to-video job per scene, preserving the scene index in the batch record. Wait for the complete batch, present the results in scene order, and concatenate only the completed intended jobs. Do not infer chronology from upload order.

Disable model-generated audio when narration copy, a selected voice, or subtitles must remain independently editable. Discover the exact voice identifier and type before speech generation. A change to spoken wording invalidates the prior narration and every assembled master that contains it, but does not require regenerating approved visual clips.

Do not treat a catalog name as approval of timbre. If the user has not heard the voice or asks for a subjective quality such as warm, sweet, authoritative, or conversational, generate an approved short audition from representative copy before the full read. Keep audition, approved narration, rejected narration, and superseded masters as distinct revision states. Never assemble from a rejected or superseded audio job.

## 6. Reuse completed work

When creating an approved variant, use Higgsfield's completed job or asset identifiers if the provider supports them. Prefer reuse over downloading and re-uploading, and prefer a deterministic finish over a full regeneration when visuals are already acceptable.

## 7. Finish and deliver

If Higgsfield exposes a sandbox or FFmpeg execution path, use it for exact captions, spelling corrections, end cards, trims, and simple audio replacement. Verify the final output, not only the command status. Preserve the unmodified generated result unless replacement was explicitly requested.

Measure the completed narration and visual runtimes before assembly. When narration is slightly longer, prefer modest deterministic visual retiming and a final-frame hold over paid visual regeneration if motion remains natural. Record the retiming factor and verify the resulting motion. If the gap is too large or retiming weakens the scene, revise the script or seek approval for new visuals instead of hiding the mismatch.

For spoken captions, use the available subtitle workflow to run Whisper or another approved transcription backend against the final approved audio or assembled video. Supply authored narration only to correct the transcribed words while retaining audio-derived timing. Request word timestamps when a sentence or caption line must be split inside a larger transcription segment. Every voice or copy change requires fresh transcription and a rebuilt captioned master. For a vertical social ad, use the workflow's platform-safe social style unless the user selects another supported look. If a bundled font path fails, rerun the burn with a verified installed font path; do not estimate subtitle timings or hand-roll a replacement caption burner.

After assembly, inspect media metadata and the delivered artifact: duration, 9:16 or 16:9 dimensions, frame rate, video and audio codecs/streams, exact narration revision, captions, end-card text, and accessibility. Confirm the provider upload before sharing the final URL. Present the assembled revision rather than a source generation and include a direct download path when available.

Return the actual resulting media in the host's supported presentation or provide the provider-supported direct artifact. Do not say “you should see it” without evidence that the media was attached or displayed. If only a job ID is available, state that plainly and continue status tracking when requested.

## Seedance review emphasis

Regardless of version, inspect multi-shot causality, subject and location persistence, hand/object interactions, doors and hinges, readable generated text, brand pronunciation, audio continuity, and native 16:9 versus 9:16 composition. Version differences do not remove the need for human review.
