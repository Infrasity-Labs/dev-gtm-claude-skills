# Output Template — The design.md template

This is the **base** template of the `design.md` file the skill generates. Use it as the
output contract. Adapt the depth of each section based on the user's emphasis
(reconstruction / mood / system), but **don't remove sections** unless explicitly empty
due to lack of info — in which case, say so.

---

## Template

The design.md has **two halves**: a YAML frontmatter block fenced by `---` that holds
structured tokens an agent can parse mechanically, followed by a markdown body of prose
sections that turns those tokens into language an agent (or a human) can act on.

The frontmatter is intentionally a subset of what the companion `design-tokens.json`
contains. The JSON is the canonical DTCG-compliant source (with `$value`/`$type`,
confidence metadata, etc.) — the YAML is the inline-readable shorthand the body
references via `{token.refs}`.

```markdown
---
version: anydesign-1
name: [Site / file / reference name]
source: [the URL, file path, or Figma link analyzed]
captured_at: YYYY-MM-DD
description: |
  [2-3 sentence atmosphere paragraph that anchors the brand voice. NOT a tagline —
  a dense summary an agent can read before parsing the rest. Mirrors the TL;DR but
  scoped to brand atmosphere, not actionable insights.]

colors:
  primary: "#171717"
  surface: "#FFFFFF"
  text-primary: "#171717"
  text-muted: "#4D4D4D"
  border: "#EBEBEB"
  accent: "#10B981"
  # ... use semantic names, not numeric scales. Mirror the design-tokens.json palette
  # but flatten to one-level for inline reference. Full scale lives in the JSON.

typography:
  display:
    fontFamily: "Geist, Inter, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    letterSpacing: -0.02em
  h2:
    fontFamily: "Geist, Inter, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
  body:
    fontFamily: "Geist, Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  caption-mono:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400
  # ... role-named styles, not h1/h2/h3 HTML tags

spacing:
  base: 4px
  scale: [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]

rounded:
  sm: 6px
  md: 8px
  lg: 12px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
  card:
    backgroundColor: "{colors.surface}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.lg}"
    padding: 32px
  # ... every component named here MUST have a matching prose entry in Section 3.
  # The lint script enforces 1:1.
---

# Design Analysis — [Site / file / reference name]

> Analysis generated with the `anydesign` skill.
> Date: YYYY-MM-DD
> Analysis emphasis: [reconstruction | mood | design system | mixed]

---

## Source

- **Source type**: [local image | URL | Figma | combination]
- **Path / URL**: `<the concrete source>`
- **Capture method**: [direct vision | HTML via WebFetch + CSS vars extraction | Playwright multi-viewport screenshot | Figma MCP]
- **Detected limitations**: [if any, e.g., "only desktop material visible, no responsive"]

---

## TL;DR

[2-3 sentences. Visual personality + what's distinctive + one actionable insight.]

*Example: Clinical productivity-oriented design, in the aesthetic line of Linear/Vercel.
Restricted palette in cool neutrals with a single blue accent (#3B82F6). Geometric sans
typography with negative tracking on headings, suggesting Inter or Geist.*

---

## 1. Visual identity

### 1.1 Surface description

**Personality** (3-5 adjectives): [adjectives]

**Mood**: [what emotion it conveys, briefly]

**Detectable stylistic references**: [if you recognize patterns, e.g., "Linear-like aesthetic",
"current web brutalism", "Apple homepage editorial"]

**Information density**: [minimalist | balanced | dense | saturated]

**Implicit positioning**: [who this design speaks to — devs, enterprise, creatives, etc.]

**Confidence**: [✅ high | ⚠️ medium | ❓ low]

### 1.2 Brand voice / Atmosphere

[2-3 dense paragraphs answering: **what does this design BELIEVE about its audience, and
how does every aesthetic choice line up with that belief?** This is not the surface
description (Section 1.1) — this is the *philosophical why* behind the surface.

Concrete vs vague: "developer-targeted" is Identity (vague, surface). "The product
surface is restrained because the platform IS the product — marketing's job is to not
dilute what infrastructure already promises" is Brand Voice (specific, philosophical,
forces a coherent set of follow-on choices).

Avoid generic copywriting voice ("approachable yet premium", "modern and friendly").
Force yourself to write something the brand would *agree* describes them but that a
generic designer couldn't have written without seeing this specific design.]

### 1.3 The "ONE brand thing"

The single element that does the brand work alone — the gesture that, if removed,
collapses the brand identity. Everything else is restrained *relative to* this one
thing.

- **The thing**: [color / typography move / decorative element / geometric move / etc.]
- **Why it carries the brand**: [what would be lost if you removed or weakened it]
- **How everything else supports it**: [what's deliberately restrained to make this
  stand out]
- **Where it appears (and where it deliberately doesn't)**: [scoping discipline — is
  it allowed only in the hero? Only on CTAs? Never in product UI?]

*Confidence*: [✅ | ⚠️ | ❓]

*Most strong design systems have ONE such thing. If you can't identify it, the system
is either very young, deliberately neutral (like internal admin tools), or you don't
have enough material yet. Say so explicitly — don't invent one.*

---

## 2. Design System (tokens)

### 2.1 Colors

| Token | Hex | Role | Where it appears | Confidence |
|---|---|---|---|---|
| `primary` | `#3B82F6` | Main action, links | CTA buttons, nav links | ✅ high |
| `surface` | `#FFFFFF` | Base background | Body | ✅ high |
| `text-primary` | `#111827` | Main text | Body, headings | ✅ high |
| `text-muted` | `#6B7280` | Secondary text | Captions, labels | ⚠️ medium |
| ... | | | | |

[If dark mode exists, add equivalent table below.]

### 2.2 Typography

- **Detected family**: `[Inter | Geist | etc.]` *(confidence: ⚠️ medium — visually inferred)*
- **Suggested fallback**: `system-ui, sans-serif`

**Observed scale:**

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `display` | 64px | 600 | 1.1 | Hero title |
| `h1` | 48px | 600 | 1.15 | Section titles |
| `h2` | 32px | 600 | 1.2 | Subsection |
| `body` | 16px | 400 | 1.6 | Main text |
| `body-sm` | 14px | 400 | 1.5 | Captions, metadata |

**Notable tracking**: -0.02em on display and h1 (typographic care signal)

### 2.3 Spacing

- **Inferred base unit**: 4px (Tailwind-like scale)
- **Observable multiples**: 4, 8, 12, 16, 24, 32, 48, 64, 96
- **Consistency**: ✅ high — systematic pattern

### 2.4 Radii

- `sm`: 6px (buttons, inputs)
- `md`: 12px (cards)
- `full`: 9999px (avatars, badges)

### 2.5 Elevation system

Levels declared 0-N where Level 0 is "flat / no chrome" and higher numbers mean greater
elevation. Each level has a **treatment** (the CSS recipe) and a **use** (where it appears
on the surface).

| Level | Name | Treatment | Use |
|---|---|---|---|
| 0 | Flat | No shadow, no border | Full-bleed bands, hero |
| 1 | Hairline | `1px solid #E5E7EB` | Default card chrome |
| 2 | Subtle drop | `0 1px 2px rgba(0,0,0,0.04)` + hairline | Hovered cards |
| 3 | Stack | `0 2px 4px + 0 4px 8px rgba(0,0,0,0.05)` | Floating menus, popovers |
| 4 | Modal | Multi-stop stack `0 8px 16px + 0 24px 32px` | Dialogs, fullscreen overlays |

*If the system uses only one or two tiers, **say so explicitly** — many brands deliberately
avoid heavy elevation. Don't fabricate a 5-tier system that isn't there.*

#### Decorative depth (non-functional)

Atmospheric effects that establish visual depth without serving UI elevation:

- **Polarity flips**: light/dark band alternation between page sections (depth by surface
  inversion, not shadow)
- **Atmospheric gradients**: hero meshes, ambient washes — typically scoped to a single
  area, never miniaturized
- **Background patterns**: dot grids, noise, subtle textures applied as `background-image`

*Omit this subsection if the design has no decorative depth cues.*

### 2.6 Borders

- Base color: `#E5E7EB` (light gray)
- Thickness: 1px
- Focus states: 2px ring in `primary` with opacity

### 2.7 Accessibility quick-check

See companion `design-a11y.md`. Summary:
- `text-primary` on `surface`: **17.06:1** — AAA ✅
- `accent` on `surface`: **6.96:1** — AA ✅, AAA large ✅

*Omit this subsection if fewer than 2 colors with clear text/surface relationships were
captured.*

---

## 3. Components Inventory

### 3.1 Generic components

Standard UI primitives that any system has (Button, Input, Card, Badge, etc.). For each:

#### Button
- **Variants**: primary (bg-primary), ghost (transparent + border)
- **Observed sizes**: md (40px tall)
- **Visible states**: default
- **Padding**: ~24px horizontal, 10px vertical
- **Radius**: 6px
- **Confidence**: ✅ high

#### Input
- **Variants**: single text
- **Visible states**: empty, focus
- **Border**: 1px solid border, primary focus ring
- **Confidence**: ⚠️ medium — only saw one case

[...continue with each observed generic component]

### 3.2 Signature components

UI patterns that are uniquely the brand's — the "if you see this, you know which product
this is" elements. These are the components a competitor would have to deliberately avoid
copying.

#### [Component name — e.g., "Mesh-gradient hero"]
- **What it is**: brief description of the pattern
- **Why it's signature**: what makes it distinct vs. a generic equivalent
- **Composition**: how it's built (tokens used, layered effects)
- **Where it appears**: hero only, every page, etc.
- **Confidence**: [✅ | ⚠️ | ❓]

*If the design uses only generic patterns and has no clearly distinctive UI motif, write:
"No signature components detected — system uses standard UI primitives." Don't force it.*

---

## 4. Layout & Composition

### 4.1 Grid & containers

- **Inferable grid**: container max-width ~1280px, horizontal padding 24px on desktop
- **Vertical rhythm**: sections separated by ~96px
- **Visual hierarchy**: established by typographic size and color contrast (not by
  oversaturated color)

### 4.2 Composition patterns

- Centered hero
- 3-column feature grid
- Dense footer with 5-column link matrix

### 4.3 Responsive behavior

#### Breakpoints

| Name | Width | Key changes |
|---|---|---|
| Mobile | < 600px | Nav collapses to hamburger; 3-up grids drop to 1-up; hero stacks |
| Tablet | 600–959px | 3-up grids drop to 2-up; nav still horizontal |
| Desktop | 960–1279px | Full 3-up grids; sticky sidebar |
| Wide | ≥ 1280px | Content caps at 1280px; gutters absorb the rest |

*If only one viewport was captured, write: "Only desktop material captured — breakpoints
inferred from fluid CSS / clamp() functions where present, otherwise marked ❓ low." Pair
with the `--viewports` capture command in Open Questions.*

#### Touch targets

- Primary CTAs: ≥ 44 × 44px (WCAG AAA threshold)
- Form inputs: ~48px height
- *Note any patterns that fall below 44px and need adjustment.*

#### Collapsing strategy

- **Nav**: full horizontal at desktop → hamburger overlay at mobile
- **Grids**: 3-up → 2-up → 1-up at the breakpoints above; cards keep `{rounded.md}` shape
- **Hero**: stacks vertically at all breakpoints (no split-hero pattern)

### 4.4 Image behavior

How each kind of image is treated. List one per image category observed:

- **Decorative gradient** (hero): inline SVG or canvas, scales fluidly with container, never
  crops, never tiles
- **Brand logo strip**: monochrome SVGs at consistent ~24px height
- **Product mockups**: dark-mode mockup, treated as image at layout level
- **Photography**: aspect ratio (16:9), placeholder treatment (skeleton, blur, dominant
  color), lazy-load behavior
- **Icons**: source set (Lucide, Heroicons, custom), stroke/fill convention

*Omit this subsection if the source has no images — but say so explicitly.*

---

## 5. Reconstruction Notes

### Suggested stack

**[Tailwind | Tailwind + shadcn/ui | vanilla CSS | other]**

Justification: [why — observed classes, recognized patterns, simplicity of the case]

### Quick wins

- [What's direct to replicate with basic tokens]
- [Example: palette and typography cover 80% of the look]

### Tricky bits

- [What needs special care]
- [Animations, custom fonts, non-trivial layouts, invisible states]

### Implicit states to define

Probably exist but weren't captured — define before implementing:
- Button hover states
- Visible focus
- Loading states
- Empty states
- Input error states

### Confidence map

| Layer | Confidence | Why |
|---|---|---|
| Identity | ✅ high | Sufficient material, clear patterns |
| Colors | ✅ high | Hex extracted directly |
| Typography | ⚠️ medium | Family visually inferred |
| Spacing | ✅ high | Verifiable consistent pattern |
| Components | ⚠️ medium | Partial catalog observed |
| Layout | ❓ low | Only desktop material |

---

## 6. Do's and Don'ts

Explicit usage rules an AI agent (or human) should follow when extending this system.
Each rule is **specific to this design**, not generic UX advice. Aim for 5-7 of each. Cite
tokens explicitly (e.g., `text-primary`, `space-6x`) wherever possible.

### Do

- **Reserve `primary` for primary CTAs.** Don't use it for decorative or background fills.
- **Use `radius-sm` (6px) for nav-scale interactive elements and `radius-md` (12px) for
  cards.** The two scales coexist deliberately — don't mix.
- **Set every headline in semibold (600) with negative tracking (-0.02em).** Aggressive
  tracking is part of the voice.
- **Use the mesh gradient at hero scale only.** Never miniaturize it to an icon, never
  reduce to a single color.
- **Layer multiple small shadows for elevation.** The brand's elevation system avoids
  single heavy drops.
- **Cycle surface tones in alternating bands** (`surface` → `surface-elevated` → `surface`)
  rather than using a single background.
- **Set every code/technical label in the monospaced face.** Mono is the voice of the
  platform.

### Don't

- **Don't introduce a sixth accent color.** The brand operates with text + neutral + one
  accent + the feedback semantics. New accents flatten the voice.
- **Don't render headlines in all-caps.** Sentence-case + tight tracking is non-negotiable.
- **Don't use a single heavy drop-shadow on cards.** The system uses stacked, layered
  shadows.
- **Don't promote font weights above 600 for display type.** The brand's weight ceiling is
  semibold.
- **Don't pair pill radius (full-rounded) and `radius-sm` (6px) on the same screen.** Pick
  a scale and stay there.
- **Don't set body paragraphs in the monospaced face.** Mono is reserved for code +
  technical labels.

*If you can't generate at least 3 Do's and 3 Don'ts grounded in observed patterns, write:
"Insufficient evidence to derive brand-specific usage rules — only the token-level rules
captured above apply." Don't fill with generic UX advice.*

---

## 7. Open Questions

[List of things you COULDN'T determine that need user input or more material]

- Does the site have dark mode? Saw no indications.
- Are there Button variants besides primary and ghost?
- Is the typography Inter or Geist? Need to see CSS to confirm.
- What are the exact breakpoints? Only saw desktop — recommend
  `python scripts/capture_site.py <URL> --viewports desktop,tablet,mobile`.

*If no open questions, justify it: "Material sufficient for complete reconstruction."*

---

## 8. Companion files

- [ ] `design-tokens.json` — structured tokens in W3C DTCG format (`$value`/`$type`),
      ready for Style Dictionary, Figma Variables, Tokens Studio
- [ ] `design-a11y.md` — WCAG 2.1 contrast report for the extracted color pairs
      (emit when at least two colors with clear text/surface relationships were captured)
- [ ] `design-screenshot.png` — capture used (if generated by Playwright or MCP);
      `-desktop` / `-tablet` / `-mobile` suffixes when multi-viewport

---

*End of analysis. If you want to deepen any section, convert this into a prompt for Claude
Code, v0, Lovable, or another generation tool, or analyze another source to compare, let
me know.*
```

---

## Notes for filling the template

### Adaptation based on emphasis

- **If emphasis = reconstruction** → Sections 5, 6 more detailed; Section 1 briefer
- **If emphasis = mood/reference** → Section 1 more detailed with rich vocabulary;
  Sections 2-3 briefer
- **If emphasis = design system** → Sections 2-3 very detailed, plus always generate
  `design-tokens.json`

### Confidence marker rules

- ✅ high: directly seen, without significant inference
- ⚠️ medium: well-grounded inference but could be wrong
- ❓ low: reasonable speculation, say so openly

### What's never missing

1. **Source** with complete source info
2. **TL;DR** of 2-3 sentences
3. **Confidence map** at the end of Reconstruction Notes
4. **Open Questions** (or justification of their absence)
5. **Do's and Don'ts** (or justification — see Section 6 note)

### What can be missing (with explicit justification)

- Token sub-sections if the source doesn't support them (e.g., static image without
  detectable typography info → omit the weights sub-section, say so)
- 3.2 Signature components if the design uses only generic patterns
- 4.3 Responsive behavior breakpoint table if only one viewport was captured (still
  include the section, populate with the "only desktop" note)
- 4.4 Image behavior if the source has no images
- 2.5 Decorative depth subsection if there are no atmospheric effects
- 2.7 Accessibility quick-check if fewer than 2 color pairs available

### Token reference syntax

In the prose body, reference frontmatter tokens using `{...}` syntax:

| Form | Example | Renders as |
|---|---|---|
| Color | `` `{colors.primary}` `` | A reference an agent can resolve to `#171717` |
| Typography | `` `{typography.display}` `` | A reference resolving to the full display style block |
| Spacing | `` `{spacing.scale[4]}` `` or `` `{spacing.base}` `` | Indexed or named |
| Radius | `` `{rounded.sm}` `` | Resolves to `6px` |
| Component | `` `{components.button-primary}` `` | Composed reference |

**Convention**: in prose, write the ref followed by the literal value in parens for
human readability — `{colors.primary}` (#171717). The ref is for machines and
refactoring; the value is for the reader who's scanning.

**Why this matters**: if Vercel later moves `--ds-gray-1000` from `#171717` to `#0F0F0F`,
you change one line in the YAML frontmatter and every reference in the prose
re-resolves. The `design.md` becomes refactor-safe.

### Lint enforcement

Run `python scripts/lint_design_md.py design.md` to verify:

- **Frontmatter is valid YAML** with required fields (`version`, `name`, `source`)
- **Every `{token.ref}` in the body resolves** to something defined in the frontmatter
- **Every component named in YAML `components:` has a matching prose entry** in
  Section 3 (the 1:1 rule)
- **Section 6 Do's and Don'ts is non-empty** or carries the explicit abstain
  justification
- **Open Questions section is non-empty** or carries the "material sufficient"
  justification

The lint is advisory, not strict — it returns exit code 1 on failures so it can wire
into pre-commit hooks if desired.
