#!/usr/bin/env bash
# Install claude-skills into OpenClaw's shared skills directory
# Uses `openclaw skills install --global` so OpenClaw manages the entries.
#
# Usage: ./scripts/openclaw-install.sh [--dry-run] [--force]

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DRY_RUN=false
FORCE=false

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --force)   FORCE=true ;;
  esac
done

FORCE_FLAG=""
$FORCE && FORCE_FLAG="--force"

installed=0
skipped=0
failed=0

while IFS= read -r skill_md; do
  skill_dir="$(dirname "$skill_md")"
  skill_name="$(basename "$skill_dir")"
  target="${HOME}/.openclaw/skills/${skill_name}"

  if [[ -e "$target" ]] && ! $FORCE; then
    skipped=$((skipped + 1))
    continue
  fi

  if $DRY_RUN; then
    echo "  [dry-run] would install: $skill_name"
    installed=$((installed + 1))
    continue
  fi

  if openclaw skills install "$skill_dir" --global --as "$skill_name" $FORCE_FLAG > /dev/null 2>&1; then
    echo "  ✅ installed: $skill_name"
    installed=$((installed + 1))
  else
    echo "  ❌ failed: $skill_name"
    failed=$((failed + 1))
  fi
done < <(
  cd "$REPO_DIR" && \
  find skills marketing-skills writing-skills seo-skills web-design product-management-skills \
    -name "SKILL.md" -not -path "*/.git/*" 2>/dev/null | sed "s|^|$REPO_DIR/|"
)

echo ""
if $DRY_RUN; then
  echo "Dry run complete. Would install $installed skill(s). ($skipped already exist)"
else
  echo "Done. Installed $installed skill(s). ($skipped skipped, $failed failed)"
  echo "Run 'openclaw skills list' to verify."
fi
