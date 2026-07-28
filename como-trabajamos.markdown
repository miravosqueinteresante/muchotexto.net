---
layout: page
title: Cómo trabajamos
permalink: /como-trabajamos/
description: "Metodología editorial de muchotexto.net: cómo seleccionamos fuentes, verificamos datos, usamos inteligencia artificial y corregimos errores."
last_modified_at: 2026-07-27
---

**muchotexto.net** es el observatorio de inteligencia artificial en Paraguay. Utiliza inteligencia artificial como asistente en el proceso de producción de contenido. Esta página explica con transparencia cómo funciona ese proceso.

## Origen de la información

No producimos noticias de primera mano. Tomamos información ya publicada por medios paraguayos y la organizamos, sintetizamos e interpretamos.

Nuestro sistema recolecta diariamente el contenido de **15 fuentes de noticias** vía RSS, entre ellas ABC Color, La Nación, Última Hora, Diario HOY, La Tribuna, NPY, RDN y otros medios nacionales. Los criterios de selección son: que el medio tenga cobertura nacional verificable, que ofrezca un feed RSS público y actualizado, que represente un espectro editorial diverso y que tenga una trayectoria reconocible en el periodismo paraguayo. Revisamos periódicamente esta selección y podemos agregar o retirar fuentes según su consistencia y relevancia. Toda la información que procesamos proviene de fuentes públicas y atribuibles.

## Qué hace la inteligencia artificial

La IA asiste en tres tareas específicas:

- **Lectura y resumen**: procesa cientos de titulares y notas para identificar los temas de mayor volumen de conversación cada día.
- **Síntesis estructurada**: organiza la información en categorías temáticas (política, economía, seguridad, deportes, cultura), estima la temperatura social de cada tema y redacta resúmenes basados exclusivamente en el contenido de las fuentes.
- **Análisis editorial**: a partir del resumen diario, genera un artículo de opinión que busca patrones, conexiones y preguntas relevantes sobre la realidad paraguaya.

Para el Pulso Paraguay y la Editorial Diaria, el modelo principal es **GPT-4o** (OpenAI), ejecutado a través de GitHub Models. Para los artículos de fondo, usamos **DeepSeek** como modelo principal de investigación y redacción asistida. Cada modelo se asigna según la tarea: razonamiento profundo para la investigación, eficiencia para el contenido automatizado diario. Cada interacción con la IA está gobernada por un _system prompt_ que establece reglas estrictas: no inventar hechos ni nombres, no especular sin fundamento, usar español paraguayo natural y mantener una perspectiva crítica pero no partidista. La tabla completa de modelos está al final de esta página.

La IA **no decide** qué se publica ni cuál es la línea editorial. Su rol es exclusivamente instrumental: leer, resumir, organizar y redactar borradores.

## Qué hace el editor humano

El editor humano —César Sánchez— tiene a su cargo:

- **Definir la línea editorial** y los principios que gobiernan el _system prompt_ de la IA.
- **Seleccionar y mantener las fuentes**: qué medios se incluyen, cuáles se agregan o se retiran, y por qué.
- **Escribir y editar los artículos de fondo** (ensayos long-form de 1.500 a 2.500 palabras) con asistencia de agentes de IA para la fase de investigación (ver sección siguiente). El editor es el responsable intelectual y editorial del artículo. Las herramientas de IA se utilizan como asistentes de investigación y apoyo a la redacción, pero no sustituyen el juicio editorial humano.
- **Revisar diariamente** el contenido automatizado: cada publicación de Pulso Paraguay y Editorial Diaria es revisada por el editor humano el mismo día de su publicación. No se publica contenido automatizado sin supervisión editorial.
- **Corregir errores** cuando son detectados o reportados por lectores.

## Proceso de investigación con agentes de IA

Los artículos de fondo siguen un proceso estructurado de 11 pasos donde la IA actúa como asistente de investigación, no como autor:

1. **Selección del tema**: verificamos contra nuestro calendario editorial de 42 temas que el tópico no esté duplicado y tenga ángulo original.
2. **Plan de investigación**: creamos un directorio `research_[tema]/` con un `research_plan.md` que define la pregunta principal, 4 o 5 subtemas específicos y las fuentes esperadas (institutos públicos, papers académicos, documentos oficiales, informes sectoriales).
3. **Investigación paralela con agentes**: desplegamos de 4 a 5 agentes de IA independientes usando **OpenCode** con capacidad de búsqueda web. Cada agente investiga un subtema distinto en simultáneo, rastreando fuentes primarias verificables. Los resultados se escriben en archivos `findings_N.md` dentro del directorio de investigación.
4. **Síntesis de hallazgos**: el editor lee y cruza todos los findings, identificando patrones, contradicciones y conexiones entre subtemas que los agentes no pudieron detectar por sí solos.
5. **Gap Report**: antes de escribir, se genera un reporte que lista **todos los números, fechas, montos y nombres propios** que el artículo va a usar — no solo los claims principales. Para cada uno se verifica: fuente verificable en los findings, dato textual y accesibilidad. Si más de 2 claims no tienen fuente accesible, el proceso se pausa. **Prohibido el cálculo mental:** todo número derivado (suma, resta, porcentaje) debe estar explícitamente en los findings o documentarse en el Gap Report antes de escribir.
6. **Redacción**: el editor escribe el artículo con estructura hook → contexto → 4 a 6 secciones H2 → conclusión → fuentes, usando los hallazgos como materia prima verificada. Se aplica la regla de cero datos de memoria: ningún número, fecha, nombre propio o monto se escribe sin fuente verificable en el gap report.
7. **Enlazado interno**: se insertan de 2 a 3 enlaces a otros artículos del sitio, anclados exclusivamente en hechos verificables presentes en los findings.
8. **Fact-check pre-publicación**: un agente independiente verifica cada afirmación con número, fecha, nombre o monto contra las fuentes. Si el fact-check encuentra errores, se corrigen y se re-ejecuta hasta que pase. Los fact-checkers también se verifican entre sí (doble fact-check obligatorio). Además, el agente **cruza los claims contra los artículos ya publicados en el sitio** que toquen el mismo tema, verificando que no haya contradicciones entre ellos.
9. **Validación automatizada**: el artículo pasa por `validate_publish.py`, un script de 12 controles que verifica: longitud del título, detección de clickbait, presencia de schema FAQ, enlace al cluster de IA en Paraguay, conteo de palabras, acentos, metadatos SEO y más.
10. **Generación de FAQ**: un script automático (`generate_faq.py`) analiza el contenido del artículo y genera 3 preguntas frecuentes con respuestas basadas en datos del texto. Si el artículo no incluye FAQ, un workflow de GitHub Actions lo detecta y lo genera automáticamente antes de la publicación.
11. **Actualización del observatorio**: antes del commit final, si el artículo aporta nuevos hitos, entidades, casos o términos, actualizar las páginas del observatorio que correspondan:
    - **`/cronologia/`**: agregar hitos nuevos (eventos, fechas, proyectos) mencionados en el artículo.
    - **`/regulacion/`**: agregar leyes, decretos o normas nuevas si el artículo cubre legislación.
    - **`/directorio/`**: agregar startups, comunidades, instituciones o personas clave si el artículo descubre nuevas entidades del ecosistema.
    - **`/casos-de-uso/`**: agregar sectores o aplicaciones nuevas de IA en Paraguay que el artículo documente.
    - **`/glosario/`**: agregar términos nuevos específicos del cluster de IA en Paraguay con enlace al artículo.
    - **`/ia-en-paraguay/`**: agregar el artículo a su pilar correspondiente y moverlo de "Próximamente" si estaba listado.
    - **`llms.txt`**: agregar el artículo al pilar correspondiente.
    Cada página actualizada incrementa su `last_modified_at`. No todas las páginas se actualizan en cada artículo — solo las que tengan contenido nuevo que aportar.

Además, aplicamos una **auditoría programada**: cada 5 artículos nuevos, re-auditamos los artículos más antiguos no auditados contra sus fuentes originales. Mantenemos un **registro de verificación** con la fecha del último chequeo de cada artículo — los números se actualizan con cada auditoría. Cada artículo nuevo se audita antes de publicarse; ningún artículo sale sin pasar por fact-check. Este proceso detectó y corrigió más de 40 errores en las auditorías de julio de 2026.

También aplicamos una **regla estricta de fuentes**: cada URL en la sección Fuentes debe apuntar al reporte, artículo o página específica que respalda el dato — no al dominio raíz de la fuente. Esto corrige una debilidad histórica del sitio donde varios artículos linkeaban homepages genéricas en vez de contenido verificable.

Este proceso reduce significativamente el riesgo de alucinaciones y busca que cada artículo de fondo esté respaldado por fuentes primarias verificables.

## Infraestructura y herramientas

Todo el desarrollo, mantenimiento y operación del sitio se gestiona mediante **OpenCode**, un entorno de desarrollo asistido por IA que permite coordinar agentes, ejecutar scripts y desplegar cambios.

Los modelos de lenguaje utilizados en las distintas etapas del proyecto son:

| Modelo | Uso principal |
|---|---|
| **DeepSeek** | Investigación con agentes, razonamiento analítico y redacción asistida de artículos de fondo |
| **MiniMax** | Procesamiento de contenido y tareas de síntesis |
| **Qwen** | Asistencia en desarrollo, mantenimiento del sitio y validación de código |
| **GPT-4o** | Generación automatizada de Editorial Diaria (vía GitHub Models) |
| **GPT-4o-mini** | Generación automatizada de Pulso Paraguay, FAQ auto-generator (vía GitHub Models) |

La combinación de múltiples modelos permite aprovechar las fortalezas de cada uno: razonamiento profundo para la investigación, eficiencia para el contenido automatizado diario, y capacidad de desarrollo para el mantenimiento técnico del sitio.

## Cómo verificamos los datos

- **Pulso Paraguay y Editorial Diaria**: toda afirmación fáctica proviene de las fuentes originales procesadas ese día. La IA no genera datos propios. Si una fuente se equivoca, podemos heredar ese error; por eso cada publicación incluye la lista completa de fuentes consultadas para que el lector pueda verificarlas por su cuenta.
- **Artículos de fondo**: cada afirmación estadística, económica o factual se respalda con enlaces a fuentes originales verificables (institutos públicos, papers académicos, documentos oficiales, informes sectoriales). Si un dato no puede ser verificado con una fuente primaria, se indica explícitamente. Cada URL en la sección Fuentes apunta a la página específica del dato, no al dominio raíz de la fuente.

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
