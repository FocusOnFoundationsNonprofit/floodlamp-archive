METADATA
last updated: 2026-03-06 by BA
file_name: RADx 2022 Submitted Proposal - FloodLAMP (Oct 2022 - 3M - Not Funded).md
file_date: 2022-10-31
title: RADx 2022 Submitted Proposal - FloodLAMP (Oct 2022 - 3M - Not Funded)
category: various
subcategory: fl-proposals
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1FD3-N6AC2PQKKS_WpqtdQ1FnSvZAhJdyZrOcnaXb_AI
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/fl-proposals/RADx%202022%20Submitted%20Proposal%20-%20FloodLAMP%20%28Oct%202022%20-%203M%20-%20Not%20Funded%29.docx
pdf_gdrive_url: https://drive.google.com/file/d/1E75bmMN2ddomYiFTMdJC7rnz7uPzdebr/view?usp=drive_link
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/fl-proposals/RADx%202022%20Submitted%20Proposal%20-%20FloodLAMP%20%28Oct%202022%20-%203M%20-%20Not%20Funded%29.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 7938
words: 5777
notes:
summary_short: The FloodLAMP RADx submission outlines a next-generation, low-cost LAMP-based screening platform pairing reagent-in-cap test devices with modular heater/reader instruments and an integrated mobile app/admin portal for pooled, decentralized testing programs. It summarizes pilot experience (~35,000 samples across 11 surveillance deployments), projected performance and costs, and an open-source business model built around disclosed chemistry, Rights of Reference, and broad licensing for interoperability. It also proposes a two-phase RADx work plan to prototype devices/instruments, run multi-site clinical studies, pursue EUA/510(k) pathways, and scale manufacturing and digital infrastructure for pandemic-ready screening.


CONTENT

***INTERNAL TITLE:*** FloodLAMP RADx Submission 10-31-2022

[https://www.poctrn.org/web/radx-tech-high-performance-tests](https://www.poctrn.org/web/radx-tech-high-performance-tests)


## Abstract (50)
*Please provide a brief description of the problem and solution being addressed*

Recent advances in diagnostics are not yet configured for population-level pandemic response. Despite large amounts of COVID-19 response funding in the space, the market for true pandemic screening products and services remains highly unstable. We propose a durable next generation molecular platform with isothermal test devices and flexible heater-reader designs.


## Solution Summary (200) 
*Provide a brief solution overview*

FloodLAMP’s new platform combines key innovations in diagnostic testing technology and modalities that have matured during the COVID-19 pandemic: isothermal amplification (LAMP), direct extraction-free assays, and sample pooling. Our new test device comprises a reagent-containing cap that is coupled to a standard collection tube. The tube is inserted into a compact instrument that both heats and reads the assay signal optically, wirelessly transmitting results for walkaway operation. Heating and reading subunits of the instrument are decoupled to leverage low cost, high volume manufacturing of PCB’s and standard dry bath heaters. The heater-reader versions comprise one for a single device and anotherst version accepting up to 60 asynchronously. We’re also planning a device version with visual readout.

The new device and instrument are combined with program components optimized over the last 16 months in 11 LAMP surveillance pilots. We’ve developed self-pooled collection kits, registered on-the-fly with our mobile app which is integrated with onboarding and program administration tools.

We are innovating in a third domain, using a public benefit corporate structure and open source business model. We have committed to fully disclosing the test chemistry and primer sequences in all of our FDA submissions, granting ROR’s, and widely licensing for interoperability.


## Technical Characteristics (200)
*Briefly describe technical characteristics of the solution including how clinical performance approaching PCR levels is achieved*

Our new test system is anticipated to have an LOD and clinical sensitivity in the range of other COVID-19 EUA tests that use similar LAMP chemistry. We use 3 primer sets (18 oligos) combined in one reaction. These primers have demonstrated good performance in a clinical study by Stanford (March 2021), in silico, and importantly in extensive real world testing (~35,000 samples at 10 sites).

The per sample cost is anticipated to be approximately \$1, based on current all-in test kit COGS <\$.50 (collection kit, consumables, reagents - for pool of 4). The device design uses a reduced reaction volume to the 10-50 uL range, minimizing the enzymes needed which are the cost driver. The single instrument is expected to cost $50-100, and the 60-wide version, ~$1000.

For the POC/PON intended use, throughput is important and a primary design consideration. We’ve modeled the hands-on time to be 12 seconds per tube, and anticipate ~30 minute total turnaround time. The instrument runs asynchronously, with results transmitted wirelessly. Thus, one operator can process ~1,000 samples per hour (average pool size 3). The ease of use of the system means minimal training is needed for the POC operator.


## Key Performance Parameters
**Sensitivity (This is a required field).**
88-96% (anticipated, based on comparables and FloodLAMP's QuickColor COVID-19 LAMP test performance in real world and clinical study)

**Specificity (This is a required field).**
98-100% (anticipated, based on comparables and FloodLAMP's QuickColor COVID-19 test performance in real world and clinical study)

**Level of detection (This is a required field).**
300 - 3,000 copies per swab (anticipated, based on comparables and FloodLAMP's QuickColor COVID-19 test performance in real world and clinical study)

**Time to run a single test (This is a required field).**
30 minutes (anticipated, based on comparables and FloodLAMP's QuickColor COVID-19 test)

**Production cost of the test (This is a required field).**
$3-5 individual sample, $0.80-1.25 per sample with pool of 4 (anticipated)

**Production cost of the instrument (put n/a if not applicable) (This is a required field).**
$1,000 for 60-sample version, $50 single sample version (anticipated)


## Prior Work and Current Status (750)
*Describe the current status of your proposed solution and any additional information you would like reviewers to consider. (750 words or less)*

FloodLAMP has run 11 end-to-end COVID-19 surveillance screening pilots using our current extraction-free LAMP test and other program components, with ~35,000 samples tested. We supported many of these programs through the 2021/22 Omicron surge, including three EMS departments, two 1,000 person municipal workforces, and a preschool that used at-home pooled sample collection. The inspiration and design objectives of the new platform are drawn directly from the experience and lessons learned from implementing these pilot surveillance screening programs over the last 2 years.

Pilots stats:
- 11 programs, 10 sites in 5 states, from Dec 2020 to present;
- 35,184 samples tested total; 15,748 pools; 3,587 individuals tested;
- 550 positive samples;
- 23 test operators trained, majority with no prior experience;
- 483 users collecting with our mobile app.

The FloodLAMP Mobile App and Admin Web Portal were launched in the spring of 2021 and are available in the Apple and Google app stores. All but one of our surveillance pilots have used them. They were designed as a holistic digital suite for decentralized, organization and community based disease screening. The app has 3 interfaces, 1) for participants to manage their profile, collect pooled samples, and view test status; 2) for testing staff to intake, track, and result tubes; and 3) for program administrators to onboard users, manage permissions, and view results. A novel capability is the self-registration of participants in pooled sample collections. We filed broad IP in this area in 2020 (published application US20220208394A1), and received a favorable written opinion from the USPTO on our PCT, enabling prioritized examination of our regular US patent application. We filed a followup provisional patent covering additional inventions on digital components of screening programs.

The new test devices and reader instrument work is currently at the design stage. We seek RADx support to build initial prototypes, and also to carry out clinical studies on other components of the test system. These include the OTC pooled collection kit and our mobile app. FloodLAMP has filed a 161 page provisional patent, broadly covering many embodiments of the new platform components, systems, and methods.

Our pilots provided critical feedback in improving our program components. Several program administrators commented that once they had their “lab” set up and were comfortable running the test, the logistics of coordinating sample collection and transfer was far more work. Both of our EMS+municipal workforce programs used a hub and spoke model, with 7-10 sites around the city where samples were aggregated then shuttled 5-30 minutes away to the single processing site. With the flexibility of both single and many device instruments, our new platform can span a range of volumes of screening at different levels of decentralization. We see the organizational based, point-of-need modality as important for workplaces and schools, especially during surges. We’re planning to enable both individual/single household at-home and POC/PON screening with the same platform.

Overall in the space, we see the need for a fully vertically integrated company to hit the low price need for pandemic screening, which needs to both rapidly scale and maintain readiness. We commercialized our in-house surveillance at the price point of $5 per pool ($1.25 per sample). The COGS are $1.93 per pool at the 1M scale, including the collection kit, reagents, all consumables, and digital license. FloodLAMP provided all of the materials, training, and support to bring up the in-house pilot programs. Our service pilots were the white-glove model. We intend to offer the same end-to-end programs built around our new platform, while at the same time extensively partnering and licensing.

During the pandemic, we have been involved with many projects and groups and made a number of connections that will bring support during our next stage. These include: the executive leadership at New Englands Biolabs (see below), the global LAMP consortium and Professor Chris Mason of Cornell Weill, Anne Wyllie (Yale, Saliva Direct), Jeff Huber (Grail, Open COVID Screen), Simon Johnson (MIT, MA testing), Robby Sikka and the Sports and Society Working Group, Taylor Sexton (Todd Strategy Group, formerly ASPR).

Our focus to date has been in building and piloting screening programs that have the characteristics needed for resilient, decentralized pandemic preparedness and response. With the filing of IP on this next generation platform and upcoming publication of our work, we are transitioning to fundraising and outreach. We are eager to engage with RADx and hope our work may be of help in a national and global pandemic testing strategy.


## Regulatory Status (200)
*Provide an overview of regulatory status (FDA and CLIA approvals) (200 words or less)*

FloodLAMP has filed a Pre-EUA on our pooled self-collection kit + mobile app, and 2 full EUA submissions, as “open source protocol” tests, the most recent in October 2021. We received written feedback and had a conference call, attended by myself, Anne Wyllie of SalivaDIrect (a close advisor to FloodLAMP), several reviewers, and Kris Roth from the FDA. The FDA declined to continue our review, it’s our understanding due to FloodLAMP not being a large manufacturer or experienced developer. We have concluded based on the FDA November 2021 guidance that agency support is required for further engagement or review by the FDA.

Submission information:
PEUA210313 FloodLAMP Pooled Swab Collection Kit DTC
EUA210581 FloodLAMP EasyPCR COVID-19 Test
EUA210582 FloodLAMP QuickColor COVID-19 Test

We have an active IRB protocol (WCG 20210401) for 3 variations of prospective clinical studies of asymptomatic subjects, including user factors regarding the collection kit and mobile app.

We have implemented initial modules of an ISO 13485 compliant QMS system, supported by consultants at Rook Quality Systems. We have also contracted with regulatory consultants at Arete Biosciences in support of our EUA submissions and IRB.

We have not undertaken steps toward regulatory approval for our new platform.


## Performance Testing (200)
*Provide an overview of performance testing done to date (200 words or less)*

The performance testing done to date has been with the moderate complexity, pipet based version of our colorimetric LAMP assay. We expect the technical performance of the new platform to meet or exceed that of our current test system, while greatly improving the usability and reducing contamination concerns. Our new platform will likely use the same 3 primer sets as our current test, with similar LAMP reaction chemistry.

A clinical evaluation of our direct PCR and colorimetric LAMP tests was completed on March 10, 2021 by the Stanford Clinical lab, in preparation for our first EUA submissions. A summary of analytical and clinical results follow:

Direct Colorimetric LAMP:
- analytical LOD: 12,000 copies/mL;
- no cross reactivity;
- expected results on interfering substances;
- 90% clinical sensitivity (PPA 36/40);
- 100% specificity (40/40);
- no false positives;
- missed positives only high Ct (>36 with PCR).

Direct PCR:
- analytical LOD: 3,000 copies/mL;
- 98% clinical sensitivity (PPA 39/40);
- 100% specificity (40/40);
- no false positives.

The real world performance of our surveillance LAMP test has been excellent, robustly identifying new infections early. That will improve with the convenience and portability of the new platform, thus reducing barriers to routine testing.


## Implementation and Production (200)
*Provide a summary of your implementation and production plans (including projected monthly production capacity) (200 words or less)*

FloodLAMP’s implementation plans include initiating prototype development for the new device and instrument (see Work Package #1). Simultaneously we will execute on 2 sets of deliverables that can both have independent impact in the field and are on the critical path of the overall plan of developing pandemic screening using the new platform. The first is gaining EUA for the OTC pooled collection kit and app, which we plan to broadly license and partner around. The second is assay work to translate our current test to POC format, comprising lyophilizing our current test, optimizing a 1-step chemistry, sourcing single reaction dispensers of the inactivation solution, and a dropper cap. These steps bridge to our new platform and offer significant workflow improvements that may themselves warrant scale up.

Regarding production, we will utilize multiple suppliers and manufacturers and partner for US and global distribution, starting with companies with which we have existing relationships. We completed an order from LGC for a 1.2M reactions of our primer sets and are working with the OEM team at NEB.

Post COVID-19, we will source primers and assay technology IP from academic labs, offering a commercialization model that facilitates scale through open access.


## Other Information (750)
*Provide other relevant information including handling variants, accessibility for individuals with disabilities, support for telemedicine and communications of results, platform and/or multiplexing capabilities, avoidance of common supply chain issues, addressing unmet needs of traditionally underserved and underprivliged populations, and scalability of production.*

### Multiplexing
Some new device designs incorporate multiple reaction chambers to multiplex targets. Additionally, some device designs utilize swappable reaction components to enable different pathogens to be tested from the same sample tube. Multicolor detection by the instrument is also possible but adds complexity and cost.

### Variants
Our current LAMP test and primers are very robust to variants. We use 3 primer sets (18 oligos) all combined in the same reaction. The primers comprise 2 open sets (N2, E1) and 1 proprietary set “Rabe-Cepko AS1e” (ORF1ab). We used the NEB Primer Monitoring for our Evaluation of Impact of Viral Mutations section of our October 2021 EUA Submission. Further, NEB completed a large, comprehensive wet study earlier this year of the effect of mutations in our same 3 primer sets, finding “no effect on detection sensitivity at positions equivalent to those that significantly impact RT-qPCR assays.” FloodLAMP has an option to the exclusive license on Rabe-Cepko IP and is in late stage license negotiations with Harvard Medical School.

These 3 primers have performed well in real world surveillance programs and our Stanford clinical study, offering high sensitivity and a low false positivity rate. Over 500 positive samples have been detected and confirmed, the vast majority Omicron variants.

### Accessibility
The core of our new platform is ease of use, which in turn enables accessibility and scale. We have minimized the number of steps and components in the new test workflows. All actions of manipulating the consumables require low physical effort and have a high tolerance for error with no lab training necessary. We will provide alternative instruction materials in accordance with ADA guidelines in order to make them accessible to those with visual, audio, or other impairments.

### Telemedicine Support
We have an API to our digital platform that can automate all required federal, state and local reporting requirements, as well as interface to any 3rd party digital health platform or EMR system.

### Supply Chain
A key aspect of the primary device designs is that they utilize standard sample tubes, allowing us to leverage existing supplies and manufacturing capacity. The main instrument design also leverages existing systems, using a drop-in replacement of a standard sized dry block that is inserted into dry bath heaters.

### Production Scalability
The device design is relatively simple, facilitating large-scale production of the plastic cap units. An advantage is the enablement of distributed 2nd stage manufacturing of the reagent component, through a 2 part design that can be loaded by pipette, or at various production scales using liquid handlers. The low cost plastic components of the consumable device can be supplied to testing centers in LMICs as prepositioned assets to reduce supply chain risk during health emergencies. It also supports redundant domestic manufacturing.

U.S. based reagent manufacturing is anticipated to use lyophilization. FloodLAMP is thankful to New England Biolabs, one of the largest enzyme producers globally, with whom we have a close relationship and multiple collaborations on community testing, including early childcare screening in the U.S., and 2 with universities in South America. We have had multiple meetings with the leadership team of NEB, which is also a Public Benefit Corporation, and they have provided us with a letter of support for federal funding that includes early access and recommendations, specifically for lyophilized formats.

### Underserved Populations
Our new platform addresses underserved populations through the combination of low cost and scalability. A primary motivation for the new platform, and FloodLAMP’s work in general, has been to translate the on-demand rapid molecular programs enjoyed by sports and entertainment to the rest of society. It’s important that underprivileged communities have access to reliable tests for screening, which currently means molecular. One day in December 2021, our Coral Springs program had 22 positives in one run. They reran the plate, getting the same results. Per protocol, all LAMP positives were immediately tested with BinaXNow. Only 1 came back antigen positive. This caused some of the positive firefighters, paramedics, and police officers to question the LAMP test. Over the next few days of serial testing, all 22 turned antigen positive. Doubt in the reliability of antigen tests has been cited in studies as a primary reason for not participating in free screening programs.

We see the potential for innovation on incentives to drive adoption in underserved communities, and we hope to work in this area as well in the future. Further advances in ease of use and cost, along with digital and program integration, are needed first to provide the foundational decentralized screening capacity.

*We are not now asking for detailed work plans - that will come later.*

*Describe the result of the work you expect to complete in discrete "Deliverables" or outputs of your work. If you are selected we will work with you to finalize plans, including access to needed resources.*

***Work Package #1 is intended to address high-risk barriers to success which, when successfully resolved, will enable Work Package #2 which will focus on implementation***

## Work Package #1 (200)
*Budget – Please indicate your expected direct budget (including labor and all expenses with full Federal OH rates) – Short answer*
*Duration – What is the expected duration of WP #1 (in weeks) – Short answer*
*Deliverables (200 words or less)*

Budget - $3M
Duration - 16 weeks
Deliverables:

We first propose to publish the results of our EMS and school pilots, with feedback and support from the RADx team.

To de-risk key elements of the new platform, we propose the following deliverables:

1.  Prototypes of new device designs and instrument:
    a.  devices built at Stanford Nanofabrication Lab and CRO;
    b.  instrument design and build (subcontract).

2.  Large scale, multi-site clinical studies:
    a.  for OTC pooled collection kit and FloodLAMP Mobile App;
    b.  for 2 moderate complexity tests - direct LAMP and PCR;
    c.  leverages current surveillance program infrastructure;
    d.  uses enrichment strategy in surveillance population and site/household exposure;
    e.  daily serial testing to evaluate performance in identifying new infections;
    f.  comparison against both antigen tests and high sensitivity lab PCR;
    g.  single site fast-tracked for EUA’s;
    h.  expansion to multiple sites for 510K data collection;
    i.  sites primed for clinical studies using new platform prototypes;
    j.  proposal for adjunct funding (RADx-UP) for saturation screening in 10,000+ person population (endpoint outcomes: disease burden reduction, staff/student outage, and adoption rate, comparing different incentives).

3.  FDA EUA submissions for tests, pooled collection kit, and app.

4.  Bridge assay development.

5.  Manufacturing partnerships:
    a.  NEB, LGC, Twist, and CMO;
    b.  manufacturing and kitting of 1st 800,000 LAMP test kits.

6.  Fully integrated digital suite for program execution and management.


## Work Package #2 (200)
*Budget – Please indicate your expected direct budget (including labor and all expenses with full Federal OH rates) – Short answer*
*Duration – What is the expected duration of WP #2 (in weeks) – Short answer*
*Deliverables (200 words or less)*

Budget - $20M
Duration - 76 weeks
Deliverables

The following deliverables form the core of the operational aspects of commercialization, including FDA full market approval. Business deliverables will be funded from additional sources and are excluded below.

1.  510K approvals for all components of new platform and current moderate complexity tests:
    1.  completion of optimized devices, including both visually read and instrument read versions;
    2.  multi-site clinical studies with the new platform;

2.  Pilot manufacturing run of new platform consumables, including cap components and loaded reagents.
    1.  implementation of full ISO13485 QMS system.

3.  Completion of commercialization-ready instrument:
    1.  one or more manufacturing partners identified and supply agreements negotiated.

4.  Full suite of commercialized digital tools:
    1.  program Admin Web Portal;
    2.  participant Web Portal (onboarding and communications);
    3.  FloodLAMP Mobile App (native and web app versions);
    4.  infrastructure upgrades to support scale.


## Overview of Team and Environment (200)
*Please provide an overview of the team members and why they collectively have the expertise and access to resources to be successful in achieving a deployable solution. (200 words or less)*

Our core team has a successful track record of technology innovation in assay platforms, microfabrication, fluidics, and molecular biology with applications in diagnostics. We’ve demonstrated the ability to carry research and development projects forward into production as exemplified by Randy and Gary’s work at Affymetrix.

We have expertise in design and execution of clinical studies through our medical advisor, Dr. Peter Antevy who is experienced in clinical study protocol design and recruitment.

We also have deep expertise in digital design and user experience, both on our team and in our network.

Our extended team of investors and advisors include individuals in diagnostics, biotech finance, venture capital, academic research, and clinical medicine.

Anne Wiley, founder of SalivaDirect and pioneer of the first open source protocol EUA, is on our Scientific Advisory Board, as well as being a friend and mentor on all FDA matters.

Being based in Silicon Valley and 10 minutes from Stanford University, FloodLAMP is in a prime location physically and in our development to bring human and financial resources to bear on the problem of pandemic-level disease screening.


## Team Member - Randy (200)
Team Member Name – Randy True
Role on Team – Founder and CEO
Level of Effort – 100%

### Relevant Experience
Randy brings a broad background in science, engineering, and management to the company, as well as specialized experience in molecular detection technology, including DNA and RNA bioassay development and microfabrication. His particular strengths are in innovation and integration, drawing on engineering skills spanning hardware, software, and materials. He has led the rapid execution of multidisciplinary projects, design at scale, and successfully transfer processes to high volume manufacturing facilities. Randy is the inventor of ten issued US patents.

Randy has been an advisor and consultant across many industries. In 2018, he founded Focus on Foundations, a science education 501(c)3 non-profit whose mission is to develop innovative, impactful STEM curricula by connecting hands-on learning and practical skills with deep theoretical knowledge.

Randy has a B.S. in Physics and M.S. in Electrical Engineering from Stanford University. While at Stanford, he did research on quantum electronic devices, training at the Stanford Nanofabrication Facility. He worked in startups and the semiconductor industry, and as a microfabrication consultant at the Stanford Nanofab for 10+ years. This extensive experience in rapid iteration on designing, building, and testing microdevices is well suited to development of the new platform.

### Current or most recent position - Include start and end dates, title and position description
FloodLAMP Biotechnologies, PBC
August 2020 - present, Founder and CEO

As FloodLAMP’s CEO, Randy is responsible for the key executive functions of fundraising and recruiting. He also leads the regulatory and communications strategy. Being a startup, Randy also contributes to engineering and design, as well as overseeing the company’s training program and quality system.

### Past position #1 - Include start and end dates, title and position description
True Materials Inc. and Affymetrix
December 2005 - 2010, Founder and CEO, VP R&D

Randy previously founded the biotech startup True Materials, Inc., which developed a barcoded microparticle technology with a variety of applications including particle-based DNA microarrays for genetic analysis and molecular diagnostics. Randy built the microparticle prototypes at the Stanford Nanofabrication Facility and successfully transferred production to a high volume semiconductor foundry. True Materials was incubated in the first cohort of companies at UCSF/QB3 Garage at Mission Bay.

True Materials was acquired by Affymetrix in 2008 where Randy served as VP of R&D, Liquid Arrays. He built and managed an interdisciplinary team of 20 that brought the technology to pilot production, prior to the Affymetrix sale to Thermo Fisher.

### Past position #2 - Include start and end dates, title and position description
Shaper Tools, Inc
January 2016 - January 2018, Technical and Business Advisor
Technical consulting, fundraising, and patent strategy.


## Team Member - Gary (200)
Team Member Name – Gary Withey
Role on Team – VP of R&D
Level of Effort – Full-time

### Relevant Experience (up to 200 words)
Gary brings fifteen years of industrial biotech experience in technology development, invention, process development, and product development. He has broad expertise spanning diagnostic platforms, therapeutic discovery platforms, microfluidics, semiconductor microfabrication, rapid prototyping, automated liquid handling, molecular biology, and data science. He is the inventor of three U.S. patents and two patent applications in the fields of microfluidics, diagnostics, molecular biology, and single-cell sequencing.

In his work at Atreca and Gigagen, Gary has designed and constructed droplet microfluidic devices and associated emulsion chemistry and molecular biology for high throughput single cell screening and analysis. This work included rapid prototyping via 3D printing and CNC machining of custom components and extensive design and execution of experiments to optimize droplet stability and performance of biomolecular assays on single cells. He also performed downstream bioinformatic analysis of large single cell sequencing datasets.

At Affymetrix, he developed a process to produce DNA-labeled, barcoded microparticles for highly customizable, low-to-mid-plex, particle-based DNA microarrays for genetic and transcriptomic applications in diagnostics and research. He served as company liaison at a semiconductor microfabrication core to produce barcoded microparticles. He designed and managed a pilot production facility to conjugate particles to synthetic DNA via high throughput, automated liquid handling.

### Current or most recent position - Include start and end dates, title and position description (198)
FloodLAMP Biotechnologies, PBC
Nov 2020 - present, VP of R&D

Gary has helped to adapt and optimize the current extraction-free colorimetric LAMP assay that is the workhorse of our disease screening programs. He devised many of FloodLAMP’s custom reagent formulations and created the system for their production and quality control that has over time evolved into a mature quality management system. He integrated robot liquid handling to scale reagent preparation and kitting capacity of FloodLAMP reagents. He has rapidly prototyped and produced custom labware components such as tube racks for which there exist no suitable standard products. He has designed and implemented systems for inventory control, lab operations and decontamination procedures, and project management.

Gary has played a key role in overseeing the initiation and ongoing operational support of multiple of FloodLAMP’s surveillance testing deployments, including training and knowledge transfer, transfer of materials and inventory management, lab setup, technical troubleshooting in the laboratory and digital spaces, and support related to data management and program management.

Gary also led the IP effort for our new platform technology, contributing many of the core design aspects of the consumable cap and the heater/reader instrument to our provisional patent application.

### Past position #1 - Include start and end dates, title and position description (123)
Atreca, Inc
July 2013 - March 2022, Associate Director of Engineering, Head of Engineering

Gary’s responsibilities included the construction of a microfluidic system for high-throughput single-cell transcriptome analysis. This involved fabrication of custom microfluidic components through collaboration with external partners as well as hands-on fabrication of device components using CNC machining, laser cutters, 3D printers, milling machines, and other standard workshop equipment. He performed extensive studies to optimize complex emulsion-based RT-PCR reactions to enable a phage display technology built on this microfluidic system for the discovery of promising antibodies for immuno-oncological therapeutics. Gary also performed bioinformatic analysis and protein engineering based on sequencing pipeline data in order to optimize antibody synthesis yield. He developed IP that led to three issued patents and one patent application.

### Past position #2 - Include start and end dates, title and position description (108)
GigaGen, Inc
March 2011 - July 2013, Director of Engineering

Gary designed and assembled microfluidic chips and custom hardware into a system for high-throughput genetic analysis of single cells. His design work included rapid prototyping of microfluidic chip designs in PDMS before then translating design features into glass chips. He performed studies to optimize oil/surfactant formulations for both thermostability and compatibility with emulsion PCR in the presence of cell lysate. He also performed studies to optimize emulsion based RT-PCR for next-gen sequencing library preparation. He also developed software for device control of system components. Gary also contributed to IP development in microfluidic chip design and single-cell sequencing applications.


## Team Member - Theresa (200)
Team Member Name – Theresa Ling
Role on Team – Lead, Design and Program Experience
Level of Effort – Part-time

### Relevant Experience
Theresa Ling is a Product and Experience Design professional seasoned in creating systems and tools for complex information and interactions. Her work has spanned projects for Fortune 500 companies, startups, and nonprofit organizations, and she has participated in the inception and launch of multiple large scale software efforts spanning different platforms and industries. Notable projects prior to joining FloodLAMP include creating a new sales platform for Nike’s Global Sales department (pilot program sales exceeded $1B), designing and launching New Relic’s Infrastructure product, and devising a unifying web access strategy for Uber’s many, disparate apps in advance of their IPO. Before transitioning to design, Theresa worked in the performing arts as a dancer and choreographer. This background informs her human-centered design approach and strengthens her ability to see the connections between people and the programs, spaces, and tools they use.

### Current or most recent position - Include start and end dates, title and position description
FloodLAMP Biotechnologies, PBC
August 2020 - present, Program Experience and Design

Theresa has contributed extensively to the user experience of FloodLAMP’s testing program. This includes product design for the digital tool set (app, most web tools), site and population considerations with respect to usability and collection challenges, and developing outbound communications for participating organizations and test subjects (i.e. collection kit instructions, signage, program overviews). She acted as Program Manager for FloodLAMP’s first preschool pilot with at-home family pooling, managing all communications, site planning and scheduling with an eye toward reducing the friction and pain points associated with COVID testing for busy families.

Theresa has integrated user feedback into ongoing improvements in the app design, including streamlining the core participant flow and updating interaction patterns for the staff user, and continued to design new tools for program registration. Theresa additionally manages the company website and communications, and will be leading the user experience and design of the new platform. Theresa also contributed to the IP effort for FloodLAMP’s digital tools featuring pooled self-collection as well as the followup provisional application covering additional inventions on digital components of screening programs.

### Past position #1 - Include start and end dates, title and position description
Uber
November 2017 - May 2019, UX Lead

Hybrid IC/manager managing several designers within the web team as well as leading key design initiatives. Key projects include leading the creation of web design system templates for Uber’s international operations workforce, and designing and planning a new web portal experience to unify a fragmented app ecosystem prior to IPO.

### Past position #2 - Include start and end dates, title and position description
New Relic
February 2016 - June 2017, Senior Product Designer

Principal designer for the new Infrastructure product working in an agile framework. Established design system for new product within an existing product suite, conducted all user research on Beta and synthesized findings into design updates per sprint, worked in step with engineering team to ensure design to spec, supported product launch and advised on roadmap.


## Team Member - Peter (200)
Team Member Name – Dr. Peter Antevy
Role on Team – Medical Director
Level of Effort – Part-time
Relevant Experience (up to 200 words)

Dr. Antevy is a Pediatric Emergency Medicine Physician at Joe DiMaggio Children’s Hospital in South Florida and the Founder & CMO of Handtevy Pediatric Emergency Standards Inc. He serves as the Medical Director for Coral Springs Fire Department, Davie Fire-Rescue, Southwest Ranches Fire Rescue and American Ambulance, and is the Associate Medical Director for several other agencies. He is also a longstanding medical director for two paramedic training programs and several mobile integrated healthcare (MIH) programs. Dr. Antevy has authored studies and spearheaded a system used to expedite resuscitative care for children. He is involved in his departments’ continuous quality improvement (CQI) programs and has seen dramatic improvements in the outcomes of cardiac arrest patients. This year, he helped bring the Seattle Resuscitation Academy to Florida and has demonstrated a significant impact on prehospital cardiac arrest outcomes.

### Current or most recent position - Include start and end dates, title and position description
FloodLAMP Biotechnologies, PBC
December 2021 - present, Medical Director

Peter serves as FloodLAMP’s Medical Director, where he has been instrumental in building both the relationships and program protocols to make FloodLAMP’s EMS COVID-19 surveillance programs successful. As a nationally recognized leader in EMS, Peter provides important connections to EMS departments at state and regional levels. In addition, he advises on testing procedures, communications, and clinical studies.

### Past position #1 - Include start and end dates, title and position description
Handtevy - Pediatric Emergency Standards, Inc
January 2010 - present, Founder & Chief Medical Officer

Peter founded Handtevy with the mission to improve pediatric resuscitation and reduce medical errors in EMS Agencies and Emergency Departments around the country. Handtevy is succeeding in this mission with programs in all 50 states. The Handtevy product is a simple and responsive web based system that can intake patient information and rapidly develop a treatment plan, allowing EMS personnel to act precisely and effectively. Patient data is properly stored according to HIPPA regulations and all resuscitative actions are completely documented automatically. The emphasis on user experience on all platforms reduces the chance of mis inputs or misuse, increasing rates of correct pediatric dosing to over 85%.

Peter founded and built Handtevy from the ground up. He currently serves as Handtevy’s Chief Medical Director, managing key staff as well as leading high level outreach to state health departments and other stakeholders.

### Past position #2 - Include start and end dates, title and position description
C3MD, LLC
December 2014 - Present, President

Peter is Principal and President of 3CMD, which is engaged in various medical business activities. 3CMD is a provider of the EcoTest COVID-19 IgG/IgM Rapid Test Device - an in-vitro immunoassay for the direct and qualitative detection of anti-SARS-CoV-2 IgM and anti-SARS-CoV-2 IgG in human whole blood, serum or plasma.
