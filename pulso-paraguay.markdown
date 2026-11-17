---
layout: page
title: "Pulso Paraguay"
permalink: /pulso-paraguay/
description: "Archivo de Pulso Paraguay: el resumen diario de noticias de muchotexto.net, ordenado por mes."
last_modified_at: 2026-11-17
---

Pulso Paraguay es el resumen diario de noticias del sitio. Acá quedan ordenadas todas las ediciones por mes, de la más reciente a la más antigua, para que no se pierdan en el archivo general.

Si buscás un tema puntual, usá el [buscador](/buscar/) o el [archivo completo](/archive/).

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
