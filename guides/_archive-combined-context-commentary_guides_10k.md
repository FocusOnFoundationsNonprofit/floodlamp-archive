METADATA
last updated: 2026-04-03_083523
file_name: _archive-combined-context-commentary_guides_10k.md
category: guides
subcategory: NA
words: 7034
tokens: 10275


CONTENT

# _archive-combined-context-commentary_guides_10k (8 files, 10,275 tokens)

# 1,882  _context-commentary_guides-manufacturing.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-manufacturing.md
category: guides
subcategory: manufacturing
gfile_url: https://docs.google.com/document/d/1RvVKQlXvqdQK0zOlwJVCPwtqUeBTmEM5KROt_0pPW5I
words: 1318
tokens: 1882


CONTENT

## Context
The `guides/manufacturing` subcategory contains the Standard Operating Procedures (SOPs) and process flow diagrams that represent FloodLAMP's most mature approach to producing its two key reagents: the Primer-Guanidine Solution (PGS48) and the 100X Inactivation Solution (100XIS).

PGS48 is the Primer-Guanidine Solution formulated for 48 reactions. It combines LAMP primer sets (As1e, N2, E1) with guanidine hydrochloride and nuclease-free water. The resulting solution is mixed with NEB's colorimetric LAMP master mix to form the reaction mix for the QuickColor LAMP test. The "48" refers to the standardized batch size of 48 reactions, tuned to FloodLAMP's typical customer usage patterns of 20–100+ reactions per session.

100XIS is the 100X (one hundred times concentration) Inactivation Solution, a TCEP-based formulation combining TCEP, EDTA, and NaOH. When diluted to 1X Inactivation Saline Solution and added to dry swabs, it extracts and protects the RNA for downstream testing upon heating. Both reagent formulations are straight from the Rabe-Cepko protocol.

The subcategory includes five files:

- `Assay and Reagent Manufacturing Diagrams` — A 19-slide presentation containing process flow diagrams for all key reagent manufacturing and assay workflows, covering PGS batching, 100XIS manufacturing, primer preparation, positive control aliquoting, and assay setup at various reaction scales (24, 48, and 96 reactions).
- `SOP-201-A_2 PGS48 Manufacturing - Run Form` — Step-by-step manufacturing procedure for PGS48, including primer resuspension, guanidine-HCl mixing, and robotic aliquoting on an OpenTrons liquid handler.
- `SOP-202-A_1 100XIS Manufacturing - Run Form` — Manufacturing procedure for 100XIS, covering TCEP weighing, component mixing in a 1L glass bottle, and aliquoting into 5 mL vials for storage at -20°C.
- `SOP-301 PGS48 Verification - Run Form` — Quality verification procedure for PGS48 batches via CLAMP amplification with positive and negative controls, including a plate layout map for tracking results by lot number.
- `SOP-302 100XIS Verification - Run Form` — Quality verification procedure for 100XIS batches via CLAMP amplification.

The term "manufacturing" is used loosely here. FloodLAMP's production was small-scale pilot manufacturing — a small team working in a shared lab space at MBC BioLabs in San Carlos, California, without the infrastructure or experience typical of industrial reagent manufacturing. The team included a PhD scientist who developed the initial batch records and then these SOPs, which represented the most controlled and streamlined versions of the processes FloodLAMP achieved.

These SOPs were preceded by a less formal system of batch records. The transition to SOPs was substantially but not fully complete by early 2022 (January–February), with the PGS48 and 100XIS procedures being the primary ones formalized. The PGS48 manufacturing process used an OpenTrons liquid handling robot for aliquoting, along with custom 3D-printed tube holders.

Over its operating period, FloodLAMP produced approximately 100,000 reactions worth of PGS and 150,000–200,000 samples worth of 100X Inactivation Solution. The PGS48 process yielded 3,264 reactions per lot (68 tubes at 550 µL each) and could produce roughly 10,000 reactions per hour once setup was complete, though setup time was significant. The 100XIS was produced in much larger lots — approximately 108,000 reactions per lot (216 five-mL tubes), achievable in a few hours with setup time dominating the run.

No formal stability study was conducted on PGS, as it was stored frozen and once thawed, used immediately to make the reaction mix. The more pressing stability concern was the reaction mix itself: when sites stored pre-made reaction mix, the deep pink color of the colorimetric LAMP reaction would sometimes fade or turn orange. FloodLAMP recommended against storing pre-made reaction mix when possible, and if stored frozen, to verify the deep pink color before use (and discard it if faded). A cursory stability study was performed on the 1X Inactivation Saline Solution (1XISS) using PCR as the endpoint, measuring over a period of two weeks. No significant loss of signal was observed, so two weeks was specified as the usage window for 1XISS.

These documents connect to other parts of the archive: the reagents produced here were shipped to FloodLAMP's pilot program customers (documented in the `Pilots` category), and the testing protocols that use these reagents are covered in other `Guides` subcategories.

### Archive Files Not Converted to Markdown
`2022-01-13 1X ISS Stability Study.xlsx` - 14-day stability study of the 1X Inactivation Saline Solution, using spiked Zeptometrix positive control run on PCR. Ct was stable with < 1 variation across 6 timepoints.


## Commentary
These SOPs and the reagent formulations they document were among the most important operational work at FloodLAMP. They represented a significant step in simplifying and standardizing the reagent production process. The Primer-Guanidine Solution, in particular, was a meaningful improvement — premixing the primers with guanidine hydrochloride eliminated a preparation step for the end user, and we and others confirmed through testing that this premixing did not result in significant assay performance degradation. We also put considerable thought into the volumes and tube sizes to minimize waste while providing enough reagent for a typical testing session of 20 to several hundred reactions.

The OpenTrons robot was used for PGS48 aliquoting, and we had custom 3D-printed tube holders to support the workflow. In hindsight, the robotic aliquoting was overkill for the volumes we actually produced. We over-indexed on process improvements at a time when the bottleneck was elsewhere. We couldn't scale the rest of our operations (ordering, logistics, customer support) to match the demand during the Omicron surge in late 2021 and early 2022. We had on the order of half a million reactions worth of primers on hand. The process control was a step in the right direction, but the investment in automation and even this modest scale of manufacturing wasn't justified in the end by our actual needs.

For FloodLAMP, the bottleneck during the Omicron surge was not reagent manufacturing itself but the overall kit and supplies preparation, shipment, tracking, and coordination. The system involved over 100 parts, many requiring qualification and preparation. Preparing, delivering, and supporting the complete testing systems was a large burden for a small team. The process didn't fully mature until FloodLAMP's last pilot (Abrome, in mid 2022), where a cart-and-drawers system worked well. Beyond the physical logistics, the digital side — apps, data tracking, troubleshooting — was a constant challenge with significant downtime and outages.

That said, the formulation work itself — consolidating into PGS, tuning the volumes, and standardizing at 48 reactions — was genuinely valuable. That's the endpoint worth preserving from what we did here.

The broader lesson that may be valuable for others is about the reagent supply chain. Small organizations like FloodLAMP should not be manufacturing their own reagents if there's any way to avoid it. What's needed is for reagent manufacturers, the actual producers of the master mixes, oligo probes, and positive control materials, to produce low-cost, high-volume formulations that are ready-to-use, and to thus support the most widely used open protocols. This has to go hand in hand with establishing the open EUA protocols and rights of reference so that multiple parties can legally use and distribute these reagents to run validated, consensus testing protocols.

A useful model here is SalivaDirect, which contracted with Eurofins to produce commercially available SalivaDirect kits, which were available for general order and not restricted to clinical labs designated under SalivaDirect's open EUA. When we ordered those kits, they arrived next day, were well formulated, and a relatively inexperienced lab tech was able to run the protocol successfully on a PCR machine. That combination — simplified protocol, commercially manufactured reagents, fast shipping — is what decentralized testing needs. Having individual labs or small companies mix their own reagents is a dead end for scale.

FloodLAMP was aiming for a similar commercial supply relationship (with LGC Biosearch who supplied our large scale production run of the Rabe-Cepko primers), but due to the lack of an EUA and regulatory limbo of surveillance (see the `Regulatory` category of the archive), we did not achieve that goal. Hence this internal work on scaling and standardizing our reagent manufacturing.


# 1,221  _context-commentary_guides-operations.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-operations.md
category: guides
subcategory: operations
gfile_url: https://docs.google.com/document/d/19NJD2EwFLjyhDDMETNjV7k65W30j8rWeACroz8truo0
words: 930
tokens: 1221


CONTENT

## Context
The `guides/operations` subcategory contains three files addressing the organizational and logistical underpinnings of FloodLAMP's testing programs. Unlike the test-site subcategory, which houses the protocols, setup guides, and training materials that front-line test administrators and staff used, these files capture the higher-level planning: what the economics looked like, what inventory was required, and what primers needed to be ordered.

The `Cost Model - FloodLAMP` is a working spreadsheet that modeled cost-of-goods-sold at various production scales. It reflects the iterative process of understanding what decentralized LAMP-based testing would actually cost, tracking the relative weight of each cost driver — from the dominant NEB LAMP master mix down to individual consumables and labor. Multiple versions were produced as the operation evolved; this represents one of the more mature iterations.

The `Inventory Dashboard - FloodLAMP (Updated Aug 2022)` was a practical tracking tool for cataloging everything from pipettes and heat blocks to biohazard bags and collection swabs. It gives a concrete picture of the material complexity involved in running FloodLAMP's pop-up lab model. This involved dozens of distinct items spanning reagents, consumables, equipment, lab supplies, collection materials, and training kits. FloodLAMP also used Airtable and other systems for inventory management; the dashboard here is one view of a broader operations/logistics effort.

The `LAMP Primers UPDATED 12-17-2020` document specifies the primer sets (derived from the Rabe–Cepko protocol) used for FloodLAMP's SARS-CoV-2 assay, along with ordering and handling specifications. Primer procurement was a key operational step, comprising sourcing HPLC-purified primers at the required quantities and concentrations. This document captures the standardized ordering information that supported that process.

For readers wanting to explore the actual cost breakdowns, inventory details, or primer sequences, the source spreadsheets are included in the archive and may be used for AI-assisted exploration.

### Archive Files Not Converted to Markdown
`GUIDE PCR INSTRUMENT_Using Quant Studio 7 Pro w_ Cloud Connect` - manual for the Applied Biosystems PCR machine we used at MBC Biolabs.

## Commentary
The operational and supply chain challenges were among the most persistent day-to-day problems we faced. Ideally, we would have contracted with a major distributor — Fisher Scientific, USA Scientific, or similar — to handle the full kitting of our lab supplies. In practice, that was not realistic for FloodLAMP given our volumes and lack of an EUA. No single supplier carried everything we needed, and given our unusual model of deploying pop-up labs in non-laboratory settings with non-laboratory staff, the selection of specific supplies and labware was deliberate. Some items could be substituted without issue, but others would create downstream problems if swapped. We eventually settled on a good set of materials, but the way we managed kitting and distribution was fundamentally not scalable. The scalability problem came from several converging factors: our small organizational size, operational inexperience, lack of established supplier partnerships, and the persistent iteration of kit compositions as the assay and protocols evolved. A more scalable approach would have combined top-down and bottom-up elements — standardized kit specifications and equipment bundles that established suppliers could assemble and ship, paired with clear documentation of acceptable substitutions and flexibility ranges so that smaller labs and pop-up operations could also source and validate their own combinations. 

An area of note was the sample (swab) collection tube and barcoding process. Early on, we had interns and TaskRabbits manually applying barcode labels to collection tubes — a tedious, labor-intensive task. We then sourced custom QR-coded tubes from a Chinese manufacturer (Jable), which was a major improvement, but not achieved until Q1 2022. Also, the minimum order quantity was large and the lead time stretched to several months. During those waiting periods, we still had workers coming in to manually barcode tubes by hand for days at a time.

The swab and collection tube situation was another significant challenge. Like most testing operations during the pandemic, we had difficulty sourcing swabs. But our specific problem was harder than most: we needed a swab with a breakpoint that would leave the remaining tip and shaft fitting inside a reasonably sized tube, and would accommodate 4 swab tips for pooling. We settled on a 5mL tube as our main collection vessel (the mini system used 1.5mL tubes) and tried many tube-and-swab combinations before finding one that worked. The swab we ultimately adopted was, of all things, a urethral swab. We ended up ordering 100,000 swabs and tubes from Jable. We even hired a consultant to tackle the swab sourcing problem, but that effort didn't produce useful results.

For NEB's colorimetric LAMP master mix — by far our largest single cost item — we arranged for NEB to drop-ship directly to test sites for larger orders, which significantly streamlined logistics.

The core lesson from our operational experience is: simplify relentlessly. Every part that can be eliminated reduces cost, training burden, and failure modes. Every standard, off-the-shelf item you can use in place of something custom reduces lead times and sourcing risk. For heating, we found that water baths, dry heat blocks, and even repurposed PCR machines all served as workable heaters. Flexibility in equipment selection was critical given our resource-constrained deployments.

On the economics side, the NEB master mix dominated our reagent costs and we had limited leverage on pricing even at higher volumes. This was the key reagent of the test and NEB was a great company overall to work with. The cost model in the archive gives the full picture, and our per-person cost with pooling was competitive for the time. Future effort to bring LAMP-based screening to large scale would likely involve substantial attention to the enzyme cost dependency.


# 818  _context-commentary_guides-qms-sops.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-qms-sops.md
category: guides
subcategory: qms-sops
gfile_url: https://docs.google.com/document/d/1S2HbDM9dEC4xZ4GBZoF9V0LBe0gpqWat_mO1szrpR6c
words: 585
tokens: 818


CONTENT

## Context
The `guides/qms-sops` subcategory contains seven files that comprise FloodLAMP's formal Quality Management System standard operating procedures for its colorimetric LAMP-based COVID-19 surveillance testing operations. These SOPs were designed as practical, field-ready documents. Most were printed and kept in folders or clipboard containers at testing sites for staff to reference and fill out during routine testing.

The collection covers the full testing workflow: reagent preparation (`SOP-101-A_2 1X Inactivation Saline Solution Prep - Table Form`, `SOP-102-A_2 Reaction Mix Prep - Table Form`), the core amplification assay procedure (`SOP-103-A_1 Amplification - Run Form`), training protocols for new operators (`SOP-104-A_1 Test Training - Run Form`), quick-reference visual aids (`SOP-105-A_1 QuickColor Test Diagrams` and `SOP-105-B_1 QuickColor Test Signage`), and logistics (`SOP-030-A_1 Shipping - Run Form`).

The `SOP-103-A_1 Amplification - Run Form` served as the central operational document — the form staff completed for each testing run, which was then scanned to create the Run Form Report (RFR) and entered into a Google Form for record-keeping. The training run form (SOP-104) is the most detailed document in the collection, walking new operators through the complete workflow with specific contamination-control procedures, handling rules, and timing requirements.

Each SOP follows a consistent format with document numbers, effective dates, versioning, and write-in fields for traceability, including lot numbers, reagent IDs, operator names, and timestamps. This structure reflected FloodLAMP's approach to maintaining quality documentation while operating under surveillance testing guidance rather than FDA-authorized clinical use.

Related materials can be found in the `guides/test-training` subcategory (additional training documentation), the `guides/test-validation` subcategory (assay validation work), and the `guides/operations` subcategory (broader operational workflows and site management).


## Commentary
These SOPs originated from templates provided by a quality systems consultant. We considered adopting Greenlight Guru, a common quality management software package used in the medical device and diagnostics industry, and worked with a consultant who supported its implementation. Ultimately, I think we wisely decided it was not needed given our size, as it would have been overkill for a small operation like ours.

There were primarily two reasons for building a formal QMS. The first was the practical need to understand and control changes to our protocols and files, since we were distributing them to multiple pilot sites. The second was that we applied multiple times for FDA authorization — a process that extended into October 2021, when we received what was our last denial and closure of our submissions. The IRB work and QMS formalization in 2021 were undertaken with the plan of continuing to pursue FDA authorization.

The forms themselves were generally effective in practice. They served their purpose, and we were happy with where they ended up. Most sites used them without complaint or negative feedback. Having the full set of SOPs in place prior to the initial training at a pilot site was helpful. Sites that started with the forms adopted them readily, whereas sites that were already operating when the forms were developed were more reluctant to incorporate them, though there is uncertainty about this. One part of the Amplification Run Form that was not frequently used was the lookup map on the second page. These were infrequently used overall and some pilot sites, like Abrome, put participant initials rather than tube IDs into that form. A tool that would have been particularly useful, and this cross-references to the `guides/software` subcategory, was a way to intake tubes and register their position in the custom tube racks at the same time. This is discussed further in the software subcategory context and commentary (`guides/software/_context-commentary_guides-software.md`).


# 890  _context-commentary_guides-sds.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-sds.md
category: guides
subcategory: sds
gfile_url: https://docs.google.com/document/d/1f_35t2FdLmr_YW9GzeCFGwbkYhDrwaaQlZh6EvDdUY0
words: 642
tokens: 890


CONTENT

## Context
The `guides/sds` subcategory within the Guides collection contains Safety Data Sheets for the key chemicals used in FloodLAMP's LAMP-based COVID-19 testing workflow, along with an original analysis document addressing waste disposal and risk assessment.

The five SDS files cover the chemicals central to FloodLAMP's reagent system:
- `SDS - TCEP` (tris(2-carboxyethyl)phosphine hydrochloride) — the reducing agent used in the Inactivation Saline Solution for viral inactivation; classified as a corrosive solid
- `SDS - EDTA` (ethylenediaminetetraacetic acid) — the chelating agent also used in the Inactivation Saline Solution; relatively low hazard at working concentrations
- `SDS - Clorox Bleach Regular` (sodium hypochlorite 5–10%) — used for decontamination and cleaning at test sites; corrosive with aquatic toxicity concerns
- `SDS - Isopropyl Alcohol 70 percent` — used for surface disinfection; a Class 3 flammable liquid
- `SDS - Twist Synthetic SARS-CoV-2 RNA Control Rev7 001038v7` — the non-hazardous synthetic RNA positive control used in test verification

These SDS files were maintained as a convenient reference for FloodLAMP personnel and pilot site operators, providing standardized hazard, handling, PPE, and disposal information for the chemicals they encountered during testing operations.

The sixth file in the subcategory, `_AI_Waste Disposal and Risk Assessment` is an original analysis created by AI during archive preparation. It addresses questions that were operationally important during FloodLAMP's active period: whether the used and unused reagents constituted hazardous waste under federal RCRA and state regulations (California, Florida, and Texas), how pilot sites should have disposed of the two primary waste streams (inactivated sample tubes and spent reaction tubes), and what the regulatory landscape looked like for both the chemical and biological components of the waste. The document also reviews a qualitative biological risk assessment that FloodLAMP commissioned in 2022 and a use-FMEA (uFMEA) document (both files omitted from archive due to confidentiality commitments) that FloodLAMP began developing to obtain the numerical risk quantification the narrative assessment lacked. These disposal and risk questions connect to the `guides/manufacturing` subcategory (where the reagent formulations are defined) and to the `guides/qms-sops`subcategory (where the related SOPs reside).


## Commentary
The substantive commentary for this subcategory lives in the "_AI_Waste Disposal and Risk Assessment.md" file, which documents the analysis that we wish we had done more rigorously during FloodLAMP's active period. The core issue was consequential: we needed to better understand how our reagents and testing waste were classified with respect to hazards and risk, and how pilot sites in three different states should dispose of them. We had a PhD bioscientist research the question multiple times, and the conclusion — that the working-concentration solutions were not hazardous waste — turns out to be substantially correct from a chemical standpoint. But the full picture is more nuanced than we appreciated at the time, particularly around the concentrated 100X Inactivation Solution (which likely qualifies as D002 corrosive hazardous waste due to NaOH concentration) and the biological waste classification question, which is governed by state medical waste regulations rather than RCRA.

The lesson to take from this now is about the value of AI-assisted research tools for these kinds of regulatory and technical questions. All of that earlier research was done pre-AI, without a written record of the reasoning. During archive preparation, we were able to use AI to produce the detailed, chemical-by-chemical analysis with specific regulatory citations that we would have liked to have had during FloodLAMP's operation. For any future decentralized testing operation, we recommend a documented waste determination memo for each site — something that maps each waste stream to the applicable federal and state regulations and reaches an explicit disposal recommendation. AI tools make this kind of thorough, multi-jurisdictional regulatory research dramatically more accessible, even for a small company without in-house experts. That is a genuine advancement for the field as the barrier to getting these operational safety and compliance questions properly answered has dropped significantly.


# 972  _context-commentary_guides-software.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-software.md
category: guides
subcategory: software
gfile_url: https://docs.google.com/document/d/1GBp-i-VoHRHfNx5H8Ck0CrKHxXDbRMTeJhxnf9_wddo
words: 778
tokens: 972


CONTENT

## Context
The `guides/software` subcategory contains three files documenting the FloodLAMP mobile app and admin web portal. These describe the custom software system FloodLAMP developed to manage its decentralized pooled surveillance testing programs.

FloodLAMP built its app on Appivo, a low-code development platform, with the majority of custom code written in JavaScript. The system had 3 main interfaces serving different user roles: 1) a participant-facing mobile app for onboarding, consent, and sample collection registration; 2) a staff-facing mobile app view for sample intake, processing, and resulting; and 3) an admin web portal for program management, user administration, and data export.

The files in this subcategory include step-by-step guides for the admin web portal and the staff mobile app workflow, as well as instructions for adding minors to household accounts — a feature specific to FloodLAMP's household pooling model. Together, they document the software's role in managing the end-to-end testing workflow: from participant registration and consent, through sample collection and accessioning, to processing, resulting, and notification. Related operational procedures and test site logistics are covered in the `guides/operations` and `guides/test-site` subcategories.


## Commentary
The world of software development has changed fundamentally since we built this system, and it's continuing to change very quickly. With AI-assisted coding now widely available, how a small company would go about developing custom software today is completely different from our circumstances in 2020 to 2022. We think the primary value of our software work for the archive lies not in the technical implementation, but in the specific features and user flows we designed — particularly those tailored to self-collected household pooling, which was central to FloodLAMP's approach. Even these should be reconsidered from scratch given current and potential future AI capabilities.

The FloodLAMP app was a critical part of our overall offering, managing everything from participant onboarding and consent to sample tracking and result notification. That said, at least one site (Davie) ran a substantial screening program of hundreds of samples per week entirely without the app, tracking everything manually. So while the software was important, it was not strictly required to operate one of our programs.

Most of the features and user flows are described in the files themselves, but one worth highlighting here is the "notes" field we added to the collection step. During a collection, the sponsor, the person scanning the sample tube and entering which participants contributed swabs to a pooled tube, could use this field to add someone on the fly who was not registered in the program. This obviously introduced potential issues: that person may not have consented, their name might be misspelled, and it brought non-registered individuals into the system and data. But we thought the flexibility was more important and worth the tradeoff. The notes field was widely used in practice for both non-registered participants and when there were glitches in the app. Ideally, this flexibility would be paired with post-processing software that could reconcile any unrecognized names added on the fly.

We learned about software development the hard way. FloodLAMP never had any software engineers on staff, and relied almost entirely on our partner Appivo (the low-code platform). The FloodLAMP app grew to be quite complex for the Appivo platform at the time, and there were substantial problems on both sides, due to our inexperience with software development, our limited budget, and also due to problems with the platform itself. The interaction effects between our app and the Appivo platform created periods of instability, outages, and downtime during critical operational periods, along with persistent bugs. For FloodLAMP, being a small biotech company, the software work was often the bottleneck in our operations and a persistent source of serious problems. 

One particular challenge worth noting was getting the app approved for the Apple App Store. Apparently because of Apple's heightened scrutiny around health and COVID-related apps, we were rejected multiple times through the standard review process. It ultimately required reaching out to a high-level contact at Apple, a connection made through a COVID testing group call. Without that personal connection, we may not have been able to get the app approved at all. This is an area where there is room for meaningful progress in pandemic preparedness: platform companies like Apple should have expedited review pathways and dedicated attention for pandemic-related applications, rather than subjecting them to impersonal, blanket denials, and no pathways to resolution or even timely engagement.

One area of software work we planned but never implemented was integrating the program's initial guidance (customized per site), sign-up, consenting, and registration directly into the app itself, so that the entire onboarding flow could be handled in a single streamlined experience rather than across separate systems.


# 1,149  _context-commentary_guides-test-site.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-test-site.md
category: guides
subcategory: test-site
gfile_url: https://docs.google.com/document/d/1qcNxrpc_XY34lGFBFofGKz6CVd_kkMWCL7A1Gkq2UxY
words: 842
tokens: 1149


CONTENT

## Context
The `guides/test-site` subcategory contains 16 documents that collectively address the operational side of running FloodLAMP surveillance testing at deployment sites. These files served the people responsible for day-to-day test execution—site administrators, testing staff, and in some cases individuals filling both roles.

There was never a single comprehensive operational manual. FloodLAMP's deployments varied significantly in scale and setting, from municipal programs testing fire and first responder staff in cities like Coral Springs and Davie, Florida, to small school-based programs with limited testing volumes, such as Needham, MA. This variation made a one-size-fits-all document impractical, and the materials in this subcategory reflect that: they are a collection of targeted documents, each addressing a specific aspect of site operations.

The files fall into several functional groupings:

- **Site checklists** — Daily testing procedures, weekly maintenance tasks, and ongoing readiness standards, customized for specific sites (Abrome, Alpine, Portola). These were the core operational documents that staff used each testing day.
- **Setup and logistics** — Facilities requirements, equipment receiving instructions (drop ship template), and the assay cart drawer arrangement guide, which standardized how supplies were organized in the four-drawer rolling carts used at some sites.
- **Specimen handling and testing workflows** — Collection kit assembly instructions, the resulting decision charts (both tabular and flow chart formats) defining how to interpret test outcomes through triplicate re-run logic, and decontamination procedures at three severity levels (light, moderate, and heavy).
- **Participant- and family-facing materials** — Consent forms, a school program information flyer template for families explaining how pooled surveillance testing worked, collection guides for participants, and app quick-start guides for sponsors and participants.
- **Results communication** — Guidelines for staff on how to communicate outcomes within the regulatory constraints of non-diagnostic surveillance testing, including templates for notifying sponsors and organizations about positive or inconclusive pools.
- **Best practices** — A do's and don'ts checklist (from the Kent Camp deployment) capturing practical lab handling habits to reduce contamination risk and prevent sample mix-ups.

The backup collection form (a Google Form for the Abrome site) served as a fallback for registering samples when the FloodLAMP mobile app was unavailable.

Several of these documents connect to other parts of the archive. The reagent preparation SOPs referenced in the site checklists are found in the `guides/manufacturing` subcategory. The test training materials referenced in the Abrome checklist are in `guides/test-training`. The consent language and surveillance framing tie directly to the regulatory materials in `regulatory/surveillance` and the IRB documentation in `regulatory/irb`. Additionally, the archive file `various/fl-presentations/Bend Pilot Program Bring-up (12-01-2021)` is relevant as a bring-up guide.

### Archive Files Not Converted to Markdown
`Collection Kit pamphlet 4-13-22.pdf`
`Collection Workflow Slides.pdf`
`Collection Workflow Slides.pptx`
`Nose Swab Animation.gif`
`QuickColor Test Diagrams.pptx`
`Signage Clean and Dirty.pdf`
`Signage Clean and Dirty.pptx`
`Signage Collection Kit Bins and Dropboxes.pdf`
`Signage Collection Kit Bins and Dropboxes.pptx`
`Signage Deployments v5 - QMS SOP-105-B_1.pdf`
`Signage Deployments v5 - QMS SOP-105-B_1.pptx`

## Commentary
These files represent the documents we were most satisfied with and that proved most useful in practice. We had many more operational documents over the course of the project, but what's included here are the ones we think others are most likely to be interested in.

The move to the assay cart drawer arrangement was one of the more impactful operational improvements. Before that, sites kept supplies in bins, or bags on shelves. The four-drawer plastic cart was a significant upgrade. It was easy to clean and keep clean (key for a molecular lab test), the size was right, and having a standardized layout for what went in each drawer made our job and that of the on-site tester easier. For initial site setups, we shipped labeled bags with the contents pre-sorted by drawer, which helped with coordination, training, and standardization across sites.

The fact that there's no single comprehensive operational manual reflects the reality of our deployments. The programs were quite different from each other. A municipal program testing hundreds of first responders in South Florida operates very differently from a small school-based program in Texas. A universal guide would have been either too generic to be useful or too complex to maintain. The site-specific checklists worked reasonably well in practice. They were customized to each location's workflow, intake logistics, and communication channels (typically Slack), and they gave testing staff a concrete, step-by-step reference for every testing day. However, this variety made support and maintenance a huge challenge and barrier to scaling for FloodLAMP.

The communications guidelines addressed a real constraint of operating under surveillance testing guidance. We could not give participants individual diagnostic results. The language in that document was carefully developed to refer participants for follow-up diagnostic testing without technically crossing that line. It's a good example of how regulatory framing shaped day-to-day operations in ways that wouldn't be obvious from the outside. Some of these documents were adapted from others used for surveillance testing, rather than drafted de novo by FloodLAMP attorneys. We very much appreciate others in the space who shared their documents openly during the pandemic. These were crucial for us at FloodLAMP.


# 1,106  _context-commentary_guides-test-training.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-test-training.md
category: guides
subcategory: test-training
gfile_url: https://docs.google.com/document/d/1S6h3QfU0HthWXZA25EH2U3mSBIDrGBNYfm5-2X3MyrU
words: 844
tokens: 1106


CONTENT

## Context
The `guides/test-training` subcategory contains materials from FloodLAMP's structured, video-based training program for its QuickColor COVID-19 test. The program was designed to enable new operators, including non-laboratory personnel such as firefighters, to learn the full testing workflow independently, including safety and contamination control through sample processing, amplification, and result logging.

The training system used Moodle Cloud as the learning management platform, with EdPuzzle integrated for interactive video content. An administrative guide `CRTT Moodle and EdPuzzle Guide` documented how to manage the platform, including user enrollment, course setup, content creation, activity completion settings, course copying, and learner reporting. The concept for the training program originated with FloodLAMP and was developed with a consulting firm specializing in educational curriculum development.

A series of 17 training videos were produced covering the complete testing workflow. The transcripts, preserved in the archive file `Test Training Video Transcripts`, address: introductory orientation; safety and PPE; contamination protocols for RNase, positive control, sample cross-contamination, and amplicon handling; each procedural step from 1X inactivation solution preparation through the inactivation step, reaction mix preparation, thawing, adding samples to reactions, intaking samples via the FloodLAMP app, resulting, and run logging. Scale-up procedures for larger batches including dispensing and water bath inactivation; and appendices on lab setup, pipette cleaning, and dispenser operation. The videos were narrated walkthroughs filmed in working lab environments, often with real-time interaction between the trainer and site personnel. The companion file `Test Training Video Index` provides a compact index to the 17 videos with durations and links to the main FloodLAMP webpage, downloadable video archive, Vimeo pages, and YouTube versions.

The `Certification Run Assessment v1.1` provided a formal pass/fail checklist for evaluating new operators by reviewing a recorded test run. The assessment covered PPE and safety compliance, contamination control practices and common infractions, documentation, and correct execution of each procedural step from inactivation through app-based tube handling, with an optional module for plate-scale testing. The assessment was designed for self-grading. The expectation was that the trainee would typically go through several iterations on running the test and reviewing the checklist, identifying their own mistakes. Then only when the trainee checked all the boxes in the latest assessment would FloodLAMP personnel review the records. This was set up to be scalable, being self-driven by the trainee and then only require about 30 minutes of FloodLAMP staff time for certification.

In practice, only a small number of operators completed the video-based training program. FloodLAMP's pilot sites generally preferred in-person training from experienced FloodLAMP testing staff, and the program saw limited adoption relative to the investment required to produce it. The training content itself, however, documents the full testing workflow in considerable procedural detail and provides a record of how a decentralized molecular test was taught to non-laboratory personnel.

These materials connect to the operational guides in the `guides/test-site` subcategory, which cover site setup and deployment logistics, and to the `pilots/pilot-sites` subcategory, which documents the individual pilot programs where the training was (or was not) used.

### Archive Files Not Converted to Markdown
`FloodLAMP Rapid Test Training - Storyboard.pdf`
`FloodLamp Rapid Test Training - Storyboard.pptx`
`QuickColor LAMP Trainee Tracking List SPREADSHEET.xlsx`

## Commentary
The video-based training program was overly ambitious for the scale at which we actually deployed FloodLAMP testing programs. For our last deployment at Abrome, our final pilot site, they chose to pay extra to have one of our experienced test technicians fly out to set up the lab and train their people in person rather than rely on the self-guided video curriculum. And this was a school with folks very experienced in educational programs. The handful of operators who did use the videos — notably at the Needham, Massachusetts site — completed the training successfully. But even this case had considerable hand-holding and in-person interaction (FloodLAMP staff set up the Needham lab and helped with the tester training).

Beyond the procedures themselves, the video transcripts capture the reasoning behind contamination controls, quality practices, and the practical tips that come from running the test repeatedly — things like why you treat the amplification area as radioactive, how to handle the positive control with one hand, or when to just replace materials rather than trying to track down a contamination source. As a record of how a decentralized, point-of-need molecular test was taught to non-laboratory personnel, including firefighters, this material may have reference value for those interested in designing similar programs.

AI completely changes how a program like this would be done today. In addition to or instead of pre-recorded videos and an LMS, a lab testing person would likely be best served by a multi-modal AI assistant that could use audio, display information on a screen, and answer questions in real time. Such a system could adapt to the operator's pace, respond to specific questions as they arise during a run, and scale both training and ongoing operational support without requiring experienced personnel to be physically present at each site. This is one area where the gap between what we built in 2021-2022 and what would be possible today is particularly striking.


# 1,329  _context-commentary_guides-test-validation.md
METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-test-validation.md
category: guides
subcategory: test-validation
gfile_url: https://docs.google.com/document/d/1SAV2Xaj7PxRepMAQGeuBhy7vCf3r_1traljR6saWMcg
words: 921
tokens: 1329


CONTENT

## Context
This `guides/test-validation` subcategory contains two formal protocol documents — the `2021-03-10_Clinical Eval Guide - from FloodLAMP IFU DRAFTS` and the `FloodLAMP Test Validation Guide v1.0` (June 2021) — both derived from FloodLAMP's draft Instructions for Use (IFU) for its COVID-19 molecular assays. They are self-contained, externally-facing technical documents.

Both documents share a common parent: the draft IFUs for FloodLAMP's EasyPCR and QuickColor COVID-19 tests. Large sections of bench procedure — sample preparation, sample inactivation, amplification reaction preparation, and sample addition — are nearly word-for-word identical between them. The core protocol steps (1 mL sample transfer, 100X Inactivation Solution, 30-second vortex, 8 minutes at 100°C, 10-minute cool-down, 2 µL sample addition into prepared reaction mixes) are shared verbatim. Per-reaction volumes are the same: 18 µL reaction mix + 2 µL sample = 20 µL for EasyPCR; 23 µL reaction mix + 2 µL sample = 25 µL for QuickColor (Colorimetric LAMP).

The Clinical Eval Guide was written for a specific clinical evaluation at Stanford University's clinical laboratory in March 2021, for the FDA EUA submissions. It covers three assays — EasyPCR, QuickColor (Colorimetric LAMP), and QuickFluor (Fluorimetric LAMP) — and includes the full recipe for preparing the 100X Inactivation Solution from raw components (TCEP, EDTA, NaOH, nuclease-free water) as well as the Primer-Guanidine Solution from 10X LAMP Primer Mix and Guanidine HCl. The equipment and materials lists are organized simply by what the lab provides versus what FloodLAMP ships.

The Test Validation Guide, dated June 2021, represents a later and more mature version of the protocol. It covers only two assays — EasyPCR and QuickColor — having dropped the Fluorimetric LAMP assay (QuickFluor). The fluorimetric readout was redundant: if a site had a PCR machine, EasyPCR already served that role. FloodLAMP seldom ran the fluorimetric test internally, and none of the pilot sites used it. Importantly, the performance of this test, as we developed it, was considerably worse compared to the PCR and colorimetric LAMP tests (in terms of Limit of Detection). Key differences from the earlier guide include: pre-made 100X Inactivation Solution and pre-mixed Primer-Guanidine Solution (PGS) shipped as part of a formalized validation kit, eliminating the need for sites to prepare these reagents from raw components; detailed kit contents with photos, catalog numbers, exact amounts, concentrations, and number of reactions supported; a structured two-run validation process (Run 1: alternating positive and negative amplification controls in strip tubes; Run 2: contrived positive sample with LoD dilution series in 48-reaction plates); performance data from the EUA submission (LoD of 3,100 cp/mL for EasyPCR and 12,500 cp/mL for QuickColor; clinical sensitivity of 97.5% and 90.0% respectively; 100% specificity for both); Ct-value thresholds and color interpretation criteria for result reporting; thermal cycling parameters for the Bio-Rad CFX96; and 24-reaction scale volumes alongside the 96-reaction scale.

The progression from the Clinical Eval Guide to the Test Validation Guide reflects FloodLAMP's progress over several months — from a bench protocol for generating clinical evaluation data at one specific lab to a more polished, kit-based validation document designed for broader distribution to potential partner labs and organizations.

Connections to other parts of the archive:
- the clinical evaluation data generated using the Clinical Eval Guide formed the core of the March 22, 2021 FDA EUA submissions, which are documented in the `regulatory/fl-fda-submissions` subcategory along with sample sizes, concordance results, and other validation data.
- the manufacturing processes for the reagents referenced here (100X Inactivation Solution, PGS, primer stocks) are detailed in the `guides/manufacturing` subcategory.
- the pilot sites that eventually ran these assays are documented in the `pilots/pilot-sites` subcategory.


## Commentary
These two documents may be of the highest interest/value in the entire archive. They're self-contained, formal, and written for scientists and diagnostic professionals — the kind of documents you could hand to a qualified lab and they could run the test. That's exactly what happened with the Clinical Eval Guide: Stanford's clinical lab ran the test successfully on the first attempt, with no training, using only this guide and the materials we provided. That was a significant validation, not just of the assay performance, but of the documentation itself.

The Clinical Eval Guide dates to March 2021, right before the first round of full FDA EUA submissions. It still required the receiving lab to prepare the 100X Inactivation Solution and Primer-Guanidine Solution from raw components. By the time the Test Validation Guide was written in June 2021, the protocol had matured substantially. We were shipping pre-made reagents — the 100X Inactivation Solution and PGS — as part of a formalized validation kit with catalog numbers, photos, and exact quantities. The fluorimetric LAMP assay (QuickFluor) had been dropped. It was redundant because EasyPCR already covered the PCR-machine use case, and its limit of detection was considerably worse than both other assays. We seldom ran it internally, and none of the pilot sites used it. Of note, none of our pilot sites used EasyPCR either (excluding our own internal staff plus community testing); QuickColor was the assay deployed in all operational surveillance programs.

The Test Validation Guide was not just for our own test sites though. It was created for potential partnerships and external sharing. We did actually share it with one major US healthcare company.

Looking at these two documents together, you can see the evolution from a lab-specific bench protocol to a transferable validation package. The core procedures remained the same, but everything around them — the kit design, the result interpretation criteria, the validation run structure — became more rigorous and more self-sufficient.
