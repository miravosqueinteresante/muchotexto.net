#!/usr/bin/env python3
"""Reescribe las descripciones de Pulso y Editorial con Gemini.

Idempotente: escribe `description_ai: true` y saltea los posts ya procesados.
Uso:
    python scripts/rewrite_descriptions.py --limit 50 --only pulso
    python scripts/rewrite_descriptions.py --dry-run
"""

import argparse
import glob
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gemini_client import (
    fallback_meta_description,
    validate_meta_description,
    write_meta_description,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "_posts")
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
CATEGORIES = {"pulso": "pulso-paraguay", "editorial": "editorial"}


def split_post(text):
    m = FM.match(text)
    if not m:
        return None, ""
    return m.group(1), text[m.end():]


def set_description(fm, desc):
    lines = [ln for ln in fm.split("\n") if not ln.startswith("description_ai:")]
    out, replaced = [], False
    for line in lines:
        if re.match(r"^description:\s", line):
            out.append(f'description: "{desc}"')
            out.append("description_ai: true")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out.append(f'description: "{desc}"')
        out.append("description_ai: true")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", choices=["pulso", "editorial", "all"], default="all")
    ap.add_argument("--sleep", type=float, default=2.0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    targets = [CATEGORIES[args.only]] if args.only != "all" else list(CATEGORIES.values())

    done = skipped = fallback = failed = 0
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        with open(path, encoding="utf-8-sig") as fh:
            text = fh.read()
        fm, body = split_post(text)
        if fm is None:
            continue
        cm = re.search(r"^categories:\s*\[?([^\]\n]+)", fm, re.M)
        if not cm or cm.group(1).strip() not in targets:
            continue

        current = re.search(r'^description:\s*"?(.*?)"?$', fm, re.M)
        current = current.group(1) if current else ""
        marked = re.search(r"^description_ai:\s*true", fm, re.M)
        if marked and not validate_meta_description(current)[1]:
            skipped += 1
            continue
        if args.limit and done + fallback + failed >= args.limit:
            break
        if args.dry_run:
            print(f"[dry] {os.path.basename(path)} ({len(current.encode())} bytes)")
            done += 1
            continue

        tm = re.search(r'^title:\s*"?(.*?)"?$', fm, re.M)
        category = "pulso" if "pulso-paraguay" in targets else "editorial"
        desc = write_meta_description(
            title=tm.group(1) if tm else "",
            body=body,
            api_key=api_key,
            category=category,
        )
        if desc:
            done += 1
        else:
            desc = fallback_meta_description(body)
            fallback += 1
            print(f"FALLBACK {os.path.basename(path)}")

        desc = desc.replace('"', "'")
        new_text = "---\n" + set_description(fm, desc) + "\n---\n" + body
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new_text)
        print(f"OK {os.path.basename(path)} ({len(desc.encode())} bytes)")
        time.sleep(args.sleep)

    print(f"\nProcesados: {done} | fallback: {fallback} | ya tenían: {skipped}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
