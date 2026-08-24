# Prompt patterns

Use these structures as provider-neutral planning aids. Adapt them to the selected model's documented input format.

## Causal multi-beat story

```text
Objective: <one viewer takeaway>
Tone and visual language: <human description, not model jargon>

Beat 1 — Establish: <subject, action, and unmistakable starting location>
Beat 2 — Trigger: <new information or event that motivates movement>
Beat 3 — Transition: <how the subject travels, searches, or changes state>
Beat 4 — Payoff: <arrival, interaction, or result>

Continuity invariants: <identity, wardrobe, prop, location, light>
Camera: <shot size and one physically plausible move per beat>
Audio: <ambience, dialogue, pronunciation, music behavior>
Exclude: <contradictory geography, extra characters, malformed contact, text>
```

The trigger must be visible enough to explain the transition. If a customer discovers a shop on a phone, make the first location visually unrelated to the shop, then show the discovery, travel, and arrival as separate beats.

## Reference-role map

| Asset | Role | Establishes | Must not control |
| --- | --- | --- | --- |
| Image A | Identity | face, hair, age | location |
| Image B | Location | facade, doorway, materials | readable sign copy |
| Image C | Start frame | composition at time zero | ending action |
| Video D | Motion | walking pace or camera move | wardrobe |
| Audio E | Voice | speaker and pronunciation | ambient scene |

Assign roles explicitly even when one asset has multiple uses. Resolve conflicts before uploading.

## Physical interaction

```text
The subject stands on the handle side of the closed door. Their hand reaches the fixed handle, fingers close around it, the door rotates around the visible hinge line, and the subject steps through only after the opening is clear. The camera remains steady and preserves the full hand-handle-hinge relationship.
```

Replace the objects and action as needed. Describe contact, force, path, and order. If the model cannot maintain the interaction, cut before and after it.

## Continuity block

```text
Same person throughout: <stable identity traits>.
Same wardrobe throughout: <garments and colors>.
Same location after arrival: <facade/interior invariants>.
Persistent prop: <appearance and which hand carries it>.
Time progression: <permitted lighting change>.
No substitutions, duplicate subjects, wardrobe changes, or geometry changes.
```

## Audio and pronunciation

Write spoken copy separately from visual direction. Include a pronunciation hint only when the provider supports it. Avoid ambiguous symbols in narration: write the intended spoken form, while reserving exact brand typography for deterministic overlays.

## Aspect-ratio adaptation

For 16:9, define lateral relationships and safe negative space. For 9:16, stack actions in depth, keep the main subject central, enlarge phone/action details, and reserve upper and lower safe areas for interface overlays and captions. Rebuild shot composition; do not request a crop of the landscape render.

## High-value exclusions

Use exclusions sparingly and concretely:

- no storefront or coffee-shop imagery in the remote discovery scene;
- no readable generated signs, captions, logos, URLs, or end-card text;
- no duplicated people, disappearing props, wardrobe changes, or location morphs;
- no hand-object fusion, backward hinges, sliding doors described as swinging, or impossible contact;
- no abrupt time-of-day change unless specified.
