---
layout: page
title: "Cronología de la IA en Paraguay"
permalink: /cronologia/
description: "Cronología de la IA en Paraguay: hitos de energía, infraestructura, datos y regulación desde 1965 hasta las fechas anunciadas para 2027-2040"
last_modified_at: 2026-11-17
---

Cada hito enlaza con el artículo completo donde se analiza en profundidad con fuentes verificables.

> Esta página se genera a partir de una fuente única: los hitos declarados en el front matter de cada artículo, más un *seed* curado de contexto histórico. No se edita a mano — ver `/como-trabajamos/`.

La cronología está dividida por etapas para que puedas leerla como un proceso, no como una lista infinita. Cada sección tiene su propia página y enlaces al artículo donde se analiza el hito. Las fechas futuras están separadas en “Lo que viene” y no son hechos consumados: son anuncios, proyecciones o vencimientos normativos.

{% for grupo in site.data.cronologia %}
{% assign sec_slug = grupo.seccion | slugify %}
## {{ grupo.seccion }}

<p>{{ grupo.items.size }} hitos. <a href="{{ '/cronologia/' | append: sec_slug | append: '/' | relative_url }}">Ver sección {{ grupo.seccion }}</a></p>

{% endfor %}
