METADATA
last updated: 2026-03-06 by BA
file_name: XPrize FloodLAMP Submission - QS Part 4_ Innovation.md
file_date: 2020-09-09
title: FloodLAMP XPRIZE Qualifying Submission - QS Part 4 Innovation
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1Vc87logYUNc-fLuXBXMkH5StXjA2rBMQ/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20QS%20Part%204_%20Innovation.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1548
words: 1120
notes: 
summary_short: FloodLAMP's XPRIZE QS Part 4 (Innovation) submission covers biosafety protocols, data collection and privacy through the custom Appivo app, innovative sample collection approach with in-app guided self-pooling by households, and the team's core innovation of combining available LAMP technology into an open-source integrated screening platform designed for scalable, affordable deployment by any basic laboratory.


CONTENT

***INTERNAL TITLE:*** FloodLAMP XPRIZE Qualifying Submission - QS Part 4: Innovation

### (BIO SAFETY) DO YOU USE STANDARD PPE & BIOHAZARD WASTE PROCEDURES TO ENSURE PERSONNEL & BIOHAZARD SAFETY?
Yes

### (BIO SAFETY) DO YOU HAVE A UNIQUE OR INNOVATIVE WAY TO ENSURE PERSONNEL OR BIOHAZARD SAFETY?
No

### (DATA) HOW DO YOU COLLECT & PROCESS RESULTS?
Automated

### (DATA) DO YOU STORE PATIENT RESULTS?
Yes

### IF YES, HOW DO YOU ENSURE DATA & RESULT PRIVACY & SAFETY?
Using industry standard procedures. Personal Identifying Information is carefully protected by assigning non-PII unique identifiers that are utilized to track samples and pools.

### (DATA) HOW DO YOU REPORT RESULTS?
Other

### IF OTHER, PLEASE SPECIFY
Through a custom app, with the participants selecting their method of notification. In-app notification is the most secure, however some participants may choose less secure but more convenient direct notification by text or email. Anonymized, aggregated results will also be reported to organizations and participants per specific agreements.

### (DATA) DO YOU HAVE AN INNOVATIVE WAY TO PROCESS DATA AND REPORT RESULTS, SUCH AS AN APP?
Yes

### IF YES, TELL US ABOUT YOUR INNOVATIVE METHOD:
Yes, we have developed a custom app with a partner company, Appivo, that has a low-code app development platform. The alpha version of our app is currently under review by Apple. Through the app, participants collect individual samples and self-pooled samples, thus greatly streamlining the overall system. The collection process is initiated and supervised by a "sponsor" who is typically a member of the pool and who has accepted responsibility for understanding and implementing the proper collection process. This is facilitated by in-app instruction (including video links), which take a few minutes. The app has been optimized for a smooth user experience and for repeated screening by pre-populating with previous collection information. Pooled collection including minors with parents/guardians is included.

### IF YES, IS THIS METHOD COMPATIBLE WITH SAMPLE POOLING?
Yes

### (DATA) CAN YOU INTEGRATE WITH EMPLOYERS/ADMIN FOR TRACKING?
Yes.

### (DATA) CAN YOU INTEGRATE WITH PUBLIC DOMAIN TRACKERS (I.E. APPLE, GOOGLE)?
Yes, our app has an API.

### (DATA) DO YOU HAVE A UNIQUE OR INNOVATIVE WAY TO COLLECT SAMPLES?
Yes

### IF YES, HOW DO YOU ENSURE DATA & RESULT PRIVACY & SAFETY?
The Appivo platform has built-in industry standard security. Appivo has developed apps that include health data for NGOs, and we are leveraging legal and privacy elements of those apps. The Appivo platform enables separate secure instances to be spun up, siloing separate organizations data. The Appivo platform also enables customization of the app—the branding, the design, and the actual functionality. With the mission to spread mass screening capability, FloodLAMP will license the app to other partner organizations, such as universities, which can customize it to suit any specific needs.

### WHAT MAKES YOUR TEST UNIQUE? WHAT IS YOUR BIGGEST INNOVATION?
FloodLAMP's innovation is combining currently available technology into a highly efficient, integrated infectious disease screening program that can scale—and doing so in a truly open way. New technologies have enormous potential, but it's not clear if any will be ready in 2020. Both well-funded startups and large diagnostics companies will surely bring online significant additional testing capacity, but most of that will be on closed systems or in closed labs, and will be at the highest price the market will bear. Some new options will have impactful tradeoffs, such as antigen tests with LOD's above the threshold for infectiousness. Incentives have not been properly set to encourage the development of a program that any basic lab can affordably bring up and run at significant scale. FloodLAMP is building upon the foundational work of others to combine a sensitive, super cheap, flexible and molecular assay with streamlined sample collection. We are openly sharing not just our protocols but the wrap around processes for a dedicated screening program that is designed to be accessible for all other labs. At the same time we are soliciting help in best practices, under a structure where that knowledge is shared and disseminated, not just used in a limited, closed offering. In short, we're bringing open source to biotech, helping to create the Linux of infectious disease screening. We're building on the current important open efforts (such as JOGL, gLAMP, shared protocol websites like protocols.io) and implementing an integrated screening program to address the global COVID-19 crisis.

### OPENTRONS IS PARTNERING WITH XPRIZE TO SUPPORT TEAMS WITH LIQUID HANDLING ROBOTS DURING THE PILOT PHASE. PLEASE TELL US WHETHER YOUR TEST CAN BENEFIT FROM LIQUID HANDLING AUTOMATION AND HOW YOU MIGHT USE (OR ARE ALREADY USING) THE OPENTRONS LIQUID HANDLER.
Yes, we can benefit greatly from liquid handling automation. We plan to develop the next configuration of our assay protocol around the OpenTrons robot. There is one at our shared lab facility (MBC Biolabs in San Carlos) that we would like to gain access to in mid Sept. We have consulted with the automation expert at Denali Pharmaceuticals who planned to automate the Rabe Cepko assay, which primarily involves the silica washing steps. We have extensive experience in automating assay protocols involving silica microparticles, through FloodLAMP founder's previous startup True Materials. Affymetrix acquired True Materials in 2008, and we automated several processes for pilot production of liquid arrays using the True Materials' silica microbarcodes on a Biomek Fx, plate washers, and vacuum aspirators. The OpenTrons system is ideal for our automation development because of the low upfront cost of the system and the open source approach of the company.

### PLEASE TELL US ANY REASONS THE PROFICIENCY OR CLINICAL TESTS MAY NOT ACCURATELY RECAPITULATE HOW WELL YOUR TEST WORKS.
The buffer that the proficiency samples are in may not be compatible with our nucleic acid binding protocol. At a high level, we are not just developing a test (or assay protocol, that's already been done by Rabe and Cepko and their clinical collaborators, Anahtar et al)—we are developing an integrated screening program. That being said, many parts of the system are plug and play. For example, with a slight modification of our existing protocol (elution from the dried pellet), we can go into qPCR as well. We have done almost all of our development on real human samples, starting with raw saliva and soaked nasal swabs. We inactivate those samples with a chemical reducing agent, TCEP/EDTA per the Rabe Cepko protocol. The next step of the main assay protocol uses a high salt solution (NaI) along with the prepared silica for nucleic acid binding, and that may not work or work as well without the TCEP. For our no template controls, we use 1X PBS with the corresponding amount of the TCEP Inactivation Solution. We have not yet run our assay protocol with VTM or other sample collection buffers, as we will collect and inactivate using our protocol.
