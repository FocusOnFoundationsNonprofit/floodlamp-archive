"""
FloodLAMP pilot site weekly plots utility.

This module reads curated weekly-summary CSVs and writes three plot variants per site:
(1) Weekly volume - Testing Volume (total participants which includes pooling)
(2) Weekly percent positives - Percent Positive Tubes (may include re-tests of same individual)
(3) Weekly composite - Composite of Weekly Testing Volume and Percent Positive Tubes

All outputs are written into a per-site plots folder inside each {SITE}_pilot-data folder.
Aggregate plots are also generated from the aggregate_pilot-data folder and written to aggregate_pilot-data/plots/.
"""

import os
import re
import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

### Constants: file discovery
SITE_FOLDER_RE = re.compile(r"^[A-Z]{4}_pilot-data$")
WEEKLY_FILE_RE = re.compile(r"^(?P<site>[A-Z]{4})_(?P<ftype>[A-Z]{3})_weekly-summary\.csv$")
WEEKLY_TYPE_PRIORITY = ["APS", "RFR", "RSR", "STS"]
DEFAULT_PLOTS_SUBFOLDER_NAME = "plots"
AGGREGATE_FOLDER_NAME = "aggregate_pilot-data"
AGGREGATE_WEEKLY_CSV_NAME = "aggregate_pilot-data_weekly-summary.csv"

### Constants: plot titles
PROGRAM_TITLE_BASE = "FloodLAMP COVID Surveillance Testing Pilot Program"
AGGREGATE_TITLE_LINE1 = "ALL SITES (Aggregate) - FloodLAMP COVID Surveillance Testing Pilot Programs (11)"
PLOT_SUBTITLE_VOLUME = "Testing Volume (total participants which includes pooling)"
PLOT_SUBTITLE_PERCENT_POSITIVES = "Percent Positive Tubes (may include re-tests of same individual)"
PLOT_SUBTITLE_COMPOSITE = "Composite of Weekly Testing Volume and Percent Positive Tubes"
# Stats CSV file type priority for reading site info
STATS_CSV_TYPE_PRIORITY = ["APS", "RFR", "RSR"]

### Constants: plot styling
COLOR_PEOPLE = "tab:blue"
COLOR_POSITIVES = "tab:red"

### Constants: style prototyping
PROTOTYPE_SITE_CODE = "ABRM"
# Style A: Minimal Modern - softer, muted colors
STYLE_A_COLORS = {"people": "#5B9BD5", "positives": "#E07B7B"}
# Style B: FiveThirtyEight-Inspired - warm, bold colors
STYLE_B_COLORS = {"people": "#008FD5", "positives": "#FC4F30"}
# Style C: Clean Corporate - muted teal/coral
STYLE_C_COLORS = {"people": "#2E8B8B", "positives": "#E8927C"}

### Helpers: printing
def _print_section(title):
    """
    Print a standardized section header.

    :param title: str, section title.
    :return result: none, prints to stdout.
    """
    print(f"=== {title} ===")
def _print_kv(label, value):
    """
    Print a standardized key/value line.

    :param label: str, label to print.
    :param value: any, value to print.
    :return result: none, prints to stdout.
    """
    print(f"{label}: {value}")

### Helpers: filesystem
def _ensure_folder(folder_path):
    """
    Ensure a folder exists.

    :param folder_path: str, folder to create if missing.
    :return result: none, creates folder if needed.
    """
    os.makedirs(folder_path, exist_ok=True)
def _safe_join(*parts):
    """
    Join filesystem path parts safely.

    :param parts: tuple, path parts.
    :return result: str, joined path.
    """
    return os.path.join(*[p for p in parts if p is not None and str(p) != ""])

### Helpers: parsing and cleaning
def _to_float(value):
    """
    Convert a value to float if possible.

    :param value: any, input value.
    :return result: float, float value or nan if not parseable.
    """
    if value is None:
        return float("nan")
    try:
        if isinstance(value, str) and value.strip() == "":
            return float("nan")
        return float(value)
    except Exception:
        return float("nan")
def _normalize_weekly_df(df):
    """
    Normalize a weekly-summary dataframe into a consistent plotting schema.

    :param df: dataframe, weekly-summary dataframe.
    :return result: dataframe, normalized dataframe.
    """
    df = df.copy()
    required_cols = ["week_start_date", "participants_n", "tubes_n", "positive_tubes_n", "pct_positive"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Weekly summary missing required columns: {missing}")
    df["week_start_date"] = pd.to_datetime(df["week_start_date"], errors="coerce")
    df = df.sort_values(["week_start_date"]).reset_index(drop=True)
    for c in ["participants_n", "tubes_n", "positive_tubes_n"]:
        df[c] = df[c].apply(_to_float)
    df["pct_positive"] = df["pct_positive"].apply(_to_float)
    if "pct_positive_status" not in df.columns:
        df["pct_positive_status"] = "ok"
    df["week_label"] = df["week_start_date"].dt.strftime("%m-%d-%Y")
    return df

### Helpers: discovery
def _discover_site_folders(pilot_data_root):
    """
    Discover site folders in the pilot data root.

    :param pilot_data_root: str, root folder containing {SITE}_pilot-data folders.
    :return result: list, list of absolute site folder paths.
    """
    if not os.path.isdir(pilot_data_root):
        raise ValueError(f"pilot_data_root not found: {pilot_data_root}")
    site_folders = []
    for name in sorted(os.listdir(pilot_data_root)):
        full = os.path.join(pilot_data_root, name)
        if os.path.isdir(full) and SITE_FOLDER_RE.match(name):
            site_folders.append(full)
    return site_folders
def _discover_weekly_summary_csv(site_folder_path):
    """
    Find the best weekly-summary CSV for a site folder.

    :param site_folder_path: str, absolute site folder path.
    :return result: str, best weekly-summary CSV path or empty string if none found.
    """
    candidates = []
    for root, _, files in os.walk(site_folder_path):
        for fn in files:
            if not fn.endswith("_weekly-summary.csv"):
                continue
            m = WEEKLY_FILE_RE.match(fn)
            if not m:
                continue
            ftype = m.group("ftype")
            csv_path = os.path.join(root, fn)
            candidates.append((ftype, csv_path))
    if not candidates:
        return ""
    by_type = {}
    for ftype, path in candidates:
        by_type.setdefault(ftype, []).append(path)
    for preferred in WEEKLY_TYPE_PRIORITY:
        if preferred in by_type:
            return sorted(by_type[preferred])[0]
    return sorted([p for _, p in candidates])[0]
def _infer_site_code_from_folder(site_folder_path):
    """
    Infer the site code from a {SITE}_pilot-data folder name.

    :param site_folder_path: str, absolute site folder path.
    :return result: str, inferred site code.
    """
    base = os.path.basename(site_folder_path)
    return base.split("_")[0] if "_" in base else base
def _find_stats_csv_path(site_folder_path, site_code):
    """
    Find the best stats key-values CSV path for a site.

    :param site_folder_path: str, absolute site folder path.
    :param site_code: str, 4-letter site code.
    :return result: str or none, path to stats CSV or None if not found.
    """
    csv_folder = os.path.join(site_folder_path, f"{site_code}_curated_csvs")
    if not os.path.isdir(csv_folder):
        return None
    for ftype in STATS_CSV_TYPE_PRIORITY:
        csv_path = os.path.join(csv_folder, f"{site_code}_{ftype}_stats_key-values.csv")
        if os.path.isfile(csv_path):
            return csv_path
    return None
def _read_site_info_from_stats_csv(stats_csv_path):
    """
    Read site info (Program Name, Site Type, Location) from a stats key-values CSV.

    :param stats_csv_path: str, path to stats key-values CSV.
    :return result: dict, with keys: program_name, site_type, location (values may be None).
    """
    result = {"program_name": None, "site_type": None, "location": None}
    if not stats_csv_path or not os.path.isfile(stats_csv_path):
        return result
    try:
        df = pd.read_csv(stats_csv_path)
        # Look for rows in the Info section with specific metrics
        for _, row in df.iterrows():
            section = str(row.get("section", "")).strip()
            metric = str(row.get("metric", "")).strip()
            value = str(row.get("value", "")).strip()
            if section == "Info":
                if metric == "Program Name" and value:
                    result["program_name"] = value
                elif metric == "Site Type" and value:
                    result["site_type"] = value
                elif metric == "Location" and value:
                    result["location"] = value
    except Exception:
        pass
    return result

### Helpers: plotting primitives
### Constants: tick stride overrides for dense plots
DENSE_PLOT_SITE_CODES = {"FLMP"}  # Sites that need stride=4 due to many weeks
DENSE_PLOT_TICK_STRIDE = 4
DEFAULT_TICK_STRIDE = 1
def _format_site_title_line1(site_code, site_folder_path):
    """
    Format the first line of the plot title for a site.

    :param site_code: str, site code.
    :param site_folder_path: str, path to site folder (to read stats CSV).
    :return result: str, formatted first line of title.
    """
    stats_csv = _find_stats_csv_path(site_folder_path, site_code)
    info = _read_site_info_from_stats_csv(stats_csv)
    program_name = info.get("program_name")
    site_type = info.get("site_type")
    location = info.get("location")
    # Build title with available info
    if program_name and site_type and location:
        return f"{site_code} - {PROGRAM_TITLE_BASE} - {program_name} ({site_type}) - {location}"
    elif program_name and site_type:
        return f"{site_code} - {PROGRAM_TITLE_BASE} - {program_name} ({site_type})"
    elif program_name:
        return f"{site_code} - {PROGRAM_TITLE_BASE} - {program_name}"
    return f"{site_code} - {PROGRAM_TITLE_BASE}"
def _format_two_line_title(title_line1, subtitle):
    """
    Format a two-line title for a plot.

    :param title_line1: str, first line of title.
    :param subtitle: str, second line (plot type description).
    :return result: str, two-line title with newline separator.
    """
    return f"{title_line1}\n{subtitle}"

### Plotting: per-plot writers
def _plot_weekly_volume(df, title_line1, output_path_base, file_formats, tick_stride=DEFAULT_TICK_STRIDE):
    """
    Write the weekly volume plot.

    :param df: dataframe, normalized weekly dataframe.
    :param title_line1: str, first line of title (site/program info).
    :param output_path_base: str, output path without extension.
    :param file_formats: list, list of file extensions (e.g., ["png", "pdf"]).
    :param tick_stride: int, stride for x-axis tick labels.
    :return result: list, list of written file paths.
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    x = list(range(len(df)))
    y = df["participants_n"].fillna(0).tolist()
    ax.bar(x, y, color=COLOR_PEOPLE)
    full_title = _format_two_line_title(title_line1, PLOT_SUBTITLE_VOLUME)
    ax.set_title(full_title, fontsize=11)
    ax.set_xlabel("Week Starting")
    ax.set_ylabel("People Tested (Participants including pooling)")
    ax.set_xticks([i for i in x if i % tick_stride == 0])
    ax.set_xticklabels([df.loc[i, "week_label"] for i in x if i % tick_stride == 0], rotation=45, ha="right")
    ax.yaxis.grid(True, linestyle="--", alpha=0.4)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}"))
    # Ensure minimum x-axis width for charts with few weeks (prevents overly wide bars)
    if len(x) < 12:
        ax.set_xlim(-6, 6)
    fig.tight_layout()
    written = []
    for ext in file_formats:
        out_path = f"{output_path_base}.{ext}"
        fig.savefig(out_path, dpi=300 if ext.lower() == "png" else None)
        written.append(out_path)
    plt.close(fig)
    return written
def _plot_weekly_percent_positives(df, title_line1, output_path_base, file_formats, tick_stride=DEFAULT_TICK_STRIDE):
    """
    Write the weekly percent positives plot.

    :param df: dataframe, normalized weekly dataframe.
    :param title_line1: str, first line of title (site/program info).
    :param output_path_base: str, output path without extension.
    :param file_formats: list, list of file extensions (e.g., ["png", "pdf"]).
    :param tick_stride: int, stride for x-axis tick labels.
    :return result: list, list of written file paths.
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    x = list(range(len(df)))
    pct = (df["pct_positive"].fillna(0) * 100.0).tolist()
    ax.plot(x, pct, marker="o", color=COLOR_POSITIVES)
    full_title = _format_two_line_title(title_line1, PLOT_SUBTITLE_PERCENT_POSITIVES)
    ax.set_title(full_title, fontsize=11)
    ax.set_xlabel("Week Starting")
    ax.set_ylabel("Percent Positive Tubes (%)")
    ax.set_xticks([i for i in x if i % tick_stride == 0])
    ax.set_xticklabels([df.loc[i, "week_label"] for i in x if i % tick_stride == 0], rotation=45, ha="right")
    ax.set_ylim(bottom=0)
    ax.yaxis.grid(True, linestyle="--", alpha=0.4)
    # Ensure minimum x-axis width for charts with few weeks
    if len(x) < 12:
        ax.set_xlim(-6, 6)
    fig.tight_layout()
    written = []
    for ext in file_formats:
        out_path = f"{output_path_base}.{ext}"
        fig.savefig(out_path, dpi=300 if ext.lower() == "png" else None)
        written.append(out_path)
    plt.close(fig)
    return written
def _plot_weekly_composite(df, title_line1, output_path_base, file_formats, tick_stride=DEFAULT_TICK_STRIDE, label_zero_pct=True, pct_label_min_threshold=0.000001, pct_label_rotation=0, pct_label_fontsize=10):
    """
    Write the weekly composite stacked bar plot.

    :param df: dataframe, normalized weekly dataframe.
    :param title_line1: str, first line of title (site/program info).
    :param output_path_base: str, output path without extension.
    :param file_formats: list, list of file extensions (e.g., ["png", "pdf"]).
    :param tick_stride: int, stride for x-axis tick labels.
    :param label_zero_pct: bool, whether to label 0.0% weeks.
    :param pct_label_min_threshold: float, minimum positivity (as decimal, e.g. 0.02 for 2%) to show label.
    :param pct_label_rotation: int, rotation angle for percentage labels (0=horizontal, 90=vertical).
    :param pct_label_fontsize: int, font size for percentage labels.
    :return result: list, list of written file paths.
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    x = list(range(len(df)))
    people = df["participants_n"].fillna(0).tolist()
    pos = df["positive_tubes_n"].fillna(0).tolist()
    base = []
    neg_clamped_n = 0
    for i in range(len(x)):
        b = people[i] - pos[i]
        if not math.isfinite(b):
            b = 0
        if b < 0:
            b = 0
            neg_clamped_n += 1
        base.append(b)
    ax.bar(x, base, label="People Screened", color=COLOR_PEOPLE)
    ax.bar(x, pos, bottom=base, label="Positives", color=COLOR_POSITIVES)
    full_title = _format_two_line_title(title_line1, PLOT_SUBTITLE_COMPOSITE)
    ax.set_title(full_title, fontsize=11)
    ax.set_xlabel("Week Starting")
    ax.set_ylabel("People Tested (Participants including pooling)")
    ax.set_xticks([i for i in x if i % tick_stride == 0])
    ax.set_xticklabels([df.loc[i, "week_label"] for i in x if i % tick_stride == 0], rotation=45, ha="right")
    y_max = max(people) if people else 0
    # Increase y-axis headroom for rotated labels
    y_headroom = 1.35 if pct_label_rotation != 0 else 1.25
    ax.set_ylim(0, y_max * y_headroom if y_max > 0 else 1)
    # Determine text alignment based on rotation
    if pct_label_rotation == 90:
        ha, va = "center", "bottom"
    elif pct_label_rotation == -90:
        ha, va = "center", "top"
    else:
        ha, va = "center", "bottom"
    for i in range(len(x)):
        status = str(df.loc[i, "pct_positive_status"]) if "pct_positive_status" in df.columns else "ok"
        if status != "ok":
            continue
        pct = df.loc[i, "pct_positive"]
        if pd.isna(pct):
            continue
        if not label_zero_pct and float(pct) == 0.0:
            continue
        # Skip labels below the minimum threshold
        if float(pct) < pct_label_min_threshold:
            continue
        label = f"{pct * 100.0:.0f}%"
        ax.text(i, people[i] + (y_max * 0.02 if y_max > 0 else 0.2), label, ha=ha, va=va, fontsize=pct_label_fontsize, color=COLOR_POSITIVES, rotation=pct_label_rotation)
    ax.legend(loc="upper center", ncol=2, frameon=False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.4)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}"))
    # Ensure minimum x-axis width for charts with few weeks (prevents overly wide bars)
    if len(x) < 12:
        ax.set_xlim(-6, 6)
    fig.tight_layout()
    written = []
    for ext in file_formats:
        out_path = f"{output_path_base}.{ext}"
        fig.savefig(out_path, dpi=300 if ext.lower() == "png" else None)
        written.append(out_path)
    plt.close(fig)
    return written

### Helpers: cleanup old files
def _delete_old_positivity_files(plots_folder, site_code, file_formats):
    """
    Delete old positivity plot files (renamed to percent_positives).

    :param plots_folder: str, path to plots folder.
    :param site_code: str, site code (or "aggregate" for aggregate plots).
    :param file_formats: list, list of file extensions.
    :return deleted: list, list of deleted file paths.
    """
    deleted = []
    for ext in file_formats:
        old_path = os.path.join(plots_folder, f"{site_code}_weekly_positivity.{ext}")
        if os.path.isfile(old_path):
            os.remove(old_path)
            deleted.append(old_path)
    return deleted

### Helpers: style prototyping
def _apply_style_a(ax, fig):
    """
    Apply Style A (Minimal Modern) to axes.

    :param ax: axes, matplotlib axes object.
    :param fig: figure, matplotlib figure object.
    :return result: none, modifies axes in place.
    """
    # Remove top and right spines for open-frame look
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.5)
    ax.spines["bottom"].set_linewidth(0.5)
    # Lighter, thinner grid lines
    ax.yaxis.grid(True, linestyle="-", alpha=0.2, linewidth=0.5)
    ax.xaxis.grid(False)
    # Set tick parameters
    ax.tick_params(axis="both", which="major", labelsize=9, width=0.5)
    # Set background to white
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
def _apply_style_b(ax, fig):
    """
    Apply Style B (FiveThirtyEight-Inspired) to axes.

    :param ax: axes, matplotlib axes object.
    :param fig: figure, matplotlib figure object.
    :return result: none, modifies axes in place.
    """
    # Remove top and right spines, keep left and bottom
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.8)
    ax.spines["bottom"].set_linewidth(0.8)
    # Very subtle grid or none
    ax.yaxis.grid(True, linestyle="-", alpha=0.15, linewidth=0.8)
    ax.xaxis.grid(False)
    # Bolder tick labels
    ax.tick_params(axis="both", which="major", labelsize=10, width=0.8)
    # Light gray background
    ax.set_facecolor("#F0F0F0")
    fig.patch.set_facecolor("#F0F0F0")
def _apply_style_c(ax, fig):
    """
    Apply Style C (Clean Corporate) to axes.

    :param ax: axes, matplotlib axes object.
    :param fig: figure, matplotlib figure object.
    :return result: none, modifies axes in place.
    """
    # Thin bottom/left spines only, in gray
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#888888")
    ax.spines["left"].set_linewidth(0.8)
    ax.spines["bottom"].set_color("#888888")
    ax.spines["bottom"].set_linewidth(0.8)
    # No background grid
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    # Clean tick parameters
    ax.tick_params(axis="both", which="major", labelsize=9, colors="#555555", width=0.8)
    # White background
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
def _get_style_config(style_name):
    """
    Get style configuration (colors, applier function) for a style name.

    :param style_name: str, one of "a", "b", or "c".
    :return result: dict, with keys: colors, applier, title_fontsize, subtitle_fontsize, title_fontweight.
    """
    configs = {
        "a": {
            "colors": STYLE_A_COLORS,
            "applier": _apply_style_a,
            "title_fontsize": 11,
            "subtitle_fontsize": 11,
            "title_fontweight": "normal",
            "font_family": "sans-serif",
        },
        "b": {
            "colors": STYLE_B_COLORS,
            "applier": _apply_style_b,
            "title_fontsize": 13,
            "subtitle_fontsize": 17,
            "title_fontweight": "bold",
            "font_family": "sans-serif",
        },
        "c": {
            "colors": STYLE_C_COLORS,
            "applier": _apply_style_c,
            "title_fontsize": 11,
            "subtitle_fontsize": 11,
            "title_fontweight": "normal",
            "font_family": "sans-serif",
        },
    }
    return configs.get(style_name.lower(), configs["b"])

### Plotting: styled prototypes
def _plot_weekly_volume_styled(df, title_line1, output_path_base, style_name, file_formats, tick_stride=DEFAULT_TICK_STRIDE):
    """
    Write the weekly volume plot with a specific style.

    :param df: dataframe, normalized weekly dataframe.
    :param title_line1: str, first line of title (site/program info).
    :param output_path_base: str, output path without extension.
    :param style_name: str, style variant ("a", "b", or "c").
    :param file_formats: list, list of file extensions (e.g., ["png"]).
    :param tick_stride: int, stride for x-axis tick labels.
    :return result: list, list of written file paths.
    """
    config = _get_style_config(style_name)
    colors = config["colors"]
    fig, ax = plt.subplots(figsize=(14, 7))
    x = list(range(len(df)))
    y = df["participants_n"].fillna(0).tolist()
    ax.bar(x, y, color=colors["people"], edgecolor="none")
    # Use separate title and subtitle with different font sizes
    fig.suptitle(title_line1, fontsize=config["title_fontsize"], fontweight=config["title_fontweight"], fontfamily=config["font_family"], y=0.98)
    ax.set_title(PLOT_SUBTITLE_VOLUME, fontsize=config["subtitle_fontsize"], fontweight=config["title_fontweight"], fontfamily=config["font_family"], pad=10)
    ax.set_xlabel("Week Starting", fontsize=10, fontfamily=config["font_family"])
    ax.set_ylabel("People Tested (Participants including pooling)", fontsize=10, fontfamily=config["font_family"])
    ax.set_xticks([i for i in x if i % tick_stride == 0])
    ax.set_xticklabels([df.loc[i, "week_label"] for i in x if i % tick_stride == 0], rotation=45, ha="right")
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}"))
    # Ensure minimum x-axis width for charts with few weeks
    if len(x) < 12:
        ax.set_xlim(-6, 6)
    # Apply style after setting up plot elements
    config["applier"](ax, fig)
    fig.tight_layout()
    written = []
    for ext in file_formats:
        out_path = f"{output_path_base}.{ext}"
        fig.savefig(out_path, dpi=300 if ext.lower() == "png" else None, facecolor=fig.get_facecolor())
        written.append(out_path)
    plt.close(fig)
    return written
def _plot_weekly_percent_positives_styled(df, title_line1, output_path_base, style_name, file_formats, tick_stride=DEFAULT_TICK_STRIDE):
    """
    Write the weekly percent positives plot with a specific style.

    :param df: dataframe, normalized weekly dataframe.
    :param title_line1: str, first line of title (site/program info).
    :param output_path_base: str, output path without extension.
    :param style_name: str, style variant ("a", "b", or "c").
    :param file_formats: list, list of file extensions (e.g., ["png"]).
    :param tick_stride: int, stride for x-axis tick labels.
    :return result: list, list of written file paths.
    """
    config = _get_style_config(style_name)
    colors = config["colors"]
    fig, ax = plt.subplots(figsize=(14, 7))
    x = list(range(len(df)))
    pct = (df["pct_positive"].fillna(0) * 100.0).tolist()
    # Style B uses thicker lines
    line_width = 2.5 if style_name.lower() == "b" else 1.5
    marker_size = 8 if style_name.lower() == "b" else 6
    ax.plot(x, pct, marker="o", color=colors["positives"], linewidth=line_width, markersize=marker_size)
    # Use separate title and subtitle with different font sizes
    fig.suptitle(title_line1, fontsize=config["title_fontsize"], fontweight=config["title_fontweight"], fontfamily=config["font_family"], y=0.98)
    ax.set_title(PLOT_SUBTITLE_PERCENT_POSITIVES, fontsize=config["subtitle_fontsize"], fontweight=config["title_fontweight"], fontfamily=config["font_family"], pad=10)
    ax.set_xlabel("Week Starting", fontsize=10, fontfamily=config["font_family"])
    ax.set_ylabel("Percent Positive Tubes (%)", fontsize=10, fontfamily=config["font_family"])
    ax.set_xticks([i for i in x if i % tick_stride == 0])
    ax.set_xticklabels([df.loc[i, "week_label"] for i in x if i % tick_stride == 0], rotation=45, ha="right")
    ax.set_ylim(bottom=0)
    # Ensure minimum x-axis width for charts with few weeks
    if len(x) < 12:
        ax.set_xlim(-6, 6)
    # Apply style after setting up plot elements
    config["applier"](ax, fig)
    fig.tight_layout()
    written = []
    for ext in file_formats:
        out_path = f"{output_path_base}.{ext}"
        fig.savefig(out_path, dpi=300 if ext.lower() == "png" else None, facecolor=fig.get_facecolor())
        written.append(out_path)
    plt.close(fig)
    return written
def _plot_weekly_composite_styled(df, title_line1, output_path_base, style_name, file_formats, tick_stride=DEFAULT_TICK_STRIDE, label_zero_pct=True, pct_label_min_threshold=0.000001, pct_label_rotation=0, pct_label_fontsize=10):
    """
    Write the weekly composite stacked bar plot with a specific style.

    :param df: dataframe, normalized weekly dataframe.
    :param title_line1: str, first line of title (site/program info).
    :param output_path_base: str, output path without extension.
    :param style_name: str, style variant ("a", "b", or "c").
    :param file_formats: list, list of file extensions (e.g., ["png"]).
    :param tick_stride: int, stride for x-axis tick labels.
    :param label_zero_pct: bool, whether to label 0.0% weeks.
    :param pct_label_min_threshold: float, minimum positivity (as decimal) to show label.
    :param pct_label_rotation: int, rotation angle for percentage labels.
    :param pct_label_fontsize: int, font size for percentage labels.
    :return result: list, list of written file paths.
    """
    config = _get_style_config(style_name)
    colors = config["colors"]
    fig, ax = plt.subplots(figsize=(14, 7))
    x = list(range(len(df)))
    people = df["participants_n"].fillna(0).tolist()
    pos = df["positive_tubes_n"].fillna(0).tolist()
    base = []
    for i in range(len(x)):
        b = people[i] - pos[i]
        if not math.isfinite(b):
            b = 0
        if b < 0:
            b = 0
        base.append(b)
    ax.bar(x, base, label="People Screened", color=colors["people"], edgecolor="none")
    ax.bar(x, pos, bottom=base, label="Positives", color=colors["positives"], edgecolor="none")
    # Use separate title and subtitle with different font sizes
    fig.suptitle(title_line1, fontsize=config["title_fontsize"], fontweight=config["title_fontweight"], fontfamily=config["font_family"], y=0.98)
    ax.set_title(PLOT_SUBTITLE_COMPOSITE, fontsize=config["subtitle_fontsize"], fontweight=config["title_fontweight"], fontfamily=config["font_family"], pad=10)
    ax.set_xlabel("Week Starting", fontsize=10, fontfamily=config["font_family"])
    ax.set_ylabel("People Tested (Participants including pooling)", fontsize=10, fontfamily=config["font_family"])
    ax.set_xticks([i for i in x if i % tick_stride == 0])
    ax.set_xticklabels([df.loc[i, "week_label"] for i in x if i % tick_stride == 0], rotation=45, ha="right")
    y_max = max(people) if people else 0
    y_headroom = 1.35 if pct_label_rotation != 0 else 1.25
    ax.set_ylim(0, y_max * y_headroom if y_max > 0 else 1)
    # Determine text alignment based on rotation
    if pct_label_rotation == 90:
        ha, va = "center", "bottom"
    elif pct_label_rotation == -90:
        ha, va = "center", "top"
    else:
        ha, va = "center", "bottom"
    for i in range(len(x)):
        status = str(df.loc[i, "pct_positive_status"]) if "pct_positive_status" in df.columns else "ok"
        if status != "ok":
            continue
        pct = df.loc[i, "pct_positive"]
        if pd.isna(pct):
            continue
        if not label_zero_pct and float(pct) == 0.0:
            continue
        if float(pct) < pct_label_min_threshold:
            continue
        label = f"{pct * 100.0:.0f}%"
        ax.text(i, people[i] + (y_max * 0.02 if y_max > 0 else 0.2), label, ha=ha, va=va, fontsize=pct_label_fontsize, color=colors["positives"], rotation=pct_label_rotation)
    ax.legend(loc="upper center", ncol=2, frameon=False)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}"))
    # Ensure minimum x-axis width for charts with few weeks
    if len(x) < 12:
        ax.set_xlim(-6, 6)
    # Apply style after setting up plot elements
    config["applier"](ax, fig)
    fig.tight_layout()
    written = []
    for ext in file_formats:
        out_path = f"{output_path_base}.{ext}"
        fig.savefig(out_path, dpi=300 if ext.lower() == "png" else None, facecolor=fig.get_facecolor())
        written.append(out_path)
    plt.close(fig)
    return written

### Plotting: batch writers
def write_site_weekly_plots(site_folder_path, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME, file_formats=None, overwrite=True):
    """
    Write the three weekly plots for a single site folder.

    :param site_folder_path: str, absolute path to {SITE}_pilot-data folder.
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :param file_formats: list, list of formats like ["png", "pdf"].
    :param overwrite: bool, whether to overwrite existing plot files.
    :return result: dict, summary including inputs and written paths.
    """
    if file_formats is None:
        file_formats = ["png"]
    site_code = _infer_site_code_from_folder(site_folder_path)
    weekly_csv_path = _discover_weekly_summary_csv(site_folder_path)
    if weekly_csv_path == "":
        return {"site_code": site_code, "status": "skipped_no_weekly_csv", "written": []}
    df = pd.read_csv(weekly_csv_path)
    df = _normalize_weekly_df(df)
    title_line1 = _format_site_title_line1(site_code, site_folder_path)
    plots_folder = _safe_join(site_folder_path, plots_subfolder_name)
    _ensure_folder(plots_folder)
    # Delete old positivity files (renamed to percent_positives)
    _delete_old_positivity_files(plots_folder, site_code, file_formats)
    # Determine tick stride: dense plots (FLMP) use stride=4, others use stride=1
    tick_stride = DENSE_PLOT_TICK_STRIDE if site_code in DENSE_PLOT_SITE_CODES else DEFAULT_TICK_STRIDE
    written = []
    base_name = _safe_join(plots_folder, f"{site_code}_weekly_volume")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_volume(df, title_line1, base_name, file_formats, tick_stride=tick_stride)
    base_name = _safe_join(plots_folder, f"{site_code}_weekly_percent_positives")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_percent_positives(df, title_line1, base_name, file_formats, tick_stride=tick_stride)
    base_name = _safe_join(plots_folder, f"{site_code}_weekly_composite")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_composite(df, title_line1, base_name, file_formats, tick_stride=tick_stride)
    return {"site_code": site_code, "status": "ok", "weekly_csv_path": weekly_csv_path, "written": written}
def write_all_sites_weekly_plots(pilot_data_root, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME, file_formats=None, overwrite=True, skip_site_codes=None):
    """
    Write weekly plots for all sites under a pilot data root.

    :param pilot_data_root: str, root folder containing {SITE}_pilot-data folders.
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :param file_formats: list, list of formats like ["png", "pdf"].
    :param overwrite: bool, whether to overwrite existing plot files.
    :param skip_site_codes: list, optional list of site codes to skip.
    :return result: dict, summary including per-site results.
    """
    if file_formats is None:
        file_formats = ["png"]
    skip = set([s.strip().upper() for s in (skip_site_codes or []) if str(s).strip() != ""])
    site_folders = _discover_site_folders(pilot_data_root)
    _print_section("WEEKLY PLOTS: SETUP")
    _print_kv("Root folder", pilot_data_root)
    _print_kv("Sites found", len(site_folders))
    _print_kv("Output formats", ", ".join(file_formats))
    _print_kv("Plots subfolder", plots_subfolder_name)
    print()
    _print_section("WEEKLY PLOTS: PROCESSING SITES")
    results = []
    for site_folder in site_folders:
        site_code = _infer_site_code_from_folder(site_folder)
        if site_code in skip:
            results.append({"site_code": site_code, "status": "skipped_by_user"})
            _print_kv(f"  {site_code}", "SKIPPED (by user request)")
            continue
        res = write_site_weekly_plots(site_folder, plots_subfolder_name=plots_subfolder_name, file_formats=file_formats, overwrite=overwrite)
        results.append(res)
        if res["status"] == "ok":
            _print_kv(f"  {site_code}", f"OK - wrote {len(res['written'])} files to {plots_subfolder_name}/")
        elif res["status"] == "skipped_no_weekly_csv":
            _print_kv(f"  {site_code}", "SKIPPED (no weekly-summary CSV found)")
        else:
            _print_kv(f"  {site_code}", f"STATUS: {res['status']}")
    print()
    # Process aggregate data
    _print_section("WEEKLY PLOTS: PROCESSING AGGREGATE")
    aggregate_res = write_aggregate_weekly_plots(pilot_data_root, plots_subfolder_name=plots_subfolder_name, file_formats=file_formats, overwrite=overwrite)
    if aggregate_res["status"] == "ok":
        _print_kv("  AGGREGATE", f"OK - wrote {len(aggregate_res['written'])} files to {AGGREGATE_FOLDER_NAME}/{plots_subfolder_name}/")
    elif aggregate_res["status"] == "skipped_no_aggregate_folder":
        _print_kv("  AGGREGATE", "SKIPPED (no aggregate folder found)")
    elif aggregate_res["status"] == "skipped_no_weekly_csv":
        _print_kv("  AGGREGATE", "SKIPPED (no weekly-summary CSV found)")
    else:
        _print_kv("  AGGREGATE", f"STATUS: {aggregate_res['status']}")
    print()
    # Compute summary stats
    ok_count = sum(1 for r in results if r["status"] == "ok")
    skipped_no_csv = [r["site_code"] for r in results if r["status"] == "skipped_no_weekly_csv"]
    skipped_by_user = [r["site_code"] for r in results if r["status"] == "skipped_by_user"]
    total_files = sum(len(r.get("written", [])) for r in results)
    aggregate_files = len(aggregate_res.get("written", []))
    _print_section("WEEKLY PLOTS: SUMMARY")
    _print_kv("Sites succeeded", f"{ok_count} of {len(site_folders)}")
    _print_kv("Total site files written", total_files)
    _print_kv("Aggregate files written", aggregate_files)
    _print_kv("Grand total files written", total_files + aggregate_files)
    if skipped_no_csv:
        _print_kv("Skipped (no CSV)", ", ".join(skipped_no_csv))
    if skipped_by_user:
        _print_kv("Skipped (by user)", ", ".join(skipped_by_user))
    _print_section("WEEKLY PLOTS: DONE")
    return {"pilot_data_root": pilot_data_root, "sites_n": len(site_folders), "results": results, "aggregate_result": aggregate_res}
def write_aggregate_weekly_plots(pilot_data_root, aggregate_folder_name=AGGREGATE_FOLDER_NAME, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME, file_formats=None, overwrite=True):
    """
    Write weekly plots for the aggregate data.

    :param pilot_data_root: str, root folder containing the aggregate_pilot-data folder.
    :param aggregate_folder_name: str, name of the aggregate folder.
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :param file_formats: list, list of formats like ["png", "pdf"].
    :param overwrite: bool, whether to overwrite existing plot files.
    :return result: dict, summary including written paths.
    """
    if file_formats is None:
        file_formats = ["png"]
    aggregate_folder = _safe_join(pilot_data_root, aggregate_folder_name)
    if not os.path.isdir(aggregate_folder):
        return {"status": "skipped_no_aggregate_folder", "written": []}
    weekly_csv_path = _safe_join(aggregate_folder, AGGREGATE_WEEKLY_CSV_NAME)
    if not os.path.isfile(weekly_csv_path):
        return {"status": "skipped_no_weekly_csv", "written": []}
    df = pd.read_csv(weekly_csv_path)
    df = _normalize_weekly_df(df)
    title_line1 = AGGREGATE_TITLE_LINE1
    plots_folder = _safe_join(aggregate_folder, plots_subfolder_name)
    _ensure_folder(plots_folder)
    # Delete old positivity files (renamed to percent_positives)
    _delete_old_positivity_files(plots_folder, "aggregate", file_formats)
    # Aggregate uses dense tick stride
    tick_stride = DENSE_PLOT_TICK_STRIDE
    written = []
    base_name = _safe_join(plots_folder, "aggregate_weekly_volume")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_volume(df, title_line1, base_name, file_formats, tick_stride=tick_stride)
    base_name = _safe_join(plots_folder, "aggregate_weekly_percent_positives")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_percent_positives(df, title_line1, base_name, file_formats, tick_stride=tick_stride)
    base_name = _safe_join(plots_folder, "aggregate_weekly_composite")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        # Aggregate has many weeks - use rotated labels with threshold to improve readability
        written += _plot_weekly_composite(df, title_line1, base_name, file_formats, tick_stride=tick_stride, label_zero_pct=False, pct_label_min_threshold=0.02, pct_label_rotation=90, pct_label_fontsize=6)
    return {"status": "ok", "weekly_csv_path": weekly_csv_path, "written": written}
def write_abrm_style_prototypes(pilot_data_root, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME):
    """
    Write style prototype plots for ABRM site only (3 plots x 3 styles = 9 files).

    :param pilot_data_root: str, root folder containing {SITE}_pilot-data folders.
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :return result: dict, summary including written paths.
    """
    site_code = PROTOTYPE_SITE_CODE
    site_folder = _safe_join(pilot_data_root, f"{site_code}_pilot-data")
    if not os.path.isdir(site_folder):
        return {"site_code": site_code, "status": "error_folder_not_found", "written": []}
    weekly_csv_path = _discover_weekly_summary_csv(site_folder)
    if weekly_csv_path == "":
        return {"site_code": site_code, "status": "skipped_no_weekly_csv", "written": []}
    df = pd.read_csv(weekly_csv_path)
    df = _normalize_weekly_df(df)
    title_line1 = _format_site_title_line1(site_code, site_folder)
    plots_folder = _safe_join(site_folder, plots_subfolder_name)
    _ensure_folder(plots_folder)
    tick_stride = DENSE_PLOT_TICK_STRIDE if site_code in DENSE_PLOT_SITE_CODES else DEFAULT_TICK_STRIDE
    file_formats = ["png"]
    styles = ["a", "b", "c"]
    written = []
    _print_section("STYLE PROTOTYPES: GENERATING FOR ABRM")
    _print_kv("Site folder", site_folder)
    _print_kv("Weekly CSV", weekly_csv_path)
    _print_kv("Output folder", plots_folder)
    print()
    for style in styles:
        style_label = {"a": "Minimal Modern", "b": "FiveThirtyEight", "c": "Clean Corporate"}[style]
        _print_kv(f"  Style {style.upper()}", style_label)
        # Volume plot
        base_name = _safe_join(plots_folder, f"{site_code}_weekly_volume_style_{style}")
        written += _plot_weekly_volume_styled(df, title_line1, base_name, style, file_formats, tick_stride=tick_stride)
        # Percent positives plot
        base_name = _safe_join(plots_folder, f"{site_code}_weekly_percent_positives_style_{style}")
        written += _plot_weekly_percent_positives_styled(df, title_line1, base_name, style, file_formats, tick_stride=tick_stride)
        # Composite plot
        base_name = _safe_join(plots_folder, f"{site_code}_weekly_composite_style_{style}")
        written += _plot_weekly_composite_styled(df, title_line1, base_name, style, file_formats, tick_stride=tick_stride)
    print()
    _print_section("STYLE PROTOTYPES: SUMMARY")
    _print_kv("Total files written", len(written))
    for path in written:
        _print_kv("  ", os.path.basename(path))
    _print_section("STYLE PROTOTYPES: DONE")
    return {"site_code": site_code, "status": "ok", "written": written}
def write_all_sites_weekly_plots_styled(pilot_data_root, style_name="b", plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME, file_formats=None, overwrite=True, skip_site_codes=None):
    """
    Write weekly plots for all sites using a specific style.

    :param pilot_data_root: str, root folder containing {SITE}_pilot-data folders.
    :param style_name: str, style variant ("a", "b", or "c"). Default is "b".
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :param file_formats: list, list of formats like ["png", "pdf"].
    :param overwrite: bool, whether to overwrite existing plot files.
    :param skip_site_codes: list, optional list of site codes to skip.
    :return result: dict, summary including per-site results.
    """
    if file_formats is None:
        file_formats = ["png"]
    skip = set([s.strip().upper() for s in (skip_site_codes or []) if str(s).strip() != ""])
    site_folders = _discover_site_folders(pilot_data_root)
    style_label = {"a": "Minimal Modern", "b": "FiveThirtyEight", "c": "Clean Corporate"}.get(style_name.lower(), style_name)
    _print_section(f"STYLED WEEKLY PLOTS: SETUP (Style {style_name.upper()}: {style_label})")
    _print_kv("Root folder", pilot_data_root)
    _print_kv("Sites found", len(site_folders))
    _print_kv("Output formats", ", ".join(file_formats))
    _print_kv("Plots subfolder", plots_subfolder_name)
    print()
    _print_section("STYLED WEEKLY PLOTS: PROCESSING SITES")
    results = []
    for site_folder in site_folders:
        site_code = _infer_site_code_from_folder(site_folder)
        if site_code in skip:
            results.append({"site_code": site_code, "status": "skipped_by_user"})
            _print_kv(f"  {site_code}", "SKIPPED (by user request)")
            continue
        weekly_csv_path = _discover_weekly_summary_csv(site_folder)
        if weekly_csv_path == "":
            results.append({"site_code": site_code, "status": "skipped_no_weekly_csv", "written": []})
            _print_kv(f"  {site_code}", "SKIPPED (no weekly-summary CSV found)")
            continue
        df = pd.read_csv(weekly_csv_path)
        df = _normalize_weekly_df(df)
        title_line1 = _format_site_title_line1(site_code, site_folder)
        plots_folder = _safe_join(site_folder, plots_subfolder_name)
        _ensure_folder(plots_folder)
        tick_stride = DENSE_PLOT_TICK_STRIDE if site_code in DENSE_PLOT_SITE_CODES else DEFAULT_TICK_STRIDE
        written = []
        base_name = _safe_join(plots_folder, f"{site_code}_weekly_volume")
        if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
            written += _plot_weekly_volume_styled(df, title_line1, base_name, style_name, file_formats, tick_stride=tick_stride)
        base_name = _safe_join(plots_folder, f"{site_code}_weekly_percent_positives")
        if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
            written += _plot_weekly_percent_positives_styled(df, title_line1, base_name, style_name, file_formats, tick_stride=tick_stride)
        base_name = _safe_join(plots_folder, f"{site_code}_weekly_composite")
        if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
            written += _plot_weekly_composite_styled(df, title_line1, base_name, style_name, file_formats, tick_stride=tick_stride)
        results.append({"site_code": site_code, "status": "ok", "weekly_csv_path": weekly_csv_path, "written": written})
        _print_kv(f"  {site_code}", f"OK - wrote {len(written)} files to {plots_subfolder_name}/")
    print()
    # Process aggregate data
    _print_section("STYLED WEEKLY PLOTS: PROCESSING AGGREGATE")
    aggregate_res = write_aggregate_weekly_plots_styled(pilot_data_root, style_name=style_name, plots_subfolder_name=plots_subfolder_name, file_formats=file_formats, overwrite=overwrite)
    if aggregate_res["status"] == "ok":
        _print_kv("  AGGREGATE", f"OK - wrote {len(aggregate_res['written'])} files to {AGGREGATE_FOLDER_NAME}/{plots_subfolder_name}/")
    elif aggregate_res["status"] == "skipped_no_aggregate_folder":
        _print_kv("  AGGREGATE", "SKIPPED (no aggregate folder found)")
    elif aggregate_res["status"] == "skipped_no_weekly_csv":
        _print_kv("  AGGREGATE", "SKIPPED (no weekly-summary CSV found)")
    else:
        _print_kv("  AGGREGATE", f"STATUS: {aggregate_res['status']}")
    print()
    # Compute summary stats
    ok_count = sum(1 for r in results if r["status"] == "ok")
    skipped_no_csv = [r["site_code"] for r in results if r["status"] == "skipped_no_weekly_csv"]
    skipped_by_user = [r["site_code"] for r in results if r["status"] == "skipped_by_user"]
    total_files = sum(len(r.get("written", [])) for r in results)
    aggregate_files = len(aggregate_res.get("written", []))
    _print_section("STYLED WEEKLY PLOTS: SUMMARY")
    _print_kv("Style", f"{style_name.upper()} ({style_label})")
    _print_kv("Sites succeeded", f"{ok_count} of {len(site_folders)}")
    _print_kv("Total site files written", total_files)
    _print_kv("Aggregate files written", aggregate_files)
    _print_kv("Grand total files written", total_files + aggregate_files)
    if skipped_no_csv:
        _print_kv("Skipped (no CSV)", ", ".join(skipped_no_csv))
    if skipped_by_user:
        _print_kv("Skipped (by user)", ", ".join(skipped_by_user))
    _print_section("STYLED WEEKLY PLOTS: DONE")
    return {"pilot_data_root": pilot_data_root, "style": style_name, "sites_n": len(site_folders), "results": results, "aggregate_result": aggregate_res}
def write_aggregate_weekly_plots_styled(pilot_data_root, style_name="b", aggregate_folder_name=AGGREGATE_FOLDER_NAME, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME, file_formats=None, overwrite=True):
    """
    Write weekly plots for the aggregate data using a specific style.

    :param pilot_data_root: str, root folder containing the aggregate_pilot-data folder.
    :param style_name: str, style variant ("a", "b", or "c"). Default is "b".
    :param aggregate_folder_name: str, name of the aggregate folder.
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :param file_formats: list, list of formats like ["png", "pdf"].
    :param overwrite: bool, whether to overwrite existing plot files.
    :return result: dict, summary including written paths.
    """
    if file_formats is None:
        file_formats = ["png"]
    aggregate_folder = _safe_join(pilot_data_root, aggregate_folder_name)
    if not os.path.isdir(aggregate_folder):
        return {"status": "skipped_no_aggregate_folder", "written": []}
    weekly_csv_path = _safe_join(aggregate_folder, AGGREGATE_WEEKLY_CSV_NAME)
    if not os.path.isfile(weekly_csv_path):
        return {"status": "skipped_no_weekly_csv", "written": []}
    df = pd.read_csv(weekly_csv_path)
    df = _normalize_weekly_df(df)
    title_line1 = AGGREGATE_TITLE_LINE1
    plots_folder = _safe_join(aggregate_folder, plots_subfolder_name)
    _ensure_folder(plots_folder)
    tick_stride = DENSE_PLOT_TICK_STRIDE
    written = []
    base_name = _safe_join(plots_folder, "aggregate_weekly_volume")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_volume_styled(df, title_line1, base_name, style_name, file_formats, tick_stride=tick_stride)
    base_name = _safe_join(plots_folder, "aggregate_weekly_percent_positives")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_percent_positives_styled(df, title_line1, base_name, style_name, file_formats, tick_stride=tick_stride)
    base_name = _safe_join(plots_folder, "aggregate_weekly_composite")
    if overwrite or not any(os.path.exists(f"{base_name}.{ext}") for ext in file_formats):
        written += _plot_weekly_composite_styled(df, title_line1, base_name, style_name, file_formats, tick_stride=tick_stride, label_zero_pct=False, pct_label_min_threshold=0.02, pct_label_rotation=90, pct_label_fontsize=6)
    return {"status": "ok", "weekly_csv_path": weekly_csv_path, "written": written}

### Markdown integration: insert plots into summary markdown files
def _build_plots_markdown_section(site_code, plots_subfolder_name):
    """
    Build the markdown section content for plots.

    :param site_code: str, site code (or "aggregate" for aggregate).
    :param plots_subfolder_name: str, subfolder name where plots are stored.
    :return result: str, markdown content for the plots section.
    """
    prefix = site_code if site_code != "aggregate" else "aggregate"
    lines = [
        "## Plots",
        "",
        "### Composite",
        "",
        f"![{prefix} Weekly Composite]({plots_subfolder_name}/{prefix}_weekly_composite.png)",
        "",
        "### Percent Positive Tubes",
        "",
        f"![{prefix} Weekly Percent Positives]({plots_subfolder_name}/{prefix}_weekly_percent_positives.png)",
        "",
        "### Volume",
        "",
        f"![{prefix} Weekly Volume]({plots_subfolder_name}/{prefix}_weekly_volume.png)",
        "",
    ]
    return "\n".join(lines)
def _insert_plots_section_into_markdown(markdown_path, site_code, plots_subfolder_name):
    """
    Insert or update the plots section in an existing markdown summary file.

    :param markdown_path: str, path to the markdown summary file.
    :param site_code: str, site code (or "aggregate" for aggregate).
    :param plots_subfolder_name: str, subfolder name where plots are stored.
    :return result: dict, with keys: status, message.
    """
    if not os.path.isfile(markdown_path):
        return {"status": "skipped_no_file", "message": f"Markdown file not found: {markdown_path}"}
    with open(markdown_path, "r", encoding="utf-8") as f:
        content = f.read()
    plots_section = _build_plots_markdown_section(site_code, plots_subfolder_name)
    # Check if plots section already exists - if so, replace it
    plots_header_pattern = re.compile(r"^## Plots\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    if "## Plots" in content:
        # Replace existing plots section
        content = plots_header_pattern.sub(plots_section, content)
        action = "updated"
    else:
        # Insert before ## Files
        files_pattern = re.compile(r"^## Files", re.MULTILINE)
        match = files_pattern.search(content)
        if match:
            insert_pos = match.start()
            content = content[:insert_pos] + plots_section + "\n" + content[insert_pos:]
            action = "inserted"
        else:
            return {"status": "skipped_no_files_section", "message": "Could not find ## Files section to insert before"}
    with open(markdown_path, "w", encoding="utf-8") as f:
        f.write(content)
    return {"status": "ok", "message": f"Plots section {action} in {os.path.basename(markdown_path)}"}
def insert_plots_into_site_markdown(site_folder_path, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME):
    """
    Insert plots section into a single site's markdown summary file.

    :param site_folder_path: str, absolute path to {SITE}_pilot-data folder.
    :param plots_subfolder_name: str, subfolder name where plots are stored.
    :return result: dict, summary including status and message.
    """
    site_code = _infer_site_code_from_folder(site_folder_path)
    markdown_filename = f"{site_code}_pilot-data_summary.md"
    markdown_path = os.path.join(site_folder_path, markdown_filename)
    return _insert_plots_section_into_markdown(markdown_path, site_code, plots_subfolder_name)
def insert_plots_into_aggregate_markdown(pilot_data_root, aggregate_folder_name=AGGREGATE_FOLDER_NAME, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME):
    """
    Insert plots section into the aggregate markdown summary file.

    :param pilot_data_root: str, root folder containing the aggregate_pilot-data folder.
    :param aggregate_folder_name: str, name of the aggregate folder.
    :param plots_subfolder_name: str, subfolder name where plots are stored.
    :return result: dict, summary including status and message.
    """
    aggregate_folder = _safe_join(pilot_data_root, aggregate_folder_name)
    markdown_filename = f"{aggregate_folder_name}_summary.md"
    markdown_path = os.path.join(aggregate_folder, markdown_filename)
    return _insert_plots_section_into_markdown(markdown_path, "aggregate", plots_subfolder_name)
def insert_plots_into_all_markdowns(pilot_data_root, plots_subfolder_name=DEFAULT_PLOTS_SUBFOLDER_NAME, skip_site_codes=None):
    """
    Insert plots sections into all site markdown summary files and the aggregate markdown.

    :param pilot_data_root: str, root folder containing {SITE}_pilot-data folders.
    :param plots_subfolder_name: str, subfolder name where plots are stored.
    :param skip_site_codes: list, optional list of site codes to skip.
    :return result: dict, summary including per-site results and aggregate result.
    """
    skip = set([s.strip().upper() for s in (skip_site_codes or []) if str(s).strip() != ""])
    site_folders = _discover_site_folders(pilot_data_root)
    _print_section("MARKDOWN PLOTS INSERT: SETUP")
    _print_kv("Root folder", pilot_data_root)
    _print_kv("Sites found", len(site_folders))
    _print_kv("Plots subfolder", plots_subfolder_name)
    print()
    _print_section("MARKDOWN PLOTS INSERT: PROCESSING SITES")
    results = []
    for site_folder in site_folders:
        site_code = _infer_site_code_from_folder(site_folder)
        if site_code in skip:
            results.append({"site_code": site_code, "status": "skipped_by_user"})
            _print_kv(f"  {site_code}", "SKIPPED (by user request)")
            continue
        res = insert_plots_into_site_markdown(site_folder, plots_subfolder_name=plots_subfolder_name)
        res["site_code"] = site_code
        results.append(res)
        if res["status"] == "ok":
            _print_kv(f"  {site_code}", res["message"])
        else:
            _print_kv(f"  {site_code}", f"{res['status']}: {res['message']}")
    print()
    _print_section("MARKDOWN PLOTS INSERT: PROCESSING AGGREGATE")
    aggregate_res = insert_plots_into_aggregate_markdown(pilot_data_root, plots_subfolder_name=plots_subfolder_name)
    if aggregate_res["status"] == "ok":
        _print_kv("  AGGREGATE", aggregate_res["message"])
    else:
        _print_kv("  AGGREGATE", f"{aggregate_res['status']}: {aggregate_res['message']}")
    print()
    ok_count = sum(1 for r in results if r["status"] == "ok")
    _print_section("MARKDOWN PLOTS INSERT: SUMMARY")
    _print_kv("Sites succeeded", f"{ok_count} of {len(site_folders)}")
    _print_kv("Aggregate status", aggregate_res["status"])
    _print_section("MARKDOWN PLOTS INSERT: DONE")
    return {"pilot_data_root": pilot_data_root, "sites_n": len(site_folders), "results": results, "aggregate_result": aggregate_res}
def mrun_insert_plots_into_all_markdowns():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    plots_subfolder_name = "_plots"
    skip_site_codes = []
    insert_plots_into_all_markdowns(pilot_data_root, plots_subfolder_name=plots_subfolder_name, skip_site_codes=skip_site_codes)

### Execution: run all pilot plots
def run_all_pilot_plots(pilot_data_root, plots_subfolder_name="_plots", file_formats=None, overwrite=True, skip_site_codes=None, run_mode="styled", selected_style="b", insert_into_markdown=True):
    """
    Run pilot plot generation with specified mode and options.

    Run modes:
    - "styled": Generates plots using selected_style (a, b, or c) for ALL sites + aggregate. Production mode.
    - "prototypes": Generates 9 prototype files for ABRM only (3 plots × 3 styles) to compare styles. Skips markdown.
    - "original": Generates plots using the older non-styled plotting functions for all sites.
    - "markdown_only": Only inserts image references into markdown files. Does NOT regenerate plots.

    Style options (for "styled" and "prototypes" modes):
    - "a": Minimal Modern
    - "b": FiveThirtyEight (default)
    - "c": Clean Corporate

    Typical workflow:
    1. Run with run_mode="prototypes" to compare styles on ABRM
    2. Pick favorite style (a, b, or c)
    3. Run with run_mode="styled" and selected_style to generate for all sites + insert into markdown

    :param pilot_data_root: str, root folder containing {SITE}_pilot-data folders.
    :param plots_subfolder_name: str, subfolder name to write plots into.
    :param file_formats: list, list of formats like ["png", "pdf"].
    :param overwrite: bool, whether to overwrite existing plot files.
    :param skip_site_codes: list, optional list of site codes to skip.
    :param run_mode: str, one of "styled", "prototypes", "original", "markdown_only".
    :param selected_style: str, style variant ("a", "b", or "c") for styled mode.
    :param insert_into_markdown: bool, whether to insert plots into markdown summary files after generating.
    :return result: dict, results from the executed run mode.
    """
    if file_formats is None:
        file_formats = ["png", "pdf"]
    if run_mode == "prototypes":
        result = write_abrm_style_prototypes(pilot_data_root, plots_subfolder_name=plots_subfolder_name)
    elif run_mode == "styled":
        result = write_all_sites_weekly_plots_styled(pilot_data_root, style_name=selected_style, plots_subfolder_name=plots_subfolder_name, file_formats=file_formats, overwrite=overwrite, skip_site_codes=skip_site_codes)
    elif run_mode == "markdown_only":
        result = insert_plots_into_all_markdowns(pilot_data_root, plots_subfolder_name=plots_subfolder_name, skip_site_codes=skip_site_codes)
        insert_into_markdown = False
    else:
        result = write_all_sites_weekly_plots(pilot_data_root, plots_subfolder_name=plots_subfolder_name, file_formats=file_formats, overwrite=overwrite, skip_site_codes=skip_site_codes)
    if insert_into_markdown and run_mode != "prototypes":
        print()
        insert_plots_into_all_markdowns(pilot_data_root, plots_subfolder_name=plots_subfolder_name, skip_site_codes=skip_site_codes)
    return result
def mrun_run_all_pilot_plots():
    pass
if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    plots_subfolder_name = "_plots"
    file_formats = ["png", "pdf"]
    overwrite = True
    skip_site_codes = []
    selected_style = "b"
    insert_into_markdown = True
    # run_mode = "prototypes"  # Generates 9 prototype files for ABRM only (3 plots × 3 styles) to compare styles. Skips markdown.
    run_mode = "styled"  # Generates plots using selected_style for ALL sites + aggregate. Production mode.
    # run_mode = "original"  # Generates plots using older non-styled plotting functions for all sites.
    #run_mode = "markdown_only"  # Only inserts image references into markdown files. Does NOT regenerate plots.
    run_all_pilot_plots(pilot_data_root, plots_subfolder_name=plots_subfolder_name, file_formats=file_formats, overwrite=overwrite, skip_site_codes=skip_site_codes, run_mode=run_mode, selected_style=selected_style, insert_into_markdown=insert_into_markdown)


