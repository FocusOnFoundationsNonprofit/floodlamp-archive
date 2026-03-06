[Download the plotting module](sandbox:/mnt/data/pilot_site_weekly_plots.py)

This module generates **three weekly plots per site** (matching the style you showed in your example image):

1. **Weekly testing volume** (bars): `participants_n`
2. **Weekly positivity** (line): `pct_positive * 100`
3. **Weekly composite** (stacked bars): total bar height = `participants_n`, with the **top segment** = `positive_tubes_n`, and **percent positivity labels** (1 decimal) above each bar from `pct_positive`

It writes outputs into a `plots/` subfolder inside each `{SITE}_pilot-data/` folder.

## What it looks for (inputs)

For each site folder, it auto-finds the “best” weekly summary CSV by preference order:

`APS > RFR > RSR > STS`

So it works even when ABRM only has `*_RFR_weekly-summary.csv`, etc.

## Where it writes (outputs)

For each site (e.g., `ABRM_pilot-data/`), it creates:

* `ABRM_pilot-data/plots/ABRM_weekly_volume.png`
* `ABRM_pilot-data/plots/ABRM_weekly_positivity.png`
* `ABRM_pilot-data/plots/ABRM_weekly_composite.png`

(You can also write PDFs by passing `file_formats=["png","pdf"]`.)

## How to run it

Example usage from your repo root:

```python
from pilot_site_weekly_plots import write_all_sites_weekly_plots

pilot_data_root = "data/floodlamp/pilots/pilot-data"
result = write_all_sites_weekly_plots(
    pilot_data_root,
    plots_subfolder_name="plots",
    file_formats=["png"],     # or ["png","pdf"]
    overwrite=True,
    skip_site_codes=[]        # e.g. ["FLMP","DAVI"] if you want to skip for now
)
print(result)
```

## Optional: site titles like “Preschool, CA”

Right now the plot title defaults to the **site code** (e.g., `ABRM`).
If you want friendly titles, pass a `site_title_map`:

```python
site_title_map = {
    "CRLN": "Preschool, CA",
    "FLSP": "FloodLAMP Staff, CA",
}
result = write_all_sites_weekly_plots(
    pilot_data_root,
    site_title_map=site_title_map,
)
```

## One line you might want to tweak later

In the composite plot, the stacked bars are built from:

* total = `participants_n`
* positives segment = `positive_tubes_n`
* base segment = `participants_n - positive_tubes_n` (clamped at 0)

If you decide later you want the composite to be **tube-consistent** (total = `tubes_n`, positives = `positive_tubes_n`), the change is localized inside `_plot_weekly_composite(...)`:

* replace `people = df["participants_n"]...` with `people = df["tubes_n"]...`

But as written, it follows your described “people screened bar with positive segment” approach and uses `pct_positive` for the label at the top.
