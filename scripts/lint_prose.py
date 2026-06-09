#!/usr/bin/env python3
"""Lint markdown and Python files for forbidden prose characters per
CONTRIBUTING.md: unicode em-dash (U+2014), unicode en-dash (U+2013), and
ASCII ` -- ` (double-hyphen with spaces).

Respects code fences and inline backticks (where the chars may appear as
pedagogical references or CLI examples). Exit nonzero on violations.

Allowlist (intentional content):
  - tests/test_discourse_research.py: em-dash fixtures + assertions
    verifying strip_em_dashes behaviour.
  - scripts/discourse_research.py: em-dash chars are DICT KEYS in
    EM_DASH_REPLACEMENTS (the pattern we want to MATCH, not replace).

Usage:
    python3 scripts/lint_prose.py [--root <path>]

Returns 0 on clean, 1 on violations (with file:line:context output).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FORBIDDEN = {
    "—": "U+2014 em-dash",
    "–": "U+2013 en-dash",
    " -- ": "ASCII double-hyphen with spaces",
}

# Files where the chars appear ONLY inside backticks (pedagogical uses
# documenting the rule itself) and the prose linter has no need to scan.
# The smarter check would respect inline-backtick boundaries, but a few
# files have so many that the per-file allowlist is clearer.
FILE_ALLOWLIST = {
    "tests/test_discourse_research.py",   # fixtures + assertions
    "tests/test_lint_prose.py",           # v1.8.5: intentional violation fixtures
    "scripts/discourse_research.py",      # dict keys
    "scripts/lint_prose.py",              # this file itself: dict keys + pattern data
    "skills/blog/references/synthesis-contract.md",  # pedagogical inside backticks
}


def _find_violations_in_line(line: str) -> list[tuple[str, str]]:
    """Return list of (char, description) for any forbidden chars in this
    line OUTSIDE backtick spans. Caller has already verified the line is
    not inside a code fence.

    v1.8.5 fix (6TH-AUDIT-007): mask double-backtick spans (``code``) FIRST,
    then single-backtick spans. Single-backtick regex would otherwise match
    the empty span between two opening backticks and leave content exposed.
    """
    # Mask double-backtick spans first: ``content with single ` inside``.
    masked = re.sub(r"``[^\n]*?``", lambda m: " " * len(m.group(0)), line)
    # Then mask single-backtick spans.
    masked = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), masked)
    out: list[tuple[str, str]] = []
    for char, name in FORBIDDEN.items():
        if char in masked:
            out.append((char, name))
    return out


def lint_file(path: Path) -> list[tuple[int, str, str, str]]:
    """Return list of (line_no, char, description, line_text) violations.

    v1.8.5 fix (6TH-AUDIT-006): track the OPENING fence delimiter so a
    nested fence with a different delimiter doesn't toggle state. A
    `~~~` fence is closed only by `~~~`, and a ``` fence is closed only
    by ```.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    violations: list[tuple[int, str, str, str]] = []
    # fence_open is the OPENING delimiter string (e.g. "```", "````", "~~~").
    # Per CommonMark, the closing fence must consist of >= the same number of
    # the same character. v1.8.6 (7TH-AUDIT-013) fix: track the full opening
    # string, not just the type, so a 4-backtick fence is closed only by
    # 4+ backticks; an inner ``` line does not close the outer ````.
    fence_open: str | None = None
    in_frontmatter = False
    for i, line in enumerate(text.splitlines(), 1):
        if i == 1 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            continue
        stripped = line.lstrip()
        if fence_open is None:
            m = re.match(r"(`{3,}|~{3,})", stripped)
            if m is not None:
                fence_open = m.group(1)
                continue
        else:
            # Closing fence: same char, length >= opening.
            m = re.match(r"(`{3,}|~{3,})", stripped)
            if (m is not None
                    and m.group(1)[0] == fence_open[0]
                    and len(m.group(1)) >= len(fence_open)):
                fence_open = None
            continue  # all lines inside a fence are skipped
        for char, name in _find_violations_in_line(line):
            violations.append((i, char, name, line.rstrip()))
    return violations


def gather_targets(root: Path) -> list[Path]:
    targets: list[Path] = []
    for sub in ("skills", "agents", "docs", "scripts", "tests"):
        d = root / sub
        if d.is_dir():
            targets.extend(d.rglob("*.md"))
            targets.extend(d.rglob("*.py"))
    for name in ("README.md", "SECURITY.md", "CONTRIBUTING.md", "CHANGELOG.md",
                 "CLAUDE.md", "CONTRIBUTORS.md", "PRIVACY.md", "TODO.md",
                 "NOTICE"):
        p = root / name
        if p.exists() and p.is_file():
            targets.append(p)
    return sorted(set(targets))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    total = 0
    for path in gather_targets(root):
        rel = path.relative_to(root)
        rel_str = str(rel).replace("\\", "/")
        # Exclude virtualenvs and untracked dirs.
        if any(part.startswith(".") or
               part in ("venv", ".venv", "__pycache__", "node_modules",
                        "superpowers")
               for part in rel.parts):
            continue
        if rel_str in FILE_ALLOWLIST:
            continue
        for line_no, char, name, text in lint_file(path):
            total += 1
            print(f"{rel_str}:{line_no}: {name}  {text[:120]}")
    if total > 0:
        print(f"\nFAIL: {total} prose-hygiene violations (CONTRIBUTING.md rule).")
        print("Replace with: '. ', ', ', ': ', '; ', '()', or ' - ' (hyphen).")
        return 1
    print("OK: zero prose-hygiene violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
