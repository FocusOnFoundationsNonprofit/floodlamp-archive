METADATA
last updated: 2026-01-25
file_name: KENT_pilot-data_summary.md
file_date: 2021-07-29
title: KENT Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/pilots/pilot-data/KENT_xlsx_downloads
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 1929
tokens: 2748
notes: 
summary_short: Kent (KENT) was a youth camp testing program at Camp Kenmont in Kent, CT, where volunteers and camp staff operated FloodLAMP for pooled HCW-collected testing of young adult campers and staff, brought up remotely, and using the FloodLAMP mobile app. The 1-month summer program (2021-06-28 to 2021-07-29) tested 190 tubes from 696 participant results (avg pool size 3.7) with 2 positive tubes detected.


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
- [KENT_STS_PUB](https://docs.google.com/spreadsheets/d/1J1Gqc0KAQX_xxiSJ5MR8DVjGzFSfDR-ckCKRNDYmDNQ/edit?usp=drive_link)

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
