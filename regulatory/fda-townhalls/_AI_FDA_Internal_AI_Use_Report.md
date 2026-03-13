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
