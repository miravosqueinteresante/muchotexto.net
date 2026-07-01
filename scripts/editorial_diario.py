#!/usr/bin/env python3
"""
Editorial Diaria — Generador automático del artículo analisis del día.
Lee el Pulso Paraguay publicado, lo analiza con GPT-4o y genera
una Editorial que conecta los temas del día con precision y sin alucinaciones.
"""

import os
import sys
import re
import json
import time
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

SYSTEM_PROMPT = """Eres un analista paraguayo que escribe en español paraguayo natural (con voseo, sin jopara ni guaraní).

Tu trabajo: leer el Pulso Paraguay del día e identificar 2 o 3 conexiones entre los temas que los datos ya muestran. No inventes interpretaciones: señalá patrones que están en el Pulso.

Reglas estrictas:
- Solo usar información presente en el Pulso Paraguay proporcionado. No agregues contexto externo ni conocimiento general.
- Nunca atribuyas citas, frases, ideas o dichos a personas reales. No digas "como decía X" a menos que esa cita aparezca textual en el Pulso.
- Nunca inventes datos, fechas, cifras ni nombres de personas. Los nombres propios deben coincidir EXACTAMENTE con los del Pulso.
- Si el Pulso menciona a una persona, limitate a lo que el Pulso dice de ella. No la conviertas en símbolo, ejemplo, metáfora ni emblema de nada. No digas que "refuerza", "encarna", "representa" o "simboliza". Es una persona, no un recurso retórico.
- Si el Pulso dice que alguien "compartió su análisis", no digas que "elogió", "criticó" o "respaldó". No infieras el tono. Si el Pulso no califica la declaración, vos tampoco.
- Si un dato no está en el Pulso, no lo uses.
- No uses metáforas forzadas del tipo "X es el espejo de Y", "X como Y", "X es el Y de Z".
- No uses preguntas retóricas vacías como apertura o cierre.
- El estilo es directo y periodístico. La opinión surge de contrastar hechos, no de filosofar.
- Idioma: español de Paraguay (voseo, "che", etc.). NO uses jopara ni guaraní.

Formato:
- Título: descriptivo y concreto. Máximo 70 caracteres sin contar "— Editorial [fecha]".
- Primer párrafo: arranca con un hecho concreto del Pulso, no con una pregunta ni con una afirmación abstracta.
- Subtítulos (2 o 3) con ## que adelanten una idea concreta. No uses subtítulos genéricos como "Contexto" o "Análisis".
- La palabra "Paraguay" debe aparecer al menos 3 veces distribuidas en el texto.
- Último párrafo: cerrar con una conclusión firme basada en los hechos presentados.
- Extensión: 500-700 palabras.
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
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        log.error("Error leyendo Pulso %s: %s", filepath, e)
        return None, None
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
        "temperature": 0.3,
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

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            with urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode())
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            if not content.strip():
                log.error("API devolvio contenido vacio")
                return None
            return content.strip()
        except Exception as e:
            log.warning("Intento %d/%d fallo: %s", attempt, max_retries, e)
            if attempt < max_retries:
                time.sleep(2 ** attempt)
            else:
                log.error("Error calling GitHub Models tras %d intentos: %s", max_retries, e)
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
    # ponytail: strip chars that break YAML, keep quotes out
    return re.sub(r'[":\\{}\[\]&*!|>#%`]', '', text).strip()


def make_meta_description(body: str, max_len: int = 155) -> str:
    plain = re.sub(r"[#*_\[\]()`>|~\"]", "", body)
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) <= max_len:
        return plain
    return plain[:plain.rfind(" ", 0, max_len)] + "..."


ARTICULOS_LINKEABLES = [
    ("Yguazú Digital", "yguazu digital", "{% post_url 2026-06-23-yguazu-digital-paraguay-hub-ia-mas-grande-del-mundo %}"),
    ("centro de datos|centro de IA|data center|centro de inteligencia artificial", "centro de IA", "{% post_url 2026-06-23-yguazu-digital-paraguay-hub-ia-mas-grande-del-mundo %}"),
    ("ANDE|sector eléctrico|apertura eléctrica|reforma energética|ley 7599", "sector eléctrico", "{% post_url 2026-05-27-apertura-sector-electrico-privado-paraguay %}"),
    ("Itaipú|energía hidroeléctrica|excedente energético", "energía de Itaipú", "{% post_url 2026-05-27-apertura-sector-electrico-privado-paraguay %}"),
    ("Peter Thiel|Palantir|Crusoe AI|Cully Cavness", "Peter Thiel", "{% post_url 2026-05-16-peter-thiel-paraguay-experimento %}"),
    ("burbuja de la IA|burbuja inteligencia artificial|costos de la IA|cuesta más que los humanos", "burbuja de la IA", "{% post_url 2026-05-27-ia-cuesta-mas-que-humanos-burbuja %}"),
    ("tokenización|blockchain.{0,40}?agro|soja.{0,20}?token", "tokenización del agro", "{% post_url 2026-05-18-tokenizacion-del-agro-paraguay %}"),
    ("encíclica|Papa León XIV|Magnifica Humanitas|ética.{0,60}?inteligencia artificial|IA.{0,40}?ética", "encíclica Magnifica Humanitas", "{% post_url 2026-05-28-magnifica-humanitas-enciclica-ia %}"),
    ("inteligencia artificial.{0,60}?fútbol|IA.{0,40}?deporte|Sportian|Pochettino.{0,30}?IA|datos.{0,20}?deportivos", "uso de IA en el fútbol", "{% post_url 2026-06-23-laboratorio-americano-ia-futbol-mundial-2026 %}"),
    ("ley de protección de datos|protección de datos personales|privacidad.{0,40}?datos", "ley de protección de datos", "{% post_url 2026-05-18-tokenizacion-del-agro-paraguay %}"),
    ("identidad digital|conciencia.{0,40}?tecnología|ciberhumanidad", "identidad digital", "{% post_url 2026-05-13-ciberhumanidad %}"),
]


def add_internal_links(body: str) -> str:
    for pattern, anchor, post_url in ARTICULOS_LINKEABLES:
        match = re.search(r'\b(?:' + pattern + r')\b', body, re.IGNORECASE)
        if match:
            # ponytail: safety check — link must not split a word
            start, end = match.start(), match.end()
            before_char = body[start - 1:start] if start > 0 else ' '
            after_char = body[end:end + 1] if end < len(body) else ' '
            if (before_char.isalnum() or before_char == '_' or
                after_char.isalnum() or after_char == '_'):
                log.warning("Link insertion habria cortado una palabra — saltando patron '%s' en pos %d", pattern, start)
                continue
            link = f"[{anchor}]({post_url})"
            body = body[:start] + link + body[end:]
    return body


def validate_content(body: str, pulso_content: str):
    """Post-proceso: loguea posibles alucinaciones. Devuelve dict con conteos."""
    pulso_lower = pulso_content.lower()
    critical = []
    warnings = []

    # Patterns that indicate output is probably hallucinated
    critical_patterns = [
        (r"pelea por entrar al Mundial", "El Mundial ya se esta jugando, Paraguay ya esta adentro"),
        (r"clasificar al Mundial", "Verificar si el Pulso dice que Paraguay ya esta en el Mundial"),
        (r"eliminado", "Verificar si Paraguay fue eliminado segun el Pulso"),
        (r"partido de ayer|el día de ayer|ayer.*partido", "No se debe referir a 'ayer' — usar hechos del Pulso de hoy"),
    ]

    for pattern, reason in critical_patterns:
        if re.search(pattern, body, re.IGNORECASE):
            msg = f"CRITICO: '{pattern}' — {reason}"
            log.error(msg)
            critical.append(msg)

    # Person embellishment: extract capitalized names from body, check Pulso context
    body_names = set(re.findall(r'\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\b', body))
    pulso_names = set(re.findall(r'\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\b', pulso_content))
    new_names = body_names - pulso_names
    for name in new_names:
        if name not in ("Paraguay", "Alemania", "Estados Unidos", "Brasil", "Argentina"):
            log.warning("Nombre no presente en el Pulso: '%s'", name)

    # Detect emotional framing around person names from Pulso
    embellish_patterns = [
        r'(?:refuerza|encarna|representa|simboliza)\s+(?:este|el|la|un)\s+\w+',
        r'(?:experiencia|liderazgo)\s+(?:y|e)\s+(?:liderazgo|experiencia|histórico)',
    ]
    for ep in embellish_patterns:
        if re.search(ep, body, re.IGNORECASE):
            log.warning("Posible embellecimiento de persona detectado: '%s'", ep)
            warnings.append(f"embellecimiento: {ep}")

    # Log sentences with low Pulso overlap
    sentences = re.split(r'(?<=[.!?])\s+', body)
    for s in sentences:
        words = set(re.findall(r'\b\w{5,}\b', s.lower()))
        if len(words) >= 6:
            pulso_words = set(re.findall(r'\b\w{5,}\b', pulso_lower))
            overlap = words & pulso_words
            if len(overlap) < 2:
                log.warning("Oracion con poca conexion al Pulso: %s...", s[:100])

    if critical:
        log.error("Editorial generada con %d alertas CRITICAS — publicada pero requiere revision humana urgente", len(critical))
    elif warnings:
        log.warning("Editorial generada con %d alertas — revisar", len(warnings))
    else:
        log.info("Validacion superada sin alertas")
    return {"critical": len(critical), "warnings": len(warnings)}


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
    body = add_internal_links(body)
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

    log.info("Paso 2.5: Validando contenido contra el Pulso...")
    vresult = validate_content(body, pulso)
    if vresult["critical"] > 0:
        log.error("Editorial publicada con %d alertas criticas — requiere revision humana.", vresult["critical"])

    log.info("Paso 3/3: Guardando post de Jekyll...")
    filepath = save_editorial_post(title, body)

    log.info("¡Listo! Editorial generada: %s", filepath)


if __name__ == "__main__":
    main()
