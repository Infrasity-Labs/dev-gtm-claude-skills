---
name: analytics-report
description: >
  Generates a weekly analytics report for infrasity.com using live Google Search Console and
  GA4 data, builds a styled HTML report, saves it as a downloadable file, and posts a summary
  to a Slack channel. Fetches GSC performance (clicks, impressions, CTR, position, top pages,
  top queries) and GA4 performance (sessions, users, new users, pageviews, conversions,
  engagement rate, bounce rate, avg session duration, channel breakdown, and AI/LLM traffic
  with the full source × medium × landing page cross-dimensional table).
  Trigger this skill when asked to run the weekly report, generate the analytics report,
  send the weekly summary to Slack, or check this week's performance.
user-invokable: true
argument-hint: "[slack_channel]"
license: MIT
metadata:
  author: Infrasity
  version: "1.0.0"
  category: analytics
---

# Weekly Analytics Report

Fetches live GSC + GA4 data for the last 7 days vs the prior 7 days, builds a complete
HTML report, saves it as a downloadable file, and posts a summary to Slack.

---

## TOOLS REQUIRED

- `GSC-GA4:get_gsc_report` — Google Search Console data
- `GSC-GA4:get_ga4_report` — Google Analytics 4 data
- `GSC-GA4:save_report` — saves the finished HTML and returns a public URL
- Slack MCP — posts the summary message to the target channel

---

## STEP 0 — CONFIRM SLACK CHANNEL

If a Slack channel was not provided as an argument, ask:

> Which Slack channel should I send the weekly report to? (e.g. `#analytics`, `#growth`)

Do not proceed until the channel is confirmed. Store it as `SLACK_CHANNEL`.

---

## STEP 1 — FETCH DATA

Call both tools with no date parameters. They auto-default to the last 7 days vs the
prior 7 days and return the period dates in the response.

```
GSC-GA4:get_gsc_report()
GSC-GA4:get_ga4_report()
```

Store the full responses as `GSC` and `GA4`.

After both calls complete, extract and store the period dates for use in report headers:

```
CURRENT_START  = GSC.period.current.startDate    e.g. "2026-05-27"
CURRENT_END    = GSC.period.current.endDate      e.g. "2026-06-02"
PREVIOUS_START = GSC.period.previous.startDate   e.g. "2026-05-20"
PREVIOUS_END   = GSC.period.previous.endDate     e.g. "2026-05-26"
```

Format dates for display as "May 27 – Jun 2, 2026" (short month, day range, year).

---

## STEP 2 — PARSE DATA

### 2a — Pre-compute values not returned directly by the API

**Avg session duration in mm:ss**
```
secs = GA4.overview.avg_session_duration_secs.current
duration_display = floor(secs / 60) + "m " + (secs % 60 | 0) + "s"
```

**Channels totals row** (API does not return a pre-aggregated total)
```
total_sessions_cur  = sum of channels[].sessions
total_sessions_prev = sum of channels[].previous_sessions
total_sessions_pct  = round((total_sessions_cur - total_sessions_prev) / total_sessions_prev * 100, 1) + "%"
(same for users and pageviews)
```

**Position change direction** (lower number = better rank)
- If `overview.average_position.current` < `overview.average_position.previous` → label "↑ improved"
- If `overview.average_position.current` > `overview.average_position.previous` → label "↓ dropped"
- If equal → label "→ no change"

**Bounce rate direction** (lower = better)
- If bounce_rate decreased → "↑ improved"
- If bounce_rate increased → "↓ worse"

**"new" badge logic for pages and queries**
- If `previous_clicks = 0` and `clicks_change = "N/A"` → mark as NEW (show "new" badge, show "—" for previous column)

**AI/LLM source dot colors**
- `chatgpt.com` → green (#10a37f)
- `perplexity.ai` → purple (#6366f1)
- `claude.ai` → amber (#d97706)
- any other source → gray

### 2b — Data sections to use in report (exact field paths)

#### GSC overview (4 KPI cards)
| Card | Current | Previous | Change |
|---|---|---|---|
| Clicks | `overview.clicks.current` | `overview.clicks.previous` | `overview.clicks.change` |
| Impressions | `overview.impressions.current` | `overview.impressions.previous` | `overview.impressions.change` |
| Avg CTR | `overview.ctr_pct.current` + "%" | `overview.ctr_pct.previous` + "%" | `overview.ctr_pct.change` |
| Avg position | `overview.average_position.current` | `overview.average_position.previous` | computed in 2a |

#### GSC top pages table (all rows from top_pages[])
| Column | Field path | Format |
|---|---|---|
| Page | `top_pages[n].page` | Strip domain, keep /path only. Add "new" badge if previous_clicks = 0 |
| Clicks cur | `top_pages[n].clicks` | Integer |
| Clicks prev | `top_pages[n].previous_clicks` | Integer · "—" if new |
| Clicks Δ | `top_pages[n].clicks_change` | "↑ +10%" / "↓ −68.8%" / "N/A" |
| Impressions cur | `top_pages[n].impressions` | Formatted integer (commas) |
| Impressions prev | `top_pages[n].previous_impressions` | Integer · "—" if new |
| Impressions Δ | `top_pages[n].impressions_change` | "↑ / ↓ / N/A" |
| CTR | `top_pages[n].ctr` + "%" | Current week only — no previous available |
| Position | `top_pages[n].position` (1 decimal) | Current week only — no previous available |

#### GSC top queries table (all rows from top_queries[])
| Column | Field path | Format |
|---|---|---|
| Query | `top_queries[n].query` | Raw string. Add "new" badge if previous_clicks = 0 |
| Clicks cur | `top_queries[n].clicks` | Integer |
| Clicks prev | `top_queries[n].previous_clicks` | Integer · "—" if N/A |
| Clicks Δ | `top_queries[n].clicks_change` | "↑ / ↓ / N/A" |
| Impressions cur | `top_queries[n].impressions` | Integer |
| Impressions prev | `top_queries[n].previous_impressions` | Integer · "—" if N/A |
| Impressions Δ | `top_queries[n].impressions_change` | "↑ / ↓ / N/A" |
| CTR | `top_queries[n].ctr` + "%" | Current week only — no previous available |
| Position | `top_queries[n].position` (1 decimal) | Current week only — no previous available |

#### GA4 overview (8 KPI cards)
| Card | Current | Previous | Change |
|---|---|---|---|
| Sessions | `overview.sessions.current` | `overview.sessions.previous` | `overview.sessions.change` |
| Users | `overview.users.current` | `overview.users.previous` | `overview.users.change` |
| New users | `overview.new_users.current` | `overview.new_users.previous` | `overview.new_users.change` |
| Pageviews | `overview.pageviews.current` | `overview.pageviews.previous` | `overview.pageviews.change` |
| Conversions | `overview.conversions.current` | `overview.conversions.previous` | `overview.conversions.change` |
| Engagement rate | `overview.engagement_rate_pct.current` + "%" | `overview.engagement_rate_pct.previous` + "%" | `overview.engagement_rate_pct.change` |
| Bounce rate | `overview.bounce_rate_pct.current` + "%" | `overview.bounce_rate_pct.previous` + "%" | computed in 2a (inverted) |
| Avg duration | `duration_display` from 2a | `avg_session_duration_secs.previous` → same conversion | `overview.avg_session_duration_secs.change` |

#### GA4 channels table (all rows from channels[])
| Column | Field path | Format |
|---|---|---|
| Channel | `channels[n].channel` | Raw string |
| Sessions cur | `channels[n].sessions` | Integer |
| Sessions prev | `channels[n].previous_sessions` | Integer |
| Sessions Δ | `channels[n].sessions_change` | "↑ / ↓ + %" |
| Users cur | `channels[n].users` | Integer |
| Users prev | `channels[n].previous_users` | Integer |
| Users Δ | `channels[n].users_change` | "↑ / ↓ + %" |
| Pageviews cur | `channels[n].pageviews` | Integer |
| Pageviews prev | `channels[n].previous_pageviews` | Integer |
| Pageviews Δ | `channels[n].pageviews_change` | "↑ / ↓ + %" |
| Totals row | Computed in 2a | Sum of all channels |

#### AI/LLM totals (3 KPI cards)
| Card | Current | Previous | Change |
|---|---|---|---|
| Engaged sessions | `ai_llm_traffic.totals.engaged_sessions.current` | `.previous` | `.change` |
| Total users | `ai_llm_traffic.totals.total_users.current` | `.previous` | `.change` |
| New users | `ai_llm_traffic.totals.new_users.current` | `.previous` | `.change` |

#### AI/LLM cross-dimensional table (all rows from ai_llm_traffic.table[])
| Column | Field path | Format |
|---|---|---|
| Source | `ai_llm_traffic.table[n].source` | With colored dot per 2a |
| Medium | `ai_llm_traffic.table[n].medium` | Monospace |
| Landing page | `ai_llm_traffic.table[n].landing_page` | Full path including query string |
| Engaged sessions cur | `ai_llm_traffic.table[n].engaged_sessions` | Integer |
| Engaged sessions prev | `ai_llm_traffic.table[n].previous_engaged_sessions` | Integer |
| Engaged sessions Δ | `ai_llm_traffic.table[n].engaged_sessions_change` | "↑ / ↓ / N/A" |
| Total users cur | `ai_llm_traffic.table[n].total_users` | Integer |
| Total users prev | `ai_llm_traffic.table[n].previous_total_users` | Integer |
| Total users Δ | `ai_llm_traffic.table[n].total_users_change` | "↑ / ↓ / N/A" |
| New users cur | `ai_llm_traffic.table[n].new_users` | Integer |
| New users prev | `ai_llm_traffic.table[n].previous_new_users` | Integer |
| New users Δ | `ai_llm_traffic.table[n].new_users_change` | "↑ / ↓ / N/A" |
| Totals row | From `ai_llm_traffic.totals.*` | Pre-aggregated by API |

---

## STEP 3 — BUILD HTML REPORT

Construct the full HTML report as a single self-contained file using the structure below.
All styles are inline — no external dependencies.

### Report structure

```
<header>
  Title: "Weekly analytics report — infrasity.com"
  Subtitle: "Current: {CURRENT_START_DISPLAY} – {CURRENT_END_DISPLAY}
             Previous: {PREVIOUS_START_DISPLAY} – {PREVIOUS_END_DISPLAY}
             Sources: Google Search Console + GA4"

<section: GSC>
  Section header: teal left-border accent
  4 KPI cards (2 rows × 4 cols):
    Row 1: Clicks · Impressions · Avg CTR · Avg position
  Table 1: Top pages (all rows from top_pages[])
  Table 2: Top queries (all rows from top_queries[])

<section: GA4>
  Section header: blue left-border accent
  8 KPI cards (2 rows × 4 cols):
    Row 1: Sessions · Users · New users · Pageviews
    Row 2: Conversions · Engagement rate · Bounce rate · Avg duration
  Table 3: Channels (all rows from channels[] + computed totals row)

<section: AI/LLM traffic>
  Section header: purple left-border accent
  3 KPI cards (1 row × 3 cols):
    Engaged sessions · Total users · New users
  Table 4: Cross-dimensional table (all rows from ai_llm_traffic.table[])
            + totals row from ai_llm_traffic.totals
```

### KPI card format

Each card contains:
- Label (11px, muted)
- Current value (20px, 500 weight)
- Change indicator (11px, green/red/gray with ↑↓→)
- Previous value (11px, muted) — "was {previous}"

### Table format rules

- Grouped column headers (Clicks / Impressions / etc.) spanning cur + prev + Δ columns
- Left separator border between metric groups
- Horizontal scroll wrapper for wide tables
- Monospace font for page paths, query strings, source/medium values
- "new" badge (blue pill) on page/query rows where previous data = 0
- ↑ in green (#0F6E56), ↓ in red (#A32D2D), → / N/A in muted gray
- Total/summary rows: slightly darker background, 500 weight, top border

### CSS constants (self-contained, no external dependencies)

```css
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
       font-size: 13px; color: #1a1a1a; background: #fff;
       padding: 32px; max-width: 1200px; margin: 0 auto; }
.up  { color: #0F6E56; }
.dn  { color: #A32D2D; }
.nt  { color: #6b7280; }
/* KPI cards */
.kc  { background: #f9fafb; border-radius: 8px; padding: 10px 12px; }
/* Tables */
.tw  { border: 1px solid #e5e7eb; border-radius: 10px; overflow-x: auto; }
th   { background: #f9fafb; font-size: 11px; padding: 6px 10px;
       border-bottom: 1px solid #e5e7eb; }
td   { padding: 7px 10px; border-bottom: 1px solid #f3f4f6; }
/* Section headers */
.sh-gsc  { border-left: 3px solid #1D9E75; }
.sh-ga4  { border-left: 3px solid #378ADD; }
.sh-ai   { border-left: 3px solid #7F77DD; }
/* Source dots */
.d-gpt   { background: #10a37f; }   /* chatgpt.com */
.d-perp  { background: #6366f1; }   /* perplexity.ai */
.d-claude { background: #d97706; }  /* claude.ai */
/* New badge */
.nb { background: #EFF6FF; color: #1D4ED8; font-size: 10px;
      border-radius: 3px; padding: 1px 5px; }
```

---

## STEP 4 — SAVE REPORT

Call `GSC-GA4:save_report` with the complete HTML string built in Step 3:

```
GSC-GA4:save_report(html_content = <full HTML string>)
```

Store the returned public URL as `REPORT_URL`.

---

## STEP 5 — COMPOSE SLACK MESSAGE

Build the Slack message using the template below. Slack uses `*bold*` and plain text —
no HTML tags.

```
📊 *Weekly Analytics Report — infrasity.com*
{CURRENT_START_DISPLAY} – {CURRENT_END_DISPLAY} vs {PREVIOUS_START_DISPLAY} – {PREVIOUS_END_DISPLAY}

---

*🔍 Google Search Console*
• Clicks: *{gsc.clicks.current}* {gsc.clicks.change_arrow} {gsc.clicks.change} (was {gsc.clicks.previous})
• Impressions: *{gsc.impressions.current}* {gsc.impressions.change_arrow} {gsc.impressions.change} (was {gsc.impressions.previous})
• CTR: *{gsc.ctr.current}%* {gsc.ctr.change_arrow} {gsc.ctr.change}
• Avg position: *{gsc.position.current}* {gsc.position.direction} (was {gsc.position.previous})

*Top page:* {top_pages[0].page} — {top_pages[0].clicks} clicks {top_pages[0].clicks_change}
*Biggest drop:* {lowest_clicks_change_page.page} — {lowest_clicks_change_page.clicks} clicks ({lowest_clicks_change_page.clicks_change})

---

*📈 Google Analytics 4*
• Sessions: *{ga4.sessions.current}* {ga4.sessions.change_arrow} {ga4.sessions.change} (was {ga4.sessions.previous})
• Users: *{ga4.users.current}* {ga4.users.change_arrow} {ga4.users.change} (was {ga4.users.previous})
• New users: *{ga4.new_users.current}* {ga4.new_users.change_arrow} {ga4.new_users.change}
• Conversions: *{ga4.conversions.current}* {ga4.conversions.change_arrow} {ga4.conversions.change}
• Engagement rate: *{ga4.engagement_rate.current}%* {ga4.engagement_rate.change_arrow} {ga4.engagement_rate.change}
• Avg duration: *{duration_display}* {ga4.duration.change_arrow} {ga4.duration.change}

*Channels (sessions):*
{for each channel: • {channel}: {sessions} ({sessions_change})}

---

*🤖 AI / LLM Traffic*
• Engaged sessions: *{llm.engaged_sessions.current}* {llm.engaged_sessions.change_arrow} {llm.engaged_sessions.change} (was {llm.engaged_sessions.previous})
• Total users: *{llm.total_users.current}* {llm.total_users.change_arrow} {llm.total_users.change} (was {llm.total_users.previous})
• New users: *{llm.new_users.current}* {llm.new_users.change_arrow} {llm.new_users.change}

{for each source in ai_llm_traffic.table grouped by source:
  • {source}: {sum(engaged_sessions)} engaged · {sum(total_users)} users}

---

📄 *Full report:* {REPORT_URL}
_Generated by weekly-analytics-report skill_
```

### Arrow rules for Slack message

| Condition | Arrow |
|---|---|
| Change starts with "+" | ↑ |
| Change starts with "−" or "-" | ↓ |
| Change = "0%" or "N/A" | → |
| Position improved (number went down) | ↑ |
| Position dropped (number went up) | ↓ |
| Bounce rate decreased | ↑ improved |
| Bounce rate increased | ↓ worse |

### Top page / biggest drop logic for Slack

- **Top page** = `top_pages[0]` (already sorted by clicks descending in API response)
- **Biggest drop** = the page with the most negative `clicks_change` value where
  `clicks_change` is not "N/A" (i.e. page existed in prior week). If no drops exist,
  omit the "Biggest drop" line entirely.

### Channel list in Slack

List all channels one per line in order of sessions descending (API returns them sorted).
Format: `• {channel}: {sessions} ({sessions_change})`

### AI/LLM source grouping for Slack

Group `ai_llm_traffic.table[]` rows by `source` and sum `engaged_sessions` and `total_users`
per source. Show one bullet per source. This gives a clean per-AI-tool summary without
listing every individual landing page row.

---

## STEP 6 — POST TO SLACK

Post the composed message to `SLACK_CHANNEL` using the Slack MCP.

Use `chat.postMessage` with:
- `channel`: SLACK_CHANNEL (include the # prefix)
- `text`: the full message string from Step 5
- `mrkdwn`: true (if supported by the MCP)

---

## STEP 7 — CONFIRM DELIVERY

Output a brief confirmation in the current session:

```
✅ Weekly analytics report delivered
Period: {CURRENT_START_DISPLAY} – {CURRENT_END_DISPLAY}
Channel: {SLACK_CHANNEL}
Report URL: {REPORT_URL}
```

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| `get_gsc_report` fails | Skip GSC section in HTML and Slack. Add note: "GSC data unavailable this week." Continue with GA4. |
| `get_ga4_report` fails | Skip GA4 + AI/LLM sections in HTML and Slack. Add note: "GA4 data unavailable this week." Continue with GSC. |
| `save_report` fails | Skip the report URL from Slack message. Post Slack summary only. Note at end: "HTML report could not be saved." |
| Slack MCP fails to post | Output the full composed Slack message as plain text in the current session as fallback. |
| `ai_llm_traffic.table` is empty or missing | Write "No AI/LLM referral traffic detected this week." in that section. Omit the table. |
| `previous_clicks = 0` for all top_pages rows | Note "First week of data — no prior week comparison available for pages." |
| `biggest_drop` page not found (no drops) | Omit the "Biggest drop" line from the Slack message entirely. |
| Channel totals division by zero (prev = 0) | Show "N/A" for that channel's Δ column. |

---

## WHAT NOT TO INCLUDE

- ❌ No estimated or computed values where the API returns exact data
- ❌ No CTR previous values per page or query — the API does not return them
- ❌ No position previous values per page or query — the API does not return them
- ❌ No engaged sessions per source estimated from site-wide engagement rate —
     use only `ai_llm_traffic.table[n].engaged_sessions` (direct from API)
- ❌ No asking for confirmation before posting to Slack — run and post in one go
- ❌ No HTML tags in the Slack message — plain text and Slack markdown only
- ❌ Do not skip channels with negative WoW change — include all channels
- ❌ Do not omit the landing page query string — include it in full in the HTML table