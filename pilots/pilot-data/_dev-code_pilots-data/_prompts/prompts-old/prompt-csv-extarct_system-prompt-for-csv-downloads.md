# FloodLAMP CSV Extractors — General Prompt Preamble (for Cursor / AI code editor)

Use this preamble at the top of **every** code-generation request where the AI writes a Python module that takes a **published de-identified spreadsheet export** (XLSX) and produces one or more **curated extract CSVs** (a small, high-signal subset intended for public archive + downstream scientific analysis).

**Terminology**
- **Source workbook**: the published de-identified Google Sheet exported to XLSX (e.g., `ABRM_APS_deID_PUB.xlsx`).
- **Curated extract CSVs**: the normalized/trimmed CSV outputs we generate from specific tabs (stable schema; fewer columns; no embedded totals in headers). This is the “output CSVs” name I recommend.
- **Archive markdown**: separate step (not in scope for these extractor scripts).

---

## 0) Context & coding rules (always apply)

Follow the project’s Cursor coding rules exactly. :contentReference[oaicite:0]{index=0}  
Key reminders:
- **No type hints** in Python function signatures.
- Every non-trivial function must have a docstring in the required `:param` / `:return` format.
- Use helper functions prefixed with `_`.
- Use the **manual run pattern**: create an `mrun_...()` stub with `pass`, plus a commented `#if __name__ == "__main__":` block with example parameter assignments and function call.
- Print output conventions: `=== SECTION NAME ===`, `---` separators, summary stats at end.

---

## 1) Your job (what to generate)

Generate a **single Python module** (one file) for **one extractor task** that:
1. Loads the specified workbook/tab(s).
2. Applies the task’s trimming/normalization rules.
3. Writes the curated extract CSV(s) with the required filenames.
4. Prints deterministic QA summaries to stdout.

**Module name / link placeholder**
- Python module file: `{{PY_MODULE_PATH}}`  
  (I will replace this placeholder with the real module path in my repo and link it in my archive docs.)

---

## 2) Required implementation characteristics

### 2.1 Determinism and reproducibility
- Output should be deterministic: stable column order, stable row order (explicit sort or preserved sheet order), consistent formatting.
- Normalize headers:
  - Replace newlines `\n` with single spaces.
  - Trim whitespace.
  - If headers include embedded totals (e.g., `Weekly Participants 2954`), strip totals so schema is stable across sites.

### 2.2 Read values correctly
- If a task involves reading **cell values from an Excel layout** (not a clean table), prefer `openpyxl` with `load_workbook(..., data_only=True)` to read **displayed values**, not formulas.

### 2.3 Date/time normalization
- Date fields → `YYYY-MM-DD`
- Time fields → `HH:MM:SS`
- Datetime fields → either:
  - ISO `YYYY-MM-DDTHH:MM:SS`, **or**
  - split into date/time (only if task spec requires)
- Do not silently change timezones; treat timestamps as naive local/site timestamps.

### 2.4 PII safety
- These are public de-ID workbooks, but columns that are conceptually PII (names/emails/phones) should be **dropped** if present, even if blank in the public version, unless the task spec explicitly keeps them.
- Do not create new free-text fields that could reintroduce risk.

### 2.5 Filesystem + paths
- Use explicit `input_xlsx_path` and `output_folder_path` parameters.
- Create output folder if missing.
- Output filenames must match the task spec exactly.

---

## 3) Function layout expectations

At minimum, the module should include:

1) `extract_<something>(input_xlsx_path, output_folder_path, ...)`
- Main function that performs extraction and returns a dict summary like:
  - `{'written': [...], 'rows_written': {...}, 'warnings': [...], 'errors': [...]}`

2) Helper functions as needed:
- `_normalize_headers(...)`
- `_normalize_dates_times(...)`
- `_safe_int(...)`, `_safe_float(...)`
- `_write_csv(...)`

3) `mrun_<something>()` stub + commented main block per Cursor rules. :contentReference[oaicite:1]{index=1}

---

## 4) Output: QA prints (must be included)

Each extractor must print:
- `=== INPUT ===` (file path, sheet/tab name)
- `=== OUTPUTS ===` (full output paths written)
- `=== QA SUMMARY ===`
  - rows written
  - key uniqueness checks (if applicable)
  - simple distributions (e.g., value_counts on result fields) when relevant
  - min/max dates for time series
- `=== DONE ===`

If any rows are dropped due to filtering, print:
- how many were dropped
- why (e.g., missing primary key)

---

## 5) How to use this preamble with each task

For each extractor step, append a **Task-Specific Spec** section that defines:
- workbook filename
- tab name
- output curated extract CSV filename(s)
- row filters
- drop/keep columns
- renames (exact output schema + order)
- sorting rule
- any special parsing logic (anchors, header-row search, multi-table sheet slicing)
- QA prints unique to that task

Example of a task spec format (APS Stats) lives here (use as a pattern): :contentReference[oaicite:2]{index=2}

---

## 6) Now do the task below

**Task-Specific Spec**
{{PASTE_TASK_SPEC_HERE}}

(End of prompt.)
