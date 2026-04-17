# ===== START OF FILE floodlamp_publish_rules.py =====
# Purpose: Shared FloodLAMP publication rules, naming helpers, and path/include-exclude policy used by archive, refresh, and CMS flows.

import os

DEFAULT_EXCLUDE_SUBFOLDERS = []
DEFAULT_FLOODLAMP_CMS_SKIP_REL_PATHS = [
 "pilots/pilot-data/_filelist_pilot-data.md",
]
DEFAULT_FLOODLAMP_CMS_SKIP_REL_PREFIXES = [
 "regulatory/fda-townhalls/fda-townhalls-transcripts-qa/",
]
FDA_TOWNHALLS_CATEGORY = "regulatory"
FDA_TOWNHALLS_SUBCATEGORY = "fda-townhalls"
FDA_TOWNHALLS_NESTED_FOLDER_NAME = "fda-townhalls-transcripts-qa"
FDA_TOWNHALLS_QA_SUFFIX = "_qa-qonly.md"
FDA_TOWNHALLS_TRANSCRIPT_SUFFIX = "_section-titles.md"
DEFAULT_FLOODLAMP_UPDATE_RECORDS_FOLDER = "_exclude-from-archive/changelogs-refresh"
DEFAULT_FLOODLAMP_INTEGRATED_VIEW_FILE = "_archive-integrated-view.md"
DEFAULT_FLOODLAMP_LEGACY_PROPAGATION_REF_FILE = "_propagation-ref.md"

### Helpers: paths and naming
def normalize_rel_path(path_value):
 """
 Normalizes a relative path to forward slashes.

 :param path_value: string, the path value to normalize.
 :return normalized_path: string, the normalized path.
 """
 return str(path_value).replace(os.sep, "/").strip("/")
def rel_path_startswith(rel_path, prefix):
 """
 Checks whether a normalized relative path starts with a normalized prefix.

 :param rel_path: string, the relative path to inspect.
 :param prefix: string, the normalized prefix to match.
 :return matches: bool, True when the path starts with the prefix.
 """
 normalized_rel_path = normalize_rel_path(rel_path)
 normalized_prefix = normalize_rel_path(prefix)
 if not normalized_prefix:
  return False
 return normalized_rel_path == normalized_prefix or normalized_rel_path.startswith(normalized_prefix + "/")
def get_fda_townhalls_rel_path():
 """
 Gets the relative path for the FDA Town Halls subcategory.

 :return rel_path: string, the normalized subcategory relative path.
 """
 return f"{FDA_TOWNHALLS_CATEGORY}/{FDA_TOWNHALLS_SUBCATEGORY}"
def get_fda_townhalls_nested_rel_prefix():
 """
 Gets the relative path prefix for the nested FDA Town Halls transcript and QA folder.

 :return rel_prefix: string, the normalized nested relative path prefix.
 """
 return f"{get_fda_townhalls_rel_path()}/{FDA_TOWNHALLS_NESTED_FOLDER_NAME}"
def get_fda_townhalls_folder(root_folder="data/floodlamp"):
 """
 Gets the absolute path to the FDA Town Halls folder.

 :param root_folder: string, the FloodLAMP root folder.
 :return folder_path: string, the absolute town halls folder path.
 """
 return os.path.join(root_folder, FDA_TOWNHALLS_CATEGORY, FDA_TOWNHALLS_SUBCATEGORY)
def get_fda_townhalls_nested_folder(root_folder="data/floodlamp"):
 """
 Gets the absolute path to the nested FDA Town Halls transcript and QA folder.

 :param root_folder: string, the FloodLAMP root folder.
 :return folder_path: string, the absolute nested folder path.
 """
 return os.path.join(get_fda_townhalls_folder(root_folder), FDA_TOWNHALLS_NESTED_FOLDER_NAME)
def get_floodlamp_update_records_folder(root_folder="data/floodlamp"):
 """
 Gets the absolute path to the FloodLAMP update records folder.

 :param root_folder: string, the FloodLAMP root folder.
 :return folder_path: string, the absolute update records folder path.
 """
 return os.path.join(root_folder, DEFAULT_FLOODLAMP_UPDATE_RECORDS_FOLDER)
def get_floodlamp_integrated_view_path(root_folder="data/floodlamp"):
 """
 Gets the absolute path to the integrated archive view markdown file.

 :param root_folder: string, the FloodLAMP root folder.
 :return file_path: string, the integrated archive view file path.
 """
 return os.path.join(root_folder, DEFAULT_FLOODLAMP_INTEGRATED_VIEW_FILE)
def get_floodlamp_legacy_propagation_ref_path(root_folder="data/floodlamp"):
 """
 Gets the absolute path to the legacy propagation reference markdown file.

 :param root_folder: string, the FloodLAMP root folder.
 :return file_path: string, the legacy propagation reference file path.
 """
 return os.path.join(root_folder, DEFAULT_FLOODLAMP_LEGACY_PROPAGATION_REF_FILE)

### Helpers: publication rules
def is_default_excluded_subfolder(subfolder_name):
 """
 Checks whether a subfolder is excluded by default from standard archive rebuild flows.

 :param subfolder_name: string, the subfolder name to inspect.
 :return is_excluded: bool, True when the subfolder is excluded by default.
 """
 return subfolder_name in DEFAULT_EXCLUDE_SUBFOLDERS
def is_fda_townhalls_qa_file(file_name):
 """
 Checks whether a file name is an FDA Town Halls QA markdown file.

 :param file_name: string, the file name to inspect.
 :return is_match: bool, True when the file is a QA markdown file.
 """
 return str(file_name).endswith(FDA_TOWNHALLS_QA_SUFFIX)
def is_fda_townhalls_transcript_file(file_name):
 """
 Checks whether a file name is an FDA Town Halls transcript markdown file.

 :param file_name: string, the file name to inspect.
 :return is_match: bool, True when the file is a transcript markdown file.
 """
 return str(file_name).endswith(FDA_TOWNHALLS_TRANSCRIPT_SUFFIX)
def get_category_md_zip_exclude_suffixes(category_name):
 """
 Gets markdown suffixes that should be excluded from a category markdown-only zip.

 :param category_name: string, the category name to inspect.
 :return suffixes: list, the suffixes to exclude from the markdown-only zip.
 """
 if category_name == FDA_TOWNHALLS_CATEGORY:
  return [FDA_TOWNHALLS_QA_SUFFIX, FDA_TOWNHALLS_TRANSCRIPT_SUFFIX]
 return []
def should_create_category_md_only_zip(category_name, include_md_only_zip=True):
 """
 Checks whether a category markdown-only zip should be generated.

 :param category_name: string, the category name to inspect.
 :param include_md_only_zip: bool, the requested markdown-only zip behavior.
 :return should_create: bool, True when the category markdown-only zip should be generated.
 """
 if not include_md_only_zip:
  return False
 if category_name == FDA_TOWNHALLS_CATEGORY:
  return False
 return True
def get_floodlamp_cms_skip_rel_paths(extra_skip_rel_paths=None):
 """
 Gets the configured exact relative paths to skip for CMS inclusion.

 :param extra_skip_rel_paths: list, optional additional exact relative paths to skip.
 :return skip_rel_paths: list, the normalized exact relative paths to skip.
 """
 skip_rel_paths = [normalize_rel_path(path_value) for path_value in DEFAULT_FLOODLAMP_CMS_SKIP_REL_PATHS]
 for path_value in extra_skip_rel_paths or []:
  normalized_path = normalize_rel_path(path_value)
  if normalized_path not in skip_rel_paths:
   skip_rel_paths.append(normalized_path)
 return skip_rel_paths
def get_floodlamp_cms_skip_rel_prefixes(extra_skip_rel_prefixes=None):
 """
 Gets the configured relative path prefixes to skip for CMS inclusion.

 :param extra_skip_rel_prefixes: list, optional additional relative path prefixes to skip.
 :return skip_rel_prefixes: list, the normalized relative path prefixes to skip.
 """
 skip_rel_prefixes = [normalize_rel_path(path_value) for path_value in DEFAULT_FLOODLAMP_CMS_SKIP_REL_PREFIXES]
 for path_value in extra_skip_rel_prefixes or []:
  normalized_path = normalize_rel_path(path_value)
  if normalized_path not in skip_rel_prefixes:
   skip_rel_prefixes.append(normalized_path)
 return skip_rel_prefixes
def should_include_floodlamp_cms_rel_path(rel_path, extra_skip_rel_paths=None, extra_skip_rel_prefixes=None):
 """
 Checks whether a relative path should be included in FloodLAMP CMS generation.

 :param rel_path: string, the repo-relative path inside the FloodLAMP root.
 :param extra_skip_rel_paths: list, optional additional exact relative paths to skip.
 :param extra_skip_rel_prefixes: list, optional additional relative path prefixes to skip.
 :return should_include: bool, True when the relative path should be included.
 """
 normalized_rel_path = normalize_rel_path(rel_path)
 if normalized_rel_path in get_floodlamp_cms_skip_rel_paths(extra_skip_rel_paths):
  return False
 for skip_prefix in get_floodlamp_cms_skip_rel_prefixes(extra_skip_rel_prefixes):
  if rel_path_startswith(normalized_rel_path, skip_prefix):
   return False
 return True

# ===== END OF FILE floodlamp_publish_rules.py =====
