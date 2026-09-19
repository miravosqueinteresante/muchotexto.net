#!/usr/bin/env python3
"""
audit_consistency.py — Auditor de consistencia (READ-ONLY, stdlib only).

Hace cumplir el principio del proyecto: **un dato canonico = una unica fuente
de verdad**. Verifica que cada conteo/relacion derivable coincida con su fuente
y que las superficies publicadas usen la expresion dinamica (no copias).

No modifica ningun archivo. Exit 0 si todo es consistente; exit 1 si hay
hallazgos (ERROR). Pensado para correr local y, en una fase posterior, en CI.

Uso:
    python scripts/audit_consistency.py
    python scripts/audit_consistency.py --json
"""

import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── Fase 0: MAPA DE FUENTES (fuente unica -> consumidores) ──────────────────
# Cada conteo canonico declara su archivo fuente, su item de lista y las
# superficies que DEBEN consumirlo con una expresion dinamica (no literales).
CANON = {
    "entidades": {
        "file": "_data/entities.yml",
        "item": r"^- slug:",
        "consumers": {
            "_layouts/home.html": "site.data.entities | size",
            "_includes/grafo-observatorio.html": "site.data.entities | size",
            "ia-en-paraguay.markdown": "site.data.entities | size",
            "llms.txt": "site.data.entities | size",
        },
    },
    "normas": {
        "file": "_data/leyes.yml",
        "item": r"^- nombre:",
        "consumers": {
            "radar-legislativo.markdown": "site.data.leyes",
        },
    },
    "fuentes_news": {
        "file": "_data/fuentes.yml",
        "item": r"^- name:",
        "consumers": {
            "_layouts/home.html": "site.data.fuentes | size",
            "about.markdown": "site.data.fuentes | size",
            "como-trabajamos.markdown": "site.data.fuentes | size",
            "llms.txt": "site.data.fuentes | size",
        },
    },
    "indicadores": {
        "file": "_data/datos_publicos.json",
        "item": None,
        "consumers": {
            "_includes/datos-verificados.html": "datos_publicos.indicadores",
            "llms.txt": "datos_publicos.indicadores",
        },
    },
    "articulos": {
        "file": "_posts/",
        "item": None,
        "consumers": {
            "ia-en-paraguay.markdown": "categories contains 'articulos'",
        },
    },
}

# Archivos internos que NUNCA deben publicarse (deben estar en exclude).
INTERNAL_FILES = [
    "AGENTS.md", "README.md", "borrador_media_kit.md",
    "analisis_junio_2026.md", "analisis_julio_2026.md",
    "pulso_july_16_31_structured.json",
    "squirrel-audit-report.md", "squirrel-audit-report-v2.md",
    "squirrel-audit-report-v3.md", "squirrel-audit-report-v4.md",
    "squirrel-audit-report-v5.md",
]

# Archivos fuente que NO se escanean (internos / locales-only / historicos).
IGNORE_REL = {
    "AGENTS.md", "README.md", "borrador_media_kit.md",
    "analisis_junio_2026.md", "analisis_julio_2026.md",
    "estrategia-seo-unificada-muchotexto.md",
}

# Articulos que NO son del cluster de analisis.
NON_ANALYSIS = {
    "2026-05-10-primer-articulo",
    "2026-06-10-que-es-realmente-el-futbol",
}


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def is_ignored(path):
    base = os.path.basename(path)
    if base in IGNORE_REL:
        return True
    if base.startswith(("squirrel-audit", "analisis_", "fix_")):
        return True
    return False


def scan_targets():
    files = (
        glob.glob(os.path.join(REPO, "*.markdown"))
        + glob.glob(os.path.join(REPO, "*.md"))
        + glob.glob(os.path.join(REPO, "_posts", "*.md"))
        + glob.glob(os.path.join(REPO, "_includes", "*.html"))
        + glob.glob(os.path.join(REPO, "_layouts", "*.html"))
        + [os.path.join(REPO, "llms.txt")]
    )
    return [f for f in files if os.path.exists(f) and not is_ignored(f)]


def count_items(path, pattern):
    if not pattern or not os.path.exists(path):
        return None
    rx = re.compile(pattern)
    return sum(1 for line in read(path).splitlines() if rx.match(line))


def count_indicators():
    p = os.path.join(REPO, "_data", "datos_publicos.json")
    data = json.loads(read(p))
    per = {}
    for ind in data.get("indicadores", []):
        eid = ind.get("entidad_id")
        per[eid] = per.get(eid, 0) + 1
    return per, len(data.get("indicadores", []))


def analysis_posts():
    posts = []
    for f in glob.glob(os.path.join(REPO, "_posts", "*.md")):
        head = read(f)[:600]
        m = re.search(r"^categories:\s*\[?([^\]\n]+)\]?", head, re.M)
        if m and "articulos" in m.group(1):
            slug = os.path.basename(f)[:-3]
            if slug not in NON_ANALYSIS:
                posts.append(slug)
    return sorted(posts)


def load_config_exclude():
    """Devuelve el set de entradas bajo `exclude:` en _config.yml."""
    p = os.path.join(REPO, "_config.yml")
    if not os.path.exists(p):
        return set()
    lines = read(p).splitlines()
    entries = set()
    in_block = False
    for line in lines:
        if re.match(r"^exclude:\s*$", line):
            in_block = True
            continue
        if in_block:
            # termina en la proxima clave de nivel 0 (sin indentacion)
            if line and not line[0].isspace() and not line.startswith("#"):
                break
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m:
                entries.add(m.group(1).strip())
    return entries


def check_post_urls(targets):
    findings = []
    rx = re.compile(r"\{%\s*post_url\s+([^\s%\}]+)\s*%\}")
    for path in targets:
        for m in rx.finditer(read(path)):
            slug = m.group(1)
            if not os.path.exists(os.path.join(REPO, "_posts", slug + ".md")):
                findings.append((os.path.basename(path), slug))
    return findings


def check_pillar_links():
    p = os.path.join(REPO, "ia-en-paraguay.markdown")
    if not os.path.exists(p):
        return []
    text = read(p)
    return [s for s in analysis_posts() if s not in text]


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    errors = []
    info = []

    # INV-1: conteos fuente vs consumidores dinamicos
    for name, spec in CANON.items():
        src = os.path.join(REPO, spec["file"])
        n = count_items(src, spec["item"]) if spec["item"] else None
        for rel, expr in spec["consumers"].items():
            target = os.path.join(REPO, rel)
            if not os.path.exists(target):
                errors.append(f"[INV-1] consumidor declarado inexistente: {rel} (para {name})")
                continue
            if norm(expr) not in norm(read(target)):
                errors.append(
                    f"[INV-1] {rel} no usa la expresion dinamica '{expr}' para '{name}' "
                    f"(posible copia hardcodeada). Fuente: {spec['file']}"
                )
        if n is not None:
            info.append(f"{name}: {n} (fuente {spec['file']})")

    # INV-2: entidades <-> nodos del grafo
    n_entities = count_items(os.path.join(REPO, "_data/entities.yml"), r"^- slug:")
    grafo = os.path.join(REPO, "grafo.json")
    n_nodes = len(json.loads(read(grafo)).get("nodes", [])) if os.path.exists(grafo) else None
    if n_entities is not None and n_nodes is not None and n_entities != n_nodes:
        errors.append(
            f"[INV-2] entities.yml={n_entities} pero grafo.json={n_nodes} nodos. "
            f"Regenerar: python scripts/build_entities.py"
        )

    # INV-3: indicadores por entidad
    per, total = count_indicators()
    if total == 0:
        errors.append("[INV-3] _data/datos_publicos.json no tiene indicadores")
    info.append(f"indicadores: {total} {per}")

    # INV-4: pulso lee fuentes.yml
    pulso = os.path.join(REPO, "scripts/pulso_diario.py")
    if os.path.exists(pulso) and "fuentes.yml" not in read(pulso):
        errors.append("[INV-4] pulso_diario.py no lee _data/fuentes.yml")

    # INV-5: articulos de analisis
    posts = analysis_posts()
    info.append(f"articulos de analisis: {len(posts)}")

    # INV-6: documentos internos excluidos del build
    excluded = load_config_exclude()
    for f in INTERNAL_FILES:
        if f not in excluded:
            errors.append(f"[INV-6] '{f}' no esta en el exclude de _config.yml (puede publicarse)")

    # INV-7: post_url resuelven
    targets = scan_targets()
    for base, slug in check_post_urls(targets):
        errors.append(f"[INV-7] {base}: post_url '{slug}' no existe en _posts/")

    # INV-8: pilar enlaza todos los analisis
    for slug in check_pillar_links():
        errors.append(f"[INV-8] ia-en-paraguay.markdown no enlaza el articulo '{slug}'")

    report = {"errors": errors, "info": info, "scanned_files": [os.path.relpath(t, REPO) for t in targets]}

    if "--json" in sys.argv:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if errors else 0

    print("=" * 70)
    print("AUDITOR DE CONSISTENCIA — muchotexto.net")
    print("=" * 70)
    for line in info:
        print("  ·", line)
    print()
    if errors:
        print(f"HALLAZGOS: {len(errors)} error(es)")
        for e in errors:
            print("  ✗", e)
    else:
        print("OK — sin inconsistencias detectadas.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())