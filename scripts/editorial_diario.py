#!/usr/bin/env python3
"""
Editorial Diaria — Generador automático del artículo de opinión del día.
Lee el Pulso Paraguay publicado, lo analiza con GPT-4o y genera
una Editorial con profundidad cultural, filosófica, sociológica y política.
"""

import os
import sys
import re
import json
import logging
import unicodedata
from datetime import datetime, timezone, timedelta
from urllib.request import Request, urlopen

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("editorial")

# ─── Config ──────────────────────────────────────────────────────────────
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_DIR, "_posts")

GH_TOKEN = os.environ.get("GH_MODELS_TOKEN")
GH_MODELS_ENDPOINT = "https://models.inference.ai.azure.com/chat/completions"
GH_MODEL = "gpt-4o"

PARAGUAY_TZ = timezone(timedelta(hours=-4))

MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "setiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}

PY_TIME = "18:00:00"

SYSTEM_PROMPT = """Eres un editorialista de Opinión con una voz de análisis profundo, que escribe en español paraguayo natural (con voseo y modismos coloquiales, NO uses jopara ni guaraní). Tu estilo se caracteriza por: reflexión sobre el poder y la identidad paraguaya, ironía, crítica social aguda, compromiso con la verdad, perspectiva cultural y análisis de la realidad nacional con profundidad.

Analiza los acontecimientos desde una perspectiva cultural, filosófica, sociológica y política. El título debe relacionar inteligencia artificial, la fecha y Paraguay. Formato sugerido: "[Tema central] — Editorial [día] de [mes] de [año]"

Reglas estrictas:
- Solo usar información del Pulso Paraguay proporcionado abajo
- NUNCA atribuyas citas, frases, ideas o dichos a personas reales. No digas "como decía X" a menos que esa cita aparezca textual en el Pulso Paraguay.
- Nunca inventar datos, fechas, cifras NI nombres de personas. Los nombres propios deben coincidir EXACTAMENTE con los del Pulso.
- Si no hay suficiente información en el Pulso para analizar un tema, no lo hagas
- No seas sensacionalista ni partidario
REGLAS SEO ESTRICTAS (aplican al título y al cuerpo):
- El título debe contener las palabras "Paraguay" o "paraguaya/o" y al menos una keyword del tema principal. Máximo 70 caracteres sin contar "— Editorial [fecha]".
- El primer párrafo debe incluir la keyword principal del tema en las primeras 2 oraciones. NO empieces con fechas ni con "Hoy...". El hook debe ser una afirmación fuerte, una pregunta provocadora o un dato impactante del Pulso.
- Usá entre 2 y 4 subtítulos con ## que incluyan keywords secundarias. No uses subtítulos genéricos como "Contexto" o "Análisis": cada subtítulo debe adelantar una idea concreta.
- La palabra "Paraguay" debe aparecer al menos 3 veces distribuidas en el texto (no acumuladas en un solo párrafo).
- No uses preguntas retóricas vacías como cierre ("¿Estamos preparados?"). El último párrafo debe cerrar con una conclusión firme.

REGLAS DE ESTILO:
- PROHIBIDO usar las palabras "espejo", "reflejo", "refleja", "como espejo" o cualquier metáfora de espejo/reflejo en el título o en el cuerpo.
- PROHIBIDO usar metáforas predecibles o clichés del tipo "X como Y" donde un evento social es presentado como símbolo de algo más grande. Los títulos deben ser directos, periodísticos y evitar figuras literarias forzadas. No uses la estructura "X como Y" ni "X es el Y de Z".
- Extensión: 800-1200 palabras.
- Formato: markdown, con # para el título."""


# ─── Helpers ──────────────────────────────────────────────────────────────

def now_py() -> datetime:
    return datetime.now(PARAGUAY_TZ)


def fmt_fecha_para_titulo(dt: datetime) -> str:
    return f"{dt.day} de {MESES[dt.month]} de {dt.year}"


def date_str() -> str:
    return now_py().strftime("%Y-%m-%d")


def read_pulso_post(date: str) -> tuple[str | None, str | None]:
    import glob
    pattern = os.path.join(POSTS_DIR, f"{date}-*-pulso-paraguay.md")
    matches = sorted(glob.glob(pattern))
    if not matches:
        return None, None
    filepath = matches[-1]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    title_match = re.search(r"^title:\s*\"(.+?)\"", content, re.MULTILINE)
    pulso_title = title_match.group(1).strip() if title_match else None
    body = re.sub(r"^---.*?---\s*", "", content, count=1, flags=re.DOTALL)
    return body.strip(), pulso_title


def call_github_models(pulso_content: str, pulso_title: str | None = None) -> str | None:
    if not GH_TOKEN:
        log.error("GH_MODELS_TOKEN no está configurado")
        return None

    fecha = fmt_fecha_para_titulo(now_py())
    context = f"Hoy es {fecha}."
    if pulso_title:
        context += f" El Pulso Paraguay de hoy se titula: \"{pulso_title}\". IMPORTANTE: el título de esta Editorial NO debe repetir las mismas palabras clave principales del título del Pulso. Debe enfocarse en el ángulo de análisis/opinión, no en la noticia en sí."
    context += f"\n\nContenido del Pulso Paraguay:\n\n{pulso_content}\n\nGenera la Editorial."

    payload = json.dumps({
        "model": GH_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context},
        ],
        "temperature": 0.8,
        "max_tokens": 2000,
    }).encode()

    req = Request(
        GH_MODELS_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Bearer {GH_TOKEN}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode())
        content = data["choices"][0]["message"]["content"]
        return content.strip()
    except Exception as e:
        log.error("Error calling GitHub Models: %s", e)
        return None


def make_slug(text: str) -> str:
    slug = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = slug.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s-]+", "-", slug).strip("-")[:60].rstrip("-")
    return slug


def extract_title_and_body(markdown_text: str) -> tuple[str, str]:
    title_match = re.search(r"^#\s+(.+)$", markdown_text, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        body = re.sub(r"^#\s+.+$\n?", "", markdown_text, count=1, flags=re.MULTILINE).strip()
    else:
        title = f"Editorial del {fmt_fecha_para_titulo(now_py())}"
        body = markdown_text
    return title, body

def sanitize_yaml(text: str) -> str:
    return text.replace('"', '').replace("'", "")


def make_meta_description(body: str, max_len: int = 155) -> str:
    plain = re.sub(r"[#*_\[\]()`>|~\"]", "", body)
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) <= max_len:
        return plain
    return plain[:plain.rfind(" ", 0, max_len)] + "..."


def save_editorial_post(title: str, body: str):
    now = now_py()
    date = date_str()
    slug_base = make_slug(title)
    slug = f"{date}-{slug_base}-editorial"
    slug = slug[:80].rstrip("-")
    meta_desc = make_meta_description(body)

    frontmatter = f"""---
layout: post
title: "{sanitize_yaml(title)}"
description: "{sanitize_yaml(meta_desc)}"
date: {date} {PY_TIME} -0400
last_modified_at: {date}
categories: editorial
tags: editorial opinion paraguay analisis ia
---

"""
    full_content = frontmatter + body + "\n"

    os.makedirs(POSTS_DIR, exist_ok=True)
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)

    log.info("Editorial guardada: %s", filepath)
    return filepath


# ─── Main ─────────────────────────────────────────────────────────────────

def main():
    if not GH_TOKEN:
        log.error("Error: GH_MODELS_TOKEN no está configurado.")
        log.error("Creá un secret en GitHub: Settings → Secrets → Actions → GH_MODELS_TOKEN")
        sys.exit(1)

    log.info("=" * 50)
    log.info("EDITORIAL DIARIA — Generación automática")
    log.info("Fecha: %s", now_py().strftime("%Y-%m-%d %H:%M"))
    log.info("=" * 50)

    date = date_str()

    log.info("Paso 1/3: Leyendo Pulso Paraguay de %s...", date)
    pulso, pulso_title = read_pulso_post(date)
    if not pulso:
        log.warning("No se encontró el Pulso Paraguay para hoy (%s). Abortando.", date)
        sys.exit(0)

    log.info("Paso 2/3: Generando Editorial con %s...", GH_MODEL)
    result = call_github_models(pulso, pulso_title)
    if not result:
        log.error("No se pudo generar la Editorial. Abortando.")
        sys.exit(1)

    title, body = extract_title_and_body(result)

    log.info("Paso 3/3: Guardando post de Jekyll...")
    filepath = save_editorial_post(title, body)

    log.info("¡Listo! Editorial generada: %s", filepath)


if __name__ == "__main__":
    main()
