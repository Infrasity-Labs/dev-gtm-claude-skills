#!/usr/bin/env python3
"""
capture_site.py — Website capture with Playwright (on-demand)

This script runs when raw HTML analysis is insufficient (JS-heavy sites,
SPAs without SSR) or when responsive analysis needs multiple viewports.
Renders the site in a headless Chromium, attempts to dismiss common
cookie/consent banners, optionally scrolls to trigger lazy content, then
saves a full-page screenshot per viewport. Also saves the post-JavaScript
rendered HTML by default.

Basic usage:
    python capture_site.py https://example.com

Multi-viewport capture (for responsive analysis):
    python capture_site.py https://example.com \\
        --viewports desktop,tablet,mobile \\
        --output ./captures/example.png

Scroll capture (for lazy-loaded content):
    python capture_site.py https://example.com --scroll-capture

Element capture (for element mode — screenshots one element only):
    python capture_site.py https://example.com \\
        --selector "header.navbar" \\
        --output ./element.png

    With --selector, the screenshot covers only the element's bounding box and
    the saved HTML is the element's outerHTML instead of the full page.

Skip rendered-HTML output:
    python capture_site.py https://example.com --no-save-html

Requirements:
    pip install playwright
    playwright install chromium

If Playwright is not installed, the script prints the exact install command.
"""

import argparse
import sys
from pathlib import Path

# Ensure Unicode (em-dash, etc.) prints cleanly on Windows consoles whose
# default code page is cp1252.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


VIEWPORT_PRESETS = {
    "desktop": (1440, 900),
    "tablet": (768, 1024),
    "mobile": (375, 812),
}

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# Common cookie/consent banner accept-button selectors. Order matters:
# more specific / common patterns first. Each selector is tried with a
# short timeout; failures are silent.
COOKIE_ACCEPT_SELECTORS = [
    'button[id*="accept" i]',
    'button[id*="agree" i]',
    'button[id*="consent" i]',
    'button[class*="accept" i]',
    'button[class*="consent" i]',
    'button[aria-label*="accept" i]',
    'button[aria-label*="agree" i]',
    '[data-testid*="accept" i]',
    '[data-cy*="accept" i]',
    '#onetrust-accept-btn-handler',
    '.cc-accept',
    '.cc-allow',
    '.cookie-accept',
    '.gdpr-accept',
]


def check_playwright_installed():
    """Check if Playwright is available. If not, show clear instructions."""
    try:
        import playwright  # noqa: F401
        return True
    except ImportError:
        print(
            "Playwright is not installed in this environment.\n\n"
            "To install, run:\n\n"
            "    pip install playwright\n"
            "    playwright install chromium\n\n"
            "Note: the first time, Chromium weighs ~300MB. That's normal.\n"
            "Once installed, run this script again.",
            file=sys.stderr,
        )
        return False


def parse_viewport(viewport_str):
    """Convert '1440x900' into (1440, 900)."""
    try:
        w, h = viewport_str.lower().split("x")
        return int(w), int(h)
    except Exception:
        raise argparse.ArgumentTypeError(
            f"Invalid viewport: {viewport_str}. Expected format '1440x900'."
        )


def parse_viewports_list(viewports_str):
    """
    Convert 'desktop,mobile' or 'desktop,1024x768' into a list of
    (label, (width, height)) tuples. Mixes presets and custom sizes freely.
    """
    out = []
    for item in viewports_str.split(","):
        item = item.strip()
        if not item:
            continue
        if item in VIEWPORT_PRESETS:
            out.append((item, VIEWPORT_PRESETS[item]))
        else:
            try:
                w, h = item.lower().split("x")
                out.append((f"{w}x{h}", (int(w), int(h))))
            except Exception:
                raise argparse.ArgumentTypeError(
                    f"Invalid viewport spec: {item}. Use a preset "
                    f"({', '.join(VIEWPORT_PRESETS)}) or WxH (e.g. 1440x900)."
                )
    if not out:
        raise argparse.ArgumentTypeError("No viewports specified.")
    return out


def dismiss_cookie_banner(page, verbose=True):
    """
    Attempt to click a cookie/consent accept button. Silently fail if none
    match. Returns True if a click landed, False otherwise.
    """
    for selector in COOKIE_ACCEPT_SELECTORS:
        try:
            locator = page.locator(selector).first
            if locator.count() > 0 and locator.is_visible(timeout=500):
                locator.click(timeout=1000)
                if verbose:
                    print(f"   Dismissed banner via selector: {selector}")
                page.wait_for_timeout(500)
                return True
        except Exception:
            continue
    return False


def scroll_through_page(page, steps=(0.25, 0.5, 0.75, 1.0), pause_ms=400):
    """Scroll progressively to trigger lazy-loaded / intersection-observed content."""
    try:
        full_height = page.evaluate("document.body.scrollHeight")
    except Exception:
        return
    for step in steps:
        target = int(full_height * step)
        try:
            page.evaluate(f"window.scrollTo({{ top: {target}, behavior: 'instant' }})")
        except Exception:
            page.evaluate(f"window.scrollTo(0, {target})")
        page.wait_for_timeout(pause_ms)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(pause_ms)


def output_path_for_viewport(base_path: Path, label: str, total: int) -> Path:
    """
    Build the per-viewport output path. For a single viewport, return base_path
    unchanged. For multiple, insert '-<label>' before the extension.
    """
    if total == 1:
        return base_path
    stem = base_path.stem
    suffix = base_path.suffix or ".png"
    return base_path.with_name(f"{stem}-{label}{suffix}")


def capture_one(
    url,
    output_path,
    viewport,
    label,
    save_html=True,
    dismiss_cookies=True,
    scroll_capture=False,
    selector=None,
    user_agent=DEFAULT_USER_AGENT,
    wait_until="networkidle",
    timeout=30000,
):
    """Capture a single viewport. Returns the output path."""
    from playwright.sync_api import sync_playwright

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Capturing [{label}] {url}")
    print(f"   Viewport: {viewport[0]}x{viewport[1]}")
    print(f"   Wait until: {wait_until}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": viewport[0], "height": viewport[1]},
            user_agent=user_agent,
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until=wait_until, timeout=timeout)
        except Exception as e:
            print(f"   Page took longer than expected or partial load: {e}")
            print("   Continuing with what rendered so far.")

        # Small extra wait for entry animations
        page.wait_for_timeout(1000)

        if dismiss_cookies:
            dismiss_cookie_banner(page)

        if scroll_capture:
            print("   Scrolling to trigger lazy content...")
            scroll_through_page(page)

        if selector:
            locator = page.locator(selector).first
            try:
                locator.wait_for(state="visible", timeout=10000)
            except Exception:
                browser.close()
                raise RuntimeError(
                    f"Selector matched nothing visible: {selector!r}. "
                    "Try a broader selector, or capture without --selector and "
                    "analyze the element region visually."
                )
            locator.scroll_into_view_if_needed()
            page.wait_for_timeout(300)
            box = locator.bounding_box()
            if box:
                print(
                    f"   Element box: {int(box['width'])}x{int(box['height'])} "
                    f"at ({int(box['x'])}, {int(box['y'])})"
                )
            locator.screenshot(path=str(output_path))
            print(f"   Element screenshot saved: {output_path}")

            if save_html:
                html_path = output_path.with_suffix(".html")
                outer_html = locator.evaluate("el => el.outerHTML")
                html_path.write_text(outer_html, encoding="utf-8")
                print(f"   Element outerHTML saved: {html_path}")
        else:
            page.screenshot(path=str(output_path), full_page=True)
            print(f"   Screenshot saved: {output_path}")

            if save_html:
                html_path = output_path.with_suffix(".html")
                html_content = page.content()
                html_path.write_text(html_content, encoding="utf-8")
                print(f"   Rendered HTML saved: {html_path}")

        try:
            title = page.title()
            print(f"   Page title: {title}")
        except Exception:
            pass

        browser.close()

    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Capture a website with Playwright. Used when raw HTML is insufficient "
            "or when responsive analysis needs multiple viewports."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("url", help="URL of the site to capture")
    parser.add_argument(
        "--output",
        "-o",
        default="./capture.png",
        help="Output path of the PNG (default: ./capture.png). With --viewports, "
             "the viewport label is appended before the extension.",
    )
    parser.add_argument(
        "--viewports",
        type=parse_viewports_list,
        default=None,
        help=f"Comma-separated viewports (presets: {', '.join(VIEWPORT_PRESETS)}, "
             "or WxH like 1024x768). Default: just desktop.",
    )
    parser.add_argument(
        "--viewport",
        type=parse_viewport,
        default=None,
        help="Legacy single-viewport flag (WxH). Use --viewports for multi-viewport.",
    )
    parser.add_argument(
        "--save-html",
        dest="save_html",
        action="store_true",
        default=True,
        help="Also save the post-JS rendered HTML (default: on).",
    )
    parser.add_argument(
        "--no-save-html",
        dest="save_html",
        action="store_false",
        help="Skip saving the post-JS rendered HTML.",
    )
    parser.add_argument(
        "--no-dismiss-cookies",
        dest="dismiss_cookies",
        action="store_false",
        default=True,
        help="Disable the cookie/consent banner auto-dismiss attempt.",
    )
    parser.add_argument(
        "--selector",
        default=None,
        help="CSS selector for element capture: screenshot only the first matching "
             "element's bounding box and save its outerHTML instead of the full page. "
             "Used by element mode ('copy element').",
    )
    parser.add_argument(
        "--scroll-capture",
        action="store_true",
        help="Scroll through the page (25%%/50%%/75%%/100%%) before screenshot to "
             "trigger lazy-loaded content.",
    )
    parser.add_argument(
        "--user-agent",
        default=DEFAULT_USER_AGENT,
        help="Custom user-agent string (default: Mac Chrome 120).",
    )
    parser.add_argument(
        "--wait-until",
        choices=["load", "domcontentloaded", "networkidle"],
        default="networkidle",
        help="When to consider the page loaded (default: networkidle)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30000,
        help="Timeout in milliseconds (default: 30000)",
    )

    args = parser.parse_args()

    if not check_playwright_installed():
        sys.exit(2)

    if args.viewports:
        viewports = args.viewports
    elif args.viewport:
        viewports = [(f"{args.viewport[0]}x{args.viewport[1]}", args.viewport)]
    else:
        viewports = [("desktop", VIEWPORT_PRESETS["desktop"])]

    base_path = Path(args.output)
    total = len(viewports)

    try:
        for label, viewport in viewports:
            out = output_path_for_viewport(base_path, label, total)
            capture_one(
                url=args.url,
                output_path=out,
                viewport=viewport,
                label=label,
                save_html=args.save_html,
                dismiss_cookies=args.dismiss_cookies,
                scroll_capture=args.scroll_capture,
                selector=args.selector,
                user_agent=args.user_agent,
                wait_until=args.wait_until,
                timeout=args.timeout,
            )
    except Exception as e:
        print(f"Error during capture: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
