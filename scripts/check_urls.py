#!/usr/bin/env python3
"""
check_urls.py - Verifica que las URLs en la seccion Fuentes de un articulo respondan.
Uso: python scripts/check_urls.py _posts/2026-07-16-slug.md
"""

import re
import sys
import urllib.request
import urllib.error
import ssl

TIMEOUT = 15

def extract_urls(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    urls = re.findall(r'\((https?://[^\)]+)\)', content)
    # Filter out internal links
    urls = [u for u in urls if 'muchotexto.net' not in u]
    return urls

def check_url(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; muchotexto-audit/1.0)'
    })
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERROR: {type(e).__name__}"

def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/check_urls.py _posts/2026-07-16-slug.md")
        sys.exit(1)

    filepath = sys.argv[1]
    urls = extract_urls(filepath)
    if not urls:
        print("No se encontraron URLs externas.")
        sys.exit(0)

    broken = []
    for url in urls:
        status = check_url(url)
        symbol = "OK" if status == 200 else "!!"
        print(f"  [{symbol}] {status} - {url[:80]}")
        if status != 200:
            broken.append((url, status))

    if broken:
        print(f"\n{len(broken)} URL(s) no responden 200:")
        for url, status in broken:
            print(f"  {status}: {url}")
        sys.exit(1)
    else:
        print(f"\nTodas las {len(urls)} URLs responden OK.")

if __name__ == "__main__":
    main()
