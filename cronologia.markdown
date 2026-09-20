---
layout: page
title: "Cronología de la IA en Paraguay"
permalink: /cronologia/
description: "Hitos de la inteligencia artificial, tecnologia y energia en Paraguay desde 1973 hasta hoy."
last_modified_at: 2026-09-18
---

Cada hito enlaza con el artículo completo donde se analiza en profundidad con fuentes verificables.

> Esta página se genera a partir de una fuente única: los hitos declarados en el front matter de cada artículo, más un *seed* curado de contexto histórico. No se edita a mano — ver `/como-trabajamos/`.

{% for grupo in site.data.cronologia %}
## {{ grupo.seccion }}

{% for item in grupo.items -%}
- **{{ item.fecha }}** — {{ item.texto }}
{% endfor %}

{% endfor %}
