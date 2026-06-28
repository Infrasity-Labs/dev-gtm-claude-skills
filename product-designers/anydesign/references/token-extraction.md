# Token Extraction — How to infer tokens with rigor

This reference defines how to go from "I see colors and sizes" to a documented token system.
It's the difference between describing and systematizing.

---

## Philosophy

**Token = named, reusable design decision.**

A color is not a token; `primary-500 = #3B82F6` with a semantic role is. Your job is to
**infer the system** the designer used (consciously or not), not list loose values.

Three principles:

1. **Look for repetition.** If a value appears once, it's not a token. If it appears three or
   more times, it probably is.
2. **Infer semantic roles, not just numeric scales.** "Dark blue color" is worse than
   "primary". "14px size" is worse than "body-sm".
3. **Mark confidence honestly.** If unsure about the role, say so.

---

## Color tokens

### Process

1. **Identify unique colors** observable in the material. Get precise hex codes (not "medium
   blue-ish").
2. **Group by family**: all blues together, all grays together, etc.
3. **Assign semantic role** based on where they appear:

| If it appears in... | Likely role |
|---|---|
| CTA buttons, primary links | `primary` |
| General page backgrounds | `surface` or `background` |
| Card, modal backgrounds | `surface-elevated` or `surface-2` |
| Main text | `text-primary` or `foreground` |
| Secondary text, captions | `text-muted` or `foreground-muted` |
| Subtle borders | `border` |
| Positive action (success) | `success` |
| Warning | `warning` |
| Error, destructive | `error` or `destructive` |
| Decorative, hover, prominent secondary | `accent` |

4. **Detect scale** if present. Many design systems use numeric scales (50-900):
   - 50-100: very light tints (backgrounds)
   - 200-300: light (borders, subtle backgrounds)
   - 400-600: medium (the "real" color sits here)
   - 700-900: dark (text on light, dark hover)

   If you see 3+ tints of the same color used systematically, there's probably a scale.

### Suggested naming convention

```
primary, secondary, accent              ← main roles
surface, surface-elevated, surface-sunken ← backgrounds by elevation
text-primary, text-muted, text-disabled ← text by hierarchy
border, border-strong                   ← borders
success, warning, error, info           ← feedback semantics
```

---

## Typography tokens

### Identify family

In order of reliability:
1. **If CSS is accessible** and you see `font-family: "Inter", sans-serif` → certainty ✅
2. **If you visually recognize the font** (Inter, Geist, IBM Plex, Söhne, Helvetica, etc.) →
   ⚠️ medium confidence. Say "looks like Inter" not "it is Inter".
3. **If you don't recognize it**, describe it: "geometric sans with open apertures and
   straight terminals"

### Infer scale

Look for the **most common typographic measurements** in the material:

```
Display:  48-72px  (heroes, hero titles)
H1:       32-48px
H2:       24-32px
H3:       18-24px
H4:       16-20px
Body:     14-16px
Body-sm:  12-14px
Caption:  11-12px
```

Not all systems have all levels. Report only those you observed.

### Weights

List the detected weights: 300, 400, 500, 600, 700, 800. If you only saw body at 400 and
headings at 600, that's what you report. **Don't assume the system has 300-900 complete if
you only saw 2.**

### Tracking and line-height

Watch for these details that separate professional designs from amateur ones:
- **Negative tracking on large headings** (-0.02em or -0.03em) → typographic care signal
- **Generous line-height on body** (1.5-1.7) → reading-oriented design
- **Tight line-height on headings** (1.1-1.2) → typographically-present design

---

## Spacing tokens

### Infer base unit

Look at distances between elements. If most are multiples of 8 (8, 16, 24, 32), the unit is
8px. If you see many multiples of 4 (4, 8, 12, 16, 20), the unit is 4px.

**Common base units:**
- **4px** → fine-grained systems, more granularity (Tailwind default: 0.25rem = 4px)
- **8px** → classic standard, balance between flexibility and consistency
- **16px** → low-granularity systems, usually indicates simple marketing design

### Observable scale

Report the multiples you saw, not the entire possible scale:

```
Saw: 4, 8, 12, 16, 24, 32, 48, 64
Didn't see intermediate multiples — the system seems to skip (no 20, 28, 40)
```

### Suggested naming

```
space-0   = 0
space-1   = 4px
space-2   = 8px
space-3   = 12px
space-4   = 16px
space-6   = 24px
space-8   = 32px
space-12  = 48px
space-16  = 64px
```

---

## Radius tokens (border-radius)

### Common values to look for

```
none:    0
sm:      4px
md:      8px
lg:      12px
xl:      16px
2xl:     24px
full:    9999px (pill/circular)
```

### Typical patterns

- **Single system**: everything uses the same radius (e.g., all 8px)
- **Tiered system**: smaller buttons than cards (e.g., btn 6px, card 12px)
- **Deliberate mixed system**: some components with radius, others square (intentional design
  signal)

---

## Shadow tokens

If visible shadows exist, report them. Typical system:

```
shadow-sm:    minimal shadow, barely perceptible
shadow-md:    clear but visible shadow, for cards
shadow-lg:    strong shadow, for modals or elevated elements
shadow-xl:    very strong, for prominent overlays
```

If you can infer exact CSS values (rare from an image), report them. If not, describe
qualitative intensity.

---

## Output: design-tokens.json

When you extract concrete tokens, also generate a structured JSON file so it's parseable by
design-systems tooling (Style Dictionary, Figma Variables, Tokens Studio, Penpot, Supernova,
Framer, etc.).

**Format: W3C Design Tokens Community Group (DTCG)** — the format reached its first stable
version in October 2025 and is now natively supported by Style Dictionary, Figma Variables,
Tokens Studio and most major design-system tooling. Use the canonical `$value` / `$type`
form:

```json
{
  "color": {
    "primary":      { "$value": "#3B82F6", "$type": "color", "$description": "Primary action — CTA buttons, links",   "$extensions": { "anydesign": { "confidence": "high" } } },
    "surface":      { "$value": "#FFFFFF", "$type": "color", "$description": "Base background",                       "$extensions": { "anydesign": { "confidence": "high" } } },
    "text": {
      "primary":    { "$value": "#111827", "$type": "color", "$description": "Body text",                             "$extensions": { "anydesign": { "confidence": "high" } } },
      "muted":      { "$value": "#6B7280", "$type": "color", "$description": "Captions, metadata",                    "$extensions": { "anydesign": { "confidence": "medium" } } }
    }
  },
  "typography": {
    "font-family": {
      "sans":       { "$value": "Inter, system-ui, sans-serif", "$type": "fontFamily",                                "$extensions": { "anydesign": { "confidence": "medium" } } }
    },
    "font-size": {
      "body":       { "$value": "16px", "$type": "dimension",                                                          "$extensions": { "anydesign": { "confidence": "high" } } },
      "h1":         { "$value": "48px", "$type": "dimension",                                                          "$extensions": { "anydesign": { "confidence": "high" } } }
    }
  },
  "spacing": {
    "1":            { "$value": "4px",  "$type": "dimension" },
    "2":            { "$value": "8px",  "$type": "dimension" },
    "3":            { "$value": "12px", "$type": "dimension" },
    "4":            { "$value": "16px", "$type": "dimension" },
    "6":            { "$value": "24px", "$type": "dimension" },
    "8":            { "$value": "32px", "$type": "dimension" },
    "12":           { "$value": "48px", "$type": "dimension" },
    "16":           { "$value": "64px", "$type": "dimension" }
  },
  "radius": {
    "sm":           { "$value": "6px",  "$type": "dimension", "$extensions": { "anydesign": { "confidence": "high"   } } },
    "md":           { "$value": "12px", "$type": "dimension", "$extensions": { "anydesign": { "confidence": "medium" } } }
  },
  "$extensions": {
    "anydesign": {
      "source":      "https://example.com",
      "captured_at": "2026-05-18",
      "method":      "html + css-vars-extraction",
      "spec":        "W3C Design Tokens Community Group 2025.10"
    }
  }
}
```

### Notes on the DTCG conventions used

- **`$value`** holds the concrete value. **`$type`** is the canonical type
  (`color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `shadow`, etc.).
- **`$description`** is free-form prose — use it for the semantic role.
- **`$extensions.anydesign.confidence`** is where the skill-specific metadata lives. DTCG
  reserves `$extensions` for tool-specific data, so this is the legal place to keep the
  confidence marker without breaking spec compliance.
- File-level metadata (source URL, capture method, capture date) goes in the **root-level
  `$extensions.anydesign`** object.

### Legacy format (still valid)

The earlier `{ "value": ..., "confidence": ... }` shape without `$` prefixes is not DTCG
compliant but is still readable by some custom tooling. If a user explicitly requests the
legacy shape — emit it. Otherwise, default to DTCG.

### When to emit this file

**Only generate `design-tokens.json` if you extracted real tokens.** If the source was an
ambiguous image and you couldn't extract hex codes with confidence, don't invent the JSON —
stick to `design.md`.

### Color extraction helper for images

When the source is a local image and you need pixel-precise hex codes (rather than vision
approximation), run:

```bash
python scripts/extract_colors.py <image-path> --top 8
```

It returns the top-N dominant colors with their hex codes and area percentages, computed via
Pillow's quantization. Use the output to ground the color tokens in real pixel data and avoid
inventing values.

---

## Golden rule

> A short and honest system is better than a long and invented one.

If you only identified 4 colors with confidence, report 4 colors. Don't fill to 10 "because
there usually are 10". The consumer of the `design.md` trusts what you document.
