#!/usr/bin/env python3
"""
check_contrast.py — WCAG 2.1 contrast ratio for hex color pairs

Computes the contrast ratio for given foreground/background hex pairs and
reports pass/fail for WCAG 2.1 AA and AAA, for normal and large text.

Thresholds (WCAG 2.1):
    - AA normal text:  >= 4.5:1
    - AA large text:   >= 3.0:1  (>= 18pt or >= 14pt bold)
    - AAA normal text: >= 7.0:1
    - AAA large text:  >= 4.5:1

Usage:
    python check_contrast.py --pair "#111827,#FFFFFF"
    python check_contrast.py --pair "#111827,#FFFFFF" --pair "#3B82F6,#FFFFFF"
    python check_contrast.py --pair "#111,#fff" --json
    python check_contrast.py --pairs-file pairs.txt --output ./design-a11y.md

A pairs file contains one `fg,bg` line per pair, with optional `# comment`
after a `#` character. Empty and comment-only lines are ignored.

Stdlib only. No pip install required.
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure Unicode (≥, ✅, ❌) prints cleanly on Windows consoles whose default
# code page is cp1252.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def parse_hex(hex_str):
    """Accept '#RGB', '#RRGGBB', 'RGB', 'RRGGBB'. Return (r, g, b) ints."""
    s = hex_str.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6 or any(c not in "0123456789abcdefABCDEF" for c in s):
        raise ValueError(f"Invalid hex color: {hex_str!r}")
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


def srgb_channel(c8):
    """Linearize a single sRGB channel (0..255) per WCAG 2.1."""
    c = c8 / 255.0
    if c <= 0.03928:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    """WCAG 2.1 relative luminance."""
    r, g, b = rgb
    return (
        0.2126 * srgb_channel(r)
        + 0.7152 * srgb_channel(g)
        + 0.0722 * srgb_channel(b)
    )


def contrast_ratio(fg, bg):
    """WCAG 2.1 contrast ratio. Returns a float in [1.0, 21.0]."""
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter, darker = (l1, l2) if l1 >= l2 else (l2, l1)
    return (lighter + 0.05) / (darker + 0.05)


def grade(ratio):
    """Return AA/AAA pass/fail for normal and large text."""
    return {
        "AA_normal":  ratio >= 4.5,
        "AA_large":   ratio >= 3.0,
        "AAA_normal": ratio >= 7.0,
        "AAA_large":  ratio >= 4.5,
    }


def pair_result(fg_hex, bg_hex, label=None):
    fg = parse_hex(fg_hex)
    bg = parse_hex(bg_hex)
    ratio = contrast_ratio(fg, bg)
    return {
        "label":  label,
        "fg":     fg_hex,
        "bg":     bg_hex,
        "ratio":  round(ratio, 2),
        "grades": grade(ratio),
    }


def parse_pair_arg(s):
    """Parse 'FG,BG' (with optional ':label' suffix)."""
    label = None
    if ":" in s:
        s, label = s.rsplit(":", 1)
        label = label.strip() or None
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError(
            f"Expected 'FG,BG' or 'FG,BG:label', got: {s!r}"
        )
    return (parts[0], parts[1], label)


def load_pairs_file(path):
    """Read fg,bg[:label] pairs from a text file. Comments start with #."""
    pairs = []
    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        pairs.append(parse_pair_arg(line))
    return pairs


def tick(passed):
    return "✅" if passed else "❌"


def format_markdown(results, title="WCAG 2.1 Contrast Check"):
    lines = [
        f"# {title}",
        "",
        "Thresholds: **AA normal** ≥ 4.5:1 · **AA large** ≥ 3:1 · "
        "**AAA normal** ≥ 7:1 · **AAA large** ≥ 4.5:1",
        "",
        "| Pair | FG | BG | Ratio | AA normal | AA large | AAA normal | AAA large |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        label = r["label"] or f"`{r['fg']}` on `{r['bg']}`"
        g = r["grades"]
        lines.append(
            f"| {label} | `{r['fg']}` | `{r['bg']}` | {r['ratio']}:1 | "
            f"{tick(g['AA_normal'])} | {tick(g['AA_large'])} | "
            f"{tick(g['AAA_normal'])} | {tick(g['AAA_large'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="WCAG 2.1 contrast checker for hex color pairs (stdlib only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--pair",
        action="append",
        default=[],
        type=parse_pair_arg,
        metavar="FG,BG[:label]",
        help="A foreground/background hex pair. May be repeated. "
             "Optional ':label' suffix for human-readable naming.",
    )
    parser.add_argument(
        "--pairs-file",
        default=None,
        help="Path to a file with one 'fg,bg[:label]' pair per line.",
    )
    parser.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help="Emit JSON instead of a markdown table.",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output file path. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--title",
        default="WCAG 2.1 Contrast Check",
        help="Heading title for the markdown report.",
    )

    args = parser.parse_args()

    pairs = list(args.pair)
    if args.pairs_file:
        pairs.extend(load_pairs_file(args.pairs_file))

    if not pairs:
        parser.error("Provide at least one --pair or use --pairs-file.")

    try:
        results = [pair_result(fg, bg, label) for fg, bg, label in pairs]
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    if args.as_json:
        output = json.dumps({"results": results}, indent=2)
    else:
        output = format_markdown(results, title=args.title)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote {len(results)} pair(s) to {out_path}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
