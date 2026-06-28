#!/usr/bin/env python3
"""
extract_colors.py — Extract dominant colors from a local image

Returns the top-N dominant colors with their hex codes and area percentages,
computed via Pillow's median-cut quantization. Useful when multimodal vision
approximates colors and you need pixel-precise hex codes.

Usage:
    python extract_colors.py ./reference.png
    python extract_colors.py ./reference.png --top 8
    python extract_colors.py ./reference.png --top 12 --json --output ./colors.json

Requirements:
    pip install Pillow
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure Unicode prints cleanly on Windows consoles whose default code page
# is cp1252.
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


def check_pillow():
    try:
        import PIL  # noqa: F401
        return True
    except ImportError:
        print(
            "Pillow is not installed.\n\n"
            "Install with:\n    pip install Pillow\n",
            file=sys.stderr,
        )
        return False


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb[:3])


def extract(image_path, top_n=8, resize=400):
    """
    Reduce the image, quantize it to top_n colors, and return a list of
    {hex, rgb, count, pct} sorted by descending area.
    """
    from PIL import Image

    img = Image.open(image_path).convert("RGB")

    # Resize down to keep quantization fast and tolerant to compression noise.
    width, height = img.size
    longest = max(width, height)
    if longest > resize:
        scale = resize / longest
        img = img.resize((int(width * scale), int(height * scale)), Image.LANCZOS)

    quantized = img.quantize(colors=top_n, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()  # flat [r,g,b,r,g,b,...]
    color_counts = quantized.getcolors()  # [(count, palette_index), ...]
    if color_counts is None:
        return []

    total = sum(c for c, _ in color_counts)
    results = []
    for count, idx in color_counts:
        r = palette[idx * 3]
        g = palette[idx * 3 + 1]
        b = palette[idx * 3 + 2]
        results.append({
            "hex": rgb_to_hex((r, g, b)),
            "rgb": [r, g, b],
            "count": count,
            "pct": round(count / total * 100, 2),
        })
    results.sort(key=lambda c: c["count"], reverse=True)
    return results


def format_markdown(colors, image_path):
    lines = [
        f"# Dominant colors — `{image_path}`",
        "",
        "| Rank | Hex | RGB | % of area |",
        "|---|---|---|---|",
    ]
    for i, c in enumerate(colors, 1):
        rgb = f"{c['rgb'][0]}, {c['rgb'][1]}, {c['rgb'][2]}"
        lines.append(f"| {i} | `{c['hex']}` | {rgb} | {c['pct']}% |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Extract dominant colors from a local image (PIL median-cut).",
    )
    parser.add_argument("image", help="Path to a local image (PNG/JPG/WebP)")
    parser.add_argument(
        "--top",
        type=int,
        default=8,
        help="How many dominant colors to return (default: 8).",
    )
    parser.add_argument(
        "--resize",
        type=int,
        default=400,
        help="Resize longest edge to N pixels before quantizing (default: 400).",
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

    args = parser.parse_args()

    if not check_pillow():
        sys.exit(2)

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    colors = extract(image_path, top_n=args.top, resize=args.resize)
    if not colors:
        print("No colors extracted (image may be empty or unreadable).", file=sys.stderr)
        sys.exit(1)

    if args.as_json:
        payload = {
            "image": str(image_path),
            "top_n": args.top,
            "colors": colors,
        }
        output = json.dumps(payload, indent=2)
    else:
        output = format_markdown(colors, image_path)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote {len(colors)} colors to {out_path}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
