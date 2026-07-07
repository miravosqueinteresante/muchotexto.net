# Estrategia SEO Unificada — muchotexto.net

> **Documento vivo.** Se actualiza a medida que se implementan las estrategias, se publican artículos o surgen nuevos hallazgos.
> Última actualización: 7 de julio de 2026.
>
> ### Progreso — Fase 1 (Fundación)
>
> | Acción | Estado |
> |---|---|
> | Consolidar taxonomía de tags (43 → 8 paraguas) | ✅ 7-jul |
> | Schema Person en `/about/` | ✅ 7-jul |
> | Crear página pilar `/ia-en-paraguay/` | ✅ 7-jul |
> | Agregar navegación "IA en Paraguay" | ✅ 7-jul |
> | Actualizar description en `_config.yml` | ✅ 7-jul |
> | Actualizar `llms.txt` con nuevo enfoque | ✅ 7-jul |
> | Medir Core Web Vitals baseline | ❌ |
> | Correr squirrelscan post-cambios | ❌ |

---

## 1. Objetivo y visión

Posicionar **muchotexto.net** como el referente en español sobre inteligencia artificial en Paraguay. El espacio está vacío: nadie en el mundo hispanohablante escribe análisis profundos de IA desde Paraguay.

| Competidor | Qué hace | Qué NO hace |
|---|---|---|
| ABC Color, Última Hora, La Nación | Cubren la noticia del día | Análisis de 2.000 palabras con fuentes verificadas |
| Wired, MIT Tech Review, Rest of World | Cubren IA global | No cubren Paraguay con profundidad |
| Blogs de IA en español | Tutoriales de prompts y herramientas | No hablan de política energética paraguaya ni geopolítica de chips |

**Ventaja competitiva:** único sitio que cruza `IA + Paraguay + datos duros + fuentes verificables + 1.500+ palabras por artículo`.

**Diferenciador clave (information gain):** experiencia real de César en anotación de datos, bots con IA, consultoría SEO, y análisis de la reforma energética paraguaya. Esto es *non-commodity content* — nadie más puede replicarlo.

### Paso a seguir — validar posicionamiento
- [ ] Verificar en Search Console las impresiones actuales para `inteligencia artificial Paraguay` y variantes
- [ ] Identificar qué artículos ya rankean para términos relacionados con IA+Paraguay

---

## 2. Diagnóstico actual

### Estado del sitio (julio 2026)

| Métrica | Valor |
|---|---|
| Artículos long-form publicados | 13 |
| Editoriales | 9 |
| Pulso Paraguay | 37 |
| **Total posts** | **59** |
| SEO Score (squirrelscan) | 80/100 (Grado B) |

### Hallazgos del análisis de junio 2026

| Hallazgo | Implicancia SEO |
|---|---|
| 75% de los artículos long form tocan IA/tecnología | Pilar de contenido más fuerte — construir sobre esto |
| Paraguay es "protagonista" en 50% de esos artículos | Ángulo diferencial: cobertura local especializada |
| 25 tags únicos usados en solo 4 artículos | Taxonomía fragmentada — sin topic cluster claro |
| Editoriales mencionan IA en solo 20% de los casos | Oportunidad de subir esa proporción |
| Fuentes más citadas: ABC Color, La Nación, HOY, NPY | Estos medios son objetivo de backlink/mención |
| Sentimiento long form: mixto con sesgo positivo (+0.20) | El contenido de IA puede ser el ángulo constructivo del sitio |

### Mejoras SEO ya implementadas

- JSON-LD BlogPosting + BreadcrumbList + Organization publisher
- Twitter card `summary_large_image` + og:image 1200x630
- `last_modified_at` en todos los posts
- `description` en los 59 posts
- Internal linking: 13 artículos long-form entrelazados por cluster
- Editorial auto-linking: 11 patrones regex con detección temática
- CSS asíncrono + preconnect + GA4 con Consent Mode v2
- Google Search Console + Bing Webmaster Tools verificados
- llms.txt para AI crawlers
- Páginas legales: privacidad + términos
- 404 en español + heading hierarchy corregido

### Pendientes SEO

| Pendiente | Impacto | Bloqueante |
|---|---|---|
| HSTS header | Medio | Requiere Cloudflare |
| Thin content en home y /contacto/ | Bajo | No urgente |
| Consolidar taxonomía de tags (25 → 8-10) | Alto | **Sí — acción inmediata** |
| Schema Person en /about/ | Alto | **Sí — acción inmediata** |
| Página pilar del cluster IA+Paraguay | Alto | **Sí — acción inmediata** |

### Pasos a seguir — diagnóstico
- [ ] Consolidar los 25 tags actuales en 8-10 tags "paraguas" alineados a los 5 pilares (sección 3)
- [ ] Agregar schema `Person` en `/about/` con `sameAs` a LinkedIn, GitHub, Twitter
- [ ] Medir Core Web Vitals actuales en PageSpeed Insights y anotar baseline
- [ ] Verificar indexación en GSC: `site:muchotexto.net` y Coverage report

---

## 3. Arquitectura de contenido

### Modelo: Pillar Page + Topic Clusters

```
Página Pilar: "Inteligencia Artificial en Paraguay: Guía Completa 2026"
  ├── Pilar 1: Infraestructura y energía (8 temas)
  ├── Pilar 2: Geopolítica y regulación tech (8 temas)
  ├── Pilar 3: IA, sociedad y trabajo (10 temas)
  ├── Pilar 4: Tecnología aplicada + ecosistema (10 temas)
  └── Pilar 5: Cultura, filosofía y futuro (6 temas)
```

**Regla de interlinking:** todos los artículos enlazan hacia la página pilar, la página pilar enlaza hacia cada uno. Cada Pulso Paraguay diario que toque IA debe enlazar de vuelta al cluster.

### Los 5 pilares y sus 42 temas

**Leyenda:** ✅ Publicado | ❌ Pendiente | 🆕 Nuevo (junio-julio 2026)

#### Pilar 1: Infraestructura y energía (8 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 1 | ✅ | Yguazú Digital: ¿puede Paraguay convertirse en el hub de IA más grande del mundo? | `Yguazú Digital Paraguay Taiwán`, `centro IA Paraguay` |
| 2 | ✅ | Luces y sombras de la apertura eléctrica: cuando Paraguay decide dejar entrar al sector privado | `apertura eléctrica Paraguay`, `Ley 7599`, `ANDE energía` |
| 3 | ❌ | Criptominería en Paraguay: el lado oscuro de la energía barata | `criptominería Paraguay ANDE`, `bitcoin Paraguay energía` |
| 4 | ❌ | Itaipú 2027: ¿qué pasa con la energía paraguaya cuando se renegocie el tratado? | `Itaipú renegociación 2027`, `energía Paraguay futuro` |
| 5 | ❌ | Hidrógeno verde: ¿la próxima frontera energética de Paraguay? | `hidrógeno verde Paraguay`, `transición energética` |
| 6 | ❌ | La red eléctrica de Paraguay frente a la demanda de la IA global | `ANDE capacidad transmisión`, `red eléctrica Paraguay IA` |
| 7 | ❌ | Energía renovable y cambio climático: la paradoja paraguaya | `Paraguay energía renovable`, `cambio climático hidroeléctrica` |
| 8 | 🆕 | El efecto derrame: ¿qué pasa en una ciudad paraguaya cuando llega un data center de $200M? | `data center impacto local Paraguay`, `empleo tecnología Paraguay` |

#### Pilar 2: Geopolítica y regulación tech (8 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 9 | ✅ | El experimento paraguayo de Peter Thiel | `Peter Thiel Paraguay Palantir`, `vigilancia IA` |
| 10 | ❌ | Paraguay entre China y Taiwán: el último aliado sudamericano en la guerra fría tecnológica | `Paraguay China Taiwán`, `geopolítica chips` |
| 11 | ❌ | IA soberana: ¿qué significa y por qué Paraguay la necesita? | `IA soberana Paraguay`, `soberanía digital` |
| 12 | ❌ | Ley de protección de datos en Paraguay: ¿llega a tiempo para la era de la IA? | `ley protección datos Paraguay`, `privacidad digital` |
| 13 | ❌ | Ciberseguridad en Paraguay: ¿estamos preparados para un data center de $40B? | `ciberseguridad Paraguay`, `CERT-PY`, `data center seguridad` |
| 14 | ❌ | Semiconductores: por qué Taiwán eligió Paraguay | `semiconductores Taiwán Paraguay`, `TSMC`, `cadena chips` |
| 15 | ❌ | El modelo Itaipú aplicado a la IA: ¿puede funcionar dos veces? | `entidad binacional Paraguay Taiwán`, `gobernanza IA` |
| 16 | ❌ | Silicon Valley en el Cono Sur: ¿por qué los billonarios miran a Paraguay? | `inversión tech Paraguay`, `Crusoe AI`, `X8Cloud` |

#### Pilar 3: IA, sociedad y trabajo (10 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 17 | ✅ | Anotación de datos para IA: la ventaja silenciosa de Paraguay | `anotación datos IA Paraguay`, `trabajo digital Paraguay` |
| 18 | ❌ | Educación tech en Paraguay: la brecha que frena el hub de IA | `educación tecnología Paraguay`, `ingenieros Paraguay IA` |
| 19 | ✅ | Bienvenidos a muchotexto.net | `muchotexto.net` |
| 20 | ✅ | El futuro de la identidad y la conciencia | `identidad digital`, `filosofía tecnología` |
| 21 | ❌ | Talento tech: ¿cuántos ingenieros necesita Paraguay para ser un hub de IA? | `talento tech Paraguay`, `fuga de cerebros` |
| 22 | ❌ | Starlink en Paraguay: ¿conectividad para todos o espejismo digital? | `Starlink Paraguay`, `conectividad rural` |
| 23 | ❌ | Gobierno digital: ¿qué hizo Paraguay y qué falta? | `gobierno digital Paraguay`, `MITIC`, `Agenda Digital` |
| 24 | ❌ | IA y salud en Paraguay: del IPS a los algoritmos de diagnóstico | `IA salud Paraguay`, `IPS tecnología médica` |
| 25 | ❌ | ¿Puede la IA reducir la corrupción en Paraguay? | `IA corrupción`, `transparencia algorítmica Paraguay` |
| 26 | 🆕 | De la soja al silicio: el plan de Paraguay para cambiar su matriz exportadora | `matriz exportadora Paraguay`, `diversificación económica IA` |

#### Pilar 4: Tecnología aplicada + ecosistema (10 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 27 | ✅ | Soja, ganado y blockchain: la apuesta paraguaya por la tokenización del agro | `tokenización agro Paraguay`, `blockchain Paraguay` |
| 28 | ❌ | Agro 4.0: cómo la IA está transformando el campo paraguayo | `agro IA Paraguay`, `agricultura precisión`, `drones` |
| 29 | ❌ | Fintech en Paraguay: ¿el próximo hub financiero de LatAm? | `fintech Paraguay`, `pagarés digitales`, `inclusión financiera` |
| 30 | ✅ | La IA no es neutral: lo que dice la primera encíclica del Papa León XIV | `encíclica IA Papa León XIV`, `ética inteligencia artificial` |
| 31 | ❌ | IA y periodismo en Paraguay: ¿quién escribe las noticias del futuro? | `IA periodismo Paraguay`, `deepfakes`, `verificación` |
| 32 | ❌ | Smart cities en Paraguay: ¿Asunción puede ser una ciudad inteligente? | `smart city Asunción`, `ciudad inteligente Paraguay` |
| 33 | ❌ | IA en la justicia paraguaya: ¿algoritmos imparciales o sesgo digital? | `IA justicia Paraguay`, `expediente electrónico` |
| 34 | ❌ | E-commerce y logística: la transformación silenciosa del comercio paraguayo | `ecommerce Paraguay`, `logística IA` |
| 35 | 🆕 | Startups paraguayas de IA: quiénes son y por qué nadie habla de ellas | `startups IA Paraguay`, `ecosistema emprendedor tech` |
| 36 | 🆕 | La cadena de valor invisible: todos los negocios que rodean a un centro de datos | `cadena valor data center`, `negocios IA Paraguay` |

#### Pilar 5: Cultura, filosofía y futuro (6 temas)

| # | Estado | Tema | Keywords primarias |
|---|---|---|---|
| 37 | ✅ | 5 tecnologías que prometieron cambiar todo pero no cambiaron nada | `tecnologías fracasadas`, `hype tecnológico` |
| 38 | ✅ | ¿Qué es realmente el fútbol? | `fútbol filosofía`, `identidad fútbol` |
| 39 | ✅ | La IA cuesta más que los humanos que reemplazó: lo que dicen los números | `burbuja IA 2026`, `costos inteligencia artificial` |
| 40 | ✅ | El laboratorio americano: cómo Estados Unidos está usando IA para reinventar su fútbol | `USA fútbol IA Mundial 2026`, `Sportian Globant` |
| 41 | ❌ | Guaraní e IA: ¿puede una lengua indígena sobrevivir en la era de los algoritmos? | `guaraní inteligencia artificial`, `NLP lenguas indígenas` |
| 42 | ❌ | Paraguay 2040: un país construido con datos | `Paraguay futuro tecnología`, `prospectiva digital` |

**Total: 42 temas. 13 publicados. 29 pendientes.** A 2 artículos por semana = ~15 semanas de contenido.

### Paso a seguir — arquitectura
- [ ] Crear page `/ia-en-paraguay/` como página pilar del cluster (ver sección 6.2 para specs)
- [ ] Consolidar tags: mapear los 25 actuales → 8-10 alineados a los 5 pilares
- [ ] Agregar en cada artículo existente un enlace a la página pilar

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
| 8 | `criptominería Paraguay ANDE energía` | #3 | ❌ |
| 9 | `Paraguay Taiwán China geopolitica IA` | #10 | ❌ |
| 10 | `Santiago Peña inteligencia artificial Taiwán` | #1 | ✅ |
| 11 | `Globant Sportian IA fútbol Pochettino` | #40 | ✅ |
| 12 | `Paraguay hub tecnológico América Latina` | #1 | ✅ |
| 13 | `ley protección datos Paraguay` | #12 | ❌ |

### Paso a seguir — keywords
- [ ] Verificar en GSC el ranking actual de cada long-tail publicada
- [ ] Para keywords en posiciones 4-15: priorizar actualización del artículo antes que crear uno nuevo
- [ ] Identificar nuevas oportunidades long-tail desde "People Also Ask" de Google y Reddit en español

---

## 5. Metodología de artículos long-form

### 5.1 Formato estándar

```
1. Hook (sin encabezado, 2-3 oraciones)
   → Afirmación fuerte, pregunta provocadora o dato impactante.
   → PROHIBIDO empezar con fechas o "Hoy...".

2. Contexto (sin encabezado, 1-2 párrafos)
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
- [ ] Verificar que el tema no esté cubierto por otro artículo del plan

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
- [ ] Schema BlogPosting válido
- [ ] Tags alineados con otros artículos del mismo pilar

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

### Paso a seguir — metodología
- [ ] Crear template de `research_plan.md` reutilizable
- [ ] Revisar artículos publicados que no pasaron por este proceso y evaluar si necesitan actualización

---

## 6. SEO técnico

### 6.1 Implementado (no tocar)

Ver sección 2. Lo crítico ya está: JSON-LD, sitemap, robots.txt, GA4, GSC, speed, heading hierarchy, internal linking.

### 6.2 Acciones técnicas prioritarias

#### A. Consolidar taxonomía de tags (prioridad: urgente)

**Problema:** 25 tags sueltos fragmentan la señal de topical authority.

**Plan de consolidación (25 tags actuales → 8 tags paraguas):**

| Tag paraguas | Tags actuales que absorbe | Pilar asociado |
|---|---|---|
| `ia-paraguay` | ia, paraguay, inteligencia-artificial, tecnologia | Todos |
| `infraestructura-energia` | energia, data-center, yguazu-digital, ANDE | Pilar 1 |
| `geopolitica-regulacion` | geopolitica, taiwan, china, regulacion | Pilar 2 |
| `sociedad-trabajo` | educacion, trabajo-digital, gobierno-digital | Pilar 3 |
| `tech-ecosistema` | blockchain, fintech, startups, agro | Pilar 4 |
| `cultura-filosofia` | filosofia, etica, futbol, cultura | Pilar 5 |
| `analisis-ia` | analisis, burbuja-ia, costos-ia | Todos |
| `paraguay-futuro` | desarrollo, soberania, prospectiva | Pilar 2, 3 |

**Pasos:**
- [x] Auditar los 59 posts y mapear cada uno a los tags paraguas
- [x] Actualizar el frontmatter `tags:` en cada post (25/07/2026)
- [x] Verificar build de Jekyll sin errores
- [ ] Verificar que las páginas `/tags/` se regeneren correctamente

#### B. Crear página pilar `/ia-en-paraguay/` (prioridad: urgente)

**Especificaciones:**
- Layout: `page` (no post)
- Título: "Inteligencia Artificial en Paraguay: Guía Completa 2026"
- `last_modified_at` en frontmatter (se actualiza con cada nuevo artículo del cluster)
- `description`: 150-155 chars con keywords `inteligencia artificial Paraguay`, `IA en Paraguay`
- Schema: `Article` con `about: "Inteligencia Artificial en Paraguay"`
- Contenido: resumen ejecutivo de cada pilar + lista de artículos del cluster + enlace a cada uno
- Extensión: 800-1200 palabras (no compite con los artículos individuales)

**Pasos:**
- [x] Crear `ia-en-paraguay.markdown` en raíz del proyecto
- [x] Escribir contenido: introducción + una sección por pilar + lista de artículos
- [x] Incluir en navegación (`_data/navigation.yml`)
- [x] Verificar schema Article en HTML renderizado

#### C. Schema Person en /about/ (prioridad: urgente)

Agregar JSON-LD `Person` en `about.markdown`:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Cesar Sanchez",
  "jobTitle": "Analista de IA y Tecnologia",
  "url": "https://muchotexto.net/about/",
  "sameAs": [
    "https://www.linkedin.com/in/cesar-sanchez-melgarejo/",
    "https://github.com/miravosqueinteresante",
    "https://twitter.com/cesanz"
  ],
  "knowsAbout": [
    "Inteligencia Artificial",
    "Anotacion de Datos",
    "Tecnologia en Paraguay",
    "SEO"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "MuchoTexto"
  }
}
```

**Pasos:**
- [x] Verificar/actualizar URLs de `sameAs` con los perfiles reales
- [x] Agregar el bloque JSON-LD en `about.markdown`
- [x] Verificar renderizado en `_site/about/index.html`
- [ ] Validar en https://validator.schema.org

#### D. Versión en inglés selectiva (prioridad: baja)

Solo para piezas con interés internacional real (Yguazú Digital, geopolítica). Usar prefijo `/en/` en slug.

**Pasos:**
- [ ] Identificar 2-3 artículos con mayor potencial internacional
- [ ] Traducir (no duplicar) y publicar bajo `/en/[slug]/`
- [ ] Agregar hreflang en ambas versiones

### 6.3 Pendientes no críticos

| Pendiente | Plan |
|---|---|
| HSTS header | Cuando se migre a Cloudflare |
| Thin content en home | Agregar snippet descriptivo debajo de cada post en homepage |
| Thin content en /contacto/ | Agregar 100-150 palabras de contenido introductorio |

### Paso a seguir — SEO técnico
- [ ] Ejecutar consolidación de tags (acción A)
- [ ] Crear página pilar (acción B)
- [ ] Agregar schema Person (acción C)
- [ ] Correr squirrelscan post-cambios para verificar mejora del score

---

## 7. E-E-A-T y autoridad

### 7.1 Information gain como diferenciador

En 2026, Google prioriza el *non-commodity content* — contenido que aporta algo que no existe en ningún otro lado. La combinación `IA + Paraguay + experiencia real` es el *information gain* de muchotexto.net.

**Tácticas:**
- Escribir desde la experiencia de primera mano (anotación de datos, bots con IA, reforma energética)
- Mostrar screenshots reales, datos propios, proyectos documentados
- No rehacer contenido que ya existe — siempre aportar un ángulo nuevo

### 7.2 Author authority

- **Página /about/ con schema Person** — credenciales verificables, links a redes
- **E-E-A-T real** — trayectoria concreta (anotación de datos, proyectos con Ollama/Groq, consultoría SEO), no un "sobre mí" genérico
- **Entity SEO** — mencionar consistentemente términos relacionados: "inteligencia artificial", "Paraguay", "machine learning", "automatización", "Latinoamérica"

### 7.3 Construir autoridad off-site

| Canal | Acción | Frecuencia |
|---|---|---|
| LinkedIn | Compartir cada artículo nuevo + reflexión personal de 3-5 líneas | Cada publicación |
| Twitter/X (@cesanz) | Amplificar cada pieza nueva del cluster | Cada publicación |
| Reddit (r/Paraguay, r/devsarg) | Responder preguntas, compartir artículos cuando sean relevantes | Semanal |
| Guest posts | Escribir en blogs tech de Latinoamérica | 1 cada 2 meses |
| Podcasts | Participar como invitado en podcasts de tecnología | Según oportunidad |
| Medios paraguayos | Contactar periodistas de tecnología de ABC, La Nación, HOY, NPY ofreciendo artículos como fuente citable | Según publicación relevante |

### Paso a seguir — autoridad
- [ ] Crear/optimizar perfil de LinkedIn con keywords del nicho
- [ ] Preparar un "media kit" de una página: quién es César, qué cubre, por qué es fuente autorizada en IA+Paraguay
- [ ] Identificar 3 periodistas de tecnología en medios paraguayos para contactar

---

## 8. Google 2026: directrices y tendencias

### 8.1 Search Everywhere Optimization

En 2026, el SEO ya no es solo Google. Las personas buscan en TikTok, YouTube, Reddit, ChatGPT y más. **El contenido debe estar donde la audiencia busca.**

**Para muchotexto.net:**
- Publicar en el sitio (Google) → fuente canónica
- Compartir en LinkedIn y Twitter/X → distribución social
- Responder en Reddit → capturar búsquedas informacionales
- Estar en ChatGPT/Perplexity → vía llms.txt + E-E-A-T

### 8.2 Information gain sobre todo

Google llama *non-commodity content* al contenido que aporta información única. Es el factor individual con más probabilidad de generar visibilidad en AI search. **La experiencia de primera mano en el ecosistema tech paraguayo es imposible de replicar por AI.**

### 8.3 AI Overviews y schema

- Schema **NO** es un lever directo para AI citations, pero es señal de un sitio bien construido
- Los sitios con buena E-E-A-T son citados en AI Overviews independientemente del schema
- Lo que importa: contenido que responde preguntas reales con autoridad demostrable

### 8.4 Core Web Vitals (sin cambios mayores)

- LCP < 2.5s, INP < 200ms, CLS < 0.1
- Jekyll estático ya tiene ventaja — mantener CSS asíncrono y optimizar imágenes

### 8.5 Helpful Content System

- Contenido *people-first*: escrito para personas, no para search engines
- Evitar contenido generado masivamente sin valor agregado
- Actualizar contenido regularmente (frescura)

### Paso a seguir — Google 2026
- [ ] Auditar los artículos existentes: ¿cada uno aporta information gain o rehace contenido que ya existe?
- [ ] Verificar que llms.txt esté actualizado con todos los artículos del cluster
- [ ] Medir Core Web Vitals baseline y documentar

---

## 9. Distribución y link building

### 9.1 Estrategia de backlinks

**Objetivo:** backlinks desde medios paraguayos establecidos (ABC Color, La Nación, HOY, NPY). Estos medios ya cubren Yguazú Digital y temas de IA constantemente.

**Táctica:** al publicar piezas de referencia (explainers, comparativos regionales), contactar periodistas de tecnología ofreciendo la pieza como fuente de contexto citable.

**Piezas con mayor potencial de backlink:**
1. Yguazú Digital a fondo (#1) — ya publicado, actualizar y promover
2. Paraguay vs. la región (#5 del banco original) — inédito, alto potencial
3. Ley de Protección de Datos (#12) — inédito, coyuntura legislativa
4. El costo energético real de la IA (#6) — inédito, datos duros

### 9.2 Distribución en redes

| Plataforma | Formato | Contenido |
|---|---|---|
| Twitter/X | Hilo de 5-7 tweets | Resumen del artículo + dato más impactante + link |
| LinkedIn | Post de 3-5 párrafos | Reflexión personal + gancho + link |
| Reddit | Respuesta a preguntas | Aportar valor primero, link solo si es relevante |
| GitHub | README/proyecto | Si el artículo documenta un proyecto técnico |

### 9.3 Reutilización cruzada

- Editoriales que toquen IA (actualmente solo 20%): subir la frecuencia aprovechando la coyuntura
- Cada Pulso Paraguay que mencione IA debe enlazar a la página pilar
- En vez de multiplicar artículos casi idénticos sobre Yguazú Digital, actualizar el explainer central

### Paso a seguir — distribución
- [ ] Crear cuenta/blog en LinkedIn para publicar versiones resumidas de los artículos
- [ ] Preparar un post de LinkedIn anunciando el cluster IA+Paraguay
- [ ] Identificar 5 periodistas de tecnología en Paraguay y seguir su trabajo

---

## 10. Calendario editorial

### Ritmo: 2 artículos long-form por semana (~15 semanas de autonomía)

### Priorización por fases

#### Fase 1: Fundación (semanas 1-2, julio 2026) — ~~EN PROGRESO~~

| Acción | Tipo | Estado |
|---|---|---|
| Consolidar taxonomía de tags (25 → 8) | Técnico | ✅ |
| Crear página pilar `/ia-en-paraguay/` | Contenido | ✅ |
| Agregar schema Person en /about/ | Técnico | ✅ |
| Medir Core Web Vitals baseline | Técnico | ❌ |
| Actualizar posts existentes con enlace a la página pilar | Mantenimiento | ❌ |

#### Fase 2: Contenido prioritario (semanas 3-8)

| Semana | Artículo | Pilar | Keywords |
|---|---|---|---|
| 3 | #12 — Ley de protección de datos en Paraguay | Pilar 2 | `ley protección datos Paraguay` |
| 4 | #3 — Criptominería en Paraguay | Pilar 1 | `criptominería Paraguay ANDE` |
| 5 | #6 — La red eléctrica de Paraguay frente a la demanda de la IA global | Pilar 1 | `ANDE capacidad transmisión` |
| 6 | #10 — Paraguay entre China y Taiwán | Pilar 2 | `Paraguay China Taiwán geopolítica` |
| 7 | #18 — Educación tech en Paraguay | Pilar 3 | `educación tecnología Paraguay` |
| 8 | #21 — Talento tech: ¿cuántos ingenieros necesita Paraguay? | Pilar 3 | `talento tech Paraguay` |

#### Fase 3: Expansión (semanas 9-15)

| Semana | Artículo | Pilar |
|---|---|---|
| 9 | #14 — Semiconductores: por qué Taiwán eligió Paraguay | Pilar 2 |
| 10 | #29 — Fintech en Paraguay | Pilar 4 |
| 11 | #28 — Agro 4.0: IA en el campo paraguayo | Pilar 4 |
| 12 | #35 — Startups paraguayas de IA | Pilar 4 |
| 13 | #41 — Guaraní e IA | Pilar 5 |
| 14 | #22 — Starlink en Paraguay | Pilar 3 |
| 15 | #11 — IA soberana | Pilar 2 |

#### Fase 4: Profundización (semanas 16+)

Temas restantes de los pilares + actualización de piezas evergreen (Yguazú Digital, página pilar).

### Paso a seguir — calendario
- [ ] Crear un project board (GitHub Projects o similar) con los 29 temas pendientes
- [ ] Asignar prioridad alta/media/baja según las fases definidas
- [ ] Marcar como completado cada tema al publicarse

---

## 11. KPIs y medición

### KPIs primarios (Google Search Console)

| KPI | Baseline (julio 2026) | Meta 3 meses | Meta 6 meses |
|---|---|---|---|
| Impresiones para `inteligencia artificial Paraguay` | [Medir] | +50% | +100% |
| CTR promedio del sitio | [Medir] | +10% | +20% |
| Posición promedio para keywords del cluster | [Medir] | Mejora en 30% de términos | Mejora en 60% de términos |
| Clics totales desde Google | [Medir] | +30% | +100% |

### KPIs secundarios

| KPI | Herramienta | Frecuencia |
|---|---|---|
| Tráfico orgánico a la página pilar | GA4 | Mensual |
| Backlinks nuevos desde medios paraguayos | GSC → Links | Mensual |
| Proporción de editoriales que mencionan IA | Conteo manual | Mensual |
| Core Web Vitals (LCP, INP, CLS) | PageSpeed Insights | Trimestral |
| SEO Score general | squirrelscan | Mensual |

### Paso a seguir — KPIs
- [ ] Medir y documentar todos los baselines en GSC
- [ ] Crear un dashboard simple (Google Sheets) con los KPIs y actualizarlo mensualmente
- [ ] Programar recordatorio mensual para revisar KPIs

---

## 12. Mantenimiento del documento

Este documento se actualiza cada vez que:

- Se publica un artículo del plan (marcar ✅ en la tabla de temas)
- Se completa una acción de las listas de "Pasos a seguir"
- Hay novedades relevantes sobre Yguazú Digital u otros proyectos de IA en Paraguay
- Se ejecuta un análisis mensual de contenidos
- Cambian las prioridades o surge un nuevo tema
- Google anuncia un cambio de algoritmo relevante

**Proceso de actualización:**
1. Editar este documento con los cambios
2. Actualizar la fecha de "Última actualización" al inicio
3. Si el cambio es un artículo publicado: actualizar estado en tabla de la sección 3 y en `muchotexto_contexto_proyecto.md`
4. No commitear este archivo si contiene notas internas (es opcional — evaluar si se versiona o no)

---

## 13. Herramientas y skills

### Skills disponibles en el flujo de trabajo

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

### Herramientas gratuitas

| Herramienta | Uso |
|---|---|
| Google Search Console | Monitoreo de rankings, impresiones, CTR, backlinks |
| Google Analytics (GA4) | Tráfico, engagement |
| PageSpeed Insights | Core Web Vitals |
| validator.schema.org | Validar schema markup |
| Rich Results Test | Verificar elegibilidad para rich results |
| Ahrefs Webmaster Tools | Backlinks, auditoría técnica (gratis) |
| squirrelscan | SEO health check del sitio completo |

### Stack técnico del sitio

| Componente | Detalle |
|---|---|
| Hosting | GitHub Pages + GitHub Actions |
| SSG | Jekyll 4.4.1 con Ruby 3.3 |
| Tema | Monophase (local) |
| Dominio | muchotexto.net (GoDaddy → GitHub Pages) |
| Comentarios | Remark42 (Railway free tier) |
| Buscador | Simple-Jekyll-Search |
| Modelos IA | gpt-4o (editorial), gpt-4o-mini (pulso), vía GitHub Models API |

---

## Apéndice A: Anti-patrones documentados

| # | Error | Causa raíz | Fix |
|---|---|---|---|
| 1 | Puente narrativo inventado para enlace interno | Priorizar enlace sobre veracidad | Todo enlace requiere hecho verificable en findings |
| 2 | Regex `.*` greedy corrompiendo texto en editoriales | `IA.*deporte` devoraba párrafos enteros | `.{0,N}?` no-greedy + `\b(?:...)\b` |
| 3 | GPT-4o embellece declaraciones de personas | System prompt no prohibía inferir tono | No convertir personas en símbolos, no inferir tono |
| 4 | Títulos con fórmula repetida `¿puede Paraguay...?` | Sin regla de diversidad sintáctica | Cada título debe tener construcción única |

---

## Apéndice B: Internal linking por cluster

Cada artículo nuevo enlaza a 2-3 del mismo pilar con hechos verificables:

| Artículo nuevo | Enlaza a |
|---|---|
| Criptominería (#3) | Apertura eléctrica (#2), Yguazú Digital (#1), Itaipú 2027 (#4) |
| China-Taiwán (#10) | Peter Thiel (#9), Yguazú Digital (#1), Semiconductores (#14) |
| Educación tech (#18) | Talento (#21), Starlink (#22), De la soja al silicio (#26) |
| Startups IA (#35) | Fintech (#29), Cadena de valor (#36), Anotación de datos (#17) |
| Ley protección datos (#12) | IA soberana (#11), Ciberseguridad (#13) |
| Ciberseguridad (#13) | Ley protección datos (#12), Yguazú Digital (#1) |
| Red eléctrica (#6) | Apertura eléctrica (#2), Yguazú Digital (#1), Itaipú (#4), Hidrógeno verde (#5) |

---

## Apéndice C: Referencias de la investigación Google 2026

1. Backlinko — "How to Create an Effective SEO Strategy in 2026" (Abr 2026)
2. Backlinko — "Google E-E-A-T: How to Create People-First Content" (Jun 2026)
3. Backlinko — "Internal Linking for SEO: The Complete Guide" (Feb 2026)
4. Backlinko — "Schema Markup: What It Is and Why It Matters in 2026" (Jun 2026)
5. Backlinko — "Pillar Pages: How to Create One + Examples" (Abr 2025)
6. Backlinko — "Search Everywhere Optimization Guide" (Jun 2026)
7. Google — "AI Optimization Guide" (developers.google.com/search)
8. SparkToro — "Search Happens Everywhere" (2025)

---

> **Próxima acción inmediata:** Consolidar taxonomía de tags (sección 6.2.A) y crear página pilar (sección 6.2.B).
