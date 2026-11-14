#!/usr/bin/env python3
"""Verifica que un artículo declare y cumpla su cobertura del observatorio.

La decisión editorial vive en `_data/observatorio.yml`. Cada superficie debe
estar en `updated` (con la URL del artículo en la superficie) o `n/a` (con un
motivo). El objetivo es evitar que un build verde oculte páginas atrasadas.

Uso:
    python scripts/check_observatorio.py _posts/2026-11-13-slug.md
"""

import glob
import os
import re
import sys

import yaml

from common import read

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO, "_data", "observatorio.yml")

SURFACES = (
    "pilar", "llms", "cronologia", "glosario", "casos", "directorio",
    "radar", "regulacion", "claims", "entidades", "grafo",
)

NON_ANALYSIS = {
    "2026-05-10-primer-articulo",
    "2026-06-10-que-es-realmente-el-futbol",
}


def _slug(path):
    return os.path.basename(path)[:-3]


def _post_data(path):
    text = read(path)
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def _article_url(data, path):
    permalink = str(data.get("permalink", "") or "").strip()
    if permalink:
        return permalink if permalink.endswith("/") else permalink + "/"
    base = os.path.basename(path)[:-3]
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)$", base)
    if not m:
        return ""
    y, mo, d, slug = m.groups()
    return f"/articulos/{y}/{mo}/{d}/{slug}/"


def _contains(path, needle):
    return needle in read(os.path.join(REPO, path))


def _any_entity_mentions(url):
    for path in glob.glob(os.path.join(REPO, "entidades", "*.markdown")):
        if url in read(path):
            return True
    return False


def _surface_ok(surface, url, data, slug):
    if surface == "pilar":
        return f"{{% post_url {slug} %}}" in read(os.path.join(REPO, "ia-en-paraguay.markdown")) or url in read(os.path.join(REPO, "ia-en-paraguay.markdown"))
    if surface == "llms":
        return _contains("llms.txt", url)
    if surface == "cronologia":
        return _contains("_data/cronologia.yml", url)
    if surface == "casos":
        return _contains("_data/casos.yml", url)
    if surface == "radar":
        return _contains("_data/leyes.yml", url)
    if surface == "regulacion":
        return _contains("regulacion.markdown", url)
    if surface == "claims":
        return _contains("claims-verificados.markdown", url)
    if surface == "entidades":
        return _any_entity_mentions(url)
    if surface == "grafo":
        return _contains("grafo.json", url)
    if surface == "glosario":
        terms = data.get("glosario") or []
        if not terms:
            return False
        glossary = read(os.path.join(REPO, "_data/glosario.yml"))
        return all(str(t.get("termino", "")).strip() in glossary for t in terms if isinstance(t, dict))
    if surface == "directorio":
        items = data.get("directorio") or []
        if not items:
            return False
        directory = read(os.path.join(REPO, "_data/directorio.yml"))
        return all(str(i.get("nombre", "")).strip() in directory for i in items if isinstance(i, dict))
    return False


def check_post(path):
    """Devuelve una lista de errores; vacía si la cobertura está completa."""
    data = _post_data(path)
    slug = _slug(path)
    url = _article_url(data, path)
    if not url:
        return [f"Observatorio: no se pudo resolver la URL de '{slug}'"]

    manifest = yaml.safe_load(read(MANIFEST)) or {}
    entry = manifest.get(slug)
    if not entry:
        return [f"Observatorio: falta la entrada '{slug}' en _data/observatorio.yml"]

    surfaces = entry.get("superficies") or {}
    reasons = entry.get("motivos") or {}
    errors = []
    for surface in SURFACES:
        status = surfaces.get(surface)
        if status == "updated":
            if not _surface_ok(surface, url, data, slug):
                errors.append(f"Observatorio: '{surface}' está en updated pero no contiene {url}")
        elif status == "n/a":
            if not str(reasons.get(surface, "")).strip():
                errors.append(f"Observatorio: '{surface}' es n/a pero falta el motivo")
        else:
            errors.append(f"Observatorio: '{surface}' debe ser updated o n/a")
    return errors


def analysis_articles():
    paths = []
    for path in sorted(glob.glob(os.path.join(REPO, "_posts", "*.md"))):
        slug = os.path.basename(path)[:-3]
        data = _post_data(path)
        categories = data.get("categories") or []
        if isinstance(categories, str):
            categories = [categories]
        if "articulos" in categories and data.get("pilar") and slug not in NON_ANALYSIS:
            paths.append(path)
    return paths


def latest_article():
    paths = analysis_articles()
    return paths[-1] if paths else None


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/check_observatorio.py _posts/ARTICULO.md | --latest | --all")
        return 2
    errors = []
    if sys.argv[1] == "--latest":
        path = latest_article()
        if not path:
            print("No se encontró un artículo de análisis.")
            return 2
        errors = check_post(path)
    elif sys.argv[1] == "--all":
        for path in analysis_articles():
            errors.extend(check_post(path))
    else:
        path = os.path.join(REPO, sys.argv[1]) if not os.path.isabs(sys.argv[1]) else sys.argv[1]
        errors = check_post(path)
    if errors:
        for error in errors:
            print(f"  X  {error}")
        return 1
    print("OK: cobertura del observatorio completa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
