# Task Spec — APS / Pos and Incl → curated CSV

## Inputs
- `input_xlsx_path`: `{{APS_XLSX_PATH}}` (example: `ABRM_APS_deID_PUB.xlsx`)
- Sheet: `Pos and Incl`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_APS_pos-incl-cases.csv`

## Row filter
- Keep only rows where `TUBE ID` is not null/empty.

## Drop columns (explicit)
- SPONSOR FIRSTNAME
- SPONSOR LASTNAME
- NOTE
- Match Row in APS Data PHI - postDEL
- 0 Check
(If any of these don’t exist in a site, ignore gracefully.)

## Keep + rename (exact output schema)
IDs & timing
- TUBE ID -> tube_id
- COLLECTION DATE -> collection_date
- COLLECTION TIME -> collection_time
- SPONSOR PERSON ID -> sponsor_id
- RESULT DATE -> result_date
- RESULT TIME -> result_time

Results & corrections
- APP\nRESULT -> app_result
- FINAL RESULT -> final_result
- Result Correct Code -> result_correct_code
- Correction Notes -> correction_notes

Pooling + membership
- NUM SAMPLES (Pool Level) -> pool_level_n
- Sample Person1 -> sample_person1
- Sample Person2 -> sample_person2
- Sample Person3 -> sample_person3
- Sample Person4 -> sample_person4

Case linkage
- Case Culster ID -> case_cluster_id  (fix spelling in output)
- Index Tube - First FL Pos/Incl of Case? -> index_tube_first_case_flag

Follow-up linkage/outcomes
- Referral Test Result -> referral_test_result
- Referral Notes -> referral_notes
- 3 ACCOUNTED FOR IN RTR? -> accounted_for_in_rtr_flag
- Re-test? -> retest_flag
- Pool Deconvolution Indiv Test? -> pool_deconvolution_indiv_test_flag
- Correspondence but no Referral Test -> correspondence_no_referral_flag
- Agreement with Referral or Correspondence? -> agreement_with_ref_or_correspondence_flag
- Known Positive (not Re-test)? -> known_positive_not_retest_flag
- FloodLAMP Result Eval -> floodlamp_result_eval

## Normalization
- Header matching must handle embedded newlines.
- Dates -> `YYYY-MM-DD`
- Times -> `HH:MM:SS`
- Prefer flags as 0/1 if already numeric; don’t invent values.

## Output column order
Use the rename list order above.

## Sort order
- collection_date, collection_time, tube_id

## QA prints
- Output row count and unique tube_id count
- `final_result` value_counts
