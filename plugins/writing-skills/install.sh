#!/usr/bin/env bash
#
# writing-skills-plugin installer
#
# Installs 34 blog/writing skills, 5 sub-agents, and 9 shared runtime scripts
# into your Claude Code environment.
#
# Usage:
#   ./install.sh [--project] [--force] [--dry-run] [--configure-mcp] [--help]
#
# Options:
#   --project        Install into ./.claude/ (project-level) instead of ~/.claude/
#   --force          Overwrite existing files without prompting
#   --dry-run        Show what would be installed without making changes
#   --configure-mcp  Append optional MCP server templates to settings.json
#   --help           Show this help message

set -euo pipefail

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${PLUGIN_DIR}/../.." && pwd)"

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
  sed -n '3,14p' "$0" | sed 's/^# \{0,1\}//'
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
AGENTS_DST="${CLAUDE_HOME}/agents"
SCRIPTS_DST="${CLAUDE_HOME}/scripts"

# copy_item <src> <dst>: copies file or directory, respects --dry-run and --force.
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
  if [[ -d "$src" ]]; then
    cp -r "$src" "$dst"
  else
    cp "$src" "$dst"
  fi
  ok "Installed: $(basename "$src")"
}

echo ""
echo "  writing-skills-plugin installer"
echo "  ================================"
echo "  skills  -> ${SKILLS_DST}"
echo "  agents  -> ${AGENTS_DST}"
echo "  scripts -> ${SCRIPTS_DST}"
$DRY_RUN && warn "DRY RUN — no files will be written"
echo ""

# 1. Skills (34 directories)
info "Installing 34 skills..."
$DRY_RUN || mkdir -p "$SKILLS_DST"
skill_count=0
for skill_dir in "${PLUGIN_DIR}"/*/; do
  [[ -d "$skill_dir" ]] || continue
  # Skip non-skill directories
  [[ -f "${skill_dir}/SKILL.md" ]] || continue
  name="$(basename "$skill_dir")"
  copy_item "$skill_dir" "${SKILLS_DST}/${name}"
  skill_count=$((skill_count + 1))
done
echo ""

# 2. Agents (5 files) — sourced from repo root agents/
info "Installing 5 blog agents..."
$DRY_RUN || mkdir -p "$AGENTS_DST"
agent_count=0
for agent in blog-writer.md blog-researcher.md blog-reviewer.md blog-seo.md blog-translator.md; do
  copy_item "${REPO_ROOT}/agents/${agent}" "${AGENTS_DST}/${agent}"
  agent_count=$((agent_count + 1))
done
echo ""

# 3. Shared scripts (9 files) — sourced from repo root scripts/
info "Installing 9 shared runtime scripts..."
$DRY_RUN || mkdir -p "$SCRIPTS_DST"
script_count=0
for script in analyze_blog.py blog_preflight.py blog_render.py cognitive_load.py discourse_research.py generate_hero.py lint_prose.py load_untrusted_root.py sync_flow.py; do
  copy_item "${REPO_ROOT}/scripts/${script}" "${SCRIPTS_DST}/${script}"
  script_count=$((script_count + 1))
done
echo ""

# 4. Python dependencies
if ! $DRY_RUN; then
  info "Installing Python dependencies..."
  if command -v pip3 &>/dev/null; then
    pip3 install -q -r "${PLUGIN_DIR}/requirements.txt" && ok "Python deps installed"
  elif command -v pip &>/dev/null; then
    pip install -q -r "${PLUGIN_DIR}/requirements.txt" && ok "Python deps installed"
  else
    warn "pip not found — install manually: pip install -r requirements.txt"
  fi
  echo ""
fi

# 5. Optional MCP configuration
if $CONFIGURE_MCP && ! $DRY_RUN; then
  SETTINGS="${CLAUDE_HOME}/settings.json"
  info "MCP configuration note:"
  echo "  Copy the server templates from .mcp.json into ${SETTINGS}"
  echo "  and replace \${ENV_VAR} placeholders with your actual credentials."
  echo "  See README.md -> Optional MCP Setup for full instructions."
  echo ""
fi

# Summary
echo "  ================================"
if $DRY_RUN; then
  warn "DRY RUN complete — nothing was written."
else
  ok "Done: ${skill_count} skills, ${agent_count} agents, ${script_count} scripts installed."
fi
echo ""
echo "  Next steps:"
echo "    1. Restart Claude Code (or reload the window)"
echo "    2. Run a skill:  /blog write \"your topic here\""
echo "    3. (optional) Audio / Image: export GOOGLE_AI_API_KEY=... and configure nanobanana MCP"
echo "    4. (optional) Google APIs:   follow README.md -> Google API Setup"
echo ""
