#!/usr/bin/env python3
"""
Genera FAQPage JSON-LD a partir del contenido de un articulo.
Uso: python scripts/generate_faq.py _posts/2026-07-16-mi-articulo.md
"""

import os
import sys
import json
import logging
import re
from urllib.request import Request, urlopen

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("faqgen")

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GH_TOKEN = os.environ.get("GH_MODELS_TOKEN")
GH_ENDPOINT = "https://models.inference.ai.azure.com/chat/completions"
GH_MODEL = "gpt-4o-mini"

FAQ_JSON_SNIPPET = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "PREGUNTA_1",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RESPUESTA_1"
      }
    },
    {
      "@type": "Question",
      "name": "PREGUNTA_2",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RESPUESTA_2"
      }
    },
    {
      "@type": "Question",
      "name": "PREGUNTA_3",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RESPUESTA_3"
      }
    }
  ]
}
</script>'''


def call_llm(prompt: str) -> str | None:
    if not GH_TOKEN:
        log.error("GH_MODELS_TOKEN no configurado")
        return None

    payload = json.dumps({
        "model": GH_MODEL,
        "messages": [
            {"role": "system", "content": (
                "Sos un editor especializado en generar preguntas frecuentes (FAQ) "
                "para articulos periodisticos. Generas preguntas en español paraguayo natural, "
                "con respuestas concisas de 2 a 4 oraciones con datos duros del articulo. "
                "Devolves SOLO JSON valido, sin markdown, sin explicaciones."
            )},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.5,
        "max_tokens": 1500,
    }).encode()

    req = Request(
        GH_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Bearer {GH_TOKEN}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        log.error("Error llamando a GitHub Models: %s", e)
        return None


def strip_frontmatter(content: str) -> tuple[str, str]:
    """Devuelve (frontmatter, body) sin los --- """
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if m:
        return m.group(1), content[m.end():]
    return "", content


def strip_faq_schema(body: str) -> str:
    """Elimina bloque FAQPage JSON-LD existente del body."""
    return re.sub(
        r'<script type="application/ld\+json">\s*\{[^<]*"@type"\s*:\s*"FAQPage"[^<]*\}</script>\s*',
        '',
        body,
        flags=re.DOTALL,
    )


def extract_article_text(body: str) -> str:
    """Extrae texto limpio del markdown, sin HTML ni scripts."""
    text = strip_faq_schema(body)
    text = re.sub(r'<script[^<]*</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\{[%#][^}]*[%#]\}', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[#*>`|~_\[\]]', '', text)
    return text.strip()


def build_prompt(title: str, body: str) -> str:
    text = extract_article_text(body)
    max_chars = 8000
    if len(text) > max_chars:
        text = text[:max_chars] + "\n\n[... articulo extenso, datos clave al inicio]"

    return f"""Genera 3 preguntas frecuentes (FAQ) con sus respuestas para este articulo.

Titulo: {title}

Cada pregunta debe:
- Ser una pregunta real que un lector haria en Google (ej: "¿Como afecta X a Paraguay?")
- Incluir datos concretos del articulo (cifras, nombres, lugares)
- Respuesta en 2-4 oraciones, español paraguayo natural

Devolve UNICAMENTE un array JSON con este formato exacto:
[
  {{"q": "Pregunta 1", "a": "Respuesta 1"}},
  {{"q": "Pregunta 2", "a": "Respuesta 2"}},
  {{"q": "Pregunta 3", "a": "Respuesta 3"}}
]

Contenido del articulo:
{text}"""


def format_faq_json(questions: list[dict]) -> str:
    """Convierte [{"q":..., "a":...}] a JSON-LD FAQPage."""
    entities = []
    for item in questions:
        entities.append({
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        })

    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }

    return '<script type="application/ld+json">\n' + \
           json.dumps(faq, indent=2, ensure_ascii=False) + \
           '\n</script>'


def generate_faq(filepath: str) -> bool:
    if not os.path.isfile(filepath):
        log.error("Archivo no encontrado: %s", filepath)
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter, body = strip_frontmatter(content)
    body = strip_faq_schema(body)

    # buscar titulo en frontmatter
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.basename(filepath)

    prompt = build_prompt(title, body)
    raw = call_llm(prompt)
    if not raw:
        return False

    # limpiar respuesta
    raw = raw.strip()
    # quitar markdown code fences si existen
    raw = re.sub(r'^```(?:json)?\s*\n?', '', raw)
    raw = re.sub(r'\n?```\s*$', '', raw)

    try:
        questions = json.loads(raw)
    except json.JSONDecodeError:
        log.error("Respuesta del modelo no es JSON valido. Respuesta:\n%s", raw[:500])
        return False

    if not isinstance(questions, list) or len(questions) < 2:
        log.error("Se esperaban 3 preguntas, se recibieron %d", len(questions) if isinstance(questions, list) else 0)
        return False

    faq_block = format_faq_json(questions[:3])

    # insertar FAQ al final del body (antes de ultimo backtick si existe)
    # ponytail: insertar al final del archivo, antes del ultimo newline
    new_content = f"---\n{frontmatter}\n---\n{body.rstrip()}\n\n{faq_block}\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    log.info("FAQ generado: %d preguntas → %s", len(questions[:3]), filepath)
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <articulo.md> [articulo2.md ...]")
        sys.exit(1)

    ok = 0
    for path in sys.argv[1:]:
        if generate_faq(path):
            ok += 1

    log.info("Procesados: %d/%d exitosos", ok, len(sys.argv) - 1)
    sys.exit(0 if ok == len(sys.argv) - 1 else 1)
