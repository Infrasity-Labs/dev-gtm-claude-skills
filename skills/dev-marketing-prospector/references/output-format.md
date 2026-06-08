# Output Format Reference

## Badge Colours by Funding Stage

| Stage | Background | Text colour |
|---|---|---|
| Bootstrapped / Breakeven | `#F1EFE8` | `#5F5E5A` |
| Beta / Pre-revenue | `#FAEEDA` | `#854F0B` |
| Pre-seed | `#FAEEDA` | `#854F0B` |
| Seed | `#EAF3DE` | `#3B6D11` |
| Series A | `#E6F1FB` | `#185FA5` |
| Series B | `#EEEDFE` | `#3C3489` |
| Series C+ | `#FBEAF0` | `#993556` |

---

## Table Sort Order

Always sort rows by funding stage, earliest to latest:

Bootstrap → Pre-seed/Beta → Seed → Series A → Series B → Series C+

Within the same funding stage, sort alphabetically by company name.

---

## Header Bar Content

The table header bar must always show:

- Left: vertical name + "— Exact Vertical" or "— Full Landscape" depending on
  whether a funding cap is applied
- Right: count of companies + cap status (e.g. "8 companies · ≤50 headcount ·
  Pre-seed → Series A" or "11 companies · No funding cap · No headcount cap")

---

## Filter Tags

Always show filter tags below the header bar. Standard tags:

- The vertical name (exact wording the user gave)
- Headcount filter (e.g. "Headcount < 50") or "No headcount cap"
- Funding range (e.g. "Pre-seed → Series A") or "No funding cap"
- "SaaS / Product-led" (always present)
- "Exact vertical only" (always present)
- "All data sourced" (always present — signals the sourcing standard)

---

## Column Widths (min-width 1320px table, horizontally scrollable)

| Column | Width |
|---|---|
| Company (name + badge + headcount) | 115px |
| URL | 75px |
| LinkedIn | 80px |
| Headcount | 58px |
| Signal + Why Dev Marketing | 195px |
| Signal Sources | 130px |
| Geography | 80px |
| Pain Point | 195px |
| Pain Point Sources | 145px |

Total: ~1073px minimum. Set min-width: 1073px on the table and wrap in a
horizontally scrollable <div class="wrap">.

---

## Company Cell Content

Each company cell must contain, in order:

1. Company name — `font-weight: 500`, `font-size: 12.5px`
2. Funding badge — colour per stage table above
3. Sub-line: `Founded YYYY` in muted 10px text
4. Optional: one-line phase descriptor of what the company specifically
   does in the vertical (e.g. "Durable AI workflow orchestration")

---

## Signal Cell Content

2–4 sentences. Include:

- The specific trigger event (round, launch, partnership, award) with
  amount, date, and lead investor where applicable
- A direct connection to why developer marketing is relevant for this
  company right now — do not leave this implicit

---

## Signal Sources Cell Content

A compact numbered list. Each entry is a clickable link:

```html
<ul class="src-list">
  <li>
    <a href="https://..." target="_blank">
      <span class="ref-num">S1</span>
      Source label — what data point it proves
    </a>
  </li>
</ul>
```

Format for the ref-num span:
- `background: var(--color-background-secondary)`
- `border: 0.5px solid var(--color-border-secondary)`
- `border-radius: 3px`
- `font-size: 9px`
- `padding: 0 3px`
- `color: var(--color-text-secondary)`

Keep source labels to ~6 words. The label must describe what the source
proves, not just the source name. Examples:
- "PitchBook — funding & headcount" ✓
- "Sacra — 32k downloads, 35x YoY" ✓
- "PitchBook" ✗ (too vague)

---

## Pain Point Cell Content

2–4 sentences. Must:

- Reference specific numbers and competitor context
- State the consequence clearly — what happens if they don't fix the gap
- Never be generic ("they need more awareness")

If a claim in the pain point is self-reported by the company (not
independently verified), add this warning badge directly in the cell:

```html
<span class="warn">⚠ [Stat] is self-reported by [Company] — not independently verified</span>
```

Warning badge CSS:
- `background: #FAEEDA`
- `color: #633806`
- `font-size: 9px`
- `padding: 1px 4px`
- `border-radius: 3px`
- `display: inline-block`
- `margin-top: 2px`

---

## Pain Point Sources Cell Content

Same format as Signal Sources but using P1, P2... reference numbers.

For inferred claims (logical conclusions from multiple data points, not
directly cited statistics), add an inline italic note beneath the source list:

```html
<span style="font-size:10px;color:var(--color-text-secondary);
display:block;margin-top:4px;font-style:italic;">
Note: "[claim]" is inferred from [underlying sources] — not a cited stat.
</span>
```

---

## Three-Tier Source Classification

Apply to every data point in both the signal and pain point columns:

| Tier | Definition | Treatment in table |
|---|---|---|
| **Directly sourced** | Verifiable stat from a credible third-party source | Link only — no flag |
| **Self-reported** | Company's own claim from their blog, press release, or CEO statement | ⚠ warning badge in the cell where it appears |
| **Inferred** | Logical conclusion drawn from two or more sourced numbers | Italic note in the sources cell explaining the inference |

When tracing a self-reported stat: always find the original source (company
blog or CEO quote), not a third-party article that repeats it. The source URL
must point to where the claim first appeared.

---

## Geography Cell Content

Country flag emoji + country name + city/region on a separate sub-line in
muted text.

Examples:
- 🇺🇸 USA · San Francisco, CA
- 🇬🇧 UK · London
- 🇩🇪 Germany · Berlin
- 🇮🇳 India · Bangalore
- 🇸🇬 Singapore
- 🇧🇷 Brazil · São Paulo
- 🇪🇸 Spain · Barcelona

---

## Footer Line

Always include below the table:

```
All source links open in a new tab. ⚠ = self-reported company claim, not
independently verified. Revenue and headcount figures marked as estimates are
third-party algorithmic estimates, not company-disclosed numbers.
```

Font: 10px, `color: var(--color-text-secondary)`.

---

## Note Box (when list is short)

If the list contains fewer than 5 companies due to criteria strictness, add a
note box above the table explaining why. Use:

- Left border: `3px solid #E24B4A`
- Background: `var(--color-background-secondary)`
- Font size: 12px
- Content: explain the specific reason the list is short and what the user
  can do (e.g. remove the funding cap or widen the headcount limit)
