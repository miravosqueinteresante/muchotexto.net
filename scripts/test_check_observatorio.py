#!/usr/bin/env python3
"""Test del gate de cobertura del observatorio."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import check_observatorio as co  # noqa: E402

POST = """---
title: "Artículo de prueba"
permalink: /articulos/2026/01/01/prueba/
---

Cuerpo.
"""

MANIFEST = """2026-01-01-prueba:
  superficies:
    pilar: updated
    llms: updated
    cronologia: n/a
    glosario: n/a
    casos: n/a
    directorio: n/a
    radar: n/a
    regulacion: n/a
    claims: n/a
    entidades: n/a
    grafo: n/a
  motivos:
    cronologia: "Sin hitos."
    glosario: "Sin términos."
    casos: "Sin casos."
    directorio: "Sin entrada."
    radar: "Sin ley."
    regulacion: "Sin ley."
    claims: "Sin claims."
    entidades: "Sin entidad."
    grafo: "Sin entidad."
"""


class TestObservatorio(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "_posts").mkdir()
        (self.root / "_data").mkdir()
        (self.root / "_posts" / "2026-01-01-prueba.md").write_text(POST, encoding="utf-8")
        (self.root / "_data" / "observatorio.yml").write_text(MANIFEST, encoding="utf-8")
        (self.root / "ia-en-paraguay.markdown").write_text(
            "{% post_url 2026-01-01-prueba %}", encoding="utf-8")
        (self.root / "llms.txt").write_text(
            "https://muchotexto.net/articulos/2026/01/01/prueba/", encoding="utf-8")
        self.old_repo, self.old_manifest = co.REPO, co.MANIFEST
        co.REPO = str(self.root)
        co.MANIFEST = str(self.root / "_data" / "observatorio.yml")

    def tearDown(self):
        co.REPO, co.MANIFEST = self.old_repo, self.old_manifest
        self.tmp.cleanup()

    def test_pasa_manifest_completo(self):
        self.assertEqual(co.check_post(str(self.root / "_posts" / "2026-01-01-prueba.md")), [])

    def test_falla_si_falta_url_en_superficie(self):
        (self.root / "llms.txt").write_text("sin enlace", encoding="utf-8")
        errors = co.check_post(str(self.root / "_posts" / "2026-01-01-prueba.md"))
        self.assertTrue(any("'llms'" in e for e in errors), errors)

    def test_falla_si_falta_motivo_n_a(self):
        (self.root / "_data" / "observatorio.yml").write_text(
            MANIFEST.replace('    grafo: "Sin entidad."\n', ""), encoding="utf-8")
        errors = co.check_post(str(self.root / "_posts" / "2026-01-01-prueba.md"))
        self.assertTrue(any("'grafo'" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
