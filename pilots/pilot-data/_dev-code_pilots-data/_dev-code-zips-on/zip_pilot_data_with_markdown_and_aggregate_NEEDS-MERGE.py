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
#    pilot_data_root = "data/floodlamp/pilots/pilot-data"
#    run_errant_check(pilot_data_root, output_report_path=pilot_data_root + "/errant_values_report.csv")



### Markdown generation: pilot site summaries
# This section creates per-site archive markdown files based on key curated CSVs.
# It is intentionally conservative: it only reads curated CSVs and writes markdown into each site folder.

PILOT_SITE_MD_FILENAME_TEMPLATE = "{site_code}_pilot-data_summary.md"
PILOT_SITE_MD_CATEGORY = "pilot-data"
PILOT_SITE_MD_SUBCATEGORY = "pilot-site"
PILOT_SITE_MD_LICENSE = "CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/"
PILOT_SITE_MD_SKIP_SITE_CODES = {"FLMP", "DAVI"}  # Skip special-case sites for now (handled separately later)

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
def _render_site_pilot_data_markdown(site_code, site_folder, csv_folder, key_csv_paths, md_filename):
    """Render a site pilot-data summary markdown document.

    :param site_code: str, 4-letter site code.
    :param site_folder: str, site folder path.
    :param csv_folder: str, curated CSV folder path.
    :param key_csv_paths: dict, key CSV paths (stats_kv_csv, weekly_csv, rtr_by_person_csv).
    :param md_filename: str, markdown file name (not full path).
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
    xlsx_links = _list_xlsx_links_for_site(site_folder, site_code)
    if xlsx_links:
        md_lines.append("- XLSX downloads:")
        for x in xlsx_links:
            md_lines.append(f"  - [{x['label']}]({x['relpath']})")
    else:
        md_lines.append("- XLSX downloads: _not available_")
    md_lines.append("")
    md_lines.append("## Key tables")
    md_lines.append("")
    md_lines.append("### Stats key-values")
    md_lines.append("")
    if key_csv_paths.get("stats_kv_csv"):
        stats_data = _read_csv_rows(key_csv_paths["stats_kv_csv"])
        md_lines.append(_csv_rows_to_markdown_table(stats_data["headers"], stats_data["rows"]))
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
def write_site_pilot_data_markdown(site_code, site_folder):
    """Write a pilot-data summary markdown file for a single site.

    :param site_code: str, 4-letter site code.
    :param site_folder: str, site folder path.
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
    md_text = _render_site_pilot_data_markdown(site_code, site_folder, csv_folder, key_csv_paths, md_filename)
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    return {"site_code": site_code, "written": True, "md_path": md_path, "key_csv_paths": key_csv_paths}
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
    _print_dash()
    results = {"sites": {}, "written": 0, "skipped": 0, "errors": 0}
    _print_section("PILOT DATA MARKDOWN: PER-SITE")
    for site_code, site_folder in sites:
        r = write_site_pilot_data_markdown(site_code, site_folder)
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
#if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    write_all_sites_pilot_data_markdowns(pilot_data_root)

### Aggregation: cross-site rollups
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
    if included == 0:
        return {"value": "", "value_status": "not_available", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
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
    if included == 0:
        return {"value": "", "value_status": "not_available", "sites_included_n": included, "sites_missing_n": missing, "raw_values": raw_values}
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
def _aggregate_stats_key_values(site_code_to_stats_kv_path, output_csv_path):
    """Aggregate selected stats key-values across all sites into a single CSV.

    :param site_code_to_stats_kv_path: dict, mapping site_code -> stats key-values CSV path.
    :param output_csv_path: str, output CSV path.
    :return result: dict, summary of aggregation.
    """
    site_metric_maps = {}
    for site_code, stats_kv_path in site_code_to_stats_kv_path.items():
        site_metric_maps[site_code] = _read_stats_kv_map(stats_kv_path)

    METRICS = [
        {"section": "Overall", "metric": "Number of Tubes Tested (initial only - no re-runs)", "metric_id": "tubes_tested_initial", "kind": "sum_int", "aliases": ["Number of Tubes Tested (initial only - no re-runs)"]},
        {"section": "Overall", "metric": "Number of Tube Tests Run (includes re-runs)", "metric_id": "tube_tests_run_total", "kind": "sum_int", "aliases": ["Number of Tube Tests Run (includes re-runs)"]},
        {"section": "Overall", "metric": "Number of Initial Runs", "metric_id": "initial_runs", "kind": "sum_int", "aliases": ["Number of Initial Runs"]},
        {"section": "Overall", "metric": "Number of APS Only Tubes run", "metric_id": "aps_only_tubes", "kind": "sum_int", "aliases": ["Number of APS Only Tubes run"]},
        {"section": "Overall", "metric": "Number of Test Reactions (RFR plus APS only tubes)", "metric_id": "test_reactions", "kind": "sum_int", "aliases": ["Number of Test Reactions (RFR plus APS only tubes run)", "Number of Test Reactions (RFR plus APS only tubes)"]},
        {"section": "Overall", "metric": "Number of Participant Results", "metric_id": "participant_results", "kind": "sum_int", "aliases": ["Number of Participant Results"]},
        {"section": "Overall", "metric": "Number of ARF Tubes", "metric_id": "arf_tubes", "kind": "sum_int", "aliases": ["Number of ARF Tubes"]},
        {"section": "Overall", "metric": "Sum of Participant Results plus ARF Tubes", "metric_id": "participant_plus_arf", "kind": "derived_sum", "numerator_ids": ["participant_results", "arf_tubes"]},
        {"section": "Overall", "metric": "Average Pool Level (excludes ARF)", "metric_id": "avg_pool_level", "kind": "ratio", "numerator_id": "participant_results", "denom_id": "tubes_tested_initial"},
        {"section": "Re-runs", "metric": "Number of Run Tubes (Re-runs only)", "metric_id": "rerun_tubes", "kind": "sum_int", "aliases": ["Number of Run Tubes (Re-runs only)"]},
        {"section": "Re-runs", "metric": "Number of Reactions (Re-runs only)", "metric_id": "rerun_reactions", "kind": "sum_int", "aliases": ["Number of Reactions (Re-runs only)"]},
        {"section": "Re-runs", "metric": "Re-run % of Tubes", "metric_id": "rerun_pct_of_tubes", "kind": "ratio", "numerator_id": "rerun_tubes", "denom_id": "tubes_tested_initial"},
        {"section": "Re-runs", "metric": "Number of Initial Runs with Re-runs", "metric_id": "initial_runs_with_reruns", "kind": "sum_int", "aliases": ["Number of Initial Runs with Re-runs"]},
        {"section": "Re-runs", "metric": "% Initial Runs with Re-runs", "metric_id": "pct_initial_runs_with_reruns", "kind": "ratio", "numerator_id": "initial_runs_with_reruns", "denom_id": "initial_runs"},
        {"section": "Positives", "metric": "Number of Tubes with Final Result Positive", "metric_id": "positive_tubes_final", "kind": "sum_int", "aliases": ["Number of Tubes with Final Result Positive"]},
        {"section": "Positives", "metric": "% of Tubes Positives", "metric_id": "pct_tubes_positive", "kind": "ratio", "numerator_id": "positive_tubes_final", "denom_id": "tubes_tested_initial"},
        {"section": "Positives", "metric": "Number of Cases with Final Result Positive (Include pools not deconv)", "metric_id": "positive_cases_final", "kind": "sum_int", "aliases": ["Number of Cases with Final Result Positive (Include pools not deconv)"]},
        {"section": "Inconclusives", "metric": "Number of Tubes with Final Result Inconclusive", "metric_id": "inconclusive_tubes_final", "kind": "sum_int", "aliases": ["Number of Tubes with Final Result Inconclusive"]},
        {"section": "Inconclusives", "metric": "Number of Tubes in RFR Audit Inconclusive not in APS", "metric_id": "inconclusive_not_in_aps", "kind": "sum_int", "aliases": ["Number of Tubes in RFR Audit Inconclusive not in APS"]},
        {"section": "Inconclusives", "metric": "Total Number of Inconclusive Tubes", "metric_id": "total_inconclusive_tubes", "kind": "derived_sum", "numerator_ids": ["inconclusive_tubes_final", "inconclusive_not_in_aps"]},
        {"section": "Inconclusives", "metric": "% of Tubes Inconclusive", "metric_id": "pct_tubes_inconclusive", "kind": "ratio", "numerator_id": "total_inconclusive_tubes", "denom_id": "tubes_tested_initial"},
        {"section": "Inconclusives", "metric": "Number of Inconclusive Tubes resolved Positive by Referral Tests", "metric_id": "inconclusive_resolved_pos", "kind": "sum_int", "aliases": ["Number of Inconclusive Tubes resolved Positive by Referral Tests"]},
        {"section": "Inconclusives", "metric": "% Inconclusives resolved Positive by Referral Tests", "metric_id": "pct_inconclusive_resolved_pos", "kind": "ratio", "numerator_id": "inconclusive_resolved_pos", "denom_id": "total_inconclusive_tubes"},
        {"section": "Inconclusives", "metric": "Number of Inconclusive Test Run Calls", "metric_id": "inconclusive_run_calls", "kind": "sum_int", "aliases": ["Number of Inconclusive Test Run Calls"]},
        {"section": "Inconclusives", "metric": "% Tube Tests Run Called Inconclusive", "metric_id": "pct_tube_tests_called_inconclusive", "kind": "ratio", "numerator_id": "inconclusive_run_calls", "denom_id": "tube_tests_run_total"},
        {"section": "Referrals and Correspondence", "metric": "Number of FloodLAMP Cases with Referral Tests or Correspondence", "metric_id": "cases_with_referral", "kind": "sum_int", "aliases": ["Number of FloodLAMP Cases with Referral Tests or Correspondence"]},
        {"section": "Referrals and Correspondence", "metric": "Agree Positives", "metric_id": "agree_positives", "kind": "sum_int", "aliases": ["Agree Positives"]},
        {"section": "Referrals and Correspondence", "metric": "FL Inconclusives with Referal / Correspondence Positive", "metric_id": "incl_ref_pos", "kind": "sum_int", "aliases": ["FL Inconclusives with Referal / Correspondence Positive"]},
        {"section": "Referrals and Correspondence", "metric": "% FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive", "metric_id": "pct_pos_or_incl_with_ref_pos", "kind": "ratio_sum_numerators", "numerator_ids": ["agree_positives", "incl_ref_pos"], "denom_id": "cases_with_referral"},
        {"section": "Dates", "metric": "Start Run Date", "metric_id": "start_run_date", "kind": "min_date", "aliases": ["Start Run Date"]},
        {"section": "Dates", "metric": "End Run Date", "metric_id": "end_run_date", "kind": "max_date", "aliases": ["End Run Date"]},
    ]

    computed = {}
    for m in METRICS:
        mid = m["metric_id"]
        kind = m["kind"]
        if kind == "sum_int":
            r = _aggregate_sum_int(site_metric_maps, m["aliases"])
            r["value_formula"] = "sum(site values)"
            computed[mid] = r
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

    for m in METRICS:
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
    for m in METRICS:
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
def aggregate_zipall_curated_csvs(pilot_data_csvs_zip_path, output_folder_path):
    """Aggregate a ZIPALL curated CSV zip into three cross-site aggregate CSVs.

    :param pilot_data_csvs_zip_path: str, path to ZIPALL_pilot-data_csvs.zip.
    :param output_folder_path: str, output folder for aggregate CSVs.
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

        for site_code, site_folder in sites:
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

        out_stats = os.path.join(output_folder_path, "aggregate__pilot-data_stats_key-values.csv")
        out_weekly = os.path.join(output_folder_path, "aggregate__pilot-data_weekly-summary.csv")
        out_referral = os.path.join(output_folder_path, "aggregate__pilot-data_stats_referral-agreement.csv")

        stats_result = _aggregate_stats_key_values(site_code_to_stats, out_stats)
        weekly_result = _aggregate_weekly_summary(site_code_to_weekly, out_weekly)
        referral_result = _aggregate_referral_agreement(site_code_to_referral, out_referral)

        return {
            "sites_discovered": [s[0] for s in sites],
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
if __name__ == "__main__":
    pilot_data_root = "data/floodlamp/pilots/pilot-data"
    # Run the zipping process and get the output paths
    zip_result = run_zip_pilot_data(pilot_data_root)
    # Get the path to the ZIPALL CSVs zip from the returned result
    pilot_data_csvs_zip_path = zip_result["combined_result"]["zipall_csvs"]
    # Create aggregate_csvs folder in the pilot-data root
    output_folder_path = os.path.join(pilot_data_root, "aggregate_csvs")
    aggregate_zipall_curated_csvs(pilot_data_csvs_zip_path, output_folder_path)