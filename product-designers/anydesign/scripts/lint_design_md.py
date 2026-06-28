#!/usr/bin/env python3
"""
lint_design_md.py — Validate a design.md file against the anydesign spec

Checks:
- YAML frontmatter exists and is parseable (minimal regex-based parser, no PyYAML)
- Required frontmatter fields present (version, name, source)
- Every `{token.ref}` in the body resolves to a token defined in the frontmatter
- Every component named in YAML `components:` has a matching prose heading in Section 3
- Section 6 "Do's and Don'ts" exists and is non-empty (or carries explicit abstain
  justification)
- Section 7 "Open Questions" exists and is non-empty (or "material sufficient")

Usage:
    python lint_design_md.py design.md
    python lint_design_md.py design.md --json       # machine-readable output
    python lint_design_md.py design.md --strict     # exit 1 on warnings too

Stdlib only. No pip install required.
"""

import argparse
import json
import re
import sys
from pathlib import Path

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


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TOKEN_REF_RE = re.compile(
    r"\{([a-z][a-z0-9_-]*(?:\.[a-z0-9_-]+(?:\[\d+\])?)+)\}",
    re.IGNORECASE,
)
REQUIRED_FRONTMATTER = ("version", "name", "source")


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def extract_yaml_structure(frontmatter):
    """
    Minimal YAML walker for the shape we care about. Returns:
      {
        "top_level": {key: value_or_None},     # version, name, source, captured_at, description
        "tokens": {category: set(names)},       # colors, typography, spacing, rounded, components
      }
    Comments and blank lines are skipped. We only need keys, not values.
    """
    top_level = {}
    tokens = {}
    current_category = None
    in_description = False

    for raw in frontmatter.split("\n"):
        # Strip trailing whitespace but preserve indent
        line = raw.rstrip()
        if not line or line.strip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        # Track when we're inside a multi-line `description: |` block
        if in_description:
            if indent == 0:
                in_description = False
            else:
                continue

        m = re.match(r"^([a-zA-Z][a-zA-Z0-9_-]*)\s*:\s*(.*)$", stripped)
        if not m:
            continue

        key, val = m.group(1), m.group(2)

        if indent == 0:
            top_level[key] = val if val else None
            if key in ("colors", "typography", "spacing", "rounded", "components"):
                current_category = key
                tokens[current_category] = set()
            else:
                current_category = None
                if key == "description" and val in ("|", ">"):
                    in_description = True

        elif indent == 2 and current_category is not None:
            # one-level-down child of a category
            tokens[current_category].add(key)

    return {"top_level": top_level, "tokens": tokens}


def extract_token_refs(body):
    """Return list of (ref_string, line_number) tuples for every {ref} in body."""
    out = []
    for i, line in enumerate(body.split("\n"), 1):
        for m in TOKEN_REF_RE.finditer(line):
            out.append((m.group(1), i))
    return out


def resolve_ref(ref, tokens):
    """Check if a dotted ref resolves to a known token. Examples:
       colors.primary -> tokens['colors'] contains 'primary'
       typography.display.fontSize -> tokens['typography'] contains 'display'
       spacing.scale[4] -> tokens['spacing'] contains 'scale'
    """
    parts = ref.split(".")
    if len(parts) < 2:
        return False
    category = parts[0]
    if category not in tokens:
        return False
    # Strip array indices like 'scale[4]' -> 'scale'
    name = re.sub(r"\[\d+\]", "", parts[1])
    return name in tokens[category]


def extract_section(body, section_number):
    """Return the text of `## N. <title>` section up to the next `## ` heading."""
    pattern = rf"^##\s+{section_number}\.\s.*?\n(.*?)(?=^##\s+\d+\.\s|\Z)"
    m = re.search(pattern, body, re.DOTALL | re.MULTILINE)
    return m.group(1) if m else None


def normalize_component_name(s):
    """Map prose heading like 'Button — primary' to YAML key 'button-primary'."""
    s = s.strip()
    # Drop parenthetical notes
    s = re.split(r"\s*\(", s)[0]
    # Replace em/en dashes with hyphen
    s = re.sub(r"\s+[—–]\s+", "-", s)
    s = re.sub(r"\s+/\s+", "-", s)
    # Collapse spaces to hyphens
    s = re.sub(r"\s+", "-", s)
    return s.lower()


def extract_prose_component_names(body):
    """Pull h4 ('#### ...') headings from Section 3."""
    section3 = extract_section(body, 3)
    if section3 is None:
        return []
    names = []
    for line in section3.split("\n"):
        m = re.match(r"^####\s+(.+)$", line)
        if m:
            names.append(normalize_component_name(m.group(1)))
    return names


def section_has_content(body, section_number, abstain_phrases):
    """
    Check whether a section has substantive content OR carries an abstain justification.
    Returns: (ok: bool, summary: str)
    """
    text = extract_section(body, section_number)
    if text is None:
        return False, f"Section {section_number} not found"
    # Count bulleted items
    bullet_count = len(re.findall(r"^\s*[-*]\s+\S", text, re.MULTILINE))
    if bullet_count > 0:
        return True, f"{bullet_count} bullets"
    # Check abstain phrases
    lower = text.lower()
    for phrase in abstain_phrases:
        if phrase in lower:
            return True, f"abstain justification present ('{phrase}')"
    return False, "no bullets and no abstain justification"


def check_dos_donts(body):
    text = extract_section(body, 6)
    if text is None:
        return {"status": "fail", "msg": "Section 6 'Do's and Don'ts' not found"}
    # Count rule bullets in Do / Don't subsections
    do_match = re.search(r"###\s+Do\s*\n(.*?)(?=###\s+Don|\Z)", text, re.DOTALL)
    dont_match = re.search(r"###\s+Don[''`]t\s*\n(.*?)\Z", text, re.DOTALL)
    do_count = len(re.findall(r"^\s*[-*]\s+", do_match.group(1), re.MULTILINE)) if do_match else 0
    dont_count = len(re.findall(r"^\s*[-*]\s+", dont_match.group(1), re.MULTILINE)) if dont_match else 0
    if do_count == 0 and dont_count == 0:
        if "insufficient evidence" in text.lower():
            return {"status": "pass", "msg": "abstain justification present"}
        return {"status": "fail", "msg": "no Do or Don't rules and no abstain justification"}
    return {
        "status": "pass" if do_count >= 3 and dont_count >= 3 else "warn",
        "msg": f"{do_count} Do's, {dont_count} Don'ts (target: 5-7 each)",
    }


def lint(path):
    """Run all checks. Returns list of {check, status, msg} dicts."""
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    results = []

    # 1. Frontmatter exists
    if fm is None:
        results.append({"check": "frontmatter-exists", "status": "fail",
                        "msg": "No YAML frontmatter block found (expected ---...--- at file start)"})
        return results, body, None
    results.append({"check": "frontmatter-exists", "status": "pass",
                    "msg": f"frontmatter parsed ({len(fm.splitlines())} lines)"})

    structure = extract_yaml_structure(fm)

    # 2. Required fields
    missing = [f for f in REQUIRED_FRONTMATTER if f not in structure["top_level"]]
    if missing:
        results.append({"check": "required-fields", "status": "fail",
                        "msg": f"missing required field(s): {', '.join(missing)}"})
    else:
        results.append({"check": "required-fields", "status": "pass",
                        "msg": f"all required fields present: {', '.join(REQUIRED_FRONTMATTER)}"})

    # 3. Token refs resolve
    refs = extract_token_refs(body)
    unresolved = [(r, ln) for r, ln in refs if not resolve_ref(r, structure["tokens"])]
    if not refs:
        results.append({"check": "token-refs", "status": "warn",
                        "msg": "no {token.ref} found in body — consider using them for refactor safety"})
    elif unresolved:
        sample = ", ".join(f"{{{r}}}@L{ln}" for r, ln in unresolved[:5])
        results.append({"check": "token-refs", "status": "fail",
                        "msg": f"{len(unresolved)} unresolved ref(s) of {len(refs)} total. Examples: {sample}"})
    else:
        results.append({"check": "token-refs", "status": "pass",
                        "msg": f"all {len(refs)} refs resolve to frontmatter tokens"})

    # 4. Component 1:1 mapping
    yaml_components = structure["tokens"].get("components", set())
    prose_components = set(extract_prose_component_names(body))
    if yaml_components:
        missing_in_prose = yaml_components - prose_components
        extra_in_prose = prose_components - yaml_components
        if missing_in_prose or extra_in_prose:
            parts = []
            if missing_in_prose:
                parts.append(f"in YAML but missing from prose: {sorted(missing_in_prose)}")
            if extra_in_prose:
                parts.append(f"in prose but missing from YAML: {sorted(extra_in_prose)}")
            results.append({"check": "components-1:1", "status": "warn",
                            "msg": " | ".join(parts)})
        else:
            results.append({"check": "components-1:1", "status": "pass",
                            "msg": f"all {len(yaml_components)} components match between YAML and prose"})
    else:
        results.append({"check": "components-1:1", "status": "warn",
                        "msg": "no components: block in YAML frontmatter — skipping 1:1 check"})

    # 5. Do's and Don'ts
    dd = check_dos_donts(body)
    results.append({"check": "dos-donts", "status": dd["status"], "msg": dd["msg"]})

    # 6. Open Questions
    oq_ok, oq_msg = section_has_content(
        body, 7, abstain_phrases=("material sufficient", "no open questions"),
    )
    results.append({"check": "open-questions", "status": "pass" if oq_ok else "fail",
                    "msg": oq_msg})

    return results, body, structure


STATUS_SYMBOLS = {"pass": "✓", "warn": "⚠", "fail": "✗"}


def format_text_report(results, path):
    lines = [f"Lint report — {path}", "=" * 60]
    for r in results:
        sym = STATUS_SYMBOLS.get(r["status"], "?")
        lines.append(f"{sym} {r['check']}: {r['msg']}")
    failures = sum(1 for r in results if r["status"] == "fail")
    warnings = sum(1 for r in results if r["status"] == "warn")
    passes = sum(1 for r in results if r["status"] == "pass")
    lines.append("-" * 60)
    lines.append(f"  {passes} pass · {warnings} warn · {failures} fail")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Validate a design.md against the anydesign spec.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("path", help="Path to the design.md to lint")
    parser.add_argument("--json", dest="as_json", action="store_true",
                        help="Emit JSON instead of a text report.")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 on warnings (not just failures).")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(2)

    results, _, _ = lint(path)

    if args.as_json:
        print(json.dumps({"file": str(path), "results": results}, indent=2))
    else:
        print(format_text_report(results, path))

    fail = any(r["status"] == "fail" for r in results)
    warn = any(r["status"] == "warn" for r in results)
    if fail or (args.strict and warn):
        sys.exit(1)


if __name__ == "__main__":
    main()
