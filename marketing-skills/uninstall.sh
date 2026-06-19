#!/usr/bin/env bash
set -euo pipefail

# Marketing Skills Uninstaller for Claude Code

main() {
    SKILLS_DIR="${HOME}/.claude/skills"

    SKILLS=(
        ab-testing
        ad-creative
        ads
        ai-seo
        analytics
        churn-prevention
        cold-email
        community-marketing
        competitor-profiling
        competitors
        content-strategy
        copywriting
        cro
        customer-research
        emails
        free-tools
        launch
        lead-magnets
        marketing-ideas
        onboarding
        pricing
        programmatic-seo
        referrals
        revops
        sales-enablement
        schema
        seo-audit
        social
    )

    echo "════════════════════════════════════════"
    echo "║   Marketing Skills — Uninstaller     ║"
    echo "║   For Claude Code                    ║"
    echo "════════════════════════════════════════"
    echo ""

    REMOVED=0
    NOT_FOUND=0

    for skill in "${SKILLS[@]}"; do
        TARGET="${SKILLS_DIR}/${skill}"
        if [ -d "${TARGET}" ]; then
            rm -rf "${TARGET}"
            echo "  ✓ removed ${skill}"
            REMOVED=$((REMOVED + 1))
        else
            echo "  — ${skill} not installed (skipped)"
            NOT_FOUND=$((NOT_FOUND + 1))
        fi
    done

    echo ""
    echo "✓ ${REMOVED} skills removed"
    [ "${NOT_FOUND}" -gt 0 ] && echo "  ${NOT_FOUND} skills were not installed"
    echo ""
    echo "Marketing skills uninstalled. Restart Claude Code for changes to take effect."
}

main "$@"
