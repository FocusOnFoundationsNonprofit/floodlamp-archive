"""
Mirror publishable archive files from data/floodlamp/ to the floodlamp-archive repo.

Performs a full sync: adds new files, updates changed files, deletes orphaned files.
Also copies MIT LICENSE and README.md to the target repo root, and optionally mirrors a
curated _code/ subtree (see MIRROR_CODE_TO_TARGET). Use mirror_repo_root_and_code_bundle()
to update only LICENSE, README.md, and _code/ without syncing the archive tree.
"""
import filecmp
import os
import shutil
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
SOURCE_ROOT = os.path.join(REPO_ROOT, "data", "floodlamp")
ARCHIVE_CODE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
LOG_PATH = os.path.join(SCRIPT_DIR, "mirror_log.md")
TARGET_REPO_PATH = os.path.normpath(os.path.join(REPO_ROOT, "..", "floodlamp-archive"))
ARCHIVE_REPO_ROOT_FILES = os.path.join(SCRIPT_DIR, "archive_repo_root")
EXCLUDE_SUBCATEGORIES = []  #["fda-townhalls"]
TARGET_IGNORE_DIRS = {".git", ".vscode"}
EXCLUDE_DIR_NAME = "_exclude-from-archive"
# When True, sync the curated files below into TARGET_REPO_PATH/_code/ and remove orphans there.
# When False, leave any existing _code/ tree untouched (no deletes under _code/).
MIRROR_CODE_TO_TARGET = True
# Paths relative to ARCHIVE_CODE_ROOT; mirrored to _code/<same relative path>.
CODE_PATHS_RELATIVE = [
    os.path.join("public-repo-mirror", "mirror_to_repo.py"),
    os.path.join("public-repo-mirror", "nuke_history.sh"),
    "floodlamp_publish_rules.py",
    "floodlamp_publication_workflow.md",
    os.path.join("webcode", "floodlamp_archive_md_to_embed.py"),
    os.path.join("webcode", "floodlamp-archive-web-copy.md"),
    os.path.join("webcode", "floodlamp_archive_item_template.js"),
    os.path.join("webcode", "floodlamp_archive_item_template_setup.md"),
    os.path.join("webcode", "floodlamp_archive_site_head.html"),
    os.path.join("webcode", "floodlamp_archive_home_archive_embed.html"),
    os.path.join("webcode", "floodlamp_archive_cat_guides_embed.html"),
    os.path.join("webcode", "floodlamp_archive_cat_pilots_embed.html"),
    os.path.join("webcode", "floodlamp_archive_cat_regulatory_embed.html"),
    os.path.join("webcode", "floodlamp_archive_cat_various_embed.html"),
    os.path.join("webcode", "floodlamp_archive_item_template_embed.html"),
]
_CODE_README_SOURCE = os.path.join(SCRIPT_DIR, "_code_bundle_README.md")
_CODE_README_DEST_REL = os.path.join("_code", "README.md")

### Config and categories
def parse_categories(path):
    """
    Parse _categories.md to get category/subcategory structure.

    :param path: str, path to _categories.md file.
    :return categories: dict, mapping of category name to list of subcategory names.
    """
    categories = {}
    current_category = None
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("## "):
                current_category = line[3:].strip()
                categories[current_category] = []
            elif line and current_category is not None:
                categories[current_category].append(line)
    return categories

### Exclusion logic
def _is_excluded_dir(dirname):
    """
    Check if a directory name should be excluded from mirroring.

    :param dirname: str, the directory basename to check.
    :return excluded: bool, True if the directory should be skipped.
    """
    if dirname == EXCLUDE_DIR_NAME:
        return True
    if dirname.startswith("_zip_") and not dirname.startswith("_zip-md_"):
        return True
    return False
def _is_excluded_file(filename):
    """
    Check if a file should be excluded from mirroring.

    :param filename: str, the file basename to check.
    :return excluded: bool, True if the file should be skipped.
    """
    if filename == ".DS_Store":
        return True
    if filename.startswith("_zip_") and not filename.startswith("_zip-md_"):
        return True
    if filename.startswith("_filelist"):
        return True
    return False

### File collection
def collect_source_files(categories):
    """
    Walk the source tree and collect files to mirror, applying all exclusion rules.

    :param categories: dict, category/subcategory mapping from _categories.md.
    :return files: dict, mapping of relative path (from source root) to absolute path.
    """
    exclude_subs = set(EXCLUDE_SUBCATEGORIES)
    category_names = set(categories.keys())
    files = {}
    for dirpath, dirnames, filenames in os.walk(SOURCE_ROOT):
        rel_dir = os.path.relpath(dirpath, SOURCE_ROOT)
        if rel_dir == ".":
            rel_dir = ""
        # Prune excluded directories in-place
        dirnames[:] = [
            d for d in dirnames
            if not _is_excluded_dir(d) and d not in TARGET_IGNORE_DIRS
        ]
        # Check if this is a subcategory directory that should be excluded
        parts = rel_dir.split(os.sep) if rel_dir else []
        if len(parts) == 2 and parts[0] in category_names and parts[1] in exclude_subs:
            dirnames.clear()
            continue
        for filename in filenames:
            if _is_excluded_file(filename):
                continue
            rel_path = os.path.join(rel_dir, filename) if rel_dir else filename
            files[rel_path] = os.path.join(dirpath, filename)
    return files
def collect_target_files(target_root):
    """
    Walk the target repo and collect all existing files, skipping .git and .vscode.

    :param target_root: str, absolute path to the target repo root.
    :return files: dict, mapping of relative path to absolute path.
    """
    files = {}
    for dirpath, dirnames, filenames in os.walk(target_root):
        dirnames[:] = [d for d in dirnames if d not in TARGET_IGNORE_DIRS]
        rel_dir = os.path.relpath(dirpath, target_root)
        if rel_dir == ".":
            rel_dir = ""
        for filename in filenames:
            rel_path = os.path.join(rel_dir, filename) if rel_dir else filename
            files[rel_path] = os.path.join(dirpath, filename)
    return files

### Repo root LICENSE/README and optional _code/
def collect_repo_root_artifact_files():
    """
    Map LICENSE and README.md at the target repo root to their sources next to this script.

    :return files: dict, relative path under target repo -> absolute source path.
    """
    license_src = os.path.join(ARCHIVE_REPO_ROOT_FILES, "LICENSE")
    readme_src = os.path.join(ARCHIVE_REPO_ROOT_FILES, "README.md")
    if not os.path.isfile(license_src) or not os.path.isfile(readme_src):
        raise FileNotFoundError(f"Missing {license_src} or {readme_src}")
    return {"LICENSE": license_src, "README.md": readme_src}
def collect_code_mirror_files():
    """
    Map _code/ subtree files to sources under ARCHIVE_CODE_ROOT when MIRROR_CODE_TO_TARGET is True.

    :return files: dict, relative path under target repo -> absolute source path.
    """
    if not MIRROR_CODE_TO_TARGET:
        return {}
    out = {}
    for rel in CODE_PATHS_RELATIVE:
        rel_norm = rel.replace("\\", "/")
        abs_src = os.path.normpath(os.path.join(ARCHIVE_CODE_ROOT, rel))
        if not os.path.isfile(abs_src):
            raise FileNotFoundError(f"Code mirror source missing: {abs_src}")
        dest_rel = os.path.join("_code", *rel_norm.split("/"))
        out[dest_rel] = abs_src
    if not os.path.isfile(_CODE_README_SOURCE):
        raise FileNotFoundError(f"Code README source missing: {_CODE_README_SOURCE}")
    out[_CODE_README_DEST_REL] = _CODE_README_SOURCE
    return out
def _is_protected_path(rel_path, protected_prefixes):
    """
    Return True if rel_path is exactly a protected prefix or lives under it.

    :param rel_path: str, relative path using OS separators.
    :param protected_prefixes: list, directory name prefixes to protect from deletion.
    :return protected: bool, True when this path should not be deleted as an orphan.
    """
    if not protected_prefixes:
        return False
    for prefix in protected_prefixes:
        if rel_path == prefix or rel_path.startswith(prefix + os.sep):
            return True
    return False

### Sync
def sync(source_files, target_files, target_root, protected_prefixes=None):
    """
    Perform add/update/delete sync from source to target.

    :param source_files: dict, relative path -> absolute source path.
    :param target_files: dict, relative path -> absolute target path.
    :param target_root: str, absolute path to target repo root.
    :param protected_prefixes: list or None, top-level dir names under target_root to skip when deleting orphans.
    :return changes: dict with keys 'added', 'updated', 'deleted', each a sorted list of relative paths.
    """
    protected_prefixes = protected_prefixes or []
    added = []
    updated = []
    deleted = []
    # Add and update
    for rel_path, src_abs in source_files.items():
        tgt_abs = os.path.join(target_root, rel_path)
        if rel_path not in target_files:
            os.makedirs(os.path.dirname(tgt_abs), exist_ok=True)
            shutil.copy2(src_abs, tgt_abs)
            added.append(rel_path)
        elif not filecmp.cmp(src_abs, tgt_abs, shallow=False):
            shutil.copy2(src_abs, tgt_abs)
            updated.append(rel_path)
    # Delete orphans
    for rel_path, tgt_abs in target_files.items():
        if rel_path not in source_files:
            if _is_protected_path(rel_path, protected_prefixes):
                continue
            os.remove(tgt_abs)
            deleted.append(rel_path)
    # Clean up empty directories left by deletions
    for rel_path in deleted:
        tgt_dir = os.path.dirname(os.path.join(target_root, rel_path))
        while tgt_dir != target_root:
            if os.path.isdir(tgt_dir) and not os.listdir(tgt_dir):
                os.rmdir(tgt_dir)
                tgt_dir = os.path.dirname(tgt_dir)
            else:
                break
    return {"added": sorted(added), "updated": sorted(updated), "deleted": sorted(deleted)}
def mirror_repo_root_and_code_bundle():
    """
    Sync only LICENSE, README.md, and (when MIRROR_CODE_TO_TARGET) the _code/ tree.

    Does not add, update, or delete category folders or other archive files. Use when only root docs or scripts changed.

    :return changes: dict with keys 'added', 'updated', 'deleted', each a sorted list of relative paths, or None if target repo is missing.
    """
    if not os.path.isdir(TARGET_REPO_PATH):
        print(f"ERROR: target repo not found at {TARGET_REPO_PATH}")
        return None
    print(f"Target (partial): {TARGET_REPO_PATH}")
    print(f"Mirror _code/ bundle: {MIRROR_CODE_TO_TARGET}")
    print()
    source_files = collect_repo_root_artifact_files()
    if MIRROR_CODE_TO_TARGET:
        source_files.update(collect_code_mirror_files())
    full_target = collect_target_files(TARGET_REPO_PATH)
    managed = {}
    for rel, abs_path in full_target.items():
        if rel in ("LICENSE", "README.md"):
            managed[rel] = abs_path
        elif MIRROR_CODE_TO_TARGET and rel.startswith("_code" + os.sep):
            managed[rel] = abs_path
    changes = sync(source_files, managed, TARGET_REPO_PATH, protected_prefixes=[])
    write_log(changes)
    total = len(changes["added"]) + len(changes["updated"]) + len(changes["deleted"])
    print(f"Partial sync done. {total} changes ({len(changes['added'])} added, {len(changes['updated'])} updated, {len(changes['deleted'])} deleted)")
    if total > 0:
        print(f"Log written to {LOG_PATH}")
    return changes

### Logging
def write_log(changes):
    """
    Prepend a timestamped sync summary to the mirror log file (newest entries first).

    :param changes: dict with 'added', 'updated', 'deleted' lists of relative paths.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"# === {timestamp}  added: {len(changes['added'])}  updated: {len(changes['updated'])}  deleted: {len(changes['deleted'])} ==="
    lines = [header]
    for p in changes["added"]:
        lines.append(f"+ {p}")
    for p in changes["updated"]:
        lines.append(f"~ {p}")
    for p in changes["deleted"]:
        lines.append(f"- {p}")
    lines.append("")
    new_entry = "\n".join(lines) + "\n"
    existing = ""
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            existing = f.read()
    with open(LOG_PATH, "w") as f:
        f.write(new_entry + existing)

### Main
def main():
    """
    Run the mirror sync: load config, collect files, sync, log, and print summary.
    """
    categories = parse_categories(os.path.join(SOURCE_ROOT, "_categories.md"))
    if not os.path.isdir(TARGET_REPO_PATH):
        print(f"ERROR: target repo not found at {TARGET_REPO_PATH}")
        return
    print(f"Source: {SOURCE_ROOT}")
    print(f"Target: {TARGET_REPO_PATH}")
    print(f"Excluded subcategories: {EXCLUDE_SUBCATEGORIES}")
    print(f"Mirror _code/ bundle: {MIRROR_CODE_TO_TARGET}")
    print()
    source_files = collect_source_files(categories)
    source_files.update(collect_repo_root_artifact_files())
    if MIRROR_CODE_TO_TARGET:
        source_files.update(collect_code_mirror_files())
    target_files = collect_target_files(TARGET_REPO_PATH)
    protected = [] if MIRROR_CODE_TO_TARGET else ["_code"]
    changes = sync(source_files, target_files, TARGET_REPO_PATH, protected_prefixes=protected)
    write_log(changes)
    total = len(changes["added"]) + len(changes["updated"]) + len(changes["deleted"])
    print(f"Done. {total} changes ({len(changes['added'])} added, {len(changes['updated'])} updated, {len(changes['deleted'])} deleted)")
    if total > 0:
        print(f"Log written to {LOG_PATH}")
if __name__ == "__main__":
    main()
