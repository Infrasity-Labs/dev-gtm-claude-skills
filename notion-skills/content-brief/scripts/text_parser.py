#!/usr/bin/env python3
"""text_parser.py — Extract structured fields from Claude content brief output.

Stdlib-only. Parses the mandatory Direction prompt output format and returns
structured field values ready for Notion API mapping.

Field extraction is LABEL-EXACT. If a label doesn't match, the field returns
empty — matching the documented failure mode. Labels are case-sensitive.

Simple fields (single-line):
    TARGET_KEYWORD, VOLUME, CPC, DIFFICULTY, SEARCH_INTENT, AUDIENCE,
    RECOMMENDED_H1, CONTENT_ANGLE, WORD_COUNT, SCHEMA, PRIORITY

Block fields (multi-line until next label):
    H2_OUTLINE, FAQ, INTERNAL_LINKS, WRITER_NOTES

NO LLM CALLS. Pure line-by-line parsing.

Usage:
    python text_parser.py path/to/brief.txt
    python text_parser.py path/to/brief.txt --output json
    python text_parser.py --sample
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

SIMPLE_FIELDS = {
    "TARGET_KEYWORD", "VOLUME", "CPC", "DIFFICULTY",
    "SEARCH_INTENT", "AUDIENCE", "RECOMMENDED_H1",
    "CONTENT_ANGLE", "WORD_COUNT", "SCHEMA", "PRIORITY",
}

BLOCK_FIELDS = {"H2_OUTLINE", "FAQ", "INTERNAL_LINKS", "WRITER_NOTES"}

ALL_LABELS = SIMPLE_FIELDS | BLOCK_FIELDS

LABEL_PATTERN = re.compile(r"^([A-Z][A-Z0-9_]+):\s*(.*)")

SAMPLE_BRIEF = """TARGET_KEYWORD: employee onboarding software
VOLUME: 2400
CPC: 8.50
DIFFICULTY: 34
SEARCH_INTENT: Commercial
AUDIENCE: HR Director
RECOMMENDED_H1: 12 Employee Onboarding Software Platforms Compared (2025)
CONTENT_ANGLE: A comparison post targeting HR Directors who are evaluating onboarding tools for mid-size companies. Competitors cover feature lists but miss ROI framing and integration depth. This post leads with time-to-productivity metrics and benchmarks 12 platforms against each other on five criteria that HR teams actually care about.
WORD_COUNT: 2800
SCHEMA: FAQ + HowTo
PRIORITY: HIGH
H2_OUTLINE:
- H2: What Is Employee Onboarding Software?
  - H3: Core features to look for
  - H3: How it differs from HRIS platforms
- H2: Top 12 Employee Onboarding Software Platforms
  - H3: BambooHR
  - H3: Rippling
  - H3: Gusto
  - H3: Workday
- H2: How to Choose the Right Onboarding Software
  - H3: Company size considerations
  - H3: Integration requirements
  - H3: Pricing models compared
- H2: Implementation and ROI
  - H3: Average time-to-productivity benchmarks
  - H3: Common rollout mistakes
FAQ:
- Q: What is the best employee onboarding software for small businesses?
- Q: How much does employee onboarding software cost?
- Q: Can onboarding software integrate with our existing HRIS?
INTERNAL_LINKS:
- best HR software for startups → /hr-software/startups
- employee onboarding checklist → /resources/onboarding-checklist
WRITER_NOTES:
Write in a direct, advisory tone suited for HR Directors making a purchase decision. Lead with the ROI framing — time-to-productivity is the metric that resonates most. Avoid vendor-speak. The comparison table should be the centrepiece. Include a clear CTA at the bottom pointing to our HR software consultation page. Do not pad the introduction — get to the list by paragraph two.
"""


def parse_brief(text: str) -> Dict[str, Any]:
    """Parse Direction prompt output into a structured dict."""
    result: Dict[str, Any] = {label: "" for label in ALL_LABELS}
    current_label: Optional[str] = None
    current_is_block = False
    block_lines: List[str] = []

    def flush_block() -> None:
        if current_label and current_is_block:
            result[current_label] = "\n".join(block_lines).strip()

    for line in text.splitlines():
        match = LABEL_PATTERN.match(line)
        if match:
            candidate_label = match.group(1)
            rest = match.group(2).strip()

            if candidate_label in ALL_LABELS:
                flush_block()
                block_lines = []
                current_label = candidate_label

                if candidate_label in SIMPLE_FIELDS:
                    result[candidate_label] = rest
                    current_is_block = False
                else:
                    current_is_block = True
                    if rest:
                        block_lines.append(rest)
                continue

        if current_is_block and current_label:
            block_lines.append(line)

    flush_block()
    return result


def coerce_types(parsed: Dict[str, Any]) -> Dict[str, Any]:
    """Attempt numeric coercion for Notion number properties."""
    out = dict(parsed)
    for field in ("VOLUME", "WORD_COUNT", "DIFFICULTY"):
        raw = out.get(field, "")
        try:
            out[field] = int(str(raw).replace(",", "").strip())
        except (ValueError, TypeError):
            pass
    for field in ("CPC",):
        raw = out.get(field, "")
        try:
            out[field] = float(str(raw).strip())
        except (ValueError, TypeError):
            pass
    return out


def notion_property_map(parsed: Dict[str, Any]) -> Dict[str, Any]:
    """Return a Notion-ready property mapping keyed by database column name."""
    return {
        "Target Keyword": parsed.get("TARGET_KEYWORD", ""),
        "Volume": parsed.get("VOLUME", ""),
        "CPC": parsed.get("CPC", ""),
        "Keyword Difficulty": parsed.get("DIFFICULTY", ""),
        "Search Intent": parsed.get("SEARCH_INTENT", ""),
        "Audience": parsed.get("AUDIENCE", ""),
        "Recommended H1": parsed.get("RECOMMENDED_H1", ""),
        "Content Angle": parsed.get("CONTENT_ANGLE", ""),
        "Word Count Target": parsed.get("WORD_COUNT", ""),
        "Schema Type": parsed.get("SCHEMA", ""),
        "Priority": parsed.get("PRIORITY", ""),
        "_page_body": {
            "H2 Outline": parsed.get("H2_OUTLINE", ""),
            "FAQ": parsed.get("FAQ", ""),
            "Internal Links": parsed.get("INTERNAL_LINKS", ""),
            "Writer Notes": parsed.get("WRITER_NOTES", ""),
        },
    }


def render_human(parsed: Dict[str, Any]) -> str:
    out: List[str] = []
    out.append("=== Parsed Content Brief ===")
    out.append("")

    simple_order = [
        "TARGET_KEYWORD", "VOLUME", "CPC", "DIFFICULTY",
        "SEARCH_INTENT", "AUDIENCE", "RECOMMENDED_H1",
        "CONTENT_ANGLE", "WORD_COUNT", "SCHEMA", "PRIORITY",
    ]
    for label in simple_order:
        val = parsed.get(label, "")
        status = "[ok]" if val is not None and str(val).strip() not in ("", "not available") else "[missing]"
        out.append(f"  {status}  {label}: {val if val is not None and val != '' else '(empty)'}")

    out.append("")
    out.append("Block fields:")
    for label in ("H2_OUTLINE", "FAQ", "INTERNAL_LINKS", "WRITER_NOTES"):
        val = parsed.get(label, "")
        status = "[ok]" if val else "[missing]"
        preview = (val[:60] + "...") if len(val) > 60 else val
        out.append(f"  {status}  {label}: {preview if preview else '(empty)'}")

    empty_count = sum(1 for v in parsed.values() if v is None or str(v).strip() in ("", "not available"))
    out.append("")
    out.append(f"Fields empty or unavailable: {empty_count} / {len(ALL_LABELS)}")
    if empty_count > 2:
        out.append("  ⚠  >2 empty fields — flag for manual review before Notion push")
    return "\n".join(out)


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("path", nargs="?", help="Path to brief text file")
    parser.add_argument("--sample", action="store_true", help="Parse the embedded sample brief")
    parser.add_argument("--output", choices=["human", "json", "notion"], default="human",
                        help="human = readable summary | json = raw parsed dict | notion = Notion property map")
    args = parser.parse_args(argv)

    if args.sample:
        text = SAMPLE_BRIEF
    elif args.path:
        p = Path(args.path)
        if not p.exists():
            print(f"error: {args.path} not found", file=sys.stderr)
            return 2
        text = p.read_text(encoding="utf-8")
    else:
        parser.print_help()
        return 0

    parsed = coerce_types(parse_brief(text))

    if args.output == "json":
        print(json.dumps(parsed, indent=2))
    elif args.output == "notion":
        print(json.dumps(notion_property_map(parsed), indent=2))
    else:
        print(render_human(parsed))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
