# Source — Vercel landing (real capture)

This is a **real** end-to-end run of the `anydesign` skill against the live Vercel
homepage. Everything in `design.md`, `design-tokens.json`, and `design-a11y.md` was
produced from the artifacts captured here — no hallucinated values.

## Source

- **URL**: `https://vercel.com/`
- **Captured at**: 2026-05-18
- **Viewport**: 1440×900 (desktop only)
- **Why Vercel**: well-known reference for the Geist design system, exercises the URL
  capture flow end-to-end, has hundreds of CSS custom properties that demonstrate why
  the CSS-variables extraction step is the gold path.

## Capture method

Two scripts run in parallel:

### 1. Playwright screenshot + rendered HTML

```bash
python scripts/capture_site.py https://vercel.com/ \
    --viewports desktop \
    --output examples/vercel-landing/capture.png \
    --timeout 45000
```

- Network-idle never settles on vercel.com (likely background telemetry / analytics
  keep-alive). The script's non-fatal timeout handler caught the timeout and screenshotted
  what had rendered — full visible page captured cleanly.
- Cookie/consent banner auto-dismiss: no banner appeared (Vercel detects no consent
  needed for this geo on first visit), so the dismiss step was a silent no-op.
- Output: `capture.png` (233 KB (downsized to 720px wide for repo size)) + `capture.html` (rendered HTML, ~520 KB, not committed
  to keep repo size reasonable).

### 2. CSS custom properties extraction

```bash
python scripts/extract_css_vars.py https://vercel.com/ \
    --pretty \
    --output examples/vercel-landing/css-vars-raw.json
```

- Discovered **6 linked stylesheets** + **2 inline `<style>` blocks**.
- Extracted **808 unique CSS custom properties** in ~3 seconds (stdlib only — no pip
  install).
- The full raw extraction (`css-vars-raw.json`, 224 KB) is **not committed** to keep the
  example browsable; the analysed subset is reproduced verbatim in `design-tokens.json`.

### 3. Contrast check

```bash
python scripts/check_contrast.py \
    --pair "#171717,#FFFFFF:text on background" \
    --pair "#4D4D4D,#FFFFFF:text-muted on background" \
    --pair "#FFFFFF,#171717:CTA label on primary" \
    --pair "#0070F7,#FFFFFF:focus blue on background" \
    --pair "#F2F2F2,#FFFFFF:gray-100 surface boundary (info only)" \
    --title "WCAG 2.1 Contrast Check — Vercel landing (Geist palette)" \
    --output examples/vercel-landing/design-a11y.md
```

- Stdlib only — runs instantly.
- Manual "Findings" + "Recommendations" sections appended to the script's auto-generated
  table (the script handles math, the analyst handles interpretation).

## What's in this folder (committed)

| File | Source | Purpose |
|---|---|---|
| `source.md` | This file | Capture method log |
| `design.md` | Synthesized | The main analysis output |
| `design-tokens.json` | Synthesized from `css-vars-raw.json` | DTCG-format tokens |
| `design-a11y.md` | `check_contrast.py` + analyst | WCAG report |
| `capture.png` | `capture_site.py` | Desktop screenshot |

## What's NOT committed (regenerable)

- `capture.html` — 520 KB rendered HTML; regenerate with `--no-save-html=false` (default)
- `css-vars-raw.json` — 224 KB raw extraction; regenerate with `extract_css_vars.py`

To reproduce this example end-to-end, run the three commands above from the repo root.
