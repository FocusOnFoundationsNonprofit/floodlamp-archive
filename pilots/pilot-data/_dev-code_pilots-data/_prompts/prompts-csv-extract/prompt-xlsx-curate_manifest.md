# Task Spec — Build per-site curated CSV manifest

## Goal
Generate `{{SITE_CODE}}_csv-manifest.csv` listing all curated CSV outputs for a site, with schemas/keys/notes.

## Inputs
- `site_code`: `{{SITE_CODE}}` (example: ABRM)
- `output_folder_path`: `{{OUTPUT_DIR}}` (folder containing curated CSVs OR intended destination)
- The list of curated outputs is fixed for now (APS/RFR/RTR set below)

## Output
- `{{SITE_CODE}}_csv-manifest.csv`

## Manifest schema (exact column order)
- site_code
- source_workbook
- source_tab
- output_csv
- data_level
- primary_key
- join_keys
- row_grain
- notes

## Rows to emit (template)
Emit one row per curated CSV output with the following mappings:

APS
- `{{SITE_CODE}}_APS_stats_key-values.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `Stats`
  - data_level: `stats`
  - primary_key: blank
  - join_keys: blank
  - row_grain: one row per metric
  - notes: tidy key/value extraction from Stats A–D, sectioned by headers

- `{{SITE_CODE}}_APS_stats_referral-agreement.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `Stats`
  - data_level: `stats`
  - row_grain: one row per FL result category (Positive/Inconclusive)
  - notes: mini-table extracted from Stats E–L anchored by “Number of Tubes with FL Result”

- `{{SITE_CODE}}_APS_weekly-summary.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `REF Weekly`
  - data_level: weekly_rollup
  - join_keys: week_start_date;week_end_date
  - row_grain: one row per week

- `{{SITE_CODE}}_APS_pos-incl-cases.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `Pos and Incl`
  - data_level: tube
  - join_keys: tube_id;case_cluster_id
  - row_grain: one row per tube (pos/incl)

- `{{SITE_CODE}}_APS_swabs-in-tubes.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `postDEL`
  - data_level: participant_result
  - row_grain: one row per swab-in-tube row

- `{{SITE_CODE}}_APS_tubes.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `APS Tubes`
  - data_level: tube
  - primary_key: tube_id
  - join_keys: tube_id
  - row_grain: one row per tube

- `{{SITE_CODE}}_APS_daily-tubes-rollup.csv`
  - source_workbook: `{{SITE_CODE}}_APS_deID_PUB.xlsx`
  - source_tab: `APS Tubes by Date`
  - data_level: daily_rollup
  - primary_key: collect_date
  - join_keys: collect_date
  - row_grain: one row per collection date

RFR
- `{{SITE_CODE}}_RFR_all-tube-results.csv`
  - source_workbook: `{{SITE_CODE}}_RFR_deID_PUB.xlsx`
  - source_tab: `ALL Tube Results`
  - data_level: tube
  - primary_key: tube_id
  - join_keys: tube_id;final_assigned_run_id
  - row_grain: one row per tube

- `{{SITE_CODE}}_RFR_weekly-summary.csv`
  - source_workbook: `{{SITE_CODE}}_RFR_deID_PUB.xlsx`
  - source_tab: `Weekly`
  - data_level: weekly_rollup
  - join_keys: week_start_date;week_end_date
  - row_grain: one row per week

RTR
- `{{SITE_CODE}}_RTR_referral-tests.csv`
  - source_workbook: `{{SITE_CODE}}_RTR_deID_PUB.xlsx`
  - source_tab: `Referral Test Data`
  - data_level: referral
  - primary_key: referral_test_id
  - join_keys: participant_id;case_cluster_id;init_fl_pos_tube_id
  - row_grain: one row per referral test

- `{{SITE_CODE}}_RTR_referral-tests-by-person.csv`
  - source_workbook: `{{SITE_CODE}}_RTR_deID_PUB.xlsx`
  - source_tab: `Referral Tests by Person`
  - data_level: referral
  - primary_key: participant_id
  - join_keys: participant_id
  - row_grain: one row per participant

## Implementation notes
- This module does NOT need to read XLSX. It can simply write a manifest from the known mapping above.
- Still follow Cursor rules (docstrings, mrun stub, QA prints).
- QA prints: print the number of rows written and the output path.