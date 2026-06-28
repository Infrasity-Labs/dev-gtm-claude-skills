#!/usr/bin/env python3
"""
extract_css_vars.py — Extract CSS custom properties from a URL

Fetches the HTML of a URL, discovers every linked stylesheet and inline
<style> block, downloads them, and extracts all `--name: value;` definitions.
Groups them heuristically by category (color / spacing / typography / radius /
shadow / other) and emits a JSON document.

These are *explicit* design tokens — the ones the developer/designer named.
They should be marked as ✅ high confidence in the design.md output.

Stdlib only. No pip install required.

Usage:
    python extract_css_vars.py https://example.com
    python extract_css_vars.py https://example.com --output ./tokens.json
    python extract_css_vars.py https://example.com --pretty
"""

import argparse
import json
import re
import sys
from urllib import error as urlerror
from urllib import request as urlrequest
from urllib.parse import urljoin, urlparse

# Ensure Unicode (✅, etc.) prints cleanly on Windows consoles whose default
# code page is cp1252.
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

# CSS variable definition. Tolerates whitespace, multiline values, !important.
# Captures: name, value.
CSS_VAR_RE = re.compile(
    r"--([A-Za-z0-9_-]+)\s*:\s*([^;}]+?)\s*(?:!important\s*)?(?:;|(?=\}))",
    re.DOTALL,
)

# Stylesheet link extraction (rough but reliable for most pages).
LINK_HREF_RE = re.compile(
    r'<link\s+[^>]*rel=["\']?stylesheet["\']?[^>]*>',
    re.IGNORECASE,
)
HREF_ATTR_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)

# Inline <style> blocks.
STYLE_BLOCK_RE = re.compile(
    r"<style\b[^>]*>(.*?)</style>",
    re.IGNORECASE | re.DOTALL,
)

# Heuristic category mapping based on variable name substrings.
CATEGORY_HINTS = [
    ("color",      ("color", "bg", "background", "border", "fg", "foreground", "surface",
                    "text", "accent", "primary", "secondary", "muted", "success",
                    "warning", "error", "danger", "info", "destructive", "ring", "shadow-color")),
    ("spacing",    ("space", "spacing", "gap", "padding", "margin", "inset", "size")),
    ("typography", ("font", "text", "leading", "tracking", "line-height", "letter-spacing",
                    "weight")),
    ("radius",     ("radius", "rounded")),
    ("shadow",     ("shadow", "elevation")),
    ("z-index",    ("z-", "zindex", "z-index", "layer")),
    ("duration",   ("duration", "transition", "delay", "ease")),
    ("breakpoint", ("breakpoint", "screen", "viewport")),
]


def http_get(url, timeout=15):
    """GET a URL, return text content. Returns None on error."""
    req = urlrequest.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.read().decode(charset, errors="replace")
    except (urlerror.URLError, urlerror.HTTPError, TimeoutError, OSError) as e:
        print(f"   warn: failed to fetch {url}: {e}", file=sys.stderr)
        return None


def find_stylesheet_urls(html, base_url):
    """Extract all stylesheet URLs from the HTML, resolved against base_url."""
    urls = []
    for link_tag in LINK_HREF_RE.findall(html):
        m = HREF_ATTR_RE.search(link_tag)
        if not m:
            continue
        href = m.group(1).strip()
        if href.startswith(("data:", "javascript:", "#")):
            continue
        absolute = urljoin(base_url, href)
        urls.append(absolute)
    return urls


def find_inline_styles(html):
    """Extract content of every inline <style> block."""
    return STYLE_BLOCK_RE.findall(html)


def extract_vars_from_css(css_text):
    """Return list of (name, value) tuples for every --var: value found."""
    pairs = []
    for name, raw_value in CSS_VAR_RE.findall(css_text):
        value = " ".join(raw_value.split())  # collapse whitespace/newlines
        pairs.append((name, value))
    return pairs


def categorize(name):
    """Heuristic: map a variable name to a category bucket."""
    lower = name.lower()
    for category, hints in CATEGORY_HINTS:
        for hint in hints:
            if hint in lower:
                return category
    return "other"


def merge_uniq(pairs):
    """
    Collapse duplicates while preserving first-seen order. If a variable is
    redefined with different values across stylesheets, keep the first and
    record the alternatives in `_overrides`.
    """
    seen = {}
    overrides = {}
    for name, value in pairs:
        if name not in seen:
            seen[name] = value
        elif seen[name] != value:
            overrides.setdefault(name, []).append(value)
    return seen, overrides


def build_output(seen, overrides, url, sources):
    """Build the final grouped JSON document."""
    grouped = {}
    for name, value in seen.items():
        category = categorize(name)
        grouped.setdefault(category, {})[name] = {
            "value": value,
            "source": "css-custom-property",
        }
        if name in overrides:
            grouped[category][name]["alternatives"] = overrides[name]

    return {
        "tokens": grouped,
        "_meta": {
            "source_url": url,
            "stylesheet_count": len(sources),
            "stylesheets": sources,
            "total_variables": sum(len(v) for v in grouped.values()),
            "note": (
                "These are explicit CSS custom properties extracted from the site's "
                "stylesheets. Treat them as ✅ high-confidence tokens — the authors "
                "named them deliberately. Categories are heuristic; review before using."
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Extract CSS custom properties (--vars) from a URL. "
            "Stdlib only — no dependencies."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("url", help="URL of the site to inspect")
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output JSON path. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON (indent=2). Default is compact.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=15,
        help="HTTP timeout per request in seconds (default: 15).",
    )

    args = parser.parse_args()

    parsed = urlparse(args.url)
    if not parsed.scheme:
        print("URL must include scheme (http:// or https://)", file=sys.stderr)
        sys.exit(2)

    print(f"Fetching HTML: {args.url}", file=sys.stderr)
    html = http_get(args.url, timeout=args.timeout)
    if html is None:
        print("Could not fetch the page. Aborting.", file=sys.stderr)
        sys.exit(1)

    all_pairs = []
    sources = []

    inline_blocks = find_inline_styles(html)
    if inline_blocks:
        print(f"Found {len(inline_blocks)} inline <style> block(s).", file=sys.stderr)
        for i, css in enumerate(inline_blocks):
            pairs = extract_vars_from_css(css)
            if pairs:
                sources.append(f"inline-style-{i}")
                all_pairs.extend(pairs)

    stylesheet_urls = find_stylesheet_urls(html, args.url)
    print(f"Found {len(stylesheet_urls)} linked stylesheet(s).", file=sys.stderr)
    for ss_url in stylesheet_urls:
        css_text = http_get(ss_url, timeout=args.timeout)
        if css_text is None:
            continue
        pairs = extract_vars_from_css(css_text)
        if pairs:
            sources.append(ss_url)
            all_pairs.extend(pairs)
            print(f"   {ss_url} → {len(pairs)} vars", file=sys.stderr)

    seen, overrides = merge_uniq(all_pairs)
    output = build_output(seen, overrides, args.url, sources)

    indent = 2 if args.pretty else None
    serialized = json.dumps(output, indent=indent, ensure_ascii=False)

    if args.output:
        from pathlib import Path
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(serialized, encoding="utf-8")
        print(
            f"Wrote {output['_meta']['total_variables']} variables to {out_path}",
            file=sys.stderr,
        )
    else:
        print(serialized)


if __name__ == "__main__":
    main()
