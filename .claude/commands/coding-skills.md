Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### Code Quality & Review

- **`code-reviewer <repo or file path>`** — Invoke the `code-reviewer` skill. Analyze PRs for complexity and risk, check code quality for SOLID violations and code smells, and generate review reports across 13 languages.
- **`pr-review-expert <PR or diff>`** — Invoke the `pr-review-expert` skill. Expert-level pull request review for security issues, code quality, and correctness.
- **`karpathy-guidelines`** — Invoke the `karpathy-guidelines` skill. Apply behavioral guidelines to reduce common LLM coding mistakes when writing, reviewing, or refactoring code.

### Architecture & Design

- **`senior-architect <system or decision>`** — Invoke the `senior-architect` skill. Design system architecture, evaluate trade-offs (microservices vs monolith, database selection), create architecture diagrams, and produce ADRs.
- **`brainstorming <idea or feature>`** — Invoke the `brainstorming` skill. Explore user intent, requirements, and design through dialogue before any implementation work begins.

### Development Practices

- **`test-driven-development <feature or bugfix>`** — Invoke the `test-driven-development` skill. Write tests first, watch them fail, then write minimal code to pass.
- **`using-superpowers`** — Invoke the `using-superpowers` skill. Establish how to find and use available skills at the start of any conversation.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Code Quality & Review:
  /coding-skills code-reviewer <repo or file>       Analyze PRs, detect code smells & SOLID violations
  /coding-skills pr-review-expert <PR or diff>      Expert PR review for security & quality
  /coding-skills karpathy-guidelines                Apply guidelines to reduce LLM coding mistakes

Architecture & Design:
  /coding-skills senior-architect <system>          Design architecture, evaluate trade-offs, create diagrams
  /coding-skills brainstorming <idea or feature>    Explore requirements and design before building

Development Practices:
  /coding-skills test-driven-development <feature>  Write tests first, then minimal passing code
  /coding-skills using-superpowers                  Establish skill discovery at session start
```
