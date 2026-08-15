---
layout: post
title: "Paraguay tiene 1.5M de identidades digitales y 480 trámites online"
date: 2026-07-16
last_modified_at: 2026-08-15
categories: articulos
tags: sociedad-trabajo ia-paraguay
description: "Paraguay ya tiene 1.5M de usuarios con Identidad Electrónica, 480 trámites online y cédula digital. Pero la cédula física se emite en persona. ¿Qué falta?"
---

En 2000, un país báltico de 1,3 millones de habitantes lanzó su primer servicio de declaración de impuestos en línea. En 2001 activó X-Road, una capa de interoperabilidad que permite que todas las bases de datos del gobierno se hablen entre sí sin compartir información duplicada. En 2002 volvió obligatoria la cédula de identidad digital con chip criptográfico. En 2005 introdujo el voto por internet. En 2014 lanzó la e-Residency para no residentes. Hoy, Estonia tiene el 99% de sus servicios públicos disponibles en línea, ahorra el equivalente al 2% de su PIB en tiempo de los ciudadanos y es el estándar global de gobierno digital.

En 2018, Paraguay creó el Ministerio de Tecnologías de la Información y Comunicación. En 2019 firmó un préstamo de 130 millones de dólares con el BID para su Agenda Digital. En 2026 reporta más de 480 trámites en línea, 1,5 millones de ciudadanos con identidad electrónica, una cédula digital en el celular, una nube soberana (NubePY), un sistema de intercambio de información entre instituciones (SII), y un centro de respuesta a incidentes de ciberseguridad (CERT-PY). Paraguay tiene la arquitectura de un gobierno digital moderno, y la está usando.

Y sin embargo, para obtener o renovar la cédula física —el documento físico sin el cual no podés registrarte en el sistema digital— un paraguayo sigue yendo al Departamento de Identificaciones. Esa distancia entre lo que el sistema puede hacer y lo que el ciudadano necesita para entrar resume el estado del gobierno digital paraguayo en 2026.

## Lo que Estonia hizo (y cuánto costó)

Estonia no es rica. Cuando empezó su transformación digital en los años 90, acababa de salir de la órbita soviética con una economía destrozada. Su PIB per cápita en 1995 era de aproximadamente 3.000 dólares, en el mismo orden de magnitud que el de Paraguay. La diferencia no fue el dinero: fue una decisión política de blindar el presupuesto de tecnología del ciclo electoral.

En 1998, el parlamento estonio aprobó los "Principios de la Política de Información de Estonia", que fijaron el 1% del presupuesto estatal como piso permanente de inversión en tecnología. Esa decisión —más que cualquier innovación técnica— explica por qué Estonia tiene gobierno digital y la mayoría de los países no. Sobrevivió a cambios de gobierno, crisis económicas y la transición de una economía postsoviética a una digital.

La inversión acumulada se estima entre 1.500 y 2.500 millones de euros en 25 años. Repartido por habitante, son entre 1.100 y 1.900 euros por persona. No es poco. Pero el ahorro es mayor: la firma digital ahorra aproximadamente 6 millones de horas de trabajo al año, las declaraciones de impuestos toman tres minutos, y X-Road —un sistema de código abierto que hoy usan más de 20 países— procesa 2.200 millones de transacciones anuales. Cualquier país puede descargarlo gratis.

El modelo estonio tiene cuatro pilares: identidad digital obligatoria con chip criptográfico, interoperabilidad entre todas las bases de datos del Estado, un portal único para el ciudadano, y financiamiento blindado. Sin los cuatro, el resto es cosmética.

## Lo que Paraguay ya construyó (y es más de lo que parece)

Paraguay no empezó ayer. El MITIC fue creado por ley en octubre de 2018. La Agenda Digital, financiada por el préstamo BID 4650/OC-PR por 130 millones de dólares —extendido hasta mayo de 2028—, tiene cuatro componentes: gobierno digital, economía digital, conectividad digital y fortalecimiento institucional.

La **Identidad Electrónica** es el proyecto más ambicioso y el más exitoso. A julio de 2026 supera 1,5 millones de usuarios —aproximadamente el 30% de los paraguayos mayores de 18 años—. Funciona con el número de cédula como usuario y una contraseña creada por el ciudadano, validada a través del Sistema de Intercambio de Información y autorizada por la Ley 6822/2021 de servicios de confianza para transacciones electrónicas. El proceso de registro es remoto: se hace desde el sitio paraguay.gov.py o desde la app Portal Paraguay, sacándole tres fotos a la cédula (frente, dorso y selfie sosteniéndola), respondiendo preguntas de validación y esperando la aprobación automática o manual en un máximo de 48 horas. Desde julio de 2026, los paraguayos en el exterior también pueden registrarse mediante videollamada.

Una vez activada, la Identidad Electrónica da acceso a más de 480 trámites en línea y a documentos digitales: la cédula de identidad digital, el registro de conducir digital y la habilitación vehicular digital —disponible en 11 municipios, incluyendo Asunción—, todo desde la app. Entre los trámites más usados están el certificado de antecedentes policiales, el acta de nacimiento, la constancia de vacunación y la consulta de deuda en el Banco Central. El sistema ya está integrado con más de 27 plataformas, incluyendo MI IPS (el portal de salud del Instituto de Previsión Social). El MITIC anunció en mayo de 2026 que la autenticación por SMS será obligatoria para todos los usuarios, migrando del actual sistema de verificación por correo electrónico a un segundo factor más robusto.

El **Sistema de Intercambio de Información** es técnicamente el equivalente paraguayo de X-Road: una plataforma que permite que las instituciones públicas compartan datos en tiempo real sin que el ciudadano tenga que llevar el mismo papel de una ventanilla a otra. La **NubePY** aloja servicios gubernamentales bajo un modelo de nube híbrida. El nuevo centro de datos estatal Tier III —adjudicado en mayo de 2026 al Consorcio TIC— alojará 5.000 máquinas virtuales y 2.000 contenedores, como detallamos en el análisis sobre [la infraestructura digital que Paraguay está construyendo]({% post_url 2026-07-16-ia-soberana-paraguay %}). **CERT-PY** opera como centro nacional de respuesta a incidentes, publica boletines diarios de vulnerabilidades y mantiene un SOC gubernamental activo.

El caso más exitoso de digitalización estatal no depende del MITIC: es **Marangatu**, el sistema de la Dirección Nacional de Ingresos Tributarios. De los 47 servicios que ofrece la DNIT, 37 están en línea —la tasa más alta de digitalización del Estado paraguayo.

## El cuello de botella está en la puerta de entrada

Paraguay tiene un sistema de identidad digital con 1,5 millones de usuarios y 480 trámites en línea. La pregunta no es si existe. Es por qué la rueda no gira más rápido.

El primer cuello de botella es que la Identidad Electrónica es un sistema de usuario y contraseña —no un chip criptográfico como el de Estonia o Uruguay. Esto fue una decisión de diseño deliberada: un sistema de credenciales permite desplegar rápido y escalar sin distribuir hardware. La contracara es que no tiene validez de firma digital calificada. El MITIC lo dice explícitamente: "MITIC no emite firma electrónica cualificada". Para firmar un documento con validez legal —por ejemplo en el sistema SIARA de registros administrativos— el ciudadano necesita además un certificado de un proveedor privado acreditado por la Autoridad Certificadora Raíz, que depende del Ministerio de Industria y Comercio, no del MITIC. Son dos sistemas separados, con dos ministerios distintos, y el ciudadano tiene que navegar ambos.

El segundo cuello de botella es la puerta de entrada. Para crear tu Identidad Electrónica necesitás tu cédula física vigente. Para renovar la cédula física, tenés que ir al Departamento de Identificaciones. Es un círculo que el sistema no cierra: todo el ecosistema digital depende de un documento que solo se emite en papel y en persona. Mientras el Registro Civil (DGREC) tenga 21 servicios totales y solo 2 en línea —apenas el 10%—, y el Ministerio de Educación tenga 64 servicios con solo 2 digitalizados —el 3%—, la experiencia del ciudadano común va a ser fragmentada.

El tercer cuello de botella es anterior a la tecnología. El 62% de la fuerza laboral paraguaya es informal, según datos del Instituto Nacional de Estadística. Una persona que trabaja en la economía informal no declara impuestos, no tiene cuenta bancaria y en muchos casos no interactúa con el Estado más allá de la cédula. Para ese 62%, el gobierno digital no es una comodidad —es directamente irrelevante. El 17% de los paraguayos ni siquiera tiene acceso a internet, [un problema que abordamos en detalle en nuestro análisis de conectividad rural]({% post_url 2026-07-15-starlink-paraguay-conectividad %}). Digitalizar servicios sin incluir a quienes están fuera del sistema formal es eficiencia para los que ya están adentro, no inclusión para los que están afuera.

## Lo que cuesta no terminar lo empezado

Las cuentas son conocidas. Un trámite presencial le cuesta al Estado y al ciudadano entre 10 y 25 dólares, según el benchmark de gobierno digital de la Comisión Europea. Un trámite en línea cuesta entre 0,50 y 3 dólares. La diferencia es un factor de cinco a cincuenta veces.

Pero el costo más grande no se mide en euros por trámite. Se mide en oportunidades de corrupción. Paraguay ocupa el puesto 150 de 180 países en el Índice de Percepción de la Corrupción de Transparencia Internacional, con 24 puntos sobre 100. Cada ventanilla que un ciudadano tiene que visitar, cada papel que necesita autenticar, cada firma que un funcionario debe estampar es un punto de fricción donde puede aparecer un cobro indebido. La digitalización no elimina la corrupción, pero elimina al intermediario.

El caso de India con Aadhaar —el sistema de identidad digital más grande del mundo, con 1.380 millones de enrolados— es instructivo. El gobierno indio afirmó haber ahorrado 2.000 millones de dólares solo en subsidios de gas licuado gracias a la autenticación biométrica. Un análisis independiente del International Institute for Sustainable Development encontró que el ahorro específicamente atribuible a Aadhaar era de 140 millones de rupias —aproximadamente 1,5 millones de dólares, una cifra más de mil veces menor que la afirmación oficial. Las cifras oficiales de ahorro por digitalización casi siempre están infladas. Pero incluso la cifra corregida es positiva.

## Lo que Paraguay debería hacer con lo que ya tiene

Paraguay ya no está en la fase de "crear" un gobierno digital. Está en la fase de terminarlo. Tiene 1,5 millones de usuarios que ya pasaron por el proceso de registro —tomarse tres fotos con la cédula, esperar la validación—, lo cual demuestra que la demanda existe y que el sistema funciona. Lo que falta son tres cosas.

La primera es cerrar la brecha entre la Identidad Electrónica y la emisión del documento físico. Hoy son dos sistemas desconectados: uno digital, uno presencial. El día que un paraguayo pueda renovar su cédula enteramente en línea —con su identidad electrónica ya existente— el círculo se cierra. Uruguay lo resolvió en 2015 con la cédula electrónica con chip. Estonia en 2002. Paraguay tiene el SII que valida los datos biométricos y la Ley 6822/2022 que da el marco legal. Lo que falta es la integración entre el MITIC y el Departamento de Identificaciones.

La segunda es masificar la digitalización en las instituciones con mayor contacto ciudadano. Los datos del Portal Paraguay muestran que el MEC tiene 64 servicios y solo 2 online. El Registro Civil, 21 servicios y 2 online. La Policía Nacional, 34 servicios y 2 online. El Ministerio de Salud, 53 servicios y 7 online. Son las instituciones que un ciudadano común necesita para vivir —educación, identidad, seguridad, salud— y son las que menos han digitalizado. La DNIT tiene 37 de 47 servicios online. El estándar existe. Lo que falta es aplicarlo donde más importa.

La tercera es proteger el presupuesto de tecnología del ciclo electoral. Estonia blindó el 1% del presupuesto estatal en 1998 y lo mantuvo durante 28 años con gobiernos de izquierda y derecha. Paraguay no necesita el 1% —el programa actual del BID equivale a aproximadamente el 0,3% del PIB anual— pero necesita que ese presupuesto sobreviva a la próxima elección. El préstamo del BID vence en 2028, el mismo año de las elecciones generales. Si el próximo gobierno decide que la Agenda Digital era el proyecto del anterior, Paraguay va a perder una década de avance institucional.

Paraguay tiene 1,5 millones de ciudadanos con identidad digital, 480 trámites en línea y una cédula en el celular. Eso no es un proyecto. Es un sistema funcionando. Lo que no tiene —todavía— es la experiencia de un ciudadano que pueda hacer todo lo que necesita sin tocar una ventanilla. Esa distancia no se mide en plata. Se mide en si el Estado decide que las instituciones que más interactúan con la gente —educación, salud, identidad— se digitalicen al mismo ritmo que las que recaudan impuestos.

Leé el análisis completo sobre sociedad y tecnología en la [guía de inteligencia artificial en Paraguay](/ia-en-paraguay/).

## Fuentes

- [MITIC — "Identidad Electrónica ya supera el millón y medio de ciudadanos"](https://mitic.gov.py/) (3 junio 2026)
- [MITIC — "MITIC reitera pasos para crear la Identidad Electrónica"](https://mitic.gov.py/) (2 julio 2026)
- [MITIC — "Identidad Electrónica en el exterior"](https://mitic.gov.py/) (6 julio 2026)
- [MITIC — "SMS será obligatorio como método de verificación"](https://mitic.gov.py/) (6 mayo 2026)
- [Portal Paraguay — Estadísticas de trámites por institución](https://www.paraguay.gov.py/estadisticas-portal/tramites-institucion)
- [Portal Paraguay — Identidad Electrónica](https://www.paraguay.gov.py/identidad-electronica/informacion)
- [MITIC — Gobierno Electrónico: 13 proyectos](https://mitic.gov.py/gobierno-electronico/)
- [Agenda Digital Paraguay](https://agendadigital.mitic.gov.py/)
- [Wikipedia — e-Estonia](https://en.wikipedia.org/wiki/E-Estonia)
- [Wikipedia — Aadhaar](https://en.wikipedia.org/wiki/Aadhaar)
- [Transparencia Internacional — Corruption Perceptions Index 2024](https://www.transparency.org/en/cpi/2024)
- [INE Paraguay — Encuesta Permanente de Hogares](https://www.ine.gov.py/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Cuántos paraguayos tienen Identidad Electrónica?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Más de 1,5 millones a julio de 2026, aproximadamente el 30% de los mayores de 18 años. El sistema funciona con el número de cédula como usuario y una contraseña personal, validada por el Sistema de Intercambio de Información (SII). El registro se hace desde la web paraguay.gov.py o la app Portal Paraguay, sacando fotos a la cédula y una selfie."
      }
    },
    {
      "@type": "Question",
      "name": "¿Puedo tener la cédula de identidad en el celular?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sí. Una vez registrado en la Identidad Electrónica, la app Portal Paraguay permite acceder a la cédula de identidad digital, el registro de conducir digital y la habilitación vehicular digital. Sin embargo, para obtener o renovar la cédula física —necesaria para registrarse en el sistema— hay que ir presencialmente al Departamento de Identificaciones."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué trámites puedo hacer en línea en Paraguay?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Más de 480 trámites están disponibles en línea a través del Portal Paraguay. Incluyen certificado de antecedentes policiales, acta de nacimiento, constancia de vacunación y consulta de deuda en el Banco Central. Sin embargo, las instituciones con mayor contacto ciudadano tienen las tasas más bajas de digitalización: el MEC tiene 64 servicios y solo 2 online (3%), el Registro Civil 21 servicios y 2 online (10%), y la Policía Nacional 34 servicios y 2 online (6%)."
      }
    }
  ]
}
</script>

*Artículo elaborado con la asistencia de inteligencia artificial y supervisado por el editor humano de muchotexto.net.*
