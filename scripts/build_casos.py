#!/usr/bin/env python3
"""
build_casos.py — genera _data/casos.yml.

Fuente unica de casos de uso = seed curado (_data/casos-seed.yml) + los `casos`
declarados en el front matter de los articulos. Alimenta casos-de-uso.markdown
via site.data.casos. Los casos de articulos toman la URL del propio articulo y,
si no se da `titulo`, el titulo del articulo.

Fallback-safe: si falla, NO sobreescribe el snapshot y sale 0.

Uso:
    python scripts/build_casos.py
"""

import glob
import os
import re
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = os.path.join(REPO, "_data", "casos-seed.yml")
OUT = os.path.join(REPO, "_data", "casos.yml")

TEMA_DEFAULT = "Del observatorio"


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def norm(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("ascii").lower().strip()


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1) if m else ""


def slug_to_url(path):
    base = os.path.basename(path)[:-3]
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)$", base)
    if not m:
        return None
    y, mo, d, slug = m.groups()
    return f"/articulos/{y}/{mo}/{d}/{slug}/"


def article_casos():
    import yaml
    grouped = {}
    for path in sorted(glob.glob(os.path.join(REPO, "_posts", "*.md"))):
        fm = parse_front_matter(read(path))
        if not fm:
            continue
        try:
            data = yaml.safe_load(fm) or {}
        except Exception:
            continue
        casos = data.get("casos")
        if not casos:
            continue
        url = slug_to_url(path)
        title = str(data.get("title", "")).strip()
        for c in casos:
            if not isinstance(c, dict):
                continue
            texto = str(c.get("texto", "")).strip()
            if not texto:
                continue
            tema = str(c.get("tema", TEMA_DEFAULT)).strip() or TEMA_DEFAULT
            item = {"titulo": str(c.get("titulo", "") or title).strip(), "texto": texto}
            if url:
                item["url"] = url
            grouped.setdefault(tema, []).append(item)
    return grouped


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        import yaml
    except ImportError:
        print("WARN: PyYAML no disponible; se conserva _data/casos.yml del snapshot.")
        return 0
    try:
        seed = yaml.safe_load(read(SEED)) or []
        order = [g["tema"] for g in seed]
        grupos = {g["tema"]: list(g.get("casos") or []) for g in seed}
        existing = {(tema, norm(c.get("titulo", ""))) for tema, items in grupos.items() for c in items}

        for tema, casos in article_casos().items():
            if tema not in grupos:
                grupos[tema] = []
                order.append(tema)
            for c in casos:
                key = (tema, norm(c["titulo"]))
                if key in existing:
                    continue
                grupos[tema].append(c)
                existing.add(key)

        out = [{"tema": t, "casos": grupos[t]} for t in order]
        with open(OUT, "w", encoding="utf-8") as f:
            yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        n = sum(len(g["casos"]) for g in out)
        print(f"OK: _data/casos.yml = {len(out)} temas, {n} casos.")
        return 0
    except Exception as e:
        print(f"WARN: no se pudo generar casos ({e}); se conserva el snapshot.")
        return 0


if __name__ == "__main__":
    sys.exit(main())