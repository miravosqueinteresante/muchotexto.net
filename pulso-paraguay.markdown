---
layout: page
title: "Pulso Paraguay"
permalink: /pulso-paraguay/
description: "Archivo completo de Pulso Paraguay: todas las ediciones diarias ordenadas por mes, con enlaces a las fuentes y al contexto de cada jornada"
last_modified_at: 2026-11-17
---

Pulso Paraguay es el resumen diario de noticias del sitio. Acá quedan ordenadas todas las ediciones por mes, de la más reciente a la más antigua, para que no se pierdan en el archivo general.

Si buscás un tema puntual, usá el [buscador](/buscar/) o el [archivo completo](/archive/).

El archivo está separado por mes para que puedas seguir la evolución de la agenda sin mezclar ediciones. Cada página mensual lista solo los Pulso de ese mes; desde ahí podés abrir la edición completa, revisar sus fuentes y volver al índice. No es una lista de artículos de análisis: es el registro de la cobertura diaria, con la fecha y el título original de cada edición. Si querés ver cómo cambió la agenda, compará dos meses consecutivos.

{% assign pulsos = site.categories["pulso-paraguay"] | sort: "date" | reverse %}
{% assign grupos = pulsos | group_by_exp: "post", "post.date | date: '%Y-%m'" %}

<ul class="post-list-by-taxonomy">
{% for grupo in grupos %}
  {% assign partes = grupo.name | split: "-" %}
  <li>
    <a href="{{ '/pulso-paraguay/' | append: partes[0] | append: '/' | append: partes[1] | append: '/' | relative_url }}">
      {{ grupo.name }}
    </a>
    — {{ grupo.size }} ediciones
  </li>
{% endfor %}
</ul>
