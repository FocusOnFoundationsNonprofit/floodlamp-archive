# ===== START OF FILE _archive-combined-context-commentary_pilots_12k.md =====
# pilots context & commentary (2 files, 11,644 tokens)

# 3,225  _context-commentary_pilot-data_data-processing.md
METADATA
last updated: 2026-02-27 RT
file_name: README_pilot-data_data-processing
category: pilots
subcategory: pilot-data
words: 2465
tokens: 3225


CONTENT

## Pilot Data Overview
The FloodLAMP pilot data was collected across 11 surveillance testing programs in 4 states, drawing from three primary sources:

- **FloodLAMP mobile app** (built on the Appivo platform) — Used by participants and administrators for registering participants to barcoded collection tubes and for recording results. Not all sites used the app; usage varied across programs and was accompanied by varying degrees of completeness and data quality.
- **Google Forms** — A Run Form for logging run-related data after each testing run, and a weekly stats form for reporting aggregate numbers (samples, positives, etc.). See the Acronyms section below for details on the corresponding spreadsheet types.
- **Referral test data** — Information about non-FloodLAMP follow-up tests (typically antigen or PCR), communicated to FloodLAMP via email, text, or verbal reports.

The data underwent multiple rounds of cleaning and reconciliation, with all changes tracked in the spreadsheets using standardized codes. The processed data is available in Google Drive as Google-native spreadsheet files and as extracted CSVs. Summary markdown files containing key plots and data are also provided.

| Resource | Location |
| ----- | ----- |
| Google Drive master index | https://docs.google.com/spreadsheets/d/1b1uWHNGBL9yatTUNnzrbOTdWOMlD-XYVsn4V6pSYmmk |
| Filename listing | pilots/pilot-data/Data PUB - Pilot Data Google Files - PUB Filenames.csv |
| URL listing | pilots/pilot-data/Data PUB - Pilot Data Google Files - PUB URLs.csv |
| Aggregate summary | pilots/pilot-data/aggregate_pilot-data/aggregate_pilot-data_summary.md |

Video transcripts of data pipeline walkthroughs are included in _docs_pilot-data, and the code for generating summary markdown files and plots is in _code_pilots-data.


## Acronyms and Terms
#### Key Acronyms
| Acronym | Meaning | Context |
| ----- | ----- | ----- |
| **APS** | **Appivo Samples** | Spreadsheet of Appivo app extracted data with by sample (participant) and by tube (reaction/pool, APT) tabs  |
| **RFR** | **Run Form Response** | Spreadsheet for logging and correcting run-related data from submissions of Google Form "Run Form". |
| **RTR** | **Referral Test Report** | Spreadsheet for tracking and documenting referral test cases. |
| **RSR** | **Result Stats Report** | Spreadsheet for logging weekly compiled stats using a Google Form |
| **STS** | **Stats Table Summary** | Spreadsheet for data previously extracted and compiled for which we no longer have the raw data files (APS, RFR, or RSR) |
| **PHI** | **Protected Health Information** | Sensitive personal data that must be de-identified or stored on the "Limited PHI drive." |

#### Specialized Terms
| Term | Meaning | Context |
| ----- | ----- | ----- |
| **ARF Tubes** | Tubes present in the Run Form data but absent from Appivo, which are created and assigned ARF Tube IDs to be included in the dataset. | Run reconciliation process; appears in APS Tubes import tab. |
| **Note Names** | A field or process step in the APS correction workflow used to associate a tube with the correct participant name, often to resolve missing or inconsistent names. | Glossary, APS Row Delete, Add Note Names process. |
| **Person ID / DeID Key** | A unique identifier assigned to each individual participant; the DeID Key is the mapping used for the de-identification process. | Glossary, APS De-Identify process. |
| **Reaction Sequence** | All reactions from a **Collection Tube** (initial run and all re-runs) for a single session, which forms the **Session Call**. | RFR Reaction Table Criteria. |
| **Session Call** | The final result for a given **Collection Tube** and session, determined by the complete **Reaction Sequence**. | RFR Reaction Table Criteria. |
| **Collection Tube** | A physical tube identified by a **Tube ID** and associated with a session. | RFR Reaction Table Criteria. |
| **Case Cluster** | A group of related cases, such as a family pool that tested positive, where contributors are subsequently deconvoluted and tested individually. The original pool tube serves as the initial case identifier. | RTR referral test tracking. |


## Data Processing Flow
The pilot data processing pipeline involved multiple stages of cleaning, reconciliation, and quality tracking across several interconnected spreadsheet types. Changes at each step were tracked using standardized reason codes in dedicated spreadsheet columns.

#### APS (Appivo Samples) Processing
The starting point for most pilot sites was raw data exported from the Appivo mobile app, which appears in two pink-colored tabs in the APS spreadsheet: "raw APS" (one row per participant-tube combination) and "raw APT" (one row per tube). An early issue was that some tubes appeared in APT but not APS, typically tubes where only free-text "note names" were entered by the collection sponsor rather than a registered participant name. A process was developed to identify and add these APT-only tubes to the dataset.

The processing followed these steps:

1. **Pre-Delete PHI tab** — The full participant-level list of all Tube IDs, located in the PHI version of the spreadsheet. Each pooled tube has one row per participant (e.g., a 4-person pool produces 4 rows sharing the same Tube ID).
2. **Tube Deletion** — Tubes were flagged for removal using standardized reason codes. Common reasons included app testing artifacts (tubes scanned or entered during testing of the app itself). All deletion decisions were tracked via codes in the spreadsheet columns.
3. **Post-Delete tab** — The dataset with all flagged tubes removed.
4. **APS Tubes tab** (blue) — A rolled-up view with one row per tube rather than one per participant, including the collection sponsor name but not individual participant names.

The Stats and REF Weekly tabs at the beginning of the APS spreadsheet were populated after the run reconciliation process described below.

#### RFR (Run Form Report) Processing
The RFR captures data from the person performing the testing. After completing a run, the tester scanned their paper run form and uploaded it via a Google Form, along with photos of the reaction tubes and answers to questions about tube counts. An optional third image, a "lookup map" listing all Tube IDs in the run, was sometimes included, particularly for positive or inconclusive tubes and for reruns.

The primary data tab is "RFR Data - preExcl" (pre-exclude). Very few rows from the raw Google Forms export were excluded; those that were had been clearly noted as submission errors in the response notes, typically followed by a corrected resubmission.

A full RFR audit was then conducted: all images of paper run forms and reaction tubes were reviewed, errors were corrected, and inconsistencies identified. All changes were tracked with codes, notes, and comments. Differences in how sites filled out the forms, including systematic errors at some sites, made this audit step essential.

#### Run Reconciliation
The run reconciliation process matched RFR runs to APS tubes for sites that had both data types. The key task was reconciling tube counts between the two datasets. Common complications included:

- Tubes collected the evening before a run being associated with the following day's run
- Unresulted (null-result) tubes in APS, most of which could be determined as negative through run reconciliation and tube count matching
- RFR runs containing tubes absent from the APS/Appivo data, for which ARF Tube IDs were created (a relatively small number overall)
- Runs not captured in the RFR data, which received run IDs with an "_APS" suffix, assigned in the rightmost columns of the APS Tubes import tab

#### RFR Output and Cross-Checking
After reconciliation, the RFR spreadsheet's purple "All Tube Results" tab contains the final Tube ID-to-run ID mapping, along with run date, collection date, final result, and pool level. The "Runs Compare" tab provides side-by-side views of run data organized by run ID and by APS collection date, serving as a cross-check on counts of positives, negatives, and inconclusives across pipeline stages.

#### Final Rollup
Data was rolled up into Stats and Weekly tabs. The Stats tab typically resides in the APS file and the Weekly tab in the RFR. The APS file also includes a "REF Weekly" tab that references the weekly data, and a "POS and INCL" tab containing data for positive and inconclusive tubes only.

#### RTR (Referral Test Report) Processing
The RTR collected follow-up testing data, typically antigen or PCR tests, and sometimes other rapid LAMP tests. The "Referral Test Data" tab has one row per referral test. The "Referral Test by Person" tab rolls this up to one row per person, with columns for up to three sequential referral tests (type and result each). A "case cluster" groups related cases — for example, a family pool that tested positive where contributors were subsequently deconvoluted and tested individually. The original pool Tube ID serves as the initial case identifier for the cluster.

While column structure and lookup logic were applied to the referral test data, a fair amount of ad hoc manual processing was still required to extract the standardized metrics presented in the Stats tab.

#### RSR (Run Stats Report) and STS (Stats Table Summary)
For programs that did not use the Run Form (Coral Springs, ROSA, Davie, Kent, and FTFC), Run Form Reports could not be created. For the three earlier programs — Coral Springs, Davie, and ROSA, which began in fall 2021 — a Run Stats Report (RSR) Google Form was used for weekly reporting of test counts and results by program testers or administrators, who were otherwise tracking results in their own spreadsheets.

The STS files contain aggregated data from an earlier tracking system that predated the APS/RFR pipeline. For Kent (Camp Kenmont), data was reconstructed from an extracted Appivo dataset; Appivo had been used but the raw APS file was not created. For FTFC, the Appivo data was kept separate from Google Drive for privacy reasons and was subsequently lost. Aggregated numbers were available, however, and there were no positives during the brief testing period.


## Program Specific Comments
#### ABRM - Abrome K-12 School in Austin, TX
Abrome has one of the most complete datasets, including all three key file types: APS, RFR, and RTR.

#### BEND - Bend Fire and Rescue/EMS in Bend, OR
Bend is missing the RTR because referral testing was communicated by correspondence and was relatively straightforward: all FloodLAMP positives were confirmed by same-day lab PCR. Of the two inconclusive results, one was confirmed positive and one negative, as verified in a recent follow-up email to the program administrator.

#### COMB - Combate TV Show Production in Miami, FL
The referral data came in a separate spreadsheet from the program administrator and was processed into the standard RTR format.

#### COSP - Coral Springs City Municipal/EMS in Coral Springs, FL
This is the largest dataset. It has APS data but no RFR data because they did not use the Run Form. One of the challenges with this dataset was that a large number of participants were entered via note names, often with inconsistent spellings. Reconciling these was a laborious process. A lesson learned is that automating this with fuzzy name matching against a running participant list would be a valuable improvement.

#### CRLN - Carillon Pre-School in Portola Valley, CA
See FLMP.

#### DAVI - Town of Davie Fire/EMS in Davie, FL
Davie did not use Appivo, but the tester took extensive data, likely kept in private spreadsheets. The tester reported what appears to be very reliable data in the Run Stats Report on a weekly basis. They also provided a detailed antigen comparison dataset via spreadsheet.

#### FLMP - FloodLAMP (includes CRLN and FLSP)
This was the most challenging program to sort out and reconcile. Not only were Carillon and FloodLAMP Staff Plus intermingled for a period, but the complexity of the pooled testing, positive follow-up, deconvolution, and reruns from Carillon was challenging even with FloodLAMP's own staff and the overall completeness of the data. The fact that this was FloodLAMP's own program using its own system reveals our operational challenges, but it's also the case that the data is inherently complex. We very much had the need for improved software and systems for this type of self-pooled surveillance testing.

#### FLSP - FloodLAMP Staff Plus Other Community
See FLMP.

#### FTFC - Eagles/EMS Leadership Conference in Ft. Lauderdale, FL
This data is straightforward, covering just a few days of testing with no positives. As noted above, none of the APS, RFR, or RTR data were available; the data came from previously compiled stats that originally derived from Appivo data that was subsequently lost.

#### KENT - Camp Kenmont Youth Camp in Kent, CT
There is a separate App Data import file that was found during the archive process. This file is not included in the archive but is the source from which the data is derived.

#### NDHM - Needham Beth Shalom School in Needham, MA
Needham has APS and RFR but no RTR because there were no positives, and therefore no follow-up testing.

#### ROSA - ROSA TV Production in Davie, FL
There is APS data for ROSA but no RFR or RTR. FloodLAMP had very little contact with the program administrator, though an email was sent during the archive process to inquire about referral testing for the single positive, which was confirmed positive by a same-day antigen test.


## Data Commentary
The FloodLAMP pilot data was a giant mess. Wrangling it to its current state was a substantial undertaking requiring far more rounds of cleaning and reconciliation than anticipated. In retrospect, spreadsheets were not the right tool for this level of complexity.

A key reason why the data work was so challenging was core tension was between flexibility and standardization. FloodLAMP provided program testers and administrators with flexible data entry options, such as the ability to add participant "note names" for individuals not yet registered in Appivo. And did not force programs to use our tools (including the app). While practical in the field, this introduced significant downstream reconciliation work to match those entries to existing participant records. In hindsight, that reconciliation effort might have been limited to positive and inconclusive cases only.

Run reconciliation was further complicated by tubes collected the evening before a testing run, combined with days that included multiple initial runs and reruns — distinctions that were not captured in the original data collection design, either in Appivo or the Google Forms.

For anyone interested in pooled self-collection testing, the challenges documented in this data may offer useful insights. However, the entire data collection and processing infrastructure would look fundamentally different if built today. AI capabilities — from AI-assisted software development to natural language processing, transcription, and automated data auditing — provide the leverage that was missing during FloodLAMP's operations. The primary gap was not conceptual but practical: the staffing, funding, software experience, methods, and tooling needed for continuous data quality monitoring. Those tools are now far more accessible, making dealing with even data as ugly as ours far less painful..


# 8,282  _context-commentary_pilots-pilot-data.md
METADATA
last updated: 2026-02-26 RT
file_name: _context-commentary_pilots-pilot-data.md
category: pilots
subcategory: pilot-data
words: 5655
tokens: 8282


CONTENT

## Context
#### Aggregate of All Pilot Programs
Start Run Date: 2020-12-11
End Run Date: 2023-06-02
Number of Tubes Tested (initial only - no re-runs): 16,209
Number of Participant Results: 37,706
Number of Tubes with Final Result Positive: 884
Number of Unique Individuals Tested: 2,752

#### ABRM - Abrome K-12 School in Austin, TX
Start Run Date: 2022-09-05
End Run Date: 2023-06-02
Number of Tubes Tested (initial only - no re-runs): 1,379
Number of Participant Results: 2,954
Number of Tubes with Final Result Positive: 8
Number of Unique Individuals Tested: 87
Test Operator: Abrome School
Test Processing Site: Office
Population Tested: Students, Staff, Families
Configuration: Mini w water bath
Collection Type: Pooled Household
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person
Program Name: Abrome
Site: Abrome School
Site Type: K-12 School
Location: Austin, TX

#### BEND - Bend Fire and Rescue/EMS in Bend, OR
Start Run Date: 2021-12-10
End Run Date: 2022-05-11
Number of Tubes Tested (initial only - no re-runs): 772
Number of Participant Results: 767
Number of Tubes with Final Result Positive: 71
Number of Unique Individuals Tested: 187
Test Operator: Bend Fire and Rescue
Test Processing Site: Office Space
Population Tested: First Responders, Staff
Configuration: Double Mini
Collection Type: Individual
Self or HCW Collected: HCW
App Used?: Yes
Bring-up Type: Remote (NSVD Volunteer)
Program Name: Bend
Site: Fire Station
Site Type: Fire Dept / EMS
Location: Bend, OR

#### COMB - Combate TV Show Production in Miami, FL
Start Run Date: 2022-03-20
End Run Date: 2022-08-15
Number of Tubes Tested (initial only - no re-runs): 1,981
Number of Participant Results: 1,672
Number of Tubes with Final Result Positive: 14
Number of Unique Individuals Tested: 369
Test Operator: FloodLAMP
Test Processing Site: Hotel room
Population Tested: Martial artists, Production Staff
Configuration: Standard
Collection Type: Individual
Self or HCW Collected: HCW
App Used?: Yes
Bring-up Type: In Person
Program Name: Combate
Site: Embassy Hotel
Site Type: Production Organization
Location: Miami, FL

#### COSP - Coral Springs City Municipal/EMS in Coral Springs, FL
Start Run Date: 2021-08-31
End Run Date: 2022-03-07
Number of Tubes Tested (initial only - no re-runs): 7,146
Number of Participant Results: 22,643
Number of Tubes with Final Result Positive: 347
Number of Unique Individuals Tested: 1,074
Test Operator: City of Coral Springs
Test Processing Site: Office Space
Population Tested: EMS, First Responders, City Staff
Configuration: Double Standard
Collection Type: Pooled
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person
Program Name: Coral Springs
Site: Municipal Building
Site Type: City / EMS
Location: Coral Springs, FL

#### CRLN - Carillon Pre-School in Portola Valley, CA
Start Run Date: 2021-12-24
End Run Date: 2022-05-31
Number of Tubes Tested (initial only - no re-runs): 1,016
Number of Participant Results: 2,340
Number of Tubes with Final Result Positive: 32
Number of Unique Individuals Tested: 142
Test Operator: FloodLAMP
Test Processing Site: Garage Dedicated Room
Population Tested: Students, Staff, Families
Configuration: Standard
Collection Type: Pooled Household, Individual
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person
Program Name: Carillon
Site: Preschool
Site Type: Preschool
Location: Portola Valley, CA

#### DAVI - Town of Davie Fire/EMS in Davie, FL
Start Run Date: 2021-09-01
End Run Date: 2022-03-18
Number of Tubes Tested (initial only - no re-runs): 2,279
Number of Participant Results: 4,409
Number of Tubes with Final Result Positive: 384
Test Operator: Davie Fire and Rescue
Test Processing Site: Fire Station Office
Population Tested: EMS, First Responders, City Staff
Configuration: Standard
Collection Type: Pooled
Self or HCW Collected: Self
App Used?: No
Bring-up Type: In Person
Program Name: Davie
Site: Fire Station
Site Type: City / EMS
Location: Davie, FL

#### FLMP - FloodLAMP (includes CRLN and FLSP)
Start Run Date: 2020-12-11
End Run Date: 2023-01-02
Number of Tubes Tested (initial only - no re-runs): 1,540
Number of Participant Results: 3,399
Number of Tubes with Final Result Positive: 57
Number of Unique Individuals Tested: 212
Test Operator: FloodLAMP
Test Processing Site: Various
Population Tested: Staff, Students, Families, Community
Configuration: Various
Collection Type: Pooled Household, Individual
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person
Program Name: FloodLAMP
Site: Various
Site Type: Various
Location: Portola Valley, CA

#### FLSP - FloodLAMP Staff Plus Other Community
Start Run Date: 2020-12-11
End Run Date: 2023-01-02
Number of Tubes Tested (initial only - no re-runs): 524
Number of Participant Results: 1,059
Number of Tubes with Final Result Positive: 25
Number of Unique Individuals Tested: 70
Test Operator: FloodLAMP
Test Processing Site: Biolab, Garage, Office
Population Tested: Staff, Community
Configuration: Various
Collection Type: Pooled Household, Individual
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person
Program Name: FloodLAMP Staff Plus
Site: MBC Biolabs and Home Garage
Site Type: Company
Location: San Carlos, CA

#### FTFC - Eagles/EMS Leadership Conference in Ft. Lauderdale, FL
Start Run Date: 2021-06-14
End Run Date: 2021-06-18
Number of Tubes Tested (initial only - no re-runs): 61
Number of Participant Results: 195
Number of Tubes with Final Result Positive: 0
Number of Unique Individuals Tested: 195
Test Operator: FloodLAMP
Test Processing Site: Hotel Storage Room
Population Tested: EMS, Conference Attendees
Configuration: Standard
Collection Type: Pooled & Individual
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person
Program Name: FTFC
Site: Hard Rock Hotel
Site Type: Conference
Location: Ft. Lauderdale, FL

#### KENT - Camp Kenmont Youth Camp in Kent, CT
Start Run Date: 2021-06-28
End Run Date: 2021-07-29
Number of Tubes Tested (initial only - no re-runs): 190
Number of Participant Results: 696
Number of Tubes with Final Result Positive: 2
Number of Unique Individuals Tested: 342
Test Operator: Volunteers, Camp Staff
Test Processing Site: On Site Room
Population Tested: Young Adult Campers, Staff
Configuration: Standard
Collection Type: Pooled
Self or HCW Collected: HCW
App Used?: Yes
Bring-up Type: Remote (NSVD)
Program Name: Kent
Site: Camp Kenmont
Site Type: Youth Camp
Location: Kent, CT

#### NDHM - Needham Beth Shalom School in Needham, MA
Start Run Date: 2022-05-02
End Run Date: 2022-10-03
Number of Tubes Tested (initial only - no re-runs): 80
Number of Participant Results: 190
Number of Tubes with Final Result Positive: 0
Number of Unique Individuals Tested: 130
Test Operator: Needham Beth Shalom School
Test Processing Site: Office Space
Population Tested: Students, Staff, Families
Configuration: Standard
Collection Type: Pooled Household
Self or HCW Collected: Self
App Used?: Yes
Bring-up Type: In Person & Remote
Program Name: Needham
Site: Needham Beth Shalom School
Site Type: K-12 School
Location: Needham, MA

#### ROSA - ROSA TV Production in Davie, FL
Start Run Date: 2021-09-28
End Run Date: 2021-12-17
Number of Tubes Tested (initial only - no re-runs): 781
Number of Participant Results: 781
Number of Tubes with Final Result Positive: 1
Number of Unique Individuals Tested: 156
Test Operator: Davie Fire and Rescue
Test Processing Site: Office
Population Tested: TV Production Staff
Configuration: Standard
Collection Type: Individual
Self or HCW Collected: HCW
App Used?: Yes
Bring-up Type: In Person
Program Name: Rosa
Site: Production Set / Fire Station
Site Type: Production Organization
Location: Davie, FL

## Commentary
#### FLMP - FloodLAMP (includes CRLN and FLSP)
The FLMP designation exists because the Carillon (CRLN) and FLSP (FloodLAMP Staff Plus) programs shared a single tenant in the FloodLAMP app software, and their testing runs were intermingled. Each tube was assigned to either Carillon or FLSP based on whether the participants belonged to or were associated with the Carillon preschool community. For the FloodLAMP founders' family and household staff, the assignment was date-based: during the dates the Carillon program was active, samples were attributed to Carillon; outside those dates, to FLSP. Substantive commentary for these overlapping programs appears under their respective entries below.

#### FLSP - FloodLAMP Staff Plus Other Community
FLSP served as the catch-all program for FloodLAMP's internal staff testing plus friends, family, neighbors, co-workers, and other community members tested over the course of operations. The program start date was set at December 2020, when data collection began and the test had stabilized on the direct, no-purification protocol used going forward. Testing was conducted from multiple locations: the main lab at MBC BioLabs in San Carlos, California; a home garage lab in Portola Valley; the 2022 Portola Valley office space; and several pop-up sites.

The internal testing program produced several notable case studies. In multiple instances, routine screening unexpectedly detected positive cases among FloodLAMP staff, and the early detection appeared to contribute to preventing further spread within the company and within household contacts.

##### Case Study 1 — FloodLAMP Founder (December 2021)
The founder (Randy True) contracted COVID-19 at a holiday gathering during the Omicron surge ramp-up. He was participating in every-other-day pooled screening with staff and tested negative on the morning symptoms first appeared. A pooled test run the following morning (skipping one day) returned positive, and a rapid antigen test confirmed the result immediately. He was able to isolate before anyone else in the household became infected, and no one else in the household tested positive. While this case demonstrated the value of early detection through routine screening, it also illustrates a limitation: with every-other-day testing, The more sensitive FloodLAMP test caught the infection at the same point as a less sensitive rapid antigen test.

See: pilots/pilot-data/FLSP_pilot-data/2021-12-28_Case Report - Randy.md

##### Case Study 2 — New Year's Eve (December 31, 2021)
This case presented a more striking comparison between FloodLAMP and other FDA authorized commercial tests that missed it. 

This is easiest to review visually.
See: pilots/pilot-data/FLSP_pilot-data/2022-01-01_Case Report - New Years Eve.md

An individual nasal swab collected at 9 a.m. on December 31st tested positive on the FloodLAMP colorimetric LAMP test, and PCR run on the same TCEP-inactivated sample confirmed the result. However, subsequent testing that same afternoon using a rapid antigen test (BinaxNOW), Lucira, and Detect were all negative. A 5 p.m. resampling showed the infection presenting more strongly in a throat swab (CT 30.2) than the nasal swab (CT 39.4 on one of three PCR replicates, with the other two undetermined), suggesting low and variable viral load distribution. A saliva sample collected later that evening had a CT of 28.

The following day, New Year's Day, nasal and throat samples were positive on FloodLAMP and PCR but negative on BinaxNOW antigen. An Accula rapid molecular test (PCR-based, 30-minute cartridge with lateral flow readout) administered at an airport testing site was also negative. It was not until the morning of January 2nd that two different antigen test brands (FlowFlex and BinaxNOW) finally returned positive results, confirming the FloodLAMP detection approximately 48 hours earlier.

This case illustrates the variability across FDA-authorized testing modalities, a finding consistent with the FDA's own SARS-CoV-2 Reference Panel results, which showed unexpectedly large differences from the sensitivity figures reported in EUA submissions (see: regulatory/fda-policy/FDA SARS-CoV-2 Reference Panel Comparative Data - Complied by Matt McFarlane.md; regulatory/fda-policy/2023-09-23_FDA Response Letter - To Compliant regarding FDA Reference Panel from Dec 2020.md).

FloodLAMP developed its LAMP and PCR tests to run from the same TCEP-inactivated sample, as submitted to the FDA in March 2021. This dual-test capability proved particularly valuable for cases requiring additional confirmation (see: data/floodlamp/regulatory/fl-fda-submissions; data/floodlamp/various/fl-presentations/BARDA Market Research - FloodLAMP Presentation (2022-03-07).md, slides 46–50).

Over the full span of the FLSP program, staff testing detected four confirmed COVID-19 cases (the founder, one staff member, a domestic partner of a staff member, and the New Year's Eve case). In each instance, the case was caught early and no other FloodLAMP staff tested positive in the period immediately following. The program's primary value was as a longitudinal demonstration that routine molecular screening of a small, closely interacting group can detect infections early enough to interrupt transmission.

#### CRLN - Carillon Pre-School in Portola Valley, CA
The Carillon program is documented in detail in FloodLAMP's most comprehensive white paper (see: various/fl-whitepapers/FloodLAMP Whitepaper - California Preschool Family Pooled Screening Pilot (June 2022).md and various/fl-whitepapers/_context-commentary_various-fl-whitepapers.md).

Carillon was a small preschool in Portola Valley, California, attended by the children of FloodLAMP founders Randy True and Theresa Ling. The founders' familiarity with the school's staff facilitated the program launch. As the Omicron surge arrived in December 2021, existing discussions about a testing program turned into concrete plans, and the program was set to begin immediately after the holiday break.

The close relationship with the school enabled program features that were likely rare, or possibly unique, among pandemic-era COVID-19 screening programs. Families were onboarded before the first day of testing with signed consent and pooled collection kits (five to ten per family). A dropbox at the school entrance served as both a sample drop-off point and a kit pickup location. Families registered pooled collections through the FloodLAMP app, identifying all participants including siblings and household members such as nannies or grandparents. The typical daily workflow was straightforward: families collected samples the morning of school and dropped them off at the same time as their children. A FloodLAMP team member collected all kits from the dropbox within minutes of the morning drop-off and drove them home (approximately five minutes) for processing, with results available the same day. No extra transportation or trips were required from participating families.

A trade-off of this model was that children were already at school when results became available. Follow-up testing and confirmatory information was received for some cases but not all.

The program demonstrated its value immediately. Before the first day back from the holiday break, families dropped off samples the evening prior. Two pools tested positive that night, both asymptomatic and both subsequently confirmed. The same pre-screening approach was used successfully after spring break. These involved an extra trip to the school for drop-off but significantly increased the effectiveness of the program.

One confirmed case involved a teacher who had tested negative on antigen tests for three consecutive days following known household exposure, came to school believing they were clear, and tested positive on FloodLAMP the same day, and was confirmed by a lab PCR test. Either the timing of viral load ramp-up or the increased sensitivity of the molecular test accounted for the detection difference; regardless, the screening program identified the case before further classroom exposure occurred.

A documented case report describes one asymptomatic family pool detected on the first day back from the holiday break. Individual deconvolution the following day showed both parents positive and both children negative; the children turned antigen-positive the next day. All four family members were confirmed by PCR (results took one to two days). Return testing beginning a week later showed persistent FloodLAMP positivity: 15 days after the initial positive pool result, the family pool was still positive on FloodLAMP while all members tested negative on antigen (see: pilots/pilot-data/FLMP_pilot-data/2022-01-02_Carillon Case Report of Asymptomatic Positive Family Pool.md).

In total, the program identified eight positive pools or case clusters. Of the six with deconvolution or confirmatory referral test results, the positive individual was the school-aged child in half of cases and a parent or sibling in the other half.

The Carillon program implemented several features that FloodLAMP considered most valuable in a screening program: multi-week longitudinal surveillance, household pooling, fast same-day turnaround, and deconvolution capability. Operating it within the founders' own school community provided an unusually close perspective on the day-to-day logistics and family experience of this type of program.

#### FTFC - Eagles/EMS Leadership Conference in Ft. Lauderdale, FL
The FTFC conference in June 2021 was FloodLAMP's first significant external testing event and served as the entry point into the EMS and municipal surveillance pilots that followed (Coral Springs, Davie, and Bend). FloodLAMP staff flew from California with all lab materials in two suitcases and set up a pop-up lab in a storage room at the Hard Rock Hotel in Fort Lauderdale. A freezer and refrigerator were available on-site (possibly ordered via Amazon, though this detail is uncertain). A volunteer graduate student, was trained to run the test, freeing FloodLAMP staff for sample collection and conference interaction.

Testing was offered as a voluntary service and as a chance to learn about our program, operating as a hallway booth with signage. Participation was lower than anticipated. June 2021 represented a low point in pandemic prevalence, many attendees viewed the pandemic as winding down, masks were rarely worn, and Florida maintained a relatively lax COVID-19 posture. FloodLAMP had prepared to run thousands of samples but processed only 61 tubes covering approximately 195 individuals over three days. There were no positive or inconclusive results.

The testing was conducted in collaboration with two nonprofits: the Research Aid Network and the National Scientist Volunteer Database (NSVD). FloodLAMP gave a short invited talk to EMS leadership (see: various/fl-presentations/FTFC EMS Conference - FloodLAMP Talk Slides (6-14-2021).md). The conference was where FloodLAMP trained Dr. Peter Antevy, who became the Program Medical Director for FloodLAMP and was our main contact in the EMS world. Dr. Antevy purchased the testing equipment (approximately $7K), which was subsequently shipped to the Kent Camp pilot.

Despite the low testing volume, the FTFC conference yielded valuable EMS leadership contacts and practical experience deploying a pop-up laboratory, both of which directly contributed to FloodLAMP's subsequent pilot programs.

#### KENT - Camp Kenmont Youth Camp in Kent, CT
The Kent Camp pilot was FloodLAMP's first fully remote deployment, with no FloodLAMP staff traveling to the site. Dr. Peter Antevy trained approximately three graduate student volunteers recruited through the National Scientist Volunteer Database (NSVD), co-founded by FloodLAMP's COO. These volunteers performed all on-site testing.

A positive COVID-19 case was identified among incoming campers through initial PCR testing. In the period between testing and arrival, other campers had been exposed, creating an immediate need for on-site screening capability before the camp session began. The FloodLAMP testing was used alongside antigen testing and was reported to be helpful. The known positive sample also served an unplanned validation role: a shipping issue (likely warming during transit) compromised the frozen positive control material that FloodLAMP normally provides, making the known positive case a useful substitute for test verification.

Surveillance screening was conducted in two planned sessions, apparently covering two different cohorts of campers. Samples were processed in a single 96-well reaction plate. Besides the known positive, no additional positives were detected.

The Kent pilot demonstrated the feasibility of a remote bring-up model without FloodLAMP staff on-site. Its primary contribution was showing that fast-turnaround on-site molecular screening capability could be established remotely with trained volunteer support.

#### COSP - Coral Springs City Municipal/EMS in Coral Springs, FL
Coral Springs (population ~140,000) in south Florida was FloodLAMP's first major paid pilot and largest testing program by total volume. FloodLAMP staff traveled from California with equipment and consumables, set up a pop-up lab in an empty medical office, ran a successful validation, and trained one firefighter with no prior lab or pipetting experience.

The program started in September 2021 with modest volumes: 25 tubes covering 90 participants over the first three months. When the Omicron surge hit in mid-December, the program expanded rapidly to cover most essential first responder and municipal staff. At peak, Coral Springs ran 800 tubes per week covering 2,600 participants (includes repeated testing of the same population), with multiple collection points across city buildings, police stations, and fire stations. Two staff members operated two inactivation and amplification stations ("double standard" configuration), running LAMP reactions in 96-well plates. During the December–January surge, the site ran three to four FloodLAMP processing runs per day to cover three emergency responder shifts, operating seven days a week.

One significant limitation in the Coral Springs data is the absence of comparator testing data. The site reportedly had extensive antigen comparison data for all FloodLAMP positives, but FloodLAMP was unable to secure its release. In retrospect, de-identified data publication rights should have been included in the contract.

The available anecdotal evidence is nonetheless informative. The lead tester described a plate with 22 positive results, an unusually high number that he verified by rerunning the samples with identical results. Of those 22, only one was positive on same-day BinaxNOW rapid antigen testing. The remaining 21 antigen-negative individuals returned to work, but two days later "everybody started popping positive," with most having previously tested positive by FloodLAMP. The site concluded that BinaxNOW was less sensitive than FloodLAMP for early detection. This observation was consistent with findings from other FloodLAMP pilot sites and is not unexpected given the known sensitivity gap between molecular and antigen testing at low viral loads.

Testing ended abruptly in late February 2022 as the Omicron wave passed through the community.

#### DAVI - Town of Davie Fire/EMS in Davie, FL
The Town of Davie (population ~110,000), located adjacent to Coral Springs in south Florida, shared the same Medical Director who connected both programs to FloodLAMP. The firefighter trained at Coral Springs subsequently trained the Davie tester, also a veteran firefighter, with supplementary early-morning support calls from FloodLAMP's founder. A single individual performed all testing at the Davie site.

The program timeline paralleled Coral Springs: modest volumes averaging approximately 30 tubes and 80 participants per week from September through November 2021, followed by rapid expansion during the Omicron surge. Testing peaked at approximately 500 tubes per week in early January 2022, with positivity rates reaching 34% during the peak week.

Feedback from the site regarding program effectiveness was consistently positive. One reported case illustrated the operational value of pooled screening with deconvolution capability: a leadership member's family pool tested positive, and the site immediately resampled and ran individuals on FloodLAMP to identify the positive member. The combination of confidence in test performance and operational flexibility was what the site valued most. Program success led to expansion in mid-November 2021, extending FloodLAMP testing from EMS personnel to all Town of Davie municipal employees on a voluntary daily or weekly basis, with six designated collection points and daily pickup by Fire Rescue staff.

The Davie site produced the archive's most detailed head-to-head comparison between FloodLAMP and BinaxNOW rapid antigen testing, tracking 51 employee cases through three evolving testing protocols during the Delta and Omicron waves (see: pilots/pilot-data/DAVI_pilot-data/DAVI_pilot-data_referral-antigen-comparison.md):

- **Group 1** (15 employees, Sep 15 – Dec 23): FloodLAMP as primary test; BinaxNOW used sometimes at home on Day 0.
- **Group 2** (22 employees, Dec 24 – Jan 9): Both tests used throughout until return-to-work clearance, providing the most informative direct comparison data.
- **Group 3** (14 employees, Jan 10 – Feb 7): FloodLAMP for initial detection; BinaxNOW for return-to-work clearance.

Across cases with same-day results, FloodLAMP and BinaxNOW agreed 90% of the time. In the remaining 10% (four employees), FloodLAMP detected the infection while BinaxNOW did not; three of those four were asymptomatic. There were zero cases where antigen testing detected a positive that FloodLAMP missed. During the intensive dual-testing phase (Group 2), the two tests generally tracked closely and cleared on the same day, with an average time to negative of approximately 9 days. The divergence was concentrated at infection onset, particularly in asymptomatic or low-viral-load individuals, which is the detection gap that molecular screening is designed to address. The program reported zero false positives and zero suspected false negatives, with 98% of FloodLAMP positives confirmed by referral or correspondence.

The Davie comparison data, combined with the anecdotal report from Coral Springs (21 of 22 FloodLAMP positives antigen-negative but subsequently confirmed), reinforced a consistent finding across the pilot programs: BinaxNOW rapid antigen tests lagged FloodLAMP molecular detection at infection onset, especially in asymptomatic individuals. See pilot COMB below where the comparison with antigen tests showed significantly more positive cases identified by FloodLAMP but missed by antigen.

#### ROSA - ROSA TV Production in Davie, FL
The ROSA program was FloodLAMP's only third-party or affiliated pilot, in which another organization ran the FloodLAMP test commercially. "ROSA" is a pseudonym; FloodLAMP does not have permission to disclose the production company name.

All samples were run individually (no pooling), collected from TV show staff and actors on the production site, and shuttled to the Davie Fire and Rescue lab for processing. Processing was reportedly done promptly and separately from the Town of Davie staff samples. A dedicated COVID testing program manager at the production site administered the program, handling sample collection, app registration, and results management. FloodLAMP's involvement was limited primarily to digital and app support.

The program ran consistently at 50 to 100 samples per week for 11 weeks. No positives were detected until the final week, when one positive was identified and confirmed with a same-day antigen test. FloodLAMP had minimal involvement with this program.

#### BEND - Bend Fire and Rescue/EMS in Bend, OR
The Bend pilot was a follow-on EMS program resulting from the success of Coral Springs and Davie. Although FloodLAMP received significant interest from other EMS programs nationally, Bend was the only additional EMS site brought online.

Unlike Davie and Coral Springs, Bend tested only firefighters and EMS personnel, and all samples were run individually (no pooling). The primary motivation was dissatisfaction with the cost and turnaround time of PCR testing from a local lab.

The bring-up was conducted entirely remotely, without FloodLAMP staff traveling to Oregon. A local scientist volunteer, recruited through the National Scientist Volunteer Database, provided critical on-site support. The program began with a one-hour Zoom kickoff call with fire and emergency management leadership, followed by remote training with the volunteer scientist providing hands-on assistance. The remote training was challenging but proved effective (see: data/floodlamp/various/fl-presentations/Bend Pilot Program Bring-up (12-01-2021).md).

Positivity rates were high throughout January 2022 during the Omicron surge, ranging from 11% to 37%. All FloodLAMP positives were confirmed by the local PCR referral lab, with zero false positives. The program recorded two inconclusive results, one of which was positive by PCR and the other negative by PCR.

Bend purchased a "double mini" system: two small heaters accommodating up to 40 200μl PCR tubes each, run in strip tube format. This smaller configuration was feasible because individual (non-pooled) samples could be collected in 1.5 ml tubes, avoiding the 5 ml tubes required for 4-swab pooling (which necessitated water bath inactivation at the Davie and Coral Springs sites). FloodLAMP charged $2,800 for equipment and $6 per reaction for an initial order of 1,000 reactions ($4 for the test, $2 for the collection kit). The initial outlay was $8,800. A subsequent order of 1,000 reactions and a multi-channel pipette brought the total to approximately $15,000 including shipping.

The Bend EMS manager who administered the program described it as a "godsend."

#### COMB - Combate TV Show Production in Miami, FL
The Combate program was FloodLAMP's only surveillance-screening-as-a-service operation, in which FloodLAMP employees directly performed all testing. An experienced nurse was hired and trained on the FloodLAMP test. This person administered the program, collected samples, ran testing, and managed a trained assistant.

The pop-up lab was established in a carpeted hotel room within the TV program's accommodations, which was not an ideal laboratory environment and raised initial contamination concerns. With rigorous cleaning protocols and attention to detail, the program operated for over four months without significant contamination problems.

Testing was individual (no pooling), using 1.5 ml tubes, with approximately 100 people tested per week. The negotiated price was $35 per test all-in with a minimum of 150 tests per week ($5,250 per week). The initially discussed price was significantly higher but was negotiated downward over the months leading up to the program starting. Given staffing costs, including testing staff salaries and a prorated share of FloodLAMP scientist support time, it is likely that FloodLAMP did not recoup its costs on the contract.

##### Comparison with Antigen Tests (AI generated - Opus 4.6)
The testing results were informative for FloodLAMP vs. antigen comparison. The COMB data tells a dramatically different story from DAVI. The key numbers are right in the stats table:
**COMB (Combate) -- FL positive vs. antigen comparison:**
- 11 FloodLAMP positive/inconclusive cases with same-day antigen referral tests
- **6 antigen positive (54.5%)**
- **5 antigen negative (45.5%)**

Nearly half of FloodLAMP positives were missed by antigen -- compared to DAVI's 10%.

The referral-tests-by-person table at the bottom of the file lets us see each case individually:

| Employee | FL Result | Antigen Result | Confirmed by | FL+/Ag outcome |
|---|---|---|---|---|
| COMB170110 | Positive | Positive | -- | Agree |
| COMB213226 | Positive | Positive | -- | Agree |
| COMB242905 | Positive | **Negative** | Lab PCR Positive | FL caught it |
| COMB353066 | Positive | **Negative** | Lab PCR Positive | FL caught it |
| COMB413047 | Positive | Positive | -- | Agree |
| COMB596496 | Inconclusive | **Negative** | Lab PCR Positive | FL caught it |
| COMB704360 | Positive | **Negative** | Lab PCR Positive | FL caught it |
| COMB724402 | Inconclusive | Positive | -- | Agree |
| COMB770137 | Positive | Positive | -- | Agree |
| COMB945952 | Positive | **Negative** | Lab PCR Positive | FL caught it |
| COMB638337 | ARF Positive | Positive | -- | Agree |

All 5 antigen-negative cases were subsequently confirmed by lab-purified PCR. Zero false positives. The COMB protocol was systematic: FL first, then antigen; if antigen disagreed, send for lab PCR. That protocol gives us high confidence in these numbers.

**Why so much higher than DAVI?** A few likely factors:

1. **Testing context.** COMB was HCW-collected individual surveillance of a production crew -- likely catching people very early through routine screening before symptoms developed. DAVI had more symptomatic diagnostic testing mixed in (especially Groups 2 and 3, where many employees were already symptomatic at Day 0).

2. **Low positivity rate.** COMB's overall positivity was just 0.7% (14 positives out of 1,981 tubes). At low prevalence with routine screening, the cases you do find tend to be earlier in infection with lower viral loads -- exactly where antigen underperforms.

3. **Time period.** COMB ran March--August 2022, a lower-prevalence period compared to DAVI's Omicron surge. Finding cases during low-prevalence periods often means catching them at the earliest detectable stage.

**Side by side:**

| Site | Same-day comparisons | Antigen + | Antigen - | % Antigen Negative |
|---|---|---|---|---|
| DAVI | 42 | 38 | 4 | 10% |
| COMB | 11 | 6 | 5 | **45.5%** |

The COMB data is a much smaller sample (11 vs. 42), but the signal is strong and directionally consistent with the Coral Springs anecdote (21/22 antigen-negative). Taken together, these suggest that in surveillance contexts catching early/asymptomatic infections, the antigen miss rate can be very high -- far above DAVI's 10%, which was skewed by a large proportion of symptomatic cases who were easier for antigen to detect.

#### NDHM - Needham Beth Shalom School in Needham, MA
The Needham pilot was a small, late-stage program established through a connection via New England BioLabs, and provided free of charge. FloodLAMP's founder traveled to set up the lab and train the tester, a college student studying a bio-related field with some prior hands-on lab experience.

An office room in the school was dedicated to testing. By this point in FloodLAMP's operations, the setup process had matured and was straightforward, using the standardized four-drawer cart configuration. The program also used a recently implemented streamlined web onboarding process.

Participation was limited as prevalence was low in that area and at that point in the pandemic. Over the first four to six weeks, the program processed a few dozen samples per week, tapering off substantially afterward. The total volume was low: 80 tubes covering 130 unique individuals. This occurred during a period of declining case rates, which likely contributed to the drop-off in participation. No positive samples were detected during the program.

#### ABRM - Abrome K-12 School in Austin, TX
Abrome was a small alternative K-12 school in Austin, Texas. The school connected FloodLAMP to the Balvi grant organization and submitted for a Balvi grant that supported their system purchase.

Abrome operated the program for nine months (September 5, 2022 through June 2, 2023), running 1,379 initial tubes covering 2,954 participant results across 87 unique individuals. Testing was pooled by household with an average pool level of 2.2 individuals per tube, processed on-site using a mini water bath configuration. The program detected eight positive tubes corresponding to three distinct cases, with zero false positives or suspected false negatives.

The program's operational consistency was notable: testing was conducted on 95% of weekdays during 36 active school weeks (171 of 180 weekdays, with an effective uptime of 97% adjusting for holidays). This frequency of testing was unusual outside of significantly higher-budget screening programs.

FloodLAMP charged approximately $3,000 for equipment and system, plus $4 to $5 per test kit (reagents, consumables, collection tubes, and swabs). Abrome purchased 3,000 surveillance test kits, bringing the total program cost to approximately $20,000, including roughly $1,500 for in-person training and setup. The testing and administrative lead from the Combate program flew to Texas to set up the lab and conduct training.

The head of Abrome provided a written endorsement stating that the school emerged from 3.5 academic years of the pandemic without a known case of in-school transmission, crediting the FloodLAMP program with catching three instances of household infection before the student became infectious at school.

A documented case from December 2022 illustrates the detection model: a morning LAMP test flagged a positive household pool (two parents and one student), none of whom had symptoms. The student was immediately separated from the school. Within hours, one parent tested positive on rapid PCR; the student developed symptoms and tested positive two days later. No other Abrome students or staff tested positive, suggesting that the rapid detection and quarantine interrupted transmission to the school community.

Abrome's success was supported by conditions that may not be generalizable: a school culture that embraced mandatory daily testing, a small enough community for a single staff member to manage the program, and grant funding covering the full cost. These factors made Abrome an effective setting but also highlight the financial and cultural prerequisites for similar programs elsewhere.

# ===== END OF FILE _archive-combined-context-commentary_pilots_12k.md =====
