---
version: anydesign-element-1
name: "Discord homepage hero — 3D clay scene"
source: https://discord.com
captured_at: 2026-06-10
kind: asset
target:
  description: "the 3D illustration scene in the homepage hero (monitor + characters)"
  selector: ".hero-wr-image.desctop-show"

palette:
  - "#121773"   # deep indigo — the space field the scene floats in
  - "#1E278F"   # mid indigo — ambient gradient
  - "#2E34A9"   # bright indigo — upper gradient / glow
  - "#0B0D37"   # near-black navy — deepest shadows
  - "#1B1A20"   # charcoal — monitor screen and dark panels
  - "#8EA6DD"   # pale periwinkle — robot shell, the lightest solid
  - "#9370C5"   # lilac — character hair/outfit
  - "#6C71BC"   # lavender — ghost decorations
  - "#FA80E4"   # hot pink — tiny UI pops inside the screen (scarce)
---

# Element — Discord homepage hero, 3D clay scene

> Generated with the `anydesign` skill (element mode).
> Kind: asset · Date: 2026-06-10

## Source & target

- **Source**: <https://discord.com> (desktop viewport 1440×900)
- **Targeting**: CSS selector `.hero-wr-image.desctop-show` — DOM-based ✅.
  Element box 774×526.
- **Context**: the scene bleeds out of the hero's right half, floating on the page's
  indigo gradient. It is layered from multiple `.webp` sprites (monitor scene,
  characters, stars) composed in HTML — captured here as the rendered composition.

## 1. What this element is

Discord's signature **clay-style 3D illustration**: an oversized, slightly tilted
monitor running a chat app, flanked by a round-headed robot companion with headphones,
a lilac-haired character checking a phone, a chunky game controller, and tiny ghost
and star decorations — all floating in an indigo night-space. The style does the brand
work: toy-like proportions, soft matte clay surfaces, and a strict indigo world where
the characters' pale blues and lilacs read as warm. It says "gaming with friends at
night" without a single word.

## 2. Spec

*Not applicable — `kind: asset`. The scene ships as layered image sprites; there is
no DOM/CSS to reconstruct. The composition (sprite layering, parallax stars) is the
parent page's job, not the element's.*

## 3. Reconstruction prompt

*Not applicable — `kind: asset`. See Section 4.*

## 4. Generative image prompt

### Canonical prompt (structured)

```
SUBJECT: a cozy night scene of online hangout — an oversized retro-rounded computer
  monitor tilted slightly toward the viewer showing a glowing chat interface, a
  small friendly round robot with chunky headphones standing in the foreground, a
  stylized young character with short lilac hair holding a phone, a toy-like game
  controller resting nearby, two tiny smiling ghosts and small four-point stars
  floating in the air
STYLE / MEDIUM: clay-style 3D render — soft matte surfaces, rounded toy-like
  proportions, gentle subsurface softness, no hard edges, C4D/Blender character-art
  finish
COMPOSITION & CAMERA: 3:2 landscape, eye-level with a slight upward tilt toward the
  monitor, monitor dominating the upper two-thirds, characters grounded at the
  bottom edge, decorative elements scattered in the negative space
LIGHTING: soft studio key from the upper left, cool indigo ambient fill, gentle
  screen-glow bounce on the characters, subtle rim light separating them from the
  dark background
PALETTE: world locked to indigo — background gradient from #0B0D37 through #121773
  to #2E34A9; monitor screen #1B1A20 charcoal; robot shell #8EA6DD pale periwinkle;
  character hair and outfit #9370C5 lilac; ghosts #6C71BC lavender; one scarce hot
  pink accent #FA80E4 inside the screen UI only
MOOD: playful, communal, late-night cozy, toy-like, softly futuristic
BACKGROUND / INTEGRATION: full-bleed over a flat #121773 indigo field — the scene's
  background must blend into that exact tone at the edges, no frame, no vignette
  baked in
AVOID: no text, no logos, no watermarks, no real brand mascots, no photorealism, no
  human skin texture, no harsh shadows, no warm yellows or oranges, no glossy
  plastic shine
```

### Natural-language version

A clay-style 3D render of a cozy late-night online hangout: an oversized,
retro-rounded computer monitor tilted gently toward the viewer, its screen glowing
with a charcoal #1B1A20 chat interface. In the foreground stands a small friendly
round robot with chunky headphones, its shell in pale periwinkle #8EA6DD, next to a
stylized young character with short lilac #9370C5 hair holding a phone, and a
toy-like game controller. Two tiny smiling lavender #6C71BC ghosts and small
four-point stars float in the air. The whole world is locked to indigo — a background
gradient flowing from #0B0D37 through #121773 to #2E34A9 — with a single scarce hot
pink #FA80E4 accent inside the screen UI. Soft matte clay surfaces with rounded
toy-like proportions, lit by a soft studio key from the upper left with cool indigo
ambient fill, screen-glow bounce, and a subtle rim light. Playful, communal, softly
futuristic mood. 3:2 landscape. No text, no logos, no photorealism, no warm yellows,
no glossy plastic shine.

### Isolated variant (delivery format: `isolated`)

To extract a single subject as a web-ready asset instead of the scene — e.g. just
the robot companion. Isolated prompts must be written defensively: lead with the
isolation directive, strip the world/atmosphere words (they summon backdrops), and
keep lighting neutral — otherwise models paint a background and add extra
characters anyway. Ready to paste:

> An isolated asset on a fully transparent background (PNG with alpha): one single
> small friendly round robot with chunky headphones — nothing else in the frame, no
> scenery, no other characters, no props, no floor, no ground shadow. Clay-style 3D
> render, soft matte surfaces, rounded toy-like proportions. Pale periwinkle #8EA6DD
> shell with deep indigo #121773 accents, charcoal #1B1A20 details, one hot pink
> #FA80E4 light on its chest. Full body, three-quarter view, soft neutral studio key
> from the upper left, subtle rim light. No text, no logos, no photorealism, no warm
> tones, no glossy shine, no background of any kind.

If the model still paints a backdrop (common in chat UIs — prose transparency is
unreliable; the dependable route is gpt-image's API parameter
`background: "transparent"`), fall back to a solid flat chroma background in a color
absent from the palette ("on a solid flat pure green #00FF00 background, perfectly
uniform, no gradient, no vignette") and chroma-key it to alpha in post.

### Model adaptation notes

- **gpt-image / DALL-E**: use the natural-language version as-is. For the isolated
  variant, gpt-image supports native transparency (`background: "transparent"` via
  API, or ask for "transparent background, PNG with alpha" in the prompt).
- **Midjourney**: condense to comma phrases; append `--ar 3:2 --style raw`. No true
  alpha — for the isolated variant, prompt a flat high-contrast solid background and
  remove it in post.
- **Stable Diffusion / Flux**: tag-style from the structured fields; move the AVOID
  block into the negative prompt. Isolated variant: flat bg + background removal.

## 5. Consistency notes

- The system is **one world, one temperature**: everything lives inside the indigo
  gradient; the characters read "light" only by contrast (#8EA6DD against #121773).
  Introducing any warm tone collapses the night-hangout atmosphere — the AVOID block
  guards this.
- `#FA80E4` is voltage, not a color of the world: it exists only as tiny pops inside
  the screen UI. Don't let a generator spread it to characters or sky.
- If transplanting this style to another brand: keep the clay finish and lighting
  recipe, swap the indigo ramp for the destination's surface scale, and keep exactly
  one scarce voltage accent.
- **IP guardrail**: Discord's mascots and character designs are brand artwork. The
  prompt deliberately describes *original* characters sharing the style vocabulary
  (clay finish, proportions, palette) — it does not name or reproduce Discord's
  specific characters. Keep it that way for anything public.

## 6. Confidence & open questions

| Aspect | Confidence | Why |
|---|---|---|
| Targeting | ✅ | DOM selector, exact bounding box |
| Palette | ✅ | extracted from the crop + region-sampled accents |
| Style/medium read | ✅ | unambiguous clay-3D rendering |
| Lighting read | ⚠️ | inferred visually from highlight/shadow direction |
| Composition intent | ⚠️ | the scene bleeds off the hero — full art may extend further |
| Animation | ❓ | stars pulse via CSS; the scene may have parallax not captured in a still |

**Open questions**: does the full artwork extend beyond the hero crop (the capture
clips at the container edge)? Is there a dark/light variant served elsewhere on the
site?

> **Prompt fidelity note**: a generative image prompt is a high-fidelity
> *description*, not a guarantee of reproduction. Expect to iterate 2-4 generations;
> the PALETTE and AVOID blocks are the strongest levers.
