#!/usr/bin/env python3
"""Reporte read-only de cobertura del observatorio por artículo.

No modifica manifiestos ni páginas. Distingue:
- updated: la superficie contiene la evidencia del artículo.
- missing: el artículo declara el dato (hitos/glosario/casos/directorio)
  pero la superficie no lo contiene.
- n/a: el artículo no declara esa superficie derivada.
- linked: superficie opcional (radar/regulación/claims/entidades/grafo)
  que contiene la URL del artículo.

Uso:
    python scripts/audit_observatorio_coverage.py
    python scripts/audit_observatorio_coverage.py --json ruta.json --md ruta.md
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
OUT_DIR = os.path.join(REPO, "research_observatorio")

SURFACES = (
    "pilar", "llms", "cronologia", "glosario", "casos", "directorio",
    "radar", "regulacion", "claims", "entidades", "grafo",
)

# Mismo universo que audit_consistency: bienvenida y ensayo de fútbol no son
# análisis de IA y no se les exige cobertura del observatorio.
NON_ANALYSIS = {
    "2026-05-10-primer-articulo",
    "2026-06-10-que-es-realmente-el-futbol",
}


def post_data(path):
    text = read(path)
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def article_url(data, path):
    permalink = str(data.get("permalink", "") or "").strip()
    if permalink:
        return permalink if permalink.endswith("/") else permalink + "/"
    base = os.path.basename(path)[:-3]
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)$", base)
    if not m:
        return ""
    y, mo, d, slug = m.groups()
    return f"/articulos/{y}/{mo}/{d}/{slug}/"


def load_cache():
    return {
        "pilar": read(os.path.join(REPO, "ia-en-paraguay.markdown")),
        "llms": read(os.path.join(REPO, "llms.txt")),
        "cronologia": read(os.path.join(REPO, "_data", "cronologia.yml")),
        "glosario": read(os.path.join(REPO, "_data", "glosario.yml")),
        "casos": read(os.path.join(REPO, "_data", "casos.yml")),
        "directorio": read(os.path.join(REPO, "_data", "directorio.yml")),
        "radar": read(os.path.join(REPO, "_data", "leyes.yml")),
        "regulacion": read(os.path.join(REPO, "regulacion.markdown")),
        "claims": read(os.path.join(REPO, "claims-verificados.markdown")),
        "grafo": read(os.path.join(REPO, "grafo.json")),
        "entidades": "\n".join(read(p) for p in glob.glob(os.path.join(REPO, "entidades", "*.markdown"))),
    }


def declared_surfaces(data):
    return {
        "cronologia": bool(data.get("hitos")),
        "glosario": bool(data.get("glosario")),
        "casos": bool(data.get("casos")),
        "directorio": bool(data.get("directorio")),
    }


def surface_status(surface, data, url, slug, cache):
    text = cache.get(surface, "")
    if surface == "pilar":
        return "updated" if f"{{% post_url {slug} %}}" in text or url in text else "missing"
    if surface == "llms":
        return "updated" if url in text else "missing"
    if surface == "glosario":
        terms = [str(t.get("termino", "")).strip() for t in (data.get("glosario") or []) if isinstance(t, dict)]
        if not terms:
            return "n/a"
        return "updated" if all(t in text for t in terms) else "missing"
    if surface == "directorio":
        names = [str(i.get("nombre", "")).strip() for i in (data.get("directorio") or []) if isinstance(i, dict)]
        if not names:
            return "n/a"
        return "updated" if all(n in text for n in names) else "missing"
    if surface in ("cronologia", "casos"):
        if not declared_surfaces(data).get(surface):
            return "n/a"
        return "updated" if url in text else "missing"
    # Superficies opcionales: si no hay vínculo, no es un error de cobertura.
    return "linked" if url in text else "-"


def audit():
    cache = load_cache()
    rows = []
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        data = post_data(path)
        categories = data.get("categories") or []
        if isinstance(categories, str):
            categories = [categories]
        if "articulos" not in categories:
            continue
        slug = os.path.basename(path)[:-3]
        if slug in NON_ANALYSIS:
            continue
        url = article_url(data, path)
        row = {"slug": slug, "title": str(data.get("title", "")), "url": url, "pilar_num": data.get("pilar")}
        for surface in SURFACES:
            row[surface] = surface_status(surface, data, url, slug, cache)
        rows.append(row)
    return rows


def summary(rows):
    missing = []
    for row in rows:
        for surface in SURFACES:
            if row[surface] == "missing":
                missing.append((row["slug"], surface))
    linked = {s: sum(1 for r in rows if r.get(s) == "linked") for s in ("radar", "regulacion", "claims", "entidades", "grafo")}
    by_surface = {}
    for surface in SURFACES:
        by_surface[surface] = {}
        for row in rows:
            status = row[surface]
            by_surface[surface][status] = by_surface[surface].get(status, 0) + 1
    return {
        "articulos": len(rows),
        "pilar_ok": sum(1 for r in rows if r["pilar"] == "updated"),
        "llms_ok": sum(1 for r in rows if r["llms"] == "updated"),
        "missing": missing,
        "linked": linked,
        "by_surface": by_surface,
    }


def write_md(rows, path):
    lines = [
        "# Cobertura del observatorio",
        "",
        f"Artículos: {len(rows)}",
        "",
        "| Artículo | Pilar | LLMS | Cron. | Glos. | Casos | Dir. | Radar | Reg. | Claims | Ent. | Grafo |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        cells = [
            f"[{r['slug']}]({r['url']})",
            r["pilar"], r["llms"], r["cronologia"], r["glosario"], r["casos"],
            r["directorio"], r["radar"], r["regulacion"], r["claims"],
            r["entidades"], r["grafo"],
        ]
        lines.append("| " + " | ".join(cells) + " |")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    rows = audit()
    s = summary(rows)
    os.makedirs(OUT_DIR, exist_ok=True)
    json_path = os.path.join(OUT_DIR, "coverage.json")
    md_path = os.path.join(OUT_DIR, "coverage.md")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"summary": s, "rows": rows}, f, ensure_ascii=False, indent=2)
    write_md(rows, md_path)

    print(f"Artículos: {s['articulos']} | pilar OK: {s['pilar_ok']} | llms OK: {s['llms_ok']}")
    print("Superficies opcionales enlazadas: " + ", ".join(f"{k}={v}" for k, v in s["linked"].items()))
    print("Detalle: " + " | ".join(
        f"{name}: " + ", ".join(f"{k}={v}" for k, v in counts.items())
        for name, counts in s["by_surface"].items()
    ))
    if s["missing"]:
        print(f"Faltantes declarados: {len(s['missing'])}")
        for slug, surface in s["missing"]:
            print(f"  X  {slug}: {surface}")
    else:
        print("Faltantes declarados: 0")
    print(f"Reporte: {md_path} | {json_path}")
    return 1 if s["missing"] else 0


if __name__ == "__main__":
    sys.exit(main())
