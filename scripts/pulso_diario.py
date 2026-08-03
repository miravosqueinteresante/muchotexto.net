#!/usr/bin/env python3
"""
Pulso Diario Paraguay — Generador automático del reporte diario.
Busca noticias vía RSS, genera el Pulso con GitHub Models (GPT-4o-mini),
y lo guarda como post de Jekyll en _posts/.
"""

import os
import sys
import json
import hashlib
import logging
import re
import unicodedata
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("pulso")

# ─── Config ──────────────────────────────────────────────────────────────
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_DIR, "_posts")

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

PARAGUAY_TZ = timezone(timedelta(hours=-3))

MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "setiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}

def fmt_fecha(dt: datetime) -> str:
    return f"{dt.day} de {MESES[dt.month]} de {dt.year}"

def make_meta_description(content: str, max_len: int = 155) -> str:
    lines = content.strip().split("\n")
    useful = "\n".join(line for line in lines if not line.strip().startswith("PULSO DIARIO"))
    plain = re.sub(r"[#*_\[\]()`>|~\"]", "", useful)
    plain = re.sub(r"[📅🕐🌡🏛💰⚽🎭🚨🔥📊🔍🔎💡📈]", "", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) <= max_len:
        return plain
    return plain[:plain.rfind(" ", 0, max_len)] + "..."

def slugify(text: str, max_len: int = 50) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    if len(text) > max_len:
        cut = text.rfind("-", 0, max_len)
        if cut > 10:
            text = text[:cut]
        else:
            text = text[:max_len].rstrip("-")
    return text

RSS_FEEDS = [
    ("ABC Tecnologia", "https://www.abc.com.py/arc/outboundfeeds/rss/tecnologia/"),
    ("ABC Ciencia", "https://www.abc.com.py/arc/outboundfeeds/rss/ciencia/"),
    ("ABC Economia", "https://www.abc.com.py/arc/outboundfeeds/rss/economia/"),
    ("ABC Nacionales", "https://www.abc.com.py/arc/outboundfeeds/rss/nacionales/"),
    ("La Nacion", "https://www.lanacion.com.py/arc/outboundfeeds/rss/?outputType=xml"),
    ("NPY", "https://www.npy.com.py/index.rss"),
    ("Diario HOY", "https://www.hoy.com.py/feed/"),
    ("La Tribuna", "https://www.latribuna.com.py/arc/outboundfeeds/rss/"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# ─── Helpers ──────────────────────────────────────────────────────────────

def now_py() -> datetime:
    return datetime.now(PARAGUAY_TZ)

def fetch_url(url: str, timeout: int = 15) -> str | None:
    try:
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        log.warning("Error fetching %s: %s", url, e)
        return None

def parse_rss(xml_text: str, source_name: str, max_items: int = 10):
    items = []
    try:
        root = ElementTree.fromstring(xml_text)
        ns = {"content": "http://purl.org/rss/1.0/modules/content/"}
        for entry in root.iter("item"):
            title = entry.findtext("title", "").strip()
            link = entry.findtext("link", "").strip()
            desc = entry.findtext("description", "").strip()
            pub_date_str = entry.findtext("pubDate", "")
            pub_date = None
            for fmt in [
                "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S %Z",
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%SZ",
            ]:
                try:
                    pub_date = datetime.strptime(pub_date_str, fmt)
                    break
                except ValueError:
                    continue
            if title and link:
                items.append({
                    "source": source_name,
                    "title": title,
                    "link": link,
                    "summary": desc[:500],
                    "pub_date": pub_date,
                })
            if len(items) >= max_items:
                break
    except Exception as e:
        log.warning("Error parsing RSS from %s: %s", source_name, e)
    return items

def collect_news():
    all_items = []
    sources_used = set()
    for name, url in RSS_FEEDS:
        log.info("Fetching RSS: %s", name)
        xml_text = fetch_url(url)
        if xml_text:
            items = parse_rss(xml_text, name)
            log.info("  → %d items from %s", len(items), name)
            all_items.extend(items)
            if items:
                sources_used.add(name)
        else:
            log.warning("  → No data from %s", name)
    return all_items, sorted(sources_used)

def build_prompt(news_items: list, sources_used: list) -> str:
    now = now_py()
    fecha = fmt_fecha(now)
    dias = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
    dia = dias[now.weekday()]

    context = f"Fecha: {dia} {fecha}\n\nNoticias del día:\n\n"
    for item in news_items[:60]:
        pub = ""
        if item["pub_date"]:
            pub = item["pub_date"].strftime("%Y-%m-%d %H:%M")
        context += f"[{item['source']}] ({pub}) {item['title']}\n"
        if item["summary"]:
            context += f"  {item['summary'][:300]}\n"
        context += "\n"

    prompt = f"""Eres un analista de tecnologia e infraestructura digital especializado en Paraguay.
Genera el reporte "Pulso Tech Paraguay" para hoy ({dia} {fecha}) usando SOLO las noticias de IA, tecnologia, infraestructura digital, energia para data centers y regulacion tech.

EL FILTRO TEMATICO ES OBLIGATORIO:
SOLO debes cubrir noticias relacionadas con: inteligencia artificial, machine learning, automatizacion, data centers, infraestructura digital, energia electrica para uso industrial/tecnologico, ciberseguridad, gobierno digital, regulacion de datos y tecnologia, fibra optica, conectividad, startups de tecnologia, ciencia aplicada, innovacion. IGNORA TODO el resto: politica partidaria, futbol, crimen comun, accidentes, salud publica no-digital, entretenimiento general, clima.

INSTRUCCIONES:
1. Analiza las noticias reales listadas abajo y EXTRAE SOLO las que cumplen el filtro tematico.
2. Si hay MENOS de 3 noticias que cumplen el filtro, genera un mensaje corto: "Sin novedades de IA/tech suficientes para el Pulso del dia." y TERMINA. No generes contenido sobre otros temas.
3. NO inventes hechos, cifras ni nombres de personas. Nombres propios EXACTOS como en las noticias.
4. Idioma: español de Paraguay (voseo, "che", etc.).
5. Sin opiniones personales — solo sintesis de lo que circula.
6. NO uses formato markdown (**negritas**, *cursiva*) — solo texto plano.
7. Las secciones son CONDICIONALES: solo inclui las categorias que tengan al menos una noticia del filtro tech. Si hay 3 categorias con noticias, el Pulso tiene 3 secciones. Si hay 6, tiene 6. NUNCA pongas una seccion sin contenido. El orden de las secciones debe reflejar la relevancia (mas noticias = mas arriba).
8. El Insight Tech del Dia es la seccion mas importante: conecta los temas tech del dia.

FORMATO EXACTO (si hay >=3 noticias tech):

PULSO TECH PARAGUAY
📅 {dia} {fecha}  |  🕐 Ultima actualizacion: {now.strftime("%H:%M")}

🌐 INFRAESTRUCTURA DIGITAL

[Titulo del tema principal — data centers, fibra, conectividad]

[2-3 lineas. Dato concreto obligatorio: MW, USD, km de fibra, etc.]
📊 Relevancia: [Baja / Media / Alta]

⚡ ENERGIA Y DATA CENTERS

[Titulo del tema principal — consumo electrico industrial/tech, tarifas, ANDE]

[2-3 lineas. Cifras de MW, tarifas, contratos obligatorios.]
📊 Relevancia: [Baja / Media / Alta]

🤖 INTELIGENCIA ARTIFICIAL

[Titulo del tema principal — IA, machine learning, automatizacion, modelos]

[2-3 lineas. Empresa, tecnologia, aplicacion concreta.]
📊 Relevancia: [Baja / Media / Alta]

📋 REGULACION Y GOBERNANZA TECH

[Titulo del tema principal — leyes, decretos, ciberseguridad, gobierno digital]

[2-3 lineas. Numero de ley, fecha, institucion.]
📊 Relevancia: [Baja / Media / Alta]

🚀 INNOVACION Y STARTUPS

[Titulo del tema principal — emprendimientos tech, inversiones, aceleradoras]

[2-3 lineas. Monto, ronda, empresa.]
📊 Relevancia: [Baja / Media / Alta]

🔬 CIENCIA APLICADA

[Titulo del tema principal — investigacion, papers, descubrimientos con impacto tech]

[2-3 lineas. Hallazgo concreto, institucion, publicacion.]
📊 Relevancia: [Baja / Media / Alta]

📈 TOP 3 DEL DIA (tech/IA)

1. 🥇 [Tema]
2. 🥈 [Tema]
3. 🥉 [Tema]

💡 INSIGHT TECH DEL DIA

[Un parrafo corto conectando los temas tech del dia — el patron, la tendencia o la pregunta que emerge.]

🔎 FUENTES CONSULTADAS HOY

{{', '.join(sources_used)}}

DATOS PARA ANALIZAR (NOTICIAS REALES DE HOY):
{{context}}
"""

    return prompt


def call_gemini(prompt: str, system_prompt: str = "Eres un analista de tendencias paraguayas. Generás reportes en español paraguayo.") -> str | None:
    if not GEMINI_API_KEY:
        log.error("GEMINI_API_KEY no está configurado")
        return None

    payload = json.dumps({
        "systemInstruction": {
            "parts": [{"text": system_prompt}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 4000,
        },
    }).encode()

    url = f"{GEMINI_ENDPOINT}?key={GEMINI_API_KEY}"
    req = Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urlopen(req, timeout=120) as resp:
            raw = resp.read().decode()
            data = json.loads(raw)
        if "error" in data:
            log.error("Gemini API error: %s", json.dumps(data["error"], indent=2))
            return None
        content = data["candidates"][0]["content"]["parts"][0]["text"]
        return content
    except HTTPError as e:
        body = e.read().decode() if e.fp else "(no body)"
        log.error("Gemini HTTP %s: %s", e.code, body[:500])
        return None
    except Exception as e:
        log.error("Error calling Gemini API: %s", e)
        return None


def clean_content(content: str) -> str:
    # Add blank line before temperatura social indicators so markdown creates separate <p>
    # Handle both inline (". 📊") and newline cases
    content = re.sub(r'(\S)\s*📊 Temperatura social', r'\1\n\n📊 Temperatura social', content)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Convert "🔎 FUENTES CONSULTADAS HOY" section to bullet list
    lines = content.split('\n')
    result = []
    in_fuentes = False
    for line in lines:
        if '🔎 FUENTES CONSULTADAS HOY' in line:
            in_fuentes = True
            result.append(line)
            continue
        if in_fuentes and line.strip():
            sources = [s.strip() for s in line.split(',') if s.strip()]
            for source in sources:
                result.append(f'- {source}')
            in_fuentes = False
            continue
        result.append(line)
    return '\n'.join(result)


def save_post(content: str):
    content = clean_content(content)

    now = now_py()
    date_str = now.strftime("%Y-%m-%d")

    topic_match = re.search(r"🌡\s*TEMA\s*#1\s*DEL\s*DÍA\s*:\s*(.+?)$", content, re.MULTILINE | re.IGNORECASE)
    if not topic_match:
        topic_match = re.search(r"TEMA\s*#1\s*DEL\s*DÍA\s*:\s*(.+?)$", content, re.MULTILINE | re.IGNORECASE)

    if topic_match:
        topic = topic_match.group(1).strip()
        topic_slug = slugify(topic)
        slug = f"{date_str}-{topic_slug}-pulso-paraguay"
        title = f"Pulso Paraguay: {topic} — {fmt_fecha(now)}"
        # enforce max 80 chars for Pulso titles (SEO rule relaxed for automated content)
        TITLE_MAX = 80
        STOPWORDS = {"de", "del", "la", "el", "los", "las", "en", "con", "por", "para", "que", "un", "una", "y", "e", "o", "a", "al"}
        if len(title) > TITLE_MAX:
            prefix = "Pulso Paraguay: "
            suffix = f" — {fmt_fecha(now)}"
            max_topic = TITLE_MAX - len(prefix) - len(suffix)
            if max_topic > 10:
                # find all word boundaries within max_topic
                positions = [i for i in range(max_topic) if topic[i] == " "]
                # try last valid cut (not before a stopword of 1-3 chars)
                for pos in reversed(positions):
                    next_word = topic[pos+1:].split(" ")[0].strip(" ,;:-—")
                    if len(next_word) > 3 or next_word.lower() not in STOPWORDS:
                        topic_short = topic[:pos].rstrip(" ,;:-—")
                        break
                else:
                    cut = topic.rfind(" ", 0, max_topic)
                    topic_short = topic[:cut].rstrip(" ,;:-—") if cut > 10 else topic[:max_topic].rstrip(" ,;:-—")
            else:
                topic_short = topic[:50].rstrip(" ,;:-—")
            title = f"{prefix}{topic_short}{suffix}"
            # strip trailing stopwords from topic for cleaner truncation
            for _ in range(3):
                last = topic_short.split(" ")[-1].lower().rstrip(" ,;:-—")
                if last in STOPWORDS and len(last) <= 3:
                    topic_short = topic_short[:topic_short.rfind(" ")].rstrip(" ,;:-—")
            title = f"{prefix}{topic_short}{suffix}"
    else:
        slug = f"{date_str}-pulso-paraguay"
        title = f"Pulso Paraguay — {fmt_fecha(now)}"

    frontmatter = f"""---
layout: post
title: "{sanitize_yaml(title)}"
description: "{sanitize_yaml(make_meta_description(content))}"
date: {date_str}
last_modified_at: {date_str}
categories: pulso-paraguay
tags: pulso paraguay actualidad política economía tecnología deportes
---

"""
    full_content = frontmatter + content

    os.makedirs(POSTS_DIR, exist_ok=True)
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)

    log.info("Post guardado: %s", filepath)
    return filepath


def sanitize_yaml(text: str) -> str:
    return text.replace('"', '').replace("'", "")


def main():
    if not GEMINI_API_KEY:
        log.error("Error: GEMINI_API_KEY no está configurado.")
        log.error("Creá un API key en https://aistudio.google.com/apikey")
        log.error("Agregalo en GitHub: Settings → Secrets → Actions → GEMINI_API_KEY")
        sys.exit(1)

    log.info("=" * 50)
    log.info("PULSO DIARIO PARAGUAY — Generación automática")
    log.info("Fecha: %s", now_py().strftime("%Y-%m-%d %H:%M"))
    log.info("=" * 50)

    log.info("Fase 1/3: Recolectando noticias vía RSS...")
    news, sources = collect_news()
    log.info("→ %d noticias recolectadas de %d fuentes", len(news), len(sources))

    if len(news) < 5:
        log.warning("Muy pocas noticias (%d). El reporte puede ser limitado.", len(news))

    log.info("Fase 2/3: Generando reporte con Gemini (%s)...", GEMINI_MODEL)
    prompt = build_prompt(news, sources)
    report = call_gemini(prompt)

    if not report:
        log.error("No se pudo generar el reporte. Abortando.")
        sys.exit(1)

    log.info("Fase 3/3: Guardando post de Jekyll...")
    filepath = save_post(report)

    log.info("¡Listo! Reporte generado: %s", filepath)
    print(f"::set-output name=post_path::{filepath}")


if __name__ == "__main__":
    main()
