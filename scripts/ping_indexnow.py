#!/usr/bin/env python3
"""Ping IndexNow with new/updated URLs from the generated sitemap.

Reads _site/sitemap.xml, compares against persistent cache (URL -> lastmod),
submits new URLs and re-submits URLs whose lastmod changed.
Runs after every Jekyll build in CI.
"""

import os
import sys
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(REPO_DIR, "_site", "sitemap.xml")
CACHE_FILE = os.path.join(REPO_DIR, "scripts", ".indexnow_cache.json")
KEY = "624a4302f1714f068e9851beb7b692f2"
HOST = "muchotexto.net"
ENDPOINT = "https://api.indexnow.org/indexnow"
BATCH_SIZE = 100  # IndexNow max is 10k, batch to avoid oversized payloads


def load_cache():
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            # Migrate old set-based cache to dict-based
            return {u: "1970-01-01T00:00:00+00:00" for u in data}
        return data
    except (OSError, json.JSONDecodeError):
        return {}


def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def collect_from_sitemap():
    """Return list of (url, lastmod_str) from sitemap."""
    if not os.path.exists(SITEMAP):
        print(f"[IndexNow] Sitemap no encontrado: {SITEMAP}")
        return []

    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    tree = ET.parse(SITEMAP)
    root = tree.getroot()

    entries = []
    for url in root.findall(f"{ns}url"):
        loc = url.find(f"{ns}loc")
        if loc is None or not loc.text:
            continue
        url_str = loc.text.strip()

        lastmod_str = "1970-01-01T00:00:00+00:00"
        lastmod = url.find(f"{ns}lastmod")
        if lastmod is not None and lastmod.text:
            lastmod_str = lastmod.text.strip()

        entries.append((url_str, lastmod_str))

    return entries


def find_changes(cache, entries, force=False):
    """Compare sitemap entries against cache. Return URLs to submit."""
    if force:
        return [url for url, _ in entries], "force"

    new_urls = []
    updated_urls = []

    for url, lastmod in entries:
        cached_mod = cache.get(url)
        if cached_mod is None:
            new_urls.append(url)
        elif lastmod > cached_mod:
            updated_urls.append(url)

    reason = ""
    if new_urls:
        reason += f"{len(new_urls)} nuevas"
    if updated_urls:
        if reason:
            reason += ", "
        reason += f"{len(updated_urls)} actualizadas"

    return new_urls + updated_urls, reason


def ping(url_list):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": url_list,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        urllib.request.urlopen(req, timeout=15)
        return True
    except urllib.error.URLError as e:
        print(f"[IndexNow] Error: {e.reason}")
        return False


def main():
    force = "--force" in sys.argv

    cache = load_cache()
    entries = collect_from_sitemap()

    if not entries:
        return 0

    to_submit, reason = find_changes(cache, entries, force=force)

    if not to_submit:
        print(f"[IndexNow] Sin cambios ({len(entries)} URLs en sitemap)")
        return 0

    print(f"[IndexNow] Enviando {len(to_submit)} URLs ({reason}, total sitemap: {len(entries)})")

    # Submit in batches
    success = True
    new_lastmod = datetime.now(timezone.utc).isoformat()
    for i in range(0, len(to_submit), BATCH_SIZE):
        batch = to_submit[i:i + BATCH_SIZE]
        if not ping(batch):
            success = False
            break
        # Cache successful batches incrementally
        for url in batch:
            # Use sitemap lastmod if available
            entry = next((e for e in entries if e[0] == url), None)
            cache[url] = entry[1] if entry else new_lastmod
        save_cache(cache)
        print(f"  Batch {i // BATCH_SIZE + 1}: {len(batch)} URLs OK")

    if success:
        print(f"[IndexNow] Completado: {len(to_submit)} URLs enviadas")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
