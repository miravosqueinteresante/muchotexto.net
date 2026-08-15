---
layout: post
title: "Qué es un data center y por qué Paraguay quiere construir uno"
date: 2026-07-10
last_modified_at: 2026-08-15
categories: articulos
tags: infraestructura-energia ia-paraguay
description: "Qué es un data center, cómo funciona, qué tiene adentro y por qué Paraguay con su energía barata quiere construir el más grande de la región."
---

En cada artículo de este sitio sobre inteligencia artificial en Paraguay aparece la expresión "centro de datos" o "data center". Yguazú Digital es uno. Los mineros de criptomonedas operan versiones más pequeñas. Los servidores que entrenan a ChatGPT están dentro de uno. Pero rara vez se explica qué es exactamente un data center, qué tiene adentro, por qué consume tanta electricidad y qué lo diferencia de cualquier otro edificio industrial.

Este artículo es una guía básica. No asume conocimiento previo. Si ya sabés qué es un rack, un GPU y un sistema de refrigeración líquida, probablemente no necesites leerlo. Pero si cada vez que leés sobre los megavatios de Yguazú Digital te preguntás qué tiene que ver la electricidad con los datos, esta explicación es para vos.

## Qué es un data center, en palabras simples

Un data center es una fábrica. Pero en vez de producir autos, zapatos o alimentos, produce procesamiento de datos. Adentro tiene miles de computadoras —llamadas servidores— que funcionan las 24 horas del día, todos los días del año, sin apagarse nunca.

Cuando hacés una búsqueda en Google, mirás un video en YouTube, le pedís a ChatGPT que te escriba un correo o consultás tu saldo bancario desde el celular, tu pedido viaja por internet hasta un data center. Ahí, uno o varios servidores procesan tu solicitud, buscan la información que necesitás y te la devuelven en milisegundos. Todo eso consume electricidad. Mucha.

La escala es lo que distingue a un data center de un cuarto de servidores. Una empresa mediana puede tener un rack con diez servidores en una oficina. Un data center como los que Google, Amazon o Microsoft operan tiene decenas de miles de servidores distribuidos en edificios del tamaño de varios campos de fútbol. Yguazú Digital, en su fase final, aspira a una capacidad de 1.000 megavatios —el equivalente al consumo eléctrico de una ciudad de aproximadamente 750.000 personas.

## Lo que hay adentro de esa caja sin ventanas

Los data centers son edificios deliberadamente anónimos. No tienen ventanas. Están rodeados de cercos perimetrales, cámaras y controles de acceso biométricos. Lo que importa está adentro, y se organiza en capas.

**Los servidores.** Son computadoras optimizadas para funcionar sin interrupción. No tienen monitor, teclado ni mouse. Vienen en formato "rack": cajas planas de aproximadamente 48 centímetros de ancho que se apilan una sobre otra dentro de gabinetes metálicos. Un rack estándar puede contener entre 20 y 40 servidores. Un data center grande tiene miles de racks.

**Los procesadores.** El cerebro de cada servidor. En un data center tradicional, son CPUs —similares a las de una computadora de escritorio pero mucho más potentes y con más núcleos. En un data center de inteligencia artificial, son GPUs —los mismos chips que se usan para videojuegos, pero diseñados específicamente para entrenar modelos de IA. NVIDIA fabrica los más utilizados: los H100 y los B200. Cada uno de estos chips cuesta entre 25.000 y 40.000 dólares, y un solo rack puede contener ocho o más. Por eso los proyectos de IA requieren inversiones de cientos de millones de dólares solo en hardware.

**El almacenamiento.** Los datos no se procesan en el aire. Cada servidor tiene discos —generalmente de estado sólido (SSD) para velocidad— donde se guardan desde tu historial de búsquedas hasta los datasets de entrenamiento de los modelos de lenguaje. Un data center de IA puede almacenar petabytes de información. Un petabyte son mil millones de megabytes. Es muchísimo.

**La refrigeración.** Todos esos chips generan calor. Mucho calor. Si no se enfrían, se sobrecalientan, se apagan o se dañan. Los data centers tradicionales usan ventilación por aire forzado —básicamente, aires acondicionados industriales que mueven aire frío a través de los racks. Los data centers de IA, que concentran más potencia de cómputo en menos espacio, están migrando a refrigeración líquida: tuberías que hacen circular agua o fluidos especiales directamente sobre los chips. Es más eficiente pero más complejo y caro de instalar.

**La energía.** Nada de lo anterior funciona sin electricidad. Un data center tiene dos fuentes de alimentación: la red eléctrica principal y sistemas de respaldo. Los generadores diésel se encienden automáticamente si hay un corte. Las baterías UPS —sistema de alimentación ininterrumpida— mantienen todo funcionando durante los segundos que tarda el generador en arrancar. Un data center no puede apagarse. Un minuto sin servicio le cuesta millones a quien lo opera.

**La conectividad.** Los datos entran y salen por cables de fibra óptica. La velocidad de conexión se mide en latencia: el tiempo que tarda un dato en ir y volver. Para un data center de IA, la latencia no es crítica —entrenar un modelo puede tomar semanas y no importa si la respuesta tarda 50 milisegundos más. Para un data center que procesa transacciones financieras o streaming de video en tiempo real, cada milisegundo cuenta.

## Por qué necesitan tanta energía

Un data center consume electricidad en tres cosas: procesamiento, refrigeración y pérdidas del sistema. La regla general es que por cada megavatio que consumen los servidores, se necesita aproximadamente otro medio megavatio para refrigerarlos.

Para ponerlo en números concretos: Yguazú Digital, en su fase 1, va a consumir 10 megavatios. Esa cantidad de energía alcanza para abastecer a aproximadamente 7.500 hogares. En su fase 3, a 1.000 megavatios, consumirá lo mismo que una ciudad de 750.000 personas —más que la población de Asunción.

La [criptominería]({% post_url 2026-07-07-criptomineria-paraguay-energia-barata %}) también consume enormes cantidades de electricidad, pero con una diferencia importante: los mineros de bitcoin usan chips especializados llamados ASIC que hacen una sola tarea —resolver problemas criptográficos— y la hacen de manera extremadamente eficiente. Un data center de IA tiene que ser más flexible: los mismos servidores que hoy entrenan un modelo de lenguaje pueden mañana procesar imágenes médicas o simular escenarios climáticos.

## Data center normal vs data center de IA

| Característica | Data center tradicional | Data center de IA |
|---|---|---|
| **Procesador** | CPU (Intel, AMD) | GPU (NVIDIA H100, B200) |
| **Densidad por rack** | 5-10 kilovatios | 40-80 kilovatios |
| **Refrigeración** | Aire forzado | Líquida (agua o fluidos especiales) |
| **Consumo típico** | 10-50 MW | 100-1.000 MW |
| **Costo por MW** | USD 5-10 millones | USD 15-25 millones |
| **Personal/MW** | 0.5-1 empleado | 0.3-0.5 empleado (más automatizado) |
| **Cliente típico** | Bancos, gobiernos, Netflix | OpenAI, Google, Meta |

La diferencia fundamental es la densidad de potencia. En el mismo espacio físico, un data center de IA procesa entre cinco y diez veces más datos que uno tradicional, consume entre cinco y diez veces más electricidad y cuesta entre dos y tres veces más construir.

## Por qué Paraguay

Paraguay tiene la electricidad industrial más barata de Sudamérica: entre 30 y 45 dólares por megavatio-hora. Para un data center de 100 megavatios, cada dólar de diferencia en el precio de la electricidad representa aproximadamente 876.000 dólares al año. En un data center donde la energía representa entre el 40% y el 60% del costo operativo, la [ventaja de estar en Paraguay]({% post_url 2026-05-27-apertura-sector-electrico-privado-paraguay %}) no es marginal: es existencial.

Pero la energía barata no alcanza. Hace falta también [una red de transmisión que llegue hasta el data center]({% post_url 2026-07-08-red-electrica-paraguay-ia %}), acuerdos diplomáticos que garanticen el suministro de chips —que llevaron a Paraguay a asociarse con Taiwán—, y un marco legal que proteja los datos que se procesen en el país. Todas esas piezas están en movimiento. Este artículo explica la primera: qué es la máquina que Paraguay quiere encender.

---

El cluster de inteligencia artificial en Paraguay se construye sobre esta pieza fundamental: entender qué es un data center. Los artículos sobre [Yguazú Digital]({% post_url 2026-06-23-yguazu-digital-paraguay-hub-ia-mas-grande-del-mundo %}), la red eléctrica, la criptominería y la geopolítica de los semiconductores asumen este conocimiento. Si llegaste hasta acá, ya tenés las bases para leer cualquiera de ellos.

Este artículo es parte de la [guía completa de inteligencia artificial en Paraguay](/ia-en-paraguay/).

## Fuentes

- [Uptime Institute — "Data Center Tier Classification"](https://uptimeinstitute.com/resources)
- [NVIDIA — "H100 Tensor Core GPU"](https://www.nvidia.com/en-us/data-center/h100/)
- [Data Center Knowledge — "How Much Energy Do Data Centers Use?"](https://www.datacenterknowledge.com/)
- [Wikipedia — "Data center"](https://en.wikipedia.org/wiki/Data_center)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Qué es un data center?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Un data center es una instalación que alberga miles de servidores funcionando las 24 horas para procesar y almacenar datos. Cuando usás Google, ChatGPT o Netflix, tu solicitud viaja a uno de estos centros. Consumen enormes cantidades de electricidad: un data center grande puede usar la misma energía que una ciudad de 750.000 personas."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué diferencia un data center normal de uno de inteligencia artificial?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Los data centers de IA usan GPUs (como los NVIDIA H100 de USD 25.000-40.000 cada uno) en vez de CPUs tradicionales. Consumen 5 a 10 veces más electricidad por metro cuadrado, requieren refrigeración líquida en vez de aire, y cuestan USD 15-25 millones por megavatio construir, contra USD 5-10 millones de uno tradicional."
      }
    },
    {
      "@type": "Question",
      "name": "¿Por qué Paraguay es atractivo para construir data centers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Paraguay tiene la electricidad industrial más barata de Sudamérica: USD 30-45 por megavatio-hora, 100% hidroeléctrica. Como la energía representa el 40-60% del costo operativo de un data center, cada dólar de diferencia en el precio de electricidad representa cientos de miles de dólares al año. Además, su ubicación geopolítica y su alianza con Taiwán le dan acceso a chips."
      }
    }
  ]
}
</script>

*Artículo elaborado con la asistencia de inteligencia artificial y supervisado por el editor humano de muchotexto.net.*
