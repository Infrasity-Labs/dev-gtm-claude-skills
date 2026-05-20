---
name: growth-report
description: >
  Generates a 3-month SEO performance HTML report for any domain using DataForSEO data.
  Fetches baseline vs current traffic, keyword rankings, top content pages, and competitive
  landscape, then outputs a polished dark-theme HTML report styled like an executive briefing.
  Use this skill whenever a user provides a target domain and a list of competitor URLs and asks
  for an SEO report, performance report, SEO analysis, competitive SEO comparison, traffic report,
  ranking report, or 3-month SEO summary. Also trigger when the user says "generate SEO report for
  X vs Y and Z", "create a performance report", "compare my SEO against competitors", or pastes a
  domain and asks how it's performing versus the market. Always use this skill for SEO report
  generation — do not attempt to build the report without following this structured data-fetch and
  HTML generation workflow.
user-invokable: true
argument-hint: "[target_domain] [competitor1] [competitor2] ..."
license: MIT
metadata:
  author: Infrasity
  version: "1.1.0"
  category: seo
---

# SEO Performance Report Skill

Generates a comprehensive 3-month SEO performance HTML report using live DataForSEO data.
The report covers traffic trends, keyword rankings, top content clusters, competitive positioning,
strategic priorities, and an executive summary — all in a dark-theme executive-ready HTML file.

---

## STEP 0 — COLLECT ALL INPUTS BEFORE DOING ANYTHING

**All four inputs are mandatory.** Do not make any API calls until all four are confirmed.

Collect them in a single message using this exact format — ask for everything at once, never
ask for inputs one at a time:

---

**If the user has NOT provided all four inputs**, ask:

> To generate the report I need 4 things:
>
> 1. **Target domain** — the site to report on
> 2. **Competitor domains** — up to 5–6 competitors
> 3. **Date range** — start and end date for the 3-month window
> 4. **Location** — country for search data
>

---

**If the user has already provided the target domain and competitors** (e.g. "generate SEO report
for firefly.ai vs spacelift.io, env0.com"), confirm the two optional inputs:

> Got it — I'll generate the report for **firefly.ai** vs spacelift.io, env0.com.
>
> Just confirming the defaults:
> - **Date range:** Feb 20 → May 20, 2026
> - **Location:** United States
>
> OK to proceed with these, or would you like to change either?

---

**Input parsing rules:**

| Input | Rules |
|---|---|
| `TARGET_DOMAIN` | Strip `https://`, `http://`, `www.`, and trailing slashes. Store bare domain only (e.g. `firefly.ai`) |
| `COMPETITORS` | Strip same prefixes from each. Accept comma-separated or space-separated list. Min 2, max 6 competitors. |
| `START_DATE` | Parse any human date format → `YYYY-MM-DD`. Default: `2026-02-20` |
| `END_DATE` | Parse any human date format → `YYYY-MM-DD`. Default: `2026-05-20` |
| `LOCATION` | Accept country name. Default: `United States`. Must be a valid DataForSEO `location_name` (full country name only, never city or region). |

**After confirmation, echo back the resolved inputs clearly before proceeding:**

> ✓ **Target:** firefly.ai
> ✓ **Competitors:** spacelift.io, env0.com, controlmonkey.io, scalr.com, terraform.io
> ✓ **Date range:** Feb 20, 2026 → May 20, 2026
> ✓ **Location:** United States
>
> Fetching data now...

---

## CRITICAL API SETTINGS

**Always use `ignore_synonyms: false` on every DataForSEO call.**
Using the default `ignore_synonyms: true` underreports traffic and keyword counts by 30–50%.
This is the single most important parameter to get right — never omit it.

---

## STEP 1 — Baseline Metrics

Call `dataforseo_labs_google_historical_rank_overview` with:
```
target:        TARGET_DOMAIN
location_name: LOCATION
language_code: en
ignore_synonyms: false
```

From the returned monthly array, find the snapshot **closest to START_DATE** (match by year+month).
Extract and store:
- `baseline_traffic`  = `metrics.organic.etv`
- `baseline_keywords` = `metrics.organic.count`
- `baseline_top3`     = `metrics.organic.pos_1` + `metrics.organic.pos_2_3`

> ⚠️ There is NO `pos_1_3` field in DataForSEO. Always compute Top 3 as `pos_1 + pos_2_3`.

Also extract **all monthly snapshots** between START_DATE and END_DATE for the traffic trend
bars in the report (typically 3–4 data points):
- For each snapshot store: `month_label` (e.g. "Feb 2026"), `etv`, `year`, `month`
- Sort ascending by date
- These become `TREND_LABEL_1..4`, `TREND_ETV_1..4` in the HTML template

---

## STEP 2 — Current Metrics

Call `dataforseo_labs_google_domain_rank_overview` with:
```
target:        TARGET_DOMAIN
location_name: LOCATION
language_code: en
ignore_synonyms: false
```

Extract from `metrics.organic`:
- `current_traffic`     = `etv`
- `current_keywords`    = `count`
- `current_top3`        = `pos_1` + `pos_2_3`
- `current_pos_1`       = `pos_1`
- `current_pos_2_3`     = `pos_2_3`
- `current_pos_4_10`    = `pos_4_10`
- `current_pos_11_20`   = `pos_11_20`
- `current_pos_21_100`  = sum of `pos_21_30` + `pos_31_40` + `pos_41_50` + `pos_51_60` + `pos_61_70` + `pos_71_80` + `pos_81_90` + `pos_91_100`

Calculate all deltas:
```
traffic_growth_pct  = ((current_traffic - baseline_traffic) / baseline_traffic) * 100
keywords_change     = current_keywords - baseline_keywords
keywords_change_pct = (keywords_change / baseline_keywords) * 100
top3_growth_pct     = ((current_top3 - baseline_top3) / baseline_top3) * 100
```

Format rules:
- Prefix `+` for positive values, `-` is automatic for negative
- Round all percentages to 1 decimal place
- Add `pos` CSS class for positive deltas, `neg` for negative

---

## STEP 3 — Competitive Landscape

Call `dataforseo_labs_bulk_traffic_estimation` with:
```
targets:       [TARGET_DOMAIN, ...COMPETITORS]   ← all domains in a single API call
location_name: LOCATION
language_code: en
item_types:    ["organic"]
ignore_synonyms: false
```

For each domain returned, extract: `etv`, `count`.

Sort all domains **descending by etv**. Assign rank 1 = highest traffic.
Determine:
- `competitive_rank`   = rank position of TARGET_DOMAIN (1 = #1)
- `total_domains`      = total count of all domains in the table
- `domain_above`       = domain ranked one position above TARGET_DOMAIN (if any)
- `domain_below`       = domain ranked one position below TARGET_DOMAIN (if any)
- `gap_to_next_above`  = etv of domain_above − current_traffic (0 if TARGET_DOMAIN is #1)
- `lead_over_next_below` = current_traffic − etv of domain_below (0 if TARGET_DOMAIN is last)

**Trend assignment for the table:**
- TARGET_DOMAIN: derive from `traffic_growth_pct` → `↑ +X%` (green) if positive, `↓ -X%` (red) if negative, `→ Stable` (gray) if within ±5%
- Competitors: use `"Stable"` (gray) as default unless there is clear evidence of growth/decline

---

## STEP 4 — Top Content Clusters

Call `dataforseo_labs_google_relevant_pages` with:
```
target:        TARGET_DOMAIN
location_name: LOCATION
language_code: en
order_by:      ["metrics.organic.etv,desc"]
limit:         3
ignore_synonyms: false
```

For each of the top 3 pages extract:
- `page_address` — shorten display URL: remove `https://www.` prefix, keep path
- `metrics.organic.etv`   → page_etv (format with commas, round to nearest integer)
- `metrics.organic.count` → page_keywords

**Homepage concentration check:**
If `page_1_etv / current_traffic > 0.80`, set `homepage_concentration = true`.
This triggers a specific paragraph in the executive summary.

---

## STEP 5 — Derive Report Targets (Q2 Card)

```
IF traffic_growth_pct >= 0:
  traffic_goal   = round(current_traffic * (1 + traffic_growth_pct/100))
ELSE:
  traffic_goal   = round(baseline_traffic * 0.9)   ← recovery target

keywords_goal    = max(round(current_keywords * 1.2), round(baseline_keywords * 0.95))
top3_goal        = round(current_top3 * 1.3)

IF competitive_rank == 1:
  target_badge = "Maintain #1"
ELSE:
  target_badge = "Challenge #" + str(competitive_rank - 1)
```

Format traffic_goal as e.g. `62,000+`. Round to nearest thousand for clean presentation.

---

## STEP 6 — Derive Strategic Priority Cards

Always generate exactly 6 cards. Use actual data values in every description — no generic text.

| # | Card title formula | Content rule |
|---|---|---|
| 1 | "Close Gap to #[rank_above]" | Name domain_above, state gap_to_next_above as ETV, suggest content angle |
| 2 | "Defend vs. #[rank_below_number]" | Name domain_below, state lead_over_next_below, advise on sustaining velocity |
| 3 | Traffic recovery OR scale | If declined: "Reverse the [X]% Decline" with pos_4_10 count as pipeline. If grew: "Sustain [X]% Growth Trajectory" |
| 4 | "Scale Top Content Clusters" | Reference page_1 URL and its ETV; flag homepage concentration if true |
| 5 | "Recover/Expand Keyword Coverage" | Use keywords_change as the specific number to recover or build on |
| 6 | "Convert Pos 4–10 to Top 3" | Use current_pos_4_10 count; state that converting 20% would add ~N new top-3 rankings |

---

## STEP 7 — Derive Executive Summary (4 paragraphs)

Write naturally — no bullet points inside the paragraphs. All numbers must be real API values.

- **Para 1:** Overall result. State traffic_growth_pct, competitive_rank of total_domains, whether
  TARGET_DOMAIN is the fastest growing in the set (compare to competitors' trend badges).
  Name the domains ranked immediately above and below with their ETVs.

- **Para 2:** If `homepage_concentration = true`: flag that X% of traffic comes from one page,
  frame it as both a risk and an opportunity to diversify.
  Otherwise: describe content breadth advantage — keyword count vs competitors.

- **Para 3:** Top 3 keywords trend (top3_growth_pct). Flag keywords_change — if negative,
  state the specific number lost and the urgency to recapture. If positive, call it momentum.

- **Para 4:** Q2 strategy. Name the specific gap to close (gap_to_next_above), the competitor
  to chase (domain_above), and the recovery/scale action most impactful based on the data.

**Summary badge format:**
`Rank #[competitive_rank] | [current_traffic_K]K Traffic | [traffic_growth_pct]% Growth | [current_top3] Top-3 Keywords | [Fastest Growing / Declining / Stable]`

---

## STEP 8 — Generate the HTML Report

Read `references/html-template.md` for the complete HTML structure, CSS, and variable map.

Fill every `{{VARIABLE}}` with real data. Output the file to:
```
/mnt/user-data/outputs/{TARGET_DOMAIN}_seo_report.html
```

Then call `present_files` to deliver it to the user.

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Domain returns no data from bulk_traffic_estimation | Omit that domain from the competitive table; add a footnote |
| Historical snapshot missing for START_DATE month | Use nearest available month; note actual date used in report footer |
| `baseline_top3` or `baseline_traffic` is 0 (division by zero) | Set the corresponding growth % to "N/A" and skip the delta badge |
| `backlinks_bulk_ranks` 40204 error | Do not call this endpoint — it requires a separate subscription. Skip entirely. |
| `ai_opt_llm_ment_agg_metrics` 40204 error | Do not include AI citations section. It is excluded from this skill. |

---

## WHAT NOT TO INCLUDE

- ❌ **No AI/LLM citation section** — excluded by design (requires paid DataForSEO add-on)
- ❌ **No DFS Rank (0–1000) column** — excluded by design (requires separate subscription)
- ❌ **No `ignore_synonyms: true`** — always `false`, no exceptions
- ❌ **No placeholder text** — every number in the HTML must come from a real API response
- ❌ **No asking for inputs one at a time** — always collect all missing inputs in a single message

---

## REFERENCE FILES

- `references/html-template.md` — Full HTML template with CSS, all section markup, and complete
  variable substitution map. **Always read this file before writing any HTML.**