METADATA
last updated: 2026-04-15_165451
file_name: _archive-combined-context-commentary_regulatory_20k.md
category: regulatory
subcategory: NA
words: 13325
tokens: 20511


CONTENT

# _archive-combined-context-commentary_regulatory_20k (10 files, 20,511 tokens)

# 1,184  _context-commentary_regulatory-fda-euas.md
METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-fda-euas.md
category: regulatory
subcategory: fda-euas
gfile_url: https://docs.google.com/document/d/18JeeeAMKd7JS1pZ8bdDG6vxEt8cr9iaNOMZbTMtlsUU
words: 627
tokens: 1184


CONTENT

## Context
An Emergency Use Authorization (EUA) is a mechanism through which the FDA can authorize the use of unapproved medical products (or unapproved uses of approved products) during a declared public health emergency. During the COVID-19 pandemic, EUAs were the primary pathway by which diagnostic tests reached the market. The EUA process differs from the standard FDA authorization pathways (510(k), PMA, De Novo) in several key respects:

- **Speed**: EUAs are designed for rapid review during emergencies, with intended timelines measured in weeks rather than months or years
- **Evidence threshold**: EUAs require the FDA to determine that the product "may be effective" based on available evidence, a lower bar than the "reasonable assurance of safety and effectiveness" required for standard authorizations
- **Temporary status**: EUAs are valid only for the duration of the declared emergency and can be revised or revoked
- **Conditions of authorization**: EUA-holders must meet ongoing conditions, including labeling requirements, adverse event reporting, and sometimes performance monitoring

Each EUA includes an Instructions for Use (IFU) document that specifies the authorized specimen types, testing procedures, performance characteristics, interpretation criteria, and conditions of authorization. Some EUAs also include an EUA Summary providing the FDA's review of the submission data.

This `regulatory/fda-euas` subcategory contains a selection of EUA documents that were relevant to FloodLAMP's work — not a comprehensive collection of COVID-19 diagnostic EUAs (of which there were hundreds). The files here were included because FloodLAMP reviewed them during development, because they represent comparable technologies (particularly LAMP-based or isothermal assays), or because they illustrate specific aspects of the EUA landscape. The collection includes IFUs and EUA summaries from tests spanning RT-PCR, isothermal amplification, CRISPR-based detection, and home collection kits.

Two files merit specific mention:

- **`DetectaChem - EUA IFU - MobileDetect-BIO BCC19 Test Kit (10-6-2020)`** — This was the EUA most similar to what FloodLAMP was developing: a colorimetric LAMP-based SARS-CoV-2 test designed for point-of-care use. FloodLAMP's assays appeared to achieve significantly higher sensitivity and overall performance than the DetectaChem test based on the published performance data.
- **`2020-10-15_SalivaDirect EUA IFU - Yale School of Public Health SalivaDirect assay EUA Summary`** (available in the `regulatory/open-euas` subcategory) — Notable as the first and essentially only "open" EUA, meaning the protocol was made freely available for other labs to adopt.

- **`2020-12-01_CDC EUA IFU - CDC 2019-Novel Coronavirus (2019-nCoV) Real-Time RT-PCR Diagnostic Panel`** - The CDC's own RT-PCR Diagnostic Panel IFU is also included here. It was the original FDA-authorized COVID-19 test in the United States and provides a baseline example of an EUA IFU at the highest complexity level.

The current FDA page for SARS-CoV-2 molecular diagnostic EUAs is [FDA: In Vitro Diagnostics EUAs – Molecular Diagnostic Tests for SARS-CoV-2](https://www.fda.gov/medical-devices/covid-19-emergency-use-authorizations-medical-devices/in-vitro-diagnostics-euas-molecular-diagnostic-tests-sars-cov-2).
For historical reconstruction of how FDA EUA listings changed over time during the pandemic, useful resources may be:
- 2020 onward: [Wayback Machine archive of the FDA’s earlier IVD EUA page used during the pandemic](https://web.archive.org/web/*/https://www.fda.gov/medical-devices/emergency-situations-medical-devices/emergency-use-authorizations#covid19ivd)
- 2021-3-19 onward: [Wayback Machine archive of the FDA’s later IVD EUA page used during the pandemic](https://web.archive.org/web/*/https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/in-vitro-diagnostics-euas).
An independent COVID-19 EUA repository is the [Center for Complex Interventions - Structured SARS-2 diagnostic data repository (centerofci-archive)](https://github.com/centerofci-archive/SARS-CoV-2-testing-kit-validation-data).

For broader dashboards searchable by regulatory status, see [ASU Testing Commons](https://chs.asu.edu/diagnostics-commons/testing-commons) and [PATH COVID-19 Diagnostics Dashboard](https://www.path.org/who-we-are/programs/diagnostics/covid-dashboard-covid-19-diagnostics-dashboard/).

For broader analysis and commentary on the FDA's EUA process during the pandemic, see the `regulatory/reg-articles-misc` subcategory, which includes articles and reports examining how the process functioned. For FloodLAMP's own FDA submissions and correspondence, see the `regulatory/fl-fda-submissions` and `regulatory/fl-fda-correspondence` subcategories.

Also see the following file, which is an AI-generated report sourcing retrospectives on FDA EUAs during the COVID-19 pandemic.
`regulatory/reg-articles-misc/_AI_fda-eua-covid-retrospectives_post2022_report.md`


## Commentary
See other `regulatory` subcategories for commentary. FloodLAMP's assessments and lessons learned regarding the EUA process are addressed there where they can be grounded in specific documents and experiences.


# 3,647  _context-commentary_regulatory-fda-policy.md
METADATA
last updated: 2026-03-20 RT
file_name: _context-commentary_regulatory-fda-policy.md
category: regulatory
subcategory: fda-policy
gfile_url: https://docs.google.com/document/d/1ej8e1HjKyq1As-FsYFA1jcz2lV-dFv9ya9vmQ68Y2a0
words: 2468
tokens: 3647


CONTENT

## Context
This `regulatory/fda-policy` subcategory contains 47 documents spanning 2020–2023 that trace the evolution of FDA's regulatory policy for COVID-19 diagnostic testing. The collection includes seven versions of FDA's overarching COVID test policy guidance, EUA letters and amendment letters, review templates (molecular, antigen, home-use, pooling), fact sheet templates, FDA press announcements, and transition planning documents. Together they form a detailed record of how FDA managed the regulatory environment for COVID-19 tests from the earliest emergency through the end of the Public Health Emergency.
This collection is not complete and consists mostly of documents that we downloaded, many of which we reviewed. There are almost certainly other important documents that are not included here.

### AI Summary of FDA Policy
Below is an AI (ChatGPT 5.2 Pro and Claude Opus 4.6) generated summary, which may contain errors.

The FDA COVID-19 testing policy evolved through three broad phases:

- **Emergency expansion (early 2020):** FDA used enforcement discretion to allow CLIA high-complexity labs to develop, validate, and begin using molecular tests before EUA issuance, provided labs notified FDA and submitted an EUA within a set timeframe. Guidance versions 1–4 (Feb–May 2020) progressively broadened these pathways to include state authorization, commercial manufacturers, and serology.
- **Standardization and new use cases (mid-2020–2021):** FDA tightened quality oversight (notably revoking the serology umbrella EUA pathway), introduced standardized templates, and expanded authorized intended uses from "suspected COVID-19" into explicit asymptomatic screening and pooled testing. Serial testing emerged as a formal authorization strategy, and variant monitoring became a standard EUA condition.
- **Narrowing and wind-down (2022–2023):** FDA reduced the scope of new EUA reviews, encouraged developers toward traditional marketing pathways (510(k)/De Novo), standardized repeat-testing labeling for consumer antigen tests, and published transition plans for returning to normal device regulation. The COVID-19 PHE expired May 11, 2023, but FDA clarified that existing EUAs remain in effect as long as the underlying EUA declaration persists.

Key points of variation across the seven guidance versions:

| Version | Date | Key Change |
| --- | --- | --- |
| v1 | Feb 29, 2020 | Initial accelerated policy for CLIA high-complexity lab molecular LDTs |
| v2 | Mar 16, 2020 | Expanded pathways: state authorization, commercial distribution prior to EUA, serology policy |
| v3 | May 4, 2020 | Additional templates, clearer timelines, tightened oversight |
| v4 | May 11, 2020 | Further template and oversight refinements |
| v5 | Nov 15, 2021 | Major reset: umbrella EUAs for serial testing, reissued/narrowed molecular LDT umbrella EUA, FDA signals that newly offered tests should generally have EUA or traditional authorization before clinical use |
| v6 | Sep 27, 2022 | Narrowed EUA review priorities; encouraged traditional marketing pathways |
| v7 | Jan 12, 2023 | Final revision of the overarching COVID test policy guidance |

### AI Compilation of EUA Staffing and Review Timing
`_AI_FDA COVID-19 Diagnostic Test EUA Staffing and Review Timing.md` compiles publicly available data on FDA staffing levels and review timelines for COVID-19 diagnostic test (molecular and antigen) EUAs, covering CDRH OHT7/OIR workforce growth from 60 to 180 staff, review-time trends from 14-day to 99-day medians, submission volume and outcomes by test type and developer category, reasons for non-authorization, and the key federal sources for each metric.

Three policy innovations are specifically documented in this subcategory:
#### Serial screening (Mar 2021 onward)
FDA authorized screening claims based on strong symptomatic performance combined with a repeat-testing regimen, rather than requiring standalone evidence in asymptomatic populations. This treated the testing algorithm and frequency as part of the risk-control package. By Nov 2022, serial testing instructions were standardized into enforceable antigen test labeling (two tests over three days if symptomatic; three tests over five days if asymptomatic, at least 48 hours apart). Key archive files include:
- `2021-03-16_FDA Website - FDA takes steps to streamline path for COVID-19 screening tools`
- `2021-03-16_FDA Template - Supplemental Template for Developers of Molecular and Antigen Diagnostic COVID-19 Tests for Screening with Serial Testing`
- `2021-03-13_FDA Fact Sheet - Screening for COVID-19 Deciding Which Test to Use When Establishing Testing Programs`
- `2021-10-25_FDA Template - Supplemental Template for Developers of Molecular and Antigen Diagnostic COVID-19 Tests for Screening with Serial Testing` (updated version)
- `2022-11-01_FDA Letter - Repeat Testing Revision Letter`
- `2022-11-01_FDA Website - Antigen EUA Revisions for Serial Repeat Testing`
- `2022-11-17_FDA Website - At Home COVID-19 Antigen Tests-Take Steps`

#### Asymptomatic/screening testing (Jul 2020 onward)
FDA distinguished between testing asymptomatic individuals under clinical "suspicion" (provider judgment) and broad population screening (no symptoms, no known exposure). The Jul 24, 2020 LabCorp reissuance was the first EUA explicitly authorizing screening of people without known or suspected infection, establishing screening as a distinct intended use with its own evidence and labeling requirements. Key archive files include:
- `2020-08-24_FDA Policy IVD - Pooled Sample Testing and Screening Testing for COVID-19`
- `2021-03-13_FDA Fact Sheet - Screening for COVID-19 Deciding Which Test to Use When Establishing Testing Programs`
- `2020-10-26_FDA Template - Antigen Template for Test Developers`
- `2021-10-06_FDA Template - For Developers of Molecular Diagnostic Tests`

#### Pooled testing (Jul 2020 onward)
FDA authorized sample pooling to conserve reagents and increase throughput, but constrained it through validation requirements (replicate detection thresholds, Ct shift limits, invalid-rate caps), restriction to CLIA high-complexity labs, and behavioral controls (reflex individual testing for positive/invalid pools, specific fact-sheet language). The Apr 20, 2021 amendment letter tied pooled screening specifically to serial testing programs operating at least weekly, treating serial frequency as a mitigation for the sensitivity loss inherent in pooling. FDA distinguished swab pooling from media pooling and provided different validation pathways for each. Key archive files include:
- `2020-08-24_FDA Policy IVD - Pooled Sample Testing and Screening Testing for COVID-19`
- `2021-04-20_FDA Letter - Amendment Letter`
- `2021-04-20_FDA Website - Pooling and Serial Testing Amendment`
- `2021-04-20_FDA Fact Sheet - Sample Updated Fact Sheet for Health Care Providers`
- `2021-04-20_FDA Fact Sheet - Sample Updated Fact Sheet for Patients`

An important distinction throughout the archive is between FDA's two regulatory levers: **EUA issuance** (test-specific, enforceable conditions, required fact sheets) and **enforcement discretion** (FDA choosing not to enforce certain requirements for a period, with conditions). The early guidances relied heavily on enforcement discretion to expand access; later guidances progressively moved back toward requiring EUA or traditional authorization before clinical use.

Related subcategories include `regulatory/open-euas` (the open EUA submissions FloodLAMP prepared), `regulatory/fda-townhalls` (a RAG demo over 100 FDA townhall transcripts for COVID-19 test developers), and `regulatory/ldts` (laboratory-developed test policy context).


## Commentary
For the primary commentary on FDA policy and the Open EUAs, see `regulatory/open-euas/_context-commentary_regulatory-open-euas.md`.

There remains a need for significant progress in FDA policy as it relates to pandemic preparedness and response. The complexity of the regulatory environment documented in this subcategory, with seven guidance versions, multiple overlapping enforcement mechanisms, and evolving intended-use distinctions, illustrates both the scale of the challenge and the difficulty of navigating it in real time as a small developer.

### Deprioritization
The most consequential example of this difficulty is FDA's use of "deprioritization" — a discretionary triage mechanism through which CDRH declined to review hundreds of EUA submissions for COVID-19 diagnostic tests (see `regulatory/fl-fda-correspondence/_AI_FDA Deprioritization of COVID-19 Diagnostic EUAs.md` for a detailed AI-generated analysis). By September 2021, GAO reported that FDA had declined to review 558 EUA requests, including 230 from laboratories developing LDTs. These submissions represented enormous effort by startups, established companies, academic groups, and clinical laboratories — organizations and individuals that stepped up during a pandemic to contribute in what is arguably the single most critical area for slowing early-stage spread: testing. A small number of FDA reviewers and agency leadership, exercising broad and largely unpublicized discretion, effectively bottlenecked the efforts of thousands of scientists and businesses working to expand national testing capacity. What followed was the Omicron surge of winter 2021–2022, with severe nationwide testing shortages, hours-long lines, front-page headlines, and real consequences in lost lives, closed schools, economic destruction, and massive societal upheaval. As our own pilot programs documented (see `pilots`), there was tremendous unmet need for accessible testing even among first responders and essential workers. Despite the volume of policy documents, templates, and guidance versions cataloged in this subcategory, the underlying process was highly discretionary, capricious, and unpredictable — and the deprioritization mechanism itself was barely publicized, remaining largely unknown, perhaps even among researchers studying the pandemic response.

### Regulatory Reform
No systemic reform of the FDA diagnostic review process has occurred since the pandemic. There were ample mechanisms available — provisional authorization with post-market data collection against established comparators, for example — that could have preserved access to emerging tests while managing quality concerns, but these were not meaningfully pursued. Specific and actionable reform proposals exist, such as the one documented in `regulatory/reg-articles-misc/2021-01-18_Phillips and Dinakar - A Proposal for Increasing the Speed of Validating SARS-CoV-2 Diagnostic Tests`, but to the best of our knowledge none have been implemented or placed on any announced reform agenda. What the FDA did pursue was the 2024 LDT rule, an attempt to expand its control by imposing device-style premarket review requirements on laboratory-developed tests — effectively eliminating the ability of clinical labs to develop and offer their own diagnostics. That rule was vacated by the courts in March 2025, and FDA chose not to appeal. For a fuller account, see the AI-generated report at `regulatory/ldts/_AI_FDA 2024 LDT Rule - Status and Legal History.md`.

Discussion of FDA reform is understandably usually dominated by pharmaceutical policy, drug pricing, and drug approval. Drugs are a much larger industry and a much larger share of overall healthcare spending compared to diagnostics. But with respect to pandemic preparedness and response, diagnostic and screening testing remains underappreciated and underaddressed as a domain for regulatory reform. Without reform, there is every reason to expect the same bottlenecks, the same discretionary purges, and the same capacity constraints if another pandemic arrives. This is a significant and tractable area for progress.

### AI Tools for Regulatory Navigation
AI tools offer substantial potential for making this kind of dense regulatory material more accessible and navigable. As a related effort within this archive project, we built a demo QRAG (Question Retrieval Augmented Generation) tool over a corpus of 100 FDA virtual town hall transcripts for COVID-19 diagnostic test developers (see `regulatory/fda-townhalls`). That tool takes natural language queries and returns the closest matching quoted FDA authority responses along with an AI-generated summary, demonstrating one approach to making regulatory guidance more searchable and usable. Feel free to try it at [FDA COVID-19 Diagnostics Townhalls - QRAG Demo](https://www.focusonfoundations.org/fda-town-halls-qrag-demo).

### FDA SARS-CoV-2 Reference Panel
In 2020, the FDA created a SARS-CoV-2 Reference Panel — a standardized set of samples containing heat-inactivated virus — to independently benchmark the analytical sensitivity (limit of detection) of EUA-authorized molecular diagnostic tests. When the results were published, they revealed large and systematic discrepancies between the LoDs measured with the panel and the self-reported LoDs on which EUA authorizations had been based. The peer-reviewed study by Blommel et al. (reference below) found a statistically significant difference, with a mean FDA panel LoD of 43,750 copies/mL versus a mean EUA-reported LoD of 9,417 copies/mL. A compiled dataset showed that approximately 86% of tests performed worse on the FDA panel, with a median discrepancy of roughly 9x and nearly half of tests showing discrepancies of 10x or greater. A formal complaint was filed under the Information Quality Act in December 2020; the FDA responded nearly three years later, defending the panel and noting the data had been removed as outdated. Key archive files include:
- `_AI_FDA SARS-CoV-2 Reference Panel Report` (AI-generated comprehensive report analyzing the episode)
- `FDA SARS-CoV-2 Reference Panel Comparative Data - Complied by Matt McFarlane` (compiled LoD comparison data)
- `2022-12-15_Paper - Blommel - Authorized SARS-CoV-2 molecular methods show wide variability in the limit of detection` (peer-reviewed study directly analyzing the discrepancy)
- `2020-12-22_Complaint Letter to FDA regarding Reference Panel - IQA-Request-Hyman-Phelps-McNamara` (Information Quality Act complaint)
- `2023-09-23_FDA Response Letter - To Complaint regarding FDA Reference Panel from Dec 2020` (FDA response, issued nearly three years later)

The reference panel episode exposes a fundamental problem in how the FDA evaluates diagnostic test performance for EUA authorization. The entire EUA system relies on self-reported performance data from developers, validated using whatever materials they choose — clinical remnant samples, contrived specimens from commercial providers like Zeptometrix, gamma-inactivated virus from BEI Resources, synthetic RNA from Twist Bioscience, or other sources — each prepared under different protocols, in different matrices, and reported in inconsistent units. When the FDA's own standardized benchmark revealed that most tests performed substantially worse than their authorization data indicated, the agency neither resolved the discrepancy nor reformed the process that produced it. It archived the results, took nearly three years to respond to a formal complaint, and continued operating under the same, now even more clearly flawed framework of self-reported data and rigid performance cutoffs.

What the FDA should have done, and still to the best of our knowledge has not done, is use the knowledge it gained from the reference panel to build accessible infrastructure for generating credible, comparable performance data. That means establishing clear, standardized procedures for creating contrived positive specimens for validation work, making reference materials broadly available rather than restricting them to existing EUA holders, and creating a streamlined, permissionless pathway for developers to generate real-world comparative data against established comparator tests at partner clinical laboratories. Instead, the pathway to generating clinical performance data remained gated behind expensive IRB approvals, six-figure clinical study costs, and weeks-long BEI Resources registration delays just to obtain cross-reactivity reagents (see `regulatory/irb` and `regulatory/fl-fda-submissions`). There should have been a mechanism by which a developer whose test demonstrated performance in the right ballpark, even based on contrived specimens, could proceed directly to supervised comparative testing against an established comparator, generate real clinical data, and submit those results as part of a provisional or follow-up authorization, without the full standalone clinical study apparatus. See the `regulatory/irb` subcategory, specifically the archive files `_context-commentary_regulatory-irb` and `_AI_digestion_irb_new-clinical-study-design`.

FloodLAMP's experience illustrates the consequence of this gap. The FloodLAMP colorimetric LAMP test was not as sensitive as purified or even direct PCR, but it was consistently positive earlier than FDA-authorized rapid antigen tests in real-world surveillance comparisons, particularly in detecting early and asymptomatic infections — precisely the use case where accessible testing has the greatest public health value (see `pilots/pilot-data/_context-commentary_pilots-pilot-data.md` for case studies and comparisons). Yet it was unable to obtain authorization or even meaningful review (see `regulatory/fl-fda-submissions` and `regulatory/fl-fda-correspondence` for the full record). Meanwhile, tests with reference-panel results showing order-of-magnitude sensitivity shortfalls from their EUA claims remained authorized and on the market. The reference panel discrepancy and the FDA's failure to act on it point to a need for fundamental and substantial reform in how the agency measures, validates, and adjudicates diagnostic test performance.


# 2,228  _context-commentary_regulatory-fda-townhalls.md
METADATA
last updated: 2026-03-22 RT
file_name: _context-commentary_regulatory-fda-townhalls.md
category: regulatory
subcategory: fda-townhalls
gfile_url: https://docs.google.com/document/d/1D3TwdRTkR5UR6oydl7IDwRFOelOVrbSwDaSzmZcMJNs
words: 1709
tokens: 2228


CONTENT

## Context
This subcategory `regulatory/fda-townhalls` contains processed transcripts from approximately 100 FDA Virtual Town Hall meetings for COVID-19 diagnostic test developers, spanning from March 2020 through early 2023. The FDA held these meetings approximately every two weeks, with each session typically lasting about an hour. The town halls served as a direct engagement channel between the FDA and the diagnostic test development community during the pandemic, covering topics including Emergency Use Authorization (EUA) submissions, test validation requirements, regulatory updates, and policy changes.

The archive contains two processed file types for each town hall session: `section-titles` files (organized by agenda and topic sections) and `qa-qonly` files (extracted question-and-answer pairs only). The source transcripts were downloaded from the FDA website in PDF format. Processing involved standardizing the significant variability in these FDA transcripts, particularly speaker names and formatting across sessions. The question-and-answer extraction represented a substantial separate effort, producing the structured QA pairs that form the "QRAG" AI application described below.

### QRAG Application
QRAG (Question Retrieval Augmented Generation) is a specialized AI retrieval tool that FloodLAMP developed and applied to this corpus of FDA Town Hall transcripts. A live demo is available at:
https://www.focusonfoundations.org/fda-town-halls-qrag-demo

QRAG was developed in late 2023, which is a long time ago in the context of AI development. Current state-of-the-art reasoning and agentic AI systems may achieve comparable or superior results; however, the QRAG approach may still be faster and more cost-effective for this type of RAG/structured retrieval task.

### QRAG Explainer
The QRAG system is designed for "serious contexts of use" where authoritative, source-attributed answers are needed. It provides responses by leveraging a pre-processed, curated knowledge base of question-answer (QA) pairs. Key characteristics include:

- **Structured QA Processing**: Utilizes pre-processed QA blocks with metadata for efficient retrieval.
- **Pre-Processed QA Content**: Uses structured QA pairs that can be authority-vetted, enabling high-quality retrieval and responses.
- **Question-Based Vector Search**: Employs embeddings of questions for accurate matching to user queries.
- **Intelligent Response Routing**: Routes queries based on question match quality to appropriate LLM prompts.
- **Transparent Source Attribution**: Distinguishes between quoted and AI-generated content.

## Commentary
The FDA's decision to hold regular town halls for diagnostic test developers during the pandemic represented a valuable form of direct engagement with the regulated community. However, the volume and nature of questions from serious test developers across these sessions reveals a persistent information and clarity gap in FDA communication around diagnostic test authorization. Addressing that gap with AI to improve the efficiency, accuracy, consistency, and objectivity has enormous potential to enable progress in the diagnostics space.

### Why QRAG — the case for authority-quoted retrieval
The core motivation for the QRAG tool was to avoid full reliance on AI-generated answers for a subject as consequential as FDA diagnostic regulatory policy. Hallucination rates in large language models have decreased substantially since this work began in 2023, but for regulatory questions where precision matters, users benefit from seeing the authority directly quoted (i.e. what the FDA actually said) either before or alongside any AI-generated synthesis. This makes the output more reliable and more verifiable. A practical approach for using QRAG is to increase the number of returned chunks (direct quotations) to 20 or even 50, save the results as a markdown file, and then load that file into the user's own AI tool for deeper analysis, particularly if the user has access to extended-reasoning models through a pro-level subscription or other advanced AI tool.

### FDA refusal to answer questions: an example use case
One analysis that may be illuminating and serve as an example use case of our QRAG tool over the FDA Diagnostics Town Halls is a systematic examination of the FDA's refusal to answer questions. The FDA routinely declined to respond to questions about specific submissions, using standard language to that effect. While there is an appropriate basis for not answering in some cases, many of the questions were asked in good faith by test developers seeking to understand the status or outcome of their own submissions, and could have been better served with substantive responses rather than generic refusal. There are concerns that this standard refusal was also used to avoid addressing questions that touched on areas of potential inconsistency, lack of clarity, or unresolved policy problems. Developers regularly raised straightforward questions, such as why they had not received a review response after months of waiting. There has been important work on both reducing review timelines and increasing transparency around these processes, and the new FDA leadership appears to be moving in that direction.

### Analysis of FDA refusals to answer: an AI-enabled demonstration
As a demonstration of AI-enabled use of this FDA Townhall set of files, a comprehensive analysis was conducted and is documented in a separate companion file in this subcategory: `_AI_FDA_Townhall_Analysis_of_Refusals`.

That document contains:
- A critical analysis of the FDA's standard "we are not able to respond to questions about specific submissions" language, including its effect on transparency, accountability, and the structural silencing of the regulated community.
- An appropriateness rubric with classification categories and a 1–5 scoring system for evaluating whether individual refusal instances were justified.
- Classification and scoring of all 116 identified refusal instances across 84 of the 100 town hall transcript files (51 boilerplate opening disclaimers and 65 active in-session refusals).
- Summary statistics and interpretation of results.

The raw extraction of refusal passages is compiled in a separate file: `_compilation_fda-refusals-to-answer`.

The critical essay in Section 1 of the analysis document was authored by FloodLAMP founder Randy True and later revised with AI assistance. The initial extraction and classification of refusal instances was produced as a rapid, AI-assisted demonstration using regex pattern matching and heuristic classification generated and executed by the agentic model during that same session.

A more rigorous, non-agentic version was then implemented as a standalone Python module (`refusal_analysis.py`, included in this subcategory). This code runs a two-step structured-output pipeline against the `section-titles` transcript files: first, an LLM-based extraction pass identifies refusal instances by line range using a detailed prompt and function-call schema, supplemented by heuristic keyword matching; second, a classification pass scores each instance against an appropriateness rubric with fields for category code, appropriateness score, rationale, key excerpt, speaker identification, and contextual flags. The extraction and classification prompts, structured-output tool schemas, and the full rubric are defined in the module. The code also generates a markdown report with summary statistics, per-instance detail, and interpretive findings. This approach, structured-output prompts applied with a frontier reasoning model, produces substantially more reliable and auditable results than the initial rapid demonstration.

Additional python code that supports refusal analysis code is available in the open-source repo here https://github.com/FocusOnFoundationsNonprofit/public-corpus-tools. This code base was created and partially funded by the Balvi grant received by FloodLAMP to open-source and publish its work from the pandemic. In particular, 3 python modules fileops.py, llm.py, and rag.py contain code to 1) process text/markdown files, 2) run llm prompts over them (both normal prompts and function calls/structured output prompts), and 3) perform the QRAG retrieval and routed prompt call. With the advances in AI coding since this codebase was developed in 2024, these modules could likely be significantly improved or recreated from scratch.

The capability offered by these modules is powerful, as they enable programmatic file processing and the application of AI to collections of files. Using this code, anyone, a journalist, a researcher, an advocacy group, a government staffer, can take a large body of public records like these 100 town hall transcripts, apply a sophisticated and objective analytical framework to the entire corpus, and produce results that would have taken a team of analysts months to compile, for almost nothing in time and cost. And those results can be used to discover and expose problems, from significant structural failures to meaningful inefficiencies, in the operation of agencies, institutions, and bureaucracies. And then, crucially, to develop and advocate for specific, actionable reforms. Not vague calls for "more transparency" but concrete proposals grounded in evidence extracted from the institution's own public record. That is what this analysis attempts to demonstrate, and that is what the open-source tools in this repository are designed to enable.

### Transparency and the case for publishing rejection letters
FDA Commissioner Marty Makary, in a January 2025 interview on the All-In Podcast, stated:

> "We've got to challenge these deeply held assumptions. And we're doing it. We are doing it with new programs, new priority reviews, new pilots, new forms of transparency. We made our rejection letters public so that if the FDA does not approve a drug, the public deserves to know why. And it creates accountability. And that was not the case before. They talked about it for 30 years and we got it done."

This remark was made in the context of drug approvals, but the principle applies equally to diagnostics. In the context of the pandemic, when a diagnostic test developer submitted an EUA application, the expectation was that the submission was complete and ready for authorization. The FDA also offered a pre-submission question process (or pre-EUA process) for obtaining feedback on incomplete work. Once the formal submission was made, if the FDA authorized the test, the submission (at least a version of it in the form of the IFU) becomes public. There is a strong argument that rejected submissions and the FDA's stated reasons for rejection should both be made public. The submitter has represented the application as ready for authorization and precious resources have been used to review it. Transparency from that point forward could lead to faster processing, greater consistency, higher quality submissions, and greater encouragement of innovation.

### FDA's internal use of AI
A companion report in this subcategory (`_AI_FDA_Internal_AI_Use_Report`) examines the FDA's early adoption of internal generative AI tools, including the "Elsa" platform and the 2025 AI-assisted scientific review pilot. As of that report's date, there has been limited public progress in the direction of the standardization and transparency measures discussed above. The stated capabilities of Elsa (accelerating clinical protocol reviews, shortening scientific evaluations, summarizing adverse events, performing label comparisons) suggest operational efficiency gains, but no center-specific SOPs or workflow changes have been published. These internal AI developments are worth monitoring, as they could eventually affect review workflows, consistency, and processing times for diagnostic submissions.


# 3,338  _context-commentary_regulatory-fl-fda-submissions.md
METADATA
last updated: 2026-03-19 RT
file_name: _context-commentary_regulatory-fl-fda-submissions.md
category: regulatory
subcategory: fl-fda-submissions
gfile_url: https://docs.google.com/document/d/1hDlXqrnIvU096_wlMpKcl9oFBAuSiIalUDnoIWi5FUk
words: 1944
tokens: 3338


CONTENT

## Context
This `regulatory/fl-fda-submissions` subcategory contains FloodLAMP's FDA Emergency Use Authorization (EUA) submissions and associated Instructions for Use (IFU) documents for its SARS-CoV-2 diagnostic tests. There are 15 files spanning from November 2020 to October 2021, representing the full arc of FloodLAMP's regulatory submission effort. For background on the EUA framework itself and how it differs from standard 510(k) IVD approvals, see the `regulatory/fda-policy` subcategory. For the correspondence with the FDA that accompanied these submissions, see `regulatory/fl-fda-correspondence`.

The subcategory documents a pre-EUA in 2020 and 2 rounds of multiple EUA submissions. The "QuickColor" test is the main FloodLAMP test, and one that was used for all of FloodLAMP's surveillance pilot programs. **When the "FloodLAMP test" is used throughout the files in this archive, the direct, extraction-free colorimetric LAMP visually-read "QuickColor" test is the one being referred to.**

### Pre-EUA (Nov 2020) - Purified "Glass Milk" LAMP Test
The earliest submission, a colorimetric RT-LAMP assay using silica ("glass milk") purification of nucleic acids from saliva and anterior nares swab specimens (from the Harvard Rabe-Cepko protocol). This was a pre-EUA — a preliminary package submitted to initiate FDA engagement and enter the review queue. It targeted asymptomatic screening with sample pooling at a baseline level of 10. The limit of detection (LoD) was 2 copies/uL. The outcome of this pre-EUA was an hour-long call with a lead reviewer who strongly recommended against submitting for asymptomatic and pooling, and instead and instead recommended the standard indication of individual person suspected of COVID. We followed that advice, perhaps mistakenly (see Commentary in `regulatory/fl-fda-correspondence/_context-commentary_regulatory-fl-fda-correspondence`).
- `regulatory/fl-fda-submissions/2020-11-06_Pre-EUA Sub - FloodLAMP Glass Milk LAMP Test.md`

### First Round EUA Submissions (March 2021) - Direct Extraction-free QuickColor LAMP and EasyPCR Tests
The first round of submissions included 2 extraction-free tests: "QuickColor" - colorimetric visually-read LAMP and "EasyPCR". Both tests use the same TCEP inactivation with the PCR test using the SalivaDirect primers and probes (a variation of the CDC test). An additional test, "QuickFluor" fluorimetric LAMP, was included in all of the wet-validation experiments as well as the Stanford clinical validation, but was not submitted due to both the performance and the lack of need for the test.

#### FloodLAMP QuickColor COVID-19 Test
(EUA Submission + IFU, v1.0 March 2021, v1.1 May 2021, v1.2 draft October 2021): An extraction-free, colorimetric RT-LAMP assay with a visual pink-to-yellow readout requiring no specialized instrumentation, based directly on the Rabe-Cepko assay (see `various/papers` and `various/lamp-tech`). It used 18 LAMP primers targeting three SARS-CoV-2 genes (ORF1ab, N, E) and the same TCEP-based inactivation as the EasyPCR test. The LoD was 12,500 copies/mL. Clinical evaluation at Stanford showed 90% positive agreement and 100% negative agreement on 80 specimens. The v1.2 IFU introduced triplicate repeat procedures for inconclusive results. 
- `regulatory/fl-fda-submissions/2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md`
- `regulatory/fl-fda-submissions/2021-03-22_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.0.md`

#### FloodLAMP EasyPCR COVID-19 Test
(EUA Submission + IFU, v1.0 March 2021, v1.1 May 2021): An extraction-free, duplex RT-qPCR assay using the CDC N1 and human RNaseP primer-probe sets, with TCEP-based chemical inactivation and heat treatment. It required standard RT-PCR instruments (QuantStudio, Bio-Rad CFX96) but no nucleic acid extraction equipment. The LoD was 3,100 copies/mL. Clinical evaluation at Stanford showed 97.5% positive agreement and 100% negative agreement against a high-sensitivity comparator on 80 specimens.
- `regulatory/fl-fda-submissions/2021-03-22_EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.0.md`
- `regulatory/fl-fda-submissions/2021-03-22_Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.0.md`

#### FloodLAMP FLAMP (QuickFluor) COVID-19 Test (NOT SUBMITTED)
(EUA Submission + IFU draft, March 2021, NOT SUBMITTED): A fluorimetric RT-LAMP assay using real-time fluorescence readout on RT-PCR instruments. It used the same primers and inactivation as QuickColor but with fluorescent detection instead of colorimetric. The LoD was 50,000 copies/mL and clinical evaluation showed 80% positive agreement and 100% negative agreement. This test was prepared but never submitted to the FDA.
- `regulatory/fl-fda-submissions/2021-03-26_EUA Submission - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.md`
- `regulatory/fl-fda-submissions/2021-03-26_Instructions for Use - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.md`

### Second Round EUA Submissions (May 2021) - Re-sub QuickColor and EasyPCR plus Pre-EUA for Pooling and Asymptomatic
The second round consisted of revised May 2021 QuickColor and EasyPCR submission packages together with the separate pooling and asymptomatic screening pre-EUA materials.
- `regulatory/fl-fda-submissions/2021-05-18_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.1.md`
- `regulatory/fl-fda-submissions/2021-05-18_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.1.md`
- `regulatory/fl-fda-submissions/2021-10-01_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.2.md`
- `regulatory/fl-fda-submissions/2021-05-18_EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.1.md`
- `regulatory/fl-fda-submissions/2021-05-18_Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.1.md`

#### Pooled Swab Collection and Screening Studies
(Pre-EUA submissions, May 2021): Three documents supporting FloodLAMP's pooling and asymptomatic screening strategy, including a pre-EUA for a direct-to-consumer pooled swab collection kit (allowing 1–4 self-collected anterior nasal swabs in a single tube), collection kit instructions, and a proposed validation study design for pooling and serial asymptomatic screening aligned to FDA guidance.
- `regulatory/fl-fda-submissions/2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection DTC.md`
- `regulatory/fl-fda-submissions/2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection Kit DTC.md`
- `regulatory/fl-fda-submissions/2021-05-18_Pre-EUA Sub - FloodLAMP Proposed Pooling and Asymptomatic Screening Study.md`

Each submission follows the FDA's EUA template structure: purpose, measurand, applicant information, regulatory status, proposed intended use, device description and test principle, controls, interpretation of results, manufacturing and component sourcing, and performance evaluation (LoD, inclusivity, cross-reactivity, interfering substances, clinical evaluation). The IFU documents mirror much of this content in an operational format for laboratory use.

All of FloodLAMP's tests shared a common TCEP-based chemical inactivation step and were designed as "open source protocol" tests — meaning all reagent components were fully disclosed (no "reaction mix 1", etc.) such that designated CLIA high-complexity laboratories could source all components directly from commercial vendors rather than purchasing proprietary kits, reducing cost and enabling supply chain redundancy. This open-source approach is central to FloodLAMP's strategy, as documented in the `regulatory/open-euas` subcategory. The EasyPCR and QuickColor tests were designed to work as an integrated pair: QuickColor for high-throughput colorimetric screening (45-minute turnaround, no instruments) and EasyPCR for rapid PCR-based confirmation (~1 hour 45 minutes). New England Biolabs supported both tests with their LAMP master mix and Luna RT-qPCR kit, and LGC Biosearch Technologies supplied production-scale LAMP primer sets.

The submissions evolved across versions. The v1.0 submissions (March 2021) proposed intended use for "individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval." The v1.1 submissions (May 2021) reframed the intended use around "routine screening programs" in settings like schools and workplaces. None of these submissions received FDA authorization.

### Archive Files Not Converted to Markdown
`2020-11-04_Pre-EUA Sub Supporting Data - Glass Milk LAMP Test.xlsx`
`2021-03-22_EUA Sub Supporting Data - FloodLAMP EasyPCR COVID-19 Test.xlsx`
`2021-03-22_EUA Sub Supporting Data - FloodLAMP QuickColor COVID-19 Test.xlsx`
`2021-03-26_EUA Sub Supporting Data - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.xlsx`
`2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection Kit DTC design file.sketch`


## Commentary
The primary commentary for submissions is combined with the `regulatory/fl-fda-correspondence` subcategory — see `regulatory/fl-fda-correspondence/_context-commentary_regulatory-fl-fda-correspondence.md` regarding FloodLAMP's FDA engagement. Here are comments on the more technical aspects of the EUA submission process.

The EUA submission process involves two main types of documents: the submission itself and the Instructions for Use (IFU). The submission is the regulatory document — it follows the FDA's structured template. The IFU is the operational document intended for the laboratories that will run the test. They overlap substantially in content, but serve different audiences and purposes. Both must be prepared and aligned, and both are substantial documents. For FloodLAMP, each test's submission ran 5,000–10,000 words, and each IFU ran 7,000–14,000 words.

A critical concept in understanding these documents is that the FDA authorizes test systems, not tests in isolation. The entire system — reagents from specific vendors, validated instruments, the exact workflow, controls, and interpretation criteria — is what receives authorization. Changing a single component can require revalidation. For open-source protocol tests like FloodLAMP's, this posed an inherent tension: the whole point was to enable broad deployment using commodity components from multiple suppliers, but the regulatory framework required specificity at every level. FloodLAMP addressed this by validating multiple instruments (QuantStudio 6 Flex, QuantStudio 7 Pro, Bio-Rad CFX96) and multiple primer and probe vendors (Eurofins Genomics, IDT, LGC Biosearch) within a single submission.

The bench science for EUA validation can actually move quite fast. In a conversation with another test developer, an academic who started a company during the pandemic and did obtain an EUA, they described doing the core validation work in a weekend. The bottleneck is not the assay work itself but the surrounding logistics and documentation. FloodLAMP also had a significant delay in getting registered with BEI Resources to obtain the cross-reactivity reagents. The FDA requires testing against a panel of related pathogens and respiratory flora, and BEI is the primary source for those reference organisms. The registration and shipping process takes weeks, and for a small organization running lean, that waiting period was a significant constraint.

As an aside regarding the fluorimetric version of the LAMP test, which we did all of the validation work for but did not submit, it showed a worse limit of detection (LoD) in our hands compared to colorimetric LAMP (50,000 vs. 12,500 copies/mL). However, we spent very little time optimizing the fluorimetric test, and our requirement was that all 3 tests (colorimetric LAMP, fluorimetric LAMP, and PCR) use the same inactivated sample so there was no flexibility there. Importantly, New England Biolabs (NEB) used a combination colorimetric plus fluorimetric LAMP test for its in-house workplace screening program (see `various/papers-lamp/Tanner (NEB and Mirimus) - Preprint - Extraction-Free Saliva SARS-CoV-2 RT-LAMPWorkflow for Workplace Surveillance (3-11-2022).pdf`). Their LoD was quite similar in magnitude (40,000 copies/mL), though the matrices are different (raw saliva vs. swab eluate in TCEP+saline), so direct numerical comparison has to be done carefully. Both are roughly aligned with what you'd expect from a sensitive RT-qPCR comparator — the Tanner paper reported a clinical sensitivity of 97% and 100% specificity, which is higher than what FloodLAMP saw from the Stanford Clinical Lab clinical validation run (80% positive agreement and 100% negative agreement). See the files and section of the context and commentary in `regulatory/fda-policy` related to the FDA Reference Panel for perspective on the problems related to test performance metrics.

Even with the FDA's templates available, the document preparation for COVID-19 EUAs was a heavy lift for anyone who has not done it before. FloodLAMP benefited from other groups sharing their actual EUA submission documents — these are not published, and they differ in important ways from the public-facing authorizations and IFUs that appear on the FDA website. Having real examples was helpful for understanding the level of detail and the conventions that the templates alone do not fully convey. If the FDA allowed or facilitated sharing of these submissions, for example, by simply letting developers choose to publish their submissions openly, some likely would, especially academics and public-interest/nonprofit developers. This would meaningfully lower the barrier for new entrants.

The new capabilities of AI could transform the document preparation burden of regulatory submissions and compliance in the disease testing field. EUA submissions and IFUs are highly structured, repetitive across test types, and draw heavily on standardized language. With progress on standardization and transparency from the FDA — such as machine-readable templates, published example submissions, and clearer guidance on acceptable variations — AI tools could handle much of the drafting, cross-referencing, and consistency-checking that currently consumes weeks of a developer's time. The combination of AI and regulatory modernization could significantly reduce the cost and time to bring validated, innovative tests to market. See also `regulatory/reg-articles-misc/_context-commentary_regulatory-reg-articles-misc` and `regulatory/reg-articles-misc/2021-01-18_Phillips and Dinakar - A Proposal for Increasing the Speed of Validating SARS-CoV-2 Diagnostic Tests`.


# 1,663  _context-commentary_regulatory-fl-fda-correspondence.md
METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-fl-fda-correspondence.md
category: regulatory
subcategory: fl-fda-correspondence
gfile_url: https://docs.google.com/document/d/1Au8cMEREFdSkJl4vRh6G6dUAZr9aCqhKUFUdahlD82o
words: 1132
tokens: 1663


CONTENT

## Context
This `regulatory/fl-fda-correspondence` subcategory contains FloodLAMP's direct correspondence with the FDA regarding its SARS-CoV-2 diagnostic test EUA submissions, spanning from October 2020 through October 2021. The files include pre-EUA requests, emails to FDA leadership, FDA deficiency letters, meeting notes, FloodLAMP's written responses, and the deprioritization/closure letters that ended FloodLAMP's EUA pursuit. For the submission documents themselves and technical background on the EUA process, see `regulatory/fl-fda-submissions/_context-commentary_regulatory-fl-fda-submissions`.

During the COVID-19 pandemic, the FDA's Center for Devices and Radiological Health (CDRH) managed EUA requests for diagnostic tests through a process that evolved substantially as submission volume grew. Communication between the FDA and test developers typically occurred through a combination of formal letters (deficiency notices, final decisions), email exchanges with assigned reviewers, optional pre-EUA feedback, and periodic virtual town halls open to the broader developer community. The FDA also offered short interactive review meetings (typically 30 minutes) to discuss specific submission issues.

For developers seeking EUAs, the process began with either a pre-EUA submission (to get preliminary feedback before a full filing) or a direct EUA submission. The FDA would then triage the submission based on prioritization factors, primarily whether the test would increase testing accessibility (point-of-care, at-home) or significantly expand testing capacity (high-throughput, high-volume manufacturing). Beginning in fall 2020, the FDA formalized a deprioritization system that included two mechanisms: "Decline to Review" for low-priority submissions and "Decline to Issue" for submissions with unresolved critical deficiencies. By September 30, 2021, the FDA had declined to review 558 EUA requests for COVID-19 tests. For more on deprioritization, see the companion research report `_AI_FDA Deprioritization of COVID-19 Diagnostic EUAs`.

FloodLAMP's correspondence documents the full arc of engagement with the FDA:
- early encouragement from OIVD Director Tim Stenzel on the open-source protocol approach (December 2020),
- initial EUA submissions and immediate deprioritization (March–April 2021),
- a pre-EUA that the FDA closed without reviewing the validation data (May–June 2021),
- a direct appeal to FDA leadership with real-world surveillance data (October 4, 2021),
- a deficiency letter from the FDA followed by a 30-minute Zoom meeting and written response (October 13–20, 2021),
- final closure one day after FloodLAMP's response (October 21, 2021).

The correspondence with the FDA on FloodLAMP's open-source EUA submissions is closely connected to two other `regulatory` subcategories: the `regulatory/fda-townhalls` subcategory where FloodLAMP engaged FDA leadership publicly, and the `regulatory/open-euas` subcategory that was central to FloodLAMP's regulatory strategy.


## Commentary
FloodLAMP's experience with the FDA during the COVID-19 pandemic was defined by a persistent inability to obtain meaningful regulatory engagement on submissions that, by the FDA's own stated criteria, should have warranted review. The company developed a validated, instrument-free, colorimetric RT-LAMP test at a cost of $1–2 per reaction, designed as an open-source protocol modeled on the SalivaDirect EUA. The test was adopted by EMS agencies and municipal fire departments for routine surveillance screening. Despite multiple submissions, real-world deployment data, and direct appeals to FDA leadership, FloodLAMP received blanket deprioritization along with hundreds of other test developers. Had a meaningful review, let alone an EUA, been obtained in the spring of 2021, the trajectory of the company would have been fundamentally different.

For a detailed factual reconstruction and analysis of the critical October 2021 correspondence sequence that ended FloodLAMP's EUA pursuit, see `_AI_FloodLAMP FDA October 2021 Correspondence Analysis`. That document covers the complete timeline from October 2020 through October 2021, the FDA's stated justifications, and multiple interpretive explanations of the FDA's rationale. For related commentary on the FDA town halls and the open EUA concept, see `regulatory/fda-townhalls/_context-commentary_regulatory-fda-townhalls` and `regulatory/open-euas/_context-commentary_regulatory-open-euas`.

The first direct interaction with the FDA was in a November 2020 phone call for the pre-EUA. The assigned reviewer had not heard of SalivaDirect, DetectaChem, or even LAMP as a technology. The reviewer strongly recommended against pursuing anything unusual, specifically asymptomatic testing or pooling, saying that any indication except the standard single symptomatic person suspected of COVID-19 would face long delays and was less likely to be authorized. Despite our initial intention of doing asymptomatic and pooling, we followed the reviewer's advice and submitted our initial EUAs for the standard indication of persons suspected of COVID-19. In hindsight, we should have stuck to our guns and submitted for asymptomatic screening and pooling. We did shift to that with our second round of May 2021 submissions, after the FDA announced those as priorities, but we lost a lot of valuable time between our first pre-EUA in Nov 2020 and our second round of submissions in May 2021.

The FDA's rationale for deprioritization consistently came back to being short-staffed and resource-constrained. These were real constraints. But the response to those constraints, blanket deprioritization, failed a basic policy test. At the point FloodLAMP was deprioritized, the country was more than a year into the pandemic. The question the FDA should have been asking was: "Will this decision result in less testing?" When the answer was yes, better solutions were warranted. The FDA could have established streamlined review tracks for open-protocol tests, created batch review processes for submissions using validated primer sets, facilitated reference panels for small developers, or simply provided actionable feedback rather than closing files without reviewing the data. None of these were pursued. The ITAP (Independent Test Assessment Program) eventually emerged as a partial alternative pathway, but it had limited access and transparency.

The October 4, 2021 letter to OIVD Director Tim Stenzel stands as one of the best summaries of FloodLAMP's case for its test and its work. In that letter, FloodLAMP presented real-world surveillance data from five sites across three states, approximately 2,300 people screened in 800 pools with three unknown positives detected and no known false negatives, alongside manufacturing readiness (2 million tests on hand, 3 million more at LGC Biosearch), $1–2 per test pricing, and active commercial sites with EMS and fire departments. Stenzel never responded to this letter, which was the second non-response as FloodLAMP had sent a letter addressed directly to Dr. Stenzel in its first round of EUA submissions in March 2021. The review team sent a 6-deficiency letter nine days after the letter to Dr. Stenzel (Oct 13, 2021), offered a 30-minute Zoom call the following day, received a substantive written response on October 20, and issued a final closure on October 21. The speed of that closure, one day after FloodLAMP's response that proposed a narrowed intended use and addressed multiple deficiencies, suggests the outcome was predetermined and the interactive review seemed to be procedural rather than genuinely deliberative.

Five weeks after the FDA closed FloodLAMP's submission, the Omicron variant was reported. By January 2022, the United States experienced the worst testing shortage of the entire pandemic. The principle behind the deprioritization decision, that the country did not need more tests, was catastrophically wrong, and it was applied systematically to FloodLAMP and hundreds of other test developers.


# 1,716  _context-commentary_regulatory-irb.md
METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-irb.md
category: regulatory
subcategory: irb
gfile_url: https://docs.google.com/document/d/1sE0sSdbNQQdnjboL018-i4POE-zEj8hSqsGKJFyKYkA
words: 1232
tokens: 1716


CONTENT

## Context
An Institutional Review Board (IRB) is an independent ethics committee that reviews and approves research involving human subjects. Any clinical study collecting specimens from human participants, including the clinical performance studies needed for FDA Emergency Use Authorization (EUA) submissions, requires IRB approval before it can begin. The IRB evaluates whether the study design adequately protects participants' rights, safety, and welfare.

This `regulatory/irb` subcategory contains two files from FloodLAMP's IRB process: a clinical study protocol and an informed consent form, both dated April 2021 (Protocol 20210401). The protocol, titled "FloodLAMP COVID-19 Biobank and Test Validation Protocol" outlined a study to collect up to 100,000 consented clinical specimens across multiple U.S. sites to evaluate FloodLAMP's molecular COVID-19 assays (QuickColor RT-LAMP, QuickFluor RT-LAMP, and EasyPCR RT-qPCR) and a home collection kit. The informed consent form documented voluntary participation, specimen handling, de-identification procedures, and participant rights.

The relationship between the IRB and FDA EUA submissions is sequential rather than direct: IRB approval is a prerequisite for conducting a clinical study, and the clinical study generates the performance data that gets submitted to the FDA as part of an EUA application. The IRB itself does not appear in the EUA submission. Rather, it serves as the regulatory gatekeeper that must approve the study before clinical specimens can be collected from human participants. FloodLAMP needed clinical performance data — positive and negative percent agreement against an EUA-authorized high-sensitivity PCR comparator — to support its 2nd round of EUA submissions for pooling, asymptomatic, and the new serial screening claims. Generating that data required running a clinical study on human specimens, and running that study required IRB approval.

Note that this IRB is not related to FloodLAMP's first round of EUA submissions in March of 2021. The Stanford Clinical Lab performed the clinical study for those submissions, using banked samples.

FloodLAMP obtained IRB approval through WCG (formerly Western Institutional Review Board), a well-known commercial IRB. The protocol was broad and flexible, designed to cover three collection modalities: co-located sites adjacent to existing testing programs (such as Stanford or San Francisco city testing sites), independently operated FloodLAMP collection sites, and distributed home collection kits. The study also included provisions for the FloodLAMP Mobile App, pooled specimen collection, and multiple swab types.

Despite obtaining IRB approval and preparing a detailed protocol, FloodLAMP never executed the clinical study, due to the FDA's decision to decline further review of FloodLAMP's second round of EUA and Pre-EUA submissions. Later in FloodLAMP's trajectory, around mid-2022, a new clinical study design was developed that attempted to address some of these constraints. The design integrated clinical data collection into an active surveillance testing program (which could be school or workplace-based), using an enrichment strategy to solve the low-prevalence problem and a cascading cohort structure to maximize data yield per positive event. This study design may be able to collect clinical performance data at a fraction of the cost of a typical standalone trial. The design is documented in a companion file (`_AI_digestion_irb_new-clinical-study-design`) and may be of interest to researchers or organizations facing similar challenges in generating clinical data for novel diagnostics during periods of variable disease prevalence.

Other parts of the archive document the FDA submission process itself. The `regulatory/fl-fda-submissions` and `regulatory/fl-fda-correspondence` subcategories in the `regulatory` category contain the EUA applications and related correspondence that these IRB documents were intended to support.

### Archive Files Not Converted to Markdown
`IRB - FloodLAMP Case Report Form 20210401 v01.docx`
`IRB - FloodLAMP Case Report Form 20210401 v01.pdf`
`IRB - FloodLAMP Home Collection Kit Instructions for Use.pdf`
`IRB - FloodLAMP Study Advertisement.pdf`
`IRB - Instructions for Use - FloodLAMP QuickFluor COVID-19 Test.pdf`

Also included are 10 additional IRBs, consent forms, and clinical study designs from other organizations, located in the `IRBs and Consents from Others` subfolder:
`American Cancer Society event LIABILITY WAIVER AND RELEASE OF CLAIMS.pdf`
`Arizona Dept of Health Services informed consent.pdf`
`Color Genomics IRB.docx`
`Color Genomics IRB.pdf`
`EmpowerDX (Eurofins) consent form.docx`
`EmpowerDX (Eurofins) consent form.pdf`
`Lucira Screenshot_2021-02-17 COVID-19 Test Study.png`
`NextEraEnergy PCR Testing Patient Consent Form.pdf`
`Stanford Catch Consent.docx`
`Stanford Catch Consent.pdf`


## Commentary
The IRB process was handled through WCG (Western Institutional Review Board), with a total cost of $11,360 over two years including a renewal. On top of this was another approximately $10K of regulatory consulting. This was a considerable expense for a small company. Even more burdensome than the cost was the time required to prepare the IRB. Overall the IRB was a painful process and sore spot, especially since the clinical study was never actually conducted. The IRB approval and the detailed protocol it covered remained unused.

The experience highlighted what appeared to be a cumbersome and inefficient process. The IRB pathway felt siloed, with limited templates, examples, or structured support available for small organizations navigating it for the first time, particularly during a public health emergency when speed should have been a priority. For a small company attempting to bring a new diagnostic test through the regulatory pathway during an active pandemic, the combination of IRB costs, the time required to prepare the protocol, and the separate expense of actually running a clinical study created significant barriers to generating the clinical data that the FDA required.

To illustrate the broader cost picture: FloodLAMP received a quote of approximately $100,000 from a clinical research organization to manage participant recruitment and sourcing alone, targeting roughly 40 positive specimens. This did not include running the tests themselves; a separate CLIA laboratory was needed for that. These costs reflected the broader pandemic dynamic, where demand for clinical services far outstripped supply and pricing reflected that imbalance. This seems like an especially crazy state of affairs given the high proportion of positive people and those exposed in the population.

The IRB and clinical study process, as experienced, suggests an area where standardization and streamlining could benefit the field, both in routine times and especially during public health emergencies. The barriers to generating clinical performance data disproportionately affect small companies and organizations that lack established clinical trial infrastructure, institutional IRB relationships, or the budgets to absorb six-figure study costs. If decentralized and low-cost diagnostic testing is to play a meaningful role in future pandemic response, the regulatory pathway for generating the required clinical data may need to be correspondingly accessible.

The FDA did recognize elements of this problem. Through a collaboration with the NIH, the Rapid Acceleration of Diagnostics (RADx) program established the Independent Test Assessment Program (ITAP), which provided standardized evaluation protocols, data reporting mechanisms, and targeted outreach to test developers to accelerate regulatory review and authorization. ITAP facilitated the authorization of a number of at-home and point-of-care COVID-19 tests, and the model has since been extended to other diagnostics including multiplex respiratory panels, mpox, and hepatitis. However, ITAP's COVID-19 focus was primarily on rapid antigen tests, and the program's resources and outreach were oriented toward developers with tests already authorized in other markets or at a relatively advanced stage. While ITAP likely accelerated some authorizations, it was initiated late in the pandemic and did not address the more fundamental barriers and inefficiencies of the overall EUA clinical study and IRB process, and it was not readily accessible to smaller, earlier-stage companies and organizations developing novel testing approaches. For more on FloodLAMP's engagement with RADx-related programs, see the archive files in the `various/fl-proposals` subcategory and the archive file `various/external-programs-reports/_AI_RADx Program Overview - NIH Rapid Acceleration of Diagnostics.md`.


# 1,004  _context-commentary_regulatory-ldts.md
METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-ldts.md
category: regulatory
subcategory: ldts
gfile_url: https://docs.google.com/document/d/1-h7-WwW6LJJGXYA2PkXkabY6Bg6FkUveCizPi2xcm0c/edit?usp=sharing
words: 695
tokens: 1004


CONTENT

## Context
This `regulatory/ldts` subcategory contains documents related to LDTs, though the FloodLAMP test itself was never used as an LDT (at least in connection to us and as far as we know). Our pilots operated under surveillance (see the `regulatory/surveillance` subcategory). We submitted to the FDA for IVD EUA. The closest we came with respect to an LDT was discussions with UnitedHealth Group about a clinical lab network adopting our direct LAMP test as an LDT. We shared all of our information (data, FDA submissions, cost model, etc.), but they did not move forward with the project.

As a background explainer, Laboratory-developed tests (LDTs) are in vitro diagnostic tests that are designed, manufactured, and used within a single clinical laboratory, as opposed to commercial IVD test kits produced by diagnostic manufacturers and sold to laboratories across the country. Commercial IVDs are subject to FDA premarket review under the medical device classification system, while LDTs have historically operated under FDA "enforcement discretion," meaning the agency asserted jurisdiction but generally chose not to enforce device requirements. This distinction created a bifurcated market: commercial diagnostic products held to rigorous FDA analytical and clinical validation standards, and laboratory-developed tests for the same purposes that were primarily overseen through CMS under the Clinical Laboratory Improvement Amendments (CLIA). The tension between these two regulatory tracks became a central issue during the COVID-19 pandemic and in the years that followed.

The `2020-10-03_JD Supra Article - FDA Oversight of Laboratory-Developed Tests Continues To Evolve` article by Skadden Arps attorneys provides a useful overview of the decades-long history of LDT regulation, tracing FDA's evolving posture from initial enforcement discretion through the 2010 public workshop, the 2014 draft guidance, the 2017 retreat to Congress, and the COVID-era policy reversals. It remains a good starting point for understanding the regulatory backdrop against which COVID-era LDT policy played out.

Two AI-generated reports in this subcategory provide more detailed analysis. The first, `_AI_COVID19_LDTs_FDA_Policy_Report`, is a detailed synthesis of how FDA oversight of COVID-19 LDTs moved through three distinct phases: initial EUA-based enforcement discretion, the August 2020 HHS policy blocking mandatory premarket review, and FDA's restoration of an EUA-first posture after November 2021. The second, `_AI_FDA 2024 LDT Rule - Status and Legal History`, covers the post-pandemic attempt by FDA to formally end broad enforcement discretion for LDTs through rulemaking, the subsequent legal challenge, the March 2025 court vacatur, and FDA's decision not to appeal, which returned LDT oversight to the pre-2024 status quo.

Related regulatory subcategories in this archive include the `regulatory/fda-policy` subcategory, which covers broader FDA regulatory actions and user fee frameworks; the `regulatory/fda-townhalls` subcategory, which documents the weekly public calls FDA held with COVID-19 test developers; the `regulatory/surveillance` subcategory, which covers the surveillance testing framework under which many LDT-based programs operated; and the `regulatory/open-euas` subcategory, which discusses a promising, innovative alternative to the FDA IVD vs CMS/CLIA LDT division.


## Commentary
LDT regulation is deeply interconnected with FDA testing policy. As the `_AI_COVID19_LDTs_FDA_Policy_Report` documents in detail, the FDA went back and forth during the pandemic on whether LDTs needed EUA authorization, with HHS at one point blocking mandatory premarket review entirely and FDA later restoring an EUA-first posture. Underlying these policy swings is a structural gap in the regulatory framework: there is no middle ground between laboratory-developed tests, where a single lab has broad authority to develop and use a test internally, and commercial IVDs produced by manufacturers who contract with reagent companies to produce kits sold to laboratories nationwide (or direct to consumers for at-home devices). This gap became acutely problematic during the pandemic, when the need to rapidly scale testing could not be met by either existing regulatory model. A promising solution emerged in the form of the Open EUA, pioneered and authorized during the pandemic by the SalivaDirect program under Dr. Anne Wyllie. The EUA allowed multiple laboratories to adopt and run a validated protocol under a shared authorization, overseen and managed by a responsible party (which became a nonprofit). Unfortunately, the Open EUA concept was not further developed by FDA or the field, and it remains an underexplored pathway.

For fuller commentary on LDTs, FDA policy, and Open EUAs, see `regulatory/open-euas/_context-commentary_regulatory-open-euas.md`.


# 2,033  _context-commentary_regulatory-open-euas.md
METADATA
last updated: 2026-03-22 RT
file_name: _context-commentary_regulatory-open-euas.md
category: regulatory
subcategory: open-euas
gfile_url: https://docs.google.com/document/d/1ysH5-xFHTdvN6e2LJ5IjFgOlP7Kjb7GZZomspeV4hQg 
words: 1507
tokens: 2033


CONTENT

## Context
This subcategory `regulatory/open-euas` documents the concept of "open EUAs," the combination of open-source diagnostic protocols with a new designation-granting FDA authorization. The Open EUA approach was central to FloodLAMP's regulatory strategy. For a comprehensive analysis of the concept, its history, regulatory mechanics, and implications, see the companion research report in this subcategory: `_AI_open-euas-open-access-diagnostics-report`.

The files here include:
- **FDA press release (Aug 15, 2020)** announcing the SalivaDirect EUA, which contains FDA's explicit use of "open source protocol" framing and describes the designated-laboratory model.
- **Anne Wyllie nomination letter (June 2022)** for the Reagan-Udall Foundation Innovation in Regulatory Science Award, written by FloodLAMP's founder, articulating the regulatory novelty of SalivaDirect's approach: an academic team seeking an IVD EUA without intending to manufacture kits, using CDC primers, fully disclosing ingredients, validating multiple suppliers and instruments, and working with FDA to create a designation process for CLIA labs.
- **Open EUA Consortium main document (late 2020)** recording FloodLAMP's attempt to convene multiple test developers around the open EUA model. The consortium aimed to build a suite of 5-8 open EUAs covering different sample types and technologies, with shared validation materials and supply chain coordination. It stalled quickly by the end of 2020.

The Open EUA concept, as analyzed in the AI report, is not merely about publishing protocols. It involves an institutional and legal pattern combining open-source protocols (fully disclosed, implementable with commodity components), open supply chains (multiple validated suppliers), and open-access authorization (multiple labs operating under one EUA through a steward/designation model). SalivaDirect is the most prominent example in FDA's COVID-19 set of EUAs. FloodLAMP pursued the same approach for its colorimetric LAMP and PCR tests but was unable to obtain authorization.

A related mechanism documented in this subcategory is the FDA "right of reference," which allows a new test developer to rely on validation data that FDA already reviewed for another EUA submission. During the COVID-19 emergency, a small number of these rights of reference were granted broadly and publicly — most notably by the CDC for its assay data, and by Quantigen Biosciences for specimen-collection swab-stability data supported by the Gates Foundation. The companion report `_AI_COVID_Rights_of_Reference_Report` analyzes the public, broad, and private rights of reference used across the EUA ecosystem and documents how the Quantigen RoR was reused by multiple unrelated sponsors.

These files connect to the `regulatory/fl-fda-submissions` subcategory, which contains FloodLAMP's submitted tests, and to the `regulatory/fl-fda-correspondence` subcategory, which documents FloodLAMP's direct engagement with the agency on its own open-source protocol EUA submissions.


## Commentary
The open EUA concept was at the center of FloodLAMP's regulatory strategy, and we consider it one of the most important points of regulatory progress to emerge from the COVID-19 diagnostic response. The AI research report in this subcategory provides a thorough analysis; here we offer FloodLAMP's perspective.

The FDA called SalivaDirect's EUA in mid-2020 "the most unusual submission they had ever received." Dr. Wyllie had worked with two former FDA reviewers to craft a multifaceted creative approach to an "open-source protocol" EUA. When the agency issued the authorization, its own press release called SalivaDirect a "game changer" and highlighted it as an example of "the FDA working with test developers to bring the most innovative technology to market." The FDA Commissioner explicitly encouraged other test developers to "work with the agency to create innovative, effective products to help address the COVID-19 pandemic." We took that invitation at face value and brought forward our own open-source protocol EUAs. We got nowhere with the FDA.

SalivaDirect demonstrated that it was possible to build a scalable, supply-chain-resilient testing network under a single FDA authorization using commodity components and a steward/designation model. We modeled our own EUA submissions on this approach and nominated Anne Wyllie for the Reagan-Udall Foundation Innovation Award. The nomination letter in this subcategory lays out the case for why the open-source protocol EUA represented a genuine regulatory innovation, not just a scientific one.

The Open EUA Consortium was our attempt to scale the idea beyond a single test. We convened a small group of developers in late 2020, but the consortium stalled quickly. At one level, the reasons are well captured by the AI report's analysis: the HHS policy change in August 2020 reduced the regulatory incentive for open EUAs (labs could offer LDTs without an EUA), the stewardship burden was significant, and funding was not available to sustain the coordination effort. At another level, trying to coordinate this group was challenging. FloodLAMP founder, Randy True, decided to just pursue the open EUAs ourselves first, so we then validated and submitted three related tests, Colorimetric LAMP, Fluorimetric LAMP, and Direct PCR from the same inactivated sample. The plan was to then help other groups in the gLAMP community obtain their own EUAs or collaborate with them under the FloodLAMP organization. In hindsight, this was quite overconfident.

One step we took that went beyond even SalivaDirect was committing to a blanket, open right of reference. In our March 2021 EUA cover letter, we stated that FloodLAMP would "offer a blanket right of reference to the LAMP primer validation data for any IVD test developer or CLIA lab," modeled on what the CDC had done for PCR primers (see `regulatory/fl-fda-correspondence`). We reiterated that commitment in our October 2021 correspondence with Tim Stenzel. A right of reference is a meaningful legal commitment: it allows any qualifying developer to rely on FDA-reviewed validation data without obtaining a separate permission letter, effectively functioning as a broad, open license over the underlying regulatory data. The CDC and Quantigen Biosciences are the clearest COVID-era precedents for this kind of blanket RoR, as documented in `_AI_COVID_Rights_of_Reference_Report`. SalivaDirect, by contrast, operated through a designation model — labs ran the test under Yale's EUA — rather than through an open right of reference enabling other developers to build on its validation data for their own EUAs. That said, by openly disclosing their chemical compositions, validated suppliers, and full protocol, the SalivaDirect team achieved something of enormous practical significance: many CLIA labs built their own LDTs directly from the published SalivaDirect protocol during the period when HHS had removed FDA oversight of LDTs, and it would not surprise us if the volume of tests run outside the SalivaDirect EUA exceeded the volume run under it by an order of magnitude or more. The designation process itself was, to our understanding, offered at no or minimal charge to labs, making SalivaDirect a massive and impactful public good. It is possible that the SalivaDirect team also granted open rights of reference in one or more of their 24 EUA amendments, but the original EUA Summary in this subcategory does not mention a right of reference, and we are not aware of such a grant.

It is worth underscoring why an open EUA is so much more valuable than simply publishing a protocol and expecting labs to develop their own LDTs. Developing and validating an LDT requires substantial expertise such as in silico bioinformatic analysis, wet-lab analytical and clinical performance characterization, cross-reactivity and interference testing. Only a small, single-digit percentage of moderate and high-complexity CLIA laboratories have the resources and personnel to undertake an LDT. A test that has gone through an EUA, whether sold commercially as a kit or provided as an open protocol, arrives at the clinical lab already validated with FDA-reviewed performance data, making it relatively straightforward for any qualified lab to implement. The open EUA model is the mechanism that bridges the gap between a published protocol and a test that the broad base of clinical laboratories can actually run.

FloodLAMP submitted multiple open-source protocol EUAs and was unable to obtain authorization, or to get meaningful engagement from FDA on these submissions (see `regulatory/fl-fda-correspondence`). The structural barriers identified in the AI report were real and material. The most striking is the asymmetry between government and non-government entities: the CDC was able to produce a test that any CLIA high-complexity lab in the country could run, simply by distributing reagents. No stewardship model, no lab-by-lab designation. When an academic lab (Yale/SalivaDirect) created something comparably open, the regulatory system required a full stewardship and designation infrastructure.

The AI report's analysis of the CDC test's Appendix A, the extraction-free protocol restricted to public health labs only despite being developed in response to a nationwide reagent shortage affecting all labs, captures a pattern we observed repeatedly: technical solutions existed but were constrained by institutional caution and regulatory framing rather than by scientific or safety considerations.

The "generics of diagnostics" framing from the nomination letter remains, in our assessment, directionally correct. The U.S. diagnostic regulatory system lacks a routine mechanism for deploying validated open protocols to competent laboratories without each lab filing its own submission or depending on a single steward's capacity. SalivaDirect showed one way to accomplish this during an emergency. Whether the model can be institutionalized for future outbreaks is an open question, but the design patterns in the AI report, particularly the four-layer taxonomy of openness and the practical framework for future open-access diagnostics, may be a useful starting point.


# 736  _context-commentary_regulatory-reg-articles-misc.md
METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-reg-articles-misc.md
category: regulatory
subcategory: reg-articles-misc
gfile_url: https://docs.google.com/document/d/1xx-Q92DTu_8sfcmDy22CP438nNey_La1ak5oMeZR0Vo
words: 492
tokens: 736


CONTENT

## Context
This `regulatory/reg-articles-misc` subcategory collects a small number of higher-level reports and assessments related to FDA oversight of COVID-19 diagnostics. These files are third-party or government-produced documents that provide a broader perspective on the EUA process and diagnostic test validation during the pandemic.

The three documents are:
- `2021-10-08_FDA Report - EUA Assessment by Booze Allen`: An FDA-commissioned review of CDRH's COVID-19 test EUA response, covering how the FDA used templates, guidance updates, triage, and deprioritization to manage thousands of submissions. It includes priority recommendations around IT systems, staffing models, and a validation framework for future emergencies. This report predates the Omicron surge and the severe testing shortages that followed.
- `2022-07-01_FDA Report - FDAs Work to Combat the COVID-19 Pandemic`: A broad FDA overview summarizing cross-center actions on vaccines, therapeutics, diagnostics, supply chain, inspections, and regulatory science, with data current as of April 2022.
- `2021-01-18_Phillips and Dinakar - A Proposal for Increasing the Speed of Validating SARS-CoV-2 Diagnostic Tests`: A paper proposing three extensions to the EUA process for accelerating diagnostic test validation: structured (machine-readable) EUA data submissions, distributed FDA-directed CLIA-led validation, and building an open synthetic patient clinical specimen panel.

In addition, an AI-generated research report (`_AI_fda-eua-covid-retrospectives_post2022_report`) was created during archive preparation to identify post-2022 retrospectives, evaluations, and criticisms of the FDA's EUA process. That report catalogs sources from government oversight agencies (HHS OIG, GAO, FDA), legislative bodies, NGOs, professional associations, and academics, and may serve as a starting point for readers interested in pursuing the broader literature on EUA reform and pandemic preparedness policy.

### Archive Files Not Converted to Markdown
`2021-02-02_California Coronavirus Testing Task Force - COVID-19 Testing Task Force Laboratory List .xlsx`
`ACLA - FAQ on COVID test reporting requirements for CLIA labs.pdf`
`CLIA Related Links.docx`
`CLIA Related Links.pdf`


## Commentary
The Phillips and Dinakar proposal for structured, machine-readable EUA data submissions resonated with FloodLAMP's own experience navigating the EUA process. The idea that submissions could be standardized in a way that accelerates FDA review, reduces ambiguity for developers, and enables computational analysis of submission data is the kind of practical, systems-level reform that would likely have compounding benefits across future emergencies.

More broadly, the potential for AI to improve FDA processes around diagnostic test evaluation, guidance development, and emergency response has been a recurring theme throughout this archive (see commentary on the `regulatory/fda-townhalls` subcategory and the `regulatory/open-euas` subcategory). The scale and complexity of the COVID-19 testing response — thousands of EUA submissions, rapidly evolving guidance, variant-driven obsolescence — represent exactly the kind of problem where AI-assisted workflows could meaningfully reduce friction, increase objectivity, and greatly reduce the discretionary and unpredictable FDA EUA review process that was in place during the COVID pandemic. Imagine if those same AI evaluation systems were transparent, objective, open, and available to test developers, and had already been scrutinized by a broad base of researchers in industry and academia; that kind of infrastructure could dramatically unlock testing and improve outcomes.


# 1,761  _context-commentary_regulatory-surveillance.md
METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-surveillance.md
category: regulatory
subcategory: surveillance
gfile_url: https://docs.google.com/document/d/1dFoISqFrvoEAitKyEkhKsZAPES7O-5IqHUTIGLqZ8S0
words: 1303
tokens: 1761


CONTENT

## Context
### Testing Types: Diagnostic, Screening, and Surveillance
During the COVID-19 pandemic, U.S. testing was categorized into three overlapping purposes:

- **Diagnostic testing**: Testing an individual when there is reason to suspect infection (symptoms or known exposure). Results are returned to the individual and their healthcare provider. The test must be FDA-authorized and is often processed in a CLIA-certified laboratory.
- **Screening testing**: Testing an individual without symptoms or known exposure, with the intent of making individual decisions based on results (e.g., return to school or work). Like diagnostic testing, screening requires FDA-authorized tests and results are returned to individuals.
- **Surveillance testing**: Population-level monitoring, often but not always using de-identified specimens. Results are not returned to individuals and are not to be used for individual decision-making. Surveillance testing does not require FDA authorization or CLIA certification.

### Clarification: "Surveillance" in This Archive
Throughout this `regulatory/surveillance` subcategory and elsewhere in the FloodLAMP archive, "surveillance" refers to non-diagnostic, non-clinical testing programs designed to detect and limit the spread of COVID-19 in schools, workplaces, and communities. It does not refer to wastewater surveillance or genomic variant surveillance, both of which are distinct modalities covered in the AI-generated report referenced below. The absence of a clear regulatory category and standardized terminology for this type of frequent, pandemic stop-the-spread testing is itself a significant gap in pandemic preparedness and response frameworks. There is no good name for it and no established regulatory pathway — an unsolved problem that affected programs like FloodLAMP throughout the pandemic.

### Key Documents in This Subcategory
For the authoritative regulatory definitions, two government documents provide the clearest framing:

- `FDA Website - COVID-19 Test Uses_ FAQs on Testing for SARS-CoV-2 (updated 2023-09-29)` — The FDA's post-crisis summary of diagnostic, screening, and surveillance definitions, including examples and CLIA/setting requirements.
- `CDC - Testing Strategies for SARS-CoV-2 (includes Surveillance 12-28-2021)` — Includes a summary matrix comparing the three testing strategies across settings, reporting requirements, and whether results may be returned to individuals.

FloodLAMP's own framing of how it operated under surveillance guidance is documented in:

- `FloodLAMP Surveillance FAQ and Links (June 2022 DRAFT)` — Contrasts diagnostic and surveillance testing, cites CMS/FDA guidance, and explains FloodLAMP's compliance posture. Includes FAQ-style responses prepared for the Coral Springs pilot program.
- `FloodLAMP Surveillance Information (Aug 2021 INTERNAL)` — A detailed internal memo on the regulatory framing for pooled non-diagnostic surveillance, including CMS enforcement discretion citations, an exchange between NIH Director Francis Collins and CMS Administrator Seema Verma on referral pathways, and the eCFR research-lab exemption.

Two outside analyses by professionals that were shared with us are also included:

- `Memo - Surveillance Authority Plain-language Research (Jan 2021 from Senior Medical Director in Healthcare Industry)` — A plain-language digest of FDA/CMS surveillance framing and the conditions under which presumptive positives may be routed to CLIA confirmatory testing.
- `Memo - USA Surveillance Strategy (Sept 2021 from non-FloodLAMP Healthcare Attorney)` — Guidance confirming that surveillance testing is generally not regulated when de-identified and no individual results are returned, and recommending coordination with local public health officials.

For a comprehensive treatment of the surveillance testing regulatory landscape during COVID-19 — including the Seattle Flu Study/SCAN case study, school-based surveillance controversies (SafeGuard/New Trier), and the post-PHE transition to wastewater and genomic surveillance — see the AI-generated report: `_AI_Covid_Surveillance_Testing_Screening_Report`.


## Commentary
### Navigating the Surveillance Framework
Surveillance testing was a regulatory gray area, and operating FloodLAMP's testing programs under this framework was a significant challenge. At the same time, the surveillance designation provided meaningful flexibility.

### Communicating Results Without Giving "Results"
The central operational challenge was adhering to the requirement that surveillance programs not deliver "individual patient results." FloodLAMP's approach was to take the FDA's and CMS's language literally: when a sample indicated the presence of SARS-CoV-2, participants were told only that they were "referred to follow-up clinical testing." FloodLAMP did not tell participants they were positive or negative, and the company emphasized this distinction and terminology with program administrators.

This approach was informed by what happened at other programs. The CMS notice letter in this archive (December 2020) was sent to surveillance program operators instructing them to stop using the language "results of potential clinical significance." It was FloodLAMP's understanding, received secondhand, that this terminology had been adopted by operators attempting to comply while still communicating something to participants. In practice, everyone involved — operators, participants, and regulators — likely understood that phrasing to mean the surveillance test was positive. FloodLAMP chose to use the FDA's language, and a "referral to follow-up (clinical) testing" along with the explanation that we were not allowed to give "positive/negative" results to individual participants. The resulting communication was initially confusing for participants and program admins, but after a few repetitions, they understood. This kind of linguistic dance does not serve the public interest during a pandemic.

### The Fundamental Regulatory Gap
The core problem was that the FDA did not distinguish between two very different kinds of "individual decisions." On one hand, there are clinical medical decisions: using a test result as a diagnosis and relying on it for treatment. On the other hand, there are public health mitigation decisions such as going home from school or work, isolating from family members, and getting a follow-up diagnostic test. In FloodLAMP's programs, the individual actions triggered by surveillance testing were of the second kind — participants went home, isolated, and in nearly all cases obtained confirmatory clinical testing (antigen, PCR, or both).

A better framework for pandemic screening would require that public health screening programs mandate follow-up confirmatory testing for flagged participants and that participants report those results back to the program. This would serve two purposes: providing the comparison data needed to evaluate the screening program's performance, and codifying the principle that screening test results should not be the basis for medical decisions.

### The Coral Springs Experience
The uncertain regulatory status of surveillance nearly prevented FloodLAMP's first major program from proceeding. The Coral Springs pilot covered municipal staff and first responders in a city of approximately 140,000 people and represented FloodLAMP's first significant commercial engagement. The city attorney raised concerns requiring due diligence on the surveillance framework. FloodLAMP was not fully informed of the internal discussions but provided supporting documentation, such as that in the `FloodLAMP Surveillance FAQ and Links (June 2022 DRAFT)` file. The matter reportedly came to a head in a meeting involving city officials, the medical director, regulators (from both FDA and CMS), and at least one elected representative (state or federal level, we do not know). The outcome was a "green light" for the program, though FloodLAMP never received any correspondence about that from CMS or the FDA. (For more on the Coral Springs pilot, see the `pilots/pilot-data` subcategory.)

### Surveillance as a Fallback
Operating under the surveillance framework was not FloodLAMP's first choice — it was a fallback. The company had submitted its test to the FDA for Emergency Use Authorization as an open-source protocol in the model of SalivaDirect (see `regulatory/open-euas`), and had applied to the RADx program, but could not secure authorization, engagement, or even substantive attention through either channel. The opportunity to operate surveillance programs came about through our contact with EMS leadership and the FTFC conference in South Florida in mid 2021, where we offered pooled testing and made a presentation. One of the key executives at FloodLAMP had prior experience with surveillance and relationships with other operators of surveillance programs. That combined with the pull we were getting from the EMS community, who simply needed better, more effective testing/screening for their critical first responders, led us to do the FloodLAMP surveillance "pilot programs". These programs were very effective for the organizations that implemented them.

The primary commentary on FloodLAMP's regulatory experience, including EUA submissions and FDA correspondence, is in the `regulatory/open-euas` subcategory.
