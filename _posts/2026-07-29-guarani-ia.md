---
layout: post
title: "Paraguay está enseñando guaraní a la inteligencia artificial"
date: 2026-07-29
last_modified_at: 2026-07-29
categories: articulos
tags: cultura-filosofia ia-paraguay paraguay ia
description: "El guaraní no existe para la IA pero un grupo de periodistas paraguayos está cambiando eso con mingas comunitarias y datos abiertos."
---

De los aproximadamente 7.000 idiomas que se hablan en el mundo, el 95% no tiene ninguna herramienta de inteligencia artificial. Ni reconocimiento de voz, ni traducción automática, ni chatbot. El guaraní —lengua oficial de Paraguay junto con el español, hablada por entre 7 y 9 millones de personas en tres países— es uno de ellos. OpenAI nunca lo incluyó en Whisper. Meta no lo incluyó en el pre-entrenamiento de XLS-R, su modelo más usado para lenguas de pocos recursos. Mozilla Common Voice, el mayor repositorio abierto de voces del mundo, no tiene una sola hora de audio en guaraní verificada.

Pero un grupo de periodistas paraguayos está cambiando eso. No desde un laboratorio de Silicon Valley ni con millones de dólares de inversión, sino con mingas —encuentros comunitarios donde la gente se junta a grabar su voz, validar frases y construir el primer dataset abierto de guaraní hablado. El proyecto se llama **AIkuaa** y lo lidera El Surti, un medio independiente paraguayo que entendió, antes que muchos gobiernos, que la supervivencia de una lengua en el siglo XXI depende de su presencia digital.

> **En resumen:**
> - El guaraní es hablado por 7-9 millones de personas pero está ausente de todos los grandes modelos de IA: Whisper, XLS-R, Common Voice.
> - **AIkuaa** (El Surti) está creando el primer dataset abierto de voz en guaraní mediante mingas comunitarias, con un modelo wav2vec2 ya funcionando.
> - La tecnología para entrenar IA en guaraní es barata (~$100-500 en GPU). Lo que falta no es plata sino datos: horas de audio transcrito y validado.
> - El mundo tiene casos de éxito (maorí, galés, catalán) y de fracaso (quechua en Google Translate). La diferencia: inversión estatal sostenida + comunidad organizada.

## Por qué el guaraní no existe para la IA

El problema no es técnico. Es político y de datos. Entrenar un modelo de reconocimiento de voz para un idioma nuevo cuesta entre 100 y 500 dólares en cómputo GPU si se tienen entre 10 y 50 horas de audio transcrito. Es dinero de bolsillo para cualquier laboratorio de IA. Lo que no existe es el dataset: las horas de grabación, la transcripción verificada, el corpus de texto.

Meta entrenó su modelo MMS (Massively Multilingual Speech) en 1.107 idiomas usando grabaciones de la Biblia como fuente principal. Es una solución ingeniosa pero limitada: el corpus bíblico tiene un registro lingüístico muy específico que no sirve para entender a una persona pidiendo un turno médico o denunciando un abuso. El guaraní necesita datos diversos: conversaciones cotidianas, noticias, consultas, trámites.

Mozilla Common Voice tiene más de 250 idiomas en su plataforma. El guaraní no está entre ellos. La Secretaría de Políticas Lingüísticas (SPL) de Paraguay —el organismo estatal que debería liderar esta tarea— tiene cuatro direcciones y presupuesto para publicaciones impresas, no para datasets de entrenamiento. La Constitución de 1992 declaró al guaraní idioma oficial junto con el español. La [Ley de Lenguas 4251](/articulos/2026/07/07/ley-proteccion-datos-paraguay-ia/) de 2010 creó la SPL y estableció la obligación estatal de promover ambas lenguas en igualdad de condiciones. En papel, Paraguay es un país bilingüe. En la práctica digital, es monolingüe en español.

Entre 2002 y 2012, el uso del guaraní cayó aproximadamente 10 puntos porcentuales según los censos nacionales. La causa más citada por los investigadores no es la discriminación —que existe— sino la ausencia del guaraní en internet, en los celulares, en las aplicaciones. Una lengua que no se puede hablar con un asistente de voz es una lengua que los jóvenes abandonan porque no les sirve para el mundo en el que viven.

## AIkuaa: la minga como infraestructura cultural

El Surti es un medio independiente fundado en 2016 que hace periodismo de investigación, narrativo y visual desde Asunción. En 2024, postuló AIkuaa al JournalismAI Innovation Challenge —un programa de la London School of Economics financiado por Google News Initiative que otorga entre 50.000 y 250.000 dólares a proyectos de innovación periodística con IA, y entró en la cohorte de 35 seleccionados globales.

El diseño de AIkuaa es deliberadamente comunitario. En vez de contratar un estudio de grabación y actores de voz profesionales, El Surti organiza mingas —el término guaraní para el trabajo colectivo solidario— donde voluntarios graban frases en guaraní usando la plataforma Common Voice de Mozilla. Cada participante lee oraciones en pantalla y las graba con su celular. Otros voluntarios validan las grabaciones. El resultado es un dataset de voces reales, con acentos y variaciones dialectales genuinas, construido por la propia comunidad de hablantes.

Sobre esa base, el equipo técnico de AIkuaa —liderado por Neyen Luchelli en el desarrollo del bot e IA— entrenó un modelo de reconocimiento de voz basado en wav2vec2-XLSR-300m, un modelo pre-entrenado de Meta diseñado específicamente para adaptarse a idiomas con pocos recursos. El modelo se publicó en HuggingFace, la plataforma de referencia para modelos de IA de código abierto, donde está disponible para cualquier desarrollador del mundo. Su tasa de error de caracteres (CER) es del 17.62%, una métrica modesta comparada con los modelos comerciales de inglés (que bajan del 5%), pero funcional para un primer prototipo.

El proyecto también desarrolló SurtiLab-GTranscriptor, una API abierta que permite transcribir audio en guaraní a texto, y un chatbot de WhatsApp —el canal de comunicación dominante en Paraguay— que procesa guaraní hablado. La dirección editorial está a cargo de Jazmín Acuña; la comunidad y recolección de datos, de Laila Bareiro.

## Lo que otros países hicieron (y Paraguay puede copiar)

El guaraní no es la primera lengua minorizada que enfrenta este desafío. Y los casos de éxito comparten un patrón.

Nueva Zelanda invirtió decenas de millones de dólares en tecnología para el maorí —lengua oficial junto con el inglés, hablada por unas 185.000 personas— a través de Te Hiku Media, una organización comunitaria maorí que desarrolló modelos de reconocimiento de voz y síntesis de habla con soberanía de datos: el dataset no se entrega a las grandes tecnológicas, se mantiene bajo control de la comunidad. El proyecto Papa Reo es el más avanzado del mundo en IA para lenguas indígenas.

España lanzó en 2024 el proyecto AINA, financiado con fondos europeos y ejecutado desde el Barcelona Supercomputing Center, para crear datasets y modelos de IA en catalán, gallego, euskera y otras lenguas cooficiales. La inversión: 30 millones de euros. El resultado: corpus de entrenamiento, modelos de código abierto y asistentes de voz funcionales.

Gales financió durante más de una década el desarrollo de tecnología lingüística para el galés, incluyendo un asistente de voz de la BBC. El galés tiene aproximadamente 900.000 hablantes —la octava parte que el guaraní— y sin embargo cuenta con más herramientas de IA. La diferencia no está en la cantidad de hablantes. Está en la decisión política de invertir.

El contraejemplo es el quechua. Google lo agregó a Google Translate en 2022 con bombo y platillo. La precisión es tan baja que las comunidades quechuahablantes lo consideran inutilizable para comunicación real. El problema no fue la tecnología —Google tiene los mejores modelos de traducción del mundo— sino el enfoque: lanzar una funcionalidad para un comunicado de prensa, sin involucrar a la comunidad de hablantes en el diseño ni en la validación. El resultado es un producto que existe en el papel y no en la práctica.

## El costo real de la exclusión digital

Cuando una lengua queda fuera de la IA, quedan fuera sus hablantes. No es una metáfora. Los sistemas de reconocimiento de voz son la puerta de entrada a servicios esenciales que se están digitalizando: turnos médicos, trámites bancarios, denuncias policiales, asistencia en emergencias. Un guaranihablante monolingüe que llama al 911 y no encuentra un operador que hable su idioma depende de la misma tecnología que podría traducirlo en tiempo real pero no lo hace porque nadie entrenó el modelo.

La desinformación es otro vector. Los modelos de lenguaje grandes (LLMs) generan texto convincente en los idiomas para los que fueron entrenados. En los que no, simplemente no existen —o generan texto incoherente. En un ecosistema informativo donde la desinformación circula por WhatsApp a velocidades imposibles de verificar, una comunidad lingüística sin herramientas de IA para detectar y responder a la desinformación en su propio idioma está doblemente vulnerable.

El artículo 140 de la Constitución paraguaya dice que el guaraní es idioma oficial y que "las lenguas indígenas, así como las de otras minorías, forman parte del patrimonio cultural de la Nación". La Ley de Lenguas obliga al Estado a "garantizar el uso de las lenguas oficiales en los medios de comunicación social y en las nuevas tecnologías de la información y comunicación". Ese artículo se escribió en 2010, antes de que existieran los modelos de lenguaje masivos. Pero su mandato es inequívoco: el Estado debe garantizar la presencia del guaraní en las plataformas digitales. Dieciséis años después, la SPL no tiene un dataset público de voz en guaraní. Lo está construyendo un medio independiente con una subvención de una universidad británica.

## La minga como modelo

Lo que AIkuaa demuestra no es solo que se puede hacer —es que se puede hacer bien, con recursos modestos, desde Paraguay y con la comunidad como protagonista. El modelo wav2vec2 funciona. La API de transcripción está publicada. El chatbot de WhatsApp está operativo. El dataset crece con cada minga.

Pero una minga no reemplaza una política de Estado. El maorí no sobrevive en el mundo digital porque Te Hiku Media hace un buen trabajo —sobrevive porque el gobierno neozelandés invierte millones de dólares al año en tecnología lingüística. El galés no tiene un asistente de voz de la BBC porque un grupo de voluntarios lo construyó un fin de semana —lo tiene porque hubo una década de inversión pública sostenida.

Paraguay tiene la ventaja de llegar tarde. Sabe qué funciona (comunidad + inversión estatal + datos abiertos) y qué no (lanzar un producto para el comunicado de prensa sin involucrar a los hablantes). Tiene un proyecto funcionando —AIkuaa— que ya resolvió los problemas técnicos más difíciles. Lo que no tiene es la decisión de escalarlo. La SPL podría financiar la recolección de datos. El MITIC podría integrar el modelo en los servicios digitales del Estado. El Ministerio de Educación podría incorporar el guaraní digital en la malla curricular. Las herramientas existen. Los datos existen. La comunidad existe. Falta la voluntad de tratarlo como lo que es: un problema de derechos lingüísticos, no de tecnología.

*Este artículo es parte del [Observatorio de IA en Paraguay](/ia-en-paraguay/), una guía viva sobre cómo la inteligencia artificial está transformando el país.*

## Fuentes

1. [El Surti — "AIkuaa, un proyecto para enseñar Guaraní a la Inteligencia Artificial"](https://elsurti.com/aikuaa/) (2025)
2. [El Surti — SurtiLab-GTranscriptor, documentación técnica de la API abierta](https://elsurti.com/wp-content/uploads/2025/09/Documentacion-Tecnica-Transcriptor-2.pdf)
3. [HuggingFace — wav2vec2-xlsr-300m-guarani](https://huggingface.co/ivangtorre/wav2vec2-xlsr-300m-guarani)
4. [Mozilla Common Voice](https://commonvoice.mozilla.org/)
5. [JournalismAI — Innovation Challenge 2024](https://www.journalismai.info/programmes/innovation)
6. [Meta AI — MMS: Scaling Speech Technology to 1,000+ Languages](https://ai.meta.com/blog/multilingual-model-speech-recognition/)
7. [Te Hiku Media — Papa Reo (Māori language AI)](https://tehiku.nz/)
8. [Barcelona Supercomputing Center — Proyecto AINA (lenguas cooficiales España)](https://www.bsc.es/es/aina)
9. [Constitución de Paraguay (1992) — Artículo 140](https://www.bacn.gov.py/leyes-paraguayas/9580/constitucion-nacional-de-1992)
10. [Ley 4251/2010 — Ley de Lenguas de Paraguay](https://www.bacn.gov.py/leyes-paraguayas/689/ley-n-4251-de-lenguas)

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
        "text": "No. El guaraní está ausente de los principales modelos de IA: Whisper (OpenAI), XLS-R (Meta) y Common Voice (Mozilla). De los aproximadamente 7.000 idiomas del mundo, el 95% carece de herramientas de IA. El proyecto paraguayo AIkuaa (El Surti) está creando el primer dataset abierto de voz en guaraní mediante mingas comunitarias."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué es AIkuaa y quién lo desarrolla?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AIkuaa es un proyecto de El Surti, un medio independiente paraguayo, financiado por el JournalismAI Innovation Challenge 2024 (London School of Economics / Google News Initiative). Organiza mingas comunitarias para grabar voces en guaraní en Mozilla Common Voice, entrena modelos de reconocimiento de voz basados en wav2vec2 (con 17.62% de tasa de error), desarrolló una API abierta de transcripción guaraní-texto, y un chatbot de WhatsApp que procesa guaraní hablado."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué otros países han desarrollado IA para lenguas indígenas?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nueva Zelanda (Te Hiku Media: maorí, soberanía de datos), España (proyecto AINA: catalán, gallego, euskera — €30M), Gales (BBC Welsh voice assistant), Canadá (Microsoft Translator: inuktitut). El patrón común es inversión estatal sostenida más comunidad organizada."
      }
    }
  ]
}
</script>
