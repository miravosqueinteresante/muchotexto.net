# MuchoTexto Data
## Documento Maestro de Contexto y Arquitectura

**Proyecto:** MuchoTexto Data  
**Dominio editorial:** muchotexto.net  
**Proyecto de datos:** Datos Públicos / capa de datos de MuchoTexto  
**Primer conector:** ANDE  
**Estado:** Diseño inicial  
**Objetivo:** Construir una infraestructura de datos verificables sobre Paraguay que alimente el universo editorial y de conocimiento de MuchoTexto.

---

# 1. Visión

MuchoTexto comenzó como una plataforma editorial orientada a explicar fenómenos relacionados con Paraguay, especialmente en torno a inteligencia artificial, energía, infraestructura, tecnología, economía, regulación y geopolítica.

Datos Públicos nació como un intento de trabajar con información pública y convertirla en información comprensible.

El siguiente paso es unir ambos universos.

La idea central de **MuchoTexto Data** es construir una capa de datos estructurados, verificables y reutilizables que se encuentre debajo del contenido editorial de MuchoTexto.

La relación fundamental será:

> **MuchoTexto explica.  
> MuchoTexto Data estructura y demuestra.  
> Las fuentes oficiales proporcionan la evidencia.**

El objetivo no es copiar indiscriminadamente los datos publicados por instituciones paraguayas.

El objetivo es seleccionar información relevante, extraerla, normalizarla, conservar su procedencia y convertirla en conocimiento reutilizable.

---

# 2. El problema

La información relevante sobre Paraguay existe, pero está fragmentada.

Puede encontrarse en:

- páginas web;
- publicaciones institucionales;
- PDFs;
- informes anuales;
- estadísticas;
- series históricas;
- resoluciones;
- documentos técnicos;
- tablas;
- comunicados;
- archivos descargables;
- sistemas de consulta.

El problema no siempre es la ausencia de información.

Muchas veces el problema es que:

1. está distribuida entre diferentes lugares;
2. aparece en formatos poco reutilizables;
3. no está normalizada;
4. las series históricas están separadas;
5. los números aparecen dentro de documentos;
6. resulta difícil relacionar una cifra con su contexto;
7. no existe una capa que conecte los datos con las entidades y temas que ya analiza MuchoTexto.

MuchoTexto Data busca resolver esa fragmentación.

---

# 3. Principio fundamental: no almacenar lo que no necesitamos

El proyecto NO debe convertirse en un repositorio masivo de documentos o imágenes.

No queremos descargar cientos de gigabytes de información que ya existe en infraestructura externa.

La arquitectura debe seguir esta regla:

> **Consumir fuentes públicas, extraer únicamente la información necesaria y conservar datos derivados, metadatos y proveniencia.**

Cuando una fuente dispone de una API, endpoint, CSV, HTML, servicio estadístico o mecanismo equivalente, se utilizará preferentemente ese mecanismo.

Cuando una fuente únicamente publica un PDF, se extraerán los datos relevantes del documento y se conservará la referencia exacta a la fuente original.

La información pesada permanece donde ya existe.

MuchoTexto Data almacena principalmente:

- valores;
- series;
- entidades;
- indicadores;
- fechas;
- relaciones;
- metadatos;
- referencias;
- metodología;
- proveniencia.

---

# 4. Arquitectura conceptual

```text
                         FUENTES

      ┌──────────┬──────────┬──────────┬──────────┐
      │   ANDE   │  BCP     │   INE    │  MITIC   │
      │  DNCP    │ Itaipú   │Yacyretá │  otras   │
      └────┬─────┴────┬─────┴────┬─────┴────┬─────┘
           │          │          │          │
           ▼          ▼          ▼          ▼

                    CONECTORES

      ┌─────────────────────────────────────────┐
      │       Conectores de fuentes públicas    │
      └────────────────────┬────────────────────┘
                           │
                           ▼

                 EXTRACCIÓN / NORMALIZACIÓN

                           │
                           ▼

                  BASE MUCHOTEXTO DATA

        ┌────────────┬────────────┬────────────┐
        │ Indicadores│ Entidades  │  Fuentes   │
        │ Series     │ Relaciones │ Metadatos  │
        └────────────┴────────────┴────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼

         MuchoTexto     Datos Públicos   API
          editorial       / exploración  futura

              │
              ▼
        CONOCIMIENTO SOBRE PARAGUAY
```

---

# 5. El concepto de “conector”

Cada fuente de información debe tener su propio conector.

Ejemplo:

```text
ande/
├── connector
├── extractor
├── normalizer
├── validators
└── metadata
```

El conector conoce:

- dónde encontrar la información;
- qué páginas o endpoints consultar;
- cómo detectar actualizaciones;
- cómo extraer los datos;
- cómo interpretar tablas;
- cómo normalizar unidades;
- cómo validar resultados;
- cómo registrar la fuente;
- cómo registrar cuándo se realizó la extracción.

El objetivo es evitar construir un scraper gigante y frágil.

Cada institución tiene características diferentes.

Por eso:

> **Una fuente = un conector especializado.**

---

# 6. Primer conector: ANDE

ANDE será la primera fuente oficial incorporada.

La elección de ANDE se debe a que el universo de MuchoTexto ya trabaja con:

- energía;
- electricidad;
- infraestructura;
- consumo;
- data centers;
- criptominería;
- Itaipú;
- demanda energética;
- política energética.

Además, ANDE publica información en diferentes formatos que permiten probar las distintas estrategias de extracción que necesitará el sistema.

ANDE servirá como **laboratorio real para diseñar la arquitectura general de conectores**.

---

# 7. Objetivo del conector ANDE

El conector ANDE no intentará extraer absolutamente todo lo publicado por ANDE.

Su objetivo inicial será crear una primera base estructurada de indicadores eléctricos relevantes para el universo de MuchoTexto.

El primer conjunto de indicadores deberá concentrarse en:

## Demanda

- demanda eléctrica;
- demanda máxima;
- energía demandada;
- evolución mensual;
- evolución anual.

## Consumo

- consumo total;
- consumo por categoría cuando exista información pública;
- consumidores intensivos especiales;
- consumo residencial;
- consumo comercial;
- consumo industrial;
- otros segmentos disponibles.

## Abastecimiento / generación

Cuando los datos estén disponibles:

- Itaipú;
- Yacyretá;
- Acaray;
- otras fuentes relevantes.

## Clientes

Cuando exista información pública agregada:

- cantidad de clientes;
- evolución histórica;
- clientes por categoría.

## Pérdidas

- pérdidas totales;
- pérdidas técnicas/no técnicas cuando estén disponibles;
- evolución histórica.

## Tarifas

- categoría tarifaria;
- nivel de tensión;
- precio;
- unidad;
- período de vigencia;
- resolución/documento asociado.

## Infraestructura

Solo cuando existan datos públicos estructurados y relevantes:

- líneas;
- subestaciones;
- capacidad;
- expansión;
- proyectos relevantes.

---

# 8. Tipos de fuentes ANDE

El conector debe poder trabajar con diferentes formatos.

## 8.1 HTML

Cuando ANDE publique una cifra directamente en una página web.

Proceso:

```text
Página ANDE
↓
detección
↓
extracción
↓
normalización
↓
validación
↓
base de datos
```

---

## 8.2 PDF

Cuando la información esté contenida en informes.

Proceso:

```text
PDF oficial
↓
identificación del documento
↓
localización de tabla/sección
↓
extracción
↓
normalización
↓
validación
↓
dato estructurado
```

El PDF original no se convierte automáticamente en una gigantesca base documental.

Solo se extraen los elementos necesarios.

---

## 8.3 CSV / XLSX

Si ANDE publica archivos estructurados:

```text
archivo
↓
lectura
↓
validación de columnas
↓
normalización
↓
base de datos
```

Estos formatos tendrán prioridad sobre extracción desde PDF.

---

## 8.4 APIs / endpoints

Si se identifica un servicio público oficial:

```text
API
↓
consulta
↓
respuesta
↓
validación
↓
normalización
↓
base
```

No se asumirá que una API existe.

Primero se investigará y documentará.

---

# 9. Modelo de datos

Cada indicador debe tener, como mínimo:

```text
id
entidad
indicador
valor
unidad
fecha_inicio
fecha_fin
fuente
documento
url
fecha_publicacion
fecha_extraccion
metodo_extraccion
estado_verificacion
```

Ejemplo conceptual:

```text
entidad:
ANDE

indicador:
consumo_total

valor:
29419

unidad:
GWh

periodo:
2025

fuente:
ANDE

documento:
Publicación institucional correspondiente

fecha_extraccion:
2026-08-29

estado_verificacion:
verificado
```

---

# 10. Proveniencia

La proveniencia es uno de los elementos más importantes del proyecto.

Cada número debe poder responder:

> ¿De dónde salió?

No basta con almacenar:

```text
consumo = 29.419 GWh
```

Debe existir una cadena de evidencia:

```text
Indicador
↓
Dato
↓
Fuente
↓
Documento/página
↓
Fecha
↓
Método de extracción
```

Esto permitirá que un lector de MuchoTexto pueda pasar de una afirmación a su fuente.

---

# 11. Estados de verificación

Cada dato tendrá un estado.

## Verificado

La extracción fue contrastada con la fuente oficial.

## Extraído

El dato fue obtenido automáticamente pero todavía necesita revisión.

## Revisado

El dato fue revisado manualmente.

## En conflicto

Existen dos fuentes oficiales o dos publicaciones con valores diferentes.

## Obsoleto

El dato sigue siendo válido históricamente pero ya no representa el estado actual.

## Requiere revisión

El sistema detectó un cambio que puede deberse a una modificación de metodología, unidad o fuente.

---

# 12. Validación automática

El conector no debe limitarse a copiar números.

Debe intentar detectar errores.

Ejemplos:

### Cambio excesivo

```text
2025: 29.419 GWh
2026: 294.190 GWh
```

El sistema debe marcar:

> Cambio anormal detectado.

Puede tratarse de:

- error de extracción;
- cambio de unidad;
- error tipográfico;
- modificación metodológica;
- dato real.

No debe corregir silenciosamente.

---

### Unidad incorrecta

Detectar diferencias entre:

- kWh;
- MWh;
- GWh;
- MW;
- kW.

---

### Duplicados

Evitar registrar dos veces la misma publicación.

---

### Períodos superpuestos

Detectar si dos datos pretenden representar exactamente el mismo período.

---

# 13. No confundir dato con interpretación

MuchoTexto Data debe separar claramente:

### Dato

> ANDE reportó X GWh.

### Cálculo

> El aumento respecto al año anterior fue de X%.

### Interpretación

> Esto puede estar relacionado con...

El sistema debe conservar esa separación.

Los cálculos realizados por MuchoTexto deben poder reproducirse.

---

# 14. Datos derivados

MuchoTexto Data puede generar indicadores propios a partir de datos oficiales.

Ejemplo:

Fuente:

```text
2024 = 26.000 GWh
2025 = 29.419 GWh
```

Dato derivado:

```text
crecimiento interanual = 13,15%
```

La base debe conservar ambos:

```text
dato_original
dato_derivado
fórmula
fuentes utilizadas
```

Así se puede distinguir:

> **ANDE publicó el dato.**

de:

> **MuchoTexto calculó el porcentaje.**

---

# 15. Relación con MuchoTexto

La capa de datos debe conectarse con el contenido editorial.

Ejemplo:

```text
ARTÍCULO
"El desafío energético de Paraguay"

       ↓

ENTIDADES

ANDE
Itaipú
Yacyretá
Data Centers

       ↓

INDICADORES

demanda
consumo
pérdidas
tarifas

       ↓

FUENTES

ANDE
Itaipú
otras fuentes oficiales
```

Esto permite que un artículo deje de ser una pieza aislada.

Se convierte en una puerta de entrada a una base de conocimiento.

---

# 16. El concepto de entidad

MuchoTexto ya utiliza entidades como parte de su arquitectura de conocimiento.

MuchoTexto Data debe aprovecharlas.

Una entidad puede ser:

- empresa;
- institución;
- proyecto;
- persona pública;
- ciudad;
- departamento;
- país;
- infraestructura;
- ley;
- organismo;
- sector económico.

Ejemplo:

```text
ANDE
│
├── energía
├── electricidad
├── Itaipú
├── Yacyretá
├── Acaray
├── tarifas
├── consumidores
├── data centers
├── criptominería
└── artículos MuchoTexto
```

La base de datos no solo almacenará números.

Almacenará relaciones.

---

# 17. Evolución futura de conectores

Después de ANDE podrán incorporarse progresivamente otras fuentes.

Posibles categorías:

## Energía

- ANDE
- Itaipú
- Yacyretá
- Viceministerio de Minas y Energía
- otras fuentes relevantes

## Economía

- Banco Central del Paraguay
- Ministerio de Economía y Finanzas
- otras fuentes estadísticas oficiales

## Población

- Instituto Nacional de Estadística

## Tecnología

- MITIC
- fuentes regulatorias y estadísticas pertinentes

## Contrataciones

- DNCP

## Legislación

- fuentes oficiales legislativas y jurídicas

La incorporación no debe hacerse por cantidad.

Una fuente entra cuando aporta información relevante al universo de conocimiento de MuchoTexto.

---

# 18. Arquitectura modular

El sistema debe poder crecer así:

```text
connectors/
│
├── ande/
├── bcp/
├── ine/
├── mitic/
├── dncp/
├── itaipu/
└── yacyreta/
```

Cada conector implementará una interfaz común.

Conceptualmente:

```text
fetch()
extract()
normalize()
validate()
store()
```

Esto permitirá que el resto del sistema no tenga que saber cómo funciona cada fuente.

---

# 19. Automatización

Una vez que el conector esté probado, se automatizará.

Ejemplo:

```text
GitHub Actions
       ↓
ejecutar conector ANDE
       ↓
buscar actualizaciones
       ↓
extraer datos nuevos
       ↓
validar
       ↓
guardar
       ↓
generar indicadores
       ↓
actualizar sitio
```

La frecuencia dependerá de la fuente.

No tiene sentido consultar una fuente cada hora si solo publica datos mensualmente.

---

# 20. Registro de cambios

Cada ejecución debe dejar un registro.

Ejemplo:

```text
2026-08-29
ANDE connector

Documentos revisados: 12
Documentos nuevos: 1
Datos nuevos: 17
Datos modificados: 2
Errores: 0
Datos pendientes de revisión: 1
```

Esto permitirá auditar el sistema.

---

# 21. Control de cambios en fuentes

Las páginas institucionales pueden cambiar.

Los documentos pueden ser reemplazados.

Las URLs pueden desaparecer.

Por eso cada dato debe conservar:

- URL;
- título;
- fecha;
- fuente;
- identificador del documento cuando exista;
- fecha de extracción;
- contexto suficiente para volver a localizarlo.

Cuando sea legal y técnicamente apropiado, podrá conservarse una copia mínima de la evidencia necesaria, pero evitando transformar el proyecto en un repositorio masivo.

---

# 22. Qué NO debe hacer MuchoTexto Data

El proyecto no debe:

- intentar recopilar absolutamente todo;
- descargar enormes cantidades de datos sin propósito;
- duplicar repositorios públicos completos;
- presentar datos sin fuente;
- mezclar cifras de diferentes metodologías sin advertencia;
- convertir automáticamente una correlación en causalidad;
- afirmar corrupción a partir de anomalías;
- esconder incertidumbre;
- modificar datos oficiales sin registrar el cambio;
- convertir cálculos propios en “datos oficiales”.

---

# 23. Principio editorial

Toda cifra importante publicada por MuchoTexto debe poder clasificarse como:

### Fuente oficial

La institución publicó directamente el dato.

### Dato derivado

MuchoTexto calculó el valor utilizando una o más fuentes.

### Estimación

El valor fue estimado mediante una metodología explícita.

### Interpretación

Es una conclusión editorial basada en datos.

Esta distinción debe mantenerse visible.

---

# 24. Objetivo del primer MVP

El primer MVP no será “tener todos los datos de ANDE”.

Será demostrar que el sistema completo funciona.

Debe poder hacer:

```text
FUENTE ANDE
     ↓
CONECTOR
     ↓
EXTRACCIÓN
     ↓
NORMALIZACIÓN
     ↓
VALIDACIÓN
     ↓
BASE
     ↓
INDICADOR
     ↓
MUCHOTEXTO
     ↓
FUENTE ORIGINAL
```

Con aproximadamente 10–15 indicadores iniciales será suficiente.

El éxito del MVP no se medirá por cantidad de datos.

Se medirá por:

- exactitud;
- trazabilidad;
- reproducibilidad;
- automatización;
- facilidad para actualizar;
- posibilidad de reutilización editorial.

---

# 25. Primer producto visible

El primer producto visible podría ser:

## MuchoTexto Data — Energía

Con:

### Indicadores principales

- demanda;
- consumo;
- crecimiento;
- pérdidas;
- consumidores intensivos;
- generación/abastecimiento;
- tarifas.

### Series históricas

Gráficos simples y comparables.

### Fuentes

Cada gráfico debe mostrar la fuente.

### Metodología

Explicación de cómo se construyó cada indicador.

### Entidades relacionadas

ANDE, Itaipú, Yacyretá, etc.

### Artículos relacionados

Enlaces hacia MuchoTexto.

---

# 26. Ejemplo de experiencia de usuario

Un usuario entra en un artículo de MuchoTexto:

> **Paraguay está consumiendo cada vez más electricidad**

Encuentra:

### Consumo eléctrico

**29.419 GWh — 2025**

**+12,5% interanual**

Fuente: ANDE

[Ver serie histórica]

[Ver metodología]

[Ver fuente]

[Explorar datos]

Al pulsar “Explorar datos”:

```text
ANDE
Consumo eléctrico

1985 ─────── 2025

Gráfico
Tabla
Descargar datos
Fuentes
Metodología
```

El artículo y el dataset se complementan.

---

# 27. Evolución futura: del dato al grafo de conocimiento

Una vez existan suficientes conectores, MuchoTexto Data podrá convertirse progresivamente en un grafo de conocimiento sobre Paraguay.

Ejemplo:

```text
ANDE
 │
 ├── administra → electricidad
 │
 ├── recibe energía de → Itaipú
 │
 ├── recibe energía de → Yacyretá
 │
 ├── opera → Acaray
 │
 ├── publica → tarifas
 │
 ├── reporta → consumo
 │
 └── aparece en → artículos MuchoTexto
```

Y:

```text
Data Center
 │
 ├── requiere → electricidad
 │
 ├── relacionado con → ANDE
 │
 ├── ubicado en → Paraguay
 │
 ├── regulado por → determinadas normas
 │
 └── analizado en → MuchoTexto
```

La potencia del sistema surge de las conexiones.

---

# 28. Estrategia de crecimiento

El crecimiento será incremental.

## Fase 1

**ANDE**

Construcción del modelo y primer conector.

## Fase 2

**Energía**

Incorporación de Itaipú, Yacyretá y otras fuentes pertinentes.

## Fase 3

**Economía**

BCP, MEF y otras fuentes.

## Fase 4

**Población y territorio**

INE y fuentes geográficas.

## Fase 5

**Tecnología y regulación**

MITIC y fuentes jurídicas/regulatorias.

## Fase 6

**Grafo de conocimiento**

Conectar todas las entidades, indicadores, artículos y fuentes.

---

# 29. Filosofía técnica

El proyecto debe priorizar:

### Simpleza

No construir infraestructura compleja antes de necesitarla.

### Modularidad

Cada fuente debe poder evolucionar independientemente.

### Trazabilidad

Todo dato importante debe tener fuente.

### Reproducibilidad

Los cálculos deben poder repetirse.

### Ligereza

Evitar almacenamiento innecesario.

### Automatización

Automatizar las tareas repetitivas después de validarlas manualmente.

### Transparencia

Mostrar cuándo un dato es oficial y cuándo es un cálculo propio.

---

# 30. Filosofía de investigación

MuchoTexto Data no debe partir de:

> “¿Qué datos podemos conseguir?”

sino de:

> **“¿Qué preguntas importantes queremos responder?”**

Después se busca qué fuentes permiten responderlas.

Ejemplo:

Pregunta:

> ¿Cómo evolucionó el consumo eléctrico paraguayo?

Necesitamos:

- consumo;
- períodos;
- unidades;
- fuente;
- histórico.

Pregunta:

> ¿Qué peso tienen los consumidores intensivos?

Necesitamos:

- consumo de esa categoría;
- consumo total;
- período;
- metodología.

La pregunta determina el dato.

---

# 31. Filosofía de confianza

El objetivo no es parecer omnisciente.

El objetivo es ser confiable.

Cuando no exista información suficiente, el sistema debe decir:

> **No encontramos evidencia pública suficiente para responder esta pregunta.**

Cuando exista un dato pero tenga limitaciones:

> **Este indicador utiliza información disponible públicamente, pero la serie presenta cambios metodológicos a partir de 2024.**

Cuando haya conflicto:

> **Dos publicaciones oficiales presentan valores diferentes. El conflicto está pendiente de revisión.**

La transparencia sobre las limitaciones forma parte del producto.

---

# 32. El activo estratégico

El principal activo del proyecto no serán los artículos individuales.

Tampoco serán los gráficos.

Será la combinación de:

```text
FUENTES
+
DATOS ESTRUCTURADOS
+
HISTORIAL
+
ENTIDADES
+
RELACIONES
+
METODOLOGÍA
+
PROVENIENCIA
```

Con el tiempo, esta estructura será cada vez más difícil de replicar.

Cada nuevo conector aumenta el valor de los anteriores porque permite establecer nuevas relaciones.

---

# 33. Resultado esperado

A largo plazo, MuchoTexto Data debe permitir responder preguntas como:

> ¿Cuánta electricidad consume Paraguay?

> ¿Cómo cambió ese consumo en 40 años?

> ¿Qué sectores consumen más?

> ¿Qué relación existe entre crecimiento económico y demanda eléctrica?

> ¿Qué proyectos tecnológicos requieren infraestructura energética?

> ¿Dónde están esos proyectos?

> ¿Qué regulaciones los afectan?

> ¿Qué empresas participan?

> ¿Qué artículos de MuchoTexto explican esos fenómenos?

Y todas las respuestas deben poder conducir nuevamente hacia la evidencia.

---

# 34. Definición final del proyecto

**MuchoTexto Data es una infraestructura de datos y conocimiento sobre Paraguay que transforma información pública dispersa en indicadores estructurados, verificables y conectados con entidades, fuentes y análisis editoriales.**

No busca recopilar todo.

Busca **seleccionar, estructurar, conectar y explicar aquello que permite comprender mejor Paraguay**.

El primer experimento será ANDE.

ANDE no es el destino final.

Es el primer conector y el laboratorio donde se probará la arquitectura que posteriormente permitirá conectar otras fuentes.

La dirección estratégica es:

```text
ANDE
 ↓
conector
 ↓
datos estructurados
 ↓
indicadores
 ↓
MuchoTexto
 ↓
otras fuentes
 ↓
entidades
 ↓
relaciones
 ↓
grafo de conocimiento
 ↓
infraestructura de conocimiento sobre Paraguay
```

---

# 35. Próximo paso

No comenzar todavía con una gran base de datos ni con una interfaz compleja.

El siguiente paso es construir el **ANDE Data Map**.

Ese documento deberá identificar, indicador por indicador:

| Indicador | Fuente ANDE | Formato | Frecuencia | Histórico | Método de extracción | Prioridad |
|---|---|---|---|---|---|---|
| Demanda | Por determinar | HTML/PDF/etc. | Por determinar | Sí/No | Por determinar | Alta |
| Consumo | Por determinar | HTML/PDF/etc. | Por determinar | Sí/No | Por determinar | Alta |
| Pérdidas | Por determinar | PDF/etc. | Por determinar | Sí/No | Por determinar | Alta |
| Tarifas | Por determinar | HTML/PDF | Por determinar | Sí | Por determinar | Alta |
| Clientes | Por determinar | Por determinar | Por determinar | Por determinar | Por determinar | Media |
| Consumidores intensivos | Por determinar | PDF/etc. | Por determinar | Sí/No | Por determinar | Alta |
| Generación/abastecimiento | Por determinar | HTML/PDF | Por determinar | Sí/No | Por determinar | Alta |

Ese inventario será el **primer documento técnico del conector ANDE**.

A partir de él se diseñará el extractor real, la estructura de la base de datos y la automatización.