# Capture Flows — How to capture each source type

This reference defines the technical capture flow for each input type. Consult it when you start
Step 2 of the main workflow.

---

## Flow 1 — Local image

**Typical input:** the user uploads a PNG/JPG/WebP, or passes a path like
`/mnt/user-data/uploads/ref.png`.

**What to do:**
1. The image is already available via multimodal vision. **No script needed.**
2. If the path is in `/mnt/user-data/uploads/`, you can reference it directly.
3. If you need pixel-precise hex codes for the dominant colors (vision is approximating),
   run `python scripts/extract_colors.py <image-path>` — it returns dominant colors with area
   percentages.
4. Move to Step 3 (analysis).

**When to ask for more:**
- If the image is too small or low-resolution → ask the user for a better version before
  analyzing (analysis will be poor and you'll end up inventing tokens).
- If the image shows only part of something (e.g., only the header) → ask if they have
  captures of other sections for fuller vision.

---

## Flow 2 — Website URL

**Typical input:** a URL pasted by the user.

**Strategy: HTML first, CSS variables second, screenshot only if needed.**

### Step 2.1 — Fetch the HTML

Use the `WebFetch` tool with the URL. This retrieves raw HTML without executing JavaScript.

Review the HTML for signs of **real content**:

✅ **Good HTML (sufficient, no screenshot needed):**
- Has visible text in `<h1>`, `<p>`, `<button>`, etc.
- Has descriptive CSS classes on elements
- Has semantic structure (`<header>`, `<main>`, `<section>`)
- Links stylesheets you can inspect
- Typically: blogs, static landings, sites with SSR (Next.js/Astro/Hugo)

❌ **Empty HTML (Playwright screenshot needed):**
- `<body>` is nearly empty, just `<div id="root"></div>` or similar
- Visible content is minimal or only placeholders
- Many scripts but little text
- Typically: SPAs without SSR (pure React/Vue), dashboards, web apps

### Step 2.2 — If HTML is sufficient

Work with it. Look specifically for:
- **CSS classes** that suggest a framework: `bg-blue-500` (Tailwind), `MuiButton-root`
  (Material UI), `chakra-button` (Chakra), `ant-btn` (Ant Design), `sl-button` (Shoelace)
- **Inline `<style>` blocks** with `--*: value;` definitions
- **Linked stylesheets** (`<link rel="stylesheet" href="...">`) — see Step 2.2.bis below
- **Meta tags** with brand info: `<meta property="og:image">`, theme-color, etc.

### Step 2.2.bis — CSS variables extraction (this is where the gold is)

CSS custom properties (e.g., `--color-primary: #3B82F6;`) are the **explicit token system**
of the site. Extracting them turns guesswork into ground truth and gives you ✅ high
confidence tokens directly.

**Two ways to do it:**

**A. Batch via the helper script (preferred for multi-stylesheet sites):**

```bash
python scripts/extract_css_vars.py <URL> --output ./css-vars.json
```

This fetches the HTML, discovers every `<link rel="stylesheet">` and inline `<style>` block,
downloads them, and extracts all `--name: value;` definitions grouped by inferred category
(color / spacing / typography / radius / other). Stdlib only — no pip install required.

**B. Manual via WebFetch (when you only have one or two stylesheets and want fine control):**

1. Parse the HTML response for `<link rel="stylesheet" href="...">`.
2. For each href (resolving relative URLs against the base), call `WebFetch` with a prompt
   like *"Return only the CSS custom property definitions — lines containing `--*: value;`"*.
3. Manually map each variable to its semantic role for the token table.

**What to do with the extracted variables:**
- They go into the `design-tokens.json` with **`"confidence": "high"`** because they're
  authoritative — the designer/developer named them explicitly.
- Cite the source stylesheet URL in the `_meta` section of the JSON.
- In `design.md` Section 2 (Design System), mark these tokens with ✅.

### Step 2.3 — If HTML is empty: on-demand Playwright

Execute the script:

```bash
python scripts/capture_site.py <URL> --output ./capture.png
```

By default the script:
1. Verifies Playwright is installed; if not, prints the exact install command.
2. Renders the site in a headless Chromium.
3. **Attempts to dismiss cookie/consent banners** via a list of common selectors
   (silently fails if none match).
4. Takes a full-page screenshot.
5. **Saves the post-JavaScript rendered HTML** alongside (use `--no-save-html` to opt out).

**Multi-viewport** (for responsive analysis — Layer 4 of the framework needs this):

```bash
python scripts/capture_site.py <URL> --viewports desktop,tablet,mobile
```

Produces `capture-desktop.png`, `capture-tablet.png`, `capture-mobile.png` with sensible
default sizes (1440×900, 768×1024, 375×812). Pair this with the rendered HTML to give the
analysis layer responsive evidence.

**Scroll capture** (for lazy-loaded content):

```bash
python scripts/capture_site.py <URL> --scroll-capture
```

Scrolls through 25%/50%/75% of the page before the screenshot to trigger intersection-observer
content.

**Element capture** (element mode only — see `references/element-copy.md`):

```bash
python scripts/capture_site.py <URL> --selector "header.navbar" --output ./element.png
```

Screenshots only the first matching element's bounding box and saves its outerHTML
instead of the full page.

Then analyze the screenshots as images (Flow 1) plus the rendered HTML.

**Important user warning:** the first time Playwright runs, it downloads ~300MB of Chromium.
Warn them so they're not surprised.

---

## Flow 3 — Figma link

**Typical input:** a URL like `https://www.figma.com/file/<key>/...` or
`https://www.figma.com/design/<key>/...` or a specific node with `?node-id=...`.

**Prerequisite:** the user must have the Figma MCP connected. If not, tell them they need to
connect it from the Claude app before continuing.

### Step 3.1 — Identify the scope

- **Full file URL** → you'll analyze the entire file. This can be huge. Suggest the user pass
  a link to a specific frame/page.
- **URL with `node-id`** → already scoped. Better.

### Step 3.2 — MCP tools in order

1. **`get_metadata`** → first, to understand the structure of the file/node (what's inside,
   what element types, hierarchy). Orients you before requesting heavy content.

2. **`get_variable_defs`** → if the file uses Figma Variables (colors, spacing, typography),
   you have them explicit here. **This is gold:** they're the design system tokens already
   structured by the designer. No need to infer them.

3. **`get_design_context`** → detailed content of the node. Returns components, properties,
   values. Richest but also most token-expensive. Request it after having the overview.

4. **`get_screenshot`** → if you need visual reference besides structure (useful for Layer 1
   "Identity" — mood, personality).

### Step 3.3 — Advantage of the Figma flow

When the file is well-structured, **tokens come served**. Your role shifts: instead of
inferring from pixels, you **document** what the designer already defined and add layers of
interpretation (mood, implicit components, system decisions).

Mark this in the `design.md`: tokens with ✅ high confidence are those that came from
`get_variable_defs`, not those you inferred yourself.

---

## Flow 4 — Combinations

**Common case:** the user passes a URL **and** a manual screenshot of a specific state
(e.g., "the site rendered on mobile" or "the modal open").

Combine them like this:
- **HTML + extracted CSS vars** → structure, classes, semantics, explicit tokens
- **Screenshot** → visual presentation, real rendered colors, final layout
- In the `design.md`, "Source" section, cite both sources and clarify what each contributed

**Less common but valid case:** Figma + production site. Useful to audit whether the site
implemented what the design defined. In this case the `design.md` can have an extra section on
**design-vs-implementation discrepancies**.

---

## Error handling

| Error | What to do |
|---|---|
| URL returns 403/404 | Tell the user, offer alternatives (manual screenshot, archive.org) |
| URL blocked by Cloudflare/captcha | Tell them honestly. **Don't attempt bypass.** Request manual screenshot. |
| Playwright not installed | Give the install command. Don't attempt workaround. |
| Figma MCP can't access file | Verify the file is accessible to the logged-in user. |
| Cookie banner blocks content even after auto-dismiss | Ask the user for a manual screenshot with the banner already closed. |
| Corrupt or unreadable image | Ask for a new version. |

**Principle:** honesty about limitations is part of being professional. An invented analysis is
worse than an analysis with missing but clear data.
