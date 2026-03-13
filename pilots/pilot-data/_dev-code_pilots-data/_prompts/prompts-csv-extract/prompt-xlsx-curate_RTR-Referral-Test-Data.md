# Task Spec — RTR / Referral Test Data → curated CSV

## Inputs
- `input_xlsx_path`: `{{RTR_XLSX_PATH}}` (example: `ABRM_RTR_deID_PUB.xlsx`)
- Sheet: `Referral Test Data`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_RTR_referral-tests.csv`

## Row filter
- Keep rows where `REFERRAL TEST ID` is not null/empty.

## Drop columns (ignore if absent)
Internal matching helpers + PII:
- Num Rows with Same Name in ALL Pos and Incl IMPORT?
- Num Rows with Same Name in APS Person?
- Num Rows with Same Name in Referall Tests?
- PARTICIPANT FIRSTNAME
- PARTICIPANT LASTNAME
- PARTICIPANT FULLNAME
- NOTES (drop by default)

## Keep + rename (exact output schema)
Core linkage
- CASE CLUSTER ID -> case_cluster_id
- REFERRAL TEST ID -> referral_test_id
- PARTICIPANT ID -> participant_id

Referral test details
- REFERRAL TEST COLLECTION DATE -> referral_test_collection_date
- REFERRAL TEST COLLECTION TIME -> referral_test_collection_time
- REFERRAL TEST RESULT DATE -> referral_test_result_date
- REFERRAL TEST RESULT TIME -> referral_test_result_time
- REFERRAL TEST TYPE -> referral_test_type
- REFERRAL TEST MODEL -> referral_test_model
- REFERRAL TEST RESULT -> referral_test_result
- REFERRAL TEST CT (IF PCR) -> referral_test_ct

Clinical/context (keep if present)
- SYMPTOMS? -> symptoms_flag
- VACCINATED? -> vaccinated_flag

Provenance notes
- SOURCE NOTES -> source_notes

FloodLAMP linkage / pattern fields (keep)
- INIT FL POS TUBE ID FROM CASE CLUSTER -> init_fl_pos_tube_id
- APPIVO COLLECTION DATE -> appivo_collection_date
- APPIVO COLLECTION TIME -> appivo_collection_time
- OTHER FL COLLECTION TIMESTAMP -> other_fl_collection_timestamp
- INIT POS -> init_pos
- INIT NEG -> init_neg
- INIT INC -> init_inc
- RERUN1 POS -> rerun1_pos
- RERUN1 NEG -> rerun1_neg
- RERUN1 INC -> rerun1_inc
- RERUN2 POS -> rerun2_pos
- RERUN2 NEG -> rerun2_neg
- RERUN2 INC -> rerun2_inc
- FL RESULT -> fl_result

## Normalization
- Dates -> `YYYY-MM-DD`
- Times -> `HH:MM:SS`
- If other_fl_collection_timestamp is datetime, output ISO datetime `YYYY-MM-DDTHH:MM:SS` (do not localize timezone).

## Output column order (exact)
- referral_test_id
- participant_id
- case_cluster_id
- referral_test_collection_date
- referral_test_collection_time
- referral_test_result_date
- referral_test_result_time
- referral_test_type
- referral_test_model
- referral_test_result
- referral_test_ct
- symptoms_flag
- vaccinated_flag
- source_notes
- init_fl_pos_tube_id
- appivo_collection_date
- appivo_collection_time
- other_fl_collection_timestamp
- init_pos
- init_neg
- init_inc
- rerun1_pos
- rerun1_neg
- rerun1_inc
- rerun2_pos
- rerun2_neg
- rerun2_inc
- fl_result

## Sort order
- participant_id, referral_test_collection_date, referral_test_collection_time, referral_test_id

## QA prints
- Row count
- unique participant_id count
- referral_test_type value_counts
- referral_test_result value_counts