#!/usr/bin/env python3
"""
Domain Analyzer — domain_analyzer.py

Fetches and analyzes a domain to extract key terms and produce a domain context summary.

Usage:
    python domain_analyzer.py --url https://firefly.ai [--focus_keyword "cloud disaster recovery"]

Output (JSON to stdout):
{
  "domain_context": "...",
  "key_terms": ["term1", "term2", ...],
  "focus_area": "...",
  "success": true,
  "errors": []
}
"""

import argparse
import gzip
import json
import re
import sys
import urllib.request
import urllib.error
import zlib
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin


# ─── HTML parsing ─────────────────────────────────────────────────────────────

class MetaExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.description = ''
        self.h1 = ''
        self._in_title = False
        self._in_h1 = False
        self._skip_tags = {'script', 'style', 'noscript', 'head'}
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in self._skip_tags:
            self._skip_depth += 1
        if tag == 'title':
            self._in_title = True
        if tag == 'h1' and not self.h1:
            self._in_h1 = True
        if tag == 'meta':
            name = attrs_dict.get('name', '').lower()
            if name == 'description' and not self.description:
                self.description = attrs_dict.get('content', '')

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip_depth > 0:
            self._skip_depth -= 1
        if tag == 'title':
            self._in_title = False
        if tag == 'h1':
            self._in_h1 = False

    def handle_data(self, data):
        if self._skip_depth > 0:
            return
        if self._in_title and not self.title:
            self.title = data.strip()
        if self._in_h1 and not self.h1:
            self.h1 = data.strip()


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._chunks = []
        self._skip_depth = 0
        self._skip_tags = {'script', 'style', 'noscript'}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            text = data.strip()
            if text:
                self._chunks.append(text)

    def get_text(self):
        return ' '.join(self._chunks)


def extract_meta(html):
    parser = MetaExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    return parser.title, parser.description, parser.h1


def strip_html(html):
    parser = TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    return parser.get_text()


def extract_sitemap_urls(xml):
    urls = re.findall(r'<loc>\s*(https?://[^\s<]+)\s*</loc>', xml)
    return urls[:20]


# ─── Fetching ─────────────────────────────────────────────────────────────────

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; ContentBriefBot/1.0)',
    'Accept': 'text/html,application/xml,application/xhtml+xml,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
}

def fetch_url(url, timeout=8):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()

            # Decompress if the server sent gzip or deflate. Some CDNs compress
            # unconditionally regardless of Accept-Encoding, so we check the
            # response header rather than trusting the request.
            encoding = (resp.headers.get('Content-Encoding') or '').lower().strip()
            if encoding == 'gzip':
                raw = gzip.decompress(raw)
            elif encoding == 'deflate':
                # 'deflate' over HTTP is technically raw deflate, but some servers
                # send zlib-wrapped data. Try zlib decode first, fall back to raw.
                try:
                    raw = zlib.decompress(raw)
                except zlib.error:
                    raw = zlib.decompress(raw, -zlib.MAX_WBITS)

            charset = 'utf-8'
            ct = resp.headers.get('Content-Type', '')
            if 'charset=' in ct:
                charset = ct.split('charset=')[-1].strip().split(';')[0].strip()
            return raw.decode(charset, errors='replace')
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'HTTP {e.code} for {url}')
    except urllib.error.URLError as e:
        raise RuntimeError(f'URL error for {url}: {e.reason}')
    except Exception as e:
        raise RuntimeError(f'Fetch failed for {url}: {e}')


# ─── Key term extraction ──────────────────────────────────────────────────────

STOPWORDS = {
    'the', 'and', 'for', 'are', 'you', 'that', 'this', 'with', 'have', 'your',
    'from', 'they', 'will', 'can', 'our', 'not', 'all', 'use', 'was', 'but',
    'how', 'what', 'when', 'where', 'more', 'also', 'into', 'about', 'which',
    'been', 'its', 'get', 'has', 'their', 'any', 'one', 'each', 'new', 'just',
    'who', 'her', 'his', 'him', 'she', 'her', 'we', 'my', 'an', 'is', 'it',
    'of', 'to', 'in', 'a', 'at', 'by', 'on', 'or', 'as', 'if', 'be', 'do',
    'so', 'up', 'no', 'go', 'me', 'he', 'us', 'an', 'to',
    # Common 3-letter words admitted by the length>2 filter that aren't tech terms
    'see', 'way', 'via', 'let', 'now', 'too', 'why', 'out', 'off', 'own',
    'top', 'try', 'run', 'set', 'put', 'far', 'big', 'old', 'few', 'end',
    'yet', 'per', 'eg', 'ie',
}

def extract_key_terms(text, n=10):
    words = re.sub(r'[^a-z0-9\s-]', ' ', text.lower()).split()
    # len(w) > 2 keeps short technical terms (AWS, GCP, API, SDK, Go, Go, SQL, K8s, etc.).
    # Common short non-technical words are filtered by STOPWORDS above.
    words = [w for w in words if len(w) > 2 and w not in STOPWORDS]
    freq = Counter(words)
    return [word for word, count in freq.most_common(n * 2) if count >= 2][:n]


# ─── Main analysis ────────────────────────────────────────────────────────────

def pick_doc_urls(urls):
    patterns = ['/docs/', '/blog/', '/product/', '/features/', '/solutions/']
    return [u for u in urls if any(p in u.lower() for p in patterns)][:5]


def analyze(domain_url, focus_keyword=''):
    result = {
        'domain_context': '',
        'key_terms': [],
        'focus_area': '',
        'success': False,
        'errors': [],
    }

    combined_text = ''
    title = description = h1 = ''

    # 1. Homepage
    try:
        homepage_html = fetch_url(domain_url)
        title, description, h1 = extract_meta(homepage_html)
        combined_text += strip_html(homepage_html)[:5000]
    except Exception as e:
        result['errors'].append(f'Homepage fetch failed: {e}')

    # 2. Sitemap
    sitemap_urls = []
    try:
        base = domain_url.rstrip('/')
        sitemap_html = fetch_url(f'{base}/sitemap.xml')
        sitemap_urls = extract_sitemap_urls(sitemap_html)
    except Exception as e:
        result['errors'].append(f'Sitemap fetch failed: {e}')

    # 3. Crawl up to 5 doc/blog pages
    doc_urls = pick_doc_urls(sitemap_urls)
    for page_url in doc_urls:
        try:
            page_html = fetch_url(page_url)
            combined_text += ' ' + strip_html(page_html)[:2000]
        except Exception as e:
            result['errors'].append(f'Page fetch failed ({page_url}): {e}')

    if not combined_text.strip():
        result['domain_context'] = 'Domain context unavailable — domain fetch failed.'
        return result

    # 4. Extract key terms
    result['key_terms'] = extract_key_terms(combined_text)

    # 5. Infer focus area
    signals = [s for s in [title, h1, description] if s]
    result['focus_area'] = ' — '.join(signals[:2])[:200]

    # 6. Compose domain_context string
    parsed = urlparse(domain_url)
    domain = parsed.hostname.replace('www.', '') if parsed.hostname else domain_url
    key_term_str = ', '.join(result['key_terms'][:8])

    parts = []
    if result['focus_area']:
        parts.append(f"{domain} — {result['focus_area']}.")
    else:
        parts.append(f"{domain} (domain context partially unavailable).")
    if key_term_str:
        parts.append(f"Key terms: {key_term_str}.")

    result['domain_context'] = ' '.join(parts)
    result['success'] = True
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze a domain for the brief generator')
    parser.add_argument('--url', required=True, help='Domain URL to analyze')
    parser.add_argument('--focus_keyword', default='', help='Focus keyword for context')
    args = parser.parse_args()

    try:
        result = analyze(args.url, args.focus_keyword)
    except Exception as e:
        result = {
            'domain_context': 'Domain context unavailable — domain fetch failed.',
            'key_terms': [],
            'focus_area': '',
            'success': False,
            'errors': [str(e)],
        }

    print(json.dumps(result, indent=2))