# `_code` — reference scripts and Webflow assets

This folder is a **read-only snapshot** of tooling used to maintain and publish the FloodLAMP archive from a private development repository. It is mirrored into this public repo for transparency and for anyone adapting similar workflows.


## Layout (same filenames as in the private repo)

| Path | Purpose |
|------|--------|
| `public-repo-mirror/mirror_to_repo.py` | Syncs publishable files from the private corpus into this GitHub repo (full add/update/delete). |
| `public-repo-mirror/nuke_history.sh` | Optional one-commit squash for `main` on the public repo (guarded; local path and remote must match). |
| `floodlamp_publish_rules.py` | Shared naming, paths, and include/exclude rules for publication (standalone module; no `primary.*` imports). |
| `floodlamp_publication_workflow.md` | Human checklist for combined/zips, refresh, CMS, embeds, and mirroring. |
| `webcode/` | Webflow embed HTML, the archive web-copy markdown source, the item template script, and the Python helper that renders embeds from markdown. |


## Not included here

Heavy pipeline code (`floodlamp_archive_ops.py`, `floodlamp_refresh.py`, and related modules) depends on a large private `primary.*` library and the full corpus layout; it is **not** mirrored. The roll-up and zip generation run in that private environment before mirroring.


## License

Files in this folder are under the MIT License unless a specific file states otherwise; see the [`LICENSE`](../LICENSE) in the repository root.
