METADATA
last updated: 2026-01-25
file_name: BEND_pilot-data_summary.md
file_date: 2022-05-11
title: BEND Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/pilots/pilot-data/BEND_xlsx_downloads
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2292
tokens: 3680
notes: 
summary_short: Bend Fire and Rescue (BEND) was a fire department/EMS program in Bend, OR that used FloodLAMP for individual (non-pooled) testing of first responders and staff, with HCW-collected samples processed on-site using a double mini configuration. The program ran over 5 months (2021-12-10 to 2022-05-11), testing 772 tubes with 71 positive tubes detected — a 9.2% positivity rate that captured the Omicron wave.


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
- [BEND_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1ff9LyHzhq3Mka_W5dEm7cyYWW7cZmOZxW9bUFWjuqIQ/edit?usp=drive_link)
- [BEND_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/1lkoZ0Og6KAdMPD6eBgW3tcs8v4dg6l9-Hjnp8Do__Rg/edit?usp=drive_link)

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
