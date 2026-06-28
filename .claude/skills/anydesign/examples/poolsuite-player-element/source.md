# Source — Poolsuite FM player window (element mode)

First real-world run of **element mode** ("copy element"), introduced in v0.5.0.

- **Source**: <https://poolsuite.net> — the cult desktop-only "summer internet radio"
  with a faithful retro Mac OS interface
- **Target element**: the player window (PoolTV screen + FM transport controls) —
  the site's signature component
- **Captured**: 2026-06-10, desktop viewport 1440×900
- **Kind**: `hybrid` — the window chrome is reconstructable code; the screen content
  (VHS footage) is an asset → gets a token-grounded generative image prompt

## Reproduction commands

```bash
# 1. Scout the full page to locate the element
python scripts/capture_site.py https://poolsuite.net --scroll-capture \
    --output ./poolsuite.png

# 2. Element capture — screenshot + outerHTML of the player window only
python scripts/capture_site.py https://poolsuite.net \
    --selector "#component-is-fm" --output ./element.png

# 3. Exact palette from the element crop
python scripts/extract_colors.py ./element.png --top 10

# 4. Explicit tokens from the live CSS (shadow system, font declarations)
python scripts/extract_css_vars.py https://poolsuite.net --pretty
```

The element resolved to a 607×640 box at (417, 101). Targeting was DOM-based
(`#component-is-fm`), so structure and tokens carry ✅ high confidence.

## Downstream proof — rebuilt by v0

The reconstruction prompt (Section 3 of `element.md`) was pasted into
[v0](https://v0.dev) verbatim. The live result:

**<https://retro-radio-player-zz.vercel.app/>** — see
[`v0-result.png`](./v0-result.png)

It took **two iterations**, exactly as the prompt-fidelity note predicts. The first
pass nailed structure, hard shadows, and accent rationing but drifted to ALL-CAPS +
wide tracking on every text block — which reads "8-bit videogame" instead of
"Mac OS System 7". One surgical follow-up (sentence case everywhere except the
wordmark, button order, bevel strength) closed most of the gap. That lesson is now
baked into the skill: case discipline and tracking are captured as first-class
typography tokens (`references/element-copy.md`), and this example's reconstruction
prompt already includes the rule.

Branding note: the rebuild deliberately uses placeholder branding ("RETROWAVE FM")
and self-drawn glyphs — element mode's IP guardrail forbids reproducing Poolsuite's
wordmark and icon artwork.

## Files

- [`element.md`](./element.md) — the element-mode output (spec + reconstruction
  prompt + generative image prompt)
- [`element.png`](./element.png) — the captured element (607×640)
- [`element.html`](./element.html) — the element's outerHTML, as saved by
  `--selector`
- [`v0-result.png`](./v0-result.png) — the v0 rebuild, live at
  [retro-radio-player-zz.vercel.app](https://retro-radio-player-zz.vercel.app/)
