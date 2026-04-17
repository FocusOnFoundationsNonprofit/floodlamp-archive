METADATA
last updated: 2026-03-26 RT
file_name: _context-commentary_pilots-pilot-data.md
category: pilots
subcategory: pilot-data
gfile_url: https://docs.google.com/document/d/1B6YJLLIwFuu1lK_xPRisV_pEtoCNAswsE8gvO0kKebU
words: 3719
tokens: 5429


CONTENT

## Context

### Pilot Data Overview
The FloodLAMP pilot data (`pilots/pilot-data`) was collected across 11 surveillance testing programs in 6 states, drawing from three primary sources:
- **FloodLAMP mobile app** (built on the Appivo platform) — Used by participants and administrators for registering participants to barcoded collection tubes and for recording results. Not all sites used the app; usage varied across programs and was accompanied by varying degrees of completeness and data quality.
- **Google Forms** — A Run Form for logging run-related data after each testing run, and a weekly stats form for reporting aggregate numbers (samples, positives, etc.). See the Acronyms section below for details on the corresponding spreadsheet types.
- **Referral test data** — Information about non-FloodLAMP follow-up tests (typically antigen or PCR), communicated to FloodLAMP via email, text, or verbal reports.

The data underwent multiple rounds of cleaning and reconciliation, with all changes tracked in the spreadsheets using standardized codes. The processed data is available in Google Drive as Google-native spreadsheet files and as extracted CSVs. Summary markdown files containing key plots and data are also provided.

| Resource | Location |
| ----- | ----- |
| Google Drive master index | https://docs.google.com/spreadsheets/d/1b1uWHNGBL9yatTUNnzrbOTdWOMlD-XYVsn4V6pSYmmk |
| Filename listing | `Data PUB - Pilot Data Google Files - PUB Filenames` |
| URL listing | `Data PUB - Pilot Data Google Files - PUB URLs` |
| Aggregate summary | `aggregate_pilot-data/aggregate_pilot-data_summary` |

Video transcripts of data pipeline walkthroughs are included in `_docs_pilot-data`, and the code for generating summary markdown files and plots is in `_code_pilots-data`.


### Acronyms and Terms
#### Key Acronyms
| Acronym | Meaning | Context |
| ----- | ----- | ----- |
| **APS** | **Appivo Samples** | Spreadsheet of Appivo app extracted data with tabs by sample (participant) and by tube (reaction/pool, APT)  |
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
| **Session Call** | The final result for a given **Collection Tube** and session (initial run plus re-runs), determined by the complete **Reaction Sequence**. | RFR Reaction Table Criteria. |
| **Collection Tube** | A physical tube identified by a **Tube ID** and associated with a sample collection event. | RFR Reaction Table Criteria. |
| **Case Cluster** | A group of related cases, such as a family pool that tested positive, where contributors are subsequently deconvoluted and tested individually. The original pool tube serves as the initial case identifier. | RTR referral test tracking. |


### Data Processing Flow
The pilot data processing pipeline involved multiple stages of cleaning, reconciliation, and quality tracking across several interconnected spreadsheet types. Changes at each step were tracked using standardized reason codes in dedicated spreadsheet columns.

#### APS (Appivo Samples) Processing
The starting point for most pilot sites was raw data exported from the Appivo mobile app, which appears in two pink-colored tabs in the APS spreadsheet: "raw APS" (one row per participant-tube combination) and "raw APT" (one row per tube). An early issue was that some tubes appeared in APT but not APS, typically tubes where only free-text "note names" were entered by the collection sponsor rather than a registered participant name. A process was developed to identify and add these APT-only tubes to the dataset.

The processing followed these steps:
1. **Pre-Delete PHI tab** — The full participant-level list of all Tube IDs, located in the PHI version of the spreadsheet. Each pooled tube has one row per participant (e.g., a 4-person pool produces 4 rows sharing the same Tube ID).
2. **Tube Deletion** — Tubes were flagged for removal using standardized reason codes. Common reasons included app testing artifacts (tubes scanned or entered during testing of the app itself). All deletion decisions were tracked via codes in the spreadsheet columns.
3. **Post-Delete tab** — The dataset with all flagged tubes removed.
4. **APS Tubes tab** (blue) — A rolled-up view with one row per tube rather than one per participant, including the collection sponsor name but not individual participant names.

The Stats and REF Weekly tabs at the beginning of the APS spreadsheet comprise higher level data and were populated after the run reconciliation process described below.

#### RFR (Run Form Response) Processing
The RFR captures data from the person performing the testing. After completing a run, the tester scanned their paper run form and uploaded it via a Google Form, along with photos of the reaction tubes and answers to questions about tube counts. An optional third image, a "lookup map" listing all Tube IDs in the run, was sometimes included, particularly for positive or inconclusive tubes and for reruns.

The primary data tab is "RFR Data - preExcl" (pre-exclude). Very few rows from the raw Google Forms export were excluded; those that were had been clearly noted as submission errors in the response notes, typically followed by a corrected resubmission.

A full RFR audit was then conducted: all images of paper run forms and reaction tubes were reviewed, errors were corrected, and inconsistencies identified. All changes were tracked with codes, notes, and comments. Differences in how sites filled out the forms, including systematic errors at some sites, made this audit step essential.

#### Run Reconciliation
The run reconciliation process matched RFR runs to APS tubes for sites that had both data types. The key task was reconciling tube counts between the two datasets. Common complications included:
- Tubes collected the evening before a run being associated with the following day's run;
- Unresulted (null-result) tubes in APS, most of which could be determined as negative through run reconciliation and tube count matching;
- RFR runs containing tubes absent from the APS/Appivo data, for which ARF Tube IDs were created (a relatively small number overall);
- Runs not captured in the RFR data, which received run IDs with an "_APS" suffix, assigned in the rightmost columns of the APS Tubes import tab.

#### RFR Output and Cross-Checking
After reconciliation, the RFR spreadsheet's purple "All Tube Results" tab contains the final Tube ID-to-run ID mapping, along with run date, collection date, final result, and pool level. The "Runs Compare" tab provides side-by-side views of run data organized by run ID and by APS collection date, serving as a cross-check on counts of positives, negatives, and inconclusives across pipeline stages.

#### Final Rollup
Data was rolled up into Stats and Weekly tabs. The Stats tab typically resides in the APS file and the Weekly tab in the RFR. The APS file also includes a "REF Weekly" tab that references the weekly data, and a "POS and INCL" tab containing data for positive and inconclusive tubes only.

#### RTR (Referral Test Report) Processing
The RTR collected follow-up testing data, typically antigen or PCR tests, and sometimes other rapid LAMP tests. The "Referral Test Data" tab has one row per referral test. The "Referral Test by Person" tab rolls this up to one row per person, with columns for up to three sequential referral tests (type and result each). A "case cluster" groups related cases — for example, a family pool that tested positive where contributors were subsequently deconvoluted and tested individually. The original pool Tube ID serves as the initial case identifier for the cluster.

While column structure and lookup logic were applied to the referral test data, a fair amount of ad hoc manual processing was still required to extract the standardized metrics presented in the Stats tab.

#### RSR (Run Stats Report) and STS (Stats Table Summary)
For programs that did not use the Run Form (Coral Springs, ROSA, Davie, Kent, and FTFC), Run Form Responses could not be created. For the three earlier programs — Coral Springs, Davie, and ROSA, which began in fall 2021 — a Run Stats Report (RSR) Google Form was used for weekly reporting of test counts and results by program testers or administrators, who were otherwise tracking results in their own spreadsheets.

The STS files contain aggregated data from an earlier tracking system that predated the APS/RFR pipeline. For Kent (Camp Kenmont), data was reconstructed from an extracted Appivo dataset; Appivo had been used but the raw APS file was not created. For FTFC, the Appivo data was kept separate from Google Drive for privacy reasons and was subsequently lost. Aggregated numbers were preserved, however, and there were no positives during the brief testing period.

### Data Summaries by Program
Programs are ordered according to initiation date.

#### Aggregate of All Pilot Programs
Start Run Date: 2020-12-11
End Run Date: 2023-06-02
Number of Tubes Tested (initial only - no re-runs): 16,209
Number of Participant Results: 37,706
Number of Tubes with Final Result Positive: 884
Number of Unique Individuals Tested: 2,752

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


## Commentary
The FloodLAMP pilot data was a mess. Wrangling it to its current state was a substantial undertaking, requiring far more rounds of cleaning and reconciliation than initially anticipated. In retrospect, spreadsheets were not the right tool for this level of complexity. All of this work would be a lot easier now with AI.

A key reason why the data work was so challenging was the core tension between flexibility and standardization. FloodLAMP provided program testers and administrators with flexible data entry options, such as the ability to add participant "note names" for individuals not yet registered in Appivo, and did not require programs to use our tools (including the app). While practical in the field, this flexibility introduced significant downstream reconciliation work to match entries to existing participant records. In hindsight, that reconciliation effort might have been limited to positive and inconclusive cases only.

Run reconciliation was further complicated by tubes collected the evening before a testing run, combined with days that included multiple initial runs and reruns — distinctions that were not captured in the original data collection design, either in Appivo or the Google Forms.

For anyone interested in pooled self-collection testing, the challenges documented in this data may offer useful insights. However, the entire data collection and processing infrastructure would look fundamentally different if built today. AI capabilities — from AI-assisted software development to natural language processing, transcription, and automated data auditing — provide the leverage that was missing during FloodLAMP's operations. The primary gap was not conceptual but practical: the staffing, funding, software experience, methods, and tooling needed for continuous data quality monitoring. Those tools are now far more accessible, making dealing with even data as ugly as ours far less painful.

### Program Specific Data Notes
#### ABRM - Abrome K-12 School in Austin, TX
Abrome has one of the most complete datasets, including all three key file types: APS, RFR, and RTR.

#### BEND - Bend Fire and Rescue/EMS in Bend, OR
Bend is missing the RTR because referral testing was communicated by correspondence and was relatively straightforward: all FloodLAMP positives were confirmed by same-day lab PCR. Of the two inconclusive results, one was confirmed positive by PCR and one negative by PCR, as verified in a recent follow-up email to the program administrator.

#### COMB - Combate TV Show Production in Miami, FL
The referral data came in a separate spreadsheet from the program administrator and was processed into the standard RTR format.

#### COSP - Coral Springs City Municipal/EMS in Coral Springs, FL
This is the largest dataset. It has APS data but no RFR data because they did not use the Run Form. One of the challenges with this dataset was that a large number of participants were entered via note names, often with inconsistent spellings. Reconciling these was a laborious process. A lesson learned is that automating this with fuzzy name matching against a running participant list would be a valuable improvement.

#### CRLN - Carillon Pre-School in Portola Valley, CA
Data collected in the same Appivo tenant (application instance) with the FloodLAMP staff testing program - see FLMP.

#### DAVI - Town of Davie Fire/EMS in Davie, FL
Davie did not use Appivo, but the tester took extensive data, likely kept in private spreadsheets. The tester reported what appears to be very reliable data in the Run Stats Report on a weekly basis. They also provided a detailed antigen comparison dataset via spreadsheet.

#### FLMP - FloodLAMP (includes CRLN and FLSP)
This was the most challenging program to sort out and reconcile. Not only were Carillon and FloodLAMP Staff Plus intermingled for a period, but the data included complexity due to the pooled testing, positive follow-ups, deconvolution, and reruns. Advantages were the overall completeness of the data and the fact that it was collected by the FloodLAMP staff. The fact that this was FloodLAMP's own program using its own system reveals our operational challenges, but it's also the case that the data is inherently complex. It would have helped immensely to have internal software engineering, to improve our tooling and systems for this type of self-pooled testing program.

#### FLSP - FloodLAMP Staff Plus Other Community
Data collected in the same Appivo tenant (application instance) with the Carillon testing program - see FLMP.

#### FTFC - Eagles/EMS Leadership Conference in Ft. Lauderdale, FL
This data is straightforward, covering just a few days of testing with no positives. As noted above, none of the APS, RFR, or RTR data were available; the data came from previously compiled stats that originally derived from Appivo data that was subsequently lost.

#### KENT - Camp Kenmont Youth Camp in Kent, CT
There is a separate App Data import file that was found during the archive process. This file is not included in the archive but is the source from which the data is derived.

#### NDHM - Needham Beth Shalom School in Needham, MA
Needham has APS and RFR but no RTR because there were no positives, and therefore no follow-up testing.

#### ROSA - ROSA TV Production in Davie, FL
There is APS data for ROSA but no RFR or RTR. FloodLAMP had very little contact with the program administrator, though an email was sent during the archive process to inquire about referral testing for the single positive, which was confirmed positive by a same-day antigen test.
