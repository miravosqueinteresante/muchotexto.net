#!/usr/bin/env python3
"""Valida que el manifiesto de cierre cubra todos los análisis y use estados válidos."""

import re
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
MANIFEST = REPO / "_data" / "cierres.yml"
NON_ANALYSIS = {
    "2026-05-10-primer-articulo",
    "2026-06-10-que-es-realmente-el-futbol",
}
VALID = {"completo", "parcial", "legacy"}


def analysis_slugs():
    slugs = set()
    for path in (REPO / "_posts").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not match:
            continue
        data = yaml.safe_load(match.group(1)) or {}
        categories = data.get("categories") or []
        if isinstance(categories, str):
            categories = [categories]
        if "articulos" in categories and data.get("pilar") and path.stem not in NON_ANALYSIS:
            slugs.add(path.stem)
    return slugs


class TestCierres(unittest.TestCase):
    def setUp(self):
        self.data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
        self.entries = {e["slug"]: e for e in self.data["cierres"]}

    def test_cobertura(self):
        self.assertEqual(set(self.entries), analysis_slugs())

    def test_estados(self):
        for slug, entry in self.entries.items():
            self.assertIn(entry["estado"], VALID, slug)
            if entry["estado"] == "legacy":
                self.assertTrue(entry.get("motivo"), slug)
            if entry["estado"] == "completo":
                self.assertTrue(entry.get("research_dir"), slug)
                self.assertEqual(entry.get("faltantes"), [], slug)

    def test_sin_duplicados(self):
        slugs = [e["slug"] for e in self.data["cierres"]]
        self.assertEqual(len(slugs), len(set(slugs)))


if __name__ == "__main__":
    unittest.main()
