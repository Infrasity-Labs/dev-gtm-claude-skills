# writing-skills-plugin installer (Windows / PowerShell)
#
# Installs 34 blog/writing skills, 5 sub-agents, and 9 shared runtime scripts
# into your Claude Code environment.
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

$SkillsDst  = Join-Path $ClaudeHome "skills"
$AgentsDst  = Join-Path $ClaudeHome "agents"
$ScriptsDst = Join-Path $ClaudeHome "scripts"

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
  if (Test-Path $Src -PathType Container) {
    if (Test-Path $Dst) { Remove-Item -Recurse -Force $Dst }
    Copy-Item -Recurse -Path $Src -Destination $Dst -Force:$Force
  } else {
    Copy-Item -Path $Src -Destination $Dst -Force:$Force
  }
  Write-Ok "Installed: $(Split-Path -Leaf $Src)"
}

Write-Host ""
Write-Host "  writing-skills-plugin installer"
Write-Host "  ================================"
Write-Host "  skills  -> $SkillsDst"
Write-Host "  agents  -> $AgentsDst"
Write-Host "  scripts -> $ScriptsDst"
if ($DryRun) { Write-Warn "DRY RUN — no files will be written" }
Write-Host ""

# 1. Skills (34 directories)
Write-Info "Installing 34 skills..."
if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $SkillsDst | Out-Null }
$skillCount = 0
Get-ChildItem -Path (Join-Path $PluginDir "skills") -Directory | ForEach-Object {
  Copy-Item-Safe -Src $_.FullName -Dst (Join-Path $SkillsDst $_.Name)
  $skillCount++
}
Write-Host ""

# 2. Agents (5 files)
Write-Info "Installing 5 blog agents..."
if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $AgentsDst | Out-Null }
$agentCount = 0
Get-ChildItem -Path (Join-Path $PluginDir "agents") -Filter "*.md" | ForEach-Object {
  Copy-Item-Safe -Src $_.FullName -Dst (Join-Path $AgentsDst $_.Name)
  $agentCount++
}
Write-Host ""

# 3. Shared scripts (9 files)
Write-Info "Installing 9 shared runtime scripts..."
if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $ScriptsDst | Out-Null }
$scriptCount = 0
Get-ChildItem -Path (Join-Path $PluginDir "scripts") -Filter "*.py" | ForEach-Object {
  Copy-Item-Safe -Src $_.FullName -Dst (Join-Path $ScriptsDst $_.Name)
  $scriptCount++
}
Write-Host ""

# 4. Python dependencies
if (-not $DryRun) {
  Write-Info "Installing Python dependencies..."
  $reqFile = Join-Path $PluginDir "requirements.txt"
  if (Get-Command pip -ErrorAction SilentlyContinue) {
    pip install -q -r $reqFile
    Write-Ok "Python deps installed"
  } else {
    Write-Warn "pip not found — install manually: pip install -r requirements.txt"
  }
  Write-Host ""
}

# 5. Optional MCP configuration note
if ($ConfigureMcp -and -not $DryRun) {
  $settings = Join-Path $ClaudeHome "settings.json"
  Write-Info "MCP configuration note:"
  Write-Host "  Copy server templates from .mcp.json into $settings"
  Write-Host "  and replace `$`{ENV_VAR`} placeholders with your actual credentials."
  Write-Host "  See README.md -> Optional MCP Setup for full instructions."
  Write-Host ""
}

# Summary
Write-Host "  ================================"
if ($DryRun) {
  Write-Warn "DRY RUN complete — nothing was written."
} else {
  Write-Ok "Done: $skillCount skills, $agentCount agents, $scriptCount scripts installed."
}
Write-Host ""
Write-Host "  Next steps:"
Write-Host "    1. Restart Claude Code (or reload the window)"
Write-Host "    2. Run a skill:  /blog write `"your topic here`""
Write-Host "    3. (optional) Audio / Image: set GOOGLE_AI_API_KEY and configure nanobanana MCP"
Write-Host "    4. (optional) Google APIs:   follow README.md -> Google API Setup"
Write-Host ""
