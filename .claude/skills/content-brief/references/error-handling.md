# Error Handling — Known Failure Points and Fixes

Five documented failure points and additional Claude Code-specific failure modes.

## Failure Point 1 — Parser Extraction Failure (Most Common)

**Symptom:** One or more Notion properties arrive empty after push.

**Root cause:** The Direction prompt output used a field label that didn't exactly match the parser's expected label. Examples of silent mismatches:
- `Target_Keyword:` instead of `TARGET_KEYWORD:`
- `Search Intent:` instead of `SEARCH_INTENT:`
- Extra space before the colon: `VOLUME :`
- Label in a sentence: "The TARGET_KEYWORD is..."

**Fix:**
1. Run `python text_parser.py brief.txt` before pushing — empty fields show as `[missing]`
2. Ensure the Direction prompt output starts exactly at `TARGET_KEYWORD:` with no preamble
3. Label format is `ALL_CAPS_WITH_UNDERSCORES:` — no deviation

**Prevention:** The SKILL.md Direction prompt format section states "no additional text before TARGET_KEYWORD". Enforce this in system prompt configuration.

---

## Failure Point 2 — Select Property Value Mismatch

**Symptom:** Notion rejects the API call or creates a page with a blank select field.

**Root cause:** Select property values in Notion are case-sensitive and must exactly match the pre-configured options. Common mismatches:
- `commercial` instead of `Commercial`
- `high` instead of `HIGH`
- `FAQ+HowTo` instead of `FAQ + HowTo` (spacing matters)

**Fix:**
1. Run `python brief_validator.py brief.txt` — it checks exact select values
2. In Notion, verify the select options match exactly what the Direction prompt produces
3. Capitalize values in the prompt instruction exactly as they appear in `references/notion-schema.md`

**Prevention:** The four Search Intent values and three Priority values are fixed in the Direction prompt. Don't modify their casing.

---

## Failure Point 3 — Empty Properties (>2 Missing Fields)

**Symptom:** Brief pushed to Notion with multiple blank properties; page is unusable.

**Root cause:** Keyword data unavailable (no Ahrefs access, SERP blocked), or Claude output truncated before completing all fields.

**Fix:**
1. `brief_validator.py` flags briefs with >2 empty fields as FAIL — do not push
2. Route failed briefs to fallback output (save as local .txt file or paste to Slack) to prevent data loss
3. Continue processing remaining keywords in batch mode

**Prevention:** Set numeric fields to `not available` (not blank) when data is unavailable — validator treats this as WARN not FAIL.

---

## Failure Point 4 — Duplicate Page Creation

**Symptom:** Multiple Notion pages created for the same keyword across runs.

**Root cause:** No pre-check before calling `create_page`.

**Fix:**
1. Before every Notion push, query the database: `filter: Target Keyword equals [TARGET_KEYWORD]`
2. If a matching page exists → route to `update_page` instead of `create_page`
3. In batch mode, maintain a local set of keywords processed in the current run

**Prevention:** Make the pre-check query a mandatory Node 6.5 in the workflow.

---

## Failure Point 5 — Calendar Sync Timing (Rendering Delay)

**Symptom:** Brief page body appears empty immediately after push, then populates 5–10 seconds later.

**Root cause:** Notion's rendering pipeline has a brief delay between API write and UI render. This is not a data issue — the data is written correctly.

**Fix:** Not actionable — this is expected Notion behavior. Inform users: "If the page looks empty immediately after push, wait 10 seconds and refresh."

**Do not** re-submit the brief if the page appears empty immediately.

---

## Claude Code-Specific Failure Modes

### No Ahrefs MCP Connected

**Symptom:** Volume, CPC, Difficulty show as "not available".

**Fix:** Use WebSearch fallback (see SKILL.md Step 1). Set numeric fields to "not available" and add a note in WRITER_NOTES: "Keyword metrics unavailable — verify via Ahrefs or SEMrush before briefing writer."

Validator treats "not available" as WARN (not FAIL) — brief can still be pushed.

### SERP Scrape Blocked (403 / Paywalled)

**Symptom:** WebFetch returns 403 or paywalled content for competitor URLs.

**Fix:** Skip the competitor H2 analysis for that URL. Note in WRITER_NOTES: "Competitor outline not available for [URL] — editor should manually review top 3 results before drafting." Continue with remaining URLs.

### Notion MCP Not Connected

**Symptom:** Brief generated but no Notion push occurs.

**Fix:** Output the formatted brief + a manual entry summary. Run `text_parser.py --output notion` to get a JSON payload the user can paste into a Notion API call manually.

### Batch CSV Parse Error

**Symptom:** CSV doesn't parse or `Target Keyword` column not found.

**Fix:** Stop immediately. Ask user: "I couldn't find a 'Target Keyword' column. Can you confirm the column name?" Do not guess column names.
