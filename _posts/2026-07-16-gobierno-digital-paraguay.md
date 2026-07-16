---
layout: post
title: "Paraguay digitalizó 223 trámites pero la cédula sigue siendo en papel"
date: 2026-07-16
last_modified_at: 2026-07-16
categories: articulos
tags: sociedad-trabajo ia-paraguay
description: "Paraguay tiene 223 trámites digitales, un BID de USD 130M y un SII como X-Road. Estonia digitalizó el 99% de servicios en 2002. ¿Qué falta para que la cédula deje de ser papel?"
---

En 2000, un país báltico de 1,3 millones de habitantes lanzó su primer servicio de declaración de impuestos en línea. En 2001 activó X-Road, una capa de interoperabilidad que permite que todas las bases de datos del gobierno se hablen entre sí sin compartir información duplicada. En 2002 volvió obligatoria la cédula de identidad digital con chip criptográfico. En 2005 introdujo el voto por internet. En 2014 lanzó la e-Residency para no residentes. Hoy, Estonia tiene el 99% de sus servicios públicos disponibles en línea, ahorra el equivalente al 2% de su PIB en tiempo de los ciudadanos y es el estándar global de gobierno digital.

En 2018, Paraguay creó el Ministerio de Tecnologías de la Información y Comunicación. En 2019 firmó un préstamo de 130 millones de dólares con el BID para su Agenda Digital. En 2025 reportó 223 trámites digitalizados, 63 sistemas de gobierno desarrollados, una nube soberana (NubePY), un sistema de intercambio de información entre instituciones (SII), y un centro de respuesta a incidentes de ciberseguridad (CERT-PY). Paraguay tiene la arquitectura de un gobierno digital moderno.

Y sin embargo, un ciudadano paraguayo no puede renovar su cédula de identidad por internet.

## Lo que Estonia hizo (y cuánto costó)

Estonia no es rica. Cuando empezó su transformación digital en los años 90, acababa de salir de la órbita soviética con una economía destrozada. Su PIB per cápita en 1995 era de aproximadamente 3.000 dólares, en el mismo orden de magnitud que el de Paraguay. La diferencia no fue el dinero: fue una decisión política de blindar el presupuesto de tecnología del ciclo electoral.

En 1998, el parlamento estonio aprobó los "Principios de la Política de Información de Estonia", que fijaron el 1% del PIB como piso permanente de inversión en tecnología. Esa decisión —más que cualquier innovación técnica— explica por qué Estonia tiene gobierno digital y la mayoría de los países no. Sobrevivió a cambios de gobierno, crisis económicas y la transición de una economía postsoviética a una digital.

La inversión acumulada se estima entre 1.500 y 2.500 millones de euros en 25 años. Repartido por habitante, son entre 1.100 y 1.900 euros por persona. No es poco. Pero el ahorro es mayor: la firma digital ahorra aproximadamente 6 millones de horas de trabajo al año, las declaraciones de impuestos toman tres minutos, y X-Road —un sistema de código abierto que hoy usan más de 20 países— procesa 2.200 millones de transacciones anuales. Cualquier país puede descargarlo gratis.

El modelo estonio tiene cuatro pilares: identidad digital obligatoria con chip criptográfico, interoperabilidad entre todas las bases de datos del Estado, un portal único para el ciudadano, y financiamiento blindado. Sin los cuatro, el resto es cosmética.

## Lo que Paraguay ya construyó (y no es poco)

Paraguay no empezó ayer. El MITIC fue creado por ley en octubre de 2018. La Agenda Digital, financiada por el préstamo BID 4650/OC-PR por 130 millones de dólares —extendido hasta mayo de 2028—, tiene cuatro componentes: gobierno digital, economía digital, conectividad digital y fortalecimiento institucional. El componente de gobierno digital, con 32,6 millones de dólares asignados, lleva un 39% de ejecución.

El Sistema de Intercambio de Información es técnicamente el equivalente paraguayo de X-Road: una plataforma que permite que las instituciones públicas compartan datos en tiempo real sin que el ciudadano tenga que llevar el mismo papel de una ventanilla a otra. La NubePY aloja servicios gubernamentales bajo un modelo de nube híbrida con controles de política de datos. El nuevo centro de datos estatal Tier III —adjudicado en mayo de 2026 al Consorcio TIC— alojará 5.000 máquinas virtuales y 2.000 contenedores, como detallamos en el análisis sobre [la infraestructura digital que Paraguay está construyendo]({% post_url 2026-07-16-ia-soberana-paraguay %}). CERT-PY opera como centro nacional de respuesta a incidentes, publica boletines diarios de vulnerabilidades, y mantiene un SOC gubernamental activo. La Estrategia Nacional de Ciberseguridad 2025-2028 está aprobada.

El caso más exitoso de digitalización estatal en Paraguay no depende del MITIC: es Marangatu, el sistema de la Subsecretaría de Estado de Tributación. Procesa más de 627.000 documentos electrónicos por día, recauda aproximadamente 1,67 millones de dólares diarios por esa vía, y es la prueba de que un servicio público paraguayo puede funcionar enteramente en línea cuando existe la voluntad política y técnica de hacerlo.

Paraguay tiene, sobre el papel, todos los componentes de un gobierno digital moderno. Lo que no tiene es el cuarto pilar del modelo estonio: el que conecta los otros tres con la vida de un ciudadano común.

## Lo que todavía es papel

La brecha entre la arquitectura y la experiencia del ciudadano es el dato más revelador de este análisis.

La identidad electrónica existe y está operativa. Funciona con el número de cédula como usuario y una contraseña creada por el ciudadano, validada a través del Sistema de Intercambio de Información y autorizada por la Ley 6822/2022 de servicios de confianza para transacciones electrónicas. Permite autenticarse en el Portal Único de Gobierno y en los sistemas de los organismos del Estado. Es un sistema de usuario y contraseña —no un chip criptográfico como el de Estonia o Uruguay—, lo cual es una decisión de diseño que prioriza la velocidad de despliegue sobre la robustez criptográfica. La Autoridad Certificadora Raíz ofrece firma digital con PKI, pero está orientada a funcionarios públicos.

Con identidad electrónica o sin ella, para renovar la cédula un paraguayo sigue yendo al Departamento de Identificaciones. Para registrar una empresa, el sistema SUACE existe pero el proceso no es enteramente digital. Para una escritura de propiedad, el papel y el escribano siguen siendo el estándar.

La desconexión entre los sistemas es el síntoma más costoso. El SII está diseñado para resolverla, pero la cantidad de instituciones conectadas y el volumen de transacciones no son públicos. La interoperabilidad de la que habla el MITIC en sus documentos no se traduce —todavía— en que un ciudadano pueda hacer un trámite de principio a fin sin imprimir, firmar, escanear y autenticar.

Y luego está el problema anterior a la tecnología. El 62% de la fuerza laboral paraguaya es informal, según datos del Instituto Nacional de Estadística. Una persona que trabaja en la economía informal no declara impuestos, no tiene cuenta bancaria y en muchos casos no interactúa con el Estado más allá de la cédula. Para ese 62%, el gobierno digital no es una comodidad —es directamente irrelevante. El 17% de los paraguayos ni siquiera tiene acceso a internet, [un problema que abordamos en detalle en nuestro análisis de conectividad rural]({% post_url 2026-07-15-starlink-paraguay-conectividad %}). Digitalizar servicios sin incluir a quienes están fuera del sistema formal es eficiencia para los que ya están adentro, no inclusión para los que están afuera.

## Lo que cuesta no digitalizar

Las cuentas son conocidas. Un trámite presencial le cuesta al Estado y al ciudadano entre 10 y 25 euros, según el benchmark de la Comisión Europea. Un trámite en línea cuesta entre 0,50 y 3 euros. La diferencia es un factor de cinco a cincuenta veces. Aplicado a Paraguay, donde el BID estima que los ciudadanos realizan millones de interacciones anuales con el Estado, los ahorros potenciales son de decenas de millones de dólares al año solo en tiempo y desplazamientos.

Pero el costo más grande no se mide en euros por trámite. Se mide en oportunidades de corrupción. Cada ventanilla que un ciudadano tiene que visitar, cada papel que necesita autenticar, cada firma que un funcionario debe estampar es un punto de fricción donde puede aparecer un cobro indebido. Paraguay ocupa el puesto 150 de 180 países en el Índice de Percepción de la Corrupción de Transparencia Internacional, con 24 puntos sobre 100. La digitalización no elimina la corrupción, pero elimina al intermediario. Marangatu es el ejemplo: una vez que la facturación electrónica se volvió obligatoria, evadir impuestos requirió más creatividad que simplemente no facturar.

El caso de India con Aadhaar —el sistema de identidad digital más grande del mundo, con 1.380 millones de enrolados— es instructivo. El gobierno indio afirmó haber ahorrado 2.000 millones de dólares solo en subsidios de gas licuado gracias a la autenticación biométrica. Un análisis independiente del International Institute for Sustainable Development encontró que el ahorro específicamente atribuible a Aadhaar era de 140 millones de rupias —aproximadamente 1,5 millones de dólares, una cifra más de mil veces menor que la afirmación oficial. Las cifras oficiales de ahorro por digitalización casi siempre están infladas. Pero incluso la cifra corregida es positiva.

## Lo que Paraguay debería hacer con lo que ya tiene

Paraguay no necesita empezar de cero. Tiene el financiamiento —130 millones de dólares del BID—. Tiene la arquitectura —SII, NubePY, CERT-PY, AC Raíz—. Tiene el caso de éxito —Marangatu—. Tiene el plan —Agenda Digital—. Lo que no tiene, y es lo único que importa, es la decisión de priorizar tres cosas.

La primera es fortalecer la identidad digital que ya existe. El sistema actual de cédula más contraseña es funcional y está desplegado, pero no basta. Uruguay emitió su cédula de identidad electrónica con chip criptográfico desde 2015. Estonia lo hizo en 2002. Paraguay tiene la base —el SII valida los datos, la Ley 6822/2022 da el marco legal—, pero el salto de usuario/contraseña a una credencial criptográfica con firma digital para cada ciudadano es la diferencia entre autenticarse en un portal y firmar un documento con validez legal sin moverse de la casa. El costo incremental es de aproximadamente 10 a 30 millones de dólares.

La segunda es escalar el Sistema de Intercambio de Información hasta que ningún ciudadano tenga que presentar un documento que el Estado ya tiene. El principio de "una sola vez" —once-only principle— es la base del gobierno digital estonio: el ciudadano le da un dato al Estado una vez, y el Estado lo reutiliza. Paraguay tiene el SII. Lo que falta es conectarlo a todas las instituciones —registro civil, propiedad, tránsito, migraciones, salud, educación— y hacer obligatorio su uso.

La tercera es proteger el presupuesto de tecnología del ciclo electoral. Estonia blindó el 1% del PIB en 1998 y lo mantuvo durante 28 años con gobiernos de izquierda y derecha. Paraguay no necesita el 1% —el programa actual del BID equivale a aproximadamente el 0,3% del PIB anual— pero necesita que ese presupuesto sobreviva a la próxima elección. El préstamo del BID vence en 2028, el mismo año de las elecciones generales. Si el próximo gobierno decide que la Agenda Digital era el proyecto del anterior, Paraguay va a perder una década de avance institucional.

Paraguay tiene la arquitectura de un gobierno digital. Lo que no tiene es la experiencia de un ciudadano que pueda usarlo. Esa distancia —entre la arquitectura y la experiencia— se mide en una sola cosa: si podés renovar tu cédula sin salir de tu casa. Hasta que eso sea posible, los 223 trámites digitalizados son una cifra. No un gobierno digital.

Leé el análisis completo sobre sociedad y tecnología en la [guía de inteligencia artificial en Paraguay](/ia-en-paraguay/).

## Fuentes

- [Wikipedia — e-Estonia](https://en.wikipedia.org/wiki/E-Estonia) — cronología, X-Road, eID, 99% servicios online
- [Wikipedia — Aadhaar](https://en.wikipedia.org/wiki/Aadhaar) — costo, enrolamiento, controversias de ahorro
- [MITIC — Gobierno Electrónico](https://mitic.gov.py/gobierno-electronico/) — 13 proyectos, SII, Identidad Electrónica
- [Agenda Digital Paraguay](https://agendadigital.mitic.gov.py/) — 223 trámites, 63 sistemas, BID $130M
- [MITIC — Data Center del Estado](https://mitic.gov.py/datacenter/) — Tier III, Consorcio TIC, 5.000 VMs
- [MITIC — CERT-PY](https://www.cert.gov.py/) — CSIRT, SOC gubernamental, boletines diarios
- [SET — Marangatu y SIFEN](https://www.set.gov.py/) — facturación electrónica, 627K docs/día
- [Transparencia Internacional — Corruption Perceptions Index 2024](https://www.transparency.org/en/cpi/2024) — Paraguay 24/100, #150/180
- [INE Paraguay — Encuesta Permanente de Hogares](https://www.ine.gov.py/) — 62% informalidad laboral
- [EU eGovernment Benchmark — cost per transaction](https://digital-strategy.ec.europa.eu/en/library/egoverment-benchmark-2024) — €10-25 presencial vs €0.50-3 online

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Cuántos trámites digitales tiene Paraguay?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Según la Agenda Digital del MITIC, Paraguay tiene 223 trámites digitalizados y 63 sistemas de gobierno desarrollados a 2025. El programa cuenta con un préstamo del BID de USD 130 millones, extendido hasta mayo de 2028. Sin embargo, servicios esenciales como la renovación de la cédula de identidad siguen requiriendo presencia física."
      }
    },
    {
      "@type": "Question",
      "name": "¿Tiene Paraguay identidad digital para ciudadanos?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sí, pero es un sistema de usuario y contraseña (cédula + clave personal), no una credencial criptográfica con chip como la de Estonia o Uruguay. Está operativa, validada por el SII y autorizada por la Ley 6822/2022. Permite autenticarse en el Portal Único de Gobierno y otros sistemas del Estado. La Autoridad Certificadora Raíz (PKI) ofrece firma digital, pero está orientada a funcionarios públicos. El ciudadano común no dispone de una credencial con chip o app móvil con estándares criptográficos avanzados."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué necesita Paraguay para tener un gobierno digital como el de Estonia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tres cosas: identidad digital para ciudadanos (USD 10-30M de inversión inicial), escalar el Sistema de Intercambio de Información (SII) para que todas las instituciones compartan datos y el ciudadano no tenga que repetirlos, y proteger el presupuesto de tecnología del ciclo electoral. Paraguay ya tiene el financiamiento (BID USD 130M), la arquitectura (SII, NubePY, CERT-PY) y el caso de éxito (Marangatu de la SET). Lo que falta es la decisión política de priorizarlo."
      }
    }
  ]
}
</script>
