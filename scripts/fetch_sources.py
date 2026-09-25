#!/usr/bin/env python3
"""
fetch_sources.py - Descarga el TEXTO de cada URL citada en un articulo y lo
guarda localmente, para que el fact-checker lea el contenido real en vez de
depender de una busqueda web que puede fallar.

Motivacion (error historico): verificadores marcaron claims como
UNVERIFIABLE porque no abrieron la fuente citada (Biggie/DATO, ABC Color,
LinkedIn de Full Digital). Este script elimina ese falso negativo: entrega
todas las fuentes ya descargadas + un indice con la cita textual.

Uso:
    python scripts/fetch_sources.py _posts/2026-09-26-slug.md
    python scripts/fetch_sources.py _posts/2026-09-26-slug.md --out research_x/sources

Salida:
    <out>/sources/NN.txt   (texto plano de cada URL)
    <out>/sources/INDEX.md (indice: numero, URL, estado, extracto)

Notas:
- Anti-bot: si la descarga directa falla (403/anti-bot), reintenta via
  r.jina.ai (lector de texto). Marca el metodo usado.
- Es read-only sobre el articulo; escribe solo en la carpeta de salida
  (gitignored por research_*/).
"""

import os
import re
import sys
import ssl
import time
import urllib.request
import urllib.error

TIMEOUT = 30
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def extract_urls(filepath):
    """Extrae URLs externas de los enlaces markdown del articulo, en orden."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    urls = re.findall(r"\((https?://[^\)\s]+)\)", content)
    seen = set()
    out = []
    for u in urls:
        u = u.rstrip(").,;")
        if "muchotexto.net" in u:
            continue
        if u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


def _get(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es,en;q=0.8"})
    resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
    raw = resp.read()
    return resp.status, raw, resp.headers


def _strip_html(html):
    # Quita scripts/styles y etiquetas, colapsa espacios.
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&#8217;|&rsquo;|&#039;|&apos;", "'", text)
    text = re.sub(r"&quot;|&#8220;|&#8221;|&ldquo;|&rdquo;", '"', text)
    text = re.sub(r"&aacute;", "á", text)
    text = re.sub(r"&eacute;", "é", text)
    text = re.sub(r"&iacute;", "í", text)
    text = re.sub(r"&oacute;", "ó", text)
    text = re.sub(r"&uacute;", "ú", text)
    text = re.sub(r"&ntilde;", "ñ", text)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def _decode(raw, headers):
    """Decodifica bytes respetando el charset declarado, con fallback amplio."""
    charset = None
    ctype = headers.get("Content-Type", "") if headers else ""
    m = re.search(r"charset=([\w-]+)", ctype, re.I)
    if m:
        charset = m.group(1)
    html = None
    head = raw[:2000].decode("ascii", "ignore")
    m2 = re.search(r'charset=["\']?([\w-]+)', head, re.I)
    if m2:
        charset = m2.group(1)
    for enc in [charset, "utf-8", "latin-1"]:
        if not enc:
            continue
        try:
            html = raw.decode(enc)
            break
        except (UnicodeDecodeError, LookupError):
            continue
    if html is None:
        html = raw.decode("utf-8", "replace")
    return html


def fetch(url):
    """Devuelve (estado, metodo, texto). Metodo: direct | jina | fallo."""
    # 1) Descarga directa
    status = "ERR"
    try:
        status, raw, headers = _get(url)
        if status == 200:
            html = _decode(raw, headers)
            text = _strip_html(html)
            if len(text) > 300:
                return status, "direct", text
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception:
        pass

    # 2) Fallback via Jina Reader (maneja 403/anti-bot y paginas JS)
    try:
        jina = "https://r.jina.ai/" + url
        s2, raw2, _h = _get(jina)
        text2 = raw2.decode("utf-8", "replace").strip()
        if s2 == 200 and len(text2) > 200:
            return s2, "jina", text2
    except Exception:
        pass

    return status, "fallo", ""


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/fetch_sources.py _posts/2026-09-26-slug.md [--out carpeta]")
        sys.exit(1)

    post = sys.argv[1]
    out = None
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    if not out:
        slug = os.path.splitext(os.path.basename(post))[0]
        out = os.path.join("research_" + slug.split("-", 3)[-1][:40], "sources")

    src_dir = out
    os.makedirs(src_dir, exist_ok=True)

    urls = extract_urls(post)
    if not urls:
        print("No se encontraron URLs externas en el articulo.")
        sys.exit(0)

    print(f"Descargando {len(urls)} fuentes a {src_dir}/\n")
    index = ["# Indice de fuentes descargadas", "",
             f"Articulo: `{post}`  ",
             f"Fuentes: {len(urls)}", ""]

    ok = 0
    for i, url in enumerate(urls, 1):
        status, method, text = fetch(url)
        fn = f"{i:02d}.txt"
        path = os.path.join(src_dir, fn)
        if text:
            header = f"URL: {url}\nMETODO: {method}\n\n"
            with open(path, "w", encoding="utf-8") as f:
                f.write(header + text)
            ok += 1
            extracto = re.sub(r"\s+", " ", text)[:160]
            index.append(f"{i}. `{url}`")
            index.append(f"   - metodo: {method} | chars: {len(text)}")
            index.append(f"   - extracto: {extracto}...")
            index.append(f"   - archivo: {fn}")
            index.append("")
            print(f"  [{method:6}] {status}  {fn}  {url[:70]}")
        else:
            index.append(f"{i}. `{url}`")
            index.append(f"   - NO DESCARGADA (metodo: {method}, estado: {status})")
            index.append(f"   - abrir manualmente en navegador")
            index.append("")
            print(f"  [FALLO ] {status}  ---  {url[:70]}")
        time.sleep(0.5)

    with open(os.path.join(src_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index))

    print(f"\n{ok}/{len(urls)} fuentes descargadas en {src_dir}/")
    print(f"Indice: {os.path.join(src_dir, 'INDEX.md')}")
    if ok < len(urls):
        print("Las no descargadas pueden requerir navegador (paywall/anti-bot duro); revisar INDEX.md.")


if __name__ == "__main__":
    main()
