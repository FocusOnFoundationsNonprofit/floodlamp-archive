METADATA
last updated: 2026-02-26 RT
file_name: _context-commentary_regulatory-fda-euas.md
category: regulatory
subcategory: fda-euas
words: 502
tokens: 725


CONTENT

## Context
An Emergency Use Authorization (EUA) is a mechanism through which the FDA can authorize the use of unapproved medical products — or unapproved uses of approved products — during a declared public health emergency. During the COVID-19 pandemic, EUAs were the primary pathway by which diagnostic tests reached the market. The EUA process differs from the standard FDA authorization pathways (510(k), PMA, De Novo) in several key respects:

- **Speed**: EUAs are designed for rapid review during emergencies, with timelines measured in weeks rather than months or years
- **Evidence threshold**: EUAs require the FDA to determine that the product "may be effective" based on available evidence, a lower bar than the "reasonable assurance of safety and effectiveness" required for standard authorizations
- **Temporary status**: EUAs are valid only for the duration of the declared emergency and can be revised or revoked
- **Conditions of authorization**: EUA-holders must meet ongoing conditions, including labeling requirements, adverse event reporting, and sometimes performance monitoring

Each EUA includes an Instructions for Use (IFU) document that specifies the authorized specimen types, testing procedures, performance characteristics, interpretation criteria, and conditions of authorization. Some EUAs also include an EUA Summary providing the FDA's review of the submission data.

This subcategory contains a selection of EUA documents that were relevant to FloodLAMP's work — not a comprehensive collection of COVID-19 diagnostic EUAs (of which there were hundreds). The files here were included because FloodLAMP reviewed them during development, because they represent comparable technologies (particularly LAMP-based or isothermal assays), or because they illustrate specific aspects of the EUA landscape. The collection includes IFUs and EUA summaries from tests spanning RT-PCR, isothermal amplification, CRISPR-based detection, and home collection kits.

Two files merit specific mention:

- **Detectachem MobileDetect-BIO BCC19 Test Kit** — This was the EUA most similar to what FloodLAMP was developing: a colorimetric LAMP-based SARS-CoV-2 test designed for point-of-care use. FloodLAMP's assays appeared to achieve significantly higher sensitivity and overall performance than the Detectachem test based on the published performance data.
- **SalivaDirect** (documented primarily in the open-euas subcategory) — Notable as the first and essentially only "open" EUA, meaning the protocol was made freely available for other labs to adopt. The open-euas subcategory covers this in detail.

The CDC's own RT-PCR Diagnostic Panel IFU is also included as a reference document — it was the original FDA-authorized COVID-19 test in the United States and provides a baseline example of an EUA IFU at the highest complexity level.

For broader analysis and commentary on the FDA's EUA process during the pandemic, see the reg-articles-misc subcategory, which includes articles and reports examining how the process functioned. For FloodLAMP's own FDA submissions and correspondence, see the fl-fda-submissions and fl-fda-correspondence subcategories.

Also see the following file, which is an AI generated report sourcing retrospectives on FDA EUAs during the COVID-19 pandemic.
regulatory/reg-articles-misc/_AI_fda-eua-covid-retrospectives_post2022_report.md


## Commentary
See other regulatory subcategories for commentary. FloodLAMP's assessments and lessons learned regarding the EUA process are addressed there where they can be grounded in specific documents and experiences.


# 1,795  _context-commentary_regulatory-fda-policy.md
METADATA
last updated: 2026-03-01 RT
file_name: _context-commentary_regulatory-fda-policy.md
category: regulatory
subcategory: fda-policy
words: 1160
tokens: 1795


CONTENT

## Context
This subcategory contains 47 documents spanning 2020–2023 that trace the evolution of FDA's regulatory policy for COVID-19 diagnostic testing. The collection includes seven versions of FDA's overarching COVID test policy guidance, EUA letters and amendment letters, review templates (molecular, antigen, home-use, pooling), fact sheet templates, FDA press announcements, and transition planning documents. Together they form a detailed record of how FDA managed the regulatory environment for COVID-19 tests from the earliest emergency through the end of the Public Health Emergency.
This collection is not complete and are mostly the documents that we downloaded and reviewed at FloodLAMP. There are almost certainly other important documents that are not included here.

#### AI Summary of FDA Policy
Below is an AI (ChatGPT 5.2 Pro and Claude Opus 4.6) generated summary, which may contain errors.

The FDA policy COVID-19 testing policy evolved through three broad phases:

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

Three policy innovations are specifically documented in this subcategory:

##### Serial screening (Mar 2021 onward)
FDA authorized screening claims based on strong symptomatic performance combined with a repeat-testing regimen, rather than requiring standalone evidence in asymptomatic populations. This treated the testing algorithm and frequency as part of the risk-control package. By Nov 2022, serial testing instructions were standardized into enforceable antigen test labeling (two tests over three days if symptomatic; three tests over five days if asymptomatic, at least 48 hours apart). Key archive files include:
- `2021-03-16_FDA Website - FDA takes steps to streamline path for COVID-19 screening tools.md`
- `2021-03-16_FDA Template - Supplemental Template for Developers...for Screening with Serial Testing.md`
- `2021-03-13_FDA Fact Sheet - Screening for COVID-19 Deciding Which Test to Use When Establishing Testing Programs.md`
- `2021-10-25_FDA Template - Supplemental Template for Developers...for Screening with Serial Testing.md` (updated version)
- `2022-11-01_FDA Letter - Repeat Testing Revision Letter.md`
- `2022-11-01_FDA Website - Antigen EUA Revisions for Serial Repeat Testing.md`
- `2022-11-17_FDA Website - At Home COVID-19 Antigen Tests-Take Steps.md`

##### Asymptomatic/screening testing (Jul 2020 onward)
FDA distinguished between testing asymptomatic individuals under clinical "suspicion" (provider judgment) and broad population screening (no symptoms, no known exposure). The Jul 24, 2020 LabCorp reissuance was the first EUA explicitly authorizing screening of people without known or suspected infection, establishing screening as a distinct intended use with its own evidence and labeling requirements. Key archive files include:
- `2020-08-24_FDA Policy IVD - Pooled Sample Testing and Screening Testing for COVID-19.md`
- `2021-03-13_FDA Fact Sheet - Screening for COVID-19 Deciding Which Test to Use When Establishing Testing Programs.md`
- `2020-10-26_FDA Template - Antigen Template for Test Developers.md`
- `2021-10-06_FDA Template - For Developers of Molecular Diagnostic Tests.md`

##### Pooled testing (Jul 2020 onward)
FDA authorized sample pooling to conserve reagents and increase throughput, but constrained it through validation requirements (replicate detection thresholds, Ct shift limits, invalid-rate caps), restriction to CLIA high-complexity labs, and behavioral controls (reflex individual testing for positive/invalid pools, specific fact-sheet language). The Apr 20, 2021 amendment letter tied pooled screening specifically to serial testing programs operating at least weekly, treating serial frequency as a mitigation for the sensitivity loss inherent in pooling. FDA distinguished swab pooling from media pooling and provided different validation pathways for each. Key archive files include:
- `2020-08-24_FDA Policy IVD - Pooled Sample Testing and Screening Testing for COVID-19.md`
- `2021-04-20_FDA Letter - Amendment Letter.md`
- `2021-04-20_FDA Website - Pooling and Serial Testing Amendment.md`
- `2021-04-20_FDA Fact Sheet - Sample Updated Fact Sheet for Health Care Providers.md`
- `2021-04-20_FDA Fact Sheet - Sample Updated Fact Sheet for Patients.md`

An important distinction throughout the archive is between FDA's two regulatory levers: **EUA issuance** (test-specific, enforceable conditions, required fact sheets) and **enforcement discretion** (FDA choosing not to enforce certain requirements for a period, with conditions). The early guidances relied heavily on enforcement discretion to expand access; later guidances progressively moved back toward requiring EUA or traditional authorization before clinical use.

Related subcategories include `regulatory/open-euas` (the open EUA submissions FloodLAMP prepared), `regulatory/fda-townhalls` (a RAG demo over 100 FDA townhall transcripts for COVID-19 test developers), and `regulatory/ldts` (laboratory-developed test policy context).


## Commentary
For the primary commentary on FDA policy and the Open EUAs, see `regulatory/open-euas/_context-commentary_regulatory-open-euas.md`.

There remains a need for significant progress in FDA policy as it relates to pandemic preparedness and response. The complexity of the regulatory environment documented in this subcategory, with seven guidance versions, multiple overlapping enforcement mechanisms, and evolving intended-use distinctions, illustrates both the scale of the challenge and the difficulty of navigating it in real time as a small developer.

AI tools offer substantial potential for making this kind of dense regulatory material more accessible and navigable. As a related effort within this archive project, we built a demo RAG (Retrieval Augmented Generation) tool over a corpus of 100 FDA townhall meeting transcripts for COVID-19 diagnostic test developers (see `regulatory/fda-townhalls`). That tool takes natural language queries and returns the closest matching quoted FDA authority responses along with an AI-generated summary, demonstrating one approach to making regulatory guidance more searchable and usable. Feel free to try it at [FDA COVID-19 Diagnostics Townhalls - QRAG Demo](https://www.focusonfoundations.org/fda-town-halls-qrag-demo).


# 2,051  _context-commentary_regulatory-fl-fda-submissions.md
METADATA
last updated: 2026-03-02 RT
file_name: _context-commentary_regulatory-fl-fda-submissions.md
category: regulatory
subcategory: fl-fda-submissions
words: 1401
tokens: 2051


CONTENT

## Context
This subcategory contains FloodLAMP's FDA Emergency Use Authorization (EUA) submissions and associated Instructions for Use (IFU) documents for its SARS-CoV-2 diagnostic tests. There are 15 files spanning from November 2020 to October 2021, representing the full arc of FloodLAMP's regulatory submission effort. For background on the EUA framework itself and how it differs from standard 510(k) IVD approvals, see the FDA policy subcategory `regulatory/fda-policy`. For the correspondence with the FDA that accompanied these submissions, see `regulatory/fl-fda-correspondence`.

The subcategory documents four distinct test products and several ancillary submissions. The "QuickColor" test is the main FloodLAMP test, and one that was used for all of FloodLAMP's surveillance pilot programs. When the "FloodLAMP test" is used throughout the files in this archive, the QuickColor test is the one being referred to.

- **FloodLAMP Glass Milk LAMP Test** (Pre-EUA, November 2020): The earliest submission, a colorimetric RT-LAMP assay using silica ("glass milk") purification of nucleic acids from saliva and anterior nares swab specimens (from the Harvard Rabe-Cepko protocol). This was a pre-EUA — a preliminary package submitted to initiate FDA engagement and enter the review queue. It targeted asymptomatic screening with sample pooling at a baseline level of 10. The limit of detection (LoD) was 2 copies/uL (approximately 2,000 copies/mL).

- **FloodLAMP EasyPCR COVID-19 Test** (EUA Submission + IFU, v1.0 March 2021, v1.1 May 2021): An extraction-free, duplex RT-qPCR assay using the CDC N1 and human RNaseP primer-probe sets, with TCEP-based chemical inactivation and heat treatment. It required standard RT-PCR instruments (QuantStudio, Bio-Rad CFX96) but no nucleic acid extraction equipment. The LoD was 3,100 copies/mL. Clinical evaluation at Stanford showed 97.5% positive agreement and 100% negative agreement against a high-sensitivity comparator on 80 specimens.

- **FloodLAMP QuickColor COVID-19 Test** (EUA Submission + IFU, v1.0 March 2021, v1.1 May 2021, v1.2 draft October 2021): An extraction-free, colorimetric RT-LAMP assay with a visual pink-to-yellow readout requiring no specialized instrumentation. It used 18 LAMP primers targeting three SARS-CoV-2 genes (ORF1ab, N, E) and the same TCEP-based inactivation as the EasyPCR test. The LoD was 12,500 copies/mL. Clinical evaluation at Stanford showed 90% positive agreement and 100% negative agreement on 80 specimens. The v1.2 IFU introduced triplicate repeat procedures for inconclusive results.

- **FloodLAMP FLAMP (QuickFluor) COVID-19 Test** (EUA Submission + IFU draft, March 2021, NOT SUBMITTED): A fluorimetric RT-LAMP assay using real-time fluorescence readout on RT-PCR instruments. It used the same primers and inactivation as QuickColor but with fluorescent detection instead of colorimetric. The LoD was 50,000 copies/mL and clinical evaluation showed 80% positive agreement. This test was prepared but never submitted to the FDA.

- **Pooled Swab Collection and Screening Studies** (Pre-EUA submissions, May 2021): Three documents supporting FloodLAMP's pooling and asymptomatic screening strategy — a pre-EUA for a direct-to-consumer pooled swab collection kit (allowing 1–4 self-collected anterior nasal swabs in a single tube), collection kit instructions, and a proposed validation study design for pooling and serial asymptomatic screening aligned to FDA guidance.

Each submission follows the FDA's EUA template structure: purpose, measurand, applicant information, regulatory status, proposed intended use, device description and test principle, controls, interpretation of results, manufacturing and component sourcing, and performance evaluation (LoD, inclusivity, cross-reactivity, interfering substances, clinical evaluation). The IFU documents mirror much of this content in an operational format for laboratory use.

All of FloodLAMP's tests shared a common TCEP-based chemical inactivation step and were designed as "open source protocol" tests — meaning designated CLIA high-complexity laboratories could source all components directly from commercial vendors rather than purchasing proprietary kits. This open-source approach is central to FloodLAMP's strategy, as documented in the `regulatory/open-euas` subcategory. The EasyPCR and QuickColor tests were designed to work as an integrated pair: QuickColor for high-throughput colorimetric screening (45-minute turnaround, no instruments) and EasyPCR for rapid PCR-based confirmation (~1 hour 45 minutes). New England Biolabs supported both tests with their LAMP master mix and Luna RT-qPCR kit, and LGC Biosearch Technologies supplied production-scale LAMP primer sets.

The submissions evolved across versions. The v1.0 submissions (March 2021) proposed intended use for "individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval." The v1.1 submissions (May 2021) reframed the intended use around "routine screening programs" in settings like schools and workplaces. None of these submissions received FDA authorization.


## Commentary
The primary commentary for submissions is combined with the correspondence category — see `regulatory/fl-fda-correspondence/_context-commentary_regulatory-fl-fda-correspondence.md` regarding FloodLAMP's FDA engagement. Here are comments on the more technical aspects of the EUA submission process.

The EUA submission process involves two main types of documents: the submission itself and the Instructions for Use (IFU). The submission is the regulatory document — it follows the FDA's structured template with sections covering purpose, measurand, intended use, device description, performance evaluation, manufacturing, and so on. The IFU is the operational document intended for the laboratories that will run the test. They overlap substantially in content, but serve different audiences and purposes. Both must be prepared and aligned, and both are substantial documents. For FloodLAMP, each test's submission ran 5,000–10,000 words, and each IFU ran 7,000–14,000 words.

A critical concept in understanding these documents is that the FDA authorizes test systems, not tests in isolation. The entire system — reagents from specific vendors, validated instruments, the exact workflow, controls, and interpretation criteria — is what receives authorization. Changing a single component can require revalidation. For open-source protocol tests like FloodLAMP's, this posed an inherent tension: the whole point was to enable broad deployment using commodity components from multiple suppliers, but the regulatory framework required specificity at every level. FloodLAMP addressed this by validating multiple instruments (QuantStudio 6 Flex, QuantStudio 7 Pro, Bio-Rad CFX96) and multiple primer and probe vendors (Eurofins Genomics, IDT, LGC Biosearch) within a single submission.

The bench science for EUA validation can actually move quite fast. In a conversation with another test developer — an academic who started a company during the pandemic and did obtain an EUA — they described doing the core validation work in a weekend. The bottleneck is not the assay work itself but the surrounding logistics and documentation. For FloodLAMP, the single biggest delay was getting registered with BEI Resources to obtain the cross-reactivity reagents. The FDA requires testing against a panel of related pathogens and respiratory flora, and BEI is the primary source for those reference organisms. The registration and shipping process takes weeks, and for a small organization running lean, that waiting period was a significant constraint.

Even with the FDA's templates available, the document preparation is a heavy lift for anyone who has not done it before. FloodLAMP benefited from other groups sharing their actual EUA submission documents — these are not published, and they differ in important ways from the public-facing authorizations and IFUs that appear on the FDA website. Having real examples was helpful for understanding the level of detail and the conventions that the templates alone do not fully convey. If the FDA allowed or facilitated sharing of these submissions, for example, by simply letting developers choose to publish their submissions openly, some likely would, especially academics. This would meaningfully lower the barrier for new entrants.
Even with the FDA's templates available, the document preparation is a heavy lift for anyone who has not done it before. FloodLAMP benefited from other groups sharing their actual EUA submission documents — these are not published, and they differ in important ways from the public-facing authorizations and IFUs that appear on the FDA website. Having real examples was helpful for understanding the level of detail and the conventions that the templates alone do not fully convey. If the FDA allowed or facilitated sharing of these submissions, for example, by simply letting developers choose to publish their submissions openly, some likely would, especially academics. This would meaningfully lower the barrier for new entrants.

The new capabilities of AI could transform the document preparation burden. The EUA submission and IFU are highly structured, repetitive across test types, and draw heavily on standardized language. With progress on standardization and transparency from the FDA — such as machine-readable templates, published example submissions, and clearer guidance on what constitutes acceptable variations — AI tools could handle much of the drafting, cross-referencing, and consistency-checking that currently consumes weeks of a developer's time. The combination of AI and regulatory modernization could significantly reduce the cost and time to bring validated, innovative tests to market.


# 1,525  _context-commentary_regulatory-fl-fda-correspondence.md
METADATA
last updated: 2026-03-02 RT
file_name: _context-commentary_regulatory-fl-fda-correspondence.md
category: regulatory
subcategory: fl-fda-correspondence
words: 1021
tokens: 1525


CONTENT

## Context
This subcategory contains FloodLAMP's direct correspondence with the FDA regarding its SARS-CoV-2 diagnostic test EUA submissions, spanning from October 2020 through October 2021. The files include pre-EUA requests, emails to FDA leadership, FDA deficiency letters, meeting notes, FloodLAMP's written responses, and the deprioritization/closure letters that ended FloodLAMP's EUA pursuit. For the submission documents themselves and technical background on the EUA process, see `regulatory/fl-fda-submissions/_context-commentary_regulatory-fl-fda-submissions.md`.

During the COVID-19 pandemic, the FDA's Center for Devices and Radiological Health (CDRH) managed EUA requests for diagnostic tests through a process that evolved substantially as submission volume grew. Communication between the FDA and test developers typically occurred through a combination of formal letters (deficiency notices, final decisions), email exchanges with assigned reviewers, optional pre-EUA feedback, and periodic virtual town halls open to the broader developer community. The FDA also offered short interactive review meetings — typically 30 minutes — to discuss specific submission issues.

For developers seeking EUAs, the process began with either a pre-EUA submission (to get preliminary feedback before a full filing) or a direct EUA submission. The FDA would then triage the submission based on prioritization factors — primarily whether the test would increase testing accessibility (point-of-care, at-home) or significantly expand testing capacity (high-throughput, high-volume manufacturing). Beginning in fall 2020, the FDA formalized a deprioritization system that included two mechanisms: "Decline to Review" for low-priority submissions and "Decline to Issue" for submissions with unresolved critical deficiencies. By September 30, 2021, the FDA had declined to review 558 EUA requests for COVID-19 tests. For more on deprioritization, see the companion research report `regulatory/fl-fda-correspondence/_AI_FDA Deprioritization of COVID-19 Diagnostic EUAs.md`.

FloodLAMP's correspondence documents the full arc of engagement with the FDA: early encouragement from OIVD Director Tim Stenzel on the open-source protocol approach (December 2020), initial EUA submissions and immediate deprioritization (March–April 2021), a pre-EUA that the FDA closed without reviewing the validation data (May–June 2021), a direct appeal to FDA leadership with real-world surveillance data (October 4, 2021), a 6-deficiency letter followed by a 30-minute Zoom meeting and written response (October 13–20, 2021), and final closure one day after FloodLAMP's response (October 21, 2021). The correspondence with the FDA on FloodLAMP's open-source EUA submissions is closely connected to two other regulatory subcategories: the FDA town halls (`regulatory/fda-townhalls`) where FloodLAMP engaged FDA leadership publicly, and the open EUAs concept (`regulatory/open-euas`) that was central to FloodLAMP's regulatory strategy.


## Commentary
FloodLAMP's experience with the FDA during the COVID-19 pandemic was defined by a persistent inability to obtain meaningful regulatory engagement on submissions that, by the FDA's own stated criteria, should have warranted review. The company developed a validated, instrument-free, colorimetric RT-LAMP test at a cost of $1–2 per reaction, designed as an open-source protocol modeled on the SalivaDirect EUA. The test was adopted by EMS agencies and municipal fire departments for routine surveillance screening. Despite multiple submissions, real-world deployment data, and direct appeals to FDA leadership, FloodLAMP received blanket deprioritization along with hundreds of other test developers. Had a meaningful review, let alone an EUA, been obtained in the spring of 2021, the trajectory of the company would have been fundamentally different.

For a detailed factual reconstruction and analysis of the critical October 2021 correspondence sequence that ended FloodLAMP's EUA pursuit, see `regulatory/fl-fda-correspondence/_AI_FloodLAMP FDA October 2021 Correspondence Analysis.md`. That document covers the complete timeline from October 2020 through October 2021, the FDA's stated justifications, and multiple interpretive explanations of the FDA's rationale. For related commentary on the FDA town halls and the open EUA concept, see `regulatory/fda-townhalls/_context-commentary_regulatory-fda-townhalls.md` and `regulatory/open-euas/_context-commentary_regulatory-open-euas.md`.

The first direct interaction with the FDA set the tone for what followed. In a November 2020 phone call for the pre-EUA, the assigned reviewer had not heard of SalivaDirect, DetectaChem, or even LAMP as a technology. The reviewer strongly recommended against pursuing anything involving asymptomatic testing or pooling, and instead recommended the narrowest possible indication: a single symptomatic person suspected of COVID-19. This was the starting position from which FloodLAMP had to make its case for the open-source screening model.

The FDA's rationale for deprioritization consistently came back to being short-staffed and resource-constrained. These were real constraints. But the response to those constraints — blanket deprioritization — failed a basic policy test. At the point FloodLAMP was deprioritized, the country was more than a year into the pandemic. The question the FDA should have been asking was: "Will this decision result in less testing?" When the answer was yes, creative solutions were warranted. The FDA could have established streamlined review tracks for open-protocol tests, created batch review processes for submissions using validated primer sets, facilitated reference panels for small developers, or simply provided actionable feedback rather than closing files without reviewing the data. None of these were pursued. The ITAP (Independent Test Assessment Program) eventually emerged as a partial alternative pathway, but it had limited access and transparency.

The October 4, 2021 letter to OIVD Director Tim Stenzel stands as one of the best summaries of FloodLAMP's case for its test and its work. In that letter, FloodLAMP presented real-world surveillance data from five sites across three states, approximately 2,300 people screened in 800 pools with three unknown positives detected and no known false negatives, alongside manufacturing readiness (2 million tests on hand, 3 million more at LGC Biosearch), $1–2 per test pricing, and active commercial sites with EMS and fire departments. Stenzel never responded. The review team sent a 6-deficiency letter nine days later, offered a 30-minute Zoom call the following day, received a substantive written response on October 20, and issued a final closure on October 21. The speed of that closure, one day after FloodLAMP's response that proposed a narrowed intended use and addressed multiple deficiencies, suggests the outcome was predetermined and the interactive review seemed to be procedural rather than genuinely deliberative.

Five weeks after the FDA closed FloodLAMP's submission, the Omicron variant was reported. By January 2022, the United States experienced the worst testing shortage of the entire pandemic. The principle behind the deprioritization decision — that the country did not need more tests — was catastrophically wrong, and it was applied systematically to FloodLAMP and hundreds of other test developers.


# 1,560  _context-commentary_regulatory-irb.md
METADATA
last updated: 2026-02-28 RT
file_name: _context-commentary_regulatory-irb.md
category: regulatory
subcategory: irb
words: 1167
tokens: 1560


CONTENT

## Context
An Institutional Review Board (IRB) is an independent ethics committee that reviews and approves research involving human subjects. Any clinical study collecting specimens from human participants, including the clinical performance studies needed for FDA Emergency Use Authorization (EUA) submissions, requires IRB approval before it can begin. The IRB evaluates whether the study design adequately protects participants' rights, safety, and welfare.

This subcategory contains two files from FloodLAMP's IRB process: a clinical study protocol and an informed consent form, both dated April 2021 (Protocol 20210401). The protocol, titled "FloodLAMP COVID-19 Biobank and Test Validation Protocol," outlined a study to collect up to 100,000 consented clinical specimens across multiple U.S. sites to evaluate FloodLAMP's molecular COVID-19 assays (QuickColor RT-LAMP, QuickFluor RT-LAMP, and EasyPCR RT-qPCR) and a home collection kit. The informed consent form documented voluntary participation, specimen handling, de-identification procedures, and participant rights.

The relationship between the IRB and FDA EUA submissions is sequential rather than direct: IRB approval is a prerequisite for conducting a clinical study, and the clinical study generates the performance data that gets submitted to the FDA as part of an EUA application. The IRB itself does not appear in the EUA submission. Rather, it serves as the regulatory gatekeeper that must approve the study before clinical specimens can be collected from human participants. FloodLAMP needed clinical performance data — positive and negative percent agreement against an EUA-authorized high-sensitivity PCR comparator — to support its 2nd round of EUA submissions for pooling, asymptomatic, and the new serial screening claims. Generating that data required running a clinical study on human specimens, and running that study required IRB approval.

Note that this IRB is not related to FloodLAMP's first round of EUA submissions in March of 2021. The Stanford Clinical Lab performed the clinical study for those submissions, using banked samples.

FloodLAMP obtained IRB approval through WCG (formerly Western Institutional Review Board), a well-known commercial IRB. The protocol was broad and flexible, designed to cover three collection modalities: co-located sites adjacent to existing testing programs (such as Stanford or San Francisco city testing sites), independently operated FloodLAMP collection sites, and distributed home collection kits. The study also included provisions for the FloodLAMP Mobile App, pooled specimen collection, and multiple swab types.

Despite obtaining IRB approval and preparing a detailed protocol, FloodLAMP never executed the clinical study, due to the FDA's decision to decline further review of the FloodLAMP EUA and Pre-EUA submissions. The company later developed a more operationally integrated study design in mid-2022 that would have merged clinical data collection with an active school-based surveillance testing program (documented in the companion file `_AI_digestion_irb_new-clinical-study-design.md`), but this design also was not executed before the company ceased operations.

Other parts of the archive document the FDA submission process itself. The fl-fda-submissions and fl-fda-correspondence subcategories in the Regulatory collection contain the EUA applications and related correspondence that these IRB documents were intended to support.

The archive also includes additional IRBs, consent forms, and clinical study designs from other organizations, located in the `IRBs and Consents from Others` subfolder:
- American Cancer Society event LIABILITY WAIVER AND RELEASE OF CLAIMS.pdf
- Arizona Dept of Health Services informed consent.pdf
- Color Genomics IRB.docx
- EmpowerDX (Eurofins) consent form.docx
- Lucira Screenshot_2021-02-17 COVID-19 Test Study.png
- NextEraEnergy PCR Testing Patient Consent Form.pdf
- Stanford Catch Consent.docx
Technical note: These files are not considered primary archive files, and therefore were not converted to markdown and included in the AI-ready combined md files.


## Commentary
The IRB process was handled through WCG (Western Institutional Review Board), with a total cost of approximately $11,360 over two years including a renewal. This was a considerable expense for a small company, made more notable by the fact that the clinical study was never actually conducted. The IRB approval and the detailed protocol it covered remained unused.

The experience highlighted what appeared to be a cumbersome and inefficient process. The IRB pathway felt siloed, with limited templates, examples, or structured support available for small organizations navigating it for the first time, particularly during a public health emergency when speed should have been a priority. For a small company attempting to bring a new diagnostic test through the regulatory pathway during an active pandemic, the combination of IRB costs, the time required to prepare the protocol, and the separate expense of actually running a clinical study created significant barriers to generating the clinical data that the FDA required.

To illustrate the broader cost picture: FloodLAMP received a quote of approximately $100,000 from a clinical research organization to manage participant recruitment and sourcing alone, targeting roughly 40 positive specimens. This did not include running the tests themselves; a separate CLIA laboratory was needed for that. These costs reflected the broader pandemic dynamic, where demand for clinical services far outstripped supply and pricing reflected that imbalance.

The IRB and clinical study process, as experienced, suggests an area where standardization and streamlining could benefit the field, both in routine times and especially during public health emergencies. The barriers to generating clinical performance data disproportionately affect small companies and organizations that lack established clinical trial infrastructure, institutional IRB relationships, or the budgets to absorb six-figure study costs. If decentralized and low-cost diagnostic testing is to play a meaningful role in future pandemic response, the regulatory pathway for generating the required clinical data may need to be correspondingly accessible.

The FDA did recognize elements of this problem. Through a collaboration with the NIH, the Rapid Acceleration of Diagnostics (RADx) program established the Independent Test Assessment Program (ITAP), which provided standardized evaluation protocols, data reporting mechanisms, and targeted outreach to test developers to accelerate regulatory review and authorization. ITAP facilitated the authorization of a number of at-home and point-of-care COVID-19 tests, and the model has since been extended to other diagnostics including multiplex respiratory panels, mpox, and hepatitis. However, ITAP's COVID-19 focus was primarily on rapid antigen tests, and the program's resources and outreach were oriented toward developers with tests already authorized in other markets or at a relatively advanced stage. While ITAP likely accelerated some authorizations, it did not address the more fundamental barriers and inefficiencies of the overall EUA clinical study and IRB process, and it was not readily accessible to smaller, earlier-stage companies and organizations developing novel testing approaches. For more on FloodLAMP's engagement with RADx-related programs, see the archive files in various/fl-proposals subcategory.

Later in FloodLAMP's trajectory, around mid-2022, a new clinical study design was developed that attempted to address some of these constraints. The design integrated clinical data collection into an active school-based surveillance testing program, using an enrichment strategy to solve the low-prevalence problem and a cascading cohort structure to maximize data yield per positive event. This approach would have generated clinical performance data at a fraction of the cost of a standalone trial. The design is documented in a companion file (`_AI_digestion_irb_new-clinical-study-design.md`) and may be of interest to researchers or organizations facing similar challenges in generating clinical data for novel diagnostics during periods of variable disease prevalence.


# 947  _context-commentary_regulatory-ldts.md
METADATA
last updated: 2026-03-01 RT
file_name: _context-commentary_regulatory-ldts.md
category: regulatory
subcategory: ldts
words: 674
tokens: 947


CONTENT

## Context
The FloodLAMP test was never used as an LDT. Our pilots operated under surveillance (see archive folder regulatory/surveillance), and we submitted to the FDA for IVD EUA. We had discussions with UnitedHealth Group about a clinical lab network adopting our direct LAMP test as an LDT, shared all of our information (data, FDA submissions, cost model, etc.), but they did not move forward with the project.

As a background explainer, Laboratory-developed tests (LDTs) are in vitro diagnostic tests that are designed, manufactured, and used within a single clinical laboratory, as opposed to commercial IVD test kits produced by diagnostic manufacturers and sold to laboratories across the country. Commercial IVDs are subject to FDA premarket review under the medical device classification system, while LDTs have historically operated under FDA "enforcement discretion," meaning the agency asserted jurisdiction but generally chose not to enforce device requirements. This distinction created a bifurcated market: commercial diagnostic products held to rigorous FDA analytical and clinical validation standards, and laboratory-developed tests for the same purposes that were primarily overseen through CMS under the Clinical Laboratory Improvement Amendments (CLIA). The tension between these two regulatory tracks became a central issue during the COVID-19 pandemic and in the years that followed.

The JD Supra article by Skadden Arps attorneys (October 2020) provides a useful overview of the decades-long history of LDT regulation, tracing FDA's evolving posture from initial enforcement discretion through the 2010 public workshop, the 2014 draft guidance, the 2017 retreat to Congress, and the COVID-era policy reversals. It remains a good starting point for understanding the regulatory backdrop against which COVID-era LDT policy played out.

Two AI-generated reports in this subcategory provide more detailed analysis. The first, "FDA, LDTs, and COVID-19: Interactions, Policy Shifts, and Key Issues (2020-2023)," is a detailed synthesis of how FDA oversight of COVID-19 LDTs moved through three distinct phases: initial EUA-based enforcement discretion, the August 2020 HHS policy blocking mandatory premarket review, and FDA's restoration of an EUA-first posture after November 2021. The second, "FDA 2024 LDT Rule - Status and Legal History," covers the post-pandemic attempt by FDA to formally end broad enforcement discretion for LDTs through rulemaking, the subsequent legal challenge, the March 2025 court vacatur, and FDA's decision not to appeal, which returned LDT oversight to the pre-2024 status quo.

Related regulatory subcategories in this archive include: FDA Policy (`regulatory/fda-policy/`), which covers broader FDA regulatory actions and user fee frameworks; FDA Town Halls (`regulatory/fda-townhalls/`), which documents the weekly public calls FDA held with COVID-19 test developers; Surveillance (`regulatory/surveillance/`), which covers the surveillance testing framework under which many LDT-based programs operated; and Open EUAs (`regulatory/open-euas/`), which addresses the question of whether FDA should have made EUA pathways more accessible to LDT developers and smaller laboratories.


## Commentary
LDT regulation is deeply interconnected with FDA testing policy. As the AI report on COVID-era LDT oversight documents in detail, the FDA went back and forth during the pandemic on whether LDTs needed EUA authorization, with HHS at one point blocking mandatory premarket review entirely and FDA later restoring an EUA-first posture. Underlying these policy swings is a structural gap in the regulatory framework: there is no middle ground between laboratory-developed tests, where a single lab has broad authority to develop and use a test internally, and commercial IVDs produced by manufacturers who contract with reagent companies to produce kits sold to laboratories nationwide (or direct to consumers for at-home devices). This gap became acutely problematic during the pandemic, when the need to rapidly scale testing demanded something between the two models. A promising solution emerged in the form of the Open EUA, pioneered and authorized during the pandemic by the SalivaDirect program under Dr. Anne Wyllie, which allowed multiple laboratories to adopt and run a validated protocol under a shared authorization, overseen and managed by a responsible party (which became a nonprofit). Unfortunately, the Open EUA concept was not further developed by FDA or the field, and it remains an underexplored pathway.

For fuller commentary on LDTs, FDA policy, and Open EUAs, see `regulatory/open-euas/_context-commentary_regulatory-open-euas.md`.


# 1,190  _context-commentary_regulatory-open-euas.md
METADATA
last updated: 2026-03-02 RT
file_name: _context-commentary_regulatory-open-euas.md
category: regulatory
subcategory: open-euas
words: 864
tokens: 1190


CONTENT

## Context
This subcategory documents the concept of "open EUAs," the combination of open-source diagnostic protocols with open-access FDA authorization, which was central to FloodLAMP's regulatory strategy. For a comprehensive analysis of the concept, its history, regulatory mechanics, and implications, see the companion research report in this subcategory: `_AI_open-euas-open-access-diagnostics-report.md`.

The files here include:
- **FDA press release (Aug 15, 2020)** announcing the SalivaDirect EUA, which contains FDA's explicit use of "open source protocol" framing and describes the designated-laboratory model.
- **Anne Wyllie nomination letter (June 2022)** for the Reagan-Udall Foundation Innovation in Regulatory Science Award, written by FloodLAMP's founder, articulating the regulatory novelty of SalivaDirect's approach: an academic team seeking an IVD EUA without intending to manufacture kits, using CDC primers, fully disclosing ingredients, validating multiple suppliers and instruments, and working with FDA to create a designation process for CLIA labs.
- **Open EUA Consortium main document (late 2020)** recording FloodLAMP's attempt to convene multiple test developers around the open EUA model. The consortium aimed to build a suite of 5-8 open EUAs covering different sample types and technologies, with shared validation materials and supply chain coordination. It stalled quickly by end of 2020.

The "open EUA" concept, as analyzed in the AI report, is not merely about publishing protocols. It involves an institutional and legal pattern combining open-source protocols (fully disclosed, implementable with commodity components), open supply chains (multiple validated suppliers), and open-access authorization (multiple labs operating under one EUA through a steward/designation model). SalivaDirect remains the most prominent example in FDA's COVID-19 authorization corpus. FloodLAMP pursued the same approach for its LAMP-based tests and was unable to obtain authorization.

These files connect to the FDA correspondence subcategory (`regulatory/correspondence`), which documents FloodLAMP's direct engagement with the agency on its own open-source protocol EUA submissions, and to the FDA EUA submissions subcategory (`regulatory/fda-euas`), which contains FloodLAMP's submitted tests.


## Commentary
The open EUA concept was at the center of FloodLAMP's regulatory strategy, and we consider it one of the most important points of regulatory progress to emerge from the COVID-19 diagnostic response. The AI research report in this subcategory provides a thorough analysis; here we offer FloodLAMP's perspective.

SalivaDirect demonstrated that it was possible to build a scalable, supply-chain-resilient testing network under a single FDA authorization using commodity components and a steward/designation model. We modeled our own EUA submissions on this approach and nominated Anne Wyllie for the Reagan-Udall Foundation Innovation Award based on direct experience with the model and our assessment of its significance. The nomination letter in this subcategory lays out the case for why the open-source protocol EUA represented a genuine regulatory innovation, not just a scientific one.

The Open EUA Consortium was our attempt to scale the idea beyond a single test. We convened a small group of developers in late 2020, but the consortium stalled quickly. At one level,the reasons are well captured by the AI report's analysis: the HHS policy change in August 2020 reduced the regulatory incentive for open EUAs (labs could offer LDTs without an EUA), the stewardship burden was significant, and funding was not available to sustain the coordination effort. At another level, trying to coordinate this group was like herding cats. FloodLAMP founder, Randy True, decided it was just going to be easier to pursue the EUAs independently, so we validated and submitted three related tests, Colorimetric LAMP, Fluorimetric LAMP, and the Direct PCR from the same inactivated sample. The plan was to then either help other groups in the gLAMP community get their EUAs or collaborate with them to do under the FloodLAMP organization. In hindsight, this was quite overconfident.

FloodLAMP submitted multiple open-source protocol EUAs and was unable to obtain authorization, or to get meaningful engagement from FDA on these submissions (see `regulatory/correspondence`). The structural barriers identified in the AI report were real and material. The most striking is the asymmetry between government and non-government entities: the CDC was able to produce a test that any CLIA high-complexity lab in the country could run, simply by distributing reagents. No stewardship model, no lab-by-lab designation. When an academic lab (Yale/SalivaDirect) created something comparably open, the regulatory system required a full stewardship and designation infrastructure. When a small public benefit company (FloodLAMP) attempted the same, the barrier was even higher.

The AI report's analysis of the CDC test's Appendix A, the extraction-free protocol restricted to public health labs only despite being developed in response to a nationwide reagent shortage affecting all labs, captures a pattern we observed repeatedly: technical solutions existed but were constrained by institutional caution and regulatory framing rather than by scientific or safety considerations.

The "generics of diagnostics" framing from the nomination letter remains, in our assessment, directionally correct. The U.S. diagnostic regulatory system lacks a routine mechanism for deploying validated open protocols to competent laboratories without each lab filing its own submission or depending on a single steward's capacity. SalivaDirect showed one way to approximate this during an emergency. Whether the model can be institutionalized for future outbreaks is an open question, but the design patterns in the AI report, particularly the four-layer taxonomy of openness and the practical framework for future open-access diagnostics, may be a useful starting point.


# 649  _context-commentary_regulatory-reg-articles-misc.md
METADATA
last updated: 2026-03-01 RT
file_name: _context-commentary_regulatory-reg-articles-misc.md
category: regulatory
subcategory: reg-articles-misc
words: 430
tokens: 649


CONTENT

## Context
This subcategory collects a small number of higher-level reports and assessments related to FDA oversight of COVID-19 diagnostics. Unlike other regulatory subcategories in the archive that focus on specific FloodLAMP interactions with the FDA (submissions, correspondence, townhalls), these files are third-party or government-produced documents that provide broader perspective on the EUA process and diagnostic test validation during the pandemic.

The three documents are:

- **Booz Allen Hamilton Independent EUA Assessment** (`2021-10-08_FDA Report - EUA Assessment by Booze Allen.md`): An FDA-commissioned review of CDRH's COVID-19 test EUA response, covering how the FDA used templates, guidance updates, triage, and deprioritization to manage thousands of submissions. It includes priority recommendations around IT systems, staffing models, and a validation framework for future emergencies. This report predates the Omicron surge and the severe testing shortages that followed.
- **FDA's Work to Combat the COVID-19 Pandemic** (`2022-07-01_FDA Report - FDAs Work to Combat the COVID-19 Pandemic.md`): A broad FDA overview summarizing cross-center actions on vaccines, therapeutics, diagnostics, supply chain, inspections, and regulatory science, with data current as of April 2022.
- **Phillips and Dinakar Proposal** (`2021-01-18_Phillips and Dinakar - A Proposal for Increasing the Speed of Validating SARS-CoV-2 Diagnostic Tests.md`): A paper proposing three extensions to the EUA process for accelerating diagnostic test validation: structured (machine-readable) EUA data submissions, distributed FDA-directed CLIA-led validation, and building an open synthetic patient clinical specimen panel.

In addition, an AI-generated research report (`_AI_fda-eua-covid-retrospectives_post2022_report.md`) was created during archive preparation to identify post-2022 retrospectives, evaluations, and criticisms of the FDA's EUA process. That report catalogs sources from government oversight agencies (HHS OIG, GAO, FDA), legislative bodies, NGOs, professional associations, and academics, and may serve as a starting point for readers interested in pursuing the broader literature on EUA reform and pandemic preparedness policy.


## Commentary
TThe Phillips and Dinakar proposal for structured, machine-readable EUA data submissions resonated with FloodLAMP's own experience navigating the EUA process. The idea that submissions could be standardized in a way that accelerates FDA review, reduces ambiguity for developers, and enables computational analysis of submission data is the kind of practical, systems-level reform that would likely have compounding benefits across future emergencies.

More broadly, the potential for AI to improve FDA processes around diagnostic test evaluation, guidance development, and emergency response has been a recurring theme throughout this archive (see commentary on the FDA townhalls subcategory and the open-EUAs subcategory). The scale and complexity of the COVID-19 testing response — thousands of EUA submissions, rapidly evolving guidance, variant-driven obsolescence — represent exactly the kind of problem where AI-assisted workflows could meaningfully reduce friction and improve outcomes.


# 1,749  _context-commentary_regulatory-surveillance.md
METADATA
last updated: 2026-03-01 RT
file_name: _context-commentary_regulatory-surveillance.md
category: regulatory
subcategory: surveillance
words: 1301
tokens: 1749


CONTENT

## Context
#### Testing Types: Diagnostic, Screening, and Surveillance
During the COVID-19 pandemic, U.S. testing was categorized into three overlapping purposes:

- **Diagnostic testing**: Testing an individual when there is reason to suspect infection (symptoms or known exposure). Results are returned to the individual and their healthcare provider. The test must be FDA-authorized and performed in a CLIA-certified laboratory.
- **Screening testing**: Testing an individual without symptoms or known exposure, with the intent of making individual decisions based on results (e.g., return to school or work). Like diagnostic testing, screening requires FDA-authorized tests and CLIA-certified labs, and results are returned to individuals.
- **Surveillance testing**: Population-level monitoring, often but not always using de-identified specimens. Results are not returned to individuals and are not used for individual decision-making. Surveillance testing does not require FDA authorization or CLIA certification.

The critical practical distinction: if a test result is used to make a decision about a specific person, regulators generally treated it as screening or diagnostic.

#### Clarification: "Surveillance" in This Archive
Throughout this subcategory and elsewhere in the FloodLAMP archive, "surveillance" refers to non-diagnostic, non-clinical testing programs designed to detect and limit the spread of COVID-19 in schools, workplaces, and communities. It does not refer to wastewater surveillance or genomic variant surveillance, both of which are distinct modalities covered in the AI-generated report referenced below. The absence of a clear regulatory category and standardized terminology for this type of frequent, pandemic stop-the-spread testing is itself a significant gap in pandemic preparedness and response frameworks. There is no good name for it and no established regulatory pathway — an unsolved problem that affected programs like FloodLAMP throughout the pandemic.

#### Key Documents in This Subcategory
For the authoritative regulatory definitions, two government documents provide the clearest framing:

- **FDA "COVID-19 Test Uses: FAQs on Testing for SARS-CoV-2" (updated 2023-09-29)** — The FDA's post-crisis summary of diagnostic, screening, and surveillance definitions, including examples and CLIA/setting requirements.
- **CDC "Testing Strategies for SARS-CoV-2" (updated 2021-12-28)** — Includes a summary matrix comparing the three testing strategies across settings, reporting requirements, and whether results may be returned to individuals.

FloodLAMP's own framing of how it operated under surveillance guidance is documented in:

- **FloodLAMP Surveillance FAQ and Links (June 2022 DRAFT)** — Contrasts diagnostic and surveillance testing, cites CMS/FDA guidance, and explains FloodLAMP's compliance posture. Includes FAQ-style responses prepared for the Coral Springs pilot program.
- **FloodLAMP Surveillance Information (Aug 2021 INTERNAL)** — A detailed internal memo on the regulatory framing for pooled non-diagnostic surveillance, including CMS enforcement discretion citations, an exchange between NIH Director Francis Collins and CMS Administrator Seema Verma on referral pathways, and the eCFR research-lab exemption.

Two outside analyses by professionals that were shared with us are also included:

- **Memo — Surveillance Authority Plain-language Research (Jan 2021 from Senior Medical Director in Healthcare Industry)** — A plain-language digest of FDA/CMS surveillance framing and the conditions under which presumptive positives may be routed to CLIA confirmatory testing.
- **Memo — USA Surveillance Strategy (Sept 2021 from non-FloodLAMP Healthcare Attorney)** — Guidance confirming that surveillance testing is generally not regulated when de-identified and no individual results are returned, and recommending coordination with local public health officials.

For a comprehensive treatment of the surveillance testing regulatory landscape during COVID-19 — including the Seattle Flu Study/SCAN case study, school-based surveillance controversies (SafeGuard/New Trier), and the post-PHE transition to wastewater and genomic surveillance — see the AI-generated report: `_AI_Covid_Surveillance_Testing_Screening_Report.md`.


## Commentary
#### Navigating the Surveillance Framework
Surveillance testing was a regulatory gray area, and operating FloodLAMP's testing programs under this framework was a significant challenge. At the same time, the surveillance designation provided meaningful flexibility.

#### Communicating Results Without Giving "Results"
The central operational challenge was adhering to the requirement that surveillance programs not deliver "individual patient results." FloodLAMP's approach was to take the FDA's and CMS's language literally: when a sample indicated the presence of SARS-CoV-2, participants were told only that they were "referred to follow-up clinical testing." FloodLAMP did not tell participants they were positive or negative, and the company emphasized this distinction and terminology with program administrators.

This approach was informed by what happened at other programs. The CMS notice letter in this archive (December 2020) was sent to surveillance program operators instructing them to stop using the language "results of potential clinical significance." It was FloodLAMP's understanding, received secondhand, that this terminology had been adopted by operators attempting to comply while still communicating something to participants. In practice, everyone involved — operators, participants, and regulators — likely understood that phrasing to mean the surveillance test was positive. FloodLAMP chose to use the FDA's language, and a "referral to follow-up (clinical) testing", along with the explanation that we were not allowed to give "positive/negative" results to individual participants. The resulting communication was initially confusing for participants and program admins, but after a few repetitions they then understood. This kind of linguistic dance does not serve the public interest during a pandemic.

#### The Fundamental Regulatory Gap
The core problem was that the FDA did not distinguish between two very different kinds of "individual decisions." On one hand, there are clinical medical decisions: using a test result as a diagnosis and relying on it for treatment. On the other hand, there are public health mitigation decisions such as going home from school/work, and isolating from family members, and getting a follow-up diagnostic test. In FloodLAMP's programs, the individual actions triggered by surveillance were of the second kind — participants went home, isolated, and in nearly all cases obtained confirmatory clinical testing (antigen, PCR, or both).

A better framework for pandemic screening would require that public health screening programs mandate follow-up confirmatory testing for flagged participants and that participants report those results back to the program. This would serve two purposes: providing the comparison data needed to evaluate the screening program's performance, and codifying the principle that screening test results should not be the basis for medical decisions.

#### The Coral Springs Experience
The uncertain regulatory status of surveillance nearly prevented FloodLAMP's first major program from proceeding. The Coral Springs pilot covered municipal staff and first responders in a city of approximately 140,000 people and represented FloodLAMP's first significant commercial engagement. The city attorney raised concerns requiring due diligence on the surveillance framework. FloodLAMP was not fully informed of the internal discussions but provided supporting documentation, such as that in the "FloodLAMP Surveillance FAQ and Links" file. The matter reportedly came to a head in a meeting involving city officials, the medical director, regulators (apparently from both FDA and CMS), and at least one elected representative (state or federal level). The outcome was a "green light" for the program, though FloodLAMP never received written confirmation of this decision. (For more on the Coral Springs pilot, see the `pilots/pilot-data` subcategory.)

#### Surveillance as a Fallback
Operating under the surveillance framework was not FloodLAMP's first choice — it was a fallback. The company had submitted its test to the FDA for Emergency Use Authorization and had applied to the RADx program, but could not secure authorization, engagement, or even substantive attention through either channel. The opportunity to operate surveillance programs came about through our contact with EMS leadership and the FTFC conference in South Florida in mid 2021, where we offered pooled testing and made a presentation. One of the key executives at FloodLAMP had prior experience with surveillance and relationships with other operators of surveillance programs. That combined with the pull we were getting from the EMS community, who simply needed better, more effective testing/screening for their critical first responders, led us to do the FloodLAMP surveillance "pilot programs". These programs were very effective for the organizations that implemented them.

The primary commentary on FloodLAMP's regulatory experience, including EUA submissions and FDA correspondence, is in the `regulatory/open-euas` subcategory.

# ===== END OF FILE _archive-combined-context-commentary_regulatory_13k.md =====
