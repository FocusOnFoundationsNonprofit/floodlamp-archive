# Task Spec — APS / APS Tubes by Date → curated CSV (left table only)

## Inputs
- `input_xlsx_path`: `{{APS_XLSX_PATH}}` (example: `ABRM_APS_deID_PUB.xlsx`)
- Sheet: `APS Tubes by Date`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_APS_daily-tubes-rollup.csv`

## Source sheet structure
This sheet contains multiple horizontally-packed tables and QA checks.
Export ONLY the LEFTMOST rollup table in columns A..I.

## Extraction logic
- Read with `header=None`.
- Slice columns A..I (0..8).
- Use first row of the slice as header.
- Drop rows where the first column (collect date) is null.

## Header normalization
- Replace newlines with spaces; trim.
- Remove embedded totals, e.g. `NUM TUBES 1357` → `NUM TUBES`.

## Rename to stable output columns (exact)
- APS COLLECT DATE -> collect_date
- NUM TUBES -> tubes_n
- NEG -> neg_n
- POS -> pos_n
- INC -> inc_n
- NULL -> null_n
- INVL -> invl_n
- FAIL -> fail_n
- SUM RESULTS -> sum_results_n

## Normalization
- collect_date -> `YYYY-MM-DD`
- count columns -> ints where feasible

## Output column order (exact)
- collect_date
- tubes_n
- neg_n
- pos_n
- inc_n
- null_n
- invl_n
- fail_n
- sum_results_n

## Sort order
- collect_date

## QA prints
- Row count; min/max collect_date
- Sums of each count column
- Optional check: tubes_n == sum_results_n rowwise (log any mismatches)
