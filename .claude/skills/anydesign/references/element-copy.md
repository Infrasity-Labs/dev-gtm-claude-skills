# Element Copy — the "copy element" mode

This reference defines **element mode**: instead of analyzing a full page/file and producing
a system-level `design.md`, the skill zooms into **one visual element** (a navbar, a card,
a 3D illustration, a hero graphic) and produces a focused `element.md` that lets the user
replicate *that element* with maximum fidelity.

Consult this file when the user's intent is element-scoped (see activation rules in
SKILL.md). The mode reuses the capture flows from `references/capture-flows.md` — only the
scope and the output contract change.

---

## The core decision: what KIND of element is it?

Every element falls into one of three kinds, and the kind determines the output:

| Kind | What it is | Output |
|---|---|---|
| **`code`** | Reconstructable with DOM + CSS: navbars, cards, buttons, hero text blocks, footers, tables, pricing sections, badges | Focused spec + code reconstruction prompt |
| **`asset`** | Raster/complex art that CSS can't reasonably express: 3D illustrations, photography, mascots, hand-drawn art, complex textures, logo artwork | **Token-grounded generative image prompt** |
| **`hybrid`** | A code container with embedded asset(s): a card containing a 3D illustration, a hero with a photographic background | Code spec + nested asset prompt(s) |

**Classification heuristic** — ask: *"could a competent frontend dev rebuild this with
HTML/CSS/SVG primitives and stock fonts, without any image file?"*

- Yes → `code`. Gradients, borders, shadows, text, simple geometric SVG all count as code.
- No, it needs an image file → `asset`.
- The container is code but it embeds something that needs an image file → `hybrid`.

When unsure, prefer `hybrid` and say so — splitting the element into its code shell and
asset core is more useful than misclassifying the whole thing.

---

## Workflow (element mode)

### Step E1 — Identify the target

The user points at the element in one of these ways. Resolve to the most precise
targeting available:

| Source | Targeting methods (most → least precise) |
|---|---|
| **URL** | CSS selector given by user → selector you infer from the fetched HTML → description + cropped Playwright capture |
| **Local image** | The whole image IS the element → or the user describes a region ("the illustration on the right") and you analyze that region |
| **Figma** | `node-id` in the URL → node you locate via `get_metadata` |

If the description is ambiguous ("the card" on a page with 12 cards), ask **one** clarifying
question — element mode is precision work; guessing the wrong target wastes the whole run.

### Step E2 — Capture, element-scoped

- **URL + selector available**: run the element capture —

  ```bash
  python scripts/capture_site.py <URL> --selector "<css-selector>" --output ./element.png
  ```

  This screenshots **only the element's bounding box** and saves its `outerHTML`
  (instead of the full page). The outerHTML gives you real classes, inline styles, and
  structure — treat it like Step 2.2 of the main flow, scoped down.

- **URL, no workable selector**: full capture, then analyze the element region visually.
  Say explicitly that targeting was visual, not DOM-based (affects confidence).

- **Image**: direct vision. If the element is an `asset`, also run
  `python scripts/extract_colors.py <crop>` — the dominant hexes feed the PALETTE block
  of the image prompt (this is what makes the prompt token-grounded, not impressionistic).

- **Figma**: `get_metadata` → `get_design_context` on the node, `get_screenshot` for
  visual reference. Exported fills/images inside the node usually signal `asset` or
  `hybrid`.

### Step E3 — Classify and analyze

Classify (`code` / `asset` / `hybrid`) using the heuristic above, then run a **scoped**
version of the layered analysis: you still extract tokens (Layer 2) and identity cues
(Layer 1), but only those the element actually exhibits. Do NOT pad with page-level
analysis — that's what full mode is for.

One page-level exception: **capture the element's immediate context** (what surface it
sits on, adjacent spacing, the parent's background color). An element copied without its
context contract gets rebuilt looking alien.

### Step E4 — Generate `element.md`

Use the template below. Then deliver per Step 5 of the main workflow.
`lint_design_md.py` does **not** apply to `element.md` — it validates the full
`design.md` contract only.

**Delivery format (asset/hybrid kinds).** Before writing the image prompt, determine
how the user will USE the asset — it changes the BACKGROUND/INTEGRATION block:

| Format | When | Prompt consequence |
|---|---|---|
| `scene` | Regenerating the composition/mood (hero art, full illustration) | Background baked in, edges blend into the destination surface tone |
| `isolated` | Dropping the asset into their own web/design (most common) | **Single subject, transparent background (PNG with alpha)**, generous margin, no cast shadow on the ground unless requested |

If the user says "for my website", "as a PNG", "to place over X", default to
`isolated`. If ambiguous, generate the scene prompt and include the isolated variant
as a one-line alternative.

**Isolated prompts have two failure modes — write them defensively:**

1. **Prose transparency is unreliable.** Chat UIs frequently ignore "transparent
   background" written in the prompt and paint a backdrop anyway; the dependable
   route is the API parameter (gpt-image: `background: "transparent"`). Midjourney
   has no true alpha at all; SD/Flux varies by pipeline.
2. **Style worlds summon backdrops and cast.** Atmosphere words ("ambient fill",
   "night mood", color-named light) make the model paint that atmosphere, and
   style vocabularies that imply a universe make it add extra characters/props.

So in an `isolated` prompt: lead with the isolation directive ("an isolated asset
on a fully transparent background: one single X — nothing else in the frame, no
scenery, no other characters, no props, no floor, no ground shadow"), strip all
world/atmosphere words (keep lighting neutral: "soft studio key"), and close the
AVOID block with "no background of any kind".

**Reliable fallback** when transparency still fails: prompt the subject on a solid
flat chroma background in a color absent from the PALETTE (e.g. pure #00FF00,
"perfectly uniform, no gradient, no vignette"), then chroma-key it to alpha in
post (Pillow tolerance-based removal works well on matte renders).

---

## The `element.md` template

Same two-half structure as `design.md`: YAML frontmatter for machines, prose body for
agents/humans. Sections marked with a kind tag appear only for that kind.

```markdown
---
version: anydesign-element-1
name: [element name, e.g., "Vercel navbar" / "Hero 3D glass blob"]
source: [URL / file path / Figma link]
captured_at: YYYY-MM-DD
kind: code | asset | hybrid
target:
  description: "[how the user pointed at it, e.g., 'the main navbar']"
  selector: "header.navbar"        # only when DOM-targeted
  region: "[crop description or Figma node-id]"   # when applicable

# kind: code | hybrid — local token subset (only tokens this element uses)
colors:
  surface: "#FFFFFF"
  text-primary: "#171717"
typography:
  nav-link:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
spacing-used: [8, 16, 24]
rounded-used: { pill: 9999px }

# kind: asset | hybrid — extracted palette feeding the image prompt
palette:
  - "#5B6CFF"   # dominant, ~40% area
  - "#0E0E10"   # background field
  - "#F2B8FF"   # rim highlight
---

# Element — [name]

> Generated with the `anydesign` skill (element mode).
> Kind: [code | asset | hybrid] · Date: YYYY-MM-DD

## Source & target

- **Source**: [URL / image / Figma + link or path]
- **Targeting**: [selector / node-id / visual region] — [DOM-based ✅ | visual ⚠️]
- **Context**: [what the element sits on — parent surface color, adjacent spacing]

## 1. What this element is

[2-3 sentences: what it is, what job it does in the parent design, and the one thing
that makes it distinctive. Element-scoped — not a page analysis.]

## 2. Spec  `(kind: code | hybrid)`

[Scoped token tables + structure. Same rigor as design.md Layer 2/3: real hex, real px,
confidence per row. Include:]

- **Structure**: the DOM/layout skeleton (from outerHTML when available)
- **Tokens**: colors / typography / spacing / radii / shadows the element uses
- **States**: observed + implicit (hover, focus, active — mark unobserved ones ❓)
- **Behavior**: sticky? collapses on mobile? animates on entry?

## 3. Reconstruction prompt  `(kind: code | hybrid)`

[A ready-to-paste prompt for a code agent (Claude Code, v0, Lovable) that rebuilds JUST
this element: stack suggestion, the spec inlined, the context contract ("renders on
{colors.surface}"), and explicit don'ts.]

## 4. Generative image prompt  `(kind: asset | hybrid)`

### Canonical prompt (structured)

SUBJECT: [the thing itself, concrete and specific — "a translucent glass blob with
  three soft protrusions", not "an abstract shape"]
STYLE / MEDIUM: [3D render / flat vector / photograph / hand-drawn — plus finish:
  "matte clay render", "glossy C4D-style", "grainy risograph print"]
COMPOSITION & CAMERA: [framing, angle, focal feel — "centered, slight top-down angle,
  85mm portrait compression, generous negative space on the left"]
LIGHTING: [key direction, softness, color cast — "single soft key from upper left,
  cool fill, subtle pink rim light"]
PALETTE: [exact hexes from the frontmatter palette, with roles —
  "#5B6CFF dominant body, #F2B8FF rim highlights, on #0E0E10 background"]
MOOD: [3-5 adjectives consistent with the parent brand voice]
BACKGROUND / INTEGRATION: [delivery format — `scene`: background baked in, edges
  blending into the destination surface tone; or `isolated`: single subject on a
  transparent background (PNG with alpha), generous margin, ready to place over
  {colors.surface}]
AVOID: [negative cues — "no text, no watermark, no extra objects, no photorealistic
  skin texture, no heavy drop shadow"]

### Natural-language version

[The same prompt rewritten as one flowing paragraph — models like gpt-image and DALL-E
respond better to prose than to field lists. Keep every hex code.]

### Model adaptation notes

- **gpt-image / DALL-E**: use the natural-language version as-is.
- **Midjourney**: condense to comma phrases; append aspect ratio (`--ar`) matching the
  element's observed proportions; consider `--style raw` for design assets.
- **Stable Diffusion / Flux**: comma-separated tags from the structured fields; move the
  AVOID block into the negative prompt field.

[Keep these notes brief — the canonical prompt is the contract; these are adaptations.]

## 5. Consistency notes

[How to keep the copied element coherent with its parent system — which tokens it must
share, which Do's/Don'ts apply. If the user is transplanting it into ANOTHER design,
state what must be re-tokenized (e.g., "swap #5B6CFF for the destination's primary").]

## 6. Confidence & open questions

| Aspect | Confidence | Why |
|---|---|---|
| Targeting | ✅ | DOM selector |
| Tokens | ✅/⚠️/❓ | ... |
| States | ❓ | hover never observed |
| Prompt fidelity | ⚠️ | see note below |

[Open questions, element-scoped. ALWAYS include for `asset`/`hybrid`:]

> **Prompt fidelity note**: a generative image prompt is a high-fidelity *description*,
> not a guarantee of reproduction. Expect to iterate 2-4 generations; the PALETTE and
> AVOID blocks are the strongest levers.
```

---

## Quality rules (element mode)

### Do

- ✅ Ground every PALETTE entry in extraction (`extract_colors.py`, CSS vars, or Figma
  fills) — exact hexes with roles, never "blueish"
- ✅ Record **case discipline and tracking** as first-class typography tokens: which
  text is sentence case vs ALL-CAPS, and the letter-spacing. Downstream agents drift
  to all-caps + wide tracking on stylized fonts, which single-handedly breaks period
  fidelity — state it explicitly in the reconstruction prompt ("sentence case
  everywhere except X")
- ✅ Carry the parent brand voice into MOOD — the prompt should regenerate an asset that
  *belongs* to the source design, not a generic pretty image
- ✅ Capture the integration contract (what surface it sits on, transparent vs flat bg)
- ✅ Resolve the **delivery format** (`scene` vs `isolated`/transparent PNG) from the
  user's goal — "for my website" means isolated cutout, not a recomposed scene
- ✅ Keep the canonical prompt model-agnostic; adapt per-model only in the notes
- ✅ Apply confidence markers to the prompt itself — and always include the prompt
  fidelity note

### Don't

- ❌ Don't generate the image. The skill delivers the **prompt**; rendering is the
  user's step, in their model of choice
- ❌ Don't expand into a full-page analysis ("while I'm here..."). If the user wants the
  system, offer full mode as the follow-up
- ❌ Don't write prompt fields from imagination — every concrete claim (lighting
  direction, finish, palette) must trace to something observed
- ❌ Don't promise pixel-perfect reproduction of an asset — say "2-4 iterations" honestly
- ❌ Don't copy verbatim brand-identifying artwork (logos, mascots) for reuse outside
  analysis/documentation — flag the IP concern and scope the prompt to "in the style
  of" descriptors instead
