# Marketing Tools Registry

Quick reference for AI agents to discover tool capabilities and integration methods.

## How to Use This Registry

1. **Find tools by category** - Browse sections below for tools in each domain
2. **Check integration methods** - See what APIs, MCPs, CLIs, or SDKs are available
3. **Read integration guides** - Detailed setup and common operations in `integrations/`

---

## Tool Index

| Tool | Category | API | MCP | CLI | SDK | Guide |
|------|----------|:---:|:---:|:---:|:---:|-------|
| ga4 | Analytics | ✓ | ✓ | [✓](clis/ga4.js) | ✓ | [ga4.md](integrations/ga4.md) |
| mixpanel | Analytics | ✓ | - | [✓](clis/mixpanel.js) | ✓ | [mixpanel.md](integrations/mixpanel.md) |
| amplitude | Analytics | ✓ | - | [✓](clis/amplitude.js) | ✓ | [amplitude.md](integrations/amplitude.md) |
| posthog | Analytics | ✓ | - | ✓ | ✓ | [posthog.md](integrations/posthog.md) |
| segment | Analytics | ✓ | - | [✓](clis/segment.js) | ✓ | [segment.md](integrations/segment.md) |
| clearbit | Data Enrichment | ✓ | - | [✓](clis/clearbit.js) | ✓ | [clearbit.md](integrations/clearbit.md) |
| apollo | Data Enrichment | ✓ | - | [✓](clis/apollo.js) | - | [apollo.md](integrations/apollo.md) |
| hubspot | CRM | ✓ | - | ✓ | ✓ | [hubspot.md](integrations/hubspot.md) |
| salesforce | CRM | ✓ | - | ✓ | ✓ | [salesforce.md](integrations/salesforce.md) |
| stripe | Payments | ✓ | ✓ | ✓ | ✓ | [stripe.md](integrations/stripe.md) |
| rewardful | Referral | ✓ | - | [✓](clis/rewardful.js) | - | [rewardful.md](integrations/rewardful.md) |
| tolt | Referral | ✓ | - | [✓](clis/tolt.js) | - | [tolt.md](integrations/tolt.md) |
| dub-co | Links | ✓ | - | [✓](clis/dub.js) | ✓ | [dub-co.md](integrations/dub-co.md) |
| mention-me | Referral | ✓ | - | [✓](clis/mention-me.js) | - | [mention-me.md](integrations/mention-me.md) |
| partnerstack | Affiliate | ✓ | - | [✓](clis/partnerstack.js) | - | [partnerstack.md](integrations/partnerstack.md) |
| mailchimp | Email | ✓ | ✓ | [✓](clis/mailchimp.js) | ✓ | [mailchimp.md](integrations/mailchimp.md) |
| customer-io | Email | ✓ | - | [✓](clis/customer-io.js) | ✓ | [customer-io.md](integrations/customer-io.md) |
| sendgrid | Email | ✓ | - | [✓](clis/sendgrid.js) | ✓ | [sendgrid.md](integrations/sendgrid.md) |
| resend | Email | ✓ | ✓ | [✓](clis/resend.js) | ✓ | [resend.md](integrations/resend.md) |
| nitrosend | Email | ✓ | ✓ | - | - | [nitrosend.md](integrations/nitrosend.md) |
| kit | Email | ✓ | - | [✓](clis/kit.js) | ✓ | [kit.md](integrations/kit.md) |
| activecampaign | Email/CRM | ✓ | - | [✓](clis/activecampaign.js) | ✓ | [activecampaign.md](integrations/activecampaign.md) |
| google-ads | Ads | ✓ | ✓ | [✓](clis/google-ads.js) | ✓ | [google-ads.md](integrations/google-ads.md) |
| meta-ads | Ads | ✓ | - | [✓](clis/meta-ads.js) | ✓ | [meta-ads.md](integrations/meta-ads.md) |
| linkedin-ads | Ads | ✓ | - | [✓](clis/linkedin-ads.js) | - | [linkedin-ads.md](integrations/linkedin-ads.md) |
| tiktok-ads | Ads | ✓ | - | [✓](clis/tiktok-ads.js) | ✓ | [tiktok-ads.md](integrations/tiktok-ads.md) |
| zapier | Automation | ✓ | ✓ | [✓](clis/zapier.js) | ✓ | [zapier.md](integrations/zapier.md) |
| calendly | Scheduling | ✓ | - | [✓](clis/calendly.js) | - | [calendly.md](integrations/calendly.md) |
| savvycal | Scheduling | ✓ | - | [✓](clis/savvycal.js) | - | [savvycal.md](integrations/savvycal.md) |
| crossbeam | Partner Ecosystem | ✓ | ✓ | [✓](clis/crossbeam.js) | - | [crossbeam.md](integrations/crossbeam.md) |
| introw | Partner Ecosystem | - | ✓ | - | - | [introw.md](integrations/introw.md) |
| sparktoro | Audience Research | - | - | - | - | [sparktoro.md](integrations/sparktoro.md) |
| sanity | Headless CMS | ✓ | - | ✓ | ✓ | [sanity.md](integrations/sanity.md) |
| contentful | Headless CMS | ✓ | - | ✓ | ✓ | [contentful.md](integrations/contentful.md) |
| strapi | Headless CMS | ✓ | - | ✓ | ✓ | [strapi.md](integrations/strapi.md) |

---

## By Category

### Analytics
| Tool | Best For | MCP |
|------|----------|:---:|
| **ga4** | Web analytics, Google ecosystem | ✓ |
| **mixpanel** | Product analytics, event tracking | - |
| **amplitude** | Product analytics, cohort analysis | - |
| **posthog** | Open-source analytics, session replay | - |
| **segment** | Customer data platform, event routing | - |

### Advertising
| Tool | Best For | MCP |
|------|----------|:---:|
| **google-ads** | Search intent, high-intent traffic | ✓ |
| **meta-ads** | Demand gen, visual products, B2C | - |
| **linkedin-ads** | B2B, job title targeting | - |
| **tiktok-ads** | Younger demographics, video | - |

### Email
| Tool | Best For | MCP |
|------|----------|:---:|
| **mailchimp** | SMB email marketing | ✓ |
| **customer-io** | Behavior-based automation | - |
| **sendgrid** | Transactional email at scale | - |
| **resend** | Developer-friendly transactional | ✓ |
| **nitrosend** | AI-native email (sequences via prompts) | ✓ |
| **kit** | Creator/newsletter focused | - |
| **activecampaign** | Email automation + CRM | - |

### CRM
| Tool | Best For | CLI |
|------|----------|:---:|
| **hubspot** | SMB, marketing + sales alignment | ✓ |
| **salesforce** | Enterprise, complex sales processes | ✓ |

### Referral & Affiliate
| Tool | Best For | Stripe |
|------|----------|:------:|
| **rewardful** | Stripe-native affiliate programs | ✓ |
| **tolt** | SaaS affiliate programs | ✓ |
| **mention-me** | Enterprise referral programs | ✓ |
| **dub-co** | Link tracking, attribution | - |
| **partnerstack** | Enterprise partner programs | ✓ |

### Payments
| Tool | Best For | MCP |
|------|----------|:---:|
| **stripe** | SaaS subscriptions, developer-friendly | ✓ |

### Scheduling
| Tool | Best For | Notes |
|------|----------|-------|
| **calendly** | Meeting scheduling, lead gen | Most popular |
| **savvycal** | Personalized scheduling | Developer-friendly |

### Data Enrichment
| Tool | Best For | Notes |
|------|----------|-------|
| **clearbit** | Company/person enrichment | Now HubSpot Breeze |
| **apollo** | B2B prospecting, email finding | Large database |

### Partner Ecosystem
| Tool | Best For | Notes |
|------|----------|-------|
| **crossbeam** | Account overlaps, co-sell | Now part of Reveal |
| **introw** | Partner management, deal registration, QBRs | MCP-enabled PRM |

### Audience Research
| Tool | Best For | Notes |
|------|----------|-------|
| **sparktoro** | Audience affinities, behavioral data | Clickstream + social data |

### Automation
| Tool | Best For | MCP |
|------|----------|:---:|
| **zapier** | No-code integrations + SDK for 8,000+ apps | ✓ |

### Headless CMS
| Tool | Best For | Notes |
|------|----------|-------|
| **sanity** | Developer-flexible, structured content | GROQ queries |
| **contentful** | Enterprise headless CMS, multi-locale | Delivery/Management APIs |
| **strapi** | Open-source headless CMS, self-hosted | REST CRUD |

See [headless CMS guide](../marketing-skills/content-strategy/references/headless-cms.md) for selection criteria.

---

## CLI Tools

Zero-dependency, single-file Node.js CLIs for tools that don't ship their own. See [`clis/README.md`](clis/README.md) for install instructions and usage.

All CLIs follow a consistent pattern:
- **No dependencies** — Node 18+ only, uses native `fetch`
- **JSON output** — pipe to `jq`, save to file, or use in scripts
- **Env var auth** — set `{TOOL}_API_KEY` and go
- **Consistent commands** — `{tool} <resource> <action> [options]`

---

## MCP-Enabled Tools

These tools have Model Context Protocol servers available, enabling direct agent interaction:

- **ga4** - Google Analytics 4 data access
- **stripe** - Payment and subscription management
- **mailchimp** - Email campaign management
- **google-ads** - Ad campaign management
- **resend** - Transactional email sending
- **zapier** - Workflow automation + SDK for 8,000+ app integrations
- **crossbeam** - Partner ecosystem data
- **introw** - Partner relationship management

To use MCP tools, ensure the appropriate MCP server is configured in your environment.

---

## Quick Start by Use Case

### Setting up analytics tracking
1. Read [ga4.md](integrations/ga4.md) for web analytics
2. Read [segment.md](integrations/segment.md) if routing to multiple tools

### Launching a referral program
1. Read [rewardful.md](integrations/rewardful.md) or [tolt.md](integrations/tolt.md) for Stripe-based programs
2. Read [dub-co.md](integrations/dub-co.md) for link tracking

### Setting up email automation
1. Read [customer-io.md](integrations/customer-io.md) for behavior-based automation
2. Read [resend.md](integrations/resend.md) for transactional email

### Running paid ads
1. Read [google-ads.md](integrations/google-ads.md) for search campaigns
2. Read [meta-ads.md](integrations/meta-ads.md) for social campaigns
