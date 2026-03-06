# Task Spec — RFR / ALL Tube Results → curated CSV

## Inputs
- `input_xlsx_path`: `{{RFR_XLSX_PATH}}` (example: `ABRM_RFR_deID_PUB.xlsx`)
- Sheet: `ALL Tube Results`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_RFR_all-tube-results.csv`

## Transformations
1) Read sheet as a table (pandas `read_excel` is OK).
2) Normalize headers (newlines → spaces; trim).
3) Rename to stable schema (exact):
   - TUBE ID -> tube_id
   - FINAL ASSIGNED RUN ID -> final_assigned_run_id
   - RUN DATE -> run_date
   - COLLECTION DATE -> collection_date
   - COLLECTION TIME -> collection_time
   - FINAL RESULT -> final_result
   - NUM SAMPLES (Pool Level) -> pool_level_n
4) Normalize dates/times:
   - run_date, collection_date -> `YYYY-MM-DD`
   - collection_time -> `HH:MM:SS`
5) Filter rows:
   - Keep rows where tube_id is not null/empty.

## Output column order (exact)
- tube_id
- final_assigned_run_id
- run_date
- collection_date
- collection_time
- final_result
- pool_level_n

## Sort order
- run_date, final_assigned_run_id, tube_id

## QA prints
- Row count
- unique tube_id count
- unique final_assigned_run_id count
- final_result value_counts
