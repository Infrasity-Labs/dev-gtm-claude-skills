---
version: anydesign-1
name: Lumen Notes (fictional)
source: https://lumen.example/
captured_at: 2026-05-18
description: |
  Clinical developer-oriented dark-mode landing in the Linear/Vercel aesthetic family.
  Cool slate palette anchored on deep navy (#0F172A) with a single emerald accent
  (#10B981) applied with strict scarcity (CTA + wordmark only). Geometric sans typography
  (Inter declared in CSS). Two-tier shadow-less elevation system: depth via surface tone,
  not drop-shadow. 22 CSS custom properties extracted from a single linked stylesheet.

colors:
  bg: "#0F172A"
  surface-elevated: "#1E293B"
  text-primary: "#F8FAFC"
  text-muted: "#94A3B8"
  text-subtle: "#64748B"
  border: "#334155"
  border-strong: "#475569"
  accent: "#10B981"
  accent-hover: "#059669"
  success: "#22C55E"
  warning: "#F59E0B"
  danger: "#EF4444"

typography:
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 600
    letterSpacing: -0.02em
  h2:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  caption-mono:
    fontFamily: "ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400

spacing:
  base: 4px
  scale: [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]

rounded:
  sm: 6px
  md: 16px

components:
  button:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.bg}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
  card:
    backgroundColor: "{colors.surface-elevated}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.md}"
    padding: 32px
  input:
    backgroundColor: "{colors.bg}"
    border: "1px solid {colors.border}"
    focusRing: "2px solid {colors.border-strong}"
    rounded: "{rounded.sm}"
  badge:
    rounded: "{rounded.sm}"
    typography: "{typography.caption-mono}"
---

# Design Analysis — Lumen Notes (fictional)

> Analysis generated with the `anydesign` skill.
> Date: 2026-05-18
> Analysis emphasis: reconstruction + design system

---

## Source

- **Source type**: URL
- **Path / URL**: `https://lumen.example/` *(fictional, for documentation purposes)*
- **Capture method**: HTML via `WebFetch` + CSS custom properties via
  `scripts/extract_css_vars.py`
- **Detected limitations**: only desktop layout observed; no dark mode toggle visible in
  the captured HTML; mobile breakpoints not exercised

---

## TL;DR

Clinical, developer-oriented landing in the Linear/Vercel aesthetic family. Cool neutral
palette anchored on a deep slate background (`#0F172A`) with a single emerald accent
(`#10B981`); generous spacing on an 8px grid; geometric sans (Inter declared in CSS). The
22 extracted CSS custom properties give a high-confidence token map ready for
reconstruction.

---

## 1. Visual identity

### 1.1 Surface description

**Personality** (3-5 adjectives): clinical, calm, developer-targeted, restrained,
typographically-led

**Mood**: confident and quiet — not shouting, not playful. Reads as a tool, not a
consumer app.

**Detectable stylistic references**: strong Linear/Vercel/Anthropic-homepage family.
Dark surface with a single bright accent and lots of whitespace.

**Information density**: minimalist — the hero uses ~60% whitespace.

**Implicit positioning**: developers and technical knowledge workers. The accent is a
"command-line green" rather than a marketing blue.

**Confidence**: ✅ high — consistent signals across hero, features, and footer.

### 1.2 Brand voice / Atmosphere

**A tool for people who think in terminals.** The dark canvas is not a fashion choice —
it's the surface developers already stare at all day, presented as if to say "you don't
have to switch contexts to use this product." The emerald accent is the color of a
healthy build, of `npm install` finishing without warnings — the brand borrows that
positive-feedback green and asks: what if a note-taking tool felt the way passing tests
feel?

The restraint elsewhere protects this metaphor. There's no second accent because there
can't be — adding magenta or violet would break the "this is a healthy terminal" reading.
The mono caption beside the status indicator (a green dot in the footer) double-confirms
the positioning: this product talks to you in the same language as your CI pipeline.

### 1.3 The "ONE brand thing"

- **The thing**: the **emerald accent** (`--color-accent` #10B981) applied with extreme
  scarcity — primary CTAs and the wordmark only.
- **Why it carries the brand**: the dark canvas could belong to any dev tool; the green
  is what borrows the metaphor of "passing tests" and gives the brand its emotional
  voltage. Remove it and the page is just another dark-themed product page.
- **How everything else supports it**: the palette is otherwise slate-only. No second
  accent. No decorative gradients. Even the feedback colors (success, warning, danger)
  are reserved for explicit feedback contexts, never decorative.
- **Where it appears (and where it deliberately doesn't)**: primary CTA fills, logo
  wordmark, link hover state. Deliberately absent from body text, headings, borders,
  and decorative space — those stay slate.

**Confidence**: ✅ high — the scarcity rule is consistent across the captured surface.

---

## 2. Design System (tokens)

All values below were extracted from the site's CSS custom properties via
`scripts/extract_css_vars.py`. They are explicit tokens defined by the authors —
**not** inferred — and therefore carry ✅ high confidence by default.

### 2.1 Colors

| Token | Hex | Role | Where it appears | Confidence |
|---|---|---|---|---|
| `--color-bg` | `#0F172A` | Surface — base background | Body | ✅ high |
| `--color-surface-elevated` | `#1E293B` | Cards, feature blocks | Feature grid | ✅ high |
| `--color-text-primary` | `#F8FAFC` | Body text on dark | Body, headings | ✅ high |
| `--color-text-muted` | `#94A3B8` | Captions, metadata | Eyebrow text, labels | ✅ high |
| `--color-text-subtle` | `#64748B` | De-emphasized text | Footer links | ✅ high |
| `--color-border` | `#334155` | Subtle borders | Card outlines, dividers | ✅ high |
| `--color-border-strong` | `#475569` | Focus rings, emphasis | Input focus | ✅ high |
| `--color-accent` | `#10B981` | Primary CTA, accents | "Start free" button, logo | ✅ high |
| `--color-accent-hover` | `#059669` | CTA hover state | Hover on accent | ✅ high |
| `--color-success` | `#22C55E` | Feedback | Success badges | ✅ high |
| `--color-warning` | `#F59E0B` | Feedback | Warning badges | ✅ high |
| `--color-danger` | `#EF4444` | Feedback | Error badges | ✅ high |

### 2.2 Typography

- **Declared family**: `Inter, ui-sans-serif, system-ui, sans-serif` *(confidence: ✅ high — declared in CSS)*
- **Fallback chain**: `ui-sans-serif, system-ui, sans-serif`

**Observed scale:**

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `--font-size-display` | 60px | 600 | 1.1 | Hero title |
| `--font-size-h2` | 32px | 600 | 1.2 | Section titles |
| `--font-size-body` | 16px | 400 | 1.6 | Main text |

**Notable tracking**: `-0.02em` declared on display (typographic care signal).
**Weights used**: 400, 500, 600.

### 2.3 Spacing

- **Inferred base unit**: 4px (Tailwind-like scale; multiples observed: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128)
- **Declared tokens**: `--space-1` through `--space-16`
- **Consistency**: ✅ high — every margin/padding observed maps to a declared step

### 2.4 Radii

- `--radius-sm`: 6px (buttons, inputs, badges)
- `--radius-md`: 16px (cards) — Tailwind's `rounded-2xl` value, confirmed in CSS

### 2.5 Elevation system

Lumen Notes runs a deliberately **shadow-less elevation system** — depth is established
by surface tone, not drop-shadow.

| Level | Name | Treatment | Use |
|---|---|---|---|
| 0 | Flat | No shadow, no border | Body background (`--color-bg`) |
| 1 | Surface tint | `background: --color-surface-elevated` (#1E293B) + 1px border `--color-border` | Cards, feature blocks |

No further tiers are declared. The brand's elevation system is explicitly two-tier —
not because of capture limits but because it's the design choice.

**Confidence**: ⚠️ medium — hover states (which might use shadow) not visible in static capture.

#### Decorative depth (non-functional)

- **No atmospheric gradients, mesh effects, or patterns** observed in the captured
  surface. The dark canvas does the entire mood work alone.

### 2.6 Borders

- Default thickness: 1px
- Color: `--color-border` (`#334155`)
- Focus state: 2px ring in `--color-border-strong`

### 2.7 Accessibility quick-check

See companion `design-a11y.md`. Summary:
- `text-primary` on `bg`: **17.06:1** — AAA ✅
- `text-muted` on `bg`: **6.96:1** — AA ✅, AAA large ✅ (just under AAA normal)
- `accent` on `bg`: **7.04:1** — AAA ✅
- `text-primary` on `accent` (anti-pattern): **2.42:1** — fails all. **Do not place white text on the accent button** — the implementation correctly puts `bg` (dark) on `accent` (7.04:1 ✅).

---

## 3. Components Inventory

### 3.1 Generic components

#### Button
- **Variants**: primary (solid `{colors.accent}`), ghost (transparent + `{colors.border-strong}`)
- **Sizes**: md (40px tall)
- **Visible states**: default, hover (color shift to `{colors.accent-hover}`)
- **Padding**: 24px horizontal, 10px vertical
- **Radius**: `{rounded.sm}` (6px)
- **Confidence**: ✅ high

#### Card
- **Variants**: single — feature card with icon + title + body
- **Background**: `{colors.surface-elevated}`
- **Border**: 1px solid `{colors.border}`
- **Radius**: `{rounded.md}` (16px)
- **Padding**: 32px
- **Confidence**: ✅ high

#### Input
- **Variants**: single text input (email signup in footer)
- **Visible states**: empty, focus (2px ring in `{colors.border-strong}`)
- **Border**: 1px solid `{colors.border}`
- **Confidence**: ⚠️ medium — only one input observed

#### Badge
- **Variants**: success, warning, danger
- **Style**: pill (`{rounded.sm}`), solid background of the relevant semantic color
- **Confidence**: ⚠️ medium — observed in component examples, not in active marketing copy

### 3.2 Signature components

**No signature components detected** — the synthetic source uses standard UI primitives
only. A "real" Lumen Notes product surface would likely have signature elements (e.g.,
a distinctive note-card pattern, a signature command palette), but the captured marketing
landing operates with generic components only. Don't fabricate signatures that aren't
there.

---

## 4. Layout & Composition

### 4.1 Grid & containers

- **Container max-width**: ~1200px, horizontal padding 24px on desktop
- **Vertical rhythm**: sections separated by ~96px (`--space-16` × 1.5)
- **Visual hierarchy**: typographic size + color contrast (white on dark) — no
  oversaturated color used

### 4.2 Composition patterns

- **Hero**: centered single-column vertical stack
- **Mid-page**: 3-column feature grid with cards
- **Footer**: sitemap + email capture, 2-column structure

### 4.3 Responsive behavior

#### Breakpoints

| Name | Width | Key changes |
|---|---|---|
| Mobile | < 768px | ❓ low — not captured |
| Tablet/Desktop | ≥ 768px | ✅ captured (desktop only); 3-up grid renders |

**Confidence**: ❓ low — only desktop captured. CSS declares `--breakpoint-md: 768px`
and `--breakpoint-lg: 1024px` but their use was not exercised in the captured surface.
Recommended:

```bash
python scripts/capture_site.py https://lumen.example/ \
    --viewports desktop,tablet,mobile
```

#### Touch targets

- **Buttons**: ~40px tall — just under the WCAG AAA 44px floor on the long edge.
  If the design needs strict AAA, bump button height to 44px on mobile contexts.
- **Email input** (footer): height not measurable from static capture.

#### Collapsing strategy

- **3-up feature grid**: expected to collapse to 1-up at mobile — not captured.
- **Hero**: vertical stack at all breakpoints (no split-hero variant).
- **Footer**: 2-col structure likely stacks at mobile — not captured.

### 4.4 Image behavior

- **Icons only**: feature cards use small line icons (likely Lucide based on stroke
  weight). No photography, no decorative graphics observed.
- **No images at hero scale.** The brand carries its mood through type + color +
  surface tone alone.

---

## 5. Reconstruction Notes

### Suggested stack

**Tailwind + a custom Tailwind config that mirrors the extracted tokens.**

Justification: the CSS class names visible in the HTML (`bg-slate-900`, `text-zinc-100`,
`rounded-2xl`) are direct Tailwind utilities. Wire the extracted custom properties into
`tailwind.config.js` (Tailwind v4 reads CSS variables natively).

### Quick wins

- Palette and typography cover ~80% of the look. Drop the CSS variables into a `:root`
  block, set Inter via `next/font` or `<link>`, and the surface is immediately faithful.
- Buttons with `bg-emerald-500 text-slate-900 rounded-md px-6 py-2.5` reproduce the
  primary CTA.

### Tricky bits

- Whatever interaction / motion exists is not visible in static capture. Expect to design
  micro-interactions from scratch (subtle scale or color transitions on hover).
- The single accent color does heavy lifting — design hover/disabled/focus states
  carefully to avoid breaking the calm.
- Card hover state was not observed; the design likely has one. Define before shipping.

### Implicit states to define

- Button hover (visible)
- Button disabled
- Card hover
- Input error
- Form submission loading
- Empty states for the feature grid (if it ever has zero items)

### Confidence map

| Layer | Confidence | Why |
|---|---|---|
| Identity | ✅ high | Clear signals, consistent palette |
| Colors | ✅ high | Extracted from CSS variables, not inferred |
| Typography | ✅ high | Family declared in CSS, scale declared in CSS |
| Spacing | ✅ high | Token scale declared in CSS |
| Components | ⚠️ medium | Only 4 components observed in source |
| Layout | ❓ low | Only desktop captured |

---

## 6. Do's and Don'ts

### Do

- **Reserve `--color-accent` (#10B981) for primary CTAs and the brand wordmark.** The
  emerald accent is the only chromatic moment — using it elsewhere flattens the brand.
- **Place dark text (`--color-bg`) on the accent button, never white.** Real contrast
  testing (see `design-a11y.md`) confirms only the dark-on-accent direction reaches AAA.
- **Use surface tone, not shadow, for elevation.** The shadow-less two-tier system
  (`--color-bg` → `--color-surface-elevated`) is the brand's depth language.
- **Set every code/technical label in `--font-mono`.** The mono face is part of the
  developer-tool positioning.
- **Use `--radius-sm` (6px) for interactive controls and `--radius-md` (16px) for
  cards.** The two scales coexist intentionally.

### Don't

- **Don't put white text on the accent button.** Contrast ratio is 2.42:1 — fails all
  WCAG levels.
- **Don't introduce a second accent color.** The brand operates on neutrals + one
  emerald + feedback semantics. New accents flatten the calm.
- **Don't add drop-shadows to cards.** The system is deliberately shadow-less — drop
  shadows would break the editorial calm.
- **Don't override headings with weights above 600.** Display weight ceiling is
  semibold.
- **Don't promote secondary text (`--color-text-muted`) to body weight.** The hierarchy
  is built on tone, not weight.

*Note: this synthetic example only generates 5 of each (vs the typical 7) because the
captured surface is intentionally minimal. A real product surface would surface more
rules.*

---

## 7. Open Questions

- Does the product have a dark/light mode toggle? Only dark was observed; no
  `prefers-color-scheme` rules in the captured CSS.
- Are there Button variants beyond primary and ghost (e.g., destructive)?
- What's the mobile navigation pattern (hamburger? bottom sheet?)
- Is there a documented motion system, or are transitions ad-hoc?
- The CSS declares `--breakpoint-md` and `--breakpoint-lg` but no rules were observed
  using them in the capture — confirm whether they're used elsewhere.

---

## 8. Companion files

- [x] `design-tokens.json` — structured tokens in W3C DTCG format
      (`$value`/`$type`), ready for Style Dictionary / Figma Variables / Tokens Studio
- [x] `design-a11y.md` — WCAG 2.1 contrast report for the four key text/surface
      combinations
- [ ] No screenshot bundled — HTML+CSS extraction was sufficient

---

*End of analysis. If you want to deepen any section, convert this into a prompt for Claude
Code, or analyze another source to compare, let me know.*
