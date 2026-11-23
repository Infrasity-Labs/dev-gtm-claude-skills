#!/usr/bin/env python3
"""Rebuild the README banner, per-bundle bars and the "Browse by category" table.

Counts come straight from the filesystem, so the numbers never drift:
  python3 scripts/build_readme_assets.py

Writes (stdlib only):
  assets/hero.svg (Infrasity hero)
  assets/banner-{light,dark}.svg
  assets/bars/<bundle>-{light,dark}.svg
  the block between <!-- BROWSE:START --> and <!-- BROWSE:END --> in README.md
"""
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import hero_banner
ASSETS = ROOT / "assets"
README = ROOT / "README.md"
REPO_SLUG = "infrasity-labs / dev-gtm-claude-skills"
INSTALL = "npx skills add Infrasity-Labs/dev-gtm-claude-skills"

# (label, folder, README anchor, one-line description)
BUNDLES = [
    ("SEO, GEO & docs", "skills", "seo-geo--docs-skills", "Docs audits, AI-readiness, SEO reports"),
    ("Marketing", "marketing-skills", "marketing-skills", "Full-funnel demand gen, lifecycle, conversion"),
    ("Writing & blog", "writing-skills", "writing-skills", "Blog content engine, research to review"),
    ("SEO suite", "seo-skills", "seo-skills", "Technical, content, schema and AI search"),
    ("Web design", "web-design", "web-design-skills", "Visual design, UI audits, site planning"),
    ("Product management", "product-management-skills", "product-management-skills", "Strategy, PRDs, prioritization"),
    ("Notion", "notion-skills", "notion-skills", "Brain dumps, triage, meeting notes"),
    ("Coding", "coding-skills", "coding-skills", "Code review, architecture, TDD"),
    ("Job search", "job-search", "job-search-skills", "Resumes, applications, interview prep"),
    ("Product design", "product-designers", "product-designer-skills", "UX research to design systems"),
]

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
THEMES = {
    "light": dict(panel="#f6f8fa", line="#d1d9e0", card="#ffffff", fg="#1f2328", muted="#59636e",
                  dim="#818b98", accent="#6a5af0", accent_bg="#ece9ff", track="#eef1f4", green="#1a7f37"),
    "dark": dict(panel="#151b23", line="#30363d", card="#0d1117", fg="#f0f6fc", muted="#9198a1",
                 dim="#6e7681", accent="#8b7dff", accent_bg="#262046", track="#1d242d", green="#3fb950"),
}

# --------------------------------------------------------------------------- counting

def count_skills(folder):
    """Skill folders (containing SKILL.md) at most two levels below `folder`."""
    base = ROOT / folder
    if not base.is_dir():
        return 0
    found = {p.parent for p in base.glob("*/SKILL.md")} | {p.parent for p in base.glob("*/*/SKILL.md")}
    return len(found)

def collect():
    bundles = [(label, folder, anchor, desc, count_skills(folder)) for label, folder, anchor, desc in BUNDLES]
    agents = len(list((ROOT / "agents").glob("*.md"))) if (ROOT / "agents").is_dir() else 0
    ext_dir = ROOT / "seo-skills" / "extensions"
    extensions = len([p for p in ext_dir.iterdir() if p.is_dir()]) if ext_dir.is_dir() else 0
    return {
        "bundles": bundles,
        "skills": sum(b[4] for b in bundles),
        "agents": agents,
        "extensions": extensions,
        "n_bundles": sum(1 for b in bundles if b[4]),
    }

# --------------------------------------------------------------------------- svg

def _t(x, y, text, size, fill, weight=None, anchor=None, family=SANS, spacing=None, tabular=False):
    a = [f'x="{x}"', f'y="{y}"', f'font-family="{family}"', f'font-size="{size}"', f'fill="{fill}"']
    if weight:
        a.append(f'font-weight="{weight}"')
    if anchor:
        a.append(f'text-anchor="{anchor}"')
    if spacing:
        a.append(f'letter-spacing="{spacing}"')
    if tabular:
        a.append('style="font-variant-numeric:tabular-nums"')
    return f'<text {" ".join(a)}>{escape(str(text))}</text>'

def banner(s, c):
    tiles = [(f"{s['skills']:,}", "skills", False), (f"{s['n_bundles']}", "skill bundles", True),
             (f"{s['agents']}", "subagents", False), (f"{s['extensions']}", "MCP extensions", False)]
    out = [
        f'<rect x="0.5" y="0.5" width="1279" height="359" rx="16" fill="{c["panel"]}" stroke="{c["line"]}"/>',
        f'<rect x="64" y="56" width="34" height="34" rx="8" fill="{c["accent"]}"/>',
        '<path d="M73 66 l7 7 l-7 7" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
        '<rect x="83" y="78" width="8" height="3" rx="1.5" fill="#ffffff"/>',
        _t(112, 82, REPO_SLUG, 15, c["muted"], family=MONO),
        _t(64, 138, "Claude Skills for SEO, GEO & Developer Marketing", 44, c["fg"], 700, spacing=-1),
        _t(64, 172, "Open-source skills, agents and MCP extensions for Claude Code, Codex, Cursor and more.", 19, c["muted"]),
    ]
    for i, (num, label, hot) in enumerate(tiles):
        x = 64 + i * 286
        if hot:
            out.append(f'<rect x="{x}" y="200" width="266" height="96" rx="12" fill="{c["accent_bg"]}" stroke="{c["accent"]}" stroke-opacity="0.55"/>')
        else:
            out.append(f'<rect x="{x}" y="200" width="266" height="96" rx="12" fill="{c["card"]}" stroke="{c["line"]}"/>')
        out.append(_t(x + 22, 252, num, 36, c["accent"] if hot else c["fg"], 700, spacing=-0.8, tabular=True))
        out.append(_t(x + 22, 278, label, 15, c["muted"]))
    out.append(f'<circle cx="70" cy="328" r="4" fill="{c["green"]}"/>')
    out.append(_t(82, 333, f"MIT licensed  ·  {INSTALL}", 13, c["dim"], family=MONO))
    desc = (f"{s['skills']} skills in {s['n_bundles']} bundles, {s['agents']} subagents and "
            f"{s['extensions']} MCP extensions for Claude Code and other agents.")
    return svg(1280, 360, "Claude Skills for SEO, GEO & Developer Marketing", "\n".join(out), desc)

def svg(w, h, label, body, desc=None):
    d = f'<desc id="d">{escape(desc)}</desc>\n' if desc else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t d">\n<title id="t">{escape(label)}</title>\n{d}{body}\n</svg>\n')

def bar(count, scale_max, c):
    w = 240
    fill = max(round(count / scale_max * w), 6) if count and scale_max else 0
    body = f'<rect x="0" y="0" width="{w}" height="12" rx="4" fill="{c["track"]}"/>'
    if fill:
        body += f'<rect x="0" y="0" width="{fill}" height="12" rx="4" fill="{c["accent"]}" fill-opacity="0.75"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="12" viewBox="0 0 {w} 12">{body}</svg>\n'

# --------------------------------------------------------------------------- output

def picture(name, alt, width=None):
    w = f' width="{width}"' if width else ""
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/{name}-dark.svg">'
            f'<img{w} alt="{alt}" src="./assets/{name}-light.svg"></picture>')

def browse_table(s):
    rows = ["| Bundle | Skills | What it covers | |", "|:--|--:|:--|:--|"]
    for label, folder, anchor, desc, n in s["bundles"]:
        rows.append(f"| [{label}](#{anchor}) | **{n}** | {desc} | {picture('bars/' + folder, f'{n} skills')} |")
    rows.append(f"| **Subagents** | **{s['agents']}** | Blog and SEO specialists under [`agents/`](agents/) | |")
    rows.append(f"| **MCP extensions** | **{s['extensions']}** | DataForSEO, Ahrefs, Firecrawl and more under [`seo-skills/extensions/`](seo-skills/extensions/) | |")
    return "\n".join(rows)

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def main():
    s = collect()
    top = max((b[4] for b in s["bundles"]), default=1) or 1
    hero_banner.write(ASSETS / "hero.svg", "skills", "Dev GTM Claude Skills",
                      f"{s['skills']} skills and {s['agents']} agents for developer marketing")
    for theme, c in THEMES.items():
        write(ASSETS / f"banner-{theme}.svg", banner(s, c))
        for _, folder, _, _, n in s["bundles"]:
            write(ASSETS / "bars" / f"{folder}-{theme}.svg", bar(n, top, c))
    text = README.read_text(encoding="utf-8")
    start, end = "<!-- BROWSE:START -->", "<!-- BROWSE:END -->"
    si, ei = text.find(start), text.find(end)
    if si == -1 or ei == -1:
        print("BROWSE markers not found in README.md; SVGs written, table skipped")
    else:
        text = text[:si + len(start)] + "\n" + browse_table(s) + "\n" + text[ei:]
        README.write_text(text, encoding="utf-8")
    print(f"{s['skills']} skills · {s['n_bundles']} bundles · {s['agents']} agents · {s['extensions']} extensions")

if __name__ == "__main__":
    main()
