#!/usr/bin/env python3
"""Test del gate de enlaces internos de validate_publish.py."""

import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import validate_publish as vp  # noqa: E402

PILAR = "[Observatorio](/ia-en-paraguay/)"
FAQ = '<script type="application/ld+json">{"@type": "FAQPage"}</script>'


def post_body(links: str) -> str:
    return f"""---
layout: post
title: "Artículo de prueba"
description: "Descripción de prueba con acentos y longitud suficiente para validar el artículo."
categories: articulos
---

Cuerpo de prueba. {PILAR}

{links}

{FAQ}
"""


class TestInternalLinks(unittest.TestCase):
    def test_no_cuenta_la_pilar(self):
        body = f"{PILAR}\n[Artículo]({{% post_url 2026-05-16-peter-thiel-paraguay-experimento %}})"
        links = vp.count_contextual_internal_links(body)
        self.assertEqual(len(links), 1)
        self.assertFalse(any("ia-en-paraguay" in link for link in links))

    def test_deduplica(self):
        body = "[Uno](/a/) [Dos](/a/) [Tres]({% post_url 2026-05-16-peter-thiel-paraguay-experimento %})"
        self.assertEqual(len(vp.count_contextual_internal_links(body)), 2)

    def test_gate_falla_sin_enlaces_contextuales(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(post_body(""))
            path = f.name
        try:
            errors, _ = vp.check_post(path, [], require_cierre=False)
            self.assertTrue(
                any("Enlaces internos contextuales insuficientes" in e for e in errors),
                errors,
            )
        finally:
            os.unlink(path)

    def test_gate_pasa_con_dos_enlaces(self):
        links = (
            "[Thiel]({% post_url 2026-05-16-peter-thiel-paraguay-experimento %}) "
            "[QR]({% post_url 2026-10-20-qr-hub-paraguay %})"
        )
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(post_body(links))
            path = f.name
        try:
            errors, _ = vp.check_post(path, [], require_cierre=False)
            self.assertFalse(
                any("Enlaces internos contextuales insuficientes" in e for e in errors),
                errors,
            )
        finally:
            os.unlink(path)

    def test_cli_bloquea_sin_enlaces(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(post_body(""))
            path = f.name
        try:
            result = subprocess.run(
                [sys.executable, os.path.join(HERE, "validate_publish.py"), "--check", path],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("Enlaces internos contextuales insuficientes", result.stdout)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
