#!/usr/bin/env python3
"""
audit_canon.py — Auditor de caducidad del canon de verificación.

Lee `scripts/canon_verificacion.yml` y lista los claims cuya última
verificación ya superó su período de caducidad. No modifica nada.

Uso:
    python scripts/audit_canon.py            # salida legible
    python scripts/audit_canon.py --json     # salida para CI
    python scripts/audit_canon.py --vencer-30  # incluye los que vencen en <=30 días

Exit 0 si no hay vencidos; exit 1 si los hay (para CI/monitoreo).
"""

import json
import os
import sys
from datetime import date, datetime, timedelta

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML no disponible (pip install pyyaml)")
    sys.exit(2)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON = os.path.join(REPO, "scripts", "canon_verificacion.yml")


def load_claims():
    with open(CANON, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("claims", [])


def status(claim, today):
    """Devuelve (dias_restantes, vencido) del claim respecto a hoy."""
    fv = datetime.strptime(claim["fecha_verificacion"], "%Y-%m-%d").date()
    dias = int(claim.get("caducidad_dias", 90))
    vence = fv + timedelta(days=dias)
    return (vence - today).days


def main():
    today = date.today()
    claims = load_claims()
    horizonte = 30 if "--vencer-30" in sys.argv else 0

    vencidos = []
    proximos = []
    for c in claims:
        restantes = status(c, today)
        if restantes <= 0:
            vencidos.append({**c, "dias_vencido": -restantes})
        elif restantes <= horizonte:
            proximos.append({**c, "dias_restantes": restantes})

    report = {
        "fecha": today.isoformat(),
        "total_claims": len(claims),
        "vencidos": vencidos,
        "proximos_a_vencer": proximos,
    }

    if "--json" in sys.argv:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if vencidos else 0

    print("=" * 70)
    print("AUDITOR DE CADUCIDAD DEL CANON — muchotexto.net")
    print("=" * 70)
    print(f"Fecha: {today.isoformat()}  ·  claims rastreados: {len(claims)}")
    print()
    if vencidos:
        print(f"VENCIDOS ({len(vencidos)}):")
        for c in vencidos:
            print(f"  ✗ [{c['categoria']}] {c['id']} — vencido hace {c['dias_vencido']} días")
            print(f"      fuente: {c['fuente']}")
    else:
        print("OK — ningún claim vencido.")
    if proximos:
        print(f"\nPRÓXIMOS A VENCER (≤{horizonte} días):")
        for c in proximos:
            print(f"  ⚠ [{c['categoria']}] {c['id']} — vence en {c['dias_restantes']} días")
    return 1 if vencidos else 0


if __name__ == "__main__":
    sys.exit(main())
