#!/usr/bin/env python3
"""Reescribe titulares y descripciones de Pulso y Editorial con Gemini.

Idempotente: marca `title_ai: true` / `description_ai: true` y saltea lo ya
procesado. Uso:
    python scripts/rewrite_descriptions.py --fields both --workers 3
    python scripts/rewrite_descriptions.py --fields title --only editorial
    python scripts/rewrite_descriptions.py --dry-run
"""

import argparse
import glob
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gemini_client import (
    TITLE_MAX,
    clean_title,
    fallback_meta_description,
    fallback_title,
    validate_meta_description,
    validate_title,
    write_meta_description,
    write_title,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "_posts")
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
CATEGORIES = {"pulso": "pulso-paraguay", "editorial": "editorial"}
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

lock = threading.Lock()
taken = set()


def parse(path):
    with open(path, encoding="utf-8-sig") as fh:
        text = fh.read()
    m = FM.match(text)
    if not m:
        return None
    return {"path": path, "fm": m.group(1), "body": text[m.end():]}


def field(fm, key):
    m = re.search(rf'^{key}:\s*"?(.*?)"?$', fm, re.M)
    return m.group(1) if m else ""


def is_marked(fm, key):
    return bool(re.search(rf"^{key}_ai:\s*true", fm, re.M))


def set_field(fm, key, value, marker):
    lines = [ln for ln in fm.split("\n") if not ln.startswith(f"{marker}:")]
    out, replaced = [], False
    for line in lines:
        if re.match(rf"^{key}:\s", line):
            out += [f'{key}: "{value}"', f"{marker}: true"]
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out += [f'{key}: "{value}"', f"{marker}: true"]
    return "\n".join(out)


def reserve_is_free(candidate):
    """Reserva un titular si está libre. Devuelve True si lo tomó."""
    key = candidate.casefold()
    with lock:
        if key in taken:
            return False
        taken.add(key)
        return True


def disambiguate(candidate, date):
    """Añade la fecha para garantizar unicidad cuando el modelo repite titular."""
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date or "")
    suffix = f" · {int(m.group(3))} {MESES[int(m.group(2)) - 1]}" if m else " · Paraguay"
    base = candidate[: TITLE_MAX - len(suffix)].rstrip(" ,;:-.")
    out = base + suffix
    with lock:
        taken.add(out.casefold())
    return out


def process(rec, api_key, want_title, want_desc, category):
    fm, body = rec["fm"], rec["body"]
    new_title, new_desc = None, None

    if want_title:
        candidate = write_title(
            body, current_title=field(fm, "title"), api_key=api_key,
            category=category, is_taken=lambda t: re.sub(r"\s+", " ", t).casefold() in taken,
        )
        candidate = candidate or fallback_title(body)
        candidate, problems = validate_title(candidate)
        if problems:
            candidate = fallback_title(body)
        if not reserve_is_free(candidate):
            candidate = disambiguate(candidate, field(fm, "date"))
        new_title = candidate

    if want_desc:
        new_desc = write_meta_description(new_title or field(fm, "title"), body, api_key, category)
        new_desc = (new_desc or fallback_meta_description(body)).replace('"', "'")

    new_fm = fm
    if new_title:
        new_fm = set_field(new_fm, "title", new_title.replace('"', ""), "title_ai")
    if new_desc:
        new_fm = set_field(new_fm, "description", new_desc, "description_ai")

    with open(rec["path"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write("---\n" + new_fm + "\n---\n" + body)
    return f"{os.path.basename(rec['path'])} | {new_title or '-'} | {len((new_desc or '').encode())}b"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", choices=["pulso", "editorial", "all"], default="all")
    ap.add_argument("--fields", choices=["title", "desc", "both"], default="both")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--sleep", type=float, default=0.3)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    want_title = args.fields in ("title", "both")
    want_desc = args.fields in ("desc", "both")
    targets = [CATEGORIES[args.only]] if args.only != "all" else list(CATEGORIES.values())

    records, queue = [], []
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        rec = parse(path)
        if not rec:
            continue
        cat = field(rec["fm"], "categories").strip()
        records.append((path, cat, rec))
        if cat not in targets:
            continue
        need_t = want_title and not (is_marked(rec["fm"], "title") and not validate_title(field(rec["fm"], "title"))[1])
        need_d = want_desc and not (is_marked(rec["fm"], "description") and not validate_meta_description(field(rec["fm"], "description"))[1])
        if need_t or need_d:
            queue.append((rec, cat, need_t, need_d))

    with lock:
        for _, _, rec in records:
            taken.add(clean_title(field(rec["fm"], "title")).casefold())
        for rec, _, need_t, _ in queue:
            if need_t:  # su propio titular se reescribe: libera el lugar
                taken.discard(clean_title(field(rec["fm"], "title")).casefold())

    if args.limit:
        queue = queue[: args.limit]
    print(f"En cola: {len(queue)} posts (títulos={want_title}, descripciones={want_desc})")
    if args.dry_run or not queue:
        for rec, _, a, b in queue:
            print(f"[dry] {os.path.basename(rec['path'])} title={a} desc={b}")
        return 0

    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(process, rec, api_key, a, b, CATEGORIES["pulso"] if cat == "pulso-paraguay" else "editorial")
            for rec, cat, a, b in queue
        ]
        for fut in futures:
            try:
                print("OK", fut.result())
                done += 1
            except Exception as e:  # nosec: se reporta y sigue
                print("ERROR", e)
            time.sleep(args.sleep)

    print(f"\nProcesados: {done}/{len(queue)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
