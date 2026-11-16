#!/usr/bin/env python3
"""Valida el registro público de claims.

Uso:
    python scripts/validate_claims.py _data/claims.yml
    python scripts/validate_claims.py --self-test

Reglas:
- Campos obligatorios y fechas ISO.
- `confirmado` exige evidencia A, B o C y URL externa.
- `negacion` no puede ser `confirmado`.
- `AGENTS.md` no es una fuente pública válida.
- IDs únicos con formato xxx-000.
"""

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

REQUIRED = (
    "id", "seccion", "claim", "estado", "evidencia", "fuente",
    "url", "localizador", "extracto", "fecha_corte",
    "ultima_verificacion", "articulo",
)
STATUS = {"confirmado", "parcial", "incorrecto", "no_verificable", "no_demostrable"}
EVIDENCE = {"A", "B", "C", "D", "E"}
ID_RE = re.compile(r"^[a-z]{3}-\d{3}$")


def _date(value, field, where, errors):
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        errors.append(f"{where}: '{field}' no es una fecha ISO válida")
        return None


def validate(items, today=None):
    today = today or date.today()
    errors = []
    warnings = []
    seen = set()
    if not isinstance(items, list):
        return ["El registro debe ser una lista de claims"], warnings

    for index, item in enumerate(items, 1):
        where = f"claim #{index}"
        if not isinstance(item, dict):
            errors.append(f"{where}: debe ser un objeto")
            continue

        for field in REQUIRED:
            if item.get(field) in (None, ""):
                errors.append(f"{where}: falta '{field}'")

        claim_id = str(item.get("id", "")).strip()
        if claim_id:
            where = claim_id
            if not ID_RE.match(claim_id):
                errors.append(f"{where}: el ID debe tener formato xxx-000")
            if claim_id in seen:
                errors.append(f"{where}: ID duplicado")
            seen.add(claim_id)

        status = str(item.get("estado", "")).strip()
        evidence = str(item.get("evidencia", "")).strip().upper()
        tipo = str(item.get("tipo", "")).strip()
        url = str(item.get("url", "")).strip()
        article = str(item.get("articulo", "")).strip()

        if status and status not in STATUS:
            errors.append(f"{where}: estado inválido '{status}'")
        if evidence and evidence not in EVIDENCE:
            errors.append(f"{where}: evidencia inválida '{evidence}'")

        if status == "confirmado":
            if evidence in {"D", "E"}:
                errors.append(f"{where}: 'confirmado' no admite evidencia {evidence}")
            if not url.startswith("http"):
                errors.append(f"{where}: 'confirmado' exige URL externa")
        if tipo == "negacion" and status == "confirmado":
            errors.append(f"{where}: una negación no puede ser 'confirmado'")
        if "AGENTS.md" in url:
            errors.append(f"{where}: AGENTS.md no es una fuente pública")
        if article and not article.startswith("/"):
            errors.append(f"{where}: 'articulo' debe ser una ruta interna")

        corte = _date(item.get("fecha_corte"), "fecha_corte", where, errors)
        revisado = _date(item.get("ultima_verificacion"), "ultima_verificacion", where, errors)
        if corte and corte > today:
            errors.append(f"{where}: 'fecha_corte' está en el futuro")
        if revisado and revisado > today:
            errors.append(f"{where}: 'ultima_verificacion' está en el futuro")
        if revisado and (today - revisado).days > 180:
            warnings.append(f"{where}: revisión vencida ({(today - revisado).days} días)")

        if len(str(item.get("extracto", "")).strip()) < 20:
            errors.append(f"{where}: 'extracto' demasiado corto")

    return errors, warnings


def self_test():
    base = {
        "id": "ene-001",
        "seccion": "Energía",
        "claim": "El consumo nacional fue de 29.419 GWh en 2025.",
        "estado": "confirmado",
        "evidencia": "A",
        "fuente": "ANDE",
        "url": "https://www.ande.gov.py/",
        "localizador": "comunicado, párrafo 1",
        "extracto": "El consumo eléctrico nacional alcanzó 29.419 GWh.",
        "fecha_corte": "2026-01-14",
        "ultima_verificacion": "2026-11-16",
        "articulo": "/articulos/2026/08/12/mesa-energetica-pen-2050-paraguay/",
    }

    cases = []
    cases.append(("válido", [base], 0))
    cases.append(("confirmado con D", [dict(base, evidencia="D")], 1))
    cases.append(("negación confirmada", [dict(base, tipo="negacion")], 1))
    cases.append(("fuente interna", [dict(base, url="AGENTS.md")], 2))
    cases.append(("ID duplicado", [base, dict(base)], 1))

    failed = False
    for name, items, expected in cases:
        errors, _ = validate(items, today=date(2026, 11, 16))
        ok = len(errors) >= expected if expected else not errors
        print(f"{'OK' if ok else 'X'} {name}: {len(errors)} error(es)")
        if not ok:
            failed = True
            for error in errors:
                print(f"   {error}")
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="_data/claims.yml")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    path = Path(args.path)
    if not path.exists():
        print(f"X No existe: {path}")
        return 1
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"X YAML inválido: {exc}")
        return 1

    errors, warnings = validate(data)
    for warning in warnings:
        print(f"! {warning}")
    for error in errors:
        print(f"X {error}")
    if errors:
        print(f"\n{len(errors)} error(es), {len(warnings)} warning(s)")
        return 1
    print(f"OK: {len(data)} claims válidos, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
