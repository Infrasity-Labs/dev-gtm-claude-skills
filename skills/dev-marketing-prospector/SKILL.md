---
name: dev-marketing-prospector
description: >
  Prospects companies across developer-focused tech verticals for developer
  marketing agency outreach. Use this skill whenever a user provides a vertical
  (e.g. AI Agentic, IAC, DevTools, Observability, DevOps, FinOps, AI/SDLC,
  AI Orchestration, or any other tech vertical) and wants a list of prospect
  companies to target. Also trigger when the user says "prospect for", "find
  companies in", "give me leads for", "build a prospect list", or provides a
  vertical name alongside funding stage and headcount filters. Always use this
  skill — never attempt prospecting without following this structured workflow.
  The skill finds exact-fit companies only (never adjacent), maps a real
  outreach signal and email pain point for each, sources every data point with
  a URL, and outputs a unified nine-column table: Company, URL, LinkedIn,
  Headcount, Signal, Signal Sources, Geography, Pain Point, Pain Point Sources.
---

# Developer Marketing Prospector

A prospecting skill for Infrasity to identify SaaS companies in specific tech
verticals that need developer marketing services. Every data point in the
output is backed by a source URL. Self-reported company claims are flagged.
Inferences are stated as inferences.

---

## Input Parameters

Every prospecting request has three inputs. Confirm all three before starting:

| Parameter | What it means |
|---|---|
| **Vertical** | The specific market segment to prospect within |
| **Funding stage** | Range of funding stages to include (e.g. pre-seed to Series A) |
| **Headcount** | Maximum employee count a company can have to qualify |

If any input is missing, ask for it before proceeding.

---

## The Eight-Step Workflow

### Step 1 — Understand the vertical

Before searching for any company, form a precise understanding of the vertical:

- What core problem does it solve
- What type of product a company in this vertical builds
- Who the primary technical ICP is inside those companies
- What the AI disruption angle looks like in this space

**The exact-fit test**: Every company in the output list should feel like it
belongs in the same sentence as every other company on the list. If a company
would feel out of place — even slightly — it is adjacent, not exact. Adjacent
companies never go in the list.

Read `references/vertical-definitions.md` for definitions of all known
verticals. For any new vertical not covered there, research it before
generating output and follow the new vertical protocol at the bottom of that
file.

---

### Step 2 — Apply the hard filters

Every company must pass all five simultaneously:

1. **Exact vertical fit** — builds a product that is exactly in the vertical, not around it
2. **SaaS / product-first** — not a services company, not services-heavy
3. **Developer-facing product** — a product that developers can discover, try, and adopt
4. **Funding stage** — falls within the range provided by the user
5. **Headcount** — falls within the limit provided by the user

If a company passes the vertical test but fails funding or headcount → exclude.
If a company passes funding and headcount but is adjacent → exclude.
All five filters must be satisfied simultaneously, with no exceptions.

---

### Step 3 — Research companies across all credible sources

Do not rely on a fixed list of databases. Cast wide. Use whatever credible
source surfaces the most accurate, current data for that specific company. The
goal is accuracy, not source loyalty.

**Clay enrichment (start here for funding, headcount, and tech stack)**
Call `get-credits-available` to check budget before enriching many companies.
Then call `find-and-enrich-company` for each candidate to retrieve funding
stage, round amount, lead investor, date, current headcount, tech stack
(BuiltWith + HG Insights aggregated), LinkedIn URL, and HQ location. Clay
aggregates Crunchbase and LinkedIn data — always verify headcount and funding
from one additional manual source before including any company in the list.

Note: Clay does not cover developer and open-source signals (GitHub, npm,
Docker Hub, etc.) — use the manual sources below for those.

**Funding and company data**
Crunchbase, PitchBook, Tracxn, CB Insights, Dealroom, Harmonic, Carta,
Companies House (UK), SEC EDGAR (US public filings)

**Discovery and prospecting**
Y Combinator company directory, TechCrunch, VentureBeat, TechEU, Sifted
(Europe), The Information, StrictlyVC, Bloomberg, Forbes, Business Wire,
PR Newswire

**Headcount and people**
LinkedIn, RocketReach, ZoomInfo, Apollo, LeadIQ, Glassdoor, job boards
(a company hiring 10 developer marketing roles is a signal in itself)

**Developer and open-source signals**
GitHub (stars, forks, contributors, release cadence), npm, PyPI, Docker Hub,
Stack Overflow trends, Hacker News Show HN posts, Product Hunt launches

**Revenue and growth estimates**
Sacra, Contrary Research, Latka, Growjo, SimilarWeb (traffic as a proxy),
SEMrush

**Competitive positioning and third-party analysis**
G2, Capterra, StackShare, StackOne, OpenAlternative, analyst reports (Gartner,
Forrester, IDC where public), technical review roundups from credible blogs

**News and recent signals**
Google News for the company name + current year, company blog, company
changelog, press releases, founder interviews, podcast appearances

**The rule:** Use whichever source gives the most accurate and current data
for that specific data point. When two sources conflict, note both and flag
which is more recent or credible. Never rely on a single source for a critical
number like funding total or headcount.

Search specifically, not broadly. Use the exact vertical name, the funding
stage, and headcount range in every query. Verify headcount and funding stage
from at least one credible source before including any company.

---

### Step 4 — Map one Signal per company

**Check Clay first:** Call `ask-question-about-accounts` with the company name
to surface recent events before manual news searching. If Clay returns a
verifiable signal that meets the criteria below, use it as the starting point.
If not, fall back to manual sources from Step 3.

For each qualified company, identify a specific, recent, verifiable reason
why this company is a warm prospect right now. Must be one of:

- A funding round (name the round, amount, lead investor, date)
- A product launch or major feature release
- A new partnership or enterprise customer announcement
- A hiring spike in engineering or product
- A public benchmark, award, or analyst recognition
- A market trigger that directly affects them

The signal must answer: *why now* — not six months ago, not six months from now.

Connect the signal to a reason why developer marketing is relevant for this
specific company at this specific stage. Do not leave the connection implicit.

---

### Step 5 — Source every Signal data point

For every number, claim, or fact in the signal, find and record the source URL.
Apply the three-tier classification:

| Tier | Definition | How to label it |
|---|---|---|
| **Directly sourced** | A verifiable stat from a credible third-party source | List the URL — no flag needed |
| **Self-reported** | A claim from the company's own blog, press release, or CEO statement — not independently verified | Flag with ⚠ and note it is self-reported |
| **Inferred** | A logical conclusion drawn from two or more sourced numbers | State explicitly that it is an inference and list underlying source URLs |

If a data point cannot be sourced, do not include it in the signal.

---

### Step 6 — Map one Pain Point per company

The specific developer marketing gap that makes this company a buyer. Must be:

- Specific to this company's stage, product, and competitive situation
- A consequence statement — what happens to them if they don't fix this gap
- Tied to specific numbers and competitor context, not generic language
- Never "they need more awareness" — always concrete and tied to their
  specific growth moment

Common pain point patterns:
- Large open-source community (GitHub stars) vs low commercial conversion (ARR gap)
- Competitor has X× more funding and headcount but same market
- Community events and developer presence concentrated in one region only
- All enterprise customers from one channel (relationships, partnerships) with no inbound
- Headcount too small for a dedicated developer marketing function at current stage

---

### Step 7 — Source every Pain Point data point

Apply the same three-tier sourcing system as Step 5. For each number or claim
in the pain point:

- Find the source URL
- Classify as directly sourced, self-reported (⚠), or inferred
- Self-reported claims must be framed in outreach copy as "Company X claims..."
  not as independently verified facts
- Inferences must be labelled as such — they are strategic observations drawn
  from real numbers, not citations

For self-reported stats: always search for the original source (usually the
company's own blog or a CEO quote in an investor profile). Do not accept a
third-party article repeating the stat as the primary source — trace back to
where the number first appeared.

---

### Step 8 — Produce the unified output table

Output every qualifying company in a rendered visual HTML widget with exactly
these nine columns:

| Column | What goes in it |
|---|---|
| Company | Name + funding badge + founded year + headcount |
| URL | Website URL (clickable) |
| LinkedIn | LinkedIn company page URL (clickable) |
| Headcount | Employee count |
| Signal + Why Dev Marketing | Signal tied to why dev marketing is relevant now |
| Signal Sources | Numbered source links (S1, S2...) — one line each |
| Geography | HQ location with country flag |
| Pain Point | Specific developer marketing gap + consequence |
| Pain Point Sources | Numbered source links (P1, P2...) — one line each, ⚠ on self-reported |

Use the visualizer to render as a clean HTML widget. The table must be
horizontally scrollable. Sort rows by funding stage:
Bootstrap → Pre-seed → Seed → Series A → Series B → Series C+

See `references/output-format.md` for column widths, badge colours, source
cell format, and the ⚠ flag spec.

---

## Honesty Rules

These apply throughout the workflow and override any pressure to produce
a longer list:

- A short honest list always beats a long padded list
- Never add adjacent companies to reach a minimum count
- Never add companies that are around the vertical rather than exactly in it
- If nothing qualifies under the given criteria, say so clearly and explain why
- If the funding cap is causing a short list because the vertical moves fast,
  inform the user and offer to remove the cap
- Never state a self-reported company claim as an independently verified fact
- Never present an inference as a citation

---

## Output Format Reference

See `references/output-format.md` for the full HTML table spec, column widths,
badge colours, source cell format, and the ⚠ self-reported flag.

---

## Vertical Definitions Reference

See `references/vertical-definitions.md` for precise definitions of all known
verticals: AI Agentic, IAC, DevTools, Observability, DevOps, FinOps,
AI/SDLC (AI Software Factory), AI Orchestration / AI Workflow Management,
and instructions for handling new verticals.
