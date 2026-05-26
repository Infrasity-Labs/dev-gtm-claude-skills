Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

- **`docs-audit <url>`** — Invoke the `docs-auditor` skill. Pass the URL as the docs site to audit.
- **`api-audit <url>`** — Invoke the `api-docs-audit` skill. Pass the URL as the API docs site to audit.
- **`blog-count <company or domain>`** — Invoke the `blog-post-counter` skill. Pass the company name or domain.
- **`brief-outline <keyword or title>`** — Invoke the `brief-outline-generator` skill. Pass the keyword or blog title.
- **`growth-report <target_domain> [competitor1] [competitor2] ...`** — Invoke the `growth-report` skill. Pass the target domain and any competitor domains.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Available commands:

  /dev-gtm docs-audit <url>                         Audit developer docs — 33 checks, 0-100 score
  /dev-gtm api-audit <url>                          Audit API docs — 5 checks per endpoint, HTML report
  /dev-gtm blog-count <company or domain>           Count blog posts for any company
  /dev-gtm brief-outline <keyword or title>         Generate SEO content outline as .docx
  /dev-gtm growth-report <domain> [competitors...]  3-month SEO performance report
```
