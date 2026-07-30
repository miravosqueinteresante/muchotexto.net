---
layout: page
title: "Entidades — Infraestructura de conocimiento sobre IA en Paraguay"
description: "Índice de entidades clave del Observatorio de IA en Paraguay. MITIC, ANDE, Itaipú, Yguazú Digital, Taiwán y más. Perfiles con artículos, leyes, cronología y fuentes verificables."
permalink: /entidades/
last_modified_at: 2026-07-30
---

El observatorio de muchotexto.net ha acumulado información verificada sobre las instituciones, empresas, proyectos y actores que definen el panorama de la inteligencia artificial en Paraguay. Esta página organiza ese conocimiento por entidad.

Cada ficha reúne artículos, leyes, datos cronológicos y fuentes extraídos exclusivamente del contenido ya publicado y verificado del observatorio. No se genera información nueva: se estructura la que ya existe.

<div class="entity-grid">
{% assign entities = site.data.entities | sort: "name" %}
{% for entity in entities %}
<article class="entity-card">
  <h3><a href="/entidades/{{ entity.slug }}/">{{ entity.name }}</a></h3>
  <p class="entity-card-desc">{{ entity.description | truncate: 200 }}</p>
  <div class="entity-card-meta">
    <span class="entity-card-category">{{ entity.category | capitalize }}</span>
  </div>
</article>
{% endfor %}
</div>
