---
layout: post
title: "La IA cuesta más que los humanos que reemplazó: lo que dicen los números"
date: 2026-05-27
last_modified_at: 2026-05-27
categories: articulos
tags: analisis-ia ia-paraguay
description: "Uber quemó su presupuesto de IA en 4 meses. Starbucks eliminó su sistema porque funcionaba peor que un humano. ¿Estamos viendo el principio del fin de la burbuja de la IA?"
---

Hay un post que circula en redes sociales y que probablemente ya viste. Dice que Uber quemó todo su presupuesto anual de IA en cuatro meses. Que Microsoft está retirando licencias a sus propios ingenieros. Que Starbucks eliminó su sistema de inventario porque funcionaba peor que un empleado humano. Y que un vicepresidente de NVIDIA admitió que la IA cuesta más que los trabajadores que supuestamente reemplaza. El post termina con una pregunta: ¿estamos viendo el principio del fin de la burbuja de la IA?

La respuesta corta es: no es tan simple. Algunas de esas afirmaciones son ciertas. Otras necesitan contexto. Y lo más interesante no es si la burbuja existe o no, sino lo que revelan sobre el momento exacto en que estamos parados.

Este artículo es una verificación de esos datos, un análisis del estado real de la inversión en IA, y un intento de responder una pregunta más útil: ¿qué significa todo esto para un país como Paraguay, que está apostando su recurso energético más valioso a centros de datos de inteligencia artificial?

---

## 1. Uber: el éxito que se comió el presupuesto

Empecemos por el caso más documentado. En abril de 2026, Praveen Neppalli Naga, director de tecnología de Uber, confirmó a [The Information](https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets) que la empresa había agotado todo su presupuesto de herramientas de IA para 2026 en solo cuatro meses. No por un fracaso técnico. Por el contrario: porque la herramienta funcionaba demasiado bien.

Esto es lo que pasó. En diciembre de 2025, Uber implementó Claude Code — el asistente de codificación de Anthropic — para toda su organización de ingeniería, unos 5.000 desarrolladores. La adopción fue volcánica: pasó del 32% de los ingenieros en febrero al 84% en marzo de 2026. Para abril, el 95% de los ingenieros usaba herramientas de IA mensualmente. Aproximadamente el 70% del código commit hoy en Uber se origina con IA, y cerca del 11% de las actualizaciones de backend en producción son escritas por agentes autónomos sin intervención humana.

El problema es que Claude Code no se factura por usuario, sino por consumo de tokens. Un ingeniero que corre un agente contra un repositorio moderado cuesta ~$500 al mes. Uno que corre múltiples agentes en paralelo, refactorizando codebases completos, puede llegar a $2.000 mensuales. El propio Naga gastó $1.200 en una sesión de demostración de dos horas. Multiplicado por 5.000 ingenieros, la cuenta mensual oscila entre $2.5 y $10 millones. En cuatro meses, eso son entre $10 y $40 millones. El presupuesto de un año desapareció en un trimestre.

Pero la historia no terminó ahí. Semanas después, el presidente de Uber, Andrew Macdonald, dio una entrevista a [Rapid Response](https://www.fastcompany.com/91547368/ubers-andrew-macdonald-on-what-americas-economy-looks-like-from-the-drivers-seat) donde dijo algo todavía más inquietante: la empresa no puede trazar una línea clara entre el consumo de tokens y las funcionalidades entregadas a los usuarios. *"Ese vínculo no existe todavía"*, admitió. El CEO Dara Khosrowshahi había planteado la estrategia como una sustitución directa — menos humanos, más infraestructura de IA — pero Macdonald ahora cuestiona si ese trade-off se puede defender sin métricas de impacto.

El caso Uber no es un fracaso. Es una advertencia sobre lo que pasa cuando una herramienta que funciona bien encuentra un modelo de precios que no fue diseñado para el uso que los ingenieros le dan.

---

## 2. Microsoft: cuando tu propio producto compite con el que usas

En mayo de 2026, [Windows Central](https://www.windowscentral.com/microsoft/microsoft-cancels-claude-code-licenses-shifting-developers-to-github-copilot-cli-a-move-likely-driven-by-financial-motives) reportó que Microsoft estaba cancelando la mayoría de las licencias internas de Claude Code en su división Experiences + Devices — la que construye Windows, Microsoft 365, Outlook, Teams y Surface. Los ingenieros afectados recibieron la instrucción de migrar a GitHub Copilot CLI antes del 30 de junio, el último día del año fiscal.

La razón oficial es "unificación de toolchain". Rajesh Jha, vicepresidente ejecutivo de la división, dijo que Claude Code sirvió como referencia valiosa, pero que Copilot CLI ofrece un producto que Microsoft puede moldear directamente. La razón no oficial, según múltiples fuentes, es que Claude Code se había vuelto "quizás un poco demasiado popular" entre los ingenieros de Microsoft, generando costos de tokens que escalaban más rápido de lo que nadie había proyectado.

La ironía es notable. Microsoft es el mayor inversor de OpenAI, dueño de GitHub, y ha apostado su identidad corporativa al liderazgo en IA. Pero cuando sus propios ingenieros prefieren la herramienta de Anthropic sobre la propia, la decisión de negocios es clara: es mejor forzar la adopción interna de Copilot, aunque sea inferior, que seguir pagando la factura de Claude Code.

Esto no es un caso aislado. En abril de 2026, GitHub — propiedad de Microsoft — anunció que todos los planes de Copilot pasarían a [facturación por uso](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) a partir del 1 de junio. La semana anterior, había [pausado las nuevas suscripciones](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/) de Copilot Pro y Pro+ porque los costos de inferencia de los usuarios intensivos superaban el precio mensual del plan. Como lo resumió The Register, Microsoft está cerrando el buffet de IA: el modelo de suscripción plana no cubre los costos cuando los usuarios abusan del servicio.

El CEO de NVIDIA, Jensen Huang, dijo recientemente que los CEOs que culpan a la IA por los despidos están siendo *"flojos"* y usando la tecnología como excusa. Quizás. Pero cuando la empresa que más ha invertido en IA del mundo retira licencias a sus propios ingenieros por costos, algo está cambiando.

---

## 3. Starbucks: cuando la IA no distingue los tipos de leche

En septiembre de 2025, Starbucks lanzó "Automated Counting", un sistema basado en visión computarizada desarrollado por NomadGo. Los baristas usarían tablets con cámaras y LIDAR (detección por luz y distancia) para escanear estantes de leches, jarabes y otros ingredientes. El sistema, según el comunicado oficial, contaría el inventario ocho veces más rápido que el método manual, con un 99% de precisión, y permitiría a los empleados *"pasar más tiempo haciendo café y conectándose con los clientes"*.

Nueve meses después, [Reuters](https://www.aol.com/articles/exclusive-starbucks-scraps-ai-inventory-185730000.html) reveló que Starbucks estaba retirando el sistema de todas sus más de 11.000 tiendas en Norteamérica. Un newsletter interno fechado el 19 de mayo de 2026 decía: *"A partir de hoy, Automated Counting será retirado. Los componentes de bebidas y la leche se contarán de la misma manera que las otras categorías de inventario."* Es decir, a mano.

¿Qué pasó? Según reportó Reuters ya en febrero de 2026, el sistema confundía tipos similares de leche, no reconocía productos, y en un [video promocional](https://www.aol.com/articles/exclusive-starbucks-scraps-ai-inventory-185730000.html) que la propia Starbucks había subido, se veía a la herramienta fallando al detectar una botella de jarabe de menta en el estante mientras contaba las botellas de al lado.

El problema no era técnico, era estructural. Cuando un sistema de IA requiere que el usuario verifique cada salida manualmente, no está ahorrando trabajo: lo está duplicando. Los baristas terminaban haciendo dos ciclos de inventario donde antes hacían uno. La eficiencia prometida se convertía en una carga cognitiva adicional.

El caso Starbucks ilustra una lección que se repite en múltiples industrias. La visión computarizada en entornos operativos requiere una precisión casi perfecta para que los trabajadores confíen en ella. Por debajo de ese umbral, el trabajador verifica cada salida. Y si el trabajador verifica cada salida, el software no ha reducido trabajo: lo ha redistribuido. El caso de eficiencia colapsa por completo.

---

## 4. NVIDIA: el vendedor de palas admite que la fiebre del oro es cara

En abril de 2026, Bryan Catanzaro, vicepresidente de Applied Deep Learning de NVIDIA, dijo a Axios: *"Para mi equipo, el costo del cómputo está muy por encima del costo de los empleados."*

La frase merece contexto. Catanzaro lidera un equipo de investigación en deep learning dentro de NVIDIA — literalmente uno de los grupos más intensivos en GPUs del planeta. Sus cargas de trabajo (entrenamiento de modelos, pipelines de inferencia, pruebas iterativas) son inherentemente costosas en cómputo. No es una afirmación que pueda extrapolarse a toda la economía: el equipo de Catanzaro vive en el extremo más intensivo en cómputo del espectro de IA.

Pero el hecho de que provenga del principal vendedor de la infraestructura de IA es lo que le da peso. Es como si el vendedor de palas en la fiebre del oro admitiera que las palas cuestan más que el oro que se encuentra con ellas. El comentario tuvo más de 2.500 upvotes en Reddit, no porque sorprendiera a los que trabajan en el campo, sino porque alguien con autoridad finalmente dijo en público lo que los equipos financieros vienen descubriendo en privado.

Un [estudio del MIT de 2024](https://www.csail.mit.edu/news/rethinking-ais-impact-mit-csail-study-reveals-economic-limits-job-automation) respalda esta visión. Analizando 1.000 categorías de tareas visuales automatizables, los investigadores encontraron que solo el 23% eran económicamente viables para reemplazo por IA a los costos actuales. En el 77% restante, los humanos seguían siendo más baratos.

Mes y medio después, el CEO de NVIDIA, Jensen Huang, contradijo implícitamente a su propio vicepresidente. En una entrevista con [Channel NewsAsia](https://www.channelnewsasia.com/shorts/narrative-connects-ai-job-loss-too-lazy-nvidia-ceo-jensen-huang-6139891), Huang dijo que los CEOs que vinculan la IA con despidos están siendo *"flojos"* y usando la tecnología para *"sonar inteligentes"*. *"La IA acaba de llegar. ¿Cómo es posible que ya estén perdiendo empleos?"*, preguntó.

La contradicción entre Catanzaro y Huang no es una hipocresía. Es la tensión natural entre la realidad operativa de la IA (es cara) y la necesidad comercial de venderla (va a ser más barata). Ambas cosas pueden ser ciertas en diferentes horizontes de tiempo.

---

## 5. El patrón: no son casos aislados

Los cuatro casos no son anomalías. Son la punta visible de un patrón que los datos confirman.

La consultora Sinch encuestó a 2.527 tomadores de decisiones en 10 países y encontró que el 74% de las empresas que desplegaron agentes de IA en servicio al cliente ya los retiraron. La tasa sube al 81% entre las organizaciones con controles de gobierno más maduros. El 84% de los equipos de IA pasa al menos la mitad de su tiempo en infraestructura de seguridad, no en desarrollar IA.

La firma G-P encuestó a ejecutivos globales y encontró que el [73% reportó](https://www.fairplaytalks.com/2026/05/20/seven-in-10-companies-could-slash-ai-budgets-as-roi-disappoints-report-finds/) que al menos algunas inversiones en IA no cumplieron expectativas, y el 70% está dispuesto a recortar presupuestos si no se alcanzan las metas de ROI. El número de empresas que se describen como "agresivamente" usando IA para innovar cayó del 60% al 42%.

S&P Global Market Intelligence documentó que el [42% de las empresas](https://www.forbes.com/sites/josipamajic/2026/05/25/the-ceo-ai-confidence-gap-is-costing-enterprises-billions/) abandonaron la mayoría de sus iniciativas de IA en 2025, frente al 17% del año anterior. La organización promedio canceló casi la mitad de sus proofs-of-concept antes de llegar a producción.

Y Gartner, la consultora que inventó el Hype Cycle, colocó a la IA generativa explícitamente en el ["valle de la desilusión" (trough of disillusionment)](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026). Solo el 28% de los proyectos de infraestructura de IA entregan completamente contra su caso de negocio (el 72% restante no cumple lo prometido), y el 25% del presupuesto planificado para 2026 se deslizará a 2027.

Klarna, la abanderada del reemplazo laboral, comenzó a [recontratar agentes humanos](https://officechai.com/ai/how-uber-microsoft-klarna-and-others-are-pulling-back-from-ai/) después de que la satisfacción del cliente cayera 22%. Su CEO admitió: *"Nos enfocamos demasiado en eficiencia y costo. El resultado fue menor calidad."* El Commonwealth Bank of Australia reemplazó 45 agentes con un bot de voz y [revirtió la decisión](https://officechai.com/ai/how-uber-microsoft-klarna-and-others-are-pulling-back-from-ai/) un mes después, disculpándose y ofreciendo salarios caídos.

El patrón no es que la IA no funcione. Es que funciona bien en laboratorio y mal en producción. Funciona bien en tareas acotadas y mal en flujos complejos. Funciona bien cuando el costo lo absorbe el VC y mal cuando lo tiene que pagar el CFO.

---

## 6. La burbuja de los $725 mil millones

Detrás de estos retrocesos hay una realidad macroeconómica que merece atención.

En 2026, las cuatro grandes empresas tecnológicas — Amazon, Google, Microsoft y Meta — gastarán un total de aproximadamente [$725 mil millones](https://bkobog.substack.com/p/the-ai-capex-supercycle-725-billion) en capex (gasto de capital: inversión en infraestructura física como centros de datos y GPUs), un 77% más que en 2025. Es la inversión en infraestructura privada más grande en un solo año en la historia de la humanidad. Amazon sola gastará más en capex que todo el sector eléctrico estadounidense.

Goldman Sachs calcula que, para mantener los retornos actuales sobre el capital invertido, estas empresas necesitan generar aproximadamente [$1 billón en ingresos anuales adicionales](https://bkobog.substack.com/p/the-ai-capex-supercycle-725-billion) para 2027. Las estimaciones actuales de consenso proyectan $450 mil millones. Hay una brecha de 2x entre lo que el gasto requiere y lo que los analistas esperan.

JPMorgan fue más específico: para que la inversión acumulada en IA genere un retorno del 10% para 2030, la industria necesitaría producir unos [$650 mil millones](https://www.cnbc.com/2026/05/21/ai-spending-expected-to-top-1-trillion-in-2-years-why-that-estimate-may-be-too-low.html) en ingresos anuales adicionales. Hoy, los ingresos de IA empresarial rondan los $90 mil millones. Cerrar esa brecha requiere un crecimiento compuesto cercano al 50% anual durante cinco años. Cloud computing, en su década de mayor expansión, creció al 40%.

El flujo de caja libre (free cash flow: el efectivo que queda después de gastos operativos y de capital) de los hiperescaladores (las megaprocesadoras tecnológicas: Amazon, Google, Microsoft, Meta) ya muestra la presión. Meta cayó de $26 mil millones en el primer trimestre de 2025 a $1.2 mil millones en el mismo período de 2026. Microsoft vio su margen de flujo de caja libre reducirse del 30% al 25%. La correlación entre los precios de las acciones de los cuatro gigantes — que históricamente se movían juntos — cayó del 80% al 20%, señal de que el mercado está empezando a diferenciar entre los que pueden monetizar la IA y los que no.

Nadie está diciendo que la IA colapsará como las punto-com. La diferencia clave es que este dinero se gastó en activos físicos (GPUs, data centers, redes eléctricas), no en acciones especulativas. Pero eso también significa que el dinero ya está gastado y no se recupera fácilmente. Los data centers no se mudan. Las GPUs se pueden revender, pero a pérdida si la demanda se contrae.

---

## 7. Donde la IA sí funciona

Un análisis equilibrado requiere reconocer que no todo es negativo. La IA está generando valor real en áreas específicas.

La productividad en codificación asistida está documentada. Uber, a pesar del problema de presupuesto, produce ~70% de su código con IA. Eso tiene un valor real, aunque sea difícil de cuantificar en términos de funcionalidades entregadas.

La infraestructura de IA está impulsando avances en salud (diagnóstico por imágenes, descubrimiento de fármacos), logística (optimización de rutas, gestión de inventarios en entornos controlados) y ciencia climática (modelos de predicción meteorológica, eficiencia energética). En estos sectores, el costo de la IA se justifica porque el valor del acierto — o el costo del error — es mucho mayor que en una tarea administrativa.

El propio Gartner proyecta que los costos de inferencia para modelos de 1 billón de parámetros caerán más del [90% en los próximos cuatro años](https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025). Si esa proyección se cumple, la ecuación económica actual se invierte: lo que hoy es caro será barato. El problema es el timing — las empresas están gastando como si esa caída ya hubiera ocurrido.

Los ingresos de IA empresarial crecen al 40% anual. El backlog de Google Cloud casi se duplicó trimestre contra trimestre. NVIDIA reporta ingresos récord cada trimestre. Hay demanda real, no solo hype. La pregunta es si la demanda puede crecer lo suficientemente rápido para justificar la montaña de capex que ya se comprometió.

---

## 8. El contraste paraguayo: ¿llegamos tarde o justo a tiempo?

Todo lo anterior importa poco si no se conecta con la realidad local. Porque Paraguay está apostando su recurso más valioso — la energía de Itaipú — a esta misma industria, justo cuando el mercado global muestra señales de corrección. [La apuesta tiene nombre concreto: Yguazú Digital]({% post_url 2026-06-23-yguazu-digital-paraguay-hub-ia-mas-grande-del-mundo %}), [en un país que recién está abriendo su sector eléctrico al capital privado]({% post_url 2026-05-27-apertura-sector-electrico-privado-paraguay %}).

Los proyectos anunciados son de una escala que el país nunca vio. X8 Cloud planea invertir entre [$10 y $50 mil millones](https://www.asunciontimes.com/paraguay-news/national-news/ai-data-centre-paraguay-a-historic-moment-for-the-nation/) en 30 años para construir el centro de datos de IA "más grande de América Latina", con un target de 5 GW de capacidad. Yguazú Digital, la alianza con Taiwán, proyecta tres fases que culminan en una inversión de [$40 mil millones](https://www.abc.com.py/economia/2026/05/13/centro-de-datos-soberano-con-taiwan-ministro-de-industria-habla-de-inversion-de-us-40000-millones/) — equivalente al PIB total de Paraguay — para consumir 1.000 MW. Hive Digital ya invirtió [$400 millones](https://www.bnamericas.com/en/interviews/paraguays-multimillion-ai-data-center-surge-latams-new-frontier) y está expandiendo sus centros a 400 MW. Crusoe AI y Peter Thiel están explorando el país.

Paraguay tiene lo que la IA necesita: energía barata ($0.04/kWh), 100% renovable, y un gobierno dispuesto a recibirla. El ministro de Industria, Marco Riquelme, viajó a Silicon Valley y se reunió con ejecutivos de NVIDIA, OpenAI y Crusoe. El presidente Peña firmó acuerdos con Taiwán y recibió a Thiel en la residencia presidencial.

Pero la lección de la criptominería debería darnos una pausa. Hoy, 41 empresas del Grupo de Consumo Intensivo Especial consumen ~944 MW, equivalentes al 13.5% de la energía paraguaya de Itaipú, o 1.4 turbinas completas. Generan apenas [1.58 empleos por MW](https://www.abc.com.py/economia/2026/03/16/solo-cuatro-criptomineras-consumen-mas-que-una-turbina-de-itaipu/). El 66% no paga aportes al IPS. Y hay denuncias de que altos directivos de ANDE cobran hasta $500.000 mensuales en coimas de operaciones ilegales.

Los centros de datos de IA tienen el mismo perfil: alta intensidad energética, baja creación de empleo. El proyecto insignia de Crusoe en Texas, Abilene, consumirá 1.2 GW y generará unos pocos cientos de empleos permanentes. Para un país que necesita empleo formal y diversificación económica, la ecuación no es automáticamente favorable.

Y luego está el timing. Paraguay está entrando al mercado de centros de datos de IA en 2026, exactamente cuando:
- Gartner coloca a la IA en el "valle de la desilusión" (trough of disillusionment)
- Los hiperescaladores (Amazon, Google, Microsoft, Meta) muestran fatiga financiera
- Las empresas están retrocediendo en proyectos de IA
- La brecha entre capex e ingresos está en máximos históricos

Los contratos que exigen las empresas como X8 Cloud son de 30 a 50 años. Si la burbuja de IA se desinfla en los próximos 5 años, Paraguay podría quedar atrapado en contratos desfavorables, con energía comprometida, infraestructura construida y beneficios que nunca llegaron. Los excedentes energéticos que el ministro Riquelme da por seguros podrían agotarse entre [2030 y 2033](https://www.abc.com.py/economia/2025/04/24/senado-pide-informe-urgente-a-la-ande-sobre-crisis-electrica-pronosticada-para-el-2029/) según el expresidente de ANDE, Pedro Ferreira. La UIP advierte sobre apagones recurrentes a partir de 2029.

No se trata de decir que no a la inversión. Se trata de preguntar, antes de firmar contratos que comprometen recursos estratégicos por décadas, si el riesgo está siendo evaluado con la misma profundidad con la que se evalúa el beneficio potencial. Porque las empresas que negocian estos acuerdos tienen equipos de análisis de riesgo global. Paraguay tiene un Viceministerio, una ANDE con historial de corrupción, y una ley de protección de datos que no entra en vigor hasta noviembre de 2027.

---

## No es el fin. Es el fin del principio.

La pregunta del post viral — ¿estamos viendo el principio del fin de la burbuja IA? — probablemente es la pregunta incorrecta. Una burbuja no termina de golpe. Se desinfla gradualmente, a medida que los inversores, los CFOs y los gobiernos ajustan sus expectativas a la realidad.

Lo que estamos viendo no es el colapso de la IA. Es el fin de la fase experimental, la fase en que las empresas estaban dispuestas a absorber costos arbitrarios de tokens a cambio de aprendizaje. Ese aprendizaje ya ocurrió. Ahora viene la parte difícil: demostrar que la IA genera valor económico real, no solo métricas de adopción impresionantes.

Para las grandes empresas tecnológicas, la pregunta es si los $725 mil millones en capex de 2026 generarán los $1 billón en ingresos que necesitan para justificarse. Para las startups y consultoras, la pregunta es si el mercado seguirá comprando la promesa del reemplazo laboral cuando los datos muestran que, por ahora, la IA cuesta más que el humano que reemplaza.

Y para Paraguay, la pregunta es más urgente que para nadie. Porque cuando firmas un contrato a 50 años comprometiendo tu energía, no te puedes permitir el lujo de esperar a que la burbuja se desinfle para descubrir que llegaste tarde.

La tecnología no necesita ser una burbuja para ser una mala inversión para un país con instituciones frágiles. Necesita apenas no cumplir las promesas con las que se vendió. Y en eso, la historia de la tecnología tiene un precedente que Paraguay debería considerar antes de firmar la próxima línea de transmisión.

---

## Fuentes

<ol class="sources-list">
<li>**The Information** — Uber CTO confirma agotamiento de presupuesto IA 2026 (abril 2026): reportaje original (detrás de paywall)</li>
<li><strong>Fortune</strong> – <a href="https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/">"Nvidia executive: The cost of AI tools is far beyond the cost of human workers"</a> (28 abril 2026)</li>
<li>**Axios** — Entrevista original a Bryan Catanzaro, NVIDIA VP (abril 2026)</li>
<li>**Reuters** — "Starbucks scraps AI inventory tool across North America" (21 mayo 2026): reportaje original</li>
<li><strong>CNBC</strong> – <a href="https://www.cnbc.com/2026/05/21/starbucks-scraps-ai-inventory-tool-across-north-america.html">"Starbucks scraps AI inventory tool across North America"</a> (21 mayo 2026)</li>
<li>**Windows Central** — Microsoft cancelling Claude Code licences (mayo 2026): reportaje original</li>
<li>**The Verge** — Cobertura de Microsoft y declaraciones Andrew Macdonald (Uber)</li>
<li><strong>GitHub Blog</strong> – <a href="https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/">"GitHub Copilot is moving to usage-based billing"</a> (27 abril 2026)</li>
<li><strong>GitHub Blog</strong> – <a href="https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/">"Changes to GitHub Copilot Individual plans"</a> (20 abril 2026)</li>
<li><strong>The Register</strong> – "Microsoft's GitHub shifts to metered AI billing" (28 abril 2026)</li>
<li><strong>The Register</strong> – "AI customer service bots get rolled back at 74% of firms" (13 mayo 2026)</li>
<li><strong>The Next Web</strong> – <a href="https://thenextweb.com/news/microsoft-claude-code-retreat-ai-cost">"Microsoft's quiet Claude Code retreat and the real cost of enterprise AI"</a> (25 mayo 2026)</li>
<li><strong>Forbes</strong> – <a href="https://www.forbes.com/sites/josipamajic/2026/05/25/the-ceo-ai-confidence-gap-is-costing-enterprises-billions/">"The CEO AI Confidence Gap Is Costing Enterprises Billions"</a> (25 mayo 2026)</li>
<li><strong>Fair Play Talks</strong> – <a href="https://www.fairplaytalks.com/2026/05/20/seven-in-10-companies-could-slash-ai-budgets-as-roi-disappoints-report-finds/">"Seven in 10 Companies Could Slash AI Budgets as ROI Disappoints"</a> (20 mayo 2026)</li>
<li><strong>CNBC</strong> – <a href="https://www.cnbc.com/2026/05/21/ai-spending-expected-to-top-1-trillion-in-2-years-why-that-estimate-may-be-too-low.html">"AI spending expected to top $1 trillion in 2 years"</a> (21 mayo 2026)</li>
<li><strong>CNBC</strong> – <a href="https://www.cnbc.com/2026/04/30/ai-boom-big-tech-capital-expenditures-now-seen-topping-1-trillion-in-2027-.html">"AI boom: Big Tech capital expenditures now seen topping $1 trillion in 2027"</a> (30 abril 2026)</li>
<li><strong>Gartner</strong> – <a href="https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026">"Worldwide AI Spending Will Total $2.5 Trillion in 2026"</a> (15 enero 2026)</li>
<li><strong>OfficeChai</strong> – <a href="https://officechai.com/ai/how-uber-microsoft-klarna-and-others-are-pulling-back-from-ai/">"How Uber, Microsoft, Klarna and Others Are Pulling Back From AI"</a> (27 mayo 2026)</li>
<li><strong>BNamericas</strong> – <a href="https://www.bnamericas.com/en/interviews/paraguays-multimillion-ai-data-center-surge-latams-new-frontier">"Paraguay's multimillion AI data center surge: LatAm's new frontier?"</a> (abril 2026)</li>
<li><strong>BNamericas</strong> – <a href="https://www.bnamericas.com/en/interviews/my-goal-is-to-reach-5gw-of-ai-says-x8-cloud-about-mega-project-in-paraguay">"My goal is to reach 5GW of AI, says X8 Cloud"</a> (septiembre 2025)</li>
<li><strong>ABC Color</strong> – <a href="https://www.abc.com.py/economia/2026/05/13/centro-de-datos-soberano-con-taiwan-ministro-de-industria-habla-de-inversion-de-us-40000-millones/">"Centro de datos soberano con Taiwán: inversión de US$ 40.000 millones"</a> (13 mayo 2026)</li>
<li><strong>ABC Color</strong> – <a href="https://www.abc.com.py/economia/2026/03/16/solo-cuatro-criptomineras-consumen-mas-que-una-turbina-de-itaipu/">"Solo cuatro criptomineras consumen más que una turbina de Itaipú"</a> (16 marzo 2026)</li>
<li><strong>ABC Color</strong> – <a href="https://www.abc.com.py/economia/2025/04/24/senado-pide-informe-urgente-a-la-ande-sobre-crisis-electrica-pronosticada-para-el-2029/">"Senado pide informe urgente a la ANDE sobre crisis eléctrica"</a> (24 abril 2025)</li>
<li><strong>Asunción Times</strong> – <a href="https://asunciontimes.com/paraguay-news/national-news/ai-data-centre-paraguay-a-historic-moment-for-the-nation/">"AI Data Centre Paraguay: biggest-ever foreign investment"</a> (diciembre 2025)</li>
<li><strong>Startup Fortune</strong> – <a href="https://startupfortune.com/uber-burned-its-entire-2026-ai-budget-in-four-months-and-claude-code-is-why-finance-teams-should-be-worried/">"Uber Burned Its Entire 2026 AI Budget in Four Months"</a> (2 mayo 2026)</li>
<li><strong>Startup Fortune</strong> – <a href="https://startupfortune.com/an-nvidia-vp-just-said-ai-costs-more-than-the-people-its-supposed-to-replace-and-every-founder-selling-labor-replacement-should-read-that-carefully/">"An Nvidia VP Just Said AI Costs More Than the People It's Supposed to Replace"</a> (4 mayo 2026)</li>
<li><strong>Tom's Hardware</strong> – <a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-exec-says-ai-is-more-expensive-than-actual-workers-yet-some-companies-dont-see-the-extra-costs-as-a-negative">"Nvidia exec says AI is more expensive than actual workers"</a> (29 abril 2026)</li>
<li><strong>Agencia IP</strong> – <a href="https://www.ip.gov.py/ip/2026/03/19/con-alianzas-claves-paraguay-se-posiciona-como-jugador-relevante-en-la-industria-de-la-inteligencia-artificial/">"Con alianzas claves, Paraguay se posiciona como jugador relevante en la industria IA"</a> (marzo 2026)</li>
<li><strong>The Street</strong> – <a href="https://www.thestreet.com/restaurants/starbucks-investors-get-tough-luck-news-on-ai-inventory-bet">"Starbucks investors get tough-luck news on AI inventory bet"</a> (24 mayo 2026)</li>
<li><strong>Cryptobriefing</strong> – <a href="https://cryptobriefing.com/uber-questions-ai-spending-effectiveness/">"Uber questions AI spending effectiveness as budget runs dry"</a> (26 mayo 2026)</li>
<li><strong>A.L. Capital Advisory</strong> – <a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html">"AI Capex Cycle 2026: $725B Hyperscaler Buildout — CFA Analysis"</a> (enero 2026)</li>
<li><strong>Benson Kong</strong> – <a href="https://bkobog.substack.com/p/the-ai-capex-supercycle-725-billion">"The AI Capex Supercycle: $725 Billion, Bottlenecks Everywhere"</a> (mayo 2026)</li>
<li>**Channel NewsAsia** — Jensen Huang entrevista (mayo 2026): citado en Financial Express</li>
<li>**MIT Technology Review** — Economic viability of AI automation study (2024)</li>
<li>**S&P Global Market Intelligence** — AI initiative abandonment rates (2025-2026)</li>
<li>**RAND Corporation** — AI project failure rates vs. non-AI projects</li>
<li><strong>TechTimes</strong> – <a href="https://www.techtimes.com/articles/317058/20260523/starbucks-retires-nomadgo-inventory-ai-across-11000-stores-workers-had-recount-every-scan.htm">"Starbucks Retires NomadGo Inventory AI Across 11,000 Stores"</a> (23 mayo 2026)</li>
<li><strong>Gartner</strong> – <a href="https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025">"Cost of LLM Inference Will Drop Over 90% by 2030"</a> (25 marzo 2026)</li>
<li><strong>PRNewswire / Sinch</strong> – <a href="https://www.prnewswire.com/news-releases/sinch-research-reveals-74-of-enterprises-have-rolled-back-live-ai-customer-communications-agents-302770750.html">"Sinch research reveals 74% of enterprises have rolled back live AI customer communications agents"</a> (13 mayo 2026)</li>
</ol>