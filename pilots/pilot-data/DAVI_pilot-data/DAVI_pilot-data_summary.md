METADATA
last updated: 2026-01-25
file_name: DAVI_pilot-data_summary.md
file_date: 2022-03-18
title: DAVI Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: **FLAGGED - TO BE INSERTED**
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/pilots/pilot-data/DAVI_xlsx_downloads
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2539
tokens: 4082
notes: 
summary_short: Davie Fire and Rescue (DAVI) was a city/EMS program in Davie, FL where fire department staff operated FloodLAMP for pooled self-collection testing of EMS, first responders, and city staff at their fire station, using a standard configuration without the FloodLAMP mobile app. The program ran over 6 months (2021-09-01 to 2022-03-18), testing 2,279 tubes from 4,409 participant results with 384 positive tubes detected (16.8% positivity rate during the Delta and Omicron waves). All sample processing for the ROSA production pilot program was performed at the Davie site by the Davie staff.


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
- [DAVI_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/1gIvvt-IHhGwbIv_mVSF5QEfjbm5WdoSUDe4MW8SSCcA/edit?usp=drive_link)
- [DAVI_RSR_deID_PUB](https://docs.google.com/spreadsheets/d/1QslpxtCjyHeau4SIHuLbkjLaLtB7tNrK3jQh96s3bIo/edit?usp=drive_link)

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
