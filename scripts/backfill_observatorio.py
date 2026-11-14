#!/usr/bin/env python3
"""Genera entradas base en _data/observatorio.yml desde evidencia real.

No adivina: usa el reporte read-only de audit_observatorio_coverage.py.
Las entradas existentes no se tocan. `--apply` escribe; sin flag es dry-run.

Uso:
    python scripts/backfill_observatorio.py
    python scripts/backfill_observatorio.py --apply
"""

import os
import sys

import yaml

from audit_observatorio_coverage import audit
from common import read

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO, "_data", "observatorio.yml")

HEADER = """# Decisiones de cobertura del observatorio por artículo.
# updated = la superficie contiene la URL del artículo.
# n/a = no aplica; exige un motivo en `motivos`.
# Generado por scripts/backfill_observatorio.py; las entradas existentes se preservan.
"""

MOTIVOS = {
    "cronologia": "El artículo no declara hitos en su front matter.",
    "glosario": "El artículo no declara términos en su front matter.",
    "casos": "El artículo no declara casos en su front matter.",
    "directorio": "El artículo no declara entradas de directorio en su front matter.",
    "radar": "No se identificó un vínculo con una norma del radar en este backfill.",
    "regulacion": "No se identificó un vínculo con una norma del mapa regulatorio en este backfill.",
    "claims": "No se identificó un claim en la página pública en este backfill.",
    "entidades": "El artículo no aparece en ninguna página de entidad.",
    "grafo": "El grafo no indexa URLs de artículos.",
}

DERIVED = ("cronologia", "glosario", "casos", "directorio")
OPTIONAL = ("radar", "regulacion", "claims", "entidades", "grafo")


def build_entry(row):
    surfaces = {"pilar": "updated", "llms": "updated"}
    reasons = {}
    for surface in DERIVED:
        if row[surface] == "updated":
            surfaces[surface] = "updated"
        else:
            surfaces[surface] = "n/a"
            reasons[surface] = MOTIVOS[surface]
    for surface in OPTIONAL:
        if row[surface] == "linked":
            surfaces[surface] = "updated"
        else:
            surfaces[surface] = "n/a"
            reasons[surface] = MOTIVOS[surface]
    return {"superficies": surfaces, "motivos": reasons}


def main():
    rows = audit()
    existing = yaml.safe_load(read(MANIFEST)) or {}
    out = dict(existing)
    added = 0
    for row in rows:
        if row["slug"] not in out:
            out[row["slug"]] = build_entry(row)
            added += 1

    print(f"Artículos: {len(rows)} | entradas existentes: {len(existing)} | nuevas: {added}")
    if "--apply" not in sys.argv:
        print("Dry-run: no se escribió el manifiesto. Usar --apply para guardar.")
        return 0

    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write(HEADER)
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"OK: {MANIFEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
