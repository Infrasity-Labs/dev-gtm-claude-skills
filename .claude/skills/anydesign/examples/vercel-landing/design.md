---
version: anydesign-1
name: Vercel landing (vercel.com)
source: https://vercel.com/
captured_at: 2026-05-18
description: |
  Near-monochrome editorial surface from Vercel's Geist design system. White background,
  near-black text (#171717), black primary buttons. The brand statement is the multi-stop
  AI gradient (orange-to-teal) wrapping the Vercel triangle in the hero. Every other
  surface is restrained — the gradient is the one place where the brand admits marketing
  function and quarantines it. Polarity-flipped section bands provide rhythm without
  shadow. Full Geist token map extracted live (808 CSS custom properties).

colors:
  primary: "#171717"
  surface: "#FFFFFF"
  surface-alt: "#FAFAFA"
  text-primary: "#171717"
  text-muted: "#4D4D4D"
  text-subtle: "#8F8F8F"
  border: "#EBEBEB"
  border-strong: "#A8A8A8"
  focus-blue: "#0070F7"
  success: "#28A948"
  marketing-bg: "#FAFBFC"
  geist-violet: "#7928CA"
  geist-cyan: "#50E3C2"
  highlight-pink: "#FF0080"

typography:
  display:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    letterSpacing: -0.02em
  h2:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 600
  body:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
  caption-mono:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400

spacing:
  base: 4px
  scale: [4, 8, 12, 16, 24, 32, 40, 64, 96, 128, 192, 256]

rounded:
  sm: 6px
  marketing: 8px
  modal: 12px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  tag-pill:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.primary}"
    rounded: "{rounded.marketing}"
    padding: 2px 6px
  top-navigation:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  footer-link-matrix:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
  mesh-gradient-hero-asset:
    description: "Multi-stop AI gradient at hero scale only — see Section 3.2"
  polarity-flipped-section-bands:
    description: "Rhythmic alternation of {colors.surface} and {colors.primary} as section background"
  dot-grid-hero-background-pattern:
    description: "4px radial-gradient dot raster overlaid on hero white surface"
  operational-status-indicator:
    backgroundColor: "{colors.success}"
    typography: "{typography.caption-mono}"
---

# Design Analysis — Vercel landing (vercel.com)

> Analysis generated with the `anydesign` skill on a **real** capture.
> Date: 2026-05-18
> Analysis emphasis: design system + reconstruction

---

## Source

- **Source type**: URL
- **Path / URL**: `https://vercel.com/`
- **Capture method**: HTML via `WebFetch`, CSS custom properties via
  `scripts/extract_css_vars.py` (808 vars across 6 stylesheets + 2 inline blocks),
  visual via `scripts/capture_site.py` (desktop screenshot 1440×900)
- **Detected limitations**: only desktop viewport captured; network-idle never settled
  (Vercel has constant background traffic) — the screenshot is what had rendered at
  T+45s, which is the full visible page

---

## TL;DR

Editorial, near-monochrome marketing surface from Vercel's Geist design system. White
background, near-black text (`#171717`), black primary buttons. The brand statement is
the multi-stop AI gradient (orange → yellow → green → teal) wrapping the Vercel triangle
in the hero — every other surface is restrained. 808 CSS custom properties extracted —
including a complete `ds-*` palette (10 shades × 8 hues, plus alpha variants), a
4px-based `geist-space-*` scale, and 7 named shadow tiers — give a high-confidence
reconstruction map.

---

## 1. Visual identity

### 1.1 Surface description

**Personality** (3-5 adjectives): editorial, monochromatic, precise, restrained,
typographically-led

**Mood**: confident and quiet. The page does not shout; the AI gradient does — once, in
the hero — and then disappears. The rest is whitespace and type.

**Detectable stylistic references**: this *is* the Geist aesthetic — the original
reference that "Linear-like / Vercel-like" descriptions point at. Influences: editorial
print typography, Swiss minimalism, "developer documentation" density patterns.

**Information density**: minimalist in the hero, **dense in the footer** (10-column link
matrix). The page swings from breath to library on purpose.

**Implicit positioning**: developers and platform engineers. The AI gradient is the
concession to a broader buyer audience (executives shopping AI tooling) but the
typography, density, and information hierarchy speak to people who deploy code.

**Distinctive visual moves**:
- Dot-grid background pattern in the hero (subtle 4-pixel dots) — a Geist signature.
- The Vercel triangle is overlaid on a soft multi-color gradient — the only chromatic
  moment on the page, so it carries enormous weight.
- Footer typography is all-caps small labels (`GET STARTED`, `BUILD`, `SCALE`) — feels
  like a print magazine masthead.

**Confidence**: ✅ high — consistent across the captured area.

### 1.2 Brand voice / Atmosphere

**Engineering quietude.** The product surface is restrained because the platform IS the
product — marketing's job is to not dilute what infrastructure already promises. Every
choice line ups: monochrome palette (no need to perform color when uptime performs
itself), sentence-case headlines (caps would shout, and the platform doesn't shout),
mono-spaced status indicator in the footer (the brand wants you to know it runs servers,
not campaigns), all-caps tiny footer labels (the masthead of a serious publication, not
a startup landing).

The mesh gradient is the **one place where the brand admits there's a marketing function
to perform** — and it's quarantined to the hero so it doesn't infect the rest of the
surface. The polarity-flipped bands further enforce the discipline: each band gets its
own polarity, recommits to monochrome, then moves on. There's no decorative drift, no
"let's add a small gradient accent here". The decoration is a tightly scoped admission,
not a vocabulary.

This belief — that infrastructure should be visible only at the moments that demand it —
is why a developer reading the page never feels sold-to. They feel *acknowledged as the
audience that doesn't need to be sold to*. Which is, in turn, what closes the deal.

### 1.3 The "ONE brand thing"

- **The thing**: the **mesh gradient** behind the Vercel triangle in the hero — multi-stop
  orange → yellow → green → teal, scoped to a single zone.
- **Why it carries the brand**: it's the ONLY chromatic moment on a near-monochrome
  surface. Remove it and the page reads as a generic developer-tool landing — well-typeset
  but indistinguishable from a dozen Linear-adjacent SaaS sites. The gradient *is* what
  makes someone glance at the page and know it's Vercel.
- **How everything else supports it**: the entire rest of the design is restrained
  *relative to* this one element. The palette is reduced to grays + ink so the gradient's
  saturation has nowhere to compete. Headlines are weight 600, not 700+, so they don't
  out-shout the visual moment. The mesh has the only saturated hues on the page; every
  other "color" is a feedback semantic (success green, error red) used in micro-contexts.
- **Where it appears (and where it deliberately doesn't)**: hero zone only. Never
  miniaturized to an icon. Never reduced to a single color. Never re-used as a decorative
  flourish elsewhere. The scoping is the discipline.

**Confidence**: ✅ high — this is widely understood as Vercel's signature move within
the design community, and the captured surface confirms the discipline.

---

## 2. Design System (tokens)

All values below are extracted from CSS custom properties on the live site. The
`--ds-*` prefix is Vercel's Design System namespace; `--geist-*` is the older Geist
namespace (still active for marketing-specific properties). They are **explicit tokens
defined by the authors** — therefore ✅ high confidence by default.

### 2.1 Colors

#### Core surface & text

| Token | Hex | Role | Confidence |
|---|---|---|---|
| `--ds-background-100` | `#FFFFFF` | Base surface | ✅ high |
| `--ds-background-200` | `#FAFAFA` | Subtle alternate surface | ✅ high |
| `--ds-gray-1000` | `#171717` | Primary text, primary button fill | ✅ high |
| `--ds-gray-900` | `#4D4D4D` | Secondary text | ✅ high |
| `--ds-gray-700` | `#8F8F8F` | Tertiary text, icons | ✅ high |
| `--ds-gray-500` | `#C9C9C9` | Subtle borders, disabled | ✅ high |
| `--ds-gray-200` | `#EBEBEB` | Light surface, dividers | ✅ high |
| `--ds-gray-100` | `#F2F2F2` | Section background tint | ✅ high |
| `--ds-black` | `#000000` | True black (rare, foregrounds & icons) | ✅ high |
| `--ds-white` | `#FFFFFF` | True white | ✅ high |

#### Alpha scale (transparent overlays)

Vercel ships a parallel **alpha** scale (`--ds-gray-alpha-100` through `-1000`) for
elements that need to sit on photographic or gradient backgrounds. Notable values:
`#0000000D` (5%) to `#000000E8` (91%). Use these — not the solid grays — when overlaying
the hero gradient.

#### Full DS palette (10 shades × 8 hues)

The design system ships a complete numeric scale (100-1000) per hue: `blue`, `red`,
`amber`, `green`, `teal`, `purple`, `pink`, plus the gray ramp above. Pulled verbatim
in `design-tokens.json`. On the landing itself only a small subset is actually used —
most are infrastructure for product UI elsewhere on the site. The ones in evidence on
the marketing surface:

| Token | Hex | Visible role |
|---|---|---|
| `--ds-blue-700` | `#0070F7` | Focus ring color (`--ds-focus-color`) |
| `--ds-green-700` | `#28A948` | Status indicator (system status dot in footer) |

#### Marketing-only accents

| Token | Hex | Use |
|---|---|---|
| `--geist-marketing-gray` | `#FAFBFC` | Marketing-page background tint |
| `--geist-violet` | `#7928CA` | Marketing decorative accent |
| `--geist-cyan` | `#50E3C2` | Marketing decorative accent (visible in hero gradient) |
| `--geist-highlight-pink` | `#FF0080` | Marketing emphasis (used sparingly) |

### 2.2 Typography

- **Sans family** (`--font-sans`): `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"`
- **Sans fallback chain** (`--font-sans-fallback`): `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", ...`
- **Mono family** (`--font-mono`): `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New"`
- **Custom**: `--font-pixel-square` references a Geist custom pixel font (`var(--font-geist-pixel-square)`) — likely loaded via `next/font` and not extractable from CSS vars alone

The actual rendered font on the live page is **Geist Sans** (Vercel's house typeface),
loaded via `next/font` — that's why it doesn't appear directly in `--font-sans` (which
holds the fallback chain).

**Weight scale** (`--font-weight-*`): 100, 300, 400, 500, 600, 700, 800

**Size scale** (`--text-*` Tailwind-aligned):

| Token | rem | px (approx) | Use |
|---|---|---|---|
| `--text-xs` | 0.75 | 12 | Small UI text |
| `--text-sm` | 0.875 | 14 | Body small, footer labels |
| `--text-base` | 1.0 | 16 | Body default |
| `--text-lg` | 1.125 | 18 | Lead paragraphs |
| `--text-xl` | 1.25 | 20 | Subheadings |
| `--text-2xl` | 1.5 | 24 | Section titles |
| `--text-3xl` | 1.875 | 30 | Block titles |
| `--text-5xl` | 3.0 | 48 | Hero title (display) |

**Fluid typography scale** (`--text-fluid-*`) — multiple `clamp()` tokens for responsive
type. Notable: `--text-fluid-32-80` ranging from 2rem to 5rem — likely the hero treatment
at larger viewports.

**Tracking** (`--tracking-*`): `tighter: -0.05em`, `tight: -0.025em`, `normal: 0em` —
heading-tight tracking declared.

**Leading** (`--leading-*`): `tight: 1.25`, `normal: 1.5`, `relaxed: 1.625`.

### 2.3 Spacing

**Base unit**: 4px (`--geist-space: 4px`).

**Geist spacing scale**:

| Token | px | Multiplier |
|---|---|---|
| `--geist-space` | 4 | 1× |
| `--geist-space-2x` | 8 | 2× |
| `--geist-space-3x` | 12 | 3× |
| `--geist-space-4x` | 16 | 4× |
| `--geist-space-6x` | 24 | 6× |
| `--geist-space-8x` | 32 | 8× |
| `--geist-space-10x` | 40 | 10× |
| `--geist-space-16x` | 64 | 16× |
| `--geist-space-24x` | 96 | 24× |
| `--geist-space-32x` | 128 | 32× |
| `--geist-space-48x` | 192 | 48× |
| `--geist-space-64x` | 256 | 64× |

**Negative variants** also declared (`--geist-space-*-negative`) for asymmetric layout
adjustments.

**Page widths**: `--geist-page-width: 1200px` (older Geist) and `--ds-page-width: 1400px`
(newer Design System) coexist — the marketing surface uses the 1200px container.

**Fluid spacing** (`--spacing-fluid-*`): responsive `clamp()` values for vertical rhythm
that scales with viewport.

### 2.4 Radii

| Token | Value | Use |
|---|---|---|
| `--geist-radius` | 6px | Default — buttons, inputs, tags |
| `--geist-marketing-radius` | 8px | Marketing-specific surfaces |
| `--code-block-radius` | 6px | Code blocks |
| `--modal-radius` | 12px | Modals |
| `--radius-3xl` | 1.5rem (24px) | Large container radius (Tailwind alignment) |

### 2.5 Elevation system

Vercel runs a **7-level stacked-shadow elevation** plus a parallel "inset hairline ring"
applied to most card surfaces. The system's signature move: every elevated surface
combines an inset 1px border (`--ds-shadow-border`) with one or more drop-shadow layers.
The brand never uses a single heavy drop.

| Level | Name | Treatment (verbatim CSS) | Use |
|---|---|---|---|
| 0 | Flat | No shadow, no border | Full-bleed hero band, dark polarity-flip bands |
| 1 | Hairline | `0 0 0 1px #00000014` inset | Default card chrome — universal "this is a card" cue |
| 2 | Subtle drop | `0px 1px 1px #0000000a` + hairline | Slight elevation, e.g. resting nav, light interactive states |
| 3 | Small drop | `0px 1px 2px #0000000a` + hairline | Buttons / tag surfaces (`--ds-shadow-xs`) |
| 4 | Medium | `0px 2px 2px #0000000a, 0px 8px 8px -8px #0000000a` + hairline | Standard cards, feature blocks (`--ds-shadow-medium`) |
| 5 | Large stack | `0px 2px 2px #0000000a, 0px 8px 16px -4px #0000000a` + hairline | Pricing cards, callout panels (`--ds-shadow-large`) |
| 6 | XL float | `0px 1px 1px #00000005, 0px 4px 8px -4px #0000000a, 0px 16px 24px -8px #0000000f` | Floating menus, dropdowns (`--ds-shadow-xl`) |
| 7 | Modal | `0px 1px 1px #00000005, 0px 8px 16px -4px #0000000a, 0px 24px 32px -8px #0000000f` | Modals, dialogs (`--ds-shadow-2xl`) |

Semantic compounds: `--ds-shadow-tooltip`, `--ds-shadow-menu`, `--ds-shadow-modal`,
`--ds-shadow-fullscreen` — each composes base shadows with `--ds-shadow-border-base`.

#### Decorative depth (non-functional)

Three distinct atmospheric devices establish depth without using the elevation system:

- **Polarity-flipped bands**: cycling between `--ds-background-100` (white) and
  `--ds-gray-1000` (near-black) as page surface creates section-depth by inversion.
  This is the chief band-rhythm cue. No shadow needed.
- **Hero mesh gradient**: orange → yellow → green → teal multi-stop gradient wrapping
  the Vercel triangle. Lives at hero scale only, never miniaturized to an icon, never
  reduced to a single color.
- **Dot-grid background pattern**: subtle 4px-spaced dot raster overlaid on the hero
  surface. Implemented as `background-image: radial-gradient(circle, rgba(0,0,0,0.04) 1px, transparent 1px)`
  with appropriate sizing.

The `--ds-shadow-border` (inset 1px) trick is itself worth noting: Vercel uses inset
shadows in place of real borders for sub-pixel crispness on Retina displays.

### 2.6 Borders

- Default: 1px solid (using `--ds-shadow-border` as a 1-pixel-inset shadow, not a real
  border — a Geist trick for subpixel control on Retina screens)
- Focus ring: `--ds-focus-ring: 0 0 0 2px var(--ds-background-100), 0 0 0 4px var(--ds-focus-color)`
  — a 2px white inner ring + 2px blue outer ring (`#0070F7`)

### 2.7 Motion

- `--ease-in`: `cubic-bezier(.4, 0, 1, 1)`
- `--ease-out`: `cubic-bezier(0, 0, .2, 1)`
- `--ease-in-out`: `cubic-bezier(.4, 0, .2, 1)`
- `--ds-motion-timing-swift`: `cubic-bezier(.175, .885, .32, 1.1)` *(slight overshoot)*
- `--default-transition-duration`: `0.15s`
- `--ds-motion-overlay-duration`: `0.3s`
- `--ds-motion-popover-duration`: `0.2s`

### 2.8 Accessibility quick-check

See companion `design-a11y.md`. Summary:
- Primary text on background: **17.93:1** — AAA ✅
- Muted text on background: **8.45:1** — AAA ✅
- CTA label on primary button: **17.93:1** — AAA ✅
- Focus blue on background: **4.51:1** — AA ✅, AAA ❌ *(adequate for focus rings)*

---

## 3. Components Inventory

### 3.1 Generic components

#### Button — primary (observed in hero CTA, "Ready to deploy?" CTA)

- **Fill**: `{colors.primary}` (#171717)
- **Label**: `{colors.surface}` (#FFFFFF)
- **Radius**: `{rounded.sm}` (6px)
- **Iconography**: optional left-icon (Vercel triangle on "Start Deploying")
- **Padding**: ~24px horizontal, ~10px vertical (visual estimate)
- **Confidence**: ✅ high — observed in 2+ contexts

#### Button — secondary

- **Fill**: `{colors.surface}` / transparent
- **Border**: 1px via inset shadow (Vercel's `--ds-shadow-border` trick)
- **Label**: `{colors.primary}` (#171717)
- **Radius**: `{rounded.sm}` (6px)
- **Observed as**: "Get a Demo" CTA
- **Confidence**: ✅ high

#### Button — ghost

- **No fill, no border**
- **Label**: `{colors.primary}`
- **Hover**: presumably underline / opacity shift (not captured in static)
- **Observed as**: "Talk to an Expert" text link
- **Confidence**: ⚠️ medium — only one instance captured

#### Tag — pill

- **Fill**: `{colors.surface-alt}` (very subtle gray)
- **Border**: 1px subtle inset shadow
- **Radius**: `{rounded.marketing}` (8px) or `{rounded.pill}` (both visible)
- **Padding**: tight (~6px horizontal, ~2px vertical)
- **Label**: `{colors.primary}`
- **Observed in**: "Scale your [Enterprise] without compromising [Security]"
- **Confidence**: ✅ high

#### Top navigation

- **Layout**: horizontal, left-aligned product/resources/solutions dropdowns, right-aligned
  Sign In / Log In / Sign Up
- **Background**: transparent over white surface
- **Items**: text-only with subtle hover (no visible bg change captured in static)
- **Confidence**: ⚠️ medium — dropdowns not exercised

#### Footer link matrix

- **Structure**: 10 columns × variable rows of categorized links
- **Section labels**: all-caps small (`{typography.body-sm}`), `{colors.text-subtle}`
- **Links**: regular case, `{colors.primary}`
- **Confidence**: ✅ high

### 3.2 Signature components

UI patterns that **are** the Vercel brand — the elements another developer-platform
brand would have to deliberately avoid copying.

#### Mesh-gradient hero asset

- **What it is**: a multi-stop AI-colored gradient (orange / yellow / green / teal) that
  wraps the Vercel triangle, occupying the hero zone.
- **Why it's signature**: the rest of the page is monochrome by deliberate restraint.
  The gradient is the ONLY chromatic moment — therefore it carries the entire brand
  voltage. Replicating Vercel without it loses the brand.
- **Composition**: layered SVG / CSS gradient (not extractable as a CSS variable —
  treat as an asset), centered, scales fluidly with the hero container, never tiles.
- **Where it appears**: hero only. Never miniaturized to icon, never reduced to a
  single color.
- **Confidence**: ✅ high

#### Polarity-flipped section bands

- **What it is**: rhythmic alternation between `--ds-background-100` (white) and
  `--ds-gray-1000` (near-black) surfaces as you scroll, with content recomposed onto
  each polarity.
- **Why it's signature**: it's how Vercel establishes "depth between sections" without
  shadow — a structural rhythm device, not just a styling choice. Linear and Stripe
  use related-but-distinct patterns; this specific cycle is Vercel's.
- **Composition**: full-bleed `background-color` swap per `<section>`; content tokens
  invert (`text-primary` ↔ `text-on-primary`); CTA button polarity also flips.
- **Where it appears**: throughout the marketing surface, ~every 2-3 sections.
- **Confidence**: ✅ high

#### Dot-grid hero background pattern

- **What it is**: subtle 4px-spaced dot raster overlaid on the hero white surface,
  visible behind the mesh gradient and triangle.
- **Why it's signature**: Geist marketing surfaces have used this pattern consistently
  for years — it's recognizable on sight as "a Vercel/Next.js property". Other dev
  platforms use grids or noise; Vercel uses the dot raster specifically.
- **Composition**: `background-image: radial-gradient(circle, rgba(0,0,0,~0.04) 1px, transparent 1px)`
  with appropriate spacing.
- **Where it appears**: hero zone only.
- **Confidence**: ✅ high

#### Operational status indicator (footer)

- **What it is**: a small green filled circle (`--ds-green-700` #28A948) with a
  mono-spaced text label, indicating system status.
- **Why it's signature**: developer-platform brands signal "platform health is part of
  the product surface". The mono caption next to the dot is the brand's way of saying
  "we run infrastructure, not marketing". Linear, Stripe, GitHub use related patterns;
  the mono caption is the Geist-specific signal.
- **Composition**: 8px circle + `--font-mono` caption + link to status page.
- **Where it appears**: footer.
- **Confidence**: ✅ high

---

## 4. Layout & Composition

### 4.1 Grid & containers

- **Container**: `--geist-page-width` 1200px (used on the marketing surface). A newer
  `--ds-page-width: 1400px` coexists — the marketing surface uses 1200 in this capture.
- **Horizontal padding**: ~24px on desktop
- **Vertical rhythm**: hero ≈ 600px tall; section blocks separated by `--geist-space-24x`
  (96px) approximately
- **Visual hierarchy**: typography size + weight do nearly all of the work. Color
  contrast is limited to the binary (black on white, occasionally muted).

### 4.2 Composition patterns

- **Hero**: centered, vertical stack (eyebrow / h1 / sub / CTA-pair / brand graphic).
  No split-hero pattern.
- **Polarity-flipped section bands** (see Signature components 3.2): alternating
  white / near-black surfaces structure the page rhythm.
- **"Develop with your favorite tools"**: three line-items with inline icons + mono
  technical labels.
- **"Scale your X without compromising Y"**: large typographic phrase with inline
  Tag/Pill components substituted for the X and Y nouns.
- **Final CTA**: split — primary CTA pair on the left, separate "Explore Enterprise"
  pull-out card on the right.
- **Footer**: dense 10-column link matrix + brand mark + status indicator (see
  Signature components).

### 4.3 Responsive behavior

#### Breakpoints

| Name | Width | Key changes |
|---|---|---|
| Mobile | < ~600px | ❓ low — not captured; footer's 10-col matrix likely collapses to accordion; nav to hamburger |
| Tablet | ~600–960px | ❓ low — not captured |
| Desktop | ~960–1280px | ✅ captured; full 10-col footer, horizontal nav, hero centered |
| Wide | > 1280px | ❓ low — container caps at `--geist-page-width` 1200; gutters absorb the rest |

**Confidence**: ❓ low — only desktop captured. The CSS declares fluid tokens
(`--text-fluid-*`, `--spacing-fluid-*`) suggesting viewport-aware scaling via `clamp()`
rather than discrete breakpoints, but live responsive behavior was not exercised.

To populate this table with real data, re-run:

```bash
python scripts/capture_site.py https://vercel.com/ \
    --viewports desktop,tablet,mobile
```

#### Touch targets

- **Primary CTA** ("Start Deploying"): ~40-44px tall in marketing context — at the WCAG
  AAA threshold (44 × 44). Nav-scale buttons likely shrink below 44px (would need
  mobile capture to confirm and validate against the 44 floor).
- **Tag/Pill** components: small (~24px tall) — interactive role uncertain (some look
  link-like, some decorative). Not safe to assume tap targets without mobile capture.

#### Collapsing strategy

- **Nav**: full horizontal product/resources/solutions dropdowns at desktop. Expected
  to collapse to hamburger overlay at mobile — not captured.
- **Hero**: vertical stack at desktop; should hold at all breakpoints (no split-hero).
- **Section bands**: full-bleed surface stays; content reflows from 1280px container
  to fluid width.
- **Footer 10-col matrix**: expected to drop to 5 → 2 → 1 columns; mono status
  indicator likely stays in place. Not captured.

### 4.4 Image behavior

- **Mesh-gradient hero asset** (see Signature components): inline SVG or canvas-painted,
  scales fluidly with the hero container, never crops, never tiles, never reduced to a
  single color or miniaturized.
- **Vercel triangle logo**: monochrome SVG. Appears in nav (small) and inside the hero
  gradient (larger). Same SVG, two scales.
- **Customer / framework logos** (visible in "Develop with your favorite tools"
  section): monochrome SVGs at consistent height (~24px); muted gray rendering, full
  color on hover plausibly (not captured).
- **No photography observed** in this capture. The marketing surface is purely
  typographic + iconic.

---

## 5. Reconstruction Notes

### Suggested stack

**Tailwind v4 + the Geist family of npm packages.**

Justification: the extracted CSS uses Tailwind utilities everywhere (`--tw-*` prefixed
properties confirm), plus a layered design-tokens system. The Geist tokens are published
by Vercel as `@vercel/geist` / available via `geist/font` for typography. For
reconstruction outside the Vercel ecosystem, treat the extracted token map as Tailwind
v4 `@theme` directives and load `Geist Sans` via `next/font/google` or `geist/font/sans`.

### Quick wins

- **Typography is one import.** `import { GeistSans } from 'geist/font/sans'` and the
  display surface is faithful.
- **Palette is a copy-paste.** Drop the 80+ DS palette tokens from `design-tokens.json`
  into a Tailwind v4 `@theme` block (or feed via Style Dictionary).
- **Buttons are trivial.** Black fill, white text, 6px radius, ~10/24 padding — three
  Tailwind utilities reproduce the primary CTA exactly.

### Tricky bits

- **The hero gradient is the brand.** Reproducing the orange → green → teal multi-stop
  gradient behind the Vercel triangle needs careful tuning; this is the one piece you
  cannot extract as a token (it's an SVG/CSS asset, not a CSS variable). Get a
  high-resolution capture of just that area and treat it as a custom asset.
- **Dot-grid background.** The hero has a subtle dot pattern overlay — not a CSS variable
  either, likely an SVG. Reproduce as `background-image: radial-gradient(circle, #0000000a 1px, transparent 1px)` with appropriate sizing.
- **Geist Sans is proprietary.** Free for personal/Vercel-deployed projects via the
  `geist/font` npm package, but licensing for non-Vercel commercial use deserves a check.
- **`--ds-shadow-border` instead of real borders.** Vercel uses inset shadows for
  1-pixel divisions, which renders crisper on Retina. Replicate the trick if pixel
  fidelity matters; otherwise standard borders are fine.
- **The custom `--font-pixel-square`** (Geist pixel square) is a display font used in
  rare moments not visible in this capture. If your reconstruction needs it, it'll
  require licensing the Geist font family fully.

### Implicit states to define

- Button hover (visible color shift expected; not captured statically)
- Button disabled
- Link hover (likely underline or opacity)
- Top-nav dropdown open state
- Input focus (use `--ds-focus-ring`)
- Status indicator other states (yellow = degraded, red = down)

### Confidence map

| Layer | Confidence | Why |
|---|---|---|
| Identity | ✅ high | Strong signals across hero + middle + footer |
| Colors | ✅ high | Extracted from declared CSS vars — not inferred |
| Typography | ✅ high (system), ⚠️ medium (rendered font) | Tokens declared; actual Geist Sans loaded via `next/font` (outside CSS scope) |
| Spacing | ✅ high | Full named scale declared |
| Shadows | ✅ high | 7-tier system declared verbatim |
| Components | ⚠️ medium | Captured 5-6 components; product surface (dashboard) would expose many more |
| Layout | ❓ low | Only desktop captured |
| Motion | ⚠️ medium | Easing/duration tokens declared but actual animation behavior not exercised |

---

## 6. Do's and Don'ts

Brand-specific usage rules grounded in observation. Use these to extend the system
without drifting from Vercel's voice.

### Do

- **Reserve `--ds-gray-1000` (#171717) for primary CTAs and primary text only.** Black
  ink is the conversion target — using it as a background fill or decorative element
  flattens the brand.
- **Layer multiple small drop-shadows + an inset hairline ring for elevation.** Vercel's
  cards are NEVER a single heavy drop — the stacked-shadow + ring trick is the brand's
  elevation signature.
- **Use `--geist-radius` (6px) for nav/UI controls and `--geist-marketing-radius` (8px)
  for marketing-scale surfaces.** The two scales coexist deliberately — pick the one
  that matches the context.
- **Cycle page surfaces in polarity-flipped bands** (`--ds-background-100` ↔
  `--ds-gray-1000`). The dark band IS the depth cue between sections — don't substitute
  shadow.
- **Set every code block, technical eyebrow, or status caption in `--font-mono`.** Mono
  is the brand's voice of "we run infrastructure".
- **Display type at weight 600, sentence-case, with negative tracking** (`--tracking-tight`
  or `--tracking-tighter`). Aggressive negative tracking is part of the typographic
  voice.
- **Use inset shadows (`--ds-shadow-border`) instead of real CSS borders** for crisp
  1-pixel divisions on Retina. Vercel's "card edge" sharpness depends on this.

### Don't

- **Don't introduce a sixth accent color.** The system runs on text + neutral grays +
  the four-pair mesh gradient. New accents (a "brand blue", a "secondary purple")
  flatten the voice instantly.
- **Don't miniaturize or single-color-reduce the mesh gradient.** It lives at hero
  scale only. Shrinking it to an icon or solid-fill flattens the brand's only chromatic
  moment.
- **Don't render display headlines in all-caps.** Sentence-case + tight tracking is
  the typographic contract.
- **Don't promote display weights above 600.** Vercel never goes 700+ for display
  type. The brand trusts size + tracking to set hierarchy, not heavy ink.
- **Don't use a single heavy drop-shadow** like `0 4px 8px rgba(0,0,0,0.2)`. Vercel's
  shadows are stacked small offsets; a single big drop reads as Material, not Geist.
- **Don't mix the marketing CTA shape with nav-scale radius on the same screen.** Pick
  6px or 8px and stay consistent within a context.
- **Don't set body paragraphs in `--font-mono`.** Mono is reserved for code, technical
  labels, status captions, and eyebrow text — never running prose.

---

## 7. Open Questions

- What are the **actual breakpoint values**? `--text-fluid-*` and `--spacing-fluid-*`
  suggest fluid scaling, not discrete breakpoints — but the layout collapses must
  happen somewhere. Need a mobile capture to confirm.
- Is there a **dark mode**? No `prefers-color-scheme` rules were observed in the captured
  CSS, but the alpha gray scale would support one cleanly.
- What are the **hover and focus states** for the primary button? Not exercised in a
  static capture.
- **`--ds-page-width: 1400px` vs `--geist-page-width: 1200px`** — both coexist. Is 1400
  the new container for newly designed sections (e.g., the AI Cloud surface) and 1200
  the legacy marketing default? Marketing surface used 1200 in this capture.
- The hero gradient asset — is it an SVG, a Canvas, or a layered CSS gradient? Not
  determinable from CSS vars; would need to inspect the rendered DOM.

---

## 8. Companion files

- [x] `design-tokens.json` — structured tokens in W3C DTCG format
      (`$value` / `$type`)
- [x] `design-a11y.md` — WCAG 2.1 contrast report
- [x] `capture.png` — desktop screenshot (downsized to 720×1095, 233 KB; original was 1440×2191)
- [ ] `capture.html` — rendered HTML not committed (regenerable, 520 KB)
- [ ] `css-vars-raw.json` — raw 808-var extraction not committed (regenerable, 224 KB)

---

*End of analysis. To go further: refine the analysis with a mobile capture, convert this
document into a Claude Code prompt for a from-scratch rebuild, or compare against another
landing in the Geist aesthetic family (Linear, Resend, Cal.com).*
