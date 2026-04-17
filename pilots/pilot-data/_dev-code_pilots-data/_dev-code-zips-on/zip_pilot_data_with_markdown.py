"""
FloodLAMP pilot data zipping utility.

This module creates zip archives of curated CSVs and XLSX files for pilot sites.
It auto-discovers site folders by pattern matching (4 uppercase letters + "_pilot-data")
and creates both per-site and combined zip archives.

Output structure:
  - {SITE}_pilot-data_csvs.zip: Just the curated CSVs for that site
  - {SITE}_pilot-data_csvs-and-xlsx.zip: CSVs + XLSX downloads for that site
  - ZIPALL_pilot-data_csvs.zip: All CSVs from all sites (preserving folder structure)
  - ZIPALL_pilot-data_csvs-and-xlsx.zip: All CSVs and XLSX from all sites

"""

import csv
import datetime
import os
import re
import zipfile

### Constants: errant value patterns
# These patterns indicate data quality issues that should be flagged
ERRANT_PATTERNS = [
    # Excel formula errors
    r"^#REF!$",
    r"^#NAME\?$",
    r"^#VALUE!$",
    r"^#DIV/0!$",
    r"^#N/A$",
    r"^#NULL!$",
    r"^#NUM!$",
    r"^#GETTING_DATA$",
    r"^#SPILL!$",
    # NaN/NaT variants that shouldn't appear as literal strings
    r"^nan$",
    r"^NaN$",
    r"^NaT$",
    r"^NAT$",
    # Placeholder values
    r"^\?+$",  # One or more question marks
    r"^-$",   # Single dash (sometimes used as placeholder)
    r"^n/a$",
    r"^N/A$",
    r"^NA$",
    r"^null$",
    r"^NULL$",
    r"^none$",
    r"^None$",
    r"^undefined$",
    r"^UNDEFINED$",
    # Suspicious patterns
    r"^\s+$",  # Whitespace-only cells
]
# Compile patterns for efficiency
ERRANT_REGEXES = [re.compile(p) for p in ERRANT_PATTERNS]

### Helpers: printing
def _print_section(title):
    """Print a section header.

    :param title: str, section title.
    :return: None
    """
    print(f"=== {title} ===")
def _print_kv(label, value):
    """Print a label/value line.

    :param label: str, label.
    :param value: any, value.
    :return: None
    """
    print(f"{label}: {value}")
def _print_dash():
    """Print a dashed divider.

    :return: None
    """
    print("---")

### Helpers: filesystem
def _ensure_folder(folder_path):
    """Ensure a folder exists.

    :param folder_path: str, folder path.
    :return: str, normalized folder path.
    """
    folder_path = os.path.abspath(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path
def _discover_site_folders(pilot_data_root):
    """Discover site folders by pattern matching.

    Looks for folders matching pattern: 4 uppercase letters + "_pilot-data"
    (e.g., ABRM_pilot-data, BEND_pilot-data)

    :param pilot_data_root: str, path to pilot-data root folder.
    :return sites: list of tuples (site_code, site_folder_path)
    """
    pattern = re.compile(r"^([A-Z]{4})_pilot-data$")
    sites = []

    if not os.path.isdir(pilot_data_root):
        return sites

    for entry in os.listdir(pilot_data_root):
        full_path = os.path.join(pilot_data_root, entry)
        if os.path.isdir(full_path):
            match = pattern.match(entry)
            if match:
                site_code = match.group(1)
                sites.append((site_code, full_path))

    # Sort by site code for deterministic ordering
    sites.sort(key=lambda x: x[0])
    return sites
def _get_csv_folder(site_folder, site_code):
    """Get the curated CSVs folder path for a site.

    Checks for both naming conventions: {SITE}_curated_csvs (plural) and {SITE}_curated_csv (singular).

    :param site_folder: str, path to site folder.
    :param site_code: str, 4-letter site code.
    :return: str or None, path to CSV folder if exists.
    """
    # Try plural first (standard convention)
    csv_folder = os.path.join(site_folder, f"{site_code}_curated_csvs")
    if os.path.isdir(csv_folder):
        return csv_folder
    # Try singular as fallback
    csv_folder = os.path.join(site_folder, f"{site_code}_curated_csv")
    if os.path.isdir(csv_folder):
        return csv_folder
    return None
def _get_xlsx_folder(site_folder, site_code):
    """Get the XLSX downloads folder path for a site.

    :param site_folder: str, path to site folder.
    :param site_code: str, 4-letter site code.
    :return: str or None, path to XLSX folder if exists.
    """
    xlsx_folder = os.path.join(site_folder, f"{site_code}_xlsx_downloads")
    if os.path.isdir(xlsx_folder):
        return xlsx_folder
    return None
def _list_files_in_folder(folder_path, extensions=None):
    """List files in a folder, optionally filtered by extension.

    :param folder_path: str, path to folder.
    :param extensions: list of str or None, file extensions to include (e.g., [".csv", ".xlsx"]).
    :return: list of str, full file paths.
    """
    files = []
    if not os.path.isdir(folder_path):
        return files

    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        if os.path.isfile(full_path):
            if extensions is None:
                files.append(full_path)
            else:
                ext = os.path.splitext(entry)[1].lower()
                if ext in extensions:
                    files.append(full_path)

    files.sort()
    return files

### Helpers: errant value checking
def _is_errant_value(value):
    """Check if a value matches any errant pattern.

    :param value: str, cell value to check.
    :return: bool, True if value matches an errant pattern.
    """
    if not value:
        return False
    value_str = str(value).strip()
    for regex in ERRANT_REGEXES:
        if regex.match(value_str):
            return True
    return False
def _check_csv_for_errant_values(csv_path):
    """Scan a CSV file for errant values.

    :param csv_path: str, path to CSV file.
    :return findings: list of dicts, each with keys: row, col, col_name, value, pattern.
    """
    findings = []
    try:
        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if headers is None:
                return findings

            for row_idx, row in enumerate(reader, start=2):  # Start at 2 (1 for header, 1-indexed)
                for col_idx, value in enumerate(row):
                    if _is_errant_value(value):
                        col_name = headers[col_idx] if col_idx < len(headers) else f"col_{col_idx}"
                        # Determine which pattern matched
                        matched_pattern = None
                        value_str = str(value).strip()
                        for pattern, regex in zip(ERRANT_PATTERNS, ERRANT_REGEXES):
                            if regex.match(value_str):
                                matched_pattern = pattern
                                break
                        findings.append({
                            "row": row_idx,
                            "col": col_idx + 1,  # 1-indexed
                            "col_name": col_name,
                            "value": value,
                            "pattern": matched_pattern,
                        })
    except Exception as e:
        _print_kv("  ERROR reading CSV", f"{csv_path}: {e}")
    return findings
def _check_site_csvs_for_errant_values(csv_folder, site_code):
    """Check all CSVs in a site folder for errant values.

    :param csv_folder: str, path to CSV folder.
    :param site_code: str, 4-letter site code.
    :return results: dict with keys: site_code, csv_count, total_findings, files_with_findings, details.
    """
    results = {
        "site_code": site_code,
        "csv_count": 0,
        "total_findings": 0,
        "files_with_findings": 0,
        "details": {},
    }

    if not csv_folder or not os.path.isdir(csv_folder):
        return results

    csv_files = _list_files_in_folder(csv_folder, extensions=[".csv"])
    results["csv_count"] = len(csv_files)

    for csv_path in csv_files:
        csv_name = os.path.basename(csv_path)
        findings = _check_csv_for_errant_values(csv_path)
        if findings:
            results["files_with_findings"] += 1
            results["total_findings"] += len(findings)
            results["details"][csv_name] = findings

    return results
def check_all_sites_for_errant_values(pilot_data_root):
    """Check all sites for errant values in their curated CSVs.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return all_results: dict with site codes as keys, check results as values.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)

    _print_section("ERRANT VALUE CHECK: SETUP")
    _print_kv("Root folder", pilot_data_root)

    sites = _discover_site_folders(pilot_data_root)
    _print_kv("Sites found", len(sites))
    _print_dash()

    if not sites:
        print("ERROR: No site folders found matching pattern [A-Z]{4}_pilot-data")
        return {"error": "No sites found"}

    all_results = {}
    total_findings = 0
    total_files_with_findings = 0

    _print_section("ERRANT VALUE CHECK: PER-SITE RESULTS")
    for site_code, site_folder in sites:
        csv_folder = _get_csv_folder(site_folder, site_code)
        results = _check_site_csvs_for_errant_values(csv_folder, site_code)
        all_results[site_code] = results

        if results["total_findings"] > 0:
            _print_kv(f"{site_code}", f"ISSUES FOUND: {results['total_findings']} errant values in {results['files_with_findings']} files")
            for csv_name, findings in results["details"].items():
                _print_kv(f"  {csv_name}", f"{len(findings)} errant values")
                # Print first few findings as examples
                for f in findings[:3]:
                    _print_kv(f"    Row {f['row']}, Col '{f['col_name']}'", f"'{f['value']}' (matched {f['pattern']})")
                if len(findings) > 3:
                    _print_kv("    ...", f"and {len(findings) - 3} more")
            total_findings += results["total_findings"]
            total_files_with_findings += results["files_with_findings"]
        else:
            _print_kv(f"{site_code}", f"OK ({results['csv_count']} CSVs checked, no errant values)")
    _print_dash()

    # Summary
    _print_section("ERRANT VALUE CHECK: SUMMARY")
    if total_findings > 0:
        _print_kv("STATUS", "ISSUES FOUND")
        _print_kv("Total errant values", total_findings)
        _print_kv("Files with errant values", total_files_with_findings)
    else:
        _print_kv("STATUS", "ALL CLEAN")
        _print_kv("Total CSVs checked", sum(r["csv_count"] for r in all_results.values()))
    _print_section("ERRANT VALUE CHECK: DONE")

    return all_results
def write_errant_values_report(all_results, output_path):
    """Write a detailed CSV report of all errant values found.

    :param all_results: dict, results from check_all_sites_for_errant_values.
    :param output_path: str, path to output CSV report.
    :return: str, path to written report.
    """
    rows = []
    for site_code, results in all_results.items():
        if "details" not in results:
            continue
        for csv_name, findings in results["details"].items():
            for f in findings:
                rows.append({
                    "site_code": site_code,
                    "csv_file": csv_name,
                    "row": f["row"],
                    "col": f["col"],
                    "col_name": f["col_name"],
                    "value": f["value"],
                    "matched_pattern": f["pattern"],
                })

    if not rows:
        _print_kv("No errant values to report", output_path)
        return None

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    fieldnames = ["site_code", "csv_file", "row", "col", "col_name", "value", "matched_pattern"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _print_kv("Wrote errant values report", f"{output_path} ({len(rows)} rows)")
    return output_path
def _create_zip(zip_path, files_with_arcnames):
    """Create a zip archive with specified files.

    :param zip_path: str, output zip file path.
    :param files_with_arcnames: list of tuples (file_path, arcname), where arcname is the name in the archive.
    :return: int, number of files added to archive.
    """
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path, arcname in files_with_arcnames:
            zf.write(file_path, arcname)

    return len(files_with_arcnames)
def _generate_timestamp():
    """Generate a timestamp string in format YYYY-MM-DD_HHMM.

    :return: str, timestamp string.
    """
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d_%H%M")

### Main functions
def zip_site_data(site_code, site_folder, output_folder):
    """Create zip archives for a single site.

    Creates:
    - {SITE}_pilot-data_csvs.zip: Just the curated CSVs
    - {SITE}_pilot-data_csvs-and-xlsx.zip: CSVs + XLSX downloads

    :param site_code: str, 4-letter site code.
    :param site_folder: str, path to site folder.
    :param output_folder: str, path to output folder for zips.
    :return: dict, summary with zip paths and file counts.
    """
    csv_folder = _get_csv_folder(site_folder, site_code)
    xlsx_folder = _get_xlsx_folder(site_folder, site_code)

    results = {
        "site_code": site_code,
        "csvs_zip": None,
        "csvs_xlsx_zip": None,
        "csv_count": 0,
        "xlsx_count": 0,
        "csv_folder": csv_folder,
        "xlsx_folder": xlsx_folder,
    }

    # Collect CSV files
    csv_files = []
    if csv_folder:
        csv_files = _list_files_in_folder(csv_folder, extensions=[".csv"])
        _print_kv("  CSV folder", f"{os.path.basename(csv_folder)} ({len(csv_files)} .csv files)")
    else:
        _print_kv("  CSV folder", "NOT FOUND (looked for {}_curated_csvs or {}_curated_csv)".format(site_code, site_code))
    results["csv_count"] = len(csv_files)

    # Collect XLSX files
    xlsx_files = []
    if xlsx_folder:
        xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
        _print_kv("  XLSX folder", f"{os.path.basename(xlsx_folder)} ({len(xlsx_files)} .xlsx files)")
    else:
        _print_kv("  XLSX folder", "NOT FOUND (looked for {}_xlsx_downloads)".format(site_code))
    results["xlsx_count"] = len(xlsx_files)

    if not csv_files and not xlsx_files:
        _print_kv("  Skip", "no CSV or XLSX files found")
        return results

    # Create CSVs-only zip
    if csv_files:
        csvs_zip_path = os.path.join(output_folder, f"{site_code}_pilot-data_csvs.zip")
        files_with_arcnames = [(f, os.path.basename(f)) for f in csv_files]
        count = _create_zip(csvs_zip_path, files_with_arcnames)
        results["csvs_zip"] = csvs_zip_path
        _print_kv("  Created", f"{os.path.basename(csvs_zip_path)} ({count} files)")
    else:
        _print_kv("  Skip", f"{site_code}_pilot-data_csvs.zip (no CSV files)")

    # Create CSVs + XLSX zip
    if csv_files or xlsx_files:
        csvs_xlsx_zip_path = os.path.join(output_folder, f"{site_code}_pilot-data_csvs-and-xlsx.zip")
        files_with_arcnames = []
        for f in csv_files:
            files_with_arcnames.append((f, os.path.basename(f)))
        for f in xlsx_files:
            files_with_arcnames.append((f, os.path.basename(f)))
        count = _create_zip(csvs_xlsx_zip_path, files_with_arcnames)
        results["csvs_xlsx_zip"] = csvs_xlsx_zip_path
        _print_kv("  Created", f"{os.path.basename(csvs_xlsx_zip_path)} ({count} files)")

    return results
def zip_all_sites_combined(sites_data, output_folder):
    """Create combined zip archives for all sites.

    Creates:
    - ZIPALL_pilot-data_csvs.zip: All CSVs from all sites (in {SITE}_pilot-data folders)
    - ZIPALL_pilot-data_csvs-and-xlsx.zip: All CSVs and XLSX from all sites

    :param sites_data: list of dicts, site data from zip_site_data calls.
    :param output_folder: str, path to output folder for zips.
    :return: dict, summary with zip paths and file counts.
    """
    results = {
        "zipall_csvs": None,
        "zipall_csvs_xlsx": None,
        "total_csv_count": 0,
        "total_xlsx_count": 0,
    }

    all_csv_files = []
    all_xlsx_files = []

    for site_info in sites_data:
        site_code = site_info["site_code"]
        site_folder = site_info["site_folder"]

        csv_folder = _get_csv_folder(site_folder, site_code)
        xlsx_folder = _get_xlsx_folder(site_folder, site_code)

        # Collect CSV files with folder structure preserved
        if csv_folder:
            csv_files = _list_files_in_folder(csv_folder, extensions=[".csv"])
            csv_folder_name = os.path.basename(csv_folder)
            for f in csv_files:
                # Archive name preserves site folder structure: {SITE}_pilot-data/{actual_csv_folder}/filename.csv
                arcname = os.path.join(
                    f"{site_code}_pilot-data",
                    csv_folder_name,
                    os.path.basename(f)
                )
                all_csv_files.append((f, arcname))

        # Collect XLSX files with folder structure preserved
        if xlsx_folder:
            xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
            xlsx_folder_name = os.path.basename(xlsx_folder)
            for f in xlsx_files:
                # Archive name preserves site folder structure: {SITE}_pilot-data/{actual_xlsx_folder}/filename.xlsx
                arcname = os.path.join(
                    f"{site_code}_pilot-data",
                    xlsx_folder_name,
                    os.path.basename(f)
                )
                all_xlsx_files.append((f, arcname))

    results["total_csv_count"] = len(all_csv_files)
    results["total_xlsx_count"] = len(all_xlsx_files)

    # Create ZIPALL CSVs-only zip
    if all_csv_files:
        zipall_csvs_path = os.path.join(output_folder, "ZIPALL_pilot-data_csvs.zip")
        count = _create_zip(zipall_csvs_path, all_csv_files)
        results["zipall_csvs"] = zipall_csvs_path
        _print_kv("Created", f"{os.path.basename(zipall_csvs_path)} ({count} files)")

    # Create ZIPALL CSVs + XLSX zip
    if all_csv_files or all_xlsx_files:
        zipall_csvs_xlsx_path = os.path.join(output_folder, "ZIPALL_pilot-data_csvs-and-xlsx.zip")
        all_files = all_csv_files + all_xlsx_files
        count = _create_zip(zipall_csvs_xlsx_path, all_files)
        results["zipall_csvs_xlsx"] = zipall_csvs_xlsx_path
        _print_kv("Created", f"{os.path.basename(zipall_csvs_xlsx_path)} ({count} files)")

    return results
def run_zip_pilot_data(pilot_data_root):
    """Main entry point: discover sites, create all zips.

    Creates a timestamped output folder and generates:
    - Per-site zips (CSVs-only and CSVs+XLSX)
    - Combined ZIPALL zips (all sites together)

    :param pilot_data_root: str, path to pilot-data root folder.
    :return: dict, summary of all operations.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)

    _print_section("ZIP PILOT DATA: SETUP")
    _print_kv("Root folder", pilot_data_root)

    # Discover sites
    sites = _discover_site_folders(pilot_data_root)
    _print_kv("Sites found", len(sites))
    for site_code, site_folder in sites:
        _print_kv(f"  {site_code}", os.path.basename(site_folder))
    _print_dash()

    if not sites:
        print("ERROR: No site folders found matching pattern [A-Z]{4}_pilot-data")
        return {"error": "No sites found"}

    # Create timestamped output folder
    timestamp = _generate_timestamp()
    output_folder_name = f"zips_pilot-data_{timestamp}"
    output_folder = os.path.join(pilot_data_root, output_folder_name)
    _ensure_folder(output_folder)

    _print_section("ZIP PILOT DATA: OUTPUT FOLDER")
    _print_kv("Output folder", output_folder)
    _print_dash()

    # Process each site
    _print_section("ZIP PILOT DATA: PER-SITE ZIPS")
    sites_data = []
    for site_code, site_folder in sites:
        _print_kv("Processing", site_code)
        result = zip_site_data(site_code, site_folder, output_folder)
        result["site_folder"] = site_folder
        sites_data.append(result)
    _print_dash()

    # Create combined zips
    _print_section("ZIP PILOT DATA: COMBINED ZIPS")
    combined_result = zip_all_sites_combined(sites_data, output_folder)
    _print_dash()

    # Summary
    _print_section("ZIP PILOT DATA: SUMMARY")
    total_zips = 0
    for site_result in sites_data:
        if site_result["csvs_zip"]:
            total_zips += 1
        if site_result["csvs_xlsx_zip"]:
            total_zips += 1
    if combined_result["zipall_csvs"]:
        total_zips += 1
    if combined_result["zipall_csvs_xlsx"]:
        total_zips += 1

    _print_kv("Total zip files created", total_zips)
    _print_kv("Total CSVs archived", combined_result["total_csv_count"])
    _print_kv("Total XLSX archived", combined_result["total_xlsx_count"])
    _print_kv("Output folder", output_folder)
    _print_section("ZIP PILOT DATA: DONE")

    return {
        "output_folder": output_folder,
        "sites_data": sites_data,
        "combined_result": combined_result,
        "total_zips": total_zips,
    }
def run_errant_check(pilot_data_root, output_report_path=None):
    """Run errant value check on all site CSVs.

    Scans all curated CSVs for errant values like #REF!, NaN, ?, etc.
    Optionally writes a detailed CSV report.

    :param pilot_data_root: str, path to pilot-data root folder.
    :param output_report_path: str or None, optional path for CSV report.
    :return: dict, errant check results by site.
    """
    results = check_all_sites_for_errant_values(pilot_data_root)
    total_errant = sum(r.get("total_findings", 0) for r in results.values() if isinstance(r, dict))

    if total_errant > 0 and output_report_path:
        write_errant_values_report(results, output_report_path)

    return results
def mrun_zip_pilot_data():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    run_zip_pilot_data(pilot_data_root)
def mrun_errant_check():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    run_errant_check(pilot_data_root, output_report_path=pilot_data_root + "/errant_values_report.csv")



### Markdown generation: pilot site summaries
# This section creates per-site archive markdown files based on key curated CSVs.
# It is intentionally conservative: it only reads curated CSVs and writes markdown into each site folder.

PILOT_SITE_MD_FILENAME_TEMPLATE = "{site_code}_pilot-data_summary.md"
# Google Sheets reference CSV files (relative to pilots folder)
GSHEETS_FILENAMES_CSV = "Data PUB - Pilot Data Google Files - PUB Filenames.csv"
GSHEETS_URLS_CSV = "Data PUB - Pilot Data Google Files - PUB URLs.csv"
PILOT_SITE_MD_CATEGORY = "pilot-data"
PILOT_SITE_MD_SUBCATEGORY = "pilot-site"
PILOT_SITE_MD_LICENSE = "CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/"
PILOT_SITE_MD_SKIP_SITE_CODES = set()  # All special cases now handled explicitly
# FLMP is a special case: it contains sub-programs that each get their own markdown
FLMP_SUB_PROGRAMS = ["CRLN", "FLMP", "FLSP"]
# DAVI is a special case: RTR has a custom "referral-antigen-comparison" format instead of standard referral tests
DAVI_ANTIGEN_COMPARISON_CSV = "DAVI_RTR_referral-antigen-comparison.csv"
DAVI_GROUP_DEFINITIONS = [
    {"name": "Group 1", "desc": "Testing between Sept 15th and Dec 23rd (FloodLAMP used as main test and BinaxNOW used sometimes at home on day 0)", "start_row": 13, "end_row": 28},
    {"name": "Group 2", "desc": "Testing between Dec 24th and Jan 9th (Both FloodLAMP and BinaxNOW used until cleared to RTW)", "start_row": 32, "end_row": 56},
    {"name": "Group 3", "desc": "Testing between Jan 10th and Feb 7th (FloodLAMP used for initial + diagnosis and BinaxNOW used to RTW)", "start_row": 58, "end_row": 75},
]
DAVI_AS_REPORTED_COLS = list(range(0, 23))  # Columns A-W (indices 0-22)
DAVI_STRUCTURED_COLS = list(range(23, 34))  # Columns X-AH (indices 23-33)

### Helpers: markdown
def _escape_md_cell(value):
    """Escape a value for safe insertion into a markdown table cell.

    :param value: any, value to escape.
    :return escaped: str, escaped markdown cell value.
    """
    if value is None:
        return ""
    s = str(value)
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = s.replace("|", r"\|")
    s = s.replace("\n", "<br>")
    return s
def _read_csv_rows(csv_path, max_rows=None):
    """Read a CSV file into headers and rows.

    :param csv_path: str, path to CSV file.
    :param max_rows: int or none, optional maximum number of data rows to read.
    :return result: dict, with keys: headers (list of str), rows (list of list of str).
    """
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        if headers is None:
            return {"headers": [], "rows": []}
        rows = []
        for row in reader:
            rows.append(row)
            if max_rows is not None and len(rows) >= max_rows:
                break
    return {"headers": headers, "rows": rows}
def _csv_rows_to_markdown_table(headers, rows):
    """Convert CSV headers/rows to a markdown table string.

    :param headers: list of str, column headers.
    :param rows: list of list of str, row data.
    :return md: str, markdown table.
    """
    if not headers:
        return "_No data._"
    header_line = "| " + " | ".join(_escape_md_cell(h) for h in headers) + " |"
    sep_line = "| " + " | ".join("---" for _ in headers) + " |"
    out_lines = [header_line, sep_line]
    for row in rows:
        padded = list(row) + [""] * (len(headers) - len(row))
        out_lines.append("| " + " | ".join(_escape_md_cell(v) for v in padded[:len(headers)]) + " |")
    return "\n".join(out_lines)

### Helpers: parsing
def _safe_int(value):
    """Parse an integer from a value.

    :param value: any, value to parse.
    :return result: int or none, parsed integer or None if not parseable.
    """
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    try:
        return int(float(s))
    except Exception:
        return None
def _safe_date(value):
    """Parse a YYYY-MM-DD date string and return it if valid.

    :param value: any, input value.
    :return result: str or none, normalized date string or None.
    """
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s
    return None

### Helpers: number formatting for stats tables
def _format_number_with_commas(value):
    """Format a number with commas at thousands places.

    :param value: str or number, value to format.
    :return formatted: str, formatted number or original value if not numeric.
    """
    try:
        num = float(value)
        if num == int(num):
            return f"{int(num):,}"
        else:
            return f"{num:,}"
    except (ValueError, TypeError):
        return str(value)
def _format_percentage(value):
    """Format a decimal value as a percentage with one decimal place.

    :param value: str or number, decimal value (e.g., 0.25 for 25%).
    :return formatted: str, percentage string (e.g., "25.0%").
    """
    try:
        num = float(value)
        return f"{num * 100:.1f}%"
    except (ValueError, TypeError):
        return str(value)
def _format_stats_value(value, metric):
    """Format a stats key-value based on the metric name.

    Rules:
    - Average Pool Level: round to 1 decimal place
    - Percentages (metric contains "%" or "Percent"): format as X.X%
    - Other numbers: add commas at thousands place

    :param value: str, the value to format.
    :param metric: str, the metric name.
    :return formatted: str, formatted value.
    """
    if value is None:
        return ""
    value_str = str(value).strip()
    if not value_str:
        return ""
    # Check if it's a numeric value
    try:
        num = float(value_str)
    except (ValueError, TypeError):
        # Not numeric, return as-is
        return value_str
    # Check for Average Pool Level - round to 1 decimal
    if "pool level" in metric.lower() or "avgerage pool" in metric.lower():
        return f"{num:.1f}"
    # Check for percentage metrics
    if "%" in metric or "percent" in metric.lower() or "pct" in metric.lower():
        # Value is already a decimal (e.g., 0.25), format as percentage
        return f"{num * 100:.1f}%"
    # Check if value looks like a raw percentage (decimal between 0 and 1, exclusive)
    # but only if metric suggests it's a ratio/rate
    if 0 < num < 1 and ("rate" in metric.lower() or "ratio" in metric.lower()):
        return f"{num * 100:.1f}%"
    # Regular number - format with commas
    if num == int(num):
        return f"{int(num):,}"
    else:
        # Keep reasonable precision for decimals
        return f"{num:,.2f}"
def _format_stats_kv_rows(headers, rows):
    """Format stats key-values rows with proper number formatting.

    :param headers: list of str, column headers.
    :param rows: list of list of str, row data.
    :return formatted_rows: list of list of str, formatted row data.
    """
    # Find the indices for 'metric' and 'value' columns
    metric_idx = None
    value_idx = None
    for i, h in enumerate(headers):
        h_lower = h.lower().strip()
        if h_lower == "metric":
            metric_idx = i
        elif h_lower == "value":
            value_idx = i
    if metric_idx is None or value_idx is None:
        # Can't format without both columns
        return rows
    formatted_rows = []
    for row in rows:
        new_row = list(row)
        if len(new_row) > max(metric_idx, value_idx):
            metric = new_row[metric_idx]
            value = new_row[value_idx]
            new_row[value_idx] = _format_stats_value(value, metric)
        formatted_rows.append(new_row)
    return formatted_rows

### Helpers: pilot data discovery
def _choose_weekly_csv_path(csv_folder, site_code):
    """Choose the best available weekly summary CSV for a site.

    Preference order: APS weekly, then RFR weekly, then RSR weekly.

    :param csv_folder: str, path to curated CSV folder.
    :param site_code: str, 4-letter site code.
    :return path: str or none, chosen weekly summary CSV path.
    """
    candidates = [
        os.path.join(csv_folder, f"{site_code}_APS_weekly-summary.csv"),
        os.path.join(csv_folder, f"{site_code}_RFR_weekly-summary.csv"),
        os.path.join(csv_folder, f"{site_code}_RSR_weekly-summary.csv"),
    ]
    for p in candidates:
        if os.path.isfile(p):
            return p
    return None
def _find_key_csv_paths(csv_folder, site_code):
    """Find key curated CSV paths used for site markdown generation.

    :param csv_folder: str, path to curated CSV folder.
    :param site_code: str, 4-letter site code.
    :return result: dict, keys: stats_kv_csv, weekly_csv, rtr_by_person_csv.
    """
    stats_kv_csv = os.path.join(csv_folder, f"{site_code}_APS_stats_key-values.csv")
    if not os.path.isfile(stats_kv_csv):
        stats_kv_csv = None
    weekly_csv = _choose_weekly_csv_path(csv_folder, site_code)
    rtr_by_person_csv = os.path.join(csv_folder, f"{site_code}_RTR_referral-tests-by-person.csv")
    if not os.path.isfile(rtr_by_person_csv):
        rtr_by_person_csv = None
    return {
        "stats_kv_csv": stats_kv_csv,
        "weekly_csv": weekly_csv,
        "rtr_by_person_csv": rtr_by_person_csv,
    }
def _list_xlsx_links_for_site(site_folder, site_code):
    """List XLSX download links (relative paths) for a site.

    :param site_folder: str, site folder path.
    :param site_code: str, 4-letter site code.
    :return links: list of dict, each with keys: label, relpath.
    """
    xlsx_folder = _get_xlsx_folder(site_folder, site_code)
    if not xlsx_folder:
        return []
    xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
    links = []
    xlsx_folder_name = os.path.basename(xlsx_folder)
    for fp in xlsx_files:
        links.append({"label": os.path.basename(fp), "relpath": os.path.join(xlsx_folder_name, os.path.basename(fp))})
    return links
def _load_gsheets_lookup(pilot_data_root):
    """Load Google Sheets filename and URL lookup from CSV files.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return lookup: dict, keyed by site acronym, with dict of file types to {filename, url}.
    """
    pilots_folder = os.path.dirname(pilot_data_root)
    filenames_csv = os.path.join(pilots_folder, GSHEETS_FILENAMES_CSV)
    urls_csv = os.path.join(pilots_folder, GSHEETS_URLS_CSV)
    if not os.path.isfile(filenames_csv) or not os.path.isfile(urls_csv):
        return {}
    # Read both CSVs
    with open(filenames_csv, "r", encoding="utf-8", newline="") as f:
        filenames_reader = csv.DictReader(f)
        filenames_rows = list(filenames_reader)
    with open(urls_csv, "r", encoding="utf-8", newline="") as f:
        urls_reader = csv.DictReader(f)
        urls_rows = list(urls_reader)
    # Build lookup keyed by Acronym
    lookup = {}
    file_type_cols = ["APS GDrive File", "RFR GDrive File", "RTR GDrive File", "RSR GDrive File", "Stats and Weekly"]
    for fn_row, url_row in zip(filenames_rows, urls_rows):
        acronym = fn_row.get("Acronym", "").strip()
        if not acronym:
            continue
        site_data = {}
        for col in file_type_cols:
            filename = fn_row.get(col, "").strip()
            url = url_row.get(col, "").strip()
            # Skip NA values and special notes
            if filename and url and not filename.upper().startswith("NA") and url.startswith("http"):
                site_data[col] = {"filename": filename, "url": url}
        if site_data:
            lookup[acronym] = site_data
    return lookup
def _get_gsheets_links_for_site(gsheets_lookup, site_code):
    """Get Google Sheets links for a site from the lookup.

    :param gsheets_lookup: dict, lookup from _load_gsheets_lookup.
    :param site_code: str, 4-letter site code.
    :return links: list of dict, each with keys: label, url.
    """
    site_data = gsheets_lookup.get(site_code, {})
    links = []
    for col, data in site_data.items():
        links.append({"label": data["filename"], "url": data["url"]})
    return links

### Helpers: weekly totals
def _compute_weekly_totals(weekly_csv_path):
    """Compute total tubes/positives/participants from a weekly summary CSV.

    :param weekly_csv_path: str, path to weekly summary CSV.
    :return totals: dict, totals and date range.
    """
    totals = {
        "week_start_min": None,
        "week_end_max": None,
        "participants_total": None,
        "tubes_total": None,
        "positive_tubes_total": None,
        "inconclusive_tubes_total": None,
    }
    if not weekly_csv_path or not os.path.isfile(weekly_csv_path):
        return totals

    with open(weekly_csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        participants_sum = 0
        tubes_sum = 0
        pos_sum = 0
        inc_sum = 0
        has_participants = False
        has_tubes = False
        has_pos = False
        has_inc = False
        week_start_min = None
        week_end_max = None

        for row in reader:
            ws = _safe_date(row.get("week_start_date"))
            we = _safe_date(row.get("week_end_date"))
            if ws and (week_start_min is None or ws < week_start_min):
                week_start_min = ws
            if we and (week_end_max is None or we > week_end_max):
                week_end_max = we

            p = _safe_int(row.get("participants_n"))
            t = _safe_int(row.get("tubes_n"))
            pos = _safe_int(row.get("positive_tubes_n"))
            inc = _safe_int(row.get("inconclusive_tubes_n"))

            if p is not None:
                participants_sum += p
                has_participants = True
            if t is not None:
                tubes_sum += t
                has_tubes = True
            if pos is not None:
                pos_sum += pos
                has_pos = True
            if inc is not None:
                inc_sum += inc
                has_inc = True

    totals["week_start_min"] = week_start_min
    totals["week_end_max"] = week_end_max
    totals["participants_total"] = participants_sum if has_participants else None
    totals["tubes_total"] = tubes_sum if has_tubes else None
    totals["positive_tubes_total"] = pos_sum if has_pos else None
    totals["inconclusive_tubes_total"] = inc_sum if has_inc else None
    return totals

### Markdown generation: rendering
def _render_site_pilot_data_markdown(site_code, site_folder, csv_folder, key_csv_paths, md_filename, gsheets_lookup=None):
    """Render a site pilot-data summary markdown document.

    :param site_code: str, 4-letter site code.
    :param site_folder: str, site folder path.
    :param csv_folder: str, curated CSV folder path.
    :param key_csv_paths: dict, key CSV paths (stats_kv_csv, weekly_csv, rtr_by_person_csv).
    :param md_filename: str, markdown file name (not full path).
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :return md_text: str, markdown document content.
    """
    today = datetime.date.today().isoformat()
    weekly_totals = _compute_weekly_totals(key_csv_paths.get("weekly_csv"))

    title = f"{site_code} Pilot Data Summary"
    summary_parts = []
    if weekly_totals.get("tubes_total") is not None:
        summary_parts.append(f"Total tubes run: {weekly_totals['tubes_total']}")
    if weekly_totals.get("positive_tubes_total") is not None:
        summary_parts.append(f"Total positive tubes: {weekly_totals['positive_tubes_total']}")
    if weekly_totals.get("participants_total") is not None:
        summary_parts.append(f"Total participants: {weekly_totals['participants_total']}")
    if weekly_totals.get("week_start_min") and weekly_totals.get("week_end_max"):
        summary_parts.append(f"Date range: {weekly_totals['week_start_min']} to {weekly_totals['week_end_max']}")
    summary_short = f"Site {site_code} FloodLAMP pilot data summary based on curated CSV extracts."
    if summary_parts:
        summary_short = summary_short + " " + "; ".join(summary_parts) + "."

    md_lines = []
    md_lines.append("METADATA")
    md_lines.append(f"last updated: {today}")
    md_lines.append(f"file_name: {md_filename}")
    md_lines.append(f"file_date: {today}")
    md_lines.append(f"title: {title}")
    md_lines.append(f"category: {PILOT_SITE_MD_CATEGORY}")
    md_lines.append(f"subcategory: {PILOT_SITE_MD_SUBCATEGORY}")
    md_lines.append("tags: ")
    md_lines.append("source_file_type: csv")
    md_lines.append("xfile_type: xlsx")
    md_lines.append(f"license: {PILOT_SITE_MD_LICENSE}")
    md_lines.append("notes: ")
    md_lines.append(f"summary_short: {summary_short}")
    md_lines.append("")
    md_lines.append("CONTENT")
    md_lines.append("")
    md_lines.append("## Files")
    md_lines.append("")
    md_lines.append("### Google Sheets URLs")
    gsheets_links = _get_gsheets_links_for_site(gsheets_lookup or {}, site_code)
    if gsheets_links:
        for link in gsheets_links:
            md_lines.append(f"- [{link['label']}]({link['url']})")
    else:
        md_lines.append("_not available_")
    md_lines.append("")
    md_lines.append("### Curated CSVs")
    csv_folder_name = os.path.basename(csv_folder)
    md_lines.append(f"- Curated CSV folder: `{csv_folder_name}/`")
    if key_csv_paths.get("stats_kv_csv"):
        rel_stats = os.path.join(csv_folder_name, os.path.basename(key_csv_paths["stats_kv_csv"]))
        md_lines.append(f"- Stats key-values CSV: [{os.path.basename(key_csv_paths['stats_kv_csv'])}]({rel_stats})")
    else:
        md_lines.append("- Stats key-values CSV: _not available_")
    if key_csv_paths.get("weekly_csv"):
        rel_weekly = os.path.join(csv_folder_name, os.path.basename(key_csv_paths["weekly_csv"]))
        md_lines.append(f"- Weekly summary CSV: [{os.path.basename(key_csv_paths['weekly_csv'])}]({rel_weekly})")
    else:
        md_lines.append("- Weekly summary CSV: _not available_")
    if key_csv_paths.get("rtr_by_person_csv"):
        rel_rtr = os.path.join(csv_folder_name, os.path.basename(key_csv_paths["rtr_by_person_csv"]))
        md_lines.append(f"- Referral tests by person CSV: [{os.path.basename(key_csv_paths['rtr_by_person_csv'])}]({rel_rtr})")
    else:
        md_lines.append("- Referral tests by person CSV: _not available_")
    md_lines.append("")
    md_lines.append("### XLSX downloads:")
    xlsx_links = _list_xlsx_links_for_site(site_folder, site_code)
    if xlsx_links:
        for x in xlsx_links:
            md_lines.append(f"- [{x['label']}]({x['relpath']})")
    else:
        md_lines.append("_not available_")
    md_lines.append("")
    md_lines.append("## Key tables")
    md_lines.append("")
    md_lines.append("### Stats key-values")
    md_lines.append("")
    if key_csv_paths.get("stats_kv_csv"):
        stats_data = _read_csv_rows(key_csv_paths["stats_kv_csv"])
        formatted_rows = _format_stats_kv_rows(stats_data["headers"], stats_data["rows"])
        md_lines.append(_csv_rows_to_markdown_table(stats_data["headers"], formatted_rows))
    else:
        md_lines.append("_Stats key-values CSV not found for this site._")
    md_lines.append("")
    md_lines.append("### Weekly summary")
    md_lines.append("")
    if key_csv_paths.get("weekly_csv"):
        weekly_data = _read_csv_rows(key_csv_paths["weekly_csv"])
        md_lines.append(_csv_rows_to_markdown_table(weekly_data["headers"], weekly_data["rows"]))
    else:
        md_lines.append("_Weekly summary CSV not found for this site._")
    if key_csv_paths.get("rtr_by_person_csv"):
        md_lines.append("")
        md_lines.append("### Referral tests by person")
        md_lines.append("")
        rtr_data = _read_csv_rows(key_csv_paths["rtr_by_person_csv"])
        md_lines.append(_csv_rows_to_markdown_table(rtr_data["headers"], rtr_data["rows"]))
    md_lines.append("")
    return "\n".join(md_lines)

### Main functions: markdown generation
def write_site_pilot_data_markdown(site_code, site_folder, gsheets_lookup=None):
    """Write a pilot-data summary markdown file for a single site.

    :param site_code: str, 4-letter site code.
    :param site_folder: str, site folder path.
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :return result: dict, summary with output path and file availability.
    """
    csv_folder = _get_csv_folder(site_folder, site_code)
    if not csv_folder:
        return {"site_code": site_code, "written": False, "reason": "csv_folder_not_found"}
    if site_code in PILOT_SITE_MD_SKIP_SITE_CODES:
        return {"site_code": site_code, "written": False, "reason": "site_skipped"}
    key_csv_paths = _find_key_csv_paths(csv_folder, site_code)
    md_filename = PILOT_SITE_MD_FILENAME_TEMPLATE.format(site_code=site_code)
    md_path = os.path.join(site_folder, md_filename)
    md_text = _render_site_pilot_data_markdown(site_code, site_folder, csv_folder, key_csv_paths, md_filename, gsheets_lookup)
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    return {"site_code": site_code, "written": True, "md_path": md_path, "key_csv_paths": key_csv_paths}
def write_flmp_pilot_data_markdowns(site_folder, gsheets_lookup=None):
    """Write pilot-data summary markdown files for FLMP's sub-programs.

    FLMP is special: it contains multiple programs (CRLN, FLMP, FLSP) in one folder.
    Each program gets its own markdown file.

    :param site_folder: str, path to FLMP_pilot-data folder.
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :return results: list of dict, one result per sub-program.
    """
    results = []
    # FLMP uses its own curated_csvs folder for all sub-programs
    csv_folder = _get_csv_folder(site_folder, "FLMP")
    if not csv_folder:
        return [{"program_code": p, "written": False, "reason": "csv_folder_not_found"} for p in FLMP_SUB_PROGRAMS]
    for program_code in FLMP_SUB_PROGRAMS:
        key_csv_paths = _find_key_csv_paths(csv_folder, program_code)
        md_filename = PILOT_SITE_MD_FILENAME_TEMPLATE.format(site_code=program_code)
        md_path = os.path.join(site_folder, md_filename)
        md_text = _render_site_pilot_data_markdown(program_code, site_folder, csv_folder, key_csv_paths, md_filename, gsheets_lookup)
        with open(md_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(md_text)
        results.append({"program_code": program_code, "written": True, "md_path": md_path, "key_csv_paths": key_csv_paths})
    return results

### DAVI special handling: referral antigen comparison
def _parse_davi_antigen_comparison_csv(csv_path):
    """Parse the DAVI RTR referral-antigen-comparison CSV into structured sections.

    :param csv_path: str, path to the CSV file.
    :return parsed: dict with keys: summary, legend, groups.
    """
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    # Summary table: rows 2-7 (1-indexed: 3-8), columns 27-30
    summary = {
        "headers": ["", "FL +, B -", "FL +, B +"],
        "rows": [
            ["Asymptomatic", rows[3][27] if len(rows[3]) > 27 else "", rows[3][28] if len(rows[3]) > 28 else ""],
            ["Symptomatic", rows[4][27] if len(rows[4]) > 27 else "", rows[4][28] if len(rows[4]) > 28 else ""],
            ["Total", rows[5][27] if len(rows[5]) > 27 else "", rows[5][28] if len(rows[5]) > 28 else "", rows[5][29] if len(rows[5]) > 29 else ""],
            ["% Asymp", rows[6][27] if len(rows[6]) > 27 else "", _format_pct(rows[6][28]) if len(rows[6]) > 28 else ""],
        ],
    }
    # Legend: extracted from rows 5-9, columns 3-11
    legend = [
        ("FL", "FloodLAMP"),
        ("B", "BinaxNOW Rapid Antigen"),
        ("ASY", "Asymptomatic"),
        ("SYM", "Symptomatic"),
        ("RTW", "Return To Work"),
        ("V1/V2/V3", "Vaccinated 1/2/3 doses"),
        ("UN", "Unvaccinated"),
    ]
    # Additional legend info from rows 8-9
    legend_extra = [
        "+ on FloodLAMP and - on BinaxNOW: " + str(rows[7][10] if len(rows[7]) > 10 else ""),
        "+ on FloodLAMP and + on BinaxNOW: " + str(rows[8][10] if len(rows[8]) > 10 else "") + " (" + _format_pct(rows[8][11]) + ")" if len(rows[8]) > 11 else "",
    ]
    # Headers from row 11 (0-indexed: 10)
    header_row = rows[10] if len(rows) > 10 else []
    as_reported_headers = [header_row[i] if i < len(header_row) else "" for i in DAVI_AS_REPORTED_COLS]
    structured_headers = [header_row[i] if i < len(header_row) else "" for i in DAVI_STRUCTURED_COLS]
    # Clean up multi-line headers (they have embedded newlines in CSV)
    as_reported_headers = [h.replace("\n", " ").strip() for h in as_reported_headers]
    structured_headers = [h.replace("\n", " ").strip() for h in structured_headers]
    # Parse groups
    groups = []
    for gdef in DAVI_GROUP_DEFINITIONS:
        group_rows_as_reported = []
        group_rows_structured = []
        for row_idx in range(gdef["start_row"], gdef["end_row"] + 1):
            if row_idx >= len(rows):
                break
            row = rows[row_idx]
            # Skip empty rows
            if not any(row):
                continue
            as_reported = [row[i] if i < len(row) else "" for i in DAVI_AS_REPORTED_COLS]
            structured = [row[i] if i < len(row) else "" for i in DAVI_STRUCTURED_COLS]
            # Only include rows that have employee data (col 5 should have a numeric employee number)
            employee_val = row[5] if len(row) > 5 else ""
            try:
                int(employee_val)
                is_data_row = True
            except (ValueError, TypeError):
                is_data_row = False
            if is_data_row:
                group_rows_as_reported.append(as_reported)
                group_rows_structured.append(structured)
        groups.append({
            "name": gdef["name"],
            "desc": gdef["desc"],
            "as_reported_headers": as_reported_headers,
            "as_reported_rows": group_rows_as_reported,
            "structured_headers": structured_headers,
            "structured_rows": group_rows_structured,
        })
    return {
        "summary": summary,
        "legend": legend,
        "legend_extra": legend_extra,
        "groups": groups,
    }
def _format_pct(value):
    """Format a decimal value as a percentage string.

    :param value: str or float, decimal value.
    :return formatted: str, percentage string.
    """
    try:
        v = float(value)
        return f"{v * 100:.1f}%"
    except (ValueError, TypeError):
        return str(value)
def _render_davi_antigen_comparison_markdown(parsed):
    """Render the parsed DAVI antigen comparison data as markdown.

    :param parsed: dict, output from _parse_davi_antigen_comparison_csv.
    :return md_text: str, markdown content.
    """
    lines = []
    # Summary section
    lines.append("## Summary: Same Day Test Comparison")
    lines.append("")
    lines.append("Comparison of FloodLAMP (FL) and BinaxNOW (B) same-day test results:")
    lines.append("")
    summary = parsed["summary"]
    lines.append("| " + " | ".join(summary["headers"]) + " |")
    lines.append("| " + " | ".join(["---"] * len(summary["headers"])) + " |")
    for row in summary["rows"]:
        lines.append("| " + " | ".join([_escape_md_cell(c) for c in row[:len(summary["headers"])]]) + " |")
    lines.append("")
    # Legend section
    lines.append("## Legend")
    lines.append("")
    lines.append("| Abbreviation | Meaning |")
    lines.append("| --- | --- |")
    for abbr, meaning in parsed["legend"]:
        lines.append(f"| {abbr} | {meaning} |")
    lines.append("")
    if parsed["legend_extra"]:
        for extra in parsed["legend_extra"]:
            if extra:
                lines.append(f"- {extra}")
        lines.append("")
    # Group sections
    for group in parsed["groups"]:
        lines.append(f"## {group['name']}")
        lines.append("")
        lines.append(f"_{group['desc']}_")
        lines.append("")
        # As Reported table
        lines.append("### As Reported")
        lines.append("")
        if group["as_reported_rows"]:
            # Filter to non-empty headers for cleaner table
            headers = group["as_reported_headers"]
            lines.append("| " + " | ".join([_escape_md_cell(h) for h in headers]) + " |")
            lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
            for row in group["as_reported_rows"]:
                lines.append("| " + " | ".join([_escape_md_cell(c) for c in row]) + " |")
        else:
            lines.append("_No data rows for this group._")
        lines.append("")
        # Structured table
        lines.append("### Structured")
        lines.append("")
        if group["structured_rows"]:
            headers = group["structured_headers"]
            lines.append("| " + " | ".join([_escape_md_cell(h) for h in headers]) + " |")
            lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
            for row in group["structured_rows"]:
                lines.append("| " + " | ".join([_escape_md_cell(c) for c in row]) + " |")
        else:
            lines.append("_No structured data rows for this group._")
        lines.append("")
    return "\n".join(lines)
def _render_davi_pilot_data_markdown(site_folder, csv_folder, md_filename, gsheets_lookup=None):
    """Render the full DAVI pilot data markdown including the antigen comparison section.

    :param site_folder: str, path to DAVI_pilot-data folder.
    :param csv_folder: str, path to DAVI_curated_csvs folder.
    :param md_filename: str, output filename for metadata.
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :return md_text: str, markdown content.
    """
    today = datetime.date.today().isoformat()
    site_code = "DAVI"
    md_lines = []
    # Metadata block
    md_lines.append("METADATA")
    md_lines.append(f"last updated: {today}")
    md_lines.append(f"file_name: {md_filename}")
    md_lines.append(f"file_date: {today}")
    md_lines.append(f"title: {site_code} Pilot Data Summary")
    md_lines.append(f"category: {PILOT_SITE_MD_CATEGORY}")
    md_lines.append(f"subcategory: {PILOT_SITE_MD_SUBCATEGORY}")
    md_lines.append("tags: ")
    md_lines.append("source_file_type: csv")
    md_lines.append("xfile_type: xlsx")
    md_lines.append(f"license: {PILOT_SITE_MD_LICENSE}")
    md_lines.append("notes: DAVI has a custom referral-antigen-comparison format instead of standard referral tests.")
    md_lines.append(f"summary_short: Site {site_code} FloodLAMP pilot data summary with referral antigen comparison.")
    md_lines.append("")
    md_lines.append("CONTENT")
    md_lines.append("")
    # Files section
    md_lines.append("## Files")
    md_lines.append("")
    md_lines.append("### Google Sheets URLs")
    gsheets_links = _get_gsheets_links_for_site(gsheets_lookup or {}, site_code)
    if gsheets_links:
        for link in gsheets_links:
            md_lines.append(f"- [{link['label']}]({link['url']})")
    else:
        md_lines.append("_not available_")
    md_lines.append("")
    md_lines.append("### Curated CSVs")
    csv_folder_name = os.path.basename(csv_folder)
    md_lines.append(f"- Curated CSV folder: `{csv_folder_name}/`")
    # List CSVs
    csv_files = _list_files_in_folder(csv_folder, extensions=[".csv"])
    for fp in csv_files:
        fname = os.path.basename(fp)
        md_lines.append(f"- [{fname}]({csv_folder_name}/{fname})")
    md_lines.append("")
    md_lines.append("### XLSX downloads:")
    # XLSX links
    xlsx_folder = _get_xlsx_folder(site_folder, site_code)
    if xlsx_folder:
        xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
        xlsx_folder_name = os.path.basename(xlsx_folder)
        for fp in xlsx_files:
            fname = os.path.basename(fp)
            md_lines.append(f"- [{fname}]({xlsx_folder_name}/{fname})")
    else:
        md_lines.append("_not available_")
    md_lines.append("")
    # Antigen comparison section
    antigen_csv_path = os.path.join(csv_folder, DAVI_ANTIGEN_COMPARISON_CSV)
    if os.path.isfile(antigen_csv_path):
        parsed = _parse_davi_antigen_comparison_csv(antigen_csv_path)
        md_lines.append(_render_davi_antigen_comparison_markdown(parsed))
    else:
        md_lines.append("## Referral Antigen Comparison")
        md_lines.append("")
        md_lines.append("_Referral antigen comparison CSV not found._")
        md_lines.append("")
    return "\n".join(md_lines)
def write_davi_pilot_data_markdown(site_folder, gsheets_lookup=None):
    """Write the pilot-data summary markdown file for DAVI.

    DAVI is special: it has a custom referral-antigen-comparison format.

    :param site_folder: str, path to DAVI_pilot-data folder.
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :return result: dict, summary with output path.
    """
    site_code = "DAVI"
    csv_folder = _get_csv_folder(site_folder, site_code)
    if not csv_folder:
        return {"site_code": site_code, "written": False, "reason": "csv_folder_not_found"}
    md_filename = "DAVI_pilot-data_referral-antigen-comparison.md"
    md_path = os.path.join(site_folder, md_filename)
    md_text = _render_davi_pilot_data_markdown(site_folder, csv_folder, md_filename, gsheets_lookup)
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    return {"site_code": site_code, "written": True, "md_path": md_path}
def write_all_sites_pilot_data_markdowns(pilot_data_root):
    """Write pilot-data summary markdown files for all discovered sites.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return results: dict, per-site results and totals.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    _print_section("PILOT DATA MARKDOWN: SETUP")
    _print_kv("Root folder", pilot_data_root)
    sites = _discover_site_folders(pilot_data_root)
    _print_kv("Sites found", len(sites))
    # Load Google Sheets lookup
    gsheets_lookup = _load_gsheets_lookup(pilot_data_root)
    _print_kv("Google Sheets sites loaded", len(gsheets_lookup))
    _print_dash()
    results = {"sites": {}, "written": 0, "skipped": 0, "errors": 0}
    _print_section("PILOT DATA MARKDOWN: PER-SITE")
    for site_code, site_folder in sites:
        # FLMP is special: it has sub-programs that each get their own markdown
        if site_code == "FLMP":
            flmp_results = write_flmp_pilot_data_markdowns(site_folder, gsheets_lookup)
            results["sites"]["FLMP"] = {"sub_programs": flmp_results}
            for sub_r in flmp_results:
                if sub_r.get("written"):
                    results["written"] += 1
                    _print_kv(f"FLMP/{sub_r['program_code']}", f"WROTE {os.path.basename(sub_r['md_path'])}")
                else:
                    results["skipped"] += 1
                    _print_kv(f"FLMP/{sub_r['program_code']}", f"SKIP ({sub_r.get('reason')})")
            continue
        # DAVI is special: it has a custom referral-antigen-comparison format
        if site_code == "DAVI":
            r = write_davi_pilot_data_markdown(site_folder, gsheets_lookup)
            results["sites"]["DAVI"] = r
            if r.get("written"):
                results["written"] += 1
                _print_kv(site_code, f"WROTE {os.path.basename(r['md_path'])}")
            else:
                results["skipped"] += 1
                _print_kv(site_code, f"SKIP ({r.get('reason')})")
            continue
        r = write_site_pilot_data_markdown(site_code, site_folder, gsheets_lookup)
        results["sites"][site_code] = r
        if r.get("written"):
            results["written"] += 1
            _print_kv(site_code, f"WROTE {os.path.basename(r['md_path'])}")
        else:
            results["skipped"] += 1
            _print_kv(site_code, f"SKIP ({r.get('reason')})")
    _print_dash()
    _print_section("PILOT DATA MARKDOWN: SUMMARY")
    _print_kv("Markdown files written", results["written"])
    _print_kv("Sites skipped", results["skipped"])
    _print_section("PILOT DATA MARKDOWN: DONE")
    return results
def mrun_write_all_sites_pilot_data_markdowns():
    pass
if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    write_all_sites_pilot_data_markdowns(pilot_data_root)
