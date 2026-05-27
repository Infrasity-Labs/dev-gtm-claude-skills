---
name: sdk-docs-auditor
description: Audits any SDK documentation site and produces a fully scored, downloadable HTML report. Use this skill whenever a user provides a documentation URL and asks to audit, review, analyse, score, or check the quality of SDK docs. Also trigger for phrases like "audit the SDK docs at X", "check if the docs at X are complete", "review this SDK documentation", "how good are these docs", "run an SDK audit on X", or any time a user pastes a URL alongside words like audit, review, crawl, check, analyse, quality, completeness, or gaps. ALWAYS use this skill — do not attempt the audit without following this structured crawl → analyse → cross-reference → report workflow.
---

# SDK Docs Auditor

Produces a comprehensive, cross-referenced audit of any SDK documentation site with a fully styled downloadable HTML report.

## What this skill does

1. Discovers all SDK pages via `llms.txt` first, falling back to homepage nav crawl
2. Fetches and reads every relevant SDK page
3. Audits six fixed sections: Installation, Quick Start, Error Handling, Troubleshooting, Examples, Best Practices
4. Cross-references every gap across ALL other SDK pages — never flag something as missing if it exists elsewhere
5. Scores each section 0–100 and assigns a rating tier
6. Generates a beautiful, self-contained, downloadable HTML report

---

## Step 1 — Discover all SDK pages

### 1a. Try llms.txt first

Fetch `<docs_url>/llms.txt`.

If found:
- Extract every URL from lines matching the pattern `- [Page Title](URL): description`
- Filter to SDK-relevant pages only — keep URLs whose path contains any of:
  `sdk`, `installation`, `quickstart`, `quick-start`, `error`, `troubleshoot`, `example`, `best-practice`, `getting-started`, `reference`, `api-reference`, `overview`, `client`, `service`, `memory`, `search`, `worker`, `job`, `policy`, `agent`, `team`
- Exclude: marketing pages, changelog, blog, legal, community/forum pages
- Store as `SDK_PAGES[]` — list of `{title, url, description}`

If not found or returns an error:
- Fetch the docs homepage (`<docs_url>`)
- Extract all links from the nav sidebar or sitemap structure
- Filter using the same keyword list above
- Extract all SDK-relevant page URLs from the nav structure
- Note in the report that llms.txt was unavailable and nav crawl was used instead

### 1b. Identify section mapping

From the discovered pages, identify which pages map to the six audit targets:

| Audit section | Look for paths/titles containing |
|---|---|
| Installation | `install`, `setup`, `getting-started` |
| Quick Start | `quick-start`, `quickstart`, `tutorial` |
| Error Handling | `error`, `exception`, `errors` |
| Troubleshooting | `troubleshoot`, `faq`, `debug` |
| Examples | `example`, `sample`, `cookbook`, `tutorial` |
| Best Practices | `best-practice`, `guide`, `pattern` |

If a dedicated page is not found for a section, note it — the absence itself is a finding.

### Build the corpus

All discovered pages form the **page corpus** used for both section auditing and cross-referencing.

Report discovery summary:
> Found N pages. llms.txt [found / not found — used nav crawl]. Fetching now...

---

## Step 2 — Fetch every page in the corpus

Fetch each page using `web_fetch`. Store the full text content for cross-referencing.

For large sites (>30 pages), prioritise in this order:
1. The six target section pages (installation, quick-start, error-handling, troubleshooting, examples, best-practices)
2. Overview / client overview pages
3. API reference
4. Service-specific pages (agents, jobs, workers, policies, memory, search, etc.)

---

## Step 3 — Audit the six target sections

For each of the six sections below, read its page carefully and evaluate against the criteria. Then check every other fetched page to see if any gap is actually addressed elsewhere.

### 3a. Installation

**Must have (deduct heavily if missing):**
- Prerequisites with exact versions (Python/Node/language version, package manager)
- At least one complete install command (pip/npm/etc.)
- Authentication setup with exact steps to obtain and configure credentials
- A working verification snippet that proves the install succeeded
- At least one expected output or confirmation of success

**Should have (deduct moderately):**
- Multiple install methods (package manager, source, Docker)
- IDE/editor setup
- Environment variable configuration with `.env` examples
- Version compatibility table
- Optional dependency explanations (what each extra includes)
- Constructor parameter reference (all params, types, defaults)

**Common gaps to check across other pages:**
- Env-var auto-detection (does the client read env vars when called with no args?) — check api-reference, overview
- Advanced constructor params (timeout, retries, org) — check api-reference
- Version pinning guidance — check any getting-started pages

### 3b. Quick Start

**Must have:**
- A minimal, numbered step-by-step path a first-time user can follow in under 5 minutes
- Complete working code from zero to first successful call
- Expected output for every code snippet
- Explanation of any prerequisite service/resource (queues, workers, etc.)

**Should have:**
- Both env-var and inline credential patterns
- Multiple install options (pip + poetry, etc.)
- Links to deeper docs for each concept introduced

**Common gaps to check:**
- Worker/queue prerequisites — check workers/environments pages
- Valid model/runtime IDs — check models/runtimes service pages
- Execute call signature accuracy — check api-reference and agents service pages

### 3c. Error Handling

**Must have:**
- Complete exception hierarchy (all exception classes, inheritance tree)
- Every exception class documented with: description, import path, code example
- At minimum: authentication, connection, timeout, rate-limit, API/HTTP errors
- HTTP status code branching (400/401/403/404/500 at minimum)
- At least one resilience pattern (retry with backoff)

**Should have:**
- Resource-specific exceptions (one per major service)
- Streaming error handling
- Context manager cleanup pattern
- Testing/pytest examples for error scenarios
- Do/don't anti-pattern examples

**Cross-reference check — critical:**
- List every exception class that appears in the api-reference or service pages
- Flag any that are missing from this page
- Check execute/method call signatures match across all pages — flag any discrepancies

### 3d. Troubleshooting

**Must have:**
- Authentication failures with diagnostic steps
- Connection / timeout issues with solutions
- At least one service-specific troubleshooting section

**Should have:**
- Troubleshooting for every major service (workers, jobs, policies, agents, etc.)
- Self-hosted / custom base_url issues
- Import errors with correct import paths
- A summary error-message lookup table
- Rate limiting with backoff references
- Actionable "getting help" checklist with actual links/commands

**Cross-reference check:**
- For every service page that has its own error handling section, check if its scenarios appear here
- Check if dataset/resource creation methods are linked when "not found" errors are described
- Check if health check API is referenced in the "verify status" step

### 3e. Examples

**Must have:**
- At least one complete, runnable end-to-end example per major service
- Expected output shown for every example
- Error handling within workflow examples

**Should have:**
- Coverage across: agent lifecycle, jobs/scheduling, memory/recall, semantic search, policy management, worker management, streaming
- No "workflow" examples that only survey resources without executing anything
- Multi-turn / session management examples where the SDK supports sessions

**Cross-reference check — this is where most gaps accumulate:**
- For every service that has its own dedicated page with examples, check if those examples are represented here
- Flag each missing service category with the source page that has the examples

### 3f. Best Practices

**Must have:**
- Authentication / credential security section
- Error handling / retry logic
- Performance (batching, pagination, caching)

**Should have:**
- One best-practices section per major service (workers, jobs, policies, agents)
- Resource cleanup / context managers
- Code organisation (type hints, reusable functions)
- Testing patterns
- Concurrency / thread-safety guidance
- Secret rotation / credential lifecycle

**Cross-reference check:**
- For every service page that defines its own best practices, check if those patterns appear here
- Note if concurrency/thread-safety is addressed anywhere in the entire corpus

---

## Step 4 — Score each section

Score 0–100 using this rubric:

| Score | Meaning |
|-------|---------|
| 85–100 | Strong — all must-haves present, most should-haves, few gaps |
| 70–84 | Good — all must-haves, some should-haves missing |
| 50–69 | Adequate — most must-haves but notable gaps |
| 30–49 | Weak — multiple must-haves missing |
| 0–29 | Poor — section is superficial or largely absent |

Assign a rating label: **Strong / Good / Adequate / Weak / Poor**

---

## Step 5 — Build the gap list for each section

For every gap:
- Write a clear one-sentence description of what is missing
- Tag it with where the content EXISTS in the corpus (if it does): `[covered in: page-name]`
- Or tag it: `[not covered anywhere in corpus]`

This distinction is critical — a gap that exists nowhere needs a new page; a gap that exists elsewhere just needs a cross-reference or consolidation.

---

## Step 6 — Derive top priority recommendations

Rank the top 6–8 actions by impact × effort. Prioritise:
1. Factual errors / signature mismatches (highest priority — causes user failures)
2. Must-have gaps not covered anywhere
3. Must-have gaps covered elsewhere but not linked
4. High-value should-have gaps
5. Cross-referencing and consolidation opportunities

---

## Step 7 — Generate the HTML report

Read the template at `assets/report-template.html` and inject all audit data into it.

Fill these placeholders:
- `__AUDIT_URL__` → the audited URL
- `__PAGES_FETCHED__` → total pages fetched
- `__AUDIT_DATE__` → today's date
- `__SECTION_DATA_JSON__` → JSON blob (see schema below)
- `__PRIORITIES_JSON__` → JSON blob (see schema below)
- `__OVERALL_SCORE__` → integer 0-100 (weighted average of six scores)

### Data schema

```json
{
  "sections": [
    {
      "num": "01",
      "name": "Installation Guide",
      "rating": "Good",
      "score": 74,
      "strengths": ["string", ...],
      "gaps": [
        {
          "text": "Description of the gap",
          "covered_in": ["page-name-1", "page-name-2"],
          "nowhere": false
        }
      ]
    }
  ]
}
```

Set `"nowhere": true` and `"covered_in": []` when the gap exists nowhere in the corpus.

```json
{
  "priorities": [
    {
      "rank": 1,
      "text": "Fix X in Y page. The correct form per api-reference is Z.",
      "type": "error"
    }
  ]
}
```

Priority types: `"error"` (factual mistake), `"missing"` (not covered anywhere), `"xref"` (covered elsewhere, needs linking), `"improvement"` (should-have gap).

---

## Output

Save the final report to `/mnt/user-data/outputs/sdk-audit-report.html` and present it with `present_files`.

Tell the user:
- How many pages were fetched
- The overall score and what it means
- The single most critical finding

Do NOT reproduce the full report text in the chat — just present the file and give the brief summary.