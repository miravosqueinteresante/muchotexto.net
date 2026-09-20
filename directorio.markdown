---
layout: page
title: "Directorio de IA en Paraguay"
permalink: /directorio/
description: "Startups, aceleradoras, comunidades, eventos y espacios de inteligencia artificial y tecnologia en Paraguay."
last_modified_at: 2026-09-18
---

Este directorio se actualiza constantemente. Si conocés una startup, comunidad o evento que debería estar acá, [escribinos](/contacto/).

> Esta página se genera desde una fuente única: el seed curado más las entradas que cada artículo declara en su front matter. No se edita a mano — ver `/como-trabajamos/`.

{% for grupo in site.data.directorio %}
## {{ grupo.seccion }}
{% if grupo.intro %}

{{ grupo.intro }}
{% endif %}

{% for it in grupo.items -%}
{% if it.url %}- **[{{ it.nombre }}]({{ it.url }})** — {{ it.descripcion }}
{% else %}- **{{ it.nombre }}** — {{ it.descripcion }}
{% endif %}
{% endfor %}
{% if grupo.nota %}
{{ grupo.nota }}
{% endif %}
{% endfor %}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "@id": "https://muchotexto.net/directorio/#directory",
  "name": "Directorio de IA en Paraguay",
  "description": "Startups, aceleradoras, comunidades y espacios de inteligencia artificial y tecnología en Paraguay.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": { "@type": "Organization", "name": "KOGA Impact Lab", "url": "https://koga.com.py/", "description": "Aceleradora y hub de innovación con más de 14 años operando en Paraguay." }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": { "@type": "Organization", "name": "HIVE Digital Technologies", "url": "https://www.hivedigitaltechnologies.com/", "description": "Opera un campus de 100 MW de cómputo GPU en Yguazú con energía de Itaipú." }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": { "@type": "Organization", "name": "Yguazú Digital", "description": "Proyecto binacional Paraguay-Taiwán para construir un data center de IA de hasta 1 GW." }
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": { "@type": "Organization", "name": "Autograph", "description": "Startup paraguaya de IA en el ecosistema local." }
    },
    {
      "@type": "ListItem",
      "position": 5,
      "item": { "@type": "Organization", "name": "BUZZ AI Cloud", "description": "Primer cluster de GPU para inteligencia artificial en Paraguay." }
    }
  ]
}
</script>
