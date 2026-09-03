#!/usr/bin/env python3
"""
Sync datos verificables desde muchotexto-data (datos-publicos) al sitio Jekyll.

Descarga los indicadores publicados por el repo hermano
https://github.com/miravosqueinteresante/datos-publicos y los escribe en
`_data/datos_publicos.json` para que el dashboard los consuma via
`site.data.datos_publicos`.

Seguridad:
- El archivo `_data/datos_publicos.json` SIEMPRE existe (snapshot commiteado).
- Si la descarga falla (red, parseo, estructura invalida) el script NO
  sobreescribe y sale con 0: el build Jekyll nunca se rompe por esto.
- Estrategia de fallback: snapshot local == datos de la ultima sincronizacion ok.

Uso:
    python scripts/sync_datos.py            # descarga y escribe si es valido
    python scripts/sync_datos.py --local-only  # no toca la red (diagnostico)
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_DIR, "_data", "datos_publicos.json")

BASE_URL = "https://raw.githubusercontent.com/miravosqueinteresante/datos-publicos/main/www/datos"
SOURCES = (
    ("ande", "ande-indicadores.json"),
    ("itaipu", "itaipu-indicadores.json"),
    ("yacyreta", "yacyreta-indicadores.json"),
)
TIMEOUT = 60
REQUIRED_KEYS = ("id", "entidad_id", "indicador", "valor", "unidad")


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "muchotexto-sync/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def validate_payload(payload):
    """Estructura minima: lista de registros con las claves requeridas."""
    if not isinstance(payload, list) or not payload:
        return False
    for item in payload:
        if not isinstance(item, dict):
            return False
        for key in REQUIRED_KEYS:
            if key not in item:
                return False
    return True


def build_meta(payloads):
    n = sum(len(p) for p in payloads)
    return {
        "sincronizado": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "indicadores": n,
        "origen": "https://github.com/miravosqueinteresante/datos-publicos",
        "nota": "Snapshot por fallback. Si este archivo no se actualiza, la red "
                "no estaba disponible durante el ultimo build.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-only", action="store_true", help="no descarga, solo lee el snapshot actual")
    args = parser.parse_args()

    if args.local_only:
        with open(OUT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("Snapshot local: %d indicadores (sync %s)" %
              (data.get("_meta", {}).get("indicadores", 0), data.get("_meta", {}).get("sincronizado", "?")))
        return 0

    try:
        payloads = []
        for entidad, fname in SOURCES:
            url = "%s/%s" % (BASE_URL, fname)
            payload = fetch_json(url)
            if not validate_payload(payload):
                raise ValueError("Estructura invalida en %s" % url)
            payloads.append(payload)
            print("  OK %s: %d indicadores (%s)" % (entidad, len(payload), url))
    except Exception as exc:  # red, parseo o estructura: no romper el build
        print("  WARN: sync fallido (%s). Se conserva el snapshot local." % exc)
        print("  El sitio usa _data/datos_publicos.json del ultimo sync OK.")
        return 0

    combined = {"_meta": build_meta(payloads)}
    combined["indicadores"] = [r for p in payloads for r in p]

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print("OK: _data/datos_publicos.json = %d indicadores desde %s" % (len(combined["indicadores"]), BASE_URL))
    return 0


if __name__ == "__main__":
    sys.exit(main())