#!/usr/bin/env bash
#
# writing-skills-plugin uninstaller
#
# Removes skills, agents, and shared scripts installed by install.sh.
# Does NOT touch ~/.claude/settings.json (user-managed).
#
# Usage:
#   ./uninstall.sh [--project] [--dry-run] [--help]
#
# Options:
#   --project   Remove from ./.claude/ instead of ~/.claude/
#   --dry-run   Show what would be removed without deleting anything
#   --help      Show this help message

set -euo pipefail

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

ok()   { echo -e "${GREEN}[OK]${NC} $*"; }
warn() { echo -e "${YELLOW}[!!]${NC} $*"; }
err()  { echo -e "${RED}[ERR]${NC} $*" >&2; }

usage() {
  sed -n '3,13p' "$0" | sed 's/^# \{0,1\}//'
}

PROJECT=false
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) PROJECT=true; shift ;;
    --dry-run) DRY_RUN=true; shift ;;
    --help|-h) usage; exit 0 ;;
    *) err "Unknown argument: $1"; usage; exit 1 ;;
  esac
done

if $PROJECT; then
  CLAUDE_HOME="${PWD}/.claude"
else
  CLAUDE_HOME="${HOME}/.claude"
fi

SKILLS_DST="${CLAUDE_HOME}/skills"
AGENTS_DST="${CLAUDE_HOME}/agents"
SCRIPTS_DST="${CLAUDE_HOME}/scripts"

remove_item() {
  local path="$1"
  if [[ ! -e "$path" ]]; then
    return 0
  fi
  if $DRY_RUN; then
    echo "  would remove: $path"
    return 0
  fi
  rm -rf "$path"
  ok "Removed: $path"
}

echo ""
echo "  writing-skills-plugin uninstaller"
echo "  ==================================="
$DRY_RUN && warn "DRY RUN — no files will be deleted"
echo ""

# Skills
removed_skills=0
for skill_dir in "${PLUGIN_DIR}/skills"/*/; do
  name="$(basename "$skill_dir")"
  remove_item "${SKILLS_DST}/${name}"
  removed_skills=$((removed_skills + 1))
done

# Agents
removed_agents=0
for agent_file in "${PLUGIN_DIR}/agents"/*.md; do
  name="$(basename "$agent_file")"
  remove_item "${AGENTS_DST}/${name}"
  removed_agents=$((removed_agents + 1))
done

# Scripts
removed_scripts=0
for script_file in "${PLUGIN_DIR}/scripts"/*.py; do
  name="$(basename "$script_file")"
  remove_item "${SCRIPTS_DST}/${name}"
  removed_scripts=$((removed_scripts + 1))
done

echo ""
echo "  ==================================="
if $DRY_RUN; then
  warn "DRY RUN complete — nothing was deleted."
else
  ok "Done: ${removed_skills} skills, ${removed_agents} agents, ${removed_scripts} scripts removed."
  echo ""
  warn "settings.json was NOT modified. Remove MCP entries manually if needed."
fi
echo ""
