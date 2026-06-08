Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### SEO & discoverability

- **`seo-audit <domain or url>`** — Invoke the `seo-audit` skill. Pass the domain or URL to diagnose technical and on-page SEO issues.
- **`ai-seo <url or topic>`** — Invoke the `ai-seo` skill. Pass the URL or topic to optimize for AI search engines and LLM citations.
- **`schema <url or page type>`** — Invoke the `schema` skill. Pass the URL or page type to add/fix structured data markup.
- **`programmatic-seo <keyword pattern>`** — Invoke the `programmatic-seo` skill. Pass the keyword/template pattern to build SEO pages at scale.

### Content & copy

- **`content-strategy <product or niche>`** — Invoke the `content-strategy` skill. Pass the product or niche to plan what content to create.
- **`copywriting <page or url>`** — Invoke the `copywriting` skill. Pass the page or URL to write or improve marketing copy.
- **`social <platform or topic>`** — Invoke the `social` skill. Pass the platform or topic to create/schedule social content.
- **`lead-magnets <topic or audience>`** — Invoke the `lead-magnets` skill. Pass the topic or audience to plan a lead magnet.
- **`free-tools <product or idea>`** — Invoke the `free-tools` skill. Pass the product or idea to plan a free marketing tool.

### Demand gen & growth

- **`ads <product or goal>`** — Invoke the `ads` skill. Pass the product or goal for paid campaign strategy and targeting.
- **`ad-creative <product or offer>`** — Invoke the `ad-creative` skill. Pass the product or offer to generate ad copy variations at scale.
- **`ab-testing <what to test>`** — Invoke the `ab-testing` skill. Pass what you want to test to design an experiment.
- **`cro <page url>`** — Invoke the `cro` skill. Pass the page URL to improve conversion rate.
- **`launch <product or feature>`** — Invoke the `launch` skill. Pass the product or feature to plan a launch.
- **`marketing-ideas <product>`** — Invoke the `marketing-ideas` skill. Pass the product to brainstorm growth ideas.
- **`referrals <product>`** — Invoke the `referrals` skill. Pass the product to design a referral/affiliate program.
- **`community-marketing <product or goal>`** — Invoke the `community-marketing` skill. Pass the product or goal to plan community-led growth.

### Lifecycle & retention

- **`emails <sequence type>`** — Invoke the `emails` skill. Pass the sequence type to build a lifecycle/drip email flow.
- **`cold-email <target or offer>`** — Invoke the `cold-email` skill. Pass the target or offer to write cold outreach sequences.
- **`onboarding <product>`** — Invoke the `onboarding` skill. Pass the product to optimize post-signup activation.
- **`churn-prevention <context>`** — Invoke the `churn-prevention` skill. Pass the context to reduce churn and build retention flows.

### Research & competitive

- **`customer-research <source or topic>`** — Invoke the `customer-research` skill. Pass the source or topic to conduct/analyze customer research.
- **`competitor-profiling <competitor URLs>`** — Invoke the `competitor-profiling` skill. Pass competitor URLs to produce structured profiles.
- **`competitors <your product vs competitor>`** — Invoke the `competitors` skill. Pass the matchup to create comparison/alternative pages.
- **`analytics <what to track>`** — Invoke the `analytics` skill. Pass what to track to set up or audit measurement.

### Monetization & RevOps

- **`pricing <product or context>`** — Invoke the `pricing` skill. Pass the product or context for pricing and packaging strategy.
- **`revops <context>`** — Invoke the `revops` skill. Pass the context for lead lifecycle and marketing-to-sales handoff.
- **`sales-enablement <asset type>`** — Invoke the `sales-enablement` skill. Pass the asset type to create sales collateral.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
SEO & discoverability:
  /marketing seo-audit <domain or url>              Diagnose technical & on-page SEO issues
  /marketing ai-seo <url or topic>                  Optimize for AI search engines & LLM citations
  /marketing schema <url or page type>              Add or fix structured data markup
  /marketing programmatic-seo <keyword pattern>     Build SEO pages at scale from templates

Content & copy:
  /marketing content-strategy <product or niche>    Plan what content to create
  /marketing copywriting <page or url>              Write or improve marketing copy
  /marketing social <platform or topic>             Create & schedule social content
  /marketing lead-magnets <topic or audience>       Plan a lead magnet
  /marketing free-tools <product or idea>           Plan a free marketing tool

Demand gen & growth:
  /marketing ads <product or goal>                  Paid campaign strategy & targeting
  /marketing ad-creative <product or offer>         Generate ad copy variations at scale
  /marketing ab-testing <what to test>             Design an A/B test or experiment
  /marketing cro <page url>                          Improve conversion rate
  /marketing launch <product or feature>            Plan a product/feature launch
  /marketing marketing-ideas <product>             Brainstorm growth ideas
  /marketing referrals <product>                    Design a referral/affiliate program
  /marketing community-marketing <product or goal>  Plan community-led growth

Lifecycle & retention:
  /marketing emails <sequence type>                 Build a lifecycle/drip email flow
  /marketing cold-email <target or offer>           Write cold outreach sequences
  /marketing onboarding <product>                   Optimize post-signup activation
  /marketing churn-prevention <context>             Reduce churn & build retention flows

Research & competitive:
  /marketing customer-research <source or topic>    Conduct or analyze customer research
  /marketing competitor-profiling <competitor URLs> Produce structured competitor profiles
  /marketing competitors <you vs competitor>        Create comparison/alternative pages
  /marketing analytics <what to track>              Set up or audit measurement

Monetization & RevOps:
  /marketing pricing <product or context>           Pricing & packaging strategy
  /marketing revops <context>                       Lead lifecycle & sales handoff
  /marketing sales-enablement <asset type>          Create sales collateral
```
