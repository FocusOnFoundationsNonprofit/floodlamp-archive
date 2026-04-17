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
if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    run_errant_check(pilot_data_root, output_report_path=pilot_data_root + "/errant_values_report.csv")

