#!/usr/bin/env bash
#
# claude-blog runtime installer
#
# The blog skills under writing-skills/ depend on two shared resources that
# `npx skills add` (which only installs SKILL.md folders) does NOT copy:
#
#   1. 5 subagents  (agents/*.md)            -> ~/.claude/agents/
#   2. 9 shared scripts (this directory)     -> ~/.claude/scripts/
#
# Run this once after installing the blog skills so the /blog write pipeline
# (research -> write -> seo -> review) and the delivery-contract scripts work.
#
# Usage:
#   ./scripts/claude-blog-install.sh [--project] [--force] [--dry-run] [--help]
#
# Options:
#   --project   Install into ./.claude/ (project-level) instead of ~/.claude/
#   --force     Overwrite existing files without prompting
#   --dry-run   Show what would be installed without making changes
#   --help      Show this help message

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

ok()   { echo -e "${GREEN}[OK]${NC} $*"; }
warn() { echo -e "${YELLOW}[!!]${NC} $*"; }
err()  { echo -e "${RED}[ERR]${NC} $*" >&2; }

usage() {
  sed -n '3,21p' "$0" | sed 's/^# \{0,1\}//'
}

# Whitelist of the 9 shared blog runtime scripts. Explicit so this installer
# never copies the multi-tool converter scripts (install.sh, convert.sh,
# sync-*.py, *-install.sh) that also live in scripts/.
BLOG_SCRIPTS=(
  analyze_blog.py
  blog_preflight.py
  blog_render.py
  cognitive_load.py
  discourse_research.py
  generate_hero.py
  lint_prose.py
  load_untrusted_root.py
  sync_flow.py
)

PROJECT=false
FORCE=false
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) PROJECT=true; shift ;;
    --force)   FORCE=true; shift ;;
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

AGENTS_DST="${CLAUDE_HOME}/agents"
SCRIPTS_DST="${CLAUDE_HOME}/scripts"

# copy_file <src> <dst>: respects --dry-run and --force/prompt on overwrite.
copy_file() {
  local src="$1" dst="$2"
  if [[ ! -f "$src" ]]; then
    warn "Source missing, skipped: $src"
    return 0
  fi
  if $DRY_RUN; then
    echo "  would copy $(basename "$src") -> $dst"
    return 0
  fi
  if [[ -e "$dst" ]] && ! $FORCE; then
    printf "Overwrite existing %s? [y/N]: " "$dst"
    read -r reply
    case "$reply" in
      y|Y|yes|YES) ;;
      *) warn "Skipped $dst"; return 0 ;;
    esac
  fi
  cp "$src" "$dst"
  ok "Installed $(basename "$src") -> $dst"
}

echo ""
echo "claude-blog runtime installer"
echo "  agents  -> ${AGENTS_DST}"
echo "  scripts -> ${SCRIPTS_DST}"
$DRY_RUN && warn "DRY RUN — no files will be written"
echo ""

# 1. Agents
if [[ ! -d "${REPO_ROOT}/agents" ]]; then
  err "No agents/ directory at repo root (${REPO_ROOT}/agents). Are you running from the repo?"
  exit 1
fi
$DRY_RUN || mkdir -p "$AGENTS_DST"
agent_count=0
for agent in "${REPO_ROOT}"/agents/*.md; do
  [[ -e "$agent" ]] || continue
  copy_file "$agent" "${AGENTS_DST}/$(basename "$agent")"
  agent_count=$((agent_count + 1))
done

echo ""

# 2. Shared scripts (whitelist only)
$DRY_RUN || mkdir -p "$SCRIPTS_DST"
script_count=0
for name in "${BLOG_SCRIPTS[@]}"; do
  copy_file "${SCRIPT_DIR}/${name}" "${SCRIPTS_DST}/${name}"
  script_count=$((script_count + 1))
done

echo ""
ok "Done: ${agent_count} agents, ${script_count} scripts targeted."
echo ""
echo "Next steps:"
echo "  1. Install Python deps:   pip install -r writing-skills/requirements.txt"
echo "  2. (optional) Image/audio: export GOOGLE_AI_API_KEY=... and configure nanobanana MCP"
echo "  3. Run a skill:            /blog write \"your topic\""
