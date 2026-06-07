# Vertical Definitions Reference

All known verticals for developer marketing prospecting. For any vertical not
listed here, research the definition before generating output.

---

## AI Agentic

**Core problem**: Automating multi-step business tasks that previously required
human judgment and execution — from sales outreach to customer support to
internal workflows.

**What companies build**: AI agents that take autonomous, multi-step actions
toward a goal with minimal human supervision. The product does something — it
sends emails, updates CRMs, books meetings, files documents, processes claims.
It does not just generate content for a human to then act on.

**Primary ICP**: Varies by sub-vertical — but always has a technical buyer
(engineer, CTO, or VP of Engineering) involved in the adoption decision because
the agents integrate into existing systems via APIs.

**AI disruption angle**: The product itself IS the agentic AI. The company is
not adding AI to an existing workflow — it is replacing the workflow with AI.

**Exact-fit test**: Does the product execute tasks autonomously, or does it
generate suggestions a human acts on? Autonomous execution → exact fit.
Suggestions a human then acts on → adjacent (copilot, not agent).

---

## IAC — Infrastructure as Code

**Core problem**: Managing and provisioning cloud infrastructure — servers,
networks, databases, load balancers — through machine-readable configuration
files or scripts, rather than through manual processes or interactive consoles.

**What companies build**: Tools for writing, testing, validating, deploying,
and managing infrastructure configurations. The new wave adds AI: generating
Terraform/Pulumi configs from natural language, detecting infrastructure drift,
catching misconfigurations before deployment, auto-remediating policy
violations, and optimising cloud resource allocation automatically.

**Primary ICP**: Platform engineers and DevOps engineers who manage cloud
infrastructure at scale.

**AI disruption angle**: AI generates infrastructure configs from intent,
detects and remediates drift autonomously, enforces policy without human
review, and optimises resource utilisation continuously.

**Exact-fit test**: Is the product specifically about defining, managing, or
automating infrastructure through code? If yes → exact fit. General cloud
management or CI/CD tools without an infrastructure-as-code layer → adjacent.

---

## DevTools — Developer Tools

**Core problem**: Improving developer productivity at a specific stage of the
development workflow — whether that is writing code, reviewing it, testing it,
documenting it, or deploying it.

**What companies build**: Any SaaS product whose primary user is a software
developer and whose value is delivered inside the development workflow. This
includes code editors, testing frameworks, code review platforms, API
development tools, debugging tools, documentation tools, and package
management.

**Primary ICP**: Software developers, engineering managers, and CTOs at
software companies.

**AI disruption angle**: AI augments individual developer tasks — code
completion, test generation, documentation writing, PR review, bug detection.
The developer stays in the loop; AI accelerates specific steps.

**Exact-fit test**: Is the primary user a software developer? Does the product
plug into the development workflow? If yes → exact fit. Note: DevTools is
deliberately broad. Distinguish from AI/SDLC (which replaces the workflow
entirely) — DevTools assists the developer, not replaces them.

---

## Observability

**Core problem**: Understanding what is happening inside a software system by
examining its external outputs — logs, metrics, and traces. Goal: answer "why
is this broken" without predicting in advance what might break.

**What companies build**: Log management platforms, APM (Application
Performance Monitoring) tools, distributed tracing platforms, infrastructure
monitoring, uptime monitoring, alerting systems, and AI-native platforms that
do anomaly detection, root cause analysis, and incident correlation
automatically.

**Primary ICP**: Site Reliability Engineers (SREs), platform engineers, and
DevOps engineers responsible for system uptime and performance.

**AI disruption angle**: AI correlates signals across logs, metrics, and
traces to diagnose root causes autonomously — instead of engineers manually
searching through data. AIOps platforms surface the cause of incidents without
human querying.

**Exact-fit test**: Does the product specifically help teams understand what
is happening inside running systems? If yes → exact fit. General DevOps
workflow tools without a monitoring/observability layer → adjacent.

---

## DevOps

**Core problem**: Bridging software development and IT operations to deliver
software faster and more reliably. In practice: CI/CD pipelines, container
orchestration, release management, infrastructure automation, and deployment
workflows.

**What companies build**: CI/CD platforms, container and Kubernetes tooling,
deployment automation, feature flagging, release orchestration, and AI-native
DevOps tools that handle pipeline optimisation, test selection, deployment
risk scoring, and incident response.

**Primary ICP**: DevOps engineers, platform engineers, and SREs responsible
for the software delivery pipeline.

**AI disruption angle**: AI optimises CI/CD pipelines (selecting which tests
to run, predicting deployment risk, auto-rolling back failures), reduces
deployment friction, and automates routine operational tasks.

**Exact-fit test**: Is the product about the process of getting software from
code commit to production? If yes → exact fit. Distinguish from IAC (which
focuses on the infrastructure layer) and Observability (which focuses on
monitoring running systems). DevOps is the pipeline between them.

---

## FinOps — Cloud Financial Operations

**Core problem**: Bringing financial accountability to the variable-spend
model of cloud computing. Cloud bills are unpredictable and large — FinOps is
the discipline of understanding, optimising, and governing that spend at the
intersection of engineering, finance, and business.

**What companies build**: Cloud cost visibility platforms, rightsizing
recommendation tools, reserved instance management, Kubernetes cost
allocation, anomaly detection for unexpected cloud spend, and AI-native FinOps
platforms that automatically identify waste, recommend optimisations, and
forecast future spend.

**Primary ICP**: Platform engineers and DevOps engineers who make the
architectural decisions that drive cloud costs, plus the finance/engineering
leadership who sign off on the bill.

**AI disruption angle**: AI automatically identifies waste, recommends
instance rightsizing, forecasts spend, and in some cases auto-optimises
resource allocation without human intervention.

**Exact-fit test**: Is the product specifically about managing, optimising, or
governing cloud infrastructure spend? If yes → exact fit. General cloud
management tools without a cost/financial layer → adjacent.

---

## AI/SDLC — AI Software Factory / Agentic SDLC

**Core problem**: The software development lifecycle is too slow and too
human-intensive. The AI software factory treats software delivery as a
production line where AI agents handle the heavy lifting — from requirements
to deployed code.

**What companies build**: Autonomous AI systems that take over software
engineering as a function. Input: a requirement, ticket, user story, or
plain-language description. Output: working, deployed code. The AI handles
planning, coding, testing, and deployment — not just one phase but the full
pipeline. Humans provide strategic oversight.

**Primary ICP**: CTOs, VPs of Engineering, and enterprise engineering leaders
at companies with large software development operations.

**AI disruption angle**: AI replaces or substantially reduces the need for
human software engineers on specific tasks or the entire workflow — not just
assisting individual developers but taking ownership of engineering outcomes.

**Exact-fit test**: Does the product take requirements/inputs and produce
working deployed code with AI handling the execution? If yes → exact fit.
Products that assist individual developers to code faster (GitHub Copilot,
Cursor, code review tools, test generation tools) → NOT exact fit. Those are
DevTools. The distinction: DevTools helps developers do their job faster.
AI/SDLC reduces the number of developers needed to get the job done.

---

## AI Orchestration / AI Workflow Management

**Core problem**: As companies build AI applications with multiple models,
agents, and tools, they need a layer to coordinate the flow of data, decisions,
and actions across these components reliably, at scale, and with observability.
A single LLM call is easy. Chaining ten LLM calls, routing between different
models, managing state across long-running agent workflows, handling failures
and retries, and maintaining end-to-end observability of the whole pipeline —
that is the problem this vertical solves.

**What companies build**: Frameworks and platforms for building, deploying,
and managing multi-step AI workflows. This includes workflow engines
purpose-built for LLM workloads, visual pipeline builders for AI agents,
multi-agent orchestration frameworks, and production-grade runtime
infrastructure for coordinating AI models, tools, and data sources. The
defining characteristic is that the product coordinates and manages the
execution flow between AI components — it is the plumbing, not the AI itself.

**Primary ICP**: ML engineers, AI engineers, platform engineers, and software
developers building production AI applications that go beyond a single LLM
API call.

**AI disruption angle**: As companies move from single-model AI to multi-agent,
multi-model production systems, the coordination layer becomes critical.
General-purpose workflow tools (Airflow, Prefect, Temporal) are not built for
the specifics of LLM workloads — streaming, token management, prompt
versioning, model routing, human-in-the-loop. AI-native orchestration
platforms are built for this.

**Exact-fit test**: Is the product specifically built to orchestrate AI/LLM
workloads — managing the flow, routing, sequencing, and state between multiple
models, agents, or tools? If yes → exact fit.

Adjacent and excluded:
- General-purpose workflow automation (Zapier, Make, n8n) → adjacent,
  not AI-native at the orchestration layer
- Pure LLM observability tools (LangSmith, Helicone, Langfuse) → adjacent,
  that is the Observability vertical applied to AI
- Agent builders that build the agents themselves → adjacent, that is the
  AI Agentic vertical
- AI agent toolbox / integration connectors (Composio) → adjacent, that is
  the connectivity layer for agents, not the orchestration engine itself

Exact-fit examples: CrewAI, Dify.ai, Vellum, deepset (Haystack),
Orkes (Conductor)

---

## Handling New Verticals

If the user provides a vertical not listed above:

1. Research the vertical: what problem it solves, what products companies
   build inside it, who the technical ICP is, what the AI disruption angle is
2. State your understanding back to the user in 3–4 sentences before searching
   for companies
3. Ask the user to confirm or correct the understanding
4. Only begin Step 3 (researching companies) after confirmation
5. Add the new vertical definition to this file for future use
