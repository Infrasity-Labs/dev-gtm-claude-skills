#!/usr/bin/env python3
"""
verify_design.py — Audit a design-tokens.json against the live URL it came from

Takes a previously-generated `design-tokens.json` (DTCG format) and a URL, fetches
the current CSS custom properties from the live site, and reports drift:

- **MATCH**: token value still present in the live CSS exactly as declared
- **CHANGED**: token's value is no longer in the CSS at the same hex (possibly renamed
  or recolored)
- **NEW**: CSS custom property in the live site whose value is NOT in the design-tokens.json
  (possibly a token added since the last extraction)

This is the audit tool — answer to "is the design.md I wrote three months ago still
accurate?" If the brand evolved, you'll see the drift. If the brand is stable, you'll
see all-match.

Usage:
    python verify_design.py design-tokens.json https://vercel.com/
    python verify_design.py design-tokens.json https://vercel.com/ --output ./drift.md
    python verify_design.py design-tokens.json https://vercel.com/ --json

Stdlib only. No pip install required.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib import error as urlerror
from urllib import request as urlrequest
from urllib.parse import urljoin, urlparse

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

CSS_VAR_RE = re.compile(
    r"--([A-Za-z0-9_-]+)\s*:\s*([^;}]+?)\s*(?:!important\s*)?(?:;|(?=\}))",
    re.DOTALL,
)
LINK_HREF_RE = re.compile(
    r'<link\s+[^>]*rel=["\']?stylesheet["\']?[^>]*>',
    re.IGNORECASE,
)
HREF_ATTR_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
STYLE_BLOCK_RE = re.compile(
    r"<style\b[^>]*>(.*?)</style>",
    re.IGNORECASE | re.DOTALL,
)
HEX_RE = re.compile(r"#([0-9a-fA-F]{3,8})")


def http_get(url, timeout=15):
    req = urlrequest.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.read().decode(charset, errors="replace")
    except (urlerror.URLError, urlerror.HTTPError, TimeoutError, OSError) as e:
        print(f"   warn: failed to fetch {url}: {e}", file=sys.stderr)
        return None


def fetch_live_css_vars(url, timeout=15):
    """Reproduces extract_css_vars logic to get the live var set as {name: value}."""
    html = http_get(url, timeout=timeout)
    if html is None:
        return None
    vars_map = {}
    # Inline <style> blocks
    for css in STYLE_BLOCK_RE.findall(html):
        for name, raw_value in CSS_VAR_RE.findall(css):
            vars_map.setdefault(name, " ".join(raw_value.split()))
    # Linked stylesheets
    for link_tag in LINK_HREF_RE.findall(html):
        m = HREF_ATTR_RE.search(link_tag)
        if not m:
            continue
        href = m.group(1).strip()
        if href.startswith(("data:", "javascript:", "#")):
            continue
        absolute = urljoin(url, href)
        css_text = http_get(absolute, timeout=timeout)
        if css_text is None:
            continue
        for name, raw_value in CSS_VAR_RE.findall(css_text):
            vars_map.setdefault(name, " ".join(raw_value.split()))
    return vars_map


def normalize_hex(s):
    """Normalize hex strings for comparison: #ff0080 == #FF0080 == #ff0080ff (alpha stripped)."""
    m = HEX_RE.fullmatch(s.strip()) if isinstance(s, str) else None
    if not m:
        return s.strip().lower() if isinstance(s, str) else s
    h = m.group(1).lower()
    # Expand 3-digit to 6
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    # Strip alpha if it's FF (fully opaque) — keeps comparisons reasonable
    if len(h) == 8 and h.endswith("ff"):
        h = h[:6]
    return f"#{h}"


def walk_dtcg_tokens(obj, path=""):
    """
    Recursively walk a DTCG tokens document. Yield (dotted_path, value, type) tuples
    for every leaf that has a $value.
    """
    if isinstance(obj, dict):
        if "$value" in obj:
            yield path, obj["$value"], obj.get("$type")
        else:
            for key, val in obj.items():
                if key.startswith("$"):
                    continue
                sub_path = f"{path}.{key}" if path else key
                yield from walk_dtcg_tokens(val, sub_path)


def compare(declared_tokens, live_css):
    """
    Build a drift report. Token-by-token: is its value still in the live CSS?

    Strategy: for each declared token with a hex value, check whether ANY live CSS var
    has that same normalized hex. Match by VALUE, not by name (names differ between
    "primary" in DTCG and "--ds-gray-1000" in CSS).

    Returns dict:
      {
        "matches": [(token_path, value), ...],
        "changed": [(token_path, declared_value), ...],   # not found in live CSS
        "new":     [(css_name, value), ...],              # in CSS but not in DTCG
      }
    """
    declared_color_tokens = []
    for path, value, type_ in declared_tokens:
        if isinstance(value, str) and HEX_RE.fullmatch(value.strip()):
            declared_color_tokens.append((path, normalize_hex(value)))

    live_hex_values = {}
    for name, raw_val in live_css.items():
        # CSS values can be complex; extract hex if any
        for m in HEX_RE.finditer(raw_val):
            live_hex_values.setdefault(normalize_hex(f"#{m.group(1)}"), set()).add(name)

    matches = []
    changed = []
    for path, hex_val in declared_color_tokens:
        if hex_val in live_hex_values:
            matches.append((path, hex_val, sorted(live_hex_values[hex_val])[:3]))
        else:
            changed.append((path, hex_val))

    # Find live CSS hex values not represented in declared tokens
    declared_set = {v for _, v in declared_color_tokens}
    new = []
    for hex_val, css_names in live_hex_values.items():
        if hex_val not in declared_set:
            new.append((hex_val, sorted(css_names)[:3]))

    return {"matches": matches, "changed": changed, "new": new}


def format_markdown(report, tokens_file, url):
    lines = [
        f"# Design drift report",
        "",
        f"- **Tokens file**: `{tokens_file}`",
        f"- **Live URL**: {url}",
        f"- **Generated by**: `scripts/verify_design.py`",
        "",
        "---",
        "",
        f"## Summary",
        "",
        f"| Status | Count |",
        f"|---|---|",
        f"| ✅ Match (declared token value still present in live CSS) | {len(report['matches'])} |",
        f"| ⚠ Changed (declared value no longer found) | {len(report['changed'])} |",
        f"| 🆕 New (live CSS value not in your tokens file) | {len(report['new'])} |",
        "",
    ]
    if report["changed"]:
        lines.append("## ⚠ Changed — declared values not found in live CSS")
        lines.append("")
        lines.append("These tokens are in your design-tokens.json but their values no longer")
        lines.append("appear in any live CSS variable. The brand may have evolved, the variable")
        lines.append("may have been renamed, or the color may have shifted.")
        lines.append("")
        lines.append("| Token path | Declared value |")
        lines.append("|---|---|")
        for path, val in sorted(report["changed"]):
            lines.append(f"| `{path}` | `{val}` |")
        lines.append("")

    if report["new"]:
        lines.append("## 🆕 New — live CSS values not in your tokens file")
        lines.append("")
        lines.append("These hex values appear in the live CSS but were not declared in your")
        lines.append("design-tokens.json. They may be additions since the last extraction, or")
        lines.append("internal values not deemed token-worthy. Sample CSS variable names shown.")
        lines.append("")
        lines.append("| Hex | Sample CSS var(s) using it |")
        lines.append("|---|---|")
        for val, css_names in sorted(report["new"]):
            sample = ", ".join(f"`--{n}`" for n in css_names[:2])
            lines.append(f"| `{val}` | {sample} |")
        lines.append("")

    if report["matches"]:
        lines.append("## ✅ Matches — declared tokens still in live CSS")
        lines.append("")
        lines.append("<details><summary>Show full list ({} tokens)</summary>".format(len(report["matches"])))
        lines.append("")
        lines.append("| Token path | Value | Sample matching CSS var(s) |")
        lines.append("|---|---|---|")
        for path, val, css_names in sorted(report["matches"]):
            sample = ", ".join(f"`--{n}`" for n in css_names[:2])
            lines.append(f"| `{path}` | `{val}` | {sample} |")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    if not report["changed"]:
        lines.append("## Verdict")
        lines.append("")
        lines.append("**No drift detected on declared tokens.** The brand's published values still")
        lines.append("match the design-tokens.json. The `New` section, if populated, just shows")
        lines.append("which live CSS values weren't part of your original extraction scope.")
    else:
        lines.append("## Verdict")
        lines.append("")
        lines.append(f"**{len(report['changed'])} declared token(s) drifted.** Review the Changed section")
        lines.append("above and update `design-tokens.json` (and the `design.md` it backs) to reflect")
        lines.append("the brand's current state. Then re-run this script to confirm clean.")

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Audit a design-tokens.json against the live URL. "
            "Reports drift between declared values and live CSS."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("tokens", help="Path to a design-tokens.json file (DTCG format)")
    parser.add_argument("url", help="URL to verify against")
    parser.add_argument("--output", "-o", default=None,
                        help="Markdown output path. If omitted, prints to stdout.")
    parser.add_argument("--json", dest="as_json", action="store_true",
                        help="Emit JSON instead of markdown.")
    parser.add_argument("--timeout", type=int, default=15,
                        help="HTTP timeout per request (default: 15).")
    args = parser.parse_args()

    tokens_path = Path(args.tokens)
    if not tokens_path.exists():
        print(f"Tokens file not found: {tokens_path}", file=sys.stderr)
        sys.exit(2)

    parsed = urlparse(args.url)
    if not parsed.scheme:
        print("URL must include scheme (http:// or https://)", file=sys.stderr)
        sys.exit(2)

    try:
        tokens_doc = json.loads(tokens_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Could not parse tokens file as JSON: {e}", file=sys.stderr)
        sys.exit(2)

    declared = list(walk_dtcg_tokens(tokens_doc))
    print(f"Walked {len(declared)} tokens from {tokens_path}", file=sys.stderr)

    print(f"Fetching live CSS from {args.url}...", file=sys.stderr)
    live = fetch_live_css_vars(args.url, timeout=args.timeout)
    if live is None:
        print("Could not fetch the URL. Aborting.", file=sys.stderr)
        sys.exit(1)
    print(f"Fetched {len(live)} live CSS custom properties", file=sys.stderr)

    report = compare(declared, live)

    if args.as_json:
        out = json.dumps({
            "tokens_file": str(tokens_path),
            "url": args.url,
            "matches": [{"path": p, "value": v} for p, v, _ in report["matches"]],
            "changed": [{"path": p, "declared_value": v} for p, v in report["changed"]],
            "new": [{"value": v, "css_names": n} for v, n in report["new"]],
        }, indent=2)
    else:
        out = format_markdown(report, tokens_path, args.url)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out, encoding="utf-8")
        print(f"Wrote drift report to {out_path}", file=sys.stderr)
    else:
        print(out)

    if report["changed"]:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
