# Task Spec — APS / postDEL → curated CSV

## Inputs
- `input_xlsx_path`: `{{APS_XLSX_PATH}}` (example: `ABRM_APS_deID_PUB.xlsx`)
- Sheet: `postDEL`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_APS_swabs-in-tubes.csv`

## Row filters
- Keep rows where `TUBE ID` is not null/empty.
- Keep rows where `Participant ID` is not null/empty (log drops if any).

## Drop columns
Drop all conceptually PII fields (even if blank) and internal QA/pipeline scaffolding. Explicitly drop (ignore if absent):
- SPONSOR FIRSTNAME, SPONSOR LASTNAME
- PARTICIPANT FIRSTNAME, PARTICIPANT LASTNAME, PARTICIPANT EMAIL
- MINOR FIRSTNAME, MINOR LASTNAME
- Sponsor FullName and any combined participant name columns
- Status / QA / delete scaffolding columns such as:
  STATUS, Tube ID First Row?, Num Tube IDs, Add N Names,
  NOTE FIRSTNAME/LASTNAME, Names Adjust, Note Name?,
  >4 Samples, Has Note?, Preserve Note, Initial Order,
  Added from APT?, Minutes Col to Result,
  ERROR!!..., Delete?, Delete Code,
  PARTCIP NAME COLS, MINOR NAME COLS, NOTE NAME COLS,
  Note Name Extras..., END, and any numeric header like `0`.

## Keep + rename (exact output schema)
- TUBE ID -> tube_id
- Participant ID -> participant_id
- Sponsor ID -> sponsor_id
- COLLECTION DATE -> collection_date
- COLLECTION TIME -> collection_time
- RESULT DATE -> result_date
- RESULT TIME -> result_time
- APP\nRESULT -> app_result
- FINAL RESULT -> final_result
- APP\nGROUP -> app_group
- FINAL\nGROUP -> final_group
- Basic Correct Code -> basic_correct_code
- Result Correct Code -> result_correct_code
- Correction Notes -> correction_notes

## Normalization
- Dates -> `YYYY-MM-DD`
- Times -> `HH:MM:SS`
- Strip whitespace from IDs

## Output column order (exact)
- tube_id
- participant_id
- sponsor_id
- collection_date
- collection_time
- result_date
- result_time
- app_result
- final_result
- app_group
- final_group
- basic_correct_code
- result_correct_code
- correction_notes

## Sort order
- collection_date, collection_time, tube_id, participant_id

## QA prints
- Row count; unique tube_id; unique participant_id
- app_result value_counts; final_result value_counts