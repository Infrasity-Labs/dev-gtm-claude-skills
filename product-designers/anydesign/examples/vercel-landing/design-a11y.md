# WCAG 2.1 Contrast Check — Vercel landing (Geist palette)

Thresholds: **AA normal** ≥ 4.5:1 · **AA large** ≥ 3:1 · **AAA normal** ≥ 7:1 · **AAA large** ≥ 4.5:1

| Pair | FG | BG | Ratio | AA normal | AA large | AAA normal | AAA large |
|---|---|---|---|---|---|---|---|
| text on background | `#171717` | `#FFFFFF` | 17.93:1 | ✅ | ✅ | ✅ | ✅ |
| text-muted on background | `#4D4D4D` | `#FFFFFF` | 8.45:1 | ✅ | ✅ | ✅ | ✅ |
| CTA label on primary | `#FFFFFF` | `#171717` | 17.93:1 | ✅ | ✅ | ✅ | ✅ |
| focus blue on background | `#0070F7` | `#FFFFFF` | 4.51:1 | ✅ | ✅ | ❌ | ✅ |
| gray-100 surface boundary (info only) | `#F2F2F2` | `#FFFFFF` | 1.12:1 | ❌ | ❌ | ❌ | ❌ |

## Findings

- **Primary text combinations land at AAA.** `--ds-gray-1000` (#171717) on
  `--ds-background-100` (#FFFFFF) hits 17.93:1 — well above AAA 7:1. The same ratio holds
  for the inverted CTA (white text on near-black button) since contrast is symmetric.
- **`--ds-gray-900` muted text passes AAA at 8.45:1.** This is the color used for secondary
  body copy on the landing — robust accessibility headroom.
- **`--ds-blue-700` (focus color) at 4.51:1 is at the AA-normal edge.** This is the
  *focus ring color*, not body text, so 4.51:1 is acceptable for its role. If Vercel ever
  uses this same blue for an inline text link on white, it would barely pass AA-normal and
  fail AAA-normal. Worth flagging.
- **Last row is intentional non-text.** `--ds-gray-100` against `--ds-background-100` is
  a *surface separator*, not a text/foreground pair — WCAG 1.4.11 (non-text contrast)
  applies a different threshold (3:1). At 1.12:1, this is decorative only and is fine for
  its role (e.g., subtle section dividers). Listed here purely for transparency.

## Recommendations

- No changes needed for the observed text combinations — the system is solid at AAA across
  the body copy palette.
- If extending the brand: any new text/icon color introduced on white should aim for ≥ 7:1
  to keep parity with the existing tier.
- Re-run this check with a dark-mode palette if Vercel ships theming variants for the
  landing.
