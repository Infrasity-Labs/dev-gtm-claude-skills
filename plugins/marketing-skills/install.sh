#!/usr/bin/env bash
#
# marketing-skills-plugin installer
#
# Installs 28 marketing skills into your Claude Code environment.
# No agents or shared scripts are required for this plugin — skills only.
#
# Usage:
#   ./install.sh [--project] [--force] [--dry-run] [--configure-mcp] [--help]
#
# Options:
#   --project        Install into ./.claude/ (project-level) instead of ~/.claude/
#   --force          Overwrite existing files without prompting
#   --dry-run        Show what would be installed without making changes
#   --configure-mcp  Print MCP configuration instructions
#   --help           Show this help message

set -euo pipefail

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

ok()   { echo -e "${GREEN}[OK]${NC} $*"; }
warn() { echo -e "${YELLOW}[!!]${NC} $*"; }
err()  { echo -e "${RED}[ERR]${NC} $*" >&2; }
info() { echo -e "${CYAN}[--]${NC} $*"; }

usage() {
  sed -n '3,16p' "$0" | sed 's/^# \{0,1\}//'
}

PROJECT=false
FORCE=false
DRY_RUN=false
CONFIGURE_MCP=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)       PROJECT=true; shift ;;
    --force)         FORCE=true; shift ;;
    --dry-run)       DRY_RUN=true; shift ;;
    --configure-mcp) CONFIGURE_MCP=true; shift ;;
    --help|-h)       usage; exit 0 ;;
    *) err "Unknown argument: $1"; usage; exit 1 ;;
  esac
done

if $PROJECT; then
  CLAUDE_HOME="${PWD}/.claude"
else
  CLAUDE_HOME="${HOME}/.claude"
fi

SKILLS_DST="${CLAUDE_HOME}/skills"

copy_item() {
  local src="$1" dst="$2"
  if [[ ! -e "$src" ]]; then
    warn "Source missing, skipped: $src"
    return 0
  fi
  if $DRY_RUN; then
    echo "  would install: $(basename "$src") -> $dst"
    return 0
  fi
  if [[ -e "$dst" ]] && ! $FORCE; then
    printf "  Overwrite %s? [y/N]: " "$(basename "$dst")"
    read -r reply
    case "$reply" in
      y|Y|yes|YES) ;;
      *) warn "Skipped: $(basename "$dst")"; return 0 ;;
    esac
  fi
  [[ -e "$dst" ]] && rm -rf "$dst"
  cp -r "$src" "$dst"
  ok "Installed: $(basename "$src")"
}

echo ""
echo "  marketing-skills-plugin installer"
echo "  ==================================="
echo "  skills -> ${SKILLS_DST}"
$DRY_RUN && warn "DRY RUN — no files will be written"
echo ""

# Skills (28 directories)
info "Installing 28 skills..."
$DRY_RUN || mkdir -p "$SKILLS_DST"
skill_count=0
for skill_dir in "${PLUGIN_DIR}/skills"/*/; do
  [[ -d "$skill_dir" ]] || continue
  name="$(basename "$skill_dir")"
  copy_item "$skill_dir" "${SKILLS_DST}/${name}"
  skill_count=$((skill_count + 1))
done
echo ""

# Optional MCP configuration note
if $CONFIGURE_MCP && ! $DRY_RUN; then
  SETTINGS="${CLAUDE_HOME}/settings.json"
  info "MCP configuration note:"
  echo "  Copy server templates from .mcp.json into ${SETTINGS}"
  echo "  and replace \${ENV_VAR} placeholders with your actual credentials."
  echo "  See README.md -> Optional MCP Setup for full instructions."
  echo ""
fi

echo "  ==================================="
if $DRY_RUN; then
  warn "DRY RUN complete — nothing was written."
else
  ok "Done: ${skill_count} skills installed."
fi
echo ""
echo "  Next steps:"
echo "    1. Restart Claude Code (or reload the window)"
echo "    2. Run a skill:  /analytics, /ads, /copywriting, /cro ..."
echo "    3. (optional) Configure MCP servers — see README.md -> Optional MCP Setup"
echo ""
