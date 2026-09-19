---
layout: page
title: "Casos de uso de IA en Paraguay"
permalink: /casos-de-uso/
description: "Cómo se usa la inteligencia artificial en sectores productivos de Paraguay. Casos documentados con fuentes verificables."
last_modified_at: 2026-09-18
---

Cada caso enlaza con el artículo completo donde se analiza con fuentes verificables.

> Esta página se genera desde una fuente única: el seed curado más los casos que cada artículo declara en su front matter. No se edita a mano — ver `/como-trabajamos/`.

{% for grupo in site.data.casos %}
## {{ grupo.tema }}

{% for c in grupo.casos -%}
{% if c.url %}- **[{{ c.titulo }}]({{ c.url }})** — {{ c.texto }}
{% else %}- **{{ c.titulo }}** — {{ c.texto }}
{% endif %}
{% endfor %}

{% endfor %}
