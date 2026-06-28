# Source — Discord homepage hero 3D scene (element mode, asset kind)

Validation run of element mode's **`asset` path**: the element is visual art (a
clay-style 3D illustration), so the output is a token-grounded generative image
prompt instead of a code spec.

- **Source**: <https://discord.com> — homepage hero, desktop viewport 1440×900
- **Target element**: the 3D illustration scene (tilted monitor + robot + character
  + decorations), composed from layered `.webp` sprites
- **Captured**: 2026-06-10
- **Kind**: `asset`

## Reproduction commands

```bash
# 1. Scout the full page
python scripts/capture_site.py https://discord.com --scroll-capture \
    --output ./discord.png

# 2. Element capture of the composed hero scene
python scripts/capture_site.py https://discord.com \
    --selector ".hero-wr-image.desctop-show" --output ./element.png

# 3. Exact palette from the crop (plus region crops for character accents)
python scripts/extract_colors.py ./element.png --top 10
```

The element resolved to a 774×526 box. Background palette extracted from the full
crop; character accents (robot periwinkle, lilac hair, lavender ghosts) sampled from
region crops.

## Downstream proof — generated from the prompt

Both delivery formats were validated against a real image model:

**`scene`** — the natural-language prompt from `element.md` Section 4 produced
[`element-3D.png`](./element-3D.png), first-pass result, no iterations.

**`isolated`** — the defensive isolated-variant prompt produced
[`element-3D-isolated.png`](./element-3D-isolated.png): the robot companion alone,
with **real alpha** (verified histogram: 65% transparent / 22% opaque / 13%
partial-alpha antialiased edges), no scenery, no ground shadow — a web-ready cutout.
It took two attempts: the first, politely-worded request for transparency was
ignored (the model painted a backdrop and added extra characters), which is why the
prompt in `element.md` leads with the isolation directive and strips all
world/atmosphere words. That lesson is baked into
`references/element-copy.md`.

What the token grounding visibly bought: the world stayed locked to the indigo ramp
(no warm tones — the AVOID block held), the robot landed on the pale periwinkle
`#8EA6DD`, the character's hair on lilac `#9370C5`, the ghosts on lavender `#6C71BC`,
and the scarce hot pink `#FA80E4` appeared **only inside the screen UI**, exactly as
the PALETTE block scoped it. Matte clay finish throughout, no glossy plastic — and
original characters, per the IP guardrail.

## Files

- [`element.md`](./element.md) — the asset-kind output (token-grounded generative
  image prompt, including the `isolated`/transparent-PNG variant)
- [`element.png`](./element.png) — the captured element (774×526)
- [`element-3D.png`](./element-3D.png) — the scene generated from the prompt
- [`element-3D-isolated.png`](./element-3D-isolated.png) — the isolated cutout
  (real alpha) generated from the defensive variant
