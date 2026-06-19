#!/usr/bin/env bash
set -euo pipefail

# Marketing Skills Installer for Claude Code
# Wraps everything in main() to prevent partial execution on network failure

main() {
    SKILLS_DIR="${HOME}/.claude/skills"
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

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
    echo "║   Marketing Skills — Installer       ║"
    echo "║   For Claude Code                    ║"
    echo "════════════════════════════════════════"
    echo ""
    echo "Installing ${#SKILLS[@]} skills to ${SKILLS_DIR}/"
    echo ""

    mkdir -p "${SKILLS_DIR}"

    INSTALLED=0
    SKIPPED=0

    for skill in "${SKILLS[@]}"; do
        if [ -d "${SCRIPT_DIR}/${skill}" ]; then
            mkdir -p "${SKILLS_DIR}/${skill}"
            cp -r "${SCRIPT_DIR}/${skill}/." "${SKILLS_DIR}/${skill}/"
            echo "  ✓ ${skill}"
            INSTALLED=$((INSTALLED + 1))
        else
            echo "  ⚠  ${skill} not found in ${SCRIPT_DIR} (skipped)"
            SKIPPED=$((SKIPPED + 1))
        fi
    done

    echo ""
    echo "✓ ${INSTALLED} skills installed"
    [ "${SKIPPED}" -gt 0 ] && echo "⚠  ${SKIPPED} skills skipped (source not found)"
    echo ""
    echo "Usage (restart Claude Code first):"
    echo "  /analytics         — GA4 & conversion tracking setup"
    echo "  /ads               — Paid ads strategy"
    echo "  /cold-email        — Cold outreach sequences"
    echo "  /competitor-profiling — Research competitor URLs"
    echo "  /revops            — Lead lifecycle & CRM automation"
    echo "  /cro               — Conversion rate optimization"
    echo "  /emails            — Email drip campaigns"
    echo "  /launch            — Product launch playbooks"
    echo "  ... and 20 more skills"
    echo ""
    echo "To uninstall: ./uninstall.sh"
}

main "$@"
