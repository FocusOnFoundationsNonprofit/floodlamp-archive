# Task Spec — APS / APS Tubes → curated CSV

## Inputs
- `input_xlsx_path`: `{{APS_XLSX_PATH}}` (example: `ABRM_APS_deID_PUB.xlsx`)
- Sheet: `APS Tubes`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_APS_tubes.csv`

## Row filter
- Keep rows where `TUBE ID` is not null/empty.

## Drop columns (ignore if absent)
- SPONSOR FIRSTNAME
- SPONSOR LASTNAME
- NOTE
- Match Row in APS Data PHI - postDEL
- First Row of Collection Date
- Result Date Minus Collect Date

## Keep + rename (exact output schema)
- TUBE ID -> tube_id
- COLLECTION DATE -> collection_date
- COLLECTION TIME -> collection_time
- SPONSOR PERSON ID -> sponsor_id
- NUM SAMPLES (Pool Level) -> pool_level_n
- APP\nRESULT -> app_result
- FINAL RESULT -> final_result
- RESULT DATE -> result_date
- RESULT TIME -> result_time
- Result Correct Code -> result_correct_code
- Correction Notes -> correction_notes

## Normalization
- Dates -> `YYYY-MM-DD`
- Times -> `HH:MM:SS`

## Output column order
Use the rename list order above.

## Sort order
- collection_date, collection_time, tube_id

## QA prints
- Row count; unique tube_id count
- pool_level_n min/mean/max
- final_result value_counts
