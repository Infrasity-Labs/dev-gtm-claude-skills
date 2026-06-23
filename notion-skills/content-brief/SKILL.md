---
name: content-brief
description: "Generates a fully structured SEO content brief for a target keyword and optionally pushes it to a Notion database. Use this skill whenever the user says 'create a content brief', 'brief this keyword', 'run a content brief for', 'generate a brief', 'write a brief for [keyword]', 'content brief on [topic]', or any variation where someone needs a keyword researched and turned into a structured writing assignment with H1, H2 outline, FAQ, internal links, word count target, and writer notes. Also triggers when the user provides a keyword and asks for an SEO brief, editorial brief, or writing spec. Outputs a mandatory structured format that the text parser maps directly to Notion properties. Supports single-keyword and batch (CSV) modes."
metadata:
---

# Content Brief — Keyword-to-Notion Brief Generator

Generates a structured SEO content brief from a target keyword. Output follows the mandatory Direction prompt format so the `text_parser.py` script can extract every field for Notion without manual cleanup.

## Invocation Triggers

**Explicit phrases** (any of):
- "create a content brief for [keyword]"
- "brief this keyword: [keyword]"
- "content brief on [topic]"
- "generate a brief for [keyword]"
- "write a brief for [keyword]"
- "run the content brief skill"

**Implicit signals:**
- User provides a keyword and asks for an SEO spec, editorial spec, or writing assignment
- User pastes a keyword list and asks for briefs

When triggered, run immediately — no upfront intake beyond the keyword itself.

## Grill-Me Intake (One Question, Optional)

Run the brief without questions when the keyword is clear.

Ask **one** clarifying question only when **both** are true:
1. The target audience or client is not inferrable from context
2. Audience changes the content angle meaningfully (e.g., "project management software" could target PMs or developers)

> **Quick clarification — who is the primary audience for "[keyword]"?**
> 1. [Inferred persona A — e.g., HR Director]
> 2. [Inferred persona B — e.g., Operations Manager]
> 3. Tell me
>
> *Why I'm asking: audience shapes the H1, content angle, and writer notes. One question prevents a wrong brief.*

Max one question. If audience is inferable, skip and proceed.

## Data Gathering (Before Writing the Brief)

Run these steps before generating the Direction prompt output:

### Step 1 — Keyword Metrics
**Preferred:** Ahrefs MCP (`keywords_explorer_overview`) → volume, KD, CPC, SERP data.

**Fallback (no Ahrefs MCP):** Use WebSearch to estimate:
- Search `[keyword] search volume KD CPC site:ahrefs.com OR site:semrush.com OR site:moz.com`
- Extract available volume/KD/CPC estimates
- If no data found, set VOLUME/CPC/DIFFICULTY to `[not available — add manually]`

### Step 2 — Competitor H2/H3 Analysis
- WebSearch `[keyword]` → identify top 3 organic results (skip ads, maps, featured snippets)
- WebFetch each URL → extract all H2 and H3 headings
- Note: competitor structure informs the H2_OUTLINE. Do not copy — use as gap analysis.

### Step 3 — Search Intent Classification
Based on keyword + SERP type, classify as one of exactly four options:
- `Informational` — user wants to learn
- `Commercial` — user is comparing options before buying
- `Transactional` — user is ready to act/purchase
- `Navigational` — user seeks a specific brand/site

### Step 4 — Priority Scoring
Apply routing logic from `references/routing-logic.md`:
- HIGH: Volume > 200 AND KD < 40 AND intent is Commercial or Transactional
- MEDIUM: Doesn't meet HIGH criteria but has meaningful volume or strategic importance
- LOW: Low volume, high difficulty, or informational with limited conversion value

## Direction Prompt Output Format (Mandatory)

**This format is non-negotiable.** The `text_parser.py` script performs label-exact extraction. If any label deviates from the format below — wrong case, extra space, missing underscore — the Notion property will arrive empty.

After data gathering, output the brief using EXACTLY this structure:

```
TARGET_KEYWORD: [keyword]
VOLUME: [number or "not available"]
CPC: [decimal or "not available"]
DIFFICULTY: [0-100 integer or "not available"]
SEARCH_INTENT: [Informational | Commercial | Transactional | Navigational]
AUDIENCE: [persona — job title or role]
RECOMMENDED_H1: [final proposed title]
CONTENT_ANGLE: [one paragraph describing the unique angle, why this beats competitors, what the post must do]
WORD_COUNT: [number]
SCHEMA: [schema type — e.g., FAQ, HowTo, Article, FAQ + HowTo]
PRIORITY: [HIGH | MEDIUM | LOW]
H2_OUTLINE:
- H2: [heading]
  - H3: [subheading]
  - H3: [subheading]
- H2: [heading]
  - H3: [subheading]
FAQ:
- Q: [question the audience actually searches]
- Q: [question]
- Q: [question]
INTERNAL_LINKS:
- [anchor text] → [relative URL or page title if URL unknown]
WRITER_NOTES:
[one paragraph of specific guidance: tone, POV, what to avoid, key differentiators to emphasize, CTAs, any client-specific requirements]
```

**Critical rules:**
- Every field label must appear exactly as shown (ALL_CAPS with underscores)
- SEARCH_INTENT value must exactly match one of the four options (capitalized)
- PRIORITY value must be exactly HIGH, MEDIUM, or LOW
- H2_OUTLINE, FAQ, INTERNAL_LINKS, WRITER_NOTES are block fields — content follows on the next line(s)
- No additional text before TARGET_KEYWORD or after WRITER_NOTES block

## Workflow Architecture (9 Nodes)

| Node | Role | Tool |
|---|---|---|
| 1 — Input | Accept keyword + optional client/audience context | User message |
| 2 — Keyword Metrics | Pull volume, KD, CPC, SERP type | Ahrefs MCP OR WebSearch fallback |
| 3 — SERP Scrape | Extract H2/H3 from top 3 organic results | WebFetch |
| 4 — Brief Generation | Process data through Direction prompt → structured output | Claude (this skill) |
| 5 — Text Parser | Extract labeled fields → structured variables | `scripts/text_parser.py` |
| 6 — Conditional Router | Route based on PRIORITY value | Routing logic |
| 7A — Notion Create (HIGH) | Create page, Status = "Briefed: Ready for Assignment" | Notion MCP |
| 7B — Notion Create (MED/LOW) | Create page, Status = "Briefed: Weekly Review Queue" | Notion MCP |
| 8A — Slack Notify (HIGH only) | Post brief summary + Notion link to channel | Slack MCP |
| 9 — Calendar Sync | Create linked entry in Content Calendar database | Notion MCP |

In Claude Code without MCP connectors: Nodes 1–5 run automatically. Nodes 6–9 produce a ready-to-paste summary and instruct the user on manual Notion entry.

## Batch Processing Mode

Trigger: user provides a CSV with a `Target Keyword` column (optional `Priority Override` column).

Process:
1. Confirm CSV is readable and `Target Keyword` column exists
2. Run each keyword through the full pipeline sequentially
3. Output all briefs in sequence, separated by `---`
4. After all briefs: output a summary table (keyword | priority | word count | schema)

Expected throughput: 20 briefs in 20–25 minutes (60–75 seconds per brief).

If any keyword fails (no SERP data, ambiguous intent): note it in the summary table as `[FAILED — reason]` and continue processing remaining keywords.

## Notion Push (When MCP Available)

Map parser output to Notion properties using `references/notion-schema.md`.

Two paths based on PRIORITY:

**HIGH:**
- Status → "Briefed: Ready for Assignment"
- Target Publish Date → today + 14 days
- Trigger Slack notification (Node 8A)

**MEDIUM:**
- Status → "Briefed: Weekly Review Queue"
- Target Publish Date → today + 28 days

**LOW:**
- Status → "Briefed: Weekly Review Queue"
- Target Publish Date → today + 42 days

After page creation: run Calendar Sync (Node 9) to create linked entry in Content Calendar database.

Pre-check before creating: query Notion for existing page with same TARGET_KEYWORD. If found → route to `update_page` instead of `create_page` to prevent duplicates.

## Multi-Client Setup

Each client has:
- Separate Notion integration token
- Separate database ID
- Client-specific Direction prompt variant (adjust audience, tone, internal link base URLs)

Onboarding a new client: ~45–60 minutes to configure connector + test one brief end-to-end.

## Output When Notion MCP Is Not Connected

If Notion MCP is not available, after generating the Direction prompt output, append:

```
---
NOTION PUSH: Not connected. To add this brief to Notion manually:

1. Open your Notion database
2. Create a new page
3. Paste the following field values:
   [formatted summary of all extracted fields]

Or run: python scripts/text_parser.py brief.txt --output json
to get a JSON payload ready for the Notion API.
---
```

## Validation Gate

After generating output, mentally verify:
- All 11 simple fields are present and non-empty
- SEARCH_INTENT is one of the 4 valid values
- PRIORITY is exactly HIGH, MEDIUM, or LOW
- H2_OUTLINE has at least 4 H2s each with at least 1 H3
- FAQ has at least 3 questions
- INTERNAL_LINKS has at least 2 entries
- WRITER_NOTES is a substantive paragraph (not a placeholder)

Run `scripts/brief_validator.py` on the output file for automated validation.

## Error Handling

| Situation | Behavior |
|---|---|
| No keyword data available | Set numeric fields to "not available", add note in WRITER_NOTES instructing editor to verify manually |
| SERP scrape blocked (403/paywalled) | Skip scrape, note "competitor outline not available" in WRITER_NOTES, proceed with brief |
| Ambiguous search intent | Default to Informational; flag in WRITER_NOTES: "Intent ambiguous — verify before briefing writer" |
| Select value mismatch in Notion | Capitalize values exactly; Notion select is case-sensitive |
| Duplicate keyword detected | Route to update_page instead of create_page |
| >2 empty properties in parsed brief | Flag for manual review; do not push to Notion |
| Batch keyword fails | Note in summary table, continue processing |
| CSV missing Target Keyword column | Stop and ask user to confirm column name |

See `references/error-handling.md` for full failure-point catalog.

## Tooling

| Script | Role |
|---|---|
| `scripts/text_parser.py` | Extracts labeled fields from Direction prompt output → structured dict. `python text_parser.py brief.txt --output json` |
| `scripts/brief_validator.py` | Validates all required fields are present, values are in allowed sets. `python brief_validator.py brief.txt` |

## References

- `references/notion-schema.md` — Notion database property config (names, types, allowed values)
- `references/routing-logic.md` — Priority scoring rules and publish date calculations
- `references/error-handling.md` — Known failure points and fixes

## Anti-Patterns To Reject

- Deviating from the mandatory Direction prompt label format (breaks parser)
- Using lowercase or mixed-case field labels (TARGET_KEYWORD not Target_Keyword)
- Putting SEARCH_INTENT outside the four allowed values
- Generating a brief without first gathering keyword + SERP data
- Asking multiple intake questions before running
- Writing vague WRITER_NOTES ("write a good post about this topic")
- Fabricating keyword metrics when data is unavailable — always flag as "not available"
- Pushing to Notion when >2 fields are empty

