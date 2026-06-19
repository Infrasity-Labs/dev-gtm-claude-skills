#Requires -Version 5.1
# Marketing Skills Installer for Claude Code (Windows)

function Main {
    $SkillsDir = Join-Path $env:USERPROFILE ".claude\skills"
    $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

    $Skills = @(
        "ab-testing",
        "ad-creative",
        "ads",
        "ai-seo",
        "analytics",
        "churn-prevention",
        "cold-email",
        "community-marketing",
        "competitor-profiling",
        "competitors",
        "content-strategy",
        "copywriting",
        "cro",
        "customer-research",
        "emails",
        "free-tools",
        "launch",
        "lead-magnets",
        "marketing-ideas",
        "onboarding",
        "pricing",
        "programmatic-seo",
        "referrals",
        "revops",
        "sales-enablement",
        "schema",
        "seo-audit",
        "social"
    )

    Write-Host "========================================"
    Write-Host "   Marketing Skills -- Installer"
    Write-Host "   For Claude Code"
    Write-Host "========================================"
    Write-Host ""
    Write-Host "Installing $($Skills.Count) skills to $SkillsDir\"
    Write-Host ""

    if (-not (Test-Path $SkillsDir)) {
        New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
    }

    $Installed = 0
    $Skipped = 0

    foreach ($skill in $Skills) {
        $Source = Join-Path $ScriptDir $skill
        $Dest   = Join-Path $SkillsDir $skill

        if (Test-Path $Source) {
            if (-not (Test-Path $Dest)) {
                New-Item -ItemType Directory -Path $Dest -Force | Out-Null
            }
            Copy-Item -Path "$Source\*" -Destination $Dest -Recurse -Force
            Write-Host "  OK $skill"
            $Installed++
        } else {
            Write-Host "  SKIP $skill (source not found)"
            $Skipped++
        }
    }

    Write-Host ""
    Write-Host "OK $Installed skills installed"
    if ($Skipped -gt 0) {
        Write-Host "WARN $Skipped skills skipped (source not found)"
    }
    Write-Host ""
    Write-Host "Usage (restart Claude Code first):"
    Write-Host "  /analytics          -- GA4 & conversion tracking setup"
    Write-Host "  /ads                -- Paid ads strategy"
    Write-Host "  /cold-email         -- Cold outreach sequences"
    Write-Host "  /competitor-profiling -- Research competitor URLs"
    Write-Host "  /revops             -- Lead lifecycle & CRM automation"
    Write-Host "  ... and 23 more skills"
    Write-Host ""
    Write-Host "To uninstall: .\uninstall.ps1"
}

Main
