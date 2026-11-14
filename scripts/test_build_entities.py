#!/usr/bin/env python3
"""Test del override manual de artículos en entidades."""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_entities as be  # noqa: E402


class TestManualArticles(unittest.TestCase):
    def test_agrega_y_no_duplica(self):
        related = [{"title": "Existente", "url": "/a/", "date": "", "context": "", "score": 1}]
        entity = {"manual_articles": [
            {"title": "Existente", "url": "/a/", "context": "dup"},
            {"title": "Nuevo", "url": "/b/", "context": "ctx"},
        ]}
        out = be.merge_manual_articles(related, entity)
        self.assertEqual({a["url"] for a in out}, {"/a/", "/b/"})
        self.assertEqual(next(a for a in out if a["url"] == "/a/")["context"], "dup")
        self.assertTrue(all(a["score"] == 2 for a in out))


if __name__ == "__main__":
    unittest.main()
