---
layout: page
title: "Glosario de IA en Paraguay"
permalink: /glosario/
description: "Glosario de terminos clave de inteligencia artificial en Paraguay explicados en contexto local."
last_modified_at: 2026-09-18
---

Este glosario reúne los términos clave sobre inteligencia artificial en Paraguay y los explica en contexto local. Cada definición conecta con un artículo completo de la [guía de IA en Paraguay](/ia-en-paraguay/), donde el tema se trata en profundidad con fuentes y datos verificables.

Los términos están agrupados por tema: infraestructura y energía, tecnología IA, geopolítica, fintech, startups, agro, justicia, y comercio electrónico y logística. No están ordenados alfabéticamente sino por relación temática, para que el lector pueda explorar por bloques de interés.

> Esta página se genera desde una fuente única: los términos del seed curado más los que cada artículo declara en su front matter. No se edita a mano — ver `/como-trabajamos/`.

{% for grupo in site.data.glosario %}
## {{ grupo.tema }}

{% for t in grupo.terminos -%}
**{{ t.termino }}** — {{ t.definicion }}
{% if t.link %}
→ [{{ t.link_text }}]({{ t.link }})
{% endif %}

{% endfor %}
{% endfor %}

---

Este glosario se actualiza a medida que crece el ecosistema. Para un análisis completo de cada tema, visita la [guía de IA en Paraguay](/ia-en-paraguay/).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "DefinedTermSet",
  "@id": "https://muchotexto.net/glosario/#glossary",
  "name": "Glosario de IA en Paraguay",
  "description": "Términos clave de inteligencia artificial explicados en contexto paraguayo.",
  "hasDefinedTerm": [
    {
      "@type": "DefinedTerm",
      "name": "Data center",
      "description": "Instalación que alberga miles de servidores funcionando 24/7 para procesar y almacenar datos."
    },
    {
      "@type": "DefinedTerm",
      "name": "GPU",
      "description": "Chip especializado en cálculo paralelo, esencial para entrenar modelos de inteligencia artificial."
    },
    {
      "@type": "DefinedTerm",
      "name": "MW (megavatio)",
      "description": "Unidad de potencia eléctrica. La capacidad de un data center se mide en MW."
    },
    {
      "@type": "DefinedTerm",
      "name": "PUE",
      "description": "Índice que mide la eficiencia energética de un data center."
    },
    {
      "@type": "DefinedTerm",
      "name": "GCIE",
      "description": "Programa tarifario de la ANDE para grandes consumidores de energía intensiva (criptomineras y data centers), con tarifas por nivel de tensión. 943,8 MW reservados a julio 2026."
    },
    {
      "@type": "DefinedTerm",
      "name": "Yguazú Digital",
      "description": "Proyecto binacional Paraguay-Taiwán para construir uno de los centros de datos de IA más grandes del mundo."
    }
  ]
}
</script>
