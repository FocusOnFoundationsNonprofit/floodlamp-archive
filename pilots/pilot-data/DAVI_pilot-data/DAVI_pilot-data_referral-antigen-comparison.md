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
gfile_url: NA
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/pilots/pilot-data/DAVI_xlsx_downloads
pdf_gdrive_url: NA
pdf_github_url: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
words: 4754
tokens: 8120
notes: DAVI has a custom referral-antigen-comparison format instead of standard referral tests.
summary_short: Site DAVI FloodLAMP pilot data summary with referral antigen comparison.


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
