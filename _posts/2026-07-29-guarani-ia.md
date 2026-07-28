---
layout: post
title: "Paraguay está enseñando guaraní a la inteligencia artificial"
date: 2026-07-29
last_modified_at: 2026-07-29
categories: articulos
tags: cultura-filosofia ia-paraguay paraguay ia
description: "El guaraní tiene 7 millones de hablantes y está ausente de los grandes modelos de voz e IA generativa. Un grupo de periodistas paraguayos está cambiando eso con mingas comunitarias y datos abiertos."
---

De los aproximadamente 7.000 idiomas que se hablan en el mundo, diversos estudios estiman que el 95% carece de herramientas de inteligencia artificial. Ni reconocimiento de voz, ni traducción automática, ni chatbot. El guaraní —lengua oficial de Paraguay junto con el español, hablada por entre 7 y 9 millones de personas en Paraguay, Argentina y Bolivia— es uno de ellos. OpenAI nunca lo incluyó en Whisper. Meta no lo incluyó en el pre-entrenamiento de XLS-R, su modelo más usado para lenguas de pocos recursos —no existe evidencia de que el corpus de entrenamiento contuviera suficiente guaraní. Mozilla Common Voice, el mayor repositorio abierto de voces del mundo con más de 250 idiomas, no tiene al guaraní en su plataforma.

Pero un grupo de periodistas paraguayos está cambiando eso. No desde un laboratorio de Silicon Valley ni con millones de dólares de inversión, sino con mingas —encuentros comunitarios donde la gente se junta a grabar su voz, validar frases y construir el primer dataset abierto de guaraní hablado. El proyecto se llama **AIkuaa** y lo lidera El Surti, un medio independiente paraguayo fundado en 2016 que entendió, antes que muchos gobiernos, que la supervivencia de una lengua en el siglo XXI depende de su presencia digital.

> **En resumen:**
> - El guaraní es hablado por 7-9 millones de personas pero está ausente de los grandes modelos de reconocimiento de voz (Whisper, XLS-R) y del mayor repositorio abierto de voces (Common Voice).
> - **AIkuaa** (El Surti) está creando el primer dataset comunitario de voz en guaraní en Common Voice mediante mingas comunitarias, con un modelo wav2vec2 ya publicado en HuggingFace.
> - La tecnología para entrenar IA en guaraní es barata (USD 100-500 en GPU con 10-50 horas de audio transcrito). Lo que falta no es plata sino datos.
> - El mundo tiene casos de éxito impulsados por comunidades (maorí) o con inversión pública (catalán, galés) y fracasos de Big Tech (quechua en Google Translate). La diferencia: inversión estatal sostenida + comunidad organizada.

## Por qué el guaraní no existe para la IA

El problema no es técnico. Es de datos. Entrenar un modelo de reconocimiento de voz para un idioma nuevo cuesta entre 100 y 500 dólares en cómputo GPU si se tienen entre 10 y 50 horas de audio transcrito. Es dinero de bolsillo para cualquier laboratorio de IA. Lo que no existe es el dataset: las horas de grabación, la transcripción verificada, el corpus de texto.

Meta entrenó su modelo MMS (Massively Multilingual Speech) en 1.107 idiomas usando grabaciones de la Biblia como fuente principal. Es una solución ingeniosa pero limitada: el corpus bíblico tiene un registro lingüístico muy específico que no sirve para entender a una persona pidiendo un turno médico o denunciando un abuso. El guaraní necesita datos diversos: conversaciones cotidianas, noticias, consultas.

La Secretaría de Políticas Lingüísticas (SPL) de Paraguay —el organismo estatal que debería liderar esta tarea— tiene tres direcciones generales según la Ley 4251 (Planificación Lingüística, Investigación Lingüística, Documentación y Promoción de Lenguas Indígenas) y presupuesto para publicaciones impresas, no para datasets de entrenamiento. La Constitución de 1992 declaró al guaraní idioma oficial junto con el español (Artículo 140). La Ley de Lenguas 4251 de 2010 creó la SPL y estableció la obligación estatal de promover ambas lenguas en igualdad de condiciones. En papel, Paraguay es un país bilingüe. En la práctica digital, no.

Entre 2002 y 2012, el uso del guaraní como lengua habitual en el hogar cayó aproximadamente 10 puntos porcentuales según los censos nacionales. Diversos investigadores señalan que la escasa presencia digital del guaraní —en internet, celulares y aplicaciones— es uno de los factores que acelera su desplazamiento, junto con la urbanización, la escolarización en español y las presiones del mercado laboral. Una lengua que no se puede hablar con un asistente de voz es una lengua que los jóvenes abandonan porque no les sirve para el mundo en el que viven.

## AIkuaa: la minga como infraestructura cultural

En 2024, El Surti postuló AIkuaa al JournalismAI Innovation Challenge —un programa de la London School of Economics financiado por Google News Initiative— y entró en la cohorte de 35 seleccionados globales.

El diseño de AIkuaa es deliberadamente comunitario. En vez de contratar un estudio de grabación y actores de voz profesionales, El Surti organiza mingas —el término guaraní para el trabajo colectivo solidario— donde voluntarios graban frases en guaraní usando la plataforma Common Voice de Mozilla. Cada participante lee oraciones en pantalla y las graba con su celular. Otros voluntarios validan las grabaciones. El resultado es un dataset de voces reales, con acentos y variaciones dialectales genuinas, construido por la propia comunidad de hablantes.

Sobre esa base, el equipo técnico —liderado por Neyen Luchelli en el desarrollo del bot e IA— construyó SurtiLab-GTranscriptor, una API abierta que permite transcribir audio en guaraní a texto usando el modelo wav2vec2-xlsr-300m-guarani disponible en HuggingFace. Ese modelo, entrenado por Ivan G. Torre sobre el dataset Americas NLP 2022, alcanza una tasa de error de caracteres (CER) del 17.62%, funcional para un primer prototipo. El proyecto también desarrolló un chatbot de WhatsApp que procesa guaraní hablado. La dirección editorial está a cargo de Jazmín Acuña; la comunidad y recolección de datos, de Laila Bareiro.

## Lo que otros hicieron (y Paraguay puede copiar)

El guaraní no es la primera lengua minorizada que enfrenta este desafío. Los casos de éxito comparten un patrón.

Nueva Zelanda invirtió durante años en tecnología para el maorí —lengua oficial junto con el inglés, hablada por unas 213.000 personas según el censo de 2023— a través de Te Hiku Media, una organización comunitaria maorí que desarrolló modelos de reconocimiento de voz con soberanía de datos: el dataset no se entrega a las grandes tecnológicas, se mantiene bajo control de la comunidad.

En Cataluña, el proyecto AINA —financiado por la Generalitat y ejecutado desde el Barcelona Supercomputing Center— creó datasets y modelos de IA para el catalán. Por separado, el gobierno español lanzó el programa ILENIA, que agrupa proyectos para cada lengua cooficial: AINA (catalán), GAITU (euskera), NÓS (gallego) y VIVES (valenciano), con el BSC como coordinador.

El galés —con aproximadamente 538.000 hablantes según el censo de 2021, la décima parte que el guaraní— cuenta con más herramientas de IA gracias a años de inversión pública sostenida. La diferencia no está en la cantidad de hablantes. Está en la decisión política de invertir.

El contraejemplo es el quechua. Google lo agregó a Google Translate en 2022. La precisión es tan baja que las comunidades quechuahablantes lo consideran poco confiable para comunicación real. El problema no fue la tecnología sino el enfoque: lanzar una funcionalidad para un comunicado de prensa, sin involucrar a la comunidad de hablantes en el diseño ni en la validación. Investigadores del AmericasNLP han documentado que los modelos de traducción para lenguas indígenas entrenados sin datos comunitarios obtienen resultados significativamente peores que aquellos desarrollados con participación local.

## El costo real de la exclusión

Cuando una lengua queda fuera de la IA, quedan fuera sus hablantes. Los sistemas de reconocimiento de voz son la puerta de entrada a servicios que se están digitalizando: turnos médicos, trámites bancarios, denuncias, asistencia en emergencias. Un guaranihablante monolingüe depende de la misma tecnología que podría traducirlo en tiempo real pero no lo hace porque nadie entrenó el modelo.

La desinformación es otro vector. Los modelos de lenguaje generan texto convincente en los idiomas para los que fueron entrenados. En los que no, simplemente no existen. En un ecosistema informativo donde la desinformación circula por WhatsApp, una comunidad lingüística sin herramientas de IA para detectar y responder en su propio idioma está doblemente vulnerable.

La Ley de Lenguas obliga al Estado a "garantizar el uso de las lenguas oficiales en los medios de comunicación social y en las nuevas tecnologías de la información y comunicación". Ese artículo se escribió en 2010, antes de los modelos de lenguaje masivos. Dieciséis años después, la SPL no tiene un dataset público de voz en guaraní. Lo está construyendo un medio independiente con una subvención del JournalismAI de la LSE, financiado por Google News Initiative.

## La minga no reemplaza una política de Estado

Lo que AIkuaa demuestra no es solo que se puede hacer —es que se puede hacer bien, con recursos modestos, desde Paraguay y con la comunidad como protagonista. El modelo wav2vec2 funciona. La API de transcripción está publicada. El chatbot de WhatsApp está operativo. El dataset crece con cada minga.

Pero una minga no reemplaza una política de Estado. El maorí no sobrevive en el mundo digital porque Te Hiku Media hace un buen trabajo —sobrevive porque el gobierno neozelandés invierte en tecnología lingüística. El catalán no tiene modelos de IA porque un grupo de voluntarios los construyó un fin de semana —los tiene porque hubo inversión pública sostenida.

Paraguay tiene la ventaja de llegar tarde. Sabe qué funciona (comunidad + inversión estatal + datos abiertos) y qué no (lanzar un producto para el comunicado de prensa sin involucrar a los hablantes). Tiene un proyecto funcionando —AIkuaa— que ya resolvió los problemas técnicos más difíciles. Lo que no tiene es la decisión de escalarlo. La SPL podría financiar la recolección de datos. El MITIC podría integrar el modelo en los servicios digitales del Estado. Las herramientas existen. Los datos existen. La comunidad existe. Falta la voluntad de tratarlo como lo que es: un problema de derechos lingüísticos, no de tecnología.

*Este artículo es parte del [Observatorio de IA en Paraguay](/ia-en-paraguay/), una guía viva sobre cómo la inteligencia artificial está transformando el país.*

## Fuentes

1. [El Surti — "AIkuaa, un proyecto para enseñar Guaraní a la Inteligencia Artificial"](https://elsurti.com/aikuaa/) (2025)
2. [HuggingFace — wav2vec2-xlsr-300m-guarani](https://huggingface.co/ivangtorre/wav2vec2-xlsr-300m-guarani)
3. [Mozilla Common Voice](https://commonvoice.mozilla.org/)
4. [JournalismAI — Innovation Challenge](https://www.journalismai.info/programmes/innovation)
5. [Meta AI — MMS: Scaling Speech Technology to 1,000+ Languages](https://ai.meta.com/blog/multilingual-model-speech-recognition/)
6. [Te Hiku Media — Papa Reo (Māori language AI)](https://tehiku.nz/)
7. [Barcelona Supercomputing Center — Proyecto AINA](https://www.bsc.es/es/aina)
8. [Constitución de Paraguay (1992) — Artículo 140](https://www.bacn.gov.py/leyes-paraguayas/9580/constitucion-nacional-de-1992)
9. [Ley 4251/2010 — Ley de Lenguas de Paraguay](https://www.bacn.gov.py/leyes-paraguayas/689/ley-n-4251-de-lenguas)
10. [Wikipedia en guaraní](https://gn.wikipedia.org/)
11. [UNESCO — Atlas of the World’s Languages in Danger](https://en.wales/)
12. [Ethnologue — Guaraní, Paraguayan](https://www.ethnologue.com/language/gug/)
13. [Meta AI — XLS-R: Self-supervised Cross-lingual Speech Representation Learning at Scale](https://arxiv.org/abs/2111.09296)
14. [AmericasNLP — Workshop on Natural Language Processing for Indigenous Languages of the Americas](https://turing.iimas.unam.mx/americasnlp/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿El guaraní está incluido en los modelos de inteligencia artificial?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. El guaraní está ausente de los principales modelos de reconocimiento de voz (Whisper, XLS-R) y de Common Voice, el mayor repositorio abierto de voces. De los aproximadamente 7.000 idiomas del mundo, el 95% carece de herramientas de IA. El proyecto paraguayo AIkuaa (El Surti) está creando el primer dataset comunitario de voz en guaraní en Common Voice mediante mingas comunitarias."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué es AIkuaa y quién lo desarrolla?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AIkuaa es un proyecto de El Surti, un medio independiente paraguayo fundado en 2016, financiado por el JournalismAI Innovation Challenge 2024 (London School of Economics / Google News Initiative). Organiza mingas comunitarias para grabar voces en guaraní en Mozilla Common Voice y adoptó un modelo wav2vec2 entrenado por Iván G. Torre (17.62% CER) y lo publicó en HuggingFace. Desarrolló una API abierta de transcripción y un chatbot de WhatsApp."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué otros países han desarrollado IA para lenguas indígenas o minoritarias?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nueva Zelanda (Te Hiku Media: maorí, con soberanía de datos comunitaria), Cataluña (proyecto AINA: catalán, financiado por la Generalitat), y Gales (inversión pública en tecnología para el galés). El patrón común es inversión estatal sostenida más comunidad organizada. El contraejemplo es el quechua en Google Translate (2022), lanzado sin involucrar a la comunidad y con baja precisión."
      }
    }
  ]
}
</script>
