# WCAG 2.1 Contrast Check — Lumen Notes (fictional)

Generated with `python scripts/check_contrast.py`.
Thresholds: **AA normal** ≥ 4.5:1 · **AA large** ≥ 3:1 · **AAA normal** ≥ 7:1 · **AAA large** ≥ 4.5:1

| Pair | FG | BG | Ratio | AA normal | AA large | AAA normal | AAA large |
|---|---|---|---|---|---|---|---|
| text-primary on bg | `#F8FAFC` | `#0F172A` | 17.06:1 | ✅ | ✅ | ✅ | ✅ |
| text-muted on bg | `#94A3B8` | `#0F172A` | 6.96:1 | ✅ | ✅ | ❌ | ✅ |
| accent on bg (link text) | `#10B981` | `#0F172A` | 7.04:1 | ✅ | ✅ | ✅ | ✅ |
| bg on accent (CTA label) | `#0F172A` | `#10B981` | 7.04:1 | ✅ | ✅ | ✅ | ✅ |
| text-primary on accent (anti-pattern) | `#F8FAFC` | `#10B981` | 2.42:1 | ❌ | ❌ | ❌ | ❌ |

## Findings

- The dark surface (`#0F172A`) carries the system: every primary text/icon combination
  against it lands at AAA or near-AAA.
- **Do not** put `text-primary` (white) on the accent button — it fails AA at 2.42:1.
  The implementation correctly uses the dark background color on the accent fill
  (`bg` on `accent` = 7.04:1, AAA ✅).
- `text-muted` against the base surface lands just under AAA for normal text (6.96:1)
  but comfortably above AA. Acceptable for secondary text but consider darkening if you
  want AAA across the board.

## Recommendations

- Keep the CTA contract: dark text on accent, never white text on accent.
- If you ever introduce a light theme variant, re-run this check against the inverted
  palette — the muted/subtle steps need separate verification.
