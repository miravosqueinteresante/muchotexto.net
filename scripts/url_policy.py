#!/usr/bin/env python3
"""Política compartida de 403 anti-bot para check_urls y validate_publish."""

import os
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOWLIST = os.path.join(HERE, "url_403_allowlist.txt")


def load_allowlist(path=ALLOWLIST):
    domains = set()
    if not os.path.exists(path):
        return domains
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().lower()
            if line and not line.startswith("#"):
                domains.add(line)
    return domains


def is_allowed_403(url, domains=None):
    domains = load_allowlist() if domains is None else domains
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in domains)
