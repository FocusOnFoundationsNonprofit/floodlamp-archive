Here you go — I added a **cross-site aggregation step** (from the **ZIPALL curated CSV zip**) and kept the code in the same condensed style. I also fixed a small syntax issue in the previous module (the commented `#if __name__ == "__main__":` blocks had indented lines that weren’t commented, which would otherwise cause an `IndentationError` on import).

[Download the updated Python module](sandbox:/mnt/data/zip_pilot_data_with_markdown_and_aggregate_FINAL.py)

I also ran it against the `ZIPALL_pilot-data_csvs.zip` you provided and packaged the resulting **3 aggregate CSVs** so you can inspect the shape/content immediately:

[Download example aggregate outputs (3 CSVs)](sandbox:/mnt/data/ZIPALL_pilot-data_aggregate_outputs_example_FINAL.zip)

---

## What the new code does

### New entrypoint function

**`aggregate_zipall_curated_csvs(pilot_data_csvs_zip_path, output_folder_path)`**

It:

1. **Extracts** the ZIP to a temporary folder.
2. **Discovers site folders** (e.g., `ABRM_pilot-data`, `BEND_pilot-data`, …).
3. For each site, **chooses the “best” available CSV** for each rollup:

   * Weekly summary: **APS > RFR > RSR > STS**
   * Stats key-values: **APS > RSR > STS**
   * Referral agreement: **APS > RSR > STS**
4. Aggregates and writes **three outputs** into `output_folder_path`:

   * `ZIPALL_pilot-data_aggregate_stats_key-values.csv`
   * `ZIPALL_pilot-data_aggregate_weekly-summary.csv`
   * `ZIPALL_pilot-data_aggregate_stats_referral-agreement.csv`

### Formulas are explicit in the output

* The aggregated **stats key-values** CSV includes a new column: **`value_formula`**
* Weekly and referral agreement aggregates also include formula columns (e.g. `pct_positive_formula`, `agree_pct_formula`, etc.), so you can see exactly how the percentages were computed.

### Denominator-zero and not-available handling

* Percent fields are computed with:

  * `value_status = "denom_zero"` when denominator is 0
  * `value_status = "not_available"` when missing
  * `value_status = "partial"` when only some sites contributed (useful for transparency)

---

## Where to edit if you want different aggregation behavior

### 1) Which stats metrics are included (and what formulas they use)

Edit the `METRICS = [...]` list inside:

**`_aggregate_stats_key_values(...)`**

That list controls:

* which metrics appear in the aggregate stats CSV
* how each is computed (sum vs ratio vs derived sum)
* metric name aliases (if any site uses slightly different wording)

Example: I already included aliases where I found a real mismatch (`Number of Test Reactions...tubes run` vs other possible variants).

### 2) How “best available file” is chosen

Edit these helper functions (same file):

* `_choose_weekly_csv_path_agg(...)`
* `_choose_stats_kv_csv_path_agg(...)`
* `_choose_referral_agreement_csv_path_agg(...)`

### 3) Output filenames

Edit the three `out_*` paths in:

**`aggregate_zipall_curated_csvs(...)`**

---

## One important design decision (FLMP sub-sites)

Because the ZIP structure is organized by **site folders** (and FLMP is one folder), the aggregator treats **FLMP as one unit** and uses the **`FLMP_*` combined** files — it does **not** aggregate `FLSP_*` and `CRLN_*` separately.

That is correct for **grand totals** (avoids double-counting), but if you later want “11-site” rollups where FLSP and CRLN are separate sites, the aggregation discovery should be changed to scan **files** rather than only **site folders**.

---

## How to run it

In your environment (repo), call:

```python
from zip_pilot_data_with_markdown_and_aggregate_FINAL import aggregate_zipall_curated_csvs

result = aggregate_zipall_curated_csvs(
    pilot_data_csvs_zip_path="path/to/ZIPALL_pilot-data_csvs.zip",
    output_folder_path="path/to/output/aggregates"
)
print(result)
```

That will create the 3 aggregate CSVs in your chosen output folder.

---

If you want, paste (or upload) one of the aggregate outputs you generate in your repo and I can sanity-check the totals (e.g., total tubes, total positives, referral agreement denominators) against expectations before you lock the archive.