#!/usr/bin/env python3
"""
gemini_client.py - Cliente compartido de Gemini con fallback en cascada de
modelos y backoff con jitter.

Motivacion: el 21-24 de septiembre de 2026 el Pulso Diario fallo 4 dias
seguidos por HTTP 503 ("model currently experiencing high demand") del modelo
unico gemini-3.1-flash-lite. El script reintentaba 3 veces con backoff corto
(2s, 4s) y abortaba sin fallback.

Solucion: si el modelo primario devuelve 503, probar modelos alternativos
(con picos de carga independientes) y usar backoff mas largo con jitter.

Uso:
    from gemini_client import generate
    text = generate(prompt, system_prompt=..., api_key=...)
"""

import json
import logging
import random
import re
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

log = logging.getLogger("gemini")

# Modelos en orden de preferencia. El primero es el primario; los siguientes
# son fallbacks ante 503/429 (sobrecarga). Todos verificados como disponibles
# con la API key del repo (paso "Diagnosticar API key" del workflow).
# ponytail: backoff 5/15/45s x 3 modelos = hasta ~3,5 min de reintentos.
DEFAULT_MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-2.5-flash-lite",
]

ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

# Codigos que valen reintentar (sobrecarga/cuota temporal). 4xx duros no.
RETRYABLE = {429, 500, 502, 503, 504}


def generate(
    prompt: str,
    system_prompt: str = "Eres un analista de tendencias paraguayas. Generás reportes en español paraguayo.",
    api_key: str | None = None,
    models: list[str] | None = None,
    temperature: float = 0.7,
    max_output_tokens: int = 4000,
    timeout: int = 120,
) -> str | None:
    """Genera texto con Gemini probando modelos en cascada. Devuelve None si
    todos fallan."""
    if not api_key:
        log.error("GEMINI_API_KEY no está configurado")
        return None

    models = models or DEFAULT_MODELS
    payload = json.dumps({
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_output_tokens,
        },
    }).encode()

    for mi, model in enumerate(models):
        url = f"{ENDPOINT.format(model=model)}?key={api_key}"
        for attempt in range(1, 4):
            try:
                req = Request(url, data=payload, headers={"Content-Type": "application/json"})
                with urlopen(req, timeout=timeout) as resp:
                    data = json.loads(resp.read().decode())
                if "error" in data:
                    log.error("Gemini API error (%s): %s", model, json.dumps(data["error"])[:300])
                    return None
                content = data["candidates"][0]["content"]["parts"][0]["text"]
                if mi > 0:
                    log.info("Gemini OK con modelo de fallback: %s", model)
                return content
            except HTTPError as e:
                body = e.read().decode() if e.fp else "(no body)"
                if e.code in RETRYABLE and attempt < 3:
                    wait = (2 ** (attempt + 1)) + random.uniform(0, 2)  # ~5/9s + jitter
                    log.warning("Gemini %s HTTP %s (intento %d/3), esperando %.1fs...",
                                model, e.code, attempt, wait)
                    time.sleep(wait)
                    continue
                log.warning("Gemini %s HTTP %s agotado: %s", model, e.code, body[:200])
                break  # pasa al siguiente modelo
            except Exception as e:
                log.warning("Error con %s: %s", model, e)
                break  # pasa al siguiente modelo

    log.error("Todos los modelos fallaron: %s", ", ".join(models))
    return None


_MD_NOISE = re.compile(r"\{[{%].*?[}%]\}|\[([^\]]+)\]\([^)]*\)|[#*_`>|~]")
_EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF\uFE0F]"
)
_BOILERPLATE = re.compile(r"^\s*PULSO (DIARIO|TECH) PARAGUAY.*$", re.I | re.M)


def clean_body(body: str, limit: int = 3000) -> str:
    """Texto plano del artículo, sin front matter, markdown, emojis ni cabeceras."""
    text = body.split("\n---", 1)[0]
    text = _MD_NOISE.sub(r"\1", text)
    text = _EMOJI.sub("", text)
    text = _BOILERPLATE.sub("", text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip(" :-—#")
        if len(stripped) >= 8 and stripped.isupper() and stripped.replace(" ", "").isalpha():
            continue  # cabecera de sección tipo "ENERGIA Y DATA CENTERS"
        lines.append(line)
    text = re.sub(r"\s+", " ", "\n".join(lines)).strip()
    return text[:limit]


def validate_meta_description(text: str) -> tuple[str, list[str]]:
    """Normaliza y valida una meta description. Devuelve (texto, problemas)."""
    t = " ".join(text.split()).strip().strip('"\'')
    problems = []
    b = len(t.encode("utf-8"))
    if b < 120 or b > 160:
        problems.append(f"tiene {b} bytes; debe tener entre 120 y 160")
    if "..." in t or "…" in t:
        problems.append("no debe usar puntos suspensivos")
    if not t.endswith((".", "!", "?")):
        problems.append("debe terminar en punto")
    if '"' in t:
        problems.append("no debe usar comillas")
    return t, problems


def fallback_meta_description(body: str, max_bytes: int = 160) -> str:
    """Plan B determinista: oraciones completas, sin '...' ni cortes a mitad de palabra."""
    plain = clean_body(body)
    out = ""
    for sentence in re.split(r"(?<=[.!?])\s+", plain):
        candidate = (out + " " + sentence).strip()
        if len(candidate.encode("utf-8")) <= max_bytes:
            out = candidate
        else:
            if not out:
                cut = sentence.encode("utf-8")[:max_bytes].decode("utf-8", "ignore")
                cut = cut[: cut.rfind(" ")].rstrip(" ,;:-") if " " in cut else cut
                out = cut.rstrip(" ,;:-") + "."
            break
    if not out:
        out = "Análisis de actualidad paraguaya con datos y contexto."
    if len(out.encode("utf-8")) < 120:
        out = (out.rstrip(".") + ". Análisis y contexto de la jornada.").strip()
    return out


def write_meta_description(
    title: str, body: str, api_key: str | None, category: str = "", attempts: int = 3
) -> str | None:
    """Pide a Gemini una meta description editorial (120-160 bytes, sin copiar
    el primer párrafo). Devuelve None si tras los intentos no es válida."""
    plain = clean_body(body)
    first_60 = plain[:60].lower()
    feedback = ""
    for attempt in range(1, attempts + 1):
        prompt = f"""Escribí la meta description (para Google) de este artículo de muchotexto.net.

Reglas obligatorias:
- Entre 130 y 155 caracteres, en una o dos oraciones completas.
- Español paraguayo correcto, con acentos y eñes.
- Arrancá con el hecho o la tesis concreta; incluí la palabra clave principal.
- NO copies ni parafrasees la primera oración del cuerpo.
- Sin comillas, sin saltos de línea, sin puntos suspensivos, sin "En este artículo".
- Terminá con punto. Respondé SOLO la frase.

Categoría: {category or "actualidad"}
Título: {title}
Cuerpo: {plain}
{feedback}"""
        out = generate(
            prompt,
            system_prompt="Sos editor SEO de un medio paraguayo. Escribís metadescripciones precisas y profesionales.",
            api_key=api_key,
            temperature=0.4,
            max_output_tokens=200,
        )
        if not out:
            return None
        candidate, problems = validate_meta_description(out)
        if candidate[:60].lower() and candidate[:60].lower() == first_60[: len(candidate)]:
            problems.append("copiaste el inicio del cuerpo")
        if not problems:
            return candidate
        feedback = "Corregí: " + "; ".join(problems) + "."
        log.warning("Meta description inválida (intento %d/%d): %s", attempt, attempts, feedback)
    return None


if __name__ == "__main__":
    # Self-check: carga el módulo y valida la estructura de fallback (sin red).
    assert len(DEFAULT_MODELS) >= 2, "debe haber al menos un modelo de fallback"
    assert "3.1-flash-lite" in DEFAULT_MODELS[0]
    assert 503 in RETRYABLE and 400 not in RETRYABLE
    print("gemini_client OK:", ", ".join(DEFAULT_MODELS))
