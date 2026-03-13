METADATA
last updated: 2026-03-12_081655
file_name: _archive-combined-files_fda-townhalls_145k.md
category: regulatory
subcategory: fda-townhalls
gfile_url: **FLAGGED - TBD user-facing Google-hosted public file URL**
words: 113301
tokens: 145521


CONTENT

# _archive-combined-files_fda-townhalls_145k (4 files, 145,496 tokens)

# 2,798  _AI_FDA_Internal_AI_Use_Report.md
METADATA
last updated: 2026-03-01 AI
file_name: _AI_FDA_Internal_AI_Use_Report.md
file_date: 2026-03-01
title: FloodLAMP FDA Internal Use of AI -- Developments in Using AI to Improve Review Speed, Quality, and Consistency
category: regulatory
subcategory: fda-townhalls
tags: fda, ai, internal-ai, review-process, elsa, genai
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1z6_Z0zlMd66pUrHBCy9MnIALQpicI2BO4LWhxMIV5jw
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/regulatory/fda-townhalls/_AI_FDA_Internal_AI_Use_Report.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 2798
words: 1711
notes: Created by Claude (claude-4.6-opus) during archive preparation. **NOT HUMAN VERIFIED - MAY CONTAIN ERRORS** Report on FDA's internal adoption of AI/GenAI tools to improve review speed, quality, and consistency. Derived by extracting and refocusing the internal-use content (Track B) from a broader AI+FDA diagnostics report originally produced by an external AI tool. Key sources include FDA press releases on the AI review pilot and Elsa launch, and the CDRH 2025 Annual Report.
summary_short: Report on FDA's internal adoption of generative AI tools -- including the "Elsa" platform and the 2025 AI-assisted scientific review pilot -- to improve the speed, quality, and consistency of regulatory review workflows across CDRH and other centers. Covers stated capabilities, data separation commitments, transparency gaps, and implications for regulated industry.


CONTENT

## 1) Executive Summary
FDA has moved from exploratory interest in internal AI to concrete deployment. In May 2025, FDA announced completion of its first **AI-assisted scientific review pilot** and directed all centers to integrate internal AI by June 30, 2025. One month later, FDA launched **Elsa**, an agency-wide generative AI tool built in a secure GovCloud environment, with stated use cases ranging from accelerating clinical protocol reviews to summarizing adverse events. CDRH (the device center responsible for diagnostics/IVD oversight) has confirmed it is using Elsa to streamline routine tasks.

**What this means for regulated industry:**
- FDA is actively investing in tools to reduce reviewer "busywork" and speed up scientific evaluations, which could translate into faster review timelines and more consistent outputs.
- The stated guardrail -- that models do not train on data submitted by regulated industry -- is an early signal about how FDA intends to manage data separation concerns.
- Detailed center-by-center SOPs for how internal AI changes actual review workflows have not yet been published, so the impact on submission strategy remains indirect for now -- but worth monitoring closely.

---

## 2) Background: Where Internal AI Fits in FDA's Structure

### 2.1 Agency-wide scope
The internal AI initiative is not limited to a single center. FDA's announcements describe an **agency-wide** rollout with a common, secure generative AI system integrated with FDA's internal data platforms. This means the initiative spans CDRH (devices/diagnostics), CBER (biologics), CDER (drugs), and other centers.[^fda_ai_rollout_may2025]

### 2.2 CDRH / OHT7 (diagnostics/IVD relevance)
Within CDRH, **OHT7 (Office of In Vitro Diagnostics)** handles premarket review (510(k), De Novo, PMA, IDE), compliance, quality, and surveillance for IVDs. OHT7 includes a division (**DPOM**) specifically focused on developing and implementing policy and processes to ensure *quality and consistency across regulatory submission programs* -- i.e., the exact kind of operational work where internal AI could have significant impact.[^oht7]

### 2.3 The Diagnostic Data Program and interdisciplinary review
FDA's Diagnostic Data Program notes that IVD submissions increasingly combine assay + hardware + software/digital applications, requiring interdisciplinary review to "manage and expedite the review processes." Internal AI tools could help manage this increasing complexity by assisting reviewers in cross-referencing standards, summarizing multi-domain submissions, and maintaining consistency across interdisciplinary teams.[^ddp_otc_poc]

---

## 3) The AI-Assisted Scientific Review Pilot (completed May 2025)

### 3.1 What was announced
On **May 8, 2025**, FDA issued a press release announcing:
- Completion of its **first AI-assisted scientific review pilot**
- A directive for all FDA centers to deploy internal AI
- A target of **full integration by June 30, 2025** on a "common, secure generative AI system integrated with FDA's internal data platforms"[^fda_ai_rollout_may2025]

### 3.2 What is not yet public
FDA has not published detailed findings from the pilot -- e.g., which review types were tested, what metrics were used (time savings, accuracy, consistency), or what the pilot revealed about limitations. The press release frames it as a milestone justifying broader rollout rather than providing a detailed evaluation report.

---

## 4) "Elsa" -- FDA's Internal Generative AI Tool

### 4.1 Launch and architecture
On **June 2, 2025**, FDA announced the launch of **Elsa**, described as an agency-wide internal GenAI tool built in a **high-security GovCloud environment**. The tool is designed to help employees "from scientific reviewers to investigators" work more efficiently.[^fda_elsa_jun2025]

### 4.2 Stated capabilities and use cases
FDA's press release specifically lists these current and planned functions:
- **Accelerating clinical protocol reviews** -- helping reviewers process and evaluate clinical study protocols faster
- **Shortening time for scientific evaluations** -- reducing the time reviewers spend on analytical and scientific assessment tasks
- **Summarizing adverse events** -- automating the distillation of adverse event reports into usable summaries
- **Performing label comparisons** -- comparing product labeling across submissions or against standards
- **Generating code for databases** -- assisting with technical/data infrastructure tasks
- **Planned future integration** into additional processes like data processing[^fda_elsa_jun2025]

### 4.3 Data separation guardrail
FDA states explicitly that **models do not train on data submitted by regulated industry**. This is a significant public commitment regarding data handling and suggests FDA is aware of the sensitivity around using industry-submitted proprietary data in AI training.[^fda_elsa_jun2025]

### 4.4 Secure platform for internal documents
Elsa provides a secure platform to access FDA's internal documents, meaning reviewers can use it to search, summarize, and cross-reference internal guidance, precedent decisions, and institutional knowledge -- potentially improving consistency across reviewers and divisions.[^fda_elsa_jun2025]

---

## 5) Evidence of CDRH Adoption

### 5.1 CDRH Annual Report 2025
CDRH's 2025 annual report confirms the device center is advancing use of new digital tools, "like Elsa, a generative AI tool," to help staff streamline routine tasks. This is the most direct public confirmation that Elsa is being used within the center responsible for device and IVD review.[^cdrh_annual_report_2025]

### 5.2 Implications for diagnostics review workflows
While no CDRH-specific SOPs or workflow changes have been published, the combination of:
- Elsa's stated capabilities (protocol review acceleration, scientific evaluation support, label comparisons)
- CDRH's confirmation of adoption
- OHT7's existing focus on process quality and consistency (via DPOM)

...suggests internal AI is likely touching or will soon touch IVD submission review workflows in some capacity -- even if the details remain opaque.

---

## 6) What Is Not Yet Publicly Detailed (Gaps in Transparency)
As of this report date, FDA has **not** published granular documentation describing:

| Gap | Why it matters |
| --- | --- |
| Center-specific SOPs for AI-assisted review | No visibility into exactly how AI changes the review process for a 510(k) vs. De Novo vs. PMA in CDRH/OHT7 |
| Whether AI outputs serve as decision support vs. purely administrative support | Significant difference between "AI drafts a deficiency letter" and "AI helps format a summary" |
| How submission triage may be affected | AI could change how submissions are prioritized, routed, or initially categorized |
| Template generation and deficiency letter drafting | These are high-volume, pattern-driven tasks well-suited to AI -- but no public confirmation of use here |
| Quality assurance / validation of AI-assisted reviewer outputs | No public information on how FDA validates that internal AI tools produce accurate, consistent, unbiased outputs |
| Metrics from the review pilot | Time savings, error rates, reviewer satisfaction -- none published |
|||

---

## 7) Practical Implications for Regulated Industry

### 7.1 Near-term: operational speed, not evidentiary standard changes
The most likely near-term impact is **operational** -- faster summarization, comparisons, and drafting support for reviewers. Changes to formal evidentiary standards or review criteria would normally require guidance or policy updates, which have not been announced in connection with internal AI.[^fda_elsa_jun2025]

### 7.2 Consistency improvements
If internal AI is being used to cross-reference precedent, compare labeling, and surface relevant guidance, it could lead to **more consistent** review outcomes across divisions and reviewers -- reducing the variability that sponsors sometimes experience between different review teams.

### 7.3 Faster review cycles (potential)
Acceleration of clinical protocol reviews and scientific evaluations, as stated by FDA, could translate into shorter review clocks -- particularly for the labor-intensive aspects of review (literature review, comparator analysis, adverse event assessment, standards cross-referencing).

### 7.4 New questions for sponsors to consider
- **Submission formatting:** If FDA reviewers are using AI to parse and summarize submissions, well-structured, machine-readable submissions may be processed more efficiently.
- **Consistency of FDA outputs:** Watch for whether AI-assisted review leads to more standardized deficiency letters, review memos, or decision language.
- **Data separation:** FDA's claim that models don't train on submitted data is worth monitoring -- any change in this policy would have significant implications for trade secret and confidential commercial information.

---

## 8) Timeline of Key Internal AI Developments at FDA

| Date | Event | Significance |
| --- | --- | --- |
| May 8, 2025 | FDA announces completion of first AI-assisted scientific review pilot and agency-wide rollout directive | First public confirmation of a concrete internal AI pilot; sets June 30, 2025 integration target |
| Jun 2, 2025 | FDA launches "Elsa" (agency-wide internal GenAI tool) | Named tool with specific stated use cases; GovCloud architecture; data separation commitment |
| Jun 30, 2025 | Target date for full AI integration across all FDA centers | Deadline set in May 2025 announcement |
| 2025 (annual report) | CDRH confirms using Elsa to streamline routine tasks | Direct evidence of adoption within the device/diagnostics center |
||||

---

## 9) What to Monitor Next
1. **Any FDA publications describing outcomes of the review pilot** -- metrics, lessons learned, expansion plans.
2. **CDRH-specific announcements about AI in review workflows** -- particularly any changes to review SOPs, triage processes, or reviewer tools that are made public.
3. **Policy or guidance updates linked to internal AI adoption** -- if FDA's use of AI internally leads to changes in what they expect from submissions (e.g., structured data requirements, machine-readable formats).
4. **Data handling policy evolution** -- any updates to the "models do not train on submitted data" commitment, especially as AI capabilities expand.
5. **Congressional or GAO oversight** -- internal AI adoption at a regulatory agency may attract legislative or audit interest, which could produce additional public documentation about how AI is being used.
6. **MDUFA/user fee negotiations** -- if AI-driven efficiencies affect review timelines, this could surface in user fee performance goal discussions.

---

## Source Index (URLs)
- FDA press release (AI review pilot + rollout, May 8, 2025): https://www.fda.gov/news-events/press-announcements/fda-announces-completion-first-ai-assisted-scientific-review-pilot-and-aggressive-agency-wide-ai
- FDA press release (Elsa launch, June 2, 2025): https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people
- CDRH Annual Report 2025 PDF: https://www.fda.gov/media/190779/download
- OHT7 office page (IVD org + divisions + TPLC responsibilities): https://www.fda.gov/about-fda/cdrh-offices/oht7-office-in-vitro-diagnostics-office-product-evaluation-and-quality
- Diagnostic Data Program (OTC/POC digital diagnostics, interdisciplinary review): https://www.fda.gov/medical-devices/diagnostic-data-program/digital-diagnostics-over-counter-otc-and-point-care-poc

---

## Footnotes
[^fda_ai_rollout_may2025]: FDA press release announcing completion of first AI-assisted scientific review pilot and agency-wide rollout timeline (May 8, 2025): https://www.fda.gov/news-events/press-announcements/fda-announces-completion-first-ai-assisted-scientific-review-pilot-and-aggressive-agency-wide-ai
[^fda_elsa_jun2025]: FDA press release launching "Elsa" internal GenAI tool and describing use cases and training/data claims (June 2, 2025): https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people
[^cdrh_annual_report_2025]: CDRH Annual Report 2025 (mentions Elsa use; includes AI-related activities): https://www.fda.gov/media/190779/download
[^oht7]: FDA OHT7 (Office of In Vitro Diagnostics) page describing TPLC responsibilities and divisions (DCTD, DIHD, DMD, DMGP, DPOM): https://www.fda.gov/about-fda/cdrh-offices/oht7-office-in-vitro-diagnostics-office-product-evaluation-and-quality
[^ddp_otc_poc]: FDA Diagnostic Data Program page on digital diagnostics (OTC/POC), convergence of IVDs with software/digital apps, and interdisciplinary review: https://www.fda.gov/medical-devices/diagnostic-data-program/digital-diagnostics-over-counter-otc-and-point-care-poc


# 26,646  _AI_FDA_Townhall_Analysis_of_Refusals_and_Legitimacy.md
METADATA
last updated: 2026-02-26 AI
file_name: _AI_FDA_Townhall_Analysis_of_Refusals_and_Legitimacy.md
file_date: 2026-03-05
title: FloodLAMP FDA Town Hall Refusals to Answer -- Legitimacy Analysis
category: regulatory
subcategory: fda-townhalls
tags: fda, townhalls, refusals, legitimacy, transparency, accountability
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1rrsMpiCYggp_lBAYkGLRwybjXNdQxiEKWaf_5Gc1oIQ
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/regulatory/fda-townhalls/_AI_FDA_Townhall_Analysis_of_Refusals_and_Legitimacy.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 26646
words: 18602
notes: Created by Claude Opus 4.6 during archive preparation. **NOT HUMAN VERIFIED - MAY CONTAIN ERRORS** Critical analysis of FDA's refusal to answer questions during COVID-19 Diagnostic Virtual Town Hall series (~100 sessions, March 2020 through early 2023), including a legitimacy rubric, classification and scoring of 116 identified refusal instances, and summary statistics. Section 1 (critical analysis) substantively authored by Randy True via voice dictation; Sections 2-4 produced collaboratively between the author and the model. Instance-level classifications in Section 3 were generated by heuristic code, not model evaluation, and are not individually audited. Based on section-titles transcript files. Companion file: _compilation_fda-refusals-to-answer.md.
summary_short: Critical analysis of the FDA's systematic refusal to answer questions during ~100 COVID-19 Diagnostic Virtual Town Hall sessions (2020-2023), covering the "specific submissions" policy's impact on transparency and accountability. Includes a legitimacy rubric, classification and scoring of all 116 identified refusal instances, and summary statistics showing an average legitimacy score of 2.7/5 for active refusals, with 48% scoring "Questionable" or worse.


CONTENT

## Prompt (Verbatim)
[Original voice-dictated prompts not preserved. This document was produced through a multi-turn, voice-prompted interaction with Claude Opus 4.6 within Cursor. See the Methodology Disclaimer at the top of the response body for a detailed description of the creation process for each section.]

**Files included in context window:**
- ~100 section-titles transcript files from the FDA COVID-19 Diagnostic Virtual Town Hall series (2020-2023)
- _compilation_fda-refusals-to-answer.md

## Prompt (Cleaned)
[Original prompts not individually preserved. The document was produced in a multi-turn collaborative session: (1) Section 1 arguments, factual claims, framing, and examples were provided by Randy True (FloodLAMP founder/CEO) through voice dictation; (2) Section 2 rubric was developed collaboratively between the author and the model; (3) Section 3 classification was generated by a Python script using regex and heuristic rules written and executed by the model; (4) Section 4 summarizes the classification output. See the Methodology Disclaimer for full details.]

**Files included in context window:**
- ~100 section-titles transcript files from the FDA COVID-19 Diagnostic Virtual Town Hall series (2020-2023)
- _compilation_fda-refusals-to-answer.md

## FDA Town Hall Refusals to Answer: Legitimacy Analysis

This document presents a critical analysis of the FDA's refusal to answer questions during
the COVID-19 Diagnostic Virtual Town Hall series (~100 sessions, March 2020 through early 2023),
including a legitimacy rubric, classification and scoring of all identified instances, and a summary of results.

### Methodology Disclaimer — Read Before Citing

**This document is an unaudited demonstration, not a human/peer-reviewed analysis. The classifications and scores in Sections 3 and 4 should be treated as provisional and likely contain a significant fraction of errors.**

This analysis was produced through a rapid, voice-prompted interaction with Claude Opus 4.6 (Anthropic's agentic reasoning model) within Cursor, an AI-assisted IDE. The process worked as follows:

- **Section 1 (Critical Analysis):** The arguments, factual claims, framing, and specific examples were provided by the author (Randy True, FloodLAMP founder and CEO during the pandemic) through voice dictation. The model produced the written text based on these prompts. The author reviewed and directed revisions but did not line-edit the full output.
- **Section 2 (Rubric):** The rubric categories and scoring definitions were developed collaboratively between the author and the model.
- **Section 3 (Classification and Scoring):** The model wrote and executed a Python script that used regex pattern matching and heuristic rules to classify each of the 116 identified refusal instances. This was not done through structured-output prompting with a frontier reasoning model — it was code-based classification using keyword and context heuristics. The classification logic was reviewed at a high level but the individual instance-level outputs were not audited.
- **Section 4 (Summary):** The summary statistics are accurate reflections of the classification output in Section 3, but inherit whatever errors exist in that classification.
- **The compilation of raw refusal passages** (in the companion file `_compilation_fda-refusals-to-answer.md`) was extracted by a separate script using the same regex patterns and is likely fairly reliable — the author scanned those results and found them to be generally accurate.

**What this analysis does well:** The critical essay in Section 1 reflects the author's direct experience as a diagnostic test developer during the pandemic and is substantively authored content. The rubric in Section 2 is a reasonable framework for evaluating refusal legitimacy. The overall patterns identified in Section 4 (dominance of boilerplate disclaimers, low average legitimacy scores for active refusals, prevalence of email deflection) are likely directionally correct.

**What this analysis does not do well:** The instance-level classification in Section 3 was performed by heuristic code, not by a reasoning model evaluating each instance in context. Some classifications are likely wrong — the heuristics may misread the tone or substance of an exchange, misclassify a partial answer as a deflection, or fail to detect that a useful general answer was provided alongside a refusal. The excerpts were extracted programmatically (300 characters on either side of the regex match) and may not capture the most relevant context for each instance.

**How this should ideally be done:** A more rigorous approach would involve:
1. Developing a structured-output prompt with defined fields (category, score, rationale, key excerpt, speaker) for each refusal instance.
2. Tuning and evaluating that prompt against a human-scored sample of 20–30 instances.
3. Running the prompt with a high-quality frontier reasoning model (e.g., Claude Opus, GPT-4o, Gemini 2.5 Pro) across all identified instances, potentially comparing results across models.
4. Performing human evaluation of a random sample of the model's output to measure agreement and identify systematic errors.
5. Iterating on the prompt based on error analysis.

This level of rigor is achievable with current tools and would produce a substantially more reliable analysis. The rapid demonstration here is sufficient to illustrate the patterns and to motivate the effort, but it should not be cited as if the individual instance-level scores are reliable.

**What this demonstrates about AI capability:** This entire analysis — the extraction of 116 refusal instances from 100 transcript files, the development of a classification rubric, the coding and execution of a classification script, the generation of a 1,100+ line analytical document, and multiple rounds of revision incorporating the author's voice-dictated feedback — was produced in a single working session using an agentic AI model. This work was performed directly against the `section-titles` transcript files and did not use the QA extraction files or the QRAG retrieval tool. Current agentic models can develop code, execute it in sandboxed environments, read and process large file sets, and produce analytical documents of this scope — but they do not yet reliably implement the structured-prompt-and-evaluate loop described above without explicit human direction. The gap between what was done here (rapid heuristic classification) and what could be done (prompt-tuned, model-evaluated, human-audited classification) represents the current frontier of AI-assisted analysis (consumer-grade and widely available), and closing that gap is maybe a weekend project for someone with experience with code and AI/LLM projects.

---

## 1. Critical Analysis: "We Are Not Able to Respond to Questions About Specific Submissions"

### The Standard Language
Across nearly every one of the ~100 FDA Virtual Town Halls for COVID-19 diagnostic test developers, the moderator opened with a variation of:

> "Please remember that during this Town Hall, we are not able to respond to questions about specific submissions that might be under review."

This language became the default framing for all engagement. It was not presented as a circumstantial limitation but as a blanket policy. And it shaped the entire dynamic of these calls: developers learned quickly that any question touching on their own submission would be deflected, regardless of the nature of the question or the willingness of the developer to waive any confidentiality concerns.

### What Does the FDA Actually Mean?
The stated justification for this policy was confidentiality — that submission details are proprietary and the FDA cannot disclose them on a public call. But this framing obscures what is actually happening in the majority of cases. Consider the participants:

- Almost everyone calling in is either preparing to submit, has submitted, or is actively engaged with the FDA on a COVID-19 diagnostic test EUA.
- When a developer asks a question about their *own* submission on a public call, they are voluntarily disclosing whatever details they choose. There is no third-party confidentiality to protect.
- The FDA's concern about confidentiality is therefore not about protecting the *caller* — it is about protecting the FDA's own discretion over what it says, when, and to whom.

If we strip away the confidentiality framing, the most charitable interpretation of what the FDA is actually saying is:

> "We cannot look up your submission in our systems during this live call, review the details, and give you a case-specific answer on the spot. We can only answer from general knowledge and established policy."

That is a *reasonable operational limitation*. It would be unreasonable to expect Tim Stenzel or Toby Lowe to pull up a submission file during a live town hall and conduct an ad hoc review. No one disputes that.

### The Problem: Refusal Instead of Generalization
The critical failure is not the limitation itself — it is what the FDA chose to do with it. When a developer asked a specific question, the FDA had two options:

1. **Generalize and answer**: Reframe the question as a general policy or process question and provide the closest applicable answer. This is what subject matter experts do in every other public-facing context (or _should_ do).
2. **Refuse and deflect**: Invoke the "specific submissions" language, provide no substantive guidance, and redirect the caller to a private email or the pre-EUA process where they are not publicly accountable for their response..

The FDA chose option 2 far more often than necessary. In many instances, the Director of the Office of In Vitro Diagnostics — one of the most qualified people in the world to answer these questions — was sitting on the call, understood the general policy perfectly well, and could have provided a useful general answer. Instead, the caller was told to "reach out to the templates email address" and wait days or weeks for a response that might or might not come.

It is important to recognize who these callers were and why they were calling in to a public forum. These were diagnostic test developers — scientists, regulatory affairs professionals, and company leaders who understood the FDA's processes and knew that they could submit questions in writing through pre-EUA submissions, Q-subs (question submissions), or the templates email address. They chose to ask on a public call for reasons that the "send it in writing" redirect systematically undermined:

- **Timeliness.** Written submissions to the FDA could take weeks or months to receive a response. During a pandemic where delays cost lives, waiting weeks for guidance on a validation question was not a neutral outcome. A developer on the call could get an answer in real time — if the FDA chose to give one.
- **Public accountability.** A question asked and answered on a recorded call with hundreds of listeners becomes part of the public record. Other developers with similar questions benefit from the answer. And the FDA is accountable for the consistency of its answer because anyone can compare it to what was said on previous calls. A private email response has none of these properties.
- **Signal of importance.** Calling in to a live town hall, identifying yourself, and asking a question publicly was a signal that the issue mattered and that the developer wanted the broader community to hear the FDA's position.

There is a legitimate use for the email redirect: when a question genuinely requires case-specific review that cannot be done live, directing the developer to a channel where that review can happen is reasonable — provided the FDA actually follows through in a timely manner. But the transcripts show that the redirect was used routinely for questions that did not require case-specific review, as a blanket deflection that moved questions out of the public forum and into private, unaccountable channels. The later town halls formalized this further, pre-screening emailed questions before the call and declining to address any deemed "too detailed or case-specific" — a category that appeared to expand over time.

### The Effect on Transparency and Accountability
The "specific submissions" policy had several compounding effects:

- **Public accountability was removed.** When a question is answered on a recorded public call, the answer is on the record. When it is redirected to a private email exchange, there is no public record, no consistency check, and no accountability.
- **Inconsistency was hidden.** If the FDA's answer to Developer A differs from its answer to Developer B on the same policy question, the public call format would expose that. The email redirect ensures it never comes to light.
- **Developers were trained not to ask.** Over 100 sessions, developers internalized the refusal pattern. The quality and specificity of questions declined over time, not because developers had fewer questions, but because they learned there was no point in asking.
- **The appearance of engagement substituted for actual engagement.** The town halls allowed the FDA to claim it was holding regular, open sessions with the developer community. But if the most pressing questions are systematically deflected, the engagement is performative.

### The Chilling Effect: Retaliation Risk and Structural Silencing
There is a deeper dimension to this pattern that the transcripts cannot directly show, but that anyone who operated in the COVID-19 diagnostics space understood: **the people best positioned to criticize the FDA's process were the people most vulnerable to retaliation by the FDA.**

The diagnostics industry is entirely dependent on FDA authorization. A company cannot sell a test without it. A CEO who publicly criticized the FDA's review process, questioned the consistency of its decisions, or challenged a refusal on one of these town halls was not engaging in normal public discourse — they were risking their company's relationship with the one entity that controlled whether their product could exist in the market. The consequences were not hypothetical:

- The FDA had complete discretion over review timelines. A submission could be prioritized or deprioritized with no public justification.
- The FDA had complete discretion over the depth of review. A submission could receive one round of questions or five, with no external check on whether the additional scrutiny was warranted.
- The FDA had discretion over informal guidance. A developer who maintained a cooperative relationship might receive a helpful pre-EUA call; one who had been publicly critical might receive a form response pointing to the templates.
- The consequences extended beyond any single company. A CEO perceived as antagonistic to the FDA could find their professional reputation in the field damaged — not through any formal action, but through the informal networks that connect regulators, reviewers, and the companies that depend on them. In a field this specialized, being blackballed by the FDA is not a setback — it is a career-ending event.
- For smaller companies, even a delay — not a rejection, just a delay — could be existential. Diagnostic startups burning cash on R&D and manufacturing scale-up cannot survive indefinitely without revenue, and revenue requires authorization. The case of Lucira Health illustrates this starkly: Lucira developed the first at-home combination COVID-19 and flu test, anticipated FDA authorization by August 2022, and spent through its reserves waiting. The FDA finally issued the EUA on February 27, 2023 — five days after Lucira filed for Chapter 11 bankruptcy protection. The company that built one of the most innovative diagnostic products of the pandemic was destroyed not by the market but by the timeline of regulatory authorization. (Sources: FDA CDRH Statement on EUA of Lucira Health's COVID-19 & Flu Home Test, Feb. 2023; GlobeNewsWire, Lucira Health press releases, Feb. 22 and Feb. 27, 2023.)

None of this is provable in individual cases, and that is precisely the point. The system was structured so that inconsistency, favoritism, and retaliation were *impossible to detect from the outside*. Review decisions were made behind closed doors. Rejection reasoning was not published. Comparative timelines across similar submissions were not available. And the one public forum where these issues might surface — the town halls — systematically deflected the questions that would expose them.

The result was a structural silencing of the FDA's most knowledgeable constituency. The developers, scientists, and CEOs who understood the FDA's review process well enough to identify its flaws were the same people who could not afford to say so publicly. The field is so technically specialized that outside observers — journalists, legislators, the general public — lack the expertise to evaluate whether the FDA's review decisions were consistent, timely, or well-reasoned. Only the regulated community had that knowledge, and the regulated community was effectively muzzled by its dependence on the regulator's goodwill.

This dynamic is worth noting in the context of the town hall transcripts specifically: listen to how callers framed their questions. They were deferential, grateful, and careful not to imply criticism. Even when a developer had waited months for a response, or when the FDA's guidance contradicted its own templates, the questions were phrased as requests for clarification rather than challenges. This was not politeness — it was self-preservation. The power asymmetry between the FDA and its regulated community was so complete that even on a public call with hundreds of listeners, no one could afford to say what many of them were thinking.

### The Consistency Problem: No Mechanism for Accountability
It is worth pausing on the specific nature of the consistency concern. Tim Stenzel, the Director of the Office of In Vitro Diagnostics who led these town halls, came to the FDA from industry — he had previously served as head of diagnostics at Quidel, one of the largest diagnostic test manufacturers in the United States. Quidel received several early and notable authorizations during the pandemic, including early point-of-care and screening claims. This is not presented as evidence of impropriety — Quidel is a major company with significant technical capabilities, and early authorizations for large manufacturers may be entirely justified. But it illustrates the structural problem: **there was no mechanism by which anyone could assess whether review decisions were consistent across applicants.**

When a small company waited months for a response while a large company received rapid authorization, there was no public data to determine whether the difference was explained by submission quality, technical merit, review staffing, or something else. The FDA's answer to this concern — as evidenced throughout these transcripts — was to decline to discuss specific submissions. The effect was to make the consistency question permanently unanswerable. And because the people who would have the standing to raise this concern were the same people who depended on the FDA for their livelihood, the question was rarely raised at all.

The performance data problem compounds this. Throughout the EUA process, companies self-reported their own analytical performance data — including their Limit of Detection (LoD), which is the key measure of test sensitivity. Because different developers used different viral materials, sample matrices, and protocols to establish their LoDs, these self-reported figures were not directly comparable across tests. The FDA recognized this and developed its own SARS-CoV-2 Reference Panel: a standardized set of materials sent to all EUA-authorized molecular test developers, with results to be posted publicly. This was the one attempt at independent, standardized, comparative performance evaluation.

The results were revealing. When tests were evaluated against the same reference material, many showed LoDs dramatically different than what appeared in their EUA labeling. The discrepancies were not marginal — some tests showed reference panel LoDs 10x, 100x, or even 1000x worse than their self-reported EUA LoDs. (See: `FDA SARS-CoV-2 Reference Panel Comparative Data`, compiled by Matt McFarlane, archived in this repository.) The response from industry was not to address the discrepancies but to challenge the panel itself. A law firm representing unidentified EUA holders filed a formal complaint under the Information Quality Act in December 2020, demanding that the FDA remove the comparative data from its website, claiming it was "inaccurate and misleading" and that their clients had suffered "direct harm" from having their tests "inaccurately presented as having a low sensitivity." (See: `2023-09-23_FDA Response Letter - To Compliant regarding FDA Reference Panel from Dec 2020`, archived in this repository.)

The FDA's response letter, dated September 29, 2023 — nearly three years later — defended the scientific validity of the reference panel and protocol. But it also noted that the FDA had stopped distributing the panel when the materials expired and had removed the comparative data from its website "as part of its regular review and updating of COVID-related information because that data has become outdated." The one mechanism that existed for independent comparative assessment of test performance was allowed to expire, the data was taken down, and the practice of self-reported, non-comparable performance claims was effectively restored.

This episode is directly relevant to the refusal-to-answer pattern documented in these transcripts. When the FDA says it "cannot discuss specific submissions," one of the things it is not discussing is whether the performance claims in those submissions are consistent with independent evaluation. The reference panel data suggested they often were not. And the constituency that objected loudest to the publication of that data was not the public — it was the regulated industry, which preferred the opacity of self-reported figures to the accountability of standardized comparison. [RT - don't agree with this paragraph]

### The Broader Context: Discretion Without Accountability
This refusal pattern is one small but telling manifestation of a larger structural problem: the FDA operated during the pandemic with enormous discretion over diagnostic test authorization and very little public transparency about how that discretion was exercised. Submissions were reviewed behind closed doors. Rejection reasons were not published. Timeline expectations were vague. And when developers tried to ask about these things on the one public channel available to them, they were told the FDA could not discuss it.

The cost of this opacity was not abstract. Delayed authorizations meant delayed testing. Delayed testing meant undetected infections. Undetected infections meant preventable transmission and preventable deaths. The FDA's role as the sole gatekeeper for diagnostic tests during a pandemic gave it extraordinary power, and the absence of transparency around how that power was exercised was not a minor procedural shortcoming — it was a structural failure with direct public health consequences.

And the constituency that understood this best — the diagnostics developers, the lab directors, the scientists building the tests — could not say so without jeopardizing their own ability to get tests authorized. The retaliation risk described above meant that the FDA's opacity was self-reinforcing: the less transparent the process, the more dependent developers were on maintaining a good relationship with the agency, and the less likely anyone was to demand transparency. It was a closed loop, and it operated largely unchallenged for the duration of the pandemic.

FDA Commissioner Marty Makary's recent decision to publish drug rejection letters reflects an understanding that transparency about *why* a regulatory agency says no is essential to accountability. The same logic applies to diagnostics — arguably more so, given that during a pandemic the stakes of delayed or inconsistent test authorization are measured directly in lives. The principle should extend to every stage of the regulatory process, including the informal, public-facing engagement that these town halls were supposed to provide.

### What Should Have Happened
A more legitimate version of the "specific submissions" policy would have:

1. **Stated the actual limitation honestly**: "We cannot look up your submission during this call, so we will answer from general policy."
2. **Required generalization, not refusal**: FDA staff should have been directed to reframe specific questions as general ones and provide the best available public answer.
3. **Committed to public follow-up**: Questions redirected to email should have been answered in a public FAQ update, not buried in private correspondence.
4. **Distinguished between confidentiality and convenience**: Protecting a third party's submission details is legitimate. Declining to answer a caller's question about their own submission, on a call they chose to join, is not confidentiality — it is discretion.
5. **Published comparative review metrics**: Aggregate data on review timelines, rounds of questions, and outcomes by submission type would allow the developer community and the public to assess whether the FDA's discretion was exercised consistently. Without this data, concerns about favoritism and retaliation are permanently unanswerable — which benefits the FDA and no one else.
6. **Established structural protections against retaliation**: When the regulated community cannot criticize the regulator without risking its livelihood, accountability depends entirely on the regulator's self-discipline. That is not a system — it is an honor code, and it failed during the pandemic.
7. **Created a non-confidential submission pathway**: The FDA has no mechanism by which a developer can elect to make their submission, and the FDA's review correspondence, public. During a global pandemic, many developers — particularly academic laboratories, university research groups, and public health institutions — would have willingly open-sourced their submissions and invited public scrutiny of the review process if such an option existed. This would have allowed independent assessment of review consistency, surfaced best practices across developers, and demonstrated the FDA's reasoning in real time. The absence of this option was not an oversight — it reflected a system designed around the assumption that all regulatory interactions must be confidential, even when the regulated party would prefer transparency.

### Anticipating the Defense
It is important to engage honestly with the strongest version of the FDA's position before concluding that it was inadequate. The best defense of the FDA's conduct during these town halls would include the following arguments:

**"The FDA was operating under unprecedented resource constraints."** This is true. Tim Stenzel himself stated on multiple calls that his virology branch saw a 60-fold increase in workload. Staff were working around the clock. The surge in submissions was genuinely overwhelming, and the FDA added review staff and reorganized teams to address it. Under these conditions, asking reviewers to also prepare public answers to specific questions on live calls would have been an additional burden.

**Response:** Resource constraints explain slow timelines. They do not explain the choice to refuse rather than generalize. Saying "we cannot look up your submission right now, but here is the general policy on that question" requires no additional staff, no database access, and no case-specific review. It requires only a directive to FDA staff that generalization is the expected response to specific questions. The senior FDA officials on these calls — Stenzel, Lowe, and others — had deep enough command of their own policies and templates to do this routinely. They occasionally did (Category C1 instances in the scoring), proving it was possible. The choice not to do it consistently was a policy decision, not a resource constraint.

**"Changing the system mid-pandemic would have caused further delays."** The argument here is that introducing new transparency mechanisms — published review metrics, non-confidential submission pathways, public follow-up to redirected questions — would have required process development, legal review, and IT infrastructure, all of which would have diverted resources from the core mission of reviewing submissions.

**Response:** Some of the reforms described above would indeed require process development. But the most impactful changes were not process changes — they were posture changes. Directing staff to generalize instead of refuse, committing to post redirected questions as FAQs, and publishing aggregate review timeline data are not infrastructure projects. They are leadership decisions that could have been made in a single directive. The FDA did, in fact, update its FAQ page almost weekly based on town hall questions — this infrastructure already existed. The question is why the answers to redirected questions were not added to it.

**"The confidentiality framework exists for good reasons and cannot be selectively applied."** The FDA would argue that treating all submission information as confidential — even when the submitter would waive confidentiality — is necessary to maintain a consistent legal framework. If the FDA began discussing some submissions publicly while keeping others confidential, it might create pressure on developers to waive confidentiality in order to receive more favorable or faster treatment, which could disadvantage companies with legitimate trade-secret concerns.

**Response:** This is the strongest argument, and it has some merit. However, it proves too much. The solution is not to maintain blanket confidentiality at the cost of all accountability — it is to create opt-in mechanisms that give developers the choice. A non-confidential submission pathway, where a developer affirmatively elects public review, preserves the default of confidentiality for those who want it while enabling transparency for those who prefer it. During the pandemic, many academic labs, public health institutions, and mission-driven companies would have enthusiastically opted in. The COVID-19 pandemic prompted an extraordinary outpouring of public-spirited scientific work — researchers publishing preprints at unprecedented speed, sharing protocols openly, collaborating across institutions. A non-confidential submission pathway would have channeled that same energy into the regulatory process, and it would have given the FDA access to something it badly needed: external validation that its review decisions were consistent and well-reasoned.

**"The town halls were never intended to be a review forum."** The FDA would point out that the town halls were designed to provide general updates and address general questions, not to serve as an alternative review channel. Developers who needed case-specific guidance had dedicated pathways: pre-EUA submissions, assigned reviewers, and the templates email.

**Response:** This is correct in its framing and misleading in its implication. No one expected the town halls to replace the formal review process. But the town halls were the only public forum in which the FDA's diagnostic review process was subject to external questioning. They were the closest thing to public accountability that existed for the hundreds of life-and-death authorization decisions being made behind closed doors. To argue that they were "not intended" for substantive questioning is to admit that no public forum for substantive questioning was ever intended — which is the core of the transparency problem.

### The Choice of the Term "Town Hall"
It is worth pausing on the name itself. A town hall — in American civic tradition — is a meeting where constituents confront their representatives, ask hard questions, and expect direct answers. The power dynamic is supposed to flow upward: the officials serve the public and are accountable to it. Elected officials who refuse to answer at a town hall pay a political price. The format exists specifically because accountability requires a forum where the powerful cannot control the terms of engagement.

The FDA's "Virtual Town Hall Meetings" for COVID-19 diagnostic test developers bore the name but inverted the dynamic. Consider what these sessions actually were:

- The FDA controlled the agenda, the opening remarks, the order of questions, and the length of the call.
- The moderator opened every session with a preemptive disclaimer that the FDA would not answer the most substantive category of questions.
- Callers identified themselves by name and affiliation, making themselves visible to the regulator they depended on for authorization.
- In the later sessions, the FDA pre-screened emailed questions before the call, declining to address any it deemed "too detailed or case-specific." The questions that made it to the call were, in effect, curated by the FDA.
- When a caller asked something that touched on their submission, the response was some variation of "we are not able to discuss that." The caller had no recourse — no follow-up, no appeal, no mechanism to compel a public answer.

There are ways in which these sessions did resemble a town hall: they were open to the public, they were recorded and transcribed (though often with multi-week delay), and FDA leadership did show up regularly and provide substantive technical updates. Tim Stenzel and Toby Lowe did provide their time and expertise. The opening remarks on each call contained useful policy updates, and some of the Q&A exchanges — particularly in the earlier sessions — were substantively helpful.

But the core function of a town hall — the part where constituents hold officials accountable by asking questions the officials cannot deflect (or may pay a price for doing so) — was systematically disabled. The "specific submissions" policy, the email redirect, the pre-screening of questions, and the power asymmetry between a regulator and its regulated community all combined to produce something that looked like a town hall and functioned like a press briefing. The FDA spoke; the audience listened; questions were taken at the FDA's discretion and answered at the FDA's discretion; and the most important questions were deferred to private channels where the answers would never be publicly visible.

The choice to call these sessions "town halls" was not accidental. It projected openness, accessibility, and accountability — qualities that the FDA has strong institutional reasons to project, whether or not the underlying reality supports them. In his book *Reputation and Power: Organizational Image and Pharmaceutical Regulation at the FDA* (Princeton University Press, 2010), political scientist Daniel Carpenter argues that the FDA became the world's most powerful regulatory agency not primarily through its legal authority but through the cultivation and maintenance of an *organizational reputation* for competence and vigilance. That reputation — carefully maintained across relationships with Congress, industry, advocacy groups, media, and foreign governments — is both the source of the FDA's extraordinary power and the mechanism by which it insulates itself from challenge. Calling a controlled briefing a "town hall" is a small example of reputation management in action: it frames the interaction on the FDA's terms while borrowing the legitimacy of a format that implies accountability.

This matters beyond the town halls themselves. The FDA regulates approximately 20% of the U.S. economy by some estimates, including food, drugs, biologics, and medical devices. Its decisions on diagnostics alone — the subject of these transcripts — directly determined how many COVID-19 tests were available, how fast they reached the market, and whether innovative approaches were authorized or left to die in review queues. And through a process known as regulatory harmonization, the FDA's standards and decisions propagate globally: other nations' regulatory agencies look to the FDA as the benchmark, adopt its frameworks, and defer to its judgments. A decision made in Silver Spring, Maryland about whether to authorize a diagnostic test does not stay in Silver Spring — it shapes what tests are available to patients worldwide.

Balaji Srinivasan — a Stanford-trained engineer (BS, MS, PhD), co-founder and former CTO of Counsyl (a genomics company that at its peak screened approximately 4% of all U.S. births), former general partner at Andreessen Horowitz, and former CTO of Coinbase — has described regulatory harmonization as "perhaps the single worst thing in the world," referring to the mechanism by which U.S. regulators effectively impose their regulatory framework on the entire global market. ([Source: "FDA is broken: How to fix it," Balaji Srinivasan in conversation with Lex Fridman, YouTube.](https://www.youtube.com/watch?v=awIRM3-9JNc)) This characterization is obviously debatable, but it captures a structural reality that is often invisible to those outside the regulated industries: the FDA's decisions have a monopoly-like reach that extends far beyond its formal jurisdiction. Srinivasan was himself considered for the position of FDA Commissioner in 2017, and his trajectory — from biotech CEO to broader technology leadership — has placed him in a position to be candidly critical of the FDA in a way that most current industry participants cannot afford to be, for exactly the reasons described throughout this analysis.

And that is the closing observation. Look at how the FDA ran its "town hall meetings" for diagnostic test developers during the worst public health crisis in a century. An agency with total discretion over authorization timelines, blanket refusal to answer substantive questions on a public call, no published review metrics, no mechanism for developers to opt into transparent review, and a regulated constituency of scientists and entrepreneurs who stepped up to build — alongside vaccines — the single most important intervention available during the pandemic: testing and screening. Look at the gap between how these sessions were presented and what they actually were. Look at the gap between the accountability the term "town hall" implies and the discretion the FDA actually exercised.

Then consider that this agency's decisions propagate to every country that harmonizes with U.S. regulatory standards. The transparency deficit documented in these 100 transcripts is not a local problem — it is a structural feature of the institution that sets the global standard for how drugs, medical devices, and diagnostic tests (basically all important aspects of healthcare) reach patients.

But this is not a counsel of despair. The reforms are not radical and they are not expensive. EUA and diagnostic test submissions — which by definition must contain sufficient data to support authorization — could be made public by default when they are submitted, with a narrow carve-out for genuinely proprietary information (trade secrets, manufacturing processes) that can be identified and redacted systematically. The FDA's review correspondence, questions, and reasoning could be published alongside each authorization decision, as current reform-minded FDA Commissioner Marty Makary has begun doing for drug rejection letters. Aggregate review metrics — timelines, rounds of review, outcomes by submission type and applicant size — could be openly published. A non-confidential submission pathway could be created for developers who choose full transparency. And AI tools, which the FDA itself is beginning to adopt internally, could be applied to minimize the role of individual discretion in review: flagging inconsistencies across reviewers, standardizing the depth and rigor of review, and making the review process auditable in ways that were not technically feasible even a few years ago.

Transparency, consistency, and accountability are achievable. The technology exists, And with AI, is now at our fingertips. The precedents are being set in other parts of the FDA. What is required is the recognition that the current system — in which the world's most consequential regulatory decisions are made behind closed doors, with no public record of reasoning, no comparative metrics, and a regulated constituency that cannot afford to demand better — is not adequate to the stakes. The pandemic made this visible. The question is whether we act on what it revealed.

---

## 2. Legitimacy Rubric

Each identified refusal instance is classified into one of the following categories and assigned a legitimacy score.

### Classification Categories

| Code | Category | Description |
| --- | --- | --- |
| A | Boilerplate Opening Disclaimer | Standard moderator script read at the opening of nearly every session. Not scored (not an active refusal). |
| B | Third-Party Confidentiality Protection | Someone asking about another company's submission. FDA legitimately cannot disclose. |
| C1 | Declined Specifics / Provided Useful General Guidance | FDA declined the specific question but provided substantive general guidance that partially addresses the underlying issue. |
| C2 | Partial Answer with Redirect | FDA provided some general guidance but redirected the substantive question to email or pre-EUA. |
| D1 | Timeline/Status Deflection with Redirect | Developer asks about submission status or timeline; FDA declines specifics but offers a contact channel. |
| D2 | Timeline/Status Deflection (No Substantive Response) | Developer asks about submission status or timeline; FDA declines with no substantive guidance. |
| E | Deflection to Email (No Substantive Answer) | FDA provides no on-call guidance and redirects entirely to offline channels. |
| E2 | Policy/Process Refusal | FDA declines to engage on a generalizable policy or process question using 'specific submission' language. |
| F1 | Blanket Pre-Filter with Email Redirect | FDA pre-screens emailed questions as 'too detailed or case-specific' and promises written response. |
| F2 | Blanket Pre-Filter (No Redirect) | FDA declines emailed question as 'too detailed' without clear alternative. |
|||

### Legitimacy Scoring (1-5)

| Score | Label | Description |
| --- | --- | --- |
| 5 | Fully Legitimate | True third-party confidentiality protection. FDA cannot and should not disclose. |
| 4 | Largely Legitimate | Question genuinely requires case-specific review; FDA provides useful general guidance as substitute. |
| 3 | Mixed | Question is partially answerable in general terms; FDA provides some guidance but also deflects substantively. Alternatively, FDA pre-filters with a promise of written follow-up. |
| 2 | Questionable | Question is generalizable and touches on policy/process that should be publicly answerable; refusal appears to protect discretion rather than confidentiality. |
| 1 | Not Legitimate | Refusal is used to avoid a question the FDA could and should answer publicly. No substantive alternative is offered. |
|||

---

## 3. Classification and Scoring of All Identified Instances **LIKELY LOTS OF ERRORS**
_see 'Methodology Disclaimer' at the top of this file - the application of the scoring has not been human reviewed or even rigorously developed with AI. It almost certainly has lots of errors. Perhaps majority errors._

**Total instances identified:** 116
**Boilerplate opening disclaimers (Category A):** 51
**Active refusals (scored):** 65

### 3a. Boilerplate Instances (Category A — Not Scored)

The following instances are the standard moderator disclaimer read at the opening of each session. They are catalogued but not scored, as they represent institutional policy rather than active refusals. However, their near-universal presence (appearing in the vast majority of the ~100 sessions) reflects how deeply the refusal-to-engage posture was embedded in the structure of these calls.

| # | File | Section |
| --- | --- | --- |
| 1 | 2020-06-03_Virtual Town Hall 11_section-titles.md | #### 1. FDA Updates on Diagnostic Tests and Safety Issues |
| 2 | 2020-06-10_Virtual Town Hall 12_section-titles.md | #### 1. FDA Updates on COVID-19 Testing Procedures |
| 3 | 2020-06-17_Virtual Town Hall 13_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and EUA Processes |
| 4 | 2020-06-24_Virtual Town Hall 14_section-titles.md | #### 1. FDA Guidance on COVID-19 Testing Updates |
| 5 | 2020-07-01_Virtual Town Hall 15_section-titles.md | #### 1. FDA Updates and Guidance on SARS-CoV-2 Testing |
| 6 | 2020-07-08_Virtual Town Hall 16_section-titles.md | #### 1. Updates on COVID-19 Testing and Device Authorization |
| 7 | 2020-07-15_Virtual Town Hall 17_section-titles.md | #### 1. FDA Updates and Q&A on SARS-CoV-2 Testing |
| 8 | 2020-07-22_Virtual Town Hall 18_section-titles.md | #### 1. FDA Updates on COVID-19 Testing Policies and Guidance |
| 9 | 2020-07-29_Virtual Town Hall 19_section-titles.md | #### 1. FDA Updates on Testing Templates and Validation Strategies |
| 10 | 2020-08-05_Virtual Town Hall 20_section-titles.md | #### 1. FDA Updates on EUA Applications and Pooling Strategies |
| 11 | 2020-08-26_Virtual Town Hall 23_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Guidelines and Templates |
| 12 | 2020-09-02_Virtual Town Hall 24_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Development Guidance |
| 13 | 2020-09-09_Virtual Town Hall 25_section-titles.md | #### 1. FDA Updates on COVID-19 Test Development Progress |
| 14 | 2020-09-16_Virtual Town Hall 26_section-titles.md | #### 1. False Positives and Testing Accuracy in SARS-CoV-2 Diagnostics |
| 15 | 2020-09-23_Virtual Town Hall 27_section-titles.md | #### 1. FDA Virtual Town Hall: SARS-CoV-2 Testing Updates |
| 16 | 2020-09-30_Virtual Town Hall 28_section-titles.md | #### 1. Improving Quality and Efficiency of EUA Submissions |
| 17 | 2020-10-07_Virtual Town Hall 29_section-titles.md | #### 1. Positive Predictive Value Challenges in Low-Prevalence Populations |
| 18 | 2020-10-14_Virtual Town Hall 30_section-titles.md | #### 1. FDA Updates on SARS CoV-2 Testing Guidance |
| 19 | 2020-10-21_Virtual Town Hall 31_section-titles.md | #### 1. Addressing False Positives in COVID-19 Testing Strategies |
| 20 | 2020-10-28_Virtual Town Hall 32_section-titles.md | #### 1. FDA Virtual Town Hall: SARS-CoV-2 Test Updates |
| 21 | 2020-11-04_Virtual Town Hall 33_section-titles.md | #### 1. False Positive Risks in Antigen Test Reporting |
| 22 | 2020-11-18_Virtual Town Hall 34_section-titles.md | #### 1. FDA Updates on COVID-19 Testing Authorization |
| 23 | 2020-12-02_Virtual Town Hall 35_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Developments and Priorities |
| 24 | 2020-12-09_Virtual Town Hall 36_section-titles.md | #### 1. Updates on COVID-19 Testing Developments and Priorities |
| 25 | 2020-12-16_Virtual Town Hall 37_section-titles.md | #### 1. FDA Updates on COVID-19 Testing and Authorization Guidelines |
| 26 | 2021-01-06_Virtual Town Hall 38_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Variant Impact |
| 27 | 2021-01-27_Virtual Town Hall 40_section-titles.md | #### 1. Developing and Validating COVID-19 Tests Amid Mutations |
| 28 | 2021-02-10_Virtual Town Hall 42_section-titles.md | #### 1. FDA Updates and Q&A on SARS-CoV-2 Diagnostics |
| 29 | 2021-02-17_Virtual Town Hall 43_section-titles.md | #### 1. Updates and Guidance on COVID-19 Test Development |
| 30 | 2021-02-24_Virtual Town Hall 44_section-titles.md | #### 1. FDA Updates on COVID-19 Test Guidance and Monitoring |
| 31 | 2021-03-03_Virtual Town Hall 45_section-titles.md | #### 1. FDA Town Hall: SARS-CoV-2 Test Development Updates |
| 32 | 2021-03-10_Virtual Town Hall 46_section-titles.md | #### 1. FDA Updates on At-Home SARS-CoV-2 Test Authorizations |
| 33 | 2021-03-17_Virtual Town Hall 47_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Development and Screening Policies |
| 34 | 2021-03-24_Virtual Town Hall 48_section-titles.md | #### 1. FDA Guidance on SARS-CoV-2 Testing and Validation. |
| 35 | 2021-04-07_Virtual Town Hall 50_section-titles.md | #### 1. FDA Update on COVID-19 Test Authorizations and Validation Guidance |
| 36 | 2021-04-14_Virtual Town Hall 51_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Authorizations |
| 37 | 2021-04-21_Virtual Town Hall 52_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Guidance and Authorizations |
| 38 | 2021-04-28_Virtual Town Hall 53_section-titles.md | #### 1. FDA Webinar on COVID-19 Test Guidance Updates |
| 39 | 2021-05-05_Virtual Town Hall 54_section-titles.md | #### 1. Updates on FDA COVID-19 Test Submissions and Recommendations |
| 40 | 2021-05-12_Virtual Town Hall 55_section-titles.md | #### 1. FDA Updates on COVID-19 Testing and Submissions Priorities |
| 41 | 2021-05-19_Virtual Town Hall 56_section-titles.md | #### 1. FDA Virtual Town Hall: SARS-CoV-2 Testing Updates and Questions |
| 42 | 2021-05-26_Virtual Town Hall 57_section-titles.md | #### 1. Guidance on Validation and Study Design for SARS-CoV-2 Tests |
| 43 | 2021-06-02_Virtual Town Hall 58_section-titles.md | #### 1. Updates on SARS-CoV-2 Test Development and Safety Concerns |
| 44 | 2021-06-09_Virtual Town Hall 59_section-titles.md | #### 1. Updates on SARS-CoV-2 Testing and Mutations Impact |
| 45 | 2021-06-16_Virtual Town Hall 60_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Prioritization |
| 46 | 2021-06-23_Virtual Town Hall 61_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Innovations |
| 47 | 2021-07-14_Virtual Town Hall 63_section-titles.md | #### 1. Updates on SARS-CoV-2 Testing Development Challenges |
| 48 | 2021-07-28_Virtual Town Hall 64_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Validation Efforts |
| 49 | 2021-09-08_Virtual Town Hall 69_section-titles.md | #### 1. COVID-19 Test Development and Authorization Guidelines Presentation |
| 50 | 2021-09-22_Virtual Town Hall 70_section-titles.md | #### 1. Updates on SARS-CoV-2 Testing and EUA Reviews |
| 51 | 2021-10-21_Virtual Town Hall 72_section-titles.md | #### 1. Updates on COVID Test Development and Prioritization Strategies |
|||

**Total boilerplate instances:** 51

### 3b. Active Refusals (Scored)

Each instance below is an active refusal during a Q&A exchange. A snippet of the refusal context is provided, followed by the classification and score.

#### Instance 1: 2020-05-20_Virtual Town Hall 9_section-titles.md
**Section:** #### 9. Concerns About Small Diagnostics Companies and Test Approvals
**Category:** B — Third-Party Confidentiality Protection
**Legitimacy Score:** 5/5 (Fully Legitimate)
**Rationale:** Caller asking about another company's submission. FDA legitimately cannot disclose third-party confidential information.

**Excerpt:**
> panies or…
> 
> Larry Lines:
> You comment on AYGU a second ago which is confusing to me.
> 
> Toby Lowe (FDA IVD Assoc Director):
> No, I don't think we commented anything specific to that company or test driver.
> 
> Larry Lines:
> I understand. You know, I don't want to take up any more time. I feel like you guys won't answer my question specifically. Thank you very much.
> 
> Coordinator (FDA):
> Thank you very much.
> 
> Tim Stenzel (FDA IVD Director):
> [...]

---

#### Instance 2: 2020-05-27_Virtual Town Hall 10_section-titles.md
**Section:** #### 1. FDA Updates on SARS-CoV-2 Testing Policies and FAQs
**Category:** D1 — Timeline/Status Deflection with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** Developer asks about submission timeline or status; FDA declines specifics but offers a contact channel or general process information.

**Excerpt:**
> to update our Web site with some information as soon as possible. Here's another question. Wasn't the FDA required to provide approval within 45 days of submission? Somebody has been waiting a while since studies have shown success. Why is there such a delay when other companies get authorized? We cannot comment on specific submissions. We encourage the sponsor of this submission to reach out to a lead reviewer if they have any concerns. We do make it a priority to review applications that require EUA authorization prior to marketing or prior to offering that kit or that service. And so as long as somebody can offer s

---

#### Instance 3: 2020-05-27_Virtual Town Hall 10_section-titles.md
**Section:** #### 13. FDA Emergency Policies on Test Kit Approvals
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> ement to keep. And there are other provisions that we have or will have made requirements for that are above what we usually consider in an emergency situation. But practically speaking, if we didn't allow some flexibility when it comes to those regulations and compliance with those regulations, we wouldn't be able to address some of the significant needs in an emergency such as this. Toby do you have anything else to add?
> 
> Toby Lowe (FDA IVD Assoc Director):
> Yes, that's correct. It's part of the benefit-risk evaluation under the emergency. And as Tim said we are not waiving all requirements. We do consider whic

---

#### Instance 4: 2020-06-10_Virtual Town Hall 12_section-titles.md
**Section:** #### 11. Antigen Test Availability and Contractual Restrictions Concerns
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> rying to actually do good things for the country in terms of diagnosing disease and you can't get situations where someone is going to lock you into something that, you know, NWX-FDA OC isn't really credible. Three months from now there will be another antigen that might be better and we can't - we wouldn't be able to switch to it legally.
> 
> Tim Stenzel (FDA IVD Director):
> Okay. I certainly hear what you're saying and understand what you're saying and, you know, it's probably best if internally at the Agency we look into this and talk with you further. There's a lot of listeners on this call and, you know, there'

---

#### Instance 5: 2020-07-22_Virtual Town Hall 18_section-titles.md
**Section:** #### 5. EUA Submission Process and Reporting Responsibilities Explained
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> tions, that we can get to that much quicker than two weeks. So you should hopefully get an assignment - a user, reviewer or somebody that you can otherwise contact to get a status update. Hopefully that clarifies that process.
> 
> Elaine Barry:
> Yes it does thank you very much. And in the event that we wouldn't be able to go down that EUA pathway should we just go ahead and, you know, start preparing for an IDE submission?
> 
> Tim Stenzel (FDA IVD Director):
> So an IDE we've typically not been reviewing IDEs for this pandemic. So it would depend on the particular situation. And say you want to use it in a clinical trial

---

#### Instance 6: 2020-10-21_Virtual Town Hall 31_section-titles.md
**Section:** #### 6. Challenges in Validating Rapid Antigen Test Methods
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> that.
> 
> Elliott Millinton:
> Great. Thank you.
> 
> Tim Stenzel (FDA IVD Director):
> And that would be to an alteration to what's recommended. And, you know, over time our thinking can change and we try to remain open. Now that we have a lot more saliva experience the team's thoughts may have changed. I'm not going to speak for them though.
> 
> Elliott Millinton:
> Thank you very much.
> 
> Coordinator (FDA):
> Our next question is from Edward Strong. Go ahead sir. You may go ahead.

---

#### Instance 7: 2020-10-28_Virtual Town Hall 32_section-titles.md
**Section:** #### 5. Equipment and Software Requirements for Reference Panel Validation
**Category:** B — Third-Party Confidentiality Protection
**Legitimacy Score:** 5/5 (Fully Legitimate)
**Rationale:** Caller asking about another company's submission. FDA legitimately cannot disclose third-party confidential information.

**Excerpt:**
> oes - it is reflective of the test that was authorized.
> 
> Gustavo Heteray:
> Oh okay. They have introduced an amendment including the equipment that I have mentioned. But the amendment has not been reviewed. I guess maybe pending the reference panel results?
> 
> Toby Lowe (FDA IVD Assoc Director):
> So I'm not able to answer any questions about a specific test. Generally we do expect the reference panel to be performed using the authorized test. If there is any specific questions about any, you know, an amendment or any authorizations there those should go directly to the review team.
> 
> Gustavo Heteray:
> Okay then we'll

---

#### Instance 8: 2021-02-10_Virtual Town Hall 42_section-titles.md
**Section:** #### 19. Sample Size Requirements for Antibody Test Kit Approvals
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> of 30 participants for prescription-only; then 150 participants, or 100 sessions with some pairs for over-the-counter? Because I've received conflicting emails from the FDA implying that perhaps OTC could be achieved with a sample size as low as 30.
> 
> Toby Lowe (FDA IVD Assoc Director):
> I don't - I can't speak to what exactly will be in that template. Hopefully, we will be able to get it out soon so that we will be able to speak to it more definitively. But if you do have specific questions as you're planning your approach now, you can send them to the mailbox. And if you're having difficulty getting a FDA Townh

---

#### Instance 9: 2021-03-31_Virtual Town Hall 49_section-titles.md
**Section:** #### 1. Updates on SARS-CoV-2 Test Validations and Mutations
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> rector of the Office of In-vitro Diagnostics and Radiological Health from CDRH will provide a brief update. Following their opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall, we are not able to answer or respond to questions about the specific submissions that might be under review. I will now turn the call over the Toby.
> 
> Toby Lowe (FDA IVD Assoc Director):
> Thank you, Kemba and thanks everyone for joining us again this week. I have a couple of updates and I will go through some of the questions

---

#### Instance 10: 2021-03-31_Virtual Town Hall 49_section-titles.md
**Section:** #### 9. Guidance on At-Home Serology Test Development
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> Toby Lowe (FDA IVD Assoc Director):
> Our next question is regarding the development of rapid tests for antigen and antibody. Basically a few questions about at-home serology tests and whether there's a template available. We have not yet published a template for at- home serology tests and we're not able to speak to when or whether there will be one that is published. However, we know that some test developers have received some draft feedback from the review team and that is a good starting point. If you have specific questions about your own validation or study design, you can reach out through the mailbo

---

#### Instance 11: 2021-04-07_Virtual Town Hall 50_section-titles.md
**Section:** #### 2. BioFire De Novo Updates and Submission Guidance
**Category:** D1 — Timeline/Status Deflection with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** Developer asks about submission timeline or status; FDA declines specifics but offers a contact channel or general process information.

**Excerpt:**
> at all of that information is available on our website and it's very helpful for the test developer. So moving along, we have a couple of questions about the BioFire de novo. We do have a question about whether the decision summary for the BioFire will be posted and it will be. We unfortunately are not able to comment on the timeline. We are working on getting that out. I'm sure everyone is aware FDA Webinar that decision summaries for de novo sometimes takes some time to get posted. But we are working to expedite that one. We also briefly discussed just a little bit last week but there's a question about the Bi

---

#### Instance 12: 2021-04-07_Virtual Town Hall 50_section-titles.md
**Section:** #### 3. Asymptomatic Screening and Over-the-Counter Test Authorization Guidelines
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> see your proposal for a serial testing plan and the post- FDA Webinar authorization study in your EUA request. And we would discuss that with you during the review particularly the statistical plan which is what this question is focused on. We would want to go through that with you in detail. So we can't really get into too many details on the specific book on this call because it will be specific to each individual test and each approach that you're looking to take as a test developer to validate your test. And then along the same lines with serial screening using that supplemental template, we have some question

---

#### Instance 13: 2021-05-12_Virtual Town Hall 55_section-titles.md
**Section:** #### 13. Defining High Throughput and Testing Prioritization Criteria
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> Tim Stenzel (FDA IVD Director):
> Yes so again we're looking at access. And so it does - it's home, it's point- of-care or it's high throughput. It really needs to pass those bars right now first, those thresholds. Having a great neutralizing antibody assay that can't really help that many people is not going to address the country's needs right now. So we are, you know, this is - you know, these priorities are out there for clear reasons. One is to inform developers of what we're not prioritizing. And it also is to hopefully stimulate developers to develop the tests that are really needed at this stage of the pan

---

#### Instance 14: 2021-05-19_Virtual Town Hall 56_section-titles.md
**Section:** #### 5. Validation and Approval for Home Use Antibody Tests
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> Toby Lowe (FDA IVD Assoc Director):
> The next question that we have is about home use antibody tests and asking specific questions about the validation and prioritization. So, unfortunately since we have not yet finalized a template for COVID-19 serology home use self-testing, we're not able to comment further at this time on specific validation study recommendations. And we would recommend that you reach out through a pre-EUA or if you would like to pursue a de novo or 510k through a pre-submission to further discuss your approach.

---

#### Instance 15: 2021-06-30_Virtual Town Hall 62_section-titles.md
**Section:** #### 1. Developing and Validating SARS-CoV-2 Diagnostic Tests: Updates and Guidance
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> ector of the Office of in Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to development and the validation of tests for SARS- CoV-2. Please remember that during the town hall, we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.
> 
> Toby Lowe (FDA IVD Assoc Director):
> Thanks, Irene. Thanks, everyone, as usual, for joining us this week. I have a couple of updates, and then I will go through some of the questions that we received by email

---

#### Instance 16: 2021-08-04_Virtual Town Hall 65_section-titles.md
**Section:** #### 1. FDA Updates on EUA Tests and Prioritization Policies
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> of In Vitro Diagnostics and Radiological Health, and Dr. Kristian Roth, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to development and validation of tests for SARS-CoV-2. Please remember that, during this town hall, we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.
> 
> Toby Lowe (FDA IVD Assoc Director):
> Thank you. Thanks, everyone, for joining us again this week. I don't have much in the way of updates today. But I did want to point out, I think Tim mentioned last week, th

---

#### Instance 17: 2021-08-04_Virtual Town Hall 65_section-titles.md
**Section:** #### 3. Prioritization of Multi-Analyte Tests and Resubmission Considerations
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> a company that had a previous EUA for a respiratory panel deprioritized to resubmit the same EUA. And so to reiterate what we've previously said, multi-analyte tests that have sufficient manufacturing and testing capacity are included in our priorities and will continue to be prioritized. While we can't discuss specific submissions on this call as we've mentioned, we can generally share that if an EUA request was deprioritized previously, it was likely because the test either had low manufacturing or testing capacity or that the submission was deficient in some way. If such an EUA request was resubmitted and addre

---

#### Instance 18: 2021-08-04_Virtual Town Hall 65_section-titles.md
**Section:** #### 9. Clarifying EUA Approval Timelines for OTC Test Kits
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> y will speed up in the process? And how long we are supposed to wait? Is there any kind of rough estimation for those type of EUA approval? And what kind of resources does the FDA put on the priority to speed up the OTC product? Thank you.
> 
> Toby Lowe (FDA IVD Assoc Director):
> Sure. So obviously, we can't speak to specific tests. And I don't know off-hand the specific situation with yours. If you do have concerns about your file, you can send an email to the Templates mailbox and ask that it be sent to me, and I can take a look at it. But generally, OTC and home use tests are a priority. We do have a large number of

---

#### Instance 19: 2021-08-11_Virtual Town Hall 66_section-titles.md
**Section:** #### 1. Expanding Access to High-Volume COVID-19 Diagnostic Testing
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> luation and Quality, and Toby Lowe, associate director also from OIR We'll start today's program with some opening remarks and updates from our panelists, and then we'll spend the rest of our time today answering your questions about the development and validation of COVID tests. Please note, we're not able to discuss specific submissions that are under review. To ask a question, please go to your name on the Zoom meeting and select the Raise Your Hand icon. Now let's turn the program over to Tim for some opening remarks and updates. Thank you, Tim.
> 
> Tim Stenzel (FDA IVD Director):
> And thank you, Elias, and welc

---

#### Instance 20: 2021-08-18_Virtual Town Hall 67_section-titles.md
**Section:** #### 1. FDA Priorities for SARS-CoV-2 Test Development
**Category:** F2 — Blanket Pre-Filter (No Redirect)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declines to address question on call as 'too detailed' without clear alternative path.

**Excerpt:**
> Lowe, Associate Director also from OIR. First, we will have opening remarks from our speakers. And then we'll begin answering your questions about the development and validation of COVID tests. To ask a question, please select the Raise Your Hand icon at the bottom of your screen. Please note we're not able to discuss specific submissions that are under review. Now, I'll hand the program over to Tim.
> 
> Tim Stenzel (FDA IVD Director):
> Welcome, everyone. I believe this is the 67th CDRH virtual town hall meeting to assist all of you test developers in developing tests to meet current pandemic needs. And, just to rei

---

#### Instance 21: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Section:** #### 1. SARS-CoV-2 Test Development and Validation Updates
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> uality, and Dr. Kristian Roth, also from OIR. We will begin with opening remarks from our speakers and then we'll answer your questions about the COVID test development and validation process. To ask a question, please select the Raise Your Hand icon at the bottom of your screen. Please note we are not able to discuss specific submissions that are under review. Now, I will hand the program over to Tim.
> 
> Tim Stenzel (FDA IVD Director):
> Thank you, and welcome everyone to another weekly webinar and virtual town meeting. And we will be moving to every other and see if that works. We always have the flexibility to go

---

#### Instance 22: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Section:** #### 4. FDA Plans for Transitioning COVID-19 Test EUAs
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** Developer asks about submission timeline or status; FDA declines with no substantive guidance.

**Excerpt:**
> to a longer answer here shortly. Also, would tests previously granted EUA be allowed to remain on market if the EUA pathway is ended? And the answer is there is a short answer, is yes. Let me go into more detail on this. We have covered this before on this call, but we'll go over it again. While we can't comment on the timeline, we're working on a transition plan for devices offered under EUA. But we still are encouraging full authorization submissions to the FDA soon as you want. We are accepting Q-Subs, Pre-Subs for those. And we're accepting full authorization applications. For molecular, that mostly would be 510k subm

---

#### Instance 23: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Section:** #### 11. FDA Guidance on EUA to 510k Transitions
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** Developer asks about submission timeline or status; FDA declines with no substantive guidance.

**Excerpt:**
> And the final question from this person notes that in an August 12 article, in Agency IQ by Laura DiAngelo on the FDA transition from QSR to ISO 13485, that there are questions about the impact on EUA authorizations. So yes, we are in the process of converting from QSR to ISO 13485. However, and we can't comment on the timeline for a transition plan. But again, we do not see an end anywhere in the near future to the EUA pathway for review of critical assays by the FDA.

---

#### Instance 24: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Section:** #### 20. Transition from EUA to Full 820 Compliance
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** Developer asks about submission timeline or status; FDA declines with no substantive guidance.

**Excerpt:**
> nk the last time we talked about 820 at these town halls was in February, when the plan was the transition guidance will address kind of the things that were waved out under EUA and the transition into a fully compliant 820 system. And then forward looking, and the answer might just literally be we can't comment on the timeline. But my question was, if we're transitioning from EUA with some parts waived out in 820, to full 820, is there going to be another plan for? Or is this just we'll take as it comes for the transition to ISO, which I know is kind of in the hopper?
> 
> Tim Stenzel (FDA IVD Director):
> So I don't I don't s

---

#### Instance 25: 2021-09-22_Virtual Town Hall 70_section-titles.md
**Section:** #### 8. Clarification on Confirmed Positives and FDA Communication Response Time
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> usability?
> 
> Tim Stenzel (FDA IVD Director):
> So I neglected to read a disclaimer at the beginning of the question that we went over that were received prior to the call. And this is true for every week. So we do receive some questions that are a little too detailed or test- or case-specific that we will not address on the call. And so I forgot to do that. So that was the case for your question. So I do recommend that you reach out to FDA staff through the CDRH EUA Templates email address. Or if you already have a reviewer assigned, to reach out to them to engage them in this conversation. I'm not going to be

---

#### Instance 26: 2021-10-06_Virtual Town Hall 71_section-titles.md
**Section:** #### 1. COVID-19 Test Updates and EUA Prioritization Changes
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> tion. And then finally, we'll open the line up your live questions. To ask a live questions, please select the Raise Hand icon at the bottom of your screen when we get to that part of the program. When you're called on, please identify yourself and ask your question promptly. Also please note we're not able to discuss specific submissions that are currently under review. With that, I will hand the program over now to Toby. Welcome, Toby.
> 
> Toby Lowe (FDA IVD Assoc Director):
> Thanks, Joe, and thanks, everyone, for joining us again this week. We do have several updates to share and then we'll get into the questions

---

#### Instance 27: 2021-12-01_Virtual Town Hall 74_section-titles.md
**Section:** #### 1. COVID-19 Test Guidance Amid Omicron Variant Concerns
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> ivision of Microbiology Devices, also in OIR. We'll begin with opening remarks from our panelists, and then we'll answer your previously emailed questions about COVID test development and validation. Please note we received some questions that are a little too detailed or test case specific that we will not address on the call. For those questions, we'll try to send our response in writing within a few days. If you submitted a question and do not hear it addressed, please look for a written response. If you do not receive one within a few days, please feel free to reach back out to CDRH-EUA- Templates@fda.hhs

---

#### Instance 28: 2021-12-15_Virtual Town Hall 75_section-titles.md
**Section:** #### 6. FDA Guidance on EUA Amendments and Live Questions
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> So please keep a lookout for that email response. And now we'll move on and take your live questions. So to ask a live question, please select the “Raise Hand” icon at the bottom of the screen. When you are called on, please identify yourself and ask your question promptly. Also, please note we're not able to discuss specific submissions that are currently under review. So we have a few people already with their hands raised. So I'm going to start with the top. So Bridget, I'm going to unmute you. Please unmute yourself and ask your question.

---

#### Instance 29: 2022-01-26_Virtual Town Hall 77_section-titles.md
**Section:** #### 1. FDA Updates on COVID-19 Test Development Guidance
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> of the Division of Microbiological Devices. With that, we will begin with open remarks from our panelists, and then we'll answer your previously emailed questions about COVID test development and validation. Please note, we received some questions that are too detailed or test case specific that we will not address on the call. For those questions, we'll try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed, please look for the written response. If you do not receive one within a few days, please feel free to reach back out to CDRH-EUA- Templates@fd

---

#### Instance 30: 2022-01-26_Virtual Town Hall 77_section-titles.md
**Section:** #### 8. FDA Guidance on Multi-Analyte Test Emergency Use Authorizations
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> d with that, we are now going to transition to the live questions. So now let's take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your screen. When you are called on, please identify yourself and ask your question promptly. Also, please note we are not able to discuss specific submissions under review. Again, for those type of questions, please email the EUA Templates mailbox. So with that, we're going to get to our first question. MHK, I'm unmuting you. Please unmute yourself and ask your question.

---

#### Instance 31: 2022-02-09_Virtual Town Hall 78_section-titles.md
_???_
**Section:** #### 7. Delays in EUA Amendment Review Process
**Category:** B — Third-Party Confidentiality Protection
**Legitimacy Score:** 5/5 (Fully Legitimate)
**Rationale:** Caller asking about another company's submission. FDA legitimately cannot disclose third-party confidential information.

**Excerpt:**
> Richard Montagna:
> Thank you for taking the call. This is Richard Montagna from Rheonix. I know that the FDA is not able to respond to specific questions about a specific submission, so I'll try to frame this in a very general way. We submitted an amendment to our PCR EUA back in September. It was intended to validate the assay as a moderate complexity rather than the originally authorized high complexity. We were notified that

---

#### Instance 32: 2022-02-23_Virtual Town Hall 79_section-titles.md
**Section:** #### 1. COVID-19 IVD Town Hall Updates and FAQs
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> es also in OIR. We'll begin today's program with opening remarks from our panelists. And they'll provide updates and answer your previously emailed questions about COVID test development and validation. Please note we received some email questions that are too detailed or test case-specific that we will not address on the call. For those questions, we'll try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed, please look for a written response. If you do not receive one within a few days, please feel free to reach back out to CDRH-EUA-Templates@fda.h

---

#### Instance 33: 2022-02-23_Virtual Town Hall 79_section-titles.md
**Section:** #### 7. Regulatory Requirements for Legally Marketed Nasal Swabs
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> ive portion. So now let's take some live questions from you. Remember, to ask a live question, please select the Raise Hand icon at the bottom of your screen. When you're called on, please identify yourself and ask your question promptly. Also, please note just like with the emailed questions we're not able to discuss specific submissions that are under review. So there may be times where we'll ask you to email that question to the templates mailbox because it's a very specific type of question. With that, we're going to take our first live question of the day. So Thomas, please unmute yourself and ask your ques

---

#### Instance 34: 2022-02-23_Virtual Town Hall 79_section-titles.md
**Section:** #### 9. FDA Prioritization for COVID-19 Test Submissions
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> Toby Lowe (FDA IVD Assoc Director):
> Thanks for that question. The transition guidances that were put out and that were discussed in the webinar yesterday were put out for comment. And so we do recommend that if there are points that are unclear there that you submit comments to the docket. And we can't really comment fully on what will or will not be done at that stage since that guidance is out in draft for comments and not for implementation. So the prioritization that we've laid out in our current COVID test policy guidance still holds for our EUA requests. And that does provide our current thinking about th

---

#### Instance 35: 2022-03-09_Virtual Town Hall 80_section-titles.md
**Section:** #### 2. FDA Warns Against Unauthorized COVID-19 Diagnostic Tests
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> ver to Kim. Thank you.
> 
> Commander Kimberly Piermatteo (FDA):
> Thank you Tim and Kris for those opening remarks. We'll now answer your previously emailed questions about COVID-19 Test Development and Validation. _Please note we receive some questions that are too detailed or test case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days._ If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out

---

#### Instance 36: 2022-03-09_Virtual Town Hall 80_section-titles.md
**Section:** #### 5. FDA Guidance on De Novo Serology Test Submissions
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Thank you, alright. The next question, is FDA currently reviewing any de novo submissions for serology tests? If so, would it be possible to share recommendations provided to developers at this time?
> 
> Kris Roth (FDA):
> So again, we're not going to comment on any submissions that may be under review, however if you intend to pursue a de novo regulatory pathway for your serology test, we recommend that you submit a Pre-Submission with your study protocols, in order for FDA to provide appropriate feedback.

---

#### Instance 37: 2022-03-09_Virtual Town Hall 80_section-titles.md
**Section:** #### 7. Guidance on Enrichment Approaches for COVID-19 Test Evaluation
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> . Thank you Kris. That wraps up the previously submitted questions. We will now take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your screen. When you are called on, please identify yourself and ask your question promptly. Also please note, we are not able to discuss specific submissions under review. Our first live question is from Sam. Sam I'm going to unmute you, please unmute yourself and ask your question.

---

#### Instance 38: 2022-03-23_Virtual Town Hall 81_section-titles.md
**Section:** #### 9. Live Q&A Guidelines and Participant Instructions
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> ask your question promptly. A few reminders before we take our first question—please limit yourself to one question only. If you have an additional question, you may raise your hand again to get back into the queue, and we will call on you again as time permits. And lastly, please remember, we are not able to discuss specific submissions under review. Our first live question is from Phil. Phil, I'm going to unmute you. Please unmute yourself and ask your question.

---

#### Instance 39: 2022-04-06_Virtual Town Hall 82_section-titles.md
**Section:** #### 2. Checking Authorization and Safety of COVID-19 Tests
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> ask your question promptly. A few reminders before we take our first question, please limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue and we will call on you as time permits. And lastly, please remember, we are not able to discuss specific submissions under review. So our first live question is from James. James, I'm going to unmute you. Please unmute yourself and ask your question.

---

#### Instance 40: 2022-04-20_Virtual Town Hall 83_section-titles.md
**Section:** #### 2. Fresh Samples Required for COVID-19 Antigen Test Studies
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Thank you, Tim. Like Tim said, we'll now move to your previously emailed questions. __Please note we did receive some questions that are too detailed or too case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days.__ If you have submitted a question, and you do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach b

---

#### Instance 41: 2022-04-20_Virtual Town Hall 83_section-titles.md
**Section:** #### 5. Guidelines for COVID-19 Breath Test Development and EUA Process
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> t in Zoom to unmute yourself. Then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you if time permits. And please remember we are not able to discuss specific submissions under review. Alright, our first question is from Enes. Enes, I'm going to unmute you. Please unmute yourself and ask your question. Enes, are you able to unmute yourself and ask your question? Alright, we'll go ahead and we'll move to the next question. The next question comes

---

#### Instance 42: 2022-05-04_Virtual Town Hall 84_section-titles.md
**Section:** #### 2. Non-CLIA Labs for COVID Test Candidate Studies
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Thanks, Toby. We'll now go to answer your previously emailed questions about COVID test development and validation. Please note, we have received some questions that are too detailed or test‐case specific, that we will not address during today's Town Hall. For those questions, we will try to send you a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, you may reach back out to the

---

#### Instance 43: 2022-05-04_Virtual Town Hall 84_section-titles.md
**Section:** #### 7. Analyzing Low Positives in Antigen Test Performance
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> in Zoom to unmute yourself, then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. OK, our first live question is coming from Homer. Homer, I'm going to unmute you. Please unmute yourself and ask your question.

---

#### Instance 44: 2022-05-18_Virtual Town Hall 85_section-titles.md
**Section:** #### 2. FDA Prioritization of COVID-19 Test Accessibility
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> OK. Thank you, Toby. We'll now answer your previously emailed questions about COVID test development and validation. As mentioned before, please note we do receive some questions that are too detailed or test case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out

---

#### Instance 45: 2022-05-18_Virtual Town Hall 85_section-titles.md
**Section:** #### 6. Challenges in Flu Test Validation and FDA Recommendations
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> m to unmute yourself, then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And lastly, please remember we are not able to discuss device or specific submissions under review. Alright, our first live question is coming from Wendy. Wendy, I am going to unmute your line. Please unmute yourself and ask your question.

---

#### Instance 46: 2022-06-01_Virtual Town Hall 86_section-titles.md
**Section:** #### 2. FDA Guidance on Multiplex Antigen Test Authorization
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Great, thank you, Tim. We'll now answer your previously emailed questions about COVID test development and validation. Again, as we've mentioned before, please note we have received some questions that are too detailed or test‐case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within that few days, please feel free to reach back

---

#### Instance 47: 2022-06-01_Virtual Town Hall 86_section-titles.md
**Section:** #### 4. Exclusion Criteria for Symptomatic Subjects in COVID-19 Studies
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> and Zoom to unmute yourself. Then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. So our first live question for today is coming from Jennifer. Jennifer, I'm going to unmute you. Please unmute yourself and ask your question.

---

#### Instance 48: 2022-06-15_Virtual Town Hall 87_section-titles.md
**Section:** #### 2. Evaluating Variants for OTC Rapid Antigen Test Authorization
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Great. Thanks Toby. We'll now answer your previously emailed questions. Please note, we have received some questions that were too detailed or test case specific that we will not address today. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA­ T

---

#### Instance 49: 2022-06-15_Virtual Town Hall 87_section-titles.md
**Section:** #### 5. FDA Prioritization of Diagnostic Breath Test Evaluations
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> in Zoom to unmute yourself. Then identify yourself, and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. So our first live question is coming from James. James, I have unmuted your line. Please unmute yourself and ask your question.

---

#### Instance 50: 2022-06-29_Virtual Town Hall 88_section-titles.md
**Section:** #### 2. Human Sample Controls in Molecular OTC Tests
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Great. Thank you, Tim. Alright, we will now answer your previously emailed questions about COVID test development and validation. Please note, we have received some questions that were too detailed or test‐case specific that we will not address today. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA‐Te

---

#### Instance 51: 2022-06-29_Virtual Town Hall 88_section-titles.md
**Section:** #### 7. EUA Requirements for OTC SARS-CoV-2 Antigen Tests
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> button to unmute your line. Then identify yourself, and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you as time permits. And please remember, we're not able to discuss specific submissions under review. Our first live question is from Sam. Sam, I have unmuted your line. Please unmute yourself and ask your question.

---

#### Instance 52: 2022-07-27_Virtual Town Hall 89_section-titles.md
**Section:** #### 2. Acceptability of Non-U.S. Flu A and RSV Samples
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Great. Thank you, Tim and Kris. We will now answer your previously emailed questions. Please note, we do receive some questions that are too detailed or test case-specific that we will not address today. For those questions, we will try to send you a response in writing within a few days. If you have submitted a question and do not here to addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH-EU

---

#### Instance 53: 2022-07-27_Virtual Town Hall 89_section-titles.md
**Section:** #### 3. Guidance for Clinical Validation and Live Q&A Challenges
**Category:** E — Deflection to Email/Pre-EUA (No Substantive Answer)
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA provided no substantive on-call guidance and redirected entirely to offline channels, removing public accountability for the answer.

**Excerpt:**
> tton to unmute your line, then identify yourself and ask your question. Please do remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. Our first live question is coming from Joshua. Joshua, I'm going to unmute you. Please unmute yourself and ask your question. Joshua, I've unmuted you again, if you can look for that prompt to unmute yourself. Alright, Joshua, I'm going to come back to you. Keep a

---

#### Instance 54: 2022-08-24_Virtual Town Hall 90_section-titles.md
**Section:** #### 2. EUA Requirements for Multiplex COVID-19 and Flu Tests
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> Commander Kimberly Piermatteo (FDA):
> Great. Thank you, Kris, for those opening remarks. We will now answer your previously emailed questions. Please note, as always, we do receive some questions that are too detailed or test‐case specific that we will not address today. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA­ T

---

#### Instance 55: 2022-08-24_Virtual Town Hall 90_section-titles.md
**Section:** #### 6. FDA Authorization of COVID-19 Diagnostic Breath Tests
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> button to unmute your line. Then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you as time permits. And please remember, we are not able to discuss specific submissions under review. Alright, our first live question is coming from Anjali. Anjali, I'm going to unmute your line. Please unmute yourself and ask your question.

---

#### Instance 56: 2022-08-24_Virtual Town Hall 90_section-titles.md
**Section:** #### 9. Optimizing Clinical Trial Design for Dual Testing Kits
**Category:** E2 — Policy/Process Refusal
**Legitimacy Score:** 2/5 (Questionable)
**Rationale:** FDA declined to engage on a question that appears to involve generalizable policy or process, using 'specific submission' language as a shield.

**Excerpt:**
> nstances or provide us a plan, I guess, in both instances, one, using the same abstraction buffer and two, provide a sampling plan that minimizes bias for the two candidate tests.
> 
> Seungjin Ha Gina:
> So you recommend we have to get through the pre‐EUA for those submissions?
> 
> Kris Roth (FDA):
> Yeah, I wouldn't be able to comment. I can't say on the phone, yes, it's fine to use the same abstraction buffer. One, it's off‐label use to use against the instructions for use. And number two, we'd be concerned about running out of buffer.
> 
> Seungjin Ha Gina:
> OK. I got it. So before we are going to conduct the clinical trial

---

#### Instance 57: 2022-09-28_Virtual Town Hall 93_section-titles.md
**Section:** #### 2. Guidance for Submitting Monkeypox EUA Requests to FDA
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> today's previously emailed questions in two parts. The first part will address monkeypox previously emailed questions. And then we will address the COVID-19 previously emailed questions. As always, please note we do receive some emailed questions that are too detailed or test case specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out

---

#### Instance 58: 2022-10-26_Virtual Town Hall 96_section-titles.md
**Section:** #### 2. Guidelines for Monkeypox Test Development and Validation
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> der Kimberly Piermatteo (FDA):
> Thank you Tim and Toby for those remarks. We will now answer your previously emailed questions about monkeypox and COVID‐19 test development and validation. As always, please note we do receive some emailed questions that are too detailed or test case‐specific that we will not address during today's Virtual Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach

---

#### Instance 59: 2022-10-26_Virtual Town Hall 96_section-titles.md
**Section:** #### 5. FDA Transition Plans for COVID-19 Device Policies
**Category:** C1 — Declined Specifics but Provided Useful General Guidance
**Legitimacy Score:** 4/5 (Largely Legitimate)
**Rationale:** FDA declined to discuss the specific submission but provided substantive general guidance that partially addresses the underlying question.

**Excerpt:**
> ument titled “Transition Plan for Medical Devices Issued Emergency Use Authorizations During the COVID‐19 Public Health Emergency,” which addresses the transition back‐to‐normal operations when the emergency use declarations that allowed for FDA to issue EUAs are no longer in effect. However, we're not able to comment on estimated finalization dates for draft guidances, so we do recommend that you keep an eye on FDA's website for any updates there.
> 
> Commander Kimberly Piermatteo (FDA):
> Thanks again, Toby, for all of your responses. And thank you to those stakeholders who submitted those questions. That wraps up

---

#### Instance 60: 2022-11-30_Virtual Town Hall 98_section-titles.md
**Section:** #### 1. Monkeypox and COVID-19 Testing Updates and EUA Plans
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> he questions.
> 
> Commander Kimberly Piermatteo (FDA):
> Great. Thank you, Toby. We'll now answer your previously emailed questions about monkeypox and COVID‐19 test development and validation. As always, please note, we do receive some email questions that are too detailed or test case specific that we will not address during today's Virtual Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach

---

#### Instance 61: 2022-12-14_Virtual Town Hall 99_section-titles.md
**Section:** #### 1. Mpox and COVID-19 Diagnostic Test Updates and Guidance
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> iermatteo (FDA):
> Thanks, Toby, for those remarks. Alright, we will now address or answer, sorry, your previously emailed questions about mpox and COVID‐19 test development and validation. As always, please note we do receive some emailed questions that are too detailed or test case specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out

---

#### Instance 62: 2023-01-11_Virtual Town Hall 100_section-titles.md
**Section:** #### 2. Guidance on SARS-CoV-2 Test Development Controls
**Category:** C2 — Partial Answer with Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA provided some general guidance but redirected the substantive question to email or pre-EUA process.

**Excerpt:**
> Joseph Tartal (FDA):
> Thank you, Toby. We'll now answer your previously emailed questions. Please note, we do receive some email questions that are too detailed or to test case-specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out

---

#### Instance 63: 2023-02-15_Virtual Town Hall 101_section-titles.md
**Section:** #### 2. Updates on Mpox and COVID-19 Test Policies
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> ly Piermatteo (FDA):
> Thank you, Toby, and thank you, Tim, for those remarks. We will now answer your previously emailed questions about mpox and COVID-19 test development and validation. As always, please note, we do receive some emailed questions that are too detailed or test case-specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out

---

#### Instance 64: 2023-03-22_Virtual Town Hall 102_section-titles.md
**Section:** #### 3. COVID-19 Antigen Test Submission Pathways and Regulations
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> Joseph Tartal (FDA):
> Thank you, everyone, for those opening remarks. We'll now answer your previously- emailed questions about mpox and COVID-19 test development and validation. Please note, we do receive some emailed questions that are too detailed or test case-specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a written response in a few days, please feel free to reach back

---

#### Instance 65: 2023-04-26_Virtual Town Hall 103_section-titles.md
**Section:** #### 2. COVID-19 Test Regulations Post-Public Health Emergency
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Legitimacy Score:** 3/5 (Mixed / Could Have Done Better)
**Rationale:** FDA pre-filters certain emailed questions as 'too detailed or case-specific' and promises written response. Provides a channel but removes public accountability.

**Excerpt:**
> rmation. Great presentation. We'll now answer your previously emailed questions about COVID-19 test development validation and the final emergency use authorization transition guidance documents. As always, we have received some questions that are a little too detailed or test case specific that we will not address on today's call. Further, we are focusing primarily on the transition for today's town hall, and some questions we received are not related to the transition and the transition guidances. For those questions that we don't address on today's call, we will try to send a response in writing within a f

---

## 4. Summary of Results

### Overall Distribution

| Metric | Count |
| --- | --- |
| Total refusal instances identified | 116 |
| Boilerplate opening disclaimers (not scored) | 51 |
| Active refusals (scored) | 65 |
| Town hall files with at least one refusal | 84 of 100 |
|||

### Distribution by Category (Active Refusals Only)

| Code | Category | Count | Avg Score |
| --- | --- | --- | --- |
| B | Third-Party Confidentiality Protection | 3 | 5.0 |
| C1 | Declined Specifics / Provided Useful General Guidance | 8 | 4.0 |
| C2 | Partial Answer with Redirect | 7 | 3.0 |
| D1 | Timeline/Status Deflection with Redirect | 2 | 3.0 |
| D2 | Timeline/Status Deflection (No Substantive Response) | 3 | 2.0 |
| E | Deflection to Email/Pre-EUA (No Substantive Answer) | 10 | 2.0 |
| E2 | Policy/Process Refusal | 17 | 2.0 |
| F1 | Blanket Pre-Filter with Email Redirect | 14 | 3.0 |
| F2 | Blanket Pre-Filter (No Redirect) | 1 | 2.0 |
|||

### Distribution by Legitimacy Score (Active Refusals Only)

| Score | Label | Count | % of Active Refusals |
| --- | --- | --- | --- |
| 5 | Fully Legitimate | 3 | 5% |
| 4 | Largely Legitimate | 8 | 12% |
| 3 | Mixed / Could Have Done Better | 23 | 35% |
| 2 | Questionable | 31 | 48% |
| 1 | Not Legitimate | 0 | 0% |
|||

### Key Findings

- **Average legitimacy score across active refusals: 2.7/5**
- **31 of 65 active refusals (48%) scored 2 or below ("Questionable" or worse)**
- **11 of 65 active refusals (17%) scored 4 or above ("Largely Legitimate" or better)**
- The boilerplate disclaimer appeared in 51 of 116 total instances, confirming that the refusal-to-engage posture was institutionalized from the start of every session.
- The most common active refusal pattern was deflection to email or pre-EUA channels, which removes public accountability and allows for inconsistent answers across developers.
- Even where the FDA's stated reason (confidentiality) had some basis, the response was almost always refusal rather than generalization. The Director of IVD was on most calls and could have reframed specific questions into general policy answers.

### Interpretation

The data supports the following conclusions:

1. **The "specific submissions" policy was applied far more broadly than confidentiality requires.** True third-party confidentiality protection (Category B) accounts for a small fraction of refusals. The majority of refusals involved developers asking about their own submissions or about general policy.

2. **Refusal was the default; generalization was the exception.** When the FDA did provide general guidance alongside a refusal (Categories C1, C2), the result was usually more useful. But this was not the standard practice.

3. **The pattern enabled discretion without accountability.** By systematically redirecting substantive questions to private channels, the FDA ensured that its answers, reasoning, and any inconsistencies were not part of the public record.

4. **The boilerplate disclaimer normalized the refusal.** By stating the policy at the opening of every session, the FDA pre-emptively framed all questions as potentially off-limits and trained developers to self-censor.

5. **The system structurally silenced the people most qualified to challenge it.** Diagnostics developers had the technical expertise to evaluate whether the FDA's review process was consistent, timely, and well-reasoned. But their complete dependence on FDA authorization for market access meant that public criticism carried an unacceptable risk of retaliation — not through any formal mechanism, but through the informal discretion the FDA exercised over timelines, depth of review, and responsiveness. The refusal pattern documented here is both a symptom and a reinforcing mechanism of that silencing: by keeping substantive exchanges private, the FDA ensured there was no public record against which consistency could be measured, and no forum in which the power asymmetry could be safely challenged.

6. **Reform is straightforward.** Replacing "we cannot respond" with "we will answer from general policy" and committing to public follow-up for redirected questions would address the core transparency failure without requiring the FDA to conduct ad hoc reviews on live calls. Publishing review timelines, rejection reasoning, and comparative metrics across submissions would address the consistency and retaliation concerns. These are not radical proposals — they are the minimum conditions for accountability in an agency that exercises life-and-death discretion over public health tools during a pandemic.


# 110,997  _compilation_fda-refusals-to-answer.md
METADATA
last updated: 2026-02-26 AI
file_name: _compilation_fda-refusals-to-answer.md
category: regulatory
subcategory: fda-townhalls
words: 89494
tokens: 110997


CONTENT

***INTERNAL TITLE: FDA Town Hall — Instances of Refusal to Answer Questions***

This is a raw compilation of passages from FDA COVID-19 Diagnostic Virtual Town Hall transcripts
where the FDA declined or was unable to answer a question. Extracted from `section-titles` files.
No analysis or commentary has been applied; this is search output only.

**Files with refusals:** 84 of 100 section-titles files
**Total sections extracted:** 116

---

## 2020-05-20_Virtual Town Hall 9_section-titles.md

#### 9. Concerns About Small Diagnostics Companies and Test Approvals

Larry Lines:
Hey there. I just had a question – I'm no professional or anything, but I've been following along with a local USA company in Utah called Co-Diagnostics, and they were talking about having a dual serology and PCR test, and those tests really interest me because, like I said, I'm no professional, but I've been reading up a lot. FDA Townhall And most of the tests seem to be having some of their false results due to the primer dimers in the RT PCR chain reaction process, and that is a big part – they have, you know, intellectual property on their co-primers which eliminates that. They also are working with an oil lab DNA with their co- primers to try to work for a saliva test, which I haven't heard much about. They submitted that mid-April. I'm just really curious. That's a local company. It's a little small. I'm worried they may be overlooked because of small, but from the research I've done, their intellectual property and could really help, so I would just love to hear back from that.

Tim Stenzel (FDA IVD Director):
So, yeah, there is information that might be considered confidential. The…

Larry Lines:
That's what I worried about. You know, I'm local. I'm right by Utah, and I know dozens of people who can't get tests, and, you know, I'm with no media, and I just worry about my friends and family where these good tests may be being held up, you know, the spit tests which have these co-primers which would reduce a lot of these primer dimers which is a very predominant cause of these false positives in these RT PCR chain reaction. And I'm just worried that some of this whole business confidentiality is really overtaking the safety of these tests. As long as – you know, they've been bragging this new test could be serology and RT PCR and that could be the gold standard for our company.

Toby Lowe (FDA IVD Assoc Director):
I think… Crosstalk

Tim Stenzel (FDA IVD Director):
So yeah… FDA Townhall

Toby Lowe (FDA IVD Assoc Director):
Go ahead, Tim.

Tim Stenzel (FDA IVD Director):
No. No. You go ahead.

Toby Lowe (FDA IVD Assoc Director):
So the confidentiality that Tim's mentioning is not holding up any reviews. We just are not able to provide any information about any specific companies that may or may not be seeking EUA until that is public, so we just can't share any of those details on these calls, but we are definitely open to any new technologies or improvements on existing technologies, and we encourage all of those companies to come talk to us.

Larry Lines:
Is there any movement on their oil DNA lab saliva test using co-primer technology to reduce false positives?

Toby Lowe (FDA IVD Assoc Director):
Again, we can't comment about any specific companies or…

Larry Lines:
You comment on AYGU a second ago which is confusing to me.

Toby Lowe (FDA IVD Assoc Director):
No, I don't think we commented anything specific to that company or test driver.

Larry Lines:
I understand. You know, I don't want to take up any more time. I feel like you guys won't answer my question specifically. Thank you very much.

Coordinator (FDA):
Thank you very much.

Tim Stenzel (FDA IVD Director):
Let me just – hold on. Let me just complete the loop on this. Toby was right. We welcome all developers. If - we do not speak specifically about any FDA Townhall developers that haven't given us permission to speak or we haven't taken public action. However, we do work with those developers, and we are working very closely, and if there's any innovative technologies that will assist us, we've authorized now over 100 tests, and that represents tens of millions of testing opportunities…

Larry Lines:
May I say one thing?

Tim Stenzel (FDA IVD Director):
Yeah.

Larry Lines:
Over those hundreds of tests, I do believe it's about 40 or 50 percent coming from the same four or five companies, and that's just what worries me. You know, seeing such a pandemic and you have a small company that has the potential to grow, I just do worry it may be overshadowed. For the good of the community just based off of, you know, large corporate greed and – that is my main point. You know, I do believe in their technology very soundly. You can speak to the stock price, which I have no interest into it as well. I just want to get good tests, you know, made in America out to my friends and family, and, you know, I just worry. I have a lot of elderly family, but, again, thank you for your time. I understand if you can't get any more into detail. I do not want to take up one more minute of your time. Thank you.

Tim Stenzel (FDA IVD Director):
Okay. Let's move to the next question please.

Coordinator (FDA):
Thank you. Our next question comes from Ms. Zimmer. Your line is open. FDA Townhall


---

## 2020-05-27_Virtual Town Hall 10_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing Policies and FAQs

Coordinator (FDA):
Welcome and thank you for standing by. At this time all participant lines are in a listen-only mode. After today's presentation, you will have the opportunity to ask questions and you may do so over the phone, by pressing star then 1 at that time. Today's conference call is being recorded. If you have any objections to this, please disconnect. And now, I would like to turn the call over to your host for today, Ms. Irene Aihie. Ms. Aihie, you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie, of CDRH's Office of Communication and Education. Welcome to the FDA's 9th in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, Sara Brenner, Associate Director for Medical Affairs; and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, all in CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Now I give you Timothy. FDA Townhall

Tim Stenzel (FDA IVD Director):
Welcome back to our virtual town hall meeting today. We will continue these calls through June and you will receive information about that in the very near future. I did want to take this opportunity to correct some of my remarks that I made last week. This has to do with the notification list for any notified tests, but especially about the serology tests. So enforcement discretion and policies in our guidance do not make notified tests legally marketed. Enforcement discretion means that we do not intend to enforce the requirement. It does not waive the requirement. So I perhaps should have correctly said tests on the notification list may market their device under the policy in the FDA policy for Coronavirus Disease 2019 test. So I hope that is helpful in clarifying my remarks from last week. There are several updates and then we have a number of chat questions that we didn't get to last week that I'd like to go through. First up, on the FAQ page updates, it said 29 notified serology tip developers were removed from our notification list for pathway D. There is a new list that's been added and it's under the question what test should no longer be distributed for COVID-19. Commercial or manufacturers listed below this question did provide notification to the FDA that they had validated and intended to distribute their serology tests for infection as set forth in section 4.D of our policy. The FDA had previously included them on the Web site notification list of commercial manufacturers distributing through all of these test kids under their pharmacy, but they have now been removed from the notification list and placed on this list. As noted in the guidance, if the EUA request is not submitted by a commercial manufacturer of serology tests within a reasonable period of time or if significant problems are identified with such a test that cannot be - had not been addressed in a timely manner, FDA intends to remove the manufacturer and test FDA Townhall from the notifications list. Some commercial manufacturers have voluntarily withdrawn their tests from notification and such tests are noted by an asterisk on this list. All right. With that, I wanted to move into a couple of other brief FAQ updates. One is we added a new extraction option and that is the Beckman Extraction Reagent. Also, we've provided a notice on the RADx program. There is significant funding for developers of a rapid antigen, as well as molecular diagnostic tests. This applies to all developers and to just a new start-up developer. So even established companies who want to develop on the line that are noted in the RADx notification, we do want to make that widely available to all developers. And with that, I will move onto the chat questions that we didn't get to last week. There was a question about are there any current saliva test applications under review? And is there any expectation that new saliva tests will be offered? Unfortunately, I cannot share any information on submissions under review. We can however, share that on May 21st we authorized the second test home specimen collection and this can be found on the EUA authorization Web page. Can we develop a rapid detection assay use another rapid assay as a comparator method to demonstrate equivalence? At this time we are recommending that the developers use a high sensitivity molecular assay as a comparator. This is noted on a rapid antigen template on our Web site, as a recommendation. So is there any role for point of care tests in asymptomatic pre-surgical patients? We are open to receiving data that we provide education on appropriateness for a test that can be promoted for this type of application. We have noted very clearly on our FAQ page that with an order for a test labs are FDA Townhall allowed to perform tests that EUA authorized tests for asymptomatic patients. Another question is are the NCI panel samples available for manufacturers or developers to test their platforms? And at the moment, the testing is being performed at NCI, but we are looking into how would you make the panel available for developers at their sites. For home collection kits, new questions, does the kit need to receive an EUA approval prior to using the kit or can an EUA be submitted and the kits used in parallel with EUA in the field? The notification policies in the guidance that permit clinical use prior to receiving EUA do not apply to that home collection kit, which must be authorized prior to use. Next question - how long does it take to validate a lateral flow serology test? It depends on the data; validation is data dependent and not time dependent. Next question. With so many serology tests that we're required to submit now for EUA approval you can expect some notifications of these tests that start to be published on the FDA? EUAs will be posted once granted, which will happen as soon as possible. And so stay tuned and keep an eye on it. What approval steps are necessary to begin selling nasal pharyngeal swabs? NP swabs are class 1 exempt and manufacturers should be aware of other requirements for class 1 exempt devices, such as adverse events reporting. For those manufacturers who have unconventional or alternative manufacturing needs, we encourage you to collaborate and validate your NP swabs through engagement with the NIH 3D Print exchange. Next question. What's the position from FDA on use of current EUA PCR based test in asymptomatic and pre-symptomatic patients or for use to screen patients undergoing elective procedures? I did address this question earlier and as long as their healthcare professional is ordering the test and no plans are FDA Townhall being made for asymptomatic testing the FDA asks that a manufacturer using the EUA authorized test can go ahead and test those samples and report out those results. Let's see. There's a question about when an EUA designation may end and when to move into the 510k pathway. And so the emergency declarations for public health are made by the secretary and are unlikely to be terminated any time soon. We always do encourage developers to work towards a routine application. In the first case, this will be a de novo and then the second case will follow that. So we encourage these applications as soon as developers are ready and we're willing to work with them right now to convert these over to routine applications and routine authorizations. We do have considerable discretion. Once tests begin to be authorized under this pathway to keep other EUA tests on the market, we look for the importance of those tests remaining on the market. And we do not foresee that need from going away anytime soon. Can the FDA address requirements for pooling samples from EUA? Have any EUAs been granted for approval samples? So we have not authorized EUA's approved samples. We know that there's a lot of interest in this as both reagents may be sometimes limited. And also as we ramp up testing as part of the get back to work and get back to school program. And so we are very open to pooling approaches. We would invite you to come in to discuss validation of these with us by emailing us at the template email address. One of the - a couple of the real critical functions here or - for consideration is what is the impact on detection on even low positive samples and what is the impact on the limited detection when you perform pooled testing? So we do have thoughts that we can readily share with developers. Please reach FDA Townhall out. And we will be looking for opportunities to update our Web site with some information as soon as possible. Here's another question. Wasn't the FDA required to provide approval within 45 days of submission? Somebody has been waiting a while since studies have shown success. Why is there such a delay when other companies get authorized? We cannot comment on specific submissions. We encourage the sponsor of this submission to reach out to a lead reviewer if they have any concerns. We do make it a priority to review applications that require EUA authorization prior to marketing or prior to offering that kit or that service. And so as long as somebody can offer something through one of the notified lists, that allows us to focus our resources on those that clearly require our EUA authorization. I think that pretty much addresses the questions from last week that we didn't get to. So we can open it up for Q&A now. Thank you.

Coordinator (FDA):
Thank you. If you would like to ask a question over the phone at this time, please unmute your phone and press star 1. You will be prompted to record your name and your name is needed to introduce your question. If at any time your question has been answered while waiting in the queue, you can remove your request by pressing star 2. Once again, that is star 1 for questions over the phone. And we do have our first question over the phone, from Mark. Your line is open.

---

#### 13. FDA Emergency Policies on Test Kit Approvals

Alex Vacilli:
Hi. Thank you for taking my call. And before I ask you in a Newsweek see a lot of counties, buy these rapid test kits. And they kind of sit on the shelves because they're waiting for approval. So there's a number of tests with a CE mark. Can you clarify if, you know, you recommend using tests with a CE mark until you can get the full EUA authorization?

Tim Stenzel (FDA IVD Director):
Yes, we wouldn't make that statement. It's my understanding that the CE mark for this kind of test is a self-certification and not by an agency or a notified body or other third-party. So you know, it's not something that for CE mark for the contest would be reviewed prior to making those kits commercially available. So you know, our FDA would not. However, I will say that where there is a review -- a country of origin review -- any other countries that do review these and make horrible decisions we do incorporate those decisions into our review thinking for a given test what it has achieved so.

Alex Vacilli:
Okay.

Tim Stenzel (FDA IVD Director):
That's about as satisfying an answer as you could wish for. That's how we handle CE marking.

Alex Vacilli:
Okay. One more quick question. Crosstalk

Toby Lowe (FDA IVD Assoc Director):
Also important to note that, you know, those tests if they've completed their validation can notify, and then they can offer under the notification policy while their EUA is under review. FDA Townhall

Alex Vacilli:
Okay.

Tim Stenzel (FDA IVD Director):
That is correct. But I think I heard that from folks who may be purchasing kits out there are waiting for EUA authorization. And again, we're working very hard to make those decisions and make those decisions public.

Coordinator (FDA):
And our last question for today is from Jackie Chan. Your line is open. Jackie Chan Hello and thank you unintelligible last question. Thank you. My question is that I notice in all the EUA there is a waiver cost that we've all manufacturer of this GMP requirement and the quality system requirements. I'm just wondering why is FDA doing that. Wouldn't it be a risk to waive that requirement?

Tim Stenzel (FDA IVD Director):
So under the emergency declaration situation, in order to make as many tests and other devices available, we do make efficient use. We do not waive all requirements. And Toby can fill in the details. But we still do require some important elements such as complaint handling and MDR reporting that we believe is an important safety element to keep. And there are other provisions that we have or will have made requirements for that are above what we usually consider in an emergency situation. But practically speaking, if we didn't allow some flexibility when it comes to those regulations and compliance with those regulations, we wouldn't be able to address some of the significant needs in an emergency such as this. Toby do you have anything else to add?

Toby Lowe (FDA IVD Assoc Director):
Yes, that's correct. It's part of the benefit-risk evaluation under the emergency. And as Tim said we are not waiving all requirements. We do consider which requirements may be appropriate to waive in this particular setting. FDA Townhall Jackie Chan Okay. Thank you. Thank you again for everything, everyone at your agency does. Thank you.

Tim Stenzel (FDA IVD Director):
You're welcome. Thank you.

Coordinator (FDA):
Now I will turn the call back over to Irene Aihie. Ms. Aihie, please go ahead.

Irene Aihie (FDA Moderator):
Thank you. This is Irene Aihie. We appreciate your participation and thoughtful questions. Today's presentation and transcript will be made available on the CDRH Learn web page at www.fda.gov/training/cdrhlearn by Tuesday, June 2. If you have additional questions about today's presentation, please email cdrh-eua-template@fda.hhs.gov. As always we appreciate your feedback. Following the conclusion of the presentation, please complete a short 13-question survey about your FDA CDRH virtual town hall experience. The survey can be found at www.fda.gov/cdrhwebinar immediately following the conclusion of today's live discussion. Again, thank you for participating. This concludes today's discussion.

Coordinator (FDA):
Thank you. All participants you may disconnect at this time. Speakers, please stand by.


---

## 2020-06-03_Virtual Town Hall 11_section-titles.md

#### 1. FDA Updates on Diagnostic Tests and Safety Issues


Coordinator (FDA):
Welcome and thank you for standing by. My name is Amber and I will be your operator today. Today's conference will be on listen-only until the question and answer session. At that time you may press Star 1 to ask a question. Today's conference is being recorded. If you have any objections please disconnect at this time. I know like to turn the meeting over to your host Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA 11th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS CV during the public health emergency. Today Timothy Stenzel, the Director of Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, Sara Brenner, Associate Director for Medical Affairs and Toby Lowe, Associate Director in the Office of In Vitro Diagnostics and Radiological Health all from CDRH will provide a brief update. NWX-FDA OC Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Good day. Thanks for joining us again today and apologies for the technical glitches. And we know that we'll have a number of folks probably joining over the course of this call. And we'll make sure that this is all resolved next week. There will be a transcript from this call for the folks who couldn't join at the beginning. We can get updated and we endeavor to get those transcripts reviewed, edited for correction of the actual spoken word and out - back out to folks. So just a high-level overview we've now authorized 120 one-two=zero diagnostic tests. We have also authorized 15 serology tests. When those serology tests have had testing performed at the National Cancer Institute as part of the Interagency Serology Testing Program that information while usually if not always be immediately available in the instructions for use section of the posted authorization for that serology test. And then as soon as we are able to, we will launch and link the product-specific report from the NCI testing. So be on the lookout for those. But once serology tests has been posted and is authorized check the ISU for NCI data. And then I also wanted to update that there are now 31 removed serology tests removed from the notified list. We have that removal is posted on our FAQ page. Next, I wanted to cover updates to the Abbott ID Now. Monday this week updates to the Abbott authorization ID NOW authorization were made. NWX-FDA OC Now formally as we previously announced negatives by the Abbott ID NOW tests are classified as presumed negative tests or negative results and as clinical situation warrants it is recommended that those negatives be reassessed to another molecular test. In addition in the letter of authorization that is posted on our Web site for the Abbott ID NOW, there is an additional condition that includes a requirement for a formal post-market study that's agreed-upon with the FDA. And the time period in which that has to be performed and reported back to the FDA is also listed in that updated letter of authorization. So the FDA will be monitoring this and any other potential situations closely. We always welcome input on performance of any of the tests that we've authorized or any other situations that you feel would be important for us to know about and we thank you in advance for that. With that, I will turn it over to Toby Lowe who has a brief announcement.

Toby Lowe (FDA IVD Assoc Director):
All right, thanks, Tim. Thanks, everyone for joining us today. We wanted to plug a safety issue that's come up as we've discussed previously, I think on these town halls and we've included in our FAQ on our Web site there are certain types of transport media that are not compatible with certain testing platforms. When materials that contain one of these guanidinium thiocyanates interact with bleach the resulting chemical reaction produces dangerous cyanide gas. On our FAQs we have a warning about this specifically regarding the Prime Store MTM which contains guanidinium thiocyanate that it should not be used with a Hologic Panther or Panther Fusion System since those systems have a disinfecting step that involves bleach. NWX-FDA OC We've recently become aware that some transport media are being distributed without appropriate labeling which makes it difficult for laboratories to know which media they're using and what the ingredients are. Because this is a big risk, we want to make sure that all labs are aware of this issue and we're working with manufacturers to correct it. We're also working on providing further communications to laboratories about this issue. So we want to make sure that labs are aware that the Prime Store MTM the Zymo DNA RNA Shield and the Spectrum Saliva Collection device, as well as any other transport media that contains guanidinium thiocyanate and similar chemicals, should not be used with the Hologic Panther or Panther Fusion System or with any other systems or laboratory processes that use bleach. If there are any questions about this or if you come across any issues with transport media or come across any media that is being sent your laboratory without appropriate labeling, we would appreciate you coming to FDA and notifying us about those issues. And you can do that through the normal Medwatch process and you can also email us at the CDRH EUA templates email address.

Tim Stenzel (FDA IVD Director):
Okay I think we're ready to open it up for questions.

Irene Aihie (FDA Moderator):
Operator we'll now take questions from our participants.

Coordinator (FDA):
Thank you. We'll now begin the question and answer session. If you'd like to ask a question please press star 1. You will be prompted to record your name. Please be sure to unmute your phone. Once again if you'd like to ask a question please press Star 1 and we'll pause for just a moment to allow those questions to start coming through. Our first question comes from Val. Your line is open. NWX-FDA OC


---

## 2020-06-10_Virtual Town Hall 12_section-titles.md

#### 1. FDA Updates on COVID-19 Testing Procedures


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are in a listen-only mode until the question and answer session of today's conference. At that time, you may press Star 1 on your phone to ask a question. I would like to inform all parties that today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the conference over to Miss Irene Aihie. Thank you. You may begin.

Irene Aihie (FDA Moderator):
Hello, I am Irene Aihie, of CDRH's Office of Communication and Education. Welcome to the FDA's 12th in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, Sara Brenner, Associate Director for Medical Affairs, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, all from CDRH, will provide a brief update. Following opening remarks, we will open NWX-FDA OC the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now, I give you Timothy…

Tim Stenzel (FDA IVD Director):
Thank you and welcome, everybody, to this town hall today and look forward to the questions and helping out any way we can there. I wanted to talk about a couple of key topics first. One is prioritization of reviews. So we have - these are unprecedented times and we've seen unprecedented submission. I calculate that the virology branch within our office -- which handles the EUAs for SARS-CoV-2 and COVID -- has seen the workload just for EUAs, not the PEUAs and not any other communication that is 60-folds greater than their usual submission volume. This is, of course, why updated our guidance with the notification pathways so that once developers have validated their tests and if an EUA is required that they can notify us and then once that's been confirmed we'll add them to the notification list and they can market their test in the U.S. And there are certain categories that do require prior EUA approval and, of course, we prioritized those and those would be home collections and home testings. Another prioritization that we make are for anything that is high throughput. We typically define high throughput as having a batch size of, let's say, 200 or more tests per batch so that those applications obviously have - as all do, but also has significant public health importance because they allow us to get testing done more quickly and more efficiently. NWX-FDA OC The other category that we placed a very high priority on are the point of care tests and any of it - for any of the types of tests that we authorize. So we do have this relatively small staff of virology expertise that manages our usual workload and which is sufficient for that. We are not staffed for an emergency such as this type. Now, we have added to that, more than doubling our review staff and bringing in strong, scientific support for other areas in health. It is our goal to authorize every EUA as soon as possible as long as there are no issues. We review applications when they come in. We make sure that there aren't any issues and we prioritize them based on the priorities that I've already mentioned. If there are no issues with the application and they are not in one of the high priority categories, we do let these developers know that we have received their application and that basically due to the volume of applications they will get to them as soon as possible, but in those cases a substantive review hasn't begun. And we - for those that are eligible through the notification pathway to be marketed in the U.S., we do our best to make sure that everybody knows, but if you fit in that category and you notify us and we acknowledge that, then you're allowed to go ahead and market. So that's how we've dealt with this overwhelming workload and we know that there's a lot of interest in getting EUA authorizations finalized as soon as possible. NWX-FDA OC Next, I wanted to move onto an important topic as hopefully over time the number of patients who have been diagnosed with COVID and therefore have samples that would be corrected and could be utilized for test developments and validation that if you see yourself developing an assay and need those - patient samples in order to pursue your validation tests and even perhaps development tests, we would urge you to begin collecting and perhaps banking those samples appropriately, of course. And if there is anything related to stability of samples, that could be an issue ee would ask you to reach out to the template's email address so that we can address any potential stability issues in storing those samples, but we are going to be open to the use of these banked samples for not just EUA applications and validations, but also conversions to usual full authorization. Okay. I think that's maybe all that I'm going to cover right now. So I'm going to turn this over to Toby who has a few updates. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Hi, everyone. Thanks, Tim. So I just wanted to give a couple of updates on some recent information that we've put out on our Web site. We discussed a little bit last week about issues with certain transport media being incompatible with certain testing platforms and late last week, we did issue a letter to health care providers regarding that issue specifically talking about the issue of using transport media containing guanidine thiocyanate or similar chemicals with the Hologic platforms or with other tests or processes that use bleach due to the risk of producing cyanide gas. That letter to health care providers, really to labs, can be found on our Web site. It's also linked from our FAQ page if you look in the What If I Do Not Have section of the FAQ and specifically in the first question under that section NWX-FDA OC which is about swabs and media. There's a link to that letter in that section. We also updated that question. We streamlined the answer to focus on the types of swabs and media rather than looking out for specific catalog numbers as we had previously. And going along with that update, we also linked in that same section of the FAQ's as well as in the blue box at the top of that page. We put out a PowerPoint presentation that is a tool for labs and other stakeholders to use to determine the best testing supplies substitution strategies. So sort of a mix-and-match PowerPoint tool that focuses on the different areas that we have already included in the FAQ's in that what if I do not have section. It just provides another resource to see what are some of the different compatibilities are there. Also on the FAQ's, we added a section to the FAQ with questions about 3-D printed swabs and we may have mentioned this previously on this call, but we also added a section about data reporting for labs to report to public health authorities. And also relative to that, last week HHS issued a guidance on the CARES Act laboratory reporting requirements. They put out a statement about that and a guidance document with corresponding FAQ's up on the HHS Web site. And lastly, at the end of the week last week we put out a new Web page that includes data from the independent evaluation of COVID-19 serological test. So we previously talked about the independent evaluation program mostly NWX-FDA OC being done at the NCI labs for serology tests and this new Web page -- which was also linked from the blue box at the top of the FAQ page -- provides some of the - or provides the data for the tests that have been - that have gone through that program. So I think that's all of the updates that I wanted to make sure to flag at this point. And so I can turn it back over to Irene and we can get started with questions.

Irene Aihie (FDA Moderator):
Thanks, Toby. Operator, we'll now take questions from our participants.

Coordinator (FDA):
Thank you. We will now begin the question and answer session. We ask that you limit yourself to one question only, please. If you would like to ask a question, please press Star 1, unmute your phone and record your name clearly. Your name is required to introduce your question. If you need to withdraw your question, press Star 2. Again, to ask a question, please press Star 1. Our first question will come from Mark Hackman. Your line is open. Mark, we're not able to hear you in conference Be sure to unmute feature on your phone.

---

#### 11. Antigen Test Availability and Contractual Restrictions Concerns


Ken Kim:
Hi. I'm a physician and actually quite involved in the clinical trial space. My NWX-FDA OC question revolves around antigen. I want to know how many companies that you - the FDA is aware of that is developing antigens that already applied for EUA for antigen. And I'm aware of the Clodel EUA antigen approval. The reason why I ask that is I wanted to get antigen to actually use that as a diagnostic tool of Clodel, but then they wanted - they're mandating their contract that we have to exclusively use Clodel and cannot replace it for the next three years unless there's a double-blind randomized trial showing this other agent head-to-head is better. And I said, number one, most things are going to be EUA-approved. Number two, no one's going to do a head-to-head to the initial trial and three years is ridiculous. So basically, wanted to create a monopoly to lock in people and it's very frustrating and I'm actually a little worried that a Clodel person that's on this phone will also retaliate because now they will not even - they won't sell me kits because I won't sign that if we supply. I was wondering is the FDA allowing that to happen and is there any way you can actually lock other people out with that kind of language?

Tim Stenzel (FDA IVD Director):
Let me just make sure that I understand your question. You want to obtain antibodies or antigens?

Ken Kim:
Antigens for...

Tim Stenzel (FDA IVD Director):
Antigens?

Ken Kim:
... for a serology test. No, antigen, not serology. Antigen is different from NWX-FDA OC serology, right?

Tim Stenzel (FDA IVD Director):
So the antigen… Crosstalk

Toby Lowe (FDA IVD Assoc Director):
You're looking to use the actual antigen test? You're not looking to source the antigen ; is that correct?

Ken Kim:
Correct. When we want to use the antigen test for diagnostic purposes and there's only one FDA EUA-approved antigen, to me as a physician, I've been doing clinical trials of one over 700 clinical trials, antigen is going to be a very good screen test that could actually replace TCR for screening, but we need more antigen tests. I think we need more antigen tests, not antibody tests. So I've requested Cordel...

Tim Stenzel (FDA IVD Director):
Okay. Okay.

Ken Kim:
... to use this. Yes. So...

Tim Stenzel (FDA IVD Director):
Okay.

Ken Kim:
... I have two questions… Crosstalk

Tim Stenzel (FDA IVD Director):
So you're having trouble acquiring those Cordel tests?

Ken Kim:
Yes. Well, because they're refusing because they want me to sign a contract that NWX-FDA OC says that I would not go to a different antigen test if something comes up for three years unless there's a double-blind randomized trial head-to-head against their antigens, which to me is not - to me, I think, is not right in this emergency environment. So they are using their EUA to actually, you know - I'm at a standstill because I would like to buy their - I'd like to buy lots of their kits, but they won't sell them to me because I won't sign that.

Tim Stenzel (FDA IVD Director):
Okay. I understand better. Thanks for explaining that.

Ken Kim:
Yes. So that's the problem. It's really frustrating because, you know, on the fields we definitely want to use this as a point of care test. It's great. But I don't know whether this is legal for them to take an EUA and actually create a market lock that anyone who starts using these we're locked in with them for three years. We can't use another antigen test when another one gets approved. You see what the problem is?

Tim Stenzel (FDA IVD Director):
Yes. Yes, no, I see. Let me note this and we'll look internally at this unintelligible...

Ken Kim:
I can talk offline.

Tim Stenzel (FDA IVD Director):
Yes, talking offline may be helpful too.

Ken Kim:
Yes. I - you know, I think - I typed it up in the email. So if you email me, I could set up a call, we could talk about it and I could send you the language, but I think it's a problem because that shouldn't - that - we're trying to actually do good things for the country in terms of diagnosing disease and you can't get situations where someone is going to lock you into something that, you know, NWX-FDA OC isn't really credible. Three months from now there will be another antigen that might be better and we can't - we wouldn't be able to switch to it legally.

Tim Stenzel (FDA IVD Director):
Okay. I certainly hear what you're saying and understand what you're saying and, you know, it's probably best if internally at the Agency we look into this and talk with you further. There's a lot of listeners on this call and, you know, there's obviously a good bit of transparency that goes on because there's a lot of listeners on this call. So - and we make ourselves available right now week in, week out here on this call. So I appreciate your calling. I would just add that we're very interested in additional antigen tests to be authorized. There seems to be a real shortage of developers in this space. So I would encourage anyone who wants to develop an antigen test, that's - they come talk to us and let's see what we can do because we are very interested in adding to the number of antigen tests.

Coordinator (FDA):
Thank you. Our next question will come from Shanivas Natribody. Your line is open.


---

## 2020-06-17_Virtual Town Hall 13_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing and EUA Processes


Coordinator (FDA):
Welcome and thank you for standing by. I'd like to inform all participants that today's call is being recorded. If you have any objections you may disconnect at this time. You have been placed in listen-only mode until the question-and- answer session of today's call. At that time if you would like to ask a question, please press star 1. And please make sure that your phone is unmuted, and record your name clearly when prompted, so I may announce you for your question. Thank you. And I would now like to turn the call over to your host, Ms. Kemba Ford. Thank you, ma'am. You may begin.

Kemba Ford (FDA):
Thank you, Missy. Hello, I am Kemba Ford of CDRH's Office of Communication and Education. Welcome to the FDA's 13th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during this public health emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, and the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, all from CDRH, will provide a brief update. NWX-FDA OC Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that may be under review. I would now turn the call over to Timothy.

Tim Stenzel (FDA IVD Director):
Hello everyone and thanks for joining us again. And I appreciate what everybody is doing to help in this current emergency. And we are going to do our best to address your questions today, and going forward, as well, as we have in the past. So there are a number of updates that both I and Toby Lowe will make today. You're probably aware that we made updates to the molecular EUA template, to include information about recommendations for validation of asymptomatic testing. If that is a claim that you want to make about your tests or assay. As well as for pooling. And that's pooling samples so that you might test more samples with given reagents. So obviously we're interested that accurate testing still occurs in those situations. And we do want to make it clear that EUAs are required for pooling and authorizations. And they are also required if you want to make a claim about the ability of your test or assay to detect asymptomatic viral positive patients. And obviously this applies mainly to molecular tests. But it could apply to direct antigen tests as well. Second, all that, if you are in a lab that's running a commercial test that's been authorized, and want to add either asymptomatic or pooling, you can work with the commercial test manufacturer. We are encouraging, obviously, those kit manufacturers to submit a EUA Amendment for these. If we can facilitate you working with the commercial manufacturer to add these additional NWX-FDA OC claims, we will do our part to do that. You can submit your own EUA if the manufacturer gives you Right of Reference to do so. It's just a simple, brief memo that says the agency can refer to data the manufacturer has filed when they review your validation data for pooling or asymptomatic. It has been our experience that most, if not all, manufacturers are very open to doing this for their customers. But we can't make that 100% assuring. Next, you may have seen press that we have revoked the Chembio Serology test. As we have worked with Serology developers in this emergency and pandemic, we have gained additional knowledge. We have raised the bar on the expectation for Serology performance. And Chembio unfortunately, was no longer able to meet that bar in subsequent evaluation. And so we have moved to revoke their authorization. As with all tests that have been removed from the notification list, the majority of those are, of course, if you've looked at that, are Serology tests. If you have inventory, we recommend that you reach out to the FDA if you are not interested in discarding that material. And if, of course, the developer hasn't asked you to do that. So we're working with all developers to appropriately triage inventory that may still be in the field. But if you feel like you've validated that and it's performing well in your hand, I've had that question before. Let's have a one- on-one dialogue. So you can reach out to our EUA Template email address. Next is that if you're a developer and you're having trouble getting clinical specimens to do your validation work, I'd like to refer you to our FAQ page NWX-FDA OC where there's information about validation material. More and more vendors are able to provide validation material for you. You can also look at our list of EUA authorized LDTs, and consider reaching out to any of those labs to see if they are able to provide any remnants of leftover specimens for your validation work. In this pandemic and emergency I've seen, you know, lots of folks pool resources. Get together and help one another. And that's - and we're so appreciative of that. And of course, any sort of IRB requirements should be followed and adhered to in that situation. Finally, for my talking points, before I turn it over to Toby, and before we open it up for questions, we have seen unprecedented volumes of submissions. Our Expert Team is working very hard, long days. We want all -- and this is at my direction within the office -- we want EUA submissions. This doesn't apply to pre-EUAs necessarily. But to EUA submissions where the application is complete, all data is there, and it's ready for us to review it. I want a directive that all EUA submissions should be assigned a contact within our office within two weeks of receipt. Now I've heard some, at least one-offs, where this hasn't happened. And we're going to correct that. And as part of that correction, if you're in that situation I'd like you to reach out through our EUA Template email address, to me, Timothy Stenzel. Just ask to have that email directed to me. And I will be ensuring personally, that you get assigned a contact within our office, that you can ask about status and get updates on a regular basis. So again, I'm going to step up and do that, to make sure that all are going assignments within two weeks. For those that received that, and send an NWX-FDA OC email, I'll be working to get those caught up as soon as possible. And I will work on that, as fast and as soon as possible. So with that, I will turn it over to Toby for her opening remarks.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Tim. Hi everyone. Thanks for joining us today. I just wanted to give a quick update. As many of you may have noticed, our EUA page has been restructured. While this may be a little bit shocking at first, we hope that the restructuring will ultimately make it easier to find what you're looking for. Previously on the Device EUA page, all device EUAs were on the same Web page which may have made it difficult to find what you were looking for. And specifically to find the IVD section. And all of the tests were grouped together in a single table. So this restructuring has created a standalone COVID-19 EUA Medical Device page with separate pages for each device type. So IVD EUAs now have their own page. If you had bookmarked the direct link to the IVD section of the EUA page previously, that should redirect you to the new IVD page. (Post meeting clarification - the old link to the IVD section does not redirect to the new page. The link to the new COVID-19 IVD EUA page is www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas). And then on the IVD page, now the EUAs are broken out into separate tables so that it will be easier to distinguish between authorizations for molecular tests, antigen tests, serology, and so on. So we hope that this will make things more streamlined and easier to find what you're looking for. If you have trouble with the page or if you notice anything that looks not correct, please reach out - you can reach out to me NWX-FDA OC directly, or you can reach out through the EUA mailbox. And they'll get that over to me. And we absolutely want to correct anything that we may not have gotten quite right with this restructuring. And unintelligible, if you have any feedback also on things that might be helpful, we'd love to hear that. And then another update is we just this morning posted a new FAQ on laboratory reporting requirements. This ties to the HHS guidance that was posted a couple of weeks ago, that I think we mentioned last week on the town hall regarding laboratory data reporting requirements. Set up a new FAQ that points over to the HHS Web page - or the HHS announcement, rather. And then as Tim mentioned, with the new templates that were posted yesterday that included information on asymptomatic testing and pooling, we also updated the FAQ page with new questions regarding that. So there are three new questions. Actually, one updated question and two new ones, regarding asymptomatic testing and surveillance testing. So we hope that those are helpful for you as well. And that's all I have today. We can open it up for questions now.

Coordinator (FDA):
Yes, ma'am it is now time for the question and answer session of today's call. If you would like to ask a question, please press star 1. Please make sure that your phone is unmuted and record your name clearly when prompted. First question comes from Shannon Clark. Your line is open.


---

## 2020-06-24_Virtual Town Hall 14_section-titles.md

#### 1. FDA Guidance on COVID-19 Testing Updates


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode until the question and answer session of the call. If you would like to ask a question during that time, please press star followed by the number 1. Today's conference is being recorded. Any objections, you may disconnect at this time. Now I'd like to turn over the meeting to Irene Aihie. Thank you. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 14th in a series of virtual town hall meetings to help answer technical questions about the development and validations of tests for SARS-CoV-2 during the Public Health Emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the lines for your questions related NWX-FDA OC to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Hi everyone. Thanks for joining us today. I'm going to start out by just giving a couple of updates on information that we've put on our Web site. We talked last week a little bit about the new information that we put up about polling and asymptomatic testing. We did get a couple of updated FAQs on that out shortly after last week's town hall. And then this morning we just updated a couple of our FAQs on validation and on the bridging policy and the modification policy in our guidance. So those updates were intended to better explain that our recommendation for validation for all tests including tests offered under the policies and the guidance as well as the tests that have submitted for an EUA prior to offering the test that our recommendations for validation for all of those are included in the policy guidance as well as in the EUA templates that are referenced from the guidance. We also clarified in the questions, FAQ, about the modifications policy and about bridging studies that the policy on modifications for use of a new specimen type does not reference bridging studies. So we would recommend that developers who are modifying an EUA authorized test for use of a new specimen type such as saliva, refer to the policy guidance and the molecular diagnostics template for information about our recommendations on validation for the new specimen type. We also clarified in that FAQ that for modifications to an EUA authorized test we have indicated that we don't expect a new EUA or an EUA amendment in certain situations, for modifications. But we clarified that that does mean that NWX-FDA OC the test is not under the original EUA, so it is being offered as a non- authorized test under the policies in the guidance if you follow that pathway. So those were a couple of the clarifications that we put out today. And then we - since we put out the FAQs last week including the FAQ on surveillance testing, we've gotten quite a few questions about the distinction between screening and surveillance and diagnostics testing in terms of testing asymptomatic individuals and testing different populations. So we're working on getting similar information out about that and I wanted to give a quick rundown of how we look at those different terms. So for surveillance, we generally think of that as looking for information at a population of community level. Obviously you'll be testing at an individual level but the purpose of surveillance testing is to gain information at that population level rather than to make individual decisions at an individual person level. Screening on the other hand, is looking for occurrence at the individual level in situations where there might not be a specific reason for that individual to suspect that they would have COVID-19. So where you might be looking at all employees returning to a workplace or all students or faculty coming back to a school. Things like that we would consider to be screening because we are looking to make a decision at the individual level there. And then obviously diagnostic testing also looking for occurrence at the individual level, but that's done when there's a particular reason for that individual to be suspected that they may be infected. And so as we have discussed previously, the tests that we've authorized so far that are indicated for individuals suspected of COVID-19, by a healthcare provider, are generally indicated that that diagnostic testing level where there is a reason to believe that individual may be infected. And any asymptomatic testing is done at the discretion of the ordering healthcare NWX-FDA OC provider. So I'd like to provide a little bit of clarification on that. Hopefully that's helpful. And now I'll turn it over to Tim, for his update.

Tim Stenzel (FDA IVD Director):
Thanks, Toby. Yes. So we're going to try to provide even more sort of helpful hints and tips today on making this whole process efficient for everybody and for aiding everyone in arriving at a decision of EUA authorizations as soon as possible. So last week I asked folks to contact me if they had not been assigned a contact within two weeks of their EUA submission. That's EUA not a pre-EUA. And it's my understanding that as of today, all of those subject EUA submissions have a contact and still there is the opportunity to reach out to me for EUAs that have not been assigned a contact within two weeks of the date of submission. We are now also focusing our attention on pre-EUA and where there are templates that we've provided under guidance with recommendations that would apply to a given pre-EUA, we would ask whenever possible, to use those templates to guide the process. If there is something in your development or in your plan that is not in the template as far as there are not recommendations because you have something that's not been covered, we want to in particular, focus our attention on providing developer's that feedback that is not present in guidance or templates. I want to re-review or review as a priority EUA submission and for our review staff, which are quite busy. These are EUAs that have data even if all the studies aren't complete we want to review priority submissions on a rolling basis. So any applications deemed high priority and have data such as point of care, such as high throughput automated instruments such as, you know, those are - in both those - the situations at the point of care that does require EUA NWX-FDA OC authorization, the high through put should be obviously and that would be a priority. And then also for any home collection where there's data or there's home testing where there is data for us to review. And obviously with home collection and home testing those activities require an EUA before authorization. You know, in working with our reviewers, we would ask that when all reviewers ask for additional information, additional analyses of data that maybe you've already provided, or any new data that may be required to complete a review, we would ask that you please provide that as soon as possible. And this states that many times we are - will be unable to advance the application until we get that requested information. And so we would ask that, you know, that that be addressed as soon as we can, when you get those requests. Next is a general update. We are obviously now posting all NCI results. Once a decision has been made, a regulatory decision has been made, and once we complete the QC and QA of those reports. So hopefully, soon after the decision we can post those. And as of today, there are results for 21 of the tests that have been submitted to the NCI and they are now public. So that is present - that link is present on our EUA page. All right. so another helpful hint here is if you could provide information regarding test validation using the templates that have been made available online if possible, we would greatly appreciate that. And the better organized and the greater the clarity of the information that's provided to really assist our reviewers to efficiently review that. If there is something, for example, that they don't understand about the application that, you know, they will reach out and ask you questions. And NWX-FDA OC that obviously takes time to do that. So, thanks in advance for helping us in that way. Also, if the templates have been updated since you provided information, I would ask that you track that. And you may want to proactively reach out to our reviewers or the contacts, to ask if those updates might apply to you and determine what might be asked for there. And so proactivity on both of our parts will help speed these reviews. Specifically regarding the serology template and the information that we will - that we asked for in that template, please remember to provide data that is specific to each sample that's evaluated in your validation studies. These are also called line data. And for clinical agreement study this should include the date the specimen was collected for evaluation with the serology test, the date the specimen was collected for the PCR comparative results, the sample type evaluated plasma, serum, whole blood, finger prick, whatever, and the day from symptom onset to the date the specimen was collected, for evaluation with the serology test, the result of the PCR test and obviously the serology result. If the serology test reports IGM as well as IGG, these results should be provided in separate columns in this line data format. Obviously timing of the various tests and symptom onset is obviously important to understand the true performance of the test. You know, we do look at what are the results after symptom onset; what are the results in days after PCR results? So that helps us to understand the true performance of the test and when a test might turn positive. It also informs future users of that test so that they understand those kinds of performance characteristics. And then also, when you do study protocols for each validation study, please provide those predefined study protocols electronically, to our review staff, so they can fully understand the validation NWX-FDA OC testing that you performed with your tests and the measures you used to determine if your test met its pre-specified, predefined performance targets. And with that, we can turn it over to the operator for questions and we look forward to the rest of the call. Thank you.

Coordinator (FDA):
Thank you. We will now begin the question and answer session. If you'd like to ask a question please press star 1, unmute your phone, and record your name clearly. Once again, to ask a question, please press star followed by the number 1. Our first question comes from Mark Heckman. Your line is open.

Tim Stenzel (FDA IVD Director):
Hello, Mark. Make sure you're not on mute.


---

## 2020-07-01_Virtual Town Hall 15_section-titles.md

#### 1. FDA Updates and Guidance on SARS-CoV-2 Testing


Coordinator (FDA):
Good afternoon. And thank you all for standing by. For the duration of today's conference all participants' lines are on a listen-only mode until the question and answer session. At that time if you would like to ask a question press Star 1. Today's call is being recorded. If you have any objections you may disconnect at this time. It is my pleasure to introduce Irene Aihie. Thank you ma'am. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I'm Irene Aihie of CDRH's Office of Communications and Communication. Welcome to the FDA's 15th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Timothy Stenzel the Director of the Office of In Vitro Diagnostics and Radiological Health and the Office of Product Evaluation and Quality and Toby Lowe Associate Director of the Office of In Vitro Diagnostics and Radiological Health - both in CDRH - will provide a brief update. Following opening remarks we will open the lines for your questions related NWX-FDA OC to today's discussion. Please remember that we are not able to respond to questions about specifics submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Hi everyone. Thanks Irene. So I just have a quick update today. We put out a couple updates to the FAQs last week. I believe they went out on Wednesday but I think it was after the town hall so I don't think I mentioned it. If I did and this is a repeat sorry about that. So the first question that we updated last week was the question about current validation study recommendations. And we updated that question to clarify that the recommendations for testing apply - the FDA's recommendations for testing apply both to tests for which an EUA request is submitted as well as tests that are claiming to be validated and offered under the policies in the guidance prior to submission of an EUA request. So those recommendations for validation are included in both the guidance and the accompanying EUA templates. So we encourage developers to consult those documents for those recommendations. And then the second question that we updated is the question on modifications to a previously authorized test. And the update in that question was to clarify a couple of points. The first is that modifications that are done by a high complexity CLIA Certified Lab under the policy in the guidance when we don't expect an EUA it does come outside of the scope of the EUA and therefore those tests are being offered as non-authorized tests. And then the other clarification was to point out that we have two different policies regarding modifications. One is for tests that are modifying to add a new specimen type. And the other is for all other types of modifications. And we're pointing out that for new specimen types the guidance does not include NWX-FDA OC validation using a bridging study. So that type of modification we are encouraging developers to reference the information in the guidance and the templates regarding recommendations for validation of a new specimen type. So those are all my updates for today.

Tim Stenzel (FDA IVD Director):
All right. Thank you Toby. This is Tim. Welcome this week to our town hall. I don't have that many updates. In fact I just have one important announcement to make. We have noticed a spike in complaints about one of the newest authorized molecular tests. It is the BD SARS-CoV-2 reagent for the BD MAX System. There are two sets of reagents that are authorized for the BD MAX System. This is only one of them and this announcement only applies to the BD SARS-CoV-2 reagent. It does not apply to the BioGX SARS-CoV-2 reagents. The new spikes in the complaints that we saw and have seen concern potential false-positive results. This appears to be a low level of approximately 3% of the overall positive results. So this is a small subset of the BD MAX positive results for this assay. For the time being out of an abundance of caution we are recommending that a positive result with this assay be treated as presumed positive and that you act accordingly when you are doing readings. So we are working closely with BD, very interactively with them to establish what the root cause is and what the correction will be and what the validation plan for their correction will be. Stay tuned for additional announcements which is incoming in the near future with more details about what to do about this. But for the time being please treat positive results as presumptive positive. And with that we turn - open this up to questions. Thank you. NWX-FDA OC

Coordinator (FDA):
Thank you. If you would like to ask a question please unmute your phone. Press Star 1. And record your first and last name clearly when prompted so I can introduce you. If you wish to withdraw your question press Star 2. Again to ask a question press Star 1. It may take a few moments for questions to come in. Please stand by. And our first question is from Lubna. You may ask your question.

Tim Stenzel (FDA IVD Director):
Hello.


---

## 2020-07-08_Virtual Town Hall 16_section-titles.md

#### 1. Updates on COVID-19 Testing and Device Authorization


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode. During the Q&A session if you'd like to ask a question you may press Star 1 on your phone. Today's call is being recorded if there are any objections, please disconnect at this time. And I like to turn the meeting over to Ms. Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA 16th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for the SARS COV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In vitro Diagnostics and Radiological Health both from CDRH will provide a brief update. Following opening remarks we will open line for your questions related to NWX-FDA OC US today's discussion. Please remember that we are not able to respond to questions about specific submission that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Welcome to our call today. We look forward to having great and productive dialogue with each caller. I would just ask that we, you know, continue along those veins and will all be great. You know, and otherwise we'll have to move to the next caller. And with that I will turn it over to Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Tim. Thanks everyone for joining us this afternoon. I have a few updates to share. We've had some recent inquiries so I want to share that we are welcoming certain immediate requests for collection devices that would otherwise need a 510k such as saliva collection devices. If you're interested in this please approach us through the templates email address and we can discuss if your device may be appropriate for that approach. We see this approach as being helpful to developers that want to use these devices and eliminate some of the validations that might otherwise be required for each individual assay. And we're also looking at other ways to ease the path to market for other devices during the emergency. So for collection device manufacturers who are interested in pursuing this we suggest that you take a look at the EUA template for home collection. It may not be a perfect fit but that template does include a lot of information that we would want to see for standalone collection devices such as stability and usability data. So as we continue to work through this, we'll continue to provide additional information regarding the process. And then moving on to some updates from last week and earlier this week we have updated FAQs and templates. So late last week we added an FAQ to NWX-FDA OC US clarify the difference between surveillance, screening and diagnostic testing for COVID-19. We previewed that a little bit in the discussion last week on this call. And that last week and again earlier this week we provided updates to the molecular EUA template. So the first update late last week was to add information about multi-analyte respiratory panels under EUA. As we approach flu season, we're encouraging developers to consider tests that will include SARS CoV-2 along with influenza and potentially other respiratory pathogens. And then the second update earlier this week was to include more detailed recommendations on validations for pooling. We're encouraging commercial test kit manufacturers to submit EUA amendments to authorize pooling of your assays so that labs can implement this approach. That will be much more streamlined than that each lab having to perform their own validation and submit their own EUA to add pooling. And then a few other updates, last week we also authorized CDC's combination SARS COV-2 and influenza multiplex test. So that's the third EUA that we've issued for a combination test like this. BioFire and Qiagen both previously added SARS COV-2 to their previously cleared respiratory panel. And last week we also issued an EUA for the second COVID-19 antigen test. That was to Becton Dickinson BD for their BD Veritor system for rapid detection of SARS COV-2. And then on Monday this week we issued a letter to clinical laboratory staff and healthcare providers about false positive results with one of the authorized BD molecular tests. And Tim mentioned that issue on last week's town hall as well so that letter can be found on our Web site as well. And that's all I have as an intro so we can turn NWX-FDA OC US it over to questions.

Coordinator (FDA):
The phone lines are now open for questions. If you'd like to ask a question over the phone please press Star 1 and record your name. Also please limit yourself to one question. If you'd like to withdraw your question press Star 2. Thank you. First question in the queue is from Lily Wong. Your line is now open.


---

## 2020-07-15_Virtual Town Hall 17_section-titles.md

#### 1. FDA Updates and Q&A on SARS-CoV-2 Testing


Coordinator (FDA):
Good afternoon and thank you all for standing by. For the duration of today's conference, all participants' lines are on listen-only mode until the question-and-answer session. At that time, if you have a question you may press star 1. Today's call is being recorded. If you have any objections you may disconnect at this time. It is my pleasure to introduce Irene Aihie. Thank you, ma'am. You may begin.

Irene Aihie (FDA Moderator):
Hello, I am Irene Aihie, of CDRH's Office of Communication and Education. Welcome to the FDA's 17th in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about FDA Townhall specific submissions that might be under review. Now, I give you Timothy…

Tim Stenzel (FDA IVD Director):
Welcome everyone to this week's call and thanks for all that you're doing, during this emergency. I'm going to turn it over now to Toby, for some opening updates and then we'll open it for questions. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Tim. Thanks, everyone for joining us today. Just a quick update today, this morning we made some updates on our FAQ page to the question about obtaining viral transport media and swab alternatives. The edits were primarily for clarification and additional language around the warning regarding media that includes guanidine thiocyanate or similar chemicals. And then the other update that we made this morning was to add a new question under the "What test should no longer be used or distributed?" section, and that is for laboratories that had previously provided notification under the policy in section 4A of the guidance but has now been removed from the notification list and the tests should no longer be used. So those are the only updates that we've made to the FAQs since last week's call I believe. And now we can open things up for questions.

Coordinator (FDA):
Thank you. And if you would like to ask a question please unmute your phone, press star 1 and record your first and last name clearly when prompted, so I may introduce you. Again, that is star 1 if you have a question. Our first question is from C. Wolfe. Your line is open.


---

## 2020-07-22_Virtual Town Hall 18_section-titles.md

#### 1. FDA Updates on COVID-19 Testing Policies and Guidance


Coordinator (FDA):
Good afternoon and thank you all for standing by. For the duration of today's conference, all participants' lines are in a listen-only mode until the question and answer session. At that time if you would like to ask a question press Star 1. Today's call is being recorded. If you have any objections you may disconnect at this time. It is my pleasure to introduce Miss Irene Aihie. Thank you, ma'am, you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie of the CRHs Office of Communication and Education. Welcome to the FDAs 18th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health both through CDRH and provide a brief update. Following opening remarks we will open the lines and take your questions related to today's session. Please remember that we are not able to respond to questions about specific admissions that might be under review. Now I give you Toby… NWX-FDA OC US

Toby Lowe (FDA IVD Assoc Director):
Hi everyone. Thanks for joining us today. Just a couple of updates from last week or since last week rather. Earlier this week we issued a new FDA Voices blog post by Dr. Shuren and that discusses our ongoing work supporting and advancing COVID-19 diagnostic test accuracy and availability. And that can be found on the FDA Web site. We also earlier this week issued a guidance document on transport media. I know we've had a lot of questions on that topic in the town halls recently. And so I hope that everyone finds that useful. The document is about our enforcement policies for viral transport media during the COVID-19 public health emergency. And it outlines a few different policies for commercial manufacturers of VTM and sterile PPS and saline as well as high complexity CLIA certified laboratories that are developing their own transport media. Along with that guidance we've put out a new FAQ page specific to viral transport media and questions related to that new guidance document. The easiest way to find that FAQ is probably from the testing FAQ page where we link over to that new FAQ page. We also updated a couple of the testing supplies related FAQs on the test FAQ page. There were a lot of FAQs in that sentence - sorry about that. And then the last update that I have today is that we have revoked the umbrella EUA for serology tests. From our perspective we see this as fairly administrative. In the three months since we issued that umbrella EUA no tests have been added to it because we found that it is more appropriate for us to individualize the EUAs for each specific test so that we can allow for a broader indication for scopes of authorization on individualized conditions of authorization that are specific to each unique test. So this is - we had intended for the umbrella EUA to remind the administrator NWX-FDA OC US of progress from our end. But it turns out that doing individual EUAs is actually the more streamlined process for us. So this does not change anything from the perspective of what we expect to see in EUA requests. We're still using the NCI data to inform our decisions for the individual EUAs as we have been doing and we will continue to do that. But we did just want to flag that for you. And with that I'll turn it over to Tim.

Tim Stenzel (FDA IVD Director):
Thank you Toby and hello everyone. Thanks again for joining us. I'm just going to give you some updates. So maybe that can address some potential questions. We are working on a number of template additions and updates. And unfortunately, they're not publicly available yet although if any developer has any questions on any of these topics send us an email to the template email address box. And we've given quite a bit of thought to most of these already and can provide feedback. So that includes what we used to call home testing for molecular diagnostics indirect antigen. That will be transitioning to being called a non-laboratory testing because the setting may not always be home could be schools or places, et cetera. We're working on updates to the regular molecular template to include more information about pooling, more information about simple, or Dorfman pooling as well as what to do if you want to pool swabs. We're also updating language having to do with development of multi-analyte tests including things, like, Flu A, Flu B in addition to SARS. We are working on finalizing what used to be called the serology home collection which will now be the non-laboratory serology collection template. We are working also a little bit further out will be what we used to refer to as NWX-FDA OC US serology home testing which will now be serology non-laboratory testing. And then finally we've been requested to update our direct antigen template to allow for recommendations for multi-analyte testing. So just like molecular with direct antigen you can put more than one target on the direct antigen test so you could for example look at Flu A and B again in addition to SARS. And so with that update from Toby - those updates from Toby and me we can go ahead and take some questions now. Thank you.

Coordinator (FDA):
Thank you. If you would like to ask a question please unmute your phone, press Star 1 and record your name clearly when prompted so I may introduce you. If you would like to withdraw your question you may press Star 2. Again to ask a question press Star 1. It may take a few moments for questions to come in. Please standby. And our first question is from Jackie Chan. Your line is open.

---

#### 5. EUA Submission Process and Reporting Responsibilities Explained


Elaine Barry:
Hi good afternoon. Thanks for taking my call. I'm a little new at this and I was listening, you know, I've been listening for a couple of weeks. I was just wondering if you could kind of take me through the process of the EUA template submission. So, like, once the templates are populated and submitted how long does it typically take for someone to review it and respond and what kind of a response can we expect? Will it be, like, a feasibility assessment or specific guidance? One of the products that I'm facilitating has unintelligible. I'm really anxious to get word from you to know whether we can proceed and how we can proceed.

Tim Stenzel (FDA IVD Director):
You're breaking up a little bit when you were describing what the technology was that you were considering submitting. Can you just go over that again so I know what kind of test it is?

Elaine Barry:
Actually I'm not really at liberty to say. But it is does have military readiness applications. And we're just wondering, like, what kind of guidance might we expect from the EUA or the review and how long that might take once we submit to get some kind of response. NWX-FDA OC US

Tim Stenzel (FDA IVD Director):
Okay can you tell me whether it fits in the bucket of serology, molecular or direct antigen?

Elaine Barry:
Yes serology.

Tim Stenzel (FDA IVD Director):
Okay serology. So serology are allowed to submit or at least validate and notify us. And then we'll review that notification and we can decide to post that notification on our Web site. And then if you certified that you validated for the intended purposes following the guidelines you can begin marketing that test while we review that submission. We will do an initial assessment of that submission to make sure there are no public health concerns. To make sure that it is complete. And to assess whether it is one of the high priorities. The reason for high priority is we've gotten so many applications needing so many high priority applications that especially those that require EUA authorization to be able to market the test versus a serology test that can be marketed following notification. You know we want to get to those applications first that require our review and authorization. So and both assessments will be done. If there's any concerns whether it's incomplete or we think the data doesn't look good we will reach back out to you. If it is classified as a high priority as soon as there is room on the reviewer's plate, they'll move that in ahead of lower priority application. And if you're deemed to be a lower priority application you will still be given a contact to keep you updated weekly on your submission and be able to ask questions, and get any sort of reassurances that you need about where things stand. I've directed the office that within two weeks of those EUAs, hopefully a lot sooner than that now that we've cleared some backlog because there's hundreds NWX-FDA OC US of applications, that we can get to that much quicker than two weeks. So you should hopefully get an assignment - a user, reviewer or somebody that you can otherwise contact to get a status update. Hopefully that clarifies that process.

Elaine Barry:
Yes it does thank you very much. And in the event that we wouldn't be able to go down that EUA pathway should we just go ahead and, you know, start preparing for an IDE submission?

Tim Stenzel (FDA IVD Director):
So an IDE we've typically not been reviewing IDEs for this pandemic. So it would depend on the particular situation. And say you want to use it in a clinical trial situation where an IDE would be required, then yes. So you can email us at the template email address to address any concerns you might have about potential need for an IDE. But in most cases, we haven't seen a need for an IDE but you may have special circumstances.

Elaine Barry:
That's kind of what I thought. Okay great, thank you so much.

Tim Stenzel (FDA IVD Director):
Yes.

Coordinator (FDA):
And before we go to the next question just as a reminder, we are taking one question per caller. Our next question comes from Todd Lewis. You may go ahead.

Toby Lowe (FDA IVD Assoc Director):
Hello. Our lab is conducting a lateral flow assay for COVID. And my question is who is responsible for reporting the results? Do you know that answer? Is it the clinical lab or is it - if we're going through a practitioner do, we report to the practitioner and then practitioner reports it to the...

Tim Stenzel (FDA IVD Director):
Yes, if the testing is being done in a CLIA lab and they're high, moderate or waived. It is the laboratory's responsibility to report that result. If you're going NWX-FDA OC US to develop a test that might be used in a non-laboratory setting, then we are asking reviewers what your plan is to make that data available to the government so that we can track that information. So we just upfront want to hear your plan about how you would do that. But if the testing is all done within a CLIA lab it's the CLIA lab's responsibility.

Toby Lowe (FDA IVD Assoc Director):
Okay. And is there a central location to report that or what agency would that be through?

Tim Stenzel (FDA IVD Director):
Well those are details you would - I think Toby do you know? I think you go through the regular reporting which may be directly to the CDC. But I know the department also has a different system. You know what this was set up I believe by the CDC not by the FDA...

Toby Lowe (FDA IVD Assoc Director):
Okay.

Tim Stenzel (FDA IVD Director):
...and/or the HHS. So I would refer you to them unless, Toby, you can provide any additional assistance.

Toby Lowe (FDA IVD Assoc Director):
There's a guidance that HHS put out about laboratory data reporting and what goes with it.

Toby Lowe (FDA IVD Assoc Director):
Okay.

Toby Lowe (FDA IVD Assoc Director):
We have that linked from our FAQ page. So if you go to our FAQ page to the section titled COVID-19 related test data and reporting FAQs, the first question has a link to the HHS guidance.

Toby Lowe (FDA IVD Assoc Director):
Okay thank you. NWX-FDA OC US

Toby Lowe (FDA IVD Assoc Director):
Yes.

Coordinator (FDA):
Our next question is from Wendy Jule your line is open.


---

## 2020-07-29_Virtual Town Hall 19_section-titles.md

#### 1. FDA Updates on Testing Templates and Validation Strategies


Coordinator (FDA):
Good afternoon and thank you all for standing by. For the duration of today's conference, all participant's lines are on a listen-only mode until the question and answer session. At that time if you would like to ask a question press star 1. Today's call is being recorded. If you have any objections you may disconnect at this time. It is my pleasure to introduce Ms. Irene Aihie. Thank you, ma'am. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 19th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-Co-V-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks, everyone for joining us on these town halls. I have a couple of updates. As we've discussed previously, we are - we've been working on updating some of our EUA templates that are available for you all to help facilitate your EUA submissions. And yesterday we updated the Molecular Diagnostic templates, both for commercial manufacturers and laboratories to include additional information on our recommendations for validation of pooling strategies. As well as, multi-analyte respiratory panels. And in the manufacturer template, also included recommendations for point-of-care testing. Along with those template updates yesterday, we updated the FAQs. So we updated the question on the FAQ page related to pooling. And we added questions related to point-of-care and multi-analyte respiratory panels. And then just before this call we finally got out the much anticipated, formerly known as, at-home test. Now known as non-laboratory use test template for manufacturers of molecular and antigen diagnostic tests. So that was just posted about 20 minutes ago, along with an update to the FAQ about those types of non-laboratory or at-home tests. And with that, I will turn it over to Tim.

Tim Stenzel (FDA IVD Director):
Thank you, Toby, and welcome everybody. We look forward to these conversations and assisting in any way that we can. A couple of updates. One is on LabCorp. Many, if not most of you, have seen that we have authorized LabCorp for both pooling and an asymptomatic claim. So this is the first authorization where the FDA has authorized a test developer to claim performance in the asymptomatic population. And we welcome additional, both pooling and asymptomatic submissions. I want to just briefly review pooling, and just make sure that everybody on the call today knows that we welcome pooling. With the template updates, we've provided even more information on pooling that find, we hope, to be helpful. Nothing really has changed in what our recommendations are for validation. But I do want to clarify the regulatory pathway for pooling. As we have seen highly variable results, even on the same platforms in different labs. We believe that the science here is still evolving. And we would like to be involved in the pooling. However, we've made it very regulatory friendly. That is, go ahead and validate your pool. We ask that you follow the recommendations if not, and contact us. But once you've validated the pooling, and if you follow our recommendations, you don't even, you know, need to have contact with us. Validate it. Once you validate it you can start pooling while you work on pulling the data together and submit it to us within 15 business days. We would ask that you notify us, as well, when you begin that pooling testing, and that you've finished validation, so we can be on the lookout for your data when it comes in. And then after you submit, and during that whole time, you can continue to test. As long as you don't experience any issues. And we'll receive it. I'll take a quick look at it. We'll assign it to a staff member. If we have any concerns we'll reach out. But all during this time, unless you hear from us, you can continue to test. So this is a bit on the honor system as we say, that the labs will do a good job validating this. And manufacturers, as well. And we look forward to working with you to expand testing in this way. And then one last update is that you may have seen yesterday, an amendment update for Quest testing - their LDT testing. They submitted a new extraction method that gives them greater throughput. Normally we don't make these updates that big a deal, although they're all important to all the developers. But the new update allows Quest to test 36,000 - that's 36K or 36,000 more tests - up to, more tests per day. And then if you add pooling on top of that, which they're already authorized to do pooling, then they can substantially increase the throughput. And we welcome working with all developers, including kits and labs, to help you know, provide more testing. And most of these pathways don't require an EUA authorization to get started. The new non-laboratory testing template that was just posted for molecular testing and direct antigen testing outside of a healthcare facility, will add additional testing as well. And then of course the non-laboratory collection also adds. So these are all the things that we are trying to do to help facilitate and to see implemented, additional testing across the country. And with that, we can turn this over to questions. And hopefully, we can give you some good answers. Thank you.

Coordinator (FDA):
Thank you. If you would like to ask a question, please unmute your phone, press star 1, and record your first and last name clearly when prompted so we may introduce you. Again, that is star 1 to ask a question. Our first question comes from Shannon Clark. You may go ahead.


---

## 2020-08-05_Virtual Town Hall 20_section-titles.md

#### 1. FDA Updates on EUA Applications and Pooling Strategies


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode until the question and answer session of today's conference. At that time to ask a question from the phone lines please press Star 1 and record your name when prompted. This conference is being recorded. If you have any objections please disconnect at this time. I would now like to turn the call over to your host. Irene Aihie. You may begin

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie, of CDRH's Office of Communication and Education. Welcome to the FDA's 20th in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following NWX-FDA OC US opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now, I give you Timothy…

Tim Stenzel (FDA IVD Director):
Thank you Irene and hello again everyone and thank you for joining us. And we greatly appreciate everything you're doing to help out in this pandemic. We passed a new milestone recently. We have authorized now over 200 tests in the EUA pathway. And thanks to many of you for that accomplishment. Without developers like yourselves doing this, we could not have achieved that goal. We are going to have many many more. __We have hundreds of EUA applications in house. And the vast majority of these have come through the notification pathway so that they are able to if they do that if that's allowed to them you are all able to go out and market your test prior to EUA authorization. It is the honor system. We expect that the validations have been done well, the performance is acceptable and we thank you for that. We allowed this pathway in this pandemic because of the absolute huge need to provide testing in abundance as soon as possible.__ And so please do bear with us as we go through these applications for EUA authorization. We obviously have to have a prioritizing so that we make the best decisions possible in all cases. So everyone's EUA is important and we will get to them. Please work closely with the contact that we've provided. Again for EUAs, not pre-EUAs, for EUAs direct to the office make sure that every EUA applicant has a contact within two weeks of submission hopefully less time now. And that's important that you have a contact that you can get at least weekly updates from. NWX-FDA OC US And __those that do require an EUA prior to launch they obviously get triaged.__ For those new submissions new technologies that require an EUA, they do get higher priority because they are waiting EUA authorization to be able to get to the market versus those who come through the notification pathway. The second update has to do with pooling. Of course there are, there's a greater need for tests than available tests and turnaround times at labs have increased. One of the potential solutions to this is that we find a way to pool. __Pooling in all cases appears to decrease the percent positive rate that is low positives are going to be missed.__ And that's just a given if you start pooling. We want to limit those misses to an acceptable level. __And our updated templates call for a PPA relative to single tests on the platform of 85%.__ __You can pool up to as many as you want as long as you hit that number.__ __We are asking for an even distribution of levels of positivity so a good range of low positive and high positives, up to high positives. So there's not an overabundance of either, an overabundance of low positives if it doesn't match your distribution in your lab which is the ideal thing is to match the distribution your lab sees then, you know, it's not as helpful. So we'll work closely with you to make sure that that distribution is good.__ The pathway for pooling additions both for kit developers as well as labs to alter kits and/or alter their own LDTs is through the notification pathways. So validate whatever pool scheme you want to use. Make sure the performance is good. On the honor system, you can notify us and submit your data within 15 days. All the while, 15 business days, all the while continuing the test pools unless you hear any concerns from us. NWX-FDA OC US And we'll get to those applications as soon as possible. They are a priority now so that we understand the variables that go into developing a pool scheme. There are multiple schemes. We have seen tremendous variability between labs that have tried to validate pooling even with the same kit. So for example somebody might fail the bar at a lower sample pool where another lab seems to pass and so we are gaining more and more information about why that might be. __It seems to be driven by two different things at least but these are probably the major drivers of pooling success. And that is the LOD of the assay.__ Obviously a more sensitive assay will be less likely to miss the average low positive than a test that is pooled that has not as great a sensitivity. And then second is the distribution of low positives in a given labs menu and experience. So it's important to understand historically what your low positive rate is. We like to see CTs historically for the labs to help them guide them to the right pool scheme. It will give them great performance with pooling and balance the need to increase throughput with getting an acceptable performance and not missing a lot of positives. And then finally I wanted to mention that recently we did authorize the first semi-quant serology test in fact there were two of them that we authorized semi-quant, quant and neutralizing antibody serology tests will be a priority going forward. There is a lot of interest relative to vaccines as you might guess. So we are working closely with any party that any developer that wants to advance development of these tests. And we look forward to more and more authorizations. It is a bit more complicated to semi-quant, a bit more complicated to do a neutralizing essay or to correlate a given serology test to a neutralizing assay. NWX-FDA OC US So we look forward to working with you. And with that, that ends our introductory remarks today and we can turn it over to questions. Thank you.

Irene Aihie (FDA Moderator):
Operator, we'll now take questions. Hello, operator are you there?

Coordinator (FDA):
Yes I'm here. My apologies. We will now begin a Q&A session. To ask a question over the phone lines please press Star 1 and ensure your phone is unmuted and record your name at the prompt. Your name is required to introduce your question. To withdraw your question press Star 2. One moment please for incoming questions. We do have a few questions in queue. One moment, please. Our first question comes from Elisa Maldonado-Colbert. Your line is open.


---

## 2020-08-26_Virtual Town Hall 23_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing Guidelines and Templates


Operator (FDA):
Good afternoon and thank you all for standing by. For the duration of today's conference, all participants' lines are in listen-only mode until the question and answer session. At that time if you a question press Star 1. Today's call is being recorded. If you have any objections you may disconnect at this time. It is my pleasure to introduce Miss Irene Aihie. Thank you, ma'am. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 23rd in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostic and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health both in CDRH will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific missions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Hello and thanks again for joining us and I look forward to today's call. Today we will not be answering any general questions about the HHS test statement of last week but we can address questions regarding data recommendations to support EUA authorization. If you have specific questions about your situation then please send them to cdrh-eua-templates@fda.hhs.gov and we'll work closely with you to address your specific questions. We do as I said earlier welcome any questions today about how to seek an EUA and the data and recommendations whether it is for an LDT or for a kit. Next, I wanted to lead into further discussion a little bit on our non-lab template that was recently posted. Now, this is primarily directed at home testing situation. Templates specifically addresses recommendations for molecular as well as direct antigen tests. They're also open to home serology tests. So just want to reiterate that the recommendations in there are just that, recommendations that if you have alternative ways of addressing the data and submission please reach out to us. We have set recommended levels of sensitivity and specificity. And there may be alternatives to achieving the goal of having a net positive benefit versus risk equation. So we remain flexible in approaches and we'll welcome dialogue around that. Also, there are in the templates there are mentioned there is mention that we'd like to hear from developers what their ideas are on reporting data and of course reporting data for maintaining, you know, vigilance on the public health situation with regards to, you know, how many positive tests to negative tests are being seen in the home or non-lab situation. You know, we think this is the important thing to facilitate if we can at the FDA. However not having a finalized plan or not having a clear plan on how that data can be transmitted will not hold up our review and our decision. In other words, we say it's not a review decision issue. It is important and we would like to facilitate anywhere can - reporting. And so we do invite hearing from you about that as well. We will continue this meeting into September on a weekly basis so we welcome your attendance next month as well. With that I'll like to turn it over to Toby. Thanks

Toby Lowe (FDA IVD Assoc Director):
Thanks, Tim. Hi everyone. A couple updates from information we've put out for the past week. On Monday put out ,we updated one of our FAQs. We have an FAQ on recommendations for health care providers using SARS CoV-2 diagnostic test for screening in asymptomatic individuals. And we updated on Monday to provide some additional clarity on our recommendations for health care providers using tests for asymptomatic screening including off-label use. And to go along with that we also on Monday posted a new Web page. We've had a lot of interest in screening testing and in pool sample testing. So we put up a new Web page on Monday that pulls together all of the available resources and recommendations that we've put out regarding pooling and screening testing. So with that, that Web page can be found it's linked from the main devices COVID-19 page. And there was also an email that went out probably to everyone on this call on Monday with that new Website. If you're having trouble finding it just let us know and hopefully the information on there will be helpful. And with that, we can get started with questions.

Irene Aihie (FDA Moderator):
Operator we'll now take questions. Please stand by while we - our operator gets back on the call.

Operator (FDA):
Thank you. If you would like to ask the question please ensure your phone is not muted. press Star 1 and when prompted clearly record your first and last name so I may introduce you. Again that is star 1 to ask a question. And our first question is from Ben Jamieson. Sir, you may go ahead.


---

## 2020-09-02_Virtual Town Hall 24_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Test Development Guidance


Operator (FDA):
Welcome and thank you for standing by. At this time, I'd like to inform all participants that today's call is being recorded. If you have any objections you may disconnect at this time. You have been placed in a listen-only mode until the question and answer session of today's call. At that time if you would like to ask a question, please press star followed by one. Please make sure that your phone is unmuted and record your name when prompted. Please allow yourself one question and one follow up. Questions will be taking -- be taken over the phone only. I would now like to turn the call over to your host, Ms. Irene Aihie. Thank you, ma'am you may begin. Page 2

Irene Aihie (FDA Moderator):
Thank you. Hello, I'm Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 24th in a series of virtual town hall meetings to help answer technical questions about the development and validations of tests for SARS-CoV-2 during the Public Health Emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality; and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the lines for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Hello, everyone, and thanks again for joining us today. We appreciate the dialogue that happens during these calls and the dialogue that happens in between these calls offline through our emails and other contacts. Page 3 We look forward to trying to help out again today. I wanted to just go over some remarks that I've made in previous public forums. First, regarding our templates that are posted on the website, we, first of all are working on a serology, non-lab or home collection template. And we're working on a serology home test or non-lab test template. And the progress there continues to go forward. And then regarding the templates that are already posted, we have recommendations in there on validation. And we have given a lot of thought to those recommendations. So we feel like those are good starting points for discussion. However, they are recommendations and we are open to alternatives. The other thing I wanted to make clear was for home use or non-lab tests for both molecular and antigen tests, we are very open to serial testing protocols in order to increase the PPA, or sensitivity of the essays. During the same period of time, that folks who have contracted the virus and are symptomatic, you know, in those first five to seven days or so, we really want to see good overall performance on detection of virus in that time Page 4 period. You know, and it would be a similar time period post infection for asymptomatic individuals. But we really would like to see, you know, good performance on detection of virus positive individuals during that period, which generally correlates, if not completely correlates with the period of maximum infectivity risk. So that individuals will get tested, know if they're at risk of spreading SARS or not and they can take appropriate actions to protect those they may come in contact with. And with that, I will turn it over to the operator for questions from callers. Thank you.

Operator (FDA):
Yes, sir. It is now time for the question and answer session of today's call. If you would like to ask a question over the phone, please press star followed by one. Please make sure that your phone is unmuted and record your name when prompted. Again, please allow yourself one question and one follow up. Thank you. Page 5 First question comes from Greg. Your line is open. First question comes from Greg Ping. Your line is open, sir.


---

## 2020-09-09_Virtual Town Hall 25_section-titles.md

#### 1. FDA Updates on COVID-19 Test Development Progress


Operator (FDA):
Welcome and thank you for standing by. At this time, all participants are on listen-only mode until our question-and-answer session. At that time, if you would like to ask a question please press star then one. Today's conference is being recorded. If you have any objections, you may disconnect at this time. And now, I would like to turn the meeting over to Ms. Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 25th in a series of virtual townhall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember if we are not able to respond to questions about specific submission that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Hi, everyone. Thanks for joining us again this week. I just have a couple updates this morning. We added a new question-and-answer to our FAQ page and updated a few of the existing questions. The new question is regarding leveraging validation data that has already been reviewed by the FDA for another test. We've had a lot of questions about the proper way to do that and proper way to use or right of reference. So we added some additional information about that to the question. And we also updated a couple of the questions to add information about the CDC multiplex tests because CDC has the right of reference to the performance data in their EUA for their Multi-Analyte Respiratory Panel. So we've also had questions about that and added information there. And we updated a couple of the questions in the testing supply FAQ section, specifically the questions related to extraction platforms and instruments for use with the CDC singleplex test. And that's all that I have today. So I'll turn it over to Tim for his update.

Tim Stenzel (FDA IVD Director):
Thank you, Toby. And welcome again, everyone, to this weekly call. We hold this call weekly to assist all developers of COVID-related tests to assist them in explaining any of our recommendations, to listen to concerns that we can sometimes address immediately or take back for consideration. It is an ongoing effort and extension of what we do day-in and day-out, every day of the week, and nearly every hour of the day in working with developers. So again, welcome. We are committed to being transparent and to giving us a direct response as we can on the effort to help. I don't usually note up-to-date the number of authorizations we've made, and I make this as long as these calls go on at least a monthly update. To date, we have authorized 243 tests, and it includes 195 on molecular diagnostic tests, 44 antibody or serology tests, and four antigen or direct antigen rapid tests. We definitely are interested in seeing more submissions for the direct rapid antigen tests. We just haven't seen as many of those as we have seen in the others, and that's reflected in the relative number of authorizations. However, we also in addition to these authorizations, offer very flexible policies that have allowed more than a hundred other tests, frankly hundreds of tests to be on the market while their EUAs are under review and consideration. So in total, the amount of tests that are in the market undergoing review or already authorized are in the many hundreds. I did want to also open up that we are eager to authorize as many antigen tests and molecular diagnostic point of care and home tests as possible. We have provided templates with our recommendations for both point of care antigen and molecular assays as well as in the non-lab or home situation. Our templates provide recommendations for validations. If you have alternate approaches, please engage with us through the cdrh-eua- templates@fda.hhs.gov email address and/or provide us with something to assess through pre-EUA submission. With regard to point of care tests, we would like to further assist developers in the pre-market validation period by opening, further opening up the chance for developers to use banked samples for their point of care studies. If the technology is amenable to that where they can use banked samples, then that may be a very good approach pre-market. We do ask that and work with the member of our team to define your study plan because we would like to mimic as near as possible those samples being handed off to a point of care tester in a manner similar to which they would normally see patients in the clinic and do an actual prospective collection and test so that we can mimic a busy clinical workplace and assess the performance of the test. So that is the loosening, further loosening under an EUA situation pre-market. There may, of course, be some post-market studies that are likely to be part of such an authorization. Similarly, we have heard from a lot of developers that accumulating asymptomatic samples for asymptomatic claims or over-the-counter tests has been a little bit more challenging than expected. So there are two ways that we suggest that can aid in the accumulation of asymptomatic patients. One is to team up with any of the large screening and/or surveillance programs, I'm looking at large populations. Of course, this is being done on many college campuses across the country. And if they identify a patient in their screening or surveillance, that's potentially a perfect opportunity to enroll that patient or that residual sample into the clinical study for asymptomatic claims. So that can be accomplished in a number of different ways. One is that it's banked samples can be used for your device from those testing efforts. And you can simply of all your local authorizations are achieved to use that sample for development of a commercial product allowed then you can use that banked sample. The other thing you can do is potentially call back any positives for re- collection. So we have been working with recently, very recently, with some who have tried to utilize this approach. And there has been some success in this. So we wanted to make that further awareness available to all developers. We also would like to start something new. Again, this is a pre-market validation assistance. We're open to, in addition to having a minimum number of asymptomatic patients pre-market, sometimes it's only as few as 10 or 20. We ask there be a minimum of 10 asymptomatic patients enrolled and tested. If in the case that 20 maybe required which is the most common number of samples that are asymptomatic to be required, we'll allow a minimum of 10 pre-market and the other 10 could be matched symptomatic samples and the matching process should be worked out with a member of our team but in general we'll be trying to find samples that reflect the viral loads, or CTs, or viral levels of those 10 asymptomatic patients who have been enrolled. If the requirement is for more than 20 asymptomatic which is in some cases where developers only want to seek an asymptomatic claim, there may be requirements for 30 asymptomatic samples and we are going to allow 15 of those 30 to be supplemented by symptomatic in the pre-market. Again, with the point of care studies there maybe requirements post-market to bring the total up to the recommended amounts. In both cases, we will obviously allow enough time for those studies to be completed post-market. The other thing I wanted to mention is that this morning the center director and I have published an opinion piece in The Hill. We hope you find our comments welcome. They are on all along the lines of what I just mentioned, our flexibility to adapt to the changing situation, adapt to the needs of developers and to speed access to technologies that will help. A lot of it has to do with point of care and or home type testing. We are very open to all developers who come to us with these ideas, and their tests. As I said earlier and from an opinion piece, our recommendations are just that, recommendations. The FDA is always open to alternative proposals from developers and we'll continue to consider those. There could be significant trade-offs and test accuracy that maybe appropriate where the need for availability and fast results is not being met. So for one example where our recommended levels of sensitivity may not be achieved with a single test result in a home situation, maybe with the paper strip test. Strategies utilizing serial testing, for less sensitive tests, could be deployed. Regarding serial testing, I mentioned this last week I believe. For example, what if the test had a 70 percent sensitivity? I also want to go into further detail about what we mean by 70 percent sensitivity. Let's just say that 70 percent sensitivity is what can be achieved with one test result. Well perhaps with a two-pack, two test results you can achieve a greater sensitivity together and maybe on a day one, day two, or day one, day three strategy. So the sensitivities can be such that one or the other being positive gives you a positive result. We are open to that kind of testing format to see that we're capturing, and this is where I'll go in to what we mean by sensitivity. In some senses, the absolute LOD of an assay doesn't matter as much especially in this home situation where you're trying to find folks who are carrying a level of virus that can infect others. So we typically think for symptomatic patients that the first five to seven days are some of the peak days for potential for infecting others with the virus. There's in all likelihood a very similar window for those who are without symptoms who are infected to start shedding virus and then eventually tail-off and are no longer shedding significant or any virus. We are really looking and as we've authorized our direct antigen tests, some of them have been authorized for five days post-symptoms because those are either the days that were studied in a clinical trial or those are the days at which performance was high enough to authorize. So some less sensitive tests may fall off more quickly after that five day period. That can be OK. We do want to see adequate sensitivity during those peak periods of virus shedding when patients are at most risk of being able to infect others. We think that by identification, of course, those individuals and isolating them, and treating them as needed we can do great good in reducing the incidence of new cases in the U.S. So with that, we will now turn it over to questions and answers.

Operator (FDA):
Thank you. As a reminder, if you would like to ask a question please press star, then one and record your name clearly when prompted. If you need to withdraw your question, you may do so by pressing star, then two. Our first question comes from Cory Yekkel. Your line is now open.


---

## 2020-09-16_Virtual Town Hall 26_section-titles.md

#### 1. False Positives and Testing Accuracy in SARS-CoV-2 Diagnostics


Coordinator (FDA):
Good afternoon and thank you all for standing by. For the duration of today's conference, all participants will enter on a listen-only mode until the question- and-answer session. At that time if you would like to ask a question, press star 1. Today's call is being recorded. If you have any objections, you may disconnect at this time. It is my pleasure to introduce Ms. Irene Aihie. Thank you, ma'am, you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 26th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-Co-V-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality from CDRH following opening remarks will provide a brief update. Following opening remarks, we will open the lines to discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now, I give you Timothy.

Tim Stenzel (FDA IVD Director):
Hello, everyone and thanks again for joining us today. It will just be me today. Toby is on a well-deserved leave and we hope that she is recharging her batteries and comes back strong next week and I did want to start-off with a few brief remarks. A topic that seems to be well-recognized now and we certainly made some public statements about certain tests is false positives so we are still dealing with some tests that have been publicly mentioned by the FDA and we continue to look for all signals whether they be significant false negatives or false positives and certainly pay a lot of attention to any sort of false results, work with those who are reporting issues as well as the test developers, understand the issues, see if there truly is an issue and if so, to quickly resolve that and quell that. And of course when something is known and decided to make that transparent to all of you, but in general false positives perhaps haven't received as much attention as false negatives but as we move into this pandemic and the response, you know, false positives are important to be aware of. They can occur, there's no perfect test and you know, we have gotten some recent reports and made public those that have been confirmed to be issues and I just wanted, you know, as we move into also, as we move the opening of schools and workplaces, some of the populations that get screened are potentially low you know, percent positive populations. And as we've talked about previously a while ago for serology tests even if molecular tests or an antigen test is quite specific and let's just plug-in some numbers into our PPV calculator and so if you plug-in a 95% sensitivity and a 99% specificity against the sensitivity 95 and specificity 99 so many would agree that's a fairly high-performing test. And if you put in a number of perhaps 0.2% positive but again that's 0.2, we have seen that relative level of positivity in a number of different populations who are doing screening or they're doing surveillance, you know, it's interesting because you plug that into a calculator for PPV or positive predictive value it's 1/6 or 16% and that's pretty low. That means that only one out of six positives is an actually true positive result. We know that in some clinical settings based on a single positive result that patients can be moved into a COVID ward where presumably everybody else has been confirmed positive to have COVID and may carry the virus, may carry infectious levels of the virus, may increase the risk of transmissibility to anyone who goes into that ward and here you'll have a potential patient who is falsely positive, may be in an at-risk group due to the age or previous conditions and goes into that increased-risk ward or area and may unfortunately, you know, contract the disease. So it's really important to not only understand the sensitivity and specificity of tests to the best of our ability but it's also important to understand what the positive predictive value for the population in that you're testing so let's hope that those remarks are helpful. Of course there's also the update that we've provided yesterday regarding the FDA SARS reference panel. We've made public announcements before about this panel. Yesterday we released the first batch of results on almost 60 tests and we hope that this information is helpful. We assessed relative LODs in three different ways, one for essentially the sample that used or test that uses - sample test that use - VTM and go into an extraction sort of chemistry from a liquid source and then we looked at dry swabs and separately we started looking at saliva. We think that within a sample type, we have three different tables and that's publicly available information. Within a table you can look at relative LOD and you can understand I think to a great degree based on how we ask the testing to be done and our analysis, we have a pretty good rank order, a lower LOD to a higher LOD within a table but making comparisons between tables are a little bit more difficult because the method of assessing the LOD was not exactly the same and we do put some details about how those how the panel was used for the different sample types so that those that go to the table and try to use it understand what those differences may be. So again we hope this publicly-available information on relative LODs will be helpful to the community. We have contacted a lot more developers in this first batch and so we're already working on finalizing LOD determinations for a lot more and we'll post as soon as we're ready to post the next batch. With that I think we can go into the Q&A portion of this meeting.

Coordinator (FDA):
Thank you. If you would like to ask a question, please unmute your phone, press star 1 and when prompted clearly record your first and last name so I may introduce you. Again to ask a question, press star 1. Our first question is from Alexis Sauer-Budge with Exponent. You may go ahead.


---

## 2020-09-23_Virtual Town Hall 27_section-titles.md

#### 1. FDA Virtual Town Hall: SARS-CoV-2 Testing Updates


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen only mode until the question and answer session of today's conference. At that time, you may press star 1 on your phone to ask a question. I would like to inform all parties that today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the conference over to Irene Aihie. Thank you, you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I'm Irene Aihie of CDRHs Office of Communication and Education. Welcome to the FDA 27th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2, during the public health emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality. And Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I'll give you Timothy.

Tim Stenzel (FDA IVD Director):
Thank you, Irene and welcome everyone to this week's call. We look forward to answering questions. And I just have a few brief introductory remarks. Mostly this is just going over some reminders. So, first of all, you know our templates contain important recommendations for validation and I encourage you to check those out. And then if folks, developers submit a pre-EUA and they ask questions that can be directly addressed by the templates, in order to assist us to most efficiently handle all of the applications that we get, we are going to typically close those by referencing the relevant templates. So we hope that works. If you have questions, you know that the templates don't go into them, that's where we'll focus most of our pre EUA response. And also, if there is something that you're asking that we haven't yet created a template or posted template, then obviously, that's important for us to see and provide feedback on. And again, the recommendations in the templates are exactly that, they are recommendations. We're are open to alternative validation strategies, we encourage you to check with us on those alternative strategies. So that we're all aligned prior to doing the work. And then finally, I just wanted to go over some of the top priorities for review and for application processing. This is not an all-inclusive list. But does include some of them. There remains a robust interest in pooling and in particular kit manufacturers who have pooling submissions that would allow those kit users in the labs that use that kit to immediately pool with minimal work and perhaps no bench work for their own lab. That obviously greatly amplifies our efforts around trying to promote the opportunities for pooling. So those would be priority. And then point of care tests, especially those that are molecular in antigen remain high priorities. As to those that help us to expand testing further and that includes home collection, and home testing, especially for molecular diagnostics and antigen testing. So, with that can then move into the question and answer phase and look forward to that. I don't believe Toby has any updates. So, she's here to assist me today. So, operator, we can go into the Q&A session.

Coordinator (FDA):
Thank you. We will now begin the question and answer session. If you would like to ask a question, please press star 1, unmute your phone and record your name clearly. Your name is required to introduce your question. If you need to withdraw your question, press star 2. Again, to ask a question, please press star 1. Our first question comes from Shannon Clark from User Wide.


---

## 2020-09-30_Virtual Town Hall 28_section-titles.md

#### 1. Improving Quality and Efficiency of EUA Submissions


Coordinator (FDA):
Today's conference call at this time your lines have been placed on listen-only for today's conference until the question-answer portion of our call. At which time you will be prompted to press star 1 on your touch-tone phone. Please ensure that your line is unmuted and please record your name when prompted so that I may introduce you to ask your question. Our conference is being recorded and if you have any objections you may disconnect at this time. I will now turn the conference over to our host Ms. Irene Aihie. Ma'am, you may proceed.

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie of the CDRH's Office of Communication and Education. FDA Virtual Townhall Welcome to the FDA 28th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health and Timothy Stenzel, Director of the Office of In Vitro Diagnostic and Radiological Health in the Office of Product Evaluation and Quality both from CDRH will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now, I give you, Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks everyone, for joining us today. My update today is that, we updated the Web site that we have for the reference panel comparative data this is the reference panel that we have been sending out to test developers to characterize their LOD in comparison to other tests. And we first published data two weeks ago and we just published some new data that's come in since that - the first batch where I believe we added somewhere around 20 to 25 new tests to the data that we posted there. And now I'll turn it over to Timothy for his update. FDA Virtual Townhall

Tim Stenzel (FDA IVD Director):
Thank you, Toby. And thanks to all for joining us again today. The first thing I wanted to do is to give a shout out to those who are critical and so important for us to put on these weekly calls. First of all, you're very familiar with Irene but her backup is Kemba. All of them get involved with transcribing this and then posting that. Of course Toby and the operators and everyone else. There is a little bit of an Echo. I apologize for that.

Irene Aihie (FDA Moderator):
Now you're better, Timothy.

Tim Stenzel (FDA IVD Director):
Is that clear? Okay. Thanks.

Irene Aihie (FDA Moderator):
Perfect. Good.

Toby Lowe (FDA IVD Assoc Director):
Sure thanks, Timothy.

Tim Stenzel (FDA IVD Director):
So thanks. Thanks, Irene, Vickie, Kemba, everyone. Okay, I wanted to speak about the quality of EUA submission. So it's important to have a complete, well-organized submission, including your validation protocols so we know that's how your validations were performed and whether or not those were accurately and correctly done. Those are all important in order for us to move swiftly towards an authorization decision. You know, our expert reviewers have expressed to me a growing frequency of getting bogged down with less than optimal submissions. FDA Virtual Townhall And they have spent valuable time working with these developers in trying to help. And the process, of course, has delayed review of other applications. __We're in a new phase now and we've authorized quite a few tests. And therefore we are going to take steps to correct the situation so that we can work through all submissions as quickly as possible.__ So please take steps to have, you know, the best quality submissions. If you've already submitted and you want to update and make updates to it, please do. And then when we have questions, please address them directly and clearly and as quickly and as completely as possible. So that we can work through those submissions with you and then move on to the others as quickly as possible. So I thank you all in advance for help with this. And so with that, we'll turn it over to question and answers. Hello.

Coordinator (FDA):
Your line is open.

Irene Aihie (FDA Moderator):
Timothy are you there?

Tim Stenzel (FDA IVD Director):
Yes.

Irene Aihie (FDA Moderator):
We can hear you.

Tim Stenzel (FDA IVD Director):
All right. Yes, moving to Q&A now if possible. FDA Virtual Townhall

Coordinator (FDA):
At this time, if you would like to ask a question, please press star 1 on your touch-tone phone. Please ensure that your line is unmuted and please record your name when prompted, so that I may introduce you to ask your question. Please stand by for questions. The first question is from Savannah SP your line is open.


---

## 2020-10-07_Virtual Town Hall 29_section-titles.md

#### 1. Positive Predictive Value Challenges in Low-Prevalence Populations


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode until the question-and-answer portion of today's call. During that time if you would like to ask a question over the phone line please press star 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 29th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality from CDRH, will provide a brief update. Following opening remarks, we will open the lines for your questions related to today's discussion. Please remember that FDA Virtual TH we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Thank you, Irene. And hello again, everyone. Today it will be me. Toby is on a well-deserved leave this week. So I have a few starting discussion points. The first thing that - relative to pre-EUA submissions, if a question that is asked in a pre-EUA is something that can be answered clearly and directly from a template that we've already posted, we will defer to that and not generally provide any more direct feedback. This will really help us triage these questions because we spend a great deal of time on unintelligible the templates and keeping them as up to date as we can. I've directed the office staff to cut and paste the relevant section into the email, if you send it by email, as well as to attach the full template. So I'm hoping that, that works for everybody because that would be a very efficient way of handling this. Next I wanted to revisit positive predictive value. It is - we get frequent questions about the application of positive predictive value, in particular I think for - currently, for rapid antigen tests. So everybody has seen various publications about potential false positives as there have been rollout and use in lower percent positive populations in nursing homes and other settings. And I just want to reiterate the value of looking at positive predictive value in assessing what to do with a positive result, specifically for a direct antigen test. But it can apply to any diagnostic test including molecular tests. Because in general, if the percent positivity is low in these populations, even with the relatively specific test, the number of false positives can be significant. FDA Virtual TH And therefore, we have recommended that, and the CDC does as well, that you confirm those results before taking any potential action, especially in regards patients. Obviously there's less - potentially less impact on healthcare workers if they have the false positive that can be confirmed to be false positive within a day or so. And then they don't need to be further quarantined if there's no other indication to do so. But with the patients there can be obviously a little bit more disruption. So it is very beneficial to have a plan in place to - when you utilize these tests, to have a plan in place to rapidly reflex those positive individuals to a second test. And work out a way that we can get a fairly rapid turnaround time on those critical. It's very clear in some of those preliminary data that I've seen, that the deployment of rapid antigen tests have been able to identify positives in low percent positive - true positive ways and low percent positive populations. And that this may have an incredibly valuable - be an incredibly valuable tool in the fight because you may be able to identify those positive individuals with the rapid antigen test which is not super sensitive. So you're not necessarily seeing, you know, late, you know, I'm not going to say late RNA shedding for example, but typically you're going to see patients who are potentially and most likely, have the ability to infect others. And so if you can identify those in 15, 20 minutes with a quick turnaround test on location, if you can identify those individuals you can enhance your ability to protect your staff and others unintelligible the staff. And I just want to go through a different set of numbers than I did last week or the week before, with regard to this PPV. So in this case I'm setting the percent positivity rate at just over 2%. It's actually 2.3%. The sensitivity of FDA Virtual TH the test I've dialed in 85% and the specificity I've dialed in at 98%. The positive predictive value for a positive result is then 50% in this population. I kind of selected these numbers to come up with a 50%. That means one out of two results is a true positive and one out of two results is on average, a false positive. So again, it just highlights that you can have a very specific test, 98%, in a prevalent population of a little bit over 2% and still see significant numbers of false positives. And in my view, there is nothing wrong with this test. It is just, you know, the importance of recognizing positive predictive value in low incident populations. And so the other thing I wanted to mention regarding direct imaging tests is there, because there has been a good bit of press about it, is whenever we get medical device reports or we get other signals of potential problems with any test and in particular, any EUA or COVID test. We do look into those NDRs and if warranted, we do an investigation. We of course, will reach out to the sponsors and understand what they know; review the complaints that they've received; and if we can confirm anything we will make that transparent to the community, the larger community, the testing community, clinical community through various means as soon as we can. And, you know, and I have nothing new to announce along those lines today, about direct antigen tests. So moving onto the final topic in my preliminary remarks, I did want to update an important new practice for this community. We've already issued a frequently asked question on our Web site and I do have prepared remarks for this. It is an important announcement. FDA Virtual TH So today the FDA issued a new frequently asked question for test developers to share an update on our prioritization of EUA requests. We recognize that we are currently in a different phase of the pandemic with respect to tests than we were previously. One second. Many COVID-19 tests are now authorized to be run in labs. Presently, over 250 EUAs for tests are authorized and over 400 tests are already being offered following notification under FDA's testing guidance. We prioritize review of EUA requests for tests taking into account a wide variety of factors, such as the public health need for the product and the availability of the product. And we have prioritized with you EUA requests for tests where authorization would increase testing accessibility such as point of care tests, home collection kits, and at home tests. And - or would significantly increase testing capacity, such as tests that reduce reliance on test supplies or high throughput and widely distributed tests. So all those should be relatively common sense as we go forward. In light of this and the recent HHS announcement that FDA will not require pre-market review of LDTs, to make the best use of our resources for the greatest public health benefit the FDA is declining to review EUA requests for LDTs at this time. FDA continues to prioritize review of EUA requests for point of care tests, home collection test kits, at home tests, tests that reduce reliance on test supplies, as well as high throughput, widely distributed tests. This approach will provide greater potential to improve the national testing capacity and permit FDA to take appropriate steps to assure that authorized tests may be effective. And so with that, I think we can open it up for the Q&A. Thank you. FDA Virtual TH

Coordinator (FDA):
Thank you. We will now begin the question and answer session. If you would like to ask a question, please press star 1, please unmute your phone and record your first and last name clearly when prompted. Your name is required to introduce your question. To withdraw your question you may press star 2. Once again, at this time if you would like to ask a question please press star 1. And our first question is from Shannon Clark. Your line is open.


---

## 2020-10-14_Virtual Town Hall 30_section-titles.md

#### 1. FDA Updates on SARS CoV-2 Testing Guidance


Coordinator (FDA):
Welcome and thank you for standing by. Today's call is being recorded. If you have any objections you may disconnect at this time. All participants are in a listen-only mode until the question and answer period. At that time, you may press Star 1 on your phone to ask a question. I would now like to turn the conference over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 30th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS CoV-2 during the public health emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health both from CDRH will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene. Hi everyone. Thanks for joining us again this week. I've got a couple of announcements that I wanted to share with you and then we can open up the line for questions. So the first thing I wanted to mention is last week in case folks didn't see it, we put out a letter to healthcare providers on recommendations on providing clear instructions to patients to self-collect an Anterior Nares Nasal sample in a healthcare setting for SARS CoV-2 testing. So that walked through the importance of having appropriate directions for patients who are self-collecting so that we make sure that they get a good sample prior to that sample being sent into the lab. And we link in that letter to healthcare provider to a couple of examples of it and instructions that can be used that, you know, are available for public use so providers can use those if there are not other instructions that they already have available so encourage folks to take a look at that. Along with that on the same day last week we also updated some of the FAQs related to swabs both in the testing supply FAQ section and the 3-D printed swabs FAQ section on the FAQ page. So take a look there for some updated information. And then yesterday we issued an immediately in effect guidance on enforcing the - sorry titled, the Enforcement Policy for Modifications to FDA Cleared Molecular Influenza and RSV Tests during the COVID-19 Public Health Emergency. We put this policy in place to help with the potential for shortages during the upcoming flu season since a lot of the flu and RSV tests use the same components as many of the SARS CoV-2 molecular assays. So this policy will help expand access to certain FDA cleared molecular tests intended for detection and identification of flu viruses. And it includes those influenza tests that also detect and identify RSV. And so that was issued yesterday and is posted up on our Web site as well. And with those updates we can go ahead and open line for questions. Thanks.

Irene Aihie (FDA Moderator):
Operator, we'll now take questions.

Coordinator (FDA):
If you would like to ask a question press - if you like to ask a question press Star 1 from your phone, unmute your line and speak your name clearly when prompted. Again, if you would like to ask a question press Star 1. One moment as we wait for any questions. There are currently no questions in queue.

Irene Aihie (FDA Moderator):
Operator can you get scripting one more time? I'm sure that we have questions folks are probably trying to get into the queue.

Coordinator (FDA):
If you would like to ask a question, press Star 1 from your phone, unmute your line and speak your name clearly when prompted. Again, if you would like to ask a question press Star 1. One moment as we wait for any questions. Our first question comes from Adam Beatty. Your line is now open.


---

## 2020-10-21_Virtual Town Hall 31_section-titles.md

#### 1. Addressing False Positives in COVID-19 Testing Strategies


Coordinator (FDA):
Good afternoon and thank you all for standing by. For the duration of today's conference all participants' lines are on a listen-only mode until the question- and-answer session. At that time, if you would like to ask a question press star 1. Today's call is being recorded. If you have any objections you may disconnect at this time. It is my pleasure to introduce Ms. Irene Aihie. Thank you ma'am, you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I'm Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 31st in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the lines for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Welcome everyone. A pleasure to be on the call again with all of you. So I appreciate all of your creative minds and dedication to addressing unmet COVID pandemic needs. We look forward to working with you. You may start to realize that you have additional folks who you've not met before. We've been hiring and we've been shifting some resources to try to work through all of the volumes of submissions as quickly as possible. We've been doing that since day one and we continue to do that. So hopefully that has a net positive influence on all of us. Just to start off, I wanted to talk about something that's very important to all of us as test developers and those involved with validation and authorization and use of these tests in this pandemic. It also applies to non-pandemic situations. I do want to help enlist your support and help in educating all of the various stakeholders who utilize these tests in different situations. So I wanted to talk about false positives again. We continue to hear about challenges relating to getting false positive results. And I would add, even in situations where it's totally expected that might seem odd. So first of all, there is no - I'm not aware of any perfect test. And I want to go back to my example of using a test, whether it be an antigen test or a molecular test. Neither - I don't know a single one that's perfect, that is 100% specific that is every time a patient is truly negative the test is negative. It just doesn't exist to my knowledge. So if we just assume for a second just for the math, that 99 - the specificity of any of these tests is 99%. It is 99 times out of 100 a patient who is negative will test negative. And only one time out of a 100 will a patient who is negative test positive. I think that's a very high specificity for almost any category of test. The challenge of course is if we begin to test in large scale screening, whether it's antigen or molecular, and we're screening populations that in particular, have a low percent positive rate, if that percent positive rate falls below the 1% false positive rate, it means that even for a perfectly well-functioning test it's a well-designed test, it's a well-validated test and the users who are performing the test are following the instruction, this, you know, according to the package insert, they are going to get a 1% false positive rate if the test is 99% specific. And it really doesn't matter if the patient is symptomatic or not. If the asymptomatic it applies the same. And it doesn't even really matter if a test has achieved a claim for screening asymptomatics. Specificity - is specificity typically going to be the same in all of these different populations for a given test format, a given sample type? And so the challenge is what do you do when the false positives which are totally expected, outnumber the true positives? I think it's important to say this is a totally expected situation and we plan for it. And we plan for it by - in those situations where the prevalence of positive disease, where the percent positive is low, significantly less or even in a, you know, even if it's a 1% positive rate you're going to have - half your positives are going to be false positives and half your positives are going to be true positives. So unless your percent positive rate is pretty high the idea that you might have as false positive is going to - if it's going to impact somebody's livelihood that is they may be asked to quarantine themselves for 14 plus days, or it involves putting a patient into a risky situation or healthcare workers aren't alerted to a patient having this or it determines outcome. You know, if they have flu they're going to treat somebody this way; if they have SARS they're going to treat them another. So all those situations matter. And you know your population is such that the false positive rate is not insignificant. And it's important and I would recommend that you get some sort of orthogonal confirmatory test done. I would prefer it be a molecular test of high specificity and sensitivity. You know, there is the option potentially of using another direct antigen test if your primary test is a direct antigen test. What I don't think we have a good handle on yet is whatever causes a false positive for one test, in particular a test that doesn't have an extraction of nucleic acid step up front, you know, if there's something in that sample that lends itself to a false positive result in a given individual, if you just fully go to another different orthogonal or direct antigen test, I just don't know at the moment and maybe somebody does, if you do please reach out to us through our Templates email address, you know, if that second direct antigen test will give you a true result based on the sample having certain potential characteristics that may lend itself in a direct antigen test to giving you a false positive. So I don't know. I think - I personally lack the information to give a recommendation on that. I would be very interested in seeing data about two orthogonal direct antigen tests and when you have a false positive, you know, can you use that orthogonal test to determine that? The other thing is if there is any sort of loss of sensitivity with a direct antigen second test, a high sensitive - a highly, highly specific molecular test is more likely to give you an accurate confirmation of whether you have disease or not. So that's the introductory remarks for today. Thanks again for joining us. And I look forward to your questions. Thank you so much.

Irene Aihie (FDA Moderator):
Operator, we'll now take questions.

Coordinator (FDA):
Thank you. If you would like to ask a question please make sure your phone is not muted, please press 1, star 1 and when prompted, clearly record your first and last name so I may introduce you. Again, to ask a question press star 1. Our first question is from Alberto Gambini. Sir, you may go ahead.

---

#### 6. Challenges in Validating Rapid Antigen Test Methods


Elliott Millinton:
I had a couple of questions. One is, is there a panel for an antigen test validation for a rapid antigen test?

Tim Stenzel (FDA IVD Director):
Not yet to my knowledge. And there have been fairly detailed discussions about what we can do in this area. One of the concerns relates to the prior conversation about the fact that this is a BSL-3 level virus and we - most folks don't have a BSL. Most developers in labs don't have a BSL-3 facility so that they can safely handle it. There are some, but most don't. And therefore, I'm just going to tell you that transparent issues that we're facing. So you can go ahead and inactivate that virus in a number of different ways. And then you want to make sure it actually still functions at the antigen level. And it's going to be challenging to, you know, provide that kind of assurance that it's going to behave just like Wild-Type, live virus. But we are looking into it or, you know, our methods of inactivation to make it safe. We are looking into how well it performs. We're also looking at potentially the opportunity to express antigen and make protein. And then obviously you get away from the need for inactivation because it's not whole virus and should be very nontoxic. So we're working on it and I'll say that we're working on it within the US government and there may be others outside the government who are working on it. We're just not ready to move forward but we certainly are very interested. So thank you for your question.

Elliott Millinton:
Thank you. And when you say you'd have to make sure the antigen still functions, first of all, do you have any preference for heat inactivated versus radiation inactivated? And how would you recommend determining whether it's still functioning?

Tim Stenzel (FDA IVD Director):
Yes. So I don't know that I have a preference there as far as I think, you know, the way to go about this is to try a potentially different method and conditions and see if it - see how robust that is. And then see how it impacts, you know, at least the EUA authorized antigen test. But again, they're not cookie cutter. The direct antigen tests are not cookie cutter. And if they are using antibodies that are different those antibodies then in most cases, are going to see a different epitope. And that could be very - different epitopes can be variably impacted by different methods of inactivation. Likewise if you began expecting proteins, if it doesn't - if the proteins aren't processed and get the non-nucleic acid directed modifications in the same way as in human cells then there could be alterations in performance. So they're just very clearly additional challenge when you try to develop a direct antigen reference panel as compared to a reference panel for molecular that we can basically inactivate, know that we inactivate, and know that if the RNA is there and stable that we'll have uniform good results.

Elliott Millinton:
Thank you. And one more question - for a - for validating an antigen test with saliva, can it be compared to a PCR test with saliva and do you have a preference as to whether it's a saliva sample for PCR or a nasal swab sample?

Tim Stenzel (FDA IVD Director):
I think that's a great question. I think it's important to - whenever you're doing kind of comparative tests, so just to make sure with the FDA staff in our office that it's an okay comparator. I would say that if it's an EUA authorized high sensitivity molecular method there's good chances that you could use saliva as the comparator, molecular saliva for the antigen comparison. But I would say it can depend and just double check with our team.

Toby Lowe (FDA IVD Assoc Director):
I don't have it up in front of me right now, but I believe the antigen template discusses appropriate comparators and specifically mentions no saliva. So if you are particularly interested in using saliva as a comparator I would recommend reaching out to the antigen team prior to beginning that study, to discuss that.

Elliott Millinton:
Great. Thank you.

Tim Stenzel (FDA IVD Director):
And that would be to an alteration to what's recommended. And, you know, over time our thinking can change and we try to remain open. Now that we have a lot more saliva experience the team's thoughts may have changed. I'm not going to speak for them though.

Elliott Millinton:
Thank you very much.

Coordinator (FDA):
Our next question is from Edward Strong. Go ahead sir. You may go ahead.


---

## 2020-10-28_Virtual Town Hall 32_section-titles.md

#### 1. FDA Virtual Town Hall: SARS-CoV-2 Test Updates


Coordinator (FDA):
Welcome and thank you for standing by. Today's call is being recorded. If you have any objections you may disconnect at this time. All participants are in a listen-only mode until the question-and-answer session of today's conference. And at that time you may press Star 1 on your phone to ask a question. I would now like to turn the call over to your host Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie of CDRH'S office of Communication and Education. Welcome to the FDA's 32nd in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS CoV-2 during the public health emergency. Today Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality here in CDRH will provide a brief update. She is joined by Dr. Brittany Schuck (FDA) and Dr. Kris Roth. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene. Hi everyone. Thanks for joining us again. Tim is not able to join us this week since he had a conflict so I've asked Kris and Brittany to join me to help with some of the more technical questions since as you all know I am a policy person. So a couple updates quickly before we get into questions. First just want to point out as we head into the end of the year, the schedule for the town halls may shift so keep an eye on your emails. Our team that handles the Webinars will make sure to send out emails with updates on the dates for the town halls in case they're not every week. And then the other update that I have is that earlier this week we updated the antigen template, the EUA template for antigen tests. And this update adds some recommendations regarding studies for screening of asymptomatic individuals and for multi-analyte antigen tests. So that template replaced the older one that was on our Web site and is available for test developers to use as you prepare your EUA request. And with that we can turn it over to questions.

Coordinator (FDA):
Thank you. We will now begin our question-and-answer session. If you'd like to ask a question over the phone lines please press Star 1 from your phone, unmute your line, and speak your name clearly when prompted. Your name is required to introduce your question. If you'd like to withdraw your question press Star 2. Again to ask a question over the phone line, please press Star then 1. One moment as we wait for our first question. Our first question comes from Shannon Clark. Your line is open.

---

#### 5. Equipment and Software Requirements for Reference Panel Validation


Gustavo Heteray:
Hi. Good afternoon. My name is Gustavo Heteray and my question is in reference to using a real-time PCR equipment to do the reference final validation. So we're trying to help a Chinese company called Enshare Biotech comply with the required reference panel. As such we have a question regarding the devices that may be used to perform the test. We have at our disposal an ABIs 7500 Fast Dx REAL-Time PCR instrument and a SLAN-96 P REAL-Time PCR system. However the IFU in the EUA mentions an ABIs 7500 REAL-Time PCR system. Is it possible to perform the reference panel using the ABIs 7500 Fast Dx REAL-Time PCR system or the SLAN-96 REAL-Time PCR system as we do not have access to the one mentioned in the IFU?

Toby Lowe (FDA IVD Assoc Director):
So if you're referring to performing the reference panel as a condition of the authorization which is typically what the - how the reference panel is currently being used then the performance of the reference panel does need to be in line with the instructions for use in - of the authorized test so that the - so that it does - it is reflective of the test that was authorized.

Gustavo Heteray:
Oh okay. They have introduced an amendment including the equipment that I have mentioned. But the amendment has not been reviewed. I guess maybe pending the reference panel results?

Toby Lowe (FDA IVD Assoc Director):
So I'm not able to answer any questions about a specific test. Generally we do expect the reference panel to be performed using the authorized test. If there is any specific questions about any, you know, an amendment or any authorizations there those should go directly to the review team.

Gustavo Heteray:
Okay then we'll find an equipment as mentioned in the IFU. And in regards to the software does the software have to be the exact same software or could be - could it be a more updated software on the equipment?

Toby Lowe (FDA IVD Assoc Director):
It should be the test as authorized.

Gustavo Heteray:
Okay all right well thanks a lot. That answers my question.

Toby Lowe (FDA IVD Assoc Director):
Great.

Coordinator (FDA):
Our next question comes from Arvita Tripati. Your line is open.


---

## 2020-11-04_Virtual Town Hall 33_section-titles.md

#### 1. False Positive Risks in Antigen Test Reporting


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen only mode until the question and answer session of today's call. At that time, if you would like to ask a question, you may press star 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie or CDRH's Office of Communications and Education. Welcome to the FDA's 33rd in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, here in CDRH, will provide a brief update. She is joined by Dr. Brittany Schuck and Dr. Kris Roth. Following opening remarks, we will open the lines for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene and thanks everyone, for joining us again this week. So I just have a quick update and I have seen that yesterday we issued a letter to Clinical Laboratories staff and healthcare providers regarding false positive results with antigen tests. So we put that out because we have become aware of reports of false positive results in nursing homes and other settings. And as we continue to monitor and evaluate these reports, we wanted to share some information with stakeholders about this risk and about stuff that can be taken by clinical laboratory staff and healthcare providers to help ensure the accurate reporting of test results. So that's available on our website and was also sent out by email yesterday. So a few of the key points there are to be aware of the information in the package insert for each test, which does include information about appropriate handling of the test cartridge or card -- excuse me -- at appropriate storage of those components. If they're not handled properly that can impact the performance of the test. And also about the time that it takes to read the results and being sure to read the results at the appropriate time since reading the test before or after that timeframe, can result in false positive or false negative results. We also include some information about minimizing the risk of cross contamination and pointing to the CDC guidance and recommendations about the use of PPE and changing gloves and also cleaning the instrument and the work area in between specimens. Then the other point that is made in that communication is about the positive predictive value. And just reminding everyone that false positives are expected with all tests. You know, any test that's out there will have some false positives and some false negatives. No test is perfect. And particularly with some of these tests being used to screen individuals in low prevalence areas, we do expect there to be a higher incidence of false positives as that prevalence decreases. So you can find that on our website and take a look at that and let us know if you have any questions. The only other update I have is just to remind everyone that we will not have a town hall next week. Wednesday of next week is Veteran's Day so we will be taking a break next week and we'll be back on the 18th. So with that, we can open the line for questions.

Coordinator (FDA):
If you would like to ask a question please press star 1 and record your name clearly when prompted. To withdraw your question you may press star 2. One moment please, for our first question. Our first question comes from Mark Hackman. Your line is open.


---

## 2020-11-18_Virtual Town Hall 34_section-titles.md

#### 1. FDA Updates on COVID-19 Testing Authorization


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in listen-only mode. At the end of today's presentation we will conduct a question and answer session. To ask a question please press Star 1. Today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie, you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I'm Irene Aihie of CDRH Office of Communication and Education. Welcome to the FDAs 34th in a series of virtual town hall meetings to help answer technical questions about the development and validation of test for SARS COV-2 during the public health emergency. Today, Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality. And Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now, I give you, Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene. Thanks everyone for joining us again. We're always glad to have a good audience, good discussion. So my update today is, you may have seen an email announcement that went out on Monday, regarding the FAQ website. I know a lot of you use that site regularly. And we did update it to restructure the entire page. So it looks quite different than it did before. The page had become fairly cumbersome to use with so much content that it became difficult to find what you're looking for. And it also became difficult for our web staff to maintain. So we've updated it to break it out into separate pages for the different sections of questions. And to break the question down into sections that hopefully makes them a little easier to find what you're looking for. And if you do find that it is difficult to use, or you have thoughts on ways to make it easier to use, please send those and we're always looking for feedback on that. And hopefully you'll find the information to be easier to navigate and to be useful. And we did also update a few questions while we did the restructuring and added some new information and mostly made some clarifying edits to questions that we had heard were a little bit confusing. Hopefully, that's helpful. And I will turn it over to Tim for his update.

Tim Stenzel (FDA IVD Director):
Thank you, Toby. Yes, welcome again to the session. Obviously, we have a little bit of big news. And that was released yesterday. The FDA has authorized the first COVID-19 test for self-testing at home. This is an entirely self-contained test. And it doesn't require a separate instance. Single use device. And it's a swab based test, molecular based test. And it's pretty good. About 94% PPA or sensitivity in that population. So it is by prescription. And so we had heard from a number of developers that they might seek the first home test through the prescription pathway as Jeff Shuren and I wrote in September and as I've mentioned multiple times, we are open to over the counter availability of testing, OTC for short. Both on the home collection side and on the home testing side. As far as I know, the last time I checked, that we have not received any EUAs with complete data for a home test that is over the counter. We look forward to authorizing the first over the counter home test. I think that's going to happen. I can't say exactly when that's going to happen. But again, this is big news of something that I'd hoped for and worked with our team and encouraged the community to develop - a long time. So I'm very happy to see this first example and should see many more coming in. The second topic I wanted to cover briefly. We continue to get a number of questions frequently about conversion from an EUA authorized test to a test that's fully authorized. For all the SARs related test, that pathway will likely, if not in all cases, be through the de novo pathway for the first submission. And then subsequent submissions after that first grant of de novo will be through the 510k pathway. And we'll work with -- if we get multiple submissions for de novos, we'll work with developers to authorize as soon as we can. But just so you know, not all - only the first submission is the one that is required to pay the de novo fee and we'll work with all others after that. And it's something that we've handled before prior to the pandemic. So once we grant that first de novo, there will be special controls written. These are special -- these are instructions for developers to follow in order to fall within the grant - that pathway, that newly created pathway regulation. To tell developers that this is what we expect to see. And obviously that's going to be in line with our thinking and interactive review that we share with developers, so that anyone who has submitted a de novo, will get that feedback from this. And then, you know, thereafter special controls and at first glance becomes publicly known and we post the summary statements, then that's for all to see about what our current thinking is, short of approaching this. We are inundated with both COVID related application and our normal volume of non COVID applications in our office. They are - the non COVID related applications are just as numerous as they have ever been, if not more. So we, you know, one of those things that we have decided that for Q subs and pre submissions is a bit challenging for us to answer all of those. So we do hope to provide more information as time goes along for, you know, what are what is our thinking about conversion. But a good guide would be, you know, what we've done for similar tests in the past. That will cover the vast bulk of questions, you know, is to look through previous authorization for respiratory viruses in recent ones, especially for and this is for 510k most of the time, for panel tests, for individual molecular tests, and the panel test could be antigen or molecular. And also for serology tests. So we do want to be as informative as we can area. However, our focus still remains on getting through the many, many EUA applications we have coming to a decision point. The current thought is that guidance is being drafted by OPEQ and the center that will cover diagnostics. And as soon as we can make that draft available we will. I can't promise when that will be available. But obviously we're thinking about this and thinking about how to provide developers with more directions. We're also - that will have important timeline. And we want to establish timelines for each of the technologies and the types of devices that makes sense. We hope that you feel that as well. We are really looking to support all COVID, really, developers through this process so that everybody has good chance to get through that conversion. And the timelines aren't too short. So stay tuned on that. I can't promise again when that draft guidance will be issued, but as soon as we can, we will. With that I think we can go to the open line and to Q&A. Thank you.

Coordinator (FDA):
Thank you. At this time, we will now begin the question and answer session. If you would like to ask a question, please press Star 1. Please unmute your phone and record your first and last name clearly when prompted. Your name is required to introduce your question. To withdraw your question, you may press Star 2. Once again, at this time, if you would like to ask a question, please press Star 1. And our first question is from Shannon Clark. Your line is open.


---

## 2020-12-02_Virtual Town Hall 35_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing Developments and Priorities


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are on listen-only mode until our question-and-answer session. At that time, if you would like to ask a question, please press star then 1. Today's conference is being recorded. If you have any objections, you may disconnect at this time. And now I would like to turn the meeting over to Ms. Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie or CDRH's Office of Communications and Education. Welcome to the FDA's 35th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks for joining us, everyone. I hope everyone had a nice Thanksgiving although this year is much different than normal Thanksgiving celebrations I'm sure. So just a couple updates today. This morning we updated two of our FAQs, one regarding antibody tests and what their purpose is, and one regarding testing supplies for extraction platforms for use with the CDC assay. An email blast went out this morning as well. So most of you probably received that already. This morning we also updated the data on our reference panel Web page. An email blast went out with that one as well. But check that out. Some additional tests were added to that page. And last week, we updated - or we posted two serology templates, EUA templates on our EUA page. One is the serology template for test developers and that replaced both the serology template for commercial manufacturers and the serology template for laboratories, so it's a single template for test developers now. And we also added a home specimen collection serology template for finger stick dried blood spot. So those are both available on the IVD EUA page. And with that, I will turn it over to Tim for his update.

Tim Stenzel (FDA IVD Director):
Oh, thank you, Toby. I hope everybody had a great Thanksgiving last week. And we stayed very busy, all of us. We see continuing increasing demand for testing, to reduce turnaround times for results, which we have seen have crept up recently, due to the overwhelming demand for testing. And I did want to reiterate our current thinking on the top, top, top priorities. And still probably mainly overall, for the office, although it doesn't functionally matter because we have separate teams for antigen, molecular and serology. So it doesn't mean that there's necessarily strong competition across those buckets for submissions. We do try to balance the review staff to the workload. Those silos or buckets, operate independently of one another, all the way through authorization and other decisions. What we're hearing and what we believe is absolutely needed, is more availability for point of care tests, more availability for prescription home collection and prescription home tests, as well as OTC collection and OTC testing. And so those basically are our top priority. Panels that include flu and other respiratory viruses also are a priority. As are truly steps forward in throughput capability for central lab tests. And so probably none of those are surprises to anyone. And we remain eager to authorize good tests in those categories as soon as possible. Just some pointers - Toby mentioned that we made available a template now that was cleared. And we have been providing advice on a case by case basis, for serology home collection by blood spot. And so we're happy to make that that is cleared and that is on our Web site and available for developers who are interested in that. You know, there are perhaps volume requirements for home serology collection and home serology testing. So we advise developers to pay attention to what those volume requirement are. Obviously, we've got to have enough of a sample in order to get an accurate result. And how that - and how to make that as easy as possible, for end users for the patients and those who would buy an OTC test for those studies. Just a heads up to pay attention to those needs for your assay and then how you make the validation, you know, in the home use either by prescription or OTC environment in the most expeditious study manner. Okay. I wanted to spend a brief time on talking about particularly for I think molecular assays, we've authorized some semi-quant and quant assays. We spent - we've already authorized some serology quant assays. You know, we really have either few or none depending on the category in non-serology quant and semi-quant submissions. We do think that this is going to pick up because there seems to be an interest in having it, you know, semi-quant and quant molecular assays and perhaps antigen assays. So that, you know, clinicians have an additional tool to make some assessments. Now what exactly the quantitative results or semi-quant results will translate into as far as clinical benefit is unknown. But we're very interested in as an office, to make good tools, as accurate and precise tools available, for those who would like it. So obviously in molecular assays, people have been looking at cycle thresholds. Of course cycle thresholds have a relationship to the amount of intact virus in the sample. Due to sampling variabilities, other issues having to do with viral stability, exactly how that precisely and accurately correlates to what's going on in the patients, maybe a different question. On a case - individual patient by individual patient basis, there are potential challenges in interpreting CT results. There are also technical hurdles with CTs. So CTs across molecular assays that aren't made semi-quant or quant, so that you're actually not really focusing on CTs but you're focusing on actual viral target levels. But if you just try to compare CTs assay to assay and you haven't controlled for variables, that's an imprecise, inaccurate, challenging correlation. And even for a given assay there could be - there absolutely is the chance and many times there is the variability around lot to lot variability. So every time you take a new lot of master mix you can upset the delicate balance a little bit and alter the readout ever so slightly. So when selecting CTs for cutoff I mean hopefully that's, you know, there's a fairly flexible within the variability range, to set that. And you're not, you know, you're not getting false positives and you're not getting unintended false negatives. And - but this is a highly technical area to move towards true quantitation probably through the process of developing a semi-quant assay. First, since we don't have yet a recognized international standard which is really ideal and/or necessary for a true quantitative assay, so that all assays can be harmonized around that international standard and compare results assay to assay, lot to lot, et cetera. So for the serology assays, we've been authorizing semi-quant because there isn't yet an international recognized standard for serology. We anticipate that for those that are interested that - in the molecular and antigen space for developers to come in for EUA authorization of semi-quant perhaps leading to the quant assay. Then we'll go through those who want it now before the international standard is available and we'll go through a semi-quant authorization pathway. And of course you need calibrators for that, probably at least a two point. And so there's an important development of those calibrators and it's important development of how you're going to assay the semi-quant and what sort of meaning it is. We're also potentially challenged on the science around, you know, intended use for semi-quant and quant assays, to actually show say correlations on important clinical factor. You put in there what you want. Could involve to generate the data that supports that, could involve a significant clinical study. You know, in order to authorize a semi-quant or quant assay, you know, I think we're going to be as flexible and adaptable as possible. And we're not going to be overburdensome on what those claims are at least as far as they don't claim things that aren't supported by actual data. So that's where I think a lot of discussion will surround this topic, is okay, can we first of all, prove that our assay is semi-quant or quant; is it linear over a certain, or claimed, dynamic range, upper limit of quant, lower limit of quant, you know, that thing, really a blank limit detection, stability and reliability of your calibrators from run to run, etc., batch to batch, lot to lot. We'll try to put, you know, we'll try to be as flexible and least burdensome as possible upfront, for authorization. There may be some post-market commitments just to make sure everything is sound and accurate. But, you know, we're getting a lot of questions about hey, can I compare this CT to that CT or this assay and that assay, and those in the know, know that that's very problematic. And so probably the best next step forward is to encourage developers who are interested to come in with semi-quant and quant assays with their actual standard. Okay. Next topic. And these are having to do with submissions of pre-EUAs and EUAs. And we're obviously still getting a lot of them. We have surged our reviewers; we have a surge of effort bringing reviewers from other areas into this effort, to try to, you know, make decisions much more quickly and reduce the list of open submissions. I'm happy to report that as of the end of last week, we have turned that corner and we are reducing the overall amount of open submissions, both originals and supplements. So the surge is working. We hope that it will accelerate. We do ask for your help. You know, due to the overwhelming interest by developers still, in pre- EUAs and EUAs we want to try to limit our feedback on pre-EUAs and EUAs, to one round. I know this is challenging. We want to be fair to all developers; we want to move through applications as quickly and expeditiously as possible, to come to a decision point. And so we would ask that you work closely with us and when we have questions you completely address those after say a first round of questions, if there are some. And then we want to really close those applications out. In pre-EUAs we're going to use templates to the greatest extent possible, or prepared language to the greatest extent possible. I want to make it clear that our templates and our thoughts in these communications even on EUAs, are recommendations. If something goes a little off recommendation it is going to slow us down. So while they're not firm and fast requirements necessarily, our recommendations are well thought out, they're streamlined. We're dealing with this volume of applications and we want to be fair to all. So, you know, those that follow our recommendations, they could have a more expeditious pathway through to the decision point. And we're also starting to get questions about conversions from EUAs to full submissions. Those are coming in as QSUBs. As is generally probably known for our office, we are trying to close QSUBs in most areas except for select areas, as quickly as possible. We'll do a similar thing for QSUBs for conversion of EUAs related to SARS-2 to full submissions. We have our thoughts now that we can share with developers who ask. We'll also have a subset of questions that we know that some developers may have that we want to answer in those QSUBs. And but there will be some that we're going to ask that you rely on especially the most recent related authorizations as evidenced in the decision summary. And the specific SARS feedback that we are now giving to developers who asked. We - dwelling on any one particular application and spending an overabundance of time only slows down our process and doesn't allow us to get to all developers as quickly as possible. So, you know, your understanding of this and your help with this would be greatly appreciate not only by me and our staff, but I think the other sponsors as well, because they want to get to this decision point as quickly as possible. All right. So Operator and Irene, that pretty much closes out a longwinded and hopefully helpful update from me and from Toby. Thank you Toby. We can go onto Q&A.

Coordinator (FDA):
Thank you. We'll now begin our question and answer session. If you would like to ask a question over the phone, you may do so by pressing star then 1. If you need to withdraw your question, you may do so by pressing star then 2. Our first question comes from Shannon Clark. Your line is now open.


---

## 2020-12-09_Virtual Town Hall 36_section-titles.md

#### 1. Updates on COVID-19 Testing Developments and Priorities


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are on listen-only mode until our question-and-answer session. At that time if you would like to ask a question please press Star then 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. And now I'd like to turn the meeting over to Ms. Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you hello. I'm Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 36th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health both from CDRH will provide a brief update. Following opening remarks we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Welcome everyone and we're so glad you could join us again today. And as always our desire is to do our best from the FDA's perspective to provide clear recommendations and information that you can use to further development of from COVID-19 tests and to continue our mission during this pandemic to speed access to as much accurate testing as possible. Since I last mentioned that we had organized a further surge of resources into the COVID applications, we continue to see success with that surge and see an increasing pace of decisions. So I did want to highlight this week that since last week there have been several additions to our authorization including more pooling authorizations that are especially useful we believe in trying to identify asymptomatic positive patients. When the prevalence of disease is low in a population such as a routinely screened population which is congregant settings or universities and workplaces, colleges, other educational institutions, we expect that once a regular screening program is initiated that you will hopefully rapidly see a decline in positives making pooling a very efficient way, efficient use of resources. Please note all the caveats in our authorizations about the use of pooling. And of course if the pooling scheme has not yet been authorized for an asymptomatic screening we do clearly state on the FDA Web site and we're supported by both the CDC and the CMS that you can use the tests that off label as long as there is no specific limitation about the use, very specific use limitations to very rare perhaps authorizations about the limitations to only symptomatic patients. We also saw more home collection kits authorized and of note the first home collection for a panel test that involves both SARS-CoV-2 and flu detection. And of course we signal with that authorization our continued desire to see panel testing in all forms that are supported by data. We authorized another rapid antigen test. We also authorized more serology tests. And so it has been a busy - another busy week. We - and want to remind everyone of our current highest priorities. This is - this - the priorities in two ways, one for review but also in seeking development of these tests from the development community. so that obviously they really haven't changed recently and so they are again __point of care tests, home collection kits from home testing opportunities, panels and extremely high throughput systems that allow the most efficient testing of large volumes of samples.__ And so that concludes my introductory remarks today and I look forward to our dialogue. And we can open it up for questions. Thank you.

Coordinator (FDA):
Thank you. We will now begin our question and answer session. If you'd like to ask a question over the phone please press Star then 1 and record your name clearly when prompted. If you need to withdraw your question you may do so by pressing Star then 2. Our first question comes from Randy True. Your line is now open.


---

## 2020-12-16_Virtual Town Hall 37_section-titles.md

#### 1. FDA Updates on COVID-19 Testing and Authorization Guidelines


Coordinator (FDA):
Welcome everyone to today's conference call. At this time your lines have been placed on listen only for today's conference until the question-and- answer portion of our call, at which time you will be prompted to press star 1 on your touchtone phone. Please ensure that your line is unmuted and please record your name when prompted so that I may introduce you to ask your question. Our conference is being recorded and if you have any objections, you may disconnect at this time. I will now turn the conference over to our host, Ms. Irene Aihie. Ma'am, you may proceed.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 37th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to today's discussion. Please remember that we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Hello everyone. Welcome again. We look forward to interacting with you today on these important topics. And we're doing everything that we can do at the FDA, to greatly expand access to testing so that we can be more and more able to battle this deadly virus. So I did want to start off by reminding everyone that the FDA is allowing tests, diagnostic tests to be used, antigen and molecular tests that are authorized, to be used off label in testing asymptomatic patients. So that is completely legitimate to do. We're encouraging it because we only have a small number of tests right now that are authorized for asymptomatic screening. So off label use as directed by the prescriber for prescription tests is completely acceptable and encouraged. In particular, direct antigen tests, it's, you know, that have been authorized, all of them that have been authorized can be used for this purpose. The only - there is a rare - there are rare examples where we've seen asymptomatic data that is not sufficient for authorization. And we make a very rare and unusual statement in the IFU, in the instructions for use. Otherwise, we just categorically say that all the authorized tests for direct antigen testing, can be used off label by prescription in the asymptomatic population. Again, the, you know, we don't know the actual performance and that should, you know, be understood by the prescribers. But we, you know, if there's something that's positive then that's great. But even in that situation, you want to make sure and look at, you know, the spread of the virus in that particular area. If the incidents of positive results is low then it's important to strongly consider a confirmatory test. We typically say use a high sensitivity molecular test. Hopefully you have arrangements that you can get that result back in 24 to 48 hours. That would be ideal obviously. You know, another antigen - different antigen test potential could be used as well. You know, whatever you have access to that's important to be sure and confirm that result. But again, I think the highest sensitivity molecular test. A different antigen test may have slightly lower performance than a centralized high sensitivity molecular test and could return potentially a false negative on the repeat testing. So all that should be taken into account. But we don't know unless we see data on a particular submission, we don't know the performance in the asymptomatic population. as I said, we are looking and encouraging more and more submissions for asymptomatic claims for screening plans and we welcome those. But in the interim, we've made this very clear and CMS and HHS have made this very clear as well. They have removed any potential roadblocks at the federal level. If there's anything else that we can do to assist in deploying the test in that manner if you have questions, please email us at the template email address and we'll do our very best. We have FAQs on this, CMS has FAQs on this, as does HHS. I did want to also state that starting in the new year, we will continue these town halls. Look for announcements. We will try something a little bit different in the new year. I want to make sure that those developers of antigen and molecular point of care tests and home tests, have the ability to get their questions asked and potentially answered, to the best of my ability and our abilities. You know, there's typically a number of callers and sometimes we don't know if callers don't get their questions answered. So we are looking at different ways of doing this. I anticipate that after - we may do this by topic alternating weeks. And - but I anticipate that in all cases, by the end of the hour, we will accept all questions. So that I just want to sort of make sure that every different development group out there gets a chance to ask some key questions so that we can clarify, explain, stimulate, encourage all test development. So of course, if you were paying attention to our announcement, we've had more authorizations in the intervening week. Of note is one very important authorization and that was an antigen - it happened to be an antigen test. But it is an antigen test that has been authorized as the first home based over the counter test. And so we are extremely excited about that here at the agency. And look forward to more and more home testing authorizations, not just for antigen tests; not just for ­ and molecular, but also for serology tests as well. And of course, we had a prior prescription based molecular test and we look forward to more authorizations both by prescription and OTC in the home. Of course, you know, molecular is great if it can be done in the home environment. There is a challenge though in that it is more difficult to manufacture molecular tests in quite the same volume as direct antigen lateral flow tests. And that - and also there may be cost differentials too. But because of the manufacturing capacity of these so-called paper strip tests or lateral flow tests, the authorization yesterday for the first home OTC test is - was such a paper strip test. It - those - the capacity of making those tests is in the potentially tens of millions per month, if not even to the 100 million mark, even from a single manufacturer. So obviously, deploying such testing that has been EUA authorized, by which we've had a chance to look at the test and authorize it and get a good initial feel at least under the EUA framework, of its performance, so that the public can - and users of these tests can have assurances that the FDA believes they are accurate for the intended purpose. So I mean that kind of explains why it's so important. Because right now there is a desire I believe out there, to have a lot more testing. There's a willingness to do this. And so we're looking at - and we're looking at, you know, how we can make that testing as widely available as possible so that consumers even can - and home users, can get a fast, accurate result that they can use to make the very best decisions about their lives and those of their loved ones and other situations that are important for doing that. Okay. We will move into the Q&A portion now. And I look forward to your questions. Thank you.

Coordinator (FDA):
Thank you. At this time if you would like to ask a question please press star 1 on your touchtone phone. Please ensure that your line is unmuted. Please record your name when prompted so that you may be introduced. Our first question is from Melissa Grusajia. Your line is open.


---

## 2021-01-06_Virtual Town Hall 38_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing and Variant Impact


Coordinator (FDA):
Welcome and thank you for standing by. Today's call is being recorded. If you have any objections you may disconnect at this time. All participants are in a listen-only mode until the question-and-answer session of today's agenda. To ask a question at that time you may press star 1 and clearly record your name for question introduction. I would now like to turn the call over to your host Kemba Ford, thank you.

Kemba Ford (FDA):
Thank you. Hello. I am Kemba Ford of CRH's Office of Communication and Education. I'd like to welcome you to the FDA's 38th in a series of virtual townhall meetings to help answer technical questions about the development and validation of tests for SARS CoV-2 during this public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health and the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH will provide a brief update. Following opening remarks we will open the line for your questions related to the development and validation of tests for SARS CoV-2. Please remember that during this townhall we are not able to respond to questions about specific submissions that might be under review. Thank you and I'll now turn the call over to Tim.

Tim Stenzel (FDA IVD Director):
Hello everyone and welcome again to this continuing dialogue. It's a new year. I certainly hope that this is a much better year for us due to our combined efforts than the last year. So we look forward to assisting the development of new products that can play a key role in the pandemic. We were busy over the holidays. If you remained aware we had a number of authorizations that happened and that has carried into this week. One authorization that's a little bit unique is we did authorize the first antigen dipstick assay. So this is a simple strip that goes down into a test tube. It's authorized for point of care. There's been a lot of interest in the, you know, very inexpensive tests. And this antigen test doesn't even have a test cartridge around it. So hopefully this adds to our arsenal. That is the Quidel QuickVue SARS test and, you know, joins the Abbott BinaxNow as a very, very simple, non- instrumented antigen test. And it's just one example of the many awesome products that have been developed during the pandemic to meet our needs. And it's I think a little bit unique in that it can really drive down the cost of the results and because it's a rapid antigen test it can be produced in high volumes as you might expect just like the Abbott BinaxNOW. And there are great other antigen tests. I just know that there's huge public interest in driving s down that's why I highlight that one. We of course want to continue just to make clear what our priorities are. They're focused on those things that can have the greatest public health impact. So home tests, home collections, point of care tests and super high volume central lab tests. All, you know, primarily the diagnostic tests but obviously we look at serology tests as well. So, you know, these are our priorities. And if an application comes in and it's complete and picks one of these boxes, we will make it a priority to give you feedback as soon as possible and try to authorize these tests as soon as possible. We do continue to ask that the submissions are complete. That they're well written and clear so that our folks can rapidly assess the submission. We also need Why Missing data submitted in a common spreadsheet so that we can look at the data very quickly. We don't have to ask for this because we will ask for this. And really it's considered incomplete unless we have that Why Missing data which should have the results plus any demographics of the candidate test plus the comparative tests in enough detail. We also want to see your protocols for your clinical examination study - important and a detailed one. It's important to know how you selected samples, how you collected samples, how you tested samples, how you did the comparator assay. These are all really important questions. And we really can't make our assessment without them. So it only slows us down if we don't have complete information about these things. I did want to also talk about another hot topic and that is mutation. So we're all aware now of the UK variant mutation and it's a concern in the U.S. and we've seen a handful already confirmed. And then also the South African variant which has some overlapping mutations but also some clear differences between the South African variant and the UK variant. Both of these variants appear to be of higher infectivity due to the viral mutation with enhanced binding to the receptor and that's the theory at least. There's some pretty good evidence for that. Some of them may also have increased amounts of virus and then also greater binding to the receptor obviously can lead into a greater impact. So it's important to understand the variants that are circulating. We do have an interest in sequencing-based tests that can provide a whole genome sequence. Of course we've already authorized at least one such kit. That's the Illumina Kit. It is authorized and has within it reagents to sequence the entire genome. And that's been a great step forward that we authorized quite a long time ago before we really knew how important the mutations would be. The other thing that the FDA has been doing is on a regular basis of course with all applicants especially for the molecular assays we've been asking them at least twice during the authorization process to check the known sequences of variants and explain any challenges with their primer and probe sets that we have with those variants that are in the database. In addition the FDA has bioinformatics capability. We have the list of all EUA authorized primers and probes for molecular assays. And we have been interrogating the sequence databases to see if there are any mutations that could impact test performance. We have done this for the UK variant. We have done this for the South African variant. And we have done this prior to these variants for any variant that's seen in the database that was at 5% of the sequences in the database or above. In all cases we reach out to the test developers. We ask for their assessment of the impact of these mutations on the performance of the test. We do our own evaluation of what we anticipate might be a significant potential performance alteration. And work with the developers to assess the potential impact. As soon as all that work has reached a point where we feel like it's important to share any information with the community we will. And what I can talk about today of course is publicly known that the UK variant there's at least one test out there that has been publicly mentioned that's the Thermofisher Attack Path Assay that has S gene dropout. So with S gene dropout we have looked at a number of variants in the U.S. database and a number of sequences. And the majority to date do not have all of the UK variant mutations. What that means exactly we're not sure yet. But only a subset right now in the U.S. have - of the S gene dropout by Thermofisher have that. We believe that around 5% of the Thermofisher positives have an S gene dropout. But again as I said we think the great majority of those to date have not carried the UK variant mutation. So for the time being at least sequence verification of S gene dropout samples is something that we would recommend. Hopefully you have access to sequencing. As I mentioned there is an EUA authorized sequencing assay from Illumina that can suit this purpose. Also you can reach out to your state and local public health labs and they may or may not have a sequence capability. Some of them do and/or they can guide you in what is the best process to assess this. If you're a public health lab the CDC has asked that those isolates, those samples be sent to the CDC for sequencing. And so follow the CDC procedures and, you know, I would refer the public health labs to the CDC for any further questions on that. Obviously there are assay design issues that could be impacted by mutations particularly if an assay is a single gene target assay. And there are a number of single gene target assays that we have authorized. So it goes without saying that multi-gene assays are going to be less impacted by mutations as they continue to propagate in this pandemic. And will have an advantage over single gene target assays. Some technologies don't lend themselves well to multi-gene targets. We understand that completely. There's nothing wrong with the single gene assay. However there is a little bit more pressing need to understand, you know, how variants might impact performance with single gene assays. With the Thermofisher assay it is a 3-gene target assay and with S gene target dropout you can still detect positives by the other two targets. So we don't know as of now that there's any significant decrease in test performance of the Thermofisher assay. And for the moment at least it's a very helpful assay to identify potential S gene dropouts that could be the UK variant as we try to assess whether spread is continuing within the U.S. of the UK on variant. Moving onto antigen tests. Obviously there are mutations in the targets for antigen tests as well. It's a bit more difficult to assess the impact on antigen tests because we can't just simply look up sequences and primers and probes and identify whether there could be an impact on antigen tests. So the CDC has graciously agreed at least for the UK variants which they are now culturing to test the EUA authorized antigen tests at the CDC for their ability to detect the UK variant. So we will be reaching out to all of the EUA authorized antigen tests and asking them to send their kits. I think we need to be looking at 75 to 100 test's worth to send to the CDC because they do multiple levels and multiple replicates even for just a single variant such as the UK variant. So stay tuned with your EUA authorized antigen test and we will be reaching out to you with more information shortly. And finally I did want not mention serology tests. Obviously they can be impacted as well. And we will need to await the availability of immune serum or plasma from certain variant patients in order to assess the impact on serology. We have put requests out already for such samples. Obviously and thankfully at the moment there aren't that many in the U.S. of the UK variant and the South African variant. But if they do become more prevalent we expect to be able to access immune plasma or serum to assess performance in serology tests. And again antigen and serology tests are a little bit more difficult beasts to handle when it comes to assessing their performance with variants but we'll do our best here given the limitations of biology and science. I don't believe I have any other preliminary remarks. So let's go ahead and open this up to questions and we look forward to that, thank you.

Coordinator (FDA):
If you'd like to ask a question at this time you may press Star 1 and record your name clearly. Our first question will come from Wendy Strongen your line is now open.


---

## 2021-01-27_Virtual Town Hall 40_section-titles.md

#### 1. Developing and Validating COVID-19 Tests Amid Mutations


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode until the question-and-answer session of today's conference. At that time you may press star 1 on your phone to ask a question. I would like to inform all parties that today's conference is being recorded. If you have any objections you may disconnect at this time. I would now like to turn the conference over to Irene Aihie. Thank you. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 40th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Thank you, Irene, and hello everyone. And welcome back to our town hall today. I'm going to start off on a somber note, a remembrance for a pioneering COVID test developer who we recently lost. So Dr. Andrew Brooks was a Research Professor at Rutgers New Brunswick School of Arts and Science in the Department of Genetics. He also led the creation of the first EUA-authorized saliva based test and the first home collection of saliva. And reportedly, reported in the news now, at least on the Rutgers site, more than 4 million of those tests were performed between authorization and now. So it's really sad to see somebody who was able to advance testing in this way to be lost to us. He passed unexpectedly on Saturday and leaves his wife, Jill and three daughters, Lauren, Hannah and Danielle. Sorry. It's been a long fight. Anyway, we're very thankful to him for his work. And we'll remember him always. Okay pull it together Stenzel. I wanted to give some heads up on mutations. This continues to be a very hot topic and, you know, I think it's ideal for those that already have an EUA-authorized test and those who are developing tests, to consider the variants. We move to authorizing single target assays relatively early in the pandemic with the knowledge at that time that single target assays - we had not seen mutations that would impact them. But we are starting to see mutation to impact tests and obviously single target versus multiple target - targeting multiple reasons of SARS virus and, you know, there may be a performance difference going forward. So we'll certainly stay vigilant at the FDA's side on monitoring this. But we do want to put a shout out to developers to certainly be considering this. And they - as - when they, you know, and to work with us as - in looking ahead in how we can maintain the highest performance possible, for COVID tests, for molecular tests that includes probes and primers. We're obviously open to talking to developers who want to make updates or that are in development, you know, about how best to do this. So no change in recommendations at this time. Just, you know, a heads up. We think that antigen developers and serology developers should keep these variants in mind as well. You know, numerous of the serology tests do target the spike protein which can alter and at least one of the antigen tests does target spike protein. But of course, there can be a mutation that could affect other genes, other targets within the virus. So with that, we'll go into questions. Thanks so much.

Irene Aihie (FDA Moderator):
Operator, we'll now take questions.

Coordinator (FDA):
Thank you. We will now begin the question and answer session. If you would like to ask a question, please press star 1, unmute your phone, and record your name clearly. Your name is required to introduce your question. If you need to withdraw your question, press star 2. Our first question comes from Hannah Gabrielli. Your line is now open.


---

## 2021-02-10_Virtual Town Hall 42_section-titles.md

#### 1. FDA Updates and Q&A on SARS-CoV-2 Diagnostics


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are in a listen-only mode until the question-and-answer portion of today's call. During that time, if you would like to ask a question, please press star 1. Today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 42nd in a series of virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS CoV-2 during the Public Health Emergency. Today, Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, and Timothy Stenzel, Director of the Office of In FDA Townhall Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS CoV-2. Please remember that during this Town Hall, we are not able to respond to questions about specific submissions that are under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks everyone for joining us again today. First, we have a new funding opportunity to tell you about. There should be a slide showing now that has some additional information about this. This is a funding opportunity for COVID-19-related diagnostics that opened on February 5. FDA is not leading this effort, but we wanted to flag it for you. It's being coordinated by HHS OASH, Office of Assistant Secretary for Health, and the DoD, and it's open until March 7. The slide that's showing now has more details, including a link for information and the process for submitting proposals. And we will get the slide deck posted on our Website on the Town Hall page either later this week or when we post the transcript. So, this is an Area of Interest, or an AOI, that's soliciting for proposals where you may request investment funding for capacity expansion and provide price quotes for raw materials, test components, supplies, et cetera for COVID-19 point-of-care tests and other IVDs. This is an expedited process that's coordinated by HHS and OASH and DoD to support the government's FDA Townhall COVID-19 response to rapidly increase manufacturing capabilities within the diagnostic supply chain. So, with that, we can go on to the next slide, Irene. And we've added a couple of additional links to this slide as well that we think will be helpful resources for you. One of them is the January 2021 HHS FAQ on COVID-19 diagnostic data standards and core data elements for test reporting. And then the next one is the HHS COVID-19 testing and diagnostics working group additional testing information. So, those links will be up on the slides that will get posted as well and may have some helpful information for you. And then my last update is that we had a question last week about UDI, Unique Device Identifiers, and whether UDI is required for EUA devices. And generally, for - at least for the diagnostics, UDI has not been included as a condition of authorization. So, we would not typically expect a UDI unless it is included as a condition of authorization in the letter - the EUA letters. However, there's no restriction from providing UDIs, which many manufacturers do, and this is really helpful because the device identifier is a required data element to fulfill the laboratory reporting requirements listed in the HHS COVID-19 laboratory data reporting guidance. So that was just a follow-up from last week's call. And with that, I think we can turn it over to questions.

Irene Aihie (FDA Moderator):
Operator, we'll now take questions. FDA Townhall

Coordinator (FDA):
Thank you. We will now begin the question-and-answer session. If you would like to ask a question, please press star 1. Please unmute your phone and record your first and last name clearly when prompted. Your name is required to introduce your question. Also, we ask that you limit yourself to one question. To withdraw your question, you may press star 2. Once again, at this time, if you would like to ask a question, please press star 1. And our first question is from Christy Bergerson. Your line is open.

---

#### 19. Sample Size Requirements for Antibody Test Kit Approvals


Shannon Clark:
Hello, again. Shannon Clark with UserWise Consulting. Question about - I'm really looking forward to this template coming out for this home-use test kits for antibody testing. Do you expect that it's going to require a sample size of 30 participants for prescription-only; then 150 participants, or 100 sessions with some pairs for over-the-counter? Because I've received conflicting emails from the FDA implying that perhaps OTC could be achieved with a sample size as low as 30.

Toby Lowe (FDA IVD Assoc Director):
I don't - I can't speak to what exactly will be in that template. Hopefully, we will be able to get it out soon so that we will be able to speak to it more definitively. But if you do have specific questions as you're planning your approach now, you can send them to the mailbox. And if you're having difficulty getting a FDA Townhall uniform answer, you can flag the question for Tim and me, and we'll take a look into it.

Coordinator (FDA):
Your next question is from Jackie Chin. Your line is open.


---

## 2021-02-17_Virtual Town Hall 43_section-titles.md

#### 1. Updates and Guidance on COVID-19 Test Development


Coordinator (FDA):
Welcome everyone to today's conference call. At this time your lines have been placed on listen only for today's conference, until the question-and- answer portion of our call, at which time you will be prompted to press star 1 on your touchtone phone. Please ensure that our line is unmuted and please record your name when prompted so that I may introduce you to ask your question. Our conference is also being recorded. And if you have any objections you may disconnect at this time. I will now turn the conference over to our host, Ms. Irene Aihie. Ma'am, you may proceed.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 43rd in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and FDA Townhall Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Wow, 43 town halls to date. That's a lot. And we'll keep going as long as you all think this is helpful. And these sessions are designed to provide assistance to all COVID-19 test developers, whether they be molecular, antigen and/or serology tests. That's why we do this. And obviously, we have a lot of interaction with essentially all developers who have submitted a question or an application to the FDA through our office. And those are happening sometimes 24/7. And that's how we do it. I wanted to give an update on authorizations. As of yesterday evening we had authorized 331 tests and sample collection devices including 247 molecular tests and sample collection devices, 70 antibody tests and 14 antigen tests. There are 37 molecular authorizations that can be used for home collected samples. There's one molecular prescription at home test, one antigen prescription at home test, and one over the counter at home antigen test. We expect to see more home collection kits come in, in wider availability through that, including when prescriptions are not required in that home collection kit we are calling it direct to consumer and you can search on the FDA authorized Web site for any direct to consumer home collection kits. FDA Townhall When it's a test in the home we're calling it over the counter and - when it's not prescription. We expect more collection kits including more direct to consumer kits, and more at home tests including more OTC at home tests. So those are obviously priorities along with very high throughput central lab tests. So with those brief updates let's move right into questions. And we look forward to hopefully helping you out today. Thanks.

Coordinator (FDA):
Thank you. At this time if you would like to ask a question, please press star 1 on your touchtone phone. Please ensure that your line is unmuted and please record your name when prompted so that I may introduce you to ask your question. Our first question is from Shannon. Your line is open.


---

## 2021-02-24_Virtual Town Hall 44_section-titles.md

#### 1. FDA Updates on COVID-19 Test Guidance and Monitoring


Coordinator (FDA):
Good morning. Welcome everyone to today's conference call. At this time your lines have been placed on listen-only for today's conference until the question-and-answer portion of our call at which time you will be prompted to press Star 1 on your touch-tone phone. Please ensure that your line is on muted and please record your name when prompted to be introduced to ask your question. Our conference is being recorded and if you have any objections you may disconnect at this time. I will now turn the conference over to our host Ms. Irene Aihie. Ma'am you may proceed.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 44th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests on SARS-CoV-2 during the public health emergency. Today Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health and Timothy Stenzel, Director of the Office of In NWX-FDA OC Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, both from CDRH, will provide a brief update. Following opening remarks we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene and thanks everyone for joining us again this week. I have a couple of updates this afternoon. First as you may have seen on Monday we issued a new guidance document for the policy for evaluating impact of viral mutations on COVID-19 tests. Obviously this is a topic that we've talked about here on the town hall quite a bit recently. And we now have this guidance document out that was put out along with a suite of guidance documents from the other centers as well on the same topic for different medical products. So our guidance provides information on evaluating the potential impact of emerging and future viral genetic mutations on COVID-19 tests including design considerations and ongoing monitoring. As you all know we've already issued a safety alert about this topic and identified a few tests that are known to be impacted though at this time that impact does not appear to be significant. We continue to monitor and will put out additional alerts as needed if and when future impacted tests are identified. Now the guidance goes into the monitoring that FDA does as well as describing recommendations for test developers, such as considering the potential for future viral genetic mutations when designing your test, NWX-FDA OC conducting your own routine monitoring to evaluate the potential impact of new and emerging genetic mutations and information that we would expect to be provided to FDA on both in an EUA requests and in supplemental EUA requests or reports after authorization with ongoing monitoring. And it does provide more detailed recommendations for developers of molecular CoV-2 tests and also discusses the sort of landscape of monitoring for antigen and serology as far as SARS-CoV-2 tests and forecasts that we will put additional information regarding that monitoring in the EUA templates as more details are worked out. So that guidance can be found on our Web site and if there are any questions we're happy to take them on the call today or you can also send a questions to the mailbox as you're all familiar with. The other topic that I wanted to bring up before we get into the questions is to clarify some comments that were made last week regarding usability test - usability and user comprehension studies. One of the risks of a town hall forum like this is that Tim and I don't always have the source documents open in front of us, so we don't always have all of the details to best answer the questions that come up. So sometimes we like to do a little research and come back and clarify for everyone.


---

## 2021-03-03_Virtual Town Hall 45_section-titles.md

#### 1. FDA Town Hall: SARS-CoV-2 Test Development Updates


Coordinator (FDA):
At this time all participants are on listen-only mode. Today's conference is being recorded. If you have any objections you may disconnect at this time. And now I would like to turn the meeting over to Ms. Kemba Ford. You may begin.

Kemba Ford (FDA):
Thank you. This is Kemba Ford of CDRH's Office of Communication Education. We apologize for a delay in starting today's call. We do want to welcome you to the FDA's 45th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Timothy Stenzel, the Director of the Office of In Vitro Diagnostics and Radiological Health and the Office of Product Evaluation and Quality and Toby Lowe, the Associate Director of the Office of In Vitro Diagnostics and Radiological Health both from CDRH will provide a brief update. Following opening remarks we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during today's town hall we are not able to respond to questions about FDA Townhall specific submissions that may be under review. Now I will turn the call over to Timothy.

Tim Stenzel (FDA IVD Director):
Yes apologies for the delays. We had multiple technical issues. And I'm not sure that everybody who wants to be is on the call quite yet. We did have a formal remarks that we are ready to present but I think we're going to delay on that until we have a, you know, as many people call in as possible. People should look to their emails if they're - if you know of folks who are having trouble connecting with the connection information. And with that I think we'll get into - right into questions. We'll take questions for a little bit then we'll pause and do the usual announcements. And so operator if you are able to set up the questions that would be great.

Coordinator (FDA):
And if you would like to ask a question over the phone please press Star 1. One moment. Thank you for your patience. Our first question comes from Shannon Clark. Your line is now open.


---

## 2021-03-10_Virtual Town Hall 46_section-titles.md

#### 1. FDA Updates on At-Home SARS-CoV-2 Test Authorizations


Coordinator (FDA):
Welcome, and thank you for standing by. At this time, all participants are in a listen-only mode. At the end of today's presentation, we will conduct a question-and-answer session. To ask a question, please press Star 1. Today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I'm Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 46th in a series of virtual town hall meetings, to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Toby Lowe, Associate Director of the Office of in Vitro Diagnostics and Radiological Health, and Timothy Stenzel, Director of the Office of in Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, both from CDRH, will provide a brief update. FDA Virtual TH Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS CoV-2. Please remember that during this town hall, we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks, everyone, for joining us again this week. I have a couple of updates from last week. The first is an authorization that went out on Friday for the Cue COVID-19 test for home and over-the-counter use. And this is the first molecular at-home over-the-counter non-prescription based tests that we've authorized. And this is, excuse me - Cue did have a test that was authorized for point-of- care use already. And now this is their over-the-counter version that was authorized on Friday. And then also on Friday, authorized the first test for an adaptive T-cell immune response. This is the adaptive technologies to detect COVID test, which is NGS-based to aid in identifying individuals with an adaptive T-solver immune response to SARS CoV-2. So, both of those authorizations have been posted on our website, along with other recent authorizations, and there was also a press release issued for each of those that you can find on our website. And I'll turn it over to Tim for his updates.

Tim Stenzel (FDA IVD Director):
Yes. A pleasure to join all of you again today. Thanks for all that you're doing. We want to help you and speed access to additional diagnostics. So to - you know, we again, emphasize our priorities in particular home tests, is very, very important for us right now, either prescription or over-the-counter, whatever developers choose to come in with. FDA Virtual TH I do have a suggestion. It's just a suggestion, not a recommendation, but if you are developing a test that you envision can perform in the home, if you go straight to the home study, and don't do point-of-care studies, if we're able to authorize based on the home studies, you automatically get the point-of-care authorization as well. So that is probably going to be a more efficient pathway, if you have high confidence in your test to be able to perform in the home, and you're ultimately going there, you cut out all those point-of-care studies, and you go right to the home user. I also suggest, not necessarily recommend, because there is some risk to this, is that when you do the home clinical studies, that you overlap with that the same participants' usability study, user comprehension, with the clinical study. So that will potentially make it a lot more efficient, fewer patients to enroll in your overall studies, you combine all those things. Don't forget the flex studies that are called for point-of-care. Those are also needed for home. And - yes. And so, you know, to get into the home, it just requires adequate performance on 30 symptomatic patients, and that would be for a prescription. And then for over-the-counter, we'd like to see a minimum of 10 asymptomatic positives. And then any additional asymptomatic positives that we'd like to see, can be obtained post authorization. So again, you know, we'd really like to see more home applications, either for a prescription or over-the-counter. And if it is more efficient for you to FDA Virtual TH bypass the point-of-care studies in CLIA waived clinics, that works for us as well. Okay. I think we're ready to go into the questions. Thank you so much.

Coordinator (FDA):
Thank you. We will now begin the question-and-answer session. If you would like to ask a question, please press Star 1, please unmute your phone, and record your first and last name clearly when prompted. Your name is required to introduce your question. To withdraw your question, you may press Star 2. Once again, at this time, if you would like to ask a question, please press Star 1. And our first question is from Shannon Clark. Your line is open.


---

## 2021-03-17_Virtual Town Hall 47_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Test Development and Screening Policies


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode. During the Q&A session, if you'd like to ask a question you may press star 1 on your phone. Today's call is being recorded. If you have any objections you may disconnect at this time. I'd like to turn the call over to Ms. Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communications and Education. Welcome to the FDA's 47th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, and Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks everyone, for joining today. I have a couple of updates and then I will hand it over to Tim for some more. First, I wanted to make sure everyone was aware that just this morning the updated templates on our Web site, we updated the serology template for test developers. And in that update we added some information about viral mutations and variants, and also did some clarifying edits throughout. So hopefully that will be useful. And then we also posted a new template for test developers of serology tests that the text will correlate to neutralizing antibodies. So I know we've had a lot of interest in that template and a lot of people waiting for it. So it has been posted and we hope that is still helpful for you. The other update that I have is that starting tomorrow we will open up the ability for you to send questions by email ahead of time for us to consider prior to the town hall, so that we can try and address potentially more frequently asked questions. So we will be - there will be an email that goes out likely tomorrow, with instructions on how to do that. And the email address will be CDRHWebinars@FDA.HHS.gov. But again, you'll get an email - if you're on the town hall email list you'll get an email with those instructions tomorrow, once that opens up. And with that, I will turn over to Tim, to give some additional updates.

Tim Stenzel (FDA IVD Director):
Thank you, Toby and welcome again, today. I am hearing that some callers may be having trouble calling in. So if our technical team could check on that and assist those callers, that would be great. Let me start off with, prior to getting to the main topic, with frequently asked question that we get about the use of frozen bank samples for validation of point of care tests on a particular antigen test. And yes, we are allowing banked frozen samples to be used and banked samples can be mixed in with fresh samples. We still are asking that at least 10% to 20% of the positives are composed of low positive samples which reflect the natural distribution of SARS-CoV-2 viral loads. We have seen that even early in symptomatic disease that CTs can be relatively high. Per the antigen template, you know, we do want to see these low positives, at least 10%. You know, and then we do want to see fresh sample as well, a minimum of five positive samples pre-market. And this is because we have noted multiple times now, both for molecular and for antigen, that freezing can actually for still specifically undetermined reasons, allows a greater sensitivity. And so pre-frost studies can show that the performance is same or different. But just to be safe we do want to see a minimum of five fresh samples pre- market, positive samples. And then we would ask you to fulfill that on the rest of the samples being fresh after authorization. Okay. With that, I will move into the main topic. So yesterday we issued a new policy, serial screening and particularly screening asymptomatic individuals which we view as a critical part of reducing the spread of COVID- 19. You know, screening involves testing asymptomatic individuals who do not have known or suspected exposure to COVID-19 in order to make individual patient decisions such as whether an individual participates in an activity based on the test results. Yesterday we also issued a fact sheet to assist schools, workplaces, communities and others, looking to establish blood testing programs to screen asymptomatic individuals as they are selecting a test for screening. We also posted a new template for molecular and antigen tests for serial screening. We expect that the recommendations and information we provided here for test developers, will help streamline the path to an EUA authorization for screening tests, specifically the template outlines, outline situations in which FDA may authorize certain tests for screening, with serial testing prior to conducting - prior to the developers conducting certain performance evaluations with asymptomatic individuals. This may include, in certain circumstances, authorizing a point of care and at home tests for OTC, nonprescription use, if all the appropriate studies have been other studies for usability and user studies and user comprehension have been outperformed. In this situation we are leveraging evidence of a test strong performance in symptomatic patients. Combined with serial testing it mitigates the risk of false results when testing asymptomatic individuals for the cases in which we have not reviewed the asymptomatic testing performance pre-market. And we expect to see that in the post market studies showing and demonstrating adequate performance in the post-market setting would demonstrate that adequate performance with the serial testing plan. I want to back up a little bit, talk about how important home tests, point of care tests in particular antigen tests are. So starting in January 2020 we - the FDA and other US government entities reached out to companies that are capable of producing antigen point of care tests and ultimately obviously, home tests which we've authorized. You know, it wasn't that long to the year that we authorized our first antigen test. And then to date I think we've authorized 15 antigen tests. We are very interested in home use and on July 29, 2020 we issued a template with our recommendations, for home validations so that we can authorize both prescription and over the counter testing. In September of 2020 in a piece on the Hill, we suggested that for a test that may be performing lower than recommended levels could use serial testing to improve overall performance using the combined results, two or more tests, to be able to achieve, you know, a good level of sensitivity. To date though, we've received no formal EUA submission of a fixed serial testing plan showing that it is functioning. We hope this - that this new pathway, this new policy will accelerate the use of serial testing to reopen schools and reopen workplaces and other situations and say to keep convalescent settings safe. We recently were - FDA was recently briefed on a very well-designed, well-executed study that used serial testing of an EUA authorized molecular test and an EUA authorized antigen test. And although it clearly showed that on a head to head competition or comparison, the antigen testing was significantly less sensitive than the molecular test. It also demonstrated that a serial testing program for the antigen test significantly mitigated the risk of false negatives in that serial testing program. So that was sort of the first really firm good evidence that we had and helped usher in this new policy. So throughout this - throughout the year, last year, we have striven to provide flexibility and adaptability in approaches to validate all tests including home tests, screening tests. So we have authorized a number of screening tests, I think almost a score, and we hope that this greatly accelerates that as well. I wanted to go into a few more details. You know, CLIA requirements are overseen by CMS and FDA's actions in this policy are not removing any CLIA requirements for the use of at home tests for self-testing in the - is not subject to CLIA requirements. This new template is also not automatically changing any authorizations. It is providing a streamlined path for test developers seeking serial screening claims. So in order for a test to be authorized for OTC or nonprescription use, such tests need to be - needs to have previously shown asymptomatic screening data. But with this, since - in order to be an OTC test. But now we are allowing that data for asymptomatic performance using screening, to be revealed to us after authorization. This template provides an option for screening authorization prior to collecting data or submitting - completing the validation for asymptomatic individuals. We would still expect validation symptomatic individuals as well as usability, user comprehension and layperson appropriate labeling for an OTC test. For a developer who's already submitting that information, they would not need to submit more for FDA to authorize their test for OTC though. They can simply come in with a supplemented amendment application asking to convert to OTC based on the serial testing program. Of course, the older pathway still exists. If someone comes in with, you know, meeting your performance expectations for an OTC test, on a one time test performance we will continue to authorize that, without the recommendation for serial testing. And that may be still an attractive option. Obviously we've already authorized many OTC collection kits and some OTC home tests. So - and of course, providers must still order tests that are authorized only for diagnostic purposes and we're not going to object to the off label prescription use of those tests that don't have a screening claim. You know, the FDA does not determine the claims the test developer decides to request for their test or their application. We are encouraging them to pursue this option if it's applicable to them and they are interested in it. We do authorize tests for certain indications and for certain - use in certain settings as appropriate by their validation. Generally point of care tests are authorized for use in the settings of under CLIA certificate of waiver with healthcare workers that are untrained non- laboratorians. These tests typically included an instrument and required a trained user to operate them, but not always. And it's not required to have an instrument. CMS is responsible for oversight of CLIA certification. Of course tests that are authorized for at home use are appropriate for self-testing. Without a trained operator it may be used for self-testing at home or self-testing in other settings, such as schools, workplaces, and are not subject to CLIA requirements in that specific narrow self-test category. Going further, each authorization indicates whether a test is for prescription or nonprescription use. Or as we said before in reiterating the fact sheet, when we issued yesterday, tests authorized for a symptomatic claim, can be ordered by a provider for screening purposes and I've made that clear earlier in this discussion. Some entities may use a blanket prescription to cover screening tests for their entire population. And if a test is authorized for OTC, over the counter, no prescription of course, is required. And as we've said previously including our prior FAQ and reiterated in the fact sheet we issued yesterday, you know, clinicians can absolutely order tests for off label use of screening. We're not going to object to that. It is important however to be aware that certain tests include labeling. And state the tests should only be used for symptomatic individuals. These tests should not be used for screening and they would - this pathway would not be open to them. However, we do know that some groups are setting up testing programs for back to school, back to work, and prefer to use a test that is authorized for screening. That's an important point. We have definitely heard resistance about using tests off label from some quarters and from some clinicians. And this hopefully paves the way for getting rid of that as an issue. And once we authorize a test for screening they of course are covered by PrEP Act coverage. So again, we hope that this streamlined path will lead to more test developers seeking and receiving a screening claim. And as we indicated, and this is primarily for antigen tests that will be severely tested multiple times a week, we expect to see a minimum performance sensitivity for symptomatic testing of at least 80% with 70% as the lower bound of the two sided 95% confidence sample, which we believe offers additional flexibility in obtaining the screening claim and using and including an OTC, over the counter use. So with that, that was a lot of information, we would like to go ahead and open up this call for questions and we look forward to that. Thank you.

Coordinator (FDA):
The phone lines are now open for questions. If you would like to ask a question over the phone, please press star 1 and record your name. If you'd like to withdraw your question press star 2. First question in the queue is from Shannon…

Toby Lowe (FDA IVD Assoc Director):
Okay. Before - sorry, before we take the first question, this is Toby Lowe, I just wanted to jump in with one additional point of clarification. Tim talked about healthcare providers ordering tests off label and since there was quite a bit of discussion about at home testing in that I just want to clarify that a healthcare provider can order a test for a different indication but not - but they cannot order a test for home use if it is not authorized for home use.

Coordinator (FDA):
And with that, I will turn it back over to you to take the first caller.

Tim Stenzel (FDA IVD Director):
Yes. I didn't cover that caveat. Thank you, Toby. I appreciate that.

Toby Lowe (FDA IVD Assoc Director):
Yes.

Coordinator (FDA):
First question in the queue is from Shannon Clark. Your line is open.


---

## 2021-03-24_Virtual Town Hall 48_section-titles.md

#### 1. FDA Guidance on SARS-CoV-2 Testing and Validation.


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode. At the end of today's presentation we will conduct a question-and-answer session. To ask a question, please press star 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I'm Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 48th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Toby Lowe, Associate Director of the Office of In Vitro Diagnostics in Radiological Health and Timothy Stenzel, Director of the Office of In Vitro Diagnostics in Radiological Health in the Office of Product Evaluation and Quality, both from CDRH will provide a brief update. Following opening remarks, we will open the line for questions related to the development and validation of tests for SARS-CoV-2. Please remember, during this town hall we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks everyone for joining us again. As we started, we mentioned last week, we started taking questions ahead of time by email so I will give an update on those as well as a follow up on a question or two from last week. So first I want to touch on a question that came in during the call last week that we then followed up with over some emails and wanted to clarify for everyone on the call. This is regarding the use of pooling and in what situations that is considered screening versus surveillance. We have gotten a number of questions about surveillance versus screening and it is a tricky topic. So we did clarify with this specific situation that was asking about collecting a ten-swab pool where all the swabs are placed into the same transport tube with media. With the assumption that you plan to recollect specimens from each of those individuals if the pool is positive, where the intent is to determine each individual's COVID-19 status for SARS-CoV-2 positive or negative status -- such that that individual could or would take action based on that result. So in that case the testing protocol that was proposed appears to be screening since it is intended for individual action. Along those same lines we received over email one other question related to use of an EUA to test for surveillance purposes. And what I would like to ask is that anyone who is interested in or has specific questions about surveillance, please send those in by email. __We receive a lot of questions about testing proposals that are actually screening, not surveillance.__ And so we want to make sure that we have all the pertinent details before we give you feedback so that we can make sure that we provide the appropriate feedback for your specific situation. So let me start walking through the rest of the questions here that we received. We received some questions about supporting a screening claim when there is already an EUA for the qualitative detection of SARS-CoV-2 and this is related to the supplemental EUA template that was issued last week. So our recommendation generally for validating asymptomatic screening are included in the main molecular EUA template if you are interested in an individual screening claim. If you are interested in the serial screening claim as outlined in the supplemental EUA template, you likely don't need any additional pre-authorization data. In that case we recommend that you submit a supplemental EUA request with your requested indication including the serial testing interval and your proposed post authorization validation study. Regarding serial testing we also received a question about antigen tests and whether the serial testing approach would be acceptable if the antigen assay does not reach the 80% sensitivity in symptomatic individuals. We do discuss in the antigen template for test developers that strategies for serial testing with less sensitive tests such as the PPO less than 80% may be able to support authorization. But in those cases we would expect the clinical evaluation in an asymptomatic population to be completed prior to authorization of a screening claim. The shift of the validation to post authorization discussed in the supplemental template is not applicable for tests with sensitivity below 80% in symptomatic subjects.

Tim Stenzel (FDA IVD Director):
And I would just add that the pathway for, you know, those suspected with COVID for an antigen test, you know, it's still available for those that have a single test PPA of less than 80% and if, you want to use serial testing in the symptomatic population as well. So pathway still remains open as described in the health piece we wrote back in September. Thanks Toby.


---

## 2021-03-31_Virtual Town Hall 49_section-titles.md

#### 1. Updates on SARS-CoV-2 Test Validations and Mutations


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen-only mode until the question-and-answer session of today's conference. At that time you may press Star 1 on your phone to ask a question. I would like to inform all parties that today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the conference over to Kemba Ford. Thank you. You may begin.

Kemba Ford (FDA):
Thank you, Courtney. Hello. I'm Kemba Ford of CDRH's Office Communication and Education. I would like to welcome you to the FDA's 49th in a series of virtual town hall meetings designed to help answer technical questions about the development and validation of tests for SARS- CoV-2 during the public health emergency. Today, Timothy Stenzel, Director of the Office of In-vitro Diagnostics and Radiological Health with the Office of Products Evaluation and Quality. And Toby Lowe, our Associate Director of the Office of In-vitro Diagnostics and Radiological Health from CDRH will provide a brief update. Following their opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall, we are not able to answer or respond to questions about the specific submissions that might be under review. I will now turn the call over the Toby.

Toby Lowe (FDA IVD Assoc Director):
Thank you, Kemba and thanks everyone for joining us again this week. I have a couple of updates and I will go through some of the questions that we received by email. Then we can get started with live questions. So first, I wanted to share with everyone that we posted a new webpage yesterday with information on the impact of viral mutation on COVID-19 tests. This is a follow-up to the letter to healthcare providers and clinical laboratory staff that we issued in January regarding the potential for false- negative results due to the impact of viral mutations on molecular SARS- CoV-2 tests. The webpage includes information about viral mutations and the potential impact as well as listing specific molecular tests that are impacted or where we have seen the potential for impact by viral mutations and specific recommendations for those tests. Right now the webpage includes the three tests that were included in the January safety alert as well as new information on three seitan tests based on new information that we have received. Going forward, we intend to include updates related to viral mutations and the potential impact on tests on this webpage and we will announce any updates through this venue as well as email blasts out to the email list and inclusion on the regular COVID update press releases. So we'll use that as a central location for those types of updates rather than individual safety alerts each time there are issues that we become aware of. So that website, you can find that on our webpage and there's an email that went out yesterday as well that I believe most people on this call likely received.

Tim Stenzel (FDA IVD Director):
Thanks, Toby. This is an effort to keep everybody updated on the current status of mutations and testing. It's there for easy access. So thanks Toby and the team for making that happen. As before, currently we do not know of any significant impact of mutations on overall test performance. That includes the new addition with seitan which is a multi-target assay. Only one target was affected by two different mutations as updated in the mutation update. So that test and the others still remain, you know, strong options for fighting this pandemic. It's out of an abundance of caution that we make these updates and we know that users might spot potential problems ahead of developer and/or the FDA and we ask your assistance in identifying concerns and bringing them to us. Thank you. Back over to you, Toby.

---

#### 9. Guidance on At-Home Serology Test Development


Toby Lowe (FDA IVD Assoc Director):
Our next question is regarding the development of rapid tests for antigen and antibody. Basically a few questions about at-home serology tests and whether there's a template available. We have not yet published a template for at- home serology tests and we're not able to speak to when or whether there will be one that is published. However, we know that some test developers have received some draft feedback from the review team and that is a good starting point. If you have specific questions about your own validation or study design, you can reach out through the mailbox or to your review team if you already have one. There's additionally a question about a test, a serology test that has already received an EUA to the point of care and what additional performance data is needed. So we would expect to see validation in an at-home setting if you are looking to have an at-home claim.


---

## 2021-04-07_Virtual Town Hall 50_section-titles.md

#### 1. FDA Update on COVID-19 Test Authorizations and Validation Guidance


Coordinator (FDA):
Welcome and thank you for standing by. Today's call is being recorded. If you have any objections, you may disconnect at this time. All participants are currently in a listen-only mode until the question-and-answer session of today's call. I would now like to turn the call over to our host today and that's going to be Irene Aihie. Thank you. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I'm Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 50th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Toby Lowe, Associate Director of the Office of In-vitro Diagnostics and Radiological Health and Dr. Kristian Roth both from CDRH will provide a brief update. Following opening remarks, with will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall, we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby. FDA Webinar

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Fifty town halls that was a milestone I didn't know I was trying to hit. So seriously though, the FDA has found this to be very helpful as a way to engage with stakeholders and hopefully you all have also found this to be very helpful. So thank you again for joining us this week and for the past 50 weeks for many of you. So, I have a couple of updates today and then we'll go through the questions that were sent ahead of time and then open the lineup for live Q&A. So, last week right after last week's town hall, we issued EUAs for five serial antigen tests. I guess it was UA3 test one of them in a few different configurations, but five EUAs. We've issued another serial screening antigen EUA, I believe, the day after. And since then we have also issued one serial screening molecular test EUA. So, those are all based on the serial screening supplemental template that we issued a couple weeks ago that we talked about on this call. And we're pretty excited that developers have been picking that up and we've been able to get several authorizations out under that approach and we know that there are other developers that are pursuing that and we look forward to keeping the momentum going there. We think this will be very helpful for the serial screening program that we know are being stood up around the country. We also since the last town hall issued an EUA for the first antibody test that can be used with home collected specimens. So that test can be used with unintelligible blood spot samples and since two allowed for processing. And then just this week our COVID testing basic front page was updated. So that's available on the FDA website and provides a lot of good background information on Coronavirus testing and the different types of tests, when to get a test, things like that. FDA Webinar Probably all things that the developers who are our typical audience on this call already know, but it's a good page to share with folks who may be interested in that information. So with those updated, I will move onto the questions that we got by email. Since started out, we got a couple of questions about validation studies for multi-analyte molecular tests looking at coronavirus as well as flu, RSV, et cetera. And the concern with acquiring archived influenza specimens particularly is one of the questions that we got. And asking whether FDA would consider the use of contrived influenza specimens for an EUA submission with the expectation that a perspective clinical study would be conducted post-authorization. We do know that there's been some concerns with the ability to obtain archived specimens. And if you are, you know, running into that roadblock, we encourage you to reach out to us to discuss your specific situations. But for the most part, we do continue to recommend the use of archived positive and negative clinical specimens rather than contrived. We know that, you know, they may be difficult to obtain, but that perspective testing is going to be with those, with actual clinical specimens is going to be generally what we expect for those types of studies. We have another similar question about studies for the same type of tests and also getting into studies that would support a potential 510K. We do generally recommend that you evaluate clinical performance of those multi NI tests with a perspective clinical study. FDA Webinar And for EUA, we have indicated that a single site using archived specimens would be sufficient and you may want to consider concerning the sample positivity due to possible degradation over time. There was also a question in that same one about specimen types and whether it was okay to use a single swab to obtain an OP sample and then also an NT sample so that the specimens tested would be OP/NT. And actually whether that would be acceptable for a 510K submission. So we do accept specimens that are a mixture of a sample that are unintelligible specimens, but if you're seeking an upper respiratory claim for individual specimen types, we do recommend that each specimen is individually correct and we generally consider NP swabs, the pharyngeal swabs to be most challenging upper respiratory metric. Kris, do you have anything to add on those questions about molecular analyte tests?

Kris Roth (FDA):
Sure, I would say there's a long documented regulatory history for flu and RSV and those types of panels and there's numerous deficient summaries that are publicly available for analytes that are not in the SARS-CoV-2 and there's a lot of information there and a lot of questions can be answered by previous decisions on this.

---

#### 2. BioFire De Novo Updates and Submission Guidance


Toby Lowe (FDA IVD Assoc Director):
Thanks, Kris. That's a really good point that all of that information is available on our website and it's very helpful for the test developer. So moving along, we have a couple of questions about the BioFire de novo. We do have a question about whether the decision summary for the BioFire will be posted and it will be. We unfortunately are not able to comment on the timeline. We are working on getting that out. I'm sure everyone is aware FDA Webinar that decision summaries for de novo sometimes takes some time to get posted. But we are working to expedite that one. We also briefly discussed just a little bit last week but there's a question about the BioFire being challenging to have access to as a predicate since it's the only de novo currently in the - the only predicate for a future 510K for a SARS-CoV-2 test. And we did talk last week that you can use an EUA authorized test as a comparator for your clinical studies even though BioFire would e your predicate for the submission itself. The question also was asking about whether there are other options such as testing to the reference panel to support a 510K. And while we do consider another EUA authorized comparator to the acceptable we do really want to see the perspective clinical study in your 510K submission. You can also include reference panel results and the clinicals that are from your authorized EUA if you have one and leverage those but they would not be, generally they would not be considered to be sufficient on their own to support a 510K clearance. Kris, anything to add on that one?

Kris Roth (FDA):
Sure, I think, you know, in this time between while we're waiting for that decision to maybe be posted, you know, the granting letter is posted and it does have the special controls noted for these types of tests and you can take a look at those special controls and design your studies to mee those requirements as well.

---

#### 3. Asymptomatic Screening and Over-the-Counter Test Authorization Guidelines


Toby Lowe (FDA IVD Assoc Director):
Great, thanks. So moving on, we have some questions about asymptomatic screening. And particularly related to the supplemental template that we put out and asking about the post-authorization validation studies. Generally we would want to see your proposal for a serial testing plan and the post- FDA Webinar authorization study in your EUA request. And we would discuss that with you during the review particularly the statistical plan which is what this question is focused on. We would want to go through that with you in detail. So we can't really get into too many details on the specific book on this call because it will be specific to each individual test and each approach that you're looking to take as a test developer to validate your test. And then along the same lines with serial screening using that supplemental template, we have some questions about the additional data that we would expect to see. And so, you know, the way that supplemental template is laid out is that it is there as an approach sot that if you have symptomatic validation data and you've been authorized for testing symptomatic individuals, that template allows you to expand your or to request expanding your claims to asymptomatic serial screening without doing that additional asymptomatic validation ahead of time. That would be the post-authorization condition. So generally, you know, for most cases as long as nothing else is changing, so you're not changing your patient population such as point of care to at home or other changes that might impact the usability. We would not expect to see additional validation clinical or usability as long as nothing is changing except for going from symptomatic to serial screening. And we could discuss that on a case-by-case basis if there are things that are changing whether there is additional data that we would need to see. And then there is another question along the same lines asking about removing the prescription requirement when going from prescription to over- the-counter. We do have recommendations in the template for OTC use that's in the non-laboratory use template for molecular and antigen tests. The supplemental template that we've been talking about also can support this FDA Webinar move from prescription to over-the-counter because one of the requirements for over-the-counter is that there is an asymptomatic claim. We generally would not authorize a test for over-the-counter use if it does not have that broad asymptomatic screening claim since that's how we would expect it to be used over the counter. And so if you are able to use the supplemental template to get that asymptomatic claim, as long as everything else about your test is appropriate for over-the-counter use and has appropriate labeling, usability user comprehension for a lay user then we would be able to do that over-the-counter labeling for you as well in that same EUA request.


---

## 2021-04-14_Virtual Town Hall 51_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Test Authorizations


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are on listen-only mode until our question-and-answer session. At that time if you would like to ask a question please press Star then 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. And now I would like to turn the meeting over to Ms. Irene Aihie you may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I'm Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 51st in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health and Dr. Kristian Roth both from CDRH will provide a brief update. Following opening remarks we will open the line for your questions related to development and validation of tests for SARS-CoV-2. Please remember that during this townhall we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene. Thanks everyone for joining us again. I have a few updates of actions that we've taken recently. Last week we authorized the Lucira Check It COVID-19 tests for over-the-counter use for single use at-home screening tests. And this one was previously authorized for prescription home testing. We also authorized the amplitude solution with the TaqPath High Throughput Combo Kit from Thermofisher. And that is a test that has the ability to perform up to 8,000 reactions within a 24-hour period. And then we also reissued the Saliva Direct Test from Yale for serial screening with self- collected saliva samples at home. So those were a few notable authorizations from last week. And then we also had a question last week that stumped us a little bit about the difference in terminology that we use in the email updates to CDRH new email updates that our Comms office prepares to send out updates to the listeners about Web site updates. And those include new or newly posted EUAs. So we did check into that and I think clarified that when the email says that it is a new posting, that it is a new test that did not have any previous EUAs and we issued a letter of authorization. If it says that it is a reissue that means that we reissued the letter of authorization and that's generally used for updates that change any of the details in the letter of authorization including updating the intended use and the conditions of authorization, et cetera. And then revised generally means that we issued what we refer to as granting letters. So those are the letters that you'll see if you expand the little plus sign on the EUA list and that will be letters that we grant to update some details about the EUA. And those are generally used for updates that require FDA  concurrence such as changing to labeling or changes to labeling but they don't impact the letter of authorization. And then if the email says updated then that is referring to updates to labeling where we might have posted new labeling without issuing any letters. So without reissuing the letter of authorization and without issuing a granting letter. And that's usually used for minor changes to the labeling fixing typos, minor clarifications, things that are generally not substantive to the performance of the test or don't involve evaluation of new data. And then we also use that updated labeling when we are adding results from the reference panel to the labeling of the test. Okay so those are my updates from last week. And now I can go through the questions that we received ahead of time.


---

## 2021-04-21_Virtual Town Hall 52_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing Guidance and Authorizations


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are in a listen-only mode all until the question and answer session of today's conference. At that time, you may press Star 1 on your phone to ask a question. I would like to inform all parties that today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the conference over to Ms. Irene Aihie. Thank you. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 52nd in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2during the Public Health Emergency. Today Dr. Timothy Stenzel, PhD Director, Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Dr. Kristian Roth, both from CDRH, will provide a brief update. Following opening remarks, we will open the conference to your questions related to the development and validation of tests for SARS-CoV-2. Soon to remember that  during this Town Hall, we are not able to respond to questions about specific submissions that are currently under review. Now, I give you to Timothy.

Tim Stenzel (FDA IVD Director):
Hello. Hopefully my sound here is good. Irene, yours was breaking up just a little bit. Okay. Good. Thanks. So, today is the 52nd Town Hall. We missed a couple of weeks due to various, I don't know, holidays and other events. But obviously, now we're, we're over a year since we started these and we're still getting a lot of callers and there's still work to do. So, I mean, we look forward continuing to work with you on, on all of this. I had a couple of introductory remarks then we'll finish up with a discussion of new pooling and serial testing and guidance that came out yesterday and then Kris, who thankfully has joined us today will go into some of the details and the recommendations in that guidance. So, to start off, you know, our current priorities for review remain unchanged. We are really looking for the biggest bang for increasing access to testing for all Americans and for all those in the United States. That includes point of care, home, and extremely high thruput of central lab tests. And as I discussed, you know, this new pooling guidance that we'll talk about will continue along those veins, that vein, and continue to expand. We believe greatly in testing as we begin to more widely reopen. I did want to just pause and talk about, you know, some of the totals for authorizations, roughly to date. I totaled these earlier in the week. We've now authorized 63 home collections for molecular, central lab testing, and 3 actually in-home tests, 2 of which are over the counter. And I'm adding that to 9 point of care tests so we have 12 authorizations for molecular devices and for that could also be of point of care. And then turning it over to the antigen side, we have authorized six submissions for in-home use, four of those authorizations are for over the counter. Adding to the 12 point of care devices,  we then have 18 authorizations for point of care uses. So, we're making progress on that front and of course, I think last week, Toby mentioned the Thermofisher Amplitude Authorization. They can test up to, and this is without pooling, up to 8,000 results a day on one instrument. And so, you should be able to add pooling to that, you actually, you know, can really get even above that greatly increase testing. So, turning over to the new pooling guidance. So, you know, we made a number of pooling authorizations as also, for screening authorizations. And these are for the pooling it's all been central lab high sensitivity molecular assays and we've learned a lot from all those submissions. And we, we have enough data from the previous submissions and their analysis of those. So that we could move forward with this new guidance that pertains to swabs and high complexity lab tests that have been previously authorized. I'd like to offer this review of streamlined pathway, in particular, we have not seen in the data we've received any issues when pool, in pools of three, 3x or less. As long as the test itself is a high sensitivity, molecular central lab test. And so, that, that, you know, to us gave us reassurance that we could offer the pathway if somebody under this new pathway wants to just offer a 3x pool, but we don't need to revisit it. We'll continue to monitor performance on market. You know of course, if there's any issues, we will address them. Going into just a bit more detail. So, you know, this is a new streamlined approach that pooled serial screening claims to certain authorized tests for use in serial testing programs. So, our previous review with FDA and authorizations allows us to go forward and the serial testing nature of this provides some additional mitigation for these authorizations to happen without the FDA first reviewing the data. And they are limited, as I said, to pool interior nasal respiratory specimens in a serial testing program. And so,  that many of the molecular diagnostic tests that have already received EUA authorization have this pathway open to them. So, these new authorizations and new pathway would offer authorization for both diagnosis and screening and when tested at least per week as part of a serial testing program. To utilize this approach, EUA holders would follow the guidance. You know if validation is required, go ahead and do that. If not, if it's the 3x pool, then once you've completed the validation or you've decided you're doing 3x, you know. You notify us and we'll update the labeling and post this on the FDA Website. The public including organizations purchasing these tests are using these services for testing pool specimens for the serial testing program can see the full list of tests that are then covered under this umbrella authorization. You know last month, we introduced a new supplement template for those seeking Emergency Use Authorization for certain tests for screening with serial testing and we've authorized a number of those. This pooling and serial testing amendment really builds upon that earlier action. All serial testing programs should include retesting individuals as needed in case there are any potential false negatives. And of course, testing alone does not replace the need for other public health measures such as getting vaccinated, social distancing, and washing hands and wearing masks. And with that, I'll turn it over to Kris to provide some more granularity to this, to this new amendment. Kris?

Kris Roth (FDA):
Sure. Thanks Tim. So, there are, you know, multiple validation pathways in this EUA Amendment and it does cover both swab and media pooling. So, if the existing, as Tim mentioned, if the existing EUA test performance with clinical sample that are above 95%. Then that 3x pooling claim is available as long as there's a serial testing program and these claims can be added to your  existing EUA, either for swab, or media pooling. There's also two other I guess pooling levels, one of 5x and one of 10x, and they are both discussed again for swab and media pooling. And to get those from additional pooling claims, you know, there are two approaches which are the same for the 5x and 10x. And the first is an analytical study and in this case, it's, you know, the study is intended to establish that the pooling approach is impacting test performance in a predictable manner. This is evaluated by testing contrived samples and head-to-head kind of study, you know, both individually and pooled. And if the CT scores follow what was expected to, you know, due to the design of the pooling approach. For instance, if you're looking at 10x media pooling approach, you have a predictable 10x dilution effect on the CT score. You know there's acceptance criteria that's laid out there and, you know, if hat acceptance criteria is met then you can go ahead and notify with that particular data set. There's also the option to test pooled and individual clinical samples. This is very similar to the approach that's already laid out in the molecular template. You know we are looking for 20% to be near the LOD and this amendment calls for testing of 20 individual positives and then other clinical samples. And then take those same 20 and test them in the proposed pooling approach and I think the target there is an 85% agreement and, you know, 5% less, less than invalid rate. So, you know, the regulatory path I think in the validation protocol, the acceptance criteria, all of those pieces are clearly laid out in the amendment letter. And I believe the intent here is to provide a kind of a recipe for, you know, what can be followed. And, you know, this is again to support, you know, clinically adding these claims to your existing EUA. That's it. Back to you, Tim. 

Tim Stenzel (FDA IVD Director):
Thank you, Kris, and obviously we can take questions on this or any other topics, and we'll turn it over to the Operator to open it up for questions.

Coordinator (FDA):
Thank you. We will now begin the question and answer session. If you would like to ask a question, please press Star 1, unmute your phone, and record your name clearly. Your name is required to introduce your question. If you need to withdraw your question, press Star 2. Again, to ask a question, please press Star 1. Our first question will come from Susan Sharp. Your line is open.


---

## 2021-04-28_Virtual Town Hall 53_section-titles.md

#### 1. FDA Webinar on COVID-19 Test Guidance Updates


Coordinator (FDA):
Welcome and thank you very much for standing by. At this time, all participants are in a listen only mode. At the end of today's presentation, we will conduct a question-and-answer session. To ask a question, please press star 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. I would now like to turn the meeting over to Ivory Howard. You may begin.

Ivory Howard (FDA):
Thank you. Hello. I'm Ivory Howard of CDRH's Office of Communication and Education. Welcome to FDA's 53rd webinar in a series of virtual Town Hall Meetings to answer technical questions about the development and validation of tests for COVID-19. Today Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health and the Office of Product Evaluation and Quality, and Toby Lowe, both from CDRH, will provide a brief update. Following opening remarks we will open the line for your questions. Please remember that during this Town Hall we're not able to respond to questions about specific submissions that might be under review. Now please welcome Dr. Timothy Stenzel.

Tim Stenzel (FDA IVD Director):
Hello and, you know, welcome again to this Town Hall call. And we look forward to helping as much as we can on this call. And we do have some questions we received in our inbox. Last week, I neglected to go over those. My apologies, we'll try to hit all of those that we haven't already answered offline today. I'll start off just by, you know, going over our current priorities again. They remain focused on expanding access to testing. This includes primarily diagnostic tests at home and point of care tests, and also collection at home and as well as extremely high throughput central lab tests. And with that, I will turn it over to Toby who will have some additional announcements. And then we'll get into the questions that we received prior to the meeting. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Thanks Tim. Thanks everyone again for joining us today. Just a quick update on the web page for EUA authorized serology test performance. If you're on our email list you likely got an email earlier today. That page has been updated to provide additional information on the expected predictive value of authorized serology tests that have submitted performance data to provide information for prevalence assumptions ranging from 5% to 50% to potentially help healthcare providers interpret those antibody test results for their patients in their communities. And then I wanted to quickly update again on the pooling and serial testing amendment that went out last week that I believe Chris and Tim spoke about on the Town Hall last week. There were a couple of topics that we wanted to highlight. I know that one of the topics that came up last week was regarding a condition of approval. I believe its Condition F about a post-authorization study. And we just wanted to clarify. That commitment or that condition is specific to the screening aspect of the indication. So the pooling aspect we do expect to be validated ahead of time as outlined in the amendment. And those - that validation should be submitted as part of your request to be added to the exhibit. The post-authorization condition lines up with the approach that we outlined in the serial screening supplemental template that we posted last month. March 16th I believe. That provided a path for authorization of screening claims prior to validation with asymptomatic individuals. So under this amendment we've rolled that in so that if a test did not previously have screening claims the amendment will give that test the serial screening claims and the post-authorization condition requires that validation with asymptomatic individuals. So we wanted to clarify that. And hopefully everything else was fairly clear on that amendment. But I think we do have some of the questions that we'll go through, also touch on that. So we'll talk some other aspects of it. So moving onto the questions that were sent in ahead of today's call, actually the first one is about that pooling and serial testing amendment. And the - this question is specifically asking whether this only applies to RT-PCRs or whether other types of nucleus acid amplification tests could also fall under this amendment. So the amendment is specific to previously authorized molecular-based RT- PCR SARS-CoV-2 tests that are - that meet all of the criteria outlined in the amendment. This is based on the experience we've had with SARS-CoV-2 tests over the past year and our experience with data that demonstrates that tests within the scope of the amendment are likely to maintain appropriate performance when they add pooling. Other types of NAATs may be able to add the same indication but we would expect an individual supplemental EUA request to add the same pooled serial screening indications. The validation approaches that are outlined in the appendices of the amendment may be applicable depending on the technology. But you would have to take a look and see whether those validation approaches would work for your test. For example, there are, you know, some of the validation approaches require the use of CT scores and some tests don't return CT scores. So there are two validation options for media pooling. Option 2, I believe it is, does not rely on CT scores so that would likely be the applicable validation option for a test that does not use CT scores. Tim, did you want to add anything on that?

Tim Stenzel (FDA IVD Director):
No. I think that's good. Thanks Toby.


---

## 2021-05-05_Virtual Town Hall 54_section-titles.md

#### 1. Updates on FDA COVID-19 Test Submissions and Recommendations


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are on listen-only mode until the question-and-answer session. At that time if you would like to ask a question over the phone please press star then 1. Today's conference is being recorded. If you have any objections you may disconnect at this time. And now I would like to turn the meeting over to Ms. Ivory Howard. You may begin.

Ivory Howard (FDA):
Thank you. Hello. I'm Ivory Howard of CDRH's Office of Communication and Education. Welcome to the FDA's 54th webinar in a series of virtual town hall meetings to answer technical questions about the development and validation of tests for COVID-19. Today Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director for Regulatory Programs, will provide a brief update. Following opening remarks, we will open the line for your questions. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now please welcome Dr. Timothy Stenzel.

Tim Stenzel (FDA IVD Director):
Welcome again to this week's call. We look forward to engaging you. We did receive some prior questions which Toby will go through first. There aren't that many so we'll go through all of them first and then go to live questions. I did want to make one comment and that is we still recommend that any molecular comparator for any submission be of high sensitivity with an extraction step and that it be EUA authorized as used in the developer's, in the sponsor study. If it is not EUA authorized or if there is an alteration to the authorized method it will cause a significant delay in our review because then we'll be required to bring in a molecular review group to look at the method that you use. So if you want to streamline your submission we recommend you use an EUA authorized test. We also recommend that you check with us first to make sure it's an appropriate molecular comparator. And if there is some requirement by what - for whatever reason for your product, to make an alteration to an EUA authorized product or not use an EUA authorized product, we do recommend you reach out to the FDA and explain that and let's have a discussion, to make sure that, you know, that is the most efficient and best way to go forward. So yes, that's just going to help you, the developer group, to have an efficient review by our teams. And we have seen issues come up. We've seen issues come up that - aware that sponsors did not do this and in both different cases, and it has caused significant delays in the review and so we recommend we together, try to avoid that. Okay. Thanks. Over to Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Tim. Thanks everyone for joining us again this week. I'll go through the questions that we received through the mailbox prior to today's call. So the first one is about validating changes in the volume of collection media, specifically they're noting that they've validated their assays for specific volumes and are considering increasing or decreasing the volume of collection media. And since the LOD is defined in terms of concentration it doesn't reflect the change of sensitivity of the assay when changing the volume. So we do recommend that you validate your test with the transport media identified in your intended use. Media is provided in a range of volumes and you should specify in your LOD testing what volume you tested and note that that's the average or expected fill volume in the VTM provided by the vendor. If you're trying to change the transport media or the volume for your test, we would recommend performing a matrix equivalency study to evaluate the LOD. And you can start with a swab spiked with known concentrations placed in different volumes of the same collection medium and follow the testing instructions for your test. That should take into account the dilution factor there. You can also, if your test uses an appropriate extraction step, you could perform a clinical evaluation with samples collected in a larger volume to test the worst case scenario. The next question that we have is asking about pre-submissions for non- COVID projects. As we've discussed previously, the volume of submissions for COVID tests has impacted our non-COVID work. And we did put out some information, I believe it was last week, about - through a Voices blog about that workload. And we, generally unless an IVD pre-submission is related to COVID-19 companion diagnostics, a breakthrough designation request, or has a significant public health impact, we have been unable to review them and we are using all of the tools at our disposal and we expect at this point, for the remainder of this year, to be declining IVD pre-submission requests that don't fall into those categories. The next question is about a serology assay developer for looking to seek FDA clearance rather than an EUA and asking whether that would be through a de novo or a 510k. Since we have not yet authorized a serology assay for SARS-CoV-2 outside of the EUA provisions, we would expect that the first submission would be a de novo request. After we get the first one and are able to classify them through the de novo process, so subsequent tests would be able to come through the 510k pathway. Our next question is about the use of serology tests after vaccination. And related to comments that Tim has made in previous town halls about, you know, certain tests coming back negative because they don't detect the antibodies that are created by the vaccine. And so this is asking whether FDA's position is that site S1 antigen-based serology tests are the most appropriate serology tests if a clinician decides to look for immune response from the current vaccines. So we generally don't have formal guidance on this topic. We can, you know, point out that the antibody testing guidelines from the CDC states that antibody testing is not currently recommended to assess for immunity to COVID-19 following COVID-19 vaccination. We don't yet know whether the cutoff for available serology tests would be the same as a protective antibody concentration threshold. That has not yet been established for SARS-CoV-2. And further studies would be needed to establish a relationship between the detection or measure of antibodies and protection from infection. So that continues to be a topic of conversation as more scientific and clinical information becomes available.

Tim Stenzel (FDA IVD Director):
Thank you Toby. Yes. This is definitely a very active area of review for the FDA. We simply don't have the data and we've checked with our federal government partners to support such immunity claims at this moment. As we have authorized for non-COVID, for certain non-COVID infections where monitoring antibodies and antibody levels have been authorized. So there certainly isn't necessarily any prohibition about moving in this area. We simply wait enough data to understand. It's quite likely that a quantitative test is - a truly quantitative test may be the best answer ultimately, as we have- as those have been primarily if not exclusively, the ones that we've authorized for other amenable infections and the vaccinations for them. Okay Toby. Back over to you.


---

## 2021-05-12_Virtual Town Hall 55_section-titles.md

#### 1. FDA Updates on COVID-19 Testing and Submissions Priorities


Irene Aihie (FDA Moderator):
Today Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostic and Radiological Health in the Office of Product Evaluation and Quality and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health also from CDRH will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
So thank you Irene and welcome back. Yes we look forward to having today's call and doing our best to address developers questions. I did want to go over to topics first before turning it over to Toby. And we will go through selected questions that were received prior to the deadline for this call and for which we formulated answers. First I want to go over our current priorities. They remained largely obvious and unchanged. Of course we've issued new amendments recently pooling and screening asymptomatics. And for those tests that qualify for those amendments those are obviously priorities for us because they're both designed to increase access substantially for testing. And of course our continued focus on particularly on diagnostic tests for point of care in home and home collection of diagnostic tests remains top priority and as well central lab tests that are extremely high throughput tests. All of these again are designed to increase access to testing and hopefully decrease turnaround time and better and folks are better able to manage this virus and in particular as they go to work and go to school and as we prepare going back to school in the fall. The second topic has to do with regular full submissions to ARGOS. So we are now in the process of removing all the MDUFA files that for full authorization that were on hold. The vast majority have already been taken off hold. And going forward we're not going to place files on hold due to workload issues. There is one area though where we still do not have the bandwidth to handle currently for regular submissions. And this has to do in the category of what's called Pre-Submissions or Q-subs. And we are reviewing a select categories of Pre-Subs. These are not pre- EUAs. These are normal well submissions sort of pre-submissions. And they include COVID related pre-submissions. So for those developers who want to see feedback on their proposed plans for converting to full authorization we are accepting Pre-Subs and we are reviewing Pre-Subs. We would ask as with all other full authorization sort of submissions typically we're doing our best to hit our MDUFA guidelines for times but we are swamped and we're going to do our best to try to hit those usual timelines but in some cases if not many we're going to have to go a bit longer due to the workload and continuing workload for COVID. So the other piece that we we'll be continuing to review are breakthrough requests, IDE requests and companion diagnostic requests. So the whole point of bringing up MDUFA is to, you know, generally let people know about what we're doing on that front but also to encourage those test developers who want to have a COVID related test on the market for long-term that we're open for business on Pre-Subs for COVID and our full submissions for COVID. Of course for molecular, for the lion's share of molecular tests we've already authorized one de novo and that means all subsequent molecular submissions for SARS CoV-2 whether they be single analyte for SARS CoV-2 or a multi- analyte panel, they all, you know, they meet the other criteria, fall under that, the new pathway, continue with the 510k. For serology and for antigen tests, the first submissions will be de novo. Thereafter the lion's share of those will then also be 510ks. So we do actually urge folks developers who want to be in the market long term with the SARS CoV-2 test to begin turning their attention to this and preparing for full authorization and in particular making sure that they have the samples needed or banking of samples is allowed to do all the analytical work as well as the clinical validation that we expect for those full authorizations. So now is the time I think to not delay to turning attention to that. We hope that the, you know, there's what of about 40,000 new infections a day in the US right now, it's still substantial. We do hope that that continues to fall and it falls greatly. So we have seen following prior emergencies where developers when they turn attention to moving towards a full authorization, the positive samples fell off and they struggled at times at forgetting positive samples. So I just bring that up because I think, you know, the FDA is obviously interested in full authorizations and I think developers are too and I wanted to bring this up. And I will be probably reminding developers of this relatively frequently going forward. Okay those were the two topics I wanted to cover. Now over to Toby. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Thanks Tim and thanks as always to everyone for joining us again this week. We do have a few questions that came in that we're going to address before we open it up to the phone lines. So the first question that we have is asking about saliva collection devices and whether a saliva collection device or a specimen is added to VTM prior to testing need to have an EUA? There are - and the answer is yes. There currently are no FDA cleared or approved saliva collection devices intended for use with viral RNA. Since these are not 510k exempt devices FDA authorization either through full premarket review or through EUA is required for these saliva collection devices. We have to date issued three EUA as I believe for saliva collection devices for use with SARS CoV-2 tests. And we recommend that you look at the authorization documents for those three EUAs as a reference point. Additionally, the home specimen collection molecular diagnostic template includes some recommendations including four analytical and clinical studies that may be applicable even if the selection - or sorry a unintelligible saliva collection device is not intended to be used for home specimen collection specifically.

---

#### 13. Defining High Throughput and Testing Prioritization Criteria


Jackie Chin:
Just following-up on the previous question on priority. In particular if a developer has got multiple tests like the unmet needs such as the - a neutralizing antibody test or other type of technology they - it's not on the high throughput platform that so it is not - so it cannot test at least 150 tests at once but it can still test multiple tests at once. Is this of a lower priority than other POC tests or the bigger platform test?

Tim Stenzel (FDA IVD Director):
Yes so again we're looking at access. And so it does - it's home, it's point- of-care or it's high throughput. It really needs to pass those bars right now first, those thresholds. Having a great neutralizing antibody assay that can't really help that many people is not going to address the country's needs right now. So we are, you know, this is - you know, these priorities are out there for clear reasons. One is to inform developers of what we're not prioritizing. And it also is to hopefully stimulate developers to develop the tests that are really needed at this stage of the pandemic. Okay?

Jackie Chin:
Okay. Can you define high throughput? Is it at least 150 at one?

Tim Stenzel (FDA IVD Director):
So, yes as we said before if you want to check and see if your test will meet current priorities, you know, do send in a pre-EUA with relevant information for us to assess that. You don't have to fill out a full pre-EUA if you're going to use the templates as in the template recommendations as intended. You can simply say our one question is do we need the high throughput at all? That is something that we're not publishing right now because as we go through the pandemic that may - they may elevate and if the needs change. So it's best just to check with our staff through the pre-EUA process to see if your test would currently match our priorities.

Jackie Chin:
Thank you.

Coordinator (FDA):
Thank you. Our next question is from Dana Hummel. Your line is open.


---

## 2021-05-19_Virtual Town Hall 56_section-titles.md

#### 1. FDA Virtual Town Hall: SARS-CoV-2 Testing Updates and Questions


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are in a listen-only mode until the question-an- answer portion of today's call. During that time if you would like to ask a question, please press Star 1. Today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 56th in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Toby Lowe, Associate Director of the Office of  In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality and Dr. Timothy Stenzel, Director of the Office of  In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during the Town Hall, we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene. Hey everyone, thanks for joining us again this week. Excuse me. Every week I'm always amazed when I hear Irene announce the number of the Town Hall that we're on. It's been quite the, the year, plus a bit at this point. So, I have one update to give this morning, or this afternoon, and then I'll go through some of the questions that we received in advance. So, first I just want to highlight that right before the Town Hall, a new Safety Communication was posted discussing the use of antibody tests after COVID- 19 vaccination. And specifically, recommending not to use antibody tests to assess immunity after COVID-19 vaccination. So, those of you on this call most likely get the emails that go out with updates when we put out actions like this. So, you probably have gotten that just a short while ago, and if not, it is found on our Web site under Medical Device Safety Communications. And there was also a press release issued or rather an FDA in brief press statement. So, you can find that on our Press Announcements page as well. And with that, I will switch over to some of the questions that we received ahead of time and I'll go through those. So, the first, the first question that we got in is related to modifications to an authorized molecular SARS-CoV-2 assay. Specifically, to speed up the processing time by implementing a software change to a fully automated system to allow the system to simultaneously perform some steps that were previously performed sequentially. The question notes that the change would be implemented through their design control process, design change control process, and validation data would be documented in their quality system. And that there were no changes to the assay design or reagents so they're asking whether they can put out that change without further amendments to their EUA. So, that will depend a little bit on the changes that are made if parameters to the test which is the temperature, dwell times, ramp rates, or the extractions speeds are changed. Then we would expect performance to be impacted. And in that case, we would expect a supplement to an EUA request. If your proposed change did not impact the performance of the device or change to the claims in the intended use or introduced substantially new information such as the addition of new hardware to support the software change, or any additional steps the user needs to take into the instructions for use or any of the authorized labeling. Then the change could be made without further amendment. An example to that would be if the reaction steps used the same parameters on a per-sample basis. Then there would be little risk that performance would be impacted.

---

#### 5. Validation and Approval for Home Use Antibody Tests


Toby Lowe (FDA IVD Assoc Director):
The next question that we have is about home use antibody tests and asking specific questions about the validation and prioritization. So, unfortunately since we have not yet finalized a template for COVID-19 serology home use self-testing, we're not able to comment further at this time on specific validation study recommendations. And we would recommend that you reach out through a pre-EUA or if you would like to pursue a de novo or 510k through a pre-submission to further discuss your approach.


---

## 2021-05-26_Virtual Town Hall 57_section-titles.md

#### 1. Guidance on Validation and Study Design for SARS-CoV-2 Tests


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are in a listen-only mode. At the end of today's presentation, we will conduct a question-and-answer session. To ask a question please press Star 1. Today's conference is being recorded. If you have any objections, you may disconnect at this time. I would now like to turn the meeting over to Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I'm Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 57th in a series of virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Toby Lowe, Associate director of the Office of In vitro Diagnostics and Radiological Health and Dr. Timothy Stenzel, Director of the Office of In vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to development and validation of tests for SARS-CoV-2. Please remember that during this Town Hall we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks Irene and thanks everyone for joining us yet again this week. I don't have any particular announcements today, so I'll start with the questions that we received by email ahead of time. The first one that we have is related to equivocal evaluation study preparing for a 510k submission for a respiratory PCI multiplex panel, including COVID-19 Flue A-B and RSV. The question notes that FDA generally requires that the Flu and RSV comparative methods be cleared by 510k PCR devices. But they're getting feedback from many CLIA labs that manufacturers have stopped selling their Flu and RSV multiplex kits and are only manufacturing their EUA multiplex kits that have COVID added into it. So, the question is asking whether it would be possible to use an EUA respiratory multiplex kit for COVID, Influenza, and RSVP, I'm sorry, RSV as the comparator in the clinical study. So, generally we do recommend that the respiratory multiplex comparator methods are 510k cleared. But we do know that that's, that maybe challenging at the moment, so you could also consider using an EUA-authorized, highly sensitive RT PCR assay as your comparator method for your clinical evaluation. But we do note that the EUA tests are validated with a different level of evidence than a 510k tests, a cleared test. So, we would probably recommend that you use multiple EUA tests in an algorithm to determine positive and negative comparator test results. For example, you could use two EUA tests per sample of the comparator and if there's disagreement between those, use a third tiebreaker test. And as we've mentioned here on this call before, we do recommend that if you're pursing 510k pathway, that you submit a presubmission to discuss your proposed comparator method. And, you know, as I'm sure most of you are aware when you submit your 510k, you do need to have a predicate that has been cleared or de novo-granted device. And so, right now that is just the BioFire assay so that would be an appropriate predicate, but it does not have to necessarily be your comparator method. Our next question has to do with a topic that was previously discussed on the Town Hall, where the question is stating the FDA mentioned that after 50% of clinical specimens for a 510k clinical validation study can be frozen prospective specimens. And they're asking if we can confirm if frozen retrospective samples can be used as well if they're retested on a comparative method in the clinical study. And if not, to please provide more information on how the frozen prospective samples should be collected to qualify for the clinical validation study. Such as whether they can be US or outside the USA, if they must be collected during the clinical validation study and not before; whether the concerned positive-negative status must be known. So, generally we do recommend that clinical studies include prospectively fresh and frozen samples to preserve analyte prevalence. Retrospective samples are considered to be selected and archived samples that are previously frozen usually based on a previous positive result. So, since that approach is more than minimally biased since the prevalence is generally not preserved, that's not, not our recommended method. Typically, the, or often the archived samples are also very high concentration so they would not be near the LOD of the assay and may not be reflective of the actual patient population. So, we do agree that sponsors can supplement with retrospective samples but usually only after conducting a prospective study which yielded too few samples to demonstrate adequate performance. In terms of US versus outside the US, we recommend that sponsors conduct their prospective clinical studies primarily in the US to support a 510k or de novo. Data from outside the US prospective clinical studies can also be submitted to supplement the US data, especially in cases where there's difficulty getting enough specimens in the US due to low prevalence with a heavily vaccinated population. Our next question also has to do with enrichment studies due to the current COVID positive cases decreasing here in the US. And mentioning a comment in that Dr. Stenzel made on a previous Town Hall about the acceptability of enriching studies in order to meet the study requirements. The question is asking if we can clarify what would be appropriate for study enrichment. So, there are multiple options for clinical study enrichment, and they really should be appropriately tailored for your specific test and the claims that you are validating. So, we do recommend that we, that you submit a pre-EUA so that we can review your proposal and consider the alternate study designs that would streamline enrollment of positive subjects when prevalence drops low. That would be best appropriate or most appropriate for your, for your situation.

Tim Stenzel (FDA IVD Director):
Yes, and thanks, Toby. And I would add that, the original reason to offer enrichment was for stimulating additional development of screening assays. You know for screening asymptomatic patients and when it was, when in sometimes in populations that's very low or you have to screen a lot of folks. We have now considered doing to allow enrichment for original submissions where obtaining of positives may be more challenging, symptomatic positives even. And, you know, where maybe banked samples are not appropriate or of such. But we would still like to see, you know, a prospective attempt to try to get true positives and then looking at supplementing them with a method of enrichment. Banked samples is one. The other is to use some sort of selection where a patient may be and this might be more, so for, an asymptomatic carrier then an symptomatic person. But it could also be done with an symptomatic person and that is, where they are identified as positive with some orthogonal method and some sort of routine study or protocol for screening. They would be open to study designs that try to mitigate the bias in that situation. If the patient themselves knows the result of the test and it's not going to involve self-collection for the candidate test, then that may be acceptable. If the patient although is going to be doing self-testing with candidate device knowing the previous result, this will bias the result. But, you know, for the situation where they're not going to be self-collecting for the candidate device, the person doing the collection, you know, should be blinded to the previous results. The patient should be asked not to identify whether they were positive negative and of course, to keep the immigration of the study honest and unbiased. A suitable number of negative patients should be offered in the same way so that the person doing the testing doesn't assume that it should be positive. This way, bias can be mitigated to a greater extent. So, there are multiple paths, and we're open to multiple paths. We do recommend, highly recommend, that you run those strategies by the FDA prior to initiating your study. And in order to avoid any sort of duplication of studies because study plan and design was not suitable. Back over to you, Toby.


---

## 2021-06-02_Virtual Town Hall 58_section-titles.md

#### 1. Updates on SARS-CoV-2 Test Development and Safety Concerns


Coordinator (FDA):
Welcome and thank you for standing by. Today's call is being recorded. If you have any objections, you may disconnect this time. All participants are in a listen-only until the question-and-answer session of today's conference. At that time, you may press star 1 on your phone to ask a question. I would now like to turn the call over to your host, Ivory Howard. You may begin.

Ivory Howard (FDA):
Hello. This is Ivory Howard of CDRH's Office of Communication and Education. Welcome to the FDA's 58th webinar in a series of virtual Town Hall Meetings to answer technical questions about the development and validation of tests for SARS-CoV-2. Today, Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health both in CDRH, will provide a brief update. Following the opening remarks, we will open the line for questions related to the development and validation of tests for SARS-CoV-2. Remember that during the Town Hall, they're not able to respond to questions about specific submissions that might be under review. Now I give you Dr. Timothy Stenzel.

Tim Stenzel (FDA IVD Director):
Thank you and hello everyone. Welcome to another week of the Town Hall. We have some opening remarks and then we'll go into the received - the questions received prior to today's call and open the line. We are still seeing a significant number of applications every week. I mean, and then as a monthly total for COVID EAUs, pre-EAUs, amendments, and supplements, we're seeing still around 160 to 200 applications a month. And this is keeping us very busy, especially since the surge in staff for COVID has largely returned to prior to the surge capacity and workload per reviewer. So though the surge folks have gone back to regular MDUFA work, which does include COVID pre submissions, Q submissions, and full submissions for COVID assays. That does leave us back to a lower level of staffing for EUA. And I just wanted sponsors and developers to know that. We're doing our best to keep up with the volume and largely we're clearing applications weekly at the same - approximately at the same rate that we're receiving them. So we should be cycling through on a pretty routine basis. So but because we have fewer staff, our times for responses and everything may go up a little bit. This is unfortunate, we know. We're doing the best we can. We ask for your patience. On the other hand, we've now authorized over 380 unique submissions and well over 500 supplements and amendments to date. So there is quite a significant number of tests available in the market. And we have seen testing go down across all categories in the U.S. and also the number of positive samples is way down. Let's remember that positive samples and percent positive rate going way down is great news for the country. I just want to put all that in context. All right. And our priorities remain the same as most recently previously stated, diagnostic tests for point of care, in-home and home collection and high throughput central lab tests. And I will turn it over to Toby. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Tim. Thanks, everyone for joining us today. I have one update. We - on Friday of last week, we issued a safety communication regarding a Class I recall for the Lepu Medical Technology's SARS-CoV-2 Antigen and Leccurate Antibody Tests. These were tests that had not been authorized, cleared, or approved by the FDA. And the company is recalling them under a Class I recall because they were distributed as unauthorized tests. We are aware that they were distributed to pharmacies to be sold for at-home testing by consumers, as well as offered for sale directly to consumers. So that safety communication and Class I recall were posted on Friday of last week. And then I can move into the handful of questions that we received ahead of time. The first one we have is related to comments that were made on a previous Town Hall recommending that for antigen and molecular test data subset should be provided in the EUA submission for vaccinated individuals enrolled in the clinical study. And the questions being asked are for a point of care and over-the-counter EUA low cost for a lateral flow antigen test, what data should be collected from the enrolled vaccinated subjects to be provided in the data subset? And if a vaccinated subject is confirmed positive or negative with both the candidate device and the EUA authorized highly sensitive RT-PCR comparator method in the clinical study, can the vaccinated subject be considered part of the confirmed positive or negative samples needed for the EUA submission? So to address those, first, we would ask that the data be included in the clinical line data of additional columns and should include the date of vaccination, which vaccine was administered, and if it's a multi-dose vaccine the number of doses and the dates that were - that they were administered. And then it may be acceptable to include all subjects together provided that they're not pooled retrospective and prospective specimens. But we do want to see the performance stratified by nonvaccinated verse vaccinated individuals. And depending on the specific situation, we may request additional presentations of the data, such as one dose verse two doses. And we would also want to see asymptomatic and symptomatic stratified as well.


---

## 2021-06-09_Virtual Town Hall 59_section-titles.md

#### 1. Updates on SARS-CoV-2 Testing and Mutations Impact


Coordinator (FDA):
Welcome and thank you for standing by. At this time all participants are in a listen only mode until the question and answer session of today's conference. At that time you may press star 1 on your phone to ask a question. I would like to inform all parties that today's conference is being recorded. If you have any objections you may disconnect at this time. I would now like to turn the conference over to Ms. Irene Aihie. Thank you. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 59th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Dr. Kristian Ross, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks everyone, for joining us again this week. One update that I have before we get into the Q&A, is late last week we updated the Web page on SARS-CoV-2 viral mutations and the impact on COVID-19 tests. We added new information about a potential impact on the performance of the MESA Biotech Accula SARS-CoV-2 test, due to a genetic mutation at specific positions in patient samples. That test was already listed on that Web site so it's not a new test that we've identified in the impacts from viral mutations. It's just an additional mutation that we have identified that impacts that test. Same as in the previous communications about the impacts on COVID-19 tests, we do not think that this impact is significant. But we are providing this information out of an abundance of caution and we will continue to do so, updating this Web page and sending out information about impact of viral mutations, as additional information comes about. And with that, I will move onto the prepared Q&A that we have. So the first one is about antigen tests regarding using fresh samples and that FDA has generally indicated a preference for fresh samples for supporting antigen tests. However, this inquiry notes that there's a growing complexity of obtaining fresh positive samples and that the sponsor would like to freeze samples collected during a post-EUA study and then use frozen samples to support development of another assay for an EUA submission. And they're seeking FDA feedback on that. And then along with that, they're also asking about achieving the sample sizes currently discussed for post-authorization studies and the difficulty in achieving those sample sizes due to dropping positivity rates and rising vaccination rates in the US. So they're asking what other options are available to reach those post-EUA study numbers.


---

## 2021-06-16_Virtual Town Hall 60_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing and Prioritization


Coordinator (FDA):
Welcome and thank you for standing by. At this time, all participants are in a listen-only. This call is being recorded. If you have any objections, you may disconnect at this point. Now, I will turn the meeting over to your host, Irene Aihie. You may begin.

Irene Aihie (FDA Moderator):
Hello. I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA's 60th in a series of Virtual Town Hall Meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this Town Hall we are not able to respond to questions about specific submissions that might be under review. Now I give you Timothy.

Tim Stenzel (FDA IVD Director):
Hello again. Thanks for joining us. We hope you find today's call helpful and instructive. Couple announcements and then I'll hand it over to Toby who will go through the questions received by email ahead of this meeting. First off is did want to discuss serology testing a little bit. We've had numerous inquiries about using serology to measure immunity and/or protection either from natural infection or following vaccines. This is a hot topic for our office. We are awaiting data from U.S. Government-sponsored immunity and protection studies to understand what are the factors that determine and can be relied on to make these assessments. You know, sponsors, test developers are free to generate that kind of information, although, it seems like it would take fairly large studies to see what a certain level of antibodies, for example, offers in the way of immunity because you are looking at outcomes. So, you know, as soon as we have definitive information about how to measure immunity and protection, we will be able to provide some more help to developers as far as what our recommendations are for validation of serology tests for this purpose. So stay tuned. We can't - we don't know when that information is going to be made public. We expect we'll see it, you know, and pretty much real- time. And it will probably be made public pretty much in real-time as well. So we're waiting on pins and needles. Next topic is priorities. Our current priorities remain the same. We are focusing on ways to expand testing opportunities, making it more accessible. We do think it's important that there are lower-cost opportunities. And so over-the-counter and home diagnostic tests and collection devices are our priorities, as are really high throughput diagnostic central lab tests and point of care tests. Finally, I wanted to make a few statements about our current workload. We are still receiving a high volume of submissions for COVID. And however, we are keeping up with the volume even with reducing the surge, mainly to pre-surge, almost to pre-surge level as far as staffing goes. But we are staying ahead of it. We are closing out our files more quickly than we are receiving them. But there is still a bit of a backlog. In particular, the pre-EUA backlog is not insignificant. And Toby and I have been making recommendations on recent calls for certain callers to check-in through the pre-EUA process. So we - you know, the pre-EUA process is not a required process. And it's designed to try to be helpful and make sure that we're aligned on what the recommendations are from the FDA. So test developers can, you know, not do something and find out it doesn't quite work. Developers are always able to go ahead and submit and do the work and submit their EUAs. However, there are certain things that, you know, that may not be known. So we really are hoping only to advise your pre-EUAs, those things that are unique and different from what are present in the template. So, you know, look at our prior decisions. Look at - that are public. And look at, you know, our templates. And hopefully, that meets the lion's share of pre-EUA requests. We know that there's questions that don't quite neatly fall in the template. You know, it is our priority to get through those pre-EUAs. It's just that we have a significant number of submissions, as I said. And we're doing our best to work through them. Okay. With that, I will turn it over to Toby so that she can get into the questions.


---

## 2021-06-23_Virtual Town Hall 61_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Testing and Innovations


Coordinator (FDA):
Good afternoon, and thank you all for standing by. At this time, all participants' line are in a listen-only mode. After today's presentation, you will have the opportunity to ask questions, and you may do so over the phone by pressing Star 1 at that time. Today's call is being recorded. If you have any objections, you may disconnect at this time. It is my pleasure to turn the call over to your host for today, Ms. Irene Aihie. Thank you, ma'am. You may begin.

Irene Aihie (FDA Moderator):
Thank you. Hello, I am Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA 61st in a series of virtual town hall meetings, to help answer technical questions about the development and validation of tests for SARS- CoV-2 during the public health emergency. Today, Dr. Timothy Stenzel, director of the Office of In Vitro Diagnostic and Radiological Health, in the Office of Product Evaluation and Quality, and Dr. Kristian Roth, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall, we are not able to respond to questions about specific submissions that might be under review. Now, I give you Timothy.

Tim Stenzel (FDA IVD Director):
Thank you, Irene. So, welcome again to this week's call. We continue to get some really good questions pre-submitted, and we will respond to all cases - all questions, whether live here on the call or offline. So, if we do not mention your question, rest assured that either we've already sent something, or we will send something relatively shortly as far as a response to your question. And sometimes questions - some questions are best handled offline. We look for general applicability to these questions and rather than sort of specific questions. I wanted to start off with some announcements, just some updates, and then move into the pre-submitted questions, and then into the live questions. So we continue to see SARS positivity rates fall in the US. That's great. We do continue to see the Delta variant increasing in the percentage of the positives, and it's - Delta variant rise is particularly in those who are unvaccinated, which, there are in some areas of the country, a large number of unvaccinated adults. So, we're monitoring this closely, and hope all is well. But we're pleased with the overall rates falling, as we'll get into in some questions today, and, you know, there is some challenges when the rates are falling for test developers. I wanted to also expand upon those things that we're currently reviewing. So we've stated frequently our current priorities are still the same. Did want to expand, so we will see new technologies be developed that could be helpful in this pandemic. And our stated priorities are not intended to cover those things that we don't know about, or are new. Our stated priorities largely revolve around detection of Immunoglobulins, the raise to natural infection for SARS or a typical serology test, antigen tests, and molecular tests. So there are technologies that are new, novel, unique, and may come to bear and be helpful. And we recommend that you check with us through the pre-EUA process to see if it's something that we think would fall under the EUA review criteria and that we think has potential to impact in a positive manner, our pandemic response. And I will call out one particular type of test now that is emerging, and we've heard about, and that has to do with T Cell assays. We have authorized already a T Cell receptor sequencing beta-receptor sequencing assay. That particular assay functions largely in a way a typical serology assay doesn't in that we're looking at a T Cell receptor response to SARS-CoV-2. There are other T Cell assays that are more looking at functional T Cell response, and those are the newer types of assays that we're hearing about. So, you know, I just want to state that these types of new technologies, want to hear about through the pre-EUA process. If we think there's potential, we want to work with the developers to work on an EUA submission. And we are absolutely receiving these T Cell functional assays now for review, and do hope that ultimately they will pan out to be helpful, although I think there's a lot of open questions that remain. But we're committed to reviewing those right now. I also wanted to talk about two other things. One is the use of international studies, given the falling rates of SARS positivity in the US right now, and conversions to full authorization. So, we're continuing to recommend those that want to remain long- term on the market, you know, this would be, you know, probably long-term in the future, that this would be necessary to stay on the market. But we are encouraging the folks who want to go this pathway, to convert their EUAs to full authorization. We know that with the falling rates, this is challenging. When appropriate, we'll make full use of banked samples, in addition to prospective trials or rather studies, not trials, prospective clinical studies. We are also now very open to the use of international studies to acquire positive samples. That's both for EUA and for conversions. So we've done this in the past when rates of positivity in the US are too low, or are relatively low and are very challenging to developers, such as pathogens such as Ebola, TB, malaria, dengue fever. So we've done this in the past. And now that we are seeing falling rates in the US, we are more open to the use of international studies. We do want to make sure that they are done as we recommend. For example, if they're point of care tests, that the settings that they're evaluating in internationally, are truly point of care. We want to make sure that the language requirements are there. You know, non-US foreign language instruction should not be used to instruct non- US users of the test. And this applies - point of care can apply also to home tests if the appropriate settings are used for evaluating home tests. This is all in an effort to get actual positive patient samples for the validation, which is always preferable to the alternatives, which is why we're encouraging that now. Okay. I think with that, we'll move into the pre-submitted questions. Let me just pull those up. So the first question has to do with the use of retrospective samples for antigen test validation. And in particular, the question was, can we use banked samples, banked frozen samples for OTC, over the counter and or home test applications? And while we're - and I'll get to it. While we're open to using banked frozen samples for point of care validations, it's really, really challenging using home users to substitute samples. So, that's why I'm encouraging international studies when needed for home testing and or point of care testing if it's difficult to get the banked samples. But for point of care, as I'll get into, there's a pathway and - or if you use this for a long time already. So, we do not recommend banked samples for home test validations, whether OTC or prescription use. We do want to see - we recommend fresh samples, as we're really looking at the lay user collection process here. So we want to know that home users can collect and also accurately perform the tests and get the right result to explain that. So, for - as I said, for point of care, so we would want to see a full set of a minimum of 30 positives and 30 negatives with the frozen banked samples for a point of care claim. And then we would authorize that test if we saw a minimum of at least five prospectively collected positive samples with successful performance, in addition to the frozen samples. So we do want a complete set of frozen samples so we can evaluate frozen samples and sample type. And we're willing to authorize them with a minimum of at least five prospectively collected positive samples. And again, those can be international if needed. And then post-authorization, we would expect the study to complete a fresh sample prospective study, so that we have a complete set of fresh samples to understand performance and to continue to allow the test to be marketed in the US. Okay. I think that pretty much covers that question. Okay. So, the next question has to do with pod pooling, and it doesn't specify whether those are antigen tests or molecular tests, point of care tests, or central lab tests. So, you know, antigen tests are particularly challenging for pooling due to the sensitivity requirements of pooling. So, that's - that would be important to have an offline conversation with our expert staff on antigen test pooling. However, for media pooling or swab pooling, both are very - we're very open to that, to non-point of care molecular tests. And - because we think moderate to high complexity labs can perform media pooling. For point of care tests, we are recommending that you consider swab pooling, and we do not recommend media pooling in the point of care. In that setting, with untrained non-laboratorians performing the testing, media pooling presents some inherent risks of a mix-up and cross-contamination that we do not feel that that - that the benefit-risk profile on point of care settings justifies media pooling. However, I think swab pooling is a great alternative, especially in the point of care setting, where you can then potentially relatively easily follow up with an additional swab for those pools that test positive. Okay. Next question has to do with priorities, having to do with panel tests, particularly as we may see a rising prevalence of non-SARS respiratory viruses. We have stated our priorities for review currently where our position is focusing on increased testing, accessibility, and capacity. Panel tests have the ability to be more efficient, because we don't know whether it's SARS or some other virus, and you end up doing two tests versus one. That's less efficient. It uses more resources and supplies. So we continue to prioritize high volume, multi-analyte devices, including, central lab, of course, but including point of care and home RX tests. We are not recommending multi- analyte tests for over the counter, which could very well include testing of asymptomatic. We just don't have any experience of using non-SARS tests in the asymptomatic population. But home RX is acceptable and is what we recommend if you're interested in a home multi- analyte device. Next question is, if you have a home - a prescription antigen test, this would apply to molecular tests as well, can you limit it only to symptomatic individuals? Yes. So that's been the pathway so far. We know - we've heard from multiple commercial parties that there is value in having a prescription home test. And you don't absolutely need an over-the-counter test to access the home test situation. And, you know, if you do your validation on symptomatic individuals in the US or ex- US, that's fine. We'll authorize the test. It will be the typical language of authorization that is, the patient is suspected of having COVID, and there won't be any claims about asymptomatic screening. And then, of course, if in a symptomatic population, the performance is acceptable for our - serial testing and pooling - not pooling, serial testing pathway for getting any symptomatic screening claim with a PPA of at least 80%, or lower bound of at least 70%, you always have the option at that point after submission or in your submission, to ask for the serial testing claim. The serial testing claim is not required. And if you want a single-use home antigen or molecular test in the symptomatic population only, that's fine. We'll definitely take a look at that. There was also a question related to the use of CT values to exclude patients in studies. We are still not recommending exclusion of test subjects based on CT values. There's multiple sources that say that CT values are not reliable enough to predict whether someone's infectious, for example. So, we are still not recommending use of CT values to exclude test results from the clinical study. The next question includes topics of point of care gene expression. Chris has given thought to this question and has prepared a response. So, I'll hand it over to Chris for responding to this question. Over to you, Chris.


---

## 2021-06-30_Virtual Town Hall 62_section-titles.md

#### 1. Developing and Validating SARS-CoV-2 Diagnostic Tests: Updates and Guidance


Coordinator (FDA):
Welcome everyone to today's conference call. At this time, your lines have been placed on listen-only for today's conference until the question-and-answer portion of our call, at which time you will be prompted to press Star 1 on your touchtone phone. Please ensure that your line is unmuted, and please record your name when prompted so that I may introduce you to ask your question. Our conference is being recorded, and if you have any objections, you may disconnect at this time. I will now turn conference over to our host, Miss Irene Aihie. Ma'am, you may proceed.

Irene Aihie (FDA Moderator):
Thank you. Hello, this is Irene Aihie of CDRH's Office of Communication and Education. Welcome to the FDA 62nd in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS- CoV-2 during the public health emergency. As a point of information, we will not be hosting a town hall on Wednesday, July 7th. We will resume on July 14th via Zoom with updated login and dial in information to follow. Today, Dr. Timothy Stenzel, Director of the Office of in Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of in Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to development and the validation of tests for SARS- CoV-2. Please remember that during the town hall, we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Irene. Thanks, everyone, as usual, for joining us this week. I have a couple of updates, and then I will go through some of the questions that we received by email before we start the live questions. So, first, I know we've had a lot of questions about the decision summary for the BioFire de novo. That decision summary has now been posted on our website. It was posted last week, I believe, on the 26th. And that can be found on the de novo summary page, as well as the - with the BioFire de novo authorization as well. And then I also wanted to update that we just recently added three tests, three EUAs to the pooling and serial testing amendment. So, that is the amendment that we put out recently to allow for a streamlined addition of pooled serial screenings to previously authorized RT-PCR tests. So, an email went out earlier this week about the three tests that were added. And those can also be found on the EAU page, the molecular EUA page, where they'll be noted under the amendment itself, as well as the authorization documents for those three tests specifically. That will be available - or that are available, rather, on that page. So, to get into the questions that we received by email, I do want to note, as we have before, that we've received some questions that are a little too detailed or test- specific or case-specific, to address on the call. So we won't address those individually on the call. So, those questions, we will try to send a response in writing within a few days. And if you submitted a question and don't hear it addressed on the call, and don't receive a written response in the next few days, please feel free to reach back out to the CDRH-EUA-templates@FDA.HHS.gov mailbox for an update. So, the first question that we have today is regarding an EUA submission for a professional use diagnostic assay, where they're pursuing a clinical performance study using retrospective samples stored in viral transport media, and as well as collecting prospective samples in VTM to complement that data set. However, they also note that they have a proprietary assay buffer that they intend to supply with the kit. And they're asking about matrix equivalency study to demonstrate compatibility with the proprietary buffer, and whether they need to repeat all the validation studies, or just the - or just do a limit of detection analysis as an acceptable matrix equivalency. So, generally, the matrix equivalency study should be performed to compare the assay performance in the VTM and the proprietary assay buffer. So, we would recommend testing be performed in parallel at the same target levels in both simulated and naturally occurring matrices. And to demonstrate equivalency, you should observe the expected proportion of positive results at each target level in both sample types. The LOD can serve as an acceptable matrix study, and if determined to be equivalent, repeating the other validation studies should not be needed in most cases.

Tim Stenzel (FDA IVD Director):
And I would just add that this is kind of a little bit of a special case, but, you know, where banked samples are used for central lab test validation, it's always been acceptable for molecular tests, for specific potential issues with antigen tests. And we want to work through that. So, but the same thing goes for point of care. So, we are accepting banked samples for point-of-care and for molecular. Typically, we would like you to use whatever buffer remains in your actual test, if there is going to be a transport buffer. Just kind of bridging study about cross-validation is perhaps a special case. We do know that using banked samples and banked positives, is going to be important for many, now that test positivity rate in the US is going down. And still, say an antigen point-of-care test, you know, we would like to see and we've done this before, in fact, the first antigen authorization was allowed completely banked samples VTM frozen, but we also recommended that they do at least five positive fresh samples demonstrating, you know, good results on those five prospective fresh samples. And the intervening negatives that happen with the collection of those fresh positives or fresh negatives and fresh positives, we expect that fresh negatives are going to be easy to obtain. And - but, you know, a complete data set on using bank samples, particularly for antigen tests, is good to establish performance. We just want to see those five - a minimum of five fresh positives, and then the remainder of the fresh positives will be placed into a post-authorization requirement study. Thanks, Toby.


---

## 2021-07-14_Virtual Town Hall 63_section-titles.md

#### 1. Updates on SARS-CoV-2 Testing Development Challenges


Irene Aihie (FDA Moderator):
Hello. Welcome to the FDA 63rd in a series of virtual town hall meetings to help answer technical questions about the development and validation of a test for SARS-CoV- 2 during the public health emergency. Today, Dr. Timothy Stenzel in the Office of Product Evaluation and Quality and Toby Lowe, associate director of radiological health will provide a brief update. Following opening remarks, we will open the line for your questions developing the test for SARS-CoV-2. To ensure that we answer questions from as many people as possible, we ask that you use the raise your hand feature. Please remember we are not able to respond to questions about specific submissions that might be under review. We will not hold a town hall on Wednesday, July 21. We will resume Wednesday, July 28.

Tim Stenzel (FDA IVD Director):
Thank you for joining, everyone. We are doing this with a different format so hopefully this works. Hopefully there will not be technical glitches. It is quite different from what we have done before, but we will work through those together. Of course, this is being recorded, so if you do not want to be recorded please drop off. First, I wanted to note unfortunately we're seeing a resurgence in cases of COVID in the U.S. We are now daily above 20,000 new cases and we also see many localities experiencing not only high numbers of cases but also high test positivity rates. Many are above 15% positivity. This is unfortunate. It is what it is. We will continue to work hard to deal with this ongoing pandemic. It does for developers, though ease some of the challenges in getting positive samples. In the recent weeks we have expressed willingness, as numbers were falling to have foreign studies done in order to get positive samples, especially in the point of care and home situations and of course we always said we would like to see, we recommend you attempt to try those studies in the U.S.U.S. first and only if you are unable to get the positives that are needed to go to the ex-U.S. site. We have given a lot of parameters around that. One of the reasons for starting in the U.S. has been we wanted to see even negative sample usability and user interaction in typical point-of-care and typical home situations in the U.S., in English, so we have a good understanding of that. Of course, with point-of-care tests, the U.S. is different than some other countries in how point of care testing is done during this pandemic in a lot of different ways now that point of care testing can be done at schools and at workplaces which have never done it before. There is more than 30,000 new waived labs in the U.S. Traditionally, and we like to see that here in the U.S., that the point-of-care study is done in busy clinical office practices where they are frequently distracted by the many things that they do in that office. And even in the midst of those distractions can get an accurate result. That is the real situation in the U.S. typically for point- of-care tests and we want to make sure the instructions in these will work such that even in the busy setting where they are not just potentially standing there watching the test develop, but if it is 15 minute incubation, they are off doing other things and they correctly get back to the testing workstation, for example, and read the test. Just some thoughts to start us off. With that, Toby I think we can go into the questions that we received prior to the call, and then we will move into live questions. Over to you Toby.


---

## 2021-07-28_Virtual Town Hall 64_section-titles.md

#### 1. FDA Updates on SARS-CoV-2 Test Validation Efforts


Irene Aihie (FDA Moderator):
Hello, I am Irene Aihie, of CDRH's Office of Communication and Education. Welcome to the FDA's 64th in a series of Virtual Town Hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the Public Health Emergency. Today, Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health in the Office of Product Evaluation and Quality, and Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to the development and validation of tests for SARS-CoV-2. Please remember that during this town hall we are not able to respond to questions about specific submissions that might be under review. Now, I give you Timothy.

Tim Stenzel (FDA IVD Director):
Thank you Irene and hello everyone and welcome to this week's installment of the FDA CDRH town hall, where we, Toby and I, and sometimes other special guests really try to be informative and transparent and direct as possible with our current thinking and our recommendations for test valid validation. This is in an effort to assist in the public health response. We continue to see this pandemic evolve and stay with us, unfortunately, in a very significant way, and so we stay very close to the situation so that we can always provide the priority for those tests that are going to best meet the needs at the moment, and this has evolved over time. Our priorities are listed on our website. You can go there, and you can you can review them. They're all designed to increase the volume of tests significantly and the access to test significantly, and that is primarily focused at diagnostic tests, in the home, point of care, and in the central labs. And we are most focused on those tests that are high volume tests in certainly safer point of care or home, no single point of care side or home site is going to do a significant volume. But in distributing that test in as many homes as possible and as many point of care sites possible in supporting those sites with significant production of the tests, you provide that possibility and that's what we are focusing our reviews on at this time. I did want to briefly mention the CDC lab alert that we have had multiple questions over multiple days and multiple forums. The CDC has announced that after December 31st they have requested the US Food and Drug Administration to withdraw the EUA for their original SARS CoV-2 test it was interested in getting used in February of 2020 for the detection of SARS CoV-2 only. The impact, and I'll go into this later I'll go into some of the questions, is it only on the CDC test and not on anyone else, and so only those who are currently receiving the CDC test and either directly through the CDC or through Bio Search or IDT, those are the only labs that will be impacted by this decision and so we would direct any other further questions to the CDC if you are impacted by this. If there's something that the FDA can do to alleviate access issues by alternative means we are all ears and you can send an email to the template email box. We also have a theme, the many questions around branding. So we do allow private labels for authorized tests, so this is an effort to expand access through the use of different sales channels and oftentimes those sales channels want their own brand for any EUA authorized test. That's a simple procedure to update that. The EUA authorization holder can simply request this and by submission to the templates email address, and we'll make this update and will post, the new brand name or additional brand name on the FDA website where we post all the authorizations. That's' in the drop down plus sign on the website. And this is an effort to provide complete transparency so because it may not be as evident that this new brand name or another brand name is an EUA authorized test, and so folks who want to know this can go to the FDA website, make sure that that brand is attached to that EUA authorization. So that's our desire to be totally transparent and clear and make this very clear about what tests are authorized, and perhaps which aren't so that purchasers of tests can be totally sure of what's authorized. Toby, do you have anything else to add to my opening remarks there before we go into the pre-submitted questions?

Toby Lowe (FDA IVD Assoc Director):
No, I don't think so. Not today. Thanks.


---

## 2021-08-04_Virtual Town Hall 65_section-titles.md

#### 1. FDA Updates on EUA Tests and Prioritization Policies


Anike Freeman (FDA)
Hello. I'm Anike Freeman of CDRH's Office of Communication and Education. Welcome to the FDA's 65th in a series of virtual town hall meetings to help answer technical questions about the development and validation of tests for SARS-CoV-2 during the public health emergency. Today, Toby Lowe, Associate Director of the Office of In Vitro Diagnostics and Radiological Health, and Dr. Kristian Roth, both from CDRH, will provide a brief update. Following opening remarks, we will open the line for your questions related to development and validation of tests for SARS-CoV-2. Please remember that, during this town hall, we are not able to respond to questions about specific submissions that might be under review. Now, I give you Toby.

Toby Lowe (FDA IVD Assoc Director):
Thank you. Thanks, everyone, for joining us again this week. I don't have much in the way of updates today. But I did want to point out, I think Tim mentioned last week, that we would be adding some information to the website on the EUA tables to clarify that you can expand each row for each EUA listing. And that's where you can find things like the granting letters and additional brand names. So that question, especially brand names, has come up quite a bit. So we wanted to make sure that was a little bit more clear on the website. And that feature or that addition to the text there went up late last week. I also want to reiterate one of the points that we made last week. We've got a lot of questions about the CDC announcement about withdrawing their EUA for their single analyte test. I just want to reiterate that that announcement from CDC and that decision by CDC does not impact any other tests. And it also does not impact FDA's review priorities. So we can move into the questions that we got. And the first couple are actually related to that same CDC announcement. So the first one is asking if we can clarify why CDC withdrew its EUA. And that is a CDC decision, so you would have to check in with the CDC to get their reasons behind their decision making. But as I said, it does not signal any policy changes for FDA. And then they go on to ask whether the withdrawal signals any change in prioritization policies and specifically asking whether FDA intends to prioritize multiplexed testing. And as I said, the announcement does not impact the EUA pathway for any other tests. It does not impact FDA's priorities. We've mentioned, on previous calls here, that multi-analyte tests that have sufficient manufacturing and testing capacity are included in our priorities and will continue to be prioritized. And that is not changing.

---

#### 3. Prioritization of Multi-Analyte Tests and Resubmission Considerations


Toby Lowe (FDA IVD Assoc Director):
The next question that we received is similar to previous questions that have been asked regarding whether the US is prioritizing multi-analyte tests and specifically asking whether we would permit a company that had a previous EUA for a respiratory panel deprioritized to resubmit the same EUA. And so to reiterate what we've previously said, multi-analyte tests that have sufficient manufacturing and testing capacity are included in our priorities and will continue to be prioritized. While we can't discuss specific submissions on this call as we've mentioned, we can generally share that if an EUA request was deprioritized previously, it was likely because the test either had low manufacturing or testing capacity or that the submission was deficient in some way. If such an EUA request was resubmitted and addressed any outstanding issues, then it would be considered and prioritized as appropriate based on the information in the EUA request.

---

#### 9. Clarifying EUA Approval Timelines for OTC Test Kits


Tianyang Liu:
Hi. Could you hear me?

Toby Lowe (FDA IVD Assoc Director):
Yes.

Tianyang Liu:
OK, thank you. So my question is that our company has submitted the EUA for our antigen home tester kit months ago. But we just took our feedback from FDA that said it gets started and at a very early stage. Although FDA claimed the OTC home used test kit is a priority, but it seems not going that fast. We are eager to get it approved, since we all see the Delta virus is currently spreading fast and more and more people are being infected. OTC tester kit can play a greater role against the Delta virus, because they can easily and rapidly detect the virus. Could you please let me know how much this priority bill for OTC study will speed up in the process? And how long we are supposed to wait? Is there any kind of rough estimation for those type of EUA approval? And what kind of resources does the FDA put on the priority to speed up the OTC product? Thank you.

Toby Lowe (FDA IVD Assoc Director):
Sure. So obviously, we can't speak to specific tests. And I don't know off-hand the specific situation with yours. If you do have concerns about your file, you can send an email to the Templates mailbox and ask that it be sent to me, and I can take a look at it. But generally, OTC and home use tests are a priority. We do have a large number of submissions in the house, and we are prioritizing those reviews as much as possible and moving through them as quickly as possible. In addition to prioritizing the home use tests, we also do look at the content of the submission. So it does make a difference if the submission is complete and followed the recommendations in the template and looks promising at first glance, if you will. And those aspects are all factored in when we have to prioritize reviews with so many submissions in-house.

Tianyang Liu:
Oh. I see, I see. Thank you, Megan. And is your average-- I mean, average days or months that you already OTC EUA has been approved? I know that right now, we have five OTC products approved by the FDA right now.

Toby Lowe (FDA IVD Assoc Director):
So sorry, I'm not sure I caught that question.

Tianyang Liu:
I mean, is there an average months or days that-­

Toby Lowe (FDA IVD Assoc Director):
Oh. No, I can't necessarily specify a specific timeline or an average. It really does depend on the submission, the quality of the submission. And if you follow the recommendations in the template, that definitely helps to speed things up.

Tianyang Liu:
OK. OK, thank you very much sir-- thank you very much, madam. And in this case, you said that we can send it to you. Is there an email address that we could refer to?

Toby Lowe (FDA IVD Assoc Director):
So if you send an email to the CDRH EUA Templates mailbox, it should be showing on the screen, and you can ask that it be sent to Toby to take a look and get back to you.

Tianyang Liu:
OK. Thank you very much.

Toby Lowe (FDA IVD Assoc Director):
No problem.

Anike Freeman (FDA)
OK. Our next question is from Michael D'Armiento.


---

## 2021-08-11_Virtual Town Hall 66_section-titles.md

#### 1. Expanding Access to High-Volume COVID-19 Diagnostic Testing


Elias Mallis (FDA):
Greetings, everyone, and thanks for joining us today. I'm Elias Mallis, director of the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. I'll be your moderator for today's program. Welcome to the CDRH Virtual Town Hall Meeting for developers of tests for SARS-CoV-2. This is meeting number 66 in our series during which we'll discuss and answer your questions about tests in the fight against COVID. Our panelists for today's program are Dr. Timothy Stenzel, director of the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality, and Toby Lowe, associate director also from OIR We'll start today's program with some opening remarks and updates from our panelists, and then we'll spend the rest of our time today answering your questions about the development and validation of COVID tests. Please note, we're not able to discuss specific submissions that are under review. To ask a question, please go to your name on the Zoom meeting and select the Raise Your Hand icon. Now let's turn the program over to Tim for some opening remarks and updates. Thank you, Tim.

Tim Stenzel (FDA IVD Director):
And thank you, Elias, and welcome again. 66, wow, that number keeps coming up and will continue to. And we already have a number of attendees, and thank you for joining us again. Again, our purpose here is to assist you in order to assist the nation's response to the ongoing pandemic. And obviously, testing needs to persist with the Delta surge in the US that continues to go up. The amount of testing is going up, and obviously, the positivity rate is pretty high compared to earlier this summer and is hovering nationally around 10% right now. And there are certain areas where it's-- currently numerous areas where it's much higher than that even. I just wanted to again go over some key current priorities. As I mentioned, the importance for testing is ongoing, and the demand's ongoing. And so it's very important. And our key focus is to do anything we can to significantly expand access to testing through a high-volume test to support high-volume testing. And so that is the best use of our public resources, public health resources, is to focus our attention on that. And we're trying to stimulate development of those kinds of tests. So tests, particularly I would say diagnostic tests, in high-volume central lab tests systems that can run through a ton of samples in a shift, and they're manufactured in high volume. And then point of care and home tests, so diagnostic tests that, by virtue of their higher distribution, being performed in a lot more sites than, say, a high complexity lab, tens of thousands of CLIA waived labs and hundreds of thousands actually of CLIA waived labs and obviously potentially tens or hundreds of millions of home sites. And so to supply those over 100,000 point of care labs and as many households there are in the United States, that does require a high manufacturing volume of point-of-care tests and in-home tests. So for those that want to know if they qualify and meet the high volume considerations, they can reach out to the FDA and ask if their technology will meet that. I also wanted to briefly cover the bar that the EUA provision allows her to use to make decisions on authorization decisions on tests, and these are primarily focused at SARS tests and diagnostic tests, and that bar is that the likely benefits outweigh the likely risks. As we move through the pandemic and as the virus mutates and new variants show up and others recede, this balance between likely benefit versus likely risk can alter. And so that is a fluid sort of bar that we apply going forward. It hasn't changed drastically, but it does enter into our thinking. It is the standard that we use for making authorization decisions. And of course, the target is SARS. That's what the EUA provisions are for. They aren't for other viruses, but we have-- obviously, the FDA has shown a good deal of flexibility to allow other viruses and panels to be submitted to the FDA. And those panels when produced in high volume are able to be tested in labs in high volume do remain a priority. All right, enough on priorities. We've covered all that before. Also, we have recently obviously switched to a new platform, the Zoom platform, and there are clear advantages to it. But in moving over to this platform, we have had a challenge of dealing with transcript generation. And the awesome team that we have here at the FDA has been working on that, and we are working as hard and quickly as we can to restore the previous timelines for posting transcripts after calls. And we do see a light at the end of the tunnel and hopefully in the relatively near future. So in the interim, we do ask for your patience until we get back to those previous timelines for transcript posting. With that, we can move into the phase of the call that we usually go to, which is we address the previously submitted questions, and for that, Toby, I will turn it over to you. Thank you.


---

## 2021-08-18_Virtual Town Hall 67_section-titles.md

#### 1. FDA Priorities for SARS-CoV-2 Test Development


Anike Freeman (FDA)
Good afternoon and thank you for joining us today. My name is Anike Freeman, a Senior Consumer Safety Officer in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. I'll be moderating today's program. I'd like to welcome you to our virtual town hall meeting for SARS-CoV-2 test developers. This is meeting number 67 in our series in which we'll discuss and answer your questions about diagnostic tests in the fight against COVID. Our panelists for today's program are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality, and Toby Lowe, Associate Director also from OIR. First, we will have opening remarks from our speakers. And then we'll begin answering your questions about the development and validation of COVID tests. To ask a question, please select the Raise Your Hand icon at the bottom of your screen. Please note we're not able to discuss specific submissions that are under review. Now, I'll hand the program over to Tim.

Tim Stenzel (FDA IVD Director):
Welcome, everyone. I believe this is the 67th CDRH virtual town hall meeting to assist all of you test developers in developing tests to meet current pandemic needs. And, just to reiterate, our priorities have not changed. We continue to prioritize access to high-volume testing nationwide, particularly for diagnostic tests, so point-of-care diagnostic tests, home diagnostic tests, high-volume central lab tests, and diagnostic home collection. So those are the priorities for, I presume, obvious reasons. And we continue those. One second because Toby wanted me to mention something, and I'm not finding that. Toby, do you want to make that statement? I'm not finding what you wanted.

Toby Lowe (FDA IVD Assoc Director):
Sure. Yeah, it's part of the discussion on priorities. I know we've had a lot of questions recently about multianalyte tests. So I just wanted to clarify that we are accepting and prioritizing prescription multianalyte tests, but not over-the-counter.

Tim Stenzel (FDA IVD Director):
Thank you, Toby. And, with that, I think we can move over to the few questions that we received ahead of the call. And over to you, Toby.

Toby Lowe (FDA IVD Assoc Director):
Great. Thanks, Tim. And welcome, everyone. So, __as I have mentioned on previous calls, we do sometimes receive questions that are too detailed or case specific to address on this call. For those, we do try to send a response in writing within a few days.__ So, if you've submitted a question and don't hear it addressed on the call today, please keep an eye out for a written response. And, if you don't receive one within a few days, please reach back out to the CDRH- EUA-Templates@fda.hhs.gov mailbox for an update. So we do have one question that we received ahead of time today that we'll address regarding an antigen test for SARS-CoV-2. And there are two related questions here. The first is asking about what review pathway FDA recommends, whether the EUA review pathway or the traditional, premarket review pathway. And, similar to what we've said on previous calls about both molecular and antigen tests, for tests that will most benefit the current public health needs, EUA does remain the fastest and least burdensome route to authorization. Sponsors interested in pursuing full marketing authorization through a de novo or a 510K are also welcomed to do so. And then the second part of this question is asking about what additional clinical performance requirements would be in place for traditional premarket review pathways, such as 510K or de novo, compared with an EUA request and, specifically, with respect to clinical performance data, asking whether both prospective and retrospective studies are required if the developer plans to use the traditional premarket review pathway. So, since we've not yet authorized an antigen SARS-CoV-2 test for full marketing yet, we would generally recommend a pre-submission. Typically, for full marketing authorization, we're likely to expect a higher-powered, prospective clinical study, so more positive than negative, than what we would expect to support an EUA, as well as analytical studies of course. And, while it is specific to molecular, the decision summary for the SARS-CoV-2 BioFire de novo, which is the only SARS-CoV-2 test that has received full marketing authorization at this time, might give some insight into FDA's thinking about what we're looking for full marketing authorization. And, with that, Tim, I can pass it back to you unless we have any hands raised for questions at this time.

Tim Stenzel (FDA IVD Director):
It doesn't-- if my dashboard is correct, we're not seeing any hands raised at the moment. Oh, there's one. Now they're coming in. So let's go ahead and look to that. Thank you.

Anike Freeman (FDA)
Alright, our first question will be from John Mann.


---

## 2021-08-25_Virtual Town Hall 68_section-titles.md

#### 1. SARS-CoV-2 Test Development and Validation Updates


Anike Freeman (FDA)
Hello, and thank you for joining us today. I'm Anike Freeman, a Senior Consumer Safety Officer in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. I'll be moderating today's program. I'd like to welcome you to our virtual town hall meeting for SARS-CoV-2 test developers. This is meeting number 68 in our series in which we'll discuss and answer your questions about diagnostic tests in the fight against COVID. Please note that, after today, we are switching to a biweekly format. The next town hall will take place on September 8. Our panelists for today's program are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality, and Dr. Kristian Roth, also from OIR. We will begin with opening remarks from our speakers and then we'll answer your questions about the COVID test development and validation process. To ask a question, please select the Raise Your Hand icon at the bottom of your screen. Please note we are not able to discuss specific submissions that are under review. Now, I will hand the program over to Tim.

Tim Stenzel (FDA IVD Director):
Thank you, and welcome everyone to another weekly webinar and virtual town meeting. And we will be moving to every other and see if that works. We always have the flexibility to go back to weekly if that's important. So, I had a few brief opening remarks. And then I'll move into the answering the questions that were submitted prior to the call, and then we'll go into live Q and A. First of all, our clear priorities for review are diagnostic tests that greatly expand access. These are very high volume central lab tests or point-of-care tests and home tests and home collection for diagnostic assays. There are some serology tests that are clear priorities. And they are fully quantitative serology tests that are traceable to the WHO international standard. This will really help us move forward and inform on whether or not there's a level of antibody that is able to provide complete immunity and/or protection. Neutralizing antibody tests are also a clear priority as well, although that may not always correlate with the development of some immunity or protection. So I also want to say that most of the questions today that were submitted ahead of the meeting have been answered, some of them even last week. But I do want to apologize for going over these topics again. But perhaps clearly, repetition may be needed. So apologies in advance. So with that, we'll move into those questions.

---

#### 4. FDA Plans for Transitioning COVID-19 Test EUAs


Tim Stenzel (FDA IVD Director):
Next question. Does the FDA plan to end the EUA pathway for any SARS-CoV-2 related test diagnostics, serology, et cetera, prior to the official end of the public health emergency? The short answer is no. If so, what would be the criteria for ending the EUA pathway? The FDA is actually not the one that would declare an end to the emergency. That's the brief answer. I'll go into a longer answer here shortly. Also, would tests previously granted EUA be allowed to remain on market if the EUA pathway is ended? And the answer is there is a short answer, is yes. Let me go into more detail on this. We have covered this before on this call, but we'll go over it again. While we can't comment on the timeline, we're working on a transition plan for devices offered under EUA. But we still are encouraging full authorization submissions to the FDA soon as you want. We are accepting Q-Subs, Pre-Subs for those. And we're accepting full authorization applications. For molecular, that mostly would be 510k submissions now, since we've already granted one submission. And then for serology and antigen, it would be-- the first one would be a de novo application. And then subsequent to that, most of the antigen and serology tests would be 510k submission. So the transition plan guidance is on the Center's, CDRH's FY '21 priority list. And additionally, revoked EUAs are in effect until the public health emergency is terminated. This does not typically happen for quite a while, and as can be seen from previous public health emergencies that still have not been terminated, like Zika and Ebola. So there are still non SARS-CoV-2 tests that are able to be sold and used under EUA authorities. We cannot anticipate when the public health emergency will end. However, the FDA is committed to helping ensure the public has access to a wide variety of test options for COVID. And we'll continue to review the EUAs to address public health needs.

---

#### 11. FDA Guidance on EUA to 510k Transitions


Tim Stenzel (FDA IVD Director):
Next question. For an EUA over-the-counter nonprescription COVID-19 rapid lateral flow assay with a serial testing claim that will eventually provide FDA with acceptable asymptomatic serial study data, is it a correct assumption that, for the transition from EUA to 510k, no new asymptomatic testing would be necessary for the 510k? Meaning that only the acceptable asymptomatic serial study data is required to support the asymptomatic claim. So currently, the serial testing program is only applicable to EUA tests. However, we will want to incorporate as much of the EUA data as is possible. And that's possible if the device does not change in any material way that can impact performance. So but as far as the minimum recommendations for the number of samples, et cetera, you'll want to validate that according to FDA recommendations. And you can go ahead and submit a Pre-Sub or a Q- Sub with your proposed studies on specific questions. So depending on the size of that asymptomatic study, it may or may not meet the expectations for full authorization. Second question from this person, for an at-home test by prescription multi-analyte COVID-19 and influenza EB lateral flow test intended for symptomatic individuals, presuming EUA authorization and eventual 510k clearance, is it correct that no testing of asymptomatic individuals would be required, either single or serial testing? If you're proposing a claim for a symptomatic population, which is the likely population, when you have a multi-analyte test other than SARS, we simply don't know what's going on with other viruses, respiratory viruses, in an asymptomatic population, you would not need to test asymptomatic individuals. Next question from this individual, in general, when the performance of an assay isn't expected to exceed 90% PPA or sensitivity, does a test developer need to include symptomatic and asymptomatic serial testing in a clinical study to support 510k clearance for COVID-19 rapid lateral flow assay for over the counter? So again, depending on what claims you want to make, we recommend you submit a Pre-Sub to get more information. And the final question from this person notes that in an August 12 article, in Agency IQ by Laura DiAngelo on the FDA transition from QSR to ISO 13485, that there are questions about the impact on EUA authorizations. So yes, we are in the process of converting from QSR to ISO 13485. However, and we can't comment on the timeline for a transition plan. But again, we do not see an end anywhere in the near future to the EUA pathway for review of critical assays by the FDA.

---

#### 20. Transition from EUA to Full 820 Compliance


Laura D'Angelo:
Hi there. I would like to follow up on myself on the 820 question. I think the last time we talked about 820 at these town halls was in February, when the plan was the transition guidance will address kind of the things that were waved out under EUA and the transition into a fully compliant 820 system. And then forward looking, and the answer might just literally be we can't comment on the timeline. But my question was, if we're transitioning from EUA with some parts waived out in 820, to full 820, is there going to be another plan for? Or is this just we'll take as it comes for the transition to ISO, which I know is kind of in the hopper?

Tim Stenzel (FDA IVD Director):
So I don't I don't see any immediate change to how we have EUA and how we have full authorization in the near future. We are accepting Q-Subs and Pre-Subs for full authorization. We are reviewing those. We are getting back to folks as soon as possible. And all our areas antigen, molecular, and serology have ideas. Of course, molecular, we've already done it. So we have very clear recommendations. We are going to work on templates, updates on what those full authorization recommendations are. I am recommending that, those that want to stay on the market long term, that they do start working on their full authorizations and submit Pre-Subs for us to review if needed. I mean, you can look at things in the molecular. You can look at what we've already reauthorized. You may not have any questions, and you can just go forward. And so I really can't comment on the guidance. That's really not within my control anymore. It's going through the process to be able to be made public. That document will not specify for IVDs the recommendations for conversions in all likelihood. It'll just be outlying things like timelines and general high level expectations. But our plan is to update the templates with specific recommendations for those.

Laura D'Angelo:
OK. Very cool. Thank you.

Anike Freeman (FDA)
All right. I think we have time for one more?

Tim Stenzel (FDA IVD Director):
We have time for one more.

Anike Freeman (FDA)
Yep. And that will be from Diane B.


---

## 2021-09-08_Virtual Town Hall 69_section-titles.md

#### 1. COVID-19 Test Development and Authorization Guidelines Presentation


Joseph Tartal (FDA):
Hello, and thank you for joining us today. I'm Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. I'll be moderating today's program. Welcome to another virtual town hall meeting for SARS-CoV-2 test developers. This is meeting number 69 in our continuing series in which we'll discuss and answer your questions about diagnostic tests in the fight against COVID. Please note that we have switched to a biweekly schedule. The next town hall will take place on Wednesday September 22nd. Our panelists for today's program are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality. And Dr. Kristian Roth, also from OIR. We'll begin with opening remarks from our panelists and then we'll answer your emailed questions about COVID test development and validation and finally open the line to live questions. To ask your questions, please select the Raise Hand icon at the bottom of your screen. When you're called on, please identify yourself and ask your question promptly. Also, please note, we are not able to discuss specific submissions that are under review. Now I'll hand over the program to Tim.

Tim Stenzel (FDA IVD Director):
Well thank you and welcome again to this week's edition of the town hall. We note, unfortunately, that COVID infections are very prevalent in the US today as they are in many parts of the world. I do want to remind those that have been inquiring through perhaps the pre-EUA process about OUS, or outside the US, studies for SARS, since there are plenty of patients, positive patients in the US, and as I've said before-- we said before that we really want you to start your studies in the US where possible and especially for point of care and home diagnostic tests. And that only if you run into hurdles about getting enough positive patients you reach out to us and find ways that you can perhaps go outside the US. Regarding panel tests which we'll talk about a little bit more later, in the US right now there's hardly any flu circulating. And there may be parts of the world where there's more flu and obviously for panel tests, it may be easier in some cases to get positives outside the US, so that's still one caveat. I do want to re-review the priorities which remain intact and they're primarily for diagnostic tests that are high volume central lab tests as well as point of care in home. For serology, the highest priority tests are quantitative tests that are traceable to the international WHO standard as well as neutralizing antibody serology tests. As we move forward, particularly for the antigen submissions, we are moving towards-- we've noted that in many cases, the relative priorities of antigen submissions, at this time at least, is relatively equivalent. So we are moving, and I've directed the team to move, to making sure that first in for these tests that are in this category of being roughly equivalent, that generally we will review them on a first come, first serve basis, a first in, would likely get-- we endeavor to get comments back or other feedback back or potentially authorizations first. I also want to go back to panels and I think there are some questions that we received ahead of the call about panels but in particular antigen panels. So we've gotten a number of inquiries about non-SARS viruses and how to get them such as flu A B which is not circulating very much in the US, which is a good thing for patients but challenge for developers. For antigen tests in particular and for all home diagnostic assays, we do recommend fresh samples. Banked or even contrived samples for non-SARS viruses are going to be-- are not something that we recommend. There are, at least in the point of care in central lab, there are a number of flu AB or RSV assays that are fully authorized that can be used to assess patients for them. So if you are developing a panel assay where it's challenging because, especially for antigen, we're going to recommend that you have fresh samples. We recommend that you consider a ways of getting your SARS analytes authorized and somehow blocking the signal or not identifying the signal for any other analytes you might have on that panel for which you don't have available fresh samples to validate the assay. And, let's see, more into that a little bit later. One other item we wish to note is that for kit developers that are implementing changes to their EUA authorized devices, when you implement a change prior to EUA authorization of that change, that's only going to be relevant to high complexity labs. So other labs or home situations, whether that be moderately complex or point of care or home, are not going to be able to be implemented prior to authorization. So reading from the COVID test policy guidance as well as FAQs, "Unless and until an EUA is issued that authorizes additional testing environments for a specific test under CLIA, use of that test is limited to laboratories certified to perform high complexity testing and including testing at the point of care when the site is covered by the laboratory's CLIA certificate for high complexity testing." End quote. So again, for implementation of modifications, those can be implemented prior to EUA authorization in a high complexity environment. And with that, I think we have covered the introductory remarks and we'll go to the questions that we received prior to the call and have prepared answers. And Kris and I will tag team.


---

## 2021-09-22_Virtual Town Hall 70_section-titles.md

#### 1. Updates on SARS-CoV-2 Testing and EUA Reviews


Joseph Tartal (FDA):
Hello, and thank you for joining us today. I'm Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. And I'll be moderating today's program. Welcome to Virtual IVD Town Hall Number 70 for SARS-CoV-2 test developers in which we'll discuss and answer your questions about diagnostic tests in the fight against COVID. The next IVD Town Hall will take place on Wednesday, October 6. Our panelists for today's program are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality, and Toby Lowe, also from OIR. We will begin with opening remarks from our speakers, and then we'll answer your previously emailed questions about COVID test development and validation. And then, finally, we'll open the line to your live questions. To ask a live question, please select the Raise Your Hand icon at the bottom of your screen when it is time. When you're called on, please identify yourself and ask your question promptly. Also, please note, we are not able to discuss specific submissions that are under review. Now, I'll hand the program over to Tim.

Tim Stenzel (FDA IVD Director):
Thank you, and welcome all to this virtual town hall. We endeavor to help developers get EUA authorization as quickly as possible. That's what we do pretty much 24/7 these days and have done since January 2020. A couple of quick updates, and then go into the pre-submitted questions. The first update is - those who are customers of Abbot Molecular Alinity tests for SARS-CoV-2, there is a SARS only in a panel. You would have received a letter from the company talking about a false positive issue. Also, the FDA did make a communication about this. So there was a design issue with the Abbot Alinity m that resulted in confirmed false positive. Don't know the exact rate. So we do recommend that the prior two weeks of cases, that you look and see if you were to retest those positives to confirm the positive with another SARS-CoV-2 molecular test. The company thinks they understand the cause. The company thinks they have a fix. The FDA is currently reviewing that fix to see if it indeed works. In the meantime, the firm can launch that update into high complexity labs only, if those labs wish to have that update, while the FDA reviews the update and prior to EUA authorization. When the FDA updates the EUA authorization with a fix or a mitigation that can be extended to all labs, including moderate and complex labs, then we will do so, and the firm can go ahead and update the software in all those labs too. The second update has to do with EUA submissions for antigen tests. As we stated, it's a high priority for us to review these submissions, particularly point-of-care and home tests. We have added more personnel from other EUA review areas onto the antigen team. And we are making a concerted effort to reduce the turnaround time for those submissions. Some developers have started getting feedback. And we plan to get through all the current submissions as rapidly as possible. And we hope this becomes evident over the days and weeks ahead. With that, I'm going to move into the pre-submitted questions.

---

#### 8. Clarification on Confirmed Positives and FDA Communication Response Time


Julio Herrera:
Yes, can you hear me?

Joseph Tartal (FDA):
Yes.

Julio Herrera:
All right, so I submitted this via email. And I guess it got missed or maybe it's for next week. So we're working on an at-home collection for serology assays. And so we're doing the clinical agreement section, which is the 30 unvaccinated and the 30 vaccinated confirmed infections. My question is actually twofold. One is, for confirming positives, can we use an FDA EUA antigen or rapid test, such as the BinaxNOW, as a positive confirmatory test to basically include that as our positives? The second question is related, but we've also had a number of individuals that we've collected that were vaccinated individuals and let's say are four to six months past their last dose of the vaccine that basically are now sending us a confirmatory positive result. Would those individuals be eligible as confirmed positives for this clinical agreement or for the usability?

Tim Stenzel (FDA IVD Director):
So I neglected to read a disclaimer at the beginning of the question that we went over that were received prior to the call. And this is true for every week. So we do receive some questions that are a little too detailed or test- or case-specific that we will not address on the call. And so I forgot to do that. So that was the case for your question. So I do recommend that you reach out to FDA staff through the CDRH EUA Templates email address. Or if you already have a reviewer assigned, to reach out to them to engage them in this conversation. I'm not going to be able to go over that question today.

Julio Herrera:
OK, all right. How long does it take them to respond? Because I sent in a question to them through that site several weeks ago and I haven't heard back from them yet.

Tim Stenzel (FDA IVD Director):
If it's been more than a couple of weeks, you can go ahead and send an another email to the Templates email address and ask them, in this case, to contact Toby.

Julio Herrera:
All right, all right, thank you.

Joseph Tartal (FDA):
Thank you. We'll go on to our next question. Tianyang Liu. I'm opening up your microphone so that you can unmute and ask your question.


---

## 2021-10-06_Virtual Town Hall 71_section-titles.md

#### 1. COVID-19 Test Updates and EUA Prioritization Changes


Joseph Tartal (FDA):
Hello, and thank you for joining us today. I'm Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education, and I'll be moderating today's program. Welcome the virtual IVD Town Hall Number 71 for SARS-CoV-2 test developers, in which we'll discuss and answer your questions about diagnostic tests in the fight against COVID. The next IVD Town Hall will take place on Wednesday, October 20. Today's presentation and transcript will be made available at CDRH Learn under the subsection title, Coronavirus COVID-19 Test Development and Validation Virtual Town Hall Series. Please note, the August recordings and transcripts are now available, and we're currently working towards making the September transcripts and recordings available as soon as possible. Our panelists for today's program are Toby Lowe, associate director for regulatory programs in the Office of In Vitro Diagnostics and Radiological Health or OIR, and CDRH's Office of Product Evaluation and Quality, and Dr. Kristian Roth, also from OIR. We'll begin with opening remarks from our speakers. And then we'll answer your previously emailed submitted questions about COVID test development and validation. And then finally, we'll open the line up your live questions. To ask a live questions, please select the Raise Hand icon at the bottom of your screen when we get to that part of the program. When you're called on, please identify yourself and ask your question promptly. Also please note we're not able to discuss specific submissions that are currently under review. With that, I will hand the program over now to Toby. Welcome, Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe, and thanks, everyone, for joining us again this week. We do have several updates to share and then we'll get into the questions, as Joe said. So first you may have noticed that yesterday we updated one of our FAQs. It's the FAQ related to-- sorry I think this was Monday, actually, not yesterday-- but the FAQ related to how we prioritize review. That was updated to indicate that for at-home tests and home collection tests, we are prioritizing diagnostic testing there. So we are not prioritizing home tests or home collection for serology or antibody tests at this time. We will continue to evaluate the priority there for those types of tests. And corresponding to that FAQ update, we removed the serology home collection EUA template, from the website, just to avoid any confusion there. So then this morning, we updated all of the remaining templates on our website. We added a cover sheet template for molecular diagnostic EUAs, EUA requests. And we updated all of the remaining molecular antigen and serology templates. You will see a lot of changes if you were to do a red line compare, if you've saved an old version. But these were primarily updates to bring these current, provide clarifications, add information in areas where we've had a lot of questions to help streamline the process. There were no major policy changes in these updates. The performance recommendations primarily remained the same. But some of these hadn't been updated in several months, and we wanted to make sure that they included all of the most current information. So those can be found in the same place on the website. The next update we have is that on September 23, so just after our last town hall, we issued an EUA revision that applied to most previously authorized molecular, antigen and serology tests for COVID-19 to add conditions of authorization regarding viral mutations. So this revision was intended to bring all of the EUAs up to where we currently are since we've started adding conditions of authorization related to viral mutations in recent months to new authorizations. So it adds conditions related to monitoring of emerging viral mutations and their potential impact on the performance of authorized SARS-CoV-2 tests. And it also requires developers to update their test labeling regarding the impact of potential viral mutations. So the next update is earlier this week on Monday, we authorized the Acon Laboratories Flowflex COVID-19 home test, which is an over-the-counter antigen test. It can be used for both symptomatic and asymptomatic without the need for serial testing. And we announced in the press statement that the company is expecting significant manufacturing capacity, so we expect that this authorization should double rapid at-home testing capacity in the US over the next several weeks. And then yesterday, we issued a safety communication related to a recall that Ellume put out for the Ellume COVID-19 home test. There was a recently identified manufacturing issue that led to a potential for false positive results with certain lots of the Ellume home test. So Ellume issued a recall on Friday, and we put out the related safety communication yesterday. So all of those can be found on our website as well. And hopefully, those updates will be helpful to folks. So now we can go into the prepared Q&As, the ones that we've received ahead of time. As usual, we will caveat this that we sometimes receive questions that are a little too detailed or case-specific, so we won't address those on the call, and we'll try to address those in writing. And if you have additional questions or don't receive an answer to your question, please feel free to reach back out to the CDRH- EUA-templates@fda.hhs.gov mailbox for an update. And as we get into the questions, I will ask Kris to take the first one.


---

## 2021-10-21_Virtual Town Hall 72_section-titles.md

#### 1. Updates on COVID Test Development and Prioritization Strategies


Joseph Tartal (FDA):
Hello, and thank you for joining us today. I'm Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. And I'll be moderating today's program. Welcome to virtual IVD Town Hall Number 72 for SARS COVID test developers, in which we'll discuss and answer your questions about diagnostic tests and the fight against COVID. The next IVD town hall will take place next month on Wednesday, November 17th. Today's presentation transcript will be made available at CDRH Learn under the subsection titled, Coronavirus COVID-19 Test Development and Validation Virtual Town Hall Series. Please note that all the recordings and transcripts to date are now available. Our panelists for today's program are Toby Lowe, Associate Director for Regulatory Programs in the Office of In Vitro Diagnostics and Radiological Health or OIR, and CRH's Office of Product Evaluation and Quality, and Dr. Kristian Roth, also from OIR. We'll begin with opening remarks from our speakers. And then we'll answer your previously emailed questions about COVID test development and validation. And then finally, we'll open the lines up to your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your screen. Please wait until we get to that time to raise your hand. When you're called on, please identify yourself and ask your question promptly. Also please note we are not able to discuss any specific submissions that are under review. Now I'll hand the program over to Toby. Welcome, Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. And thanks, everyone, for joining us again this week. We have just a little bit of in the way of updates. And then we'll do our prepared questions that we received ahead of time, and then jump into the live questions. So I believe at the last Town Hall, we mentioned the letter to health care providers about the Abbott Alinity potential for false positive results. We have since issued, or classified rather, the Abbott recall for that issue. And also, we clarified in the letter to health care providers and the recall notice, that the recall is to update the software. The actual test kits do not need to be returned. And they can continue to be used with the updated software. We also discussed last time, the updates that we made to our FAQ about priorities. I just want to reiterate that for anyone who may have missed it last time. We have updated our FAQ about priorities to be clear that we are prioritizing at home and home collection tests for diagnostic tests-- so molecular and antigen-- and not for serology tests. So with that, we've also removed the corresponding template from our website so that there's no confusion there. And we are generally declining to review EUA requests for home collection and at- home serology tests for the time being. If that changes in the future, if we determine that there's a public health priority to review those, we will announce that accordingly. So we also, last week, announced that we had updated all of the templates available on our website. So those are obviously still there. And we will continue to update those as we have new recommendations to share. And along the update with prioritizing at-home and home collection tests, we are, as we've discussed in the past, we really are focusing on increasing availability for over-the-counter rapid at- home tests. And we will continue to update recommendations to help facilitate additional availability. So please keep an eye on the templates. Because that's where we'll be updating those recommendations.


---

## 2021-12-01_Virtual Town Hall 74_section-titles.md

#### 1. COVID-19 Test Guidance Amid Omicron Variant Concerns


Joseph Tartal (FDA):
Hello, and thank you for joining us today. I am Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. And I'll be moderating today's program. Welcome to Virtual In Vitro Diagnostic IVD Town Hall Number 74 for SARS-CoV-2 test developers in which we'll discuss and answer your questions about diagnostic tests in response to COVID-19. Today's presentation and transcript will be made available at CDRH Learn under the subsection title Coronavirus COVID-19 Test Development and Validation Virtual Town Hall Series. Please note we are working to post the recording and transcript from the last town hall that was held on November 17th. We're hoping to post that by next week. The next and last IVD town hall for calendar year 2021 will take place in two weeks on Wednesday, December 15th. The next and last IVD Town Hall for calendar year 2021 will take place in two weeks. Our panelists for today's program are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, or OIR in CDRH's Office of Product Evaluation and Quality, Toby Lowe, Associate Director for Regulatory Programs in OIR, and Dr. Kristian Roth, Deputy Director of the Division of Microbiology Devices, also in OIR. We'll begin with opening remarks from our panelists, and then we'll answer your previously emailed questions about COVID test development and validation. Please note we received some questions that are a little too detailed or test case specific that we will not address on the call. For those questions, we'll try to send our response in writing within a few days. If you submitted a question and do not hear it addressed, please look for a written response. If you do not receive one within a few days, please feel free to reach back out to CDRH-EUA- Templates@fda.hhs.gov and send it to that mailbox for an update. Last, then we'll open up to live questions. Please note that we are only doing live questions by phone. So please do not type anything into a Q&A box. With that, I will now hand this over to Tim for opening remarks. Welcome, Tim.

Tim Stenzel (FDA IVD Director):
Thank you, Joe, and welcome everyone. Of course, the big news for this week is going to center around omicron. The FDA and other agencies within the federal government and state, local, and public health labs are very busy assessing the situation and putting plans in place to screen for omicron in the US. And just the general statement, we have done our typical bioinformatics search of all EUA authorized tests, and we have no certainty now that any test is negatively impacted by mutations seen in Omicron. However, we have a fair amount of work to do to definitively say at the end of the day that there is no impact. We have already sent notifications out to key developers where we would specifically like them to assess performance for omicron. And we also note that all test developers are expected to do to their own evaluation for variant performance issues. Because there is so much concern about omicron, we certainly want you to go ahead and do your assessment. And if you haven't been contacted by an email, it means that we think that the risk is relatively low. However, if for your particular test, however, if you do discover something, please let us know as soon as possible, and we'll work with you on that. One of the easiest methods to screen for omicron is through the so-called S-gene dropout. The best known widest utilized assay out there is probably the Thermo Fisher TaqPath combo assay. As we saw with alpha and have posted on our website already, that assay is able to detect the deletion 69 70 through the dropout of S, but the other signals are positive. So these are the best samples to send for sequencing to determine whether or not that sample is coming from a patient infected with the omicron variant. And at this moment it's public health monitoring only. We know of no definitive decrease in vaccine or therapeutic efficacy. Obviously, separate efforts are going on for that. So we are encouraging all labs that can use a test that has the S-gene dropout signal when they can to test with that now until we get a good handle on omicron. At least there are over 20 tests that are able to detect the S-gene dropout. All of them have the S-gene design that Thermo Fisher has. We are working on updating our FDA website with this information. Also look to the website for any updates on any tests that may see a decrease in sensitivity for omicron. And we will update that web page on an ongoing basis. So check back when you can. In all likelihood, we will do some sort of communication on that web page when it's first updated with omicron. Let's see. Yeah, I think that's what I wanted to introduce and to get us kicked off here today. And then I'm going to turn it now over to Toby who's going to go through the questions we received ahead of time along with the answers. Thank you.


---

## 2021-12-15_Virtual Town Hall 75_section-titles.md

#### 6. FDA Guidance on EUA Amendments and Live Questions


Joseph Tartal (FDA):
OK. Great answer. And we'll move on to our last emailed-in question. Does FDA's current priorities extend to amendments and revisions for already existing EUAs?

Toby Lowe (FDA IVD Assoc Director):
So we do consider each submission, including amendments or supplemental EUA requests independently when determining the priority for review. So we consider whether the submission at that time is within FDA's priorities that are described in the test guidance, the test policy guidance.

Joseph Tartal (FDA):
OK. So that is the end of our emailed questions. And please remember, as we noted earlier, if we did not answer your question on the call, it's likely because there was a lot of detail, or it was test or case specific. And we will be sending out an email response to you. So please keep a lookout for that email response. And now we'll move on and take your live questions. So to ask a live question, please select the “Raise Hand” icon at the bottom of the screen. When you are called on, please identify yourself and ask your question promptly. Also, please note we're not able to discuss specific submissions that are currently under review. So we have a few people already with their hands raised. So I'm going to start with the top. So Bridget, I'm going to unmute you. Please unmute yourself and ask your question.


---

## 2022-01-26_Virtual Town Hall 77_section-titles.md

#### 1. FDA Updates on COVID-19 Test Development Guidance


Joseph Tartal (FDA):
So hello, and thank you for joining us today. I'm Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication Education, and I'll be moderating today's program. Welcome to Virtual IVD Town Hall Number 77 for SARS-CoV-2 test developers in which we'll discuss and answer your questions about diagnostic tests in response to COVID-19. Today's presentation and transcript will be made available at CDRH Learn under the subsection titled Coronavirus COVID-19 Test Development and Validation Virtual Town Hall Series. Please note we are working to post the recording and transcript from the last Town Hall that was held on January 12. We hope to post it soon. The next scheduled IVD Town Hall will take place Wednesday, February 9, 2022. Our panelists for today's program are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality; Toby Lowe, Associate Director for Regulatory Programs in OIR; and Dr. Kristian Roth, also in OIR as the Deputy Director of the Division of Microbiological Devices. With that, we will begin with open remarks from our panelists, and then we'll answer your previously emailed questions about COVID test development and validation. Please note, we received some questions that are too detailed or test case specific that we will not address on the call. For those questions, we'll try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed, please look for the written response. If you do not receive one within a few days, please feel free to reach back out to CDRH-EUA- Templates@fda.hhs.gov for an update. Last, we'll open up the live lines for your questions. So with that, I will now hand over the program to Toby for opening remarks. Welcome, Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. Thanks, everyone, for joining us again this week. So, I do have a handful of updates, and then we'll get into the questions. So, following the last Town Hall, we became aware that there was some confusion over the discussion about distributors. Generally, we recommend that all EUA holders refer to their conditions of authorization in their letter of authorization to determine what needs to be sent to FDA and in which cases they need concurrence from FDA prior to implementation. In general, the conditions of authorization typically state that an EUA holder must tell the FDA of any new distributors and must have concurrence from FDA prior to implementation of any updated labeling, including any new brand names. So, the concurrence is generally only if there is updated labeling. If you are adding a new distributor without changing any labeling, we will generally acknowledge receipt, but you do not need to wait for concurrence. And that is, again, dependent on what is in your letter of authorization, but that is the typical situation for most EUAs. And then we do also continue to receive questions about plans for submission of a 510k for molecular SARS-CoV-2 tests. We've generally recommended that developers submit a presubmission to discuss their approach, and we've stated that previously on this call many times. At this point, we are able to provide feedback more rapidly. So we welcome any developers that are considering a 510k for a molecular SARS-CoV-2 test to send an email to the EUA mailbox requesting feedback regarding submission of a 510k. And for those developers that have already submitted a presubmission, you don't need to do anything differently. We will get that feedback to you through your presubmission. A couple more updates on previous actions. On the 19th, just last week, we issued an EUA for the MaximBio ClearDetect COVID-19 Antigen Home Test. That's another over-the-counter rapid test that went through the ITAP program. And then on Friday of last week, we also updated the IVD EUA Molecular and Antigen web pages to add information about whether each authorized assay is a single or multiple target test. And this is intended to better inform potential users which tests are more susceptible to changes in performance due to viral mutations. We also added a new FAQ to the Test FAQ page regarding the inclusion of multiple targets to protect against performance impacts from future mutations. And then on Saturday the 22nd, we added an FAQ and put out some social media regarding the use of tests that are shipped and left outside in freezing temperatures. And the last update, last month in December, FDA issued a draft guidance titled "The Transition Plan for Medical Devices Issued EUAs During the COVID-19 Public Health Emergency." That is a draft guidance that was issued for comment, not for implementation. And we have received some questions regarding how specific situations would be handled under that guidance. Since that guidance has been issued in draft for comment and not for implementation, if there are points about the guidance that are unclear, we recommend that you submit a comment to the docket indicating areas that could benefit from added clarity. And if you have a question about how to manage your current plans for moving forward now with your emergency use test or with a 510k, we recommend that you send an email to the EUA Templates mailbox with sufficient details so that we can provide appropriate feedback for your particular situation. And with that, we can move into the questions that we received by email.

---

#### 8. FDA Guidance on Multi-Analyte Test Emergency Use Authorizations


Joseph Tartal (FDA):
OK, thank you for that information. And we're getting now to our last email question that came in. Please keep those coming for the next and future town halls. So the last question is, is FDA still considering emergency use authorizations for multi-analyte over-the-counter tests?

Toby Lowe (FDA IVD Assoc Director):
Yes, the FDA continues to recommend that developers interested in pursuing an EUA for an over-the-counter multi-analyte test to submit a pre-EUA to further discuss your proposal.

Joseph Tartal (FDA):
OK, thank you very much, Toby. And with that, we are now going to transition to the live questions. So now let's take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your screen. When you are called on, please identify yourself and ask your question promptly. Also, please note we are not able to discuss specific submissions under review. Again, for those type of questions, please email the EUA Templates mailbox. So with that, we're going to get to our first question. MHK, I'm unmuting you. Please unmute yourself and ask your question.


---

## 2022-02-09_Virtual Town Hall 78_section-titles.md

#### 7. Delays in EUA Amendment Review Process


Richard Montagna:
Thank you for taking the call. This is Richard Montagna from Rheonix. I know that the FDA is not able to respond to specific questions about a specific submission, so I'll try to frame this in a very general way. We submitted an amendment to our PCR EUA back in September. It was intended to validate the assay as a moderate complexity rather than the originally authorized high complexity. We were notified that it was in the triage, it would be evaluated, but for the past five months, we've got nothing but the biweekly updates. I'm wondering, is this what we should expect, or is it possible it's fallen through the cracks? Because it's also impacting another amendment we want to send in that will reduce the time of the assay. And we don't know whether we should run that with the software that would be used for high complexity or whether we should run it with the moderate complexity, because we don't know where we stand on that. I guess the question is, is it possible that it fell through the cracks, or is this what we should expect? So thanks for any guidance.

Tim Stenzel (FDA IVD Director):
Sorry for that experience. If you just follow up later today with an email to our templates email inbox and relay this information and ask for Tim and Toby to be copied, I'll go ahead and figure out what's going on and get a response back to you.

Richard Montagna:
OK, thank you very much. I really appreciate it.

Joseph Tartal (FDA):
OK, thank you our next question, Karl. Karl, I'm unmuting you. Please unmute yourself and ask your question.


---

## 2022-02-23_Virtual Town Hall 79_section-titles.md

#### 1. COVID-19 IVD Town Hall Updates and FAQs


Joseph Tartal (FDA):
Hello and thank you for joining us today. I am Joseph Tartal, Deputy Director in the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. And I'll be moderating today's program. Welcome to Virtual IVD Town Hall Number 79 for SARS-CoV-2 test developers in which we'll discuss and answer your questions about diagnostic tests in response to COVID-19. Today's presentation and transcript will be made available at CDRH Learn under the subsection title Coronavirus COVID-19 Test Development and Validation Virtual Town Hall Series. The January 26 and February 9 town hall recordings and transcripts are posted. The next scheduled IVD town hall will take place on Wednesday, Our panelists for today's program are Toby Lowe, Associate Director for Regulatory Programs in the Office of In Vitro Diagnostics and Radiological Health, or OIR, in CDRH's Office of Product Evaluation and Quality, and Dr. Kristian Roth, Deputy Director of the Division of Microbiology Devices also in OIR. We'll begin today's program with opening remarks from our panelists. And they'll provide updates and answer your previously emailed questions about COVID test development and validation. Please note we received some email questions that are too detailed or test case-specific that we will not address on the call. For those questions, we'll try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed, please look for a written response. If you do not receive one within a few days, please feel free to reach back out to CDRH-EUA-Templates@fda.hhs.gov mailbox for an update. And then last, we'll open with your live questions. So now I'll hand over to the program to Toby for opening remarks and updates. Welcome, Toby.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. Thanks everyone for joining us again this week. So we only have one update today and that is that yesterday we posted a new web page that lists the over the counter, at-home COVID-19 diagnostic tests. We had had quite a few requests for a more consumer-friendly, user-friendly version of that list since the EUA tables include quite a bit more information and much more technical information. So we did just get this out yesterday with a more consumer-facing page there for the home tests. And then beyond that, we can jump right into the questions that we received ahead of time.

---

#### 7. Regulatory Requirements for Legally Marketed Nasal Swabs


Joseph Tartal (FDA):
Thank you, Toby. And this is our last email question of the town hall. Can we use nasal swabs that are not listed in the 510k premarket notification database? And how do we ensure that swabs are legally marketed even if sourced from a third party, such as a distributor?

Toby Lowe (FDA IVD Assoc Director):
Yeah, so swabs typically are 510k-exempt devices, which means that they don't generally require premarket review. So they're considered to be legally marketed if they comply with other regulatory requirements, including registration and listing. So the FDA registration and listing database includes all device manufacturers and devices that are registered and listed. And so you can search that database for the specific swab manufacturer and specific swabs that you're looking at. So typically, swabs that are used for upper respiratory collection should be sterile. And so the requirements for the sterile swabs do include manufacturing under 21 CFR 820, which is the quality system regulation for medical devices. And then there are some swabs including those that are provided with viral transport media that are not exempt from premarket review. And so those swabs will be listed in the 510k database once they're cleared. And in terms of purchasing from third parties and distributors, that is certainly acceptable. Swabs can be purchased from third parties or distributors as long as they are also following the pertinent regulations that apply to them. And for any medical device including swabs, the outer packaging must include information that's noted in the labeling regulations. This would include the manufacturer and product name along with other information that's noted in that regulation. And then as I mentioned before, you can look in the registration and listing database to make sure that swab is listed there. And if it's not listed in the registration and listing database, then it may not be a legally marketed swab. And you should consider switching to one to a swab that is legally marketed to acquire a patient sample since you should be using sterile and appropriately marketed swabs for collection of patient samples.

Joseph Tartal (FDA):
Thank you, Toby. And that's the last of our emailed questions. So next, we're going to get to the live portion. So now let's take some live questions from you. Remember, to ask a live question, please select the Raise Hand icon at the bottom of your screen. When you're called on, please identify yourself and ask your question promptly. Also, please note just like with the emailed questions we're not able to discuss specific submissions that are under review. So there may be times where we'll ask you to email that question to the templates mailbox because it's a very specific type of question. With that, we're going to take our first live question of the day. So Thomas, please unmute yourself and ask your question.

---

#### 9. FDA Prioritization for COVID-19 Test Submissions


Veronica Colinayo:
Hi, this is Veronica Colinayo from Beckman Coulter. Yesterday at the webinar for the COVID-19 transition policy for devices, there was mention of possible review prioritization of de novo or 510k submissions. I'd like to understand if FDA will be reviewing all serology submissions, including those for qualitative or semi-quantitative assays. Or will they be practicing similar prioritization that's currently being implemented for EUA?

Toby Lowe (FDA IVD Assoc Director):
Thanks for that question. The transition guidances that were put out and that were discussed in the webinar yesterday were put out for comment. And so we do recommend that if there are points that are unclear there that you submit comments to the docket. And we can't really comment fully on what will or will not be done at that stage since that guidance is out in draft for comments and not for implementation. So the prioritization that we've laid out in our current COVID test policy guidance still holds for our EUA requests. And that does provide our current thinking about the priorities that are important for the current public health needs. So that is something that would be considered as time goes on. Right now we have specified that quantitative is where we're prioritizing given the WHO standard that's available. And so we will continue to consider what those priorities should be.

Veronica Colinayo:
Thank you.

Joseph Tartal (FDA):
Thank you. Our next question is Karl. Karl, I'm going to unmute you. Please unmute yourself and ask your question.


---

## 2022-03-09_Virtual Town Hall 80_section-titles.md

#### 2. FDA Warns Against Unauthorized COVID-19 Diagnostic Tests


Kris Roth (FDA):
OK great. Thank you Tim. I just want to highlight a couple of safety communications that recently that came out on March 1st. So these safety communications are CDRH warning folks not to use these tests, which have the same or similar names as FDA authorized tests. I think the first we want to discuss is the Celltrion DiaTrust COVID-19 test. We are warning people not to use certain Celltrion USA, Inc. DiaTrust COVID-19 Ag rapid tests. People should not use this particular Celltrion test if it is in a green and white packaging. The second test is the SD Biosensor Standard Q COVID-19 Ag home test. We are warning people not to use the SD Biosensor Standard Q COVID-19 Ag home test. This test is packaged in a white and magenta box and has not been authorized, cleared, or approved by the FDA for the distribution or use in the United States. And the last one is a test from ACON Laboratories. We are warning people should not use the ACON Laboratories test named FlowFlex SARS-CoV-2 Antigen Rapid Test in parentheses Self-Testing, and this is packaged in a dark blue box. For more information about these particular safety comms and what to be done if you come across these products, please go to these links and it's very thoroughly described within that text. With that, I will turn it back over to Kim. Thank you.

Commander Kimberly Piermatteo (FDA):
Thank you Tim and Kris for those opening remarks. We'll now answer your previously emailed questions about COVID-19 Test Development and Validation. Please note we receive some questions that are too detailed or test case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH-EUA-Templates@fda.hhs.gov mailbox for an update. Now let's get to the questions you sent in advance of today's Town Hall. Kris, I'll be directing these questions to you. The first question is, would real-world data also be considered acceptable for subsequent marketing applications of other EUA products, such as molecular in-vitro diagnostic tests?

Kris Roth (FDA):
Yeah, Thanks Kim. We are open to considering existing data to support a regulatory submission if you believe that you have real-world data that can be used to establish performance of your test. We're glad to engage in a discussion to appropriately leverage that real-world use and experience as part of your marketing application.

---

#### 5. FDA Guidance on De Novo Serology Test Submissions


Commander Kimberly Piermatteo (FDA):
Thank you, alright. The next question, is FDA currently reviewing any de novo submissions for serology tests? If so, would it be possible to share recommendations provided to developers at this time?

Kris Roth (FDA):
So again, we're not going to comment on any submissions that may be under review, however if you intend to pursue a de novo regulatory pathway for your serology test, we recommend that you submit a Pre-Submission with your study protocols, in order for FDA to provide appropriate feedback.

---

#### 7. Guidance on Enrichment Approaches for COVID-19 Test Evaluation


Commander Kimberly Piermatteo (FDA):
Thank you very much Kris. Alright, so our last pre-submitted question is, due to the recent decline in COVID-19 positivity rates, is it acceptable to test archive samples to supplement the positives tested during the clinical evaluation for an antigen point-of-care test?

Kris Roth (FDA):
Yes, thanks. So if pursuing an enrichment approach, which is really what this question is describing, you should appropriately tailor the study design for your specific test and you'll clearly document and describe how any bias associated with your proposal is minimized. We strongly recommend that you submit a pre-EUA with a detailed clinical study protocol prior to implementing any enrichment activities, such as using big samples.

Commander Kimberly Piermatteo (FDA):
Great. Thank you Kris. That wraps up the previously submitted questions. We will now take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your screen. When you are called on, please identify yourself and ask your question promptly. Also please note, we are not able to discuss specific submissions under review. Our first live question is from Sam. Sam I'm going to unmute you, please unmute yourself and ask your question.


---

## 2022-03-23_Virtual Town Hall 81_section-titles.md

#### 9. Live Q&A Guidelines and Participant Instructions


Commander Kimberly Piermatteo (FDA):
Great. Thank you, Toby. That wraps up the previously submitted questions. We will now move to the live question and answer part of today's town hall. To ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom to unmute yourself. Then identify yourself, and ask your question promptly. A few reminders before we take our first question—please limit yourself to one question only. If you have an additional question, you may raise your hand again to get back into the queue, and we will call on you again as time permits. And lastly, please remember, we are not able to discuss specific submissions under review. Our first live question is from Phil. Phil, I'm going to unmute you. Please unmute yourself and ask your question.


---

## 2022-04-06_Virtual Town Hall 82_section-titles.md

#### 2. Checking Authorization and Safety of COVID-19 Tests


Commander Kimberly Piermatteo (FDA):
Great, thank you, Toby. So we'll now answer a previously emailed question about COVID test development and validation. So, Toby, the first question we have is, "there have been several COVID‐19 test recalls recently for tests that were not FDA authorized, how can we check which COVID‐19 tests have been cleared or authorized by the FDA?"

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So all FDA authorized tests are listed on the FDA web page. The slides for this webinar, typically include the link to the listing of EUAs. And so you can find that on the slides that are posted from these webinars, and also, I think probably everyone on this call is familiar at this point with where on our website the EUAs are posted. We also have a risk specifically of FDA authorized at‐home, over the counter COVID‐19 diagnostic tests that can be found at the FDA's at‐home, OTC COVID‐19 diagnostic tests web page. Regarding the recalls that have been posted recently, we do regularly monitor the safety and performance of COVID‐19 diagnostic tests, including reports of adverse events and performance issues, and also, the marketing of unauthorized, unapproved, or uncleared tests. And we issue safety communications to help educate test users, caregivers, health care providers, and generally the public to‐‐ and to help reduce the risk of false test results that could lead to serious illness and death. So only home tests that are authorized by the FDA should be used by the American public. And we take steps to remove unauthorized home tests or any inappropriately offered tests from the market and inform test users and the public, caregivers, health care providers, to avoid using those tests. And we do want to emphasize that the use of inaccurate tests could harm our collective ability to stop the spread of COVID‐19. So that is why we have been putting out those notices for those recalls.

Commander Kimberly Piermatteo (FDA):
Thank you, Toby. So that wraps up our previously submitted question. We will now go ahead and take your live questions. So to ask a live question, please select the Raise Hand icon at the bottom of your screen. When you're called on, please follow the prompt in Zoom to unmute yourself, then identify yourself and ask your question promptly. A few reminders before we take our first question, please limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue and we will call on you as time permits. And lastly, please remember, we are not able to discuss specific submissions under review. So our first live question is from James. James, I'm going to unmute you. Please unmute yourself and ask your question.


---

## 2022-04-20_Virtual Town Hall 83_section-titles.md

#### 2. Fresh Samples Required for COVID-19 Antigen Test Studies


Commander Kimberly Piermatteo (FDA):
Thank you, Tim. Like Tim said, we'll now move to your previously emailed questions. __Please note we did receive some questions that are too detailed or too case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days.__ If you have submitted a question, and you do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA‐Templates@fda.hhs.gov mailbox for an update. Alright, Kris, I'll be directing these questions to you. The first question is due to the recent decline in COVID‐19 positivity rates, is it acceptable to test frozen archived positive samples during the clinical evaluation for an antigen home use test?

Kris Roth (FDA):
Yeah, OK, thanks, Kim. So for COVID‐19 home antigen tests, frozen retrospective samples are not appropriate or not an appropriate sample type at this time. We do recommend for OTC clinical studies that these studies be‐‐ use fresh prospectively collected samples for the intended use. And this gives this study a chance to evaluate not only the testing but the lay‐user collection process as well.

---

#### 5. Guidelines for COVID-19 Breath Test Development and EUA Process


Commander Kimberly Piermatteo (FDA):
Thank you, Kris. Alright, our last previously submitted question is, can test developers reference the InspectIR COVID‐19 Breathalyzer EUA summary for recommended studies for COVID‐19 tests using GC‐MS platforms?

Kris Roth (FDA):
Yes, thanks. So there is no template for breath tests intended for asymptomatic screening for COVID‐19. This particular question didn't mention that it was a breath test, but that's our assumption. And yes, for breath tests it is appropriate to reference the InspectIR COVID‐19 Breathalyzer EUA summary for recommended analytical and clinical validation studies to support EUA authorization for COVID‐19 testing using a GC‐MS approach. We're also glad to engage with breath test developers during the review of a pre‐EUA. And that is likely a good approach because this is a new kind of technology. And there may be nuances to a new platform when compared with the InspectIR platform. So we would welcome pre‐EUAs ways for these types of tests.

Commander Kimberly Piermatteo (FDA):
Alright, thank you, Kris and Tim. That wraps up the previously submitted questions. We will now move to take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you were called on, please follow the prompt in Zoom to unmute yourself. Then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you if time permits. And please remember we are not able to discuss specific submissions under review. Alright, our first question is from Enes. Enes, I'm going to unmute you. Please unmute yourself and ask your question. Enes, are you able to unmute yourself and ask your question? Alright, we'll go ahead and we'll move to the next question. The next question comes from Abdul. Abdul, I am unmuting you. Please unmute yourself and ask your question. Abdul, are you able to unmute yourself?


---

## 2022-05-04_Virtual Town Hall 84_section-titles.md

#### 2. Non-CLIA Labs for COVID Test Candidate Studies


Commander Kimberly Piermatteo (FDA):
Thanks, Toby. We'll now go to answer your previously emailed questions about COVID test development and validation. Please note, we have received some questions that are too detailed or test‐case specific, that we will not address during today's Town Hall. For those questions, we will try to send you a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, you may reach back out to the CDRH‐EUA‐Templates@fda.hhs.gov mailbox for an update. Toby, I'll be directing the first few questions to you. So the first question is, can moderate to high complexity labs that are not CLIA‐certified, and who do not generate or report patient results, be used to perform candidate testing?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. Yes, from FDA's perspective, we do not have an issue with clinical study testing being performed in a non‐CLIA lab, provided the results are not returned to the patient or provider, and the laboratory is able to perform the testing according to an appropriate study protocol.

---

#### 7. Analyzing Low Positives in Antigen Test Performance


Commander Kimberly Piermatteo (FDA):
Great, thanks Toby. Alright, our last previously submitted question I'll be directing to you, Tim. So the question is, some recently authorized at‐home antigen tests include tables showing performance calculations at varying percentages of low positives. How and when is this type of data analysis appropriate?

Tim Stenzel (FDA IVD Director):
Thank you, Kim. So data from recent prospective clinical studies with the omicron variant have shown unusually high rates of low viral load samples. Typically we've seen 10 to 20% low positive for all previous variants. This one, which may in fact‐‐ this time, which may in fact be linked to omicron, we're seeing the low positives range from about 30 to 40%‐‐ with obviously poorer performance with those low positive samples versus higher positive samples. Our current performance targets are based on a target of 10 to 20% low positives in the clinical study. For data sets that have more than 20% low positives, we have additional recommendations that can be used to calculate performance within the 10 to 20% target range. There are caveats to this approach, and so far it has only been used for tests evaluated by the NIH's Independent Test Assessment Program, which utilizes study designs developed in collaboration with the FDA, as well as a calibrated RT‐PCR reference method. If you have completed a current clinical validation study with confirmed omicron positive samples, and have collected more than 20% low positives in your prospective study, then please submit all of your data, including all the low positives, and we can work with you on this new analysis approach. If you have not yet completed your clinical validation and are planning your approach, we recommend that you submit a pre‐EUA if you would like to discuss your study design, including the percent low positives and the comparator method.

Commander Kimberly Piermatteo (FDA):
Great, thank you both, Tim and Toby. That wraps up our previously submitted questions. We'll now take your live questions. So to ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom to unmute yourself, then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. OK, our first live question is coming from Homer. Homer, I'm going to unmute you. Please unmute yourself and ask your question.


---

## 2022-05-18_Virtual Town Hall 85_section-titles.md

#### 2. FDA Prioritization of COVID-19 Test Accessibility


Commander Kimberly Piermatteo (FDA):
OK. Thank you, Toby. We'll now answer your previously emailed questions about COVID test development and validation. As mentioned before, please note we do receive some questions that are too detailed or test case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA‐Templates@fda.hhs.gov mailbox for an update. Alright, Toby. Our first question is, is FDA prioritizing review of OTC tests versus prescription home use rapid diagnostic COVID test kits?

Toby Lowe (FDA IVD Assoc Director):
So FDA's current thinking on prioritization of In Vitro Diagnostic EUA requests is explained in the FDA guidance document Policy for COVID‐19 Tests During the Public Health Emergency. That is the version that was issued on November 15th of 2021. And as discussed in section 4A of that guidance document, the priorities do not specify prescription status, but they do focus on tests that will significantly increase testing capacity and accessibility. Generally, the ability for consumers to purchase or otherwise acquire, since there are free distribution programs, home tests without a prescription typically would increase access to testing more than a test that requires a prescription.

---

#### 6. Challenges in Flu Test Validation and FDA Recommendations


Commander Kimberly Piermatteo (FDA):
OK. Our last previously submitted question for today is, can moderate to high‐complexity labs that are not CLIA‐certified and who do not generate or report patient results be used to perform a clinical study to support an EUA, either pre‐market or post‐market?

Toby Lowe (FDA IVD Assoc Director):
From an FDA perspective, we do not have an issue with a clinical study being performed in a non‐CLIA‐certified lab, provided there is appropriate IRB oversight and the results are not returned to the patient or provider, and that the laboratory is able to perform the testing according to an appropriate study protocol. And this is true for moderate and high‐complexity tests. This is not appropriate for waived tests.

Commander Kimberly Piermatteo (FDA):
Great. Thank you, Toby.

Toby Lowe (FDA IVD Assoc Director):
Or tests seeking waived status.

Commander Kimberly Piermatteo (FDA):
OK. Thanks, Toby.

Toby Lowe (FDA IVD Assoc Director):
Sorry about that.

Commander Kimberly Piermatteo (FDA):
No worries. Alright, Tim, we're going to go ahead and turn it over to you for some additional remarks today.

Tim Stenzel (FDA IVD Director):
Alright, thank you, Kim and Toby. Yeah, so I note that, yesterday, it was estimated in the U.S. that there was around 700,000 U.S. COVID positive test results. The vast majority of those are likely over‐the‐counter home test results, but the official numbers may under-represent how many COVID cases are still occurring on a daily basis in the U.S. So unfortunately, in the U.S., for SARS‐CoV‐2 at least, there are, unfortunately, plenty of positive patients for test validation work. Turning to the panel tests, particularly flu, we get a lot of questions about what to do about flu, especially flu B. I will note the latest weekly report from the CDC reports that the percent of flu positives within influenza‐like illnesses is at 8.6%. So among those who were thought to potentially have flu in the United States, there is a significant number that are actually flu positive. In addition, in the last week, there have been more than 3,000 hospitalizations for flu. So it is, unfortunately, a significant problem in the U.S. The challenge for test developers, at least in the U.S., is that 99.2% of the flu positives that are circulating now are flu A. So flu B, at the moment, is only 0.8% of the flu positives. So where it may be feasible to get flu A in the U.S. now with a well‐designed, well‐coordinated and well‐stationed study, even where there is flu, getting sufficient prospective fresh flu B positive is going to be challenging. I think if there are areas of the world where flu B is circulating, I think the FDA is going to be open to being able to go there, because there are some technologies, particularly direct detection technologies, that don't go into a VTM, which Toby mentioned earlier. And VTM for rapid antigen tests is problematic when it includes, at least for SARS, because we've seen so many challenges with VTM, and nearly all, if not all, of the antigen tests have moved away from the use of VTM. There are potential use of saline, but by and large, it is a direct swab. So getting banked direct swabs samples for evaluation of a flu A/B test is going to be challenging. And so prospective collection is still one option. So we're going to display some flexibility on where in the world you get the flu A/Bs. Also, Toby hit on this, as well, but really want to emphasize the importance of seeking full authorization as soon as possible for any developers who do want to stay in the market. So I encourage you to get started, if you haven't already. Q‐Subs for full conversions of molecular antigen and serology tests are being accepted. So reach out, and we'll give you some recommendations on those validations. And with that, we can, Kim, go back to you and open it up for live questions. Thank you.

Commander Kimberly Piermatteo (FDA):
Great. Thank you, Tim. Alright, we will now take your live questions. So to ask a live question, please select the Raise Hand icon at the bottom of your screen. When you are called on, please follow the prompt in Zoom to unmute yourself, then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And lastly, please remember we are not able to discuss device or specific submissions under review. Alright, our first live question is coming from Wendy. Wendy, I am going to unmute your line. Please unmute yourself and ask your question.


---

## 2022-06-01_Virtual Town Hall 86_section-titles.md

#### 2. FDA Guidance on Multiplex Antigen Test Authorization


Commander Kimberly Piermatteo (FDA):
Great, thank you, Tim. We'll now answer your previously emailed questions about COVID test development and validation. Again, as we've mentioned before, please note we have received some questions that are too detailed or test‐case specific that we will not address during today's Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within that few days, please feel free to reach back out to CDRH‐EUA­ Templates@fda.hhs.gov mailbox for an update. Kris, I'll be directing these questions to you. So our first question is, is FDA currently accepting EUA requests for multiplex antigen tests that can detect a combination of viruses such as SARS COVID‐19 and influenza intended for use in a point‐of‐care or over‐the‐counter setting?

Kris Roth (FDA):
Yes. Thank you, Kim. So, yes, FDA has authorized several antigen multi‐analyte diagnostic tests intended for use at laboratory and POC sites. We currently don't have any multi‐analyte OTC tests authorized at this time. However, we have recommendations in the appropriate template. And these types of tests do meet the current priorities. As we've noted before, if you are considering an OTC multi‐analyte test we recommend you submit a pre‐EUA to further discuss your test design and proposal.

---

#### 4. Exclusion Criteria for Symptomatic Subjects in COVID-19 Studies


Commander Kimberly Piermatteo (FDA):
Thank you, Kris. Alright, our last previously emailed question is, we are currently conducting a prospective clinical study to support an at‐home, rapid antigen test. One of the exclusion criteria recommended in the antigen template is ‐‐ Knows infected status positive or negative based on a predecessor COVID‐19 test resulted in 14 days prior to enrollment. Is this exclusion criteria appropriate to apply to symptomatic subjects? If so, what should be considered a predecessor COVID‐19 test?

Kris Roth (FDA):
The answer is yes. This inclusion criteria is appropriate for symptomatic subjects. And all COVID‐19 diagnostic tests‐‐ both antigen and molecular are considered predecessor tests. Currently, there are numerous tests available to many U.S. citizens. If you are observing that many individuals in your study have a known test result within the 14 days prior to enrollment, we recommend reaching out for additional recommendations specific for your clinical study design.

Commander Kimberly Piermatteo (FDA):
Thank you, Kris. So that wraps up our previously submitted questions for today. We will now take your live questions. To ask a live question, please select the Raise Hand icon at the top of your Zoom screen. When you were called on, please follow the prompt and Zoom to unmute yourself. Then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. So our first live question for today is coming from Jennifer. Jennifer, I'm going to unmute you. Please unmute yourself and ask your question.


---

## 2022-06-15_Virtual Town Hall 87_section-titles.md

#### 2. Evaluating Variants for OTC Rapid Antigen Test Authorization


Commander Kimberly Piermatteo (FDA):
Great. Thanks Toby. We'll now answer your previously emailed questions. Please note, we have received some questions that were too detailed or test case specific that we will not address today. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA­ Templates@fda.hhs.gov mailbox for an update. Alright, Toby. I'll be directing these questions to you. Our first question is, does FDA have a recommended number of variants that should be evaluated to support the EUA authorization for an OTC rapid antigen test?

Toby Lowe (FDA IVD Assoc Director):
No, we don't have specific requirements, but we do expect developers to evaluate the impact of all relevant variants. So for that, we recommend assessing the prevalence of viral mutations in sequence databases, such as the GISAID database, as mutations observed in these databases at a significant frequency may signify that the mutation is present in an increasing portion of infected individuals in the U.S. And generally, we consider a significant frequency to be greater than 5% when considering at least 2,000 sequences over a recent period of time, such as the past week, month, or quarter. We do have some additional information on evaluating the impact of viral mutations in our viral mutation guidance that was issued in 2021 and on our viral mutation webpage for COVID. And both of those can be found if you go to the FAQ page that's posted on the slide currently showing. Those resources can be found there.

---

#### 5. FDA Prioritization of Diagnostic Breath Test Evaluations


Commander Kimberly Piermatteo (FDA):
Thanks. Alright, our last previously submitted question is, is there an expedited track for FDA's evaluation of diagnostic breath tests?

Toby Lowe (FDA IVD Assoc Director):
There's not an expedited track, but FDA's current thinking on prioritization of in vitro diagnostic EUA requests is explained in our guidance policy for COVID tests during the public health emergency that was reissued on November 15 of 2021. And that is linked also on the resource slide that's currently showing. And we encourage you to review the FDA's current priorities in section 4a of the guidance document, which is on page 7, and the priorities are also explained in the flow charts in Appendix A of the same guidance document. And in those priorities, we lay out that we intend to focus on EUA requests for diagnostic tests, which can include breath tests, that can be used at the point of care or completely at home from developers who have indicated the ability to scale up manufacturing capacity shortly after authorization. And we do consider the public health needs as we prioritize submissions, so if there is a submission, an EUA request submitted for a test that looks like it will be highly beneficial for public health, we would prioritize such a submission.

Commander Kimberly Piermatteo (FDA):
Thank you, Toby. That wraps up our previously submitted questions. We will now take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom to unmute yourself. Then identify yourself, and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. So our first live question is coming from James. James, I have unmuted your line. Please unmute yourself and ask your question.


---

## 2022-06-29_Virtual Town Hall 88_section-titles.md

#### 2. Human Sample Controls in Molecular OTC Tests


Commander Kimberly Piermatteo (FDA):
Great. Thank you, Tim. Alright, we will now answer your previously emailed questions about COVID test development and validation. Please note, we have received some questions that were too detailed or test‐case specific that we will not address today. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA‐Templates@fda.hhs.gov mailbox for an update. Tim and Toby will be addressing today's previously emailed questions. So for the first question, I'll be directing it to Toby. Toby, the first question is, is a human sample control required for a molecular‐based OTC test? And if not, what other options would the FDA recommend test developers take to mitigate for improper collection?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So generally, FDA recommends including an internal process control and, ideally, a human specimen control to ensure that an adequate sample was taken. Tests without a human specimen control should use a well‐established collection procedure, such as a nasal swab placed into a buffer tube. This type of workflow is well‐established, and this has been shown, among other places, in the adequacy of nasal self‐swabbing for SARS‐CoV‐2 testing in children study that demonstrated that even young children are capable of collecting an appropriate nasal swab sample. Other types of samples or sampling protocols should be discussed with FDA to determine whether a human specimen control is recommended.

---

#### 7. EUA Requirements for OTC SARS-CoV-2 Antigen Tests


Commander Kimberly Piermatteo (FDA):
Great. Thanks, Toby. Alright, our last previously submitted question is, to support EUA for an OTC SARS‐CoV‐2 antigen test, does the FDA require a minimum percentage of low‐ positive samples collected in the clinical study?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So in order to support the EUA authorization for over‐the‐counter SARS‐CoV‐2 antigen tests, we generally recommend that a developer evaluate a minimum of 10% low positive samples. Low positives are typically defined as samples in which any gene target is within three cycle threshold CTs of the mean CT count at the comparator tests LoD. This information can be found in the main antigen diagnostic test EUA template on page 28. And it's important to note that we do want to see all of the data collected in your clinical studies provided in your EUA request, not only the first 10% low positives. Back to you.

Commander Kimberly Piermatteo (FDA):
Alright, thank you, Tim and Toby. That wraps up the previously submitted questions. We will now move to take your live questions. To ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom and select the blue button to unmute your line. Then identify yourself, and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you as time permits. And please remember, we're not able to discuss specific submissions under review. Our first live question is from Sam. Sam, I have unmuted your line. Please unmute yourself and ask your question.


---

## 2022-07-27_Virtual Town Hall 89_section-titles.md

#### 2. Acceptability of Non-U.S. Flu A and RSV Samples


Commander Kimberly Piermatteo (FDA):
Great. Thank you, Tim and Kris. We will now answer your previously emailed questions. Please note, we do receive some questions that are too detailed or test case-specific that we will not address today. For those questions, we will try to send you a response in writing within a few days. If you have submitted a question and do not here to addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH-EUA­ Templates@fda.hhs.gov mailbox for an update. Kris, I'll be directing these questions to you. The first question is, can FDA clarify if Flu A and RSV samples from outside the U.S. are acceptable to use in analytical test studies?

Kris Roth (FDA):
Thanks, Kim. So again, I just want to highlight this is analytical test studies. So, well- characterized Flu A and RSV strains with certificate of analysis or other such assurances of identity and quality from reputable institutions or sources outside the U.S. could be considered as acceptable for conducting analytical studies. We recommend that you document and, if needed, demonstrate that the strains tested were well-characterized.

---

#### 3. Guidance for Clinical Validation and Live Q&A Challenges


Commander Kimberly Piermatteo (FDA):
Thank you, Kris. Alright, our next question has two parts. I'll read them both, and then I'll turn it over to you, Kris. So that first part is, can FDA provide additional recommendations that can be used to calculate performance within the 10% to 20% target? The second part is, can multiple positive percent agreement calculations be used if a prospective clinical data set for a home use antigen test has greater than 20% low positives?

Kris Roth (FDA):
Sure. Thanks. So if you have completed a clinical validation study with confirmed omicron positive samples, and you have collected more than 20% low positives in your prospective clinical study, then we recommend submitting all of your data, including all the low positives, and we can work with you on a data analysis approach. If you have not yet completed your clinical validation and are planning your approach, we recommend that you submit a pre-EUA if you would like to discuss your study design, including the percent low positives and the comparator method. However, this should not delay the start of your clinical study since the study protocol details, such as enrollment criteria and the number of positives needed, is not impacted.

Commander Kimberly Piermatteo (FDA):
Thanks, Kris. That wraps up our previously submitted questions. We will now take your live questions. So as a reminder, to ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom and select the blue button to unmute your line, then identify yourself and ask your question. Please do remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you if time permits. And please remember, we are not able to discuss specific submissions under review. Our first live question is coming from Joshua. Joshua, I'm going to unmute you. Please unmute yourself and ask your question. Joshua, I've unmuted you again, if you can look for that prompt to unmute yourself. Alright, Joshua, I'm going to come back to you. Keep an eye out. I'll try to come back to you after we go to our next caller. Annie, I am unmuting your line. Please unmute yourself and ask your question.

Tim Stenzel (FDA IVD Director):
Kim, I don't usually see the mute function still on. I'm just wondering if you're really unmuting these folks or if they're muted.

Commander Kimberly Piermatteo (FDA):
Yes.

Tim Stenzel (FDA IVD Director):
OK.

Commander Kimberly Piermatteo (FDA):
So I'm going to ask Annie to unmute again.

Tim Stenzel (FDA IVD Director):
Hope we're not having technical difficulties.

Commander Kimberly Piermatteo (FDA):
Yes. Let me.

Tim Stenzel (FDA IVD Director):
Could you try the next person? Try to get somebody who's live.

Commander Kimberly Piermatteo (FDA):
Yep. So we're going to go ahead and move down to Anjali Zimmer. I'm going to allow you to talk. Please unmute yourself and ask your question.


---

## 2022-08-24_Virtual Town Hall 90_section-titles.md

#### 2. EUA Requirements for Multiplex COVID-19 and Flu Tests


Commander Kimberly Piermatteo (FDA):
Great. Thank you, Kris, for those opening remarks. We will now answer your previously emailed questions. Please note, as always, we do receive some questions that are too detailed or test‐case specific that we will not address today. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the CDRH‐EUA­ Templates@fda.hhs.gov mailbox for an update. Toby, I'll be directing these questions to you. The first question has two parts. And the question is, the first part, "Is FDA currently accepting EUA requests for multiplex antigen tests that can detect a combination of viruses, for example, SARS‐CoV‐2 and influenza, intended for use in an OTC setting?". The second part of that question is "For a multiplex molecular test with both flu and COVID, is it required to have a separate call for both flu A flu B in addition to COVID, or is it acceptable to combine flu A and flu B into a general influenza call?".

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So we have authorized several antigen multi‐analyte diagnostic tests intended for use at laboratory and point of care sites. We currently do not have any multi‐analyte over‐the­ counter tests authorized, but we do have recommendations in the appropriate template, and these types of tests do meet the current priorities. We've noted here before that if you're considering an over­ the‐counter multi‐analyte test, we recommend that you submit a pre‐EUA to further discuss your test design and proposal. Regarding the flu and COVID and the separate calls for flu A and B, there are numerous flu A/B rapid antigen tests on the market, and all of those differentiate between flu A and B. So our current recommendations are in favor of reporting a separate flu A and B result because the risks and benefits of flu A and B results are different.

---

#### 6. FDA Authorization of COVID-19 Diagnostic Breath Tests


Commander Kimberly Piermatteo (FDA):
Thanks, Toby. Our last previously emailed question is "Has FDA authorized SARS‐CoV‐2 diagnostic breath tests?".

Toby Lowe (FDA IVD Assoc Director):
Yes, we have authorized one, that is the InspectIR COVID‐19 breathalyzer, that analyzes breath samples for SARS‐CoV‐2 detection. And information about that test can be found on our website on the EUA Other Tests for SARS‐CoV‐2 web page. And anyone who is interested in submitting an EUA request for additional breath tests can take a look at the information, authorization documents for that authorized test to see what data we looked at for that one.

Commander Kimberly Piermatteo (FDA):
Great Thanks, Toby. So that wraps up our previously submitted question segment. We will now take your live questions. So to ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom and select the blue button to unmute your line. Then identify yourself and ask your question. Please remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue, and I will call on you as time permits. And please remember, we are not able to discuss specific submissions under review. Alright, our first live question is coming from Anjali. Anjali, I'm going to unmute your line. Please unmute yourself and ask your question.

---

#### 9. Optimizing Clinical Trial Design for Dual Testing Kits


Seungjin Ha Gina:
Hi, how are you? This is Gina from Seungjin. And our company is developing the influenza A and B with COVID‐19 detection antigen testing kits under the FDA EUA process. And the other one, we are also developing for the influenza A and B, also antigen testing kits under the FDA 510k process. But we are trying to conduct a clinical trial with those two testing kits under the same procedure at the same time by the IRB operable with the clinical trial protocol. So I would like to know, if we collect one swab sample from our patients and it will be added into the reagent tube and containing the extraction of buffer. And also, we will use this one swab and one extraction buffer to the two kits at the same time. So we would like to know if it is possible for clinical trial with these two kits at the same time under the IRB approval. Do you think it is available or acceptable by your side?

Kris Roth (FDA):
Yeah, thanks for that. It's a little bit of a challenge because you are using the test kind of off label or not with the instructions that folks will have if it's either the COVID/flu combo or the flu alone. That being said, we do want to try to make efficiencies available to developers where it's appropriate. And so I think probably you're going to want to submit this as a pre‐EUA and let us know what the volumes are, what the challenges are, what happens if they run out of volume on the second test or something of that nature. And then I would also maybe think about a backup plan as well. So propose a sampling plan of, we'll do the standard care first, then we'll do the flu/COVID next, then the flu alone, and some sort of randomization scheme. So I would just plan for both instances or provide us a plan, I guess, in both instances, one, using the same abstraction buffer and two, provide a sampling plan that minimizes bias for the two candidate tests.

Seungjin Ha Gina:
So you recommend we have to get through the pre‐EUA for those submissions?

Kris Roth (FDA):
Yeah, I wouldn't be able to comment. I can't say on the phone, yes, it's fine to use the same abstraction buffer. One, it's off‐label use to use against the instructions for use. And number two, we'd be concerned about running out of buffer.

Seungjin Ha Gina:
OK. I got it. So before we are going to conduct the clinical trials with these at the same time, clinical trials, we have to get through the pre‐EUA and FDA should have reviewed our clinical trial first before removing every bias for conducting this clinical study. Am I correct?

Kris Roth (FDA):
That would lower your risk. Of course, if we know what you're going to do prior to you doing it, then you've got buy in from us, and you can be confident that your sampling plan is kind of agreed upon. Of course, that's not a requirement. You can go off and do your study, and then we can review it after it's done. But that's a little bit more risk on your end.

Seungjin Ha Gina:
Yeah, I understand. OK, thanks.

Kris Roth (FDA):
Thank you.

Commander Kimberly Piermatteo (FDA):
Thank you Gina and Kris. At this time, I'm going to ask if anyone has any questions to please raise your hand. OK we have a question from Kay. Kay, I have unmuted your line. Please unmute yourself and ask your question.


---

## 2022-09-28_Virtual Town Hall 93_section-titles.md

#### 2. Guidance for Submitting Monkeypox EUA Requests to FDA


Commander Kimberly Piermatteo (FDA):
All right. Thank you, Toby, for that presentation on those updates. We will now answer your previously emailed questions. We will address today's previously emailed questions in two parts. The first part will address monkeypox previously emailed questions. And then we will address the COVID-19 previously emailed questions. As always, please note we do receive some emailed questions that are too detailed or test case specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the appropriate mailbox, either the MPXDx@fda.hhs.gov mailbox or the COVID19DX@fda.hhs.gov mailbox for an update. So Toby, I'll be directing these previous emailed questions about monkeypox to you. The first question is, for monkeypox diagnostic test developers informing FDA of their intent to submit an EUA request, can the intent to submit be provided without a timeline for completion of validation studies and submission of an EUA request? So as discussed in the monkeypox test policy guidance, FDA generally recommends including certain preliminary information in the test developer's email to FDA to indicate their intent to submit an EUA request for a monkeypox diagnostic test. So that information includes the description of the test technology, manufacturing capacity, test throughput, any available validation data, and the expected timeline for development validation and submission of an EUA request. While these are recommendations, not requirements as laid out in the guidance, this information will be beneficial to facilitate FDA's prioritization efforts.


---

## 2022-10-26_Virtual Town Hall 96_section-titles.md

#### 2. Guidelines for Monkeypox Test Development and Validation


Commander Kimberly Piermatteo (FDA):
Thank you Tim and Toby for those remarks. We will now answer your previously emailed questions about monkeypox and COVID‐19 test development and validation. As always, please note we do receive some emailed questions that are too detailed or test case‐specific that we will not address during today's Virtual Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the MPXDx@fda.hhs.gov mailbox or the COVID19DX@fda.hhs.gov mailbox for an update. So Toby, I'll be directing these first previously emailed questions about monkeypox test development to you. The first question is a two‐part question regarding a clinical study using retrospective natural clinical specimens. So the first part of that question is, can an EUA‐authorized monkeypox test be used for discordant analysis between the candidate device and the CDC test?

Toby Lowe (FDA IVD Assoc Director):
They can. As noted in the molecular diagnostic templates, we do recommend establishing a discordant analysis plan prior to your clinical studies. Excuse me. Discordant samples should be tested with an EUA‐authorized PCR test that has been validated for the same type of clinical specimen, has demonstrated high sensitivity, and uses a chemical lysis step followed by solid phase extraction of nucleic acids, such as silica bead extraction. And this is all discussed in the template. And we should also note that results from a discrepant analysis should not be included in the calculation of NPA and PPA but may be added to the performance table as a footnote.

Commander Kimberly Piermatteo (FDA):
Thanks, Toby. Alright, the second part of that question is, per the FDA's template for developers of molecular diagnostic tests for monkeypox, the clinical evaluation section recommends that 20% of the samples evaluated below positive samples as measured per the comparator assay, meaning that the CT values are within three CT of the mean CT at the Level of Detection, or LOD, of the comparator test. Can prospective samples be supplemented with additional low positive samples, such that 20% of all positive samples in the analysis have low viral load?

Toby Lowe (FDA IVD Assoc Director):
Yes. We recommend that if needed, low positive samples can be supplemented with either archived samples or samples collected from convalescent patients in order to include approximately 20% low positive samples, as determined by the comparator, which right now is the FDA‐cleared CDC monkeypox virus PCR‐based assay.

Commander Kimberly Piermatteo (FDA):
Thanks, Toby. Alright, our last monkeypox test development and validation question is, if a MPXV test uses Research Use Only, or RUO, instruments, such as PCR or extraction instruments manufactured by either the test developer or another manufacturer, does FDA recommend providing a qualification protocol and For Emergency Use Only label in the tests instructions for use?

Toby Lowe (FDA IVD Assoc Director):
Yes. For monkeypox virus tests that use research use only instruments, the EUA template does discuss our recommendations for this. And the template discusses recommendations specifically for providing a qualification protocol, Emergency Use Only labeling or label, and quality system information, depending on whether the test developer is also the instrument manufacturer. And if a developer has specific details or situations that they need specific questions answered about, those generally are discussed as needed during the EUA review since labeling is typically finalized after completion of the substantive review of the data.

---

#### 5. FDA Transition Plans for COVID-19 Device Policies


Commander Kimberly Piermatteo (FDA):
Thanks again, Toby. So our last previously submitted question today is, with the implementation of new COVID‐19 test policy, is FDA also planning to implement the transition plan for medical devices that fall within enforcement policies issued during the coronavirus disease 2019, COVID­ 19, public health emergency soon? If so, can FDA provide an estimated implementation date?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So we have discussed the transition plan draft guidance documents on previous town halls. And as discussed, we are working to finalize those draft guidance documents. The drafts were issued late last year. And it's important to note that those two draft guidance documents are not test specific. They're for all medical devices that fall within enforcement policies or were issued EUAs during the COVID‐19 public health emergency. And they do address different situations than the newly updated COVID‐19 test policy guidance. So the draft guidance document titled “Transition Plan for Medical Devices that Fall within Enforcement Policies Issued During the COVID‐19 Public Health Emergency” provides FDA's recommendations and expectations for devices under COVID‐19 related enforcement policies to transition back‐to‐normal operations when the public health emergency expires. And it is very important to note that the COVID­ 19 test policy guidance is outside of the scope of that transition guidance. And then COVID‐19 tests that were issued EUAs are within the scope of the draft guidance document titled “Transition Plan for Medical Devices Issued Emergency Use Authorizations During the COVID‐19 Public Health Emergency,” which addresses the transition back‐to‐normal operations when the emergency use declarations that allowed for FDA to issue EUAs are no longer in effect. However, we're not able to comment on estimated finalization dates for draft guidances, so we do recommend that you keep an eye on FDA's website for any updates there.

Commander Kimberly Piermatteo (FDA):
Thanks again, Toby, for all of your responses. And thank you to those stakeholders who submitted those questions. That wraps up the previously emailed questions for both monkeypox and COVID‐19 test development. We will now take your live questions. As a reminder, to ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom and select the blue button to unmute your line. Then identify yourself, and ask your question, indicate whether the question is related to monkeypox or COVID‐19, and please, remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you as time permits. So our first live question is coming from Dr. Farhan Khan. I have unmuted your line. Please unmute yourself and ask your question.


---

## 2022-11-30_Virtual Town Hall 98_section-titles.md

#### 1. Monkeypox and COVID-19 Testing Updates and EUA Plans


Commander Kimberly Piermatteo (FDA):
Hello and welcome everyone to today's Virtual Town Hall Number 98 for monkeypox and SARS‐CoV‐2 test developers. Today, we will discuss and answer your questions about diagnostic tests in response to the monkeypox and COVID‐19 public health emergencies. This is Commander Kim Piermatteo of the United States Public Health Service, and I am the Education Program Administrator within the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. I'll be your moderator for today's Virtual Town Hall. Our panelists for today are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics, which is also referred to as the Office of Health Technology Number 7, or OHT 7, in CDRH's Office of Product Evaluation and Quality, or OPEQ. Joining Tim is Toby Lowe, Associate Director for Regulatory Programs in OHT 7, and Dr. Kristian Roth, Deputy Director of the Division of Microbiology Devices in OHT 7 as well, and Dr. Noel Gerald, Branch Chief for Bacterial, Respiratory, and Medical Countermeasures in OHT 7 as well. For today's Virtual Town Hall, we'll begin with opening remarks. Then, we'll answer your previously emailed monkeypox and COVID‐19 test questions. And then, lastly, we will address your live questions. As a friendly reminder for those of you participating live in today's Virtual Town Hall, please be sure you have joined us today via the Zoom app and not through a web browser to avoid any technical issues. Our last scheduled Virtual Town Hall for the calendar year 2022 will be on December 14th for both monkeypox and COVID‐19 test developers. You may refer to our webpage titled “Virtual Town Hall Series ‐ Test Development and Validation During Public Health Emergencies for COVID‐19 and Monkeypox” webpage for details on all upcoming Virtual Town Halls. Links to both of these pages have been provided on this slide. The presentation and transcript for our last Virtual Town Hall for monkeypox test developers specifically, which was held on November 9th, 2022, has been posted to CDRH Learn. I have provided a screenshot on this slide of where you can find those materials within CDRH Learn. I'd now like to welcome Toby, who will provide today's opening remarks. Toby, the floor is yours.

Toby Lowe (FDA IVD Assoc Director):
Thank you, Kim. Thanks everyone, for joining us for another town hall. Our initial update is we just have one update to provide, and that is to share that, yesterday, we posted EUA templates for antigen diagnostic tests for mpox, and those are available on our website, which is showing on the slide right now. So that's the same place where the molecular templates are on our website as well. And with that, we can move into the questions.

Commander Kimberly Piermatteo (FDA):
Great. Thank you, Toby. We'll now answer your previously emailed questions about monkeypox and COVID‐19 test development and validation. As always, please note, we do receive some email questions that are too detailed or test case specific that we will not address during today's Virtual Town Hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the MPXDx@fda.hhs.gov mailbox or the COVID19Dx@fda.hhs.gov mailbox for an update. Toby, I'll be directing this previously emailed question about monkeypox test development to you. The question is what are FDA's long‐term plans with the monkeypox EUA? Is there a time frame to keep it open, since cases are decreasing in the United States?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So as we've discussed here and in the guidance document, there is currently an EUA declaration in place under Section 564 of the FD&C Act which declares that circumstances exist justifying the authorization of emergency use of in vitro diagnostics for detection or diagnosis of monkeypox. We cannot anticipate when that declaration may be terminated. It's important to note that EUA declarations have historically been left open for quite a while to ensure that public health needs are addressed, and this is seen with several previous public health emergency declarations, including Zika, Ebola, and, obviously COVID‐19, which have not been terminated to date. And we at FDA are committed to help ensure that the public has access to appropriate test options for monkeypox, and we will continue to review EUA requests as needed to address public health needs.

Commander Kimberly Piermatteo (FDA):
Thanks, Toby. As a second part to that question, the question is in the instance the EUA is kept open, what would happen to the authorized ones in the case that any potential future product is cleared? Will this affect and/or limit the status or validity of the previously authorized EUAs?

Toby Lowe (FDA IVD Assoc Director):
Thanks. So as with all EUA declarations and EUAs, unless revoked, the EUAs are in effect until the EUA declaration is terminated. And those EUAs, the tests that are authorized under those EUAs, should be maintained in accordance with the conditions of authorization. Clearance of future products does not automatically mean that EUAs for other products will be revoked. As we can see with the COVID tests, we can clear a 510k without revoking EUAs for other tests. And, notably, for mpox, we already have a cleared 510k for a non‐variola orthopox virus test that detects monkeypox virus, and that test has been cleared since before the EUA declaration was made. And we also do welcome additional premarket submissions for mpox tests.


---

## 2022-12-14_Virtual Town Hall 99_section-titles.md

#### 1. Mpox and COVID-19 Diagnostic Test Updates and Guidance


Commander Kimberly Piermatteo (FDA):
Hello, and welcome everyone to today's Virtual Town Hall number 99 for monkeypox or mpox, and SARS‐COV‐2 test developers. Today we will discuss and answer your questions about diagnostic tests in response to the mpox and COVID‐19 public health emergencies. This is Commander Kim Piermatteo of the United States Public Health Service, and I am the Education Program Administrator within the Division of Industry and Consumer Education in CDRH's Office of Communication and Education. I'll be your moderator for today's Virtual Town Hall. Our panelists for today are Dr. Timothy Stenzel, Director of the Office of In Vitro Diagnostics, which is also referred to as the Office of Health Technology, number seven, or OHT7, in CDRH's Office of Product Evaluation and Quality or OPEQ. Joining Tim is Toby Lowe, Associate Director for Regulatory Programs in OHT7, and Dr. Kristian Roth, Deputy Director of the Division of Microbiology Devices in OHT7, and Dr. Noel Gerald, Branch Chief for Bacterial Respiratory and Medical Countermeasures in OHT7 as well. For today's Virtual Town Hall we'll begin with opening remarks, and then we'll answer your previously emailed questions. And then lastly we will address your live questions. As a friendly reminder for those of you participating live in today's virtual town hall, please be sure you have joined us via the Zoom app and not through a web browser to avoid any technical issues. Our next Virtual Town Hall will be held on Wednesday, January 11, 2023, for both mpox and COVID‐19 test developers. You may refer to our web page titled “Medical Device Webinars and Stakeholder Calls,” specifically our “Virtual Town Hall Series ‐ Test Development and Validation During Public Health Emergencies for COVID‐19 and Monkeypox” web page for details on all upcoming virtual town halls. Links to both of these web pages have been provided on this slide. The presentation and transcript for our last Virtual Town Hall, which was held on November 30, 2022, have been posted to CDRH Learn. I have provided a screenshot on this slide where you can find those materials within CDRH Learn. I'd now like to welcome Toby, who will provide today's opening remarks for mpox and COVID‐19. Toby, the floor is yours.

Toby Lowe (FDA IVD Assoc Director):
Thank you, Kim. Thanks, everyone, for joining again for another town hall. As Kim mentioned, this will be the last one of 2022. So we also wish you all a happy holiday season and end of year. So just a couple updates. As I'm sure most of you are aware, in response to the World Health Organization action, the FDA is adopting the mpox name from this point forward. We have begun to reflect this change in web content and other written material prospectively. Additionally as we've mentioned previously, we've responded to some of the pre‐EUAs for mpox tests to let sponsors know whether or not we would be prioritizing review of their test, and we have begun review of some EUA requests accordingly. If you have not yet received a response on your pre‐EUA, please just note that we are still considering some of those in the context of the shifting needs of the public health emergency, and we will get back to you with a response as soon as we're able to. Moving to COVID‐19 updates, just yesterday we updated the SARS‐COV‐2 viral mutations web page that discusses the impact on COVID‐19 tests. And that update was to add an additional entry for the Luminostics Clip COVID Rapid Antigen Test, where the sensitivity may be impacted when a patient sample containing the virus with certain mutations is tested. Excuse me, additional information is up on that website for that test. And with that, I will hand it back to you Kim.

Commander Kimberly Piermatteo (FDA):
Thanks, Toby, for those remarks. Alright, we will now address or answer, sorry, your previously emailed questions about mpox and COVID‐19 test development and validation. As always, please note we do receive some emailed questions that are too detailed or test case specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the MPXDx@fda.hhs.gov mailbox, or the COVID19Dx@fda.hhs.gov mailbox for an update. Also we have received some specific questions as a follow up to FDA feedback from pre‐EUA or Pre‐Submission requests, that we will not address during today's virtual town hall. For those questions we encourage you to contact your assigned lead reviewer to discuss or submit a supplemental request. Toby, I will be directing these previously emailed questions about mpox test development to you. The first question is a series, so it's a series of questions that pertains to mutation monitoring in mpox tests. For the first part there is one question. The mutation monitoring section of the mpox submission template states, monitoring should include identifying if there are multiple credible reports indicating that a given viral variant, which may have one or more mutations, has the potential to increase virulence, increase transmission, or otherwise increase the public health risk. The question is, can FDA clarify what credible reports are appropriate?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So we do recommend using peer reviewed literature, or in the more immediate term, using reports from public health communities, from the public health community, such as state public health laboratories. There may also be other situations where a test developer receives a signal that there may be an issue, and that's something that would be considered on a one‐off basis, since monitoring for impact of mutations is a very important aspect of maintaining test performance.

Commander Kimberly Piermatteo (FDA):
Thanks, Toby. So for the second part of this question, there are three questions. To give context it says, the mutation monitoring section of the mpox submission template states, if the mutations are found to be critical to your test design, such mutations and variants should be evaluated using clinical or contrived, as available and as appropriate, samples to assess the impact of the mutation or variant on your test performance. The aggregate impact of the mutations should not reduce the clinical performance of the test by 5% or more or decrease the clinical performance point estimates for the test below the minimum clinical performance recommendations. The first question for this part is, what does a reduction of clinical performance by 5% or more mean?

Toby Lowe (FDA IVD Assoc Director):
Thanks Kim. So we consider a reduction in clinical sensitivity of 5% or more from the previously established performance, which is the performance reflected in the authorized documents for authorized tests, or a decrease in the test performance to a level below the performance recommendations in the applicable EUA templates.

Commander Kimberly Piermatteo (FDA):
Thanks Toby. So the second question of this part is, if clinical performance is defined by positive percent agreement or PPA, what testing clinical samples compared with a high sensitivity comparator method, how are data generated from current viral sequences, though in silico or wet testing with contrived samples correlated to the original clinical study?

Toby Lowe (FDA IVD Assoc Director):
So if a test is expected to fail due to a mutation, and by fail we mean return a false negative, fail to detect the virus, and that mutation that would cause that failure is in more than 5% of currently circulating virus sequences, then we consider the test to be at risk of exhibiting a performance decrease of at least 5% of the performance in the EUA labeling, where which is the performance that was generated using clinical samples without that problematic mutation.

Commander Kimberly Piermatteo (FDA):
Thanks again, Toby. So the last and third question of this part is, are we to consider a download of current strains within a certain time frame to be indicative of all circulating strains since submission?

Toby Lowe (FDA IVD Assoc Director):
Thanks. So we do recommend monitoring on at least a monthly basis, as well as if requested at any point by FDA. And if FDA requests records, we expect that records of these evaluations be submitted for FDA review within 48 hours of the request.


---

## 2023-01-11_Virtual Town Hall 100_section-titles.md

#### 2. Guidance on SARS-CoV-2 Test Development Controls


Joseph Tartal (FDA):
Thank you, Toby. We'll now answer your previously emailed questions. Please note, we do receive some email questions that are too detailed or to test case-specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the MPXdx@fda.hhs.gov mailbox for mpox questions, or the COVID19dx@fda.hhs.gov mailbox for COVID questions for updates. Also, we received some specific questions as a follow-up to FDA feedback from pre-EUA, emergency use authorizations, or pre-submission requests that we will not address during today's virtual town hall. For those questions, we encourage you to contact your assigned lead reviewer to discuss or submit a supplement request. So as we move on to our mpox questions, there are no previously emailed questions about mpox development, so we'll move to the previously emailed questions related to COVID-19 test development. So for the previously emailed questions about SARS-CoV-2, I will be directing these questions to Toby. So the first question is, can SARS-CoV-2 test developers use plasma and serum that has been depleted of anti-SARS-CoV-2 antibodies as a negative control material for development of new serological tests and for negative controls for serology and neutralizing antibody tests that have already been granted approval?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. So generally we recommend that developers who hold an EUA authorization would first attempt to-- or who are seeking authorization would first attempt to obtain samples collected from prior to December 2019 from vendors and pull them to have enough volume for their testing. We would be concerned that depletion of SARS-CoV-2 antibodies from samples may change the sample architecture or the antibody or protein content depending on the depletion method used. So sponsors would need to validate those controls to ensure that false results would not be reported as a result of changes to the composition of the controls. And significant changes to the control's chemistry or composition would need to be submitted to the FDA for review for those tests that have already been granted an EUA-- or issued an EUA. Additionally, we recommend that sponsors review the current policy to consider the FDA's current EUA review priorities, and if the changes that you're looking to make would not meet those review priorities, we would encourage you to pursue a traditional premarket review pathway, such as a de novo or a 510k.


---

## 2023-02-15_Virtual Town Hall 101_section-titles.md

#### 2. Updates on Mpox and COVID-19 Test Policies


Toby Lowe (FDA IVD Assoc Director):
Thanks, Tim. So I will go through a couple updates and then we will get into the previously submitted questions. So first, for mpox, we just wanted to share that a few days ago, we authorized the Cepheid Xpert mpox test, which is the first mpox test authorized for use in a point-of-care setting. And that validation data for that EUA was gathered through the NIH ITAP program. For COVID, we have a few updates. In January, about a month ago, we issued a level two update, so minor policy updates, to the COVID-19 test guidance, as well as the viral mutations policy guidance. Those updates were to reflect that the guidances will be in effect for the duration of the Section 564 declaration, rather than the 319 Public Health Emergency. So that basically, affects the plan going forward-- as Tim was just talking about-- with the 319 expected to end in May, and I'll get into that a little bit more in a minute. We also updated-- some minor updates in the mutations guidance. That one hadn't been updated in a while so we updated some language to match the September 2022 update to the test policy guidance-- encouraging submissions of traditional premarket review submissions, added some links to additional web resources that we've put in place since the initial version of that guidance, and updated some of the actions we've taken since that first guidance was issued. So as mentioned, the administration has announced that the Public Health Emergency under 319 will end on May 11. As we've discussed before and as is noted in our FAQs on the website, we don't plan to take any action that would leave Americans without the tests that they need. We recognize that the manufacturers of tests that were issued EUAs will need an appropriate period of transition time to transition to normal operations when the declaration under 564 is no longer in effect, but it is important to note that only the 319 is scheduled to end on May 11th. The 564 is separate and will continue until the HHS secretary terminates it. It is not dependent upon the 319 PHE declaration. There's more information on our website in the FAQs about what happens when the 319 PHE expires, and we also have issued a draft guidance, last December, about the transition plan that is in the process of being finalized. And we received some great questions and comments during the comment period for the draft guidance, and those will be addressed in the final. If you have specific questions about how to manage your current plans, you can always send an email to the EUA Templates mailbox or submit a Pre-Submission if you plan for a de novo or 510k. And last update is a week or so ago, we made an update to our Understanding At-home OTC COVID-19 test page. This page has a step-by-step guide for lay users, and we updated that to include information about reporting OTC test results to the NIH-maintained website-- makemytestcount.org. We do encourage test users to voluntarily and anonymously report their at-home COVID-19 test results. And users can report their results to that website-- makemytestcount.org-- or by using the reporting options that might be included with a test, such as some of the tests that have an app that includes a reporting options. And with that, I can hand it back to Kim, and we can start the pre-submitted questions. www.fda.gov

Commander Kimberly Piermatteo (FDA):
Thank you, Toby, and thank you, Tim, for those remarks. We will now answer your previously emailed questions about mpox and COVID-19 test development and validation. As always, please note, we do receive some emailed questions that are too detailed or test case-specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a response within a few days, please feel free to reach back out to the MPXDx@fda.hhs.gov mailbox or the COVID19DX@fda.hhs.gov mailbox for an update. Also, we have received some specific questions as a follow-up to FDA feedback from pre-EUA or Pre- Submission requests that we will not address during today's virtual town hall. For those questions, we encourage you to contact your assigned lead reviewer to discuss or submit a supplemental request. Alright, Toby, so we have one previously submitted question for mpox test development that we'll address today, and that question is, "As the cases of mpox in the US and worldwide have declined, will FDA consider revising the current requirements, such as reducing the number of samples required or extending the timelines, for the mpox EUA clinical studies, including those required as a condition of authorization when contrived specimens were used for the initial authorization?"

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So we do continue to monitor and assess the testing landscape in the United States and other relevant factors regarding the mpox outbreak, and we will revise policies and recommendations as appropriate. Since fresh mpox samples are unlikely to be available at any time in the near future, we suggest that those developers, who have validated their tests only on contrived samples, validate them on banked positives and negatives if they have not done so already. And if a developer has further questions regarding their post-authorization study design, we recommend that you reach out to your FDA lead reviewer.


---

## 2023-03-22_Virtual Town Hall 102_section-titles.md

#### 3. COVID-19 Antigen Test Submission Pathways and Regulations


Joseph Tartal (FDA):
Thank you, everyone, for those opening remarks. We'll now answer your previously- emailed questions about mpox and COVID-19 test development and validation. Please note, we do receive some emailed questions that are too detailed or test case-specific that we will not address during today's town hall. For those questions, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed today, please look for a written response. If you do not receive a written response in a few days, please feel free to reach back out to us at MPXDx@fda.hhs.gov email box or to COVID19Dx@fda.hhs.gov mailbox for an update. Also, we have received some specific questions as a follow-up to FDA feedback from the pre-emergency- use authorization or pre-submission requests that we will not address during today's virtual town hall. For these questions, we encourage you to contact your assigned lead reviewer to discuss or submit a supplemental request. So with that, let's talk about these questions. So first, we have received no previously-emailed questions about mpox test development that we will address today. So we will move on directly to the COVID questions. So the first question, I will direct to you, Toby, which is, FDA recently granted a de novo for Quidel's Sofia 2 test antigen for use in point-of- care setting. Can an over-the-counter COVID-19 antigen test be submitted through the 510k pathway now using the Quidel's Sofia 2 test as the predicate device?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. No, the Quidel Sofia 2 test is cleared only for point-of-care use, not over-the- counter. And the regulation and special controls were drafted for point-of-care use. While we have not yet granted full marketing authorization for an at-home over-the-counter COVID-19 antigen test, we are interested in doing so, and the first such test would need to be granted through the de novo pathway.


---

## 2023-04-26_Virtual Town Hall 103_section-titles.md

#### 2. COVID-19 Test Regulations Post-Public Health Emergency


Joseph Tartal (FDA):
Yep, thank you, Toby, for that valuable information. Great presentation. We'll now answer your previously emailed questions about COVID-19 test development validation and the final emergency use authorization transition guidance documents. As always, we have received some questions that are a little too detailed or test case specific that we will not address on today's call. Further, we are focusing primarily on the transition for today's town hall, and some questions we received are not related to the transition and the transition guidances. For those questions that we don't address on today's call, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed, please look for a written response. If you do not receive one within a few days, please feel free to reach back out to the COVID19dx@fda.hhs.gov mailbox. So our first question, we have received several questions about submissions following May 11th, and the transition period for both COVID-19 transition guidances. And I'll try to group a few of these together here to respond to them all together so that we don't have overlap. So there's four parts of this. What is the FDA's plan regarding devices that are currently under EUA submission review post May 11th? During the transition period for the EUA transition guidances will supplements/amendments be allowed for modifications to the emergency use authorization devices? How do the COVID-19 transition guidances impact manufacturers with ongoing clinical studies for future EUA submissions? And in light of FDA's COVID transition guidances, does the FDA prioritize pre-market submissions? So Toby, I'll be looking to you to respond to this first four-part question.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. And yeah, we grouped those together since they sort of share a lot of aspects of the response. So as we discussed, the public health emergency under 319 will expire on May 11th and will not be renewed. The 319 and 564 declarations are independent. The 319 public health emergency expiration does not impact the 564 declarations. The EUA declarations related to COVID-19 under Section 564 of the FD&C Act will continue until the Secretary of HHS ends them. Additionally, as we've discussed and is in the transition plan guidance, we expect 180 day notice before the 564 EUA declarations are terminated. So while the 564 declaration for COVID-19 IVDs is in place, manufacturers may submit EUA requests, including supplemental EUA requests, and FDA will continue to consider them based on our previously communicated prioritization and considering the public health needs. Once the 564 declaration is terminated, we will no longer be authorized to issue EUAs, and therefore we will not continue review of any EUA requests that are under review at that time. As we've talked about, we don't have a date for the 564 declaration being terminated, and we do expect 180 days notice prior to the termination. At this point, however, rather than pursuing an EUA or a modification to an EUA, the FDA is encouraging all manufacturers to submit traditional marketing submissions, such as 510ks, de novos, and possibly PMAs, in some cases. If you have an ongoing clinical study or you're otherwise planning for a future EUA request for a COVID-19 test, we recommend that you consider how your clinical study and other validation efforts may also support a traditional marketing submission, since we are encouraging all manufacturers to pursue traditional marketing submissions. That said, marketing submissions, including 510ks and de novos, are not prioritized in the same way that EUA requests have been. We do aim to review marketing submissions according to the timelines established under the Medical Device User Fee Amendment or MDUFA program. Generally 510k applicants can expect submission acceptance review decisions within 15 calendar days, substantive review decisions within 60 days, and final decisions within 90 days. And those days are calculated as what we refer to as FDA days, so days under FDA review, not including any days where the submission might be placed on hold due to a request for additional information from the applicant.

Joseph Tartal (FDA):
OK. Thank you, Toby, for that information and clarify and ordering out a lot of good information in a nice logical order. So with that, we'll get to our next question, which is, how does the public health emergency termination on May 11th impact LDTs, laboratory developed tests? Can I offer my LDT point of care COVID-19 test after May 11th in alignment with the general enforcement discretion policy for LDTs outside of an EUA declaration? Toby, I'm going to send this question to you.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. I'm not sure why we had point of care in that question. I'll just clarify that most LDTs are not point of care. But for LDTs in general, FDA has generally exercised enforcement discretion, as we've talked about, meaning that we don't exercise our authority to enforce regulatory requirements for LDTs, although we do have that authority. We don't apply the general enforcement discretion approach to certain LDTs, as I mentioned in the slides, including those used for declared emergencies under 564. As we've mentioned, the 319 and 564 are independent. The EUA declaration under 564 is continuing, and we expect that 180-day notice before it is terminated. Therefore, even after the PHE, the Public Health Emergency, termination on May 11th, the EUA declaration for COVID-19 IVDs is still in effect, including the EUA requirements for COVID-19 tests, and that does apply for LDTs. This will continue to help assure that COVID-19 tests remain appropriately accurate and reliable, including in the setting of new variants and sub-variants that we continue to see with COVID-19. Following termination of the EUA declaration, that's the 564 declaration, which we don't have a date yet for that termination, so that 564 declaration for COVID-19 IVDs, once that is terminated, we do intend to have the same enforcement approach for COVID-19 LDTs as we do for other LDTs.

Joseph Tartal (FDA):
OK, thank you for that comprehensive response. With that, we'll go to our next question. Due to a high prevalence of low positive samples in the clinical study cohort for EUA requests for COVID- 19 antigen tests, many sponsors have used a control low positive analysis, where the analysis is stratified the positive percent agreement, PPA, of the investigational device by different percentages of low positive samples, such as 10% and 20%, in the sponsor's clinical study cohort. Can a low positive analysis such as this be used to support a traditional marketing submission such as a 510k. Kris, I'm going to turn that question over to you.

Kris Roth (FDA):
OK, great. Thank you, Joe. So our recommendations to support a traditional marketing submission are different from our recommendations to support an EUA. And at this time, we don't intend to use this type of low positive analysis to support traditional marketing authorizations. Generally, we would expect robust overall performance observed in a prospective clinical study for COVID-19 antigen tests seeking traditional marketing authorization, with a minimum PPA of 80% and a lower bounds of the 95%, confidence interval of 70%. The special controls that such tests must meet are outlined in the FDA's recently granted de novo, and that's de novo number DEN220039. And this de novo was from the Quidel Corporation for the Sofia 2 SARS Antigen plus FIA. The low positive analysis used during the EUA authorization for some tests was based on a variety of factors that were kind of unique to the pandemic. This included high prevalence of reported COVID-19 cases, the viral load of the circulating variants at that time, and the frequent use of serial testing or otherwise repeated regular testing, such as workplace or school testing programs. This all led to a determination that the benefits of wide availability of OTC COVID-19 tests outweighed the potential risks of lower sensitivity. As these factors have now largely shifted with lower prevalence of reported COVID-19 cases, as well as reduced testing, FDA's recommendations for traditional marketing authorization do not include the use of a low positive analysis.


---


# 3,898  _context-commentary_regulatory-fda-townhalls.md
METADATA
last updated: 2026-03-02 RT
file_name: _context-commentary_regulatory-fda-townhalls.md
category: regulatory
subcategory: fda-townhalls
words: 3032
tokens: 3898


CONTENT

## Context
This subcategory contains processed transcripts from approximately 100 FDA Virtual Town Hall meetings for COVID-19 diagnostic test developers, spanning from March 2020 through early 2023. The FDA held these meetings approximately every two weeks, with each session typically lasting about an hour. The town halls served as a direct engagement channel between the FDA and the diagnostic test development community during the pandemic, covering topics including Emergency Use Authorization (EUA) submissions, test validation requirements, regulatory updates, and policy changes.

The archive contains two processed file types for each town hall session: `section-titles` files (organized by agenda and topic sections) and `qa-qonly` files (extracted question-and-answer pairs only). The source transcripts were downloaded from the FDA website in PDF format. Processing involved significant variability in cleaning requirements, particularly around standardizing speaker names and formatting across sessions. The question-and-answer extraction represented a substantial separate effort, producing the structured QA pairs that form the foundation of the QRAG knowledge base described below.

#### QRAG Application
QRAG (Question Retrieval Augmented Generation) is a specialized AI retrieval tool that FloodLAMP developed and applied to this corpus of FDA Town Hall transcripts. A live demo is available at:
https://www.focusonfoundations.org/fda-town-halls-qrag-demo

QRAG was developed in late 2023, which is a long time ago in the context of AI development. Current state-of-the-art reasoning systems may achieve comparable results via a system prompt that requests the closest quotations alongside a synthesis from a large corpus of files. However, the QRAG approach may still be faster and more cost-effective for this type of RAG/structured retrieval task.

#### QRAG Explainer
The QRAG system is designed for "serious contexts of use" where authoritative, source-attributed answers are needed. It provides responses by leveraging a pre-processed, curated knowledge base of question-answer (QA) pairs. Key characteristics include:

- **Structured QA Processing**: Utilizes pre-processed QA blocks with metadata for efficient retrieval.
- **Pre-Processed QA Content**: Uses structured QA pairs that can be authority-vetted, enabling high-quality retrieval and responses.
- **Question-Based Vector Search**: Employs embeddings of questions for accurate matching.
- **Intelligent Response Routing**: Routes queries based on question match quality to appropriate LLM prompts.
- **Transparent Source Attribution**: Distinguishes between quoted and AI-generated content.

## Commentary
The FDA's decision to hold regular town halls for diagnostic test developers during the pandemic represented a valuable form of direct engagement with the regulated community. However, the volume and nature of questions from serious test developers across these sessions reveals a persistent information and clarity gap in FDA communication around diagnostic test authorization. Addressing that gap with AI has enormous potential to enable progress in the diagnostics space.

**Why QRAG — the case for authority-quoted retrieval**
The core motivation for the QRAG tool was to avoid full reliance on AI-generated answers for a subject as consequential as FDA diagnostic regulatory policy. Hallucination rates in large language models have decreased substantially since this work began in 2023, but for regulatory questions where precision matters, users benefit from seeing the authority directly quoted — what the FDA actually said — either before or alongside any AI-generated synthesis. This makes the output more reliable and more verifiable. A practical approach for using QRAG is to increase the number of returned chunks (direct quotations) to 20 or even 50, save the results as a markdown file, and then load that file into the user's own AI tool for deeper analysis, particularly if the user has access to extended-reasoning models through a pro-level subscription.

**FDA refusal to answer questions: an unexamined pattern**
One analysis that would be worthwhile but has not been performed is a systematic examination of the FDA's refusal to answer questions during these town halls. The FDA routinely declined to respond to questions about specific submissions, using standard language to that effect. While there is a legitimate basis for this position, many of the questions came from test developers seeking to understand the status or outcome of their own submissions. There are concerns that this standard refusal was also used to avoid addressing questions that touched on areas of potential inconsistency, lack of clarity, or unresolved policy problems. Developers regularly raised straightforward questions, such as why they had not received a review response after months of waiting. There has been important work on both reducing review timelines and increasing transparency around these processes, and the new FDA leadership appears to be moving in that direction.

**Transparency and the case for publishing rejection letters**
FDA Commissioner Marty Makary, in a January 2025 interview on the All-In Podcast, stated:

> "We've got to challenge these deeply held assumptions. And we're doing it. We are doing it with new programs, new priority reviews, new pilots, new forms of transparency. We made our rejection letters public so that if the FDA does not approve a drug, the public deserves to know why. And it creates accountability. And that was not the case before. They talked about it for 30 years and we got it done."

This remark was made in the context of drug approvals, but the principle applies equally to diagnostics. When a diagnostic test developer submits an EUA application, the expectation is that the submission is complete and ready for authorization. The FDA also offers a pre-submission question process (or pre-EUA process) for obtaining feedback on incomplete work. Once the formal submission is made, if the FDA authorizes it, the submission becomes public. There is a strong argument that rejected submissions and the FDA's stated reasons for rejection should also be made public. Given that the submitter has represented the application as ready for authorization, transparency from that point forward could lead to faster processing, greater consistency, higher quality submissions, and greater encouragement of innovation.

**FDA's internal use of AI**
A companion report in this subcategory (`_AI_FDA_Internal_AI_Use_Report.md`) examines the FDA's early adoption of internal generative AI tools, including the "Elsa" platform and the 2025 AI-assisted scientific review pilot. As of that report's date, there has been limited public progress in the direction of the standardization and transparency measures discussed above. The stated capabilities of Elsa (accelerating clinical protocol reviews, shortening scientific evaluations, summarizing adverse events, performing label comparisons) suggest operational efficiency gains, but no center-specific SOPs or workflow changes have been published. These internal AI developments are worth monitoring, as they could eventually affect review workflows, consistency, and processing times for diagnostic submissions.

**Analysis of FDA refusals to answer: an AI-enabled demonstration**
As a demonstration of AI-enabled use of this FDA Townhall set of files, a comprehensive analysis was conducted and is documented in a separate companion file in this subcategory: `_AI_FDA_Townhall_Analysis_of_Refusals_and_Legitimacy.md`.

That document contains:
- A critical analysis of the FDA's standard "we are not able to respond to questions about specific submissions" language, including its effect on transparency, accountability, and the structural silencing of the regulated community.
- A legitimacy rubric with classification categories and a 1–5 scoring system for evaluating whether individual refusal instances were justified.
- Classification and scoring of all 116 identified refusal instances across 84 of the 100 town hall transcript files (51 boilerplate opening disclaimers and 65 active in-session refusals).
- Summary statistics and interpretation of results.

The raw extraction of refusal passages is compiled in a separate file: `_compilation_fda-refusals-to-answer.md`.

It is important to note that this analysis was produced as a rapid, AI-assisted demonstration. The critical essay in Section 1 of the analysis document was authored through voice-dictated prompts to Claude Opus 4.6 (via Cursor's agentic coding mode), with the author providing the arguments, framing, and specific factual claims, and the model producing the written text. The classification and scoring of the 116 refusal instances was performed by Python code that the model generated and executed — using regex pattern matching and heuristic classification, not through carefully engineered structured-output prompts applied with a frontier reasoning model. As a result, the compilation of raw refusal passages likely has significant problems and errors, but the legitimacy classifications and numerical scores should be treated as merely a placeholder and demonstration of the potential of fully automated AI analysis. The methodology disclaimer in the analysis document itself provides more detail.

This work did not use the QA extraction files or the QRAG retrieval tool — it was performed directly against the `section-titles` transcript files. It demonstrates what is potentially possible with AI and well-cleaned transcripts, even through informal voice-prompted interaction with an agentic model. A more rigorous approach would involve developing a structured-output prompt (with fields for category, score, rationale, and supporting excerpt), tuning and evaluating that prompt against a human-scored sample, running it with a high-quality frontier reasoning model across all identified instances, and performing human evaluation of the results. That level of rigor is achievable with current tools and would produce a substantially more reliable analysis — but the rapid demonstration here is sufficient to illustrate the patterns and motivate the effort.

The python code to implement the rigorous, non-agentic version of this AI-analysis is available in the open-source repo here https://github.com/FocusOnFoundationsNonprofit/public-corpus-tools. This code base was created and partially funded by the Balvi grant received by FloodLAMP to open-source and publish it's work from the pandemic. In particular, 2 python modules fileops.py and llm.py contain code to 1) process text/markdown files, and 2) run llm prompts over them (both normal prompts and function calls/structured output prompts). With the advances in AI coding since this codebase was developed in 2023, these modules could likely get created now in a few minutes or even maybe seconds in one shot with a short voice dictated prompt. The capability offered by these modules is basically a superpower. It means that anyone — a journalist, a researcher, an advocacy group, a congressional staffer — can take a large body of public records like these 100 town hall transcripts, apply a sophisticated and objective analytical framework to the entire corpus, and produce results that would have taken a team of analysts months to compile, for almost nothing in time and cost. And those results can be used to discover and expose problems — from severe structural failures to quiet inefficiencies — in the operation of agencies, institutions, and bureaucracies. And then, crucially, to develop and advocate for specific, actionable reforms. Not vague calls for "more transparency" but concrete proposals grounded in evidence extracted from the institution's own public record. That is what this analysis attempts to demonstrate, and that is what the open-source tools in this repository are designed to enable.


## Follow-Up Questions

### Context Questions
1. **Were there specific town hall sessions or time periods that were particularly information-rich or that marked significant FDA policy shifts?** (Score: 4)
   Highlighting key sessions would help users prioritize their exploration and strengthen the archive's utility as a navigational reference.

2. **What are the known limitations of the processed transcripts — e.g., speaker misattributions, gaps from poor PDF quality, or sessions that could not be fully processed?** (Score: 4)
   Documenting limitations is important for an archive designed to be used with AI tools, where source quality directly affects output quality.

3. **How did the format, content, and attendance of the town halls evolve over the pandemic timeline — e.g., did participation drop off, did topics shift from EUA mechanics to post-pandemic policy?** (Score: 3)
   The evolution of these meetings may reflect broader shifts in the FDA-developer relationship and pandemic response priorities, which would add narrative depth to the context.

4. **How many total QA pairs were extracted across the ~100 town hall transcripts, and what was the distribution over time?** (Score: 3)
   Quantitative details would add specificity to the archive description and help users understand the scale and density of the corpus.

5. **What specific challenges arose during the QA extraction process, and how were edge cases handled (e.g., multi-part questions, questions with no clear FDA response)?** (Score: 2)
   Understanding the extraction methodology would help future users and researchers assess the quality and completeness of the QRAG knowledge base.

### Commentary Questions
1. **Can you provide specific examples of questions that the FDA refused to answer where the refusal seemed to avoid substantive issues rather than protect submission-specific confidentiality?** (Score: 5)
   Concrete examples would significantly strengthen the commentary's central argument about transparency gaps and give future researchers specific threads to follow.
_A: Okay, so I did a big analysis and thread on this and it produced another, the output of that was another document. This is here. Well, I'm going to include it in this in this context window here. Well, actually this is the same thread. I thought I started a new thread, but I didn't. So, well then this should be more straightforward. Yeah, I am going to drag back in the this file though. So what I want you to do is just include it here above. Well, I mean, put it at the end of the process commentary. That's where it should go. And you're going to reference this document and just give a short kind of explainer on what it is. And then what I want you to also do is add a disclaimer to the AI FDA Town Hall Analysis of Refusals and Legitimacy file, because I've only really briefly scanned the classification and I don't have high confidence in them overall. I think some are spot on, but I think some could be really off and just mistakes. And I don't, I'm even confused about the excerpts and how those were pulled and generated. Now, I don't want to redo this whole thing because it's, I'm out of time on dealing with this and I got to move on to the next important area, which is our submissions in the Open EUA concept. So what I think what I'd like to do here is I think really this is, this is look at this as a demonstration of what's potentially possible, you know, with AI and these clean transcripts and note that this was not using the QA extraction or the QRAG tool. And what I want to say is that, you know, how, what would ideally be done here? And this is almost like a technical aside, but I do want to include this because this is pretty important. You know, what would you, what, what I think you would do to do this properly or more thoroughly would be to develop a prompt and it would be a, you know, function call or structured output prompt, you know, with the, you know, the category, the score, the rationale, etc. And then, you know, tune and evaluate that prompt and use that with, you know, one of the high reasoning, high quality, you know, frontier reasoning models, you know, perhaps comparing a few of them and doing, you know, human evaluation of this rubric application and scoring. And then, and then run that in a loop, you know, using code across all of the identified refusals. I think probably the compilation of refusals is pretty good. I'm not sure about that. I did as I scan those, they looked pretty good. But Again, I have a lot less confidence in the legitimacy analysis and kind of numerical scoring and classification there. So it's important to say how this was done. I mean, this was done through very quick voice prompts to Opus 4.6 max within cursor. And so this is the power of the new agentic models is that they should be able to do something like what I described just automatically where they're applying, developing and applying prompts iteratively or sequentially across corpuses or bodies of text, compiling those results, doing these evaluations. And in the end, just delivering you the high quality output that has the consistency that is impossible with single base model calls at all, or even just the reasoning models of a couple of months ago, or just say of 2025. But I'm not sure these systems are actually there yet. I'm not sure that they are doing what I described, which is developing the prompts as structured output prompts iteratively and consistently applying them. I think they are developing and writing code behind the scenes that you don't even see and then running those in a sandbox against the files. And that's all that all seems to be, I mean, that is happening. So again, couch this as an unaudited demo, which very likely contains a significant fraction of errors in the application of the rubric and the legitimacy score for all of these instances. Okay, I think that's enough. That should be good._

2. **How does FloodLAMP's own experience as a test developer submitting to the FDA connect to the patterns observed in these town halls?** (Score: 5)
   FloodLAMP's firsthand experience with the EUA process would add direct credibility and specificity to the commentary. This is the kind of material only the founder can provide, and it connects this subcategory to the fl-fda-correspondence and open-euas subcategories.

3. **What is your assessment of whether the current FDA leadership's transparency reforms (e.g., publishing rejection letters) will meaningfully reach the diagnostics/IVD space, given that the initial focus appears to be on drugs?** (Score: 4)
   The founder's informed opinion on whether drug-side reforms will extend to diagnostics is directly relevant to the archive's regulatory collection and to users in that space.

4. **Are there specific connections between patterns in these town hall Q&As and FloodLAMP's experience documented in other archive subcategories (e.g., fl-fda-correspondence, open-euas, ldts)?** (Score: 4)
   Cross-referencing across subcategories would strengthen the archive as an interconnected resource and help users see how the town halls relate to the broader regulatory story.

5. **Were there specific QRAG queries or use patterns during development that revealed unexpected insights about the town hall corpus?** (Score: 3)
   Discovery stories from building the tool could illustrate its value more concretely than a feature description alone, and could serve as examples for users exploring the QRAG demo.

6. **Has anyone tested a modern reasoning model (e.g., o1, Claude with extended thinking) against the same queries to compare with QRAG's retrieval approach? What is your honest assessment of QRAG's ongoing utility?** (Score: 3)
   An honest comparison would be valuable for the archive's credibility and would help users decide whether to use QRAG or load the transcripts directly into their own AI tool.
