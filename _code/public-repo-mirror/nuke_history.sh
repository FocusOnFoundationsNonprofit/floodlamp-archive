#!/usr/bin/env bash
# nuke_history.sh
#
# Purpose:
#   Nuke/squash ALL history on main into a single clean snapshot commit
#   using an orphan branch + force push.
#
# SAFETY GUARDS (hard-coded):
#   - Must be run from within this exact local repo path:
#       /Users/randytrue/Documents/Code/floodlamp-archive
#   - The 'origin' remote URL must be exactly:
#       https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive.git
#   - Requires interactive confirmation: you must type "yes" (case-insensitive)
#
# Usage:
#   cd /Users/randytrue/Documents/Code/floodlamp-archive
#   bash /Users/randytrue/Documents/Code/floodlamp-archive/_code/public-repo-mirror/nuke_history.sh "Your commit message here"#
# Notes / warnings:
#   - This script will FORCE PUSH to origin/main. Make sure that's what you want.
#   - It assumes your default branch is "main" and your remote is "origin".
#   - Anyone who cloned/forked before can still have the old history.
#
set -euo pipefail

BRANCH="main"
REMOTE="origin"

EXPECTED_TOPLEVEL="/Users/randytrue/Documents/Code/floodlamp-archive"
EXPECTED_REMOTE_URL="https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive.git"

if [[ $# -lt 1 ]]; then
  echo "ERROR: Missing commit message."
  echo "Usage: bash $0 \"Clean snapshot commit message\""
  exit 2
fi

SNAPSHOT_MSG="$1"

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git not found on PATH."
  exit 2
fi

# Ensure we're inside a git repo
if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "ERROR: Not inside a git repository."
  exit 2
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
echo "Repo root detected: $REPO_ROOT"

# Guard: exact local path match
if [[ "$REPO_ROOT" != "$EXPECTED_TOPLEVEL" ]]; then
  echo "ERROR: Safety guard triggered."
  echo "  This script is hard-coded to run only in:"
  echo "    $EXPECTED_TOPLEVEL"
  echo "  But detected repo root is:"
  echo "    $REPO_ROOT"
  exit 2
fi

cd "$REPO_ROOT"

# Confirm remote exists
if ! git remote get-url "$REMOTE" >/dev/null 2>&1; then
  echo "ERROR: Remote '$REMOTE' not found. Available remotes:"
  git remote -v || true
  exit 2
fi

REMOTE_URL="$(git remote get-url "$REMOTE")"
echo "Remote ($REMOTE) detected: $REMOTE_URL"

# Guard: exact remote URL match
if [[ "$REMOTE_URL" != "$EXPECTED_REMOTE_URL" ]]; then
  echo "ERROR: Safety guard triggered."
  echo "  This script is hard-coded to run only when origin is exactly:"
  echo "    $EXPECTED_REMOTE_URL"
  echo "  But detected origin is:"
  echo "    $REMOTE_URL"
  exit 2
fi

# Ensure clean working tree
if [[ -n "$(git status --porcelain)" ]]; then
  echo "ERROR: Working tree is not clean. Commit/stash changes before running."
  git status --porcelain
  exit 2
fi

# Ensure on main
CURRENT_BRANCH="$(git branch --show-current || true)"
if [[ "$CURRENT_BRANCH" != "$BRANCH" ]]; then
  echo "Checking out $BRANCH..."
  git checkout "$BRANCH" 2>/dev/null || git checkout -B "$BRANCH"
fi

# Pull latest (best-effort; ok if diverged)
echo "Pulling latest from $REMOTE/$BRANCH (best effort)..."
git pull "$REMOTE" "$BRANCH" --ff-only || true

# Ensure still clean
if [[ -n "$(git status --porcelain)" ]]; then
  echo "ERROR: Working tree became dirty after pull (unexpected). Resolve and retry."
  git status --porcelain
  exit 2
fi

echo
echo "DANGER ZONE"
echo "This will REWRITE HISTORY and FORCE PUSH to:"
echo "  $EXPECTED_REMOTE_URL ($REMOTE/$BRANCH)"
echo
echo "It will replace ALL commit history on $BRANCH with ONE commit:"
echo "  \"$SNAPSHOT_MSG\""
echo
read -r -p "Are you sure? If so, type yes and press Enter: " CONFIRM
CONFIRM_LOWER="$(printf "%s" "$CONFIRM" | tr '[:upper:]' '[:lower:]')"

if [[ "$CONFIRM_LOWER" != "yes" ]]; then
  echo "Aborted (you did not type 'yes'). No changes made."
  exit 0
fi

echo
echo "Proceeding..."

# Nuke history via orphan branch snapshot
git checkout --orphan clean-slate
git add -A

if git diff --cached --quiet; then
  echo "ERROR: Nothing to commit. Is your working tree empty?"
  exit 2
fi

git commit -m "$SNAPSHOT_MSG"

# Replace main and force-push
git branch -M "$BRANCH"
echo "Force-pushing rewritten history to $REMOTE/$BRANCH..."
git push --force "$REMOTE" "$BRANCH"

# Cleanup: prune + local gc (optional but nice)
echo
echo "Pruning and running local GC..."
git fetch --prune "$REMOTE" || true
git gc --prune=now --aggressive || true

# Verify only 1 commit reachable from HEAD
FINAL_COUNT="$(git rev-list --count HEAD)"
echo
echo "FINAL commit count on $BRANCH (reachable from HEAD): $FINAL_COUNT"
if [[ "$FINAL_COUNT" -ne 1 ]]; then
  echo "WARNING: Expected 1, got $FINAL_COUNT. Something kept additional commits reachable."
  echo "Check for extra branches/tags pointing to old history:"
  echo "  git branch -a"
  echo "  git tag -n"
  exit 1
fi

echo
echo "SUCCESS: History nuked. '$BRANCH' now has a single commit."
echo "Next: open GitHub -> repo -> Commits (on main). You should see only:"
echo "  $SNAPSHOT_MSG"
