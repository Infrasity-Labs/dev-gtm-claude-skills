---
name: seo-bing
description: Bing Webmaster Tools + IndexNow extension. Microsoft Copilot citations are fed by the Bing index; this skill makes Bing visibility, link data, and IndexNow URL submission first-class.
metadata:
compatibility: "Requires BING_WEBMASTER_API_KEY and (optionally) INDEXNOW_KEY in ~/.claude/settings.json env. Run extensions/bing-webmaster/install.sh to configure."
---

# seo-bing

The non-Google indexing surface. Google still rejects IndexNow (per
Gary Illyes, multiple SOTR episodes 2024-2025), so this skill is
specifically for **Bing/Yandex/Seznam/Naver indexing** and
**Microsoft Copilot AI citation** (which pulls from the Bing index).

## Prerequisites

- Run `extensions/bing-webmaster/install.sh` or `install.ps1`.
- A Bing Webmaster Tools API key.
- Optional: an IndexNow host key (32+ chars) published at the URL
  declared as `INDEXNOW_KEY_LOCATION`.

## Routing

| Command | Underlying script |
|---|---|
| `/seo bing links <url>` | `python scripts/bing_webmaster.py links <url>` |
| `/seo bing compare <urlA> <urlB>` | `python scripts/bing_webmaster.py compare <urlA> <urlB>` |
| `/seo bing submit <url>` (single URL) | `python scripts/indexnow_submit.py --host ... --urls <url>` |
| `/seo bing submit-batch <file>` | `python scripts/indexnow_submit.py --urls-file <file>` |
| `/seo bing verify-indexnow` | `python scripts/indexnow_submit.py --verify-only` |

## When this skill applies

- The user is publishing new pages and wants Microsoft Copilot
  citation eligibility (Bing index ingestion).
- The user wants to nudge Bing/Yandex/Seznam/Naver indexing for fresh
  URLs.
- The user is doing competitor backlink analysis and wants Bing's
  unique link data (Bing tracks links Google's API doesn't surface).

## Cross-skill delegation

- For Google indexing (very different model — sitemap-driven, no
  IndexNow), use `seo-google indexing`.
- For multi-source backlink confidence weighting, fall back to
  `seo-backlinks` which already integrates Bing + Moz + CC.
