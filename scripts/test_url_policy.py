#!/usr/bin/env python3
"""Test de la política de 403 anti-bot."""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import url_policy as up  # noqa: E402


class TestUrlPolicy(unittest.TestCase):
    def test_allowlist_exacta_y_subdominio(self):
        domains = {"bcp.gov.py", "dni.gov"}
        self.assertTrue(up.is_allowed_403("https://www.bcp.gov.py/x", domains))
        self.assertTrue(up.is_allowed_403("https://bcp.gov.py/x", domains))
        self.assertTrue(up.is_allowed_403("https://www.dni.gov/x", domains))

    def test_rechaza_dominio_ajeno(self):
        self.assertFalse(up.is_allowed_403("https://example.com/x", {"bcp.gov.py"}))

    def test_no_confunde_sufijo(self):
        self.assertFalse(up.is_allowed_403("https://fakebcp.gov.py/x", {"bcp.gov.py"}))

    def test_homepage_allowlist_exacta_y_subdominio(self):
        domains = {"ande.gov.py", "worldbank.org"}
        self.assertTrue(up.is_allowed_homepage("https://www.ande.gov.py/", domains))
        self.assertTrue(up.is_allowed_homepage("https://ande.gov.py/", domains))
        self.assertTrue(up.is_allowed_homepage("https://www.worldbank.org/", domains))

    def test_homepage_rechaza_dominio_ajeno(self):
        self.assertFalse(up.is_allowed_homepage("https://example.com/", {"ande.gov.py"}))


if __name__ == "__main__":
    unittest.main()
