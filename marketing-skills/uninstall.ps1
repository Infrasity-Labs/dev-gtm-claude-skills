#Requires -Version 5.1
# Marketing Skills Uninstaller for Claude Code (Windows)

function Main {
    $SkillsDir = Join-Path $env:USERPROFILE ".claude\skills"

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
    Write-Host "   Marketing Skills -- Uninstaller"
    Write-Host "   For Claude Code"
    Write-Host "========================================"
    Write-Host ""

    $Removed  = 0
    $NotFound = 0

    foreach ($skill in $Skills) {
        $Target = Join-Path $SkillsDir $skill
        if (Test-Path $Target) {
            Remove-Item -Path $Target -Recurse -Force
            Write-Host "  OK removed $skill"
            $Removed++
        } else {
            Write-Host "  -- $skill not installed (skipped)"
            $NotFound++
        }
    }

    Write-Host ""
    Write-Host "OK $Removed skills removed"
    if ($NotFound -gt 0) {
        Write-Host "   $NotFound skills were not installed"
    }
    Write-Host ""
    Write-Host "Marketing skills uninstalled. Restart Claude Code for changes to take effect."
}

Main
