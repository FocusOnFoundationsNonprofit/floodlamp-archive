METADATA
last updated: 2026-01-25
file_name: COMB_pilot-data_summary.md
file_date: 2022-08-15
title: COMB Pilot Data Summary
category: pilots
subcategory: pilot-data
tags: 
source_file_type: csv
xfile_type: xlsx
gfile_url: NA
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/pilots/pilot-data/COMB_xlsx_downloads
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 2888
tokens: 4813
notes: 
summary_short: Combate (COMB) was a martial arts production organization in Miami, FL where FloodLAMP staff provided individual HCW-collected testing of martial artists and production staff, with test processing done in a hotel room using a standard equipment configuration. The program ran over 5 months (2022-03-20 to 2022-08-15), testing 1,981 tubes from 1,672 participants with 14 positive tubes detected.


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
- [COMB_APS_deID_PUB](https://docs.google.com/spreadsheets/d/1LFbt-1PJ6c9qoDfwMx2pw9f39i21yZvpYWuzSxg0nhk/edit?usp=drive_link)
- [COMB_RFR_deID_PUB](https://docs.google.com/spreadsheets/d/1P_FWpqIBJV0FqluwOZMjMumc6wynKbdR-70WJR03DZc/edit?usp=sharing)
- [COMB_RTR_deID_PUB](https://docs.google.com/spreadsheets/d/1ODszJJPOKDcEBwA3MiMwAH98TVB65cpz6lqisSF1Uqo/edit?usp=drive_link)

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
| COMB185924 | 2 | 0 | not found | not found | not found | 2022-08-08 | Negative | Antigen | Negative |  |  |  |  | 0 | Referral Confirmed FL Positive |
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
