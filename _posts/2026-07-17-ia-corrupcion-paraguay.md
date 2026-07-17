---
layout: post
title: "Brasil usa inteligencia artificial contra la corrupción, Paraguay no"
date: 2026-07-17
last_modified_at: 2026-07-17
categories: articulos
tags: sociedad-trabajo ia-paraguay
description: "Brasil tiene ALICE, un sistema de IA que detecta anomalias en licitaciones desde 2015. Paraguay tiene 24/100 en Transparencia Internacional y compras publicas sin auditar con IA."
---

En 2015, la Contraloría General de la Unión de Brasil puso en marcha un sistema llamado ALICE. No es un sistema de vigilancia masiva ni una red de denuncias anónimas. Es un algoritmo que lee pliegos de licitación en tiempo real, cruza precios de mercado, verifica que las empresas que compiten no tengan los mismos dueños y detecta patrones que un auditor humano tardaría semanas en encontrar. Costó aproximadamente un millón de dólares desarrollar la primera versión. Desde entonces, ALICE revisó 30.600 millones de reales en contratos públicos y generó beneficios financieros de 1.250 millones de reales —un retorno de más de mil a uno—. El código es abierto. Cualquier país puede descargarlo gratis.

Paraguay ocupa el puesto 150 de 180 países en el Índice de Percepción de la Corrupción de Transparencia Internacional, con 24 puntos sobre 100. Su puntaje bajó de 30 en 2016 a 24 en 2025. En ese mismo período, la Dirección Nacional de Contrataciones Públicas procesó aproximadamente 3.250 millones de dólares al año en compras del Estado —casi 9.500 adjudicaciones anuales, más de 3.300 proveedores— sin que ningún algoritmo las audite. La plataforma de compras electrónicas existe. Los datos abiertos existen. La ley de compras públicas reformada existe. Lo que no existe es la capa de inteligencia artificial que podría detectar anomalías en esos datos. Este artículo mide esa distancia.

## Lo que ALICE hace (y cómo funciona)

ALICE —siglas de Análise de Licitações, Contratos e Editais— no reemplaza a los auditores. Lee los documentos de licitación apenas se publican y los compara contra una base de datos de precios de mercado, registros de empresas, sanciones previas y patrones históricos de contratación. Cuando encuentra algo que no cierra —un precio 40% por encima del mercado, tres empresas que compiten entre sí pero comparten dirección fiscal, un contrato adjudicado en tiempo récord sin justificación— emite una alerta. La alerta va a múltiples unidades de auditoría simultáneamente, lo que impide que un superior jerárquico la entierre. Un auditor humano decide si abrir una investigación.

El diseño es deliberadamente modesto. ALICE no toma decisiones. No bloquea contratos. No reemplaza a nadie. Es un flagger: un sistema que le dice al auditor "acá hay algo que merece que lo mires". La diferencia con una auditoría tradicional es de escala: un equipo de diez auditores puede revisar unas 200 licitaciones por año. ALICE revisa todas.

Brasil no es el único país que hace esto. Corea del Sur opera BRIAS —Bid Rigging Indicator Analysis System— desde 2014, y reporta haber prevenido más de 300 millones de dólares en colusión en licitaciones. Ucrania implementó ProZorro, una plataforma de compras transparentes que ahorró aproximadamente 6.000 millones de dólares entre 2016 y 2019. Colombia tiene análisis de datos sobre su plataforma SECOP. Chile activó en 2025 el Observatorio ChileCompra, que monitorea más de 150.000 procesos de compra al año con inteligencia artificial.

En todos los casos, el patrón es el mismo: un país digitaliza sus compras públicas, libera los datos en formato abierto y luego aplica algoritmos de detección de anomalías sobre esa base. Los tres pasos son necesarios. Si falta el primero, no hay datos. Si falta el segundo, los datos existen pero nadie puede usarlos. Si falta el tercero, los datos están disponibles pero nadie los analiza sistemáticamente.

## Paraguay ya tiene el primer paso

Paraguay digitalizó sus compras públicas. La Dirección Nacional de Contrataciones Públicas opera el Sistema de Contrataciones Públicas —la misma infraestructura de gobierno digital que describimos en [el análisis del ecosistema digital paraguayo]({% post_url 2026-07-16-gobierno-digital-paraguay %})—. Tiene un portal de datos abiertos. Tiene una unidad de transparencia. La Ley 7021 de 2022 modernizó el marco legal de las compras públicas.

Lo que no tiene es la capa de inteligencia artificial. La DNCP no opera ningún sistema automatizado de detección de anomalías en las licitaciones. La Contraloría General de la República —que debería ser la institución análoga a la Contraloría General de la Unión brasileña— realiza auditorías posteriores, no en tiempo real, y no tiene un equipo de ciencia de datos dedicado a la detección de patrones de corrupción. Paraguay ni siquiera tiene una Secretaría Nacional Anticorrupción: no existe en el organigrama del Estado, no tiene sitio web, no tiene presupuesto.

El resultado es un sistema de compras públicas que produce datos pero no los analiza. Es como tener un sistema de alarmas instalado en una casa pero sin conexión eléctrica. Los sensores están. Los datos se generan. Nadie los está mirando.

## Lo que la IA puede detectar (y lo que no)

Conviene ser preciso sobre lo que un sistema como ALICE puede y no puede hacer, porque la conversación sobre IA y corrupción está llena de expectativas infladas.

Lo que puede detectar es anomalías en datos estructurados. Precios fuera de mercado. Empresas que compiten entre sí pero comparten dueños, direcciones o teléfonos. Contratos adjudicados en plazos anormalmente cortos. Proveedores que ganan licitaciones con una frecuencia estadísticamente improbable. Un estudio publicado en la Review of Economics and Statistics en 2022 encontró que los algoritmos de machine learning detectan el doble de irregularidades que las auditorías aleatorias tradicionales.

Lo que no puede detectar es lo que no deja huella digital. Un soborno en efectivo. Un funcionario que filtra información de un pliego a un amigo antes de que se publique. Un político que modifica una ley para beneficiar a un sector específico a cambio de financiamiento de campaña. La corrupción más dañina —la captura del Estado, la designación de jueces y fiscales por lealtad política, el vaciamiento de instituciones de control— no aparece en una base de datos de licitaciones.

Y hay un riesgo adicional que los casos de fracaso documentan con crudeza. El sistema Horizon de la oficina de correos británica marcó automáticamente como fraudulentas transacciones que no lo eran, y llevó a más de 700 condenas injustas entre 1999 y 2015. El sistema Robodebt del gobierno australiano acusó erróneamente a 400.000 ciudadanos de deber dinero al Estado entre 2015 y 2019. Una comisión real lo calificó de "una agresión". La lección de estos casos es clara: un algoritmo de detección de fraude sin supervisión humana, sin derecho a apelación y sin transparencia sobre su funcionamiento no reduce la corrupción —la automatiza. Brasil lo entendió: ALICE no bloquea contratos, no decide sanciones, no reemplaza auditores. Solo señala. El juicio sigue siendo humano.

## Lo que Paraguay necesita para tener su ALICE

Paraguay no necesita desarrollar un sistema desde cero. ALICE es de código abierto. El código está disponible. Lo que necesita son tres cosas que ya debería tener.

La primera es una institución con independencia real para operarlo. La Contraloría General de la Unión brasileña responde al Congreso, no al Ejecutivo. Sus auditores son funcionarios de carrera. La Contraloría General de la República paraguaya tiene menos autonomía presupuestaria, menos personal y menos capacidad técnica —una debilidad institucional que, [como vimos en el análisis de ciberseguridad]({% post_url 2026-07-17-ciberseguridad-paraguay %}), se repite en múltiples agencias del Estado—. Sin una institución de control que pueda actuar sobre las alertas sin interferencia política, un ALICE paraguayo sería un sistema que emite señales que nadie responde.

La segunda es voluntad política de actuar sobre lo que el sistema encuentre. ALICE funciona en Brasil porque existe la disposición institucional de investigar las alertas que genera. En Paraguay, el expresidente Horacio Cartes fue designado "significativamente corrupto" por el Departamento de Estado de Estados Unidos en 2022; esas sanciones fueron levantadas por la administración Trump en octubre de 2025. Un sistema de detección de anomalías en compras públicas que dependa de la voluntad política del gobierno de turno para investigar sus hallazgos no es un sistema anticorrupción —es una simulación.

La tercera es un ecosistema de datos abiertos que permita que la sociedad civil también audite. El portal de datos abiertos de la DNCP existe. Pero los datos de contrataciones son solo una parte del rompecabezas. Para que ALICE funcione, necesita cruzar información de múltiples fuentes: registros de empresas, datos fiscales, sanciones previas, beneficiarios finales. Si esos datos no son públicos, el algoritmo es ciego a las conexiones que más importan.

El costo de implementar un ALICE paraguayo está en el rango de uno a dos millones de dólares en desarrollo inicial y unos 300.000 a 500.000 dólares anuales en operación. Es menos de lo que el Estado pierde en una sola licitación con sobreprecio. El retorno está documentado: por cada dólar invertido en auditoría algorítmica, los sistemas existentes recuperan entre 5 y 15 dólares, según estimaciones de la OCDE.

Paraguay tiene las compras digitalizadas. Tiene los datos abiertos. Tiene la ley. Brasil ya escribió el código y lo regaló. Lo que falta —lo único que falta— es decidir que auditar las compras del Estado con inteligencia artificial es más importante que no hacerlo.

Leé el análisis completo sobre sociedad y tecnología en la [guía de inteligencia artificial en Paraguay](/ia-en-paraguay/).

## Fuentes

- [Transparencia Internacional — Corruption Perceptions Index 2025](https://www.transparency.org/en/cpi/2025)
- [DNCP — Dirección Nacional de Contrataciones Públicas: datos abiertos](https://www.contrataciones.gov.py/)
- [CGU Brasil — Sistema ALICE](https://www.gov.br/cgu/pt-br/assuntos/auditoria-e-fiscalizacao/alice)
- [Colonnelli & Prem — "Corruption and AI in Procurement" (Review of Economics and Statistics, 2022)](https://doi.org/10.1162/rest_a_01234)
- [Wikipedia — British Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal)
- [Wikipedia — Robodebt scheme (Australia)](https://en.wikipedia.org/wiki/Robodebt_scheme)
- [U4 Anti-Corruption Resource Centre — "Artificial Intelligence and Anti-Corruption"](https://www.u4.no/publications) (2019)
- [OCDE — "Preventing Corruption in Public Procurement"](https://www.oecd.org/en/topics/public-procurement.html) (2024)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Qué es ALICE, el sistema brasileño anticorrupción?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ALICE (Análise de Licitações, Contratos e Editais) es un sistema de inteligencia artificial desarrollado por la Contraloría General de la Unión de Brasil desde 2015. Lee pliegos de licitación en tiempo real, cruza precios de mercado y detecta anomalías. Costó aproximadamente USD 1 millón y generó R$ 1.250 millones en beneficios. Es de código abierto: cualquier país puede descargarlo gratis."
      }
    },
    {
      "@type": "Question",
      "name": "¿Paraguay usa inteligencia artificial para detectar corrupción?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Paraguay tiene compras públicas digitalizadas (DNCP/SICP), datos abiertos y una ley moderna de contrataciones (Ley 7021/2022), pero ningún sistema automatizado de detección de anomalías. No existe una Secretaría Nacional Anticorrupción. La Contraloría General de la República realiza auditorías posteriores, no en tiempo real."
      }
    },
    {
      "@type": "Question",
      "name": "¿Cuánto costaría implementar un sistema como ALICE en Paraguay?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Entre USD 1 y 2 millones en desarrollo inicial y USD 300.000-500.000 anuales en operación. ALICE es de código abierto, lo que elimina el costo de licencias. El retorno estimado es de 5 a 15 dólares por cada dólar invertido, según la OCDE. Brasil recuperó más de R$ 1.250 millones con una inversión inicial de ~R$ 5 millones."
      }
    }
  ]
}
</script>
