#!/usr/bin/env bash
set -euo pipefail
TARGET=".agents/skills"
FORCE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) [[ $# -ge 2 ]] || { echo "Missing target path" >&2; exit 2; }; TARGET="$2"; shift 2 ;;
    --force) FORCE=1; shift ;;
    -h|--help) echo "Usage: bash scripts/install.sh [--target PATH] [--force]"; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done
SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SOURCE="$REPO_ROOT/skills/synthesise-ai-free"
DEST="$TARGET/synthesise-ai-free"
[[ -f "$SOURCE/SKILL.md" ]] || { echo "Canonical SKILL.md not found: $SOURCE" >&2; exit 1; }
mkdir -p "$TARGET"
if [[ -e "$DEST" && "$FORCE" -ne 1 ]]; then echo "Destination exists: $DEST (use --force to replace)" >&2; exit 1; fi
[[ ! -e "$DEST" ]] || rm -rf -- "$DEST"
cp -R "$SOURCE" "$DEST"
echo "Installed Synthesise AI Free to: $DEST"
