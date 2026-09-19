#!/usr/bin/env python3
"""
build_derived.py — motor unico para las superficies derivadas del observatorio.

Cuatro superficies comparten el mismo patron: un seed curado en
`_data/<nombre>-seed.yml` + lo que los articulos declaran en su front matter
-> `_data/<nombre>.yml`, que las paginas consumen via `site.data.<nombre>`.

    cronologia  <- front matter `hitos`       (seccion por anio)
    glosario    <- front matter `glosario`    (seccion = tema)
    casos       <- front matter `casos`       (seccion = tema)
    directorio  <- front matter `directorio`  (seccion = seccion)

Fallback-safe: si una superficie falla, conserva su snapshot y sale 0.

Uso:
    python scripts/build_derived.py              # todas
    python scripts/build_derived.py glosario     # una
"""

import glob
import os
import re
import sys
import unicodedata
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "_data")
POSTS = os.path.join(REPO, "_posts")

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


# ── helpers ──────────────────────────────────────────────────────────────
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


def fmt_fecha(iso):
    try:
        d = datetime.strptime(iso, "%Y-%m-%d")
        return f"{d.day} {MESES[d.month - 1].capitalize()} {d.year}"
    except ValueError:
        return iso


def seccion_por_anio(year):
    if year <= 2009:
        return "1973 — 2009"
    if year <= 2019:
        return "2010 — 2019"
    if year <= 2023:
        return "2020 — 2023"
    if year == 2024:
        return "2024"
    if year == 2025:
        return "2025"
    return "2026"


# ── transforms: item del front matter -> (seccion, item) ─────────────────
def _hito(it, ctx):
    fecha = str(it.get("fecha", "")).strip()
    texto = str(it.get("texto", "")).strip()
    if not fecha or not texto:
        return None
    extra = f" [Leer análisis]({ctx['url']})" if ctx["url"] else ""
    if it.get("futuro"):
        return "Lo que viene", {"orden": "9999", "fecha": fmt_fecha(fecha), "texto": texto + extra}
    year = int(fecha[:4]) if re.match(r"\d{4}", fecha) else 9999
    return seccion_por_anio(year), {"orden": fecha, "fecha": fmt_fecha(fecha), "texto": texto + extra}


def _glosario(it, ctx):
    termino = str(it.get("termino", "")).strip()
    defin = str(it.get("definicion", "")).strip()
    if not termino or not defin:
        return None
    tema = str(it.get("tema", "Del observatorio")).strip() or "Del observatorio"
    item = {"termino": termino, "definicion": defin}
    if it.get("link"):
        item["link"] = str(it["link"]).strip()
        item["link_text"] = str(it.get("link_text", "")).strip()
    return tema, item


def _caso(it, ctx):
    texto = str(it.get("texto", "")).strip()
    if not texto:
        return None
    tema = str(it.get("tema", "Del observatorio")).strip() or "Del observatorio"
    item = {"titulo": str(it.get("titulo", "") or ctx["title"]).strip(), "texto": texto}
    if ctx["url"]:
        item["url"] = ctx["url"]
    return tema, item


def _directorio(it, ctx):
    nombre = str(it.get("nombre", "")).strip()
    desc = str(it.get("descripcion", "")).strip()
    if not nombre or not desc:
        return None
    seccion = str(it.get("seccion", "Otros")).strip() or "Otros"
    item = {"nombre": nombre, "descripcion": desc}
    if it.get("url"):
        item["url"] = str(it["url"]).strip()
    return seccion, item


# ── configuracion por superficie ─────────────────────────────────────────
SURFACES = {
    "cronologia": {
        "seed": "cronologia-seed.yml", "out": "cronologia.yml",
        "section_key": "seccion", "item_key": "items", "article_field": "hitos",
        "transform": _hito, "dedup": None,
        "sort": lambda it: str(it.get("orden") or "9999"),
    },
    "glosario": {
        "seed": "glosario-seed.yml", "out": "glosario.yml",
        "section_key": "tema", "item_key": "terminos", "article_field": "glosario",
        "transform": _glosario,
        "dedup": lambda s, it: (s, norm(it.get("termino", ""))),
        "sort": None,
    },
    "casos": {
        "seed": "casos-seed.yml", "out": "casos.yml",
        "section_key": "tema", "item_key": "casos", "article_field": "casos",
        "transform": _caso,
        "dedup": lambda s, it: (s, norm(it.get("titulo", ""))),
        "sort": None,
    },
    "directorio": {
        "seed": "directorio-seed.yml", "out": "directorio.yml",
        "section_key": "seccion", "item_key": "items", "article_field": "directorio",
        "transform": _directorio,
        "dedup": lambda s, it: (s, norm(it.get("nombre", ""))),
        "sort": None,
    },
}


def iter_article_items(cfg):
    """Genera (seccion, item) desde el front matter de los articulos."""
    import yaml
    field = cfg["article_field"]
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        fm = parse_front_matter(read(path))
        if not fm:
            continue
        try:
            data = yaml.safe_load(fm) or {}
        except Exception:
            continue
        items = data.get(field)
        if not items:
            continue
        ctx = {"url": slug_to_url(path), "title": str(data.get("title", "")).strip()}
        for it in items:
            if not isinstance(it, dict):
                continue
            res = cfg["transform"](it, ctx)
            if res:
                yield res


def build_surface(name, yaml):
    cfg = SURFACES[name]
    seed = yaml.safe_load(read(os.path.join(DATA, cfg["seed"]))) or []
    sec = cfg["section_key"]
    ikey = cfg["item_key"]

    groups = {g[sec]: dict(g) for g in seed}
    order = [g[sec] for g in seed]
    existing = set()
    if cfg["dedup"]:
        for s, g in groups.items():
            for it in (g.get(ikey) or []):
                existing.add(cfg["dedup"](s, it))

    for section, item in iter_article_items(cfg):
        if section not in groups:
            groups[section] = {sec: section, ikey: []}
            order.append(section)
        key = cfg["dedup"](section, item) if cfg["dedup"] else None
        if key is not None and key in existing:
            continue
        groups[section].setdefault(ikey, []).append(item)
        if key is not None:
            existing.add(key)

    out = []
    for s in order:
        g = groups[s]
        entry = {sec: s}
        if g.get("intro"):
            entry["intro"] = g["intro"]
        if g.get("nota"):
            entry["nota"] = g["nota"]
        items = g.get(ikey) or []
        if cfg["sort"]:
            items = sorted(items, key=cfg["sort"])
        entry[ikey] = items
        out.append(entry)

    with open(os.path.join(DATA, cfg["out"]), "w", encoding="utf-8") as f:
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    n = sum(len(g[ikey]) for g in out)
    return len(out), n


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        import yaml
    except ImportError:
        print("WARN: PyYAML no disponible; se conservan los snapshots.")
        return 0

    names = [a for a in sys.argv[1:] if a in SURFACES] or list(SURFACES)
    for name in names:
        try:
            secs, items = build_surface(name, yaml)
            print(f"OK: _data/{SURFACES[name]['out']} = {secs} secciones, {items} items.")
        except Exception as e:
            print(f"WARN: no se pudo generar '{name}' ({e}); se conserva el snapshot.")
    return 0


if __name__ == "__main__":
    sys.exit(main())