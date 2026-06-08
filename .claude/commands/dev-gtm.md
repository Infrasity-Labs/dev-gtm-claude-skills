Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

- **`docs-audit <url>`** — Invoke the `docs-auditor` skill. Pass the URL as the docs site to audit.
- **`sdk-audit <url>`** — Invoke the `sdk-docs-auditor` skill. Pass the URL as the SDK docs site to audit.
- **`api-audit <url>`** — Invoke the `api-docs-quality-report` skill. Pass the URL as the API docs site to audit.
- **`blog-count <company or domain>`** — Invoke the `blog-post-counter` skill. Pass the company name or domain.
- **`brief-outline <keyword or title>`** — Invoke the `brief-outline-generator` skill. Pass the keyword or blog title.
- **`growth-report <target_domain> [competitor1] [competitor2] ...`** — Invoke the `growth-report` skill. Pass the target domain and any competitor domains.
- **`llms-check <domain>`** — Invoke the `llms-txt-checker` skill. Pass the domain to audit for AI-readiness (robots.txt, llms.txt, llms-full.txt).
- **`orphan-pages <domain>`** — Invoke the `orphan-pages-internal-linking-opportunities` skill. Pass the domain to find orphan pages with zero incoming internal links.
- **`dead-end-pages <domain>`** — Invoke the `no-outlinks-audit` skill. Pass the domain to find dead-end pages with zero outgoing internal links.
- **`prospect <domain or ICP>`** — Invoke the `dev-marketing-prospector` skill. Pass the domain or ICP to find developer-marketing prospects.

For marketing skills (ads, SEO, content, copy, lifecycle, pricing, etc.), use `/marketing` instead.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Available commands:

  /dev-gtm docs-audit <url>                         Audit developer docs — 33 checks, 0-100 score
  /dev-gtm sdk-audit <url>                          Audit SDK docs — scored HTML report
  /dev-gtm api-audit <url>                          Audit API docs — 5 checks per endpoint, HTML report
  /dev-gtm blog-count <company or domain>           Count blog posts for any company
  /dev-gtm brief-outline <keyword or title>         Generate SEO content outline as .docx
  /dev-gtm growth-report <domain> [competitors...]  3-month SEO performance report
  /dev-gtm llms-check <domain>                      Audit AI-readiness — robots.txt, llms.txt, llms-full.txt
  /dev-gtm orphan-pages <domain>                    Find pages with zero incoming internal links
  /dev-gtm dead-end-pages <domain>                  Find pages with zero outgoing internal links
  /dev-gtm prospect <domain or ICP>                 Find developer-marketing prospects

  For marketing skills, run /marketing
```
