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


if __name__ == "__main__":
    # Self-check: carga el módulo y valida la estructura de fallback (sin red).
    assert len(DEFAULT_MODELS) >= 2, "debe haber al menos un modelo de fallback"
    assert "3.1-flash-lite" in DEFAULT_MODELS[0]
    assert 503 in RETRYABLE and 400 not in RETRYABLE
    print("gemini_client OK:", ", ".join(DEFAULT_MODELS))
