# Source — Lumen Notes (fictional)

This example uses a fictional SaaS landing page called **Lumen Notes** — a note-taking
product positioned for developers. The "source" was a static HTML mock with linked CSS,
so the skill could exercise both the HTML inspection path and the CSS variables extraction
path.

## Synthetic source description

- **Type**: static landing page (single hero, three feature blocks, footer)
- **Stack signals visible in HTML**: utility classes following the Tailwind convention
  (`bg-slate-900`, `text-zinc-100`, `rounded-2xl`)
- **Stylesheet**: a single linked `/styles.css` with a `:root` block defining ~22 CSS
  custom properties

## Capture method used by the skill

1. `WebFetch https://lumen.example/` → HTML had real content (no Playwright needed).
2. `python scripts/extract_css_vars.py https://lumen.example/ --pretty` →
   pulled 22 custom properties grouped into color (12), spacing (5), typography (3),
   radius (2).
3. No multimodal vision was needed because the HTML + CSS were sufficient.
4. `python scripts/check_contrast.py --pairs-file pairs.txt` →
   contrast report for the 4 key text-on-surface combinations.

## Limitations of this example

- No screenshot bundled (would inflate the repo and not add information already in
  `design.md`).
- Components inventory is partial — the synthetic source only includes Button, Card,
  Input, Badge.
- Only desktop viewport modeled; the `design.md` flags this in Open Questions.
