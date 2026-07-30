---
layout: page
title: "Entidades — Infraestructura de conocimiento sobre IA en Paraguay"
description: "Indice de entidades clave del Observatorio de IA en Paraguay. MITIC, ANDE, Itaipu, Yguazu Digital, Taiwan, CONACYT y mas. Perfiles con articulos, leyes, cronologia y fuentes verificables."
permalink: /entidades/
last_modified_at: 2026-07-30
---

El observatorio de muchotexto.net ha acumulado informacion verificada sobre las instituciones, empresas, proyectos y actores que definen el panorama de la inteligencia artificial en Paraguay. Esta pagina organiza ese conocimiento por entidad.

Cada ficha reune articulos, leyes, datos cronologicos y fuentes extraidos exclusivamente del contenido ya publicado y verificado del observatorio. No se genera informacion nueva: se estructura la que ya existe.

<div class="entity-grid">
{% assign entities = site.data.entities | sort: "name" %}
{% for entity in entities %}
{% if entity.featured or entities.size <= 20 %}
<article class="entity-card">
  <h3><a href="/entidades/{{ entity.slug }}/">{{ entity.name }}</a></h3>
  <p class="entity-card-desc">{{ entity.description | truncate: 200 }}</p>
  <div class="entity-card-meta">
    <span class="entity-card-category">{{ entity.category | capitalize }}</span>
    {% assign count = 0 %}
    {% for post in site.posts %}
      {% assign content_lower = post.content | downcase %}
      {% for kw in entity.keywords %}
        {% assign kw_lower = kw | downcase %}
        {% if content_lower contains kw_lower %}
          {% assign count = count | plus: 1 %}
          {% break %}
        {% endif %}
      {% endfor %}
    {% endfor %}
    <span class="entity-card-count">{{ count }} articulos</span>
  </div>
</article>
{% endif %}
{% endfor %}
</div>
