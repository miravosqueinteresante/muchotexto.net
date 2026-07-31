# Estrategia SEO Unificada — muchotexto.net

> **Documento definitivo del proyecto.** Cubre estrategia de contenidos, SEO técnico, automatización, control de calidad, procedimientos operativos y seguimiento.
> Última actualización: 31 de julio de 2026 (sincronización post-auditoría).

---

## Tabla de Contenidos

1. [Producto y visión](#1-producto-y-visión)
   1.1 [Qué es Muchotexto](#11-qué-es-muchotexto)
   1.2 [Visión y posicionamiento](#12-visión-y-posicionamiento)
2. [Diagnóstico actual](#2-diagnóstico-actual)
   2.1 [Estado del sitio](#21-estado-del-sitio-julio-2026)
   2.2 [Hallazgos del análisis](#22-hallazgos-del-análisis-de-junio-2026)
   2.3 [Resultados medidos](#23-resultados-medidos--actualizado-20-jul-2026)
   2.4 [Rendimiento técnico](#24-rendimiento-técnico-core-web-vitals)
3. [Arquitectura de contenido](#3-arquitectura-de-contenido)
4. [Estrategia de keywords](#4-estrategia-de-keywords)
5. [Metodología editorial](#5-metodología-editorial)
6. [Control de calidad editorial](#6-control-de-calidad-editorial)
7. [SEO técnico](#7-seo-técnico)
8. [AI Search Optimization](#8-ai-search-optimization)
9. [E-E-A-T y autoridad](#9-e-e-a-t-y-autoridad)
10. [Distribución y link building](#10-distribución-y-link-building)
11. [Observatorio: páginas vivas](#11-observatorio-páginas-vivas)
12. [Automatización — Pulso + Editorial](#12-automatización--pulso--editorial)
    12.1 [Pulso Paraguay](#121-pulso-paraguay-cron-0800-pyt--1200-utc)
    12.2 [Editorial Diaria](#122-editorial-diaria-cron-1800-pyt--2200-utc)
    12.3 [System prompt](#123-system-prompt--reglas-clave)
    12.4 [Validación de contenido](#124-validación-de-contenido-validate_content)
    12.5 [Auto-linking](#125-auto-linking-add_internal_links)
    12.6 [Hardening de infraestructura](#126-hardening-de-infraestructura)
    12.7 [Observatorio Intel](#127-observatorio-intel--dashboard-editorial)
    12.8 [Entidades](#128-entidades--infraestructura-de-conocimiento)
    12.9 [Pendientes conocidos](#129-pendientes-conocidos-no-críticos)
13. [Stack técnico y herramientas](#13-stack-técnico-y-herramientas)
14. [Procedimientos operativos](#14-procedimientos-operativos)
15. [Plan de acción pendiente](#15-plan-de-acción-pendiente)
16. [Registro de verificación de datos](#16-registro-de-verificación-de-datos)
17. [Progreso completado](#17-progreso-completado)
18. [Apéndices](#18-apéndices)
19. [Registro de cambios](#19-registro-de-cambios)

---

## 1. Producto y visión

### 1.1 Qué es Muchotexto

**muchotexto.net es el observatorio de inteligencia artificial en Paraguay.** Un medio digital que publica análisis en profundidad sobre cómo la inteligencia artificial está transformando el país — su energía, su economía, su regulación, su fuerza laboral y su lugar en el tablero geopolítico.

**Qué publica:**

| Formato | Qué es | Frecuencia | Generación |
|---|---|---|---|
| **Artículos long-form** | Análisis de 1.500-2.500 palabras con metodología PROS/CONTRAS, 7 dimensiones de análisis, fuentes verificadas y FAQ schema | 1-2 por semana | Manual, con investigación multi-agente |
| **Pulso Paraguay** | Reporte diario de las 10 noticias más relevantes del país, con puntuación de temperatura | Lun-Sáb 08:00 | Automático (gpt-4o-mini, 15 feeds RSS) |
| **Editorial** | Opinión diaria basada en el Pulso, con análisis de una noticia en profundidad, voseo paraguayo, auto-linking a artículos relacionados | Lun-Sáb 18:00 | Automático (gpt-4o, temperature 0.3) |
| **Observatorio** | Páginas vivas: cronología de hitos, directorio de startups, mapa regulatorio, glosario, casos de uso por sector | Actualización continua | Manual |

**Para quién es:**
- Profesionales y tomadores de decisión en Paraguay que necesitan entender el impacto de la IA
- Periodistas y analistas que cubren tecnología en Latinoamérica
- Inversores y empresas evaluando el ecosistema tech paraguayo
- Ciudadanos paraguayos que quieren información verificada sobre el futuro digital de su país

**Qué NO es:**
- No es un blog de tutoriales de IA ni prompts
- No es un medio de noticias de último momento
- No es un agregador de contenido ajeno
- No escribe para SEO primero — escribe para humanos, con SEO como consecuencia

### 1.2 Visión y posicionamiento

Posicionar **muchotexto.net** como el referente en español sobre inteligencia artificial en Paraguay. El espacio está vacío: nadie en el mundo hispanohablante escribe análisis profundos de IA desde Paraguay.

| Competidor | Qué hace | Qué NO hace |
|---|---|---|
| ABC Color, Última Hora, La Nación | Cubren la noticia del día | Análisis de 2.000 palabras con fuentes verificadas |
| Wired, MIT Tech Review, Rest of World | Cubren IA global | No cubren Paraguay con profundidad |
| Blogs de IA en español | Tutoriales de prompts y herramientas | No hablan de política energética paraguaya ni geopolítica de chips |

**Ventaja competitiva:** único sitio que cruza `IA + Paraguay + datos duros + fuentes verificables + 1.500+ palabras por artículo`.

**Diferenciador clave (information gain):** experiencia real de César en anotación de datos, bots con IA, consultoría SEO, y análisis de la reforma energética paraguaya. Esto es *non-commodity content* — nadie más puede replicarlo.

> **Nota operativa:** El autor no tiene experiencia en programación. La IA (OpenCode) debe guiar paso a paso cada procedimiento técnico, explicando cada acción de forma clara y sencilla antes de ejecutarla.

---

## 2. Diagnóstico actual

### 2.1 Estado del sitio (julio 2026)

| Métrica | Valor |
|---|---|
| Artículos long-form publicados | 38 (35 en el observatorio) |
| Editoriales | 44 |
| Pulso Paraguay | 66 |
| **Total posts** | **148** |
| SEO Score (squirrelscan) | 75/100 (C) |

### 2.2 Hallazgos del análisis de junio 2026

| Hallazgo | Implicancia SEO |
|---|---|
| 75% de los artículos long form tocan IA/tecnología | Pilar de contenido más fuerte — construir sobre esto |
| Paraguay es "protagonista" en 50% de esos artículos | Ángulo diferencial: cobertura local especializada |
| 25 tags únicos usados en solo 4 artículos | Taxonomía fragmentada — sin topic cluster claro |
| Editoriales mencionan IA en solo 20% de los casos | Oportunidad de subir esa proporción |
| Fuentes más citadas: ABC Color, La Nación, HOY, NPY | Estos medios son objetivo de backlink/mención |
| Sentimiento long form: mixto con sesgo positivo (+0.20) | El contenido de IA puede ser el ángulo constructivo del sitio |

**Métricas registradas — 20-jul-2026:***

| Métrica | Valor | Herramienta |
|---|---|---|
| Clics totales (28 días) | **8** | GSC |
| Impresiones totales (28 días) | **160** | GSC |
| CTR medio | **5%** | GSC |
| Posición media | **5.0** | GSC |
| Core Web Vitals (LCP/TBT/CLS) | 3.3s / 150ms / 0 (ver §6) | PageSpeed Insights |
| Tráfico orgánico a `/ia-en-paraguay/` | Sin datos | GA4 (pendiente configurar) |
| Backlinks desde medios paraguayos | Sin detectar | GSC |
| Menciones en ChatGPT/Perplexity/Claude | Sin verificar | — |

**Consultas principales (28 días):**

| Consulta | Clics | Impresiones | Posición media |
|---|---|---|---|
| `muchotexto` | 0 | 34 | 4.3 |
| `quién es el autor?` | 0 | 1 | 3 |
| `peter thiel paraguay` | 0 | 1 | 5 |
| `dime todo lo que sepas de el` | 0 | 1 | 5 |
| `bid paraguay` | 0 | 1 | 6 |

**Análisis:** el sitio tiene presencia en Google pero es mínima — 160 impresiones en 28 días, casi todas de marca (`muchotexto`). No hay tráfico orgánico real. Las consultas con intención informacional (`peter thiel paraguay`, `bid paraguay`) tienen 1 impresión cada una. Esto es normal para un sitio de 2 meses sin backlinks. El próximo trimestre dirá si la estrategia de contenidos empieza a generar tráfico orgánico.

**Plan:** mantener publicación semanal. Re-medir en 3 meses (oct 2026). Si no hay mejora significativa, revisar estrategia de keywords y distribución.

### 2.4 Rendimiento técnico (Core Web Vitals)

| Métrica | Valor | Meta | Estado |
|---|---|---|---|
| LCP | 3.3s | <2.5s | ⚠️ Mejorable |
| TBT | 150ms | <200ms | ✅ Bueno |
| CLS | 0 | <0.1 | ✅ Perfecto |
| FCP | 0.9s | <1.8s | ✅ Excelente |
| Speed Index | 2.2s | <3.4s | ✅ Bueno |

**Scores Lighthouse (Mobile, 20-jul-2026):** Performance 91, Accesibilidad 96, Prácticas recomendadas 96, SEO 100.
**Issues conocidos:** LCP elevado por CSS síncrono (trade-off aceptado por CLS 0). GA4 no removible. Contraste corregido (opacity .7).

---

## 3. Arquitectura de contenido

### 3.1 Modelo: Pillar Page + Topic Clusters

```
Página Pilar: "Observatorio de IA en Paraguay — Guía Completa 2026"
  ├── Pilar 1: Infraestructura y energía (8 temas)
  ├── Pilar 2: Geopolítica y regulación tech (8 temas)
  ├── Pilar 3: IA, sociedad y trabajo (10 temas)
  ├── Pilar 4: Tecnología aplicada + ecosistema (10 temas)
  └── Pilar 5: Cultura, filosofía y futuro (6 temas)
```

**Regla de interlinking:** todos los artículos enlazan hacia la página pilar, la página pilar enlaza hacia cada uno. Cada Pulso Paraguay diario que toque IA debe enlazar de vuelta al cluster.

### 3.2 Los 5 pilares y sus 42 temas

**Leyenda:** ✅ Publicado | ⬜ Pendiente | ⭐ Nuevo (junio-julio 2026)

#### Pilar 1: Infraestructura y energía (8 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 1 | ✅ | Yguazú Digital y la apuesta de Paraguay por convertirse en hub de IA | `Yguazú Digital Paraguay Taiwán`, `centro IA Paraguay` |
| 2 | ✅ | Luces y sombras de la apertura eléctrica: Paraguay y el sector privado | `apertura eléctrica Paraguay`, `Ley 7599`, `ANDE energía` |
| 3 | ✅ | Criptominería en Paraguay: el costo real de la energía barata | `criptominería Paraguay ANDE`, `bitcoin Paraguay energía` |
| 4 | ✅ | Itaipú 2027: ¿qué pasa con la energía paraguaya cuando se renegocie el tratado? | `Itaipú renegociación 2027`, `energía Paraguay futuro` |
| 5 | ✅ | Hidrógeno verde: ¿la próxima frontera energética de Paraguay? | `hidrógeno verde Paraguay`, `transición energética` |
| 6 | ✅ | La red eléctrica de Paraguay frente a la demanda de la IA global | `ANDE capacidad transmisión`, `red eléctrica Paraguay IA` |
| 7 | ⬜ | Energía renovable y cambio climático: la paradoja paraguaya | `Paraguay energía renovable`, `cambio climático hidroeléctrica` |
| 8 | ⭐ | El efecto derrame: ¿qué pasa en una ciudad paraguaya cuando llega un data center de $200M? | `data center impacto local Paraguay`, `empleo tecnología Paraguay` |

#### Pilar 2: Geopolítica y regulación tech (8 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 9 | ✅ | El experimento paraguayo de Peter Thiel | `Peter Thiel Paraguay Palantir`, `vigilancia IA` |
| 10 | ✅ | Paraguay entre China y Taiwán: el último aliado sudamericano en la guerra fría tecnológica | `Paraguay China Taiwán`, `geopolítica chips` |
| 11 | ✅ | IA soberana: ¿qué significa y por qué Paraguay la necesita? | `IA soberana Paraguay`, `soberanía digital` |
| 12 | ✅ | Ley de protección de datos en Paraguay: ¿llega a tiempo para la era de la IA? | `ley protección datos Paraguay`, `privacidad digital` |
| 13 | ✅ | Ciberseguridad en Paraguay: ¿estamos preparados para un data center de $40B? | `ciberseguridad Paraguay`, `CERT-PY`, `data center seguridad` |
| 14 | ✅ | Semiconductores: por qué Taiwán eligió Paraguay | `semiconductores Taiwán Paraguay`, `TSMC`, `cadena chips` |
| 15 | ⬜ | El modelo Itaipú aplicado a la IA: ¿puede funcionar dos veces? | `entidad binacional Paraguay Taiwán`, `gobernanza IA` |
| 16 | ⬜ | Silicon Valley en el Cono Sur: ¿por qué los billonarios miran a Paraguay? | `inversión tech Paraguay`, `Crusoe AI`, `X8Cloud` |

#### Pilar 3: IA, sociedad y trabajo (10 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 17 | ✅ | Anotación de datos para IA: la ventaja silenciosa de Paraguay | `anotación datos IA Paraguay`, `trabajo digital Paraguay` |
| 18 | ✅ | Educación tech en Paraguay: la brecha que frena el hub de IA | `educación tecnología Paraguay`, `ingenieros Paraguay IA` |
| 19 | ✅ | Bienvenidos a muchotexto.net | `muchotexto.net` |
| 20 | ✅ | El futuro de la identidad y la conciencia | `identidad digital`, `filosofía tecnología` |
| 21 | ✅ | Talento tech: ¿cuántos ingenieros necesita Paraguay para ser un hub de IA? | `talento tech Paraguay`, `fuga de cerebros` |
| 22 | ✅ | Starlink en Paraguay: ¿conectividad para todos o espejismo digital? | `Starlink Paraguay`, `conectividad rural` |
| 23 | ✅ | Gobierno digital: ¿qué hizo Paraguay y qué falta? | `gobierno digital Paraguay`, `MITIC`, `Agenda Digital` |
| 24 | ✅ | IA y salud en Paraguay: del IPS a los algoritmos de diagnóstico | `IA salud Paraguay`, `IPS tecnología médica` |
| 25 | ✅ | ¿Puede la IA reducir la corrupción en Paraguay? | `IA corrupción`, `transparencia algorítmica Paraguay` |
| 26 | ✅ | De la soja al silicio: el plan de Paraguay para cambiar su matriz exportadora | `matriz exportadora Paraguay`, `diversificación económica IA` |

#### Pilar 4: Tecnología aplicada + ecosistema (10 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 27 | ✅ | Soja, ganado y blockchain: la apuesta paraguaya por la tokenización del agro | `tokenización agro Paraguay`, `blockchain Paraguay` |
| 28 | ✅ | Agro 4.0: cómo la IA está transformando el campo paraguayo | `agro IA Paraguay`, `agricultura precisión`, `drones` |
| 29 | ✅ | Fintech en Paraguay: ¿el próximo hub financiero de LatAm? | `fintech Paraguay`, `pagarés digitales`, `inclusión financiera` |
| 30 | ✅ | La IA no es neutral: lo que dice la primera encíclica del Papa León XIV | `encíclica IA Papa León XIV`, `ética inteligencia artificial` |
| 31 | ✅ | IA y periodismo en Paraguay: ¿quién escribe las noticias del futuro? | `IA periodismo Paraguay`, `deepfakes`, `verificación` |
| 32 | ✅ | Smart cities en Paraguay: ¿Asunción puede ser una ciudad inteligente? | `smart city Asunción`, `ciudad inteligente Paraguay` |
| 33 | ✅ | IA en la justicia paraguaya: ¿algoritmos imparciales o sesgo digital? | `IA justicia Paraguay`, `expediente electrónico` |
| 34 | ✅ | E-commerce y logística: la transformación silenciosa del comercio paraguayo | `ecommerce Paraguay`, `logística IA` |
| 35 | ✅ | Startups paraguayas de IA: quiénes son y por qué nadie habla de ellas | `startups IA Paraguay`, `ecosistema emprendedor tech` |
| 36 | ✅ | La cadena de valor invisible: todos los negocios que rodean a un centro de datos | `cadena valor data center`, `negocios IA Paraguay` |

#### Pilar 5: Cultura, filosofía y futuro (6 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 37 | ✅ | 5 tecnologías que prometieron cambiar todo pero no cambiaron nada | `tecnologías fracasadas`, `hype tecnológico` |
| 38 | ✅ | ¿Qué es realmente el fútbol? | `fútbol filosofía`, `identidad fútbol` |
| 39 | ✅ | La IA cuesta más que los humanos que reemplazó: lo que dicen los números | `burbuja IA 2026`, `costos inteligencia artificial` |
| 40 | ✅ | El laboratorio americano: cómo Estados Unidos está usando IA para reinventar su fútbol | `USA fútbol IA Mundial 2026`, `Sportian Globant` |
| 41 | ✅ | Guaraní e IA: ¿puede una lengua indígena sobrevivir en la era de los algoritmos? | `guaraní inteligencia artificial`, `NLP lenguas indígenas` |
| 42 | ⬜ | Paraguay 2040: un país construido con datos | `Paraguay futuro tecnología`, `prospectiva digital` |

**Total: 42 temas. 38 publicados (✅). 4 pendientes (2 ⬜ + 2 ⭐).**

> **Desglose real del observatorio:** de los 42 temas, 38 están publicados. De esos 38, 35 son análisis de IA que integran el observatorio + 1 artículo extra ("Qué es un data center", explicador de referencia) = **36 en el observatorio**. Los otros 2 publicados (#19 Bienvenidos y #38 Fútbol) no son análisis de IA y están excluidos del observatorio. Total real en `_posts/` con `categories: articulos`: 38.

---

## 4. Estrategia de keywords

### Keyword principal (head term — aspiracional, largo plazo)

| Keyword | Volumen | Competencia |
|---|---|---|
| `inteligencia artificial Paraguay` | Medio | Baja |

### Keywords cuerpo (body terms — mediano plazo)

| Keyword | Por qué |
|---|---|
| `Paraguay inteligencia artificial` | Variante natural para usuarios paraguayos |
| `centro de datos IA Paraguay` | Yguazú Digital, X8Cloud |
| `IA en Paraguay` | Búsqueda genérica de quien quiere saber qué está pasando |
| `inteligencia artificial Latinoamérica` | Alcance regional sin perder relevancia |
| `análisis inteligencia artificial` | Refleja el formato del sitio (long-form, profundo) |

### Long-tail (ranking inmediato o a un paso)

| # | Keyword | Artículo asociado | Estado |
|---|---|---|---|
| 1 | `Yguazú Digital Paraguay Taiwán` | #1 | ✅ |
| 2 | `tokenización agro Paraguay blockchain` | #27 | ✅ |
| 3 | `Peter Thiel Paraguay Palantir` | #9 | ✅ |
| 4 | `encíclica Magnifica Humanitas IA Papa León XIV` | #30 | ✅ |
| 5 | `burbuja inteligencia artificial 2026 costos` | #39 | ✅ |
| 6 | `USA fútbol inteligencia artificial Mundial 2026` | #40 | ✅ |
| 7 | `Paraguay energía IA data center` | #1, #2 | ✅ |
| 8 | `criptominería Paraguay ANDE energía` | #3 | ✅ |
| 9 | `Paraguay Taiwán China geopolitica IA` | #10 | ✅ |
| 10 | `Santiago Peña inteligencia artificial Taiwán` | #1 | ✅ |
| 11 | `Globant Sportian IA fútbol Pochettino` | #40 | ✅ |
| 12 | `ley protección datos Paraguay` | #12 | ✅ |

---

## 5. Metodología editorial

### 5.1 Formato estándar

```
1. Hook (sin encabezado, 2-3 oraciones)
   → Afirmación fuerte, pregunta provocadora o dato impactante.
   → PROHIBIDO empezar con fechas o "Hoy...".

2. TL;DR — Resumen ejecutivo (bloque destacado, justo después del hook)
   → 3-4 viñetas con los datos más importantes del artículo.
   → Formato: `> **En resumen:**` seguido de bullets con `>`.
   → Optimizado para extracción por ChatGPT, Perplexity y Google AI Overviews.
   → Debe ser auto-contenido: alguien que lea solo el TL;DR entiende de qué trata el artículo.
   → Se actualiza si el artículo recibe correcciones post-publicación.

3. Contexto (sin encabezado, 1-2 párrafos)
   → Por qué importa este tema ahora. Conexión con Paraguay.

3. Cuerpo (4-6 secciones con ##)
   → Cada H2 debe contener una keyword secundaria o variación.
   → PROHIBIDOS subtítulos genéricos como "Contexto" o "Análisis".
   → Cada sección: 3-5 párrafos con datos duros y fuentes.

4. Conclusión (últimos 2-3 párrafos)
   → Cierre firme, sin preguntas retóricas vacías.
   → Conectar con el panorama general.

5. Fuentes (lista numerada o viñetas)
   → Mínimo 5 URLs externas.
   → Formato: [Medio — "Título del artículo"](URL) (fecha)
```

### 5.2 Frontmatter template

```yaml
---
layout: post
title: "Título con keyword primaria al inicio — máximo 70 caracteres"
date: YYYY-MM-DD
last_modified_at: YYYY-MM-DD
categories: articulos
tags: [keyword1] [keyword2] [keyword3] [paraguay] [ia] [etc]
description: "Keyword primaria + promesa de valor. 150-155 caracteres."
---
```

### 5.3 Reglas para títulos

| Regla | Detalle |
|---|---|
| Keyword primaria al inicio | Primera mitad del título, idealmente primeras 3-4 palabras |
| Máximo 70 caracteres | Sin excepciones |
| Sin signos de exclamación | Ni admiración, ni excesos tipográficos |
| Construcción sintáctica única por artículo | Si uno usó `¿puede Paraguay [X]?`, ningún otro puede usar la misma estructura. Si ya hay un `cuando Paraguay [X]`, no repetir `cuando`. Variar conectores. |
| Preferir afirmación sobre pregunta | Una afirmación fuerte tiene más peso que una pregunta retórica. La pregunta se reserva para títulos donde la incertidumbre es genuina. |
| **Ortografía española correcta** | Título y description deben usar acentos (tildes), eñes y demás caracteres del español correctamente: á, é, í, ó, ú, ñ, ü. NO escribir "mas" por "más" ni "esta" por "está". |
| **Prohibido abusar de la fórmula `[Tema]: [Subtítulo]`** | Máximo 1 de cada 5 artículos puede usar esta estructura. Alternativas: empezar con verbo (`Paraguay aprobó...`), con conector causal (`Por qué Paraguay...`), con preposición (`Sin red de 500 kV no hay IA...`), o con sujeto + predicado sin dos puntos. |
| **Ortografía española en TODO el proyecto** | Cada texto en español debe usar acentos, eñes y caracteres del español correctamente. Esto incluye: títulos, descriptions, página pilar, llms.txt, about, footer. El validador marca como WARNING cualquier texto 100% ASCII. |
| **Auditar títulos antes de publicar** | Contar cuántos artículos consecutivos usan la misma estructura sintáctica. Si hay 2+ seguidos con `[X]: [Y]`, cambiar el nuevo. |

### 5.4 Metodología PROS y CONTRAS

**Cada artículo debe presentar argumentos a favor y en contra.** No como secciones fijas, sino como principio metodológico integrado en la narrativa.

**Dimensiones a cubrir:**

| Dimensión | Preguntas guía |
|---|---|
| Económica | ¿Es viable financieramente? ¿Quién paga? |
| Técnica | ¿Funciona? ¿Qué infraestructura requiere? |
| Social | ¿A quién beneficia? ¿A quién perjudica? |
| Cultural | ¿Qué dice de nosotros como país? |
| Geopolítica | ¿Quién gana poder? ¿Qué riesgo implica? |
| Ambiental | ¿Qué impacto tiene en recursos naturales? |
| Filosófica | ¿Qué significa para la idea de progreso? |

**Reglas del balance:**
1. Nunca un artículo es 100% a favor ni 100% en contra
2. Los CONTRAS no son un párrafo al final — deben aparecer intercalados
3. No usar las palabras "PROS" ni "CONTRAS" como encabezados
4. Si no encontrás contras sólidos, el artículo no está listo. Volvé a investigar
5. Citar fuentes para ambos lados

### 5.5 Checklist SEO por artículo

**Antes de escribir:**
- [ ] Definir keyword primaria + 3 secundarias + 5 long-tail
- [ ] Identificar 2-3 artículos del sitio para enlazar (mismo pilar)
- [ ] **Leer los artículos ya publicados del mismo pilar**: verificar que el nuevo artículo no repita datos, fuentes o conclusiones que ya existen. Complementar, no duplicar.
- [ ] **Leer https://muchotexto.net/ia-en-paraguay/ antes de escribir**: revisar los 5 pilares, los artículos ya publicados y los Próximamente listados. El nuevo artículo debe complementar el ecosistema, no repetir temas ni pisar Próximamente vacíos. Cada artículo nuevo refuerza la página pilar como centro del cluster.

**Durante la escritura:**

| Elemento | Regla SEO |
|---|---|
| Título | Keyword primaria al inicio. 50-70 chars. Sin signos de exclamación |
| Meta description | 150-155 chars. Incluye keyword primaria + promesa de valor |
| Primer párrafo | Keyword primaria en las primeras 2 oraciones |
| H2s | 4-6 subtítulos. Cada uno con keyword secundaria o variación |
| Cuerpo | Keyword primaria 3+ veces, distribuida |
| Anchor text | Descriptivo, no "clic aquí". Usar keywords naturales |
| Slug | En español, sin stopwords, con keyword primaria, guiones |

**Después de escribir:**
- [ ] Keyword primaria en título, H2, primer párrafo y meta description
- [ ] 3+ keywords secundarias en H2s
- [ ] 2-3 enlaces internos con hechos verificables (ver regla de oro en 5.6)
- [ ] 5+ enlaces externos a fuentes de autoridad (nivel A, B o C)
- [ ] Slug optimizado (keyword, sin stopwords, guiones)
- [ ] Meta description 150-155 chars con keyword + gancho
- [ ] Word count: 1.500 - 2.500
- [ ] Build de Jekyll sin errores
- [ ] Schema Article válido
- [ ] Tags alineados con otros artículos del mismo pilar
- [ ] Enlace a la página pilar `/ia-en-paraguay/` con anchor text variado y descriptivo (no repetir texto ancla entre artículos)
- [ ] **Ortografía**: título y description con acentos correctos (á, é, í, ó, ú, ñ). NO escribir mas por más, esta por está, analisis por análisis, año por año.

### 5.6 Regla de oro para enlaces internos

**Cada enlace interno se inserta con un hecho verificable, no con una inferencia.**

| Correcto | Incorrecto |
|---|---|
| "X8Cloud anunció 250M para un data center. [Yguazú Digital](...), el proyecto con Taiwán, es el más ambicioso." | "El crecimiento de servicios digitales fue impulsado por [la anotación de datos](...), que empieza a tomar forma." |

**Procedimiento:**
1. Leer el artículo linkeado. Confirmar qué afirma y qué no
2. El texto ancla debe describir un hecho que existe en los findings de ese artículo
3. Si el artículo linkeado dice que algo "podría" pasar, el texto ancla dice "podría"
4. Si no hay manera de insertar el enlace sin inventar un hecho, **no se inserta**

### 5.7 Fuentes y verificación de datos

**Pirámide de calidad:**

| Nivel | Tipo | Ejemplos | Mínimo por artículo |
|---|---|---|---|
| A | Fuente oficial / primaria | MITIC, ANDE, decretos, leyes, Wikipedia (datos duros) | 1-2 |
| B | Periodismo serio con fuentes | ABC Color, La Nación, Reuters, Bloomberg | 2-3 |
| C | Análisis de expertos / papers | Frontiers, ILIA, bne Intellinews | 1-2 |
| D | Prensa internacional / nicho | Wired, MIT Tech Review, Rest of World | 1-2 |
| E | Prensa local complementaria | Hoy, Ultima Hora, Asunción Times | 0-2 |

**80% de las fuentes deben ser nivel A, B o C.**

**Lo prohibido:**
- Citar "expertos" sin nombre ni medio
- Redondear cifras sin aclarar contexto
- "Según la prensa internacional" sin especificar cuál
- Atribuir citas inventadas
- Confundir anuncio con hecho consumado ("Paraguay construirá X" vs "El gobierno anunció X")
- Inventar un puente narrativo para justificar un enlace interno

### 5.8 Proceso de investigación (obligatorio antes de escribir)

1. Crear carpeta `research_[tema]/` con `research_plan.md`
2. Desplegar 4-5 subagentes con `web-research`, cada uno investiga un subtema
3. Cada subagente guarda hallazgos en `research_[tema]/findings_*.md`
4. Leer todos los findings y sintetizar antes de escribir una sola palabra

---

## 6. Control de calidad editorial

### 6.1 Las 5 reglas críticas (implementadas 16 julio 2026)

**Regla 1: Cero datos de memoria.**
Ningún número, fecha, nombre propio o monto se escribe sin fuente verificable en el gap report.
Si un dato no tiene fuente accesible en el gap report, NO se incluye en el artículo.

**Regla 2: Doble fact-check obligatorio.**
Si un agente de fact-check afirma que algo "no existe" o "es falso", verificar con
un segundo agente independiente o fuente primaria. Nunca marcar como error con un solo check.

**Regla 3: Verificación de URLs.**
Antes de citar una fuente, `check_urls.py` verifica que la URL responde.
URLs con 404, 403 o redirect se marcan como NO VERIFICABLES.

**Regla 4: Gap Report obligatorio.**
Cada artículo requiere gap report ANTES de escribir.
Template en `docs/gap_report_template.md`.
Si más de 2 claims no tienen fuente: PAUSAR.

**Regla 5: Auditoría programada.**
Cada 5 artículos nuevos, re-auditar los 5 más antiguos no auditados.

### 6.2 Procedimiento mejorado de investigación (Compuertas A/B)

Implementado post-Artículo #23 (Gobierno digital), donde fuentes .gov.py inaccesibles por JS llevaron a datos incorrectos.

**Compuerta A — Gap Report (post-investigación, pre-escritura):**

Al recibir los findings de los agentes, antes de escribir, generar un gap report explícito:

1. Listar los 5-8 claims más importantes que el artículo necesita respaldar
2. Para cada claim: fuente verificable (URL), dato concreto o inferencia, accesible o no
3. Si más de 2 claims no tienen fuente accesible: PAUSAR y pedir al usuario verificación manual o buscar fuentes alternativas
4. Si un claim depende de una página .gov.py, verificar que el contenido fue extraído correctamente (usan JS que los agentes no ejecutan)

**Compuerta B — Pre-publicación (post-escritura, pre-commit):**

1. Leer el artículo completo
2. Para cada afirmación con número, fecha, nombre o monto: verificar que tiene fuente en la sección Fuentes
3. Si una afirmación no tiene fuente verificable: eliminarla o marcarla como "estimación del autor"
4. El fact-check con agente independiente se ejecuta ANTES del commit, no después
5. Si el fact-check encuentra errores, corregir y re-ejecutar hasta que pase

### 6.3 Auditoría retrospectiva (16 julio 2026)

Se auditaron 27 artículos long-form contra fuentes verificables. Resultados:

| # | Error | Corrección |
|---|---|---|
| #9 Peter Thiel | Crusoe Wyoming 2.7 GW | 1.8 GW |
| #17 Anotación | 2da electricidad más barata del mundo | ~27va |
| #17 Anotación | Paraguay UTC-4 | UTC-3 desde 2024 |
| #18 Educación | Constitución 7% PIB | 20% presupuesto Admin Central |
| #1 Yguazú | Población 7M y 7.5M | 6.5M (INE 2022) |
| #2 Apertura | Decreto 6034 firmado 20 mayo | 19 mayo |
| #3 Cripto | Bitfarms enero 2026 | Enero 2025 |
| #29 Fintech | Findex 2024 | No existe esa edición |
| #35 Startups | VC 325% | ~300% (error aritmético) |

**Lecciones:**
- Doble verificación obligatoria: los fact-checkers también se equivocan
- Los datos escritos de memoria son la principal fuente de errores
- Los artículos más antiguos (mayo-junio 2026) tienen más errores

---

## 7. SEO técnico

### 7.1 Schema y datos estructurados

| Schema | Ubicación | Propósito |
|---|---|---|
| Person (`@id: #author`) | `_includes/custom-head.html` | Entidad global para autoría. Incluye `image` (foto WebP 5.9KB), `description` (bio profesional), `jobTitle`, `knowsAbout` granular (7 items alineados a pilares) |
| Organization (`@id: #org`) | `_includes/custom-head.html` | Entidad global para el publisher. Incluye `publishingPrinciples` y `correctionsPolicy` → `/como-trabajamos/` |
| Article | `_layouts/post.html` | Cada artículo del blog |
| TechArticle | `_layouts/page.html` | Páginas: pillar page, glosario, directorio, cronologia, regulacion, casos-de-uso, como-trabajamos |
| CollectionPage | Homepage + `/ia-en-paraguay/` | Señal de hub temático. `mainEntity` apunta al observatorio. |
| DefinedTermSet | `/glosario/` | 5 términos como `DefinedTerm` con `name` + `description`. |
| ItemList | `/directorio/` | 5 organizaciones como `ListItem` → `Organization`. |
| FAQPage | Inline en cada artículo | Rich snippets en Google |
| BreadcrumbList | `_layouts/post.html` | Navegación estructurada |
| WebSite (con SearchAction) | Homepage (layout) | `@id: #website` + `SearchAction` → `/buscar/?q=`. Único WebSite en el sitio — reemplaza al de jekyll-seo-tag. |
| SpeakableSpecification | `_layouts/post.html` | Voice search. Se genera por artículo. |

**Arquitectura semántica hub-and-spoke:** todas las páginas del observatorio (`/cronologia/`, `/regulacion/`, `/directorio/`, `/casos-de-uso/`, `/glosario/`) incluyen `isPartOf: /ia-en-paraguay/#collection` en su `TechArticle`. Google entiende el pillar page como centro de autoridad.

**Validación:** 0 errores, 0 warnings en validator.schema.org.

### 7.2 IndexNow

| Componente | Detalle |
|---|---|
| API key | `624a4302f1714f068e9851beb7b692f2` (verificada) |
| Verificación | `https://muchotexto.net/624a4302f1714f068e9851beb7b692f2.txt` |
| Script | `scripts/ping_indexnow.py` — lee `_site/sitemap.xml`, dedupea contra cache, notifica URLs nuevas/modificadas |
| Automatización | Paso en `.github/workflows/jekyll.yml` tras cada build |
| Proveedores | Bing, Yandex, Seznam (api.indexnow.org) |

### 7.3 Infraestructura técnica

| Componente | Detalle |
|---|---|
| Hosting | GitHub Pages + GitHub Actions |
| SSG | Jekyll 4.4.1 con Ruby 3.3 |
| CSS | Síncrono (~24KB compilado, 4.6KB crítico inline) — eliminó CLS de 0.299 |
| robots.txt | Reglas explícitas para bots de IA: GPTBot, ChatGPT-User, PerplexityBot, Google-Extended, ClaudeBot, cohere-ai + wildcard \* (cubre OAI-SearchBot) |
| llms.txt | Servido en raíz, linkeado en `<head>`, actualizado con cada artículo |
| Sitemap | Generado por jekyll-sitemap + plugin para homepage |
| Paginación | Deshabilitada (19-jul-2026). Homepage rediseñada como landing page del observatorio. |
| GA4 | Consent Mode v2 |
| GSC + Bing WMT | Verificados |

### 7.4 Consolidación de tags (completado)

**43 tags originales → 8 tags paraguas:**

| Tag paraguas | Tags que absorbe | Pilar |
|---|---|---|
| `ia-paraguay` | ia, paraguay, inteligencia-artificial, tecnologia | Todos |
| `infraestructura-energia` | energia, data-center, yguazu-digital, ANDE | Pilar 1 |
| `geopolitica-regulacion` | geopolitica, taiwan, china, regulacion | Pilar 2 |
| `sociedad-trabajo` | educacion, trabajo-digital, gobierno-digital | Pilar 3 |
| `tech-ecosistema` | blockchain, fintech, startups, agro | Pilar 4 |
| `cultura-filosofia` | filosofia, etica, futbol, cultura | Pilar 5 |
| `analisis-ia` | analisis, burbuja-ia, costos-ia | Todos |
| `paraguay-futuro` | desarrollo, soberania, prospectiva | Pilar 2, 3 |

---

## 8. AI Search Optimization

### 8.1 ChatGPT Deep Research: cómo recupera contenido

ChatGPT no navega el web abierto como Google. Pasa por 4 etapas para decidir si una página aparece en una respuesta:

**Etapa 0: La compuerta (`turn_use_case`).** Antes de buscar cualquier cosa, ChatGPT clasifica el turno en un bucket. Si el bucket es `text`, no busca en el web — responde desde su corpus de entrenamiento. No importa qué tan buena sea la página. La redacción del usuario decide el bucket, no el tema.

**Etapa 1: Reformulación.** ChatGPT rara vez busca las palabras literales del usuario. Reformula la consulta en 1-3 búsquedas distintas. Hay que optimizar para las reformulaciones, no para el prompt literal.

**Etapa 2: Fetch (superficie).** ChatGPT obtiene páginas a través de 4 pipelines:

| Pipeline | Tipo | Qué alcanza |
|---|---|---|
| `bright` (Bright Data) | Scraper comercial | Mayoría del web abierto |
| `oxylabs` (Oxylabs) | Scraper comercial | Medios regionales y prensa local |
| `labrador` | Tier licenciado | Publishers con acuerdo con OpenAI (Reuters, WSJ, Wikipedia, arXiv). No se puede entrar por mérito. |
| `serp` | Línea base del web abierto | Consultas de noticias, resultados de buscadores |

**El motor de búsqueda de ChatGPT es Bing, no Google.** Cada búsqueda lleva `"source":"web_with_bing"`. La visibilidad en Bing determina si una página existe para ChatGPT.

**Etapa 3: Selección.** De las páginas traídas, solo un subconjunto se selecciona para influir en la respuesta. Una página puede ser traída y descartada antes de influir — es el equivalente a "rankeada pero no featured".

**Etapa 4: Citación.** Solo las páginas citadas aparecen en la respuesta visible al usuario, en el campo `citations`. Las citas se vinculan a afirmaciones específicas, no a temas generales.

### 8.2 El agente de lectura de ChatGPT

- **User-Agent:** `OAI-SearchBot` (diferente de `GPTBot`). Si `robots.txt` bloquea OAI-SearchBot, ChatGPT no lee la página.
- **Ventana de snippet Bing:** ~285 caracteres. Ese es todo el espacio para ganar el "open".
- **Ventana de lectura:** ~5.000-6.000 caracteres por open. Lo que no entre en ese primer bloque, probablemente no se lea.
- **No hace clics.** Solo ejecuta `search`, `open` y `find`. Menús JS, acordeones, SPAs renderizados en cliente no existen para el agente.
- **Lee el HTML linearizado de arriba a abajo.** El `<head>` se descarta. Cada link se renderiza inline como `→n→anchor→url→`. La posición en pantalla es irrelevante; el orden en el HTML es lo que cuenta.
- **Sigue enlaces internos** con anchor text descriptivo.
- **Lee alt text de imágenes** como contenido.
- **Re-lecturas por keyword.** Si encuentra una keyword que espera, re-abre la página posicionado en esa línea. Si no la encuentra, abandona la página.
- **Profundidad (`topn`):** hasta 10 en consultas exploratorias, 3 por defecto, 2 al verificar un hecho.

### 8.3 Diagnóstico del funnel de ChatGPT

| Síntoma | Dónde falla la página | Qué hacer |
|---|---|---|
| No aparece en `search_result_groups` | Problema de descubribilidad | Optimizar para las reformulaciones de ChatGPT. Mejorar presencia en Bing. |
| Aparece en resultados pero no en `caterpillar_selected_sources` | Visto pero no seleccionado | Mejorar alineación con intención de búsqueda. Datos duros arriba. |
| Aparece en seleccionados pero no en `citations` | Considerado pero descartado en la síntesis | El contenido no fue la mejor fuente para una afirmación específica. |
| `Fetch denied by robots.txt` | Bloqueado por OAI-SearchBot | Corregir robots.txt inmediatamente. |
| `result_source` es `bright` o `oxylabs` | Estás en el pool scrolleable | Asegurar que Bright Data pueda parsear la página: HTML semántico, sin JS crítico. |

### 8.4 Google AI Optimization Guide 2026

Basado en la guía oficial de Google (julio 2026):

| Hallazgo | Implicación para muchotexto.net |
|---|---|
| SEO sigue siendo SEO — AEO/GEO son términos de marketing, no métodos diferentes | Mantener prácticas SEO estándar |
| Google usa RAG (mismo índice que búsqueda tradicional) | El contenido que rankea en Google tiene más probabilidades de ser citado por AI Overviews |
| **Google NO usa llms.txt** | Lo mantenemos para ChatGPT/Perplexity, no por Google |
| No fragmentar contenido para AI | Validado nuestro formato de 1.500-2.500 palabras |
| No reescribir para AI — escribir para humanos | Metodología PROS/CONTRAS y fuentes verificadas es el enfoque correcto |
| Structured data no es obligatorio para AI Overviews | FAQ schema es buena práctica, no requisito de AI search |
| Contenido no genérico es el factor más importante | Experiencia de primera mano (César en anotación de datos, IA) es la ventaja |
| Las experiencias de agente (UCP) son el futuro | Evaluar cuando maduren |

### 8.5 Implicaciones prácticas

| Hallazgo | Acción |
|---|---|
| OAI-SearchBot es el user-agent de fetch | Verificar que `robots.txt` permita `OAI-SearchBot` ✅ |
| Bing es el motor de búsqueda para ChatGPT | Monitorear presencia en Bing Webmaster Tools |
| ~285 chars de snippet Bing | Meta description y primeros 285 caracteres con keyword + dato + promesa |
| ~5-6k chars de ventana de lectura | Hook, contexto y datos duros en los primeros párrafos |
| Anchor text descriptivo | Cada enlace interno debe describir exactamente adónde lleva |
| HTML linearizado, no JS | Jekyll estático cumple por defecto ✅ |
| Alt text como contenido | Poner datos clave en alt text ✅ (verificado, no aplica: sitio text-only) |
| Sin clicks (solo search/open/find) | Contenido visible en HTML inicial ✅ |

### 8.6 Brechas detectadas en AI Overview de Google (18-jul-2026)

AI Overview sobre "referentes de la IA en Paraguay" menciona temas que no cubrimos:

**Cubierto:**
- Hive Digital ✅ | NVIDIA ✅ | OpenAI ✅ | Misiones Silicon Valley ⚠️ (parcial)

**No cubierto — agregar a artículos planeados:**
- P2 "Silicon Valley en el Cono Sur" → incluir ASUS
- P3 "Formación universitaria en IA" → incluir Lilian Demattei

**No cubierto — requieren artículo nuevo:**
- Dominion AI / Paraguay Underground
- IA + biomedicina en Paraguay (Marcelo Báez, Santiago Noto, María del Mar Sánchez)

---

## 9. E-E-A-T y autoridad

### 9.1 Information gain como diferenciador

En 2026, Google prioriza el *non-commodity content* — contenido que aporta algo que no existe en ningún otro lado. La combinación `IA + Paraguay + experiencia real` es el *information gain* de muchotexto.net.

**Tácticas:**
- Escribir desde la experiencia de primera mano (anotación de datos, bots con IA, reforma energética)
- Mostrar screenshots reales, datos propios, proyectos documentados
- No rehacer contenido que ya existe — siempre aportar un ángulo nuevo

### 9.2 Author authority

- **Página /about/ con schema Person** — credenciales verificables, links a redes
- **E-E-A-T real** — trayectoria concreta (anotación de datos, proyectos con Ollama/Groq, consultoría SEO), no un "sobre mí" genérico
- **Entity SEO** — mencionar consistentemente términos relacionados: "inteligencia artificial", "Paraguay", "machine learning", "automatización", "Latinoamérica"

### 9.3 Construir autoridad off-site

| Canal | Acción | Frecuencia |
|---|---|---|
| LinkedIn | Compartir cada artículo nuevo + reflexión personal de 3-5 líneas | Cada publicación |
| Twitter/X (@cesanz) | Amplificar cada pieza nueva del cluster | Cada publicación |
| Reddit (r/Paraguay, r/devsarg) | Responder preguntas, compartir artículos cuando sean relevantes | Semanal |
| Guest posts | Escribir en blogs tech de Latinoamérica | 1 cada 2 meses |
| Podcasts | Participar como invitado en podcasts de tecnología | Según oportunidad |
| Medios paraguayos | Contactar periodistas de tecnología de ABC, La Nación, HOY, NPY ofreciendo artículos como fuente citable | Según publicación relevante |

---

## 10. Distribución y link building

### 10.1 Estrategia de backlinks

**Objetivo:** backlinks desde medios paraguayos establecidos (ABC Color, La Nación, HOY, NPY). Estos medios ya cubren Yguazú Digital y temas de IA constantemente.

**Táctica:** al publicar piezas de referencia (explainers, comparativos regionales), contactar periodistas de tecnología ofreciendo la pieza como fuente de contexto citable.

**Piezas con mayor potencial de backlink:**
1. Yguazú Digital a fondo (#1) — ya publicado, actualizar y promover
2. Paraguay vs. la región (#5 del banco original) — inédito, alto potencial
3. Ley de Protección de Datos (#12) — inédito, coyuntura legislativa
4. El costo energético real de la IA (#6) — inédito, datos duros

### 10.2 Distribución en redes

| Plataforma | Formato | Contenido |
|---|---|---|
| Twitter/X | Hilo de 5-7 tweets | Resumen del artículo + dato más impactante + link |
| LinkedIn | Post de 3-5 párrafos | Reflexión personal + gancho + link |
| Reddit | Respuesta a preguntas | Aportar valor primero, link solo si es relevante |
| GitHub | README/proyecto | Si el artículo documenta un proyecto técnico |

### 10.3 Reutilización cruzada

- Editoriales que toquen IA (actualmente solo 20%): subir la frecuencia aprovechando la coyuntura
- Cada Pulso Paraguay que mencione IA debe enlazar a la página pilar
- En vez de multiplicar artículos casi idénticos sobre Yguazú Digital, actualizar el explainer central

---

## 11. Observatorio: páginas vivas

Evolución del sitio de "medio digital" a "observatorio de IA en Paraguay": contenidos permanentes, actualizables, que construyen autoridad temática para búsqueda generativa (GEO).

### Fase 1 — Conversión de activos existentes (semana 1) ✅

| Activo | Evolución |
|---|---|
| `/ia-en-paraguay/` | Header: "Observatorio de IA en Paraguay". 31 artículos organizados por pilar. |
| `/glosario/` (~40 términos) | "Glosario vivo de IA en Paraguay". Fecha de última actualización visible. Cada término vinculado a su artículo fuente. |
| Cronología en pillar page | Ya integrada. |

### Fase 2 — Contenidos permanentes nuevos (semanas 2-6) ✅

| Página | Mantenimiento |
|---|---|
| `/cronologia/` — Hitos de IA en Paraguay | Agregar 1-2 hitos por artículo nuevo |
| `/directorio/` — Startups y comunidades de IA en Paraguay | Revisión constante. Incluye Eventos, Comunidades, Startups. |
| `/regulacion/` — Mapa regulatorio de IA en Paraguay | Actualizar con novedades legislativas |
| `/casos-de-uso/` — IA en sectores productivos | Agregar 1 caso por artículo nuevo |

### Fase 3 — Contenidos que requieren investigación nueva (pendiente)

| Página | Requiere | Prioridad |
|---|---|---|
| `/indice-adopcion/` — Índice de adopción de IA | Investigación original: mapear empresas PY usando IA | Media |
| `/ranking-universidades/` — Carreras de IA en Paraguay | Mapear UNA, UCA, UAA, UA, UNE, bootcamps | Media |

### Arquitectura objetivo

```
muchotexto.net — Observatorio de IA en Paraguay
├── /ia-en-paraguay/     (biblioteca de análisis con filtro sectorial)
├── /glosario/           (vivo, con fecha de actualización)
├── /cronologia/         (hitos de IA en Paraguay)
├── /directorio/         (startups de IA paraguayas)
├── /regulacion/         (mapa regulatorio)
├── /casos-de-uso/       (sectores productivos)
├── /indice-adopcion/    (Fase 3)
├── /ranking-universidades/ (Fase 3)
└── /como-trabajamos/
```

---

## 12. Automatización — Pulso + Editorial

### 12.1 Pulso Paraguay (cron 08:00 PYT / 12:00 UTC)

- **Script:** `scripts/pulso_diario.py`
- **Modelo:** gpt-4o-mini (GitHub Models)
- **Fuentes RSS:** 16 fuentes RSS (15 medios + 1 sección CyT de La Tribuna)
- **Formato:** TEMA #1 → Política → Economía → Deportes → Cultura → Seguridad → Virales → Ranking → Insight → Análisis → Fuentes
- **Categoría:** `pulso-paraguay`
- **Commit:** `git add _posts/` → `git pull --rebase origin main` → `git push`
- **Auto-fix:** `fix_pulso_descriptions.py` corrige descriptions antes del commit

### 12.2 Editorial Diaria (cron 18:00 PYT / 22:00 UTC)

- **Script:** `scripts/editorial_diario.py`
- **Modelo:** gpt-4o (GitHub Models), temperature 0.3
- **Dependencia:** Lee el Pulso del día; si no existe, sale sin error (`sys.exit(0)`)
- **Categoría:** `editorial`
- **Pipeline:** Leer Pulso → llamar API (3 retries, backoff 2s/4s/8s) → validar contenido → insertar links → guardar
- **Commit:** `git add _posts/` → `git pull --rebase origin main` → `git push`
- **Auto-fix:** `fix_editorial_descriptions.py` corrige descriptions antes del commit

### 12.3 System prompt — reglas clave

- Solo usar información del Pulso. No contexto externo ni conocimiento general.
- No atribuir citas, ideas o dichos a personas sin que aparezcan textualmente en el Pulso.
- No convertir personas en símbolos, ejemplos ni metáforas. No inferir tono de declaraciones.
- Prohibido: metáforas forzadas (`X es el espejo de Y`), preguntas retóricas vacías, fechas como apertura.
- Idioma: español de Paraguay con voseo, sin jopara ni guaraní.
- **Títulos editoriales:** coma entre cláusulas (ej: "Seguridad y elecciones, una conexión clave").

### 12.4 Validación de contenido (`validate_content`)

- **critical_patterns:** "pelea por entrar al Mundial", "clasificar al Mundial", "eliminado", "partido de ayer"
- **Embellish detection:** `refuerza|encarna|representa|simboliza` + `experiencia|liderazgo`
- **Name check:** nombres propios en editorial que no aparecen en el Pulso
- **Low overlap check:** oraciones con <2 palabras de 5+ chars en común con el Pulso

### 12.5 Auto-linking (`add_internal_links`)

- 11 patrones regex con `\b(?:...)\b` y gaps `.{0,N}?` no-greedy
- Safety check: no inserta link si corta una palabra (`isalnum()` + `_`)
- Temas detectados: Yguazú Digital, centro IA, ANDE/sector eléctrico, Itaipú, Peter Thiel, burbuja IA, tokenización, encíclica, IA+fútbol, protección de datos, identidad digital

### 12.6 Hardening de infraestructura

- [x] `sanitize_yaml()`: eliminación de 12 caracteres peligrosos (`:{}[]&*!|>#%` + comillas)
- [x] API retry: 3 intentos con backoff exponencial (2s, 4s, 8s)
- [x] `try/except (OSError, UnicodeDecodeError)` en lectura de archivos
- [x] `git pull --rebase` antes de `git push` en ambos workflows
- [x] `git add _posts/` (no `git add -A`) en ambos workflows
- [x] API response guard: `.get("choices", [{}])[0].get("message", {}).get("content", "")`

### 12.7 Observatorio Intel — Dashboard editorial

- **Script:** `scripts/observatorio_intel.py`
- **Ejecución:** manual, recomendado semanal (viernes)
- **Output:** `_planning/estado-observatorio.md` (no se commitea — está en `.gitignore`)
- **No usa IA.** Análisis de archivos markdown del repositorio. Sin dependencias externas.
- **4 secciones:**
  1. Cobertura por pilar — artículos publicados/pendientes y balance entre pilares
  2. Artículos vencidos — posts sin `last_modified_at` o con >90 días sin revisión
  3. Temas del Pulso sin cobertura — bigramas frecuentes en la sección Tecnología del Pulso que no tienen artículo long-form
  4. Densidad del observatorio — entradas por página viva (Glosario, Directorio, Cronología, Regulación, Casos de uso) y fecha de última actualización
- **Decisiones que alimenta:** ¿qué pilar reforzar? ¿qué artículo actualizar? ¿qué brecha detectó el Pulso? ¿qué página del observatorio está atrasada?

### 12.8 Entidades — Infraestructura de conocimiento

- **Script:** `scripts/build_entities.py`
- **Ejecución:** manual, después de publicar artículos nuevos o modificar `_data/entities.yml`
- **No usa IA.** Análisis de archivos markdown del repositorio. Dependencia: PyYAML.
- **18 entidades curadas** en `_data/entities.yml` (MITIC, ANDE, Itaipú, Yguazú Digital, Taiwán, CERT-PY, HIVE, Starlink, KOGA, X8 Cloud, Peter Thiel, Santiago Peña, BID, TSMC, SOPAIA, PTI-PY, UNA, AmCham)
- **Landing page:** `/entidades/` — grid de tarjetas responsive con categoría y conteo dinámico de artículos por entidad

**Plantilla estándar de cada página de entidad** (orden fijo para todas):

1. **Encabezado** — nombre corto + nombre completo + descripción curada + categoría + fecha en español
2. **Artículos relacionados** — artículos long-form (`categories: articulos`) donde el nombre de la entidad aparece en el título o en los primeros 800 caracteres del cuerpo. Contexto extraído por párrafo (no offset arbitrario). Full-name fallback para entidades con nombres alternativos (MITIC → "Ministerio de Tecnologías"). Sin Pulso ni Editorial.
3. **Leyes y normativas** — lista curada en `related_laws` del `_data/entities.yml`. Con link "Ver mapa regulatorio completo →"
4. **En la cronología** — hitos de `/cronologia/` que mencionan la entidad. Cada entrada linkea al artículo fuente. Con link "Ver cronología completa →"
5. **En el directorio** — entradas de `/directorio/` cuyo nombre coincide con la entidad (no por descripción). Con link "Ver directorio completo →"
6. **En regulación** — normas de `/regulacion/` que mencionan la entidad en su texto. Con link "Ver mapa regulatorio completo →"
7. **Casos de uso** — entradas de `/casos-de-uso/` que mencionan la entidad. Con deep scan en artículo linkeado (1500 chars) para detectar menciones no explícitas. Con link "Ver todos los casos de uso →"
8. **En el glosario** — términos de `/glosario/` cuyo nombre coincide con la entidad (no por descripción). Sin links individuales confusos. Con link "Ver glosario completo →"

**Reglas de calidad de la extracción:**

| Regla | Detalle |
|---|---|
| Coincidencia por nombre | Solo el nombre de la entidad (no keywords genéricos como "inversión" o "energía") |
| Sin Pulso ni Editorial | Solo `categories: articulos` (contenido verificado con Compuertas A/B) |
| Glosario/Directorio por nombre | Solo si el término o entrada se llama como la entidad (no por menciones en la definición) |
| Contextos limpios | Sin HTML, sin JSON-LD, sin markdown links, truncado en borde de palabra con "..." |
| URLs sin acentos | Normalización á→a, é→e, etc. para evitar 404s |
| Fecha en español | "30 de julio de 2026", no "30 Jul 2026" |
| Acentos correctos | Todos los textos en español con tildes, eñes y diacríticos |

**Propósito:** ofrecer a periodistas e investigadores una puerta de entrada por entidad al conocimiento acumulado del observatorio. No genera contenido nuevo — estructura y organiza el existente con fuentes verificables.

**SEO/AEO:** 18 páginas ricas en interlinking con anchor text descriptivo. Formato estructurado ideal para extracción por ChatGPT/Perplexity. Schema Thing por página. Indexadas en sitemap.

**Mantenimiento:** `python scripts/build_entities.py` regenera desde cero. Las entidades sin presencia en el contenido se eliminan automáticamente (archivos huérfanos).

### 12.9 Pendientes conocidos (no críticos)

- [ ] Timezone hardcoded UTC-4; Paraguay usa UTC-3 en horario de verano (oct-mar)
- [ ] No hay dependencia explícita Editorial→Pulso (solo separación horaria de 10h)
- [ ] Sin dedup al re-ejecutar manualmente (crea posts duplicados)

---

## 13. Stack técnico y herramientas

### 13.1 Pila tecnológica

| Componente | Detalle |
|---|---|
| Hosting | GitHub Pages + GitHub Actions |
| SSG | Jekyll 4.4.1 con Ruby 3.3 |
| Tema | Monophase (local) |
| Dominio | muchotexto.net (GoDaddy → GitHub Pages) |
| Comentarios | Sin sistema de comentarios |
| Buscador | Simple-Jekyll-Search (cliente) |
| Estilo | Modo oscuro forzado (sin light mode) |
| Plugins | jekyll-seo-tag, jekyll-sitemap, jekyll-feed, jekyll-paginate-v2 |

**Modelos IA:**
- gpt-4o (editorial) — GitHub Models
- gpt-4o-mini (pulso) — GitHub Models
- DeepSeek (investigación) — GitHub Models
- MiniMax (síntesis) — GitHub Models
- Qwen (desarrollo) — GitHub Models

### 13.2 Estructura y navegación

**Categorías de contenido:**

| Categoría | Contenido | Generación |
|---|---|---|
| `articulos` | Ensayos long-form (IA + Paraguay + análisis) | Manual + investigación con 4-5 subagentes paralelos |
| `pulso-paraguay` | Reporte diario de noticias | Automático (cron 08:00 PYT) |
| `editorial` | Opinión diaria basada en el Pulso | Automático (cron 18:00 PYT) |

**Páginas estáticas:**
`/` `/about/` `/como-trabajamos/` `/contacto/` `/ia-en-paraguay/` `/glosario/` `/cronologia/` `/directorio/` `/regulacion/` `/casos-de-uso/` `/categories/` `/archive/` `/tags/` `/buscar/` `/privacidad/` `/terminos/` `/404.html`

**Navegación:** Inicio | Observatorio IA | Entidades | Glosario | Categorías | Acerca de | Cómo trabajamos | Contacto

> `/cronologia/`, `/directorio/`, `/regulacion/`, `/casos-de-uso/` no están en la nav principal por diseño: se accede desde la página pilar y llms.txt. Son páginas de referencia, no de navegación primaria.

### 13.3 Mapa de archivos clave

```
muchotexto.net/
├── _config.yml              # Jekyll: url, plugins, pagination, SEO defaults
├── index.markdown           # Home (layout: home, paginación)
├── about.markdown           # Acerca de
├── contacto.markdown        # Contacto
├── llms.txt                 # AI crawler-friendly site map
├── robots.txt               # Allow all + AI bot rules explícitas + sitemap
├── como-trabajamos.markdown  # Metodología editorial y transparencia
├── _includes/
│   ├── head.html            # Preconnect + CSS síncrono + favicon + noindex en paginación
│   ├── custom-head.html     # CSP, GA4 consent, og:image, GSC/Bing, Person+Organization JSON-LD
│   ├── critical-css.html    # CSS crítico inline (dark mode only)
│   ├── cookie-consent.html  # Banner cookies (GA4 consent)
│   └── share.html           # Native share API
├── _layouts/
│   ├── post.html            # Article JSON-LD + BreadcrumbList + SpeakableSpecification + author bio
│   ├── page.html            # TechArticle JSON-LD + author bio
│   ├── home.html            # Homepage con paginación + WebSite schema
│   ├── entidad.html          # Pagina de entidad: 8 secciones estandar, schema Thing
│   └── default.html         # Layout base
├── _data/navigation.yml     # Menú de navegación (8 items)
├── _data/entities.yml       # Lista curada de entidades clave para build_entities.py
├── entidades/               # Paginas de entidad generadas (18 entidades)
│   ├── index.markdown       # Landing page: grid de todas las entidades
│   └── {slug}.markdown      # Pagina individual por entidad (layout: entidad)
├── scripts/
│   ├── pulso_diario.py      # Genera Pulso Paraguay (gpt-4o-mini, 15 RSS feeds)
│   ├── editorial_diario.py  # Genera Editorial (gpt-4o) + auto-linking + validación
│   ├── generate_faq.py      # Genera FAQPage JSON-LD desde artículos con IA
│   ├── validate_publish.py  # Pre-commit hook: 12 checks
│   ├── ping_indexnow.py     # IndexNow auto-ping desde sitemap tras build
│   ├── rebuild_pillar.py    # Reconstruye la página pilar
│   ├── check_editorials.py  # Auditoría de editoriales
│   ├── check_urls.py        # Verifica que URLs de fuentes respondan (200 OK)
│   ├── check_accents.py     # Detecta acentos faltantes en español
│   ├── fix_pulso_descriptions.py   # Auto-fix descriptions de Pulso Paraguay
│   ├── fix_editorial_descriptions.py # Auto-fix descriptions de Editorial
│   ├── observatorio_intel.py   # Dashboard editorial: cobertura, vencidos, brechas, densidad
│   ├── build_entities.py   # Genera paginas de entidad desde _data/entities.yml
│   ├── fix_accents.py       # Corrige acentos faltantes en frontmatter
│   ├── fix_titles.py        # Corrige títulos largos o con problemas de formato
│   ├── backfill_format.py   # Corrección retroactiva de formato
│   ├── es_ES.dic            # Diccionario español para spell-check
│   └── .indexnow_cache.json # Cache de URLs ya notificadas a IndexNow
├── .github/workflows/
│   ├── jekyll.yml           # Build + deploy + IndexNow ping
│   ├── pulso-diario.yml     # Cron Pulso (08:00 PYT / 12:00 UTC)
│   ├── editorial-diario.yml # Cron Editorial (18:00 PYT / 22:00 UTC)
│   └── faq-generator.yml    # Auto-genera FAQPage (trigger: push a _posts/)
├── docs/
│   └── gap_report_template.md  # Template obligatorio pre-escritura
└── research_*/              # Directorios de investigación (25+ temas)
```

### 13.4 Skills disponibles

| Skill | Uso |
|---|---|
| `web-research` | Investigación multi-fuente con subagentes paralelos (4-5 por artículo) |
| `blog-post` | Estructura del artículo (hook, contexto, cuerpo, conclusión) |
| `agent-reach` | Búsquedas complementarias en redes, YouTube, plataformas |
| `copy-editing` | Pulido final: claridad, voz, datos, precisión |
| `seo-audit` | Validación post-publicación (meta tags, headings, keywords) |
| `audit-website` (squirrelscan) | Health check general del sitio post-deploy |
| `brainstorming` | Diseño de nuevos features o secciones del sitio |
| `investigation-first` | Verificación de datos antes de afirmar |
| `security-review` | Revisar cambios que involucren user input, secrets, o APIs |

### 13.5 Herramientas gratuitas

| Herramienta | Uso |
|---|---|
| Google Search Console | Monitoreo de rankings, impresiones, CTR, backlinks |
| Google Analytics (GA4) | Tráfico, engagement |
| PageSpeed Insights | Core Web Vitals |
| validator.schema.org | Validar schema markup |
| Rich Results Test | Verificar elegibilidad para rich results |
| Ahrefs Webmaster Tools | Backlinks, auditoría técnica (gratis) |
| squirrelscan | SEO health check del sitio completo |

---

## 14. Procedimientos operativos

### 14.1 Flujo completo de publicación de un artículo

1. Leer estrategia — verificar que el tema no esté duplicado
2. Leer artículos del mismo pilar (evitar overlap)
3. Crear carpeta `research_[tema]/` con `research_plan.md`
4. Desplegar 4-5 subagentes con `web-research`
5. **GAP REPORT** (ver §6.2 Compuerta A)
6. Escribir artículo: hook → contexto → 4-6 H2s → conclusión → fuentes
7. **FACT-CHECK PRE-COMMIT** (ver §6.2 Compuerta B)
8. Validar con `validate_publish.py`
9. Actualizar observatorio (cronologia, regulacion, directorio, casos-de-uso, glosario, página pilar, llms.txt)
10. **Actualizar este documento:** tabla §3.2 (marcar ✅), conteo de publicados/pendientes, §15 (mover de pendiente a completado), §16 (agregar al progreso)
11. Build, commit, push

### 14.2 Comandos frecuentes

```bash
# Build local
bundle exec jekyll build

# Servir local
bundle exec jekyll serve

# Commit y push (NUNCA commitear research_*/)
git add _posts/
git commit -m "descripcion"
git push

# Disparar workflows manualmente
gh workflow run "pulso-diario.yml" --ref main
gh workflow run "editorial-diario.yml" --ref main

# Verificar deploy
gh run list --workflow jekyll.yml --limit 1

# Dashboard editorial (semanal)
python scripts/observatorio_intel.py
```

### 14.3 Configuración y troubleshooting

- **GH_MODELS_TOKEN:** GitHub → Settings → Secrets → Actions → `GH_MODELS_TOKEN`
- **SSL/CNAME:** si falla, remover y re-agregar CNAME via GitHub Pages settings
- **Horario de verano (PYST, UTC-3, oct-mar):** los timestamps de frontmatter pueden estar 1h desplazados

### 14.4 Revisión semanal del observatorio (viernes, ~5 min)

**Objetivo:** tomar decisiones editoriales informadas antes de planificar la semana siguiente.

1. Ejecutar `python scripts/observatorio_intel.py`
2. Leer `_planning/estado-observatorio.md`
3. Revisar las 4 secciones:
   - **Cobertura:** ¿hay un pilar desbalanceado? Si uno tiene <70% y sin pendientes, abrir temas nuevos.
   - **Vencidos:** ¿hay artículos sin `last_modified_at` o con >90 días? Priorizar los más antiguos para revisión.
   - **Brechas:** ¿el Pulso menciona temas de tecnología que no tienen artículo long-form? Agregar al backlog.
   - **Densidad:** ¿alguna página del observatorio tiene pocas entradas o está atrasada? Actualizar la más débil.
4. Si se publicó un artículo nuevo, regenerar entidades: `python scripts/build_entities.py`
5. Actualizar §15 (Plan de acción) con las decisiones tomadas
6. Si se detecta una brecha nueva, crear entrada en el backlog de investigación

**Comandos:** `python scripts/observatorio_intel.py` + `python scripts/build_entities.py`

---

## 15. Plan de acción pendiente

### Prioridad alta

| # | Acción | Área |
|---|---|---|
| 1 | Verificar IndexNow en Bing Webmaster Tools (crawl status) | SEO |
| 2 | Verificar indexación y ranking en Google Search Console | SEO |
| 3 | Publicar artículo #7: Energía renovable y cambio climático (Pilar 1) | Contenido |
| 4 | Publicar artículo #8: Efecto derrame del data center (Pilar 1) | Contenido |
| 5 | Publicar artículo #15: El modelo Itaipú aplicado a la IA (Pilar 2) | Contenido |
| 6 | Publicar artículo #16: Silicon Valley en el Cono Sur (Pilar 2) | Contenido |
| 7 | Actualizar §16: auditar artículos #5, #34, #36 (publicados sin registro) | Calidad |

### Prioridad media

| # | Acción | Área |
|---|---|---|
| 8 | **Revisión semanal del observatorio** (`observatorio_intel.py` → decidir semana) | Editorial |
| 9 | Crear/optimizar perfil de LinkedIn con keywords del nicho | Autoridad |
| 10 | Preparar "media kit" de una página | Autoridad |
| 11 | Identificar 3-5 periodistas de tecnología en medios paraguayos | Autoridad |
| 12 | Crear cuenta/blog en LinkedIn para publicar versiones resumidas | Distribución |
| 13 | Preparar post de LinkedIn anunciando el cluster IA+Paraguay | Distribución |
| 14 | Verificar que páginas `/tags/` se regeneren correctamente | SEO |
| 15 | Crear template de `research_plan.md` reutilizable | Metodología |
| 16 | Revisar artículos publicados sin proceso de investigación | Calidad |

### Prioridad baja

| # | Acción | Área |
|---|---|---|
| 17 | Medir y documentar todos los baselines en GSC | KPIs |
| 18 | Crear dashboard simple (Google Sheets) con KPIs | KPIs |
| 19 | Programar recordatorio mensual para revisar KPIs | KPIs |
| 20 | Verificar impresiones para `inteligencia artificial Paraguay` en GSC | Diagnóstico |
| 21 | Identificar qué artículos ya rankean para términos IA+Paraguay | Diagnóstico |
| 22 | Verificar ranking actual de cada long-tail publicada en GSC | Keywords |
| 23 | Keywords en posiciones 4-15: priorizar actualización | Keywords |
| 24 | Identificar nuevas oportunidades long-tail (Google PAA + Reddit) | Keywords |
| 25 | Publicar artículos restantes (#7, #8, #15, #16, #42) | Contenido |
| 26 | Crear `/indice-adopcion/` (Fase 3 Observatorio) | Observatorio |
| 27 | Crear `/ranking-universidades/` (Fase 3 Observatorio) | Observatorio |

---

## 16. Registro de verificación de datos

Cada artículo debe ser auditado contra fuentes verificables. Los artículos nuevos se auditan al publicarse (misma fecha). Los existentes se auditan por prioridad.

**Leyenda:** ✅ Auditado | ⬜ Pendiente

| # | Artículo | Último chequeo | Estado |
|---|---|---|---|
| 1 | Yguazú Digital | 27-jul-2026 | ✅ |
| 2 | Apertura eléctrica | 27-jul-2026 | ✅ |
| 3 | Criptominería | 27-jul-2026 | ✅ |
| 4 | Itaipú 2027 | 27-jul-2026 | ✅ |
| 5 | Hidrógeno verde | 27-jul-2026 | ✅ |
| 6 | Red eléctrica | 27-jul-2026 | ✅ |
| 9 | Peter Thiel | 27-jul-2026 | ✅ |
| 10 | China-Taiwán | 27-jul-2026 | ✅ |
| 11 | IA soberana | 27-jul-2026 | ✅ |
| 12 | Ley protección datos | 27-jul-2026 | ✅ |
| 13 | Ciberseguridad | 27-jul-2026 | ✅ |
| 14 | Semiconductores Taiwán | 27-jul-2026 | ✅ |
| 17 | Anotación de datos | 27-jul-2026 | ✅ |
| 18 | Educación tech | 27-jul-2026 | ✅ |
| 20 | Futuro de la identidad | 27-jul-2026 | ✅ |
| 21 | Talento tech | 27-jul-2026 | ✅ |
| 22 | Starlink | 27-jul-2026 | ✅ |
| 23 | Gobierno digital | 27-jul-2026 | ✅ |
| 24 | IA y salud | 27-jul-2026 | ✅ |
| 25 | IA corrupción | 27-jul-2026 | ✅ |
| 26 | Soja al silicio | 27-jul-2026 | ✅ |
| 27 | Tokenización agro | 27-jul-2026 | ✅ |
| 28 | Agro 4.0 | 27-jul-2026 | ✅ |
| 29 | Fintech | 27-jul-2026 | ✅ |
| 30 | Encíclica IA | 27-jul-2026 | ✅ |
| 31 | IA periodismo | 27-jul-2026 | ✅ |
| 32 | Smart cities | 27-jul-2026 | ✅ |
| 33 | IA justicia | 27-jul-2026 | ✅ |
| 34 | E-commerce | 27-jul-2026 | ✅ |
| 35 | Startups IA | 27-jul-2026 | ✅ |
| 36 | Cadena valor data center | 27-jul-2026 | ✅ |
| 37 | 5 tecnologías | 27-jul-2026 | ✅ |
| 39 | Burbuja IA | 27-jul-2026 | ✅ |
| 40 | USA fútbol IA | 27-jul-2026 | ✅ |
| 41 | Guaraní e IA | 28-jul-2026 | ✅ |

**Auditados: 35 de 35 análisis (38 artículos total; #19 y #38 no son análisis).**

**Regla:** todo artículo nuevo se audita ANTES de commit. Cada 5 artículos nuevos, auditar los 5 más antiguos no auditados.

---

## 17. Progreso completado

| # | Acción | Fecha |
|---|---|---|
| 1 | Consolidar taxonomía de tags (43 → 8 paraguas) | 7-jul |
| 2 | Schema Person en /about/ | 7-jul |
| 3 | Crear página pilar /ia-en-paraguay/ | 7-jul |
| 4 | Agregar navegación IA en Paraguay + Cómo trabajamos | 17-jul |
| 5 | Actualizar description _config.yml e llms.txt | 7-jul |
| 6 | Squirrelscan audit post-cambios (75/100 C) | 7-jul |
| 7 | Reparar JSON-LD (image + publisher.logo) | 7-jul |
| 8 | Reparar 5 links externos rotos | 7-jul |
| 9 | Acortar 7 títulos long-form a ≤70 chars | 7-jul |
| 10 | Description única en 9 páginas estáticas | 7-jul |
| 11 | Enlazar 15 artículos a página pilar | 7-jul |
| 12 | Footer César Sánchez → /about/ | 7-jul |
| 13 | Pillar page: TechArticle + FAQ schema + entity + 1952pal | 8-jul |
| 14 | Artículo #12: Ley protección datos | 7-jul |
| 15 | Home: thin content corregido (~150 palabras) | 8-jul |
| 16 | Script editorial: truncado títulos ≤70 chars | 8-jul |
| 17 | Script pulso: truncado títulos ≤70 chars | 8-jul |
| 18 | Artículo #6: Red eléctrica Paraguay + IA | 8-jul |
| 19 | Artículo #10: Paraguay entre China y Taiwán | 9-jul |
| 20 | Artículo #18: Educación tech en Paraguay | 10-15-jul |
| 21 | Artículo #21: Talento tech | 10-15-jul |
| 22 | Artículo #22: Starlink en Paraguay | 10-15-jul |
| 23 | Artículo #25: IA y corrupción | 10-15-jul |
| 24 | Artículo #26: De la soja al silicio | 10-15-jul |
| 25 | Artículo #28: Agro 4.0 | 10-15-jul |
| 26 | Artículo #29: Fintech en Paraguay | 10-15-jul |
| 27 | Artículo #30: Encíclica IA Papa León XIV | 17-jul |
| 28 | Artículo #32: Smart cities Asunción | 17-jul |
| 29 | Artículo #35: Startups paraguayas de IA | 17-jul |
| 30 | Artículo #4: Itaipú 2027 | 17-jul |
| 31 | Artículo #11: IA soberana | 16-jul |
| 32 | Artículo #13: Ciberseguridad | 17-jul |
| 33 | Artículo #14: Semiconductores Taiwán | 14-jul |
| 34 | Artículo #23: Gobierno digital | 16-jul |
| 35 | Artículo #24: IA y salud | 16-jul |
| 36 | Artículo #31: IA y periodismo | 16-jul |
| 37 | Entity Linking: Organization + WebSite + TechArticle con Wikipedia/Wikidata | 17-jul |
| 38 | Organization schema: areaServed/locationCreated corregido | 17-jul |
| 39 | SpeakableSpecification en todos los artículos (voice search) | 17-jul |
| 40 | Reemplazo "blog" → "medio digital" en todo el proyecto | 17-jul |
| 41 | Página /como-trabajamos/ con metodología editorial completa | 17-jul |
| 42 | FAQ auto-generator: script + workflow | 17-jul |
| 43 | Revisión editorial: "por muestreo" → "revisión diaria de cada publicación" | 17-jul |
| 44 | robots.txt con reglas explícitas para bots de IA (GPTBot, ChatGPT-User, PerplexityBot, Google-Extended, ClaudeBot, cohere-ai) | 17-jul |
| 45 | Pilares actualizados: 29 publicados → 31 publicados | 17-jul |
| 46 | Remark42 eliminado de privacidad y contacto | 17-jul |
| 47 | Schema Article JSON-LD en _layouts/post.html | 17-jul |
| 48 | Schema TechArticle JSON-LD en _layouts/page.html | 18-jul |
| 49 | sameAs unificado (Person + Organization → x.com/cesanz) | 17-jul |
| 50 | IndexNow automático desde sitemap tras cada build | 18-jul |
| 51 | IndexNow cleanup: removido ping_indexnow() muerto de validate_publish.py | 18-jul |
| 52 | Pulso Paraguay descriptions: fix 32 posts + auto-fix en CI | 18-jul |
| 53 | Editorial descriptions: fix 22 posts + auto-fix en CI | 18-jul |
| 54 | Editorial titles: coma entre cláusulas + 3 títulos corregidos | 18-jul |
| 55 | CSS síncrono (6KB) — eliminó CLS de 0.299 | — |
| 56 | llms.txt creado y linkeado en <head> | — |
| 57 | GSC + Bing Webmaster Tools verificados | — |
| 58 | Twitter tags corregidas (site + creator → @cesanz) | — |
| 59 | Sitemap: homepage incluida vía plugin post_write | — |
| 60 | Hardening automatización: sanitize_yaml, API retry, try/except, rebase | 16-jul |
| 61 | 5 reglas críticas de calidad implementadas | 16-jul |
| 62 | Compuertas A/B + Gap Report implementados (post-artículo #23) | 16-jul |
| 63 | Auditoría retrospectiva de 27 artículos (9 errores corregidos) | 16-jul |
| 64 | Homepage rediseñada: hero con pilares + 3 cards de análisis + 2 cards de daily feed + sección "Sobre el observatorio" | 19-jul |
| 65 | Paginación deshabilitada. Homepage convertida en landing page del observatorio. | 19-jul |
| 66 | Conteo de artículos dinámico en homepage y pillar page (Liquid, auto-update en build) | 19-jul |
| 67 | Tags reemplazados por nombres de sector en cards de análisis | 19-jul |
| 68 | Descripciones completas en cards (sin truncado ni ...) | 19-jul |
| 69 | Artículo #38 removido del observatorio (no es análisis de IA). Conteo: 31. | 19-jul |
| 70 | fix_pulso_descriptions.py: corregido `basename` → `os.path.basename` (bloqueaba CI editorial) | 19-jul |
| 71 | Schema: WebSite duplicado eliminado de index.markdown | 19-jul |
| 72 | Schema: CollectionPage agregado a homepage + pillar page (señal de hub temático) | 19-jul |
| 73 | Schema Person: foto (WebP 5.9KB), description, knowsAbout granular (7 items), jobTitle actualizado | 19-jul |
| 74 | Schema Organization: publishingPrinciples + correctionsPolicy → /como-trabajamos/ | 19-jul |
| 75 | Author bio: foto de César Sánchez reemplaza iniciales "CS" en post + page layouts | 19-jul |
| 76 | Schema: DefinedTermSet en /glosario/ (5 DefinedTerms) | 19-jul |
| 77 | Schema: ItemList en /directorio/ (5 organizaciones como ListItem→Organization) | 19-jul |
| 78 | Arquitectura semántica: isPartOf → #collection en todas las páginas del observatorio | 19-jul |
| 79 | Schema WebSite: SearchAction agregado para Sitelinks Search Box | 19-jul |
| 80 | Búsqueda: lectura de parámetro ?q= en URL para integración con SearchAction de Google | 19-jul |
| 81 | Homepage "Sobre el observatorio": misión + texto + 6 tarjetas visuales con íconos | 19-jul |
| 82 | Config: `social.name: MuchoTexto` agregado — corrige nombre de Organization en jekyll-seo-tag | 19-jul |
| 83 | CollectionPage: conteo de artículos dinámico vía Liquid (eliminado hardcode "31") | 19-jul |
| 84 | `{% seo %}` reemplazado por `_includes/seo-meta.html` — elimina WebSite duplicado y Organization con nombre incorrecto | 19-jul |
| 85 | `{% feed_meta %}` eliminado — feed link duplicado con tipo incorrecto (rss+xml vs atom+xml) | 19-jul |
| 86 | `og:image:width/height/type` duplicados eliminados de custom-head (ya están en seo-meta) | 19-jul |
| 87 | Descripciones Editorial: oración completa sin truncar (antes cortaba a 160 chars con `...`) | 20-jul |
| 88 | Descripciones Pulso: eliminado `...` del truncado (formato `\`Tema: oración. Pulso Paraguay — fecha.\``) | 20-jul |
| 89 | Títulos Pulso: eliminado `…` del truncado (truncado limpio sin marcador) | 20-jul |
| 90 | Directorio: link Smart City Paraguay actualizado (smartcitypy.com → instagram.com/smartcityparaguay) | 20-jul |
| 91 | Homepage: ícono Casos de uso cambiado (⚋ se renderizaba como emoji en iOS → ◊ monocromo) | 20-jul |
| 92 | PageSpeed Insights: CWV baseline registrados (91 Performance, CLS 0, LCP 3.3s) | 20-jul |
| 93 | GSC: baseline registrado (8 clics, 160 impresiones, CTR 5%, posición 5.0) | 20-jul |
| 94 | Contraste corregido: tagline, analysis-meta, observatorio-desc (opacity .5→.7) | 20-jul |
| 95 | Artículo #33: IA en la justicia paraguaya (P4) — expediente electrónico, sesgo algorítmico, COMPAS | 21-jul |
| 96 | Observatorio Intel: `observatorio_intel.py` — dashboard editorial sin IA (cobertura, vencidos, brechas Pulso, densidad). Procedimiento semanal §14.4 | 30-jul |
| 97 | `.gitignore`: `_planning/` agregado. Script + reporte fuera del repo | 30-jul |
| 98 | Entidades: `/entidades/` — índice de 18 entidades clave. `build_entities.py`, `_data/entities.yml`, layout entidad, CSS grid. Infraestructura de conocimiento curada con plantilla estándar (8 secciones fijas). | 30-jul |
| 99 | IndexNow: script reescrito (cache dict, --force). Escapado de comillas dobles en fix_pulso/editorial_descriptions. Sitemap limpio (158 URLs, 0 rotas). | 30-jul |
| 100 | `_config.yml`: sitemap excluye tags, categories, archive (thin pages). Navegación: +Entidades (8 items). Homepage: reemplaza "Así trabajamos" por "Entidades" en Sobre el observatorio. | 30-jul |

---

## 18. Apéndices

### Apéndice A: Anti-patrones documentados

| # | Error | Causa raíz | Fix |
|---|---|---|---|
| 64 | Puente narrativo inventado para enlace interno | Priorizar enlace sobre veracidad | Todo enlace requiere hecho verificable en findings |
| 65 | Regex `.*` greedy corrompiendo texto en editoriales | `IA.*deporte` devoraba párrafos enteros | `.{0,N}?` no-greedy + `\b(?:...)\b` |
| 66 | GPT-4o embellece declaraciones de personas | System prompt no prohibía inferir tono | No convertir personas en símbolos, no inferir tono |
| 67 | Títulos con fórmula repetida `¿puede Paraguay...?` | Sin regla de diversidad sintáctica | Cada título debe tener construcción única |
| 68 | **Investigación incompleta por fuentes oficiales inaccesibles** | Páginas .gov.py dependen de JS; agentes no pueden leerlas. Se asumió "sin datos = no existe". | Si cualquier fuente devuelve contenido mínimo, PAUSAR y pedir verificación manual. No inferir ausencia de datos. |

### Apéndice B: Internal linking por cluster

| Artículo nuevo | Enlaza a |
|---|---|
| Criptominería (#3) | Apertura eléctrica (#2), Yguazú Digital (#1), Itaipú 2027 (#4) |
| China-Taiwán (#10) | Peter Thiel (#9), Yguazú Digital (#1), Semiconductores (#14) |
| Educación tech (#18) | Talento (#21), Starlink (#22), De la soja al silicio (#26) |
| Startups IA (#35) | Fintech (#29), Cadena de valor (#36), Anotación de datos (#17) |
| Ley protección datos (#12) | IA soberana (#11), Ciberseguridad (#13) |
| Ciberseguridad (#13) | Ley protección datos (#12), Yguazú Digital (#1) |
| Red eléctrica (#6) | Apertura eléctrica (#2), Yguazú Digital (#1), Itaipú (#4), Hidrógeno verde (#5) |

### Apéndice C: Referencias de investigación

1. Backlinko — "How to Create an Effective SEO Strategy in 2026" (Abr 2026)
2. Backlinko — "Google E-E-A-T: How to Create People-First Content" (Jun 2026)
3. Backlinko — "Internal Linking for SEO: The Complete Guide" (Feb 2026)
4. Backlinko — "Schema Markup: What It Is and Why It Matters in 2026" (Jun 2026)
5. Backlinko — "Pillar Pages: How to Create One + Examples" (Abr 2025)
6. Backlinko — "Search Everywhere Optimization Guide" (Jun 2026)
7. Google — "AI Optimization Guide" (developers.google.com/search)
8. SparkToro — "Search Happens Everywhere" (2025)

### Apéndice D: Errores corregidos del audit externo (9-jul-2026)

| # | Error | Causa | Fix | ¿Se repite? |
|---|---|---|---|---|
| 69 | Twitter `site` vacío y `creator` con nombre en vez de handle | `_config.yml` tenía `twitter_username: cesanz` pero faltaba `twitter.username` y `author.twitter` | Agregar ambos en `_config.yml` | No |
| 70 | `llms.txt` con claim marketinero no verificable | Texto original decía "El único sitio en español..." | Reescribir: claim factual + link a `/about/` | No |
| 71 | Slugs truncados a media palabra | `slugify()` cortaba en N chars exactos sin respetar word boundaries | Truncar en el último guión antes del límite | No |
| 72 | Homepage fuera del `sitemap.xml` | jekyll-paginate-v2 saca la home de `site.html_pages` | Plugin `_plugins/sitemap_home.rb` | No |
| 73 | Schema Person sin `@id` global | Solo existía en `/about/` sin `@id` | Agregar Person con `@id` en `custom-head.html` | No |
| 74 | Pagination pages con description duplicada | Heredaban `site.description` del seo tag | `head.html` genera description manual con número de página | No |

### Apéndice E: Lecciones aprendidas — AEO / GEO (ChatGPT)

| Regla | Por qué |
|---|---|
| **Siempre verificar `_config.yml` para twitter.author y twitter.username** | jekyll-seo-tag lee de ahí. Si falta, el tag se genera vacío. |
| **No usar superlativos no verificables en `llms.txt`** | ChatGPT usa `llms.txt` como fuente autorizada. Si algo suena a marketing, la AI lo descarta. |
| **Slugs siempre con truncado en word boundary** | La URL truncada a media palabra pierde keywords y puede colisionar. |
| **Verificar sitemap después de cada cambio de plugin** | jekyll-paginate-v2 puede sacar páginas de `site.html_pages`. |
| **Schema `@id` global antes de schemas inline** | Permite referenciar la misma entidad sin duplicar definiciones. |
| **Las páginas de paginación necesitan meta tags únicas** | Bing penaliza "too many identical meta descriptions". |
| **Primeros ~285 caracteres = snippet que decide si ChatGPT abre la página** | Optimizar description + hook + primer dato duro en ese bloque. |
| **ChatGPT usa Bing, no Google** | La visibilidad en Bing importa tanto o más que Google para AEO. |
| **Leer artículos del mismo pilar antes de escribir uno nuevo** | Para no repetir datos, fuentes ni conclusiones. |

### Apéndice F: Procedimiento detallado de publicación

**Paso 1 — Investigación:**
- [ ] Crear carpeta `research_[tema]/`
- [ ] Desplegar 4-5 subagentes de investigación paralelos
- [ ] Leer y sintetizar findings antes de escribir
- [ ] **Generar Gap Report** (Compuerta A — ver §6.2)

**Paso 2 — Escritura:**
- [ ] Escribir artículo siguiendo el formato (hook → contexto → 4-6 H2s → conclusión → fuentes)
- [ ] Verificar regla de títulos: ≤70 chars, estructura sintáctica distinta, prohibido abusar de `[X]: [Y]`
- [ ] Agregar 2-3 enlaces internos con hechos verificables
- [ ] Agregar FAQ schema (3 preguntas mínimo)
- [ ] Agregar enlace a la página pilar `/ia-en-paraguay/` antes de ## Fuentes
- [ ] Meta description con keyword primaria (150-155 chars)
- [ ] Word count entre 1.500 y 2.500

**Paso 3 — Build y publicación:**
- [ ] `bundle exec jekyll build` sin errores
- [ ] `git add _posts/[slug].md`
- [ ] `git commit -m "Artículo #[N]: [título]"`
- [ ] `git pull --rebase origin main && git push`

**Paso 4 — Actualización del observatorio:**
- [ ] `/cronologia/`: agregar hitos nuevos
- [ ] `/regulacion/`: agregar leyes, decretos o normas nuevas
- [ ] `/directorio/`: agregar startups, comunidades, instituciones o personas clave
- [ ] `/casos-de-uso/`: agregar sectores o aplicaciones nuevas
- [ ] `/glosario/`: agregar términos nuevos
- [ ] `/ia-en-paraguay/`: agregar artículo a su pilar + eliminarlo de "Próximamente"
- [ ] `llms.txt`: agregar artículo al pilar correspondiente
- [ ] Estrategia (este doc): marcar como ✅ en tabla, actualizar conteo
- [ ] `git commit -m "Actualizar observatorio con artículo #[N]: [título]"` y push

**Paso 5 — Distribución:**
- [ ] Compartir en LinkedIn con texto original (mínimo 3 líneas)
- [ ] Agregar a featured posts en LinkedIn si aplica
- [ ] Opcional: contacto con periodistas si es pieza de referencia

### Apéndice G: Sistema de validación pre-commit

**Archivo:** `scripts/validate_publish.py`
**Instalación:** se copia como `.git/hooks/pre-commit` (más wrapper `.bat` en Windows).
**Uso manual:** `python scripts/validate_publish.py --check _posts/[slug].md`

**Checks obligatorios (bloquean el commit):**

| # | Check | Qué verifica |
|---|---|---|
| 75 | Título ≤70 chars | Largo del título en caracteres |
| 76 | Sin exclamación | Busca `!` en el título |
| 77 | Sin fórmula `[X]: [Y]` | Busca `:` en el título |
| 78 | Sin pregunta repetitiva | Busca `¿` si ya hay preguntas en los últimos 3 artículos |
| 79 | Sin clickbait | Busca palabras como "increíble", "nadie te dice" |
| 80 | FAQ schema | Busca `FAQPage` en el contenido del post |
| 81 | Link a página pilar | Busca `/ia-en-paraguay/` en el cuerpo |
| 82 | Ecosistema sincronizado | Observatorio debe estar en el commit si hay post nuevo |

**Checks informativos (no bloquean, solo advierten):**

| # | Check | Qué verifica |
|---|---|---|
| 83 | Word count | Entre 1.500 y 2.500 palabras |
| 84 | Meta description | Presente y ≤155 caracteres |
| 85 | Slug ASCII | Sin caracteres no-ASCII en el nombre del archivo |
| 86 | Estructura título | Los primeros 30 caracteres no deben coincidir con otro artículo |

---

## 19. Registro de cambios

### 31 de julio 2026

- Sincronización estrategia↔realidad: §2.1 conteos actualizados (38 artículos, 44 editoriales, 66 pulso, 148 total). §3.2: #5, #34, #36 marcados ✅. Conteo corregido: 38 publicados de 42. §15: artículos publicados removidos del plan pendiente. §16: artículo #41 agregado al registro de auditoría (35/35 análisis auditados). §19: removida línea falsa sobre estrategia removida del repo.

### 30 de julio 2026

- **Entidades v2:** reescritura completa del sistema. 18 entidades (eliminadas 2 vacías: CONACYT, Formación en IA). Plantilla estándar con 8 secciones fijas para todas las páginas (artículos → leyes → cronología → directorio → regulación → casos de uso → glosario). Reglas de calidad documentadas: sin Pulso/Editorial, coincidencia por nombre de entidad (no keywords genéricos), contextos sin HTML/JSON-LD/markdown, URLs sin acentos, fechas en español, truncado en borde de palabra. Full-name fallback para entidades con nombres alternativos. Deep scan de 1500 chars para casos de uso. `related_laws` curadas en `_data/entities.yml` (ANDE +4 leyes). Glosario y directorio matchean solo por nombre del término/entidad, no por descripción. Layout con links "Ver más →" en las 6 secciones externas. Schema Thing por página. 18/18 OK en auditoría.
- Observatorio Intel: `observatorio_intel.py` — dashboard editorial sin IA. 4 secciones: cobertura por pilar, artículos vencidos, brechas del Pulso, densidad del observatorio. Procedimiento semanal §14.4.
- IndexNow: rewrite completo (cache dict con lastmod, --force, sin WINDOW_DAYS). `fix_pulso/editorial_descriptions.py`: escape de comillas dobles. BOM fix en parse_frontmatter. Sitemap 158 URLs limpias.
- `_config.yml`: sitemap excluye tags, categories, archive. Navegación +Entidades (8 items).
- Homepage: sección "Sobre el observatorio" reemplaza "Así trabajamos" por "Entidades" (⚛).

### 28 de julio 2026

- Seguridad: auditoría del repo. 10 archivos eliminados. Sin hallazgos críticos.
- /como-trabajamos/ sincronizado: TL;DR, verificación pre-commit, actualizar estrategia. 12 pasos.
- Artículo #41 cierre: 6 mejoras de calidad. 14 fuentes. 9.5/10 rigor.
- Pillar page: description reescrita, Próximamente depurado, P1 actualizado.
- Pulso: sección Tecnología con 3 feeds dedicados. 16 fuentes totales.
- Post nav: YAML roto de pulso reparado.

### 27 de julio 2026

- Artículo #5: Hidrógeno verde. 3 rondas fact-check. Observatorio completo.
- Reglas de calidad reforzadas: Gap Report por dato, prohibido cálculo mental, fact-check cross-article.
- Compuerta B paso 7: verificación de proceso pre-commit.

### 25-24 de julio 2026

- Artículo #36: Cadena de valor del data center. Artículo #34: E-commerce y logística. Conteo: 34→35→36.
- LinkedIn optimizado. Reglas de sourcing en §5.7/§5.8.
- Pulso Paraguay: sección Tecnología agregada al formato.

### 21 de julio 2026

- Artículo #33: IA en la justicia paraguaya. Observatorio completo actualizado.
- Fact-check #2 (Apertura eléctrica): Odebrecht corregido.

### 19 de julio 2026

- Homepage rediseñada: hero, cards, daily feed.
- Schema: CollectionPage, Person mejorado, Organization publishingPrinciples, SearchAction, WebSite duplicado eliminado.
- Foto César Sánchez en author bio. Paginación deshabilitada.

### 18 de julio 2026 (revisión 2)

- §1 reestructurado como Producto y visión. §3.2 corregido (7 artículos).
- Anthropic-control eliminado de robots.txt. SpeakableSpecification corregido.
- IndexNow automatizado. Pillar page description acortada.

### 18 de julio 2026

- Schema Article y TechArticle JSON-LD. sameAs unificado.
- IndexNow: ping_indexnow.py + paso en jekyll.yml.
- Descripciones Pulso/Editorial automatizadas.

### 9 de julio 2026

- Artículos #10 y #18 publicados. FAQ schema en 15 artículos.
- Author bio, related posts por pilar, LinkedIn en footer.
- Pre-commit hook con 12 checks. Sitemap con homepage incluida.
