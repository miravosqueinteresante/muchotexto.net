---
layout: page
title: Cómo trabajamos
permalink: /como-trabajamos/
description: "Metodología editorial de muchotexto.net: cómo seleccionamos fuentes, verificamos datos, usamos inteligencia artificial y corregimos errores."
---

**muchotexto.net** es un medio de análisis interpretativo y editorial que utiliza inteligencia artificial como asistente en el proceso de producción de contenido. Esta página explica con transparencia cómo funciona ese proceso.

## Origen de la información

No producimos noticias de primera mano. Tomamos información ya publicada por medios paraguayos y la organizamos, sintetizamos e interpretamos.

Nuestro sistema recolecta diariamente el contenido de **15 fuentes de noticias** vía RSS, entre ellas ABC Color, La Nación, Última Hora, Diario HOY, La Tribuna, NPY, RDN y otros medios nacionales. Los criterios de selección son: que el medio tenga cobertura nacional verificable, que ofrezca un feed RSS público y actualizado, que represente un espectro editorial diverso y que tenga una trayectoria reconocible en el periodismo paraguayo. Revisamos periódicamente esta selección y podemos agregar o retirar fuentes según su consistencia y relevancia. Toda la información que procesamos proviene de fuentes públicas y atribuibles.

## Qué hace la inteligencia artificial

La IA asiste en tres tareas específicas:

- **Lectura y resumen**: procesa cientos de titulares y notas para identificar los temas de mayor volumen de conversación cada día.
- **Síntesis estructurada**: organiza la información en categorías temáticas (política, economía, seguridad, deportes, cultura), estima la temperatura social de cada tema y redacta resúmenes basados exclusivamente en el contenido de las fuentes.
- **Análisis editorial**: a partir del resumen diario, genera un artículo de opinión que busca patrones, conexiones y preguntas relevantes sobre la realidad paraguaya.

El modelo utilizado es **GPT-4o** (OpenAI), ejecutado a través de GitHub Models. Cada interacción con la IA está gobernada por un _system prompt_ que establece reglas estrictas: no inventar hechos ni nombres, no especular sin fundamento, usar español paraguayo natural y mantener una perspectiva crítica pero no partidista.

La IA **no decide** qué se publica ni cuál es la línea editorial. Su rol es exclusivamente instrumental: leer, resumir, organizar y redactar borradores.

## Qué hace el editor humano

El editor humano —César Sánchez— tiene a su cargo:

- **Definir la línea editorial** y los principios que gobiernan el _system prompt_ de la IA.
- **Seleccionar y mantener las fuentes**: qué medios se incluyen, cuáles se agregan o se retiran, y por qué.
- **Escribir y editar los artículos de fondo** (ensayos long-form de 1.500 a 2.500 palabras) con asistencia de agentes de IA para la fase de investigación (ver sección siguiente). El editor es el responsable intelectual y editorial del artículo. Las herramientas de IA se utilizan como asistentes de investigación y apoyo a la redacción, pero no sustituyen el juicio editorial humano.
- **Revisar por muestreo** el contenido automatizado diario: se revisa manualmente una muestra representativa de las publicaciones automatizadas y se amplía la revisión cuando se detectan inconsistencias.
- **Corregir errores** cuando son detectados o reportados por lectores.

## Proceso de investigación con agentes de IA

Los artículos de fondo siguen un proceso estructurado de 7 pasos donde la IA actúa como asistente de investigación, no como autor:

1. **Selección del tema**: verificamos contra nuestro calendario editorial de 42 temas que el tópico no esté duplicado y tenga ángulo original.
2. **Plan de investigación**: creamos un directorio `research_[tema]/` con un `research_plan.md` que define la pregunta principal, 4 o 5 subtemas específicos y las fuentes esperadas (institutos públicos, papers académicos, documentos oficiales, informes sectoriales).
3. **Investigación paralela con agentes**: desplegamos de 4 a 5 agentes de IA independientes usando **OpenCode** con capacidad de búsqueda web. Cada agente investiga un subtema distinto en simultáneo, rastreando fuentes primarias verificables. Los resultados se escriben en archivos `findings_N.md` dentro del directorio de investigación.
4. **Síntesis de hallazgos**: el editor lee y cruza todos los findings, identificando patrones, contradicciones y conexiones entre subtemas que los agentes no pudieron detectar por sí solos.
5. **Redacción**: el editor escribe el artículo con estructura hook → contexto → 4 a 6 secciones H2 → conclusión → fuentes, usando los hallazgos como materia prima verificada.
6. **Enlazado interno**: se insertan de 2 a 3 enlaces a otros artículos del sitio, anclados exclusivamente en hechos verificables presentes en los findings (regla anti-alucinación: si no hay soporte factual, no se crea el enlace).
7. **Validación**: el artículo pasa por un script de control de calidad (`validate_publish.py`) que verifica longitud del título, detección de clickbait, presencia de schema FAQ, enlace al cluster de IA en Paraguay, conteo de palabras, acentos y metadatos SEO antes de ser publicado.

Este proceso reduce significativamente el riesgo de alucinaciones y busca que cada artículo de fondo esté respaldado por fuentes primarias verificables.

## Infraestructura y herramientas

Todo el desarrollo, mantenimiento y operación del sitio se gestiona mediante **OpenCode**, un entorno de desarrollo asistido por IA que permite coordinar agentes, ejecutar scripts y desplegar cambios.

Los modelos de lenguaje utilizados en las distintas etapas del proyecto son:

| Modelo | Uso principal |
|---|---|
| **DeepSeek** | Investigación con agentes, razonamiento analítico y redacción asistida de artículos de fondo |
| **MiniMax** | Procesamiento de contenido y tareas de síntesis |
| **Qwen** | Asistencia en desarrollo, mantenimiento del sitio y validación de código |
| **GPT-4o** | Generación automatizada de Pulso Paraguay y Editorial Diaria (vía GitHub Models) |

La combinación de múltiples modelos permite aprovechar las fortalezas de cada uno: razonamiento profundo para la investigación, eficiencia para el contenido automatizado diario, y capacidad de desarrollo para el mantenimiento técnico del sitio.

## Cómo verificamos los datos

- **Pulso Paraguay y Editorial Diaria**: toda afirmación fáctica proviene de las fuentes originales procesadas ese día. La IA no genera datos propios. Si una fuente se equivoca, podemos heredar ese error; por eso cada publicación incluye la lista completa de fuentes consultadas para que el lector pueda verificarlas por su cuenta.
- **Artículos de fondo**: cada afirmación estadística, económica o factual se respalda con enlaces a fuentes originales verificables (institutos públicos, papers académicos, documentos oficiales, informes sectoriales). Si un dato no puede ser verificado con una fuente primaria, se indica explícitamente.

### Qué ocurre cuando las fuentes discrepan

En el procesamiento diario de noticias, es habitual que distintos medios reporten versiones diferentes de un mismo hecho. Nuestro sistema aplica el siguiente criterio:

- Si dos o más fuentes coinciden en un dato, se toma como versión principal y se indica que existe consenso entre medios.
- Si las fuentes discrepan, se reportan las distintas versiones atribuyendo cada una a su medio de origen, sin tomar partido por ninguna.
- Si la discrepancia es sobre un dato factual verificable (una cifra oficial, una fecha, un nombre), el editor humano puede intervenir para contrastar con la fuente primaria correspondiente.

Este enfoque permite que el lector conozca tanto los puntos de consenso como las divergencias entre medios, y saque sus propias conclusiones.

## Cómo corregimos errores

Si detectás un error en cualquier contenido de muchotexto.net:

1. Escribinos a través de la [página de contacto](/contacto/) detallando el error y, si es posible, la fuente que lo corrige.
2. Revisaremos el reporte y, de confirmarse el error, corregiremos el contenido indicando la fecha de la última modificación.
3. Las correcciones sustanciales se mencionan al pie del artículo con una nota de fe de erratas.

Cada artículo registra en sus metadatos una fecha de última modificación (`last_modified_at`). Esta fecha se vuelve visible para el lector junto a la fecha de publicación original cuando el artículo fue corregido con posterioridad.

## Principios editoriales

1. **Atribución**: toda información que procesamos tiene un origen identificable. No publicamos rumores ni filtraciones anónimas.
2. **Independencia**: no recibimos financiamiento de partidos políticos, gobiernos ni corporaciones para influir en nuestra línea editorial. El sitio se sostiene con publicidad no intrusiva.
3. **Transparencia metodológica**: explicamos cómo producimos cada tipo de contenido y qué rol juega la IA en cada caso.
4. **Corrección sobre orgullo**: si nos equivocamos, lo corregimos y lo decimos. La credibilidad se construye admitiendo errores.
5. **Sin sensacionalismo**: no publicamos contenido diseñado exclusivamente para generar clics, indignación o miedo. Buscamos análisis, no viralidad.

## Declaración sobre uso de IA

Todo contenido generado con asistencia de IA se identifica como tal. En cada publicación de Pulso Paraguay y Editorial Diaria se indica explícitamente que fue generada por inteligencia artificial, se nombra el modelo utilizado y se explica el proceso.

Consideramos que el uso de IA en la producción de contenido es legítimo siempre que:
- Sea transparente para el lector.
- No sustituya el criterio editorial humano.
- No invente hechos ni atribuya declaraciones falsas.
- Se base en fuentes verificables y atribuibles.

## Conflictos de interés

El editor de muchotexto.net, César Sánchez, trabaja como consultor independiente en proyectos de automatización con IA generativa, anotación de datos y desarrollo de soluciones basadas en IA. Esta actividad profesional es previa a la creación del sitio y es independiente de su línea editorial.

Si en el futuro existiera un conflicto de interés potencial entre un tema tratado y la actividad profesional del editor, se declarará explícitamente en el artículo correspondiente.
