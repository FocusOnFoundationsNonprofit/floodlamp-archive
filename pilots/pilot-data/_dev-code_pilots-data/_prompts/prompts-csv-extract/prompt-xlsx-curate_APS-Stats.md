# Task Spec — APS / Stats → curated CSVs

## Inputs
- `input_xlsx_path`: `{{APS_XLSX_PATH}}`  (example: `ABRM_APS_deID_PUB.xlsx`)
- Sheet: `Stats`
- `site_code`: `{{SITE_CODE}}` (example: `ABRM`)
- `output_folder_path`: `{{OUTPUT_DIR}}`

## Outputs (filenames must match exactly)
1) `{{SITE_CODE}}_APS_stats_key-values.csv`
2) `{{SITE_CODE}}_APS_stats_referral-agreement.csv`

## General requirements (both outputs)
- Use **openpyxl** and read displayed values: `load_workbook(input_xlsx_path, data_only=True)`.
- Normalize any header strings:
  - Replace newline `\n` with a single space
  - Trim whitespace
- Convert:
  - dates/datetimes → `YYYY-MM-DD` (if datetime, take date only unless spec says otherwise)
  - times → `HH:MM:SS`
- Deterministic ordering:
  - Keep natural order for key-values table
  - Include `source_row` for traceability
- Write both CSVs in one run of the module.

---

# PART A — Stats main blocks → `*_stats_key-values.csv`

## Goal
Create a tidy key/value dataset of all the main stats on the Stats sheet, organized by section.

## How to parse the sheet
- The Stats sheet is arranged in sections with section headers in column **B** where column **A** is empty.
- There are also 3 “file pointer” rows at the top:
  - Row 1: A=`ABRM_RFR_deID_PUB`, B=`RFR File`
  - Row 2: A=`ABRM_RTR_deID_PUB`, B=`RTR File`
  - Row 3: A=`NONE`,            B=`RSR File`
  Treat these as `section = "Files"` (or similar).

### Section headers (expected examples)
Overall, Re-runs, Positives, Inconclusives, Referrals and Correspondence, Comparison to Antigen, False Calls, People, Positivity, Dates, Info  
(Do not hardcode these only; allow new sections if encountered.)

## Row logic
Iterate rows top-to-bottom (suggested rows 1..250) and build records:
- If (A is None) AND (B is a non-empty string) AND (this row is a “section header”):
  - set `current_section = B`
  - do NOT emit a metric row for this line
- Else if (B is a non-empty string metric label) AND (A is not None metric value):
  - emit a record:
    - `section` = current_section (default "Files" until the first section header)
    - `metric` = B
    - `value` = A
    - `details` = C (may be None)
    - `comments` = D (may be None)
    - `source_sheet` = "Stats"
    - `source_row` = Excel row number
- Skip completely blank rows.

## Output schema (exact column order)
- section
- metric
- value
- details
- comments
- source_sheet
- source_row

## QA prints
- Number of metric rows written
- Distinct sections found (in order)

---

# PART B — Stats mini-table (E–L) → `*_stats_referral-agreement.csv`

## Goal
Extract the compact “positive/inconclusive follow-up agreement” mini-table (near columns E–L) into a clean 2-row CSV.

## Robust location strategy (do not hardcode row numbers)
- Search the sheet for the cell whose value is exactly: `Number of Tubes with FL Result`
- Record the found cell address as `source_anchor` (e.g., `"Stats!F23"`).
- The header row is that row, spanning columns F..L.
- The category label column is E. Data rows have values in column E like "Positive" and "Inconclusive".

## Table layout (expected)
Header row F..L includes:
- F: Number of Tubes with FL Result
- G: Number of Test Person/Cluster Cases
- H: Number with Ref or Corresp
- I: Agree with Ref or Corresp
- J: % Agree
- K: Disagree with Ref or Corresp
- L: % Disagree

Data rows:
- Find the next row where column E == "Positive"
- Find the next row where column E == "Inconclusive"

### Important quirk (inconclusive breakdown header)
Between Positive and Inconclusive rows, there may be a second header row that re-labels I..L as:
- I: Ref/Cor Pos
- J: % Incl > Pos
- K: Ref/Cor Neg
- L: % Incl > Neg

Your export must support BOTH interpretations by including BOTH sets of fields in the output schema:
- Positive row: fill agree/disagree fields; leave ref/cor pos/neg fields blank
- Inconclusive row: fill ref/cor pos/neg fields; leave agree/disagree fields blank (unless both exist)

## Output schema (exact column order)
- fl_result_category
- tubes_n
- cases_n
- with_ref_or_corresp_n
- agree_n
- agree_pct
- disagree_n
- disagree_pct
- ref_cor_pos_n
- incl_gt_pos_pct
- ref_cor_neg_n
- incl_gt_neg_pct
- source_sheet
- source_anchor

## QA prints
- Show the 2 parsed rows (as dicts)
- Print which header mode was used for each row (Agree/Disagree vs Ref/Cor breakdown)
