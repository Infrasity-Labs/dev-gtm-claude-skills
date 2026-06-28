# Analysis Framework — The 5 analysis layers

This reference defines how to analyze the captured material. Consult it when you start Step 3
of the main workflow.

Analysis goes **from general to specific**, from intent to detail. Don't skip layers: jumping
from "mood" to "tokens" without passing through "system" loses the why.

---

## Layer 1 — Visual identity

**Guiding question:** *What does this design want to be?*

Before measuring, feel. This layer is interpretive but not vague: every statement is justified
with concrete observations.

### What to identify

- **Personality** (3-5 adjectives): professional / playful / minimalist / brutalist / corporate
  / artisanal / technical / warm / clinical / editorial / experimental
- **Stylistic references** (if you recognize them): "Linear-like aesthetic", "Stripe-like",
  "Anthropic homepage", "Notion-ish", "Apple editorial", "new Gumroad-style web brutalism"
- **Mood**: what emotion does it convey? Confidence? Energy? Calm? Urgency?
- **Information density**: minimalist / balanced / dense / saturated
- **Implicit positioning**: who does it speak to? Developers? Enterprise? End consumers?
  Creatives?

### How to justify (no vagueness)

❌ Bad: "Modern and professional design"
✅ Good: "Professional/clinical. Geometric sans typography, restricted palette of
white/black/single blue, lots of whitespace. Reminiscent of Linear or Vercel."

### Common trap

Don't confuse "modern" with analysis. "Modern" means nothing — everything current looks
"modern". Talk about **what makes** it look current: variable typography, generous spacing,
cool neutrals, implicit micro-interactions, etc.

### Brand voice / Atmosphere (Section 1.2 of the output)

After capturing the surface description, write **2-3 dense paragraphs of philosophical
prose**. Not copywriting voice ("approachable yet premium"). Not Identity adjectives
("clean, modern"). Something that forces a coherent set of follow-on design choices.

The test: imagine a careful viewer reading your prose. Would they say "yes, this is
exactly what this brand believes, and now I see why every choice they made follows from
it"? If yes, you're there. If they'd say "this could describe any tech company", rewrite.

Working examples:
- Vercel → "Engineering quietude. The product surface is restrained because the platform
  IS the product — marketing's job is to not dilute what infrastructure already promises."
- Linear → "Software made by people who deploy software. The interface is so dense with
  affordances because the audience reads code, not marketing copy."
- Apple → "Permission to feel things in public about hardware. Every aesthetic move
  protects the user's right to consider the object beautiful without irony."

Each forces specific design choices. Vercel can't have a playful illustration; Linear
can't have spacious whitespace; Apple can't have sarcastic copy. The Brand Voice IS the
constraint set.

### The "ONE brand thing" (Section 1.3 of the output)

The single element that does the brand work alone. The thing you'd remove last, because
removing it collapses the identity.

Heuristic: walk through the captured surface and ask, *if I greyscaled / generic'd
everything else, what one element would still scream "this is X"?* That's the ONE thing.

Common shapes:
- **A single chromatic moment** in an otherwise neutral palette (Vercel's mesh gradient,
  Stripe's gradient ribbons, Linear's purple-blue accent)
- **A typographic gesture** that nothing else does (Apple's huge display weight + tight
  tracking, Söhne on Anthropic, Geist's specific tracking)
- **A geometric move** (Tesla's wide condensed sans, Notion's emoji-as-iconography)
- **A decoration scoping rule** (Cal.com's brand uses gradients ONLY for hero +
  empty-state illustrations — never inline)

Document:
1. **What the thing is** (concrete: hex / typeface / asset).
2. **Why it carries the brand** (what would be lost without it).
3. **How everything else supports it** (the restraint of the surroundings is what makes
   the ONE thing readable).
4. **Where it appears AND where it deliberately doesn't** (scoping discipline — Vercel's
   mesh gradient lives at hero scale only).

If you can't identify a ONE thing: say so. Some systems are deliberately neutral (admin
dashboards, white-label products). Don't fabricate.

---

## Layer 2 — System (tokens)

**Guiding question:** *Which system-level decisions repeat?*

Here you move from feeling to measurement. Every observed token is documented with its
concrete value.

### Sub-layers

**2.1 Colors**
- List observable colors with hex codes (no approximations)
- Assign inferred semantic role: `primary`, `secondary`, `accent`, `surface`,
  `surface-elevated`, `text-primary`, `text-muted`, `border`, `success`, `warning`, `error`
- Detect **extended palette** if present (e.g., shades of the same color used as a scale)
- If dark mode is visible, document both modes

**2.2 Typography**
- Detected family/families. If you can identify it by name, do so. If not, describe it
  ("geometric condensed sans", "transitional serif", "mono with ligatures")
- Observable scale: which sizes repeat? (h1, h2, body, caption, etc.) in px or rem
- Weights used: 300 / 400 / 500 / 600 / 700
- Approximate line-height per level
- Notable tracking (letter-spacing): if present, note it

**2.3 Spacing**
- Infer the **base unit** (4px, 8px, 16px are most common)
- List observable multiples: 4, 8, 12, 16, 24, 32, 48, 64...
- Mark if it seems consistent (✅) or erratic (⚠️)

**2.4 Radii**
- List observable radii in components: `0` (square), `4px`, `8px`, `12px`, `16px`,
  `pill` (full-rounded)
- Detect if there's a system (e.g., "everything uses 8px except buttons at 6px")

**2.5 Elevation system**

Don't just list "shadow values". Diagnose the elevation system:

- **Identify tiers explicitly**. Name each tier Level 0-N where Level 0 is "flat / no
  chrome". Each tier carries a treatment (the CSS recipe) and a use case (where it
  appears).
- **Detect the brand's elevation philosophy**: stacked shadows (multiple small offsets)?
  Single drop? Inset border-as-elevation (the Vercel trick)? Flat-only?
- **If the system uses only one or two tiers, say so** — many brands deliberately avoid
  heavy elevation. Don't fabricate a 5-tier system that isn't there.

*Sub-section — Decorative depth*: separate atmospheric / non-functional depth cues from
the UI elevation system. Look for:
- **Polarity-flipped bands** (light/dark section alternation as depth-by-surface-inversion)
- **Atmospheric gradients** (hero meshes, ambient color washes — usually scoped to one area)
- **Background patterns** (dot grids, noise, subtle textures)

These are not "shadows" but they ARE how the brand creates depth. Document them.

**2.6 Borders**
- Default thickness, color, style
- Differentiated border states (hover, focus)

**2.7 Accessibility signals** *(optional but recommended when tokens are extracted)*
- Once you have at least two color tokens (e.g., `text-primary` and `surface`, `primary` and
  `surface`), run a contrast check on the key pairs.
- Use `python scripts/check_contrast.py --pair "#111827,#FFFFFF" --pair "#3B82F6,#FFFFFF"`
  to get WCAG 2.1 ratios as a markdown table.
- Thresholds to flag:
  - **AA normal text**: ≥ 4.5:1
  - **AA large text** (18pt+ or 14pt+ bold): ≥ 3:1
  - **AAA normal**: ≥ 7:1
  - **AAA large**: ≥ 4.5:1
- Emit the output as a companion `design-a11y.md` and reference it from Section 7 of the
  `design.md`.

### For extracting tokens with rigor

Consult `token-extraction.md` for detailed methodology on inferring tokens from pixels and
on the DTCG output format.

### Token references in prose

Every design.md has a YAML frontmatter block holding the token map. In the prose body of
the analysis, **reference frontmatter tokens via `{token.ref}` syntax** followed by the
literal value in parens for readability:

- Instead of: *"Fill: #171717"*
- Write: *"Fill: `{colors.primary}` (#171717)"*

This makes the design.md refactor-safe (changing one YAML value re-resolves every
reference) and machine-parseable. The `lint_design_md.py` script verifies every ref
resolves and that every component named in YAML has a matching prose entry.

Apply this discipline consistently across Sections 2, 3, and 4 — the token tables
themselves don't need refs (they ARE the source), but every prose mention of a value
should ref-then-value.

---

## Layer 3 — Components

**Guiding question:** *Which reusable pieces form this design?*

Inventory the visible components, with their variants and states.

### Typical catalog to look for

- **Buttons**: variants (primary, secondary, ghost, destructive, icon-only), sizes, states
  (default, hover if visible, disabled if visible)
- **Inputs**: text, search, textarea, select, checkbox, radio, toggle. States (empty, filled,
  error, disabled)
- **Cards**: is there a card pattern? What does it contain? Are there variants (simple card,
  card with header, card with cover image)
- **Navigation**: navbar, sidebar, breadcrumbs, tabs, pagination
- **Feedback**: alerts, toasts, badges, tags, banners, modals
- **Typography as component**: headings, eyebrow text, captions, links
- **Lists and tables**: row style, separators, headers
- **Avatars and media**: image treatment, icons (inferable set: Lucide, Heroicons, Phosphor,
  Material Icons)

### Suggested format

For each component:
```
### Button
- Detected variants: primary (solid blue), ghost (transparent with border)
- Sizes: md (40px tall), sm (32px tall)
- Visible states: default, disabled (reduced opacity)
- Notes: generous horizontal padding (~24px), 6px radius
- Confidence: ✅ high (seen in multiple contexts)
```

### Generic vs signature components

Split the inventory into two groups in the output:

- **3.1 Generic components** — standard UI primitives any system would have (Button,
  Input, Card, Badge, Modal, Toast). Catalog these as above.
- **3.2 Signature components** — UI patterns that are uniquely this brand's. The "if you
  see this, you know which product this is" elements. Examples: Vercel's mesh-gradient
  hero, Linear's command palette, Stripe's gradient code-card, Apple's animated product
  hero, Anthropic's structured doc blockquote.

For each signature component, capture: what it is, why it's signature (vs a generic
equivalent), how it's composed (tokens + layered effects), where it appears.

If the design uses only generic patterns and has no distinctive UI motif, **say so
explicitly**: "No signature components detected — system uses standard UI primitives."
Don't force one.

### Common trap

Don't invent variants. If you only saw one button, say "1 variant observed" — don't assume
"primary, secondary and tertiary" exist because "most design systems have that". Stick to what
you observed.

Same rule for signature components: if the marketing surface is just a hero + feature
grid + footer with no distinctive moves, don't invent a "signature card pattern" — the
honest read is "no signatures detected".

---

## Layer 4 — Layout and composition

**Guiding question:** *How is space organized?*

This layer has four sub-sections in the output (4.1 Grid & containers, 4.2 Composition
patterns, 4.3 Responsive behavior, 4.4 Image behavior). Each one is independent — capture
what you can for each, mark gaps honestly.

### 4.1 Grid & containers

- **Inferable grid**: 12 columns? 16? Other? Detectable container max-width?
- **Vertical rhythm**: is there consistent spacing between sections?
- **Visual hierarchy**: how are primaries vs secondaries established? (size, weight, color,
  position, space)
- **Density per zone**: dense zones (dashboards, tables) vs spacious zones (heroes,
  marketing sections)

### 4.2 Composition patterns

Name the recognizable patterns: hero, feature-grid, alternating-band sections, card list,
sidebar layout, centered single-column, split-hero, full-bleed image + offset text, etc.

### 4.3 Responsive behavior

Produce three pieces (each as its own subsection in the output):

- **Breakpoints table**: Mobile / Tablet / Desktop / Wide with width ranges and key
  layout changes per tier. If you only have desktop material, populate the table with
  "❓ low confidence — only desktop captured" and recommend the user re-run with
  `python scripts/capture_site.py <URL> --viewports desktop,tablet,mobile`.
- **Touch targets**: WCAG asks for ≥ 44×44px on interactive elements. Measure the
  observable primary CTAs and inputs. Flag anything below.
- **Collapsing strategy**: per pattern (nav, grid, hero, sidebar), how it adapts. "3-up
  grid drops to 2-up at tablet, 1-up at mobile" is the level of specificity wanted.

If the CSS contains `clamp()` / fluid values, that's evidence of a fluid (rather than
discrete-breakpoint) approach — note it.

### 4.4 Image behavior

Categorize images by role and document each:

- **Decorative gradient / mesh / hero asset**: how it's rendered (SVG, canvas, CSS),
  how it scales, whether it ever tiles or crops
- **Brand logo strips**: monochrome vs color, height convention, alignment
- **Product mockups / screenshots**: aspect ratio, treatment (dark mode, browser chrome,
  device frame)
- **Photography**: aspect ratios, placeholder treatment (skeleton, blur, dominant color),
  lazy-load behavior
- **Icons**: source set if recognizable (Lucide, Heroicons, Phosphor, custom), stroke
  vs fill convention, size scale

If the source has no images, **say so explicitly** in the output.

### Common trap

Don't confuse "centered" with "good layout". Note real decisions: does it use asymmetric
whitespace? Does it align to baseline? Does it have a clear focal point?

Don't invent a 4-tier breakpoint system if you only have desktop. Document what you
captured; flag the rest.

---

## Layer 5 — Reconstruction

**Guiding question:** *If you had to rebuild it, what would you need?*

This layer is **prescriptive**, not descriptive. You're talking to a human or AI who will
build something similar.

### Sub-sections

**5.1 Suggested stack**
- Vanilla HTML/CSS? Tailwind? Tailwind + shadcn/ui? Material UI? Something more exotic?
- Justify with evidence: if you saw classes like `flex items-center gap-4`, it's Tailwind. If
  you saw `MuiButton-root`, it's MUI. If there are no clues, suggest Tailwind as a reasonable
  default.

**5.2 Quick wins (easy to replicate)**
- Things that with basic tokens and components come out the same
- Example: "Palette and typography are direct. Buttons with `bg-blue-600 rounded-md px-4 py-2`
  cover the pattern."

**5.3 Tricky bits (what needs care)**
- Animations, transitions, effects not visible in static but seemingly present
- Custom typefaces that require licensing
- Non-trivial layouts (masonry, asymmetric grid)
- States you didn't see but logically exist (hover, loading, empty)

**5.4 Responsive coverage gotcha**
- If you only have desktop material, **say so explicitly** in Open Questions and recommend
  the user rerun with `python scripts/capture_site.py <URL> --viewports desktop,tablet,mobile`
  before committing to breakpoint assumptions.
- Marketing landings often have very different mobile structures (sticky CTAs, collapsed nav,
  reordered sections) that you cannot infer from desktop alone.

**5.5 Confidence map**
General summary of how confident you are in each layer:

| Layer | Confidence | Why |
|---|---|---|
| Identity | ✅ high | Clear material |
| Tokens — colors | ✅ high | Hex extracted directly |
| Tokens — typography | ⚠️ medium | Family identified but partial weights |
| Components | ⚠️ medium | Only saw 3 of a probably larger catalog |
| Layout | ❓ low | Only desktop material, no responsive info |

---

## Layer 6 — Brand rules (Do's and Don'ts)

**Guiding question:** *What would an AI agent extending this system need to be told
explicitly so it doesn't drift?*

This layer is **prescriptive and brand-specific**. It's the most useful piece of the
output for downstream AI builders (v0, Lovable, Cursor) because it codifies the
"unwritten rules" that tokens alone can't capture.

### Rules of generation

- **Aim for 5-7 Do's and 5-7 Don'ts**. Fewer reads incomplete; more dilutes.
- **Each rule must be specific to this design**, not generic UX advice. "Use the primary
  color for primary CTAs" is generic and useless. "Reserve `primary` (#171717) for the
  conversion target — never as a card background" is specific and useful.
- **Cite tokens explicitly** wherever possible: `{colors.primary}`, `{space-6x}`,
  `{typography.display-lg}`. This makes the rules auditable against the token table.
- **Anchor rules in observation**. Each rule should trace back to something you saw in
  the source. "Don't promote font weights above 600 for display type" is grounded if you
  observed all displays at 600. If you didn't observe it, don't claim it.

### Categories to draw rules from

- **Color discipline**: which colors are reserved for which roles? Which combinations are
  forbidden? How many accents max?
- **Typography discipline**: weight ceilings, case (sentence vs all-caps), tracking rules,
  mono-for-code-only rules
- **Elevation discipline**: stacked vs single-drop, inset borders vs solid borders
- **Radius/shape discipline**: pill scale vs sharp scale, can they mix?
- **Spacing discipline**: section rhythm, band alternation patterns
- **Composition discipline**: hero scale restrictions, decorative element scoping (e.g.,
  "gradient lives at hero scale only — never miniaturize")
- **Component composition**: which tokens MUST be used together (e.g.,
  `button-primary` always pairs `text-on-primary`)

### When to abstain

If the source is shallow (single screenshot of a generic landing) or the system is too
implicit, you may not have enough evidence for 5-7 of each. In that case write:

> "Insufficient evidence to derive brand-specific usage rules — only the token-level
> rules captured in Section 2 apply. Re-run with more material (multiple pages, mobile
> capture, component examples) to extract richer guidance."

Don't pad with generic UX best practices. That breaks the contract.

### Common trap

The temptation is to write Do's that sound smart ("Do maintain hierarchy through scale,
not color"). Resist this unless you can point to a specific observation that justifies
it. The best Do's and Don'ts are the ones a careful viewer says "huh, I noticed that
too" — they're observation made explicit.

---

## Art Direction Patterns — QA pass before finalizing

After completing Layers 1-6, **do not close the analysis yet**. Run this checklist as a
QA pass — these are patterns shallow analysis routinely misses. Each one prompts:
"Did I notice this? If yes, did I document it in the right section? If no, am I
certain it's absent, or did I just not look?"

These patterns cut across Layers 1-6 — that's why they live in a separate pass. They
are what separates a "lists what I see" report from a "diagnoses how it works" report.

### Surface-rhythm patterns

- [ ] **Polarity-flipped section bands** — does the page alternate light ↔ dark surfaces
  as you scroll, with content inverting onto each polarity? If yes → document in
  Section 2.5 (Decorative depth) AND Section 4.2 (Composition patterns).
- [ ] **Atmospheric gradient scoping** — is there a gradient/mesh/wash that lives in
  ONE specific zone (typically the hero) and is forbidden everywhere else? If yes →
  Section 2.5 (Decorative depth) and call out the scoping discipline.
- [ ] **Density alternation** — does the page swing between minimalist zones (heroes,
  marketing intros) and dense zones (footer link matrices, pricing tables, feature
  comparison grids)? Document the rhythm.

### Token coexistence patterns

- [ ] **Pill scale coexistence** — does the system use two distinct radii deliberately
  (e.g., 6px for nav-scale controls + 100px pill for marketing CTAs)? Are they ever
  mixed on the same screen, or kept in separate contexts? Document AS A RULE in
  Section 6 Do's/Don'ts.
- [ ] **Mono usage scope** — is the monospaced face reserved for code only, or also
  used for captions / eyebrow text / status labels? If "platform brand uses mono for
  status indicators", that's signal → Section 6.
- [ ] **Weight ceiling** — does the display type cap at a specific weight (often 600)
  while the rest of the system has heavier weights available but unused? If yes,
  that's a deliberate brand discipline → Section 6 Don'ts.
- [ ] **Tracking discipline** — is there a clear convention (e.g., negative tracking
  on display, neutral on body)? Document in Section 2.2 and reinforce in Section 6.

### Color discipline patterns

- [ ] **Color "voltage"** — is there exactly ONE chromatic moment in an otherwise
  neutral palette? (This is often THE "ONE brand thing".) Where does it appear?
  Where is it deliberately absent?
- [ ] **Alpha overlay scale** — is there a parallel alpha-only scale alongside the
  solid color scale (for overlays on photography / gradients)? If yes, that signals
  a mature system → Section 2.1.
- [ ] **Feedback colors restraint** — are success/warning/error colors used only in
  feedback contexts, or do they leak into decorative use? Restraint = signal.

### Elevation discipline patterns

- [ ] **Stacked vs single-drop shadows** — does the system layer multiple small drops
  (Geist-style) or use single heavy drops (Material-style)? If stacked → Section 6 Do.
- [ ] **Inset-shadow-as-border** — does the system use inset 1px shadows in place of
  real CSS borders for sub-pixel crispness on Retina? Subtle but signal.
- [ ] **Surface-tone vs shadow for elevation** — does the system establish depth via
  surface color change (dark theme cards on darker background) instead of shadows?
  If yes → say so in Section 2.5.

### Composition discipline patterns

- [ ] **Split-hero vs centered-hero** — which is canonical for the brand? Mixing both
  on the same surface is usually a smell.
- [ ] **Asymmetric whitespace** — does the layout use deliberate asymmetric whitespace,
  or is it symmetric/centered throughout? This is a strong stylistic marker.
- [ ] **Image treatment consistency** — do all images share treatment rules (grayscale
  → color on hover, fixed aspect, consistent placeholder)? Inconsistency = either
  legacy debt or deliberate variety.

### How to use this checklist

- After finishing Layers 1-6, walk through every item.
- If a pattern is **present** → ensure it's documented in the right section, and
  consider whether it should also appear as a rule in Section 6 Do's/Don'ts.
- If a pattern is **absent** → ask whether you're confident in its absence (not just
  "didn't see it"). For some brands the absence is the signal (e.g., "no atmospheric
  gradients — the design earns its mood through type and surface alone").
- If a pattern is **ambiguous** → list as an Open Question in Section 7.

**Don't pad the design.md by mentioning every checklist item that isn't there.** Only
surface absences when they ARE diagnostic ("no shadows — flat-by-design"). Otherwise
just confirm the present patterns are covered.

---

## How to use all this

It's not a mechanical checklist. It's a **scaffold** so the analysis doesn't stay shallow.
You pass through the 6 layers in order, giving more depth to those the material supports
and to the emphasis the user requested. Then you run the Art Direction Patterns QA pass.

If the user said "I want mood/reference", Layer 1 weighs more. If they said "extract
tokens", Layer 2. If they said "reconstruction", Layers 5-6. But **all layers are
covered**, even briefly, and **the QA pass is non-negotiable**.
