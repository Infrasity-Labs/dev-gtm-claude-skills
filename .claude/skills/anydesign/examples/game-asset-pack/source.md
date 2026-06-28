# Source — Game asset pack from one key art (element mode, asset kind)

The game-dev use case for element mode: **one extraction → N consistent assets.**
The #1 pain of AI-generated game art is consistency — a great character, then an
item that looks like it came from a different game. Token-grounded prompts attack
exactly that: the palette and lighting are extracted once, locked hex by hex, and
shared verbatim across every asset prompt.

- **Source**: <https://supercell.com/en/games/brawlstars/> — the hero key art
  (toon 3D characters in a desert canyon)
- **Captured**: 2026-06-11, desktop viewport 1440×900
- **Kind**: `asset` — output is a prompt **pack**: a shared style base + three
  isolated asset prompts (original character, power-up pickup, environment prop),
  all transparent-PNG game sprites

## Reproduction commands

```bash
# 1. Scout the full page
python scripts/capture_site.py https://supercell.com/en/games/brawlstars/ \
    --scroll-capture --output ./brawl.png

# 2. Element capture of the key art
python scripts/capture_site.py https://supercell.com/en/games/brawlstars/ \
    --selector ".HeroImage_heroImage___Kx_A" --output ./element.png

# 3. World palette from the full crop + accents from region crops
python scripts/extract_colors.py ./element.png --top 10
```

The element resolved to a 1440×580 box. Accent colors (energy green `#479579`,
signal red `#E5032E`) were sampled from region crops of the burst and characters.

## IP note

Brawl Stars characters and the Supercell trade dress are brand assets. The prompts
in `element.md` describe **original** subjects sharing the style vocabulary — they
do not name or reproduce existing characters. Treat this as a style study.

## Downstream proof — generated from the character prompt

The Asset 1 prompt (original character + shared style base) produced
[`asset-character.png`](./asset-character.png): an original character with
**verified real alpha** (57% transparent / 29% opaque / 14% antialiased edges).

The palette grounding held: terracotta/sand armor, maroon `#7F2B3B` scarf and
accents, dusty-pink hair, and the energy green `#479579` (with its pale glow edge)
landing exactly where the visual grammar allows it — on the weapon VFX. Honest
deviations: a small ground-shadow patch appeared despite the prompt, and the finish
came out more faceted than matte-3D. Iterate or crop per the prompt-fidelity note.

## Files

- [`element.md`](./element.md) — the asset-pack output (shared style base + three
  isolated asset prompts)
- [`element.png`](./element.png) — the captured key art (1440×580)
- [`asset-character.png`](./asset-character.png) — the character generated from
  Asset 1 (real alpha)
