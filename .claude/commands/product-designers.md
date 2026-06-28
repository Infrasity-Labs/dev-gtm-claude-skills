Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### Research & Discovery

- **`user-persona <research data or context>`** — Invoke the `user-persona` skill. Create refined user personas from research data with demographics, goals, frustrations, and behavioral patterns.
- **`empathy-map <user or context>`** — Invoke the `empathy-map` skill. Build a 4-quadrant empathy map (Says, Thinks, Does, Feels) to synthesize user research into actionable insights.
- **`interview-script <topic or product>`** — Invoke the `interview-script` skill. Create a structured user interview script with warm-up, core exploration, and wrap-up sections.
- **`journey-map <user and product>`** — Invoke the `journey-map` skill. Create an end-to-end user journey map with stages, touchpoints, emotions, pain points, and opportunity areas.
- **`affinity-diagram <research data>`** — Invoke the `affinity-diagram` skill. Organize qualitative research data into themes, clusters, and insight statements.
- **`user-flow-diagram <task or feature>`** — Invoke the `user-flow-diagram` skill. Create user flow diagrams showing paths, decisions, and branch logic.
- **`experience-map <service or product>`** — Invoke the `experience-map` skill. Create a holistic map of user touchpoints, channels, and relationships across the full ecosystem.
- **`diary-study-plan <topic or behavior>`** — Invoke the `diary-study-plan` skill. Design a diary study with prompts, duration, participant criteria, and analysis framework.
- **`card-sort-analysis <data>`** — Invoke the `card-sort-analysis` skill. Analyze card sorting results to inform information architecture and navigation structure.
- **`survey-design <hypothesis or goal>`** — Invoke the `survey-design` skill. Design surveys that collect reliable, unbiased quantitative data to validate hypotheses.
- **`summarize-interview <transcript>`** — Invoke the `summarize-interview` skill. Summarize a user interview transcript into structured insights with key themes, quotes, and action items.
- **`research-repository <context>`** — Invoke the `research-repository` skill. Build and maintain a research repository that makes findings findable and reusable across the organization.

### Strategy & Planning

- **`design-brief <problem or context>`** — Invoke the `design-brief` skill. Write a comprehensive design brief defining the problem space, constraints, audience, and success criteria.
- **`design-principles <product or team>`** — Invoke the `design-principles` skill. Define actionable design principles that guide decision-making and resolve trade-offs.
- **`jobs-to-be-done <product or feature>`** — Invoke the `jobs-to-be-done` skill. Map user Jobs-to-Be-Done with functional, emotional, and social dimensions plus outcome expectations.
- **`north-star-vision <product>`** — Invoke the `north-star-vision` skill. Articulate a compelling north-star product vision that aligns teams and inspires strategic design decisions.
- **`opportunity-framework <problem or context>`** — Invoke the `opportunity-framework` skill. Identify, evaluate, and prioritize design opportunities using impact-effort frameworks.
- **`business-design <context>`** — Invoke the `business-design` skill. Think and communicate as a designer in a business context — financials, competitive landscapes, and defending decisions in the language of value.
- **`competitive-analysis <product or competitors>`** — Invoke the `competitive-analysis` skill. Structured competitive analysis comparing UX patterns, features, strengths, and gaps across rival products.
- **`metrics-definition <product or feature>`** — Invoke the `metrics-definition` skill. Define UX metrics and KPIs that connect design decisions to measurable business and user outcomes.
- **`design-impact-reporting <project or context>`** — Invoke the `design-impact-reporting` skill. Communicate design's contribution to business and user outcomes in stakeholder-friendly terms.
- **`content-strategy <product or context>`** — Invoke the `content-strategy` skill. Define what content a product needs, how it should be structured, and who owns it.
- **`stakeholder-alignment <project or context>`** — Invoke the `stakeholder-alignment` skill. Create responsibility matrices, decision frameworks, and communication plans to align stakeholders.

### UX Laws & Frameworks

- **`fitts-law <interface or component>`** — Invoke the `fitts-law` skill. Apply Fitts's Law to size and position interactive targets for fast, accurate interaction.
- **`hicks-law <interface or decision>`** — Invoke the `hicks-law` skill. Apply Hick's Law to reduce decision time by limiting the number of simultaneous choices presented.
- **`millers-law <content or interface>`** — Invoke the `millers-law` skill. Apply Miller's Law — chunk information into groups of ~4 to work within working memory limits.
- **`doherty-threshold <feature or flow>`** — Invoke the `doherty-threshold` skill. Apply the Doherty Threshold — keep system response times under 400ms to maintain user flow.
- **`aesthetic-usability <interface>`** — Invoke the `aesthetic-usability` skill. Apply the Aesthetic-Usability Effect — visually polished interfaces are perceived as more usable.
- **`law-of-proximity <layout or component>`** — Invoke the `law-of-proximity` skill. Apply the Law of Proximity to group related elements through spatial relationships.
- **`law-of-common-region <layout or component>`** — Invoke the `law-of-common-region` skill. Apply the Law of Common Region to group elements using containers, backgrounds, and boundaries.
- **`von-restorff-effect <interface or component>`** — Invoke the `von-restorff-effect` skill. Apply the Von Restorff Effect to make the most important element distinctly different from its surroundings.

### Design System

- **`color-system <product or brand>`** — Invoke the `color-system` skill. Build a comprehensive color system with palette generation, semantic mapping, and accessibility compliance.
- **`typography-scale <product or context>`** — Invoke the `typography-scale` skill. Create a modular typography scale with size, weight, and line-height relationships.
- **`spacing-system <product or context>`** — Invoke the `spacing-system` skill. Create a consistent spacing system based on a base unit with contextual application rules.
- **`layout-grid <product or breakpoints>`** — Invoke the `layout-grid` skill. Define responsive layout grid systems with columns, gutters, margins, and breakpoint behavior.
- **`design-token <system or product>`** — Invoke the `design-token` skill. Define and organize design tokens (color, spacing, typography, elevation) with naming conventions and usage guidance.
- **`design-token-audit <codebase or design file>`** — Invoke the `design-token-audit` skill. Audit design token usage across a product for consistency and coverage.
- **`naming-convention <system or component>`** — Invoke the `naming-convention` skill. Establish a naming convention system for design elements, components, and tokens with clear rules.
- **`icon-system <product or context>`** — Invoke the `icon-system` skill. Create an icon system specification covering grid, sizing, naming, categories, and implementation guidance.
- **`illustration-style <product or brand>`** — Invoke the `illustration-style` skill. Define an illustration style guide with visual language, color usage, and application rules.
- **`motion-system <product or context>`** — Invoke the `motion-system` skill. Define a motion system with duration tokens, easing vocabulary, and reduced-motion handling.
- **`pattern-library <pattern or component>`** — Invoke the `pattern-library` skill. Structure a pattern library entry with problem context, solution pattern, usage examples, and related patterns.
- **`theming-system <product or variants>`** — Invoke the `theming-system` skill. Design a theming architecture supporting brand variants, dark mode, and high-contrast modes.
- **`dark-mode-design <interface or component>`** — Invoke the `dark-mode-design` skill. Design effective dark mode interfaces with proper color adaptation, contrast, and elevation.
- **`readable-measure <typography or layout>`** — Invoke the `readable-measure` skill. Set optimal line lengths for readability across typography scales and responsive layouts.

### Interface Design

- **`interface-design <product or screen>`** — Invoke the `interface-design` skill. Craft-first interface design for dashboards, admin panels, SaaS apps, tools, and settings pages.
- **`interfaces-that-feel <interface or component>`** — Invoke the `interfaces-that-feel` skill. Apply an emotional resonance lens — identify what's missing and prescribe changes at the copy, motion, and interaction layer.
- **`information-architecture <product or content>`** — Invoke the `information-architecture` skill. Design the structure, hierarchy, and navigation model for a product's content and features.
- **`navigation-patterns <product or platform>`** — Invoke the `navigation-patterns` skill. Select and design navigation patterns that match product structure, user tasks, and platform conventions.
- **`visual-hierarchy <screen or layout>`** — Invoke the `visual-hierarchy` skill. Establish clear visual hierarchy through size, weight, color, spacing, and positioning.
- **`responsive-design <product or layout>`** — Invoke the `responsive-design` skill. Design adaptive layouts and interactions that work across all screen sizes and input methods.
- **`form-design <form or flow>`** — Invoke the `form-design` skill. Design forms that minimize friction, prevent errors, and guide users to successful completion.
- **`loading-states <feature or component>`** — Invoke the `loading-states` skill. Design loading, skeleton, and progressive content reveal patterns.
- **`error-handling-ux <flow or product>`** — Invoke the `error-handling-ux` skill. Design error prevention, detection, and recovery experiences.
- **`onboarding-design <product>`** — Invoke the `onboarding-design` skill. Design first-run experiences that get users to value quickly without overwhelming them.
- **`search-ux <product or feature>`** — Invoke the `search-ux` skill. Design search experiences that help users find what they need, recover from failure, and refine results.
- **`feedback-patterns <product or action>`** — Invoke the `feedback-patterns` skill. Design system feedback for user actions including confirmations, status updates, and notifications.
- **`data-visualization <data or context>`** — Invoke the `data-visualization` skill. Design clear, accessible data visualizations with appropriate chart selection and styling.
- **`animation-principles <interface or component>`** — Invoke the `animation-principles` skill. Apply animation principles to UI motion for purposeful, polished interactions.
- **`gesture-patterns <touch or pointer interface>`** — Invoke the `gesture-patterns` skill. Design gesture-based interactions for touch and pointer devices.
- **`micro-interaction-spec <interaction>`** — Invoke the `micro-interaction-spec` skill. Specify micro-interactions with trigger, rules, feedback, and loop/mode definitions.
- **`state-machine <component or flow>`** — Invoke the `state-machine` skill. Model complex UI behavior as finite state machines with states, events, and transitions.
- **`localization-design <product or component>`** — Invoke the `localization-design` skill. Design interfaces that adapt gracefully to multiple languages, writing directions, and cultural contexts.

### Critique

- **`critique-affordance <screen>`** — Invoke the `critique-affordance` skill. Critique a screen's interactive affordances — what looks clickable, state visibility, CTA clarity.
- **`critique-brand-consistency <screen>`** — Invoke the `critique-brand-consistency` skill. Critique brand consistency against mood, voice, and token definitions.
- **`critique-color <screen>`** — Invoke the `critique-color` skill. Critique colour usage — contrast ratios, palette coherence, semantic meaning, and colour accessibility.
- **`critique-composition <screen>`** — Invoke the `critique-composition` skill. Critique composition — balance, whitespace, rhythm, and gestalt principles.
- **`critique-information-density <screen>`** — Invoke the `critique-information-density` skill. Critique information density — cognitive load, content prioritisation, and progressive disclosure.
- **`critique-typography <screen>`** — Invoke the `critique-typography` skill. Critique typography — scale usage, readability, consistency, and token compliance.
- **`critique-visual-hierarchy <screen>`** — Invoke the `critique-visual-hierarchy` skill. Critique visual hierarchy — entry point, eye flow, weight distribution, and emphasis.

### Testing & Evaluation

- **`accessibility-audit <product or component>`** — Invoke the `accessibility-audit` skill. Comprehensive accessibility audit against WCAG guidelines with severity ratings and remediation steps.
- **`accessibility-test-plan <product or feature>`** — Invoke the `accessibility-test-plan` skill. Create accessibility testing plans covering assistive technologies and WCAG criteria.
- **`a-b-test-design <hypothesis or change>`** — Invoke the `a-b-test-design` skill. Design rigorous A/B tests with hypotheses, variants, metrics, and sample size calculations.
- **`heuristic-evaluation <product or screen>`** — Invoke the `heuristic-evaluation` skill. Conduct expert heuristic evaluations using Nielsen's heuristics and domain-specific criteria.
- **`usability-test-plan <product or feature>`** — Invoke the `usability-test-plan` skill. Design a usability test plan with tasks, success metrics, participant criteria, and facilitation guide.
- **`click-test-plan <navigation or page>`** — Invoke the `click-test-plan` skill. Design click/first-click tests to evaluate navigation and information findability.
- **`test-scenario <feature or flow>`** — Invoke the `test-scenario` skill. Generate structured usability test scenarios with realistic tasks, success criteria, and facilitation notes.
- **`design-qa-checklist <feature or release>`** — Invoke the `design-qa-checklist` skill. Create QA checklists for verifying design implementation accuracy.
- **`design-debt-audit <product or system>`** — Invoke the `design-debt-audit` skill. Identify, categorize, and prioritize accumulated design inconsistencies and structural problems.
- **`prototype-strategy <design question>`** — Invoke the `prototype-strategy` skill. Choose the right prototyping fidelity and method for the design question.

### Documentation & Handoff

- **`component-spec <component>`** — Invoke the `component-spec` skill. Write a detailed component specification including props, states, variants, accessibility requirements, and usage guidelines.
- **`handoff-spec <design or feature>`** — Invoke the `handoff-spec` skill. Create developer handoff specifications with measurements, behaviors, assets, and edge cases.
- **`design-rationale <decision or feature>`** — Invoke the `design-rationale` skill. Write clear design rationale connecting decisions to user needs, business goals, and principles.
- **`design-review-process <team or project>`** — Invoke the `design-review-process` skill. Establish design review gates with criteria, checklists, and approval workflows.
- **`design-critique <design or project>`** — Invoke the `design-critique` skill. Facilitate structured design critiques with clear feedback frameworks and actionable outcomes.
- **`documentation-template <component or pattern>`** — Invoke the `documentation-template` skill. Generate structured documentation templates for components, patterns, or guidelines.
- **`wireframe-spec <screen or layout>`** — Invoke the `wireframe-spec` skill. Specify wireframe layouts with content priority, component placement, and annotation.
- **`anydesign <URL, image, or Figma link>`** — Invoke the `anydesign` skill. Analyze any visual source — website, screenshot, Figma file, or image — to extract its design system, tokens, and components.
- **`case-study <project>`** — Invoke the `case-study` skill. Craft portfolio-ready case studies that tell the story of a design project.
- **`presentation-deck <project or context>`** — Invoke the `presentation-deck` skill. Structure compelling design presentations for stakeholders, reviews, and showcases.
- **`service-blueprint <service or product>`** — Invoke the `service-blueprint` skill. Map the end-to-end service delivery system including frontstage, backstage, and supporting infrastructure.
- **`team-workflow <team or context>`** — Invoke the `team-workflow` skill. Design team workflows covering task management, collaboration rituals, and tooling.
- **`version-control-strategy <files or system>`** — Invoke the `version-control-strategy` skill. Define version control strategies for design files, components, and libraries.
- **`design-system-governance <system or team>`** — Invoke the `design-system-governance` skill. Define how a design system evolves — contribution models, versioning, change management, and deprecation.
- **`design-system-adoption <system or team>`** — Invoke the `design-system-adoption` skill. Create adoption strategies and materials to drive design system usage across teams.
- **`design-sprint-plan <challenge or goal>`** — Invoke the `design-sprint-plan` skill. Plan and facilitate design sprints from challenge framing through prototype testing.
- **`design-negotiation <context or conflict>`** — Invoke the `design-negotiation` skill. Advocate for design quality, scope, and time with cross-functional partners using evidence and shared goals.
- **`ux-writing <screen or component>`** — Invoke the `ux-writing` skill. Write effective UI copy including microcopy, error messages, empty states, and CTAs.
- **`ux-researcher-designer <context>`** — Invoke the `ux-researcher-designer` skill. Full UX research and design toolkit — personas, journey mapping, usability testing frameworks, and research synthesis.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Research & Discovery:
  /product-designers user-persona <research>           Create user personas from research data
  /product-designers empathy-map <user>                Build empathy maps (Says/Thinks/Does/Feels)
  /product-designers interview-script <topic>          Create structured user interview scripts
  /product-designers journey-map <user + product>      End-to-end journey maps with pain points
  /product-designers affinity-diagram <data>           Organize research into themes & clusters
  /product-designers user-flow-diagram <task>          Create flow diagrams with decisions & branches
  /product-designers experience-map <service>          Map full ecosystem of touchpoints & channels
  /product-designers diary-study-plan <topic>          Design diary studies for longitudinal research
  /product-designers card-sort-analysis <data>         Analyze card sorts for IA decisions
  /product-designers survey-design <hypothesis>        Design reliable quantitative surveys
  /product-designers summarize-interview <transcript>  Summarize interviews into structured insights
  /product-designers research-repository <context>     Build a findable, reusable research repository

Strategy & Planning:
  /product-designers design-brief <problem>            Write a comprehensive design brief
  /product-designers design-principles <product>       Define actionable design principles
  /product-designers jobs-to-be-done <product>         Map Jobs-to-Be-Done with full dimensions
  /product-designers north-star-vision <product>       Articulate a compelling product vision
  /product-designers opportunity-framework <problem>   Identify & prioritize design opportunities
  /product-designers business-design <context>         Communicate design in the language of value
  /product-designers competitive-analysis <product>    Compare UX patterns across competitors
  /product-designers metrics-definition <feature>      Define UX metrics & KPIs
  /product-designers design-impact-reporting <project> Report design's business contribution
  /product-designers content-strategy <product>        Define content structure and ownership
  /product-designers stakeholder-alignment <project>   Build alignment with RACI & decision frameworks

UX Laws & Frameworks:
  /product-designers fitts-law <interface>             Size & position targets for fast interaction
  /product-designers hicks-law <interface>             Reduce decision time by limiting choices
  /product-designers millers-law <content>             Chunk info to fit working memory limits
  /product-designers doherty-threshold <feature>       Keep response times under 400ms
  /product-designers aesthetic-usability <interface>   Polished interfaces feel more usable
  /product-designers law-of-proximity <layout>         Group elements through spatial relationships
  /product-designers law-of-common-region <layout>     Group elements with containers & backgrounds
  /product-designers von-restorff-effect <interface>   Make key elements distinctly different

Design System:
  /product-designers color-system <product>            Build color palette with semantic mapping
  /product-designers typography-scale <product>        Create modular type scale with relationships
  /product-designers spacing-system <product>          Build consistent spacing with a base unit
  /product-designers layout-grid <product>             Define responsive grid with columns & gutters
  /product-designers design-token <system>             Define & organize design tokens with naming
  /product-designers design-token-audit <codebase>     Audit token usage for consistency
  /product-designers naming-convention <system>        Establish naming rules for components & tokens
  /product-designers icon-system <product>             Spec icon grid, sizing, naming & categories
  /product-designers illustration-style <product>      Define illustration visual language & rules
  /product-designers motion-system <product>           Define duration tokens, easing & reduced motion
  /product-designers pattern-library <pattern>         Structure pattern library entries
  /product-designers theming-system <product>          Design theming for brand variants & dark mode
  /product-designers dark-mode-design <interface>      Adapt color, contrast & elevation for dark mode
  /product-designers readable-measure <typography>     Set optimal line lengths for readability

Interface Design:
  /product-designers interface-design <product>        Craft-first design for SaaS & dashboards
  /product-designers interfaces-that-feel <interface>  Apply emotional resonance to flat UIs
  /product-designers information-architecture <product> Design structure, hierarchy & navigation
  /product-designers navigation-patterns <product>     Select navigation patterns by task & platform
  /product-designers visual-hierarchy <screen>         Establish hierarchy through size, weight & color
  /product-designers responsive-design <product>       Adaptive layouts across all screen sizes
  /product-designers form-design <form>                Design forms that minimize friction & errors
  /product-designers loading-states <component>        Design skeleton & progressive reveal patterns
  /product-designers error-handling-ux <flow>          Design error prevention & recovery experiences
  /product-designers onboarding-design <product>       First-run experiences that reach value fast
  /product-designers search-ux <product>               Design search with findability & failure recovery
  /product-designers feedback-patterns <product>       Confirmations, status updates & notifications
  /product-designers data-visualization <data>         Clear, accessible charts & data displays
  /product-designers animation-principles <interface>  Apply animation principles to UI motion
  /product-designers gesture-patterns <touch interface> Design gesture interactions for touch & pointer
  /product-designers micro-interaction-spec <action>   Spec micro-interactions with trigger & feedback
  /product-designers state-machine <component>         Model UI behavior as finite state machines
  /product-designers localization-design <product>     Design for multiple languages & writing directions

Critique:
  /product-designers critique-affordance <screen>      Critique what looks clickable & CTA clarity
  /product-designers critique-brand-consistency <screen> Critique brand against mood & token definitions
  /product-designers critique-color <screen>           Critique contrast, palette & colour accessibility
  /product-designers critique-composition <screen>     Critique balance, whitespace & gestalt
  /product-designers critique-information-density <screen> Critique cognitive load & prioritisation
  /product-designers critique-typography <screen>      Critique scale, readability & token compliance
  /product-designers critique-visual-hierarchy <screen> Critique entry point, eye flow & emphasis

Testing & Evaluation:
  /product-designers accessibility-audit <product>     WCAG audit with severity ratings & remediation
  /product-designers accessibility-test-plan <feature> Testing plan for assistive technologies
  /product-designers a-b-test-design <hypothesis>      Design A/B tests with metrics & sample sizes
  /product-designers heuristic-evaluation <product>    Expert evaluation using Nielsen's heuristics
  /product-designers usability-test-plan <feature>     Test plan with tasks, metrics & facilitation
  /product-designers click-test-plan <navigation>      First-click tests for findability
  /product-designers test-scenario <feature>           Structured usability test scenarios
  /product-designers design-qa-checklist <release>     QA checklist for implementation accuracy
  /product-designers design-debt-audit <product>       Identify & prioritize design inconsistencies
  /product-designers prototype-strategy <question>     Choose the right fidelity & method

Documentation & Handoff:
  /product-designers component-spec <component>        Props, states, variants & accessibility spec
  /product-designers handoff-spec <design>             Dev handoff with measurements & edge cases
  /product-designers design-rationale <decision>       Rationale connecting decisions to goals
  /product-designers design-review-process <team>      Review gates with criteria & approval workflows
  /product-designers design-critique <design>          Facilitate structured critique sessions
  /product-designers documentation-template <pattern>  Generate documentation templates
  /product-designers wireframe-spec <screen>           Wireframe spec with content priority & annotations
  /product-designers anydesign <URL or image>          Extract design system from any visual source
  /product-designers case-study <project>              Portfolio-ready design case studies
  /product-designers presentation-deck <project>       Compelling design presentations for stakeholders
  /product-designers service-blueprint <service>       Map frontstage, backstage & infrastructure
  /product-designers team-workflow <team>              Design team rituals & tooling workflows
  /product-designers version-control-strategy <files>  Version control for design files & libraries
  /product-designers design-system-governance <system> Contribution models, versioning & deprecation
  /product-designers design-system-adoption <system>   Drive design system adoption across teams
  /product-designers design-sprint-plan <challenge>    Plan design sprints from brief to prototype
  /product-designers design-negotiation <context>      Advocate for design with evidence & shared goals
  /product-designers ux-writing <screen>               Microcopy, error messages, empty states & CTAs
  /product-designers ux-researcher-designer <context>  Full UX research & design toolkit
```
