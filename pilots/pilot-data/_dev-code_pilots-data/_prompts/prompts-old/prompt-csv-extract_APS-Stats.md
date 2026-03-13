Write a Python script that reads the Excel workbook `ABRM_APS_deID_PUB.xlsx`, extracts two CSVs from the `Stats` sheet, and writes them to disk.

INPUT
- Excel path: ABRM_APS_deID_PUB.xlsx
- Sheet: "Stats"

OUTPUTS
1) aps_stats_key-values.csv
2) aps_stats_referral_agreement.csv

GENERAL REQUIREMENTS (apply to both outputs)
- Read computed/displayed cell VALUES (not formulas). Use openpyxl with `load_workbook(..., data_only=True)`.
- Normalize any header strings by replacing newline `\n` with a single space and trimming whitespace.
- Convert any Excel/Pandas dates or datetimes to ISO date strings: `YYYY-MM-DD`.
- Convert any `datetime.time` to `HH:MM:SS` strings.
- Preserve numeric values as numbers where feasible; it’s OK if the `value` column becomes mixed-type/object (CSV will still be readable).
- Deterministic ordering: keep the natural order in the sheet, and include a `source_row` field for traceability.

--------------------------------------------------------------------
PART A — aps_stats_key-values.csv (key-value metrics from Stats)

GOAL
Create a tidy key/value dataset of ALL the main stats on the Stats sheet, organized by section.

HOW TO PARSE THE SHEET
- The Stats sheet is arranged in sections with section headers in column B where column A is empty (None).
- In ABRM the section headers include:
  Overall, Re-runs, Positives, Inconclusives, Referrals and Correspondence,
  Comparison to Antigen, False Calls, People, Positivity, Dates, Info
- There are also 3 “file pointer” rows at the top:
  Row 1: A="ABRM_RFR_deID_PUB", B="RFR File"
  Row 2: A="ABRM_RTR_deID_PUB", B="RTR File"
  Row 3: A="NONE",            B="RSR File"
  Treat these as section = "Files" (or similar).

ROW LOGIC
Iterate rows top-to-bottom (e.g., rows 1..200) and build records:
- If (A is None) AND (B is a non-empty string) AND (B is one of the known section headers):
    set current_section = B
    do NOT emit a metric row for this header line
- Else if B is a non-empty string (metric label) AND A is not None (metric value):
    emit a record with:
      section = current_section (default "Files" for the first 3 rows before the first section header)
      metric  = B
      value   = A
      details = C (may be None)
      comments = D (may be None)
      source_sheet = "Stats"
      source_row = <excel row number>
- Skip completely blank rows.

OUTPUT SCHEMA (aps_stats_key-values.csv)
Columns (in this exact order):
- section
- metric
- value
- details
- comments
- source_sheet
- source_row

--------------------------------------------------------------------
PART B — aps_stats_referral_agreement.csv (mini-table at right side of Stats)

GOAL
Extract the compact “positive/inconclusive follow-up agreement” mini-table (located around columns E–L) into a clean, consistent 2-row CSV.

ROBUST LOCATION STRATEGY (do not hardcode exact row numbers)
- Find the cell whose value is exactly: "Number of Tubes with FL Result"
  In ABRM this is at F23, but your code should SEARCH the sheet.
- Once found:
  - The header row is that row, spanning columns F..L.
  - The category label column is E (same row as the data rows), with values like "Positive" and "Inconclusive".

TABLE LAYOUT DETAILS (ABRM)
Header row at F..L:
- F: Number of Tubes with FL Result
- G: Number of Test Person/Cluster Cases
- H: Number with Ref or Corresp
- I: Agree with Ref or Corresp
- J: % Agree
- K: Disagree with Ref or Corresp
- L: % Disagree

Data rows:
- The “Positive” row is the next row where column E == "Positive"
- The “Inconclusive” row is the next row where column E == "Inconclusive"

IMPORTANT QUIRK (Inconclusive breakdown)
- For inconclusives, the sheet also has a second header row that re-labels columns I..L:
  I: "Ref/Cor Pos"
  J: "% Incl > Pos"
  K: "Ref/Cor Neg"
  L: "% Incl > Neg"
- In ABRM this second header row occurs between Positive and Inconclusive.
- Your export should include BOTH concepts in the output schema, using NaN/blank where not applicable:
  - Positive row: fill agree/disagree fields; leave ref/cor pos/neg fields blank
  - Inconclusive row: fill ref/cor pos/neg fields; leave agree/disagree fields blank (unless both are actually present in a given site)

OUTPUT SCHEMA (aps_stats_referral_agreement.csv)
Exactly these columns, in this order:
- fl_result_category                      (from column E: "Positive"/"Inconclusive")
- tubes_n                                 (F)
- cases_n                                 (G)
- with_ref_or_corresp_n                   (H)
- agree_n                                 (I, only if header row is Agree…)
- agree_pct                               (J, only if header row is % Agree)
- disagree_n                              (K, only if header row is Disagree…)
- disagree_pct                            (L, only if header row is % Disagree)
- ref_cor_pos_n                           (I, only if inconclusive breakdown header row says Ref/Cor Pos)
- incl_gt_pos_pct                         (J, only if header row says % Incl > Pos)
- ref_cor_neg_n                           (K, only if header row says Ref/Cor Neg)
- incl_gt_neg_pct                         (L, only if header row says % Incl > Neg)
- source_sheet                            (constant "Stats")
- source_anchor                           (string like "F23" or "Stats!F23" indicating where the main header was found)

IMPLEMENTATION NOTE
- Use openpyxl to find the header cell and to read the required row/column values.
- Write both CSVs in one run of the script (this is the only extractor that outputs 2 CSVs).

FINAL QA PRINTS (to stdout)
- For aps_stats_key-values.csv: number of emitted metric rows and list of sections found.
- For aps_stats_referral_agreement.csv: show the parsed 2 rows and which header mode you used for each row (agree vs ref/cor breakdown).