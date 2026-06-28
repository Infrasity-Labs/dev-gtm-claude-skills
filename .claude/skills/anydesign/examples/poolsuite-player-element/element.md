---
version: anydesign-element-1
name: "Poolsuite FM player window"
source: https://poolsuite.net
captured_at: 2026-06-10
kind: hybrid
target:
  description: "the retro Mac OS player window (PoolTV screen + FM transport controls)"
  selector: "#component-is-fm"

colors:
  surface-window: "#F5F0EC"
  surface-page: "#F5D2D2"
  surface-card: "#FFFFFF"
  ink: "#000000"
  text-primary: "#231815"
  screen: "#000000"
  accent-play: "#AFE2E5"
  accent-pink: "#F6D5D5"
  live-red: "#EF4444"
  slider-gray: "#D1D1D1"
typography:
  ui-bitmap:
    fontFamily: "Chicago, 'Pixelify Sans', monospace"
    fontSize: 13px
    fontWeight: 700
  ui-bitmap-regular:
    fontFamily: "Pixolde, 'Pixelify Sans', monospace"
    fontSize: 13px
    fontWeight: 400
  filename-mono:
    fontFamily: "KHTekaMono, ui-monospace, monospace"
    fontSize: 11px
    fontWeight: 400
spacing-used: [2, 6, 12]
rounded-used: { window: 6px, control: 2px }

palette:
  - "#F5F0EC"   # window chrome, ~11% of element area
  - "#FFFFFF"   # cards and controls, ~12%
  - "#000000"   # ink: borders, screen field, type
  - "#AFE2E5"   # the aqua play button — the only cool accent
  - "#F6D5D5"   # pink accent button, echoes the page background
  - "#EF4444"   # ON AIR live dot
---

# Element — Poolsuite FM player window

> Generated with the `anydesign` skill (element mode).
> Kind: hybrid · Date: 2026-06-10

## Source & target

- **Source**: <https://poolsuite.net> (desktop-only experience, 1440×900 capture)
- **Targeting**: CSS selector `#component-is-fm` — DOM-based ✅. Element box 607×640.
- **Context**: the window floats on a flat pink page field `{colors.surface-page}`
  (#F5D2D2), draggable and resizable like a real OS window. It is the centerpiece of
  the page — everything else (top bar, dock) is satellite chrome.

## 1. What this element is

A pixel-faithful **retro Mac OS media player window**: System-7-style title bar, a
black "PoolTV" screen playing VHS-grade leisure footage, a track card with a pulsing
ON AIR dot, hardware-like transport buttons, and a channel selector with a LIVE badge.
It is the signature component of Poolsuite — the entire brand (1997 desktop nostalgia,
leisure-as-luxury) is carried by this one window. Its distinctive move: **every press
inverts the control's colors** (`active:invert`), exactly like classic Mac OS.

## 2. Spec

### Structure (from outerHTML — ✅ high)

```
window  (#component-is-fm) — 607×640, draggable + resizable
├── title bar (drag-header)
│   ├── close button 18×18 (pixel ✕ icon, active:invert)
│   ├── TV-toggle button 18×18 (black fill)
│   └── wordmark "POOLSUITE" right-aligned (bitmap caps)
├── screen — black field, 4:3-ish content (591×455)
│   └── filename bar: ◂ ▸ "TheDream91.mov" · right: "591x455"  (mono, white on black)
├── track card (white, 1px ink border)
│   ├── "Poolsuite: ON AIR" (bold bitmap) + pulsing red dot
│   └── track line: "Pacific Coliseum — Ocean City"
├── status row: "Stopped" / scrolling title when playing
│   └── transport: [▶ aqua] [■ white] [⏮ white] [⏭ white] [♪ pink]
└── channel bar: select "Channel: Poolsuite ON AIR" + LIVE badge · volume slider
    (dithered track, gray handle)
```

### Tokens

| Token | Value | Role | Confidence |
|---|---|---|---|
| `{colors.surface-window}` | `#F5F0EC` | Window chrome (bone/cream) | ✅ extracted |
| `{colors.surface-page}` | `#F5D2D2` | Page field the window sits on | ✅ extracted |
| `{colors.surface-card}` | `#FFFFFF` | Track card, transport buttons | ✅ extracted |
| `{colors.ink}` | `#000000` | Every border (1px), screen field, icons | ✅ from classes (`border-black`) |
| `{colors.accent-play}` | `#AFE2E5` | Play button only | ✅ pixel-sampled |
| `{colors.accent-pink}` | `#F6D5D5` | Special action button only | ✅ pixel-sampled |
| `{colors.live-red}` | `#EF4444` | ON AIR dot (with ping animation) | ✅ from classes (`bg-red-500`) |
| `{colors.slider-gray}` | `#D1D1D1` | Volume slider handle | ✅ from classes (`bg-[#D1D1D1]`) |

**Typography** — declared in the live CSS ✅ : `Chicago` (bitmap UI face — the
original Mac System font), `Pixolde` (regular pixel face), `KHTekaMono` (mono, used
white-on-black in the filename bar). Which face maps to which text block is visually
inferred ⚠️. Sizes ~11-13px, bitmap-crisp (no antialiasing).
**Case discipline** ✅: all UI text is **sentence case with no added tracking**
("Stopped", "Pacific Coliseum — Ocean City"); ALL-CAPS exists only in the title-bar
wordmark. This is load-bearing — all-caps + wide tracking reads "8-bit videogame"
instead of "Mac OS System 7".

**Elevation — the bevel system** (verbatim from live CSS ✅):

| Treatment | CSS | Use |
|---|---|---|
| Hard offset | `2px 2px 0 0` / `5px 5px 0 {colors.ink}` | Window drop shadow |
| Bevel raised | `inset 1px 1px 0 0` (light) + `inset -1px -1px 0 0` (dark) + `0 0 0 1px` ring | Buttons at rest |
| Bevel pressed | inverted inset pair | Buttons active |

No blur anywhere. Depth is 1-bit, like the OS it imitates.

**Radii**: window `6px`; controls `2px`. **Borders**: 1px solid `{colors.ink}`,
everywhere — the system's skeleton.

### States (observed + implicit)

- **Press**: `active:invert` — full color inversion of the control ✅ (the signature)
- **Focus**: `focus-visible:invert` ✅
- **Playing vs stopped**: status text swaps; track title scrolls (marquee) ⚠️ inferred
- **Hover**: none observed ❓ — consistent with the OS metaphor (Mac OS had no hover)

### Behavior

Draggable + resizable window (`vue-draggable-resizable`); min size 607×640. Stack
signals: Tailwind utilities + Vue 3 ✅.

## 3. Reconstruction prompt

Paste this into v0, Claude Code, or Lovable:

> Build a desktop-only retro Mac OS-style internet-radio player window, pixel-faithful
> to System 7 aesthetics. Single React component + Tailwind.
>
> **Page**: flat `#F5D2D2` pink background, window centered, ~607×640px.
> **Window**: `#F5F0EC` background, 1px solid `#000000` border, 6px radius, 6px inner
> padding, hard black shadow `5px 5px 0 #000` (no blur — depth is 1-bit everywhere).
> **Title bar**: left — an 18×18 close button with a pixel ✕ and an 18×18 black
> TV-toggle button; right — the wordmark "RETROWAVE FM" in bitmap caps.
> **Screen**: black field, 4:3, filling the window width; render animated TV static
> (SVG `feTurbulence` thresholded to 1-bit black/white, or a tiny canvas loop). Below
> it a black filename bar: white monospace "TheDream91.mov" left, "591x455" right,
> with ◂ ▸ pixel arrows.
> **Track card**: white, 1px black border, 2px radius: bold "RETROWAVE: ON AIR" plus a
> pulsing `#EF4444` dot (CSS ping), and a second line "Pacific Coliseum — Ocean City".
> **Status + transport**: "Stopped" label; a row of ~36px square buttons, each white
> with 1px black border, 2px radius, and Mac-style bevels
> (`box-shadow: inset 1px 1px 0 #fff, inset -1px -1px 0 rgba(0,0,0,.25), 0 0 0 1px #000`):
> play ▶ filled `#AFE2E5`, stop ■, prev ⏮, next ⏭, and a `#F6D5D5` pink button with a
> ♪ glyph. **On press, invert the button's colors completely** (`filter: invert(1)`)
> — this is the signature interaction, do not replace it with opacity or scale.
> **Channel bar**: a select reading "Channel: Retrowave ON AIR" with a small LIVE
> badge, plus a volume slider with a checkerboard-dithered track and a `#D1D1D1`
> square handle.
> **Type**: bitmap pixel font throughout (use Google Fonts "Pixelify Sans" for UI
> text — it has proper lowercase, closest to Mac's Chicago; the original uses the
> licensed Chicago/Pixolde faces), ~13px, `image-rendering: pixelated`, no
> antialiased smoothing, no font over 700 weight. **Sentence case for ALL UI text
> with zero added letter-spacing** ("Stopped", "Pacific Coliseum — Ocean City");
> ALL-CAPS only in the title-bar wordmark and the filename bar — all-caps UI breaks
> the System 7 illusion.
> **Hard rules**: no gradients, no blurred shadows, no rounded corners above 6px, no
> hover effects (Mac OS had none) — press-invert only. Desktop-only; don't adapt to
> mobile. Use original placeholder branding ("RETROWAVE FM") and draw the pixel
> glyphs yourself (✕ ▶ ■ ♪) — do not reproduce Poolsuite's wordmark or icon artwork.

## 4. Generative image prompt

For the screen content — the VHS still the window plays. The TV static itself is
better done in code (see Section 3); this prompt regenerates the **footage frame**.

### Canonical prompt (structured)

```
SUBJECT: freeze-frame of 1990s camcorder footage — a hotel swimming pool with a
  lone palm tree, sun flare hitting the water, an empty deck chair in the
  foreground
STYLE / MEDIUM: analog VHS still — chroma bleed, slight tape warp, faint horizontal
  scanlines, timestamp-free
COMPOSITION & CAMERA: 4:3 aspect, eye-level handheld framing, subject slightly
  off-center right, generous sky
LIGHTING: harsh midday sun, blown-out highlights, warm haze
PALETTE: water and sky pulled toward #AFE2E5 aqua; haze and highlights wash toward
  #F5D2D2 pink and #F5F0EC cream; shadows crush to #231815 — the frame must
  harmonize with the player chrome around it
MOOD: nostalgic, leisurely, sun-bleached, softly artificial
BACKGROUND / INTEGRATION: full-bleed inside a black 591×455 screen area; edges may
  vignette into black, no border baked in
AVOID: no text, no timestamp overlay, no watermark, no people's faces, no modern
  crisp digital look, no HDR
```

### Natural-language version

A freeze-frame from 1990s camcorder footage: a hotel swimming pool with a single palm
tree and an empty deck chair in the foreground, shot handheld at eye level in 4:3 under
harsh midday sun. Analog VHS texture throughout — chroma bleed, slight tape warp, faint
scanlines, blown-out highlights. The water and sky lean toward aqua #AFE2E5, the sunlit
haze washes toward pink #F5D2D2 and cream #F5F0EC, and the shadows crush to deep brown
#231815, so the frame harmonizes with the cream-and-pink player chrome that surrounds
it. Nostalgic, leisurely, sun-bleached mood. No text, no timestamp, no watermark, no
faces, no modern HDR crispness.

### Model adaptation notes

- **gpt-image / DALL-E**: use the natural-language version as-is.
- **Midjourney**: condense to comma phrases; append `--ar 4:3 --style raw`.
- **Stable Diffusion / Flux**: tag-style from the structured fields; move the AVOID
  block into the negative prompt.

## 5. Consistency notes

- The system is **1-bit honesty**: every border 1px black, every shadow hard, every
  glyph bitmap. One soft element (a blurred shadow, an antialiased font) breaks the
  whole illusion — treat crispness as the load-bearing token.
- Color is rationed: `{colors.accent-play}` appears exactly once (play), and
  `{colors.accent-pink}` exactly once. Don't spread the accents.
- The pink page field and the pink button are siblings (#F5D2D2 / #F6D5D5) — if you
  transplant the window onto another brand, re-tokenize BOTH together, and swap
  `{colors.accent-play}` for the destination's single cool accent.
- **IP guardrail**: the Poolsuite wordmark and pixel-icon artwork are brand assets.
  The reconstruction prompt deliberately uses placeholder branding and self-drawn
  glyphs; keep it that way for anything public.

## 6. Confidence & open questions

| Aspect | Confidence | Why |
|---|---|---|
| Targeting | ✅ | DOM selector, exact bounding box |
| Structure | ✅ | outerHTML captured |
| Colors | ✅ | extracted + pixel-sampled, classes cross-checked |
| Shadows/bevels | ✅ | verbatim from live CSS |
| Typography mapping | ⚠️ | faces declared in CSS; per-block usage visually inferred |
| Playing state | ⚠️ | captured stopped; marquee inferred from DOM |
| Hover states | ❓ | none observed — likely intentional (OS metaphor) |
| LIVE badge colors | ⚠️ | element too small for reliable sampling |

**Open questions**: does the screen have a poster/fallback frame when the stream is
down (we caught dithered static — possibly the designed fallback, possibly a paused
state)? Do the window's resize handles render custom chrome at larger sizes?

> **Prompt fidelity note**: a generative image prompt is a high-fidelity
> *description*, not a guarantee of reproduction. Expect to iterate 2-4 generations;
> the PALETTE and AVOID blocks are the strongest levers.
