# marketing-skills-plugin installer (Windows / PowerShell)
#
# Installs 28 marketing skills into your Claude Code environment.
# No agents or shared scripts are required for this plugin — skills only.
#
# Usage:
#   .\install.ps1 [-Project] [-Force] [-DryRun] [-ConfigureMcp] [-Help]
#
# Options:
#   -Project       Install into .\.claude\ (project-level) instead of ~\.claude\
#   -Force         Overwrite existing files without prompting
#   -DryRun        Show what would be installed without making changes
#   -ConfigureMcp  Print MCP configuration instructions
#   -Help          Show this help message

param(
  [switch]$Project,
  [switch]$Force,
  [switch]$DryRun,
  [switch]$ConfigureMcp,
  [switch]$Help
)

if ($Help) {
  Get-Content $MyInvocation.MyCommand.Path | Select-Object -First 15 | ForEach-Object { $_ -replace '^# ?', '' }
  exit 0
}

$PluginDir = Split-Path -Parent $MyInvocation.MyCommand.Path

if ($Project) {
  $ClaudeHome = Join-Path $PWD ".claude"
} else {
  $ClaudeHome = Join-Path $env:USERPROFILE ".claude"
}

$SkillsDst = Join-Path $ClaudeHome "skills"

function Write-Ok   { param($msg) Write-Host "[OK] $msg" -ForegroundColor Green }
function Write-Warn { param($msg) Write-Host "[!!] $msg" -ForegroundColor Yellow }
function Write-Err  { param($msg) Write-Host "[ERR] $msg" -ForegroundColor Red }
function Write-Info { param($msg) Write-Host "[--] $msg" -ForegroundColor Cyan }

function Copy-Item-Safe {
  param($Src, $Dst)
  if (-not (Test-Path $Src)) {
    Write-Warn "Source missing, skipped: $Src"
    return
  }
  if ($DryRun) {
    Write-Host "  would install: $(Split-Path -Leaf $Src) -> $Dst"
    return
  }
  if ((Test-Path $Dst) -and -not $Force) {
    $reply = Read-Host "  Overwrite $(Split-Path -Leaf $Dst)? [y/N]"
    if ($reply -notmatch '^[yY]') {
      Write-Warn "Skipped: $(Split-Path -Leaf $Dst)"
      return
    }
  }
  if (Test-Path $Dst) { Remove-Item -Recurse -Force $Dst }
  Copy-Item -Recurse -Path $Src -Destination $Dst -Force:$Force
  Write-Ok "Installed: $(Split-Path -Leaf $Src)"
}

Write-Host ""
Write-Host "  marketing-skills-plugin installer"
Write-Host "  ==================================="
Write-Host "  skills -> $SkillsDst"
if ($DryRun) { Write-Warn "DRY RUN — no files will be written" }
Write-Host ""

# Skills (28 directories)
Write-Info "Installing 28 skills..."
if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $SkillsDst | Out-Null }
$skillCount = 0
Get-ChildItem -Path (Join-Path $PluginDir "skills") -Directory | ForEach-Object {
  Copy-Item-Safe -Src $_.FullName -Dst (Join-Path $SkillsDst $_.Name)
  $skillCount++
}
Write-Host ""

# Optional MCP configuration note
if ($ConfigureMcp -and -not $DryRun) {
  $settings = Join-Path $ClaudeHome "settings.json"
  Write-Info "MCP configuration note:"
  Write-Host "  Copy server templates from .mcp.json into $settings"
  Write-Host "  and replace `$`{ENV_VAR`} placeholders with your actual credentials."
  Write-Host "  See README.md -> Optional MCP Setup for full instructions."
  Write-Host ""
}

Write-Host "  ==================================="
if ($DryRun) {
  Write-Warn "DRY RUN complete — nothing was written."
} else {
  Write-Ok "Done: $skillCount skills installed."
}
Write-Host ""
Write-Host "  Next steps:"
Write-Host "    1. Restart Claude Code (or reload the window)"
Write-Host "    2. Run a skill:  /analytics, /ads, /copywriting, /cro ..."
Write-Host "    3. (optional) Configure MCP servers — see README.md -> Optional MCP Setup"
Write-Host ""
