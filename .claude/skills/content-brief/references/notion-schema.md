# Notion Database Schema — Content Brief

This is the exact property configuration required in your Notion database for the content-brief skill to push data correctly. Create these properties before connecting the Notion MCP.

## Database Properties

| Property Name | Type | Allowed Values / Notes |
|---|---|---|
| Target Keyword | Title | Free text — this is the page title |
| Volume | Number | Integer — monthly search volume |
| CPC | Number | Decimal — cost per click in USD |
| Keyword Difficulty | Number | Integer 0–100 |
| Search Intent | Select | Must have **exactly four** options (see below) |
| Audience | Select | Pre-configure common personas (e.g., HR Director, Marketing Manager) |
| Recommended H1 | Rich Text | Final proposed article title |
| Content Angle | Rich Text | One paragraph — unique positioning statement |
| Word Count Target | Number | Integer |
| Schema Type | Select | Pre-configure common schema types (see below) |
| Priority | Select | Must have exactly three options: HIGH, MEDIUM, LOW |
| Status | Select | See status values below |
| Writer | Person | Assigned post-routing (populated separately) |
| Target Publish Date | Date | Calculated from priority at time of brief creation |
| Source Keyword Research | URL | Link to XLSX or Google Sheet |
| Brief Created | Created Time | Auto-populated by Notion — do not set manually |

## Required Select Property Options

### Search Intent (must match exactly — case-sensitive)
- Informational
- Commercial
- Transactional
- Navigational

### Priority (must match exactly)
- HIGH
- MEDIUM
- LOW

### Status (workflow states)
- Briefed: Ready for Assignment
- Briefed: Weekly Review Queue
- In Progress
- In Review
- Published

### Schema Type (common options — extend as needed)
- Article
- FAQ
- HowTo
- FAQ + HowTo
- Product
- Review
- BreadcrumbList

## Page Body Mapping

The following brief fields are written to the Notion page body (not properties):

| Field | Section in page |
|---|---|
| H2_OUTLINE | "Content Outline" heading block |
| FAQ | "FAQ" heading block |
| INTERNAL_LINKS | "Internal Links" heading block |
| WRITER_NOTES | "Writer Notes" heading block |

## Multi-Client Setup

Each client workspace requires:
1. A separate Notion integration token (Settings → Connections → Develop integrations)
2. The integration shared with the target database
3. The database ID copied from the database URL

Store per-client config as:
```
Client: [Name]
  Notion Token: ntn_xxxx
  Database ID: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  Direction Prompt Variant: [path or name]
```

## Content Calendar Database (Node 9)

A linked `Content Calendar` database entry is created after each brief. Required properties:
- Page (relation → Content Brief database)
- Target Publish Date (Date)
- Status (Select — mirrors brief Status)
- Keyword (Formula or rollup from relation)

The Calendar Sync node uses the Target Publish Date calculated from priority routing.
