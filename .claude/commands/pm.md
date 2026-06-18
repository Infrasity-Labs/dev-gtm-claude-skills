Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### Strategy & planning

- **`strategy <product or context>`** — Invoke the `product-strategist` skill. Pass the product or context to drive vision, OKR cascades, quarterly planning, roadmaps, and team scaling.
- **`prd <feature or notes>`** — Invoke the `prd-development` skill. Pass the feature or discovery notes to build a structured, engineering-ready PRD.
- **`prioritize <context>`** — Invoke the `prioritization-advisor` skill. Pass the context to choose the right prioritization framework (RICE, ICE, value/effort, etc.).

### Execution & agile

- **`backlog <story or sprint context>`** — Invoke the `agile-product-owner` skill. Pass the context to write user stories, define acceptance criteria, plan sprints, and track velocity.
- **`story-map <product or journey>`** — Invoke the `user-story-mapping` skill. Pass the product or user journey to build a user story map (activities, steps, tasks, release slices).

### Growth & toolkit

- **`growth <growth constraint>`** — Invoke the `organic-growth-advisor` skill. Pass the growth constraint to diagnose which organic growth path to pursue (segments, geographies, channels, or products).
- **`toolkit <PM task>`** — Invoke the `product-manager-toolkit` skill. Pass the PM task for RICE prioritization, customer interview analysis, PRD templates, discovery frameworks, and go-to-market strategy.

### Meta

- **`create-skill <idea or content>`** — Invoke the `pm-skill-creator` skill. Pass the raw idea or content to design a new PM skill through guided conversation.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Strategy & planning:
  /pm strategy <product or context>       Drive vision, OKRs, roadmaps & team scaling
  /pm prd <feature or notes>              Build a structured, engineering-ready PRD
  /pm prioritize <context>                Pick the right prioritization framework

Execution & agile:
  /pm backlog <story or sprint context>   User stories, acceptance criteria, sprints
  /pm story-map <product or journey>      Build a user story map of the journey

Growth & toolkit:
  /pm growth <growth constraint>          Diagnose the organic growth path to pursue
  /pm toolkit <PM task>                    RICE, interviews, discovery, PRD templates, GTM

Meta:
  /pm create-skill <idea or content>      Design a new PM skill through guided conversation
```
