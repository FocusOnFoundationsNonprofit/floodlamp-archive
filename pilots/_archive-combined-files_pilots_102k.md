METADATA
last updated: 2026-04-15_180754
file_name: _archive-combined-files_pilots_102k.md
category: pilots
subcategory: NA
words: 60587
tokens: 102407


CONTENT

# _archive-combined-files_pilots_102k (20 files, 102,407 tokens)

METADATA
last updated: 2026-04-15_180753
file_name: _archive-combined-files_pilot-data_87k.md
category: pilots
subcategory: pilot-data
words: 51104
tokens: 86751


CONTENT

# _archive-combined-files_pilot-data_87k (16 files, 86,751 tokens)

# 5,429  _context-commentary_pilots-pilot-data.md
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


# 9,325  aggregate_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: aggregate_pilot-data_summary.md
file_date: 2026-03-23
title: Aggregate Pilot Data Summary
category: pilots
subcategory: aggregate
tags: 
source_file_type: csv
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
notes: Aggregated statistics across all FloodLAMP pilot sites.
summary_short: Aggregate FloodLAMP pilot data summary across all sites. Total tubes run: 16715; Total positive tubes: 889; Total participants: 37200; Date range: 2020-12-07 to 2023-06-04.
words: 4897
tokens: 9325


CONTENT

## Files

### Aggregate CSVs
- Aggregate CSV folder: `aggregate_pilot-data/`
- Stats key-values CSV: [aggregate_pilot-data_stats_key-values.csv](aggregate_pilot-data_stats_key-values.csv)
- Weekly summary CSV: [aggregate_pilot-data_weekly-summary.csv](aggregate_pilot-data_weekly-summary.csv)
- Referral agreement CSV: [aggregate_pilot-data_stats_referral-agreement.csv](aggregate_pilot-data_stats_referral-agreement.csv)

## Key tables

### Stats key-values

| section | metric | value | value_status | value_formula | sites_included_n | sites_missing_n | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 16,209 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Overall | Number of Tube Tests Run (includes re-runs) | 16,484 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Overall | Number of Initial Runs | 795 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Overall | Number of APS Only Tubes run | 8,727 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 17,096 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Overall | Number of Participant Results | 37,706 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Overall | Number of ARF Tubes | 386 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Overall | Sum of Participant Results plus ARF Tubes | 38,092 | ok | participant_results + arf_tubes | 10 | 0 | AGGREGATE |  |
| Overall | Average Pool Level (excludes ARF) | 2.4 | ok | participant_results / (tubes_tested_initial - arf_tubes) | 10 | 0 | AGGREGATE |  |
| Re-runs | Number of Run Tubes (re-runs only) | 275 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Re-runs | Number of Reactions (re-runs only) | 705 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Re-runs | Re-run % of Tubes | 1.7% | partial | rerun_tubes / tubes_tested_initial | 6 | 4 | AGGREGATE |  |
| Re-runs | Number of Initial Runs with Re-runs | 148 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Re-runs | % Initial Runs with Re-runs | 18.6% | partial | initial_runs_with_reruns / initial_runs | 6 | 4 | AGGREGATE |  |
| Positives | Number of Tubes with Final Result Positive | 884 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Positives | % of Tubes Positives (Final Result) | 5.5% | ok | positive_tubes_final / tubes_tested_initial | 10 | 0 | AGGREGATE |  |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 87 | partial | sum(site values) | 8 | 2 | AGGREGATE |  |
| Positives | Known Positive Cases | 337 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Positives | Unknown Positive Cases | 134 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 14 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 3 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Inconclusives | Total Number of Inconclusive Tubes | 17 | partial | inconclusive_tubes_final + inconclusive_not_in_aps | 10 | 4 | AGGREGATE |  |
| Inconclusives | % of Tubes Inconclusive | 0.1% | partial | total_inconclusive_tubes / tubes_tested_initial | 10 | 4 | AGGREGATE |  |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 4 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 23.5% | partial | inconclusive_resolved_pos / total_inconclusive_tubes | 9 | 4 | AGGREGATE |  |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 3 | partial | sum(site values) | 8 | 2 | AGGREGATE |  |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 9 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 68 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Inconclusives | Number of Inconclusive Test Run Calls | 159 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Inconclusives | % Tube Tests Run Called Inconclusive | 1.0% | ok | inconclusive_run_calls / tube_tests_run_total | 10 | 0 | AGGREGATE |  |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 127 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 121 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 4 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 98.4% | ok | (agree_positives + incl_ref_pos) / cases_with_referral | 10 | 0 | AGGREGATE |  |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 2 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 12 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 68 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 62 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 15 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 24.2% | partial | positive_same_day_antigen_neg / positive_same_day_antigen | 6 | 4 | AGGREGATE |  |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 1 | partial | sum(site values) | 6 | 4 | AGGREGATE |  |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative |  | not_available | positive_antigen_other_neg / positive_antigen_other | 0 | 10 | AGGREGATE |  |
| False Calls | False Positives Final Results | 0 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | sum(site values) | 10 | 0 | AGGREGATE |  |
| People | Number of Unique Individuals Tested | 2,752 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| People | Number of Unique Sponsors | 481 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 444 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 16.1% | partial | unique_positive / unique_individuals | 9 | 1 | AGGREGATE |  |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 475 | partial | sum(site values) | 9 | 1 | AGGREGATE |  |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 17.3% | partial | unique_positive_incl_pool / unique_individuals | 9 | 1 | AGGREGATE |  |
| Dates | Start Run Date | 2020-12-11 | ok | min(site values) | 10 | 0 | AGGREGATE |  |
| Dates | End Run Date | 2023-06-02 | ok | max(site values) | 10 | 0 | AGGREGATE |  |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status | pct_positive_formula | sites_included_n | sites_total_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2020-12-07 | 2020-12-13 | 6 | 2 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2020-12-14 | 2020-12-20 | 3 | 1 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2020-12-21 | 2020-12-27 | 2 | 1 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2020-12-28 | 2021-01-03 | 6 | 2 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-01-04 | 2021-01-10 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-01-11 | 2021-01-17 | 36 | 15 | 3 | 0 | 20.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-01-18 | 2021-01-24 | 49 | 24 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-01-25 | 2021-01-31 | 45 | 19 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-02-01 | 2021-02-07 | 31 | 11 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-02-08 | 2021-02-14 | 40 | 13 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-02-15 | 2021-02-21 | 14 | 4 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-02-22 | 2021-02-28 | 24 | 9 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-03-01 | 2021-03-07 | 35 | 11 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-03-08 | 2021-03-14 | 30 | 9 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-03-15 | 2021-03-21 | 16 | 6 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-03-22 | 2021-03-28 | 6 | 2 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-03-29 | 2021-04-04 | 6 | 2 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-04-05 | 2021-04-11 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-04-12 | 2021-04-18 | 8 | 3 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-04-19 | 2021-04-25 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-04-26 | 2021-05-02 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-05-03 | 2021-05-09 | 1 | 1 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-05-10 | 2021-05-16 | 5 | 2 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-05-17 | 2021-05-23 | 6 | 6 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-05-24 | 2021-05-30 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-05-31 | 2021-06-06 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-06-07 | 2021-06-13 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-06-14 | 2021-06-20 | 197 | 63 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2021-06-21 | 2021-06-27 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-06-28 | 2021-07-04 | 105 | 374 | 2 | 0 | 0.5% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2021-07-05 | 2021-07-11 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 2 | 10 |
| 2021-07-12 | 2021-07-18 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 2 | 10 |
| 2021-07-19 | 2021-07-25 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 2 | 10 |
| 2021-07-26 | 2021-08-01 | 85 | 322 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2021-08-02 | 2021-08-08 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-08-09 | 2021-08-15 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-08-16 | 2021-08-22 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-08-23 | 2021-08-29 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2021-08-30 | 2021-09-05 | 172 | 55 | 2 | 0 | 3.6% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2021-09-06 | 2021-09-12 | 192 | 63 | 3 | 1 | 4.8% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2021-09-13 | 2021-09-19 | 194 | 65 | 4 | 0 | 6.2% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2021-09-20 | 2021-09-26 | 235 | 75 | 4 | 0 | 5.3% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2021-09-27 | 2021-10-03 | 240 | 108 | 1 | 0 | 0.9% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-10-04 | 2021-10-10 | 322 | 171 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-10-11 | 2021-10-17 | 281 | 154 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-10-18 | 2021-10-24 | 251 | 138 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-10-25 | 2021-10-31 | 219 | 108 | 1 | 0 | 0.9% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-11-01 | 2021-11-07 | 227 | 126 | 3 | 0 | 2.4% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-11-08 | 2021-11-14 | 220 | 120 | 16 | 0 | 13.3% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-11-15 | 2021-11-21 | 271 | 141 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-11-22 | 2021-11-28 | 157 | 74 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-11-29 | 2021-12-05 | 275 | 152 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-12-06 | 2021-12-12 | 319 | 183 | 2 | 0 | 1.1% | ok | positive_tubes_n / tubes_n | 5 | 10 |
| 2021-12-13 | 2021-12-19 | 396 | 246 | 9 | 2 | 3.7% | ok | positive_tubes_n / tubes_n | 5 | 10 |
| 2021-12-20 | 2021-12-26 | 535 | 260 | 31 | 0 | 11.9% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2021-12-27 | 2022-01-02 | 1368 | 488 | 66 | 0 | 13.5% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-01-03 | 2022-01-09 | 3400 | 1502 | 327 | 1 | 21.8% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-01-10 | 2022-01-16 | 3188 | 1251 | 167 | 1 | 13.3% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-01-17 | 2022-01-23 | 2766 | 1013 | 102 | 0 | 10.1% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-01-24 | 2022-01-30 | 3041 | 1053 | 48 | 0 | 4.6% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-01-31 | 2022-02-06 | 2897 | 966 | 27 | 0 | 2.8% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-02-07 | 2022-02-13 | 2878 | 933 | 23 | 0 | 2.5% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-02-14 | 2022-02-20 | 2876 | 977 | 5 | 2 | 0.5% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-02-21 | 2022-02-27 | 2216 | 783 | 4 | 0 | 0.5% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-02-28 | 2022-03-06 | 732 | 316 | 3 | 0 | 0.9% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-03-07 | 2022-03-13 | 271 | 165 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-03-14 | 2022-03-20 | 180 | 93 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-03-21 | 2022-03-27 | 212 | 147 | 1 | 0 | 0.7% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-03-28 | 2022-04-03 | 27 | 14 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-04-04 | 2022-04-10 | 246 | 189 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-04-11 | 2022-04-17 | 225 | 164 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-04-18 | 2022-04-24 | 250 | 187 | 1 | 0 | 0.5% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-04-25 | 2022-05-01 | 221 | 156 | 2 | 0 | 1.3% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-05-02 | 2022-05-08 | 148 | 70 | 2 | 0 | 2.9% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-05-09 | 2022-05-15 | 260 | 197 | 4 | 2 | 2.0% | ok | positive_tubes_n / tubes_n | 4 | 10 |
| 2022-05-16 | 2022-05-22 | 227 | 160 | 1 | 0 | 0.6% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-05-23 | 2022-05-29 | 243 | 189 | 1 | 0 | 0.5% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-05-30 | 2022-06-05 | 191 | 149 | 1 | 0 | 0.7% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-06-06 | 2022-06-12 | 87 | 145 | 3 | 0 | 2.1% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-06-13 | 2022-06-19 | 19 | 9 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-06-20 | 2022-06-26 | 13 | 5 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-06-27 | 2022-07-03 | 97 | 129 | 4 | 3 | 3.1% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-07-04 | 2022-07-10 | 131 | 132 | 1 | 0 | 0.8% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-07-11 | 2022-07-17 | 124 | 124 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-07-18 | 2022-07-24 | 105 | 204 | 4 | 0 | 2.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-07-25 | 2022-07-31 | 14 | 7 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-08-01 | 2022-08-07 | 63 | 90 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-08-08 | 2022-08-14 | 62 | 62 | 1 | 0 | 1.6% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-08-15 | 2022-08-21 | 0 | 37 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-08-22 | 2022-08-28 | 4 | 1 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-08-29 | 2022-09-04 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-09-05 | 2022-09-11 | 121 | 64 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-09-12 | 2022-09-18 | 145 | 57 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-09-19 | 2022-09-25 | 118 | 52 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-09-26 | 2022-10-02 | 151 | 63 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-10-03 | 2022-10-09 | 154 | 65 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 3 | 10 |
| 2022-10-10 | 2022-10-16 | 120 | 51 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-10-17 | 2022-10-23 | 111 | 50 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-10-24 | 2022-10-30 | 118 | 56 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-10-31 | 2022-11-06 | 84 | 39 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-11-07 | 2022-11-13 | 102 | 46 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-11-14 | 2022-11-20 | 89 | 46 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-11-21 | 2022-11-27 | 49 | 28 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-11-28 | 2022-12-04 | 114 | 48 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-12-05 | 2022-12-11 | 98 | 40 | 1 | 0 | 2.5% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-12-12 | 2022-12-18 | 42 | 24 | 1 | 0 | 4.2% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-12-19 | 2022-12-25 | 64 | 32 | 2 | 0 | 6.2% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2022-12-26 | 2023-01-01 | 6 | 3 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2023-01-02 | 2023-01-08 | 100 | 41 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 2 | 10 |
| 2023-01-09 | 2023-01-15 | 80 | 39 | 0 | 2 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-01-16 | 2023-01-22 | 86 | 40 | 0 | 1 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-01-23 | 2023-01-29 | 65 | 29 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-01-30 | 2023-02-05 | 13 | 7 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-02-06 | 2023-02-12 | 70 | 33 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-02-13 | 2023-02-19 | 87 | 39 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-02-20 | 2023-02-26 | 89 | 40 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-02-27 | 2023-03-05 | 81 | 37 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-03-06 | 2023-03-12 | 112 | 47 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-03-13 | 2023-03-19 | 0 | 0 | 0 | 0 |  | denom_zero | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-03-20 | 2023-03-26 | 84 | 37 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-03-27 | 2023-04-02 | 90 | 40 | 1 | 0 | 2.5% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-04-03 | 2023-04-09 | 54 | 28 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-04-10 | 2023-04-16 | 81 | 39 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-04-17 | 2023-04-23 | 67 | 39 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-04-24 | 2023-04-30 | 55 | 33 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-05-01 | 2023-05-07 | 43 | 22 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-05-08 | 2023-05-14 | 67 | 31 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-05-15 | 2023-05-21 | 54 | 31 | 1 | 0 | 3.2% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-05-22 | 2023-05-28 | 49 | 26 | 4 | 0 | 15.4% | ok | positive_tubes_n / tubes_n | 1 | 10 |
| 2023-05-29 | 2023-06-04 | 43 | 25 | 0 | 0 | 0.0% | ok | positive_tubes_n / tubes_n | 1 | 10 |

### Referral agreement

| fl_result_category | tubes_n | cases_n | with_ref_or_corresp_n | agree_n | agree_pct | agree_pct_status | disagree_n | disagree_pct | disagree_pct_status | ref_cor_pos_n | incl_gt_pos_pct | incl_gt_pos_pct_status | ref_cor_neg_n | incl_gt_neg_pct | incl_gt_neg_pct_status | source_sheet | source_anchor | agree_pct_formula | disagree_pct_formula | incl_gt_pos_pct_formula | incl_gt_neg_pct_formula | sites_included_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Positive | 884 | 87 | 120 | 119 | 99.2% | ok | 1 | 0.8% | ok |  |  |  |  |  |  | AGGREGATE |  | agree_n / with_ref_or_corresp_n | disagree_n / with_ref_or_corresp_n |  |  | 8 |
| Inconclusive | 17 | 16 | 7 |  |  |  |  |  |  | 4 | 57.1% | ok | 2 | 28.6% | ok | AGGREGATE |  |  |  | ref_cor_pos_n / with_ref_or_corresp_n | ref_cor_neg_n / with_ref_or_corresp_n | 8 |


# 4,823  ABRM_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: ABRM_pilot-data_summary.md
file_date: 2023-006-02
title: ABRM Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2836
tokens: 4823
notes: 
summary_short: The "ABRM_pilot-data_summary" covers the FloodLAMP pilot program for Abrome which was a small K-12 school in Austin, TX that used FloodLAMP for pooled household self-collection testing, with on-site test processing by school staff using a mini water bath configuration. The program tested students, staff, and their families over 9 months (2022-09-05 to 2023-06-02), often multiple times per week, running 1,379 tubes with 2,954 participant results and 8 positive tubes detected.


CONTENT

## Plots

### Composite

![ABRM Weekly Composite](_plots/ABRM_weekly_composite.png)

### Percent Positive Tubes

![ABRM Weekly Percent Positives](_plots/ABRM_weekly_percent_positives.png)

### Volume

![ABRM Weekly Volume](_plots/ABRM_weekly_volume.png)

## Files

### Google Sheets URLs
- [ABRM_APS_deID_PUB](https://docs.google.com/spreadsheets/d/140IAw1sI2nPQztTAXY9-XJxd4lPpOhpeXb-IXXnWUZk)
- [ABRM_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/1zddUuVUJJRU2gSW45EBK2qlD8uYIW8B5jm-kziiklHU)
- [ABRM_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/1g_chl4UPvP70E16V_OTjW4KxlFPRvJ7uKc1vB1X15gQ)

### Curated CSVs
- Curated CSV folder: `ABRM_curated_csvs/`
- Stats key-values CSV: [ABRM_APS_stats_key-values.csv](ABRM_curated_csvs/ABRM_APS_stats_key-values.csv)
- Weekly summary CSV: [ABRM_APS_weekly-summary.csv](ABRM_curated_csvs/ABRM_APS_weekly-summary.csv)
- Referral tests by person CSV: [ABRM_RTR_referral-tests-by-person.csv](ABRM_curated_csvs/ABRM_RTR_referral-tests-by-person.csv)

### XLSX downloads:
- [ABRM_APS_deID_PUB.xlsx](ABRM_xlsx_downloads/ABRM_APS_deID_PUB.xlsx)
- [ABRM_RFR_deID_PUB.xlsx](ABRM_xlsx_downloads/ABRM_RFR_deID_PUB.xlsx)
- [ABRM_RTR_deID_PUB.xlsx](ABRM_xlsx_downloads/ABRM_RTR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | ABRM_RFR_deID_PUB | ok |  |  | Stats | 1 |
| Files | RTR File | ABRM_RTR_deID_PUB | ok |  |  | Stats | 2 |
| Files | RSR File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 1,379 | ok | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 1,519 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 184 | ok |  |  | Stats | 7 |
| Overall | Number of APS Only Tubes run | 100 | ok |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 1,730 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 2,954 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 22 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 2,976 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 2.2 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 140 | ok | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 331 | ok | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 10.2% | ok | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 78 | ok |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 42.4% | ok |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 8 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 0.6% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 3 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 2 | ok | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 1 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 3 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 | ok |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 3 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.2% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 0.0% | ok |  |  | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 3 | ok |  | Likely Negative - otherwise admin would have reported a positive referral test result. Perhaps they were not follow up referral tested at all, which may have been the case for 1 of these 3 which was resulted as Neg in the app. | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 4 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App |  | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 48 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 3.2% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 1 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests | Only Case Cluster 1 has Referral data shared with FloodLAMP | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 1 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive | All were FL pos and confirmed with referral tests | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% | ok |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 3 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 0 | ok |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 0 | ok |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 0 | ok | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative |  | denom_zero |  | denom zero | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 0 | ok |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative |  | denom_zero |  | denom zero | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 87 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 17 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 5 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 5.7% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 10 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 11.5% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2022-09-05 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2023-06-02 | ok |  |  | Stats | 75 |
| Info | Test Operator | Abrome School | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Office | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Students, Staff, Families | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Mini w water bath | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled Household | ok |  Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Abrome | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Abrome School | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | K-12 School | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Austin, TX | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022-09-05 | 2022-09-11 | 113 | 61 | 0 | 0 | 0.0% | ok |
| 2022-09-12 | 2022-09-18 | 130 | 52 | 0 | 0 | 0.0% | ok |
| 2022-09-19 | 2022-09-25 | 108 | 48 | 0 | 0 | 0.0% | ok |
| 2022-09-26 | 2022-10-02 | 139 | 59 | 0 | 0 | 0.0% | ok |
| 2022-10-03 | 2022-10-09 | 138 | 59 | 0 | 0 | 0.0% | ok |
| 2022-10-10 | 2022-10-16 | 106 | 46 | 0 | 0 | 0.0% | ok |
| 2022-10-17 | 2022-10-23 | 99 | 46 | 0 | 0 | 0.0% | ok |
| 2022-10-24 | 2022-10-30 | 106 | 48 | 0 | 0 | 0.0% | ok |
| 2022-10-31 | 2022-11-06 | 73 | 34 | 0 | 0 | 0.0% | ok |
| 2022-11-07 | 2022-11-13 | 90 | 41 | 0 | 0 | 0.0% | ok |
| 2022-11-14 | 2022-11-20 | 81 | 41 | 0 | 0 | 0.0% | ok |
| 2022-11-21 | 2022-11-27 | 44 | 25 | 0 | 0 | 0.0% | ok |
| 2022-11-28 | 2022-12-04 | 101 | 43 | 0 | 0 | 0.0% | ok |
| 2022-12-05 | 2022-12-11 | 90 | 37 | 1 | 0 | 2.7% | ok |
| 2022-12-12 | 2022-12-18 | 19 | 13 | 0 | 0 | 0.0% | ok |
| 2022-12-19 | 2022-12-25 | 54 | 26 | 2 | 0 | 7.7% | ok |
| 2022-12-26 | 2023-01-01 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2023-01-02 | 2023-01-08 | 93 | 38 | 0 | 0 | 0.0% | ok |
| 2023-01-09 | 2023-01-15 | 80 | 39 | 0 | 2 | 0.0% | ok |
| 2023-01-16 | 2023-01-22 | 86 | 40 | 0 | 1 | 0.0% | ok |
| 2023-01-23 | 2023-01-29 | 65 | 29 | 0 | 0 | 0.0% | ok |
| 2023-01-30 | 2023-02-05 | 13 | 7 | 0 | 0 | 0.0% | ok |
| 2023-02-06 | 2023-02-12 | 70 | 33 | 0 | 0 | 0.0% | ok |
| 2023-02-13 | 2023-02-19 | 87 | 39 | 0 | 0 | 0.0% | ok |
| 2023-02-20 | 2023-02-26 | 89 | 40 | 0 | 0 | 0.0% | ok |
| 2023-02-27 | 2023-03-05 | 81 | 37 | 0 | 0 | 0.0% | ok |
| 2023-03-06 | 2023-03-12 | 112 | 47 | 0 | 0 | 0.0% | ok |
| 2023-03-13 | 2023-03-19 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2023-03-20 | 2023-03-26 | 84 | 37 | 0 | 0 | 0.0% | ok |
| 2023-03-27 | 2023-04-02 | 90 | 40 | 1 | 0 | 2.5% | ok |
| 2023-04-03 | 2023-04-09 | 54 | 28 | 0 | 0 | 0.0% | ok |
| 2023-04-10 | 2023-04-16 | 81 | 39 | 0 | 0 | 0.0% | ok |
| 2023-04-17 | 2023-04-23 | 67 | 39 | 0 | 0 | 0.0% | ok |
| 2023-04-24 | 2023-04-30 | 55 | 33 | 0 | 0 | 0.0% | ok |
| 2023-05-01 | 2023-05-07 | 43 | 22 | 0 | 0 | 0.0% | ok |
| 2023-05-08 | 2023-05-14 | 67 | 31 | 0 | 0 | 0.0% | ok |
| 2023-05-15 | 2023-05-21 | 54 | 31 | 1 | 0 | 3.2% | ok |
| 2023-05-22 | 2023-05-28 | 49 | 26 | 4 | 0 | 15.4% | ok |
| 2023-05-29 | 2023-06-04 | 43 | 25 | 0 | 0 | 0.0% | ok |

### Referral tests by person

| participant_id | num_sequential_referral_tests | num_floodlamp_results_pos_or_incl | floodlamp_tube_id | floodlamp_test_result | floodlamp_test_date | first_referral_test_date | referral_overall_result | first_referral_test_type | first_referral_test_result | second_referral_test_type | second_referral_test_result | third_referral_test_type | third_referral_test_result | antigen_neg_with_other_positive_flag | referral_eval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABRM582390 | 2 | 2 | AG173 | Positive | 2022-12-08 | 2022-12-08 | Positive | LAMP Device | Negative | LAMP Device | Positive |  |  | 0 | Not same day positive but other person in pool was - became referral test positive in following days (no indiv FL deconv) |
| ABRM771013 | 4 | 1 | AG173 | Positive | 2022-12-08 | 2022-12-08 | Positive | Rapid PCR | Negative | Antigen | Negative | Antigen | Positive | 1 | Person in Referral Test Data Antigen Pos on 12-11 did FL test with Neg result on 12-6, 12-7, and 12-8 but they nested neg by Rapid PCR (Mesa) on 12-8, and Antigen Neg on 12-9 and 12-10 before becoming Antigen pos on 12-11 |
| ABRM805764 | 1 | 2 | AG173 | Positive | 2022-12-08 | 2022-12-08 | Positive | Rapid PCR | Positive |  |  |  |  | 0 | Only same day positive from pool but other people in pool became pos in next few days |


# 3,668  BEND_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: BEND_pilot-data_summary.md
file_date: 2022-05-11
title: BEND Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2292
tokens: 3668
notes: 
summary_short: The "BEND_pilot-data_summary" covers the FloodLAMP pilot program for a fire department/EMS group in Bend, OR that used FloodLAMP for individual (non-pooled) testing of first responders and staff, with HCW-collected samples processed on-site using a double mini configuration. The program ran over 5 months (2021-12-10 to 2022-05-11), testing 772 tubes with 71 positive tubes detected — a 9.2% positivity rate that captured the Omicron wave.


CONTENT

## Plots

### Composite

![BEND Weekly Composite](_plots/BEND_weekly_composite.png)

### Percent Positive Tubes

![BEND Weekly Percent Positives](_plots/BEND_weekly_percent_positives.png)

### Volume

![BEND Weekly Volume](_plots/BEND_weekly_volume.png)

## Files

### Google Sheets URLs
- [BEND_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1ff9LyHzhq3Mka_W5dEm7cyYWW7cZmOZxW9bUFWjuqIQ)
- [BEND_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/1lkoZ0Og6KAdMPD6eBgW3tcs8v4dg6l9-Hjnp8Do__Rg)

### Curated CSVs
- Curated CSV folder: `BEND_curated_csvs/`
- Stats key-values CSV: [BEND_APS_stats_key-values.csv](BEND_curated_csvs/BEND_APS_stats_key-values.csv)
- Weekly summary CSV: [BEND_APS_weekly-summary.csv](BEND_curated_csvs/BEND_APS_weekly-summary.csv)
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [BEND_APS_deID_PUB.xlsx](BEND_xlsx_downloads/BEND_APS_deID_PUB.xlsx)
- [BEND_RFR_deID_PUB.xlsx](BEND_xlsx_downloads/BEND_RFR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | BEND_RFR_deID_PUB | ok |  |  | Stats | 1 |
| Files | RTR File | NONE | ok |  |  | Stats | 2 |
| Files | RSR File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 772 | ok | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 792 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 44 | ok |  |  | Stats | 7 |
| Overall | Number of APS Only Tubes run | 11 | ok |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 822 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 767 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 5 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 772 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 1.0 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 20 | ok | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 27 | ok | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 2.6% | ok | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 10 | ok |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 22.7% | ok |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 71 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 9.2% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 51 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 0 | ok | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 51 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 2 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 3 | ok |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 5 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.6% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 1 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 20.0% | ok |  |  | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 2 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 2 | ok |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 7 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App | 1/26, 1/28, 2/15, 2/25, 3/5 2, 3/7 | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 12 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 1.5% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 53 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 51 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 1 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 98.1% | ok |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 1 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 3 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) |  | not_available |  | Not Available - Only PCR Referral Testing | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests |  | not_available |  | Not Available - Only PCR Referral Testing | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative |  | not_available | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative | Not Available - Only PCR Referral Testing | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative |  | not_available |  | Not Available - Only PCR Referral Testing | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative |  | not_available |  | Not Available - Only PCR Referral Testing | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative |  | not_available |  | Not Available - Only PCR Referral Testing | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 187 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 103 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 50 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 26.7% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 50 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 26.7% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-12-10 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2022-05-11 | ok |  |  | Stats | 75 |
| Info | Test Operator | Bend Fire and Rescue | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Office Space | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | First Responders, Staff | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Double Mini | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Individual | ok |  Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | HCW | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | Remote (NSVD Volunteer) | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Bend | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Fire Station | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Fire Dept / EMS | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Bend, OR | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-12-06 | 2021-12-12 | 5 | 5 | 0 | 0 | 0.0% | ok |
| 2021-12-13 | 2021-12-19 | 13 | 13 | 1 | 0 | 7.7% | ok |
| 2021-12-20 | 2021-12-26 | 12 | 12 | 0 | 0 | 0.0% | ok |
| 2021-12-27 | 2022-01-02 | 27 | 27 | 2 | 0 | 7.4% | ok |
| 2022-01-03 | 2022-01-09 | 54 | 56 | 10 | 1 | 17.9% | ok |
| 2022-01-10 | 2022-01-16 | 75 | 75 | 18 | 0 | 24.0% | ok |
| 2022-01-17 | 2022-01-23 | 63 | 63 | 23 | 0 | 36.5% | ok |
| 2022-01-24 | 2022-01-30 | 36 | 36 | 4 | 0 | 11.1% | ok |
| 2022-01-31 | 2022-02-06 | 24 | 24 | 1 | 0 | 4.2% | ok |
| 2022-02-07 | 2022-02-13 | 38 | 38 | 6 | 0 | 15.8% | ok |
| 2022-02-14 | 2022-02-20 | 97 | 97 | 0 | 1 | 0.0% | ok |
| 2022-02-21 | 2022-02-27 | 128 | 129 | 3 | 0 | 2.3% | ok |
| 2022-02-28 | 2022-03-06 | 99 | 101 | 3 | 0 | 3.0% | ok |
| 2022-03-07 | 2022-03-13 | 86 | 86 | 0 | 0 | 0.0% | ok |
| 2022-03-14 | 2022-03-20 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-03-21 | 2022-03-27 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-03-28 | 2022-04-03 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-04-04 | 2022-04-10 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-04-11 | 2022-04-17 | 1 | 1 | 0 | 0 | 0.0% | ok |
| 2022-04-18 | 2022-04-24 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-04-25 | 2022-05-01 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-05-02 | 2022-05-08 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-05-09 | 2022-05-15 | 9 | 9 | 0 | 0 | 0.0% | ok |


# 4,804  COMB_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: COMB_pilot-data_summary.md
file_date: 2022-08-15
title: COMB Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2892
tokens: 4804
notes: 
summary_short: The "COMB_pilot-data_summary" covers the FloodLAMP pilot program for Combate which was a martial arts production organization in Miami, FL where FloodLAMP staff provided individual HCW-collected testing of martial artists and production staff, with test processing done in a hotel room using a standard equipment configuration. The program ran over 5 months (2022-03-20 to 2022-08-15), testing 1,981 tubes from 1,672 participants with 14 positive tubes detected.


CONTENT

## Plots

### Composite

![COMB Weekly Composite](_plots/COMB_weekly_composite.png)

### Percent Positive Tubes

![COMB Weekly Percent Positives](_plots/COMB_weekly_percent_positives.png)

### Volume

![COMB Weekly Volume](_plots/COMB_weekly_volume.png)

## Files

### Google Sheets URLs
- [COMB_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1LFbt-1PJ6c9qoDfwMx2pw9f39i21yZvpYWuzSxg0nhk)
- [COMB_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/1P_FWpqIBJV0FqluwOZMjMumc6wynKbdR-70WJR03DZc/edit?usp=sharing)
- [COMB_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/1ODszJJPOKDcEBwA3MiMwAH98TVB65cpz6lqisSF1Uqo)

### Curated CSVs
- Curated CSV folder: `COMB_curated_csvs/`
- Stats key-values CSV: [COMB_APS_stats_key-values.csv](COMB_curated_csvs/COMB_APS_stats_key-values.csv)
- Weekly summary CSV: [COMB_APS_weekly-summary.csv](COMB_curated_csvs/COMB_APS_weekly-summary.csv)
- Referral tests by person CSV: [COMB_RTR_referral-tests-by-person.csv](COMB_curated_csvs/COMB_RTR_referral-tests-by-person.csv)

### XLSX downloads:
- [COMB_APS_deID_PUB.xlsx](COMB_xlsx_downloads/COMB_APS_deID_PUB.xlsx)
- [COMB_RFR_deID_PUB.xlsx](COMB_xlsx_downloads/COMB_RFR_deID_PUB.xlsx)
- [COMB_RTR_deID_PUB.xlsx](COMB_xlsx_downloads/COMB_RTR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | COMB_RFR_deID_PUB | ok |  |  | Stats | 1 |
| Files | RTR File | COMB_RTR_deID_PUB | ok |  |  | Stats | 2 |
| Files | RSR File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 1,981 | ok | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 2,012 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 80 | ok |  |  | Stats | 7 |
| Overall | Number of APS Only Tubes run | 63 | ok |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 2,060 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 1,672 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 309 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 1,981 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 1.0 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 31 | ok | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 96 | ok | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 1.6% | ok | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 19 | ok |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 23.8% | ok |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 14 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 0.7% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 12 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 2 | ok | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 10 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 3 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 | ok |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 3 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.2% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 2 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 66.7% | ok |  |  | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 1 | ok |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 4 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App | 4 in OLD pre-Data Project summary | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 12 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 0.6% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 12 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 10 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 2 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% | ok |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 1 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 11 | ok |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 11 | ok |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 5 | ok | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 45.5% | ok |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 0 | ok |  | Referral Tests were Antigen and if Antigen Negative then followup PCR | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 0.0% | ok |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives | For the 2 FL Positives with No Referral Tests or Correspondence there is no indication they are false | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin | None in RTR or reported by Admin. There is 1 positive referral tests that is not in our FloodLAMP data (2022-06-30 and 2022-07-01) but the name is not in our App anywhere so the conclusion is that this person did not receive FloodLAMP testing at all but was antigen tested. | Stats | 61 |
| People | Number of Unique Individuals Tested | 369 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 2 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 14 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 3.8% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 14 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 3.8% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2022-03-20 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2022-08-15 | ok |  |  | Stats | 75 |
| Info | Test Operator | FloodLAMP | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Hotel room | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Martial artists, Production Staff | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Individual | ok | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | HCW | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Combate | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Embassy Hotel | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Production Organization | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Miami, FL | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022-03-14 | 2022-03-20 | 18 | 18 | 0 | 0 | 0.0% | ok |
| 2022-03-21 | 2022-03-27 | 99 | 100 | 1 | 0 | 1.0% | ok |
| 2022-03-28 | 2022-04-03 | 2 | 2 | 0 | 0 | 0.0% | ok |
| 2022-04-04 | 2022-04-10 | 127 | 142 | 0 | 0 | 0.0% | ok |
| 2022-04-11 | 2022-04-17 | 120 | 120 | 0 | 0 | 0.0% | ok |
| 2022-04-18 | 2022-04-24 | 134 | 134 | 1 | 0 | 0.7% | ok |
| 2022-04-25 | 2022-05-01 | 108 | 108 | 2 | 0 | 1.9% | ok |
| 2022-05-02 | 2022-05-08 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-05-09 | 2022-05-15 | 112 | 112 | 0 | 0 | 0.0% | ok |
| 2022-05-16 | 2022-05-22 | 99 | 99 | 0 | 0 | 0.0% | ok |
| 2022-05-23 | 2022-05-29 | 128 | 137 | 0 | 0 | 0.0% | ok |
| 2022-05-30 | 2022-06-05 | 114 | 114 | 1 | 0 | 0.9% | ok |
| 2022-06-06 | 2022-06-12 | 55 | 130 | 3 | 0 | 2.3% | ok |
| 2022-06-13 | 2022-06-19 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-06-20 | 2022-06-26 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-06-27 | 2022-07-03 | 90 | 125 | 4 | 3 | 3.2% | ok |
| 2022-07-04 | 2022-07-10 | 131 | 132 | 1 | 0 | 0.8% | ok |
| 2022-07-11 | 2022-07-17 | 122 | 123 | 0 | 0 | 0.0% | ok |
| 2022-07-18 | 2022-07-24 | 97 | 200 | 4 | 0 | 2.0% | ok |
| 2022-07-25 | 2022-07-31 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-01 | 2022-08-07 | 54 | 86 | 0 | 0 | 0.0% | ok |
| 2022-08-08 | 2022-08-14 | 62 | 62 | 1 | 0 | 1.6% | ok |
| 2022-08-15 | 2022-08-21 | 0 | 37 | 0 | 0 | 0.0% | ok |

### Referral tests by person

| participant_id | num_sequential_referral_tests | num_floodlamp_results_pos_or_incl | floodlamp_tube_id | floodlamp_test_result | floodlamp_test_date | first_referral_test_date | referral_overall_result | first_referral_test_type | first_referral_test_result | second_referral_test_type | second_referral_test_result | third_referral_test_type | third_referral_test_result | antigen_neg_with_other_positive_flag | referral_eval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COMB170110 | 1 | 1 | FM2159 | Positive | 2022-06-27 | 2022-06-27 | Positive | Antigen | Positive |  |  |  |  | 0 | Referral Confirmed FL Positive |
| COMB185924 | 2 | 0 | not found | not found | not found | 2022-08-08 | Positive | Antigen | Negative | Lab Purif PCR | Positive |  |  | 1 | Referral Confirmed FL Positive |
| COMB213226 | 1 | 1 | FM1080 | Positive | 2022-07-22 | 2022-07-22 | Positive | Antigen | Positive |  |  |  |  | 0 | Referral Confirmed FL Positive |
| COMB242905 | 2 | 1 | FM1198 | Positive | 2022-07-19 | 2022-07-19 | Positive | Antigen | Negative | Lab Purif PCR | Positive |  |  | 1 | Referral Confirmed FL Positive |
| COMB353066 | 2 | 2 | FM2198 | Positive | 2022-06-27 | 2022-06-27 | Positive | Antigen | Negative | Lab Purif PCR | Positive |  |  | 1 | Referral Confirmed FL Positive |
| COMB413047 | 1 | 1 | FM1303 | Positive | 2022-07-22 | 2022-07-22 | Positive | Antigen | Positive |  |  |  |  | 0 | Referral Confirmed FL Positive |
| COMB596496 | 2 | 1 | FM2472 | Inconclusive | 2022-06-28 | 2022-06-28 | Positive | Antigen | Negative | Lab Purif PCR | Positive |  |  | 1 | Referral Confirmed FL Inconclusive |
| COMB638337 | 1 | 0 | not found | not found | not found | 2022-06-30 | Positive | Antigen | Positive |  |  |  |  | 0 | Referral Confirmed FL Positive - ARF positive but name is in App and was tested many other times |
| COMB704360 | 2 | 2 | FM4123 | Positive | 2022-04-25 | 2022-04-25 | Positive | Antigen | Negative | Lab Purif PCR | Positive |  |  | 1 | Referral Confirmed FL Positive |
| COMB724402 | 1 | 1 | FM2492 | Inconclusive | 2022-07-01 | 2022-07-01 | Positive | Antigen | Positive |  |  |  |  | 0 | Referral Confirmed FL Inconclusive |
| COMB770137 | 1 | 1 | FM2799 | Positive | 2022-06-06 | 2022-06-06 | Positive | Antigen | Positive |  |  |  |  | 0 | Referral Confirmed FL Positive |
| COMB945952 | 2 | 1 | FM2128 | Positive | 2022-06-27 | 2022-06-27 | Positive | Antigen | Negative | Lab Purif PCR | Positive |  |  | 1 | Referral Confirmed FL Positive |
| COMB999900 | 1 | 0 | not found | not found | not found | 2022-07-01 | Positive | Antigen | Positive |  |  |  |  | 0 | Name not in App anywhere - Appeared only in correspondence w Test Admin re: positive cases. Treat as not tested by FL because only pos/incl is accounted for. |


# 3,949  COSP_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: COSP_pilot-data_summary.md
file_date: 2022-03-07
title: COSP Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2451
tokens: 3949
notes: 
summary_short: The "COSP_pilot-data_summary" covers the FloodLAMP pilot program in a city/EMS program in Coral Springs, FL where city staff operated FloodLAMP for pooled self-collection testing of EMS, first responders, and city employees, with test processing done on-site using a double standard configuration. The program ran over 6 months (2021-08-31 to 2022-03-07), testing 7,146 tubes from 22,643 participant results (avg pool size 3.2) with 347 positive tubes detected.


CONTENT

## Plots

### Composite

![COSP Weekly Composite](_plots/COSP_weekly_composite.png)

### Percent Positive Tubes

![COSP Weekly Percent Positives](_plots/COSP_weekly_percent_positives.png)

### Volume

![COSP Weekly Volume](_plots/COSP_weekly_volume.png)

## Files

### Google Sheets URLs
- [COSP_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1LnTBrjaiG5Eg8uDSXU7C4sAcKxiF978MzCWPg-VDtx4)
- [COSP_RSR_deID_PUB](https://docs.google.com/spreadsheets/d/1H7Dgq-RRdBbd3pMm9Fynb8sPu-mzpb-kdFqzOEUVkZI)

### Curated CSVs
- Curated CSV folder: `COSP_curated_csvs/`
- Stats key-values CSV: [COSP_APS_stats_key-values.csv](COSP_curated_csvs/COSP_APS_stats_key-values.csv)
- Weekly summary CSV: [COSP_APS_weekly-summary.csv](COSP_curated_csvs/COSP_APS_weekly-summary.csv)
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [COSP_APS_deID_PUB.xlsx](COSP_xlsx_downloads/COSP_APS_deID_PUB.xlsx)
- [COSP_RSR_deID_PUB.xlsx](COSP_xlsx_downloads/COSP_RSR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | NONE | ok |  |  | Stats | 1 |
| Files | RTR File | NONE | ok |  |  | Stats | 2 |
| Files | RSR File | COSP_RSR_deID_PUB | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 7,146 | ok | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 7,146 | ok | includes re-runs | no RFR so no info on re-runs | Stats | 6 |
| Overall | Number of Initial Runs | 123 | ok |  | use collection date assuming all tubes run same day | Stats | 7 |
| Overall | Number of APS Only Tubes run | 7,146 | ok |  | No RFR so all tubes are APS Only | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 7,146 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 22,643 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 0 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 22,643 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 3.2 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) |  | not_available | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) |  | not_available | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes |  | not_available | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs |  | not_available |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs |  | not_available |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 347 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 4.9% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) |  | not_available | Subtract off Re-tests | Not Available - Data provided to FloodLAMP by does not enable us to calculate this | Stats | 26 |
| Positives | Known Positive Cases |  | not_available | Previous tested (including by FloodLAMP test) or reported positive | Not Available - Coral Springs did not report this in RSR forms | Stats | 27 |
| Positives | Unknown Positive Cases |  | not_available |  | Not Available - Coral Springs did not report this in RSR forms | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 1 | ok |  | from RSR - Run Summary Report that draws from google form of weekly testing summary provided by test Admin | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results |  | not_available |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 1 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.0% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 0.0% | ok |  |  | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative |  | not_available |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence |  | not_available |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 12 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App | Conclude the "Other Per Week" column was Initial Inconclusives and Final Inconclusives were reported in App (Run Summary Form had an Inconclusives question field) | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 12 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 0.2% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 0 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 0 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive | Not Available | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  | Not Available | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive |  | not_available |  | Not Available | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative |  | not_available |  | Not Available | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence |  | not_available |  | Not Available | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) |  | not_available |  | Not Available | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests |  | not_available |  | Not Available | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative |  | not_available | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative | Not Available | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative |  | not_available |  | Not Available | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative |  | not_available |  | Not Available | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative |  | not_available |  | Not Available | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 1,074 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 264 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 347 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 32.3% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 347 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 32.3% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-08-31 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2022-03-07 | ok |  |  | Stats | 75 |
| Info | Test Operator | City of Coral Springs | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Office Space | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | EMS, First Responders, City Staff | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Double Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled | ok |  Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Coral Springs | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Municipal Building | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | City / EMS | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Coral Springs, FL | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-08-30 | 2021-09-05 | 111 | 32 | 0 | 0 | 0.0% | ok |
| 2021-09-06 | 2021-09-12 | 113 | 35 | 0 | 0 | 0.0% | ok |
| 2021-09-13 | 2021-09-19 | 110 | 33 | 0 | 0 | 0.0% | ok |
| 2021-09-20 | 2021-09-26 | 153 | 44 | 0 | 0 | 0.0% | ok |
| 2021-09-27 | 2021-10-03 | 116 | 32 | 0 | 0 | 0.0% | ok |
| 2021-10-04 | 2021-10-10 | 98 | 31 | 0 | 0 | 0.0% | ok |
| 2021-10-11 | 2021-10-17 | 100 | 30 | 0 | 0 | 0.0% | ok |
| 2021-10-18 | 2021-10-24 | 49 | 14 | 0 | 0 | 0.0% | ok |
| 2021-10-25 | 2021-10-31 | 84 | 23 | 0 | 0 | 0.0% | ok |
| 2021-11-01 | 2021-11-07 | 79 | 21 | 0 | 0 | 0.0% | ok |
| 2021-11-08 | 2021-11-14 | 61 | 16 | 14 | 0 | 87.5% | ok |
| 2021-11-15 | 2021-11-21 | 69 | 18 | 0 | 0 | 0.0% | ok |
| 2021-11-22 | 2021-11-28 | 30 | 9 | 0 | 0 | 0.0% | ok |
| 2021-11-29 | 2021-12-05 | 81 | 23 | 0 | 0 | 0.0% | ok |
| 2021-12-06 | 2021-12-12 | 76 | 20 | 0 | 0 | 0.0% | ok |
| 2021-12-13 | 2021-12-19 | 84 | 29 | 1 | 2 | 3.4% | ok |
| 2021-12-20 | 2021-12-26 | 216 | 67 | 9 | 0 | 13.4% | ok |
| 2021-12-27 | 2022-01-02 | 1263 | 418 | 58 | 0 | 13.9% | ok |
| 2022-01-03 | 2022-01-09 | 2451 | 828 | 93 | 0 | 11.2% | ok |
| 2022-01-10 | 2022-01-16 | 2580 | 858 | 74 | 0 | 8.6% | ok |
| 2022-01-17 | 2022-01-23 | 2310 | 746 | 41 | 0 | 5.5% | ok |
| 2022-01-24 | 2022-01-30 | 2649 | 844 | 30 | 0 | 3.6% | ok |
| 2022-01-31 | 2022-02-06 | 2512 | 773 | 15 | 0 | 1.9% | ok |
| 2022-02-07 | 2022-02-13 | 2469 | 744 | 8 | 0 | 1.1% | ok |
| 2022-02-14 | 2022-02-20 | 2424 | 734 | 3 | 0 | 0.4% | ok |
| 2022-02-21 | 2022-02-27 | 1865 | 570 | 1 | 0 | 0.2% | ok |
| 2022-02-28 | 2022-03-06 | 488 | 153 | 0 | 0 | 0.0% | ok |
| 2022-03-07 | 2022-03-13 | 2 | 1 | 0 | 0 | 0.0% | ok |


# 6,546  CRLN_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: CRLN_pilot-data_summary.md
file_date: 2022-05-31
title: CRLN Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 3973
tokens: 6546
notes: 
summary_short: The "CRLN_pilot-data_summary" covers the FloodLAMP pilot program for Carillon, a preschool in Portola Valley, CA that used FloodLAMP for pooled household and individual self-collection testing of students, staff, and families, with test processing done by FloodLAMP in a dedicated garage room using a standard equipment configuration. The program ran over 5 months (2021-12-24 to 2022-05-31), testing 1,016 tubes from 2,340 participant results (avg pool size 2.4) with 32 positive tubes detected.


CONTENT

## Plots

### Composite

![CRLN Weekly Composite](_plots/CRLN_weekly_composite.png)

### Percent Positive Tubes

![CRLN Weekly Percent Positives](_plots/CRLN_weekly_percent_positives.png)

### Volume

![CRLN Weekly Volume](_plots/CRLN_weekly_volume.png)

## Files

### Google Sheets URLs
- [FLMP_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1ni39vn-fdXq0HrOgHbim_FK0OZidUv-YBLvzPwhhlFQ)
- [FLMP_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/16CwPJ9LeknD8lJFTr-gJSx916WZaGEMbN6iKnlVx4dI)
- [FLMP_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/16R3LlannlrGfiIIJq4T3EWjbtFLZrtPC4gkKycu8RXc)

### Curated CSVs
- Curated CSV folder: `CRLN_curated_csvs/`
- Stats key-values CSV: [CRLN_APS_stats_key-values.csv](CRLN_curated_csvs/CRLN_APS_stats_key-values.csv)
- Weekly summary CSV: [CRLN_RFR_weekly-summary.csv](CRLN_curated_csvs/CRLN_RFR_weekly-summary.csv)
- Referral tests by person CSV: [CRLN_RTR_referral-tests-by-person.csv](CRLN_curated_csvs/CRLN_RTR_referral-tests-by-person.csv)

### XLSX downloads:
- [FLMP_APS_deID_PUB.xlsx](../FLMP_pilot-data/FLMP_xlsx_downloads/FLMP_APS_deID_PUB.xlsx)
- [FLMP_RFR_deID_PUB.xlsx](../FLMP_pilot-data/FLMP_xlsx_downloads/FLMP_RFR_deID_PUB.xlsx)
- [FLMP_RTR_deID_PUB.xlsx](../FLMP_pilot-data/FLMP_xlsx_downloads/FLMP_RTR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | FLMP_RFR_deID_PUB |  |  | Stats | 1 |
| Files | RTR File | FLMP_RTR_deID_PUB |  |  | Stats | 2 |
| Files | RSR File | NONE |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 1,016 | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 1,086 | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 79 |  | divide CRLN by time period 1-2 to 5-31 | Stats | 7 |
| Overall | Number of APS Only Tubes run | 111 |  | divide CRLN by time period 1-2 to 5-31 | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 1,130 | includes technical replicates (the same tube sample in multiple reactions in the same run) | divide CRLN by time period 1-2 to 5-31 - 135 is num FLSP tubes in CRLN time period and 1290 is num RFR audit rxns during CRLN time period | Stats | 9 |
| Overall | Number of Participant Results | 2,340 | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 48 | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF | all during CRLN period so assign to CRLN | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 2,388 | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 2.4 |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 70 | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 205 | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 6.9% | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 31 |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 39.2% |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 32 |  | count from VALUES Pos and Incl | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 3.1% |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 13 | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 3 | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 10 |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 4 |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 4 |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.4% |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 1 |  | 2022-05-08T00:00:00 | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 25.0% |  | 2/4 unknown and 1 of those was in household of positives | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 1 |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 2 |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 33 | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App | No 2.5 correction code, Sum AE - AF = 36 | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 40 | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 3.7% | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 10 | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 9 | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 1 |  | 2022-05-08T00:00:00 | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 1 |  | 2022-02-14T00:00:00 | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 2 |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 8 |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 8 |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 4 | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 50.0% |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 0 |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 0.0% |  |  | Stats | 57 |
| False Calls | False Positives Final Results |  | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) |  | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 142 | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 51 | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 17 | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 12.0% |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 40 |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 28.2% |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-12-24 |  |  | Stats | 74 |
| Dates | End Run Date | 2022-05-31 |  |  | Stats | 75 |
| Info | Test Operator | FloodLAMP | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Garage Dedicated Room | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Students, Staff, Families | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled Household, Individual | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Carillon | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Preschool | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Preschool | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Portola Valley, CA | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |
| Pooling | Number of Initial FloodLAMP Positive Pools | 10 |  |  | Stats | 92 |
| Pooling | Number of Initial FloodLAMP Positive Pools with Indiv Deconvolution | 5 |  |  | Stats | 93 |
| Pooling | Number of Initial FloodLAMP Positive Pools Confirmed by Referral Testing | 6 |  |  | Stats | 94 |
| Pooling | Number of Initial Confirmed FL Pools where the organization member (i.e. parent or other child) was Positive | 4 |  |  | Stats | 95 |
| Pooling | Number of Initial Confirmed FL Pools where Positive Individual was not the organization member (i.e. parent or other child) | 2 |  |  | Stats | 96 |
| Pooling | % Confirmed Positive Pools where Positive Individual was not the organization member (i.e. parent or other child) | 33.3% |  |  | Stats | 97 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-12-20 | 2021-12-26 | 4 | 1 | 0 | 0 | 0.0% | ok |
| 2021-12-27 | 2022-01-02 | 34 | 12 | 2 | 0 | 16.7% | ok |
| 2022-01-03 | 2022-01-09 | 85 | 37 | 6 | 0 | 16.2% | ok |
| 2022-01-10 | 2022-01-16 | 173 | 83 | 11 | 1 | 13.3% | ok |
| 2022-01-17 | 2022-01-23 | 162 | 71 | 5 | 0 | 7.0% | ok |
| 2022-01-24 | 2022-01-30 | 150 | 62 | 0 | 0 | 0.0% | ok |
| 2022-01-31 | 2022-02-06 | 143 | 58 | 0 | 0 | 0.0% | ok |
| 2022-02-07 | 2022-02-13 | 148 | 60 | 0 | 0 | 0.0% | ok |
| 2022-02-14 | 2022-02-20 | 128 | 54 | 0 | 1 | 0.0% | ok |
| 2022-02-21 | 2022-02-27 | 55 | 21 | 0 | 0 | 0.0% | ok |
| 2022-02-28 | 2022-03-06 | 51 | 25 | 0 | 0 | 0.0% | ok |
| 2022-03-07 | 2022-03-13 | 113 | 52 | 0 | 0 | 0.0% | ok |
| 2022-03-14 | 2022-03-20 | 91 | 42 | 0 | 0 | 0.0% | ok |
| 2022-03-21 | 2022-03-27 | 110 | 44 | 0 | 0 | 0.0% | ok |
| 2022-03-28 | 2022-04-03 | 22 | 9 | 0 | 0 | 0.0% | ok |
| 2022-04-04 | 2022-04-10 | 110 | 43 | 0 | 0 | 0.0% | ok |
| 2022-04-11 | 2022-04-17 | 100 | 40 | 0 | 0 | 0.0% | ok |
| 2022-04-18 | 2022-04-24 | 110 | 47 | 0 | 0 | 0.0% | ok |
| 2022-04-25 | 2022-05-01 | 107 | 42 | 0 | 0 | 0.0% | ok |
| 2022-05-02 | 2022-05-08 | 108 | 47 | 2 | 0 | 4.3% | ok |
| 2022-05-09 | 2022-05-15 | 111 | 62 | 4 | 2 | 6.5% | ok |
| 2022-05-16 | 2022-05-22 | 92 | 44 | 1 | 0 | 2.3% | ok |
| 2022-05-23 | 2022-05-29 | 89 | 41 | 1 | 0 | 2.4% | ok |
| 2022-05-30 | 2022-06-05 | 42 | 19 | 0 | 0 | 0.0% | ok |

### Referral tests by person

| participant_id | num_sequential_referral_tests | num_floodlamp_results_pos_or_incl | floodlamp_tube_id | floodlamp_test_result | floodlamp_test_date | first_referral_test_date | referral_overall_result | first_referral_test_type | first_referral_test_result | second_referral_test_type | second_referral_test_result | third_referral_test_type | third_referral_test_result | antigen_neg_with_other_positive_flag | referral_eval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLMP132170 | 7 | 0 | MA100A | Negative | 2022-05-02 | 2022-05-02 | Negative | PCR | Negative | Antigen | Negative | Antigen | Negative | False | FL pos pool of 3 in morning then indiv deconvl with FL and this person was neg but there was 1 FL deconv pos that was confirmed by PCR (neg by antigen initally then pos 2 days later) |
| FLMP147333 | 6 | 2 | FLT1465 | Positive | 2022-01-10 | 2022-01-09 | Positive | Antigen | Positive | PCR | Positive |  |  | False | known pos that tested pos by FL - not sure if they told us about antigen result before FL test |
| FLMP172687 | 1 | 1 | FLB5889 | Positive | 2022-01-06 | 2022-12-30 | NA - Return Test | Antigen | Positive |  |  |  |  | NA - Return Test | FL test (pos) was test to return after anitgen pos test 7 days prior |
| FLMP254321 | 2 | 0 | FLE269 | Negative | 2022-05-09 | 2022-05-09 | Negative | Antigen | Negative | PCR | Negative |  |  | False | FL incl pool of 3, then indiv deconv and 1 of 3 pos, this one was FL neg and also neg by PCR and antigen |
| FLMP290315 | 1 | 0 | NO FL testing |  |  | 2022-05-16 | Negative | Antigen | Negative |  |  |  |  | False |  |
| FLMP302189 | 3 | 4 | FLT1433 | Positive | 2022-01-02 | 2022-01-02 | Positive | Antigen | Negative | PCR | Positive |  |  | True | parent tested neg by antigen so did indiv deconv FL test and was pos |
| FLMP322473 | 1 | 0 | AH679 | Negative | 2022-05-09 | 2022-05-09 | Negative | PCR | Negative |  |  |  |  | False |  |
| FLMP325595 | 1 | 0 | AH245 | Negative | 2022-05-09 | 2022-05-09 | Negative | PCR | Negative |  |  |  |  | False |  |
| FLMP330127 | 4 | 2 | FLT1400 | Positive | 2022-01-10 | 2022-01-07 | Positive | Antigen | Positive | PCR | Positive |  |  | False | known pos that tested pos by FL - not sure if they told us about antigen result before FL test |
| FLMP464138 | 7 | 0 | MA82 | Negative | 2022-05-02 | 2022-05-02 | Negative | PCR | Negative | Antigen | Negative | Antigen | Negative | False | FL pos pool of 3 in morning then indiv deconvl with FL and this person was neg but there was 1 FL deconv pos that was confirmed by PCR (neg by antigen initally then pos 2 days later) |
| FLMP472803 | 7 | 1 | MA57 | Negative | 2022-05-02 | 2022-05-02 | Negative | PCR | Negative | Antigen | Negative | Antigen | Negative | False | FL pos pool of 3 in morning then indiv deconvl with FL and this person was neg but there was 1 FL deconv pos that was confirmed by PCR (neg by antigen initally then pos 2 days later) |
| FLMP473007 | 2 | 0 | FLB6845 | Positive | 2022-01-02 | 2022-01-03 | Positive | Antigen | Positive | PCR | Positive |  |  | False | Only initial FL positive pool - no indiv deconv |
| FLMP549529 | 1 | 1 | FLB5830 | Positive | 2022-01-06 | 2022-01-01 | NA - Return Test | Antigen | Positive |  |  |  |  | NA - Return Test | FL test (pos) was test to return after anitgen pos test 5 days prior |
| FLMP552537 | 2 | 2 | FLE202 | Positive | 2022-05-09 | 2022-05-09 | Positive | Antigen | Positive | PCR | Positive |  |  | False | FL incl pool of 3, then indiv deconv and 1 of 3 pos, this one was confrimed by PCR and antigen |
| FLMP601970 | 1 | 1 | FLT1129 | Positive | 2022-01-17 | 2022-01-18 | Positive | Antigen | Positive |  |  |  |  | False | this was a later return test - the CRLN child did not test on 1-10 with parents |
| FLMP608363 | 1 | 2 | AH365 | Positive | 2022-05-09 | 2022-05-09 | Positive | PCR | Positive |  |  |  |  | False | CRLN child (no symptomys) - FL pos pool of 4 then indiv deconv by FL with 1 of 4 pos and this one confimed by PCR |
| FLMP652238 | 2 | 1 | FLB6845 | Positive | 2022-01-02 | 2022-01-03 | Negative | Antigen | Negative | PCR | Negative |  |  | False | Only initial FL positive pool - no indiv deconv |
| FLMP687722 | 8 | 2 | MA108 | Positive | 2022-05-02 | 2022-05-02 | Positive | Antigen | Negative | PCR | Positive | Antigen | Positive | True | FL pos pool of 3 in morning then indiv deconvl with FL and this person was pos that was confirmed by PCR (neg by antigen initally then pos 2 days later) - other 3 in pool neg by PCR and antigen |
| FLMP705416 | 2 | 0 | FLB5969 | Negative | 2022-05-09 | 2022-05-09 | Positive | Antigen | Negative | PCR | Positive |  |  | True | FL incl pool of 3, then indiv deconv and 1 of 3 pos, this one was FL neg and also neg by antigen byt pos by PCR |
| FLMP776278 | 3 | 3 | FLT1433 | Positive | 2022-01-02 | 2022-01-04 | Positive | Antigen | Positive | PCR | Positive |  |  | False | Non-CRLN child that test pos by antigen so no indiv deconv FL test |
| FLMP779627 | 1 | 0 | AJ9253 | Negative | 2022-05-09 | 2022-05-09 | Negative | PCR | Negative |  |  |  |  | False |  |
| FLMP828735 | 4 | 3 | FLT1433 | Positive | 2022-01-02 | 2022-01-04 | Positive | Antigen | Positive | PCR | Positive |  |  | False | CRLN child that test pos by antigen so no indiv deconv FL test |
| FLMP857562 | 3 | 2 | FLT1433 | Positive | 2022-01-02 | 2022-01-02 | Positive | Antigen | Negative | PCR | Positive |  |  | True | parent tested neg by antigen so did indiv deconv FL test and was pos |
| FLMP858721 | 1 | 1 | FLT1136 | Positive | 2022-01-06 | 2022-12-29 | NA - Return Test | Antigen | Positive |  |  |  |  | NA - Return Test | FL test (pos) was test to return after anitgen pos test 8 days prior |
| FLMP876455 | 1 | 0 | FLT1161 | Positive | 2022-01-10 | 2022-01-12 | Negative | PCR | Negative |  |  |  |  | False | FL pos pool of 3 in morning then indiv deconvl with FL and this person was neg along with one other both by PCR, and 3rd pool person was PCR pos |
| FLMP887888 | 4 | 2 | FLT1161 | Positive | 2022-01-10 | 2022-01-04 | Positive | PCR | Positive |  |  |  |  | False | FL pos pool of 3 in morning then indiv deconvl with FL and only this person was pos (other 2 FL and the referral PCR neg) - ignore neg antigen tests for analysis because they were 6 days before and 5 days after FL tests |
| FLMP915544 | 2 | 0 | FLB6845 | Positive | 2022-01-02 | 2022-01-03 | Positive | Antigen | Positive | PCR | Positive |  |  | False | Only initial FL positive pool - no indiv deconv |
| FLMP939793 | 1 | 0 | FLB5852 | Negative | 2022-01-06 | 2022-12-30 | NA - Return Test | Antigen | Positive |  |  |  |  | NA - Return Test | FL test (neg) was test to return after anitgen pos test 7 days prior |
| FLMP942437 | 1 | 0 | NO FL testing |  |  | 2022-05-16 | Positive | Antigen | Positive |  |  |  |  | False |  |
| FLMP969044 | 1 | 0 | FLT1161 | Positive | 2022-01-10 | 2022-01-12 | Negative | PCR | Negative |  |  |  |  | False | FL pos pool of 3 in morning then indiv deconvl with FL and this person was neg along with one other both by PCR, and 3rd pool person was PCR pos |
| FLMP987142 | 4 | 2 | FLB6807 | Positive | 2022-05-19 | 2022-05-16 | Positive | Antigen | Negative | Antigen | Negative | PCR | Positive | True | Partner tested pos by antigen then this partner tested neg by antigen 3 days in a row then next day was FL pos, which was confirmed by PCR collected same day and resulted 2 days later (this was a teacher - so FL screening likely stopped spread!) |


# 4,070  DAVI_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: DAVI_pilot-data_summary.md
file_date: 2022-03-18
title: DAVI Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2539
tokens: 4070
notes: 
summary_short: The "DAVI_pilot-data_summary" covers the FloodLAMP pilot program in a city/EMS program in Davie, FL where fire department staff operated FloodLAMP for pooled self-collection testing of EMS, first responders, and city staff at their fire station, using a standard configuration without the FloodLAMP mobile app. The program ran over 6 months (2021-09-01 to 2022-03-18), testing 2,279 tubes from 4,409 participant results with 384 positive tubes detected (16.8% positivity rate during the Delta and Omicron waves). All sample processing for the ROSA production pilot program was performed at the Davie site by the Davie staff.


CONTENT

## Plots

### Composite

![DAVI Weekly Composite](_plots/DAVI_weekly_composite.png)

### Percent Positive Tubes

![DAVI Weekly Percent Positives](_plots/DAVI_weekly_percent_positives.png)

### Volume

![DAVI Weekly Volume](_plots/DAVI_weekly_volume.png)

## Files

### Google Sheets URLs
- [DAVI_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/1gIvvt-IHhGwbIv_mVSF5QEfjbm5WdoSUDe4MW8SSCcA)
- [DAVI_RSR_deID_PUB](https://docs.google.com/spreadsheets/d/1QslpxtCjyHeau4SIHuLbkjLaLtB7tNrK3jQh96s3bIo)

### Curated CSVs
- Curated CSV folder: `DAVI_curated_csvs/`
- Stats key-values CSV: [DAVI_RSR_stats_key-values.csv](DAVI_curated_csvs/DAVI_RSR_stats_key-values.csv)
- Weekly summary CSV: [DAVI_RSR_weekly-summary.csv](DAVI_curated_csvs/DAVI_RSR_weekly-summary.csv)
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [DAVI_RSR_deID_PUB.xlsx](DAVI_xlsx_downloads/DAVI_RSR_deID_PUB.xlsx)
- [DAVI_RTR_deID_PUB.xlsx](DAVI_xlsx_downloads/DAVI_RTR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | NONE | ok |  |  | Stats | 1 |
| Files | RTR File | DAVI_RTR_PHI_v2.0 | ok |  |  | Stats | 2 |
| Files | APS File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 2,279 | ok | initial run tubes only so excludes re-runs | Have no data on re-runs so just use reported tubes/pools total | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 2,279 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 50 | ok |  | Use estimated number of runs based on number of days and pools run in  RSR reported weekly total | Stats | 7 |
| Overall | Number of APS Only Tubes run | 0 | ok |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 2,279 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 4,409 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 0 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 4,409 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 1.9 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) |  | not_available | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) |  | not_available | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes |  | not_available | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs |  | not_available |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs |  | not_available |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 384 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 16.8% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) |  | not_available | Subtract off Re-tests | Not Available - not tube level data so no way to know cases | Stats | 26 |
| Positives | Known Positive Cases | 329 | ok | Previous tested (including by FloodLAMP test) or reported positive | Many Return To Work tests after Initial Positive | Stats | 27 |
| Positives | Unknown Positive Cases | 55 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 1 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results |  | not_available |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 1 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.0% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence |  | not_available |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 0.0% | ok |  |  | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative |  | not_available |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 1 | ok |  | No information on how this Final Inconclusive was resolved | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative |  | not_available | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App |  | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 26 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 1.1% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 44 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests | from Col C of RTR/Referral Antigen Comparison (formula to right) | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 43 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive | One missing was antigen neg same day but never follow up antigen tested - it tested positive by FloodLAMP 4 times over the next 10 days and the person became symptomatic but we cannot count it was an Agree because technically there's no Pos referral test | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  | No information on the singe Final Inconclusive | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 97.7% | ok |  | This excludes many we do not have referral data on | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 1 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 44 | ok |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 38 | ok |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 4 | ok | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative | See table at the top right of RTR/Referral Antigen Comparison (formula to right) | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 10.5% | ok |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 0 | ok |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 0.0% | ok |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested |  | not_available | Includes UnknownPerson additions but not ARF tubes | Not Available - Data provided to FloodLAMP does not enable us to calculate this | Stats | 64 |
| People | Number of Unique Sponsors |  | not_available | People who collect using the app | Not Available - Data provided to FloodLAMP does not enable us to calculate this | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive |  | not_available | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral | Not Available - Data provided to FloodLAMP does not enable us to calculate this | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) |  | not_available |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) |  | not_available |  | Not Available - Data provided to FloodLAMP does not enable us to calculate this | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) |  | not_available |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-09-01 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2022-03-18 | ok |  |  | Stats | 75 |
| Info | Test Operator | Davie Fire and Rescue | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Fire Station Office | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | EMS, First Responders, City Staff | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled | ok |  Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | No | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Davie | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Fire Station | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | City / EMS | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Davie, FL | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-08-30 | 2021-09-05 | 54 | 19 | 2 | 0 | 10.5% | ok |
| 2021-09-06 | 2021-09-12 | 75 | 26 | 3 | 1 | 11.5% | ok |
| 2021-09-13 | 2021-09-19 | 75 | 26 | 4 | 0 | 15.4% | ok |
| 2021-09-20 | 2021-09-26 | 75 | 27 | 4 | 0 | 14.8% | ok |
| 2021-09-27 | 2021-10-03 | 107 | 59 | 1 | 0 | 1.7% | ok |
| 2021-10-04 | 2021-10-10 | 130 | 49 | 0 | 0 | 0.0% | ok |
| 2021-10-11 | 2021-10-17 | 91 | 40 | 0 | 0 | 0.0% | ok |
| 2021-10-18 | 2021-10-24 | 123 | 52 | 0 | 0 | 0.0% | ok |
| 2021-10-25 | 2021-10-31 | 80 | 30 | 1 | 0 | 3.3% | ok |
| 2021-11-01 | 2021-11-07 | 61 | 28 | 3 | 0 | 10.7% | ok |
| 2021-11-08 | 2021-11-14 | 80 | 34 | 2 | 0 | 5.9% | ok |
| 2021-11-15 | 2021-11-21 | 111 | 41 | 0 | 0 | 0.0% | ok |
| 2021-11-22 | 2021-11-28 | 48 | 17 | 0 | 0 | 0.0% | ok |
| 2021-11-29 | 2021-12-05 | 117 | 62 | 0 | 0 | 0.0% | ok |
| 2021-12-06 | 2021-12-12 | 115 | 55 | 2 | 0 | 3.6% | ok |
| 2021-12-13 | 2021-12-19 | 159 | 85 | 4 | 0 | 4.7% | ok |
| 2021-12-20 | 2021-12-26 | 269 | 151 | 16 | 0 | 10.6% | ok |
| 2021-12-27 | 2022-01-02 |  |  | 0 |  |  | not_available |
| 2022-01-03 | 2022-01-09 | 801 | 575 | 217 | 0 | 37.7% | ok |
| 2022-01-10 | 2022-01-16 | 350 | 225 | 60 | 0 | 26.7% | ok |
| 2022-01-17 | 2022-01-23 | 216 | 118 | 29 | 0 | 24.6% | ok |
| 2022-01-24 | 2022-01-30 | 202 | 108 | 14 | 0 | 13.0% | ok |
| 2022-01-31 | 2022-02-06 | 217 | 110 | 11 | 0 | 10.0% | ok |
| 2022-02-07 | 2022-02-13 | 223 | 91 | 9 | 0 | 9.9% | ok |
| 2022-02-14 | 2022-02-20 | 227 | 92 | 2 | 0 | 2.2% | ok |
| 2022-02-21 | 2022-02-27 | 168 | 63 | 0 | 0 | 0.0% | ok |
| 2022-02-28 | 2022-03-06 | 94 | 37 | 0 | 0 | 0.0% | ok |
| 2022-03-07 | 2022-03-13 | 70 | 26 | 0 | 0 | 0.0% | ok |
| 2022-03-14 | 2022-03-20 | 71 | 33 | 0 | 0 | 0.0% | ok |


# 8,120  DAVI_pilot-data_referral-antigen-comparison.md
METADATA
last updated: 2026-01-25
file_name: DAVI_pilot-data_referral-antigen-comparison.md
file_date: 2022-03-18
title: DAVI Pilot Data Referral Antigen Comparison
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: https://docs.google.com/document/d/13mShkjR7lnJSbZnggKarg6NDrgYXdhvEaPbQSLn3zaA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 4754
tokens: 8120
notes: DAVI has a custom referral-antigen-comparison format instead of standard referral tests.
summary_short: The "DAVI_pilot-data_referral-antigen-comparison" covers a custom FloodLAMP referral-antigen comparison dataset from the Davie city/EMS pilot in Davie, FL, where fire department staff ran pooled self-collection testing of EMS, first responders, and city staff at a fire station using a standard configuration without the FloodLAMP mobile app. It summarizes same-day and follow-up comparisons between FloodLAMP and BinaxNOW results across three testing-policy periods during the 2021-09-01 to 2022-03-18 program, including 44 FloodLAMP-positive cases with referral antigen data, 38 same-day antigen comparisons, and 4 same-day antigen-negative cases later supported by follow-up results.


CONTENT

## Files

### Google Sheets URLs
- [DAVI_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/1gIvvt-IHhGwbIv_mVSF5QEfjbm5WdoSUDe4MW8SSCcA/edit?usp=drive_link)
- [DAVI_RSR_deID_PUB](https://docs.google.com/spreadsheets/d/1QslpxtCjyHeau4SIHuLbkjLaLtB7tNrK3jQh96s3bIo/edit?usp=drive_link)

### Curated CSVs
- Curated CSV folder: `DAVI_curated_csvs/`
- [DAVI_RSR_stats_key-values.csv](DAVI_curated_csvs/DAVI_RSR_stats_key-values.csv)
- [DAVI_RSR_stats_referral-agreement.csv](DAVI_curated_csvs/DAVI_RSR_stats_referral-agreement.csv)
- [DAVI_RSR_weekly-summary.csv](DAVI_curated_csvs/DAVI_RSR_weekly-summary.csv)
- [DAVI_RTR_referral-antigen-comparison.csv](DAVI_curated_csvs/DAVI_RTR_referral-antigen-comparison.csv)
- [DAVI_csv-manifest.csv](DAVI_curated_csvs/DAVI_csv-manifest.csv)

### XLSX downloads:
- [DAVI_RSR_deID_PUB.xlsx](DAVI_xlsx_downloads/DAVI_RSR_deID_PUB.xlsx)
- [DAVI_RTR_deID_PUB.xlsx](DAVI_xlsx_downloads/DAVI_RTR_deID_PUB.xlsx)

## Summary: Same Day Test Comparison

Comparison of FloodLAMP (FL) and BinaxNOW (B) same-day test results:

|  | FL +, B - | FL +, B + |
| --- | --- | --- |
| Asymptomatic | 3 | 12 |
| Symptomatic | 1 | 26 |
| Total | 4 | 38 |
| % Asymp | 0.75 | 31.6% |

## Legend

| Abbreviation | Meaning |
| --- | --- |
| FL | FloodLAMP |
| B | BinaxNOW Rapid Antigen |
| ASY | Asymptomatic |
| SYM | Symptomatic |
| RTW | Return To Work |
| V1/V2/V3 | Vaccinated 1/2/3 doses |
| UN | Unvaccinated |

- + on FloodLAMP and - on BinaxNOW: 3
- + on FloodLAMP and + on BinaxNOW: 12 (80%)

## Group 1

_Testing between Sept 15th and Dec 23rd (FloodLAMP used as main test and BinaxNOW used sometimes at home on day 0)_

### As Reported

| No Referral | Disagree | Agree | Vaccine |  | Employee | Test Results Day 0 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Day 11 | Day 12 | Day 13 | Day 14 | Day 15 | Day 10+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | True | V2 | 1 | 1 | FL +, B +, ASY |  | FL +, SYM |  | FL +, SYM |  | FL +, SYM | FL - | RTW |  |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 2 | FL +, B +, SYM |  | FL +, SYM |  | FL +, SYM |  | FL +, SYM |  | FL + |  | FL - | RTW |  |  |  |  | Day 10 FL -, Day 11 RTW |
|  |  | True | V2 |  | 3 | FL +, B +, SYM |  | FL +, SYM |  | FL +, SYM |  | FL +, SYM | FL - | RTW |  |  |  |  |  |  |  |  |
| True |  |  | UN |  | 4 | FL +, ASY |  | FL + |  | FL + |  | FL + |  | FL + |  | FL + | FL - | RTW |  |  |  | Day 10 FL +, Day 11 FL -, Day 12 RTW |
| True |  |  | V3 |  | 5 | FL +, SYM |  | FL + |  | FL + |  | FL + |  | FL + | FL - | RTW |  |  |  |  |  | Day 10 RTW |
| True |  |  | V3 |  | 6 | FL +, SYM |  |  | FL +, SYM | FL +, SYM |  | FL + |  | FL + |  | FL + |  |  | FL - | RTW |  | Day 10 FL +, Day 13 FL -, Day 14 RTW |
|  |  | True | V2 |  | 7 | FL +, B +, SYM |  | FL + |  | FL - | RTW |  |  |  |  |  |  |  |  |  |  |  |
|  |  | True | UN |  | 8 | FL +, B +, SYM |  | FL + SYM | FL + |  | FL - | RTW |  |  |  |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 9 | FL +, B +, SYM |  | FL + SYM |  | FL + SYM |  | FL - | RTW |  |  |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 10 | FL +, B +, SYM |  | FL + SYM |  | FL + |  | FL - | RTW |  |  |  |  |  |  |  |  |  |
| True |  |  | V3 |  | 11 | FL +, ASY |  | FL + ASY |  | FL + |  | FL - | RTW |  |  |  |  |  |  |  |  |  |
| True |  |  | V3 |  | 12 | FL +, ASY |  | FL + ASY |  | FL + | FL - | RTW |  |  |  |  |  |  |  |  |  |  |
| True |  |  | UN |  | 13 | FL +, SYM |  |  | FL + SYM |  |  | FL + SYM |  |  | FL - | RTW |  |  |  |  |  | Day 10 RTW |
|  | 1 |  | UN | 1 | 14 | FL +, B -, ASY |  | FL + SYM |  |  | FL + SYM |  | FL + SYM |  |  | FL + |  |  | FL - | RTW |  | Day 10 FL +, Day 13 FL -, Day 14 RTW |
| True |  |  | V3 |  | 15 | FL +, SYM |  | FL + SYM |  | FL + SYM |  | FL + |  |  | FL - | RTW |  |  |  |  |  | Day 10 RTW |

### Structured

| Start Date Range | End Date Range | Vaccinated Doses | Symptoms | Day 0 FloodLAMP Result | Day 0 Antigen Result | FloodLAMP Test with Same Day Antigen | Day # FloodLAMP Neg | Day # Antigen  Neg | Day # Return to Work | # FL Pos Tests after Initial before Neg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 2 | Asymptomatic | Positive | Positive | True | 7 |  | 8 | 3 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 10 |  | 11 | 4 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 2 | Symptomatic | Positive | Positive | True | 7 |  | 8 | 3 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 0 | Asymptomatic | Positive |  | False | 11 |  | 12 | 5 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Symptomatic | Positive |  | False | 9 |  | 10 | 4 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Symptomatic | Positive |  | False | 13 |  | 14 | 5 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 2 | Symptomatic | Positive | Positive | True | 4 |  | 5 | 1 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 0 | Symptomatic | Positive | Positive | True | 5 |  | 6 | 2 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 6 |  | 7 | 2 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 6 |  | 7 | 2 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Asymptomatic | Positive |  | False | 6 |  | 7 | 2 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Asymptomatic | Positive |  | False | 5 |  | 6 | 2 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 0 | Symptomatic | Positive |  | False | 9 |  | 10 | 2 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 0 | Asymptomatic | Positive | Negative | True | 13 |  | 14 | 4 |
| 2021-09-15 00:00:00 | 2021-12-23 00:00:00 | 3 | Symptomatic | Positive |  | False | 9 |  | 10 | 3 |

## Group 2

_Testing between Dec 24th and Jan 9th (Both FloodLAMP and BinaxNOW used until cleared to RTW)_

### As Reported

| No Referral | Disagree | Agree | Vaccine |  | Employee | Test Results Day 0 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Day 11 | Day 12 | Day 13 | Day 14 | Day 15 | Day 10+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | True | V3 | 1 | 16 | FL +, B +, ASY | FL +, B + SYM |  | FL +, B + |  |  | FL -, B - | RTW |  |  |  |  |  |  |  |  |  |
|  |  | True | V2 | 1 | 17 | FL +, B +, ASY | FL +, B + SYM |  | FL +, B + |  |  | FL +, B + |  | FL +, B + |  | FL +, B + |  | B - | RTW |  |  | Day 10 FL +, B +, Day 12 B -, Day 13 RTW |
|  |  | True | UN | 1 | 18 | FL +, B -, ASY |  | FL +, B + SYM |  | FL +, B + SYM |  | FL +, B + SYM |  | FL +, B + SYM |  | FL +, B + |  | B + | B + | B - | RTW | Day 10 FL +, B +, Day 12 B +, Day 13 B +, Day 14 B -, Day 15 RTW |
|  |  | True | V3 |  | 19 | FL +, B +, SYM |  | FL +, B + SYM |  | FL +, B + SYM |  | FL +, B + SYM |  |  | B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V3 |  | 20 | FL +, B +, SYM |  |  |  | FL +, B + SYM |  | FL +, B + SYM |  |  | B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V3 |  | 21 | B + SYM | FL +, B + SYM |  |  | FL +, B + SYM |  | FL +, B + SYM |  |  | FL +, B + | FL +, B + |  | FL -, B - | RTW |  |  | Day 10 FL +, B +, Day 12 FL -, B -, Day 13 RTW |
|  |  | True | V2 |  | 22 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  | FL -, B - SYM |  | SYM | SYM | SYM |  | SYM |  |  | RTW | Day 10 SYM, Day 12 SYM, Day 15 RTW |
|  |  | True | V1 | 1 | 23 | FL +, B +, ASY |  | FL +, B + |  | FL +, B + |  | FL +, B + |  | FL -, B - | RTW |  |  |  |  |  |  |  |
|  |  | True | V2 |  | 24 | FL +, B +, SYM |  | FL +, B + SYM |  | FL +, B + SYM |  | FL +, B + SYM |  | FL -, B - | RTW |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 25 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  |  | FL +, B + |  | FL -, B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V3 |  | 26 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  |  |  | FL -, B - | RTW |  |  |  |  |  |  |  |
|  |  | True | UN |  | 27 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  |  | FL +, B + | FL +, B + | FL +, B + | FL -, B - | RTW |  |  |  |  | Day 10 FL -, B -, Day 11 RTW |
|  |  | True | V3 |  | 28 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B + |  |  | FL -, B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V3 |  | 29 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  |  | FL +, B + |  | FL +, B + | FL +, B + |  | FL +, B + |  | FL -, B - | RTW | Day 10 FL +, B +, Day 12 FL +, B +, Day 14 FL -, B -, Day 15 RTW |
|  |  | True | V3 |  | 30 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  |  | FL +, B +, SYM |  | FL +, B + | FL +, R + | FL +, B + | FL -, B - | RTW |  |  | Day 10 FL +, B +, Day 11 FL +, B +, Day 12 FL -, B -, Day 13 RTW |
|  |  | True | V3 | 1 | 31 | FL +, B +, ASY |  | FL +, B +, SYM |  |  |  |  | FL +, B +, SYM |  |  | FL -, B - | RTW |  |  |  |  | Day 10 FL -, B -, Day 11 RTW |
|  |  | True | V2 |  | 32 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B + |  | FL +, B + |  | FL +, B + |  | FL +, B + | FL -,B - | RTW |  |  |  | Day 10 FL +, B +, Day 11 FL -,B -, Day 12 RTW |
|  |  | True | V3 |  | 33 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  |  |  | FL -, B - | RTW |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 34 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B + |  | FL +, B + | FL +, B + | FL +, B + | FL +, B + | FL -, B - | RTW |  |  |  |  | Day 10 FL -, B -, Day 11 RTW |
|  |  | True | UN |  | 35 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B + | FL -, B - | RTW |  |  |  |  |  |  |  |  |  |  |
|  |  | True | V3 | 1 | 36 | FL +, B +, ASY | FL +, B +, SYM |  |  | FL +, B +, SYM |  |  | FL +, B + | FL -, B - | RTW |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 37 | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  | FL +, B +, SYM |  | FL -, B - | RTW |  |  |  |  | Day 10 FL -, B -, Day 11 RTW |

### Structured

| Start Date Range | End Date Range | Vaccinated Doses | Symptoms | Day 0 FloodLAMP Result | Day 0 Antigen Result | FloodLAMP Test with Same Day Antigen | Day # FloodLAMP Neg | Day # Antigen  Neg | Day # Return to Work | # FL Pos Tests after Initial before Neg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Asymptomatic | Positive | Positive | True | 6 | 6 | 7 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 2 | Asymptomatic | Positive | Positive | True |  | 12 | 13 | 5 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 0 | Asymptomatic | Positive | Negative | True |  | 14 | 15 | 5 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True |  | 9 | 10 | 3 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True |  | 9 | 10 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic |  | Positive | False | 12 | 12 | 13 | 5 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 2 | Symptomatic | Positive | Positive | True | 6 | 6 | 15 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 1 | Asymptomatic | Positive | Positive | True | 8 | 8 | 9 | 3 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 2 | Symptomatic | Positive | Positive | True | 8 | 8 | 9 | 3 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 9 | 9 | 10 | 3 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 8 | 8 | 9 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 0 | Symptomatic | Positive | Positive | True | 10 | 10 | 11 | 5 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 9 | 9 | 10 | 3 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 14 | 14 | 15 | 6 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 12 | 12 | 13 | 6 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Asymptomatic | Positive | Positive | True | 10 | 10 | 11 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 2 | Symptomatic | Positive | Positive | True | 11 | 11 | 12 | 5 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 8 | 8 | 9 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 10 | 10 | 11 | 6 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 0 | Symptomatic | Positive | Positive | True | 5 | 5 | 6 | 2 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Asymptomatic | Positive | Positive | True | 8 | 8 | 9 | 3 |
| 2021-12-24 00:00:00 | 2022-01-09 00:00:00 | 3 | Symptomatic | Positive | Positive | True | 10 | 10 | 11 | 4 |

## Group 3

_Testing between Jan 10th and Feb 7th (FloodLAMP used for initial + diagnosis and BinaxNOW used to RTW)_

### As Reported

| No Referral | Disagree | Agree | Vaccine |  | Employee | Test Results Day 0 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Day 11 | Day 12 | Day 13 | Day 14 | Day 15 | Day 10+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | True | V2 | 1 | 38 | FL +, B +, ASY |  | B + SYM |  | B + SYM |  | B + | B - | RTW |  |  |  |  |  |  |  |  |
|  |  | True | V1 | 1 | 39 | FL +, B +, ASY |  | B + SYM |  | B + SYM |  | B + | B - | RTW |  |  |  |  |  |  |  |  |
|  |  | True | V3 | 1 | 40 | FL +, B +, ASY |  | B + ASY |  | B + SYM | B + SYM |  | B + SYM |  | B + SYM | B + SYM |  | B + |  | B + |  | Day 10 B + SYM, Day 12 B +, Day 14 B +, Day 16 B -, Day 17 RTW |
|  |  | True | V3 |  | 41 | FL +, B -, SYM |  | B + SYM |  | B + SYM |  | B + SYM |  | B + | B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V3 |  | 42 | FL +, B +, SYM |  | B + SYM |  | B + SYM |  | B + SYM |  | B + |  | B + | B - | RTW |  |  |  | Day 10 B +, Day 11 B -, Day 12 RTW |
|  |  | True | UN |  | 43 | SYM |  |  |  | B + SYM | FL + SYM |  | B + SYM |  | B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V2 | 1 | 44 | FL +, B +, ASY |  |  |  | B + SYM |  | B - | RTW |  |  |  |  |  |  |  |  |  |
|  |  | True | V3 | 1 | 45 | FL +, B -, ASY |  | B + SYM |  | B + SYM |  | B - | RTW |  |  |  |  |  |  |  |  |  |
|  |  | True | V3 | 1 | 46 | FL +, B +, ASY |  | B + SYM |  | B + SYM |  | B + |  | B +  | B +    | B + | B - | RTW |  |  |  | Day 10 B +, Day 11 B -, Day 12 RTW |
|  |  | True | UN | 1 | 47 | FL +, B +, ASY |  | B + ASY |  | B + ASY | B - | RTW |   |  |  |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 48 | FL +, B +, SYM |  | B + SYM |  | B + SYM |  | B + |  | B - | RTW |  |  |  |  |  |  |  |
|  |  | True | V3 |  | 49 | FL +, B +, SYM |  | B + SYM |  | B + |  | B - | RTW |  |  |  |  |  |  |  |  |  |
|  |  | True | UN |  | 50 | FL +, B +, SYM |  | B + SYM |  | B + SYM |  | B + |  | B + | B - | RTW |  |  |  |  |  | Day 10 RTW |
|  |  | True | V3 |  | 51 | FL +, B +, SYM |  | B + SYM |  | B + SYM |  | B + |  | B + |  | B - | RTW |  |  |  |  | Day 10 B -, Day 11 RTW |

### Structured

| Start Date Range | End Date Range | Vaccinated Doses | Symptoms | Day 0 FloodLAMP Result | Day 0 Antigen Result | FloodLAMP Test with Same Day Antigen | Day # FloodLAMP Neg | Day # Antigen  Neg | Day # Return to Work | # FL Pos Tests after Initial before Neg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 2 | Asymptomatic | Positive | Positive | True |  | 7 | 8 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 1 | Asymptomatic | Positive | Positive | True |  | 7 | 8 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Asymptomatic | Positive | Positive | True |  | 16 | 17 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Symptomatic | Positive | Negative | True |  | 0 | 10 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Symptomatic | Positive | Positive | True |  | 11 | 12 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 0 | Symptomatic |  |  | False |  | 9 | 10 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 2 | Asymptomatic | Positive | Positive | True |  | 6 | 7 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Asymptomatic | Positive | Negative | True |  | 0 | 7 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Asymptomatic | Positive | Positive | True |  | 11 | 12 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 0 | Asymptomatic | Positive | Positive | True |  | 5 | 6 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Symptomatic | Positive | Positive | True |  | 8 | 9 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Symptomatic | Positive | Positive | True |  | 6 | 7 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 0 | Symptomatic | Positive | Positive | True |  | 9 | 10 | 0 |
| 2022-01-10 00:00:00 | 2022-02-07 00:00:00 | 3 | Symptomatic | Positive | Positive | True |  | 10 | 11 | 0 |


# 4,317  DAVI_pilot-data_referral-antigen-comparison_AI-ANALYSIS-AND-CHECK.md
METADATA
last updated: 2026-03-04 BA
file_name: _AI_DAVI Pilot Data Referral Antigen Comparison Analysis.md
file_date: 2026-03-04
title: FloodLAMP DAVI Pilot Data Referral Antigen Comparison Analysis
category: pilots
subcategory: pilot-data
tags: davi, pilot-data, referral-antigen-comparison, ai-analysis
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/18kmV9Ezn2ORHu7Mh1z9MMyLp3EUHZxaV01QAJgJLNU4
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 4317
words: 2590
notes: Created by Opus 4.6 during archive preparation. **PARTIAL HUMAN VERIFICATION - MAY CONTAIN ERRORS** Commentary and analysis of DAVI referral-antigen comparison data, based primarily on `DAVI_pilot-data_referral-antigen-comparison.md` and `DAVI_pilot-data_summary.md`, with an included human verification checklist covering row-level and summary-level claims.
summary_short: DAVI pilot data referral-antigen comparison analysis summarizing same-day agreement between FloodLAMP and BinaxNOW across 51 employee cases, highlighting four FloodLAMP-positive and antigen-negative detections and the strongest sensitivity advantage in asymptomatic cases. Includes a detailed human verification checklist tied to the DAVI comparison and summary files.


CONTENT

## Commentary on DAVI Referral-Antigen Comparison Data (AI Generated - Opus 4.6)
The Davie site produced the archive's most detailed head-to-head comparison between FloodLAMP and BinaxNOW rapid antigen testing, tracking 51 employee cases through three evolving testing protocols during the Delta and Omicron waves. Across cases where both tests were administered on the same day, FloodLAMP and BinaxNOW agreed 90% of the time. In the remaining 10% of cases -- four employees -- FloodLAMP detected the infection while BinaxNOW did not. Three of those four were asymptomatic. There were no cases where antigen detected a positive that FloodLAMP missed. During the intensive dual-testing phase (Group 2, Dec 24 -- Jan 9), when both tests were used for daily follow-up through return to work, the two tests tracked closely, typically clearing on the same day. This pattern suggests that the practical sensitivity difference between FloodLAMP and antigen testing was concentrated at the onset of infection, particularly in asymptomatic or low-viral-load individuals -- precisely the detection gap that molecular screening is designed to address. The Davie data, combined with the anecdotal reports from Coral Springs where 21 of 22 FloodLAMP positives in a single plate were antigen-negative but subsequently confirmed, reinforced a consistent finding across the pilot programs: BinaxNOW rapid antigen tests lagged FloodLAMP molecular detection at infection onset, especially in asymptomatic individuals.

## Analysis of DAVI Referral-Antigen Comparison Data (AI Generated - Opus 4.6)
The file tracks 51 employee COVID cases at the Davie Fire and Rescue site across three protocol phases during the Delta and Omicron waves (Sept 2021 -- Feb 2022), each with a different approach to using FloodLAMP (FL) and BinaxNOW rapid antigen (B) together:

- **Group 1** (15 employees, Sep 15 -- Dec 23): FL as primary test; BinaxNOW used sometimes at home on Day 0. Only 8 of 15 had same-day antigen comparison data.
- **Group 2** (22 employees, Dec 24 -- Jan 9): Both FL and BinaxNOW used throughout until return-to-work clearance. This is the most informative group for head-to-head comparison.
- **Group 3** (14 employees, Jan 10 -- Feb 7): FL for initial detection/diagnosis; BinaxNOW for return-to-work clearance. FL was not used for ongoing follow-up.

### Key findings

1. **Same-day concordance on Day 0**: Of ~42 cases with same-day FL and antigen results, 38 (90.5%) agreed (both positive) and 4 (9.5%) disagreed -- all 4 being FL-positive / antigen-negative. There were zero cases of antigen catching a positive that FloodLAMP missed.

2. **Sensitivity advantage in asymptomatic cases**: Of the 4 FL+/B- discordant cases, 3 (75%) were asymptomatic. By contrast, only 31.6% of the concordant FL+/B+ cases were asymptomatic. This suggests FloodLAMP's molecular sensitivity was most valuable in exactly the population with lower viral loads where antigen tests are known to underperform.

3. **Group 2 tracking data**: When both tests were run side by side over the course of illness, they generally agreed on a day-to-day basis and cleared on the same day. The average time to negative was approximately 9 days (range 5--14). This close tracking indicates that when viral load was high enough for antigen detection, the two tests gave consistent results -- the divergence arose at low viral loads near detection onset.

4. **Zero false positives**: Across the full DAVI program, the stats file reports 0 false positives and 0 suspected false negatives for FloodLAMP, with 97.7% of FL positives confirmed by referral or correspondence.

### Inconsistency - (CAN REMOVE; ERROR HAS BEEN CORRECTED)
The inconsistency is in the original xlsx spreadsheet, not in the md processing. The md file faithfully reproduced what was in the spreadsheet.
Here's what's happening:
The correct numbers come from the "Same Day" summary table (columns AB--AD, rows 2--6), which uses proper COUNTIFS formulas scanning the structured data columns. These correctly compute FL+/B+ = 38 and FL+/B- = 4 (total 42 same-day comparisons).

The incorrect "11 (73.3%)" numbers come from cells K7--K8 and L8 in the legend/header area, which use a broken formula chain:
Cell K7 = 4 (hard-coded) -- the total FL+/B- count. This number is correct.
Cell E11 = SUM(E14:E80) = 15 -- this counts column E, which is a flag marking asymptomatic employees who had same-day antigen testing (15 of the 18 total asymptomatic cases; the 3 without the flag -- emps 4, 11, 12 -- had no antigen test).

Cell K8 = E11 - K7 = 15 - 4 = 11 -- labeled "FL+ and B+" but actually computing "asymptomatic-with-antigen minus total FL+/B-," which is a nonsensical subtraction of two unrelated quantities.
Cell L8 = K8/(K7+K8) = 11/15 = 0.7333 (73.3%)

The most likely explanation is that these cells K7/K8/L8 were written at an early stage -- possibly when only Group 1 (15 employees) existed and column E may have been used differently (e.g., as a general count). When Groups 2 and 3 were added along with the proper structured columns (X--AH) and the correct COUNTIFS summary table (AB--AD rows 2--6), the old K7/K8 formulas were never updated. They now point at a cell (E11) whose meaning shifted, producing a spurious result.

Bottom line: The "Same Day" summary table (FL+/B+ = 38, FL+/B- = 4) is the authoritative data. The "11 (73.3%)" line is a stale, broken formula artifact in the original spreadsheet. The md processing was faithful -- it just reproduced both the correct and incorrect values from the source.

## Human Verification Checklist

Instructions: Verify each claim below against the source data file `DAVI_pilot-data_referral-antigen-comparison.md` and the stats file `DAVI_pilot-data_summary.md`. The claims are quoted from the AI-generated commentary and analysis above. Multiple checkboxes may appear under a single claim; each is a distinct item to verify.


### Commentary Paragraph Checks

> "tracking 51 employee cases" - CONFIRMED

[] Count employee rows in Group 1 "As Reported" table. Expected: 15 (employees 1--15).
[] Count employee rows in Group 2 "As Reported" table. Expected: 22 (employees 16--37).
[] Count employee rows in Group 3 "As Reported" table. Expected: 14 (employees 38--51).
[] Confirm 15 + 22 + 14 = 51.

> "three evolving testing protocols during the Delta and Omicron waves" - CONFIRMED

[] Confirm three distinct groups exist in the source file with three different testing protocols.
[] Group 1 dates (Sep 15 -- Dec 23, 2021) overlap with the Delta wave in the US.
[] Group 2/3 dates (Dec 24 onward) overlap with the Omicron wave in the US.

> "FloodLAMP and BinaxNOW agreed 90% of the time" - CONFIRMED

[] Locate the summary table at the top of the source file under "Summary: Same Day Test Comparison."
[] Confirm FL+, B+ total = 38.
[] Confirm FL+, B- total = 4.
[] Compute: 38 / (38 + 4) = 38 / 42 = 0.9048 ≈ 90.5%. Confirm "90%" is a fair rounding.

> "four employees -- FloodLAMP detected the infection while BinaxNOW did not" - CONFIRMED

[] Identify the 4 FL+/B- employees by scanning Day 0 results in all three "As Reported" tables. They should be:
[] Employee 14 (Group 1): Day 0 = "FL +, B -, ASY"
[] Employee 18 (Group 2): Day 0 = "FL +, B -, ASY"
[] Employee 41 (Group 3): Day 0 = "FL +, B -, SYM"
[] Employee 45 (Group 3): Day 0 = "FL +, B -, ASY"
[] Confirm no other employees in any group have FL+, B- on Day 0.

> "Three of those four were asymptomatic" - CONFIRMED

[] Of the 4 FL+/B- employees identified above, confirm 3 have ASY in Day 0 (emps 14, 18, 45) and 1 has SYM (emp 41).
[] Cross-check against the summary table: FL+, B- row shows Asymptomatic = 3, Symptomatic = 1.

> "There were no cases where antigen detected a positive that FloodLAMP missed" - CONFIRMED

[] Scan all Day 0 results in all three "As Reported" tables for any case of "FL -, B +" or "B +, FL -" or "B +" without FL+. Expected: none.
[] Note employee 21 (Group 2) Day 0 is "B + SYM" without FL. In the Structured table, Day 0 FL is blank and "Same Day Antigen" = False. Confirm this case is excluded from the same-day comparison (not counted in the 42) and therefore does not represent a FL miss.
[] Note employee 43 (Group 3) Day 0 is "SYM" without any test result. Confirm this is also excluded ("Same Day Antigen" = False).

> "Group 2, Dec 24 -- Jan 9" - CONFIRMED

[] Confirm Group 2 header in source file says "Testing between Dec 24th and Jan 9th."
[] Confirm Group 2 Structured table dates show 2021-12-24 and 2022-01-09.

> "the two tests tracked closely, typically clearing on the same day" - CONFIRMED

[] In Group 2 Structured table, for every row where both "Day # FloodLAMP Neg" and "Day # Antigen Neg" have values, compare the two numbers. Expected: all 18 such pairs are identical (same day).
[] Specifically verify these pairs (employee: FL neg day, B neg day):
[] Emp 16: 6, 6
[] Emp 21: 12, 12
[] Emp 22: 6, 6
[] Emp 23: 8, 8
[] Emp 24: 8, 8
[] Emp 25: 9, 9
[] Emp 26: 8, 8
[] Emp 27: 10, 10
[] Emp 28: 9, 9
[] Emp 29: 14, 14
[] Emp 30: 12, 12
[] Emp 31: 10, 10
[] Emp 32: 11, 11
[] Emp 33: 8, 8
[] Emp 34: 10, 10
[] Emp 35: 5, 5
[] Emp 36: 8, 8
[] Emp 37: 10, 10
[] Confirm 4 rows (emps 17, 18, 19, 20) have blank FL neg day and only antigen neg day. These are excluded from the "same day clearing" comparison.

> "21 of 22 FloodLAMP positives in a single plate were antigen-negative but subsequently confirmed" (Coral Springs reference) - CONFIRMED

[] This claim is NOT from the DAVI data. It references Coral Springs (COSP) program.
[] Verify against `_context-commentary_pilots-pilot-data_INITIAL.md`, COSP commentary section. The text there says: "the highest number of positives they had in a single plate, which was 22...only one of the 22 were antigen positive (BinaXNow)."
[] Confirm 22 - 1 = 21 antigen-negative is the correct derivation.


### Analysis Section Checks

> Group 1: "15 employees, Sep 15 -- Dec 23" - CONFIRMED

[] Count rows in Group 1 "As Reported" table: expected 15 (employees 1--15).
[] Count rows in Group 1 "Structured" table: expected 15.
[] Confirm source header says "Testing between Sept 15th and Dec 23rd."

> "Only 8 of 15 had same-day antigen comparison data" - CONFIRMED

[] In Group 1 Structured table, count rows where "FloodLAMP Test with Same Day Antigen" = True. Expected: 8.
[] Identify the 8 True rows: employees 1, 2, 3, 7, 8, 9, 10, 14 (match to Structured table row order).
[] Count remaining False rows: expected 7 (employees 4, 5, 6, 11, 12, 13, 15).

> Group 2: "22 employees, Dec 24 -- Jan 9" - CONFIRMED

[] Count rows in Group 2 "As Reported" table: expected 22 (employees 16--37).
[] Count rows in Group 2 "Structured" table: expected 22.
[] Confirm source header says "Testing between Dec 24th and Jan 9th."

> Group 3: "14 employees, Jan 10 -- Feb 7" - CONFIRMED

[] Count rows in Group 3 "As Reported" table: expected 14 (employees 38--51).
[] Count rows in Group 3 "Structured" table: expected 14.
[] Confirm source header says "Testing between Jan 10th and Feb 7th."

> "Of ~42 cases with same-day FL and antigen results, 38 (90.5%) agreed and 4 (9.5%) disagreed" - CONFIRMED

[] Count all "True" entries in "FloodLAMP Test with Same Day Antigen" column across all three Structured tables. Expected: 8 + 21 + 13 = 42.
[] Group 2: Count True entries. Expected: 21 (emp 21 is the one False, with blank FL result Day 0).
[] Group 3: Count True entries. Expected: 13 (emp 43 is the one False, with no Day 0 test results).
[] Confirm 38 / 42 = 0.9048 = 90.5%.
[] Confirm 4 / 42 = 0.0952 = 9.5%.
[] Cross-check these totals against the summary table at top of source file: FL+, B- = 4, FL+, B+ = 38, total = 42.

> "Of the 4 FL+/B- discordant cases, 3 (75%) were asymptomatic" - CONFIRMED

[] Confirm 3/4 = 0.75 = 75%.
[] Cross-check against summary table: "% Asymp" row under FL+, B- column = 0.75.

> "only 31.6% of the concordant FL+/B+ cases were asymptomatic" - CONFIRMED

[] From the summary table, FL+, B+ column: Asymptomatic = 12, Total = 38.
[] Compute 12 / 38 = 0.3158 = 31.6%. Confirm.
[] Cross-check against summary table: "% Asymp" row under FL+, B+ column = 31.6%.

> "The average time to negative was approximately 9 days (range 5--14)" - CONFIRMED

[] Using Group 2 Structured table only, list all "Day # FloodLAMP Neg" values that are not blank: 6, 12, 6, 8, 8, 9, 8, 10, 9, 14, 12, 10, 11, 8, 10, 5, 8, 10. Expected count: 18.
[] Compute sum: 6+12+6+8+8+9+8+10+9+14+12+10+11+8+10+5+8+10 = 164.
[] Compute average: 164 / 18 = 9.11. Confirm "approximately 9" is fair.
[] Confirm minimum value = 5 and maximum value = 14 (range 5--14).
[] Alternatively, using "Day # Antigen Neg" for all 22 Group 2 rows: sum = 6+12+14+9+9+12+6+8+8+9+8+10+9+14+12+10+11+8+10+5+8+10 = 208. Average = 208/22 = 9.45. Also approximately 9. Range also 5--14.

> "the stats file reports 0 false positives and 0 suspected false negatives" - CONFIRMED

[] In `DAVI_pilot-data_summary.md`, locate "False Positives Final Results" row. Expected value: 0.
[] In `DAVI_pilot-data_summary.md`, locate "False Negative Final Results (Suspected)" row. Expected value: 0.

> "97.7% of FL positives confirmed by referral or correspondence" - CONFIRMED

[] In `DAVI_pilot-data_summary.md`, locate "% FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive" row. Expected value: 97.7%.
[] Note the comments column for that row explains the one unconfirmed case: antigen negative same day, no follow-up antigen, but FL positive 4 more times and person became symptomatic.


### Internal Consistency Check (Summary Table vs. Raw Data)

These checks verify that the summary table at the top of the source file is itself consistent with the row-level data.

> Summary table: FL+, B+ Asymptomatic = 12 - CONFIRMED

[] Count all employees across all three groups where Day 0 shows both FL+ and B+ AND ASY. List them and confirm total = 12.
[] Expected: Emps 1, 16, 17, 23, 31, 36, 38, 39, 40, 44, 46, 47 (verify each).

> Summary table: FL+, B+ Symptomatic = 26 - CONFIRMED

[] Count all employees across all three groups where Day 0 shows both FL+ and B+ AND SYM. Confirm total = 26.

> Summary table: FL+, B- Asymptomatic = 3 - CONFIRMED

[] Confirm: Emps 14 (ASY), 18 (ASY), 45 (ASY). Total = 3.

> Summary table: FL+, B- Symptomatic = 1 - CONFIRMED

[] Confirm: Emp 41 (SYM). Total = 1.

> Source file line: "+ on FloodLAMP and + on BinaxNOW: 11 (73.3%)" - CONFIRMED ERROR AND CORRECTED

[] This line appears to be inconsistent with the summary table (which says 38). Determine if "11" refers to a subset (possibly Group 1 only, or a different counting method). Flag for author review.
[] Note: If this is Group 1 only, count FL+, B+ in Group 1 "As Reported": Emps 1, 2, 3, 7, 8, 9, 10 = 7, not 11. The number 11 does not obviously correspond to any subset. The "73.3%" also does not match 7/15 (46.7%) or 38/51 (74.5%). This likely needs author clarification.


### End of Checklist


# 7,073  FLMP_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: FLMP_pilot-data_summary.md
file_date: 2023-01-02
title: FLMP Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 3788
tokens: 7073
notes: 
summary_short: The "FLMP_pilot-data_summary" document was the organization's home-base testing in San Carlos and Portola Valley, CA, where FloodLAMP staff tested themselves and their working colleagues along with their household members. The testing used pooled household and individual self-collection across various sites and configurations. The program ran for over 2 years (2020-12-11 to 2023-01-02), testing 1,540 tubes with 3,399 participant results and 57 positive tubes detected. The files for FLMP include all data for the 2 programs Carillon, a local preschool where FloodLAMP founders kids attended (CRLN), and all other FloodLAMP internal and local testing, termed "FloodLAMP Staff Plus" (FLSP). These 2 programs were intermingled and utilized the same FloodLAMP app tenant.


CONTENT

## Plots

### Composite

![FLMP Weekly Composite](_plots/FLMP_weekly_composite.png)

### Percent Positive Tubes

![FLMP Weekly Percent Positives](_plots/FLMP_weekly_percent_positives.png)

### Volume

![FLMP Weekly Volume](_plots/FLMP_weekly_volume.png)

## Files

### Google Sheets URLs
- [FLMP_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1ni39vn-fdXq0HrOgHbim_FK0OZidUv-YBLvzPwhhlFQ)
- [FLMP_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/16CwPJ9LeknD8lJFTr-gJSx916WZaGEMbN6iKnlVx4dI)
- [FLMP_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/16R3LlannlrGfiIIJq4T3EWjbtFLZrtPC4gkKycu8RXc)

### Curated CSVs
- Curated CSV folder: `FLMP_curated_csvs/`
- Stats key-values CSV: [FLMP_APS_stats_key-values.csv](FLMP_curated_csvs/FLMP_APS_stats_key-values.csv)
- Weekly summary CSV: [FLMP_APS_weekly-summary.csv](FLMP_curated_csvs/FLMP_APS_weekly-summary.csv)
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [FLMP_APS_deID_PUB.xlsx](FLMP_xlsx_downloads/FLMP_APS_deID_PUB.xlsx)
- [FLMP_RFR_deID_PUB.xlsx](FLMP_xlsx_downloads/FLMP_RFR_deID_PUB.xlsx)
- [FLMP_RTR_deID_PUB.xlsx](FLMP_xlsx_downloads/FLMP_RTR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | FLMP_RFR_deID_PUB |  |  | Stats | 1 |
| Files | RTR File | FLMP_RTR_deID_PUB |  |  | Stats | 2 |
| Files | RSR File | NONE |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 1,540 | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 1,618 | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 243 |  | divide CRLN by time period 1-2 to 5-31 | Stats | 7 |
| Overall | Number of APS Only Tubes run | 436 |  | divide CRLN by time period 1-2 to 5-31 | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 1,915 | includes technical replicates (the same tube sample in multiple reactions in the same run) | divide CRLN by time period 1-2 to 5-31 - 135 is num FLSP tubes in CRLN time period and 1290 is num RFR audit rxns during CRLN time period | Stats | 9 |
| Overall | Number of Participant Results | 3,399 | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 48 | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF | all during CRLN period so assign to CRLN | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 3,447 | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 2.3 |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 78 | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 230 | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 5.1% | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 37 |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 15.2% |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 57 |  | count from VALUES Pos and Incl | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 3.7% |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 19 | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 3 | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 16 |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 4 |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 4 |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.3% |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 1 |  | 2022-05-08T00:00:00 | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests | 25.0% |  | 2/4 unknown and 1 of those was in household of positives | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 1 |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 2 |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 36 | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App | No 2.5 correction code, Sum AE - AF = 36 | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 43 | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 2.7% | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 15 | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 14 | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 1 |  | 2022-05-08T00:00:00 | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 1 |  | 2022-02-14T00:00:00 | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 2 |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 11 |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 11 |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 5 | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 45.5% |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 1 |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 9.1% |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 212 | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 60 | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 26 | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 12.3% |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 52 |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 24.5% |  |  | Stats | 71 |
| Dates | Start Run Date | 2020-12-11 |  |  | Stats | 74 |
| Dates | End Run Date | 2023-01-02 |  |  | Stats | 75 |
| Info | Test Operator | FloodLAMP | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Various | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Staff, Students, Families, Community | Description of the participants |  | Stats | 80 |
| Info | Configuration | Various | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled Household, Individual | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | FloodLAMP | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Various | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Various | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Portola Valley, CA | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |
| Pooling | Number of Initial FloodLAMP Positive Pools | 13 |  |  | Stats | 92 |
| Pooling | Number of Initial FloodLAMP Positive Pools with Indiv Deconvolution | 8 |  |  | Stats | 93 |
| Pooling | Number of Initial FloodLAMP Positive Pools Confirmed by Referral Testing | 9 |  |  | Stats | 94 |
| Pooling | Number of Initial Confirmed FL Pools where the organization member (i.e. parent or other child) was Positive | 5 |  |  | Stats | 95 |
| Pooling | Number of Initial Confirmed FL Pools where Positive Individual was not the organization member (i.e. parent or other child) | 4 |  |  | Stats | 96 |
| Pooling | % Confirmed Positive Pools where Positive Individual was not the organization member (i.e. parent or other child) | 44.4% |  |  | Stats | 97 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2020-12-07 | 2020-12-13 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2020-12-14 | 2020-12-20 | 3 | 1 | 0 | 0 | 0.0% | ok |
| 2020-12-21 | 2020-12-27 | 2 | 1 | 0 | 0 | 0.0% | ok |
| 2020-12-28 | 2021-01-03 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2021-01-04 | 2021-01-10 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-01-11 | 2021-01-17 | 36 | 15 | 3 | 0 | 20.0% | ok |
| 2021-01-18 | 2021-01-24 | 49 | 24 | 0 | 0 | 0.0% | ok |
| 2021-01-25 | 2021-01-31 | 45 | 19 | 0 | 0 | 0.0% | ok |
| 2021-02-01 | 2021-02-07 | 31 | 11 | 0 | 0 | 0.0% | ok |
| 2021-02-08 | 2021-02-14 | 40 | 13 | 0 | 0 | 0.0% | ok |
| 2021-02-15 | 2021-02-21 | 14 | 4 | 0 | 0 | 0.0% | ok |
| 2021-02-22 | 2021-02-28 | 24 | 9 | 0 | 0 | 0.0% | ok |
| 2021-03-01 | 2021-03-07 | 35 | 11 | 0 | 0 | 0.0% | ok |
| 2021-03-08 | 2021-03-14 | 30 | 9 | 0 | 0 | 0.0% | ok |
| 2021-03-15 | 2021-03-21 | 16 | 6 | 0 | 0 | 0.0% | ok |
| 2021-03-22 | 2021-03-28 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2021-03-29 | 2021-04-04 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2021-04-05 | 2021-04-11 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-04-12 | 2021-04-18 | 8 | 3 | 0 | 0 | 0.0% | ok |
| 2021-04-19 | 2021-04-25 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-04-26 | 2021-05-02 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-05-03 | 2021-05-09 | 1 | 1 | 0 | 0 | 0.0% | ok |
| 2021-05-10 | 2021-05-16 | 5 | 2 | 0 | 0 | 0.0% | ok |
| 2021-05-17 | 2021-05-23 | 6 | 6 | 0 | 0 | 0.0% | ok |
| 2021-05-24 | 2021-05-30 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-05-31 | 2021-06-06 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-06-07 | 2021-06-13 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-06-14 | 2021-06-20 | 2 | 2 | 0 | 0 | 0.0% | ok |
| 2021-06-21 | 2021-06-27 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-06-28 | 2021-07-04 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-05 | 2021-07-11 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-12 | 2021-07-18 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-19 | 2021-07-25 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-26 | 2021-08-01 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-02 | 2021-08-08 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-09 | 2021-08-15 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-16 | 2021-08-22 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-23 | 2021-08-29 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-30 | 2021-09-05 | 7 | 4 | 0 | 0 | 0.0% | ok |
| 2021-09-06 | 2021-09-12 | 4 | 2 | 0 | 0 | 0.0% | ok |
| 2021-09-13 | 2021-09-19 | 9 | 6 | 0 | 0 | 0.0% | ok |
| 2021-09-20 | 2021-09-26 | 7 | 4 | 0 | 0 | 0.0% | ok |
| 2021-09-27 | 2021-10-03 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-10-04 | 2021-10-10 | 10 | 7 | 0 | 0 | 0.0% | ok |
| 2021-10-11 | 2021-10-17 | 11 | 5 | 0 | 0 | 0.0% | ok |
| 2021-10-18 | 2021-10-24 | 15 | 8 | 0 | 0 | 0.0% | ok |
| 2021-10-25 | 2021-10-31 | 2 | 2 | 0 | 0 | 0.0% | ok |
| 2021-11-01 | 2021-11-07 | 19 | 9 | 0 | 0 | 0.0% | ok |
| 2021-11-08 | 2021-11-14 | 15 | 6 | 0 | 0 | 0.0% | ok |
| 2021-11-15 | 2021-11-21 | 15 | 6 | 0 | 0 | 0.0% | ok |
| 2021-11-22 | 2021-11-28 | 43 | 12 | 0 | 0 | 0.0% | ok |
| 2021-11-29 | 2021-12-05 | 18 | 8 | 0 | 0 | 0.0% | ok |
| 2021-12-06 | 2021-12-12 | 39 | 19 | 0 | 0 | 0.0% | ok |
| 2021-12-13 | 2021-12-19 | 43 | 22 | 2 | 0 | 9.1% | ok |
| 2021-12-20 | 2021-12-26 | 38 | 30 | 6 | 0 | 20.0% | ok |
| 2021-12-27 | 2022-01-02 | 78 | 43 | 6 | 0 | 14.0% | ok |
| 2022-01-03 | 2022-01-09 | 94 | 43 | 7 | 0 | 16.3% | ok |
| 2022-01-10 | 2022-01-16 | 183 | 93 | 15 | 1 | 16.1% | ok |
| 2022-01-17 | 2022-01-23 | 177 | 86 | 9 | 0 | 10.5% | ok |
| 2022-01-24 | 2022-01-30 | 154 | 65 | 0 | 0 | 0.0% | ok |
| 2022-01-31 | 2022-02-06 | 144 | 59 | 0 | 0 | 0.0% | ok |
| 2022-02-07 | 2022-02-13 | 148 | 60 | 0 | 0 | 0.0% | ok |
| 2022-02-14 | 2022-02-20 | 128 | 54 | 0 | 1 | 0.0% | ok |
| 2022-02-21 | 2022-02-27 | 55 | 21 | 0 | 0 | 0.0% | ok |
| 2022-02-28 | 2022-03-06 | 51 | 25 | 0 | 0 | 0.0% | ok |
| 2022-03-07 | 2022-03-13 | 113 | 52 | 0 | 0 | 0.0% | ok |
| 2022-03-14 | 2022-03-20 | 91 | 42 | 0 | 0 | 0.0% | ok |
| 2022-03-21 | 2022-03-27 | 113 | 47 | 0 | 0 | 0.0% | ok |
| 2022-03-28 | 2022-04-03 | 25 | 12 | 0 | 0 | 0.0% | ok |
| 2022-04-04 | 2022-04-10 | 119 | 47 | 0 | 0 | 0.0% | ok |
| 2022-04-11 | 2022-04-17 | 104 | 43 | 0 | 0 | 0.0% | ok |
| 2022-04-18 | 2022-04-24 | 116 | 53 | 0 | 0 | 0.0% | ok |
| 2022-04-25 | 2022-05-01 | 113 | 48 | 0 | 0 | 0.0% | ok |
| 2022-05-02 | 2022-05-08 | 114 | 53 | 2 | 0 | 3.8% | ok |
| 2022-05-09 | 2022-05-15 | 117 | 67 | 4 | 2 | 6.0% | ok |
| 2022-05-16 | 2022-05-22 | 102 | 51 | 1 | 0 | 2.0% | ok |
| 2022-05-23 | 2022-05-29 | 93 | 44 | 1 | 0 | 2.3% | ok |
| 2022-05-30 | 2022-06-05 | 49 | 22 | 0 | 0 | 0.0% | ok |
| 2022-06-06 | 2022-06-12 | 13 | 7 | 0 | 0 | 0.0% | ok |
| 2022-06-13 | 2022-06-19 | 7 | 5 | 0 | 0 | 0.0% | ok |
| 2022-06-20 | 2022-06-26 | 9 | 3 | 0 | 0 | 0.0% | ok |
| 2022-06-27 | 2022-07-03 | 4 | 3 | 0 | 0 | 0.0% | ok |
| 2022-07-04 | 2022-07-10 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-07-11 | 2022-07-17 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-07-18 | 2022-07-24 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2022-07-25 | 2022-07-31 | 8 | 4 | 0 | 0 | 0.0% | ok |
| 2022-08-01 | 2022-08-07 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2022-08-08 | 2022-08-14 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-15 | 2022-08-21 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-22 | 2022-08-28 | 4 | 1 | 0 | 0 | 0.0% | ok |
| 2022-08-29 | 2022-09-04 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-09-05 | 2022-09-11 | 8 | 3 | 0 | 0 | 0.0% | ok |
| 2022-09-12 | 2022-09-18 | 11 | 4 | 0 | 0 | 0.0% | ok |
| 2022-09-19 | 2022-09-25 | 10 | 4 | 0 | 0 | 0.0% | ok |
| 2022-09-26 | 2022-10-02 | 12 | 4 | 0 | 0 | 0.0% | ok |
| 2022-10-03 | 2022-10-09 | 13 | 5 | 0 | 0 | 0.0% | ok |
| 2022-10-10 | 2022-10-16 | 14 | 5 | 0 | 0 | 0.0% | ok |
| 2022-10-17 | 2022-10-23 | 12 | 4 | 0 | 0 | 0.0% | ok |
| 2022-10-24 | 2022-10-30 | 12 | 8 | 0 | 0 | 0.0% | ok |
| 2022-10-31 | 2022-11-06 | 11 | 5 | 0 | 0 | 0.0% | ok |
| 2022-11-07 | 2022-11-13 | 12 | 5 | 0 | 0 | 0.0% | ok |
| 2022-11-14 | 2022-11-20 | 8 | 5 | 0 | 0 | 0.0% | ok |
| 2022-11-21 | 2022-11-27 | 5 | 3 | 0 | 0 | 0.0% | ok |
| 2022-11-28 | 2022-12-04 | 13 | 5 | 0 | 0 | 0.0% | ok |
| 2022-12-05 | 2022-12-11 | 8 | 3 | 0 | 0 | 0.0% | ok |
| 2022-12-12 | 2022-12-18 | 23 | 11 | 1 | 0 | 9.1% | ok |
| 2022-12-19 | 2022-12-25 | 10 | 6 | 0 | 0 | 0.0% | ok |
| 2022-12-26 | 2023-01-01 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2023-01-02 | 2023-01-08 | 7 | 3 | 0 | 0 | 0.0% | ok |


# 7,893  FLSP_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: FLSP_pilot-data_summary.md
file_date: 2023-01-02
title: FLSP Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 4284
tokens: 7893
notes: 
summary_short: The "FLSP_pilot-data_summary" covers the FloodLAMP pilot program for FloodLAMP staff who tested themselves and their working colleagues along with their household members. The testing used pooled household and individual self-collection across various sites and configurations. The program ran for over 2 years (2020-12-11 to 2023-01-02), testing 524 tubes with 1,061 participant results and 25 positive tubes detected.


CONTENT

## Plots

### Composite

![FLSP Weekly Composite](_plots/FLSP_weekly_composite.png)

### Percent Positive Tubes

![FLSP Weekly Percent Positives](_plots/FLSP_weekly_percent_positives.png)

### Volume

![FLSP Weekly Volume](_plots/FLSP_weekly_volume.png)

## Files

### Google Sheets URLs
- [FLMP_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1ni39vn-fdXq0HrOgHbim_FK0OZidUv-YBLvzPwhhlFQ)
- [FLMP_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/16CwPJ9LeknD8lJFTr-gJSx916WZaGEMbN6iKnlVx4dI)
- [FLMP_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/16R3LlannlrGfiIIJq4T3EWjbtFLZrtPC4gkKycu8RXc)

### Curated CSVs
- Curated CSV folder: `FLSP_curated_csvs/`
- Stats key-values CSV: [FLSP_APS_stats_key-values.csv](FLSP_curated_csvs/FLSP_APS_stats_key-values.csv)
- Weekly summary CSV: [FLSP_RFR_weekly-summary.csv](FLSP_curated_csvs/FLSP_RFR_weekly-summary.csv)
- Referral tests by person CSV: [FLSP_RTR_referral-tests-by-person.csv](FLSP_curated_csvs/FLSP_RTR_referral-tests-by-person.csv)

### XLSX downloads:
- [FLMP_APS_deID_PUB.xlsx](../FLMP_pilot-data/FLMP_xlsx_downloads/FLMP_APS_deID_PUB.xlsx)
- [FLMP_RFR_deID_PUB.xlsx](../FLMP_pilot-data/FLMP_xlsx_downloads/FLMP_RFR_deID_PUB.xlsx)
- [FLMP_RTR_deID_PUB.xlsx](../FLMP_pilot-data/FLMP_xlsx_downloads/FLMP_RTR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | FLMP_RFR_deID_PUB |  |  | Stats | 1 |
| Files | RTR File | FLMP_RTR_deID_PUB |  |  | Stats | 2 |
| Files | RSR File | NONE |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 524 | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 532 | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 164 |  | divide CRLN by time period 1-2 to 5-31 | Stats | 7 |
| Overall | Number of APS Only Tubes run | 325 |  | divide CRLN by time period 1-2 to 5-31 | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 785 | includes technical replicates (the same tube sample in multiple reactions in the same run) | divide CRLN by time period 1-2 to 5-31 - 135 is num FLSP tubes in CRLN time period and 1290 is num RFR audit rxns during CRLN time period | Stats | 9 |
| Overall | Number of Participant Results | 1,059 | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 0 | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF | all during CRLN period so assign to CRLN | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 1,059 | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 2.0 |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 8 | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 25 | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 1.5% | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 6 |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 3.7% |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 25 |  | count from VALUES Pos and Incl | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 4.8% |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 6 | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 0 | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 6 |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 0 |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 0 |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.0% |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 |  | 2022-05-08T00:00:00 | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests |  |  | 2/4 unknown and 1 of those was in household of positives | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 0 |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 3 | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App | No 2.5 correction code, Sum AE - AF = 36 | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 3 | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 0.6% | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 5 | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 5 | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 |  | 2022-05-08T00:00:00 | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 |  | 2022-02-14T00:00:00 | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 0 |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 3 |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 3 |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 1 | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 33.3% |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 1 |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 33.3% |  |  | Stats | 57 |
| False Calls | False Positives Final Results |  | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) |  | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 70 | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 9 | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 9 | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 12.9% |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 12 |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 17.1% |  |  | Stats | 71 |
| Dates | Start Run Date | 2020-12-11 |  |  | Stats | 74 |
| Dates | End Run Date | 2023-01-02 |  |  | Stats | 75 |
| Info | Test Operator | FloodLAMP | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Biolab, Garage, Office | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Staff, Community | Description of the participants |  | Stats | 80 |
| Info | Configuration | Various | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled Household, Individual | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | FloodLAMP Staff Plus | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | MBC Biolabs and Home Garage | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Company | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | San Carlos, CA | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |
| Pooling | Number of Initial FloodLAMP Positive Pools | 3 |  |  | Stats | 92 |
| Pooling | Number of Initial FloodLAMP Positive Pools with Indiv Deconvolution | 3 |  |  | Stats | 93 |
| Pooling | Number of Initial FloodLAMP Positive Pools Confirmed by Referral Testing | 3 |  |  | Stats | 94 |
| Pooling | Number of Initial Confirmed FL Pools where the organization member (i.e. parent or other child) was Positive | 1 |  |  | Stats | 95 |
| Pooling | Number of Initial Confirmed FL Pools where Positive Individual was not the organization member (i.e. parent or other child) | 2 |  |  | Stats | 96 |
| Pooling | % Confirmed Positive Pools where Positive Individual was not the organization member (i.e. parent or other child) | 66.7% |  |  | Stats | 97 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2020-12-07 | 2020-12-13 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2020-12-14 | 2020-12-20 | 3 | 1 | 0 | 0 | 0.0% | ok |
| 2020-12-21 | 2020-12-27 | 2 | 1 | 0 | 0 | 0.0% | ok |
| 2020-12-28 | 2021-01-03 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2021-01-04 | 2021-01-10 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-01-11 | 2021-01-17 | 36 | 15 | 3 | 0 | 20.0% | ok |
| 2021-01-18 | 2021-01-24 | 49 | 24 | 0 | 0 | 0.0% | ok |
| 2021-01-25 | 2021-01-31 | 45 | 19 | 0 | 0 | 0.0% | ok |
| 2021-02-01 | 2021-02-07 | 31 | 11 | 0 | 0 | 0.0% | ok |
| 2021-02-08 | 2021-02-14 | 40 | 13 | 0 | 0 | 0.0% | ok |
| 2021-02-15 | 2021-02-21 | 14 | 4 | 0 | 0 | 0.0% | ok |
| 2021-02-22 | 2021-02-28 | 24 | 9 | 0 | 0 | 0.0% | ok |
| 2021-03-01 | 2021-03-07 | 35 | 11 | 0 | 0 | 0.0% | ok |
| 2021-03-08 | 2021-03-14 | 30 | 9 | 0 | 0 | 0.0% | ok |
| 2021-03-15 | 2021-03-21 | 16 | 6 | 0 | 0 | 0.0% | ok |
| 2021-03-22 | 2021-03-28 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2021-03-29 | 2021-04-04 | 6 | 2 | 0 | 0 | 0.0% | ok |
| 2021-04-05 | 2021-04-11 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-04-12 | 2021-04-18 | 8 | 3 | 0 | 0 | 0.0% | ok |
| 2021-04-19 | 2021-04-25 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-04-26 | 2021-05-02 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-05-03 | 2021-05-09 | 1 | 1 | 0 | 0 | 0.0% | ok |
| 2021-05-10 | 2021-05-16 | 5 | 2 | 0 | 0 | 0.0% | ok |
| 2021-05-17 | 2021-05-23 | 6 | 6 | 0 | 0 | 0.0% | ok |
| 2021-05-24 | 2021-05-30 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-05-31 | 2021-06-06 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-06-07 | 2021-06-13 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-06-14 | 2021-06-20 | 2 | 2 | 0 | 0 | 0.0% | ok |
| 2021-06-21 | 2021-06-27 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-06-28 | 2021-07-04 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-05 | 2021-07-11 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-12 | 2021-07-18 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-19 | 2021-07-25 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-07-26 | 2021-08-01 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-02 | 2021-08-08 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-09 | 2021-08-15 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-16 | 2021-08-22 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-23 | 2021-08-29 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-08-30 | 2021-09-05 | 7 | 4 | 0 | 0 | 0.0% | ok |
| 2021-09-06 | 2021-09-12 | 4 | 2 | 0 | 0 | 0.0% | ok |
| 2021-09-13 | 2021-09-19 | 9 | 6 | 0 | 0 | 0.0% | ok |
| 2021-09-20 | 2021-09-26 | 7 | 4 | 0 | 0 | 0.0% | ok |
| 2021-09-27 | 2021-10-03 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2021-10-04 | 2021-10-10 | 10 | 7 | 0 | 0 | 0.0% | ok |
| 2021-10-11 | 2021-10-17 | 11 | 5 | 0 | 0 | 0.0% | ok |
| 2021-10-18 | 2021-10-24 | 15 | 8 | 0 | 0 | 0.0% | ok |
| 2021-10-25 | 2021-10-31 | 2 | 2 | 0 | 0 | 0.0% | ok |
| 2021-11-01 | 2021-11-07 | 19 | 9 | 0 | 0 | 0.0% | ok |
| 2021-11-08 | 2021-11-14 | 15 | 6 | 0 | 0 | 0.0% | ok |
| 2021-11-15 | 2021-11-21 | 15 | 6 | 0 | 0 | 0.0% | ok |
| 2021-11-22 | 2021-11-28 | 43 | 12 | 0 | 0 | 0.0% | ok |
| 2021-11-29 | 2021-12-05 | 18 | 8 | 0 | 0 | 0.0% | ok |
| 2021-12-06 | 2021-12-12 | 39 | 19 | 0 | 0 | 0.0% | ok |
| 2021-12-13 | 2021-12-19 | 43 | 22 | 2 | 0 | 9.1% | ok |
| 2021-12-20 | 2021-12-26 | 34 | 29 | 6 | 0 | 20.7% | ok |
| 2021-12-27 | 2022-01-02 | 44 | 31 | 4 | 0 | 12.9% | ok |
| 2022-01-03 | 2022-01-09 | 9 | 6 | 1 | 0 | 16.7% | ok |
| 2022-01-10 | 2022-01-16 | 10 | 10 | 4 | 0 | 40.0% | ok |
| 2022-01-17 | 2022-01-23 | 15 | 15 | 4 | 0 | 26.7% | ok |
| 2022-01-24 | 2022-01-30 | 4 | 3 | 0 | 0 | 0.0% | ok |
| 2022-01-31 | 2022-02-06 | 1 | 1 | 0 | 0 | 0.0% | ok |
| 2022-02-07 | 2022-02-13 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-02-14 | 2022-02-20 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-02-21 | 2022-02-27 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-02-28 | 2022-03-06 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-03-07 | 2022-03-13 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-03-14 | 2022-03-20 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-03-21 | 2022-03-27 | 3 | 3 | 0 | 0 | 0.0% | ok |
| 2022-03-28 | 2022-04-03 | 3 | 3 | 0 | 0 | 0.0% | ok |
| 2022-04-04 | 2022-04-10 | 9 | 4 | 0 | 0 | 0.0% | ok |
| 2022-04-11 | 2022-04-17 | 4 | 3 | 0 | 0 | 0.0% | ok |
| 2022-04-18 | 2022-04-24 | 6 | 6 | 0 | 0 | 0.0% | ok |
| 2022-04-25 | 2022-05-01 | 6 | 6 | 0 | 0 | 0.0% | ok |
| 2022-05-02 | 2022-05-08 | 6 | 6 | 0 | 0 | 0.0% | ok |
| 2022-05-09 | 2022-05-15 | 6 | 5 | 0 | 0 | 0.0% | ok |
| 2022-05-16 | 2022-05-22 | 10 | 7 | 0 | 0 | 0.0% | ok |
| 2022-05-23 | 2022-05-29 | 4 | 3 | 0 | 0 | 0.0% | ok |
| 2022-05-30 | 2022-06-05 | 7 | 3 | 0 | 0 | 0.0% | ok |
| 2022-06-06 | 2022-06-12 | 13 | 7 | 0 | 0 | 0.0% | ok |
| 2022-06-13 | 2022-06-19 | 7 | 5 | 0 | 0 | 0.0% | ok |
| 2022-06-20 | 2022-06-26 | 9 | 3 | 0 | 0 | 0.0% | ok |
| 2022-06-27 | 2022-07-03 | 4 | 3 | 0 | 0 | 0.0% | ok |
| 2022-07-04 | 2022-07-10 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-07-11 | 2022-07-17 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-07-18 | 2022-07-24 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2022-07-25 | 2022-07-31 | 8 | 4 | 0 | 0 | 0.0% | ok |
| 2022-08-01 | 2022-08-07 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2022-08-08 | 2022-08-14 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-15 | 2022-08-21 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-22 | 2022-08-28 | 4 | 1 | 0 | 0 | 0.0% | ok |
| 2022-08-29 | 2022-09-04 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-09-05 | 2022-09-11 | 8 | 3 | 0 | 0 | 0.0% | ok |
| 2022-09-12 | 2022-09-18 | 11 | 4 | 0 | 0 | 0.0% | ok |
| 2022-09-19 | 2022-09-25 | 10 | 4 | 0 | 0 | 0.0% | ok |
| 2022-09-26 | 2022-10-02 | 12 | 4 | 0 | 0 | 0.0% | ok |
| 2022-10-03 | 2022-10-09 | 13 | 5 | 0 | 0 | 0.0% | ok |
| 2022-10-10 | 2022-10-16 | 14 | 5 | 0 | 0 | 0.0% | ok |
| 2022-10-17 | 2022-10-23 | 12 | 4 | 0 | 0 | 0.0% | ok |
| 2022-10-24 | 2022-10-30 | 12 | 8 | 0 | 0 | 0.0% | ok |
| 2022-10-31 | 2022-11-06 | 11 | 5 | 0 | 0 | 0.0% | ok |
| 2022-11-07 | 2022-11-13 | 12 | 5 | 0 | 0 | 0.0% | ok |
| 2022-11-14 | 2022-11-20 | 8 | 5 | 0 | 0 | 0.0% | ok |
| 2022-11-21 | 2022-11-27 | 5 | 3 | 0 | 0 | 0.0% | ok |
| 2022-11-28 | 2022-12-04 | 13 | 5 | 0 | 0 | 0.0% | ok |
| 2022-12-05 | 2022-12-11 | 8 | 3 | 0 | 0 | 0.0% | ok |
| 2022-12-12 | 2022-12-18 | 23 | 11 | 1 | 0 | 9.1% | ok |
| 2022-12-19 | 2022-12-25 | 10 | 6 | 0 | 0 | 0.0% | ok |
| 2022-12-26 | 2023-01-01 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2023-01-02 | 2023-01-08 | 7 | 3 | 0 | 0 | 0.0% | ok |

### Referral tests by person

| participant_id | num_sequential_referral_tests | num_floodlamp_results_pos_or_incl | floodlamp_tube_id | floodlamp_test_result | floodlamp_test_date | first_referral_test_date | referral_overall_result | first_referral_test_type | first_referral_test_result | second_referral_test_type | second_referral_test_result | third_referral_test_type | third_referral_test_result | antigen_neg_with_other_positive_flag | referral_eval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLMP183184 | 2 | 1 | AH7754 | Positive | 2022-12-15 | 2022-12-15 | Positive | LAMP Device | Positive | Rapid Antigen | Negative |  |  | 1 | FL pooled positive was confirmed with a Lucira that Antigen missed - see detailed report on referral testing FLSP Referral Test for 2022-12-15 Gary and Mithrabut confounding is that same 2 people in pool were Neg (AG2168) in a collection an hour later |
| FLMP197976 | 3 | 0 | 351430A | Negative | 2021-01-15 | 2021-01-15 | Positive | Direct PCR | Negative | Direct PCR | Negative | Lab Purif PCR | Positive | 0 | Positive by Lab Purif PCR collected 2 days after FL initial pooled positive - had high exposure to person in pool who was positive |
| FLMP233123 | 2 | 1 | MA26 | Positive | 2022-01-11 | 2022-01-12 | Positive | Lab PCR | Positive | Lab PCR | Negative |  |  | 0 | Was positive in duplicate on FL and confirmed by one LAB Purif PCR test (other said Neg) - see case report. |
| FLMP268140 | 1 | 0 | 351430 | Positive | 2021-01-15 | 2021-01-15 | Positive | Direct PCR | Positive |  |  |  |  | 0 | Initial pooled positive that detected an unknown positive. |
| FLMP466389 | 3 | 3 | 351430B | Positive | 2021-01-15 | 2021-01-16 | Positive | Direct PCR | Positive | Lab Purif PCR | Positive | Direct PCR | Positive | 0 | Confirmed positive using DirectPCR and also by a referral lab PCR test |
| FLMP618864 | 2 | 0 | AH7754 | Positive | 2022-12-15 | 2022-12-15 | Negative | LAMP Device | Negative | Antigen | Negative |  |  | 0 | Other member of pooled positive that was neg by referral tests |
| FLMP619442 | 1 | 8 | MA1215 | Positive | 2021-12-18 | 2021-12-18 | Positive | Antigen | Positive |  |  |  |  | 0 | FL pooled test during routine screening detected an unknown positive - confirmed right away by antigen test. |
| FLMP964950 | 11 | 4 | MAX288FIX | Positive | 2021-12-31 | 2021-12-31 | Positive | Antigen | Negative | LAMP Device | Negative | Rapid Antigen | Positive | 1 | See Case Report 2022-01-01_MS Case Report - New Years Eve.pdf - was first Pos by FloodLAMP then was Neg by 3 molecular tests (Lucira, Detect, and Accula), before turning Pos by antigen 2 days later |


# 2,673  FTFC_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: FTFC_pilot-data_summary.md
file_date: 2021-06-18
title: FTFC Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 1891
tokens: 2673
notes: 
summary_short: The "FTFC_pilot-data_summary" covers the FloodLAMP pilot program at the FTFC Eagles EMS Leadership Conference in Ft. Lauderdale, FL, where FloodLAMP staff provided pooled and individual self-collection testing for EMS personnel and conference attendees at the Hard Rock Hotel, Fort Lauderdale. The short 5-day program (2021-06-14 to 2021-06-18) tested 61 tubes from 195 participants with no positive tubes detected. The pop-up "lab" was brought out in a suitcase and setup in a hotel storage room where the sample processing was done.


CONTENT

## Plots

### Composite

![FTFC Weekly Composite](_plots/FTFC_weekly_composite.png)

### Percent Positive Tubes

![FTFC Weekly Percent Positives](_plots/FTFC_weekly_percent_positives.png)

### Volume

![FTFC Weekly Volume](_plots/FTFC_weekly_volume.png)

## Files

### Google Sheets URLs
- [FTFC_STS_PUB](https://docs.google.com/spreadsheets/d/17BcQljnvgzdSLB2KzgH0rrUvjOd44f9CfTAL5_9CTS4)

### Curated CSVs
- Curated CSV folder: `FTFC_curated_csvs/`
- Stats key-values CSV: [FTFC_STS_stats_key-values.csv](FTFC_curated_csvs/FTFC_STS_stats_key-values.csv)
- Weekly summary CSV: _not available_
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [FTFC_STS_PUB.xlsx](FTFC_xlsx_downloads/FTFC_STS_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR or APS Files | NONE | ok |  |  | Stats | 1 |
| Files | RTR File | NONE | ok |  |  | Stats | 2 |
| Files | RSR File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 61 | ok | initial run tubes only so excludes re-runs | all data from gsheet: Data Stats - Compilation PRE DP - Compilation tab (APS RAW data not available) | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 61 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs |  | not_available |  |  | Stats | 7 |
| Overall | Number of APS Only Tubes run |  | not_available |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 61 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 195 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 0 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 195 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 3.2 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) |  | not_available | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) |  | not_available | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes |  | not_available | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs |  | not_available |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs |  | not_available |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 0 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 0.0% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 0 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 0 | ok | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 0 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 0 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results |  | not_available |  | Not Applicable - No RFR | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 0 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.0% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests |  | denom_zero |  | denom zero | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 0 | ok |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 0 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App |  | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 0 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 0.0% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 0 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 0 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive |  | denom_zero |  | denom zero | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 0 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) |  | not_available |  | Not Applicable - no positives | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests |  | not_available |  | Not Applicable - no positives | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative |  | not_available | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative | Not Applicable - no positives | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative |  | not_available |  | Not Applicable - no positives | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative |  | not_available |  | Not Applicable - no positives | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative |  | not_available |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 195 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 4 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 0 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 0.0% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 0 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 0.0% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-06-14 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2021-06-18 | ok |  |  | Stats | 75 |
| Info | Test Operator | FloodLAMP | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Hotel Storage Room | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | EMS, Conference Attendees | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled & Individual | ok | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | FTFC | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Hard Rock Hotel | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Conference | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Ft. Lauderdale, FL | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |
| Info | Event | FTFC Eagles - EMS Leadership Conference | ok |  |  | Stats | 90 |

### Weekly summary

_Weekly summary CSV not found for this site._


# 2,742  KENT_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: KENT_pilot-data_summary.md
file_date: 2021-07-29
title: KENT Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 1929
tokens: 2742
notes: 
summary_short: The "KENT_pilot-data_summary" covers the FloodLAMP pilot program for a youth camp testing program at Camp Kenmont in Kent, CT, where volunteers and camp staff operated FloodLAMP for pooled HCW-collected testing of young adult campers and staff, brought up remotely, and using the FloodLAMP mobile app. The 1-month summer program (2021-06-28 to 2021-07-29) tested 190 tubes from 696 participant results (avg pool size 3.7) with 2 positive tubes detected.


CONTENT

## Plots

### Composite

![KENT Weekly Composite](_plots/KENT_weekly_composite.png)

### Percent Positive Tubes

![KENT Weekly Percent Positives](_plots/KENT_weekly_percent_positives.png)

### Volume

![KENT Weekly Volume](_plots/KENT_weekly_volume.png)

## Files

### Google Sheets URLs
- [KENT_STS_PUB](https://docs.google.com/spreadsheets/d/1J1Gqc0KAQX_xxiSJ5MR8DVjGzFSfDR-ckCKRNDYmDNQ)

### Curated CSVs
- Curated CSV folder: `KENT_curated_csvs/`
- Stats key-values CSV: [KENT_STS_stats_key-values.csv](KENT_curated_csvs/KENT_STS_stats_key-values.csv)
- Weekly summary CSV: _not available_
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [KENT_STS_PUB.xlsx](KENT_xlsx_downloads/KENT_STS_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR or APS Files | NONE | ok |  |  | Stats | 1 |
| Files | RTR File | NONE | ok |  |  | Stats | 2 |
| Files | RSR File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 190 | ok | initial run tubes only so excludes re-runs | unless otherwise specified - all data from gsheet: Data Stats - Compilation PRE DP - Compilation tab (APS RAW data not available) | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 191 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 3 | ok |  | 4 - 2 bunk and 2 plate runs (6-28, 6-30, and 7-29) | Stats | 7 |
| Overall | Number of APS Only Tubes run | 190 | ok |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 193 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 696 | ok | counts individual samples in pools and excludes re-runs | from Compilation data | Stats | 11 |
| Overall | Number of ARF Tubes | 0 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 696 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 3.7 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 1 | ok | from RFR Audit Num Run Tubes | Assume one initial inconclusive tube was rerun and not included in 190 in Compilation because that was from Appivo data | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 3 | ok | from RFR Audit Num rxns (excl ctrls) | Assume rerun was in triplicate | Stats | 18 |
| Re-runs | Re-run % of Tubes | 0.5% | ok | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 1 | ok |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 33.3% | ok |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 2 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 1.1% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 1 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 1 | ok | Previous tested (including by FloodLAMP test) or reported positive | tested twice once on 6-28 in bunk run and other on 6-30 in plate full camp run | Stats | 27 |
| Positives | Unknown Positive Cases | 0 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 0 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 | ok |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 0 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.0% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests |  | denom_zero |  | denom zero | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 0 | ok |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 1 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App |  | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 1 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 0.5% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 1 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 1 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% | ok |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 1 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 1 | ok |  |  | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 1 | ok |  |  | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 1 | ok | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 100.0% | ok |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 0 | ok |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 0.0% | ok |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 342 | ok | Includes UnknownPerson additions but not ARF tubes | Equal to number of participants in 89 tubes in KENT_2021-06-30_App data import 6-30 8:30am | Stats | 64 |
| People | Number of Unique Sponsors | 10 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 1 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 0.3% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 1 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 0.3% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-06-28 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2021-07-29 | ok |  |  | Stats | 75 |
| Info | Test Operator | Volunteers, Camp Staff | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | On Site Room | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Young Adult Campers, Staff | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled | ok |  Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | HCW | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | Remote (NSVD) | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Kent | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Camp Kenmont | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Youth Camp | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Kent, CT | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

_Weekly summary CSV not found for this site._


# 3,617  NDHM_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: NDHM_pilot-data_summary.md
file_date: 2022-10-03
title: NDHM Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2266
tokens: 3617
notes: 
summary_short: The "NDHM_pilot-data_summary" covers the FloodLAMP pilot program in a K-12 school in Needham, MA that used FloodLAMP for pooled household self-collection testing, with on-site test processing by school staff using a standard configuration. The program tested students, staff, and their families over 5 months (2022-05-02 to 2022-10-03), running 80 tubes from 190 participant results with no positive tubes detected. This program was initiated late in the pandemic and did not ramp up to significant testing volumes.


CONTENT

## Plots

### Composite

![NDHM Weekly Composite](_plots/NDHM_weekly_composite.png)

### Percent Positive Tubes

![NDHM Weekly Percent Positives](_plots/NDHM_weekly_percent_positives.png)

### Volume

![NDHM Weekly Volume](_plots/NDHM_weekly_volume.png)

## Files

### Google Sheets URLs
- [NDHM_APS_deID_PUB](https://docs.google.com/spreadsheets/d/19gjZ2g6wjAQfB0WsPoEvDEr3R4sIK6sjT3g2ofL9Qeo)
- [NDHM_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/1SUcXSa-1wQggm8krA_VdFDp4_FCO_v1Xfrp78ITCjjQ)

### Curated CSVs
- Curated CSV folder: `NDHM_curated_csvs/`
- Stats key-values CSV: [NDHM_APS_stats_key-values.csv](NDHM_curated_csvs/NDHM_APS_stats_key-values.csv)
- Weekly summary CSV: [NDHM_APS_weekly-summary.csv](NDHM_curated_csvs/NDHM_APS_weekly-summary.csv)
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [NDHM_APS_deID_PUB.xlsx](NDHM_xlsx_downloads/NDHM_APS_deID_PUB.xlsx)
- [NDHM_RFR_deID_PUB.xlsx](NDHM_xlsx_downloads/NDHM_RFR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | NDHM_RFR_deID_PUB | ok |  |  | Stats | 1 |
| Files | RTR File | NONE | ok |  |  | Stats | 2 |
| Files | RSR File | NONE | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 80 | ok | initial run tubes only so excludes re-runs |  | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 85 | ok | includes re-runs |  | Stats | 6 |
| Overall | Number of Initial Runs | 15 | ok |  |  | Stats | 7 |
| Overall | Number of APS Only Tubes run | 0 | ok |  |  | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 109 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 190 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 2 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 192 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 2.4 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) | 5 | ok | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) | 18 | ok | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes | 6.2% | ok | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs | 3 | ok |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs | 20.0% | ok |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 0 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) |  | not_available |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 0 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 0 | ok | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 0 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 0 | ok |  |  | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results | 0 | ok |  |  | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 0 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive |  | not_available |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests |  | not_available |  |  | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 0 | ok |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 3 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App |  | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 4 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 4.7% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 0 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests |  | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 0 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive |  | denom_zero |  | denom zero | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 0 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) |  | not_available |  | Not Applicable - no positives | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests |  | not_available |  | Not Applicable - no positives | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative |  | not_available | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative | Not Applicable - no positives | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative |  | not_available |  | Not Applicable - no positives | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative |  | not_available |  | Not Applicable - no positives | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative |  | not_available |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 130 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 19 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 0 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 0.0% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 0 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 0.0% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2022-05-02 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2022-10-03 | ok |  |  | Stats | 75 |
| Info | Test Operator | Needham Beth Shalom School | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Office Space | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | Students, Staff, Families | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Pooled Household | ok | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | Self | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person & Remote | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Needham | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Needham Beth Shalom School | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | K-12 School | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Needham, MA | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022-05-02 | 2022-05-08 | 34 | 17 | 0 | 0 | 0.0% | ok |
| 2022-05-09 | 2022-05-15 | 22 | 9 | 0 | 0 | 0.0% | ok |
| 2022-05-16 | 2022-05-22 | 26 | 10 | 0 | 0 | 0.0% | ok |
| 2022-05-23 | 2022-05-29 | 22 | 8 | 0 | 0 | 0.0% | ok |
| 2022-05-30 | 2022-06-05 | 28 | 13 | 0 | 0 | 0.0% | ok |
| 2022-06-06 | 2022-06-12 | 19 | 8 | 0 | 0 | 0.0% | ok |
| 2022-06-13 | 2022-06-19 | 12 | 4 | 0 | 0 | 0.0% | ok |
| 2022-06-20 | 2022-06-26 | 4 | 2 | 0 | 0 | 0.0% | ok |
| 2022-06-27 | 2022-07-03 | 3 | 1 | 0 | 0 | 0.0% | ok |
| 2022-07-04 | 2022-07-10 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-07-11 | 2022-07-17 | 2 | 1 | 0 | 0 | 0.0% | ok |
| 2022-07-18 | 2022-07-24 | 2 | 1 | 0 | 0 | 0.0% | ok |
| 2022-07-25 | 2022-07-31 | 6 | 3 | 0 | 0 | 0.0% | ok |
| 2022-08-01 | 2022-08-07 | 3 | 1 | 0 | 0 | 0.0% | ok |
| 2022-08-08 | 2022-08-14 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-15 | 2022-08-21 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-22 | 2022-08-28 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-08-29 | 2022-09-04 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-09-05 | 2022-09-11 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-09-12 | 2022-09-18 | 4 | 1 | 0 | 0 | 0.0% | ok |
| 2022-09-19 | 2022-09-25 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-09-26 | 2022-10-02 | 0 | 0 | 0 | 0 |  | denom_zero |
| 2022-10-03 | 2022-10-09 | 3 | 1 | 0 | 0 | 0.0% | ok |


# 3,337  ROSA_pilot-data_summary.md
METADATA
last updated: 2026-03-23
file_name: ROSA_pilot-data_summary.md
file_date: 2021-12-17
title: ROSA Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2179
tokens: 3337
notes: 
summary_short: The "ROSA_pilot-data_summary" covers the FloodLAMP pilot program for a TV production in Davie, FL, where Davie Fire and Rescue operated surveillance testing for individual (non-pooled) HCW-collected testing of TV production staff at the production set. The program ran over 3 months (2021-09-28 to 2021-12-17), testing 781 tubes from 156 unique individuals with 1 positive tube detected, which was confirmed with antigen testing.


CONTENT

## Plots

### Composite

![ROSA Weekly Composite](_plots/ROSA_weekly_composite.png)

### Percent Positive Tubes

![ROSA Weekly Percent Positives](_plots/ROSA_weekly_percent_positives.png)

### Volume

![ROSA Weekly Volume](_plots/ROSA_weekly_volume.png)

## Files

### Google Sheets URLs
- [ROSA_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1pUr7UFD7gL4bUr6uBSe-H4rqQol5CwoGmRylvzEodEc)
- [ROSA_RSR_deID_PUB](https://docs.google.com/spreadsheets/d/12oIWiJjYQ8z--l4YUoXnmq9m-1pF0feO6-mnHIsSdiA)

### Curated CSVs
- Curated CSV folder: `ROSA_curated_csvs/`
- Stats key-values CSV: [ROSA_APS_stats_key-values.csv](ROSA_curated_csvs/ROSA_APS_stats_key-values.csv)
- Weekly summary CSV: [ROSA_APS_weekly-summary.csv](ROSA_curated_csvs/ROSA_APS_weekly-summary.csv)
- Referral tests by person CSV: _not available_

### XLSX downloads:
- [ROSA_APS_deID_PUB.xlsx](ROSA_xlsx_downloads/ROSA_APS_deID_PUB.xlsx)
- [ROSA_RSR_deID_PUB.xlsx](ROSA_xlsx_downloads/ROSA_RSR_deID_PUB.xlsx)

## Key tables

### Stats key-values

| section | metric | value | value_status | details | comments | source_sheet | source_row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Files | RFR File | NONE | ok |  |  | Stats | 1 |
| Files | RTR File | NONE | ok |  |  | Stats | 2 |
| Files | RSR File | ROSA_RSR_deID_PUB | ok |  |  | Stats | 3 |
| Overall | Number of Tubes Tested (initial only - no re-runs) | 781 | ok | initial run tubes only so excludes re-runs | only indiv testing - no pools. total 785 from RSR - Run Summary Report that draws from google form of weekly testing summary provided by test Admin | Stats | 5 |
| Overall | Number of Tube Tests Run (includes re-runs) | 781 | ok | includes re-runs | no RFR so no info on re-runs | Stats | 6 |
| Overall | Number of Initial Runs | 53 | ok |  | use collection date assuming all tubes run same day | Stats | 7 |
| Overall | Number of APS Only Tubes run | 781 | ok |  | No RFR so all tubes are APS Only | Stats | 8 |
| Overall | Number of Test Reactions (RFR plus APS only tubes run) | 781 | ok | includes technical replicates (the same tube sample in multiple reactions in the same run) |  | Stats | 9 |
| Overall | Number of Participant Results | 781 | ok | counts individual samples in pools and excludes re-runs |  | Stats | 11 |
| Overall | Number of ARF Tubes | 0 | ok | tubes run and present in RFR but not in Appivo - created tube IDs that start with ARF |  | Stats | 12 |
| Overall | Sum of Participant Results plus ARF Tubes | 781 | ok | Will be equal to the number of tubes tested if no pooling. |  | Stats | 13 |
| Overall | Average Pool Level (excludes ARF) | 1.0 | ok |  |  | Stats | 14 |
| Re-runs | Number of Run Tubes (re-runs only) |  | not_available | from RFR Audit Num Run Tubes |  | Stats | 17 |
| Re-runs | Number of Reactions (re-runs only) |  | not_available | from RFR Audit Num rxns (excl ctrls) |  | Stats | 18 |
| Re-runs | Re-run % of Tubes |  | not_available | re-run / initial |  | Stats | 19 |
| Re-runs | Number of Initial Runs with Re-runs |  | not_available |  |  | Stats | 20 |
| Re-runs | % Initial Runs with Re-runs |  | not_available |  |  | Stats | 21 |
| Positives | Number of Tubes with Final Result Positive | 1 | ok |  |  | Stats | 24 |
| Positives | % of Tubes Positives (Final Result) | 0.1% | ok |  |  | Stats | 25 |
| Positives | Number of Cases with Final Result Positive (Indiv or Pool) | 1 | ok | Subtract off Re-tests |  | Stats | 26 |
| Positives | Known Positive Cases | 0 | ok | Previous tested (including by FloodLAMP test) or reported positive |  | Stats | 27 |
| Positives | Unknown Positive Cases | 1 | ok |  |  | Stats | 28 |
| Inconclusives | Number of Tubes with Final Result Inconclusive | 0 | ok |  | from RSR - Run Summary Report that draws from google form of weekly testing summary provided by test Admin | Stats | 31 |
| Inconclusives | Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results |  | not_available |  | Not Applicable - No RFR | Stats | 32 |
| Inconclusives | Total Number of Inconclusive Tubes | 0 | ok |  |  | Stats | 33 |
| Inconclusives | % of Tubes Inconclusive | 0.0% | ok |  |  | Stats | 34 |
| Inconclusives | Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence | 0 | ok |  |  | Stats | 35 |
| Inconclusives | % Inconclusives resolved Positive by Referral Tests |  | denom_zero |  | denom zero | Stats | 36 |
| Inconclusives | Number of Inconclusive Tubes with Referral Test or Correspondence Negative | 0 | ok |  |  | Stats | 37 |
| Inconclusives | Number of Inconclusive Tubes with no Referral Test result or Correspondence | 0 | ok |  |  | Stats | 38 |
| Inconclusives | Number of Tubes with Initial Inconclusives and Re-run Negative | 1 | ok | Count Result Correction Code=2.5 in preDel col AJ, or from RFR preExcl if not resulted as Incl in App |  | Stats | 39 |
| Inconclusives | Number of Inconclusive Test Run Calls | 1 | ok | includes re-runs - from RFR Audit only and excludes any APS only resulted inconclusives |  | Stats | 40 |
| Inconclusives | % Tube Tests Run Called Inconclusive | 0.1% | ok | includes re-runs |  | Stats | 41 |
| Referrals and Correspondence | Number of FloodLAMP Cases with Referral Tests or Correspondence | 1 | ok | Indiv or Pool, Cases used instead of Person to account for people being contracting COVID multiple times, and instead of Results to exclude re-tests | Single pos case was confirmed with same day pos antigen test (RT Jan26 email) | Stats | 44 |
| Referrals and Correspondence | Number of Referral Confirmed FloodLAMP Positives | 1 | ok | Sometimes also termed Agree Positives - Include initial Inconclusive with Referral or Correspondence Positive |  | Stats | 45 |
| Referrals and Correspondence | FL Inconclusives with Referral / Correspondence Positive | 0 | ok |  |  | Stats | 46 |
| Referrals and Correspondence | % FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive | 100.0% | ok |  |  | Stats | 47 |
| Referrals and Correspondence | FL Inconclusives but Referral / Correspondence Negative | 0 | ok |  |  | Stats | 48 |
| Referrals and Correspondence | FL Inconclusives with No Referral Tests or Correspondence | 1 | ok |  |  | Stats | 49 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day) | 1 | ok |  | Single pos case was confirmed with same day pos antigen test (RT Jan26 email) | Stats | 52 |
| Comparison to Antigen | Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests | 1 | ok |  | Single pos case was confirmed with same day pos antigen test (RT Jan26 email) | Stats | 53 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative | 0 | ok | Agree with Referral Test Positive (usually PCR or later Antigen) but Initial Antigen Negative |  | Stats | 54 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives with Same Day Antigen Negative | 0.0% | ok |  |  | Stats | 55 |
| Comparison to Antigen | Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative | 0 | ok |  |  | Stats | 56 |
| Comparison to Antigen | % Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative | 0.0% | ok |  |  | Stats | 57 |
| False Calls | False Positives Final Results | 0 | ok | From reviewing APS/Pos and Incl tab Unconfirmed FL Positives |  | Stats | 60 |
| False Calls | False Negative Final Results (Suspected) | 0 | ok | From reviewing Referral Tests by Person and correspondence with Program Admin |  | Stats | 61 |
| People | Number of Unique Individuals Tested | 156 | ok | Includes UnknownPerson additions but not ARF tubes |  | Stats | 64 |
| People | Number of Unique Sponsors | 2 | ok | People who collect using the app |  | Stats | 65 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive | 1 | ok | includes Inconclusive FloodLAMP result confirmed Positive by follow-up or Referral |  | Stats | 68 |
| Positivity | % of Population FloodLAMP Positive (excluding pools not deconv) | 0.6% | ok |  |  | Stats | 69 |
| Positivity | Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool) | 1 | ok |  |  | Stats | 70 |
| Positivity | % of Population FloodLAMP Positive (including everyone in a positive pool) | 0.6% | ok |  |  | Stats | 71 |
| Dates | Start Run Date | 2021-09-28 | ok |  |  | Stats | 74 |
| Dates | End Run Date | 2021-12-17 | ok |  |  | Stats | 75 |
| Info | Test Operator | Davie Fire and Rescue | ok | Who ran the actual testing (running LAMP reactions) |  | Stats | 78 |
| Info | Test Processing Site | Office | ok | Where the test processing (running LAMP reactions) was done |  | Stats | 79 |
| Info | Population Tested | TV Production Staff | ok | Description of the participants |  | Stats | 80 |
| Info | Configuration | Standard | ok | Equipment set used for test processing (relates to throughput and type of test tube used) |  | Stats | 81 |
| Info | Collection Type | Individual | ok | Pooled, Individual, or Both |  | Stats | 82 |
| Info | Self or HCW Collected | HCW | ok | HCW is Health Care Worker |  | Stats | 83 |
| Info | App Used? | Yes | ok | Was the FloodLAMP Mobile App and Admin Portal utilized in the program |  | Stats | 84 |
| Info | Bring-up Type | In Person | ok | How the initial setup and validation of the testing site was done |  | Stats | 85 |
| Info | Program Name | Rosa | ok | Shorthand name used internally at FloodLAMP and in other documents for this program |  | Stats | 86 |
| Info | Site | Production Set / Fire Station | ok | Broader physical space where the testing was done and/or where participants congregated |  | Stats | 87 |
| Info | Site Type | Production Organization | ok | Type of entity or organization receiving the testing program |  | Stats | 88 |
| Info | Location | Davie, FL | ok | Geographical location of where the FloodLAMP testing program occurred |  | Stats | 89 |

### Weekly summary

| week_start_date | week_end_date | participants_n | tubes_n | positive_tubes_n | inconclusive_tubes_n | pct_positive | pct_positive_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-09-27 | 2021-10-03 | 17 | 17 | 0 | 0 | 0.0% | ok |
| 2021-10-04 | 2021-10-10 | 84 | 84 | 0 | 0 | 0.0% | ok |
| 2021-10-11 | 2021-10-17 | 79 | 79 | 0 | 0 | 0.0% | ok |
| 2021-10-18 | 2021-10-24 | 64 | 64 | 0 | 0 | 0.0% | ok |
| 2021-10-25 | 2021-10-31 | 53 | 53 | 0 | 0 | 0.0% | ok |
| 2021-11-01 | 2021-11-07 | 68 | 68 | 0 | 0 | 0.0% | ok |
| 2021-11-08 | 2021-11-14 | 64 | 64 | 0 | 0 | 0.0% | ok |
| 2021-11-15 | 2021-11-21 | 76 | 76 | 0 | 0 | 0.0% | ok |
| 2021-11-22 | 2021-11-28 | 36 | 36 | 0 | 0 | 0.0% | ok |
| 2021-11-29 | 2021-12-05 | 59 | 59 | 0 | 0 | 0.0% | ok |
| 2021-12-06 | 2021-12-12 | 84 | 84 | 0 | 0 | 0.0% | ok |
| 2021-12-13 | 2021-12-19 | 97 | 97 | 1 | 0 | 1.0% | ok |


METADATA
last updated: 2026-04-15_180754
file_name: _archive-combined-files_pilot-sites_15k.md
category: pilots
subcategory: pilot-sites
words: 9447
tokens: 15516


CONTENT

# _archive-combined-files_pilot-sites_15k (4 files, 15,516 tokens)

# 7,639  _context-commentary_pilots-pilot-sites.md
METADATA
last updated: 2026-03-23 RT
file_name: _context-commentary_pilots-pilot-sites.md
category: pilots
subcategory: pilot-sites
gfile_url: https://docs.google.com/document/d/1UDeyVPHknvMcDDQ-5ZbaSZNiQEDpmh9eSGfizTYAFWA
words: 5625
tokens: 7639


CONTENT

## Context
This `pilots/pilot-sites` subcategory covers the FloodLAMP pilot programs as site-level implementations and case studies. Quantitative summaries, data-processing notes, and dataset-specific commentary are in `pilots/pilot-data`.

## Commentary
#### FLMP - FloodLAMP (includes CRLN and FLSP)
The FLMP designation exists because the Carillon (CRLN) and FLSP (FloodLAMP Staff Plus) programs shared a single tenant (instance of the application) in the FloodLAMP app software, and their testing runs were intermingled. Each tube was assigned to either Carillon or FLSP based on whether the participants belonged to or were associated with the Carillon preschool community. For the FloodLAMP founders' family (whose 2 young kids attended Carillon) and our household help, the assignment was date-based: during the dates the Carillon program was active, samples were attributed to Carillon; outside those dates, to FLSP.

#### FLSP - FloodLAMP Staff Plus Other Community
FLSP served as the catch-all program for FloodLAMP's internal staff testing plus friends, family, neighbors, co-workers, and other community members tested over the course of 2+ years of operations. The program start date was set at December 2020, when data collection began and the test had stabilized on the direct, no-purification protocol we used going forward. Testing was conducted from multiple locations: the main lab at MBC BioLabs in San Carlos, California; a home garage lab in Portola Valley; and later at the 2022 Portola Valley office space. In addition there were several pop-up sites where the mobile kit was used.

The internal testing program produced several notable case studies. In multiple instances, routine screening unexpectedly detected positive cases among FloodLAMP staff, and the early detection appeared to contribute to preventing further spread within the company and within household contacts.

##### Case Study 1 — FloodLAMP Founder (December 2021)
The founder (Randy True) contracted COVID-19 at a holiday gathering during the Omicron surge ramp-up. He was participating in every-other-day pooled screening with staff and tested negative in the morning; minor symptoms first appeared that evening. A pooled test run 2 days later, early in the morning, was positive. A rapid antigen test confirmed the result immediately. He was able to isolate before anyone else in the household became infected, and no one else in the household tested positive. While this case illustrated the value of early detection through routine screening, it also illustrates a limitation: in some cases, even with every-other-day testing, the more sensitive FloodLAMP test can catch the infection at the same point as a less sensitive rapid antigen test.
See: `2021-12-28_Case Report - Randy`

##### Case Study 2 — New Year's Eve (December 31, 2021)
This case presented a more striking comparison between FloodLAMP and other FDA authorized commercial tests that missed this infection. 

This is easiest to review visually.
See: `2022-01-01_Case Report - New Years Eve`

An individual nasal swab collected at 9 a.m. on December 31st tested positive on the FloodLAMP colorimetric LAMP test, and PCR run on the same TCEP-inactivated sample confirmed the result. However, subsequent testing that same afternoon using several different commercial tests including a rapid antigen test (BinaxNOW), Lucira, and Detect were all negative. A 5 p.m. resampling showed the infection presenting more strongly in a throat swab (Ct 30.2) than the nasal swab (Ct 39.4 on one of three PCR replicates, with the other two undetermined), suggesting low and variable viral load distribution. A saliva sample collected later that evening had a Ct of 28.

The following day, New Year's Day, nasal and throat samples were positive on FloodLAMP and PCR but still negative on BinaxNOW antigen. An Accula rapid molecular test (PCR-based, 30-minute cartridge with lateral flow readout) administered at an airport testing site was also negative. It was not until the morning of January 2nd that two different antigen test brands (FlowFlex and BinaxNOW) finally returned positive results, confirming the FloodLAMP detection approximately 48 hours earlier.

This case illustrates the variability across FDA-authorized testing modalities, a finding consistent with the FDA's own SARS-CoV-2 Reference Panel results, which showed unexpectedly large differences from the sensitivity figures reported in EUA submissions. See:
- `regulatory/fda-policy/_AI_FDA SARS-CoV-2 Reference Panel Report`
- `regulatory/fda-policy/FDA SARS-CoV-2 Reference Panel Comparative Data - Complied by Matt McFarlane`
- `regulatory/fda-policy/2023-09-23_FDA Response Letter - To Compliant regarding FDA Reference Panel from Dec 2020`

FloodLAMP developed its LAMP and PCR tests to run from the same TCEP-inactivated sample, as submitted to the FDA in March 2021. This dual-test capability proved particularly valuable for this case where multiple EUA authorized tests returned false negatives, and could be generally useful for cases requiring additional confirmation (see: `regulatory/fl-fda-submissions`; `various/fl-presentations/BARDA Market Research - FloodLAMP Presentation (2022-03-07).md`, slides 46–50).

Over the full span of the FLSP program, staff testing detected four confirmed COVID-19 cases (the founder, one staff member, a domestic partner of a staff member, and the New Year's Eve case). In each instance, the case was caught early and no other FloodLAMP staff tested positive in the period immediately following. The program's primary value was as a longitudinal demonstration that routine molecular screening of a small, closely interacting group can detect infections early enough to stop workplace and even household transmission.

#### CRLN - Carillon Pre-School in Portola Valley, CA
The Carillon program is documented in detail in FloodLAMP's most comprehensive white paper (see: `various/fl-whitepapers/FloodLAMP Whitepaper - California Preschool Family Pooled Screening Pilot (June 2022)` and `various/fl-whitepapers/_context-commentary_various-fl-whitepapers`).

Carillon was a small preschool in Portola Valley, California, attended by the children of FloodLAMP founders Randy True and Theresa Ling. The founders' familiarity with the school's staff facilitated the program launch. As the Omicron surge arrived in December 2021, previous discussions about a testing program turned into concrete plans, and the program was set to begin immediately after the holiday break.

The close relationship with the school enabled program features that were likely rare, or possibly unique, among pandemic-era COVID-19 screening programs. Families were onboarded before the first day of testing with signed consent and pooled collection kits (five to ten per family). A dropbox at the school entrance served as both the sample drop-off and kit pickup location. Families registered pooled collections through the FloodLAMP app, identifying all participants including siblings and household members such as nannies or grandparents. The typical daily workflow was straightforward: families collected samples, swabbing themselves and kids, typically at home, the morning of school and then dropped them off at the same time as their children at the school. A FloodLAMP team member collected all kits from the dropbox within minutes of the morning drop-off and drove them home (approximately five minutes) for processing, with results available usually within 2 hours. No extra transportation or trips were required from participating families.

A trade-off of this model was that children were already at school when results became available (excluding the first run in early January and after spring break). Follow-up testing and confirmatory information was received for some cases but not all positives.

The program demonstrated its value immediately. Before the first day back from the holiday break, families dropped off samples the evening prior. Two pools tested positive that night. Both families were asymptomatic, and both positive results were subsequently confirmed. This was important news and the families were contacted and referred to follow-up diagnostic testing. The kids of those families of course did not come to school, and This early detection may have reduced onward exposure at the school, although this cannot be established from these data. This is a real-world case to understand the problems of the FDA/CMS policy with respect to "surveillance" testing and "individual decision making". See the subcategory `regulatory/surveillance` and the context and commentary file there.

The same pre-screening approach was used successfully after spring break. These involved an extra trip to the school for drop-off but significantly increased the effectiveness of the program.

Another documented case report describes one asymptomatic family pool detected on the first day back from the holiday break. Individual deconvolution the following day showed both parents positive and both children negative; the children turned antigen-positive the next day. All four family members were confirmed by PCR (results took one to two days). Return testing beginning a week later showed persistent FloodLAMP positivity: 15 days after the initial positive pool result, the family pool was still positive on FloodLAMP while all members tested negative on antigen (see: `2022-01-02_Carillon Case Report of Asymptomatic Positive Family Pool`).

Another informative case study involved a teacher who had tested negative on antigen tests for three consecutive days following known household exposure, came to school believing they were clear and tested positive on FloodLAMP the same day. The result was confirmed by a lab PCR test. Either the timing of viral load ramp-up or the increased sensitivity of the molecular test accounted for the detection difference. Regardless, the screening program identified the case before further classroom exposure occurred.

In total, the program identified eight positive pools or case clusters. Of the six with deconvolution or confirmatory referral test results, the initially positive individual was the school-aged child in half of cases and a parent or sibling in the other half. This reflects the value of extending coverage in a screening/surveillance program to the entire household.

The Carillon program implemented several program features that FloodLAMP considered both valuable and rare: multi-week longitudinal testing, household pooling, fast few-hour turnaround, and deconvolution capability. Operating it within the founders' own school community provided an unusually close perspective on the day-to-day logistics and at the same time, the experience of a participating family.

#### FTFC - Eagles/EMS Leadership Conference in Ft. Lauderdale, FL
The FTFC conference in June 2021 was FloodLAMP's first significant external testing event and served as the entry point into the EMS and municipal surveillance pilots that followed (Coral Springs, Davie, and Bend). FloodLAMP staff flew from California with all lab materials in two suitcases and set up a pop-up lab in a storage room at the Hard Rock Hotel in Fort Lauderdale. A freezer and refrigerator were available on-site (possibly ordered via Amazon, though this detail is uncertain). A volunteer graduate student was trained to run the test, freeing FloodLAMP staff for sample collection and conference interaction.

Testing was offered as a voluntary service and as a chance to learn about our program. We had a table in the hallway at the conference and a curtained tent for private sample collection. Participation was lower than anticipated. We agreed to and started preparing months before, but in June 2021 when the conference happened, prevalence had dropped and that mid-summer was a low point in pandemic prevalence. Many attendees viewed the pandemic as winding down, masks were rarely worn, and Florida maintained a relatively lax COVID-19 posture. FloodLAMP had prepared to run thousands of samples but processed only 61 tubes covering approximately 195 individuals over three days. There were no positive or inconclusive results.

The testing was conducted in collaboration with two nonprofits: the Research Aid Network and the National Scientist Volunteer Database (NSVD). FloodLAMP gave a short invited talk to EMS leadership (see: `various/fl-presentations/FTFC EMS Conference - FloodLAMP Talk Slides (6-14-2021)`). The conference was where FloodLAMP trained Dr. Peter Antevy, who became the Program Medical Director for FloodLAMP and was our main contact in the EMS world. Dr. Antevy purchased the testing equipment (approximately $7K), which was subsequently shipped to the Kent Camp pilot.

Despite the low testing volume, the FTFC conference yielded valuable EMS leadership contacts and practical experience deploying a pop-up laboratory, both of which directly contributed to FloodLAMP's subsequent pilot programs.

#### KENT - Camp Kenmont Youth Camp in Kent, CT
The Kent Camp pilot was FloodLAMP's first fully remote deployment, with no FloodLAMP staff traveling to the site. Dr. Peter Antevy trained three graduate student volunteers recruited through the National Scientist Volunteer Database (NSVD), a non-profit co-founded by FloodLAMP's COO. These volunteers performed all on-site testing.

A positive COVID-19 case was identified among incoming campers through initial PCR testing. In the period between testing and arrival, other campers had been exposed, creating an immediate need for on-site surveillance screening capability before the camp session began. The FloodLAMP testing was used alongside antigen testing and was reported to be helpful. The known positive sample also served an unplanned validation role as a shipping issue (likely warming during transit) compromised the frozen positive control material that FloodLAMP normally provides, making the known positive case a useful substitute for test verification.

Surveillance screening was conducted in two planned sessions, covering two different cohorts of campers. Samples were processed in a single 96-well reaction plate. Besides the known positive, no additional positives were detected.

The Kent pilot demonstrated the feasibility of a remote bring-up model without FloodLAMP staff on-site. Its primary contribution was showing that fast-turnaround on-site molecular screening capability could be established remotely with trained volunteer support.

#### COSP - Coral Springs City Municipal/EMS in Coral Springs, FL
Coral Springs (population ~140,000) in south Florida was FloodLAMP's first major paid pilot and largest testing program by total volume. FloodLAMP staff traveled from California with equipment and consumables, set up a pop-up lab in an empty medical office, ran a successful validation, and trained one firefighter with no prior lab or pipetting experience.

The program started in September 2021 with modest volumes: averaging 25 tubes (pools) and 90 participants for the first three months. When the Omicron surge hit in mid-December, the program expanded rapidly to comprehensively cover first responders and municipal staff. At peak, Coral Springs ran 800 tubes per week covering 2,600 participants (includes repeated testing of the same people), with multiple collection points across city buildings, police stations, and fire stations. Two staff members operated two inactivation and amplification stations ("double standard" configuration), running LAMP reactions in 96-well plates. During the December–January Omicron surge, the site ran three to four FloodLAMP processing runs per day to cover three emergency responder shifts, operating seven days a week.

One significant limitation in the Coral Springs data is the absence of comparator testing data. They did do extensive antigen testing, including follow-up testing for all FloodLAMP positives, but FloodLAMP was unable to obtain this critical data. We let Coral Springs leadership know how important this data was and gave assurances of privacy protections (FloodLAMP staff had been through CITI training and certification to properly handle PII/PHI), but they did not share the antigen test data. In retrospect, de-identified data publication rights should have been included in the contract and we simply did not consider that they would not share it.

The primary tester, however, did share the details of a particular case which was informative. He described a plate with 22 positive results, an unusually high number that he verified by rerunning the samples with identical results. Of those 22, only one was positive on same-day BinaxNOW rapid antigen testing, which was standard protocol to run after a FloodLAMP positive. The remaining 21 antigen-negative individuals returned to work, but two days later "everybody started popping positive," with most having previously tested positive by FloodLAMP. The conclusion after that episode was that BinaxNOW was significantly less sensitive than FloodLAMP for early detection. This observation was consistent with findings from other FloodLAMP pilot sites and is not unexpected given the known sensitivity gap between molecular and antigen testing, i.e. a performance gap at low viral loads.

Testing ended abruptly in late February 2022 as the Omicron wave passed through the community.

#### DAVI - Town of Davie Fire/EMS in Davie, FL
The Town of Davie (population ~110,000) is located next to Coral Springs in south Florida. During the pandemic, the two towns shared the same Medical Director who connected both to FloodLAMP and whom we worked with at the FTFC EMS Leadership Conference (and who also ran the Kent pilot). The firefighter trained at Coral Springs subsequently trained the Davie tester, also a veteran firefighter, with supplementary early-morning support calls from FloodLAMP's founder. This single individual performed all testing at the Davie site.

The program timeline paralleled Coral Springs: modest volumes averaging approximately 30 tubes and 80 participants per week from September through November 2021, followed by rapid expansion during the Omicron surge. Testing peaked at approximately 500 tubes per week in early January 2022, with positivity rates reaching 34% during the peak week.

Feedback from the site regarding program effectiveness was consistently positive. One reported case illustrated the operational value of pooled screening with deconvolution capability: a leadership member's family pool tested positive, and the tester immediately resampled the family members to deconvolute the pool, running individuals on FloodLAMP to identify positives. The combination of confidence in test performance and operational flexibility was what the site valued most. Program success led to expansion in mid-November 2021, extending FloodLAMP testing from EMS personnel to all Town of Davie municipal employees on a voluntary daily or weekly basis, with six designated collection points and daily pickup by Fire Rescue staff.

The Davie site produced the archive's most detailed head-to-head comparison between FloodLAMP and BinaxNOW rapid antigen testing, tracking 51 employee cases through three evolving testing protocols during the Delta and Omicron waves (see: `DAVI_pilot-data/DAVI_pilot-data_referral-antigen-comparison`):
- **Group 1** (15 employees, Sep 15 – Dec 23): FloodLAMP as primary test; BinaxNOW used sometimes at home on Day 0.
- **Group 2** (22 employees, Dec 24 – Jan 9): Both tests used throughout until return-to-work clearance, providing the most informative direct comparison data.
- **Group 3** (14 employees, Jan 10 – Feb 7): FloodLAMP for initial detection; BinaxNOW for return-to-work clearance.

Across cases with same-day results, FloodLAMP and BinaxNOW agreed 90% of the time. In the remaining 10% (four employees), FloodLAMP detected the infection while BinaxNOW did not; three of those four were asymptomatic. There were zero cases where antigen testing detected a positive that FloodLAMP missed. During the intensive dual-testing phase (Group 2), the two tests generally tracked closely and cleared on the same day, with an average time to negative of approximately 9 days. The divergence between the BinaxNOW antigen test and FloodLAMP was concentrated at infection onset, particularly in asymptomatic or low-viral-load individuals. This is the detection gap that molecular screening closes. The program reported no false positives or suspected false negatives in available follow-up data, with 98% of FloodLAMP positives confirmed by referral or correspondence.

The Davie comparison data, combined with the anecdotal report from Coral Springs (21 of 22 FloodLAMP positives antigen-negative but subsequently confirmed), reinforced a consistent finding across the pilot programs: BinaxNOW rapid antigen tests lagged FloodLAMP molecular detection at infection onset, especially in asymptomatic individuals. See pilot COMB below where the comparison with antigen tests showed significantly more positive cases identified by FloodLAMP but missed by antigen.

#### ROSA - ROSA TV Production in Davie, FL
The ROSA program was FloodLAMP's only third-party or affiliated pilot, in which another organization ran the FloodLAMP test commercially. "ROSA" is a pseudonym; FloodLAMP does not have permission to disclose the production company name.

All samples were run individually (no pooling), collected from TV show staff and actors on the production site, and shuttled to the Davie Fire and Rescue lab for processing. Processing was reportedly done promptly and separately from the Town of Davie staff samples. A dedicated COVID testing program manager at the production site administered the program, handling sample collection, app registration, and results management. FloodLAMP's involvement was limited primarily to digital and app support.

The program ran consistently at 50 to 100 samples per week for 11 weeks. No positives were detected until the final week, when one positive was identified and confirmed with a same-day antigen test. FloodLAMP had minimal involvement with this program.

#### BEND - Bend Fire and Rescue/EMS in Bend, OR
The Bend pilot was a follow-on EMS program resulting from the success of Coral Springs and Davie. Although FloodLAMP received significant interest from other EMS programs nationally, Bend was the only additional EMS site brought online.

Unlike Davie and Coral Springs, Bend tested only firefighters and EMS personnel, and all samples were run individually (no pooling). The primary motivation for the FloodLAMP program was dissatisfaction with the cost and turnaround time of PCR testing from a local lab.

The bring-up process was conducted entirely remotely, without FloodLAMP staff traveling to Oregon. A local scientist volunteer, recruited through the National Scientist Volunteer Database (NSVD), provided critical on-site support. The program began with a one-hour Zoom kickoff call with fire and emergency management leadership, followed by remote training with the volunteer scientist providing hands-on assistance. The remote training was a bit awkward but proved effective. See the slides presented in the archive file: `various/fl-presentations/Bend Pilot Program Bring-up (12-01-2021)`. Of note is the discussion of contamination procedures and the mental models developed for EMS personnel to adopt (see end of `various/fl-presentations/_context-commentary_various-fl-presentations`).

Positivity rates were high throughout January 2022 during the Omicron surge, ranging from 11% to 37%. All FloodLAMP positives were confirmed by the local clinical lab PCR, with no false positives documented in available follow-up data. The program recorded two inconclusive results, one of which was confirmed positive by PCR and the other negative by PCR.

Bend purchased a "double mini" system: two small heaters accommodating up to 40 200μl PCR tubes each, run in strip tube format. These min heaters were also used for inactivation, holding 15 1.5mL tubes for the 5 minute heat time. This smaller system was feasible because individual (non-pooled) samples could be collected in 1.5 ml tubes (though these tubes could hold 2 swabs), thus avoiding the 5 ml tubes required for 4-swab pooling (which necessitated water bath inactivation at the Davie and Coral Springs sites). FloodLAMP charged $2,800 for equipment and $6 per reaction for an initial order of 1,000 reactions ($4 for the test, $2 for the collection kit). The initial outlay was $8,800. A subsequent order of 1,000 reactions and a multi-channel pipette brought the total to approximately $15,000 including shipping.

The Bend program was a big success - the EMS manager who administered the program described it as a "godsend."

#### COMB - Combate TV Show Production in Miami, FL
The Combate program was FloodLAMP's only surveillance-screening-as-a-service operation, in which FloodLAMP employees directly performed all testing. An experienced nurse was hired and trained to run the FloodLAMP test. This person administered the program, collected samples, ran testing, and managed an assistant, doing an especially excellent job.

The pop-up lab was established in a carpeted hotel room within the hotel that housed the TV program's staff and participants. This was not an ideal laboratory environment and raised initial contamination concerns. With rigorous cleaning protocols and attention to detail, the program operated for over four months without significant contamination problems.

Testing was individual (no pooling), using 1.5 ml tubes, with approximately 100 people tested per week. The negotiated price was $35 per test all-in with a minimum of 150 tests per week ($5,250 per week). The initially discussed price was significantly higher but was negotiated downward over the months leading up to the program starting. Given staffing costs, including testing staff salaries and a prorated share of FloodLAMP scientist support time, it is likely that FloodLAMP did not recoup its costs on the contract.

##### Comparison with Antigen Tests (AI generated - Opus 4.6)
The testing results were informative for doing a FloodLAMP vs. antigen comparison. The COMB data tells a dramatically different story from DAVI. The key numbers are right in the stats table:
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

All 5 antigen-negative cases were subsequently confirmed by lab-purified PCR. The COMB protocol was systematic: FL first, then antigen; if antigen disagreed, send for lab PCR. That protocol gives us high confidence in these numbers.

**Why so much higher than DAVI?** A few likely factors:

1. **Testing context.** COMB was HCW-collected individual surveillance of a production crew -- likely catching people very early through routine screening before symptoms developed. DAVI had more symptomatic diagnostic testing mixed in (especially Groups 2 and 3, where many employees were already symptomatic at Day 0).

2. **Low positivity rate.** COMB's overall tube positivity was just 0.7% (14 positives out of 1,981 tubes). At low prevalence with routine screening, the cases you do find tend to be earlier in infection with lower viral loads -- exactly where antigen underperforms.

3. **Time period.** COMB ran March--August 2022, a lower-prevalence period compared to DAVI's operation during the Omicron surge. Finding cases during low-prevalence periods often means catching them at the earliest detectable stage.

**Side by side:**

| Site | Same-day comparisons | Antigen + | Antigen - | % Antigen Negative |
|---|---|---|---|---|
| DAVI | 42 | 38 | 4 | 10% |
| COMB | 11 | 6 | 5 | **45.5%** |

The COMB data is a much smaller sample (11 vs. 42), but the signal is strong and directionally consistent with the Coral Springs anecdote (21/22 antigen-negative). Taken together, these suggest that in surveillance contexts catching early/asymptomatic infections, the antigen miss rate can be very high -- far above DAVI's 10%, which was skewed by a large proportion of symptomatic cases who were easier for antigen to detect.

#### NDHM - Needham Beth Shalom School in Needham, MA
The Needham pilot was a small, late-stage program established through a connection via New England BioLabs, and provided free of charge. FloodLAMP's founder traveled to set up the lab and train the tester, a college student studying a bio-related field with some prior hands-on lab experience.

An office room in the school was dedicated to testing. By this point in FloodLAMP's operations, the setup process had matured and was straightforward, using the standardized four-drawer cart configuration. The program also used a recently implemented streamlined web onboarding process.

Participation was limited as prevalence was low in that area and at that point in the pandemic. Over the first four to six weeks, the program processed a few dozen samples per week, tapering off substantially afterward. The total volume was low: 80 tubes covering 130 unique individuals. This occurred during a period of declining case rates, which likely contributed to the drop-off in interest and participation. No positive samples were detected during the program.

#### ABRM - Abrome K-12 School in Austin, TX
Abrome was a small alternative K-12 school in Austin, Texas. The school connected FloodLAMP to the Balvi grant organization and submitted for a Balvi grant that supported their system purchase.

Abrome operated the program for nine months (September 5, 2022 through June 2, 2023), running 1,379 initial tubes covering 2,954 participant results across 87 unique individuals. Testing was pooled by household with an average pool level of 2.2 individuals per tube, processed on-site using a mini-amp heater plus water bath configuration. The program detected eight positive tubes corresponding to three distinct cases, with no false positives or suspected false negatives documented in available follow-up data.

The program's operational consistency was notable: testing was conducted on 95% of weekdays during 36 active school weeks (171 of 180 weekdays, with an effective uptime of 97% adjusting for holidays). This frequency of testing was unusual outside of significantly higher-budget screening programs.

FloodLAMP charged approximately $3,000 for equipment and system, plus $4 to $5 per test kit (reagents, consumables, collection tubes, and swabs). Abrome purchased 3,000 surveillance test kits, bringing the total program cost to approximately $20,000, including roughly $1,500 for in-person training and setup. The testing and administrative lead from the Combate program flew to Texas to set up the lab and conduct in-person training.

The head of Abrome provided a written endorsement stating that the school emerged from 3.5 academic years of the pandemic without a known case of in-school transmission, crediting the FloodLAMP program with catching three instances of household infection before the student became infectious at school.

A documented case from December 2022 illustrates the detection model: a morning LAMP test flagged a positive household pool (two parents and one student), none of whom had symptoms. The student was immediately separated from the school. Within hours, one parent tested positive on rapid PCR; the student developed symptoms and tested positive two days later. No other Abrome students or staff tested positive, suggesting that the rapid detection and quarantine interrupted transmission to the school community.

Abrome's success was supported by conditions that may not be generalizable: a school culture that embraced mandatory daily testing, a small enough community for a single staff member to manage the program, and grant funding covering the full cost. These factors made Abrome a great setting for our final FloodLAMP pilot, but also highlight the financial and participation challenges for such a comprehensive screening program.

#### False Positives and False Negatives
Across all pilot programs, no session-level false positives or false negatives were documented in available follow-up data. These zeros reflect the structure of the surveillance programs rather than a claim of perfect test performance. For false negatives - defined here as a FloodLAMP negative on a day when a referral test for the same individual had a positive referral test (non-FloodLAMP test) — the number is zero primarily because referral testing was almost always triggered by a positive FloodLAMP result, not collected in parallel. Without simultaneous higher-sensitivity comparator samples, false negatives in a screening context are effectively undetectable. Programs screened the same individuals multiple times per week, so a person will always have a preceding negative test before turning positive, but the viral load trajectory from onset of infection is unknown without paired comparator data. Test-to-return testing of known positives never produced a FloodLAMP negative for a known positive case until the tail-end of their infections (at least as far as the data we have). The Stanford clinical evaluation conducted for the FDA EUA submission (see: `regulatory/fl-fda-submissions/2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md`) did measure false negatives under controlled conditions and reported 90% positive agreement (4 of 40 positives missed, all at high Ct values indicating low viral load) with 100% negative agreement, at an established limit of detection of 12,500 copies/mL.

For false positives — defined here as a FloodLAMP session call of positive for a truly negative individual — the number is zero, but with important context. LAMP reactions are inherently prone to false positives at the individual reaction level (due to the nature of isothermal amplification). This necessitated a robust rerun workflow that resolved many reaction-level false positives into negative or inconclusive final session calls (see: `guides/test-site/Resulting Decision Chart v1.2`; `guides/test-site/Resulting Decision Flow Chart (Single Triplicate Re-run) v1.2`). At the session call level, false positives would be identifiable in the surveillance structure because the referral test for a FloodLAMP positive would come back negative, and program administrators would likely have reported such cases to FloodLAMP. For all FloodLAMP positive tubes with available referral data, every referral test was positive, with the caveat that some FloodLAMP positives lack follow-up data. The closest case to a false positive was a "false inconclusive" in the BEND program: of two inconclusive session calls on separate days, one was confirmed positive and the other confirmed negative by referral PCR, though this is technically distinct from a false positive since the session call was inconclusive rather than positive.

In summary, the zeros are consistent with expectations given the program structures but should not be interpreted as evidence of zero false positive or false negative rates as those metrics are normally understood in the testing space. A controlled study with simultaneous comparator testing would be required to establish those rates, and the Stanford clinical evaluation provides the closest available measure of analytical performance under such conditions.

#### Organizational Self-Testing as a Pandemic Necessity
A fundamental argument for decentralized screening emerges from the pilot experience. During the acute phase of a pandemic, infections rise exponentially, and neither centralized testing services, commercial testing companies, nor device manufacturers can scale fast enough to match that growth. The January 2022 Omicron surge produced the worst testing shortage of the entire pandemic despite two years of investment. One way to address these limitations is to enable organizations to use their own staff and their own resources to test their populations, without depending on external testing infrastructure that cannot keep pace with exponential spread. This is what FloodLAMP's pilot sites did: firefighters with no laboratory background ran the test, expanded coverage during the surge, and validated the test's performance against individuals already known to be positive through clinical testing. Organizations running screening programs are inherently positioned to evaluate whether the test is working. Their administrators know who is sick, see whether the screening catches those cases, and are directly accountable for the program's effectiveness. The regulatory framework should support this modality (see `regulatory/surveillance` and the reform proposals in the paper).


# 505  2021-12-28_Case Report - Randy.md
METADATA
last updated: 2026-02-25 BA
file_name: 2021-12-28_Case Report - Randy.md
file_date: 2021-12-28
title: FloodLAMP Case Report - Randy Dec21 Infection
category: pilots
subcategory: pilot-sites
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1ZIbYYZ873RjV6IuUyhZ22wNdFKRv6zz1v5_Gm9VBlwE/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/pilots/pilot-sites/2021-12-28_Case%20Report%20-%20Randy.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 505
words: 292
notes:
summary_short: The "2021-12-28_Case Report - Randy" document is a FloodLAMP case report for FloodLAMP founder Randy True documenting a COVID-19 infection from likely exposure on 2021-12-13 through recovery on 2021-12-28, tracking daily FloodLAMP QuickColor LAMP and BinaxNow antigen test results alongside symptom progression, showing first positive on Day 0 (2021-12-18) and return to negative on Day 9 (2021-12-27).


CONTENT

## Randy Dec21 Infection
| Days after 1st Pos Test | Day Week | Date  | Time    | FloodLAMP QC Test Result | BinaxNow Antigen Test Result | Symptoms / Notes                                                                                                                                                          |
|-------------------------|----------|-------|---------|-------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         | Mon      | 12-13 | 9:00 PM |                         |                              | Likely exposure at big holiday party, honor system test req, mask req but not followed<br/>I masked 80% of time there, 3 others I was with mostly mask off, none infected |
|                         | Tues     | 12-14 | 9:00 AM |                         |                              |                                                                                                                                                                           |
|                         | Thurs    | 12-16 | 9:00 AM | NEG                     |                              | symptoms start at night - bad headache and 4 hrs sleep, foggy brain                                                                                                       |
|                         | Fri      | 12-17 |         | No Test                 |                              | symptoms continue - bad headache and 4 hrs sleep, foggy brain                                                                                                             |
| 0                       | Sat      | 12-18 | 7:00 AM | POS                     | POS - bright 5min            | symptoms continue - headache, fatigue, brain fog (more than usual)                                                                                                        |
| 4                       |          | 12-22 | 6:00 AM | POS nasal, INC saliva   |                              | symptoms continue - headache, fatigue, brain fog (more than usual)                                                                                                        |
| 5                       |          | 12-23 | 9:00 AM | POS                     |                              | symptoms less                                                                                                                                                             |
| 6                       |          | 12-24 | 7:00 AM | POS                     | POS - bright                 | symptoms less                                                                                                                                                             |
| 7                       | Sat      | 12-25 | 8:00 AM | POS                     |                              | symptoms less                                                                                                                                                             |
| 8                       | Sun      | 12-26 | 5:00 AM | POS                     | 2pm POS - dim                | symptoms less                                                                                                                                                             |
| 9                       | Mon      | 12-27 | 5:00 PM | NEG                     |                              | symptoms minimal/gone                                                                                                                                                     |
| 10                      | Tues     | 12-28 | 8:00 AM | NEG                     |                              | symptoms minimal/gone                                                                                                                                                     |
||


# 1,174  2022-01-01_Case Report - New Years Eve.md
METADATA
last updated: 2026-02-25 BA
file_name: 2022-01-01_Case Report - New Years Eve.md
file_date: 2022-01-01
title: FloodLAMP Case Report - New Years Eve
category: pilots
subcategory: pilot-sites
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1hdTOuLxX7SnE7VL9Rdw61PeU-HE4ylli/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/pilots/pilot-sites/2022-01-01_Case%20Report%20-%20New%20Years%20Eve.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1174
words: 679
notes: 
summary_short: The "2022-01-01_Case Report - New Years Eve" document describes a case where FloodLAMP detected an asymptomatic SARS-CoV-2 infection that all antigen and OTC/POC molecular tests missed, tracking 19 tests across 8 different test types (FloodLAMP QuickColor LAMP, FloodLAMP EasyPCR/SalivaDirect, Accula, Lucira, Detect, FlowFlex, CareStart, BinaXNow) from 12-27-21 to 01-02-22, with FloodLAMP returning the first positive on 12-31-21 while same-day antigen and rapid molecular tests were negative.


CONTENT

| Date Collected | Time Collected | Test | Sample Type | CLAMP | Tube Code | Swab ID | Logged? | PCR Ct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12-27-21 | 9:37 AM | Detect | nasal swab | NEG |  |  |  |  |
| 12-29-21 | 7:48 AM | FlowFlex Antigen | nasal swab | NEG |  |  |  |  |
| 12-29-21 | 1:00 PM | FloodLAMP | nasal swab | NEG | MAX398 | JUR |  |  |
| 12-31-21 | 9:00 AM | FloodLAMP | nasal swab | POS | MAX288 | JUR |  | 33.9 |
| 12-31-21 | 2:01 PM | FlowFlex Antigen | nasal swab | NEG |  |  |  |  |
| 12-31-21 | 2:10 PM | Detect | nasal swab | NEG |  |  |  |  |
| 12-31-21 | 4:52 PM | Lucira | nasal swab | NEG |  |  |  |  |
| 12-31-21 | 5:00 PM | FloodLAMP | nasal swab | NEG | MAX340 | JUR |  | 2 Und, 1 39.4 |
| 12-31-21 | 5:00 PM | FloodLAMP | throat swab | POS | MAX347 | JUR |  | 30.2 |
| 12-31-21 | 5:00 PM | BinaXNow Antigen | nasal swab | NEG |  |  |  |  |
| 12-31-21 | 8:00 PM | FloodLAMP | saliva |  | MAX368 |  | logged in form | 27.7 |
| 01-01-22 | 11:00 AM | FloodLAMP | saliva |  | MA4 |  |  | 29.0 |
| 01-01-22 | 10:28 AM | BinaXNow | nasal swab | NEG |  |  |  |  |
| 01-01-22 | 10:33 AM | BinaXNow | throat swab | NEG |  |  |  |  |
| 01-01-22 | 10:45 AM | FloodLAMP | nasal swab | POS | MA63 | JUR |  | 32.2 |
| 01-01-22 | 10:50 AM | FloodLAMP | throat swab | POS | MA92 | JUR |  | 35.5 |
| 01-01-22 | 4:22 PM | Accula (Worksite) | nasal swab | NEG |  |  |  |  |
| 01-02-22 | 10:30 AM | CareStart | nasal swab | POS |  |  |  |  |
| 01-02-22 | 10:30 AM | BinaXNow | nasal swab | POS |  |  |  |  |
||

### FloodLAMP New Years Eve Case Report
caught asymptomatic infection that all antigen and OTC/POC molecular tests missed

![FloodLAMP New Years Eve Case Report](_plots/FLMP_nye_case_report.png)

|  |  |  | |  |  |  |
|---|---|---|---|---|---|---|
| FloodLAMP EasyPCR on saliva | | | | POS - SalivaDirect PCR Ct 27.7, 8 PM | POS - SalivaDirect PCR Ct 27.7, 11 AM | |
| Accula Rapid Molecular PCR (Worksite) | | | | | Accula NEG - nasal swab, 4 PM | |
| Lucira Rapid Molecular LAMP | | | | Lucira NEG - nasal swab, 5 PM | | |
| Detect Rapid Molecular LAMP | NEG - nasal swab, 10 AM |  | Detect NEG - nasal swab, 2 PM | | | |
| CaseStart Antigen | | | | | | |
| FlowFlex Antigen | | NEG - nasal swab, 8 AM | NEG - nasal swab, 2 PM | | | POS - nasal swab, 10 AM |
| BinaxNow Antigen | | | | NEG - nasal swab, 5 PM | NEG - nasal and throat swabs, 10 AM | POS - nasal swab, 10 AM |
| FloodLAMP QuickColor LAMP Nasal Swab | | NEG - nasal swab, 1 PM | | NEG - nasal swab PCR Ct Und/39.4, 5PM | POS - nasal swab PCR Ct 32.2, 10 AM | |
| FloodLAMP QuickColor LAMP Throat Swab | | | POS - nasal swab PCR Ct 33.9, 9 AM | POS - throat swab PCR Ct 30.2, 5 PM | POS - throat swab PCR Ct 35.5, 10 AM | |
|  | 12-27-21 | 12-29-21 | 12-31-21 | 12-31-22 | 1-1-22 | 1-2-22 |
||


# 4,849  2022-01-02_Carillon Case Report of Asymptomatic Positive Family Pool.md
METADATA
last updated: 2026-02-25 BA
file_name: 2022-01-02_Carillon Case Report of Asymptomatic Positive Family Pool.md
file_date: 2022-01-02
title: FloodLAMP Case Report - Carillon Asymptomatic Positive Family Pool
category: pilots
subcategory: pilot-sites
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1eWD8z2MqoZEVoTFPJWcxr7-UsxcyYGklwmAUhEuawbM/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/pilots/pilot-sites/2022-01-02_Carillon%20Case%20Report%20of%20Asymptomatic%20Positive%20Family%20Pool.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 4849
words: 2430
notes: 
summary_short: The "2022-01-02_Carillon Case Report of Asymptomatic Positive Family Pool" documents a family pool (2 parents, 2 children) where FloodLAMP detected an asymptomatic SARS-CoV-2 infection on 2022-01-02 through pooled household testing while same-day BinaxNow antigen tests were negative for both parents. Individual FloodLAMP follow-up confirmed both parents positive on 01-03, and children developed symptoms and tested positive by home antigen on 01-04, followed by confirmatory PCR lab tests for all family members. The family remained FloodLAMP-positive through 01-17.


CONTENT

## Example Data
### FLOODLAMP DATA with EXTRA COLUMNS ADDED
| TUBE ID | SPONSOR  | PARTICIPANT | MINOR | NOTE | RESULT   | COLLECTION DATE | COLLECTION TIME | RESULT DATE | TEST TYPE | TEST MODEL   | SYMPTOMS | POOLED | TAT     | NOTES |
|---------|----------|-------------|-------|------|----------|-----------------|-----------------|-------------|-----------|--------------|----------|--------|---------|-------|
| FLT1134 | Jane Doe | Kid1 Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLY1134 | Jane Doe | Kid1 Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLT1134 | Jane Doe | Kid2 Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLY1134 | Jane Doe | Kid2 Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLT1134 | Jane Doe | John Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLY1134 | Jane Doe | John Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLT1134 | Jane Doe | Jane Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLY1134 | Jane Doe | Jane Doe    |       |      | Negative | 11/28/2021      |                 | 11/28/2021  | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLE484  | Jane Doe | Kid1 Doe    |       |      | Negative | 12/6/2021       |                 | 12/7/2021   | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLE484  | Jane Doe | Kid2 Doe    |       |      | Negative | 12/6/2021       |                 | 12/7/2021   | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLE484  | Jane Doe | John Doe    |       |      | Negative | 12/6/2021       |                 | 12/7/2021   | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLE484  | Jane Doe | Jane Doe    |       |      | Negative | 12/6/2021       |                 | 12/7/2021   | Molecular | FloodLAMP QC |          | 1      |         |       |
| FLT1433 | Jane Doe | Kid1 Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |          | 1      | 2 hours |       |
| FLT1433 | Jane Doe | Kid2 Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |          | 1      | 2 hours |       |
| FLT1433 | Jane Doe | John Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |          | 1      | 2 hours |       |
| FLT1433 | Jane Doe | Jane Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |          | 1      | 2 hours |       |
| FLT1570 | Jane Doe | Kid1 Doe    |       |      | Negative | 1/3/2022        |                 | 1/3/2022    | Molecular | FloodLAMP QC |          | 0      | 1 hour  |       |
| FLT14   | Jane Doe | Kid2 Doe    |       |      | Negative | 1/3/2022        |                 | 1/3/2022    | Molecular | FloodLAMP QC |          | 0      | 1 hour  |       |
| FLT1128 | Jane Doe | John Doe    |       |      | Positive | 1/3/2022        |                 | 1/3/2022    | Molecular | FloodLAMP QC |          | 0      | 1 hour  |       |
| FLE810  | Jane Doe | Kid1 Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |          | 0      | 2 hours |       |
| FLE885  | Jane Doe | Kid2 Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |          | 0      | 2 hours |       |
| FLE895  | Jane Doe | John Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |          | 0      | 2 hours |       |
| FLE812  | Jane Doe | Jane Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |          | 0      | 2 hours |       |
| FLB7156 | Jane Doe | Kid1 Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |          | 1      | 3 hours |       |
| FLB7156 | Jane Doe | Jane Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |          | 1      | 3 hours |       |
| FLB7156 | Jane Doe | Kid2 Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |          | 1      | 3 hours |       |
| FLB7156 | Jane Doe | John Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |          | 1      | 3 hours |
||

### NON FLOODLAMP TEST DATA (can be from before or after FloodLAMP test)
| PARTICIPANT | MINOR | NOTE | RESULT   | COLLECTION DATE | COLLECTION TIME | RESULT DATE | TEST TYPE | TEST MODEL | SYMPTOMS | POOLED | TAT       | NOTES                   |
|-------------|-------|------|----------|-----------------|-----------------|-------------|-----------|------------|----------|--------|-----------|-------------------------|
| John Doe    |       |      | Negative | 1/2/2022        |                 | 1/2/2022    | Antigen   | BinaXNow   | Asym     | 0      | immediate | evening after referral  |
| Jane Doe    |       |      | Negative | 1/2/2022        |                 | 1/2/2022    | Antigen   | BinaXNow   | Asym     | 0      | immediate | evening after referral  |
| John Doe    |       |      | Positive | 1/3/2022        |                 | 1/4/2022    | Molecular | PCR Lab    |          | 0      | 1 day     |                         |
| Kid2 Doe    |       |      | Positive | 1/4/2022        |                 | 1/4/2022    | Antigen   | Unknown    | Sympt    | 0      | immediate |                         |
| Kid1 Doe    |       |      | Positive | 1/4/2022        |                 | 1/4/2022    | Antigen   | Unknown    | Sympt    | 0      | immediate |                         |
| Jane Doe    |       |      | Positive | 1/4/2022        |                 | 1/7/2022    | Molecular | PCR Lab    |          | 0      | 3 days    |                         |
| Kid2 Doe    |       |      | Positive | 1/6/2022        |                 | 1/7/2022    | Molecular | PCR Lab    |          | 0      | 1 day     |                         |
| Kid1 Doe    |       |      | Positive | 1/7/2022        |                 | 1/8/2022    | Molecular | PCR Lab    |          | 0      | 1 day     |                         |
| Kid2 Doe    |       |      | Positive | 1/13/2022       |                 | 1/13/2022   | Antigen   | Unknown    |          | 0      | immediate | slight second line      |
| John Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown    |          | 0      | immediate |                         |
| Jane Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown    |          | 0      | immediate |                         |
| Kid2 Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown    |          | 0      | immediate |                         |
| Kid1 Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown    |          | 0      | immediate |
||

### COMBINED TEST DATA
| PARTICIPANT | MINOR | NOTE | RESULT   | COLLECTION DATE | COLLECTION TIME | RESULT DATE | TEST TYPE | TEST MODEL   |  | POOLED | TAT       | NOTES                   |  | DAY SP |
|-------------|-------|------|----------|-----------------|-----------------|-------------|-----------|--------------|--|--------|-----------|-------------------------|--|--------|
| Kid1 Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |  | 1      | 2 hours   |                         |  | 0      |
| Kid2 Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |  | 1      | 2 hours   |                         |  | 0      |
| John Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |  | 1      | 2 hours   |                         |  | 0      |
| John Doe    |       |      | Negative | 1/2/2022        |                 | 1/2/2022    | Antigen   | BinaXNow     |  | 0      | immediate | evening after referral  |  | 0      |
| Jane Doe    |       |      | Positive | 1/2/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |  | 1      | 2 hours   |                         |  | 0      |
| Jane Doe    |       |      | Negative | 1/2/2022        |                 | 1/2/2022    | Antigen   | BinaXNow     |  | 0      | immediate | evening after referral  |  | 0      |
| Kid1 Doe    |       |      | Negative | 1/3/2022        |                 | 1/2/2022    | Molecular | FloodLAMP QC |  | 0      | 1 hour    |                         |  | 1      |
| Kid2 Doe    |       |      | Negative | 1/3/2022        |                 | 1/3/2022    | Molecular | FloodLAMP QC |  | 0      | 1 hour    |                         |  | 1      |
| John Doe    |       |      | Positive | 1/3/2022        |                 | 1/3/2022    | Molecular | FloodLAMP QC |  | 0      | 1 hour    |                         |  | 1      |
| John Doe    |       |      | Positive | 1/3/2022        |                 | 1/4/2022    | Molecular | PCR Lab      |  | 0      | 1 day     |                         |  | 1      |
| Jane Doe    |       |      | Positive | 1/4/2022        |                 | 1/7/2022    | Molecular | PCR Lab      |  | 0      | 3 days    |                         |  | 2      |
| Kid2 Doe    |       |      | Positive | 1/4/2022        |                 | 1/4/2022    | Antigen   | Unknown      |  | 0      | immediate |                         |  | 2      |
| Kid1 Doe    |       |      | Positive | 1/4/2022        |                 | 1/4/2022    | Antigen   | Unknown      |  | 0      | immediate |                         |  | 2      |
| Kid2 Doe    |       |      | Positive | 1/6/2022        |                 | 1/7/2022    | Molecular | PCR Lab      |  | 0      | 1 day     |                         |  | 4      |
| Kid1 Doe    |       |      | Positive | 1/7/2022        |                 | 1/8/2022    | Molecular | PCR Lab      |  | 0      | 1 day     |                         |  | 5      |
| Kid1 Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |  | 0      | 2 hours   |                         |  | 7      |
| Kid2 Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |  | 0      | 2 hours   |                         |  | 7      |
| John Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |  | 0      | 2 hours   |                         |  | 7      |
| Jane Doe    |       |      | Positive | 1/9/2022        |                 | 1/10/2022   | Molecular | FloodLAMP QC |  | 0      | 2 hours   |                         |  | 7      |
| Kid2 Doe    |       |      | Positive | 1/13/2022       |                 | 1/13/2022   | Antigen   | Unknown      |  | 0      | immediate | slight second line      |  | 11     |
| Kid1 Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown      |  | 0      | immediate |                         |  | 12     |
| Kid2 Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown      |  | 0      | immediate |                         |  | 12     |
| John Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown      |  | 0      | immediate |                         |  | 12     |
| Jane Doe    |       |      | Negative | 1/14/2022       |                 | 1/14/2022   | Antigen   | Unknown      |  | 0      | immediate |                         |  | 12     |
| Kid1 Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |  | 1      | 3 hours   |                         |  | 15     |
| Kid2 Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |  | 1      | 3 hours   |                         |  | 15     |
| John Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |  | 1      | 3 hours   |                         |  | 15     |
| Jane Doe    |       |      | Positive | 1/17/2022       |                 | 1/17/2022   | Molecular | FloodLAMP QC |  | 1      | 3 hours   |                         |  | 15     |
||

### TABLE VIEW for FAMILY
![Carillon Case Report](_plots/FLMP_carillon_case_report.png)

| | | 1/2/2022 (0) | 1/3/2022 (1) | 1/4/2022 (2) | 1/6/2022 (4) | 1/7/2022 (5) | 1/8/2022 (6) | 1/9/2022 (7) | 1/10/2022 (8) | 1/13/2022 (11) | 1/14/2022 (12) | 1/17/2022 (15) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | Family Pool | POS FloodLAMP | | | | | | | | | | POS FloodLAMP |
| Jane Doe | Parent 1 | Asymptomatic<br>POS FloodLAMP (Family Pool)<br>NEG Antigen | POS FloodLAMP (Indiv) | POS PCR Lab > | > > > > > | > POS PCR Result | | POS FloodLAMP (Indiv) | > POS FL Result | | NEG Antigen | POS FloodLAMP (Family Pool) |
| John Doe | Parent 2 | Asymptomatic<br>POS FloodLAMP (Family Pool)<br>NEG Antigen | POS FloodLAMP<br>POS PCR Lab > | Symptoms<br>> POS PCR Result | | | | POS FloodLAMP (Indiv) | > POS FL Result | | NEG Antigen | POS FloodLAMP (Family Pool) |
| Kid1 Doe | Child 1 | Asymptomatic<br>POS FloodLAMP (Family Pool) | NEG FloodLAMP | Symptoms<br>POS Antigen | Asymptomatic | POS PCR Lab > | > POS PCR Result | POS FloodLAMP (Indiv) | > POS FL Result | | NEG Antigen | POS FloodLAMP (Family Pool) |
| Kid2 Doe | Child 2 | Asymptomatic<br>POS FloodLAMP (Family Pool) | NEG FloodLAMP | Symptoms<br>POS Antigen | Asymptomatic<br>POS PCR Lab > | | > POS PCR Result | POS FloodLAMP (Indiv) | > POS FL Result | POS Antigen (slight) | NEG Antigen | POS FloodLAMP (Family Pool) |
||

### CALENDAR INFO from PEOPLE
**Jan 2nd**
- FloodLAMP pool samples – Positive result as a household
- Abbott BinaxNow Home antigen test – John & Jane, Negative result

**Jan 3rd**
- FloodLAMP individual samples provided – John & Jane positive, Kid2 Kid1 negative
- John PCR test taken

**Jan 4th**
- Jane PCR test taken
- John PCR test results – Positive
- Kid2 & Kid1 home antigen test taken – Positive

**Jan 6th**
- Kid2 PCR test taken

**Jan 7th**
- Kid1 PCR test taken
- Kid2 PCR results – Positive
- Jane PCR results – Positive

**Jan 8th**
- Kid1 PCR results – Positive

**Jan 13th**
- Kid2 home antigen test – Mostly negative with a slight second line

**Jan 14th**
- John, Kid2, Kid1, Jane home antigen test – Negative (no slight second line)

**Jan 17th**
- FloodLAMP pool samples dropped off – still detected positive as a household
