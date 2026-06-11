# Developer Marketing Prospector

Builds an exact-fit prospect list for any developer-focused tech vertical. You give it a vertical, a funding range, and a headcount cap. It returns a sourced table of companies that need developer marketing, each with a real "why now" signal and a concrete pain point. Every data point is backed by a source URL, and self-reported claims are flagged.

---

## What this skill does

You provide a vertical (AI Agentic, IAC, DevTools, Observability, DevOps, FinOps, AI/SDLC, AI Orchestration, or any other), a funding stage range, and a maximum headcount. The skill forms a precise definition of the vertical, applies five hard filters, researches candidates across many credible sources, and qualifies only companies that sit exactly in the vertical (never adjacent). For each one it maps a recent outreach signal, a specific developer marketing pain point, and sources both with URLs. The result renders as a scrollable nine-column HTML widget sorted by funding stage.

Built for:
- **Developer marketing agencies** building targeted outbound lists for a specific vertical
- **Founders and GTM teams** researching the competitive landscape in their space
- **SDRs and growth leads** who need warm, sourced reasons to reach out, not a raw name dump

---

## Installation

### Claude Code (Recommended)

Clone the repo. The skill activates automatically when you open it in Claude Code:

```bash
git clone https://github.com/Infrasity-Labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
claude
```

Then trigger it with:

```
/dev-gtm prospect AI Agentic, pre-seed to Series A, under 50 headcount
```

Or describe what you want naturally. Claude activates the skill when you name a vertical and ask for a prospect list or leads.

### Claude Web (Free / Pro)

1. Go to **[Settings → Capabilities](https://claude.ai/settings/capabilities)** and enable **Code execution and file creation**
2. Go to **[Customize → Skills](https://claude.ai/customize/skills)**
3. Click **+** → **Create skill** → **Upload a skill**
4. Zip this skill folder and upload it:

```bash
cd dev-gtm-claude-skills/skills/dev-marketing-prospector
zip -r ../dev-marketing-prospector.zip *dev-marketing-prospector/
```

Upload `dev-marketing-prospector.zip` and toggle it on.

---

## No API keys required

This skill runs entirely on web research. It does not need DataForSEO, Ahrefs, or any other paid integration. Accuracy comes from casting a wide net across credible public sources (Crunchbase, PitchBook, LinkedIn, GitHub, Y Combinator, TechCrunch, Sacra, and more) and cross-checking critical numbers like funding total and headcount against at least one source before a company is included.

---

## How to use

```
Prospect AI agent companies, Series A, 50 to 200 headcount
```

```
Find companies in the Observability vertical, seed to Series A, under 80 people
```

```
Build a prospect list for FinOps startups, pre-seed to seed, max 40 headcount
```

```
/dev-gtm prospect IAC, seed to Series A, under 60 headcount
```

Every request needs all three inputs. If any is missing, Claude asks for it before starting. For a vertical that is not already defined, Claude states its understanding back to you in a few sentences and waits for confirmation before researching companies.

### Inputs

| Field | Required | Notes |
|-------|----------|-------|
| Vertical | ✅ | The exact market segment to prospect within (e.g. AI Agentic, DevTools, Observability) |
| Funding stage | ✅ | The range to include, e.g. pre-seed to Series A |
| Headcount | ✅ | The maximum employee count a company can have to qualify |

---

## Output

A rendered HTML widget showing every qualifying company in a horizontally scrollable table, sorted by funding stage (Bootstrap, Pre-seed, Seed, Series A, Series B, Series C+) and alphabetically within each stage.

Nine columns:

| Column | What goes in it |
|--------|-----------------|
| Company | Name, funding badge, founded year, and optional phase descriptor |
| URL | Website link |
| LinkedIn | LinkedIn company page link |
| Headcount | Employee count |
| Signal + Why Dev Marketing | The recent trigger event tied to why developer marketing matters for this company now |
| Signal Sources | Numbered, clickable source links (S1, S2 ...) |
| Geography | HQ country flag, country, and city |
| Pain Point | The specific developer marketing gap plus its consequence |
| Pain Point Sources | Numbered, clickable source links (P1, P2 ...), with ⚠ on self-reported claims |

The header bar shows the vertical name and the active filters. A footer explains the ⚠ flag and the estimate disclaimer. When fewer than five companies qualify, a note box explains why and what you can loosen.

---

## Things to know

**Exact fit only, never adjacent.** Every company on the list should feel like it belongs in the same sentence as the others. If a company is around the vertical rather than exactly in it, it is excluded, even if that makes the list short.

**A short honest list beats a padded one.** The skill never adds adjacent companies to hit a count. If nothing qualifies under your criteria, it says so and explains why. If a tight funding cap is shrinking the list in a fast-moving vertical, it tells you and offers to remove the cap.

**Three tiers of sourcing.** Directly sourced facts get a plain link. Self-reported company claims (from a blog, press release, or CEO quote) get a ⚠ flag and must be framed as "Company X claims" in any outreach. Inferences drawn from two or more sourced numbers are labelled as inferences, not citations.

**Signals answer "why now."** Each signal is a recent, verifiable event (a funding round, launch, partnership, hiring spike, or award), not a stale fact from a year ago, and it is connected explicitly to why developer marketing is relevant at this stage.

**Self-reported stats are traced to the origin.** When a number comes from the company itself, the skill finds where it first appeared rather than citing a third-party article that repeats it.

---

## How it works

1. **Understand the vertical** reads `references/vertical-definitions.md` and forms a precise definition: the core problem, what companies build, the technical ICP, and the AI disruption angle. New verticals are confirmed with you first.
2. **Apply the hard filters** keeps only companies that pass all five at once: exact vertical fit, SaaS / product-first, developer-facing, in the funding range, and within the headcount cap.
3. **Research across all credible sources** casts wide across funding databases, discovery sources, people data, open-source signals, revenue estimates, and recent news. Critical numbers are verified against at least one source.
4. **Map one signal per company** identifies a single recent, verifiable "why now" trigger and ties it to a developer marketing reason.
5. **Source every signal data point** records a URL for each fact and classifies it as directly sourced, self-reported, or inferred.
6. **Map one pain point per company** names the specific developer marketing gap and its consequence, tied to real numbers and competitor context.
7. **Source every pain point data point** applies the same three-tier sourcing, tracing self-reported stats back to their origin.
8. **Produce the unified output table** renders the nine-column HTML widget, sorted by funding stage, using the spec in `references/output-format.md`.

---

## File structure

```
dev-marketing-prospector/
├── SKILL.md                          # Skill instructions Claude follows
├── README.md                         # This file
└── references/
    ├── vertical-definitions.md       # Precise definitions of all known verticals + new-vertical protocol
    └── output-format.md              # HTML table spec: column widths, badge colours, source format, flags
```
