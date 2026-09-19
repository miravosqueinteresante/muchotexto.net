#!/usr/bin/env python3
"""
build_directorio.py — genera _data/directorio.yml.

Fuente unica = seed curado (_data/directorio-seed.yml) + los `directorio`
declarados en el front matter de los articulos. Alimenta directorio.markdown
via site.data.directorio.

Fallback-safe: si falla, NO sobreescribe el snapshot y sale 0.

Uso:
    python scripts/build_directorio.py
"""

import glob
import os
import re
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = os.path.join(REPO, "_data", "directorio-seed.yml")
OUT = os.path.join(REPO, "_data", "directorio.yml")

SECCION_DEFAULT = "Otros"


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def norm(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("ascii").lower().strip()


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1) if m else ""


def article_entries():
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
        entries = data.get("directorio")
        if not entries:
            continue
        for e in entries:
            if not isinstance(e, dict):
                continue
            nombre = str(e.get("nombre", "")).strip()
            desc = str(e.get("descripcion", "")).strip()
            if not nombre or not desc:
                continue
            item = {"nombre": nombre, "descripcion": desc}
            if e.get("url"):
                item["url"] = str(e["url"]).strip()
            grouped.setdefault(str(e.get("seccion", SECCION_DEFAULT)).strip() or SECCION_DEFAULT, []).append(item)
    return grouped


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        import yaml
    except ImportError:
        print("WARN: PyYAML no disponible; se conserva _data/directorio.yml del snapshot.")
        return 0
    try:
        seed = yaml.safe_load(read(SEED)) or []
        order = [g["seccion"] for g in seed]
        grupos = {g["seccion"]: {"seccion": g["seccion"], "intro": g.get("intro", ""),
                                 "nota": g.get("nota", ""), "items": list(g.get("items") or [])}
                  for g in seed}
        existing = {(s, norm(i.get("nombre", ""))) for s, g in grupos.items() for i in g["items"]}

        for seccion, items in article_entries().items():
            if seccion not in grupos:
                grupos[seccion] = {"seccion": seccion, "intro": "", "nota": "", "items": []}
                order.append(seccion)
            for it in items:
                key = (seccion, norm(it["nombre"]))
                if key in existing:
                    continue
                grupos[seccion]["items"].append(it)
                existing.add(key)

        out = []
        for s in order:
            g = grupos[s]
            entry = {"seccion": s}
            if g.get("intro"):
                entry["intro"] = g["intro"]
            if g.get("nota"):
                entry["nota"] = g["nota"]
            entry["items"] = g["items"]
            out.append(entry)
        with open(OUT, "w", encoding="utf-8") as f:
            yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        n = sum(len(g["items"]) for g in out)
        print(f"OK: _data/directorio.yml = {len(out)} secciones, {n} items.")
        return 0
    except Exception as e:
        print(f"WARN: no se pudo generar directorio ({e}); se conserva el snapshot.")
        return 0


if __name__ == "__main__":
    sys.exit(main())