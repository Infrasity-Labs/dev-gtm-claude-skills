---
name: reddit-comments
user-invokable: true
description: Draft, review, and refactor Reddit comments for any company by providing a domain URL and a Reddit thread. Dynamically extracts product knowledge, approved terminology, voice and tone, and positioning guidelines from the domain before writing. Use this skill whenever the user provides a domain and a Reddit thread and asks to write, draft, review, or refactor a Reddit comment or engagement reply. Trigger on inputs like "Domain: [url] Thread: [url or paste]", "write a Reddit comment for this domain", "draft an engagement for this thread", or any variation where a company URL and a Reddit thread are both provided. Always use this skill — never write Reddit comments for a domain without following this full workflow.
---

# Dynamic Reddit Engagement Skill

Draft, review, and refactor Reddit comments for any company. Product knowledge, terminology, voice, positioning, and relevance rules are all derived from the domain provided — nothing is hardcoded.

---

## Input Format

```
Domain: [company URL]
Thread: [Reddit thread URL or paste]
```

Both inputs are required before starting. If either is missing, ask for it before proceeding.

---

## Step 1 — Domain Intelligence Extraction

### 1a. Sitemap Discovery (Run First, Always)

Before fetching any page, extract the full URL map of the domain using curl. Follow this exact sequence:

**Step 1: Check robots.txt for sitemap location**
```bash
curl -s https://[domain]/robots.txt
```
Look for a `Sitemap:` directive. If none found, try `https://[domain]/sitemap.xml` directly.

**Step 2: Fetch the sitemap**
```bash
curl -s https://[domain]/sitemap.xml
```
If it returns a sitemap index (multiple `<sitemap>` entries), fetch each sub-sitemap individually. If it's a single sitemap, extract URLs directly.

**Step 3: Extract all unique English-only URLs**
```bash
curl -s [sitemap_url] | grep -oP '(?<=<loc>)[^<]+' | grep -vP '/(es|de|fr|pt-BR|ja|ko|zh)/' | sort | uniq
```
Filter out all localised variants — keep only the base English URLs.

**Step 4: Select 8–10 pages for fetching**

From the full URL list, prioritise in this order:
1. Homepage — `/` or `/home`
2. Features / Product — `/features`, `/product/features`, `/product`
3. Pricing — `/pricing`
4. About — `/about-us`, `/about`
5. Use case page most relevant to the Reddit thread topic (e.g. `/use-cases/sales` for a sales thread)
6. One integration page relevant to tools mentioned in the thread
7. Customers or social proof — `/customers`
8. One blog post if the blog is accessible

Never fetch legal, forms, locale variants, or auth-gated pages.

**Step 5: web_fetch each selected page**

Fetch the 8–10 selected URLs using `web_fetch`. Extract domain intelligence from the content of those pages only.

---

### 1b. What to Extract From the Pages

**Who is [Company]**
- What does the product do in one sentence?
- Who is it built for (ICP — role, company size, industry)?
- What problem does it solve?
- Where does it sit in the stack or workflow?

**Core Technical Facts**
- Key features and capabilities
- How it works (architecture, integrations, workflow)
- Specific metrics or proof points mentioned on the site (speed, accuracy, cost savings, scale)
- Named integrations, platforms, or tools it connects with
- Products or tiers (if multiple)
- Notable customers or recognition mentioned

**Approved Terminology**
- Exact words and phrases the company uses to describe themselves and their product (pull directly from website copy)
- How they describe their category (e.g. "AI meeting assistant", "semantic layer", "observability platform")
- How they describe their differentiators
- Words or phrases they noticeably avoid

**Positioning**
- Primary differentiator vs alternatives
- What they lead with (price, performance, privacy, developer experience, etc.)
- Their narrative — what story does the website tell?
- What they explicitly do NOT claim (read disclaimers, fine print, comparison pages)

**Voice and Tone**
- Infer from homepage copy, blog posts, and about page
- Is the brand voice technical or accessible? Formal or casual? Direct or explanatory?
- Do they use humour, strong claims, community language?
- This becomes the baseline for how the product should be mentioned in a Reddit context

**What NOT to Claim**
- Features or capabilities not mentioned on the site — do not invent them
- Claims that contradict anything on the site
- Competitor comparisons not supported by the site
- Any pricing, availability, or roadmap specifics not stated

---

## Step 2 — Thread Intelligence

### Apify Connector (Optional)

Before fetching the Reddit thread, check if Apify MCP tools are available (any tool whose name includes `apify`).

**If Apify is available** — use the `apify/reddit-scraper` actor with the thread URL as input. It returns the full thread title, all comments with upvotes and reply structure, author metadata, and post date as structured JSON. Use this output directly for the extraction steps below — no WebFetch needed.

**If Apify is not available** — continue with WebFetch on the thread URL as described below.

> 💡 **Apify not connected** — Reddit threads will be read via WebFetch, which may be blocked or rate-limited by Reddit. Connect the Apify MCP connector to use `apify/reddit-scraper` for reliable full-thread extraction.

---

Read the full Reddit thread before writing. Extract:

1. What is the OP's actual question or pain? (Not the surface ask — the underlying problem)
2. What tool, product, or approach are they currently on or evaluating?
3. What do they care most about — price, performance, privacy, ease of use, trust, integrations, scale?
4. What is the tone of the thread — casual, technical, frustrated, exploratory?
5. What are the top existing replies saying? What angles are already covered?
6. Is the company/product already mentioned in the thread? If yes, address it naturally rather than introducing it cold.
7. Is there a genuine opening for this product, or would mentioning it feel forced?

If the product is not relevant to the thread, say so clearly and do not draft a comment. Forced placements hurt credibility.

---

## Step 3 — Relevance Check

Before drafting, confirm the product fits the thread. The product is relevant when:

- The thread is about a problem the product directly solves
- The OP is evaluating tools in the same category
- The thread involves a pain point the product's core features address
- The community is discussing a topic the company has credibility in

The product is NOT relevant when:

- The thread is about a tangential topic where the product would be a stretch
- The product would only be a partial or superficial fit
- Mentioning it would read as spam or off-topic
- The thread is about careers, off-topic opinions, or personal situations unrelated to the product's domain

If irrelevant → stop and tell the user why.

---

## Step 4 — Comment Writing Process

Follow this sequence for every comment drafted:

1. **Answer the question first.** The product comes in as supporting evidence, not as the answer itself.
2. **Pick an angle** that fits the thread — experience share, slight pushback, practical framing, specific insight. Match the angle to what the OP actually needs.
3. **Vary structure and opening across variants.** No two drafts should start the same way or follow the same pattern.
4. **Vary length** — short and punchy for simple threads, longer for technical or architectural discussions.
5. **Bring the product in as something used or tried**, not as a pitch. Framing like "been running [product] for this", "we switched to [product] when...", "what worked for us was..." — not "you should try [product]."
6. **Never drop a bare URL.** If the product must be referenced by name, the name alone is enough.
7. **Run the self-check before finalising.**

Produce **2–3 comment variants** per thread, each with a different angle or length. Label them clearly.

---

## Step 5 — Universal Reddit Voice Rules

These apply regardless of the company's brand voice. Reddit has its own norms and they override corporate tone.

**Always:**
- Lowercase throughout for longer replies. Proper nouns and product names keep their original casing.
- First-person, lived-experience framing: "we ran into this", "been using X for this", "what changed things for us was"
- Natural hedges: "honestly", "tbh", "fwiw", "ime", "pretty much", "kind of"
- Uneven clause lengths — real people don't write in perfect parallel structure
- Plain connectors: "and", "but", "so", "also", "though", "plus"

**Never:**
- Em dashes `—` — biggest single AI tell. Remove entirely or restructure the sentence.
- Semicolons `;` — almost no redditor uses them. Break into two sentences.
- Corporate connectors: moreover, furthermore, additionally, in addition, it is worth noting that
- Marketing adjectives: powerful, seamless, robust, cutting-edge, comprehensive, innovative, game-changer, best-in-class, world-class
- AI sign-offs: "hope this helps", "happy to elaborate", "great question", "feel free to reach out"
- Headers or bold text inside replies
- Bullet lists for short replies (under 5 items) — convert to prose
- Perfect parallelism — break it deliberately

---

## Step 6 — Self-Check Before Finalising

Run all 10 checks on every draft before presenting it:

1. Does it actually answer what the OP asked?
2. Is the product mentioned as something used, not pitched?
3. Is the product framed in a way consistent with what the domain actually claims?
4. Are there any em dashes, semicolons, or corporate connectors?
5. Are there any marketing adjectives (powerful, seamless, robust, etc.)?
6. Are there any claims not supported by the domain crawl?
7. Does it sound like something a real person with hands-on experience would write?
8. Is there a bare URL anywhere?
9. Does the opening vary from the other variants in the same batch?
10. Is the product placement natural, or does it feel inserted?

If any check fails — fix and re-check before presenting.

---

## Step 7 — Output Format

Present each variant clearly:

```
[Variant 1 — angle label, e.g. "Experience-led" or "Pushback + context"]
[comment text, plain prose, no formatting]

---

[Variant 2 — angle label]
[comment text]

---

[Variant 3 — angle label, optional]
[comment text]
```

No preamble before the comments. No explanation of what you did. Just the labelled variants, ready to paste into Reddit.

After the variants, include a one-line **Relevance note** confirming why this thread is a fit and which angle is strongest.

---

## Step 8 — Feedback Integration

If the user provides feedback after reviewing the drafts:

- Apply it precisely — do not over-correct beyond what was flagged
- Do not re-explain the change; just deliver the refined comment
- If feedback contradicts something extracted from the domain, flag it before applying
- Maintain all unchanged parts exactly as they were — only touch what was flagged

---

## What NOT to Do

- Do not write a comment if the thread is not a genuine fit
- Do not invent product features not found on the domain
- Do not use the same opening or structure across variants in a batch
- Do not over-mention the product — one natural reference per comment is enough
- Do not add questions back to the OP unless the thread tone calls for it
- Do not use "--" as an em dash replacement — restructure the sentence instead
- Do not inject Reddit meta-phrases ("this.", "came here to say this", "take my upvote") artificially
- Do not add emojis unless the thread tone clearly uses them