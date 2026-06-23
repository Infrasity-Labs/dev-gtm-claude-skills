#!/usr/bin/env python3
"""brief_validator.py — Validate a parsed content brief against Notion push requirements.

Stdlib-only. Checks that all required fields are present, values fall within
allowed sets, numeric fields are numeric, and block fields meet minimum
content thresholds.

Verdict:
  PASS  — brief is safe to push to Notion
  WARN  — minor issues, push allowed but review recommended
  FAIL  — >2 empty fields or invalid select values; do not push

NO LLM CALLS. Pure rule-based validation.

Usage:
    python brief_validator.py path/to/brief.txt
    python brief_validator.py path/to/brief.txt --output json
    python brief_validator.py --sample
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

# Import the parser from the same scripts/ directory
import importlib.util
import os

_parser_path = Path(__file__).parent / "text_parser.py"
_spec = importlib.util.spec_from_file_location("text_parser", _parser_path)
_text_parser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_text_parser)

VALID_SEARCH_INTENT = {"Informational", "Commercial", "Transactional", "Navigational"}
VALID_PRIORITY = {"HIGH", "MEDIUM", "LOW"}

REQUIRED_SIMPLE = [
    "TARGET_KEYWORD", "VOLUME", "CPC", "DIFFICULTY",
    "SEARCH_INTENT", "AUDIENCE", "RECOMMENDED_H1",
    "CONTENT_ANGLE", "WORD_COUNT", "SCHEMA", "PRIORITY",
]
REQUIRED_BLOCKS = ["H2_OUTLINE", "FAQ", "INTERNAL_LINKS", "WRITER_NOTES"]

NUMERIC_FIELDS = {
    "VOLUME": int,
    "DIFFICULTY": int,
    "WORD_COUNT": int,
    "CPC": float,
}

MIN_H2_COUNT = 4
MIN_FAQ_COUNT = 3
MIN_INTERNAL_LINKS = 2

SAMPLE_BRIEF = _text_parser.SAMPLE_BRIEF


def validate(parsed: Dict[str, Any]) -> Dict[str, Any]:
    issues: List[Dict[str, str]] = []

    # Check simple fields for emptiness
    empty_count = 0
    for field in REQUIRED_SIMPLE:
        val = parsed.get(field, "")
        if val is None or str(val).strip() in ("", "not available"):
            issues.append({
                "field": field,
                "severity": "warn" if str(val) == "not available" else "error",
                "message": f"{field} is {'not available' if str(val) == 'not available' else 'empty'}",
            })
            if str(val) != "not available":
                empty_count += 1

    # Check block fields for emptiness
    for field in REQUIRED_BLOCKS:
        val = parsed.get(field, "")
        if not val or not val.strip():
            issues.append({
                "field": field,
                "severity": "error",
                "message": f"{field} block is empty",
            })
            empty_count += 1

    # Validate select values
    intent = parsed.get("SEARCH_INTENT", "")
    if intent and intent not in VALID_SEARCH_INTENT:
        issues.append({
            "field": "SEARCH_INTENT",
            "severity": "error",
            "message": f"'{intent}' is not a valid Search Intent. Must be one of: {sorted(VALID_SEARCH_INTENT)}",
        })

    priority = parsed.get("PRIORITY", "")
    if priority and priority not in VALID_PRIORITY:
        issues.append({
            "field": "PRIORITY",
            "severity": "error",
            "message": f"'{priority}' is not a valid Priority. Must be HIGH, MEDIUM, or LOW.",
        })

    # Validate numeric fields
    for field, coerce in NUMERIC_FIELDS.items():
        val = parsed.get(field, "")
        if val and str(val) not in ("", "not available"):
            try:
                coerce(str(val).replace(",", ""))
            except (ValueError, TypeError):
                issues.append({
                    "field": field,
                    "severity": "error",
                    "message": f"{field} must be numeric, got: '{val}'",
                })

    # Check block field content thresholds
    h2_outline = parsed.get("H2_OUTLINE", "")
    h2_count = h2_outline.count("- H2:") if h2_outline else 0
    if h2_outline and h2_count < MIN_H2_COUNT:
        issues.append({
            "field": "H2_OUTLINE",
            "severity": "warn",
            "message": f"H2_OUTLINE has {h2_count} H2(s); minimum recommended is {MIN_H2_COUNT}",
        })

    faq = parsed.get("FAQ", "")
    faq_count = faq.count("- Q:") if faq else 0
    if faq and faq_count < MIN_FAQ_COUNT:
        issues.append({
            "field": "FAQ",
            "severity": "warn",
            "message": f"FAQ has {faq_count} question(s); minimum recommended is {MIN_FAQ_COUNT}",
        })

    internal_links = parsed.get("INTERNAL_LINKS", "")
    link_count = internal_links.count("→") if internal_links else 0
    if internal_links and link_count < MIN_INTERNAL_LINKS:
        issues.append({
            "field": "INTERNAL_LINKS",
            "severity": "warn",
            "message": f"INTERNAL_LINKS has {link_count} link(s); minimum recommended is {MIN_INTERNAL_LINKS}",
        })

    # Determine overall verdict
    errors = [i for i in issues if i["severity"] == "error"]
    warns = [i for i in issues if i["severity"] == "warn"]

    if empty_count > 2 or any(
        i["field"] in ("SEARCH_INTENT", "PRIORITY") for i in errors
    ):
        verdict = "FAIL"
    elif errors:
        verdict = "FAIL"
    elif warns:
        verdict = "WARN"
    else:
        verdict = "PASS"

    return {
        "verdict": verdict,
        "empty_count": empty_count,
        "error_count": len(errors),
        "warn_count": len(warns),
        "issues": issues,
        "stats": {
            "h2_count": h2_count,
            "faq_count": faq_count,
            "link_count": link_count,
            "keyword": parsed.get("TARGET_KEYWORD", ""),
            "priority": parsed.get("PRIORITY", ""),
        },
    }


def render_human(result: Dict[str, Any]) -> str:
    out: List[str] = []
    verdict = result["verdict"]
    icon = {"PASS": "[PASS]", "WARN": "[WARN]", "FAIL": "[FAIL]"}[verdict]
    out.append(f"Validation verdict: {icon}")
    out.append(f"  Keyword:  {result['stats']['keyword']}")
    out.append(f"  Priority: {result['stats']['priority']}")
    out.append(f"  H2s: {result['stats']['h2_count']}  FAQs: {result['stats']['faq_count']}  Links: {result['stats']['link_count']}")
    out.append(f"  Empty fields: {result['empty_count']}  Errors: {result['error_count']}  Warnings: {result['warn_count']}")

    if result["issues"]:
        out.append("")
        for issue in result["issues"]:
            prefix = "[error]" if issue["severity"] == "error" else "[warn] "
            out.append(f"  {prefix}  {issue['field']}: {issue['message']}")
    else:
        out.append("")
        out.append("  All checks passed. Brief is ready for Notion push.")

    if verdict == "FAIL":
        out.append("")
        out.append("  ⛔  Do NOT push to Notion until errors are resolved.")
    elif verdict == "WARN":
        out.append("")
        out.append("  ⚠   Push allowed but review warnings before assigning to writer.")

    return "\n".join(out)


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("path", nargs="?", help="Path to brief text file")
    parser.add_argument("--sample", action="store_true", help="Validate the embedded sample brief")
    parser.add_argument("--output", choices=["human", "json"], default="human")
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

    parsed = _text_parser.coerce_types(_text_parser.parse_brief(text))
    result = validate(parsed)

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print(render_human(result))

    # Exit non-zero only on FAIL so CI pipelines can gate on it
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
