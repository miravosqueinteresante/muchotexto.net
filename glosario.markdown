---
layout: page
title: "Glosario: Inteligencia Artificial en Paraguay"
permalink: /glosario/
description: "Terminos clave de inteligencia artificial en Paraguay explicados en contexto local: data centers, energia, GPUs, leyes y el ecosistema tech paraguayo."
last_modified_at: 2026-07-13
---

## Infraestructura y energía

**Data center** — Instalacion que alberga miles de servidores procesando datos 24/7. Yguazu Digital proyecta un data center de 1.000 MW en su fase final. [Que es un data center y por que Paraguay quiere construir uno](/articulos/2026/07/10/que-es-un-data-center-paraguay-ia/).

**MW (megavatio)** — Unidad de potencia electrica. La capacidad de un data center se mide en MW porque la electricidad es su principal insumo. Yguazu Digital: 10 MW (fase 1) a 1.000 MW (fase 3). 1 MW abastece aproximadamente 750 hogares. [Red electrica de Paraguay](/articulos/2026/07/08/red-electrica-paraguay-ia/).

**GPU** — Chip especializado en calculo paralelo. NVIDIA fabrica los mas usados (H100 y B200, entre USD 25.000 y 40.000 cada uno). Un data center de IA puede tener miles funcionando simultaneamente para entrenar modelos. Taiwan, que los fabrica, es socia de Paraguay via Yguazu Digital.

**Rack** — Gabinete metalico donde se apilan servidores. Un rack estandar contiene 20 a 40 servidores. Los racks de IA consumen 40-80 kW, cinco veces mas que los tradicionales.

**PUE (Power Usage Effectiveness)** — Indice que mide la eficiencia energetica de un data center. PUE 1.5 significa que por cada MW de computo, se gasta 0.5 MW en refrigeracion y perdidas. Paraguay parte con desventaja porque no tiene experiencia previa operando data centers a esta escala.

**ASIC** — Chip especializado en una sola tarea. Los mineros de bitcoin usan ASICs para resolver problemas criptograficos. Una vez que se vuelven obsoletos (vida util ~1.3 anos), generan residuo electronico. [Criptomineria en Paraguay](/articulos/2026/07/07/criptomineria-paraguay-energia-barata/).

**ANDE (Administracion Nacional de Electricidad)** — Empresa estatal que genera, transmite y distribuye la electricidad en Paraguay. Opera con tarifas politicas que no cubren sus costos, lo que limita su capacidad de inversion en la red. [Luces y sombras de la apertura electrica](/articulos/2026/05/27-apertura-sector-electrico-privado-paraguay/).

**Apertura electrica (Decreto 6034)** — Norma de mayo de 2026 que habilita por primera vez la generacion privada de energia renovable no hidraulica. Empresas privadas pueden generar, comprar, vender y exportar electricidad. Clave para los data centers que planean instalarse.

**Itaipu** — Represa hidroelectrica compartida con Brasil, de 14.000 MW de capacidad. Paraguay tiene derecho al 50% de la energia pero consume solo el 10%. El excedente se vende a Brasil a precio preferencial. La renegociacion del Anexo C en 2027 definira cuanta energia queda disponible para uso domestico y la viabilidad de los proyectos de IA en Paraguay.

---

## Tecnologia IA

**LLM (Large Language Model)** — Modelo de inteligencia artificial entrenado con enormes cantidades de texto para entender y generar lenguaje humano. ChatGPT, Claude, Gemini y GPT-4o son LLMs. Entrenar uno requiere miles de GPUs funcionando semanas o meses. En Paraguay, la [Universidad Politecnica Taiwan-Paraguay](/articulos/2026/07/09/educacion-tech-paraguay-ia/) forma a los ingenieros que podrian trabajar con esta tecnologia.

**RAG (Retrieval Augmented Generation)** — Tecnica que permite a un LLM buscar informacion actualizada en internet antes de responder, en lugar de depender solo de su entrenamiento original. Es lo que Google usa en AI Overviews y lo que hace que el contenido de sitios como muchotexto.net pueda ser citado en respuestas de IA. [Que es un data center](/articulos/2026/07/10/que-es-un-data-center-paraguay-ia/).

**Token** — Unidad basica de procesamiento de un LLM. Un token equivale aproximadamente a una silaba o un caracter. Los modelos cobran por token procesado. El chip H100 de NVIDIA puede procesar miles de millones de tokens por hora, y cada GPU cuesta entre USD 25.000 y 40.000. [Que es un data center](/articulos/2026/07/10/que-es-un-data-center-paraguay-ia/).

**Entrenamiento vs inferencia** — Dos fases de la vida de un modelo de IA. El entrenamiento (training) consume enormes cantidades de energia y datos durante semanas o meses, usando GPUs al maximo. La inferencia (cuando el modelo responde) consume menos por consulta pero se repite millones de veces. Un data center como Yguazu Digital necesita infraestructura distinta para cada fase. [Que es un data center](/articulos/2026/07/10/que-es-un-data-center-paraguay-ia/).

---

## Paraguay y Geopolitica

**Anexo C de Itaipu** — El anexo financiero del Tratado de Itaipu que fija el precio de la electricidad. Vence en 2027. Si no se renueva, la tarifa que Brasil paga por el excedente paraguayo caeria un 60%, y Paraguay perderia unos USD 1.250 millones anuales. [Articulo completo: Paraguay necesita mas ingenieros](/articulos/2026/07/09/educacion-tech-paraguay-ia/).

**Yguazu Digital** — Proyecto binacional Paraguay-Taiwan para construir el centro de datos de IA mas grande de Latinoamerica. Tres fases: 10 MW (USD 200M), 100 MW (USD 5.000M), 1.000 MW (USD 40.000M). Modelo de gobernanza 50/50 copiado de Itaipu. [Articulo completo](/articulos/2026/06/23/yguazu-digital-paraguay-hub-ia-mas-grande-del-mundo/).

**Ley 7593/2025** — Ley de Proteccion de Datos Personales de Paraguay, sancionada en noviembre de 2025. Entra en vigor en noviembre de 2027. Alineada con el GDPR europeo, crea la Agencia Nacional de Proteccion de Datos dentro del MITIC, pero la autoridad no es independiente y las multas maximas son de solo USD 160.000. [Articulo completo](/articulos/2026/07/07/ley-proteccion-datos-paraguay-ia/).

**Maquila tecnologica** — Regimen tributario que grava los servicios tecnologicos exportados al 1% (Ley 7547/2025). Similar al modelo que usaron India y Filipinas para construir sus industrias de TI. Paraguay lo aprobo pero aun no lo usa a escala.

**UPTP (Universidad Politecnica Taiwan-Paraguay)** — Universidad creada en 2018 como parte de la cooperacion bilateral. Cuatro departamentos de ingenieria, mas de 300 graduados hasta 2026. Proyecta 500+ ingenieros por ano. Es la principal fuente local de talento tech para los proyectos de IA.

---

## Fintech y Cripto

**Blockchain** — Tecnologia de registro distribuido que permite transacciones sin intermediarios. La Ley 7572/2025 reconoce los valores emitidos en blockchain, habilitando la tokenizacion de activos en Paraguay.

**Tokenizacion** — Conversion de un activo real (tierra, soja, ganado) en tokens digitales que pueden comprarse y venderse en blockchain. Paraguay aprobo la Ley 7572/2025 que permite tokenizar activos agropecuarios. [Articulo completo](/articulos/2026/05/18/tokenizacion-del-agro-paraguay/).

**SPI (Sistema de Pagos Instantaneos)** — Sistema del Banco Central de Paraguay que permite transferencias inmediatas 24/7. En junio de 2025 proceso 28 millones de transacciones. No es gratuito como el Pix brasileno, lo que limita su adopcion masiva. [Articulo completo: Fintech en Paraguay](/articulos/2026/07/10/fintech-paraguay-ecosistema/).

**Hash rate** — Medida de la potencia de computo de la red Bitcoin. Paraguay tiene el cuarto hash rate mas alto del mundo (~4.3% del total), detras de Estados Unidos, Rusia y China. Esto es gracias a la energia barata de Itaipu. [Articulo completo](/articulos/2026/07/07/criptomineria-paraguay-energia-barata/).

**Bitcoin mining** — Proceso de validacion de transacciones en la red Bitcoin, que requiere computadoras especializadas (ASICs) consumiendo grandes cantidades de electricidad. Paraguay se convirtio en un hub global de mineria gracias a su energia hidroelectrica barata. [Articulo completo](/articulos/2026/07/07/criptomineria-paraguay-energia-barata/).

---

## Agro y ecosistema

**Agricultura de precision** — Uso de tecnologia (GPS, satelites, drones, sensores) para optimizar la produccion agricola. Menos del 5% de las fincas paraguayas la usan, concentrada en grandes productores de soja y trigo. [Articulo completo](/articulos/2026/07/13/agro-40-paraguay-ia/).

**Smart Soil Py** — Startup paraguaya de agtech, financiada por BID Lab (USD 150.000). Usa IA para detectar enfermedades en cultivos mediante imagenes. Monitorea mas de 23.000 hectareas en Paraguay.

**Guarani Insights** — Plataforma satelital desarrollada por la Agencia Espacial del Paraguay y ArkEdge (Japon). Ofrece imagenes satelitales gratuitas para productores paraguayos, con 4 anos de datos historicos.

**Dron agricola** — Vehiculo aereo no tripulado usado para fumigar, monitorear y mapear cultivos. En Paraguay operan aproximadamente 300, con un ahorro de agua de hasta el 90% respecto a la fumigacion tradicional.

**Cooperativas (INCOOP)** — Instituciones de credito reguladas por el Instituto Nacional de Cooperativismo. Son, para millones de paraguayos en zonas rurales, el unico acceso al sistema financiero. Clave para conectar la tecnologia financiera con el pequeno productor.
