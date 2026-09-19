#!/usr/bin/env python3
"""
build_glosario.py — genera _data/glosario.yml.

Fuente unica de terminos = seed curado (_data/glosario-seed.yml) + los
`glosario` declarados en el front matter de los articulos. Alimenta
glosario.markdown via site.data.glosario.

Fallback-safe: si falla, NO sobreescribe el snapshot y sale 0.

Uso:
    python scripts/build_glosario.py
"""

import glob
import os
import re
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = os.path.join(REPO, "_data", "glosario-seed.yml")
OUT = os.path.join(REPO, "_data", "glosario.yml")

TEMA_DEFAULT = "Del observatorio"


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def norm(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("ascii").lower().strip()


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1) if m else ""


def article_terms():
    """{tema: [ {termino, definicion, link, link_text} ]} desde los articulos."""
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
        terms = data.get("glosario")
        if not terms:
            continue
        for t in terms:
            if not isinstance(t, dict):
                continue
            termino = str(t.get("termino", "")).strip()
            definicion = str(t.get("definicion", "")).strip()
            if not termino or not definicion:
                continue
            item = {"termino": termino, "definicion": definicion}
            if t.get("link"):
                item["link"] = str(t["link"]).strip()
                item["link_text"] = str(t.get("link_text", "")).strip()
            grouped.setdefault(str(t.get("tema", TEMA_DEFAULT)).strip(), []).append(item)
    return grouped


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        import yaml
    except ImportError:
        print("WARN: PyYAML no disponible; se conserva _data/glosario.yml del snapshot.")
        return 0
    try:
        seed = yaml.safe_load(read(SEED)) or []
        order = [g["tema"] for g in seed]
        grupos = {g["tema"]: list(g.get("terminos") or []) for g in seed}
        existing = {norm(t.get("termino", "")) for items in grupos.values() for t in items}

        for tema, terms in article_terms().items():
            if tema not in grupos:
                grupos[tema] = []
                order.append(tema)
            for t in terms:
                if norm(t["termino"]) in existing:
                    continue
                grupos[tema].append(t)
                existing.add(norm(t["termino"]))

        out = [{"tema": t, "terminos": grupos[t]} for t in order]
        with open(OUT, "w", encoding="utf-8") as f:
            yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        n = sum(len(g["terminos"]) for g in out)
        print(f"OK: _data/glosario.yml = {len(out)} temas, {n} terminos.")
        return 0
    except Exception as e:
        print(f"WARN: no se pudo generar glosario ({e}); se conserva el snapshot.")
        return 0


if __name__ == "__main__":
    sys.exit(main())