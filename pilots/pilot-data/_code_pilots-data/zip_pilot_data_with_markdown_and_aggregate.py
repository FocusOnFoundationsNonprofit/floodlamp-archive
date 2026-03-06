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

### Constants: folder names
AGGREGATE_FOLDER_NAME = "aggregate_pilot-data"
# Skip CRLN and FLSP in aggregation because they are sub-programs of FLMP (would cause double-counting)
AGGREGATE_SKIP_SITE_CODES = {"CRLN", "FLSP"}

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
def _get_latest_zips_folder(pilot_data_root):
    """Find the most recent zips_pilot-data_{timestamp} folder.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return: str or none, path to latest zips folder or None if not found.
    """
    pattern = re.compile(r"^zips_pilot-data_(\d{4}-\d{2}-\d{2}_\d{4})$")
    matches = []
    if not os.path.isdir(pilot_data_root):
        return None
    for entry in os.listdir(pilot_data_root):
        full_path = os.path.join(pilot_data_root, entry)
        if os.path.isdir(full_path):
            match = pattern.match(entry)
            if match:
                timestamp_str = match.group(1)
                matches.append((timestamp_str, full_path))
    if not matches:
        return None
    # Sort by timestamp string (lexicographic works for YYYY-MM-DD_HHMM format)
    matches.sort(key=lambda x: x[0], reverse=True)
    return matches[0][1]
def _get_zipall_csvs_path(zips_folder):
    """Get the ZIPALL_pilot-data_csvs.zip path from a zips folder.

    :param zips_folder: str, path to a zips_pilot-data_{timestamp} folder.
    :return: str or none, path to ZIPALL CSVs zip or None if not found.
    """
    if not zips_folder or not os.path.isdir(zips_folder):
        return None
    zipall_path = os.path.join(zips_folder, "ZIPALL_pilot-data_csvs.zip")
    if os.path.isfile(zipall_path):
        return zipall_path
    return None

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
def _safe_float(value):
    """Parse a float from a value.

    :param value: any, value to parse.
    :return result: float or none, parsed float or None if not parseable.
    """
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    try:
        return float(s)
    except Exception:
        return None

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
    print()  # Blank line before errant check output
    results = check_all_sites_for_errant_values(pilot_data_root)
    total_errant = sum(r.get("total_findings", 0) for r in results.values() if isinstance(r, dict))

    if output_report_path:
        if total_errant > 0:
            write_errant_values_report(results, output_report_path)
        elif os.path.exists(output_report_path):
            # Clear the report file when no issues found to avoid stale data
            os.remove(output_report_path)
            _print_kv("Cleared stale report", os.path.basename(output_report_path))

    print()  # Blank line after errant check output
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

### Aggregation: cross-site rollups
# Sections to skip in aggregation (site-specific, not aggregatable)
AGGREGATE_STATS_SKIP_SECTIONS = {"Files", "Info"}
# Reference stats metrics CSV path (relative to pilot-data root)
REFERENCE_STATS_METRICS_CSV = "reference_stats_metrics.csv"
# Special calculation formulas for metrics that aren't simple sums
# Key is metric name (matched case-insensitively), value is calculation config
AGGREGATE_METRIC_FORMULAS = {
    # Derived sums (add multiple metrics together)
    "Sum of Participant Results plus ARF Tubes": {"kind": "derived_sum", "numerator_ids": ["participant_results", "arf_tubes"]},
    "Total Number of Inconclusive Tubes": {"kind": "derived_sum", "numerator_ids": ["inconclusive_tubes_final", "inconclusive_not_in_aps"]},
    # Ratios with special denominator calculation
    "Average Pool Level (excludes ARF)": {"kind": "ratio_diff_denom", "numerator_id": "participant_results", "denom_id": "tubes_tested_initial", "denom_subtract_id": "arf_tubes"},
    # Simple ratios (numerator / denominator)
    "Re-run % of Tubes": {"kind": "ratio", "numerator_id": "rerun_tubes", "denom_id": "tubes_tested_initial"},
    "% Initial Runs with Re-runs": {"kind": "ratio", "numerator_id": "initial_runs_with_reruns", "denom_id": "initial_runs"},
    "% of Tubes Positives (Final Result)": {"kind": "ratio", "numerator_id": "positive_tubes_final", "denom_id": "tubes_tested_initial"},
    "% of Tubes Inconclusive": {"kind": "ratio", "numerator_id": "total_inconclusive_tubes", "denom_id": "tubes_tested_initial"},
    "% Inconclusives resolved Positive by Referral Tests": {"kind": "ratio", "numerator_id": "inconclusive_resolved_pos", "denom_id": "total_inconclusive_tubes"},
    "% Tube Tests Run Called Inconclusive": {"kind": "ratio", "numerator_id": "inconclusive_run_calls", "denom_id": "tube_tests_run_total"},
    "% FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive": {"kind": "ratio_sum_numerators", "numerator_ids": ["agree_positives", "incl_ref_pos"], "denom_id": "cases_with_referral"},
    "% of Population FloodLAMP Positive (excluding pools not deconv)": {"kind": "ratio", "numerator_id": "unique_positive", "denom_id": "unique_individuals"},
    "% of Population FloodLAMP Positive (including everyone in a positive pool)": {"kind": "ratio", "numerator_id": "unique_positive_incl_pool", "denom_id": "unique_individuals"},
    "% Confirmed FloodLAMP Positives with Same Day Antigen Negative": {"kind": "ratio", "numerator_id": "positive_same_day_antigen_neg", "denom_id": "positive_same_day_antigen"},
    "% Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative": {"kind": "ratio", "numerator_id": "positive_antigen_other_neg", "denom_id": "positive_antigen_other"},
    # Date metrics
    "Start Run Date": {"kind": "min_date"},
    "End Run Date": {"kind": "max_date"},
}
# Metric name to metric_id mapping (for formula references)
AGGREGATE_METRIC_ID_MAP = {
    "Number of Tubes Tested (initial only - no re-runs)": "tubes_tested_initial",
    "Number of Tube Tests Run (includes re-runs)": "tube_tests_run_total",
    "Number of Initial Runs": "initial_runs",
    "Number of APS Only Tubes run": "aps_only_tubes",
    "Number of Test Reactions (RFR plus APS only tubes run)": "test_reactions",
    "Number of Participant Results": "participant_results",
    "Number of ARF Tubes": "arf_tubes",
    "Sum of Participant Results plus ARF Tubes": "participant_plus_arf",
    "Average Pool Level (excludes ARF)": "avg_pool_level",
    "Number of Run Tubes (re-runs only)": "rerun_tubes",
    "Number of Reactions (re-runs only)": "rerun_reactions",
    "Re-run % of Tubes": "rerun_pct_of_tubes",
    "Number of Initial Runs with Re-runs": "initial_runs_with_reruns",
    "% Initial Runs with Re-runs": "pct_initial_runs_with_reruns",
    "Number of Tubes with Final Result Positive": "positive_tubes_final",
    "% of Tubes Positives (Final Result)": "pct_tubes_positive",
    "Number of Cases with Final Result Positive (Indiv or Pool)": "positive_cases_final",
    "Known Positive Cases": "known_positive_cases",
    "Unknown Positive Cases": "unknown_positive_cases",
    "Number of Tubes with Final Result Inconclusive": "inconclusive_tubes_final",
    "Number of Tubes in RFR Audit Inconclusive not in Appivo Final Results": "inconclusive_not_in_aps",
    "Total Number of Inconclusive Tubes": "total_inconclusive_tubes",
    "% of Tubes Inconclusive": "pct_tubes_inconclusive",
    "Number of Inconclusive Tubes resolved Positive by Referral Test or Correspondence": "inconclusive_resolved_pos",
    "% Inconclusives resolved Positive by Referral Tests": "pct_inconclusive_resolved_pos",
    "Number of Inconclusive Tubes with Referral Test or Correspondence Negative": "inconclusive_ref_neg",
    "Number of Inconclusive Tubes with no Referral Test result or Correspondence": "inconclusive_no_ref",
    "Number of Tubes with Initial Inconclusives and Re-run Negative": "inconclusive_rerun_neg",
    "Number of Inconclusive Test Run Calls": "inconclusive_run_calls",
    "% Tube Tests Run Called Inconclusive": "pct_tube_tests_called_inconclusive",
    "Number of FloodLAMP Cases with Referral Tests or Correspondence": "cases_with_referral",
    "Number of Referral Confirmed FloodLAMP Positives": "agree_positives",
    "FL Inconclusives with Referal / Correspondence Positive": "incl_ref_pos",
    "% FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive": "pct_pos_or_incl_with_ref_pos",
    "FL Inconclusives but Referral / Correspondence Negative": "incl_ref_neg",
    "FL Inconclusives with No Referral Tests or Correspondence": "incl_no_ref",
    "Number of FloodLAMP Test Person Cases with Referral Antigen Tests (including non-Same Day)": "cases_antigen_ref",
    "Number of FloodLAMP Test Person Cases with Same Day Referral Antigen Tests": "positive_same_day_antigen",
    "Number of FloodLAMP Positive Test Person Cases with Same Day Antigen Negative": "positive_same_day_antigen_neg",
    "% Confirmed FloodLAMP Positives with Same Day Antigen Negative": "pct_positive_same_day_antigen_neg",
    "Number of FloodLAMP Positive Test Person Cases confirmed with Referral Tests but Antigen and Other Non-Antigen Test Negative": "positive_antigen_other_neg",
    "% Confirmed FloodLAMP Positives that were Antigen and Other Non-Antigen Test Negative": "pct_positive_antigen_other_neg",
    "False Positives Final Results": "false_positives",
    "False Negative Final Results (Suspected)": "false_negatives",
    "Number of Unique Indivuals Tested": "unique_individuals",
    "Number of Unique Sponsors": "unique_sponsors",
    "Number of Unique Individual Tested FloodLAMP Positive": "unique_positive",
    "% of Population FloodLAMP Positive (excluding pools not deconv)": "pct_population_positive",
    "Number of Unique Individual Tested FloodLAMP Positive (including if in a positive pool)": "unique_positive_incl_pool",
    "% of Population FloodLAMP Positive (including everyone in a positive pool)": "pct_population_positive_incl_pool",
    "Start Run Date": "start_run_date",
    "End Run Date": "end_run_date",
}
def _load_reference_stats_metrics(pilot_data_root):
    """Load reference stats metrics from CSV file.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return metrics: list of dict, each with section and metric keys.
    """
    csv_path = os.path.join(pilot_data_root, REFERENCE_STATS_METRICS_CSV)
    if not os.path.isfile(csv_path):
        print(f"WARNING: Reference stats metrics CSV not found: {csv_path}")
        return []
    metrics = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            section = (row.get("section") or "").strip()
            metric = (row.get("metric") or "").strip()
            if section and metric:
                metrics.append({"section": section, "metric": metric})
    return metrics
def _build_aggregate_stats_metrics(reference_metrics):
    """Build AGGREGATE_STATS_METRICS list from reference metrics.

    :param reference_metrics: list of dict from _load_reference_stats_metrics.
    :return metrics: list of dict with full metric config including kind, aliases, etc.
    """
    result = []
    for ref in reference_metrics:
        section = ref["section"]
        metric = ref["metric"]
        # Skip sections not suitable for aggregation
        if section in AGGREGATE_STATS_SKIP_SECTIONS:
            continue
        # Get metric_id from mapping, or generate from metric name
        metric_id = AGGREGATE_METRIC_ID_MAP.get(metric)
        if not metric_id:
            # Generate metric_id from metric name (slugify)
            metric_id = metric.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("%", "pct").replace("/", "_").replace("-", "_")
        # Get formula config if defined, otherwise default to sum_int
        formula = AGGREGATE_METRIC_FORMULAS.get(metric, {})
        kind = formula.get("kind", "sum_int")
        entry = {
            "section": section,
            "metric": metric,
            "metric_id": metric_id,
            "kind": kind,
            "aliases": [metric],  # Use exact metric name as alias
        }
        # Add formula-specific fields
        if "numerator_id" in formula:
            entry["numerator_id"] = formula["numerator_id"]
        if "denom_id" in formula:
            entry["denom_id"] = formula["denom_id"]
        if "denom_subtract_id" in formula:
            entry["denom_subtract_id"] = formula["denom_subtract_id"]
        if "numerator_ids" in formula:
            entry["numerator_ids"] = formula["numerator_ids"]
        result.append(entry)
    return result
# Global variable - will be populated when aggregation runs
AGGREGATE_STATS_METRICS = []

def _choose_weekly_csv_path_agg(csv_folder, site_code):
    """Choose the best available weekly summary CSV for aggregation using APS > RFR > RSR > STS preference.

    :param csv_folder: str, path to curated CSV folder.
    :param site_code: str, 4-letter site code.
    :return path: str or none, chosen weekly summary CSV path.
    """
    candidates = [
        os.path.join(csv_folder, f"{site_code}_APS_weekly-summary.csv"),
        os.path.join(csv_folder, f"{site_code}_RFR_weekly-summary.csv"),
        os.path.join(csv_folder, f"{site_code}_RSR_weekly-summary.csv"),
        os.path.join(csv_folder, f"{site_code}_STS_weekly-summary.csv"),
    ]
    for p in candidates:
        if os.path.isfile(p):
            return p
    return None
def _choose_stats_kv_csv_path_agg(csv_folder, site_code):
    """Choose the best available stats key-values CSV for aggregation using APS > RSR > STS preference.

    :param csv_folder: str, path to curated CSV folder.
    :param site_code: str, 4-letter site code.
    :return path: str or none, chosen stats key-values CSV path.
    """
    candidates = [
        os.path.join(csv_folder, f"{site_code}_APS_stats_key-values.csv"),
        os.path.join(csv_folder, f"{site_code}_RSR_stats_key-values.csv"),
        os.path.join(csv_folder, f"{site_code}_STS_stats_key-values.csv"),
    ]
    for p in candidates:
        if os.path.isfile(p):
            return p
    return None
def _choose_referral_agreement_csv_path_agg(csv_folder, site_code):
    """Choose the best available referral agreement CSV for aggregation using APS > RSR > STS preference.

    :param csv_folder: str, path to curated CSV folder.
    :param site_code: str, 4-letter site code.
    :return path: str or none, chosen referral agreement CSV path.
    """
    candidates = [
        os.path.join(csv_folder, f"{site_code}_APS_stats_referral-agreement.csv"),
        os.path.join(csv_folder, f"{site_code}_RSR_stats_referral-agreement.csv"),
        os.path.join(csv_folder, f"{site_code}_STS_stats_referral-agreement.csv"),
    ]
    for p in candidates:
        if os.path.isfile(p):
            return p
    return None
def _read_stats_kv_map(stats_kv_csv_path):
    """Read a stats key-values CSV into a dict keyed by metric name.

    :param stats_kv_csv_path: str, path to stats key-values CSV.
    :return metric_map: dict, mapping metric string -> row dict.
    """
    metric_map = {}
    if not stats_kv_csv_path or not os.path.isfile(stats_kv_csv_path):
        return metric_map
    with open(stats_kv_csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            metric = (row.get("metric") or "").strip()
            if not metric:
                continue
            metric_map[metric] = row
    return metric_map
def _pick_metric_row(metric_map, metric_aliases):
    """Pick the first matching metric row given a list of aliases.

    :param metric_map: dict, mapping metric name -> row dict.
    :param metric_aliases: list of str, acceptable metric names.
    :return row: dict or none, matching row dict if found.
    """
    for m in metric_aliases:
        if m in metric_map:
            return metric_map[m]
    return None
def _aggregate_sum_int(site_metric_maps, metric_aliases):
    """Aggregate a count metric by summing across sites.

    :param site_metric_maps: dict, mapping site_code -> metric_map.
    :param metric_aliases: list of str, acceptable metric names.
    :return result: dict, fields: value, value_status, sites_included_n, sites_missing_n, raw_values.
    """
    total_sites = len(site_metric_maps)
    included = 0
    s = 0
    raw_values = {}
    for site_code, metric_map in site_metric_maps.items():
        row = _pick_metric_row(metric_map, metric_aliases)
        if not row:
            continue
        status = (row.get("value_status") or "").strip()
        value = (row.get("value") or "").strip()
        if status == "not_available" or value == "":
            continue
        n = _safe_int(value)
        if n is None:
            continue
        s += n
        included += 1
        raw_values[site_code] = n
    missing = total_sites - included
    # Treat missing sites as 0 - return 0 sum even if no sites have data
    if included == 0:
        return {"value": "0", "value_status": "all_sites_missing", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    if missing > 0:
        return {"value": str(s), "value_status": "partial", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    return {"value": str(s), "value_status": "ok", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
def _aggregate_sum_float(site_metric_maps, metric_aliases):
    """Aggregate a float metric by summing across sites.

    :param site_metric_maps: dict, mapping site_code -> metric_map.
    :param metric_aliases: list of str, acceptable metric names.
    :return result: dict, fields: value, value_status, sites_included_n, sites_missing_n, raw_values.
    """
    total_sites = len(site_metric_maps)
    included = 0
    s = 0.0
    raw_values = {}
    for site_code, metric_map in site_metric_maps.items():
        row = _pick_metric_row(metric_map, metric_aliases)
        if not row:
            continue
        status = (row.get("value_status") or "").strip()
        value = (row.get("value") or "").strip()
        if status == "not_available" or value == "":
            continue
        x = _safe_float(value)
        if x is None:
            continue
        s += x
        included += 1
        raw_values[site_code] = x
    missing = total_sites - included
    # Treat missing sites as 0 - return 0 sum even if no sites have data
    if included == 0:
        return {"value": "0", "value_status": "all_sites_missing", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    if missing > 0:
        return {"value": str(s), "value_status": "partial", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    return {"value": str(s), "value_status": "ok", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
def _aggregate_min_date(site_metric_maps, metric_aliases):
    """Aggregate a date metric by taking the earliest date across sites.

    :param site_metric_maps: dict, mapping site_code -> metric_map.
    :param metric_aliases: list of str, acceptable metric names.
    :return result: dict, fields: value, value_status, sites_included_n, sites_missing_n, raw_values.
    """
    total_sites = len(site_metric_maps)
    included = 0
    raw_values = {}
    dates = []
    for site_code, metric_map in site_metric_maps.items():
        row = _pick_metric_row(metric_map, metric_aliases)
        if not row:
            continue
        status = (row.get("value_status") or "").strip()
        value = (row.get("value") or "").strip()
        if status == "not_available" or value == "":
            continue
        d = _safe_date(value)
        if d is None:
            continue
        dates.append(d)
        included += 1
        raw_values[site_code] = d
    missing = total_sites - included
    if included == 0:
        return {"value": "", "value_status": "not_available", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    v = min(dates)
    if missing > 0:
        return {"value": v, "value_status": "partial", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    return {"value": v, "value_status": "ok", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
def _aggregate_max_date(site_metric_maps, metric_aliases):
    """Aggregate a date metric by taking the latest date across sites.

    :param site_metric_maps: dict, mapping site_code -> metric_map.
    :param metric_aliases: list of str, acceptable metric names.
    :return result: dict, fields: value, value_status, sites_included_n, sites_missing_n, raw_values.
    """
    total_sites = len(site_metric_maps)
    included = 0
    raw_values = {}
    dates = []
    for site_code, metric_map in site_metric_maps.items():
        row = _pick_metric_row(metric_map, metric_aliases)
        if not row:
            continue
        status = (row.get("value_status") or "").strip()
        value = (row.get("value") or "").strip()
        if status == "not_available" or value == "":
            continue
        d = _safe_date(value)
        if d is None:
            continue
        dates.append(d)
        included += 1
        raw_values[site_code] = d
    missing = total_sites - included
    if included == 0:
        return {"value": "", "value_status": "not_available", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    v = max(dates)
    if missing > 0:
        return {"value": v, "value_status": "partial", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
    return {"value": v, "value_status": "ok", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
def _compute_ratio(numerator_value, numerator_status, denom_value, denom_status):
    """Compute a ratio with denom_zero / not_available / partial semantics.

    :param numerator_value: float or none, numerator value.
    :param numerator_status: str, numerator status.
    :param denom_value: float or none, denominator value.
    :param denom_status: str, denominator status.
    :return result: dict, fields: value, value_status.
    """
    if denom_value is None or denom_value == "":
        return {"value": "", "value_status": "not_available"}
    try:
        d = float(denom_value)
    except Exception:
        return {"value": "", "value_status": "not_available"}
    if d == 0:
        return {"value": "", "value_status": "denom_zero"}
    if numerator_value is None or numerator_value == "":
        return {"value": "", "value_status": "not_available"}
    try:
        n = float(numerator_value)
    except Exception:
        return {"value": "", "value_status": "not_available"}
    v = n / d
    if numerator_status != "ok" or denom_status != "ok":
        return {"value": str(v), "value_status": "partial"}
    return {"value": str(v), "value_status": "ok"}
def _aggregate_stats_key_values(site_code_to_stats_kv_path, output_csv_path, pilot_data_root):
    """Aggregate selected stats key-values across all sites into a single CSV.

    :param site_code_to_stats_kv_path: dict, mapping site_code -> stats key-values CSV path.
    :param output_csv_path: str, output CSV path.
    :param pilot_data_root: str, path to pilot-data root (for loading reference metrics).
    :return result: dict, summary of aggregation.
    """
    # Load reference metrics from CSV and build AGGREGATE_STATS_METRICS
    reference_metrics = _load_reference_stats_metrics(pilot_data_root)
    aggregate_stats_metrics = _build_aggregate_stats_metrics(reference_metrics)
    if not aggregate_stats_metrics:
        print("WARNING: No aggregate stats metrics found from reference CSV")
        return {"output_csv_path": output_csv_path, "rows_written": 0, "sites_count": 0}
    site_metric_maps = {}
    for site_code, stats_kv_path in site_code_to_stats_kv_path.items():
        site_metric_maps[site_code] = _read_stats_kv_map(stats_kv_path)

    computed = {}
    for m in aggregate_stats_metrics:
        mid = m["metric_id"]
        kind = m["kind"]
        if kind == "sum_int":
            r = _aggregate_sum_int(site_metric_maps, m["aliases"])
            r["value_formula"] = "sum(site values)"
            computed[mid] = r
            # DEBUG: Print breakdown for tubes_tested_initial
            if mid == "tubes_tested_initial":
                print(f"\n=== DEBUG: {m['metric']} ===")
                raw_vals = r.get("raw_values", {})
                running_sum = 0
                for sc in sorted(raw_vals.keys()):
                    v = raw_vals[sc]
                    running_sum += v
                    print(f"  {sc}: {v}")
                print(f"  ---")
                print(f"  SUM: {running_sum}")
                print(f"  Aggregate value: {r.get('value')}")
        elif kind == "sum_float":
            r = _aggregate_sum_float(site_metric_maps, m["aliases"])
            r["value_formula"] = "sum(site values)"
            computed[mid] = r
        elif kind == "min_date":
            r = _aggregate_min_date(site_metric_maps, m["aliases"])
            r["value_formula"] = "min(site values)"
            computed[mid] = r
        elif kind == "max_date":
            r = _aggregate_max_date(site_metric_maps, m["aliases"])
            r["value_formula"] = "max(site values)"
            computed[mid] = r

    for m in aggregate_stats_metrics:
        mid = m["metric_id"]
        kind = m["kind"]
        if kind in ["sum_int", "sum_float", "min_date", "max_date"]:
            continue
        if kind == "derived_sum":
            parts = []
            included_n = 0
            missing_n = 0
            status = "ok"
            total = 0
            for pid in m["numerator_ids"]:
                pr = computed.get(pid, {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
                parts.append(pid)
                v = _safe_int(pr.get("value"))
                if v is None:
                    status = "not_available"
                else:
                    total += v
                included_n = max(included_n, pr.get("sites_included_n", 0))
                missing_n = max(missing_n, pr.get("sites_missing_n", 0))
                if pr.get("value_status") != "ok":
                    status = "partial" if status != "not_available" else status
            if status == "not_available":
                computed[mid] = {"value": "", "value_status": "not_available", "sites_included_n": included_n, "sites_missing_n": missing_n, "value_formula": " + ".join(parts)}
            else:
                computed[mid] = {"value": str(total), "value_status": status, "sites_included_n": included_n, "sites_missing_n": missing_n, "value_formula": " + ".join(parts)}
        if kind == "ratio":
            num = computed.get(m["numerator_id"], {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
            den = computed.get(m["denom_id"], {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
            rr = _compute_ratio(num.get("value"), num.get("value_status"), den.get("value"), den.get("value_status"))
            computed[mid] = {
                "value": rr["value"],
                "value_status": rr["value_status"],
                "sites_included_n": min(num.get("sites_included_n", 0), den.get("sites_included_n", 0)),
                "sites_missing_n": max(num.get("sites_missing_n", 0), den.get("sites_missing_n", 0)),
                "value_formula": f'{m["numerator_id"]} / {m["denom_id"]}',
            }
        if kind == "ratio_diff_denom":
            # Compute numerator / (denom - subtract)
            num = computed.get(m["numerator_id"], {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
            den = computed.get(m["denom_id"], {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
            sub = computed.get(m["denom_subtract_id"], {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
            den_val = _safe_int(den.get("value"))
            sub_val = _safe_int(sub.get("value"))
            if den_val is not None and sub_val is not None:
                denom_diff = den_val - sub_val
                denom_status = "ok" if den.get("value_status") == "ok" and sub.get("value_status") == "ok" else "partial"
            else:
                denom_diff = None
                denom_status = "not_available"
            rr = _compute_ratio(num.get("value"), num.get("value_status"), str(denom_diff) if denom_diff is not None else "", denom_status)
            computed[mid] = {
                "value": rr["value"],
                "value_status": rr["value_status"],
                "sites_included_n": min(num.get("sites_included_n", 0), den.get("sites_included_n", 0), sub.get("sites_included_n", 0)),
                "sites_missing_n": max(num.get("sites_missing_n", 0), den.get("sites_missing_n", 0), sub.get("sites_missing_n", 0)),
                "value_formula": f'{m["numerator_id"]} / ({m["denom_id"]} - {m["denom_subtract_id"]})',
            }
        if kind == "ratio_sum_numerators":
            num_parts = []
            total_num = 0
            status = "ok"
            included_n = 0
            missing_n = 0
            for pid in m["numerator_ids"]:
                pr = computed.get(pid, {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
                v = _safe_int(pr.get("value"))
                if v is None:
                    status = "not_available"
                else:
                    total_num += v
                included_n = max(included_n, pr.get("sites_included_n", 0))
                missing_n = max(missing_n, pr.get("sites_missing_n", 0))
                if pr.get("value_status") != "ok":
                    status = "partial" if status != "not_available" else status
                num_parts.append(pid)
            den = computed.get(m["denom_id"], {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps)})
            rr = _compute_ratio(str(total_num), status, den.get("value"), den.get("value_status"))
            computed[mid] = {
                "value": rr["value"],
                "value_status": rr["value_status"],
                "sites_included_n": min(included_n, den.get("sites_included_n", 0)),
                "sites_missing_n": max(missing_n, den.get("sites_missing_n", 0)),
                "value_formula": f'({ " + ".join(num_parts) }) / {m["denom_id"]}',
            }

    headers = ["section", "metric", "value", "value_status", "value_formula", "sites_included_n", "sites_missing_n", "source_sheet", "source_row"]
    rows_out = []
    for m in aggregate_stats_metrics:
        mid = m["metric_id"]
        r = computed.get(mid, {"value": "", "value_status": "not_available", "sites_included_n": 0, "sites_missing_n": len(site_metric_maps), "value_formula": ""})
        rows_out.append({
            "section": m["section"],
            "metric": m["metric"],
            "value": r.get("value", ""),
            "value_status": r.get("value_status", ""),
            "value_formula": r.get("value_formula", ""),
            "sites_included_n": str(r.get("sites_included_n", "")),
            "sites_missing_n": str(r.get("sites_missing_n", "")),
            "source_sheet": "AGGREGATE",
            "source_row": "",
        })

    _ensure_folder(os.path.dirname(output_csv_path))
    with open(output_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in rows_out:
            writer.writerow(r)

    return {"output_csv_path": output_csv_path, "rows_written": len(rows_out), "sites_count": len(site_metric_maps)}
def _aggregate_weekly_summary(site_code_to_weekly_csv_path, output_csv_path):
    """Aggregate weekly summaries across all sites into a single CSV.

    :param site_code_to_weekly_csv_path: dict, mapping site_code -> weekly summary CSV path.
    :param output_csv_path: str, output CSV path.
    :return result: dict, summary of aggregation.
    """
    totals_by_week = {}
    sites_total = len(site_code_to_weekly_csv_path)
    for site_code, weekly_csv_path in site_code_to_weekly_csv_path.items():
        if not weekly_csv_path or not os.path.isfile(weekly_csv_path):
            continue
        with open(weekly_csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ws = _safe_date(row.get("week_start_date"))
                we = _safe_date(row.get("week_end_date"))
                if not ws:
                    continue
                if ws not in totals_by_week:
                    totals_by_week[ws] = {
                        "week_start_date": ws,
                        "week_end_date": we or "",
                        "participants_n": 0,
                        "tubes_n": 0,
                        "positive_tubes_n": 0,
                        "inconclusive_tubes_n": 0,
                        "sites_included": set(),
                    }
                d = totals_by_week[ws]
                if not d["week_end_date"] and we:
                    d["week_end_date"] = we
                d["participants_n"] += _safe_int(row.get("participants_n")) or 0
                d["tubes_n"] += _safe_int(row.get("tubes_n")) or 0
                d["positive_tubes_n"] += _safe_int(row.get("positive_tubes_n")) or 0
                d["inconclusive_tubes_n"] += _safe_int(row.get("inconclusive_tubes_n")) or 0
                d["sites_included"].add(site_code)

    headers = ["week_start_date", "week_end_date", "participants_n", "tubes_n", "positive_tubes_n", "inconclusive_tubes_n", "pct_positive", "pct_positive_status", "pct_positive_formula", "sites_included_n", "sites_total_n"]
    rows_out = []
    for ws in sorted(totals_by_week.keys()):
        d = totals_by_week[ws]
        tubes_n = d["tubes_n"]
        pos_n = d["positive_tubes_n"]
        if tubes_n == 0:
            pct_positive = ""
            pct_status = "denom_zero"
        else:
            pct_positive = str(pos_n / tubes_n)
            pct_status = "ok"
        rows_out.append({
            "week_start_date": d["week_start_date"],
            "week_end_date": d["week_end_date"],
            "participants_n": str(d["participants_n"]),
            "tubes_n": str(d["tubes_n"]),
            "positive_tubes_n": str(d["positive_tubes_n"]),
            "inconclusive_tubes_n": str(d["inconclusive_tubes_n"]),
            "pct_positive": pct_positive,
            "pct_positive_status": pct_status,
            "pct_positive_formula": "positive_tubes_n / tubes_n",
            "sites_included_n": str(len(d["sites_included"])),
            "sites_total_n": str(sites_total),
        })
    _ensure_folder(os.path.dirname(output_csv_path))
    with open(output_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in rows_out:
            writer.writerow(r)

    return {"output_csv_path": output_csv_path, "rows_written": len(rows_out), "weeks_count": len(rows_out), "sites_count": sites_total}
def _aggregate_referral_agreement(site_code_to_referral_csv_path, output_csv_path):
    """Aggregate stats referral agreement tables across all available sites.

    :param site_code_to_referral_csv_path: dict, mapping site_code -> referral agreement CSV path.
    :param output_csv_path: str, output CSV path.
    :return result: dict, summary of aggregation.
    """
    agg = {
        "Positive": {"tubes_n": 0, "cases_n": 0, "with_ref_or_corresp_n": 0, "agree_n": 0, "disagree_n": 0, "sites": set()},
        "Inconclusive": {"tubes_n": 0, "cases_n": 0, "with_ref_or_corresp_n": 0, "ref_cor_pos_n": 0, "ref_cor_neg_n": 0, "sites": set()},
    }
    for site_code, referral_csv_path in site_code_to_referral_csv_path.items():
        if not referral_csv_path or not os.path.isfile(referral_csv_path):
            continue
        with open(referral_csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cat = (row.get("fl_result_category") or "").strip()
                if cat not in agg:
                    continue
                a = agg[cat]
                a["tubes_n"] += _safe_int(row.get("tubes_n")) or 0
                a["cases_n"] += _safe_int(row.get("cases_n")) or 0
                a["with_ref_or_corresp_n"] += _safe_int(row.get("with_ref_or_corresp_n")) or 0
                if cat == "Positive":
                    a["agree_n"] += _safe_int(row.get("agree_n")) or 0
                    a["disagree_n"] += _safe_int(row.get("disagree_n")) or 0
                if cat == "Inconclusive":
                    a["ref_cor_pos_n"] += _safe_int(row.get("ref_cor_pos_n")) or 0
                    a["ref_cor_neg_n"] += _safe_int(row.get("ref_cor_neg_n")) or 0
                a["sites"].add(site_code)

    def _pct(n, d):
        if d == 0:
            return {"v": "", "s": "denom_zero"}
        return {"v": str(n / d), "s": "ok"}

    pos = agg["Positive"]
    inc = agg["Inconclusive"]
    pos_agree = _pct(pos["agree_n"], pos["with_ref_or_corresp_n"])
    pos_disagree = _pct(pos["disagree_n"], pos["with_ref_or_corresp_n"])
    inc_pos = _pct(inc["ref_cor_pos_n"], inc["with_ref_or_corresp_n"])
    inc_neg = _pct(inc["ref_cor_neg_n"], inc["with_ref_or_corresp_n"])

    headers = [
        "fl_result_category",
        "tubes_n",
        "cases_n",
        "with_ref_or_corresp_n",
        "agree_n",
        "agree_pct",
        "agree_pct_status",
        "disagree_n",
        "disagree_pct",
        "disagree_pct_status",
        "ref_cor_pos_n",
        "incl_gt_pos_pct",
        "incl_gt_pos_pct_status",
        "ref_cor_neg_n",
        "incl_gt_neg_pct",
        "incl_gt_neg_pct_status",
        "source_sheet",
        "source_anchor",
        "agree_pct_formula",
        "disagree_pct_formula",
        "incl_gt_pos_pct_formula",
        "incl_gt_neg_pct_formula",
        "sites_included_n",
    ]
    rows_out = [
        {
            "fl_result_category": "Positive",
            "tubes_n": str(pos["tubes_n"]),
            "cases_n": str(pos["cases_n"]),
            "with_ref_or_corresp_n": str(pos["with_ref_or_corresp_n"]),
            "agree_n": str(pos["agree_n"]),
            "agree_pct": pos_agree["v"],
            "agree_pct_status": pos_agree["s"],
            "disagree_n": str(pos["disagree_n"]),
            "disagree_pct": pos_disagree["v"],
            "disagree_pct_status": pos_disagree["s"],
            "ref_cor_pos_n": "",
            "incl_gt_pos_pct": "",
            "incl_gt_pos_pct_status": "",
            "ref_cor_neg_n": "",
            "incl_gt_neg_pct": "",
            "incl_gt_neg_pct_status": "",
            "source_sheet": "AGGREGATE",
            "source_anchor": "",
            "agree_pct_formula": "agree_n / with_ref_or_corresp_n",
            "disagree_pct_formula": "disagree_n / with_ref_or_corresp_n",
            "incl_gt_pos_pct_formula": "",
            "incl_gt_neg_pct_formula": "",
            "sites_included_n": str(len(pos["sites"])),
        },
        {
            "fl_result_category": "Inconclusive",
            "tubes_n": str(inc["tubes_n"]),
            "cases_n": str(inc["cases_n"]),
            "with_ref_or_corresp_n": str(inc["with_ref_or_corresp_n"]),
            "agree_n": "",
            "agree_pct": "",
            "agree_pct_status": "",
            "disagree_n": "",
            "disagree_pct": "",
            "disagree_pct_status": "",
            "ref_cor_pos_n": str(inc["ref_cor_pos_n"]),
            "incl_gt_pos_pct": inc_pos["v"],
            "incl_gt_pos_pct_status": inc_pos["s"],
            "ref_cor_neg_n": str(inc["ref_cor_neg_n"]),
            "incl_gt_neg_pct": inc_neg["v"],
            "incl_gt_neg_pct_status": inc_neg["s"],
            "source_sheet": "AGGREGATE",
            "source_anchor": "",
            "agree_pct_formula": "",
            "disagree_pct_formula": "",
            "incl_gt_pos_pct_formula": "ref_cor_pos_n / with_ref_or_corresp_n",
            "incl_gt_neg_pct_formula": "ref_cor_neg_n / with_ref_or_corresp_n",
            "sites_included_n": str(len(inc["sites"])),
        },
    ]

    _ensure_folder(os.path.dirname(output_csv_path))
    with open(output_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in rows_out:
            writer.writerow(r)

    return {"output_csv_path": output_csv_path, "rows_written": len(rows_out), "sites_with_referral_agreement": len(site_code_to_referral_csv_path)}
def run_aggregate_csvs(pilot_data_root, zipall_csvs_path=None):
    """Run aggregate CSV generation from a ZIPALL CSVs zip.

    If zipall_csvs_path is not provided, uses the latest zips folder.

    :param pilot_data_root: str, path to pilot-data root folder.
    :param zipall_csvs_path: str or none, path to ZIPALL_pilot-data_csvs.zip (uses latest if None).
    :return: dict, aggregate results.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    print()  # Blank line before aggregate output
    _print_section("AGGREGATE CSVS: SETUP")
    if zipall_csvs_path is None:
        # Find the latest zips folder
        latest_zips = _get_latest_zips_folder(pilot_data_root)
        if not latest_zips:
            _print_kv("ERROR", "No zips_pilot-data_* folder found")
            print()  # Blank line after aggregate output
            return {"error": "No zips folder found"}
        zipall_csvs_path = _get_zipall_csvs_path(latest_zips)
        if not zipall_csvs_path:
            _print_kv("ERROR", f"No ZIPALL_pilot-data_csvs.zip in {os.path.basename(latest_zips)}")
            print()  # Blank line after aggregate output
            return {"error": "No ZIPALL CSVs zip found"}
        _print_kv("Using latest zips folder", os.path.basename(latest_zips))
    _print_kv("ZIPALL CSVs zip", os.path.basename(zipall_csvs_path))
    output_folder_path = os.path.join(pilot_data_root, AGGREGATE_FOLDER_NAME)
    _print_kv("Output folder", output_folder_path)
    _print_dash()
    _print_section("AGGREGATE CSVS: PROCESSING")
    result = aggregate_zipall_curated_csvs(zipall_csvs_path, output_folder_path, pilot_data_root)
    _print_kv("Sites discovered", len(result.get("sites_discovered", [])))
    skipped = result.get("sites_skipped", [])
    if skipped:
        _print_kv("Sites skipped (FLMP sub-programs)", ", ".join(skipped))
    _print_kv("Stats key-values sites", len(result.get("stats_sites_used", [])))
    _print_kv("Weekly summary sites", len(result.get("weekly_sites_used", [])))
    _print_kv("Referral agreement sites", len(result.get("referral_sites_used", [])))
    _print_dash()
    _print_section("AGGREGATE CSVS: DONE")
    print()  # Blank line after aggregate output
    return result
def aggregate_zipall_curated_csvs(pilot_data_csvs_zip_path, output_folder_path, pilot_data_root):
    """Aggregate a ZIPALL curated CSV zip into three cross-site aggregate CSVs.

    :param pilot_data_csvs_zip_path: str, path to ZIPALL_pilot-data_csvs.zip.
    :param output_folder_path: str, output folder for aggregate CSVs.
    :param pilot_data_root: str, path to pilot-data root (for loading reference metrics).
    :return result: dict, output paths and summaries.
    """
    import tempfile
    import shutil

    pilot_data_csvs_zip_path = os.path.abspath(pilot_data_csvs_zip_path)
    output_folder_path = os.path.abspath(output_folder_path)
    _ensure_folder(output_folder_path)

    extract_dir = tempfile.mkdtemp(prefix="zipall_curated_csvs_extract_")
    try:
        with zipfile.ZipFile(pilot_data_csvs_zip_path, "r") as z:
            z.extractall(extract_dir)

        sites = _discover_site_folders(extract_dir)
        site_code_to_stats = {}
        site_code_to_weekly = {}
        site_code_to_referral = {}
        skipped_sites = []

        for site_code, site_folder in sites:
            # Skip FLMP sub-programs to avoid double-counting (CRLN + FLSP = FLMP)
            if site_code in AGGREGATE_SKIP_SITE_CODES:
                skipped_sites.append(site_code)
                _print_kv(f"  Skip {site_code}", "FLMP sub-program (avoiding double-count with FLMP)")
                continue
            csv_folder = _get_csv_folder(site_folder, site_code)
            if not csv_folder:
                continue
            stats_kv = _choose_stats_kv_csv_path_agg(csv_folder, site_code)
            weekly = _choose_weekly_csv_path_agg(csv_folder, site_code)
            referral = _choose_referral_agreement_csv_path_agg(csv_folder, site_code)
            if stats_kv:
                site_code_to_stats[site_code] = stats_kv
            if weekly:
                site_code_to_weekly[site_code] = weekly
            if referral:
                site_code_to_referral[site_code] = referral

        out_stats = os.path.join(output_folder_path, "aggregate_pilot-data_stats_key-values.csv")
        out_weekly = os.path.join(output_folder_path, "aggregate_pilot-data_weekly-summary.csv")
        out_referral = os.path.join(output_folder_path, "aggregate_pilot-data_stats_referral-agreement.csv")

        stats_result = _aggregate_stats_key_values(site_code_to_stats, out_stats, pilot_data_root)
        weekly_result = _aggregate_weekly_summary(site_code_to_weekly, out_weekly)
        referral_result = _aggregate_referral_agreement(site_code_to_referral, out_referral)

        return {
            "sites_discovered": [s[0] for s in sites],
            "sites_skipped": skipped_sites,
            "stats_sites_used": sorted(site_code_to_stats.keys()),
            "weekly_sites_used": sorted(site_code_to_weekly.keys()),
            "referral_sites_used": sorted(site_code_to_referral.keys()),
            "outputs": {
                "stats_key_values_csv": stats_result,
                "weekly_summary_csv": weekly_result,
                "referral_agreement_csv": referral_result,
            },
        }
    finally:
        shutil.rmtree(extract_dir, ignore_errors=True)
def mrun_aggregate_zipall_curated_csvs():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    # Run the zipping process and get the output paths
    zip_result = run_zip_pilot_data(pilot_data_root)
    # Get the path to the ZIPALL CSVs zip from the returned result
    pilot_data_csvs_zip_path = zip_result["combined_result"]["zipall_csvs"]
    # Create aggregate folder in the pilot-data root
    output_folder_path = os.path.join(pilot_data_root, AGGREGATE_FOLDER_NAME)
    aggregate_zipall_curated_csvs(pilot_data_csvs_zip_path, output_folder_path, pilot_data_root)


### Markdown generation: pilot site summaries
# This section creates per-site archive markdown files based on key curated CSVs.
# It is intentionally conservative: it only reads curated CSVs and writes markdown into each site folder.

PILOT_SITE_MD_FILENAME_TEMPLATE = "{site_code}_pilot-data_summary.md"
# Aggregate data constants
AGGREGATE_STATS_KV_CSV = "aggregate_pilot-data_stats_key-values.csv"
AGGREGATE_WEEKLY_CSV = "aggregate_pilot-data_weekly-summary.csv"
AGGREGATE_REFERRAL_AGREEMENT_CSV = "aggregate_pilot-data_stats_referral-agreement.csv"
AGGREGATE_MD_FILENAME = "aggregate_pilot-data_summary.md"
# Google Sheets reference CSV files (relative to pilots folder)
GSHEETS_FILENAMES_CSV = "Data PUB - Pilot Data Google Files - PUB Filenames.csv"
GSHEETS_URLS_CSV = "Data PUB - Pilot Data Google Files - PUB URLs.csv"
PILOT_SITE_MD_CATEGORY = "pilots"
PILOT_SITE_MD_SUBCATEGORY = "pilot-data"
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
def _format_weekly_summary_rows(headers, rows):
    """Format weekly summary rows with proper percentage formatting.

    :param headers: list of str, column headers.
    :param rows: list of list of str, row data.
    :return formatted_rows: list of list of str, formatted row data.
    """
    # Find index of pct_positive column
    pct_idx = None
    for i, h in enumerate(headers):
        if h.lower().strip() == "pct_positive":
            pct_idx = i
            break
    if pct_idx is None:
        return rows
    formatted_rows = []
    for row in rows:
        new_row = list(row)
        if len(new_row) > pct_idx:
            value = new_row[pct_idx]
            if value is not None and str(value).strip() != "":
                try:
                    num = float(value)
                    new_row[pct_idx] = f"{num * 100:.1f}%"
                except (ValueError, TypeError):
                    pass
        formatted_rows.append(new_row)
    return formatted_rows
def _format_referral_agreement_rows(headers, rows):
    """Format referral agreement rows with proper percentage formatting.

    :param headers: list of str, column headers.
    :param rows: list of list of str, row data.
    :return formatted_rows: list of list of str, formatted row data.
    """
    # Find indices of all percentage columns (ending in _pct)
    pct_indices = []
    for i, h in enumerate(headers):
        h_lower = h.lower().strip()
        if h_lower.endswith("_pct"):
            pct_indices.append(i)
    if not pct_indices:
        return rows
    formatted_rows = []
    for row in rows:
        new_row = list(row)
        for pct_idx in pct_indices:
            if len(new_row) > pct_idx:
                value = new_row[pct_idx]
                if value is not None and str(value).strip() != "":
                    try:
                        num = float(value)
                        new_row[pct_idx] = f"{num * 100:.1f}%"
                    except (ValueError, TypeError):
                        pass
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
    stats_kv_candidates = [
        os.path.join(csv_folder, f"{site_code}_APS_stats_key-values.csv"),
        os.path.join(csv_folder, f"{site_code}_RSR_stats_key-values.csv"),
        os.path.join(csv_folder, f"{site_code}_STS_stats_key-values.csv"),
    ]
    if site_code == "DAVI":
        stats_kv_candidates = [
            os.path.join(csv_folder, f"{site_code}_RSR_stats_key-values.csv"),
            os.path.join(csv_folder, f"{site_code}_APS_stats_key-values.csv"),
            os.path.join(csv_folder, f"{site_code}_STS_stats_key-values.csv"),
        ]
    stats_kv_csv = None
    for p in stats_kv_candidates:
        if os.path.isfile(p):
            stats_kv_csv = p
            break
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

    CRLN and FLSP use FLMP's xlsx_downloads folder since they share the same source.

    :param site_folder: str, site folder path.
    :param site_code: str, 4-letter site code.
    :return links: list of dict, each with keys: label, relpath.
    """
    # CRLN and FLSP share FLMP's xlsx downloads
    lookup_code = "FLMP" if site_code in ("CRLN", "FLSP") else site_code
    if site_code in ("CRLN", "FLSP"):
        # Navigate to FLMP folder from CRLN/FLSP folder
        parent_folder = os.path.dirname(site_folder)
        lookup_folder = os.path.join(parent_folder, "FLMP_pilot-data")
        # Use relative path that goes up to parent then into FLMP folder
        rel_prefix = "../FLMP_pilot-data/"
    else:
        lookup_folder = site_folder
        rel_prefix = ""
    xlsx_folder = _get_xlsx_folder(lookup_folder, lookup_code)
    if not xlsx_folder:
        return []
    xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
    links = []
    xlsx_folder_name = os.path.basename(xlsx_folder)
    for fp in xlsx_files:
        links.append({"label": os.path.basename(fp), "relpath": f"{rel_prefix}{xlsx_folder_name}/{os.path.basename(fp)}"})
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

    CRLN and FLSP use FLMP's Google Sheets since they share the same source.

    :param gsheets_lookup: dict, lookup from _load_gsheets_lookup.
    :param site_code: str, 4-letter site code.
    :return links: list of dict, each with keys: label, url.
    """
    # CRLN and FLSP share FLMP's Google Sheets
    lookup_code = "FLMP" if site_code in ("CRLN", "FLSP") else site_code
    site_data = gsheets_lookup.get(lookup_code, {})
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
def _extract_existing_metadata(md_path):
    """Extract existing metadata from a markdown file.

    :param md_path: str, path to markdown file.
    :return metadata_text: str or none, metadata section text if found.
    """
    if not os.path.isfile(md_path):
        return None
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Find metadata section between "METADATA" and "CONTENT"
    if "METADATA" not in content or "CONTENT" not in content:
        return None
    metadata_start = content.find("METADATA")
    content_start = content.find("CONTENT")
    if metadata_start >= content_start:
        return None
    metadata_text = content[metadata_start:content_start].strip()
    return metadata_text
def _render_site_pilot_data_markdown(site_code, site_folder, csv_folder, key_csv_paths, md_filename, gsheets_lookup=None, skip_metadata=True):
    """Render a site pilot-data summary markdown document.

    :param site_code: str, 4-letter site code.
    :param site_folder: str, site folder path.
    :param csv_folder: str, curated CSV folder path.
    :param key_csv_paths: dict, key CSV paths (stats_kv_csv, weekly_csv, rtr_by_person_csv).
    :param md_filename: str, markdown file name (not full path).
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :param skip_metadata: bool, if true preserve existing metadata and only replace content.
    :return md_text: str, markdown document content.
    """
    today = datetime.date.today().isoformat()
    weekly_totals = _compute_weekly_totals(key_csv_paths.get("weekly_csv"))
    md_path = os.path.join(site_folder, md_filename)

    # Check if we should preserve existing metadata
    existing_metadata = None
    if skip_metadata:
        existing_metadata = _extract_existing_metadata(md_path)

    md_lines = []
    if existing_metadata:
        # Use existing metadata, only update last updated date
        metadata_lines = existing_metadata.split("\n")
        updated_metadata_lines = []
        for line in metadata_lines:
            if line.startswith("last updated:"):
                updated_metadata_lines.append(f"last updated: {today}")
            else:
                updated_metadata_lines.append(line)
        md_lines.append("\n".join(updated_metadata_lines))
        md_lines.append("")
        md_lines.append("")
        md_lines.append("CONTENT")
    else:
        # Generate fresh metadata
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
        md_lines.append("gfile_url: NA")
        md_lines.append(f"xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/pilots/pilot-data/{site_code}_xlsx_downloads")
        md_lines.append("pdf_gdrive_url: NA")
        md_lines.append("pdf_github_url: NA")
        md_lines.append(f"license: {PILOT_SITE_MD_LICENSE}")
        md_lines.append("words: ")
        md_lines.append("tokens: ")
        md_lines.append("notes: ")
        md_lines.append(f"summary_short: {summary_short}")
        md_lines.append("")
        md_lines.append("")
        md_lines.append("CONTENT")
    md_lines.append("")
    md_lines.append("## Plots")
    md_lines.append("")
    md_lines.append("### Composite")
    md_lines.append("")
    md_lines.append(f"![{site_code} Weekly Composite](_plots/{site_code}_weekly_composite.png)")
    md_lines.append("")
    md_lines.append("### Percent Positive Tubes")
    md_lines.append("")
    md_lines.append(f"![{site_code} Weekly Percent Positives](_plots/{site_code}_weekly_percent_positives.png)")
    md_lines.append("")
    md_lines.append("### Volume")
    md_lines.append("")
    md_lines.append(f"![{site_code} Weekly Volume](_plots/{site_code}_weekly_volume.png)")
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
        formatted_weekly_rows = _format_weekly_summary_rows(weekly_data["headers"], weekly_data["rows"])
        md_lines.append(_csv_rows_to_markdown_table(weekly_data["headers"], formatted_weekly_rows))
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
def write_site_pilot_data_markdown(site_code, site_folder, gsheets_lookup=None, skip_metadata=True):
    """Write a pilot-data summary markdown file for a single site.

    :param site_code: str, 4-letter site code.
    :param site_folder: str, site folder path.
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :param skip_metadata: bool, if true preserve existing metadata and only replace content.
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
    md_text = _render_site_pilot_data_markdown(site_code, site_folder, csv_folder, key_csv_paths, md_filename, gsheets_lookup, skip_metadata=skip_metadata)
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    return {"site_code": site_code, "written": True, "md_path": md_path, "key_csv_paths": key_csv_paths}
def write_flmp_pilot_data_markdowns(site_folder, gsheets_lookup=None, skip_metadata=True, sub_programs=None):
    """Write pilot-data summary markdown files for FLMP's sub-programs.

    FLMP is special: it contains multiple programs (CRLN, FLMP, FLSP) in one folder.
    Each program gets its own markdown file in its own site folder.

    :param site_folder: str, path to FLMP_pilot-data folder.
    :param gsheets_lookup: dict or none, Google Sheets lookup from _load_gsheets_lookup.
    :param skip_metadata: bool, if true preserve existing metadata and only replace content.
    :param sub_programs: list or none, specific sub-programs to process. None means all.
    :return results: list of dict, one result per sub-program.
    """
    results = []
    parent_folder = os.path.dirname(site_folder)
    programs_to_process = sub_programs if sub_programs else FLMP_SUB_PROGRAMS
    for program_code in programs_to_process:
        # Each program has its own site folder and csv folder
        if program_code == "FLMP":
            program_site_folder = site_folder
        else:
            program_site_folder = os.path.join(parent_folder, f"{program_code}_pilot-data")
        csv_folder = _get_csv_folder(program_site_folder, program_code)
        if not csv_folder:
            results.append({"program_code": program_code, "written": False, "reason": "csv_folder_not_found"})
            continue
        key_csv_paths = _find_key_csv_paths(csv_folder, program_code)
        md_filename = PILOT_SITE_MD_FILENAME_TEMPLATE.format(site_code=program_code)
        md_path = os.path.join(program_site_folder, md_filename)
        md_text = _render_site_pilot_data_markdown(program_code, program_site_folder, csv_folder, key_csv_paths, md_filename, gsheets_lookup, skip_metadata=skip_metadata)
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

### Aggregate data markdown generation
def _render_aggregate_pilot_data_markdown(pilot_data_root, aggregate_folder):
    """Render the aggregate pilot data markdown document.

    :param pilot_data_root: str, path to pilot-data root folder.
    :param aggregate_folder: str, path to aggregate_pilot-data folder.
    :return md_text: str, markdown document content.
    """
    today = datetime.date.today().isoformat()
    md_filename = AGGREGATE_MD_FILENAME
    aggregate_folder_name = os.path.basename(aggregate_folder)
    # Find CSV paths
    stats_kv_csv = os.path.join(aggregate_folder, AGGREGATE_STATS_KV_CSV)
    weekly_csv = os.path.join(aggregate_folder, AGGREGATE_WEEKLY_CSV)
    referral_agreement_csv = os.path.join(aggregate_folder, AGGREGATE_REFERRAL_AGREEMENT_CSV)
    # Compute summary info from weekly CSV
    weekly_totals = _compute_weekly_totals(weekly_csv if os.path.isfile(weekly_csv) else None)
    summary_parts = []
    if weekly_totals.get("tubes_total") is not None:
        summary_parts.append(f"Total tubes run: {weekly_totals['tubes_total']}")
    if weekly_totals.get("positive_tubes_total") is not None:
        summary_parts.append(f"Total positive tubes: {weekly_totals['positive_tubes_total']}")
    if weekly_totals.get("participants_total") is not None:
        summary_parts.append(f"Total participants: {weekly_totals['participants_total']}")
    if weekly_totals.get("week_start_min") and weekly_totals.get("week_end_max"):
        summary_parts.append(f"Date range: {weekly_totals['week_start_min']} to {weekly_totals['week_end_max']}")
    summary_short = "Aggregate FloodLAMP pilot data summary across all sites."
    if summary_parts:
        summary_short = summary_short + " " + "; ".join(summary_parts) + "."
    md_lines = []
    # Metadata block
    md_lines.append("METADATA")
    md_lines.append(f"last updated: {today}")
    md_lines.append(f"file_name: {md_filename}")
    md_lines.append(f"file_date: {today}")
    md_lines.append("title: Aggregate Pilot Data Summary")
    md_lines.append(f"category: {PILOT_SITE_MD_CATEGORY}")
    md_lines.append("subcategory: aggregate")
    md_lines.append("tags: ")
    md_lines.append("source_file_type: csv")
    md_lines.append(f"license: {PILOT_SITE_MD_LICENSE}")
    md_lines.append("notes: Aggregated statistics across all FloodLAMP pilot sites.")
    md_lines.append(f"summary_short: {summary_short}")
    md_lines.append("")
    md_lines.append("")
    md_lines.append("CONTENT")
    md_lines.append("")
    # Files section
    md_lines.append("## Files")
    md_lines.append("")
    md_lines.append("### Aggregate CSVs")
    md_lines.append(f"- Aggregate CSV folder: `{aggregate_folder_name}/`")
    # Note: aggregate CSVs are at the same level as the markdown file (no curated_csvs subfolder),
    # so relative links are just the filename, not aggregate_folder_name/filename
    if os.path.isfile(stats_kv_csv):
        md_lines.append(f"- Stats key-values CSV: [{AGGREGATE_STATS_KV_CSV}]({AGGREGATE_STATS_KV_CSV})")
    else:
        md_lines.append("- Stats key-values CSV: _not available_")
    if os.path.isfile(weekly_csv):
        md_lines.append(f"- Weekly summary CSV: [{AGGREGATE_WEEKLY_CSV}]({AGGREGATE_WEEKLY_CSV})")
    else:
        md_lines.append("- Weekly summary CSV: _not available_")
    if os.path.isfile(referral_agreement_csv):
        md_lines.append(f"- Referral agreement CSV: [{AGGREGATE_REFERRAL_AGREEMENT_CSV}]({AGGREGATE_REFERRAL_AGREEMENT_CSV})")
    else:
        md_lines.append("- Referral agreement CSV: _not available_")
    md_lines.append("")
    # Key tables section
    md_lines.append("## Key tables")
    md_lines.append("")
    # Stats key-values table
    md_lines.append("### Stats key-values")
    md_lines.append("")
    if os.path.isfile(stats_kv_csv):
        stats_data = _read_csv_rows(stats_kv_csv)
        formatted_rows = _format_stats_kv_rows(stats_data["headers"], stats_data["rows"])
        md_lines.append(_csv_rows_to_markdown_table(stats_data["headers"], formatted_rows))
    else:
        md_lines.append("_Stats key-values CSV not found._")
    md_lines.append("")
    # Weekly summary table
    md_lines.append("### Weekly summary")
    md_lines.append("")
    if os.path.isfile(weekly_csv):
        weekly_data = _read_csv_rows(weekly_csv)
        formatted_weekly_rows = _format_weekly_summary_rows(weekly_data["headers"], weekly_data["rows"])
        md_lines.append(_csv_rows_to_markdown_table(weekly_data["headers"], formatted_weekly_rows))
    else:
        md_lines.append("_Weekly summary CSV not found._")
    md_lines.append("")
    # Referral agreement table
    md_lines.append("### Referral agreement")
    md_lines.append("")
    if os.path.isfile(referral_agreement_csv):
        ref_data = _read_csv_rows(referral_agreement_csv)
        formatted_ref_rows = _format_referral_agreement_rows(ref_data["headers"], ref_data["rows"])
        md_lines.append(_csv_rows_to_markdown_table(ref_data["headers"], formatted_ref_rows))
    else:
        md_lines.append("_Referral agreement CSV not found._")
    md_lines.append("")
    return "\n".join(md_lines)
def write_aggregate_pilot_data_markdown(pilot_data_root):
    """Write the aggregate pilot-data summary markdown file.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return result: dict, summary with output path.
    """
    aggregate_folder = os.path.join(pilot_data_root, AGGREGATE_FOLDER_NAME)
    if not os.path.isdir(aggregate_folder):
        return {"written": False, "reason": "aggregate_folder_not_found"}
    md_text = _render_aggregate_pilot_data_markdown(pilot_data_root, aggregate_folder)
    md_path = os.path.join(aggregate_folder, AGGREGATE_MD_FILENAME)
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    return {"written": True, "md_path": md_path}

def write_all_sites_pilot_data_markdowns(pilot_data_root, sites_list=None, skip_metadata=True):
    """Write pilot-data summary markdown files for all or selected sites.

    :param pilot_data_root: str, path to pilot-data root folder.
    :param sites_list: list or none, specific site codes to process. None or empty list means all sites.
    :param skip_metadata: bool, if true preserve existing metadata and only replace content.
    :return results: dict, per-site results and totals.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    _print_section("PILOT DATA MARKDOWN: SETUP")
    _print_kv("Root folder", pilot_data_root)
    _print_kv("Skip metadata", skip_metadata)
    all_sites = _discover_site_folders(pilot_data_root)
    _print_kv("Sites found", len(all_sites))
    # Filter sites if sites_list is provided and non-empty
    if sites_list:
        sites_set = set(s.upper() for s in sites_list)
        # For FLMP sub-programs, include FLMP if any sub-program is requested
        flmp_sub_set = {"CRLN", "FLSP"}
        if sites_set & flmp_sub_set:
            sites_set.add("FLMP")
        sites = [(code, folder) for code, folder in all_sites if code in sites_set]
        _print_kv("Sites filtered to", [s[0] for s in sites])
    else:
        sites = all_sites
    # Load Google Sheets lookup
    gsheets_lookup = _load_gsheets_lookup(pilot_data_root)
    _print_kv("Google Sheets sites loaded", len(gsheets_lookup))
    _print_dash()
    results = {"sites": {}, "written": 0, "skipped": 0, "errors": 0}
    _print_section("PILOT DATA MARKDOWN: PER-SITE")
    for site_code, site_folder in sites:
        # FLMP is special: it has sub-programs that each get their own markdown
        if site_code == "FLMP":
            # Filter sub-programs if specific ones requested
            if sites_list:
                flmp_sub_filter = [p for p in FLMP_SUB_PROGRAMS if p in sites_set]
            else:
                flmp_sub_filter = None
            flmp_results = write_flmp_pilot_data_markdowns(site_folder, gsheets_lookup, skip_metadata=skip_metadata, sub_programs=flmp_sub_filter)
            results["sites"]["FLMP"] = {"sub_programs": flmp_results}
            for sub_r in flmp_results:
                if sub_r.get("written"):
                    results["written"] += 1
                    _print_kv(f"FLMP/{sub_r['program_code']}", f"WROTE {os.path.basename(sub_r['md_path'])}")
                else:
                    results["skipped"] += 1
                    _print_kv(f"FLMP/{sub_r['program_code']}", f"SKIP ({sub_r.get('reason')})")
            continue
        # DAVI is special: it has a custom referral-antigen-comparison markdown in addition to the standard summary
        if site_code == "DAVI":
            summary_r = write_site_pilot_data_markdown(site_code, site_folder, gsheets_lookup, skip_metadata=skip_metadata)
            antigen_r = write_davi_pilot_data_markdown(site_folder, gsheets_lookup)
            results["sites"]["DAVI"] = {"summary": summary_r, "referral_antigen_comparison": antigen_r}
            if summary_r.get("written"):
                results["written"] += 1
                _print_kv(f"{site_code}/SUMMARY", f"WROTE {os.path.basename(summary_r['md_path'])}")
            else:
                results["skipped"] += 1
                _print_kv(f"{site_code}/SUMMARY", f"SKIP ({summary_r.get('reason')})")
            if antigen_r.get("written"):
                results["written"] += 1
                _print_kv(f"{site_code}/REFERRAL-ANTIGEN", f"WROTE {os.path.basename(antigen_r['md_path'])}")
            else:
                results["skipped"] += 1
                _print_kv(f"{site_code}/REFERRAL-ANTIGEN", f"SKIP ({antigen_r.get('reason')})")
            continue
        r = write_site_pilot_data_markdown(site_code, site_folder, gsheets_lookup, skip_metadata=skip_metadata)
        results["sites"][site_code] = r
        if r.get("written"):
            results["written"] += 1
            _print_kv(site_code, f"WROTE {os.path.basename(r['md_path'])}")
        else:
            results["skipped"] += 1
            _print_kv(site_code, f"SKIP ({r.get('reason')})")
    _print_dash()
    # Write aggregate markdown only if processing all sites
    if not sites_list:
        _print_section("PILOT DATA MARKDOWN: AGGREGATE")
        aggregate_result = write_aggregate_pilot_data_markdown(pilot_data_root)
        results["aggregate"] = aggregate_result
        if aggregate_result.get("written"):
            results["written"] += 1
            _print_kv("AGGREGATE", f"WROTE {os.path.basename(aggregate_result['md_path'])}")
        else:
            results["skipped"] += 1
            _print_kv("AGGREGATE", f"SKIP ({aggregate_result.get('reason')})")
        _print_dash()
    _print_section("PILOT DATA MARKDOWN: SUMMARY")
    _print_kv("Markdown files written", results["written"])
    _print_kv("Sites skipped", results["skipped"])
    _print_section("PILOT DATA MARKDOWN: DONE")
    return results
def mrun_write_all_sites_pilot_data_markdowns():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    sites_list=["CRLN"]
    write_all_sites_pilot_data_markdowns(pilot_data_root, sites_list=sites_list, skip_metadata=True)

### Stats metrics consistency: reference-based checking
# Reference CSV file name for stats metrics consistency checking
STATS_METRICS_REFERENCE_FILENAME = "reference_stats_metrics.csv"
# Sections to exclude from consistency checking (Files is site-specific filenames, Pooling only exists for FLMP)
STATS_METRICS_IGNORE_SECTIONS = {"Files", "Pooling"}
def _find_stats_kv_csv_for_site(pilot_data_root, site_code):
    """Find the stats_key-values.csv file for a given site.

    :param pilot_data_root: str, path to pilot-data root folder.
    :param site_code: str, 4-letter site code.
    :return path: str or none, path to stats_key-values.csv file if found.
    """
    site_folder = os.path.join(pilot_data_root, f"{site_code}_pilot-data")
    if not os.path.isdir(site_folder):
        return None
    csv_folder = os.path.join(site_folder, f"{site_code}_curated_csvs")
    if not os.path.isdir(csv_folder):
        return None
    return _choose_stats_kv_csv_path_agg(csv_folder, site_code)
def _read_stats_kv_metrics(stats_kv_path):
    """Read section/metric/details from a stats_key-values.csv file.

    :param stats_kv_path: str, path to stats_key-values.csv file.
    :return metrics: list of dict with section, metric, details keys.
    """
    metrics = []
    if not stats_kv_path or not os.path.isfile(stats_kv_path):
        return metrics
    with open(stats_kv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            section = row.get("section", "").strip()
            metric = row.get("metric", "").strip()
            details = row.get("details", "").strip()
            if section and metric:
                metrics.append({"section": section, "metric": metric, "details": details})
    return metrics
def create_reference_stats_metrics(pilot_data_root, site_code):
    """Create reference_stats_metrics.csv from a given site's stats_key-values.csv.

    The reference file contains section, metric, details columns and is used
    for consistency checking against all other sites.

    :param pilot_data_root: str, path to pilot-data root folder.
    :param site_code: str, 4-letter site code to use as reference source.
    :return result: dict with status, reference_path, metrics_count, source_path.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    stats_kv_path = _find_stats_kv_csv_for_site(pilot_data_root, site_code)
    if not stats_kv_path:
        return {"status": "error", "error": f"Could not find stats_key-values.csv for site {site_code}"}
    metrics = _read_stats_kv_metrics(stats_kv_path)
    if not metrics:
        return {"status": "error", "error": f"No metrics found in {stats_kv_path}"}
    # Filter out ignored sections (only Files and Pooling)
    filtered_metrics = [m for m in metrics if m["section"] not in STATS_METRICS_IGNORE_SECTIONS]
    reference_path = os.path.join(pilot_data_root, STATS_METRICS_REFERENCE_FILENAME)
    with open(reference_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["section", "metric", "details"])
        writer.writeheader()
        for m in filtered_metrics:
            writer.writerow(m)
    return {"status": "ok", "reference_path": reference_path, "metrics_count": len(filtered_metrics), "source_path": stats_kv_path, "source_site": site_code}
def mrun_create_reference_stats_metrics():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    site_code = "ABRM"
    result = create_reference_stats_metrics(pilot_data_root, site_code)
    print(f"Reference created: {result}")
def _read_reference_stats_metrics(pilot_data_root):
    """Read the reference_stats_metrics.csv file.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return metrics: set of (section, metric) tuples, or None if file not found.
    """
    reference_path = os.path.join(pilot_data_root, STATS_METRICS_REFERENCE_FILENAME)
    if not os.path.isfile(reference_path):
        return None
    metrics = set()
    with open(reference_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            section = row.get("section", "").strip()
            metric = row.get("metric", "").strip()
            if section and metric:
                metrics.add((section, metric))
    return metrics
def stats_metrics_consistency_check(pilot_data_root):
    """Check all site stats_key-values.csv files for consistency against the reference.

    Compares each site's (section, metric) pairs against reference_stats_metrics.csv.
    Reports differences clearly and summarizes which sites are consistent.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return result: bool, True if all sites are consistent with reference.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    _print_section("STATS METRICS CONSISTENCY CHECK")
    # Read reference file
    reference_metrics = _read_reference_stats_metrics(pilot_data_root)
    if reference_metrics is None:
        reference_path = os.path.join(pilot_data_root, STATS_METRICS_REFERENCE_FILENAME)
        _print_kv("Status", "ERROR - Reference file not found")
        _print_kv("Expected", reference_path)
        print("  Create reference with: create_reference_stats_metrics(pilot_data_root, site_code)")
        _print_dash()
        return False
    _print_kv("Reference file", os.path.join(pilot_data_root, STATS_METRICS_REFERENCE_FILENAME))
    _print_kv("Reference metrics count", len(reference_metrics))
    # Discover all sites
    sites = _discover_site_folders(pilot_data_root)
    if not sites:
        _print_kv("Status", "ERROR - No site folders found")
        _print_dash()
        return False
    # Check each site against reference
    consistent_sites = []
    inconsistent_sites = []
    site_details = {}
    for site_code, site_folder in sites:
        csv_folder = os.path.join(site_folder, f"{site_code}_curated_csvs")
        stats_kv_path = _choose_stats_kv_csv_path_agg(csv_folder, site_code)
        if not stats_kv_path or not os.path.isfile(stats_kv_path):
            site_details[site_code] = {"status": "missing", "path": None, "error": "stats_key-values.csv not found"}
            inconsistent_sites.append(site_code)
            continue
        # Read site metrics (excluding ignored sections)
        site_metrics = set()
        with open(stats_kv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                section = row.get("section", "").strip()
                metric = row.get("metric", "").strip()
                if section in STATS_METRICS_IGNORE_SECTIONS:
                    continue
                if section and metric:
                    site_metrics.add((section, metric))
        # Compare against reference
        in_ref_not_site = reference_metrics - site_metrics
        in_site_not_ref = site_metrics - reference_metrics
        if in_ref_not_site or in_site_not_ref:
            inconsistent_sites.append(site_code)
            site_details[site_code] = {"status": "inconsistent", "path": stats_kv_path, "missing_from_site": sorted(in_ref_not_site), "extra_in_site": sorted(in_site_not_ref)}
        else:
            consistent_sites.append(site_code)
            site_details[site_code] = {"status": "consistent", "path": stats_kv_path}
    # Print inconsistency details first
    if inconsistent_sites:
        print()
        print("INCONSISTENCIES FOUND:")
        print()
        for site_code in inconsistent_sites:
            info = site_details[site_code]
            print(f"  {site_code}:")
            if info.get("path"):
                print(f"    File: {info['path']}")
            if info.get("error"):
                print(f"    Error: {info['error']}")
                continue
            if info.get("missing_from_site"):
                print(f"    Missing from site (in reference but not in site):")
                for section, metric in info["missing_from_site"]:
                    print(f"      - [{section}] {metric}")
            if info.get("extra_in_site"):
                print(f"    Extra in site (in site but not in reference):")
                for section, metric in info["extra_in_site"]:
                    print(f"      - [{section}] {metric}")
            print()
    # Print summary
    print()
    _print_section("SUMMARY")
    _print_kv("Total sites", len(sites))
    _print_kv("Consistent sites", len(consistent_sites))
    _print_kv("Inconsistent sites", len(inconsistent_sites))
    if consistent_sites:
        print(f"  Consistent: {', '.join(sorted(consistent_sites))}")
    if inconsistent_sites:
        print(f"  Inconsistent: {', '.join(sorted(inconsistent_sites))}")
    _print_dash()
    return len(inconsistent_sites) == 0
def mrun_stats_metrics_consistency_check():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    stats_metrics_consistency_check(pilot_data_root)

### Aggregate values comparison
REFERENCE_AGGREGATE_STATS_CSV = "reference_aggregate_stats.csv"
# Sections to skip in aggregate values comparison (not meaningful to compare)
AGGREGATE_COMPARISON_SKIP_SECTIONS = {"Dates", "Info"}
def _normalize_value_for_comparison(value):
    """Normalize a value for comparison (remove commas, handle percentages, etc).

    :param value: str, the value to normalize.
    :return normalized: str, normalized value for comparison.
    """
    if value is None:
        return ""
    v = str(value).strip()
    if not v:
        return ""
    # Remove commas from numbers
    v = v.replace(",", "")
    # Handle percentages - convert to decimal form for comparison
    if v.endswith("%"):
        try:
            pct = float(v[:-1])
            return f"{pct / 100:.6f}"  # Store as decimal with precision
        except ValueError:
            return v
    # Try to normalize as float for consistent comparison
    try:
        num = float(v)
        # Check if it's effectively an integer
        if num == int(num) and "." not in v:
            return str(int(num))
        return f"{num:.6f}"
    except ValueError:
        return v
def _values_match(ref_value, computed_value, tolerance=0.10):
    """Check if two values match within tolerance.

    :param ref_value: str, reference value.
    :param computed_value: str, computed value.
    :param tolerance: float, relative tolerance for numeric comparison (default 10% for rounded percentages).
    :return match: bool, True if values match.
    """
    ref_norm = _normalize_value_for_comparison(ref_value)
    comp_norm = _normalize_value_for_comparison(computed_value)
    # Empty values
    if not ref_norm and not comp_norm:
        return True
    if not ref_norm or not comp_norm:
        return False
    # Exact string match
    if ref_norm == comp_norm:
        return True
    # Try numeric comparison with tolerance
    try:
        ref_num = float(ref_norm)
        comp_num = float(comp_norm)
        if ref_num == 0:
            return abs(comp_num) < 0.0001  # Small absolute tolerance for zero
        rel_diff = abs(ref_num - comp_num) / abs(ref_num)
        return rel_diff <= tolerance
    except ValueError:
        return False
def aggregate_values_comparison(pilot_data_root):
    """Compare pub (generated) aggregate stats CSV values against reference expected values.

    Reads reference_aggregate_stats.csv and compares against the generated
    aggregate_pilot-data_stats_key-values.csv. Reports matches and discrepancies.

    :param pilot_data_root: str, path to pilot-data root folder.
    :return result: dict, comparison results with matches and discrepancies.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    _print_section("AGGREGATE VALUES COMPARISON")
    # Read reference file
    ref_csv_path = os.path.join(pilot_data_root, REFERENCE_AGGREGATE_STATS_CSV)
    if not os.path.isfile(ref_csv_path):
        _print_kv("Status", "ERROR - Reference file not found")
        _print_kv("Expected", ref_csv_path)
        _print_dash()
        return {"error": "reference_not_found", "matches": 0, "discrepancies": 0}
    # Read pub (generated aggregate) stats CSV
    pub_csv_path = os.path.join(pilot_data_root, AGGREGATE_FOLDER_NAME, "aggregate_pilot-data_stats_key-values.csv")
    if not os.path.isfile(pub_csv_path):
        _print_kv("Status", "ERROR - Pub stats CSV not found")
        _print_kv("Expected", pub_csv_path)
        _print_dash()
        return {"error": "pub_not_found", "matches": 0, "discrepancies": 0}
    _print_kv("Reference file", os.path.basename(ref_csv_path))
    _print_kv("Pub file", os.path.basename(pub_csv_path))
    # Load reference values (skip Dates/Info sections)
    ref_values = {}
    with open(ref_csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            section = (row.get("section") or "").strip()
            metric = (row.get("metric") or "").strip()
            value = (row.get("aggregate_value") or "").strip()
            if section in AGGREGATE_COMPARISON_SKIP_SECTIONS:
                continue
            if section and metric:
                ref_values[(section, metric)] = value
    # Load pub values (skip Dates/Info sections)
    pub_values = {}
    with open(pub_csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            section = (row.get("section") or "").strip()
            metric = (row.get("metric") or "").strip()
            value = (row.get("value") or "").strip()
            if section in AGGREGATE_COMPARISON_SKIP_SECTIONS:
                continue
            if section and metric:
                pub_values[(section, metric)] = value
    # Compare values
    matches = []
    discrepancies = []
    ref_only = []
    pub_only = []
    for key in ref_values:
        section, metric = key
        ref_val = ref_values[key]
        if key not in pub_values:
            ref_only.append({"section": section, "metric": metric, "reference": ref_val})
            continue
        pub_val = pub_values[key]
        # Skip comparison if reference is empty
        if not ref_val:
            continue
        if _values_match(ref_val, pub_val):
            matches.append({"section": section, "metric": metric, "reference": ref_val, "pub": pub_val})
        else:
            discrepancies.append({"section": section, "metric": metric, "reference": ref_val, "pub": pub_val})
    for key in pub_values:
        if key not in ref_values:
            section, metric = key
            pub_only.append({"section": section, "metric": metric, "pub": pub_values[key]})
    # Print results
    _print_kv("Reference metrics", len(ref_values))
    _print_kv("Pub metrics", len(pub_values))
    print()
    _print_kv("MATCHES", len(matches))
    _print_kv("DISCREPANCIES", len(discrepancies))
    if ref_only:
        _print_kv("In reference only (missing from pub)", len(ref_only))
    if pub_only:
        _print_kv("In pub only (not in reference)", len(pub_only))
    # Print discrepancy details
    if discrepancies:
        print()
        print("DISCREPANCIES:")
        for d in discrepancies:
            print(f"  [{d['section']}] {d['metric']}")
            print(f"    Reference:  {d['reference']}")
            print(f"    Pub:        {d['pub']}")
    # Print metrics missing from pub (in reference only)
    if ref_only:
        print()
        print("IN REFERENCE ONLY (missing from pub):")
        for r in ref_only:
            ref_val = r['reference'] if r['reference'] else "(no value in reference)"
            print(f"  [{r['section']}] {r['metric']}: {ref_val}")
    # Print metrics only in pub
    if pub_only:
        print()
        print("IN PUB ONLY (not in reference):")
        for p in pub_only:
            print(f"  [{p['section']}] {p['metric']}: {p['pub']}")
    _print_dash()
    return {
        "matches": len(matches),
        "discrepancies": len(discrepancies),
        "ref_only": len(ref_only),
        "pub_only": len(pub_only),
        "discrepancy_details": discrepancies,
        "ref_only_details": ref_only,
    }
def mrun_aggregate_values_comparison():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    aggregate_values_comparison(pilot_data_root)

def run_pilot_data_pipeline(pilot_data_root, do_errant_check=True, do_zip=True, do_aggregate=True, do_markdowns=True, do_values_comparison=True):
    """Run the complete pilot data processing pipeline.

    This is the main entry point that orchestrates all pilot data operations:
    1. Errant value check (optional)
    2. Zip creation (optional)
    3. Aggregate CSV generation (uses latest zip if do_zip=False)
    4. Markdown generation (optional)
    5. Aggregate values comparison (optional)

    :param pilot_data_root: str, path to pilot-data root folder.
    :param do_errant_check: bool, whether to run errant value check.
    :param do_zip: bool, whether to create new zips.
    :param do_aggregate: bool, whether to run aggregate CSV generation.
    :param do_markdowns: bool, whether to generate markdown files.
    :param do_values_comparison: bool, whether to run aggregate values comparison.
    :return: dict, results from all pipeline stages.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)
    results = {
        "pilot_data_root": pilot_data_root,
        "metrics_check": None,
        "errant_check": None,
        "zip": None,
        "aggregate": None,
        "markdowns": None,
        "values_comparison": None,
    }
    print()
    _print_section("PILOT DATA PIPELINE: START")
    _print_kv("Root folder", pilot_data_root)
    _print_kv("do_errant_check", do_errant_check)
    _print_kv("do_zip", do_zip)
    _print_kv("do_aggregate", do_aggregate)
    _print_kv("do_markdowns", do_markdowns)
    _print_kv("do_values_comparison", do_values_comparison)
    _print_dash()

    # Step 1: Errant check
    if do_errant_check:
        errant_report_path = os.path.join(pilot_data_root, "errant_values_report.csv")
        results["errant_check"] = run_errant_check(pilot_data_root, output_report_path=errant_report_path)
    # Step 2: Zip creation
    zipall_csvs_path = None
    if do_zip:
        zip_result = run_zip_pilot_data(pilot_data_root)
        results["zip"] = zip_result
        if zip_result and "combined_result" in zip_result:
            zipall_csvs_path = zip_result["combined_result"].get("zipall_csvs")
    # Step 3: Aggregate CSV generation
    if do_aggregate:
        results["aggregate"] = run_aggregate_csvs(pilot_data_root, zipall_csvs_path=zipall_csvs_path)
    # Step 4: Markdown generation
    if do_markdowns:
        print()  # Blank line before markdown output
        results["markdowns"] = write_all_sites_pilot_data_markdowns(pilot_data_root)
        print()  # Blank line after markdown output
    # Step 5: Aggregate values comparison
    if do_values_comparison:
        print()  # Blank line before comparison output
        results["values_comparison"] = aggregate_values_comparison(pilot_data_root)
    print()
    _print_section("PILOT DATA PIPELINE: COMPLETE")
    print()
    return results
def mrun_pilot_data_pipeline():
    pass
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    run_pilot_data_pipeline(pilot_data_root, do_errant_check=True, do_zip=True, do_aggregate=True, do_markdowns=True, do_values_comparison=True)

### Extended Zips: include markdown files and plots
def _get_md_files(site_folder):
    """Get all markdown files from a site folder root (not subfolders).

    :param site_folder: str, path to site folder.
    :return: list of str, full file paths to .md files.
    """
    md_files = []
    if not os.path.isdir(site_folder):
        return md_files
    for entry in os.listdir(site_folder):
        full_path = os.path.join(site_folder, entry)
        if os.path.isfile(full_path) and entry.lower().endswith(".md"):
            md_files.append(full_path)
    md_files.sort()
    return md_files
def _get_plots_folder(site_folder):
    """Get the _plots folder path for a site.

    :param site_folder: str, path to site folder.
    :return: str or None, path to _plots folder if exists.
    """
    plots_folder = os.path.join(site_folder, "_plots")
    if os.path.isdir(plots_folder):
        return plots_folder
    return None
def _get_plot_files(site_folder):
    """Get all plot files (PNG and PDF) from _plots subfolder.

    :param site_folder: str, path to site folder.
    :return: list of str, full file paths to plot files.
    """
    plots_folder = _get_plots_folder(site_folder)
    if not plots_folder:
        return []
    return _list_files_in_folder(plots_folder, extensions=[".png", ".pdf"])
def zip_site_data_extended(site_code, site_folder, output_folder):
    """Create extended zip archive for a single site including CSVs, XLSX, MDs, and plots.

    Creates:
    - {SITE}_pilot-data_csvs-xlsx-mds-plots.zip: CSVs + XLSX + markdown files + plots

    :param site_code: str, 4-letter site code.
    :param site_folder: str, path to site folder.
    :param output_folder: str, path to output folder for zips.
    :return: dict, summary with zip path and file counts.
    """
    csv_folder = _get_csv_folder(site_folder, site_code)
    xlsx_folder = _get_xlsx_folder(site_folder, site_code)
    plots_folder = _get_plots_folder(site_folder)

    results = {
        "site_code": site_code,
        "extended_zip": None,
        "csv_count": 0,
        "xlsx_count": 0,
        "md_count": 0,
        "plot_count": 0,
    }

    # Collect CSV files
    csv_files = []
    if csv_folder:
        csv_files = _list_files_in_folder(csv_folder, extensions=[".csv"])
    results["csv_count"] = len(csv_files)

    # Collect XLSX files
    xlsx_files = []
    if xlsx_folder:
        xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
    results["xlsx_count"] = len(xlsx_files)

    # Collect markdown files
    md_files = _get_md_files(site_folder)
    results["md_count"] = len(md_files)

    # Collect plot files
    plot_files = _get_plot_files(site_folder)
    results["plot_count"] = len(plot_files)

    total_files = len(csv_files) + len(xlsx_files) + len(md_files) + len(plot_files)
    if total_files == 0:
        _print_kv(f"  {site_code}", "SKIP (no files found)")
        return results

    # Create extended zip
    extended_zip_path = os.path.join(output_folder, f"{site_code}_pilot-data_csvs-xlsx-mds-plots.zip")
    files_with_arcnames = []
    for f in csv_files:
        files_with_arcnames.append((f, os.path.basename(f)))
    for f in xlsx_files:
        files_with_arcnames.append((f, os.path.basename(f)))
    for f in md_files:
        files_with_arcnames.append((f, os.path.basename(f)))
    for f in plot_files:
        # Put plots in _plots subfolder in archive
        files_with_arcnames.append((f, os.path.join("_plots", os.path.basename(f))))
    count = _create_zip(extended_zip_path, files_with_arcnames)
    results["extended_zip"] = extended_zip_path
    _print_kv(f"  {site_code}", f"CREATED {os.path.basename(extended_zip_path)} ({count} files: {results['csv_count']} csv, {results['xlsx_count']} xlsx, {results['md_count']} md, {results['plot_count']} plots)")

    return results
def zip_aggregate_data_extended(pilot_data_root, output_folder):
    """Create extended zip archive for aggregate data including CSVs, MDs, and plots.

    Creates:
    - aggregate_pilot-data_csvs-mds-plots.zip: Aggregate CSVs + markdown + plots

    :param pilot_data_root: str, path to pilot-data root folder.
    :param output_folder: str, path to output folder for zips.
    :return: dict, summary with zip path and file counts.
    """
    aggregate_folder = os.path.join(pilot_data_root, AGGREGATE_FOLDER_NAME)

    results = {
        "aggregate_zip": None,
        "csv_count": 0,
        "md_count": 0,
        "plot_count": 0,
    }

    if not os.path.isdir(aggregate_folder):
        _print_kv("  AGGREGATE", f"SKIP (folder not found: {AGGREGATE_FOLDER_NAME})")
        return results

    # Collect CSV files from aggregate folder root
    csv_files = _list_files_in_folder(aggregate_folder, extensions=[".csv"])
    results["csv_count"] = len(csv_files)

    # Collect markdown files from aggregate folder root
    md_files = _get_md_files(aggregate_folder)
    results["md_count"] = len(md_files)

    # Collect plot files from _plots subfolder
    plot_files = _get_plot_files(aggregate_folder)
    results["plot_count"] = len(plot_files)

    total_files = len(csv_files) + len(md_files) + len(plot_files)
    if total_files == 0:
        _print_kv("  AGGREGATE", "SKIP (no files found)")
        return results

    # Create aggregate zip
    aggregate_zip_path = os.path.join(output_folder, "aggregate_pilot-data_csvs-mds-plots.zip")
    files_with_arcnames = []
    for f in csv_files:
        files_with_arcnames.append((f, os.path.basename(f)))
    for f in md_files:
        files_with_arcnames.append((f, os.path.basename(f)))
    for f in plot_files:
        # Put plots in _plots subfolder in archive
        files_with_arcnames.append((f, os.path.join("_plots", os.path.basename(f))))
    count = _create_zip(aggregate_zip_path, files_with_arcnames)
    results["aggregate_zip"] = aggregate_zip_path
    _print_kv("  AGGREGATE", f"CREATED {os.path.basename(aggregate_zip_path)} ({count} files: {results['csv_count']} csv, {results['md_count']} md, {results['plot_count']} plots)")

    return results
def zip_all_sites_combined_extended(sites_data, pilot_data_root, output_folder):
    """Create combined extended zip archive for all sites plus aggregate.

    Creates:
    - ZIPALL_pilot-data_csvs-xlsx-mds-plots.zip: All CSVs, XLSX, MDs, and plots from all sites + aggregate

    :param sites_data: list of dicts, site data from zip_site_data_extended calls.
    :param pilot_data_root: str, path to pilot-data root folder.
    :param output_folder: str, path to output folder for zips.
    :return: dict, summary with zip path and file counts.
    """
    results = {
        "zipall_extended": None,
        "total_csv_count": 0,
        "total_xlsx_count": 0,
        "total_md_count": 0,
        "total_plot_count": 0,
    }

    all_files = []

    # Collect files from all sites
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
                arcname = os.path.join(f"{site_code}_pilot-data", csv_folder_name, os.path.basename(f))
                all_files.append((f, arcname))
            results["total_csv_count"] += len(csv_files)

        # Collect XLSX files with folder structure preserved
        if xlsx_folder:
            xlsx_files = _list_files_in_folder(xlsx_folder, extensions=[".xlsx"])
            xlsx_folder_name = os.path.basename(xlsx_folder)
            for f in xlsx_files:
                arcname = os.path.join(f"{site_code}_pilot-data", xlsx_folder_name, os.path.basename(f))
                all_files.append((f, arcname))
            results["total_xlsx_count"] += len(xlsx_files)

        # Collect MD files
        md_files = _get_md_files(site_folder)
        for f in md_files:
            arcname = os.path.join(f"{site_code}_pilot-data", os.path.basename(f))
            all_files.append((f, arcname))
        results["total_md_count"] += len(md_files)

        # Collect plot files
        plot_files = _get_plot_files(site_folder)
        for f in plot_files:
            arcname = os.path.join(f"{site_code}_pilot-data", "_plots", os.path.basename(f))
            all_files.append((f, arcname))
        results["total_plot_count"] += len(plot_files)

    # Collect files from aggregate folder
    aggregate_folder = os.path.join(pilot_data_root, AGGREGATE_FOLDER_NAME)
    if os.path.isdir(aggregate_folder):
        # Aggregate CSVs
        agg_csv_files = _list_files_in_folder(aggregate_folder, extensions=[".csv"])
        for f in agg_csv_files:
            arcname = os.path.join(AGGREGATE_FOLDER_NAME, os.path.basename(f))
            all_files.append((f, arcname))
        results["total_csv_count"] += len(agg_csv_files)

        # Aggregate MDs
        agg_md_files = _get_md_files(aggregate_folder)
        for f in agg_md_files:
            arcname = os.path.join(AGGREGATE_FOLDER_NAME, os.path.basename(f))
            all_files.append((f, arcname))
        results["total_md_count"] += len(agg_md_files)

        # Aggregate plots
        agg_plot_files = _get_plot_files(aggregate_folder)
        for f in agg_plot_files:
            arcname = os.path.join(AGGREGATE_FOLDER_NAME, "_plots", os.path.basename(f))
            all_files.append((f, arcname))
        results["total_plot_count"] += len(agg_plot_files)

    if not all_files:
        _print_kv("ZIPALL", "SKIP (no files found)")
        return results

    # Create ZIPALL extended zip
    zipall_path = os.path.join(output_folder, "ZIPALL_pilot-data_csvs-xlsx-mds-plots.zip")
    count = _create_zip(zipall_path, all_files)
    results["zipall_extended"] = zipall_path
    _print_kv("ZIPALL", f"CREATED {os.path.basename(zipall_path)} ({count} files: {results['total_csv_count']} csv, {results['total_xlsx_count']} xlsx, {results['total_md_count']} md, {results['total_plot_count']} plots)")

    return results
def run_zip_pilot_data_extended(pilot_data_root):
    """Create extended zip archives including CSVs, XLSX, MDs, and plots.

    Creates a timestamped output folder and generates:
    - Per-site extended zips (CSVs+XLSX+MDs+plots)
    - Aggregate extended zip (CSVs+MDs+plots)
    - Combined ZIPALL extended zip (all sites + aggregate)

    :param pilot_data_root: str, path to pilot-data root folder.
    :return: dict, summary of all operations.
    """
    pilot_data_root = os.path.abspath(pilot_data_root)

    _print_section("ZIP PILOT DATA EXTENDED: SETUP")
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
    output_folder_name = f"zips_pilot-data-extended_{timestamp}"
    output_folder = os.path.join(pilot_data_root, output_folder_name)
    _ensure_folder(output_folder)

    _print_section("ZIP PILOT DATA EXTENDED: OUTPUT FOLDER")
    _print_kv("Output folder", output_folder)
    _print_dash()

    # Process each site
    _print_section("ZIP PILOT DATA EXTENDED: PER-SITE ZIPS")
    sites_data = []
    for site_code, site_folder in sites:
        result = zip_site_data_extended(site_code, site_folder, output_folder)
        result["site_folder"] = site_folder
        sites_data.append(result)
    _print_dash()

    # Create aggregate zip
    _print_section("ZIP PILOT DATA EXTENDED: AGGREGATE ZIP")
    aggregate_result = zip_aggregate_data_extended(pilot_data_root, output_folder)
    _print_dash()

    # Create combined zip
    _print_section("ZIP PILOT DATA EXTENDED: COMBINED ZIPALL")
    combined_result = zip_all_sites_combined_extended(sites_data, pilot_data_root, output_folder)
    _print_dash()

    # Summary
    _print_section("ZIP PILOT DATA EXTENDED: SUMMARY")
    total_zips = 0
    for site_result in sites_data:
        if site_result["extended_zip"]:
            total_zips += 1
    if aggregate_result.get("aggregate_zip"):
        total_zips += 1
    if combined_result.get("zipall_extended"):
        total_zips += 1

    _print_kv("Total zip files created", total_zips)
    _print_kv("Output folder", output_folder)
    _print_section("ZIP PILOT DATA EXTENDED: DONE")

    return {
        "output_folder": output_folder,
        "sites_data": sites_data,
        "aggregate_result": aggregate_result,
        "combined_result": combined_result,
        "total_zips": total_zips,
    }
def mrun_zip_pilot_data_extended():
    pass
if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    run_zip_pilot_data_extended(pilot_data_root)
