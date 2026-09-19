#!/usr/bin/env python3
"""
build_cronologia.py — genera _data/cronologia.yml.

Fuente unica de hitos = seed curado (_data/cronologia-seed.yml) + los `hitos`
declarados en el front matter de los articulos. El resultado alimenta
cronologia.markdown via site.data.cronologia.

Diseno fallback-safe (como sync_datos.py): si falla, NO sobreescribe el
snapshot commiteado y sale 0 -> el build nunca se rompe.

Uso:
    python scripts/build_cronologia.py
"""

import glob
import os
import re
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = os.path.join(REPO, "_data", "cronologia-seed.yml")
OUT = os.path.join(REPO, "_data", "cronologia.yml")

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


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


def fmt_fecha(iso):
    """'2026-09-17' -> '17 Septiembre 2026'."""
    try:
        d = datetime.strptime(iso, "%Y-%m-%d")
        return f"{d.day} {MESES[d.month - 1].capitalize()} {d.year}"
    except ValueError:
        return iso


def slug_to_url(path):
    """_posts/2026-09-16-slug.md -> /articulos/2026/09/16/slug/."""
    base = os.path.basename(path)[:-3]
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)$", base)
    if not m:
        return None
    y, mo, d, slug = m.groups()
    return f"/articulos/{y}/{mo}/{d}/{slug}/"


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1) if m else ""


def load_yaml(path):
    import yaml
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def article_hitos():
    """Devuelve {seccion: [items]} a partir de los hitos de los articulos."""
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
        hitos = data.get("hitos")
        if not hitos:
            continue
        url = slug_to_url(path)
        for h in hitos:
            if not isinstance(h, dict):
                continue
            fecha = str(h.get("fecha", "")).strip()
            texto = str(h.get("texto", "")).strip()
            if not fecha or not texto:
                continue
            extra = f" [Leer análisis]({url})" if url else ""
            # respeta un 'futuro: true' explicito
            if h.get("futuro"):
                seccion = "Lo que viene"
                orden = "9999"
            else:
                year = int(fecha[:4]) if re.match(r"\d{4}", fecha) else 9999
                seccion = seccion_por_anio(year)
                orden = fecha
            grouped.setdefault(seccion, []).append({
                "orden": orden,
                "fecha": fmt_fecha(fecha),
                "texto": texto + extra,
            })
    return grouped


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        import yaml  # noqa: F401
    except ImportError:
        print("WARN: PyYAML no disponible; se conserva _data/cronologia.yml del snapshot.")
        return 0

    try:
        seed = load_yaml(SEED) or []
        order = [g["seccion"] for g in seed]
        groups = {g["seccion"]: list(g.get("items") or []) for g in seed}
        for seccion, items in article_hitos().items():
            if seccion not in groups:
                groups[seccion] = []
                order.append(seccion)
            groups[seccion].extend(items)

        out = []
        for seccion in order:
            items = sorted(groups[seccion], key=lambda it: str(it.get("orden", "") or "9999"))
            out.append({"seccion": seccion, "items": items})

        with open(OUT, "w", encoding="utf-8") as f:
            yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        n = sum(len(g["items"]) for g in out)
        print(f"OK: _data/cronologia.yml = {len(out)} secciones, {n} hitos.")
        return 0
    except Exception as e:
        print(f"WARN: no se pudo generar cronologia ({e}); se conserva el snapshot.")
        return 0


if __name__ == "__main__":
    sys.exit(main())