# Task Spec — RFR / Weekly → curated CSV

## Inputs
- `input_xlsx_path`: `{{RFR_XLSX_PATH}}` (example: `ABRM_RFR_deID_PUB.xlsx`)
- Sheet: `Weekly`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_RFR_weekly-summary.csv`

## Source sheet notes
- Similar to APS weekly but may include extra columns like `Unnamed: 7`, `Unnamed: 8` → drop them.
- Weekly tubes header may be `Weekly Tubes Run <total>` (normalize to tubes_n).
- Headers may include embedded totals → strip totals.

## Transformations
1) Read as a table.
2) Drop columns with headers starting with `Unnamed:` or entirely empty.
3) Drop rows where `Week Start Date` is null.
4) Normalize headers (newlines → spaces; trim; strip embedded totals).
5) Rename to stable schema (exact; same as APS weekly):
   - Week Start Date -> week_start_date
   - Week End Date -> week_end_date
   - Weekly Participants <anything> -> participants_n
   - Weekly Tubes <anything> OR Weekly Tubes Run <anything> -> tubes_n
   - Weekly Positive Tubes <anything> -> positive_tubes_n
   - Weekly Inconclusive Tubes <anything> -> inconclusive_tubes_n
   - % Positive -> pct_positive
6) Normalize dates (ISO).
7) pct_positive: ensure float; compute if missing and tubes_n > 0.

## Output column order (exact)
- week_start_date
- week_end_date
- participants_n
- tubes_n
- positive_tubes_n
- inconclusive_tubes_n
- pct_positive

## Sort order
- week_start_date

## QA prints
- Row count
- sums of participants_n, tubes_n, positive_tubes_n, inconclusive_tubes_n
