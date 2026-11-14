#!/usr/bin/env python3
"""Conteos canónicos del sitio. Read-only.

Universos distintos que no deben mezclarse:
- posts: todos los archivos de _posts/
- articulos: posts con categories: articulos
- con_pilar: articulos con pilar 1-5
- analisis: con_pilar menos NON_ANALYSIS (bienvenida y fútbol)

Uso:
    python scripts/site_counts.py
    python scripts/site_counts.py --json
"""

import glob
import json
import os
import re
import sys

import yaml

from common import read

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(REPO, "_posts")

NON_ANALYSIS = {
    "2026-05-10-primer-articulo",
    "2026-06-10-que-es-realmente-el-futbol",
}


def front_matter(path):
    text = read(path)
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def counts():
    posts = sorted(glob.glob(os.path.join(POSTS, "*.md")))
    articulos = 0
    con_pilar = 0
    analisis = 0
    for path in posts:
        data = front_matter(path)
        categories = data.get("categories") or []
        if isinstance(categories, str):
            categories = [categories]
        if "articulos" not in categories:
            continue
        articulos += 1
        slug = os.path.basename(path)[:-3]
        if data.get("pilar"):
            con_pilar += 1
            if slug not in NON_ANALYSIS:
                analisis += 1
    return {
        "posts": len(posts),
        "articulos": articulos,
        "con_pilar": con_pilar,
        "analisis": analisis,
    }


def main():
    data = counts()
    if "--json" in sys.argv:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"posts: {data['posts']}")
        print(f"articulos: {data['articulos']}")
        print(f"con_pilar: {data['con_pilar']}")
        print(f"analisis: {data['analisis']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
