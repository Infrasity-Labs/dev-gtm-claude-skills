# Bing Webmaster Tools + IndexNow extension setup

## What this gives you

1. **Bing Webmaster Tools API**: inbound links, crawl stats, search
   keywords, and competitor link comparison via
   `scripts/bing_webmaster.py` (already shipped with seo-skills).
2. **IndexNow URL submission** for Bing, Yandex, Seznam, Naver via
   `scripts/indexnow_submit.py`. The single POST hits all four
   engines.
3. A unified `seo-bing` skill that routes the right command at the
   right script.

## Install

```bash
./extensions/bing-webmaster/install.sh
.\extensions\bing-webmaster\install.ps1
```

You'll be prompted for:

- Bing Webmaster Tools API key (https://www.bing.com/webmasters/api)
- IndexNow host key (any random 32+ char string)
- IndexNow keyLocation URL (must serve the key file at that URL)

Both groups can be left blank if you only want one. The installer
writes only the env vars you provide.

## IndexNow setup checklist

1. Generate a key: `openssl rand -hex 32`
2. Save the key to a file at the **root** of your site, named `<key>.txt`,
   served at `https://example.com/<key>.txt`. The file body is the key.
3. Run:
   ```
   /seo bing verify-indexnow
   ```
   The verifier fetches your keyLocation URL and confirms the body
   matches the key — the #1 onboarding mistake.

## Microsoft Copilot citation

Microsoft Copilot pulls citations from the Bing index. Pages that
aren't in Bing aren't citable. IndexNow gets a page into Bing
within minutes vs. Bing's organic crawl which can take days. For
new content launches this is a meaningful indexing speed win.

## Uninstall

```bash
./extensions/bing-webmaster/uninstall.sh
```
