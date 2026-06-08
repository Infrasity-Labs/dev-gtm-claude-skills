# Marketing CLIs

Zero-dependency, single-file CLI tools for marketing platforms that don't ship their own.

Every CLI is a standalone Node.js script (Node 18+) with no `npm install` required — just `chmod +x` and go.

## Install

### Option 1: Run directly

```bash
node tools/clis/dub.js links create --url https://example.com/landing --key summer-sale
```

### Option 2: Symlink for global access

```bash
# Symlink any CLI you want available globally
ln -sf "$(pwd)/tools/clis/dub.js" ~/.local/bin/dub
ln -sf "$(pwd)/tools/clis/resend.js" ~/.local/bin/resend

# Then use directly
dub links create --url https://example.com/landing --key summer-sale
resend send --from you@example.com --to them@example.com --subject "Hello" --html "<p>Hi</p>"
```

### Option 3: Add the whole directory to PATH

```bash
export PATH="$PATH:/path/to/tools/clis"
```

## Authentication

Every CLI reads credentials from environment variables:

| CLI | Environment Variable |
|-----|---------------------|
| `activecampaign` | `ACTIVECAMPAIGN_API_KEY`, `ACTIVECAMPAIGN_API_URL` |
| `amplitude` | `AMPLITUDE_API_KEY`, `AMPLITUDE_SECRET_KEY` |
| `apollo` | `APOLLO_API_KEY` |
| `calendly` | `CALENDLY_API_KEY` |
| `clearbit` | `CLEARBIT_API_KEY` |
| `crossbeam` | `CROSSBEAM_API_KEY` |
| `customer-io` | `CUSTOMERIO_APP_KEY` (App API), `CUSTOMERIO_SITE_ID` + `CUSTOMERIO_API_KEY` (Track API) |
| `dub` | `DUB_API_KEY` |
| `ga4` | `GA4_ACCESS_TOKEN` |
| `google-ads` | `GOOGLE_ADS_TOKEN`, `GOOGLE_ADS_DEVELOPER_TOKEN`, `GOOGLE_ADS_CUSTOMER_ID` |
| `kit` | `KIT_API_KEY`, `KIT_API_SECRET` |
| `linkedin-ads` | `LINKEDIN_ACCESS_TOKEN` |
| `mailchimp` | `MAILCHIMP_API_KEY` |
| `mention-me` | `MENTIONME_API_KEY` |
| `meta-ads` | `META_ACCESS_TOKEN`, `META_AD_ACCOUNT_ID` |
| `mixpanel` | `MIXPANEL_TOKEN` (ingestion), `MIXPANEL_API_KEY` + `MIXPANEL_SECRET` (query) |
| `partnerstack` | `PARTNERSTACK_PUBLIC_KEY`, `PARTNERSTACK_SECRET_KEY` |
| `resend` | `RESEND_API_KEY` |
| `rewardful` | `REWARDFUL_API_KEY` |
| `savvycal` | `SAVVYCAL_API_KEY` |
| `segment` | `SEGMENT_WRITE_KEY` (tracking), `SEGMENT_ACCESS_TOKEN` (profile) |
| `sendgrid` | `SENDGRID_API_KEY` |
| `tiktok-ads` | `TIKTOK_ACCESS_TOKEN`, `TIKTOK_ADVERTISER_ID` |
| `tolt` | `TOLT_API_KEY` |
| `zapier` | `ZAPIER_API_KEY` |

## Security

**Never hardcode API keys or tokens in scripts.** All CLIs read credentials exclusively from environment variables.

- Store keys in your shell profile (`~/.zshrc`, `~/.bashrc`) or a `.env` file
- The `.env` file is gitignored — but double-check before committing
- Use `--dry-run` on any command to preview the request without sending it (credentials are masked as `***`)
- If you fork this repo, audit your commits to ensure no secrets are included

## Command Pattern

All CLIs follow the same structure:

```
{tool} <resource> <action> [options]
```

Examples:

```bash
dub links create --url https://example.com/landing --key summer-sale
mailchimp campaigns list --limit 20
resend send --from you@example.com --to them@example.com --subject "Hello" --html "<p>Hi</p>"
rewardful affiliates list --limit 50
```

## Output

All CLIs output JSON to stdout for easy piping:

```bash
# Pipe to jq
dub links list | jq '.[].shortLink'

# Save to file
mixpanel events list > events.json

# Use in scripts
DOMAINS=$(rewardful affiliates list | jq -r '.data[].email')
```

## Available CLIs

| CLI | Category | Tool |
|-----|----------|------|
| `activecampaign.js` | Email/CRM | [ActiveCampaign](https://activecampaign.com) |
| `amplitude.js` | Analytics | [Amplitude](https://amplitude.com) |
| `apollo.js` | Data Enrichment | [Apollo.io](https://apollo.io) |
| `calendly.js` | Scheduling | [Calendly](https://calendly.com) |
| `clearbit.js` | Data Enrichment | [Clearbit](https://clearbit.com) |
| `crossbeam.js` | Partner Ecosystem | [Crossbeam](https://crossbeam.com) |
| `customer-io.js` | Email | [Customer.io](https://customer.io) |
| `dub.js` | Links | [Dub.co](https://dub.co) |
| `ga4.js` | Analytics | [Google Analytics 4](https://analytics.google.com) |
| `google-ads.js` | Ads | [Google Ads](https://ads.google.com) |
| `kit.js` | Email | [Kit](https://kit.com) |
| `linkedin-ads.js` | Ads | [LinkedIn Ads](https://business.linkedin.com/marketing-solutions/ads) |
| `mailchimp.js` | Email | [Mailchimp](https://mailchimp.com) |
| `mention-me.js` | Referral | [Mention Me](https://www.mention-me.com) |
| `meta-ads.js` | Ads | [Meta Ads](https://www.facebook.com/business/ads) |
| `mixpanel.js` | Analytics | [Mixpanel](https://mixpanel.com) |
| `partnerstack.js` | Affiliate | [PartnerStack](https://partnerstack.com) |
| `resend.js` | Email | [Resend](https://resend.com) |
| `rewardful.js` | Referral | [Rewardful](https://www.getrewardful.com) |
| `savvycal.js` | Scheduling | [SavvyCal](https://savvycal.com) |
| `segment.js` | Analytics | [Segment](https://segment.com) |
| `sendgrid.js` | Email | [SendGrid](https://sendgrid.com) |
| `tiktok-ads.js` | Ads | [TikTok Ads](https://ads.tiktok.com) |
| `tolt.js` | Referral | [Tolt](https://tolt.io) |
| `zapier.js` | Automation | [Zapier](https://zapier.com) |
</content>
</invoke>
