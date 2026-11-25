#!/usr/bin/env python3
"""Verifica que los enlaces internos apunten a la URL canonica con slash final.

Uso:
    python scripts/test_internal_trailing_slash.py            # escanea _site si existe
    python scripts/test_internal_trailing_slash.py _site
    python scripts/test_internal_trailing_slash.py --source   # escanea fuentes

Ignora enlaces externos, anchors, assets, archivos y la raiz.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HREF_RE = re.compile(r'href=["\'](/[^"\']*)["\']')
MD_LINK_RE = re.compile(r"\]\((/[^)\s#?]*)\)")
LOC_RE = re.compile(r"<loc>https?://[^/]+(/[^<]*)</loc>")
SKIP_DIRS = {".git", ".jekyll-cache", "_site", "vendor", "node_modules", ".agents", "_planning"}


def is_file_like(path: str) -> bool:
    return bool(re.search(r"\.[A-Za-z0-9]{2,5}$", path))


def is_bad_internal(path: str) -> bool:
    if not path.startswith("/") or path.startswith("//"):
        return False
    if path == "/":
        return False
    clean = path.split("#", 1)[0].split("?", 1)[0]
    if not clean or clean == "/":
        return False
    if clean.endswith("/"):
        return False
    return not is_file_like(clean)


def scan_html(path: Path, findings: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for match in HREF_RE.finditer(text):
        url = match.group(1)
        if is_bad_internal(url):
            findings.append((str(path.relative_to(ROOT)), url))


def scan_markdown(path: Path, findings: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for match in MD_LINK_RE.finditer(text):
        url = match.group(1)
        if is_bad_internal(url):
            findings.append((str(path.relative_to(ROOT)), url))


def scan_sitemap(path: Path, findings: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for match in LOC_RE.finditer(text):
        url = match.group(1)
        if is_bad_internal(url):
            findings.append((str(path.relative_to(ROOT)), url))


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] not in ("--source",):
        target = Path(sys.argv[1])
        if not target.is_absolute():
            target = ROOT / target
        source_mode = False
    elif "--source" in sys.argv:
        target = ROOT
        source_mode = True
    else:
        site = ROOT / "_site"
        target = site if site.exists() else ROOT
        source_mode = not site.exists()

    findings: list[tuple[str, str]] = []
    if (target / "sitemap.xml").exists():
        scan_sitemap(target / "sitemap.xml", findings)

    for path in target.rglob("*"):
        if path.is_dir() or any(
            part in SKIP_DIRS or part.startswith("research_") for part in path.parts
        ):
            continue
        if path.suffix == ".html":
            scan_html(path, findings)
        elif source_mode and path.suffix in (".md", ".markdown"):
            scan_markdown(path, findings)

    if findings:
        print(f"X {len(findings)} enlace(s) interno(s) sin slash final:")
        for file, url in findings[:80]:
            print(f"  {file}: {url}")
        if len(findings) > 80:
            print(f"  ... y {len(findings) - 80} mas")
        return 1

    scope = "fuentes" if source_mode else str(target.relative_to(ROOT) if target != ROOT else ".")
    print(f"OK: sin enlaces internos sin slash final ({scope}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
