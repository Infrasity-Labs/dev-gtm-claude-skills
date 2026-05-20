# HTML Report Template Reference

This file contains the complete annotated HTML template for the SEO Performance Report.
Replace all `{{VARIABLE}}` placeholders with real data from the DataForSEO API calls.

---

## Variable Reference

| Variable | Source |
|---|---|
| `{{TARGET_DOMAIN}}` | User input |
| `{{START_DATE}}` | User input (e.g. Feb 15, 2026) |
| `{{END_DATE}}` | User input (e.g. May 15, 2026) |
| `{{BASELINE_TRAFFIC}}` | Step 1: historical etv, formatted with commas |
| `{{BASELINE_KEYWORDS}}` | Step 1: historical count, formatted with commas |
| `{{BASELINE_TOP3}}` | Step 1: pos_1 + pos_2_3, formatted with commas |
| `{{BASELINE_RANK}}` | Step 3: competitive rank at baseline period |
| `{{CURRENT_TRAFFIC}}` | Step 2: current etv, formatted with commas |
| `{{CURRENT_KEYWORDS}}` | Step 2: current count, formatted with commas |
| `{{CURRENT_TOP3}}` | Step 2: pos_1 + pos_2_3 |
| `{{CURRENT_COMP_RANK}}` | Step 3: rank in sorted competitive table |
| `{{TOTAL_COMPETITORS}}` | Count of all domains including target |
| `{{TRAFFIC_GROWTH_PCT}}` | Step 2 calc: formatted like "+36.2%" or "-31.4%" |
| `{{TRAFFIC_GROWTH_CLASS}}` | "pos" if positive, "neg" if negative |
| `{{KEYWORDS_CHANGE}}` | Step 2 calc: e.g. "-1,147" or "+523" |
| `{{KEYWORDS_CHANGE_PCT}}` | Step 2 calc: e.g. "-50.1%" |
| `{{KEYWORDS_CHANGE_CLASS}}` | "pos" or "neg" |
| `{{TOP3_GROWTH_PCT}}` | Step 2 calc: e.g. "+28.9%" |
| `{{TOP3_GROWTH_CLASS}}` | "pos" or "neg" |
| `{{TARGET_GOAL_TRAFFIC}}` | Step 6 derived target |
| `{{TARGET_GOAL_KEYWORDS}}` | Step 6 derived target |
| `{{TARGET_GOAL_TOP3}}` | Step 6 derived target |
| `{{TARGET_BADGE_TEXT}}` | e.g. "Challenge #2" or "Maintain #1" |
| `{{COMP_TABLE_ROWS}}` | Step 3: HTML `<tr>` rows for all 8 domains |
| `{{MARKET_INSIGHT_TEXT}}` | Step 3: 2–3 sentence market insight paragraph |
| `{{BIG_STAT_VAL}}` | e.g. "+36.2%" — the hero traffic growth number |
| `{{BIG_STAT_CLASS}}` | "green" if positive, "red" if negative |
| `{{GAP_TO_NEXT}}` | Step 3: etv gap to competitor one rank above |
| `{{NEXT_ABOVE_DOMAIN}}` | Domain ranked one above target |
| `{{LEAD_BELOW_DOMAIN}}` | Domain ranked one below target |
| `{{LEAD_OVER_BELOW}}` | etv lead over competitor one rank below |
| `{{TREND_LABEL_1}}` | Month label for trend bar 1 (e.g. "Feb 2026") |
| `{{TREND_ETV_1}}` | ETV value for trend bar 1 |
| `{{TREND_BAR_WIDTH_1}}` | Width % for trend bar 1 (highest month = 100%) |
| `{{TREND_LABEL_2}}` | Month label for trend bar 2 |
| `{{TREND_ETV_2}}` | ETV value for trend bar 2 |
| `{{TREND_BAR_WIDTH_2}}` | Width % for trend bar 2 |
| `{{TREND_LABEL_3}}` | Month label for trend bar 3 |
| `{{TREND_ETV_3}}` | ETV value for trend bar 3 |
| `{{TREND_BAR_WIDTH_3}}` | Width % for trend bar 3 |
| `{{TREND_LABEL_4}}` | Month label for trend bar 4 |
| `{{TREND_ETV_4}}` | ETV value for trend bar 4 |
| `{{TREND_BAR_WIDTH_4}}` | Width % for trend bar 4 |
| `{{KW_POS_1}}` | Step 2: pos_1 count |
| `{{KW_POS_2_3}}` | Step 2: pos_2_3 count |
| `{{KW_POS_4_10}}` | Step 2: pos_4_10 count |
| `{{KW_POS_11_20}}` | Step 2: pos_11_20 count |
| `{{KW_POS_21_100}}` | Step 2: sum pos_21_30 through pos_91_100 |
| `{{PAGE1_URL}}` | Step 4: top page address (shorten if needed) |
| `{{PAGE1_ETV}}` | Step 4: top page etv |
| `{{PAGE1_KW}}` | Step 4: top page keyword count |
| `{{PAGE2_URL}}` | Step 4: second page address |
| `{{PAGE2_ETV}}` | Step 4: second page etv |
| `{{PAGE2_KW}}` | Step 4: second page keyword count |
| `{{PAGE3_URL}}` | Step 4: third page address |
| `{{PAGE3_ETV}}` | Step 4: third page etv |
| `{{PAGE3_KW}}` | Step 4: third page keyword count |
| `{{STRAT_1_TITLE}}` | Strategic priority 1 title |
| `{{STRAT_1_DESC}}` | Strategic priority 1 description |
| `{{STRAT_2_TITLE}}` | Strategic priority 2 title |
| `{{STRAT_2_DESC}}` | Strategic priority 2 description |
| `{{STRAT_3_TITLE}}` | Strategic priority 3 title |
| `{{STRAT_3_DESC}}` | Strategic priority 3 description |
| `{{STRAT_4_TITLE}}` | Strategic priority 4 title |
| `{{STRAT_4_DESC}}` | Strategic priority 4 description |
| `{{STRAT_5_TITLE}}` | Strategic priority 5 title |
| `{{STRAT_5_DESC}}` | Strategic priority 5 description |
| `{{STRAT_6_TITLE}}` | Strategic priority 6 title |
| `{{STRAT_6_DESC}}` | Strategic priority 6 description |
| `{{EXEC_PARA_1}}` | Executive summary paragraph 1 |
| `{{EXEC_PARA_2}}` | Executive summary paragraph 2 |
| `{{EXEC_PARA_3}}` | Executive summary paragraph 3 |
| `{{EXEC_PARA_4}}` | Executive summary paragraph 4 |
| `{{EXEC_BADGE_TEXT}}` | Summary badge text |
| `{{COMP_TABLE_LABEL}}` | "X of Y" competitive position label |

---

## Trend Bar Width Calculation

To compute bar widths (so bars fill proportionally):
```
max_etv = highest ETV value across the 4 monthly data points
width_pct_N = round((etv_N / max_etv) * 100)
```
Minimum width = 10% (so labels are always visible).

---

## Competitive Table Row Template

For each domain in the sorted list, generate one `<tr>`:

```html
<!-- Target domain row (highlighted): -->
<tr class="highlight">
  <td><span class="rank-badge rank-N">N</span></td>
  <td><span class="company-name hl">🔥 {{TARGET_DOMAIN}}</span></td>
  <td>{{ETV_FORMATTED}}</td>
  <td>{{KW_COUNT_FORMATTED}}</td>
  <td><span class="trend-badge trend-up">↑ +XX%</span></td>
</tr>

<!-- Competitor row: -->
<tr>
  <td><span class="rank-badge rank-N">N</span></td>
  <td><span class="company-name">{{DOMAIN}}</span></td>
  <td>{{ETV_FORMATTED}}</td>
  <td>{{KW_COUNT_FORMATTED}}</td>
  <td><span class="trend-badge trend-stable">Stable</span></td>
</tr>
```

Rank badge classes: `rank-1` (red), `rank-2` (orange/gold), `rank-3` (blue), `rank-other` (gray).
Trend badge classes: `trend-up` (green), `trend-down` (red), `trend-stable` (gray).

---

## Full HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TARGET_DOMAIN}} — Q1 2026 Strategic Performance Report</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:#0a0e1a;color:#e2e8f0;font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased}
.page-wrapper{max-width:900px;margin:0 auto;padding:32px 20px 60px}

/* HEADER */
.header{text-align:center;padding:32px 0 24px}
.header-logo{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#94a3b8;margin-bottom:20px}
.header-logo span{color:#fff}
.header h1{font-size:clamp(26px,4vw,38px);font-weight:800;line-height:1.15;margin-bottom:8px}
.header h1 em{font-style:normal;background:linear-gradient(135deg,#3b82f6,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.header-sub{color:#64748b;font-size:13px;font-weight:500}

/* SECTION TITLES */
.section-title{font-size:22px;font-weight:800;text-align:center;margin:40px 0 20px;color:#f1f5f9}

/* TIMELINE */
.timeline{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;position:relative;margin-bottom:40px}
.timeline::before{content:'';position:absolute;top:50%;left:calc(33.33% - 6px);width:calc(33.33% + 12px);height:2px;background:linear-gradient(90deg,#1d4ed8,#3b82f6);z-index:0;transform:translateY(-50%)}
.tcard{background:#111827;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:22px 18px;position:relative;z-index:1}
.tcard.active{background:linear-gradient(145deg,#1e3a8a,#1d4ed8);border-color:#3b82f6;box-shadow:0 0 30px rgba(59,130,246,0.25)}
.tcard-date{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#64748b;margin-bottom:4px}
.tcard.active .tcard-date{color:#93c5fd}
.tcard-label{font-size:12px;font-weight:600;color:#94a3b8;margin-bottom:14px}
.tcard.active .tcard-label{color:#bfdbfe}
.tcard-row{display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid rgba(255,255,255,0.05)}
.tcard-row:last-of-type{border-bottom:none}
.tcard-row-label{font-size:11px;color:#64748b;font-weight:500}
.tcard.active .tcard-row-label{color:#93c5fd}
.tcard-row-val{font-size:13px;font-weight:700;color:#f1f5f9}
.tcard.active .tcard-row-val{color:#fff}
.delta{font-size:10px;font-weight:600;margin-left:4px}
.delta.neg{color:#f87171}
.delta.pos{color:#34d399}
.tcard-badge{display:inline-block;margin-top:14px;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 10px;border-radius:20px;background:rgba(255,255,255,0.08);color:#94a3b8}
.tcard.active .tcard-badge{background:rgba(255,255,255,0.15);color:#fff}
.tcard-badge.green{background:#064e3b;color:#34d399}

/* COMPETITIVE TABLE */
.comp-section{background:#111827;border:1px solid rgba(255,255,255,0.07);border-radius:16px;overflow:hidden;margin-bottom:40px}
.comp-table{width:100%;border-collapse:collapse}
.comp-table thead tr{background:#0d1526}
.comp-table th{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#475569;padding:12px 16px;text-align:left}
.comp-table th:not(:first-child){text-align:center}
.comp-table td{padding:13px 16px;border-top:1px solid rgba(255,255,255,0.04);font-size:13px;color:#cbd5e1}
.comp-table td:not(:first-child){text-align:center}
.comp-table tr.highlight{background:linear-gradient(90deg,rgba(29,78,216,0.35),rgba(29,78,216,0.18))}
.comp-table tr.highlight td{color:#fff}
.comp-table tr:not(.highlight):hover{background:rgba(255,255,255,0.03);transition:background .15s}
.rank-badge{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;font-size:11px;font-weight:800}
.rank-1{background:#7f1d1d;color:#fca5a5}
.rank-2{background:#78350f;color:#fcd34d}
.rank-3{background:#1e3a8a;color:#93c5fd}
.rank-other{background:#1e293b;color:#64748b}
.company-name{font-weight:600;color:#f1f5f9}
.company-name.hl{color:#fff;font-weight:700}
.trend-badge{display:inline-block;font-size:10px;font-weight:700;padding:3px 9px;border-radius:20px}
.trend-up{background:#064e3b;color:#34d399}
.trend-down{background:#450a0a;color:#f87171}
.trend-stable{background:#1c1917;color:#a8a29e}
.market-insight{padding:16px 20px;background:rgba(29,78,216,0.1);border-top:1px solid rgba(29,78,216,0.2)}
.market-insight p{font-size:12px;color:#94a3b8;line-height:1.6}
.market-insight strong{color:#60a5fa}

/* TWO-COL */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:40px}
.col-card{background:#111827;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:22px 18px}
.col-card-title{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#475569;margin-bottom:16px}
.big-stat{margin-bottom:16px}
.big-stat-val{font-size:40px;font-weight:800;line-height:1;margin-bottom:4px}
.big-stat-val.green{color:#34d399}
.big-stat-val.red{color:#f87171}
.big-stat-label{font-size:11px;color:#64748b;font-weight:500}
.stat-row{display:flex;justify-content:space-between;align-items:center;padding:9px 12px;background:rgba(255,255,255,0.03);border-radius:8px;margin-bottom:6px}
.stat-row-label{font-size:12px;color:#94a3b8;font-weight:500}
.stat-row-val{font-size:13px;font-weight:700;color:#f1f5f9}
.content-cluster{padding:10px 12px;background:rgba(255,255,255,0.03);border-radius:8px;margin-bottom:6px;border-left:3px solid #1d4ed8}
.cc-url{font-size:11px;color:#60a5fa;font-weight:600;margin-bottom:4px;word-break:break-all}
.cc-meta{display:flex;gap:12px}
.cc-meta span{font-size:10px;color:#64748b;font-weight:500}
.cc-meta strong{color:#94a3b8}

/* TREND BARS */
.trend-months{display:flex;flex-direction:column;gap:10px;margin-bottom:20px}
.trend-month-row{display:flex;align-items:center;gap:10px}
.trend-month-label{font-size:11px;color:#64748b;font-weight:600;width:60px;flex-shrink:0}
.trend-bar-wrap{flex:1;background:rgba(255,255,255,0.05);border-radius:4px;height:22px;overflow:hidden}
.trend-bar{height:100%;border-radius:4px;display:flex;align-items:center;padding-left:8px;font-size:10px;font-weight:700;color:#fff;background:linear-gradient(90deg,#1d4ed8,#3b82f6)}
.trend-kw-row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.04);font-size:11px}
.trend-kw-label{color:#64748b}
.trend-kw-val{color:#f1f5f9;font-weight:600}

/* STRATEGIC PRIORITIES */
.strat-section{background:#0d1117;border:1px solid rgba(255,255,255,0.06);border-radius:16px;padding:28px 22px;margin-bottom:40px}
.strat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:4px}
.strat-card{background:#111827;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:16px 14px}
.strat-num{font-size:11px;font-weight:800;color:#1d4ed8;margin-bottom:6px}
.strat-title{font-size:13px;font-weight:700;color:#f1f5f9;margin-bottom:6px;line-height:1.3}
.strat-desc{font-size:11px;color:#64748b;line-height:1.55}

/* EXECUTIVE SUMMARY */
.exec-section{background:linear-gradient(135deg,#78350f,#92400e,#b45309);border-radius:16px;padding:30px 26px;margin-bottom:24px}
.exec-section h2{font-size:20px;font-weight:800;color:#fff;margin-bottom:18px}
.exec-section p{font-size:13px;color:#fde68a;line-height:1.7;margin-bottom:12px}
.exec-section p:last-of-type{margin-bottom:0}
.exec-badge{display:inline-block;margin-top:18px;background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.2);border-radius:20px;padding:7px 18px;font-size:11px;font-weight:700;color:#fff;letter-spacing:.04em}

/* FOOTER */
.footer{text-align:center;font-size:11px;color:#1e293b;padding-top:12px;line-height:1.6}

/* RESPONSIVE */
@media(max-width:680px){
  .timeline{grid-template-columns:1fr}
  .timeline::before{display:none}
  .two-col{grid-template-columns:1fr}
  .strat-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:420px){.strat-grid{grid-template-columns:1fr}}
@media print{
  body{background:#fff;color:#000}
  .tcard,.comp-section,.col-card,.strat-section,.exec-section{border:1px solid #ccc!important;background:#fff!important;box-shadow:none!important}
}
</style>
</head>
<body>
<div class="page-wrapper">

  <!-- HEADER -->
  <div class="header">
    <div class="header-logo"><span>✦ INFRASITY</span></div>
    <h1>Q1 2026 <em>Strategic Performance</em></h1>
    <p class="header-sub">Growth Journey &amp; Competitive Analysis: {{START_DATE}} → {{END_DATE}}</p>
  </div>

  <!-- TIMELINE -->
  <div class="section-title">Our 90-Day Growth Journey</div>
  <div class="timeline">

    <div class="tcard">
      <div class="tcard-date">{{START_DATE}}</div>
      <div class="tcard-label">Where We Were</div>
      <div class="tcard-row"><span class="tcard-row-label">Monthly Traffic</span><span class="tcard-row-val">{{BASELINE_TRAFFIC}}</span></div>
      <div class="tcard-row"><span class="tcard-row-label">Organic Keywords</span><span class="tcard-row-val">{{BASELINE_KEYWORDS}}</span></div>
      <div class="tcard-row"><span class="tcard-row-label">Top 3 Keywords</span><span class="tcard-row-val">{{BASELINE_TOP3}}</span></div>
      <div class="tcard-row"><span class="tcard-row-label">Competitive Rank</span><span class="tcard-row-val">#{{BASELINE_RANK}} of {{TOTAL_COMPETITORS}}</span></div>
      <div class="tcard-badge">Starting Position</div>
    </div>

    <div class="tcard active">
      <div class="tcard-date">{{END_DATE}}</div>
      <div class="tcard-label">Where We Are</div>
      <div class="tcard-row">
        <span class="tcard-row-label">Monthly Traffic</span>
        <span class="tcard-row-val">{{CURRENT_TRAFFIC}} <span class="delta {{TRAFFIC_GROWTH_CLASS}}">{{TRAFFIC_GROWTH_PCT}}</span></span>
      </div>
      <div class="tcard-row">
        <span class="tcard-row-label">Organic Keywords</span>
        <span class="tcard-row-val">{{CURRENT_KEYWORDS}} <span class="delta {{KEYWORDS_CHANGE_CLASS}}">{{KEYWORDS_CHANGE_PCT}}</span></span>
      </div>
      <div class="tcard-row">
        <span class="tcard-row-label">Top 3 Keywords</span>
        <span class="tcard-row-val">{{CURRENT_TOP3}} <span class="delta {{TOP3_GROWTH_CLASS}}">{{TOP3_GROWTH_PCT}}</span></span>
      </div>
      <div class="tcard-row">
        <span class="tcard-row-label">Competitive Rank</span>
        <span class="tcard-row-val">#{{CURRENT_COMP_RANK}} of {{TOTAL_COMPETITORS}}</span>
      </div>
      <div class="tcard-badge">Rank #{{CURRENT_COMP_RANK}} Overall</div>
    </div>

    <div class="tcard">
      <div class="tcard-date">Q2 2026 Target</div>
      <div class="tcard-label">Where We're Going</div>
      <div class="tcard-row"><span class="tcard-row-label">Monthly Traffic</span><span class="tcard-row-val">{{TARGET_GOAL_TRAFFIC}}+</span></div>
      <div class="tcard-row"><span class="tcard-row-label">Organic Keywords</span><span class="tcard-row-val">{{TARGET_GOAL_KEYWORDS}}+</span></div>
      <div class="tcard-row"><span class="tcard-row-label">Top 3 Keywords</span><span class="tcard-row-val">{{TARGET_GOAL_TOP3}}+</span></div>
      <div class="tcard-row"><span class="tcard-row-label">Target Position</span><span class="tcard-row-val">{{TARGET_BADGE_TEXT}}</span></div>
      <div class="tcard-badge green">Target: {{TARGET_BADGE_TEXT}}</div>
    </div>

  </div>

  <!-- COMPETITIVE LANDSCAPE -->
  <div class="section-title">Competitive Landscape</div>
  <div class="comp-section">
    <table class="comp-table">
      <thead>
        <tr>
          <th>Rank</th>
          <th>Company</th>
          <th>Monthly Traffic</th>
          <th>Keywords</th>
          <th>Q1 Trend</th>
        </tr>
      </thead>
      <tbody>
        {{COMP_TABLE_ROWS}}
      </tbody>
    </table>
    <div class="market-insight">
      <p>{{MARKET_INSIGHT_TEXT}}</p>
    </div>
  </div>

  <!-- TWO-COL -->
  <div class="two-col">

    <div class="col-card">
      <div class="col-card-title">Business Impact</div>
      <div class="big-stat">
        <div class="big-stat-val {{BIG_STAT_CLASS}}">{{TRAFFIC_GROWTH_PCT}}</div>
        <div class="big-stat-label">Traffic change {{START_DATE}} → {{END_DATE}}</div>
      </div>
      <div class="stat-row">
        <span class="stat-row-label">Competitive Position</span>
        <span class="stat-row-val">#{{CURRENT_COMP_RANK}} of {{TOTAL_COMPETITORS}}</span>
      </div>
      <div class="stat-row">
        <span class="stat-row-label">Fastest Growing in Set</span>
        <span class="stat-row-val" style="color:{{FASTEST_GROWING_COLOR}}">{{FASTEST_GROWING_LABEL}}</span>
      </div>
      <div class="stat-row" style="margin-bottom:16px">
        <span class="stat-row-label">Gap to Close (#{{RANK_ABOVE}})</span>
        <span class="stat-row-val">{{GAP_TO_NEXT}} ETV</span>
      </div>
      <div class="col-card-title" style="margin-top:4px">Top Content Clusters</div>
      <div class="content-cluster">
        <div class="cc-url">{{PAGE1_URL}}</div>
        <div class="cc-meta"><span>ETV: <strong>{{PAGE1_ETV}}</strong></span><span>Keywords: <strong>{{PAGE1_KW}}</strong></span></div>
      </div>
      <div class="content-cluster">
        <div class="cc-url">{{PAGE2_URL}}</div>
        <div class="cc-meta"><span>ETV: <strong>{{PAGE2_ETV}}</strong></span><span>Keywords: <strong>{{PAGE2_KW}}</strong></span></div>
      </div>
      <div class="content-cluster">
        <div class="cc-url">{{PAGE3_URL}}</div>
        <div class="cc-meta"><span>ETV: <strong>{{PAGE3_ETV}}</strong></span><span>Keywords: <strong>{{PAGE3_KW}}</strong></span></div>
      </div>
    </div>

    <div class="col-card">
      <div class="col-card-title">Monthly Traffic Trend</div>
      <div class="trend-months">
        <div class="trend-month-row">
          <span class="trend-month-label">{{TREND_LABEL_1}}</span>
          <div class="trend-bar-wrap"><div class="trend-bar" style="width:{{TREND_BAR_WIDTH_1}}%">{{TREND_ETV_1}}</div></div>
        </div>
        <div class="trend-month-row">
          <span class="trend-month-label">{{TREND_LABEL_2}}</span>
          <div class="trend-bar-wrap"><div class="trend-bar" style="width:{{TREND_BAR_WIDTH_2}}%">{{TREND_ETV_2}}</div></div>
        </div>
        <div class="trend-month-row">
          <span class="trend-month-label">{{TREND_LABEL_3}}</span>
          <div class="trend-bar-wrap"><div class="trend-bar" style="width:{{TREND_BAR_WIDTH_3}}%">{{TREND_ETV_3}}</div></div>
        </div>
        <div class="trend-month-row">
          <span class="trend-month-label">{{TREND_LABEL_4}}</span>
          <div class="trend-bar-wrap"><div class="trend-bar" style="width:{{TREND_BAR_WIDTH_4}}%">{{TREND_ETV_4}}</div></div>
        </div>
      </div>
      <div class="col-card-title">Keyword Distribution (Current)</div>
      <div class="trend-kw-row"><span class="trend-kw-label">Position 1</span><span class="trend-kw-val">{{KW_POS_1}}</span></div>
      <div class="trend-kw-row"><span class="trend-kw-label">Position 2–3</span><span class="trend-kw-val">{{KW_POS_2_3}}</span></div>
      <div class="trend-kw-row"><span class="trend-kw-label">Position 4–10</span><span class="trend-kw-val">{{KW_POS_4_10}}</span></div>
      <div class="trend-kw-row"><span class="trend-kw-label">Position 11–20</span><span class="trend-kw-val">{{KW_POS_11_20}}</span></div>
      <div class="trend-kw-row" style="border-bottom:none"><span class="trend-kw-label">Position 21–100</span><span class="trend-kw-val">{{KW_POS_21_100}}</span></div>
    </div>

  </div>

  <!-- STRATEGIC PRIORITIES -->
  <div class="strat-section">
    <div class="section-title" style="margin-top:0;margin-bottom:18px;text-align:left;font-size:18px">Q2 2026 Strategic Priorities</div>
    <div class="strat-grid">
      <div class="strat-card">
        <div class="strat-num">1. {{STRAT_1_NUM_LABEL}}</div>
        <div class="strat-title">{{STRAT_1_TITLE}}</div>
        <div class="strat-desc">{{STRAT_1_DESC}}</div>
      </div>
      <div class="strat-card">
        <div class="strat-num">2. {{STRAT_2_NUM_LABEL}}</div>
        <div class="strat-title">{{STRAT_2_TITLE}}</div>
        <div class="strat-desc">{{STRAT_2_DESC}}</div>
      </div>
      <div class="strat-card">
        <div class="strat-num">3. {{STRAT_3_NUM_LABEL}}</div>
        <div class="strat-title">{{STRAT_3_TITLE}}</div>
        <div class="strat-desc">{{STRAT_3_DESC}}</div>
      </div>
      <div class="strat-card">
        <div class="strat-num">4. {{STRAT_4_NUM_LABEL}}</div>
        <div class="strat-title">{{STRAT_4_TITLE}}</div>
        <div class="strat-desc">{{STRAT_4_DESC}}</div>
      </div>
      <div class="strat-card">
        <div class="strat-num">5. {{STRAT_5_NUM_LABEL}}</div>
        <div class="strat-title">{{STRAT_5_TITLE}}</div>
        <div class="strat-desc">{{STRAT_5_DESC}}</div>
      </div>
      <div class="strat-card">
        <div class="strat-num">6. {{STRAT_6_NUM_LABEL}}</div>
        <div class="strat-title">{{STRAT_6_TITLE}}</div>
        <div class="strat-desc">{{STRAT_6_DESC}}</div>
      </div>
    </div>
  </div>

  <!-- EXECUTIVE SUMMARY -->
  <div class="exec-section">
    <h2>Infrasity's Notes</h2>
    <p>{{EXEC_PARA_1}}</p>
    <p>{{EXEC_PARA_2}}</p>
    <p>{{EXEC_PARA_3}}</p>
    <p>{{EXEC_PARA_4}}</p>
    <div class="exec-badge">{{EXEC_BADGE_TEXT}}</div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    Data sourced from DataForSEO (ignore_synonyms: false). Traffic figures represent estimated organic traffic value (ETV).<br>
    Competitive set: {{COMP_DOMAIN_LIST}}. Report period: {{START_DATE}} – {{END_DATE}}.
  </div>

</div>
</body>
</html>
```