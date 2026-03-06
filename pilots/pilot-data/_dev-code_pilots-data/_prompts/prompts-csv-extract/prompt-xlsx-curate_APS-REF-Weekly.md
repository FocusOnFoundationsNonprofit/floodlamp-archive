# Task Spec — APS / REF Weekly → curated CSV

## Inputs
- `input_xlsx_path`: `{{APS_XLSX_PATH}}` (example: `ABRM_APS_deID_PUB.xlsx`)
- Sheet: `REF Weekly`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_APS_weekly-summary.csv`

## Source sheet notes
- Weekly time series table with headers that may include embedded totals, e.g.:
  - `Weekly Participants 2954`
  - `Weekly Tubes 1379`
  - `Weekly Positive Tubes 9`
  - `Weekly Inconclusive Tubes 3`

## Transformations
1) Read as a table (pandas `read_excel` is OK).
2) Drop rows where `Week Start Date` is null.
3) Normalize headers:
   - Replace newlines with spaces, trim
   - Remove embedded totals from header strings so schema is stable across sites.
4) Rename columns to EXACT stable schema:
   - Week Start Date -> week_start_date
   - Week End Date -> week_end_date
   - Weekly Participants <anything> -> participants_n
   - Weekly Tubes <anything> -> tubes_n
   - Weekly Positive Tubes <anything> -> positive_tubes_n
   - Weekly Inconclusive Tubes <anything> -> inconclusive_tubes_n
   - % Positive -> pct_positive
   Use robust matching (startswith/regex) to handle varying totals.
5) Normalize dates:
   - week_start_date, week_end_date -> `YYYY-MM-DD`
6) pct_positive:
   - Ensure float
   - If missing AND tubes_n > 0: compute `positive_tubes_n / tubes_n`
   - If tubes_n == 0: leave NaN
7) Count columns should be int where feasible.

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
- min/max week_start_date
- sums of participants_n, tubes_n, positive_tubes_n, inconclusive_tubes_n
- how many pct_positive values were computed vs sourced (if easy)
