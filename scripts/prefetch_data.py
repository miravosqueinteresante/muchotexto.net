#!/usr/bin/env python3
"""
Pre-fetch de datos locales para investigación de artículos long-form.

Lee _data/datos_publicos.json y devuelve indicadores relevantes
basado en keywords o entidades. Diseñado para ejecutarse ANTES
de los subagentes de web-research y pasar su salida como contexto.

Uso:
    python scripts/prefetch_data.py ande consumo demanda
    python scripts/prefetch_data.py itaipu generacion
    python scripts/prefetch_data.py --all-ande
    python scripts/prefetch_data.py --list-entities
    python scripts/prefetch_data.py --list-indicators ande

Flujo obligatorio (AGENTS.md §OBLIGATORIO):
    1. Ejecutar este script con las keywords del artículo
    2. Adjuntar la salida al prompt de los subagentes de research
    3. Los subagentes DEBEN usar estos datos como fuente primaria
    4. Solo buscar en la web lo que NO esté en esta salida
"""

import json
import os
import sys
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REPO_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_DIR / "_data" / "datos_publicos.json"

# Mapeo de keywords a entidades y indicadores
KEYWORD_MAP = {
    # Entidades
    "ande": {"entidad_id": "ande"},
    "itaipu": {"entidad_id": "itaipu"},
    "itaipú": {"entidad_id": "itaipu"},
    "yacyreta": {"entidad_id": "yacyreta"},
    "yacyretá": {"entidad_id": "yacyreta"},
    # ANDE
    "consumo": {"indicador_contains": "consumo"},
    "demanda": {"indicador_contains": "demanda"},
    "perdida": {"indicador_contains": "perdidas"},
    "pérdida": {"indicador_contains": "perdidas"},
    "tarifa": {"indicador_contains": "tarifa"},
    "cliente": {"indicador_contains": "clientes"},
    "generacion": {"indicador_contains": "generacion"},
    "generación": {"indicador_contains": "generacion"},
    "potencia": {"indicador_contains": "potencia"},
    "factor_carga": {"indicador": "factor_carga"},
    # Itaipú
    "suministro": {"indicador_contains": "suministro"},
    "exportacion": {"indicador_contains": "exportacion"},
    "exportación": {"indicador_contains": "exportacion"},
    # Yacyretá
    "embalse": {"indicador_contains": "embalse"},
    "caudal": {"indicador_contains": "caudal"},
}


def load_data():
    if not DATA_FILE.exists():
        print("ERROR: _data/datos_publicos.json no existe. Ejecutar sync_datos.py primero.", file=sys.stderr)
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def match_indicator(indicator, filters):
    """Verifica si un indicador coincide con CUALQUIER filtro (OR logic)."""
    if not filters:
        return True
    for filt in filters:
        if "entidad_id" in filt and indicator.get("entidad_id") == filt["entidad_id"]:
            return True
        if "indicador_contains" in filt and filt["indicador_contains"] in indicator.get("indicador", ""):
            return True
        if "indicador" in filt and indicator.get("indicador") == filt["indicador"]:
            return True
    return False


def resolve_filters(keywords):
    """Resuelve keywords en filtros de búsqueda."""
    filters = []
    seen_entities = set()
    seen_indicators = set()

    for kw in keywords:
        kw_lower = kw.lower().strip()
        if kw_lower in KEYWORD_MAP:
            mapping = KEYWORD_MAP[kw_lower]
            if "entidad_id" in mapping and mapping["entidad_id"] not in seen_entities:
                filters.append(mapping)
                seen_entities.add(mapping["entidad_id"])
            elif "indicador_contains" in mapping and mapping["indicador_contains"] not in seen_indicators:
                filters.append(mapping)
                seen_indicators.add(mapping["indicador_contains"])
            elif "indicador" in mapping and mapping["indicador"] not in seen_indicators:
                filters.append(mapping)
                seen_indicators.add(mapping["indicador"])
        elif len(kw_lower) > 2:
            # Búsqueda libre: buscar en indicador y entidad
            filters.append({"indicador_contains": kw_lower})

    return filters


def format_indicator(ind, aggregate=False):
    """Formatea un indicador para lectura humana."""
    estado = ind.get("estado_verificacion", "desconocido")
    icono = {"verificado": "VERIFICADO", "revisado": "REVISADO", "extraido": "EXTRAIDO", "requiere_revision": "REVISAR"}.get(estado, "?")
    url = ind.get("url", "sin URL")
    if aggregate:
        return f"  [{icono}] {ind['indicador']}: {ind['valor']} {ind.get('unidad', '')} ({ind.get('fecha_fin', 's/f')}) — Fuente: {ind.get('fuente', '?')}"
    return (
        f"  [{icono}] {ind['entidad']} — {ind['indicador']}: "
        f"{ind['valor']} {ind.get('unidad', '')} "
        f"({ind.get('fecha_fin', ind.get('fecha_inicio', 's/f'))})\n"
        f"    Fuente: {ind.get('fuente', '?')} | URL: {url}"
    )


def prefetch(keywords=None, entity_filter=None, list_entities=False, list_indicators=None, recent_only=False):
    data = load_data()
    indicators = data.get("indicadores", [])

    if list_entities:
        entities = {}
        for ind in indicators:
            eid = ind.get("entidad_id", "?")
            if eid not in entities:
                entities[eid] = {"nombre": ind.get("entidad", "?"), "count": 0}
            entities[eid]["count"] += 1
        print("=== Entidades en datos_publicos.json ===")
        for eid, info in sorted(entities.items()):
            print(f"  {eid}: {info['nombre']} ({info['count']} indicadores)")
        return

    if list_indicators:
        entity_id = list_indicators.lower()
        filtered = [ind for ind in indicators if ind.get("entidad_id") == entity_id]
        seen = {}
        for ind in filtered:
            key = ind["indicador"]
            if key not in seen or ind.get("fecha_fin", "") > seen[key].get("fecha_fin", ""):
                seen[key] = ind
        filtered = list(seen.values())
        print(f"=== Indicadores de {entity_id} ({len(filtered)}) ===")
        for ind in sorted(filtered, key=lambda x: x["indicador"]):
            print(f"  {ind['indicador']}: {ind['valor']} {ind.get('unidad', '')} [{ind.get('estado_verificacion', '?')}]")
        return

    if entity_filter:
        filters = [{"entidad_id": entity_filter.lower()}]
    elif keywords:
        filters = resolve_filters(keywords)
    else:
        print("Uso: prefetch_data.py [keyword1] [keyword2] ...", file=sys.stderr)
        print("     prefetch_data.py --all-ande", file=sys.stderr)
        print("     prefetch_data.py --list-entities", file=sys.stderr)
        print("     prefetch_data.py --list-indicators <entidad>", file=sys.stderr)
        sys.exit(1)

    matched = [ind for ind in indicators if match_indicator(ind, filters)]

    if not matched:
        print("=== Sin resultados en la capa de datos local ===")
        print(f"Buscado: {[f for f in filters]}")
        print("Accion: investigar en la web directamente.")
        return

    # Deduplicate: keep latest per (entity, indicator)
    seen = {}
    for ind in matched:
        key = (ind.get("entidad_id"), ind.get("indicador"))
        if key not in seen or ind.get("fecha_fin", "") > seen[key].get("fecha_fin", ""):
            seen[key] = ind
    deduped = sorted(seen.values(), key=lambda x: (x.get("entidad_id", ""), x.get("indicador", "")))

    # Group by entity
    by_entity = {}
    for ind in deduped:
        eid = ind.get("entidad_id", "?")
        if eid not in by_entity:
            by_entity[eid] = []
        by_entity[eid].append(ind)

    print(f"=== Capa de datos local: {len(deduped)} indicadores ===")
    print(f"Filtros: {[f for f in filters]}")
    print()

    for eid, inds in sorted(by_entity.items()):
        entity_name = inds[0].get("entidad", eid)
        print(f"--- {entity_name} ({len(inds)} indicadores) ---")
        for ind in sorted(inds, key=lambda x: x["indicador"]):
            estado = ind.get("estado_verificacion", "?")
            icono = {"verificado": "V", "revisado": "R", "extraido": "E", "requiere_revision": "?"}.get(estado, "?")
            url = ind.get("url", "sin URL")
            print(f"  [{icono}] {ind['indicador']}: {ind['valor']} {ind.get('unidad', '')} ({ind.get('fecha_fin', '?')[:4]})")
            print(f"    Fuente: {ind.get('fuente', '?')} | {url}")
        print()

    needs_review = [ind for ind in deduped if ind.get("estado_verificacion") == "requiere_revision"]
    if needs_review:
        print(f"AVISO: {len(needs_review)} indicadores requieren revision.")
        print("  Abrir la URL original y contrastar antes de usar como fuente primaria.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    if args[0] == "--list-entities":
        prefetch(list_entities=True)
    elif args[0] == "--list-indicators" and len(args) > 1:
        prefetch(list_indicators=args[1])
    elif args[0] == "--all-ande":
        prefetch(entity_filter="ande")
    elif args[0] == "--all-itaipu":
        prefetch(entity_filter="itaipu")
    elif args[0] == "--all-yacyreta":
        prefetch(entity_filter="yacyreta")
    else:
        prefetch(keywords=args)
