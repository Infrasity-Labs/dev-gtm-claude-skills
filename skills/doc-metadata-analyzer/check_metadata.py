#!/usr/bin/env python3
"""Simple script to check documentation metadata."""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scripts import check_documentation_metadata


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_metadata.py <url>")
        print("Example: python check_metadata.py https://docs.python.org/3/")
        sys.exit(1)
    
    url = sys.argv[1]
    
    print(f"🔍 Checking: {url}\n")
    result = check_documentation_metadata(url)
    
    if not result.success:
        print(f"❌ Error: {result.error}")
        sys.exit(1)
    
    print("=" * 60)
    
    # Status indicator mapping
    status_map = {"ideal": "✓", "warning": "⚠️", "missing": "✗"}
    
    # Title section with status indicator
    title_icon = status_map.get(result.title.status, "✗")
    
    print(f"📄 TITLE — {title_icon} {result.title.status.upper()}")
    print(f"   Content: \"{result.title.value}\"" if result.title.value else "   Content: Not found")
    print(f"   Length: {result.title.length} chars (ideal: 50-60)")
    if result.title.issues:
        for issue in result.title.issues:
            print(f"   Issue: {issue}")
    
    # Description section with status indicator
    desc_icon = status_map.get(result.description.status, "✗")
    
    print(f"\n📝 DESCRIPTION — {desc_icon} {result.description.status.upper()}")
    print(f"   Content: \"{result.description.value}\"" if result.description.value else "   Content: Not found")
    print(f"   Length: {result.description.length} chars (ideal: 140-160)")
    if result.description.issues:
        for issue in result.description.issues:
            print(f"   Issue: {issue}")
    
    print("=" * 60)
    print("\n📊 JSON Output:")
    print(json.dumps(result.to_dict(), indent=2))


if __name__ == "__main__":
    main()
