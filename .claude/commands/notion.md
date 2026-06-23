Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### Productivity

- **`capture <brain dump>`** — Invoke the `capture` skill. Pass the raw brain dump (any unstructured stream of thoughts, tasks, or ideas) to organize it into Projects, Tasks, Connections, and next-step offers with zero information loss.
- **`reflect`** — Invoke the `reflect` skill. Pauses the current thread and runs a 5-dimension reassessment (macro perspective, gap analysis, reflective inquiry, bias check, contextual alignment) ending in a directional recommendation: continue, pivot, or pause.
- **`meeting-notes`** — Invoke the `meeting-notes` skill. Structures raw meeting input into a clean summary with key discussion points, decisions made, action items table, next steps, and parking lot.

### Email

- **`inbox`** — Invoke the `inbox` skill. Auto-detects state: if no knowledge base exists, runs a one-time 8-section onboarding interview to build it, then offers to run triage immediately. If the KB already exists, goes straight to triage — classifies emails, drafts replies (NEVER sends), delivers a report, and updates the KB.
- **`inbox update`** — Invoke the `inbox` skill with the `update` argument. Re-runs the setup interview on the existing knowledge base, asking per-file: replace / merge / skip.

### Content

- **`brief <keyword>`** — Invoke the `content-brief` skill. Pass a target keyword to generate a fully structured SEO content brief (H1, H2 outline, FAQ, internal links, word count, schema, priority) and optionally push it to a Notion database.

### Workflows

- **`workflow <description>`** — Invoke the `workflow-builder` skill. Pass a description of the repeatable multi-step task to design and write a deterministic multi-agent workflow `.js` file for Claude Code's Workflow tool.

### Meta

- **`claude-md`** — Invoke the `claude-md-starter` skill. Scans the repo for signal files (package.json, Makefile, .github/workflows/, .env.example, etc.), infers the stack and conventions, asks at most 3 targeted questions for what can't be inferred, then writes a fully populated CLAUDE.md. If one already exists, runs a diff-and-merge flow.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Productivity:
  /notion capture <brain dump>     Organize a brain dump into Projects, Tasks & next-step offers
  /notion reflect                  Reassess direction, gaps & bias — returns continue/pivot/pause
  /notion meeting-notes            Structure meeting input into decisions, actions & next steps

Email:
  /notion inbox                    Auto-detects: runs setup interview or triage based on KB state
  /notion inbox update             Refresh KB preferences — replace / merge / skip per file

Content:
  /notion brief <keyword>          Generate a structured SEO content brief → push to Notion

Workflows:
  /notion workflow <description>   Design & write a multi-agent workflow .js for Claude Code

Meta:
  /notion claude-md                Scan repo & generate a populated CLAUDE.md (diff-merge if exists)
```
