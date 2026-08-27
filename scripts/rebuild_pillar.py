#!/usr/bin/env python3
"""Audit ia-en-paraguay.markdown: list articulos posts not linked from the pillar.

Read-only. Never writes. Was an -obsolete static dump- that overwrote the
pillar with a stale template; replaced with this verifier so it cannot break
the page again.
"""
import glob
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PILLAR = REPO / "ia-en-paraguay.markdown"
POSTS = REPO / "_posts"

def articulos_posts():
    posts = {}
    for f in sorted(glob.glob(str(POSTS / "*.md"))):
        text = Path(f).read_text(encoding="utf-8")
        if re.search(r"categories:\s*[\w\s-]*articulos", text):
            slug = Path(f).stem
            m = re.search(r'title: "([^"]+)"', text)
            posts[slug] = m.group(1) if m else slug
    return posts

def main():
    if not PILLAR.exists():
        print(f"ERROR: no existe {PILLAR}")
        return 1

    pillar = PILLAR.read_text(encoding="utf-8")
    linked = set(re.findall(r"post_url\s+([\w-]+)", pillar))

    missing, linked_dangling = [], []
    for slug, title in sorted(articulos_posts().items()):
        if slug not in linked:
            missing.append((slug, title))
        else:
            # verify the linked slug actually has a post (dangling post_url?)
            if not (POSTS / f"{slug}.md").exists():
                linked_dangling.append(slug)

    print(f"Pilar: {PILLAR.name}")
    print(f"Artículos 'articulos': {len(missing) + len(linked)} | enlazados: {len(linked)} | sin enlazar: {len(missing)}")
    if missing:
        print("\nNO referenciados en la pilar (agregar a la sección del pilar a mano):")
        for slug, title in missing:
            print(f"  - {slug}  |  {title[:80]}")
    if linked_dangling:
        print("\nOJO: post_url en la pilar que no tienen archivo (romperían el build):")
        for slug in linked_dangling:
            print(f"  - {slug}")
    print("\nLa pilar se edita a mano. No se escribió ningún archivo.")
    return 0 if (not missing and not linked_dangling) else 1

if __name__ == "__main__":
    raise SystemExit(main())