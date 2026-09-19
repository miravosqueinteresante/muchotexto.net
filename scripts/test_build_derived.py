#!/usr/bin/env python3
"""
test_build_derived.py — tests del motor de superficies derivadas.

Sin framework externo: `python scripts/test_build_derived.py` (unittest).
Cubre los transforms (item del front matter -> item de la superficie), los
helpers, la deduplicacion y la determinismo/esquema del motor.
"""

import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_derived as bd  # noqa: E402

CTX = {"url": "/articulos/2026/09/16/x/", "title": "Titulo del articulo"}


class TestHelpers(unittest.TestCase):
    def test_fmt_fecha(self):
        self.assertEqual(bd.fmt_fecha("2026-09-17"), "17 Septiembre 2026")

    def test_fmt_fecha_invalida(self):
        self.assertEqual(bd.fmt_fecha("no-es-fecha"), "no-es-fecha")

    def test_seccion_por_anio(self):
        self.assertEqual(bd.seccion_por_anio(1990), "1973 — 2009")
        self.assertEqual(bd.seccion_por_anio(2015), "2010 — 2019")
        self.assertEqual(bd.seccion_por_anio(2022), "2020 — 2023")
        self.assertEqual(bd.seccion_por_anio(2024), "2024")
        self.assertEqual(bd.seccion_por_anio(2025), "2025")
        self.assertEqual(bd.seccion_por_anio(2026), "2026")
        self.assertEqual(bd.seccion_por_anio(2030), "2026")

    def test_slug_to_url(self):
        p = os.path.join(bd.POSTS, "2026-09-16-los-contratos.md")
        self.assertEqual(bd.slug_to_url(p), "/articulos/2026/09/16/los-contratos/")

    def test_norm(self):
        self.assertEqual(bd.norm("César SÁNCHEZ"), "cesar sanchez")


class TestTransforms(unittest.TestCase):
    def test_hito_valido(self):
        res = bd._hito({"fecha": "2026-09-17", "texto": "Hola"}, CTX)
        self.assertIsNotNone(res)
        sec, it = res
        self.assertEqual(sec, "2026")
        self.assertEqual(it["orden"], "2026-09-17")
        self.assertEqual(it["fecha"], "17 Septiembre 2026")
        self.assertIn("[Leer análisis](/articulos/2026/09/16/x/)", it["texto"])

    def test_hito_futuro(self):
        sec, _ = bd._hito({"fecha": "2027-01-01", "texto": "X", "futuro": True}, CTX)
        self.assertEqual(sec, "Lo que viene")

    def test_hito_incompleto(self):
        self.assertIsNone(bd._hito({"texto": "sin fecha"}, CTX))
        self.assertIsNone(bd._hito({"fecha": "2026-09-17"}, CTX))

    def test_glosario_valido(self):
        sec, it = bd._glosario({"termino": "GPU", "definicion": "Chip"}, CTX)
        self.assertEqual(sec, "Del observatorio")
        self.assertEqual(it, {"termino": "GPU", "definicion": "Chip"})

    def test_glosario_con_link(self):
        _, it = bd._glosario({"termino": "GCIE", "definicion": "d", "tema": "Energía",
                              "link": "/a/", "link_text": "ver"}, CTX)
        self.assertEqual(it["link"], "/a/")
        self.assertEqual(it["link_text"], "ver")

    def test_glosario_incompleto(self):
        self.assertIsNone(bd._glosario({"termino": "", "definicion": "d"}, CTX))
        self.assertIsNone(bd._glosario({"termino": "X", "definicion": ""}, CTX))

    def test_caso_usa_titulo_del_articulo(self):
        sec, it = bd._caso({"texto": "t", "tema": "Energía"}, CTX)
        self.assertEqual(sec, "Energía")
        self.assertEqual(it["titulo"], "Titulo del articulo")
        self.assertEqual(it["url"], CTX["url"])

    def test_caso_incompleto(self):
        self.assertIsNone(bd._caso({"tema": "Energía"}, CTX))

    def test_directorio_valido(self):
        sec, it = bd._directorio({"nombre": "N", "descripcion": "D", "seccion": "S"}, CTX)
        self.assertEqual(sec, "S")
        self.assertEqual(it, {"nombre": "N", "descripcion": "D"})

    def test_directorio_incompleto(self):
        self.assertIsNone(bd._directorio({"nombre": "N"}, CTX))


class TestDedup(unittest.TestCase):
    def test_glosario_ignora_mayusculas(self):
        d = bd.SURFACES["glosario"]["dedup"]
        self.assertEqual(d("T", {"termino": "GPU"}), d("T", {"termino": "gpu"}))

    def test_casos_por_titulo(self):
        d = bd.SURFACES["casos"]["dedup"]
        self.assertEqual(d("Energía", {"titulo": "GCIE"}), d("Energía", {"titulo": "gcie"}))
        self.assertNotEqual(d("Energía", {"titulo": "GCIE"}), d("Salud", {"titulo": "GCIE"}))


class TestMotor(unittest.TestCase):
    def test_determinista(self):
        import yaml
        for name in bd.SURFACES:
            with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
                bd.build_surface(name, yaml, out_dir=t1)
                bd.build_surface(name, yaml, out_dir=t2)
                a = open(os.path.join(t1, bd.SURFACES[name]["out"]), encoding="utf-8").read()
                b = open(os.path.join(t2, bd.SURFACES[name]["out"]), encoding="utf-8").read()
                self.assertEqual(a, b, f"{name} no es determinista")

    def test_esquema(self):
        import yaml
        for name, cfg in bd.SURFACES.items():
            with tempfile.TemporaryDirectory() as tmp:
                bd.build_surface(name, yaml, out_dir=tmp)
                data = yaml.safe_load(open(os.path.join(tmp, cfg["out"]), encoding="utf-8"))
                self.assertIsInstance(data, list)
                self.assertTrue(data, f"{name}: salida vacia")
                for grupo in data:
                    self.assertIn(cfg["section_key"], grupo)
                    self.assertIn(cfg["item_key"], grupo)


if __name__ == "__main__":
    unittest.main(verbosity=2)