# Routing Logic — Priority Scoring and Publish Date Calculation

Used by Node 6 (Conditional Router) to determine the brief's path through the workflow.

## Priority Classification Rules

Evaluate in order. Apply the first matching rule.

### HIGH
All three conditions must be true:
- Volume > 200 (monthly searches)
- Keyword Difficulty < 40
- Search Intent is **Commercial** or **Transactional**

Action:
- Notion Status → `Briefed: Ready for Assignment`
- Target Publish Date → brief date + **14 days**
- Trigger Slack notification (Node 8A)

### MEDIUM
Doesn't meet HIGH criteria, but meets at least one of:
- Volume is 50–200 (moderate traffic potential)
- KD is 40–60 (rankable with solid content)
- Intent is Informational with high topic authority relevance
- Strategically important keyword (client-defined override)

Action:
- Notion Status → `Briefed: Weekly Review Queue`
- Target Publish Date → brief date + **28 days**
- No Slack notification

### LOW
All others:
- Volume < 50
- KD > 60
- Informational intent with limited conversion value
- Navigational keywords (typically exclude from editorial pipeline)

Action:
- Notion Status → `Briefed: Weekly Review Queue`
- Target Publish Date → brief date + **42 days**
- No Slack notification

## Priority Override

A `Priority Override` column in batch CSV input takes precedence over calculated priority. Valid values: HIGH, MEDIUM, LOW. Invalid values are ignored and calculated priority applies.

## Publish Date Calculation Reference

| Priority | Days from brief date | Example (brief date: 2026-06-22) |
|---|---|---|
| HIGH | +14 | 2026-07-06 |
| MEDIUM | +28 | 2026-07-20 |
| LOW | +42 | 2026-08-03 |

Weekends and holidays are not accounted for — adjust manually if needed.

## Routing Decision Tree

```
Is VOLUME > 200?
├── Yes → Is KD < 40?
│         ├── Yes → Is intent Commercial or Transactional?
│         │         ├── Yes → HIGH
│         │         └── No  → MEDIUM
│         └── No  → MEDIUM
└── No  → Is VOLUME >= 50?
          ├── Yes → MEDIUM
          └── No  → LOW
```

## Slack Notification Payload (HIGH only)

Posted to configured channel when a HIGH priority brief is created:

```
*New HIGH Priority Brief Created*
Keyword: [TARGET_KEYWORD]
Volume: [VOLUME] | KD: [DIFFICULTY] | Intent: [SEARCH_INTENT]
H1: [RECOMMENDED_H1]
Word Count: [WORD_COUNT] | Schema: [SCHEMA]
Target Publish: [TARGET_PUBLISH_DATE]

→ [Notion page link]
```
