#!/usr/bin/env python3
"""Test del generador de manifiestos de cobertura."""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import backfill_observatorio as bf  # noqa: E402


class TestBackfill(unittest.TestCase):
    def test_entrada_actualizada(self):
        row = {s: "updated" for s in bf.DERIVED}
        row.update({s: "linked" for s in bf.OPTIONAL})
        row["slug"] = "x"
        entry = bf.build_entry(row)
        self.assertTrue(all(v == "updated" for v in entry["superficies"].values()))
        self.assertEqual(entry["motivos"], {})

    def test_entrada_n_a_exige_motivo(self):
        row = {s: "n/a" for s in bf.DERIVED + bf.OPTIONAL}
        row["slug"] = "x"
        entry = bf.build_entry(row)
        self.assertEqual(entry["superficies"]["radar"], "n/a")
        self.assertTrue(entry["motivos"]["radar"])


if __name__ == "__main__":
    unittest.main()
