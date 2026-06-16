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
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree
from urllib.request import Request, urlopen
from urllib.error import URLError

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("pulso")

# ─── Config ──────────────────────────────────────────────────────────────
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_DIR, "_posts")

GH_TOKEN = os.environ.get("GH_MODELS_TOKEN")
GH_MODELS_ENDPOINT = "https://models.inference.ai.azure.com/chat/completions"
GH_MODEL = "gpt-4o-mini"

PARAGUAY_TZ = timezone(timedelta(hours=-4))

MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "setiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}

def fmt_fecha(dt: datetime) -> str:
    return f"{dt.day} de {MESES[dt.month]} de {dt.year}"

RSS_FEEDS = [
    ("ABC Color", "https://www.abc.com.py/arc/outboundfeeds/rss/nacionales/"),
    ("ABC Policiales", "https://www.abc.com.py/arc/outboundfeeds/rss/policiales/"),
    ("ABC Deportes", "https://www.abc.com.py/arc/outboundfeeds/rss/deportes/"),
    ("ABC Política", "https://www.abc.com.py/arc/outboundfeeds/rss/politica/"),
    ("ABC Economía", "https://www.abc.com.py/arc/outboundfeeds/rss/economia/"),
    ("ABC Mundo", "https://www.abc.com.py/arc/outboundfeeds/rss/mundo/"),
    ("ABC Espectáculos", "https://www.abc.com.py/arc/outboundfeeds/rss/espectaculos/"),
    ("ADN Digital", "https://www.adndigital.com.py/rss"),
    ("Diario HOY", "https://www.hoy.com.py/feed/"),
    ("Diario Popular", "https://www.popular.com.py/feed/"),
    ("El Independiente", "https://www.independiente.com.py/feed/"),
    ("El Nacional", "https://www.elnacional.com.py/feed/"),
    ("La Nación", "https://www.lanacion.com.py/arc/outboundfeeds/rss/?outputType=xml"),
    ("La Tribuna", "https://www.latribuna.com.py/arc/outboundfeeds/rss/"),
    ("NPY", "https://www.npy.com.py/index.rss"),
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
    for name, url in RSS_FEEDS:
        log.info("Fetching RSS: %s", name)
        xml_text = fetch_url(url)
        if xml_text:
            items = parse_rss(xml_text, name)
            log.info("  → %d items from %s", len(items), name)
            all_items.extend(items)
        else:
            log.warning("  → No data from %s", name)
    return all_items

def build_prompt(news_items: list) -> str:
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

    prompt = f"""Eres un analista de tendencias y sentimiento social especializado en Paraguay.
Generá el reporte "Pulso Diario Paraguay" para hoy ({dia} {fecha}) en el formato exacto que se indica abajo.

INSTRUCCIONES:
1. Analizá las noticias reales listadas abajo (extraídas de RSS de medios paraguayos hoy).
2. NO inventes hechos, cifras ni nombres de personas. Los nombres propios deben preservarse EXACTAMENTE como aparecen en las noticias RSS. Si no estás 100% seguro del nombre de una persona, omití el nombre y referite al cargo ("el intendente", "el ministro", etc.).
3. La temperatura social debe justificarse con datos de volumen y sentimiento estimado.
4. El Insight del Día es la sección más importante: conectá los temas y proponé una lectura de fondo.
5. El TEMA #1 debe ser el que más volumen de conversación generó según las noticias disponibles.
6. Idioma: español de Paraguay (voseo, "che", etc.).
7. Sin opiniones personales del agente — solo síntesis de lo que circula.
8. NO uses formato markdown como **negritas** o *cursiva* — solo texto plano.
9. Cada categoría (🏛💰⚽🎭🚨🔥) debe aparecer UNA SOLA VEZ. Si hay varias noticias de la misma categoría, ponelas todas bajo el mismo subtítulo emoji.

FORMATO EXACTO DEL REPORTE (respetá esta estructura):

PULSO DIARIO PARAGUAY
📅 {dia} {fecha}  |  🕐 Última actualización: {now.strftime("%H:%M")}

🌡 TEMA #1 DEL DÍA: [Nombre del tema]

[Una línea que resume por qué es el #1]

🏛 POLÍTICA

[Título del tema principal]

[2-3 líneas de desarrollo. Dato concreto obligatorio.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🔹 [Tema secundario si existe]

[1-2 líneas]

💰 ECONOMÍA

[Título del tema principal]

[2-3 líneas. Números/cifras obligatorios.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

⚽ DEPORTES

[Título del tema principal]

[2-3 líneas. Resultado o dato deportivo concreto.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🔹 [Tema secundario si existe]

🎭 ENTRETENIMIENTO & CULTURA

[Título del tema principal]

[2-3 líneas.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🚨 SEGURIDAD & SOCIEDAD

[Título del tema principal]

[2-3 líneas.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🔥 VIRALES & TENDENCIAS

[Título del viral o tendencia]

[2-3 líneas. Origen y por qué pegó.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🔹 [Tema secundario si existe]
[1-2 líneas]

💰 ECONOMÍA

[Título del tema principal]
[2-3 líneas. Números/cifras obligatorios.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

⚽ DEPORTES

[Título del tema principal]
[2-3 líneas. Resultado o dato deportivo concreto.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🎭 ENTRETENIMIENTO & CULTURA

[Título del tema principal]
[2-3 líneas.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🚨 SEGURIDAD & SOCIEDAD

[Título del tema principal]
[2-3 líneas.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

🔥 VIRALES & TENDENCIAS

[Título del viral o tendencia]
[2-3 líneas. Origen y por qué pegó.]
📊 Temperatura social: [Baja / Media / Alta / Explosiva]

📈 RANKING DEL DÍA (por volumen de conversación estimado)

1. 🥇 [Tema]
2. 🥈 [Tema]
3. 🥉 [Tema]
4. [Tema]
5. [Tema]

💡 INSIGHT DEL DÍA

[Un párrafo corto con la observación más interesante o
el patrón que conecta los temas del día. El "por qué"
detrás de la conversación del día.]

🔍 ANÁLISIS DE SENTIMIENTO POR CATEGORÍA

| Categoría | Volumen | Positivo | Neutral | Negativo | Temperatura |
|-----------|---------|----------|---------|----------|-------------|
| 🏛 Política | | % | % | % | 🟢/🟡/🟠/🔴 |
| 💰 Economía | | % | % | % | 🟢/🟡/🟠/🔴 |
| ⚽ Deportes | | % | % | % | 🟢/🟡/🟠/🔴 |
| 🎭 Cultura | | % | % | % | 🟢/🟡/🟠/🔴 |
| 🚨 Seguridad | | % | % | % | 🟢/🟡/🟠/🔴 |
| 🔥 Virales | | % | % | % | 🟢/🟡/🟠/🔴 |

🔎 FUENTES CONSULTADAS HOY

[Lista de medios usados]

DATOS PARA ANALIZAR (NOTICIAS REALES DE HOY):
{context}
"""

    return prompt


def call_github_models(prompt: str) -> str | None:
    if not GH_TOKEN:
        log.error("GH_MODELS_TOKEN no está configurado")
        return None

    payload = json.dumps({
        "model": GH_MODEL,
        "messages": [
            {"role": "system", "content": "Eres un analista de tendencias paraguayas. Generás reportes en español paraguayo."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 4000,
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
        with urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
        content = data["choices"][0]["message"]["content"]
        return content
    except Exception as e:
        log.error("Error calling GitHub Models: %s", e)
        return None


def save_post(content: str):
    now = now_py()
    date_str = now.strftime("%Y-%m-%d")
    slug = f"{date_str}-pulso-paraguay"

    frontmatter = f"""---
layout: post
title: "Pulso Paraguay — {fmt_fecha(now)}"
date: {date_str}
categories: blog
tags: pulso paraguay actualidad política economía deportes
---

"""
    full_content = frontmatter + content

    os.makedirs(POSTS_DIR, exist_ok=True)
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)

    log.info("Post guardado: %s", filepath)
    return filepath


def main():
    if not GH_TOKEN:
        log.error("Error: GH_MODELS_TOKEN no está configurado.")
        log.error("Creá un secret en GitHub: Settings → Secrets → Actions → GH_MODELS_TOKEN")
        sys.exit(1)

    log.info("=" * 50)
    log.info("PULSO DIARIO PARAGUAY — Generación automática")
    log.info("Fecha: %s", now_py().strftime("%Y-%m-%d %H:%M"))
    log.info("=" * 50)

    log.info("Fase 1/3: Recolectando noticias vía RSS...")
    news = collect_news()
    log.info("→ %d noticias recolectadas", len(news))

    if len(news) < 5:
        log.warning("Muy pocas noticias (%d). El reporte puede ser limitado.", len(news))

    log.info("Fase 2/3: Generando reporte con GitHub Models (%s)...", GH_MODEL)
    prompt = build_prompt(news)
    report = call_github_models(prompt)

    if not report:
        log.error("No se pudo generar el reporte. Abortando.")
        sys.exit(1)

    log.info("Fase 3/3: Guardando post de Jekyll...")
    filepath = save_post(report)

    log.info("¡Listo! Reporte generado: %s", filepath)
    print(f"::set-output name=post_path::{filepath}")


if __name__ == "__main__":
    main()
