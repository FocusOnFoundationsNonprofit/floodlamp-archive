# ===== START OF FILE floodlamp_archive_md_to_embed.py =====
# Purpose: render the five FloodLAMP archive static-page HTML embeds from the canonical
# web-copy markdown file, update changed local embed files, prompt for manual Webflow
# paste/publish, and compare local embed content against the live public pages.

import csv
import os
import re
from datetime import datetime
from html import unescape
from urllib.parse import urljoin
import requests

DEFAULT_WEBCODE_FOLDER = "data/floodlamp/_exclude-from-archive/_code-floodlamp-archive/webcode"
DEFAULT_WEB_COPY_PATH = os.path.join(DEFAULT_WEBCODE_FOLDER, "floodlamp-archive-web-copy.md")
DEFAULT_GDRIVE_URLS_PATH = "data/floodlamp/_archive-gdrive-urls.md"
DEFAULT_GITHUB_REPO_URL = "https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive"
LIVE_PAGE_BASE_URL = "https://www.floodlamp.bio"
STAGING_PAGE_BASE_URL = "https://floodlamp.webflow.io"
DEFAULT_INTEGRATED_VIEW_PATH = "data/floodlamp/_archive-integrated-view.md"
DEFAULT_FILE_LIST_HEADINGS_PATH = "data/floodlamp/_archive-file-list-headings-only.md"
DEFAULT_UPDATE_RECORDS_FOLDER = "data/floodlamp/_exclude-from-archive/update-records"
DEFAULT_CHANGELOGS_REFRESH_FOLDER = "data/floodlamp/_exclude-from-archive/changelogs-refresh"
DEFAULT_ARCHIVE_ZIP_ROOT = "data/floodlamp"
DEFAULT_ARCHIVE_ZIP_PUBLIC_BUCKET = "fofpublic"
DEFAULT_ARCHIVE_ZIP_PUBLIC_PREFIX = "floodlamp-archive"
ARCHIVE_ZIP_DOWNLOAD_SPECS_BY_PAGE = {
    "home-archive": [
        ("Download the full archive zip", "_zip_floodlamp-archive-all.zip"),
    ],
    "cat-guides": [
        ("Download the Guides category zip", "guides/_zip_floodlamp-archive-guides.zip"),
    ],
    "cat-pilots": [
        ("Download the Pilots category zip", "pilots/_zip_floodlamp-archive-pilots.zip"),
    ],
    "cat-regulatory": [
        ("Download the Regulatory category zip", "regulatory/_zip_floodlamp-archive-regulatory.zip"),
    ],
    "cat-various": [
        ("Download the Various category zip", "various/_zip_floodlamp-archive-various.zip"),
    ],
}
ARCHIVE_ITEM_PAGE_PREFIX = "/archive"
PAGE_HEADING_PATTERN = re.compile(r"^# Page:\s+(.+?)\s*$")
KV_BULLET_PATTERN = re.compile(r"^- `([^`]+)`: (.+?)\s*$")
PAGE_SPECS = [
    {"slug": "home-archive", "page_name": "Home", "live_path": "/", "embed_file": "floodlamp_archive_home_archive_embed.html", "title_comment": "FloodLAMP archive homepage embed"},
    {"slug": "cat-guides", "page_name": "cat-guides", "live_path": "/cat-guides", "embed_file": "floodlamp_archive_cat_guides_embed.html", "title_comment": "FloodLAMP archive Guides page embed"},
    {"slug": "cat-pilots", "page_name": "cat-pilots", "live_path": "/cat-pilots", "embed_file": "floodlamp_archive_cat_pilots_embed.html", "title_comment": "FloodLAMP archive Pilots page embed"},
    {"slug": "cat-regulatory", "page_name": "cat-regulatory", "live_path": "/cat-regulatory", "embed_file": "floodlamp_archive_cat_regulatory_embed.html", "title_comment": "FloodLAMP archive Regulatory page embed"},
    {"slug": "cat-various", "page_name": "cat-various", "live_path": "/cat-various", "embed_file": "floodlamp_archive_cat_various_embed.html", "title_comment": "FloodLAMP archive Various page embed"},
]

### Helpers: filesystem and formatting
def _read_text(file_path):
    """
    Reads a UTF-8 text file.

    :param file_path: string, the path to the text file.
    :return text: string, the file contents.
    """
    with open(file_path, "r", encoding="utf-8") as file_handle:
        return file_handle.read()
def _write_text(file_path, text):
    """
    Writes a UTF-8 text file.

    :param file_path: string, the path to the text file.
    :param text: string, the file contents to write.
    :return file_path: string, the written file path.
    """
    with open(file_path, "w", encoding="utf-8") as file_handle:
        file_handle.write(text)
    return file_path
def _current_short_timestamp():
    """
    Builds the short FloodLAMP timestamp format.

    :return timestamp_text: string, the current timestamp in m-d hhmm format.
    """
    now = datetime.now()
    return f"{now.month}-{now.day} {now.strftime('%H%M')}"
def _format_file_size_compact(size_bytes):
    """
    Formats a byte count as a compact MB or GB label.

    :param size_bytes: int, the file size in bytes.
    :return size_label: string, the formatted size label.
    """
    if size_bytes >= 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
    return f"{round(size_bytes / (1024 * 1024))} MB"
def _archive_zip_public_url(file_name, bucket=DEFAULT_ARCHIVE_ZIP_PUBLIC_BUCKET, public_prefix=DEFAULT_ARCHIVE_ZIP_PUBLIC_PREFIX):
    """
    Builds the public S3 url for one FloodLAMP zip file.

    :param file_name: string, the zip file name in the public folder.
    :param bucket: string, the public S3 bucket name.
    :param public_prefix: string, the top-level public S3 folder.
    :return public_url: string, the public https url.
    """
    return f"https://{bucket}.s3.us-west-2.amazonaws.com/{public_prefix}/{file_name}"
def _archive_zip_download_records_by_page(root_folder=DEFAULT_ARCHIVE_ZIP_ROOT, bucket=DEFAULT_ARCHIVE_ZIP_PUBLIC_BUCKET, public_prefix=DEFAULT_ARCHIVE_ZIP_PUBLIC_PREFIX):
    """
    Builds zip-download link records for each page that surfaces zip downloads.

    :param root_folder: string, the local FloodLAMP root folder.
    :param bucket: string, the public S3 bucket name.
    :param public_prefix: string, the top-level public S3 folder.
    :return records_by_page: dict, zip-download link records keyed by page slug.
    """
    records_by_page = {}
    for page_slug, link_specs in ARCHIVE_ZIP_DOWNLOAD_SPECS_BY_PAGE.items():
        page_records = []
        for label, rel_path in link_specs:
            file_path = os.path.join(root_folder, rel_path)
            if not os.path.isfile(file_path):
                continue
            file_name = os.path.basename(rel_path)
            size_label = _format_file_size_compact(os.path.getsize(file_path))
            page_records.append({
                "label": f"{label} ({size_label})",
                "url": _archive_zip_public_url(file_name, bucket=bucket, public_prefix=public_prefix),
            })
        records_by_page[page_slug] = page_records
    return records_by_page
def _zip_download_records_for_page(page_slug, root_folder=DEFAULT_ARCHIVE_ZIP_ROOT, bucket=DEFAULT_ARCHIVE_ZIP_PUBLIC_BUCKET, public_prefix=DEFAULT_ARCHIVE_ZIP_PUBLIC_PREFIX):
    """
    Gets the zip-download link records for a single page.

    :param page_slug: string, the page slug whose zip downloads should be rendered.
    :param root_folder: string, the local FloodLAMP root folder.
    :param bucket: string, the public S3 bucket name.
    :param public_prefix: string, the top-level public S3 folder.
    :return records: list, zip-download link records for the page.
    """
    return _archive_zip_download_records_by_page(root_folder=root_folder, bucket=bucket, public_prefix=public_prefix).get(page_slug, [])
def _escape_html(text):
    """
    Escapes minimal HTML special characters.

    :param text: string, the text to escape.
    :return escaped_text: string, the escaped text.
    """
    escaped_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    escaped_text = escaped_text.replace('"', "&quot;")
    return escaped_text
def _slugify_label(text):
    """
    Converts a heading label into a stable key.

    :param text: string, the source heading label.
    :return slug_text: string, the normalized key.
    """
    slug_text = text.strip().lower()
    slug_text = slug_text.replace("&", " and ")
    slug_text = re.sub(r"[^a-z0-9]+", "_", slug_text)
    return slug_text.strip("_")
def _parse_kv_line(line_text):
    """
    Parses one markdown key-value bullet line.

    :param line_text: string, the markdown line to parse.
    :return result: tuple, the parsed key and normalized value or empty strings.
    """
    kv_match = KV_BULLET_PATTERN.match(line_text.strip())
    if not kv_match:
        return "", ""
    key = kv_match.group(1)
    value = kv_match.group(2).strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    value = value.replace("`, `", ", ").replace("`", "")
    return key, value
def _normalize_html_for_compare(html_text):
    """
    Normalizes generated HTML for equality comparison.

    :param html_text: string, the html text to normalize.
    :return normalized_html: string, the normalized html text.
    """
    normalized_html = re.sub(r"<!-- last updated:.*?-->\s*", "", html_text)
    normalized_html = normalized_html.replace("\r\n", "\n").strip()
    normalized_html = re.sub(r">\s+<", "><", normalized_html)
    normalized_html = re.sub(r"\s+", " ", normalized_html)
    return normalized_html.strip()
def _normalize_text_for_compare(text):
    """
    Normalizes visible text for comparison.

    :param text: string, the visible text to normalize.
    :return normalized_text: string, the normalized text.
    """
    normalized_text = unescape(text)
    normalized_text = normalized_text.replace("\u00a0", " ")
    normalized_text = re.sub(r"\s+", " ", normalized_text)
    return normalized_text.strip().lower()
def _html_to_visible_text(html_text):
    """
    Converts html into normalized visible text.

    :param html_text: string, the html text to simplify.
    :return visible_text: string, the extracted visible text.
    """
    visible_text = re.sub(r"<!--.*?-->", " ", html_text, flags=re.S)
    visible_text = re.sub(r"<script.*?>.*?</script>", " ", visible_text, flags=re.S | re.I)
    visible_text = re.sub(r"<style.*?>.*?</style>", " ", visible_text, flags=re.S | re.I)
    visible_text = re.sub(r"<[^>]+>", " ", visible_text)
    return _normalize_text_for_compare(visible_text)
def _extract_hrefs(html_text, base_url):
    """
    Extracts normalized href targets from html.

    :param html_text: string, the html text to inspect.
    :param base_url: string, the base url used to resolve relative links.
    :return hrefs: list, the normalized href targets.
    """
    hrefs = []
    for href_value in re.findall(r'href="([^"]+)"', html_text):
        hrefs.append(urljoin(base_url, href_value))
    return sorted(set(hrefs))
def _print_status_line(is_ok, label, detail=""):
    """
    Prints a one-line sync status message.

    :param is_ok: boolean, whether the status should be shown as success.
    :param label: string, the report label.
    :param detail: string, optional trailing detail text.
    :return status_text: string, the printed status text.
    """
    icon = "✅" if is_ok else "❌"
    status_text = f"{icon} {label}"
    if detail:
        status_text += f" - {detail}"
    print(status_text)
    return status_text
def _page_spec_to_live_url(page_spec, base_url=LIVE_PAGE_BASE_URL):
    """
    Builds the live page URL for a FloodLAMP static page.

    :param page_spec: dict, the page spec including its live path.
    :param base_url: string, the base url to build from.
    :return live_url: string, the live page URL.
    """
    live_path = page_spec.get("live_path", "").strip() or f"/{page_spec.get('slug', '').strip()}"
    if live_path == "/":
        return base_url
    return f"{base_url}{live_path}"
def _get_page_spec_map():
    """
    Builds a slug-keyed page spec map.

    :return spec_map: dict, the page specs keyed by slug.
    """
    return {page_spec["slug"]: dict(page_spec) for page_spec in PAGE_SPECS}
def _build_embed_header(page_spec, timestamp_text):
    """
    Builds the standard comment header for an embed file.

    :param page_spec: dict, the page spec for the embed file.
    :param timestamp_text: string, the current short timestamp.
    :return header_text: string, the comment header block.
    """
    header_lines = [
        f"<!-- {page_spec['title_comment']} -->",
        f"<!-- Paste into the single HTML Embed on the `{page_spec['page_name']}` page. -->",
        f"<!-- last updated: {timestamp_text} -->",
    ]
    return "\n".join(header_lines) + "\n"
def _github_commentary_url(commentary_path):
    """
    Builds the public GitHub blob URL for a commentary file.

    :param commentary_path: string, the archive-relative commentary path.
    :return url: string, the GitHub blob URL.
    """
    relative_path = commentary_path.replace("data/floodlamp/", "")
    return f"{DEFAULT_GITHUB_REPO_URL}/blob/main/{relative_path}"
def _github_blob_to_raw_url(github_url):
    """
    Converts a GitHub blob markdown URL to the raw download URL.

    :param github_url: string, the GitHub blob URL.
    :return raw_url: string, the raw GitHub download URL.
    """
    github_url = github_url.strip()
    github_match = re.match(r"^https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)$", github_url)
    if not github_match:
        return github_url
    owner = github_match.group(1)
    repo = github_match.group(2)
    branch = github_match.group(3)
    repo_path = github_match.group(4)
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{repo_path}"
def _latest_cms_expected_full_status_path(update_records_folder=DEFAULT_UPDATE_RECORDS_FOLDER, changelogs_refresh_folder=DEFAULT_CHANGELOGS_REFRESH_FOLDER):
    """
    Finds the newest CMS expected-full CSV across both update-records and changelogs-refresh folders.

    :param update_records_folder: string, the root folder containing update_* subfolders.
    :param changelogs_refresh_folder: string, the root folder containing *_refresh subfolders.
    :return csv_path: string, the latest CMS expected-full CSV path or an empty string.
    """
    candidates = []
    if os.path.isdir(update_records_folder):
        for folder_name in os.listdir(update_records_folder):
            if re.match(r"^update_\d{4}-\d{2}-\d{2}_\d{4}$", folder_name):
                csv_path = os.path.join(update_records_folder, folder_name, "cms_expected_full_status.csv")
                if os.path.isfile(csv_path):
                    date_key = folder_name.replace("update_", "")
                    candidates.append((date_key, csv_path))
    if os.path.isdir(changelogs_refresh_folder):
        for folder_name in os.listdir(changelogs_refresh_folder):
            if re.match(r"^\d{4}-\d{2}-\d{2}_\d{4}_refresh$", folder_name):
                csv_path = os.path.join(changelogs_refresh_folder, folder_name, "cms_expected_full.csv")
                if os.path.isfile(csv_path):
                    date_key = folder_name.replace("_refresh", "")
                    candidates.append((date_key, csv_path))
    if not candidates:
        return ""
    candidates.sort(key=lambda pair: pair[0], reverse=True)
    return candidates[0][1]
def _parse_archive_integrated_view_counts(integrated_view_path=DEFAULT_INTEGRATED_VIEW_PATH):
    """
    Parses per-subcategory combined-file counts from the archive integrated view.

    :param integrated_view_path: string, the path to the integrated-view markdown file.
    :return counts_map: dict, combined-file counts keyed by category then subcategory.
    """
    counts_map = {}
    if not os.path.isfile(integrated_view_path):
        return counts_map
    cur_category = ""
    for raw_line in _read_text(integrated_view_path).splitlines():
        stripped_line = raw_line.strip()
        category_match = re.match(r"^##\s+(?:✅\s+)?([a-z0-9-]+)\s*$", stripped_line)
        if category_match:
            cur_category = category_match.group(1)
            counts_map.setdefault(cur_category, {})
            continue
        subcategory_match = re.match(r"^###\s+(?:✅\s+)?([a-z0-9-]+)\s+(\d+)\s+combined\b", stripped_line)
        if cur_category and subcategory_match:
            counts_map.setdefault(cur_category, {})
            counts_map[cur_category][subcategory_match.group(1)] = int(subcategory_match.group(2))
    return counts_map
def _parse_archive_headings_counts(headings_path=DEFAULT_FILE_LIST_HEADINGS_PATH):
    """
    Parses per-subcategory file counts from the archive-file-list-headings-only file.

    :param headings_path: string, the path to the headings-only markdown file.
    :return counts_map: dict, file counts keyed by category then subcategory.
    """
    counts_map = {}
    if not os.path.isfile(headings_path):
        return counts_map
    cur_category = ""
    for raw_line in _read_text(headings_path).splitlines():
        stripped_line = raw_line.strip()
        category_match = re.match(r"^##\s+([a-z0-9-]+)\s", stripped_line)
        if category_match:
            cur_category = category_match.group(1)
            counts_map.setdefault(cur_category, {})
            continue
        subcategory_match = re.match(r"^###\s+([a-z0-9-]+)\s+\((\d+)\s+files\b", stripped_line)
        if cur_category and subcategory_match:
            counts_map.setdefault(cur_category, {})
            counts_map[cur_category][subcategory_match.group(1)] = int(subcategory_match.group(2))
    return counts_map
def _load_cms_status_index(cms_status_csv_path):
    """
    Loads combined-download links and CMS item links from a CMS status CSV.

    :param cms_status_csv_path: string, the cms_expected_full_status.csv path.
    :return cms_index: dict, download and file-link data keyed by category/subcategory.
    """
    cms_index = {
        "category_combined_downloads": {},
        "subcategory_combined_downloads": {},
        "subcategory_file_links": {},
    }
    if not cms_status_csv_path or not os.path.isfile(cms_status_csv_path):
        return cms_index
    with open(cms_status_csv_path, "r", encoding="utf-8", newline="") as file_handle:
        csv_reader = csv.DictReader(file_handle)
        for row in csv_reader:
            category = (row.get("category") or "").strip()
            subcategory = (row.get("subcategory") or "").strip()
            archive_item_type = (row.get("archive-item-type") or "").strip()
            archive_scope = (row.get("archive-scope") or "").strip()
            source_file_name = (row.get("source-file-name") or "").strip()
            title = (row.get("title") or "").strip()
            slug = (row.get("slug") or "").strip()
            raw_markdown_url = (row.get("github-markdown-download-url") or "").strip()
            github_markdown_url = (row.get("github-markdown-url") or "").strip()
            raw_markdown_url = raw_markdown_url or _github_blob_to_raw_url(github_markdown_url)
            if archive_item_type == "combined_files" and raw_markdown_url:
                download_record = {"url": raw_markdown_url, "file_name": source_file_name or "combined.md"}
                if archive_scope == "category" and category:
                    cms_index["category_combined_downloads"][category] = download_record
                elif archive_scope == "subcategory" and category and subcategory:
                    cms_index["subcategory_combined_downloads"][f"{category}/{subcategory}"] = download_record
            if archive_scope != "file" or not category or not subcategory or not slug:
                continue
            file_label = source_file_name or title or slug
            cms_index["subcategory_file_links"].setdefault(f"{category}/{subcategory}", [])
            cms_index["subcategory_file_links"][f"{category}/{subcategory}"].append({
                "label": file_label,
                "href": f"{ARCHIVE_ITEM_PAGE_PREFIX}/{slug}",
            })
    for key in cms_index["subcategory_file_links"]:
        deduped_links = {}
        for link_record in cms_index["subcategory_file_links"][key]:
            deduped_links[link_record["href"]] = link_record
        cms_index["subcategory_file_links"][key] = sorted(deduped_links.values(), key=lambda link_record: link_record["label"].lower())
    return cms_index
def _build_archive_support_data(integrated_view_path=DEFAULT_INTEGRATED_VIEW_PATH, update_records_folder=DEFAULT_UPDATE_RECORDS_FOLDER, headings_path=DEFAULT_FILE_LIST_HEADINGS_PATH):
    """
    Builds source data needed for category-page counts, downloads, and CMS file links.

    :param integrated_view_path: string, the path to the integrated-view markdown file.
    :param update_records_folder: string, the root folder containing update_* subfolders.
    :param headings_path: string, the path to the headings-only markdown file for fallback counts.
    :return support_data: dict, parsed counts and cms-link data used during rendering.
    """
    cms_status_csv_path = _latest_cms_expected_full_status_path(update_records_folder=update_records_folder)
    subcategory_counts = _parse_archive_integrated_view_counts(integrated_view_path=integrated_view_path)
    headings_counts = _parse_archive_headings_counts(headings_path=headings_path)
    for category_key, subcategory_map in headings_counts.items():
        subcategory_counts.setdefault(category_key, {})
        for subcategory_key, count_value in subcategory_map.items():
            if subcategory_key not in subcategory_counts[category_key]:
                subcategory_counts[category_key][subcategory_key] = count_value
    return {
        "subcategory_counts": subcategory_counts,
        "cms_index": _load_cms_status_index(cms_status_csv_path),
    }
def _category_key_from_page_record(metadata_fields):
    """
    Derives the category key for a category page from page metadata.

    :param metadata_fields: dict, the parsed page metadata fields.
    :return category_key: string, the normalized category key.
    """
    webflow_slug = metadata_fields.get("webflow_slug", "").strip()
    if webflow_slug.startswith("cat-"):
        return webflow_slug[4:]
    nav_label = metadata_fields.get("nav_label", "").strip()
    return _slugify_label(nav_label)
def _subcategory_count_label(category_key, subcategory_key, fallback_label, support_data):
    """
    Builds a subcategory label optionally suffixed with the integrated-view file count.

    :param category_key: string, the category key.
    :param subcategory_key: string, the subcategory key/anchor.
    :param fallback_label: string, the base subcategory label.
    :param support_data: dict, the parsed render support data.
    :return display_label: string, the display label with count when available.
    """
    count_value = support_data.get("subcategory_counts", {}).get(category_key, {}).get(subcategory_key)
    if count_value is None:
        return fallback_label
    return f"{fallback_label} ({count_value} files)"
def _download_link_html(indent, label, download_record):
    """
    Renders one download link wired for client-side markdown download.

    :param indent: string, the indentation prefix for generated html.
    :param label: string, the visible link label.
    :param download_record: dict, the url and filename for the download.
    :return link_html: string, the rendered download link html.
    """
    if not download_record or not download_record.get("url"):
        return ""
    download_url = download_record.get("url", "")
    download_file_name = download_record.get("file_name", "download.md")
    return f'{indent}<a class="fl-archive-page-link" href="{_escape_html(download_url)}" data-download-url="{_escape_html(download_url)}" data-download-filename="{_escape_html(download_file_name)}">{_escape_html(label)}</a>'
def _external_link_html(indent, label, href):
    """
    Renders one normal external page link.

    :param indent: string, the indentation prefix for generated html.
    :param label: string, the visible link label.
    :param href: string, the external href target.
    :return link_html: string, the rendered external link html.
    """
    if not href:
        return ""
    return f'{indent}<a class="fl-archive-page-link" href="{_escape_html(href)}" target="_blank" rel="noopener noreferrer">{_escape_html(label)}</a>'
def _category_support_assets_html(indent):
    """
    Renders category-page inline style and script helpers.

    :param indent: string, the indentation prefix for generated html.
    :return assets_html: string, the rendered helper assets block.
    """
    asset_lines = [
        f"{indent}<script>",
        f"{indent}(function () {{",
        f"{indent}  function cleanValue(value) {{",
        f"{indent}    return String(value || '').trim();",
        f"{indent}  }}",
        f"{indent}  function attachDownloadHandlers(root) {{",
        f"{indent}    var downloadLinks = root.querySelectorAll('[data-download-url]');",
        f"{indent}    downloadLinks.forEach(function (link) {{",
        f"{indent}      if (link.dataset.downloadBound === 'true') {{",
        f"{indent}        return;",
        f"{indent}      }}",
        f"{indent}      link.dataset.downloadBound = 'true';",
        f"{indent}      link.addEventListener('click', async function (event) {{",
        f"{indent}        event.preventDefault();",
        f"{indent}        var downloadUrl = cleanValue(link.getAttribute('data-download-url'));",
        f"{indent}        var downloadFilename = cleanValue(link.getAttribute('data-download-filename')) || 'download.md';",
        f"{indent}        if (!downloadUrl) {{",
        f"{indent}          return;",
        f"{indent}        }}",
        f"{indent}        try {{",
        f"{indent}          var response = await fetch(downloadUrl);",
        f"{indent}          if (!response.ok) {{",
        f"{indent}            throw new Error('Download failed with status ' + response.status);",
        f"{indent}          }}",
        f"{indent}          var blob = await response.blob();",
        f"{indent}          var objectUrl = window.URL.createObjectURL(blob);",
        f"{indent}          var temporaryLink = document.createElement('a');",
        f"{indent}          temporaryLink.href = objectUrl;",
        f"{indent}          temporaryLink.download = downloadFilename;",
        f"{indent}          document.body.appendChild(temporaryLink);",
        f"{indent}          temporaryLink.click();",
        f"{indent}          temporaryLink.remove();",
        f"{indent}          window.URL.revokeObjectURL(objectUrl);",
        f"{indent}        }} catch (error) {{",
        f"{indent}          console.error('FloodLAMP category markdown download failed:', error);",
        f"{indent}          window.open(downloadUrl, '_blank', 'noopener,noreferrer');",
        f"{indent}        }}",
        f"{indent}      }});",
        f"{indent}    }});",
        f"{indent}  }}",
        f"{indent}  var root = document.currentScript && document.currentScript.parentElement ? document.currentScript.parentElement : document;",
        f"{indent}  attachDownloadHandlers(root);",
        f"{indent}}})();",
        f"{indent}</script>",
    ]
    return "\n".join(asset_lines)

### Helpers: Google Drive URLs
def _parse_gdrive_urls(gdrive_urls_path=DEFAULT_GDRIVE_URLS_PATH):
    """
    Parses the Google Drive URLs markdown file into a lookup structure.

    :param gdrive_urls_path: string, the path to the _archive-gdrive-urls.md file.
    :return gdrive_urls: dict, root url and category urls keyed by slug.
    """
    gdrive_urls = {"root": "", "categories": {}}
    if not os.path.isfile(gdrive_urls_path):
        return gdrive_urls
    cur_heading = ""
    heading_level = 0
    for raw_line in _read_text(gdrive_urls_path).splitlines():
        stripped_line = raw_line.strip()
        if stripped_line.startswith("## ") and not stripped_line.startswith("### "):
            cur_heading = stripped_line[3:].strip()
            heading_level = 2
            continue
        if stripped_line.startswith("### "):
            heading_level = 3
            continue
        if stripped_line.startswith("http") and heading_level == 2 and cur_heading:
            if cur_heading == "root":
                gdrive_urls["root"] = stripped_line
            else:
                gdrive_urls["categories"][cur_heading] = stripped_line
            heading_level = 0
    return gdrive_urls
def _category_combined_file_download(category_key, archive_root=DEFAULT_ARCHIVE_ZIP_ROOT, github_repo_url=DEFAULT_GITHUB_REPO_URL):
    """
    Finds the current combined-files markdown on disk and builds a download record.

    :param category_key: string, the category slug.
    :param archive_root: string, the local archive root folder.
    :param github_repo_url: string, the base github repository url.
    :return download_record: dict, url and file_name for the combined file or empty dict.
    """
    import glob
    pattern = os.path.join(archive_root, category_key, f"_archive-combined-files_{category_key}_*.md")
    matches = glob.glob(pattern)
    if not matches:
        return {}
    matches.sort(key=os.path.getmtime, reverse=True)
    file_path = matches[0]
    file_name = os.path.basename(file_path)
    relative_path = f"{category_key}/{file_name}"
    raw_url = f"https://raw.githubusercontent.com/{github_repo_url.rstrip('/').split('github.com/')[-1]}/main/{relative_path}"
    return {"url": raw_url, "file_name": file_name}

### Helpers: markdown parsing
def _parse_overview(lines):
    """
    Parses the overview key-value bullets at the top of the markdown file.

    :param lines: list, the markdown lines to parse.
    :return overview: dict, the parsed overview values.
    """
    overview = {}
    cur_section = ""
    for raw_line in lines:
        stripped_line = raw_line.strip()
        if stripped_line.startswith("# "):
            cur_section = stripped_line[2:].strip()
            continue
        if cur_section != "Overview":
            continue
        key, value = _parse_kv_line(stripped_line)
        if key:
            overview[key] = value
    return overview
def _parse_subsection_body(lines, start_index):
    """
    Parses the markdown body directly under a subsection heading.

    :param lines: list, the markdown lines to parse.
    :param start_index: int, the line index after the subsection heading.
    :return result: tuple, the parsed fields, body markdown, and next index.
    """
    fields = {}
    body_lines = []
    cur_index = start_index
    while cur_index < len(lines):
        stripped_line = lines[cur_index].strip()
        if stripped_line.startswith("#"):
            break
        key, value = _parse_kv_line(stripped_line)
        if key and not body_lines:
            fields[key] = value
            cur_index += 1
            continue
        body_lines.append(lines[cur_index].rstrip())
        cur_index += 1
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    return fields, "\n".join(body_lines).strip(), cur_index
def parse_floodlamp_web_copy(web_copy_path=DEFAULT_WEB_COPY_PATH):
    """
    Parses the FloodLAMP web-copy markdown into a page data structure.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :return parsed_data: dict, the parsed overview and page records.
    """
    markdown_text = _read_text(web_copy_path)
    lines = markdown_text.splitlines()
    parsed_data = {
        "web_copy_path": web_copy_path,
        "overview": _parse_overview(lines),
        "pages": {},
    }
    cur_page_slug = ""
    cur_section_key = ""
    cur_index = 0
    while cur_index < len(lines):
        stripped_line = lines[cur_index].strip()
        page_match = PAGE_HEADING_PATTERN.match(stripped_line)
        if page_match:
            cur_page_slug = page_match.group(1).strip()
            parsed_data["pages"][cur_page_slug] = {"sections": {}}
            cur_section_key = ""
            cur_index += 1
            continue
        if cur_page_slug and stripped_line.startswith("## "):
            cur_section_key = _slugify_label(stripped_line[3:].strip())
            parsed_data["pages"][cur_page_slug]["sections"][cur_section_key] = []
            cur_index += 1
            continue
        if cur_page_slug and cur_section_key and stripped_line.startswith("### "):
            subsection_label = stripped_line[4:].strip()
            fields, body_markdown, next_index = _parse_subsection_body(lines, cur_index + 1)
            parsed_data["pages"][cur_page_slug]["sections"][cur_section_key].append({
                "label": subsection_label,
                "key": _slugify_label(subsection_label),
                "fields": fields,
                "body_markdown": body_markdown,
            })
            cur_index = next_index
            continue
        if cur_page_slug and cur_section_key:
            key, value = _parse_kv_line(stripped_line)
            if key and not parsed_data["pages"][cur_page_slug]["sections"][cur_section_key]:
                fields, body_markdown, next_index = _parse_subsection_body(lines, cur_index)
                parsed_data["pages"][cur_page_slug]["sections"][cur_section_key].append({
                    "label": cur_section_key.replace("_", " "),
                    "key": cur_section_key,
                    "fields": fields,
                    "body_markdown": body_markdown,
                })
                cur_index = next_index
                continue
        cur_index += 1
    return parsed_data
def _page_section_map(page_record, section_key):
    """
    Builds a subsection-key map for a page section.

    :param page_record: dict, the parsed page record.
    :param section_key: string, the normalized section key.
    :return section_map: dict, the subsections keyed by normalized key.
    """
    section_map = {}
    for subsection in page_record["sections"].get(section_key, []):
        section_map[subsection["key"]] = subsection
    return section_map
def _subcategories_by_anchor(page_record):
    """
    Builds a subcategory map keyed by anchor.

    :param page_record: dict, the parsed page record.
    :return section_map: dict, the subcategories keyed by anchor.
    """
    section_map = {}
    for subsection in page_record["sections"].get("subcategories", []):
        anchor = subsection["fields"].get("anchor", "")
        if anchor:
            section_map[anchor] = subsection
    return section_map

### Helpers: markdown body rendering
def _markdown_body_to_blocks(body_markdown):
    """
    Splits simple markdown body text into paragraph and list blocks.

    :param body_markdown: string, the subsection body markdown.
    :return blocks: list, the parsed paragraph/list blocks.
    """
    if not body_markdown.strip():
        return []
    blocks = []
    cur_lines = []
    cur_type = ""
    for raw_line in body_markdown.splitlines():
        stripped_line = raw_line.strip()
        if not stripped_line:
            if cur_lines:
                blocks.append({"type": cur_type, "lines": list(cur_lines)})
                cur_lines = []
                cur_type = ""
            continue
        if stripped_line.startswith("- "):
            if cur_type not in ["", "list"]:
                blocks.append({"type": cur_type, "lines": list(cur_lines)})
                cur_lines = []
            cur_type = "list"
            cur_lines.append(stripped_line[2:].strip())
        else:
            if cur_type not in ["", "paragraph"]:
                blocks.append({"type": cur_type, "lines": list(cur_lines)})
                cur_lines = []
            cur_type = "paragraph"
            cur_lines.append(stripped_line)
    if cur_lines:
        blocks.append({"type": cur_type, "lines": list(cur_lines)})
    return blocks
def _render_markdown_blocks(body_markdown, indent, paragraph_class, list_class):
    """
    Renders simple markdown blocks to html.

    :param body_markdown: string, the subsection body markdown.
    :param indent: string, the indentation prefix for generated html.
    :param paragraph_class: string, the css class for paragraph blocks.
    :param list_class: string, the css class for list blocks.
    :return rendered_html: string, the rendered html text.
    """
    rendered_lines = []
    for block in _markdown_body_to_blocks(body_markdown):
        if block["type"] == "paragraph":
            paragraph_text = " ".join(block["lines"])
            rendered_lines.append(f'{indent}<p class="{paragraph_class}">{_escape_html(paragraph_text)}</p>')
        elif block["type"] == "list":
            rendered_lines.append(f'{indent}<ul class="{list_class}">')
            for list_item in block["lines"]:
                rendered_lines.append(f'{indent}  <li>{_escape_html(list_item)}</li>')
            rendered_lines.append(f'{indent}</ul>')
    return "\n".join(rendered_lines)

### Helpers: page rendering
def _render_home_embed(page_record, all_pages, overview, gdrive_urls=None, support_data=None):
    """
    Renders the home-archive embed html body.

    :param page_record: dict, the parsed home page record.
    :param all_pages: dict, all parsed page records keyed by slug.
    :param overview: dict, parsed overview-level shared values.
    :param gdrive_urls: dict, parsed google drive urls or none.
    :param support_data: dict, parsed render support data or none.
    :return embed_html: string, the rendered embed html body.
    """
    if gdrive_urls is None:
        gdrive_urls = {"root": "", "categories": {}}
    if support_data is None:
        support_data = {}
    metadata = _page_section_map(page_record, "page_metadata").get("page_metadata", {"fields": {}})
    content_blocks = _page_section_map(page_record, "content_blocks")
    archive_index_map = _page_section_map(page_record, "archive_index_map")
    download_cards = page_record["sections"].get("download_cards", [])
    parts = []
    parts.append('<div class="fl-archive-page">')
    parts.append('  <section class="fl-archive-page-hero">')
    parts.append(f'    <h1 class="fl-archive-page-title">{_escape_html(metadata["fields"].get("hero_title", ""))}</h1>')
    hero_block = content_blocks.get("hero_page_intro", {})
    hero_html = _render_markdown_blocks(hero_block.get("body_markdown", ""), "    ", "fl-archive-paragraph fl-archive-page-lead", "fl-archive-page-list")
    if hero_html:
        parts.append(hero_html)
    callout_text = hero_block.get("fields", {}).get("callout_text", "")
    home_zip_downloads = _zip_download_records_for_page("home-archive")
    if callout_text or home_zip_downloads:
        parts.append('    <div class="fl-archive-page-callout">')
        if callout_text:
            parts.append(f'      <p class="fl-archive-paragraph fl-archive-page-body">{_escape_html(callout_text)}</p>')
        if home_zip_downloads or gdrive_urls.get("root"):
            parts.append('      <div class="fl-archive-page-links">')
            system_prompt_block = content_blocks.get("system_prompt", {})
            system_prompt_href = system_prompt_block.get("fields", {}).get("link_href", "")
            system_prompt_label = system_prompt_block.get("fields", {}).get("link_label", "Use the full archive system prompt")
            if system_prompt_href:
                parts.append(_external_link_html("        ", system_prompt_label, system_prompt_href))
            for download_record in home_zip_downloads:
                parts.append(f'        <a class="fl-archive-page-link" href="{_escape_html(download_record["url"])}" target="_blank" rel="noopener noreferrer">{_escape_html(download_record["label"])}</a>')
            parts.append(_external_link_html("        ", "Clone the archive GitHub", DEFAULT_GITHUB_REPO_URL))
            if gdrive_urls.get("root"):
                parts.append(_external_link_html("        ", "Go to the archive Google Drive folder", gdrive_urls["root"]))
            parts.append('      </div>')
        parts.append('    </div>')
    parts.append('  </section>')
    parts.append('')
    manuscript_block = content_blocks.get("manuscript", {})
    manuscript_title = manuscript_block.get("fields", {}).get("manuscript_title", "")
    manuscript_archive_path = manuscript_block.get("fields", {}).get("archive_path", "")
    if manuscript_title and manuscript_archive_path:
        parts.append('  <div class="fl-archive-page-callout">')
        parts.append('    <h3 class="fl-archive-page-minor-title">The FloodLAMP Manuscript</h3>')
        parts.append(f'    <p class="fl-archive-paragraph fl-archive-page-body">&quot;{_escape_html(manuscript_title)}&quot;</p>')
        manuscript_body_html = _render_markdown_blocks(manuscript_block.get("body_markdown", ""), "    ", "fl-archive-paragraph fl-archive-page-body", "fl-archive-page-list")
        if manuscript_body_html:
            parts.append(manuscript_body_html)
        parts.append('    <div class="fl-archive-page-links">')
        parts.append(_external_link_html("      ", "Open markdown on GitHub", f"{DEFAULT_GITHUB_REPO_URL}/blob/main/{manuscript_archive_path}.md"))
        parts.append(_external_link_html("      ", "Open PDF on GitHub", f"{DEFAULT_GITHUB_REPO_URL}/blob/main/{manuscript_archive_path}.pdf"))
        parts.append(_external_link_html("      ", "Download Word document from GitHub", f"{DEFAULT_GITHUB_REPO_URL}/raw/main/{manuscript_archive_path}.docx"))
        parts.append('    </div>')
        parts.append('  </div>')
    parts.append('')
    parts.append('  <div class="fl-archive-page-rule"></div>')
    parts.append('')
    for block_key in ["what_floodlamp_is", "what_this_archive_is", "how_to_use_this_archive_with_ai"]:
        block = content_blocks.get(block_key, {})
        if not block:
            continue
        anchor = block.get("fields", {}).get("anchor", "")
        parts.append(f'  <section id="{_escape_html(anchor)}" class="fl-archive-page-section">')
        parts.append(f'    <h2 class="fl-archive-page-subtitle">{_escape_html(block["label"])}</h2>')
        block_html = _render_markdown_blocks(block.get("body_markdown", ""), "    ", "fl-archive-paragraph fl-archive-page-body", "fl-archive-page-list")
        if block_html:
            parts.append(block_html)
        parts.append('  </section>')
        parts.append('')
    archive_index_block = content_blocks.get("archive_index", {})
    parts.append(f'  <section id="{_escape_html(archive_index_block.get("fields", {}).get("anchor", ""))}" class="fl-archive-page-section">')
    parts.append(f'    <h2 class="fl-archive-page-subtitle">{_escape_html(archive_index_block.get("label", ""))}</h2>')
    archive_index_html = _render_markdown_blocks(archive_index_block.get("body_markdown", ""), "    ", "fl-archive-paragraph fl-archive-page-body", "fl-archive-page-list")
    if archive_index_html:
        parts.append(archive_index_html)
    parts.append('    <div class="fl-archive-page-grid">')
    for category_key in ["guides", "pilots", "regulatory", "various"]:
        category_entry = archive_index_map.get(category_key, {})
        category_label = category_entry.get("fields", {}).get("category_label", category_entry.get("label", ""))
        category_page = category_entry.get("fields", {}).get("category_page", "")
        category_page_slug = category_entry.get("fields", {}).get("category_page", "").replace("/", "").strip()
        category_zip_downloads = _zip_download_records_for_page(category_page_slug)
        category_zip_download = category_zip_downloads[0] if category_zip_downloads else {}
        subcategory_links = [link_text.strip() for link_text in category_entry.get("fields", {}).get("subcategory_links", "").split(",") if link_text.strip()]
        target_page_record = all_pages.get(category_page_slug, {})
        target_subcategories = _subcategories_by_anchor(target_page_record)
        parts.append('      <article class="fl-archive-page-card">')
        parts.append('        <h3 class="fl-archive-page-minor-title">')
        parts.append(f'          <a class="fl-archive-page-index-category-link" href="{_escape_html(category_page)}">{_escape_html(category_label)}:</a>')
        parts.append('        </h3>')
        home_zip_label = category_zip_download.get("label", "").replace(f"the {category_label} category", "the category")
        category_zip_html = _external_link_html("        ", home_zip_label, category_zip_download.get("url", ""))
        if category_zip_html:
            parts.append(category_zip_html)
        category_combined_download = _category_combined_file_download(category_key)
        if not category_combined_download:
            category_combined_download = support_data.get("cms_index", {}).get("category_combined_downloads", {}).get(category_key, {})
        combined_token_match = re.search(r"_(\d+k)\.md$", category_combined_download.get("file_name", ""))
        combined_label = "Download the combined markdown file"
        if combined_token_match:
            combined_label += f" ({combined_token_match.group(1)} tokens)"
        category_combined_html = _download_link_html("        ", combined_label, category_combined_download)
        if category_combined_html:
            parts.append(category_combined_html)
        category_gdrive_url = gdrive_urls.get("categories", {}).get(category_key, "")
        if category_gdrive_url:
            parts.append(_external_link_html("        ", "Go to the Google Drive folder", category_gdrive_url))
        parts.append('        <p class="fl-archive-paragraph fl-archive-page-body" style="margin-bottom:0.25em;"><strong>Subcategories:</strong></p>')
        parts.append('        <div class="fl-archive-page-index-list">')
        for subcategory_link in subcategory_links:
            anchor = subcategory_link.split("#")[-1]
            label = target_subcategories.get(anchor, {}).get("fields", {}).get("label", "")
            parts.append(f'          <a class="fl-archive-page-toc-link" href="{_escape_html(subcategory_link)}">{_escape_html(label)}</a>')
        parts.append('        </div>')
        parts.append('      </article>')
    parts.append('    </div>')
    parts.append('  </section>')
    parts.append(_category_support_assets_html("  "))
    parts.append('</div>')
    return "\n".join(parts) + "\n"
def _render_category_embed(page_record, overview, support_data, gdrive_urls=None):
    """
    Renders a category-page embed html body.

    :param page_record: dict, the parsed page record.
    :param overview: dict, parsed overview-level shared values.
    :param support_data: dict, parsed render support data.
    :param gdrive_urls: dict, parsed google drive urls or none.
    :return embed_html: string, the rendered embed html body.
    """
    if gdrive_urls is None:
        gdrive_urls = {"root": "", "categories": {}}
    metadata = _page_section_map(page_record, "page_metadata").get("page_metadata", {"fields": {}})
    content_blocks = _page_section_map(page_record, "content_blocks")
    subcategories = page_record["sections"].get("subcategories", [])
    commentary_link_label = overview.get("shared_commentary_link_label", "")
    lead_block = content_blocks.get("lead_category_intro", {})
    category_key = _category_key_from_page_record(metadata["fields"])
    category_combined_download = support_data.get("cms_index", {}).get("category_combined_downloads", {}).get(category_key, {})
    category_page_slug = metadata["fields"].get("webflow_slug", "").strip() or f"cat-{category_key}"
    category_zip_downloads = _zip_download_records_for_page(category_page_slug)
    category_zip_download = category_zip_downloads[0] if category_zip_downloads else {}
    hero_eyebrow = metadata["fields"].get("hero_eyebrow", "").strip()
    parts = []
    parts.append('<div class="fl-archive-page">')
    parts.append('  <section class="fl-archive-page-hero">')
    if hero_eyebrow:
        parts.append(f'    <div class="fl-archive-page-eyebrow">{_escape_html(hero_eyebrow)}</div>')
    parts.append(f'    <h1 class="fl-archive-page-title">{_escape_html(metadata["fields"].get("hero_title", ""))}</h1>')
    lead_html = _render_markdown_blocks(lead_block.get("body_markdown", ""), "    ", "fl-archive-paragraph fl-archive-page-lead", "fl-archive-page-list")
    if lead_html:
        parts.append(lead_html)
    category_download_html = _download_link_html("    ", "Download the combined markdown of all converted archive files in this category", category_combined_download)
    if category_download_html:
        parts.append(category_download_html)
    category_zip_html = _external_link_html("    ", category_zip_download.get("label", ""), category_zip_download.get("url", ""))
    if category_zip_html:
        parts.append(category_zip_html)
    category_gdrive_url = gdrive_urls.get("categories", {}).get(category_key, "")
    if category_gdrive_url:
        category_label = metadata["fields"].get("hero_title", category_key.capitalize())
        parts.append(_external_link_html("    ", f"Go to the {category_label} Google Drive folder", category_gdrive_url))
    parts.append('  </section>')
    parts.append('')
    parts.append('  <section class="fl-archive-page-section">')
    parts.append('    <h2 class="fl-archive-page-subtitle">Subcategories</h2>')
    parts.append('    <div class="fl-archive-page-toc">')
    for subcategory in subcategories:
        anchor = subcategory["fields"].get("anchor", "")
        label = subcategory["fields"].get("label", subcategory["label"])
        toc_label = _subcategory_count_label(category_key, anchor, label, support_data)
        parts.append(f'      <a class="fl-archive-page-toc-link" href="#{_escape_html(anchor)}">{_escape_html(toc_label)}</a>')
    parts.append('    </div>')
    parts.append('  </section>')
    parts.append('')
    for subcategory in subcategories:
        anchor = subcategory["fields"].get("anchor", "")
        label = subcategory["fields"].get("label", subcategory["label"])
        display_label = _subcategory_count_label(category_key, anchor, label, support_data)
        commentary_file = subcategory["fields"].get("commentary_file", "")
        subcategory_key = f"{category_key}/{anchor}"
        subcategory_combined_download = support_data.get("cms_index", {}).get("subcategory_combined_downloads", {}).get(subcategory_key, {})
        subcategory_file_links = support_data.get("cms_index", {}).get("subcategory_file_links", {}).get(subcategory_key, [])
        parts.append(f'  <section id="{_escape_html(anchor)}" class="fl-archive-page-card">')
        parts.append(f'    <h2 class="fl-archive-page-minor-title">{_escape_html(display_label)}</h2>')
        body_html = _render_markdown_blocks(subcategory.get("body_markdown", ""), "    ", "fl-archive-paragraph fl-archive-page-body", "fl-archive-page-list")
        if body_html:
            parts.append(body_html)
        if commentary_file and commentary_link_label:
            commentary_url = _github_commentary_url(commentary_file)
            parts.append(f'    <a class="fl-archive-page-link" href="{_escape_html(commentary_url)}" target="_blank" rel="noopener noreferrer">{_escape_html(commentary_link_label)}</a>')
        subcategory_download_html = _download_link_html("    ", "Download the combined markdown of all converted archive files in this subcategory", subcategory_combined_download)
        if subcategory_download_html:
            parts.append(subcategory_download_html)
        if subcategory_file_links:
            toggle_target_id = f"primary-files-{category_key}-{anchor}"
            parts.append('    <div class="fl-archive-toggle">')
            parts.append(f'      <input id="{_escape_html(toggle_target_id)}" class="fl-archive-toggle-input" type="checkbox">')
            parts.append(f'      <label class="fl-archive-toggle-label" for="{_escape_html(toggle_target_id)}"><span class="fl-archive-toggle-caret" aria-hidden="true">&#9656;</span><span>Subcategory Primary Files</span></label>')
            parts.append('      <div class="fl-archive-page-index-list fl-archive-toggle-content">')
            for file_link in subcategory_file_links:
                parts.append(f'        <a class="fl-archive-page-toc-link" href="{_escape_html(file_link["href"])}">{_escape_html(file_link["label"])}</a>')
            parts.append('      </div>')
            parts.append('    </div>')
        parts.append('  </section>')
        parts.append('')
    if parts[-1] == "":
        parts.pop()
    parts.append(_category_support_assets_html("  "))
    parts.append('</div>')
    return "\n".join(parts) + "\n"
def _parse_archive_headings_structure(headings_path=DEFAULT_FILE_LIST_HEADINGS_PATH):
    """
    Parses the archive-file-list-headings-only file into a category/subcategory structure.

    :param headings_path: string, the path to the headings-only markdown file.
    :return archive_structure: dict, subcategory lists keyed by category slug.
    """
    archive_structure = {}
    if not os.path.isfile(headings_path):
        return archive_structure
    cur_category = ""
    for raw_line in _read_text(headings_path).splitlines():
        stripped_line = raw_line.strip()
        category_match = re.match(r"^##\s+([a-z0-9-]+)\s", stripped_line)
        if category_match:
            cur_category = category_match.group(1)
            archive_structure.setdefault(cur_category, [])
            continue
        subcategory_match = re.match(r"^###\s+([a-z0-9-]+)\s", stripped_line)
        if cur_category and subcategory_match:
            archive_structure[cur_category].append(subcategory_match.group(1))
    return archive_structure
def validate_web_copy_against_archive(web_copy_path=DEFAULT_WEB_COPY_PATH, headings_path=DEFAULT_FILE_LIST_HEADINGS_PATH, verbose=True):
    """
    Validates that the web copy subcategories match what exists on disk.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :param headings_path: string, the path to the headings-only markdown file.
    :param verbose: boolean, whether to print the validation report.
    :return is_valid: boolean, whether the web copy matches the archive on disk.
    """
    archive_structure = _parse_archive_headings_structure(headings_path=headings_path)
    if not archive_structure:
        if verbose:
            print(f"⚠️  Could not read archive structure from {headings_path}")
        return True
    parsed_data = parse_floodlamp_web_copy(web_copy_path=web_copy_path)
    page_spec_map = _get_page_spec_map()
    is_valid = True
    mismatches = []
    for page_slug, page_record in parsed_data["pages"].items():
        page_spec = page_spec_map.get(page_slug)
        if not page_spec or page_slug == "home-archive":
            continue
        metadata = _page_section_map(page_record, "page_metadata").get("page_metadata", {"fields": {}})
        category_key = _category_key_from_page_record(metadata["fields"])
        if category_key not in archive_structure:
            continue
        web_copy_anchors = set()
        for subcategory in page_record["sections"].get("subcategories", []):
            anchor = subcategory["fields"].get("anchor", "")
            if anchor:
                web_copy_anchors.add(anchor)
        disk_subcategories = set(archive_structure.get(category_key, []))
        missing_from_web_copy = disk_subcategories - web_copy_anchors
        extra_in_web_copy = web_copy_anchors - disk_subcategories
        if missing_from_web_copy:
            is_valid = False
            for subcategory_slug in sorted(missing_from_web_copy):
                mismatches.append(f"  {category_key}: subcategory '{subcategory_slug}' exists on disk but is missing from web copy")
        if extra_in_web_copy:
            is_valid = False
            for subcategory_slug in sorted(extra_in_web_copy):
                mismatches.append(f"  {category_key}: subcategory '{subcategory_slug}' is in web copy but not found on disk")
    if verbose:
        if is_valid:
            _print_status_line(True, "web copy vs archive on disk", "all category/subcategory structures match")
        else:
            _print_status_line(False, "web copy vs archive on disk", "structure mismatch detected")
            print("\nMismatches between web copy and archive on disk:")
            for mismatch_line in mismatches:
                print(mismatch_line)
            print(f"\nUpdate the web copy at:\n  {web_copy_path}")
            print("Then re-run this step.")
    return is_valid
WEBFLOW_EMBED_CHAR_LIMIT = 50000
def _compact_embed_html(html_text):
    """
    Compacts embed HTML by removing indentation, blank lines, and minifying inline JS while retaining the comment header.

    :param html_text: string, the full embed html text.
    :return compacted_html: string, the compacted embed html text.
    """
    lines = html_text.splitlines()
    output_lines = []
    in_script = False
    script_lines = []
    for raw_line in lines:
        stripped = raw_line.strip()
        if stripped.startswith("<!--"):
            output_lines.append(stripped)
            continue
        if not stripped:
            continue
        if stripped == "<script>":
            in_script = True
            script_lines = []
            continue
        if stripped == "</script>":
            in_script = False
            minified_js = " ".join(sl.strip() for sl in script_lines if sl.strip())
            output_lines.append(f"<script>{minified_js}</script>")
            continue
        if in_script:
            script_lines.append(stripped)
            continue
        output_lines.append(stripped)
    return "\n".join(output_lines) + "\n"
def render_expected_floodlamp_embeds(web_copy_path=DEFAULT_WEB_COPY_PATH):
    """
    Renders the expected embed html text for all five static pages.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :return rendered_embeds: dict, the rendered html keyed by embed file name.
    """
    parsed_data = parse_floodlamp_web_copy(web_copy_path=web_copy_path)
    support_data = _build_archive_support_data()
    gdrive_urls = _parse_gdrive_urls()
    rendered_embeds = {}
    timestamp_text = _current_short_timestamp()
    page_spec_map = _get_page_spec_map()
    for page_slug, page_record in parsed_data["pages"].items():
        page_spec = page_spec_map.get(page_slug)
        if not page_spec:
            continue
        header_text = _build_embed_header(page_spec, timestamp_text)
        if page_slug == "home-archive":
            body_text = _render_home_embed(page_record, parsed_data["pages"], parsed_data["overview"], gdrive_urls=gdrive_urls, support_data=support_data)
        else:
            body_text = _render_category_embed(page_record, parsed_data["overview"], support_data, gdrive_urls=gdrive_urls)
        full_html = header_text + body_text
        if len(full_html) > WEBFLOW_EMBED_CHAR_LIMIT:
            compacted = _compact_embed_html(full_html)
            print(f"⚠️  {page_spec['embed_file']}: {len(full_html)} chars exceeds {WEBFLOW_EMBED_CHAR_LIMIT} limit, compacted to {len(compacted)} chars")
            full_html = compacted
        rendered_embeds[page_spec["embed_file"]] = full_html
    return rendered_embeds

### Helpers: sync and live compare
def compare_web_copy_to_local_embeds(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER, verbose=True):
    """
    Compares generated embed html against the local embed files.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :param webcode_folder: string, the path to the webcode folder containing the embed files.
    :param verbose: boolean, whether to print the comparison report.
    :return results: list, per-file web-copy-to-local comparison results.
    """
    expected_embeds = render_expected_floodlamp_embeds(web_copy_path=web_copy_path)
    results = []
    for page_spec in PAGE_SPECS:
        embed_file = page_spec["embed_file"]
        local_path = os.path.join(webcode_folder, embed_file)
        local_exists = os.path.exists(local_path)
        local_html = _read_text(local_path) if local_exists else ""
        expected_html = expected_embeds.get(embed_file, "")
        matches = local_exists and _normalize_html_for_compare(local_html) == _normalize_html_for_compare(expected_html)
        results.append({
            "embed_file": embed_file,
            "page_name": page_spec["page_name"],
            "local_path": local_path,
            "local_exists": local_exists,
            "matches": matches,
            "expected_html": expected_html,
            "local_html": local_html,
        })
        if verbose:
            detail_text = "local embed matches generated web-copy output" if matches else "local embed needs update"
            _print_status_line(matches, f"web-copy -> {embed_file}", detail_text)
    return results
def update_local_embeds_from_web_copy(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER, verbose=True):
    """
    Updates changed local embed files from the canonical web-copy markdown file.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :param webcode_folder: string, the path to the webcode folder containing the embed files.
    :param verbose: boolean, whether to print the update report.
    :return updated_files: list, the embed files that were rewritten.
    """
    if not validate_web_copy_against_archive(web_copy_path=web_copy_path, verbose=verbose):
        print("\n⛔ Aborting embed update: web copy is out of sync with archive on disk.")
        return []
    comparison_results = compare_web_copy_to_local_embeds(web_copy_path=web_copy_path, webcode_folder=webcode_folder, verbose=verbose)
    updated_files = []
    for result in comparison_results:
        if result["matches"]:
            continue
        _write_text(result["local_path"], result["expected_html"])
        updated_files.append(result["embed_file"])
    if verbose:
        if updated_files:
            print("\nUpdated local embed files:")
            for embed_file in updated_files:
                print(f"- {embed_file}")
        else:
            print("\nNo local embed updates were needed.")
    return updated_files
def mrun_update_local_embeds_from_web_copy():
    pass
#if __name__ == "__main__":
    update_local_embeds_from_web_copy(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER, verbose=True)
def compare_local_embeds_to_live_pages(webcode_folder=DEFAULT_WEBCODE_FOLDER, base_url=LIVE_PAGE_BASE_URL, verbose=True):
    """
    Compares local embed content against live FloodLAMP pages at a given base url.

    :param webcode_folder: string, the path to the webcode folder containing the embed files.
    :param base_url: string, the base url of the site to compare against.
    :param verbose: boolean, whether to print the comparison report.
    :return results: list, per-page local-to-live comparison results.
    """
    results = []
    for page_spec in PAGE_SPECS:
        live_url = _page_spec_to_live_url(page_spec, base_url=base_url)
        local_path = os.path.join(webcode_folder, page_spec["embed_file"])
        local_html = _read_text(local_path)
        local_text = _html_to_visible_text(local_html)
        local_hrefs = _extract_hrefs(local_html, live_url)
        response = requests.get(live_url, timeout=30)
        response.raise_for_status()
        live_html = response.text
        live_text = _html_to_visible_text(live_html)
        live_hrefs = _extract_hrefs(live_html, live_url)
        text_matches = local_text in live_text
        hrefs_match = set(local_hrefs).issubset(set(live_hrefs))
        matches = text_matches and hrefs_match
        results.append({
            "page_name": page_spec["page_name"],
            "embed_file": page_spec["embed_file"],
            "live_url": live_url,
            "text_matches": text_matches,
            "hrefs_match": hrefs_match,
            "matches": matches,
        })
        if verbose:
            report_label = page_spec["page_name"]
            if matches:
                _print_status_line(True, f"local embed -> live page {report_label}", "visible text and links match")
            else:
                mismatch_bits = []
                if not text_matches:
                    mismatch_bits.append("text mismatch")
                if not hrefs_match:
                    mismatch_bits.append("link mismatch")
                _print_status_line(False, f"local embed -> live page {report_label}", ", ".join(mismatch_bits))
    return results
def print_floodlamp_embed_sync_report(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER):
    """
    Prints the current end-to-end FloodLAMP embed sync report.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :param webcode_folder: string, the path to the webcode folder containing the embed files.
    :return report: dict, the combined local and live comparison results.
    """
    print("\nFloodLAMP embed sync report:")
    validate_web_copy_against_archive(web_copy_path=web_copy_path, verbose=True)
    local_results = compare_web_copy_to_local_embeds(web_copy_path=web_copy_path, webcode_folder=webcode_folder, verbose=True)
    print(f"\nComparing local embeds to production ({LIVE_PAGE_BASE_URL}):")
    production_results = compare_local_embeds_to_live_pages(webcode_folder=webcode_folder, base_url=LIVE_PAGE_BASE_URL, verbose=True)
    print(f"\nComparing local embeds to staging ({STAGING_PAGE_BASE_URL}):")
    staging_results = compare_local_embeds_to_live_pages(webcode_folder=webcode_folder, base_url=STAGING_PAGE_BASE_URL, verbose=True)
    return {"web_copy_to_local": local_results, "local_to_live_production": production_results, "local_to_live_staging": staging_results}
def update_floodlamp_embeds_then_prompt_and_compare(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER):
    """
    Updates local embeds, prompts for manual Webflow paste, then compares local files to the live pages.

    :param web_copy_path: string, the path to the canonical web-copy markdown file.
    :param webcode_folder: string, the path to the webcode folder containing the embed files.
    :return results: dict, the updated files and live comparison results.
    """
    print("\nStep 1: compare canonical web copy against local embed files.")
    updated_files = update_local_embeds_from_web_copy(web_copy_path=web_copy_path, webcode_folder=webcode_folder, verbose=True)
    if updated_files:
        print("\nStep 2: copy and paste these updated embed files into Webflow, then publish:")
        for embed_file in updated_files:
            print(f"- {embed_file}")
    else:
        print("\nStep 2: no local embed files changed. If you still republished, continue.")
    input("\nHit Return when you are done updating Webflow and publishing: ")
    print(f"\nStep 3a: compare local embeds to production ({LIVE_PAGE_BASE_URL}):")
    production_results = compare_local_embeds_to_live_pages(webcode_folder=webcode_folder, base_url=LIVE_PAGE_BASE_URL, verbose=True)
    print(f"\nStep 3b: compare local embeds to staging ({STAGING_PAGE_BASE_URL}):")
    staging_results = compare_local_embeds_to_live_pages(webcode_folder=webcode_folder, base_url=STAGING_PAGE_BASE_URL, verbose=True)
    return {"updated_files": updated_files, "live_results_production": production_results, "live_results_staging": staging_results}

### Manual runs
# `update_floodlamp_embeds_then_prompt_and_compare()` is the interactive/manual Webflow helper:
# regenerate local embeds, pause for manual paste/publish, then compare local files to live pages.
# `update_local_embeds_from_web_copy()` is the direct non-interactive local rewrite helper.
def mrun_update_floodlamp_embeds_then_prompt_and_compare():
    pass
if __name__ == "__main__":
    update_floodlamp_embeds_then_prompt_and_compare(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER)

def mrun_print_floodlamp_embed_sync_report():
    pass
#if __name__ == "__main__":
    print_floodlamp_embed_sync_report(web_copy_path=DEFAULT_WEB_COPY_PATH, webcode_folder=DEFAULT_WEBCODE_FOLDER)

# ===== END OF FILE floodlamp_archive_md_to_embed.py =====
