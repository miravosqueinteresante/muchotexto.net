---
layout: post
title: "Soja, ganado y blockchain: la tokenización del agro en Paraguay"
date: 2026-05-18
last_modified_at: 2026-05-18
categories: articulos
tags: tech-ecosistema
description: "La Ley 7572 abre la puerta a tokenizar soja, ganado y tierras en blockchain. Lo que la tokenización del agro significa para Paraguay."
---

Hay una idea que está girando en los círculos fintech paraguayos y que promete cambiar quién financia el campo, cómo se vende la cosecha y hasta quién puede ser dueño de un pedazo de tierra sin moverse de su casa. Se llama tokenización agropecuaria, y la noticia ya tiene título: "Paraguay abre las puertas para la tokenización del agro", publicó ABC Color. Bruno Vaccotti, director de la Cámara Paraguaya de Fintech, hablaba de tokenizar ganado, granos y tierras. La Ley 7572/2025 del Mercado de Valores y Productos ya reconoce instrumentos emitidos en tecnología de registro distribuido — blockchain, para entendernos — y los reglamentos secundarios están en camino.

La promesa es tentadora. Un productor agropecuario podría dividir su tierra, su cosecha o su ganado en tokens digitales y venderlos a inversores de todo el mundo. Un inversor en Seúl podría ser dueño de milésimas de una hectárea en San Pedro sin moverse de su casa. El productor consigue financiamiento sin pasar por un banco que le cobra hasta 18% anual. El inversor diversifica con un activo real que no está correlacionado con los mercados de renta variable. Suena lindo, ¿no?

Pero las promesas en tecnología financiera tienen un historial que conviene revisar antes de subirse al carro. Este artículo es eso: una revisión de lo que promete la tokenización agropecuaria, lo que realmente ha pasado en el mundo cuando se intentó, lo que Paraguay tiene a favor, lo que no tiene todavía, y lo que debería pasar antes de que te entusiasmes demasiado.

---

## 1. La noticia y el contexto

La Ley N.° 7572/2025, promulgada el 7 de noviembre de 2025, derogó el mosaico normativo anterior (Ley 5810/2017 y varias otras) y estableció un marco unificado para el mercado de valores y productos en Paraguay. Su Artículo 73 es el que importa acá: reconoce como valores "aquellos emitidos, registrados, transferidos o almacenados mediante tecnologías de registros distribuidos u otras similares". Traducción: si emitís un token que representa derechos de crédito, propiedad o participación, la ley lo considera un valor y está sujeto a supervisión de la Superintendencia de Valores (SIV).

Bruno Vaccotti lo resumió bien en la entrevista con ABC: Paraguay puede tokenizar su producción agropecuaria, empezando por ganado vacuno y granos. La Cámara de Fintech, que ya tiene un comité de blockchain liderado por Fernando Arriola, está trabajando en los próximos pasos.

El superintendente de Valores, Rodrigo Ruiz, anunció una hoja de ruta en dos generaciones: la primera en 2026, con reglamentos sobre custodia digital, ciberseguridad y emisión de instrumentos digitales; la segunda, con innovación plena como fondos privados, crowdfunding y tokenización DLT completa.

Suena bien sobre el papel. Pero hay una diferencia enorme entre tener una ley y tener un ecosistema funcional.

---

## 2. Cómo funciona esto en simple (y por qué es más complejo de lo que parece)

El modelo básico de la tokenización de activos reales (RWA, por real-world assets) es siempre el mismo:

1. Un activo físico — digamos, 100 hectáreas de soja o 500 cabezas de ganado — se transfiere a un vehículo legal (un SPV, un fideicomiso, una LLC).
2. Ese vehículo emite tokens digitales que representan participaciones económicas en el activo.
3. Los tokens se venden a inversores a través de una plataforma.
4. Los retornos (renta de la tierra, venta de la cosecha, engorde del ganado) se distribuyen a los dueños de los tokens.

El dueño del token **no es dueño del activo físico**. Es dueño de un derecho contractual contra el vehículo que posee el activo. Esto no es una sutileza legal: es la diferencia entre tener una acción de una empresa que posee un campo y tener el campo. Si el campo se quema, si hay una sequía, si el SPV quiebra, el token vale lo que valga el reclamo legal del dueño, no lo que vale la tierra.

Agrotoken, la empresa argentina más grande del sector (hoy parte del ecosistema Justoken), usa el modelo de 1 token = 1 tonelada de grano almacenado en depósitos auditados. Un productor lleva su soja a un almacén, se verifica la cantidad, y se emiten tokens SOYA que pueden venderse, usarse como garantía o gastarse con una tarjeta Visa. PecuToken hace lo mismo con ganado: 1 token por arroba de carne.

Finka, en Suiza, usa un modelo distinto: un ISIN (identificador financiero tradicional) que representa derechos sobre los ingresos netos de un rodeo de 4.300 cabezas en un rancho de 3.200 hectáreas. Cumple con la regulación suiza, la más madura del mundo para tokenización (su DLT Act está vigente desde 2021).

LandX, un protocolo DeFi, hace algo más radical: los agricultores comprometen una parte de su cosecha futura a cambio de financiamiento inmediato, y los inversores reciben rendimientos diarios en stablecoins. Tiene un TVL de apenas USD 1,77 millones — diminuto comparado con los mercados que pretende reemplazar.

Cada uno de estos modelos tiene problemas diferentes. Agrotoken depende de la verificación física del grano (Proof of Grain Reserves). LandX depende de validadores locales que verifican que el agricultor realmente sembró. Finka depende de la estructura legal suiza. Ningún modelo es perfecto, y varios han fracasado estrepitosamente.

---

## 3. Casos reales: los que funcionan y los que no

Empecemos por los que funcionan, porque existen y vale la pena estudiarlos.

**Agrotoken/Justoken** es, por lejos, el caso más grande y relevante para Paraguay. Nacido en Argentina en 2020, hoy opera en Brasil y tiene planes explícitos de expansión a Paraguay y Uruguay. Ha tokenizado más de 230.000 toneladas de soja, maíz y trigo. En la Bolsa de Brasil (B3) tiene dos fondos tokenizados — JSOY (soja, USD 100 millones en activos) y JSOY_OIL (aceite de soja, USD 481 millones) — que suman más de USD 581 millones. Tiene inversores como Bunge, Visa y el Banco do Brasil. Su modelo de infraestructura como servicio (Justoken) permite que terceros usen su plataforma para tokenizar sus propios activos. Es, sin discusión, el caso más maduro y relevante.

**AgriDigital** en Australia es otro éxito, pero de un tipo diferente. No tokeniza para inversión, sino que digitaliza la cadena de suministro de granos. Procesa más de 5,2 millones de toneladas al año y ha supervisado más de USD 1.000 millones en transacciones. Blockchain le sirve para trazabilidad y pagos automáticos al transferir el título, no para emitir tokens de inversión. Es una muestra de que el mayor valor de blockchain en el agro quizás no está en la tokenización financiera, sino en la eficiencia operativa.

**Farmway Technologies**, con sede en EE.UU. pero operaciones globales, tokenizó más de USD 250 millones en activos agrícolas. Su acuerdo más notable: USD 100 millones con el gobierno de Georgia para tokenizar 500 hectáreas de almendros. Tiene financiamiento de USAID y la Unión Europea.

**Finka** en Suiza es el modelo de cumplimiento regulatorio: un token con ISIN, supervisado por FINMA, que representa ingresos de un rodeo ganadero real en Bolivia (el rancho La Pradera, de 3.200 hectáreas y más de 3.500 cabezas). Es un ejemplo relevante de cómo se puede estructurar legalmente un token agropecuario con estándares suizos, aunque el activo subyacente esté en otro país.

Ahora hablemos de los que no funcionaron.

**Agrocoin** (México, 2018): prometía rendimientos del 30% tokenizando chile habanero. La producción nunca existió. El fundador Rodrigo Domenzain fue arrestado en Cancún en 2019. Las pérdidas estimadas superan los USD 20 millones. Es el caso más conocido de fraude en tokenización agropecuaria.

**Cropto** (Turquía): tokeniza 20 productos agrícolas con un modelo de 1 kg = 1 token. Está listado en exchanges centralizados. También está señalado por falta de registro legal verificable, tráfico web casi nulo y ninguna divulgación regulatoria. Posible estafa.

**Malu Grape** (China, 2024): el primer RWA agrícola de China. Recaudó 10 millones de yuanes en capital accionario y 200.000 yuanes en NFTs. Terminó siendo un fracaso como RWA: los NFTs eran tarjetas de preventa al consumo, no activos con rendimiento; el SPV concentraba el gobierno excluyendo a los agricultores; el trading estaba restringido a menos de 10 operaciones diarias en el Shanghai Data Exchange; fue deslistado en 2025.

Y luego está el problema general de los hacks. Según CertiK, las pérdidas en exploits de RWA fueron de USD 17,9 millones en 2023, USD 6 millones en 2024 y USD 14,6 millones solo en la primera mitad de 2025 (un aumento del 143%). El 90% de los smart contracts explotados habían sido auditados (Olympix, 2026). Las auditorías no son una garantía: son una foto en un momento dado, y el código cambia.

---

## 4. Lo que Paraguay tiene a favor

Paraguay no parte de cero. De hecho, parte con ventajas que muchos países envidiarían.

**Energía**. Es la ventaja más obvia y más mencionada. Itaipú es la segunda hidroeléctrica más grande del mundo por generación anual, y Paraguay tiene electricidad industrial a ~USD 0,04/kWh, 100% renovable. El excedente energético se vende a Brasil a un precio irrisorio, y los mineros de Bitcoin ya aprovechan esta ventaja (~USD 40/MWh). Esto no solo atrae minería: atrae infraestructura blockchain. Y la tokenización necesita blockchain.

**Marco legal**. La Ley 7572/2025 es real y está vigente. No es un proyecto ni una promesa de campaña. Reconoce los tokens como valores. La Superintendencia de Valores está trabajando en los reglamentos. La Cámara de Fintech está activa. Hay una hoja de ruta. En comparación con la mayoría de los países de la región, Paraguay tiene una ventaja regulatoria clara.

**Producción agropecuaria**. Paraguay es el 4° exportador mundial de soja y uno de los mayores exportadores de carne bovina del planeta. Los modelos de Agrotoken (soja, maíz, trigo) y PecuToken (ganado) se mapean directamente sobre la estructura productiva del país. No hay que adaptar nada: el activo subyacente ya existe en escala masiva.

**Adopción digital**. El 94% de los paraguayos tiene teléfono móvil. El 84% usa internet. El sistema de pagos instantáneos (SPI/Sipap) procesa 28 millones de transacciones al mes. El 64% de los paraguayos ya paga con QR. La identidad electrónica (Identidad Electrónica del MITIC) está operativa con más de 400 trámites en línea. Paraguay no es Finlandia, pero tampoco es el desierto digital que muchos imaginan.

**Cultura de trueque**. El agro paraguayo ya usa mecanismos de intercambio no monetario: el productor entrega grano a cambio de insumos, el feedlot recibe animales a cambio de engorde. La tokenización es, en cierto sentido, una evolución digital de una práctica que ya existe.

**Cooperativas**. Cerca de 600 cooperativas activas con 1,8 millones de socios (51% de la población económicamente activa). Son canales de distribución y confianza que ninguna plataforma tecnológica podría construir desde cero.

---

## 5. Lo que Paraguay NO tiene todavía

Acá está el problema: tener energía y una ley no es suficiente. Paraguay necesita, antes de la tokenización masiva, varias cosas que no tiene.

### a. Catastro y títulos de propiedad completos

El nuevo Registro Único Nacional (RUN), lanzado en enero de 2026, reemplazó 150 años de registros en papel. Es un avance enorme. Pero el Banco Interamericano de Desarrollo, que financia el programa de modernización catastral (PR-L1061, USD 25 millones), pone un objetivo claro: llegar al 60% de cobertura de mapeo catastral rural. Eso significa que hoy, en 2026, probablemente menos del 60% de las tierras rurales tiene un registro digital claro y verificable.

Y el 40% de la tierra agrícola está en manos del 0,07% de los propietarios. La desigualdad en la tenencia de la tierra en Paraguay no es un detalle: es la estructura misma del campo. Tokenizar sin resolver primero quién es dueño de qué es emitir tokens sobre disputas. El Banco Mundial lo dice claro en sus estudios: los programas de titulación son "necesarios pero no suficientes" para el desarrollo rural.

### b. Educación financiera y digital

El promedio de alfabetización financiera en los países de la OCDE es de 63 sobre 100, según la encuesta OECD/INFE 2023. Paraguay no alcanza ese nivel: los datos de CAF, que aplican la misma metodología, ubican al país en un rango de 50-60. En áreas rurales, donde la tokenización tendría que llegar primero para ser útil, la alfabetización financiera es inevitablemente menor.

No es que la gente sea "ignorante". Es que el sistema financiero tradicional nunca llegó a esos lugares. El 30% de los distritos con más de 2.000 habitantes no tiene presencia bancaria. El 17% de la población vive en zonas sin sucursales. Pedirle a un productor que entienda wallets, gas fees, smart contracts, oráculos y riesgos de depegging cuando nunca tuvo una cuenta bancaria no es realista.

### c. Conectividad rural

El 82% de los paraguayos usa internet, sí. Pero la brecha urbano-rural persiste: 74% de cobertura rural contra 86% urbana (Internet Society, 2024). En el Chaco, donde está buena parte de la producción ganadera, la conectividad sigue siendo limitada. Starlink está llegando — 18 comunidades conectadas en enero de 2026 — pero falta mucho.

La tokenización no funciona sin conectividad. O, mejor dicho, funciona pero excluye a los productores más chicos, que son exactamente los que más necesitan alternativas de financiamiento.

### d. Sandbox regulatorio

Paraguay no tiene un sandbox regulatorio. Ni siquiera un "innovation hub" como los que operan en Brasil (BCB, desde 2020), México (CNBV, desde 2018), el Reino Unido (FCA, desde 2016) o los Emiratos Árabes Unidos (VARA, desde 2022). La Ley 7572 es de arquitectura gruesa; los reglamentos secundarios recién están en proceso. No hay un espacio controlado donde los proyectos puedan probar sin riesgo de violar normas que todavía no existen.

El Reino Unido reportó que el 75% de los proyectos que entraron a su sandbox completaron las pruebas exitosamente; de esos, el 90% obtuvo autorización plena. El sandbox no es solo protección al inversor: es un mecanismo de aprendizaje regulatorio.

### e. Auditoría y seguridad

No hay registro de auditores de smart contracts supervisado por la SIV. No hay requisito de auditoría obligatoria para contratos de tokenización. No hay un fondo de garantía para pérdidas por fallos técnicos.

Suiza exige auditoría técnica de smart contracts desde su DLT Act de 2021. VARA en Dubái exige auditoría de reservas segregadas. El Salvador, a través de la CNAD, exige auditoría de emisiones. Paraguay no exige nada de esto todavía. Y el 90% de los smart contracts explotados en DeFi habían sido auditados (Olympix, 2026). Una auditoría no es suficiente, pero no tener ninguna es negligencia.

### f. Protección de datos

La Ley de Protección de Datos Personales (Ley 7593/2025) se aprobó en noviembre de 2025. Está inspirada en el GDPR europeo y la LGPD brasileña. Tiene todos los elementos correctos: consentimiento explícito, derechos de acceso y cancelación, sanciones de hasta 10.000 salarios mínimos. Pero no entra en vigor hasta noviembre de 2027. La agencia reguladora aún no se ha creado. Los reglamentos secundarios no se han redactado.

Paraguay no tiene, hoy, ninguna ley de protección de datos efectiva. Una plataforma de tokenización que procese datos financieros de productores e inversores opera [en un país que está recibiendo inversiones billonarias en infraestructura de IA]({% post_url 2026-05-16-peter-thiel-paraguay-experimento %}) y [abriendo sectores estratégicos al capital privado]({% post_url 2026-05-27-apertura-sector-electrico-privado-paraguay %}) sin un marco de protección de datos que funcione.

---

## 6. ¿Qué hacer primero? Una propuesta

No se trata de decir "no a la tokenización". Se trata de hacerla bien. Acá va una secuencia posible, basada en lo que otros países han hecho y en lo que Paraguay necesita:

**Prioridad 1: Catastro rural completo.** El programa del BID (PR-L1061) tiene que llegar al 60% de cobertura catastral antes de que ningún token de tierra se emita masivamente. Sin título claro, no hay activo subyacente verificable. Tokenizar sobre propiedad dudosa es fabricar riesgos.

**Prioridad 2: Sandbox regulatorio agro-token.** El BCP y la SIV deberían crear, antes de fin de 2026, un sandbox específico para tokenización agropecuaria. Máximo 10 proyectos, emisión limitada a USD 5 millones por proyecto, inversor minorista limitado a USD 10.000, enfriamiento de 7 días, reporte mensual. El modelo del FCA británico — 75% de éxito en primera cohorte — es el benchmark.

**Prioridad 3: Educación vía cooperativas.** Las casi 600 cooperativas paraguayas activas con 1,8 millones de socios son el canal natural. No a través de apps ni cursos online, sino de extensionistas rurales, radio y módulos en el sistema de extensión del MAG. La alfabetización financiera digital no es un requisito previo: se construye paralelamente.

**Prioridad 4: Identidad digital rural.** La Identidad Electrónica del MITIC tiene que llegar al productor rural. Sin identidad verificable, el KYC/AML es imposible, y sin KYC/AML la plataforma no puede operar legalmente. La biometría móvil y el acuerdo con Starlink/Copaco para conectar escuelas rurales son el camino.

**Prioridad 5: Piloto selectivo en BVPASA.** Un emisor institucional — una cooperativa grande, un fondo de inversión — tokeniza un activo específico en la Bolsa de Valores de Asunción, bajo supervisión plena de la SIV. Se aprende haciendo, pero a escala controlada y con protección al inversor.

---

## 7. Preguntas abiertas que merecen respuesta antes del entusiasmo

¿Para quién es realmente la tokenización? Si el 40% de la tierra está en manos del 0,07% de los propietarios, la tokenización sin política pública corre el riesgo de ser simplemente una nueva capa de liquidez para los que ya tienen todo. El pequeño productor que necesita financiamiento pero no tiene título de propiedad ni conectividad ni educación financiera — ¿cómo accede? O, peor: ¿no corre el riesgo de que su tierra se tokenice sin su consentimiento?

¿Quién vigila? La SIV/BCP no tiene experiencia en smart contracts. Los reglamentos secundarios recién empiezan en 2026. La auditoría técnica no es obligatoria. ¿Quién garantiza que el código hace lo que dice hacer?

¿Qué pasa si el token se cae? USDR, una stablecoin respaldada por bienes raíces tokenizados, perdió el 50% de su valor en horas cuando los inversores pidieron rescates masivos y el colateral ilíquido no pudo venderse a tiempo. UST/LUNA destruyó USD 40.000 millones en 3 días. Los activos agrícolas son ilíquidos por definición — una cosecha no se vende en una hora. ¿Qué pasa cuando el pánico llega?

¿Y si se pierde la clave? Una clave privada perdida es un activo perdido permanentemente. No hay "olvidé mi contraseña". No hay chargeback. Mt. Gox perdió USD 450 millones por custodia inadecuada. Zoth perdió USD 8,4 millones por una sola clave de administrador comprometida. En un país donde el 30% de los distritos no tiene presencia bancaria, ¿quién va a custodiar las claves de los productores?

---

## La conclusión incómoda

Paraguay tiene las piezas para ser líder en tokenización agropecuaria. Energía barata y limpia. Una ley moderna. Producción agropecuaria masiva. Adopción digital creciente. Cooperativas que llegan donde los bancos no llegan.

Pero tener las piezas no es tener el rompecabezas armado. La tokenización no es una tecnología que se instala y ya. Es un sistema que requiere, al mismo tiempo: registro de tierras confiable, educación financiera, conectividad rural, protección al inversor, seguridad técnica, marco fiscal claro, supervisión competente y, sobre todo, la certeza de que los beneficios no se van a concentrar en los mismos de siempre.

La Ley 7572/2025 no dice nada de eso. Y lo que una ley no dice es tan importante como lo que dice. Paraguay puede tokenizar su campo. La pregunta no es si puede. La pregunta es si va a hacerlo bien.

---

## Fuentes

<ol class="sources-list">
<li><strong>ABC Color</strong> – <a href="https://www.abc.com.py/negocios/abc-campo/2026/05/16/paraguay-abre-las-puertas-para-la-tokenizacion-del-agro/">"Paraguay abre las puertas para la tokenización del agro"</a> (16 May 2026)</li>
<li><strong>BACN</strong> – <a href="https://www.bacn.gov.py/leyes-paraguayas/13047/ley-n-7572-mercado-de-valores-y-productos">Ley N.° 7572/2025 del Mercado de Valores y Productos</a></li>
<li><strong>Forbes Argentina</strong> – <a href="https://www.forbesargentina.com/negocios/agrotoken-levanta-us-125-millones-seguir-tokenizando-granos-region-n46003">"Agrotoken levanta USD 12,5 millones"</a> (2024)</li>
<li><strong>Forbes Brazil</strong> – <a href="https://www.forbes.com.br/forbesagro/2024/01/os-novos-reis-do-agro-argentino-como-a-agrotoken-quer-tokenizar-o-brasil/">"Os novos reis do agro argentino: como a Agrotoken quer tokenizar o Brasil"</a> (Jan 2024)</li>
<li><strong>RWA.xyz</strong> – <a href="https://app.rwa.xyz/assets/JSOY">JSOY token data</a></li>
<li><strong>FINMA</strong> – <a href="https://www.finma.ch/en/news/2025/03/20250318-mm-dlt-handelssystem/">First DLT trading facility license</a> (Mar 2025)</li>
<li><strong>CoinTelegraph</strong> – "Farmway tokenizes $100M Georgia almond orchards" (2025)</li>
<li><strong>CoinTelegraph</strong> – "CertiK RWA Security Report 2025"</li>
<li>**Olympix** — "90% of exploited smart contracts were audited" (2026)</li>
<li><strong>CriptoNoticias</strong> – <a href="https://www.criptonoticias.com/seguridad-bitcoin/detenido-mexico-promotor-criptomoneda-agrocoin">"Detenido en México promotor de criptomoneda Agrocoin"</a></li>
<li><strong>IAPP</strong> – <a href="https://iapp.org/news/a/paraguay-da-un-paso-hacia-un-marco-moderno-de-protecci-n-de-la-privacidad">"Paraguay da un paso hacia un marco moderno de protección de la privacidad"</a> (Dec 2025)</li>
<li><strong>Ferrere Abogados</strong> – <a href="https://www.ferrere.com/es/novedades/paraguay-adopta-su-ley-de-proteccion-de-datos-personales">"Paraguay adopta su Ley de Protección de Datos Personales"</a> (Nov 2025)</li>
<li><strong>IDB</strong> – <a href="https://www.iadb.org/en/news/paraguay-will-improve-security-land-ownership-idb-support">"Paraguay will improve security of land ownership with IDB support"</a> (PR-L1061)</li>
<li><strong>Asunción Times</strong> – <a href="https://asunciontimes.com/paraguay-news/national-news/unified-national-registry-of-paraguay-replaces-150-years-of-paper-records/">"Unified National Registry of Paraguay replaces 150 years of paper records"</a> (Jan 2026)</li>
<li><strong>World Bank</strong> – <a href="https://www.worldbank.org/en/publication/globalfindex">Global Findex 2025</a></li>
<li><strong>Internet Society</strong> – <a href="https://pulse.internetsociety.org/en/reports/PY/">Paraguay Pulse Report 2024</a></li>
<li><strong>BCP</strong> – <a href="https://www.bcp.gov.py/web/institucional/w/indicadores-financieros-noviembre-2025">Indicadores financieros noviembre 2025</a></li>
<li>**Cámara Paraguaya de Fintech**: https://fintech.org.py/</li>
<li><strong>DataReportal</strong> – <a href="https://datareportal.com/reports/digital-2026-paraguay">Digital 2026 Paraguay</a></li>
<li><strong>CAF</strong> – Financial capabilities surveys (OECD/INFE methodology)</li>
<li>**FATF** — Targeted Update on VA/VASPs (2024, 2025)</li>
<li><strong>Chainalysis</strong> – <a href="https://www.chainalysis.com/blog/2025-global-crypto-adoption-index">2025 Crypto Crime Report</a></li>
<li><strong>Finka</strong> – Swiss cattle tokenization platform</li>
<li><strong>PwC Brazil</strong> – <a href="https://www.pwc.com.br/pt/consultoria/agtech-innovation/agtech-innovation-news/materias/2024/Agrotoken-pioneira-na-tokenizacao-de-graos-passa-a-oferecer-sua-infraestrutura-de-blockchain-como-servico.html">Agrotoken blockchain infrastructure as a service</a></li>
<li><strong>FCA UK</strong> – <a href="https://www.fca.org.uk/publication/research-and-data/regulatory-sandbox-lessons-learned-report.pdf">Regulatory sandbox lessons learned</a></li>
<li><strong>IDB</strong> – <a href="https://publications.iadb.org/publications/english/document/Regulatory-Sandboxes-Innovation-Hubs-and-Other-Regulatory-Innovation-Tools-in-Latin-America-and-the-Caribbean.pdf">Regulatory Sandboxes, Innovation Hubs in LAC</a></li>
<li><strong>INVENTTA / Doble Filo MX</strong> – Blockchain soberana paraguaya</li>
<li><strong>RDN</strong> – <a href="https://www.rdn.com.py/2026/02/10/paraguay-en-las-puertas-del-negocio-bitcoin/">Entrevista a Bruno Vaccotti</a> (Feb 2026)</li>
<li><strong>Vouga Abogados</strong> – <a href="https://www.vouga.com.py/en/avances-en-la-regulacion-fintech-en-el-paraguay-criptomonedas-y-cripto-activos/">Avances en regulación fintech</a></li>
<li>**Nethermind** — "Securing Tokenized RWAs" (2026)</li>
</ol>