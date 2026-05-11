#!/usr/bin/env python3
"""Simple script to check documentation metadata."""

import sys
import json
from doc_metadata_analyzer.checker import MetadataChecker


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_metadata.py <url>")
        print("Example: python check_metadata.py https://docs.python.org/3/")
        sys.exit(1)
    
    url = sys.argv[1]
    checker = MetadataChecker()
    
    print(f"🔍 Checking: {url}\n")
    result = checker.check_url(url)
    
    if not result.success:
        print(f"❌ Error: {result.error}")
        sys.exit(1)
    
    print("=" * 60)
    print(f"📄 TITLE: {result.title.value or 'Missing'}")
    print(f"   Length: {result.title.length} chars")
    print(f"   Status: {result.title.status.upper()}")
    if result.title.issues:
        for issue in result.title.issues:
            print(f"   ⚠️  {issue}")
    
    print(f"\n📝 DESCRIPTION: {result.description.value or 'Missing'}")
    print(f"   Length: {result.description.length} chars")
    print(f"   Status: {result.description.status.upper()}")
    if result.description.issues:
        for issue in result.description.issues:
            print(f"   ⚠️  {issue}")
    
    print("=" * 60)
    print("\n📊 JSON Output:")
    print(json.dumps(result.to_dict(), indent=2))


if __name__ == "__main__":
    main()
