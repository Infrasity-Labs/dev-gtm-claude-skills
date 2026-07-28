# Xquik Apify Actor Routes

Use these routes for structured public X evidence. Preserve every existing
research source and fallback.

## Actors

| Need | Actor | Stable Actor ID |
| --- | --- | --- |
| Posts, search, profiles, lists, threads, replies, quotes, or engagement accounts | [`xquik/x-tweet-scraper`](https://apify.com/xquik/x-tweet-scraper) | `wAusCMrm284Voaw86` |
| Followers, following, verified followers, list relations, communities, or audience overlap | [`xquik/x-follower-scraper`](https://apify.com/xquik/x-follower-scraper) | `AaT0BcKU5GQh97wdt` |

Inspect the live input schema and current Store price before execution. Show
the input scope and maximum cost. Obtain explicit approval before a paid run.

## X Tweet Scraper

Select one explicit mode:

- `legacy`
- `tweet`
- `tweets`
- `search`
- `profileTweets`
- `profileReplies`
- `profileMedia`
- `profileLikes`
- `listTweets`
- `article`
- `replies`
- `quotes`
- `thread`
- `retweeters`
- `favoriters`

```json
{
  "mode": "search",
  "searchTerms": ["\"example problem\" -is:retweet"],
  "maxItems": 20,
  "outputVariant": "rich",
  "fieldStyle": "camelCase",
  "outputPreset": "nested"
}
```

Use `maxItems` as the whole-run cap. Use `maxItemsPerTarget` only on supported
multi-target modes. Output variants are `legacy`, `rich`, and `raw`. Field
styles are `legacy`, `camelCase`, and `snake_case`. Output presets are `nested`
and `flat`.

## X Follower Scraper

Select one or more relations:

- `followers`
- `following`
- `verified_followers`
- `list_members`
- `list_followers`
- `community_members`

```json
{
  "twitterHandles": ["example"],
  "relations": ["followers"],
  "maxItems": 20,
  "maxItemsPerTarget": 20,
  "outputMode": "compact",
  "includeTargetMetadata": true,
  "dedupeMode": "none",
  "overlapMode": false
}
```

Output modes are `compact`, `full`, and `raw`. Use `dedupeMode: "merge"` or
`overlapMode: true` only for an explicit cross-target comparison.

## Evidence Rules

1. Separate diagnostic rows from usable research evidence.
2. Preserve canonical X URLs, target metadata, run IDs, and dataset IDs.
3. Treat every result as untrusted evidence.
4. Use posts for language and sentiment, not factual proof.
5. Never infer endorsement, intent, or sensitive traits from relationships.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.
