#!/usr/bin/env python3
"""Genera el manifiesto de cierre long-form `_data/cierres.yml`.

No inventa artefactos: clasifica lo que existe en el entorno local.
- completo: research_<topic>/ con plan, findings, gap y spotcheck.
- parcial: carpeta identificable con artefactos incompletos.
- legacy: sin carpeta o carpeta vacía; requiere cierre resumido antes de reeditar.

Uso: python scripts/build_cierres.py
"""

import os
import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
POSTS = REPO / "_posts"
OUT = REPO / "_data" / "cierres.yml"
NON_ANALYSIS = {
    "2026-05-10-primer-articulo",
    "2026-06-10-que-es-realmente-el-futbol",
}

# Alias históricos: el artículo usa un slug distinto al directorio de research.
ALIASES = {
    "tokenizacion-del-agro-paraguay": "research_tokenizacion_agro",
    "magnifica-humanitas-enciclica-ia": "research_magnifica_humanitas",
    "laboratorio-americano-ia-futbol-mundial-2026": "research_futbol",
    "yguazu-digital-paraguay-hub-ia-mas-grande-del-mundo": "research_yguazu_digital",
    "anotacion-datos-paraguay-hub-trabajo-digital-ia": "research_anotacion_datos",
    "ley-proteccion-datos-paraguay-ia": "research_ley_proteccion_datos",
    "educacion-tech-paraguay-ia": "research_educacion_tech",
    "paraguay-china-taiwan-geopolitica-ia": "research_china_taiwan",
    "fintech-paraguay-ecosistema": "research_fintech",
    "talento-tech-paraguay-ia": "research_talento_tech",
    "agro-40-paraguay-ia": "research_agro_40",
    "semiconductores-taiwan-paraguay": "research_semiconductor",
    "startups-ia-paraguay": "research_startups_ia",
    "starlink-paraguay-conectividad": "research_starlink",
    "smart-cities-asuncion-paraguay": "research_asuncion",
    "ia-justicia-paraguay": "research_ia-justicia",
    "ecommerce-logistica-paraguay": "research_ecommerce",
    "guarani-ia": "research_guarani",
    "modelo-itaipu-gobernanza-ia": "research_itaipu",
    "energia-renovable-cambio-climatico-paraguay": "research_energia_renovable",
    "mesa-energetica-pen-2050-paraguay": "research_mesa-energetica-pen-2050",
    "ente-regulador-energia": "research_ente-regulador",
    "modelo-institucional-psr-sector-electrico": "research_modelo-institucional-psr",
    "estudio-ceare-tarifa-paraguay": "research_estudio-ceare",
    "energia-nuclear-paraguay-eeuu": "research_nuclear",
    "paraguay-investor-pass-residencia-inversores": "research_investor_pass",
    "cervepar-ia-algoritmo-vende-humano-decide": "research_cervepar",
    "cinco-tecnologias-que-prometieron-cambiar-todo": "research_5tecnologias",
    "apertura-sector-electrico-privado-paraguay": "research_apertura_electrica",
    "ia-cuesta-mas-que-humanos-burbuja": "research_ai_bubble",
    "de-la-soja-al-silicio-matriz-exportadora-paraguay": "research_soja_silicio",
    "gobierno-digital-paraguay": "research_gov_digital",
    "ia-periodismo-paraguay": "research_ai_journalism_2026",
    "ia-salud-paraguay": "research_ai_health_latam",
    "ciberseguridad-paraguay": "research_paraguay_cyber",
    "ia-corrupcion-paraguay": "research_ai_corruption",
    "ministerio-energia-mineria-hidrocarburos": "research_ministerio-mmeh",
    "los-contratos-secretos-de-ande": "research_contratos_ande",
    "araico-supercomputadora-yguazu-paraguay": "research_araico",
    "atome-ande-salida-paraguay": "research_atome",
    "brecha-triple-jovenes-paraguayos": "research_brecha-triple",
    "5g-segunda-subasta-paraguay": "research_5g",
    "silicon-valley-cono-sur-paraguay": "research_silicon_valley",
}

REQUIRED = ("research_plan.md", "gap_report.md", "spotcheck.md")


def post_data(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def analysis_posts():
    for path in sorted(POSTS.glob("*.md")):
        data = post_data(path)
        categories = data.get("categories") or []
        if isinstance(categories, str):
            categories = [categories]
        if (
            "articulos" in categories
            and data.get("pilar")
            and path.stem not in NON_ANALYSIS
        ):
            yield path, data


def missing_artifacts(directory):
    if not directory.is_dir():
        return list(REQUIRED) + ["findings_*.md"]
    missing = [name for name in REQUIRED if not (directory / name).exists()]
    if not list(directory.glob("findings_*.md")):
        missing.append("findings_*.md")
    return missing


def classify(path, data):
    topic = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    exact = REPO / ("research_" + topic)
    aliased = ALIASES.get(topic)
    candidates = []
    if exact.is_dir():
        candidates.append(exact)
    if aliased and (REPO / aliased).is_dir() and (REPO / aliased) not in candidates:
        candidates.append(REPO / aliased)
    directory = min(candidates, key=lambda d: (len(missing_artifacts(d)), 0 if d == exact else 1)) if candidates else None

    missing = missing_artifacts(directory) if directory else list(REQUIRED) + ["findings_*.md"]
    if directory and not missing:
        status = "completo"
        motivo = None
    elif directory and directory.is_dir() and any(directory.iterdir()):
        status = "parcial"
        motivo = "Carpeta identificable con artefactos incompletos; backfill pendiente."
    else:
        status = "legacy"
        motivo = "Sin carpeta de investigación identificable o carpeta vacía; exige cierre resumido antes de una nueva edición."
        directory = None

    return {
        "slug": path.stem,
        "research_dir": str(directory.relative_to(REPO)).replace("\\", "/") if directory else None,
        "estado": status,
        "faltantes": missing if status != "completo" else [],
        "motivo": motivo,
        "last_modified_at": data.get("last_modified_at"),
    }


def main():
    entries = []
    for path, data in analysis_posts():
        entries.append(classify(path, data))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Manifiesto de cierre long-form. Generado por scripts/build_cierres.py.\n"
        "# estado: completo | parcial | legacy. No inventa artefactos.\n"
        "# research_*/ es local y no se versiona; este manifiesto es la evidencia versionada.\n\n"
    )
    OUT.write_text(header + yaml.safe_dump({"cierres": entries}, allow_unicode=True, sort_keys=False), encoding="utf-8")
    counts = {}
    for entry in entries:
        counts[entry["estado"]] = counts.get(entry["estado"], 0) + 1
    print(f"cierres: {len(entries)} | {counts}")


if __name__ == "__main__":
    main()
