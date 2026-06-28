Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### Search & Applications

- **`job-search <keyword>`** — Invoke the `job-search` skill. Automated job search matching your resume and preferences across job boards.
- **`apply <job URL or 'last' or 'current'>`** — Invoke the `apply` skill. Fill out a job application on Greenhouse, Lever, or Workday using browser automation.
- **`application-form-filler <job description>`** — Invoke the `application-form-filler` skill. Fill application form fields with context-aware answers drawn from your CV and the job description.
- **`network-scan <number of contacts or 'all'>`** — Invoke the `network-scan` skill. Scan your LinkedIn contacts' companies for matching job openings.
- **`job-description-analyzer <job posting>`** — Invoke the `job-description-analyzer` skill. Analyze job postings, calculate match scores, identify gaps, and create an application strategy.

### Resume Building

- **`tailor-resume <job URL>`** — Invoke the `tailor-resume` skill. Tailor your resume for a specific job posting with full workflow including profile interview.
- **`resume-tailor <job posting>`** — Invoke the `resume-tailor` skill. Customize your resume for a specific job while maintaining truthfulness.
- **`resume-ats-optimizer <resume>`** — Invoke the `resume-ats-optimizer` skill. Optimize your resume for Applicant Tracking Systems and analyze keyword match.
- **`resume-bullet-writer <bullets or experience>`** — Invoke the `resume-bullet-writer` skill. Transform weak resume bullets into achievement-focused statements with metrics and impact.
- **`resume-formatter <resume>`** — Invoke the `resume-formatter` skill. Ensure ATS-friendly formatting and create a clean, scannable layout.
- **`resume-quantifier <resume>`** — Invoke the `resume-quantifier` skill. Find opportunities to add metrics and estimate numbers when exact data is unavailable.
- **`resume-section-builder <role or level>`** — Invoke the `resume-section-builder` skill. Create targeted resume sections optimized for different experience levels and roles.
- **`resume-version-manager <context>`** — Invoke the `resume-version-manager` skill. Track different resume versions, maintain a master resume, and manage tailored versions.
- **`tech-resume-optimizer <resume>`** — Invoke the `tech-resume-optimizer` skill. Optimize resumes for software engineering, PM, and technical roles.
- **`academic-cv-builder <CV or context>`** — Invoke the `academic-cv-builder` skill. Format CVs for academic positions with publications, grants, and teaching sections.
- **`executive-resume-writer <context>`** — Invoke the `executive-resume-writer` skill. Create C-suite and VP level resumes emphasizing strategic leadership.
- **`creative-portfolio-resume <context>`** — Invoke the `creative-portfolio-resume` skill. Balance visual design with ATS compatibility for creative roles.

### Cover Letters & Outreach

- **`cover-letter <job URL or 'last'>`** — Invoke the `cover-letter` skill. Write a tailored cover letter for a specific job posting.
- **`cover-letter-generator <resume and job description>`** — Invoke the `cover-letter-generator` skill. Create a personalized, compelling cover letter from your resume and the job description.
- **`cold-email-writer <target or context>`** — Invoke the `cold-email-writer` skill. Write personalized cold outreach emails to hiring managers and founders — specific and human, not a pitch deck.

### Research & Prep

- **`interview-prep-generator <resume or role>`** — Invoke the `interview-prep-generator` skill. Generate STAR stories, practice questions, and talking points from your resume.
- **`offer-comparison-analyzer <offers>`** — Invoke the `offer-comparison-analyzer` skill. Compare multiple job offers side-by-side with total compensation analysis.
- **`salary-negotiation-prep <role or offer>`** — Invoke the `salary-negotiation-prep` skill. Research market rates, build a negotiation strategy, and create counter-offer scripts.

### Profile & Portfolio

- **`linkedin-profile-optimizer <profile or context>`** — Invoke the `linkedin-profile-optimizer` skill. Optimize your LinkedIn profile for searchability, recruiter visibility, and engagement.
- **`portfolio-case-study-writer <resume bullets or project>`** — Invoke the `portfolio-case-study` skill. Transform resume bullets into detailed portfolio case studies.
- **`career-changer-translator <from industry to industry>`** — Invoke the `career-changer-translator` skill. Translate skills from one industry to another and identify transferable skills.
- **`reference-list-builder <context>`** — Invoke the `reference-list-builder` skill. Format professional references properly and prepare reference materials.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Search & Applications:
  /job-search job-search <keyword>                   Search jobs matching your resume & preferences
  /job-search apply <job URL>                        Fill out a Greenhouse, Lever, or Workday application
  /job-search application-form-filler <job desc>     Fill form fields from your CV & the job description
  /job-search network-scan <contacts or 'all'>       Scan LinkedIn contacts' companies for openings
  /job-search job-description-analyzer <posting>     Analyze job posting, score match, identify gaps

Resume Building:
  /job-search tailor-resume <job URL>                Full resume tailoring workflow with profile interview
  /job-search resume-tailor <job posting>            Customize resume for a specific role
  /job-search resume-ats-optimizer <resume>          Optimize for ATS and keyword match
  /job-search resume-bullet-writer <bullets>         Turn weak bullets into achievement statements
  /job-search resume-formatter <resume>              ATS-friendly formatting & clean layout
  /job-search resume-quantifier <resume>             Add metrics and quantified impact
  /job-search resume-section-builder <role>          Build targeted sections by level and role
  /job-search resume-version-manager <context>       Track and manage multiple resume versions
  /job-search tech-resume-optimizer <resume>         Optimize for engineering and technical roles
  /job-search academic-cv-builder <CV>               Format CVs for academic positions
  /job-search executive-resume-writer <context>      C-suite and VP level resume writing
  /job-search creative-portfolio-resume <context>    Visual resume for creative roles

Cover Letters & Outreach:
  /job-search cover-letter <job URL>                 Write a tailored cover letter
  /job-search cover-letter-generator <resume + JD>   Generate cover letter from resume & job description
  /job-search cold-email-writer <target>             Personalized cold outreach to hiring managers

Research & Prep:
  /job-search interview-prep-generator <resume>      STAR stories, practice questions & talking points
  /job-search offer-comparison-analyzer <offers>     Compare offers with total compensation analysis
  /job-search salary-negotiation-prep <role>         Market rates, negotiation strategy & scripts

Profile & Portfolio:
  /job-search linkedin-profile-optimizer <profile>   Optimize LinkedIn for recruiters & searchability
  /job-search portfolio-case-study-writer <project>  Transform resume bullets into case studies
  /job-search career-changer-translator <industries> Identify transferable skills across industries
  /job-search reference-list-builder <context>       Format and prepare professional references
```
