#!/usr/bin/env python3
"""
validate_publish.py - Pre-commit hook para validar articulos antes de publicar.

Modo pre-commit (sin args): detecta cambios en _posts/ y valida.
Modo manual: python scripts/validate_publish.py --check _posts/2026-07-10-slug.md
"""

import os
import re
import sys
import glob
import subprocess

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_DIR, "_posts")
EXIT_PASS = 0
EXIT_FAIL = 1

CLICKBAIT = [
    "increible", "nadie te dice", "la verdad sobre",
    "todos deberian", "nunca imaginaste", "cambiarlo todo",
    "lo que nadie", "te sorprendera",
]

ALTERNATIVAS_COLON = (
    "Usar estructura sin dos puntos. Alternativas:\n"
    "  - Verbo conjugado: 'Paraguay aprobo una ley que cambia las reglas'\n"
    "  - Conector causal: 'Por que Paraguay es el ultimo pais que apuesta por Taiwan'\n"
    "  - Preposicion: 'Sin red de 500 kV no hay IA en Paraguay'\n"
    "  - Sujeto + predicado lineal: 'Paraguay tiene energia pero no la red para transportarla'"
)


def get_staged_posts() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True, cwd=REPO_DIR
    )
    if result.returncode != 0:
        return []
    files = [f for f in result.stdout.strip().split("\n") if f.startswith("_posts/") and f.endswith(".md")]
    return files


def get_last_n_posts(n: int = 3) -> list[dict]:
    posts = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")), reverse=True)
    result = []
    for p in posts:
        content = read_file(p)
        title = extract_frontmatter_field(content, "title")
        categories = extract_frontmatter_field(content, "categories", "").strip()
        if categories == "articulos" and title:
            result.append({"file": os.path.basename(p), "title": title})
            if len(result) >= n:
                break
    return result


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def extract_frontmatter_field(content: str, field: str, default: str = "") -> str:
    match = re.search(rf"^{field}:\s*\"?(.*?)\"?\s*$", content, re.MULTILINE)
    if match:
        return match.group(1).strip().rstrip('"')
    return default


def extract_body(content: str) -> str:
    match = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
    if len(match) >= 3:
        return match[2].strip()
    return ""


def check_title(title: str, ultimos_3: list[dict]) -> tuple[list[str], list[str]]:
    errors = []
    warnings = []

    if len(title) > 70:
        errors.append(f"Titulo excede 70 caracteres ({len(title)} chars)")

    if "!" in title:
        errors.append("Titulo contiene signo de exclamacion")

    if ":" in title:
        errors.append(f"Titulo usa formula '[X]: [Y]'. {ALTERNATIVAS_COLON}")

    if "?" in title:
        preguntas = sum(1 for p in ultimos_3 if "?" in p["title"])
        if preguntas >= 1:
            errors.append(
                "Titulo usa pregunta, pero ya hay preguntas en los ultimos 3 articulos. "
                "Usar afirmacion. Maximo 1 de cada 5 articulos puede ser pregunta."
            )

    for palabra in CLICKBAIT:
        if palabra in title.lower():
            errors.append(f"Patron de clickbait detectado: '{palabra}'")

    titulos_prev = [p["title"] for p in ultimos_3]
    for prev in titulos_prev:
        if title[:30].lower() == prev[:30].lower():
            warnings.append(
                f"Los primeros 30 caracteres del titulo coinciden con '{prev[:50]}...'. "
                "Variar la apertura."
            )

    return errors, warnings


def check_post(post_path: str, ultimos_3: list[dict]) -> tuple[list[str], list[str]]:
    errors = []
    warnings = []
    content = read_file(post_path)

    if not content:
        return ["No se pudo leer el archivo"], []

    title = extract_frontmatter_field(content, "title")
    description = extract_frontmatter_field(content, "description")
    categories = extract_frontmatter_field(content, "categories", "")
    body = extract_body(content)

    if not title:
        errors.append("No se encontro titulo en el frontmatter")
        return errors, warnings

    e, w = check_title(title, ultimos_3)
    errors.extend(e)
    warnings.extend(w)

    if not categories:
        errors.append("Categoria no definida en frontmatter")

    if '"@type": "FAQPage"' not in content and '"@type":"FAQPage"' not in content:
        errors.append("FAQ schema requerido: agregar FAQPage con 3 preguntas")

    if "/ia-en-paraguay/" not in content:
        errors.append("Falta enlace a pagina pilar /ia-en-paraguay/ en el cuerpo del articulo")

    # === INTERNAL LINKS ===
    internal_links = len(re.findall(r'\{% post_url [^%]+\%\}', body))
    if internal_links < 2:
        warnings.append(f"Pocos links internos: {internal_links} (minimo 2 recomendados)")

    # === URL HEALTH CHECK (solo en modo --check) ===
    urls = re.findall(r'\((https?://[^\)]+)\)', body)
    external_urls = [u for u in urls if 'muchotexto.net' not in u]
    if external_urls:
        try:
            import urllib.request
            import ssl
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            broken = 0
            for url in external_urls[:10]:  # max 10 para no bloquear
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'muchotexto-validator/1.0'})
                    resp = urllib.request.urlopen(req, timeout=5, context=ctx)
                    if resp.status != 200:
                        broken += 1
                except:
                    broken += 1
            if broken > 0:
                warnings.append(f"URLs posiblemente rotas: {broken}/{len(external_urls[:10])} (verificar con scripts/check_urls.py)")
        except:
            pass  # si falla el import, no bloquea

    if not description:
        warnings.append("Meta description no definida en frontmatter")
    elif len(description) > 155:
        warnings.append(f"Meta description muy larga: {len(description)} chars (max 155)")

    # === ACENTOS FALTANTES ===
    missing_accents = []
    checks = [
        (r'\bmas\b', 'm\u00e1s'),
        (r'\besta\b', 'est\u00e1'),
        (r'\bpais\b', 'pa\u00eds'),
        (r'\benergia\b', 'energ\u00eda'),
        (r'\bregion\b', 'regi\u00f3n'),
        (r'\bregulacion\b', 'regulaci\u00f3n'),
        (r'\btecnologia\b', 'tecnolog\u00eda'),
        (r'\binformatica\b', 'inform\u00e1tica'),
        (r'\beducacion\b', 'educaci\u00f3n'),
        (r'\banalisis\b', 'an\u00e1lisis'),
        (r'\bgeopolitica\b', 'geopol\u00edtica'),
        (r'\bdeberian\b', 'deber\u00edan'),
        (r'\beconomia\b', 'econom\u00eda'),
        (r'\belectrica\b', 'el\u00e9ctrica'),
        (r'\btransmision\b', 'transmisi\u00f3n'),
    ]
    for pattern, correct in checks:
        text_to_check = f"{title or ''} {description or ''}"
        match = re.search(pattern, text_to_check, re.IGNORECASE)
        if match:
            found = match.group(0)
            missing_accents.append(f"'{found}' deberia ser '{correct}'")

    if missing_accents:
        errors.append("ACENTOS FALTANTES en titulo o description: " + ", ".join(missing_accents))

    # === CHECK: texto 100% ASCII (sin acentos) ===
    non_ascii = any(ord(c) > 127 for c in (title or '') + (description or ''))
    if not non_ascii and (title or description):
        warnings.append(
            "El titulo y description no contienen ningun caracter acentuado. "
            "El espanol tiene acentos (a, e, i, o, u, n). Revisar."
        )

    words = len(body.split()) if body else 0
    if words and words < 1500:
        warnings.append(f"Articulo corto: {words} palabras (minimo 1.500)")
    elif words > 2500:
        warnings.append(f"Articulo largo: {words} palabras (maximo 2.500)")

    slug = os.path.basename(post_path)
    slug_no_ext = slug.replace(".md", "")
    if not slug_no_ext.isascii():
        warnings.append(f"Slug contiene caracteres no-ASCII: {slug}")

    return errors, warnings


def check_ecosistema(staged_posts: list[str], staged_all: list[str]) -> tuple[list[str], list[str]]:
    errors = []
    warnings = []

    has_pillar = any("ia-en-paraguay.markdown" in f for f in staged_all)
    has_llms = any("llms.txt" in f for f in staged_all)

    if staged_posts and not has_pillar:
        errors.append(
            "Nuevo post detectado pero ia-en-paraguay.markdown no esta en el commit. "
            "Agregarlo: git add ia-en-paraguay.markdown"
        )
    if staged_posts and not has_llms:
        errors.append(
            "Nuevo post detectado pero llms.txt no esta en el commit. "
            "Agregarlo: git add llms.txt"
        )

    # Check if new article topic is still in Proximamente on pillar page
    for post_file in staged_posts:
        post_path = os.path.join(REPO_DIR, post_file)
        content = read_file(post_path)
        title = extract_frontmatter_field(content, "title")
        categories = extract_frontmatter_field(content, "categories", "").strip()
        if categories != "articulos" or not title:
            continue

        pillar_path = os.path.join(REPO_DIR, "ia-en-paraguay.markdown")
        pillar_content = read_file(pillar_path)
        pm_sections = re.findall(r'\*\*Pr.{1,2}ximamente:\*\*\s*(.+?)(?:\n\n|\n\*|\Z)', pillar_content, re.DOTALL)

        title_words = set(re.findall(r'\w+', title.lower()))
        # Keep only meaningful words (4+ chars, skip common words)
        stopwords = {'para', 'como', 'esta', 'entre', 'sobre', 'desde', 'ante', 'hacia', 'tiene', 'entre'}
        title_keywords = {w for w in title_words if len(w) >= 4 and w not in stopwords}

        for pm_text in pm_sections:
            pm_text_lower = pm_text.lower()
            for kw in title_keywords:
                if kw in pm_text_lower:
                    errors.append(
                        f"El articulo '{title[:50]}...' coincide con el keyword '{kw}' "
                        f"que todavia figura en Proximamente de la pagina pilar. "
                        "Actualizar ia-en-paraguay.markdown: sacarlo de Proximamente y agregarlo a su pilar."
                    )
                    break

    return errors, warnings


def print_report(errors: list[str], warnings: list[str], post_name: str = ""):
    if post_name:
        print(f"\n  Validando: {post_name}")

    if errors:
        print(f"\n  {'='*50}")
        print(f"  ERRORES ({len(errors)}):")
        print(f"  {'='*50}")
        for e in errors:
            print(f"  X  {e}")

    if warnings:
        print(f"\n  ADVERTENCIAS ({len(warnings)}):")
        for w in warnings:
            print(f"  !  {w}")

    if not errors and not warnings:
        print(f"\n  [OK] Validacion superada")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--check":
        post_path = os.path.join(REPO_DIR, sys.argv[2])
        ultimos_3 = get_last_n_posts(3)
        errors, warnings = check_post(post_path, ultimos_3)
        print_report(errors, warnings, os.path.basename(post_path))
        sys.exit(EXIT_FAIL if errors else EXIT_PASS)

    staged_posts = get_staged_posts()
    staged_all = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True, cwd=REPO_DIR
    ).stdout.strip().split("\n")

    if not staged_posts:
        sys.exit(EXIT_PASS)

    ultimos_3 = get_last_n_posts(3)
    all_errors = []
    all_warnings = []

    print(f"\n  {'='*50}")
    print(f"  VALIDACION PRE-COMMIT - muchotexto.net")
    print(f"  {'='*50}")
    print(f"  Posts a publicar: {len(staged_posts)}")

    for post_file in staged_posts:
        post_path = os.path.join(REPO_DIR, post_file)
        errors, warnings = check_post(post_path, ultimos_3)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        print_report(errors, warnings, os.path.basename(post_file))

    e, w = check_ecosistema(staged_posts, staged_all)
    all_errors.extend(e)
    all_warnings.extend(w)

    if e:
        print(f"\n  {'='*50}")
        print(f"  ERRORES DE ECOSISTEMA:")
        print(f"  {'='*50}")
        for err in e:
            print(f"  X  {err}")

    if all_errors:
        print(f"\n  {'='*50}")
        print(f"  [FAIL] Commit BLOQUEADO - corregi los errores antes de comitear")
        print(f"  {'='*50}")
        sys.exit(EXIT_FAIL)
    else:
        print(f"\n  [OK] Validacion superada - commit permitido")
        sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
