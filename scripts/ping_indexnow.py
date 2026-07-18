#!/usr/bin/env python3
"""Ping IndexNow with new/updated URLs from the generated sitemap.

Reads _site/sitemap.xml, filters URLs modified within WINDOW_DAYS,
dedupes against a persistent cache, and submits the batch to IndexNow.
Covers Pulso, Editorial, Articles, Pages and any other indexed URL.
"""

import os
import sys
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(REPO_DIR, "_site", "sitemap.xml")
CACHE_FILE = os.path.join(REPO_DIR, "scripts", ".indexnow_cache.json")
KEY = "624a4302f1714f068e9851beb7b692f2"
HOST = "muchotexto.net"
ENDPOINT = "https://api.indexnow.org/indexnow"
WINDOW_DAYS = 2  # URLs modified within this window are candidates


def load_cache() -> set:
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except (OSError, json.JSONDecodeError):
        return set()


def save_cache(cache: set) -> None:
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(cache), f, ensure_ascii=False, indent=2)


def collect_candidates() -> list[str]:
    if not os.path.exists(SITEMAP):
        print(f"[IndexNow] Sitemap no encontrado: {SITEMAP}")
        return []

    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    tree = ET.parse(SITEMAP)
    root = tree.getroot()

    cutoff = datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)
    candidates = []
    for url in root.findall(f"{ns}url"):
        loc = url.find(f"{ns}loc")
        lastmod = url.find(f"{ns}lastmod")
        if loc is None or not loc.text:
            continue
        url_str = loc.text.strip()
        if lastmod is not None and lastmod.text:
            try:
                mod = datetime.fromisoformat(lastmod.text.strip())
                if mod.tzinfo is None:
                    mod = mod.replace(tzinfo=timezone.utc)
                if mod < cutoff:
                    continue
            except ValueError:
                pass
        candidates.append(url_str)
    return candidates


def ping(url_list: list[str]) -> bool:
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
        print(f"[IndexNow] Ping enviado ({len(url_list)} URLs)")
        return True
    except urllib.error.URLError as e:
        print(f"[IndexNow] Error al ping: {e.reason}")
        return False


def main() -> int:
    cache = load_cache()
    candidates = collect_candidates()
    new_urls = [u for u in candidates if u not in cache]

    if not new_urls:
        print("[IndexNow] Sin URLs nuevas para notificar")
        return 0

    if ping(new_urls):
        cache.update(new_urls)
        save_cache(cache)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
