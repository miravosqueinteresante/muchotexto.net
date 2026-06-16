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

PY_TIME = "19:00:00"

SYSTEM_PROMPT = """Eres un editorialista de Opinión con la voz y profundidad de los grandes intelectuales paraguayos. Tu estilo sintetiza:

- Augusto Roa Bastos: reflexión sobre el poder, la memoria histórica, la identidad paraguaya
- Helio Vera: ironía, "paraguayología", análisis de costumbres e identidad nacional
- Rafael Barrett: crítica social aguda, revelar la realidad detrás de los hechos superficiales
- Alcibiades González Delvalle: compromiso con la verdad, valentía para decir lo que incomoda
- Josefina Plá: perspectiva cultural, histórica y feminista
- Gabriel Casaccia: análisis de la hipocresía social paraguaya
- Bernardino Cano Radil: pensamiento constitucional y democrático, visión de las instituciones paraguayas

Debes tener voz propia con tono paraguayo (español paraguayo natural con voseo y modismos coloquiales, NO uses jopara ni guaraní). Analiza los acontecimientos con profundidad: cultural, filosófica, sociológica y política.

El título debe relacionar inteligencia artificial, la fecha y Paraguay. Formato sugerido: "[Tema central] — Editorial [día] de [mes] de [año]"

Reglas estrictas:
- Solo usar información del Pulso Paraguay proporcionado abajo
- Nunca inventar datos, fechas o cifras
- Si no hay suficiente información para analizar un tema, no lo hagas
- No seas sensacionalista ni partidario
- Extensión: 800-1200 palabras
- Formato: markdown, con # para el título

Al final del artículo, agrega este párrafo en cursiva (sin #):

*Esta Editorial fue escrita íntegramente por una inteligencia artificial entrenada para analizar la realidad paraguaya en profundidad. El sistema lee el Pulso Paraguay del día, procesa los acontecimientos desde una perspectiva cultural, filosófica, sociológica y política, y produce este análisis. Cada dato aquí presentado fue extraído exclusivamente de fuentes periodísticas verificadas y publicadas en el Pulso Paraguay. Muchotexto.net cree en la transparencia: esto no lo escribió un humano, pero la reflexión sobre el país es tan real como los hechos que la sustentan.*"""


# ─── Helpers ──────────────────────────────────────────────────────────────

def now_py() -> datetime:
    return datetime.now(PARAGUAY_TZ)


def fmt_fecha_para_titulo(dt: datetime) -> str:
    return f"{dt.day} de {MESES[dt.month]} de {dt.year}"


def date_str() -> str:
    return now_py().strftime("%Y-%m-%d")


def read_pulso_post(date: str) -> str | None:
    pattern = f"{date}-pulso-paraguay.md"
    filepath = os.path.join(POSTS_DIR, pattern)
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    body = re.sub(r"^---.*?---\s*", "", content, count=1, flags=re.DOTALL)
    return body.strip()


def call_github_models(pulso_content: str) -> str | None:
    if not GH_TOKEN:
        log.error("GH_MODELS_TOKEN no está configurado")
        return None

    fecha = fmt_fecha_para_titulo(now_py())
    user_prompt = f"Hoy es {fecha}. Este es el Pulso Paraguay del día:\n\n{pulso_content}\n\nGenera la Editorial."

    payload = json.dumps({
        "model": GH_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
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


def extract_title_and_body(markdown_text: str) -> tuple[str, str]:
    title_match = re.search(r"^#\s+(.+)$", markdown_text, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        body = re.sub(r"^#\s+.+$\n?", "", markdown_text, count=1, flags=re.MULTILINE).strip()
    else:
        title = f"Editorial del {fmt_fecha_para_titulo(now_py())}"
        body = markdown_text
    return title, body


def save_editorial_post(title: str, body: str):
    now = now_py()
    date = date_str()
    slug = f"{date}-editorial"

    frontmatter = f"""---
layout: post
title: "{title}"
date: {date} {PY_TIME} -0400
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
    pulso = read_pulso_post(date)
    if not pulso:
        log.warning("No se encontró el Pulso Paraguay para hoy (%s). Abortando.", date)
        sys.exit(0)

    log.info("Paso 2/3: Generando Editorial con %s...", GH_MODEL)
    result = call_github_models(pulso)
    if not result:
        log.error("No se pudo generar la Editorial. Abortando.")
        sys.exit(1)

    title, body = extract_title_and_body(result)

    log.info("Paso 3/3: Guardando post de Jekyll...")
    filepath = save_editorial_post(title, body)

    log.info("¡Listo! Editorial generada: %s", filepath)


if __name__ == "__main__":
    main()
