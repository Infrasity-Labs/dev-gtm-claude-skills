---
version: anydesign-element-1
name: "Toon battle-royale key art — game asset pack"
source: https://supercell.com/en/games/brawlstars/
captured_at: 2026-06-11
kind: asset
target:
  description: "the hero key art (toon 3D characters charging through a desert canyon)"
  selector: ".HeroImage_heroImage___Kx_A"

palette:
  - "#DD8C70"   # terracotta — canyon rock, the world's base
  - "#F5B98D"   # warm sand — ground, highlights on rock
  - "#F9D3D5"   # dusty pink — sky wash
  - "#CCC7DB"   # pale lavender — sky horizon, atmospheric haze
  - "#8AB8C6"   # teal-blue — cool shadows on the warm world
  - "#7F2B3B"   # deep maroon — costume accents, shadow cores
  - "#479579"   # energy green — VFX, bursts (with #AFD1B0 glow edge)
  - "#E5032E"   # signal red — danger/brand voltage, used scarcely
  - "#1C2324"   # ink — linework, darkest accents
---

# Element — Toon battle-royale key art → game asset pack

> Generated with the `anydesign` skill (element mode).
> Kind: asset · Date: 2026-06-11

## Source & target

- **Source**: <https://supercell.com/en/games/brawlstars/> (desktop 1440×900)
- **Targeting**: CSS selector `.HeroImage_heroImage___Kx_A` — DOM-based ✅.
  Element box 1440×580.
- **Context**: full-bleed hero key art. Palette extracted from the whole crop;
  accents (energy green, signal red) sampled from region crops of the burst and
  characters.

## 1. What this element is

Mobile-toon **key art**: stylized 3D characters with oversized heads and hands
charging through a desert canyon, a green energy burst behind the logo, bats
scattering across a dusty pink sky. The art direction in one sentence: **a warm
terracotta world cooled by teal shadows, where green VFX and a scarce signal red do
all the shouting.** Chunky silhouettes, matte toon shading with hard light/shadow
breaks, everything readable at thumbnail size — mobile-game discipline.

## 2. Spec

*Not applicable — `kind: asset`. See Section 4.*

## 3. Reconstruction prompt

*Not applicable — `kind: asset`. See Section 4.*

## 4. Generative image prompt — asset pack

This is the game-dev use case: **one extraction → N consistent assets.** The style
base below is shared verbatim by every prompt; only the SUBJECT changes. That shared
base — palette locked hex by hex — is what keeps a character, a pickup, and a prop
looking like they shipped in the same game.

### Shared style base (paste into every asset prompt)

```
STYLE / MEDIUM: stylized mobile-game 3D toon render — matte surfaces, chunky
  proportions, oversized silhouette readable at thumbnail size, hard light/shadow
  breaks, no outlines
LIGHTING: strong warm key from the upper left (desert sun), teal-tinted #8AB8C6
  shadows, subtle bounce from the sand
PALETTE: warm world — terracotta #DD8C70, sand #F5B98D, dusty pink #F9D3D5
  accents; cool shadows #8AB8C6; deep maroon #7F2B3B for costume/detail accents;
  energy green #479579 (glow edge #AFD1B0) reserved for VFX; signal red #E5032E
  used scarcely or not at all; ink #1C2324 for the darkest details
MOOD: playful, scrappy, sun-baked, arcade-energetic
AVOID: no text, no logos, no existing game characters, no photorealism, no soft
  painterly blending, no neon blues or purples, no background of any kind
```

### Asset 1 — Original character

> An isolated game asset on a fully transparent background (PNG with alpha): one
> single original character — a scrappy desert prospector girl with an oversized
> wrench, goggles pushed up on her forehead, chunky boots — nothing else in the
> frame, no scenery, no other characters, no props, no floor, no ground shadow.
> Full body, three-quarter view, confident action pose.
> [+ shared style base]

### Asset 2 — Pickup / power-up

> An isolated game asset on a fully transparent background (PNG with alpha): one
> single power-up pickup — a chunky crystal canister glowing with energy green
> #479579, glow edge #AFD1B0, maroon #7F2B3B metal caps — nothing else in the
> frame, no scenery, no floor, no ground shadow. Slight floating tilt, readable
> at small size.
> [+ shared style base]

### Asset 3 — Environment prop

> An isolated game asset on a fully transparent background (PNG with alpha): one
> single environment prop — a squat terracotta #DD8C70 canyon cactus in a sand
> #F5B98D pot, with tiny dusty pink #F9D3D5 blooms — nothing else in the frame,
> no scenery, no floor, no ground shadow. Chunky toon proportions.
> [+ shared style base]

### Model adaptation notes

- **gpt-image / DALL-E**: paste each asset prompt followed by the shared style
  base as one message. For real alpha use the API parameter
  `background: "transparent"` — prose-only transparency is unreliable.
- **Midjourney**: comma-condense; `--ar 1:1 --style raw`; no true alpha — flat
  chroma background + removal in post.
- **SD / Flux**: tag-style; AVOID block into the negative prompt; flat-bg +
  removal for alpha.

## 5. Consistency notes

- **The pack contract**: every asset shares the lighting recipe (warm key,
  #8AB8C6 teal shadows) and the palette allocation. That's what makes them read
  as one game — change either and the set falls apart.
- Energy green is **VFX-only**: it belongs to pickups, projectiles, and bursts.
  A character wearing it as clothing breaks the visual grammar of the source.
- Signal red #E5032E is voltage: one small element per asset, or none.
- **IP guardrail**: Brawl Stars characters and the Supercell style trade dress
  are brand assets. These prompts describe *original* subjects sharing a style
  vocabulary (toon proportions, palette discipline, lighting) — they do not
  name or reproduce existing characters. For a shipped game, treat this as a
  style study and push your own direction on top.

## 6. Confidence & open questions

| Aspect | Confidence | Why |
|---|---|---|
| Targeting | ✅ | DOM selector, exact bounding box |
| Palette | ✅ | extracted from crop + region-sampled accents |
| Style read | ✅ | unambiguous toon 3D key-art conventions |
| Lighting read | ⚠️ | inferred from highlight/shadow direction in one image |
| Palette allocation rules | ⚠️ | derived from a single key art — in-game UI may differ |

**Open questions**: does the in-game asset style match the key-art style (key art
is usually higher-fidelity)? Is the green/red allocation consistent across other
marketing art?

> **Prompt fidelity note**: a generative image prompt is a high-fidelity
> *description*, not a guarantee of reproduction. Expect to iterate 2-4
> generations per asset; the PALETTE and AVOID blocks are the strongest levers.
