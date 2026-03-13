# Task Spec — RTR / Referral Tests by Person → curated CSV

## Inputs
- `input_xlsx_path`: `{{RTR_XLSX_PATH}}` (example: `ABRM_RTR_deID_PUB.xlsx`)
- Sheet: `Referral Tests by Person`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Output
- `{{SITE_CODE}}_RTR_referral-tests-by-person.csv`

## Row filter
- Keep rows where `PARTICIPANT ID` is not null/empty.

## Drop columns (ignore if absent)
- PARTICIPANT FIRSTNAME
- PARTICIPANT LASTNAME
- PARTICIPANT FULLNAME
- Referral Match Row
- FloodLAMP Match Row
- Hardcoded Tube ID
- Same Tube ID
- 3 Included in APS Pos and Incl?
- Any column whose header is numeric like `0`

## Keep + rename (exact output schema)
- PARTICIPANT ID -> participant_id
- 7 Num Sequential Referral Tests -> num_sequential_referral_tests  (strip leading "7 ")
- Num FloodLAMP Results Pos or Incl -> num_floodlamp_results_pos_or_incl
- FloodLAMP Tube ID -> floodlamp_tube_id
- FloodLAMP Test Result -> floodlamp_test_result
- FloodLAMP Test Date -> floodlamp_test_date
- 1st Referral Test Date -> first_referral_test_date
- Referral Overall Result -> referral_overall_result
- 1st Referral Test Type -> first_referral_test_type
- 1st Referral Test Result -> first_referral_test_result
- 2nd Referral Test Type -> second_referral_test_type
- 2nd Referral Test Result -> second_referral_test_result
- 3rd Referral Test Type -> third_referral_test_type
- 3rd Referral Test Result -> third_referral_test_result
- Antigen Neg with Other Positive -> antigen_neg_with_other_positive_flag
- Referral Eval -> referral_eval

## Normalization
- floodlamp_test_date, first_referral_test_date -> `YYYY-MM-DD`
- Strip whitespace from IDs

## Output column order (exact)
- participant_id
- num_sequential_referral_tests
- num_floodlamp_results_pos_or_incl
- floodlamp_tube_id
- floodlamp_test_result
- floodlamp_test_date
- first_referral_test_date
- referral_overall_result
- first_referral_test_type
- first_referral_test_result
- second_referral_test_type
- second_referral_test_result
- third_referral_test_type
- third_referral_test_result
- antigen_neg_with_other_positive_flag
- referral_eval

## Sort order
- participant_id

## QA prints
- Row count
- referral_overall_result value_counts