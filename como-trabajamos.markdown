---
layout: page
title: Cómo trabajamos
permalink: /como-trabajamos/
description: "Metodología editorial de muchotexto.net: cómo seleccionamos fuentes, verificamos datos, usamos inteligencia artificial y corregimos errores."
last_modified_at: 2026-09-03
---

**muchotexto.net** es el observatorio de inteligencia artificial en Paraguay. Utiliza inteligencia artificial como asistente en el proceso de producción de contenido. Esta página explica con transparencia cómo funciona ese proceso.

## Origen de la información

No producimos noticias de primera mano. Tomamos información ya publicada por medios paraguayos y la organizamos, sintetizamos e interpretamos.

Nuestro sistema recolecta diariamente el contenido de **6 fuentes de noticias** vía RSS: ABC Tecnología, ABC Ciencia, ABC Nacionales, La Nación, NPY y La Tribuna. El Pulso Tech Paraguay aplica un filtro temático estricto: solo procesa noticias relacionadas con inteligencia artificial, infraestructura digital, energía para data centers, regulación tecnológica, startups, ciencia aplicada y economía digital. Esta selección deliberada responde al posicionamiento del sitio como observatorio de IA en Paraguay: cada pieza de contenido —desde el artículo de fondo hasta la nota diaria— refuerza la misma señal temática.

La cobertura da prioridad a las noticias tech de Paraguay o con vínculo directo con el país; cuando hay menos de tres locales, se completa con noticias de IA, semiconductores, data centers y regulación digital globales relevantes para el sector. El mensaje "sin novedades" solo se usa en días sin ninguna noticia tech real, local o internacional; ante la duda, se genera el Pulso. Diario HOY fue retirado de las fuentes en agosto de 2026 porque su RSS permanecía estancado desde diciembre de 2023.

## Qué hace la inteligencia artificial

La IA asiste en tres tareas específicas:

- **Lectura y filtrado temático**: procesa cientos de titulares y notas para identificar exclusivamente los temas de IA, tecnología, infraestructura digital y energía que son relevantes para el observatorio. El contenido ajeno a estos ejes temáticos se descarta.
- **Síntesis estructurada**: organiza la información en categorías temáticas (infraestructura digital, energía y data centers, inteligencia artificial, regulación tech, innovación y startups, ciencia aplicada), estima la relevancia de cada tema y redacta resúmenes basados exclusivamente en el contenido de las fuentes.
- **Análisis editorial**: a partir del Pulso Tech, genera un artículo de opinión que busca patrones, conexiones y preguntas relevantes sobre la infraestructura digital y la inteligencia artificial en Paraguay.

Para el Pulso Tech Paraguay y la Editorial Diaria usamos **Gemini 3.1 Flash Lite** (Google Gemini API, tier gratuito). Para los artículos de fondo, usamos **DeepSeek** como modelo principal de investigación y redacción asistida. Cada modelo se asigna según la tarea: razonamiento profundo para la investigación, eficiencia para el contenido automatizado diario. Cada interacción con la IA está gobernada por un _system prompt_ que establece reglas estrictas: no inventar hechos ni nombres, filtrar exclusivamente contenido tech/IA/energía, usar español paraguayo profesional sin jerga coloquial y mantener una perspectiva analítica pero no partidista. La tabla completa de modelos está al final de esta página.

La IA **no decide** qué se publica ni cuál es la línea editorial. Su rol es exclusivamente instrumental: leer, resumir, organizar y redactar borradores.

## Qué la IA puede y qué no puede hacer

Como principio general, la IA actúa como asistente, nunca como autor final. Cada función de IA tiene un responsable humano que la supervisa y responde por el resultado:

| Función | Responsable | Directriz |
|---|---|---|
| Títulos y descripciones | Editor humano | La IA propone candidatos; la elección y edición final es humana |
| Borradores de artículos de fondo | Editor humano | Solo para borradores internos; la redacción final es humana |
| Pulso Tech Paraguay | Editor humano (revisión diaria) | Resúmenes basados exclusivamente en las fuentes del día; no genera datos propios |
| Editorial Diaria | Editor humano (revisión diaria) | Opinión derivada del Pulso; prohibido atribuir citas o ideas que no aparezcan en las fuentes |
| FAQ automática | Editor humano | Preguntas y respuestas derivadas del texto del artículo publicado |
| Investigación con agentes | Editor humano | Los hallazgos se sintetizan; nunca se copian textualmente sin verificación |
| Fact-check | Editor humano | Verificación en dos capas: datos factuales + claims de atribución (se abre el texto completo de la fuente para comprobar qué concluye realmente) |
| Capa de datos (MuchoTexto Data) | Editor humano | Los indicadores energéticos se sincronizan automáticamente desde la capa de datos verificables en cada build; el editor re-verifica el canon editorial cada 30 días |

**Usos prohibidos:**

- Generar contenido informativo que pueda confundirse con la realidad.
- Inventar hechos, cifras, fechas, nombres propios o citas.
- Atribuir declaraciones a personas que no las hicieron.
- Publicar cualquier contenido sin supervisión editorial humana.
- Usar la IA para rellenar un dato ausente: si un dato no se pudo verificar, no se inventa ni se aproxima.

## Cómo protegemos los datos en herramientas de IA

- **Solo herramientas autorizadas**: se utilizan únicamente los proveedores y modelos listados en la tabla de infraestructura de este documento. No se usan betas ni sistemas no autorizados para tareas editoriales.
- **Prohibido ingresar información confidencial** en herramientas de IA comerciales: datos personales de fuentes, borradores de contenidos inéditos o información sensible obtenida en investigación. Esta regla aplica incluso cuando la herramienta tenga licencia, salvo que el contrato con el proveedor garantice que los datos no se usarán para entrenar modelos.
- **Sin datos personales innecesarios**: los prompts de investigación se redactan sin incluir datos personales de terceros salvo que sea estrictamente necesario para la tarea.

## Riesgos y medidas de mitigación

| Riesgo | Medida |
|---|---|
| Alucinaciones y datos fabricados | Gap Report obligatorio, fact-check pre-commit en dos capas (datos + atribución), doble fact-check y cruce contra la base de claims verificados |
| Atribución incorrecta de conclusiones | El fact-check abre el texto completo de cada fuente citada para verificar que la conclusión atribuida es la que realmente tiene; las comparaciones del autor se marcan como propias |
| Sesgo algorítmico | System prompts con reglas de neutralidad y equilibrio PROS/CONTRAS; supervisión del editor; auditorías programadas |
| Fuga de información sensible | Solo herramientas autorizadas; prohibición de ingresar datos confidenciales en herramientas comerciales |
| Pérdida de calidad | Supervisión editorial humana obligatoria en toda publicación; revisión diaria del contenido automatizado |
| Deepfakes y alteración de la realidad | Línea roja: prohibido generar o publicar imágenes o vídeos que puedan confundirse con reales. Aplica si el sitio incorporase contenido multimedia en el futuro |
| Confianza del lector | Divulgación del uso de IA por formato, incluida la nota-pie en artículos de fondo (ver Declaración sobre uso de IA) |

## Qué hace el editor humano

El editor humano —César Sánchez— tiene a su cargo:

- **Definir la línea editorial** y los principios que gobiernan el _system prompt_ de la IA.
- **Seleccionar y mantener las fuentes**: qué medios se incluyen, cuáles se agregan o se retiran, y por qué.
- **Escribir y editar los artículos de fondo** (ensayos long-form de 1.500 a 2.500 palabras) con asistencia de agentes de IA para la fase de investigación (ver sección siguiente). El editor es el responsable intelectual y editorial del artículo. Las herramientas de IA se utilizan como asistentes de investigación y apoyo a la redacción, pero no sustituyen el juicio editorial humano.
- **Revisar diariamente** el contenido automatizado: cada publicación de Pulso Paraguay y Editorial Diaria es revisada por el editor humano el mismo día de su publicación. No se publica contenido automatizado sin supervisión editorial.
- **Corregir errores** cuando son detectados o reportados por lectores.

## Proceso de investigación con agentes de IA

Los artículos de fondo siguen un proceso estructurado de 12 pasos donde la IA actúa como asistente de investigación, no como autor:

1. **Selección del tema**: verificamos contra nuestro calendario editorial de 42 temas que el tópico no esté duplicado y tenga ángulo original.
2. **Plan de investigación**: creamos un directorio `research_[tema]/` con un `research_plan.md` que define la pregunta principal, 4 o 5 subtemas específicos y las fuentes esperadas (institutos públicos, papers académicos, documentos oficiales, informes sectoriales).
3. **Investigación paralela con agentes**: desplegamos de 4 a 5 agentes de IA independientes usando **OpenCode** con capacidad de búsqueda web. Cada agente investiga un subtema distinto en simultáneo, rastreando fuentes primarias verificables. Los resultados se escriben en archivos `findings_N.md` dentro del directorio de investigación.
4. **Síntesis de hallazgos**: el editor lee y cruza todos los findings, identificando patrones, contradicciones y conexiones entre subtemas que los agentes no pudieron detectar por sí solos.
5. **Gap Report**: antes de escribir, se genera un reporte que lista **todos los números, fechas, montos y nombres propios** que el artículo va a usar — no solo los claims principales — y, además, las **afirmaciones interpretativas o de atribución** ("X concluye/afirma/usa/cita Y"), para las que se comprueba que Y está realmente en la fuente de X. Para cada dato se verifica: fuente verificable en los findings, dato textual y accesibilidad. Si más de 2 claims no tienen fuente accesible, el proceso se pausa. **Prohibido el cálculo mental:** todo número derivado (suma, resta, porcentaje) debe estar explícitamente en los findings o documentarse en el Gap Report antes de escribir.
6. **Redacción**: el editor escribe el artículo con estructura hook → TL;DR → contexto → 4 a 6 secciones H2 → conclusión → fuentes, usando los hallazgos como materia prima verificada. Se aplica la regla de cero datos de memoria: ningún número, fecha, nombre propio o monto se escribe sin fuente verificable en el gap report. El TL;DR es un resumen ejecutivo de 3-4 viñetas justo después del hook, optimizado para extracción por ChatGPT, Perplexity y Google AI Overviews.
7. **Enlazado interno**: se insertan de 2 a 3 enlaces a otros artículos del sitio, anclados exclusivamente en hechos verificables presentes en los findings.
8. **Fact-check pre-publicación**: un agente independiente verifica cada afirmación en dos capas. Primero, los datos factuales —números, fechas, nombres y montos— contra las fuentes. Segundo, los claims interpretativos o de atribución: toda oración donde una fuente es el sujeto de un verbo de afirmación ("X concluye/afirma/usa/cita Y") exige abrir el texto completo de esa fuente y comprobar que la conclusión atribuida es la que realmente tiene. Un claim no se aprueba solo porque la fuente existe y el título coincide. Para cualquier dato sobre Paraguay, el agente debe consultar **fuentes primarias paraguayas** (Wikipedia en español, ANDE, BACN, MADES, ABC Color, La Nación, Itaipú Binacional) y no depender exclusivamente de Wikipedia en inglés o fuentes internacionales. Las fuentes primarias ya descargadas se pasan al agente por su ruta local para que las lea completas. Si el fact-check encuentra errores, se corrigen y se re-ejecuta hasta que pase. **El matiz opcional no existe:** toda observación del agente, aunque se etiquete como "matiz", "opcional" o "no FALSE", es una corrección que se aplica antes de publicar — un número impreciso o una lista incompleta son errores, no matices. Los fact-checkers también se verifican entre sí (doble fact-check obligatorio), y el editor abre personalmente 1 o 2 fuentes de alto riesgo antes de publicar. Además, el agente **cruza los claims contra los artículos ya publicados en el sitio** y contra la base de **claims verificados en AGENTS.md**.
9. **Verificación de proceso**: antes del commit, un agente independiente confirma que se completaron todos los pasos del flujo: carpeta research creada, findings existen, Gap Report existe y cada número del artículo tiene fila, fact-check ejecutado y errores corregidos. Si falta algún paso, el artículo no se publica.
10. **Validación automatizada**: el artículo pasa por `validate_publish.py`, un script de 12 controles que verifica: longitud del título, detección de clickbait, presencia de schema FAQ, enlace al cluster de IA en Paraguay, conteo de palabras, acentos, metadatos SEO y más.
11. **Generación de FAQ**: un script automático (`generate_faq.py`) analiza el contenido del artículo y genera 3 preguntas frecuentes con respuestas basadas en datos del texto. Si el artículo no incluye FAQ, un workflow de GitHub Actions lo detecta y lo genera automáticamente antes de la publicación.
12. **Actualización del observatorio y la estrategia**: antes del commit final, si el artículo aporta nuevos hitos, entidades, casos o términos, actualizar las páginas del observatorio que correspondan:
    - **`/cronologia/`**: agregar hitos nuevos (eventos, fechas, proyectos) mencionados en el artículo.
    - **`/regulacion/`**: agregar leyes, decretos o normas nuevas si el artículo cubre legislación.
    - **`/radar-legislativo/`**: actualizar el estado de las normas (vigente/proyecto/en-tramite/pendiente) en `_data/leyes.yml`.
    - **`/claims-verificados/`**: agregar los claims verificados o corregidos por el fact-check del artículo.
    - **`/directorio/`**: agregar startups, comunidades, instituciones o personas clave si el artículo descubre nuevas entidades del ecosistema.
    - **`/casos-de-uso/`**: agregar sectores o aplicaciones nuevas de IA en Paraguay que el artículo documente.
    - **`/glosario/`**: agregar términos nuevos específicos del cluster de IA en Paraguay con enlace al artículo.
    - **`/ia-en-paraguay/`**: agregar el artículo a su pilar correspondiente y moverlo de "Próximamente" si estaba listado.
    - **`llms.txt`**: agregar el artículo al pilar correspondiente.
    - **Documento de estrategia**: marcar el artículo como ✅ en §3.2, actualizar conteo de publicados/pendientes, mover de pendiente a completado en §15, agregar al progreso en §17.
    Cada página actualizada incrementa su `last_modified_at`. No todas las páginas se actualizan en cada artículo — solo las que tengan contenido nuevo que aportar.
    Las páginas de entidades (`/entidades/`) y el grafo (`/grafo/`) no se editan a mano: se regeneran con `python scripts/build_entities.py` tras publicar artículos nuevos. El dashboard (`/dashboard-energetico/`) se actualiza por cadencia de re-verificación de datos (cada 30 días), no por artículo.

Además, aplicamos una **auditoría programada**: cada 5 artículos nuevos, re-auditamos los artículos más antiguos no auditados contra sus fuentes originales. Mantenemos un **registro de verificación** con la fecha del último chequeo de cada artículo — los números se actualizan con cada auditoría. Cada artículo nuevo se audita antes de publicarse; ningún artículo sale sin pasar por fact-check. Este proceso detectó y corrigió más de 40 errores en las auditorías de julio de 2026.

También aplicamos una **regla estricta de fuentes**: cada URL en la sección Fuentes debe apuntar al reporte, artículo o página específica que respalda el dato — no al dominio raíz de la fuente. Esto corrige una debilidad histórica del sitio donde varios artículos linkeaban homepages genéricas en vez de contenido verificable.

Este proceso reduce significativamente el riesgo de alucinaciones y busca que cada artículo de fondo esté respaldado por fuentes primarias verificables.

## Infraestructura y herramientas

Todo el desarrollo, mantenimiento y operación del sitio se gestiona mediante **OpenCode**, un entorno de desarrollo asistido por IA que permite coordinar agentes, ejecutar scripts y desplegar cambios.

Los modelos de lenguaje utilizados en las distintas etapas del proyecto son:

| Modelo | Uso principal |
|---|---|
| **DeepSeek** | Investigación con agentes, razonamiento analítico y redacción asistida de artículos de fondo |
| **Gemini 3.1 Flash Lite** | Generación automatizada de Pulso Tech Paraguay y Editorial Diaria (vía Google Gemini API, tier gratuito) |
| **MiniMax** | Procesamiento de contenido y tareas de síntesis |
| **Qwen** | Asistencia en desarrollo, mantenimiento del sitio y validación de código |

La combinación de múltiples modelos permite aprovechar las fortalezas de cada uno: razonamiento profundo para la investigación, eficiencia para el contenido automatizado diario, y capacidad de desarrollo para el mantenimiento técnico del sitio.

### Capa de datos verificables

El sitio mantiene una capa de datos separada —**MuchoTexto Data** ([datospublicos.muchotexto.net](https://datospublicos.muchotexto.net/))— que estructura, normaliza y demuestra con evidencia oficial los números que el observatorio utiliza. Cada fuente (ANDE, Itaipú vía ONS, Yacyretá vía EBY) es un conector independiente que sigue el principio de no almacenar lo que no se necesita: se extraen únicamente los indicadores, metadatos y trazabilidad necesarios, conservando la referencia exacta a la fuente.

La integración con el sitio funciona así:

- **Sincronización en build**: un script (`scripts/sync_datos.py`) descarga los indicadores públicos de MuchoTexto Data y los combina en `_data/datos_publicos.json` antes de cada build de Jekyll.
- **Tolerancia a fallos**: si la descarga falla (red, parseo o estructura inválida), el sitio conserva el último snapshot sincronizado y publica igual. El build nunca se rompe por datos externos.
- **Refresco automático**: además de cada push, un cron semanal actualiza los datos aunque no haya actividad en el sitio.
- **Doble canon**: las series que son producto del conector (generación, suministro, pérdidas, clientes) se sincronizan automáticamente; los datos que dependen de criterio editorial (tarifa GCIE, timeline de decretos, proyección Ceare, distinciones de categoría) se mantienen curados y se re-verifican cada 30 días contra AGENTS.md.

## Cómo verificamos los datos

Nuestro método de verificación varía según el tipo de contenido:

- **Pulso Paraguay y Editorial Diaria**: toda afirmación fáctica proviene de las fuentes originales procesadas ese día. La IA no genera datos propios. Si una fuente se equivoca, podemos heredar ese error; por eso cada publicación incluye la lista completa de fuentes consultadas para que el lector pueda verificarlas por su cuenta.
- **Artículos de fondo**: cada afirmación estadística, económica o factual se respalda con enlaces a fuentes originales verificables (institutos públicos, papers académicos, documentos oficiales, informes sectoriales). Si un dato no puede ser verificado con una fuente primaria, se indica explícitamente. Cada URL en la sección Fuentes apunta a la página específica del dato, no al dominio raíz de la fuente.
- **Datos verificables (MuchoTexto Data)**: los números del sector energético que usa el sitio —generación, suministro, consumo, pérdidas, tarifas— tienen una capa dedicada de datos verificables en [datospublicos.muchotexto.net](https://datospublicos.muchotexto.net/). Cada indicador se extrae de la fuente oficial (ANDE, ONS Brasil, EBY), conserva su trazabilidad (fuente, método de extracción, fecha) y se sincroniza automáticamente con el sitio en cada build. El [dashboard energético](/dashboard-energetico/) y las páginas de entidad de ANDE, Itaipú y Yacyretá muestran esas series con su proveniencia. Si una serie del conector cambia en la fuente, el sitio la actualiza solo; los datos que dependen de criterio editorial (proyecciones, tarifas en revisión, distinciones de categoría) se re-verifican manualmente cada 30 días.

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

1. **Atribución**: toda información que procesamos tiene un origen identificable. No publicamos rumores ni filtraciones anónimas. No atribuimos a una fuente una conclusión que no es suya: si decimos "X concluye que Y", verificamos que Y está realmente en lo que X escribió. Las comparaciones y análisis del editor se presentan como propios, no como de las fuentes.
2. **Independencia**: no recibimos financiamiento de partidos políticos, gobiernos ni corporaciones para influir en nuestra línea editorial. El sitio se sostiene con publicidad no intrusiva.
3. **Transparencia metodológica**: explicamos cómo producimos cada tipo de contenido y qué rol juega la IA en cada caso.
4. **Corrección sobre orgullo**: si nos equivocamos, lo corregimos y lo decimos. La credibilidad se construye admitiendo errores.
5. **Sin sensacionalismo**: no publicamos contenido diseñado exclusivamente para generar clics, indignación o miedo. Buscamos análisis, no viralidad.

## Declaración sobre uso de IA

Todo contenido generado con asistencia de IA se identifica como tal. En cada publicación de Pulso Paraguay y Editorial Diaria se indica explícitamente que fue generada por inteligencia artificial, se nombra el modelo utilizado y se explica el proceso.

En los **artículos de fondo**, cuando la IA haya intervenido de forma significativa en la investigación o la redacción, el artículo incluye al pie (a modo de pie de texto, sin interrumpir la lectura) la fórmula:

> "Artículo elaborado con la asistencia de inteligencia artificial y supervisado por el editor humano de muchotexto.net."

Si el uso de la IA incidió en el contenido factual (datos, cifras, fechas), además del pie de texto se indica de forma clara qué parte del proceso fue asistido. No se requiere la fórmula cuando el uso de IA fue de mera asistencia técnica que no afectó el contenido factual (corrección ortográfica, transcripción automatizada de audios, búsqueda de datos en bases propias).

Consideramos que el uso de IA en la producción de contenido es legítimo siempre que:
- Sea transparente para el lector.
- No sustituya el criterio editorial humano.
- No invente hechos ni atribuya declaraciones falsas.
- Se base en fuentes verificables y atribuibles.

## Conflictos de interés

El editor de muchotexto.net, César Sánchez, trabaja como consultor independiente en proyectos de automatización con IA generativa, anotación de datos y desarrollo de soluciones basadas en IA. Esta actividad profesional es previa a la creación del sitio y es independiente de su línea editorial.

Si en el futuro existiera un conflicto de interés potencial entre un tema tratado y la actividad profesional del editor, se declarará explícitamente en el artículo correspondiente.

## Gobernanza de la política de IA

Esta política se revisa y actualiza de forma periódica, al menos cada 90 días o cada vez que se incorpore un modelo o herramienta nueva a los flujos de producción. La revisión evalúa:

- Si los modelos y herramientas listados siguen siendo los adecuados para cada tarea.
- Si las reglas de la presente política se cumplieron en las publicaciones del período.
- Si la política necesita actualizarse frente a nuevas capacidades de la IA o cambios en la normativa aplicable.

El editor humano es el responsable de esta revisión y de publicar las actualizaciones en esta página y en AGENTS.md.
