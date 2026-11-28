#!/usr/bin/env python3
"""
build_llms_full.py - Genera llms-full.txt con el contenido completo de los articulos clave.
Uso: python scripts/build_llms_full.py
"""
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(REPO, "_posts")
SITE_URL = "https://muchotexto.net"


def parse_front_matter(content):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if m:
        return m.group(1), content[m.end():]
    return "", content


def clean_markdown(body):
    text = re.sub(r'<script type="application/ld\+json">\s*\{[^<]*"@type"\s*:\s*"FAQPage"[^<]*\}</script>\s*', '', body, flags=re.DOTALL)
    text = re.sub(r'<script[^<]*</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'\{[%#][^}]*[%#]\}', '', text)
    return text.strip()


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    try:
        import yaml
    except ImportError:
        print("WARN: PyYAML no disponible.")
        return 1

    articles = []
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        content = open(path, encoding="utf-8").read()
        fm_str, body = parse_front_matter(content)
        try:
            data = yaml.safe_load(fm_str) or {}
        except Exception:
            continue

        title = str(data.get("title", "")).strip()
        if not title:
            continue

        url = data.get("permalink", "")
        if not url:
            url = "/" + os.path.basename(path)[:-3] + "/"

        pilar = data.get("pilar")
        if not isinstance(pilar, int):
            continue

        desc = str(data.get("description", "")).strip()
        resumen = str(data.get("resumen", "")).strip()
        clean_body = clean_markdown(body)

        articles.append({
            "title": title,
            "url": url,
            "pilar": pilar,
            "description": desc,
            "resumen": resumen,
            "body": clean_body,
            "date": str(data.get("date", "")),
        })

    lines = []
    lines.append("# muchotexto.net - Observatorio de IA en Paraguay")
    lines.append("")
    lines.append("> Contenido completo de los articulos de analisis para consumo por LLMs y agentes de IA.")
    lines.append("> Fuente: https://muchotexto.net/llms.txt (indice) y este archivo (contenido completo).")
    lines.append("")

    PILARES = {
        1: "Infraestructura y energia",
        2: "Geopolitica y regulacion tech",
        3: "IA, sociedad y trabajo",
        4: "Tecnologia aplicada + ecosistema",
        5: "Cultura, filosofia y futuro",
    }

    for n in sorted(PILARES):
        grupo = [a for a in articles if a["pilar"] == n]
        if not grupo:
            continue
        lines.append("## Pilar %d: %s" % (n, PILARES[n]))
        lines.append("")
        for a in grupo:
            lines.append("### %s" % a["title"])
            lines.append("URL: %s%s" % (SITE_URL, a["url"]))
            lines.append("Fecha: %s" % a["date"])
            if a["resumen"]:
                lines.append("Resumen: %s" % a["resumen"])
            elif a["description"]:
                lines.append("Descripcion: %s" % a["description"])
            lines.append("")
            lines.append(a["body"])
            lines.append("")
            lines.append("---")
            lines.append("")

    out_path = os.path.join(REPO, "llms-full.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("OK: llms-full.txt generado con %d articulos." % len(articles))


if __name__ == "__main__":
    sys.exit(main())
