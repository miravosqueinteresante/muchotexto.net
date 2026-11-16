---
layout: page
title: "Registro de verificación de datos del Observatorio"
permalink: /claims-verificados/
description: "Base pública de verificación de datos de muchotexto.net: qué afirmamos, qué corregimos y contra qué fuente. Transparencia editorial."
last_modified_at: 2026-11-16
---

<style>
/* ---------- claims scoped styles ---------- */
.claims {
  font-family: var(--body-font-family);
  margin-bottom: var(--spacer-3);
}

.claims-eyebrow {
  font-family: var(--code-font-family);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--oc-cyan-4);
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 var(--spacer) 0;
}

.claims-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  box-shadow: 0 0 0 3px rgba(34, 184, 207, 0.18);
  animation: claims-pulse 2.4s ease-in-out infinite;
}

@keyframes claims-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.35; }
}

.claims-intro {
  font-size: 0.92em;
  line-height: 1.6;
  opacity: 0.85;
  margin: 0 0 var(--spacer-2) 0;
}

.claims-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: var(--spacer-2);
  font-size: 0.8em;
  opacity: 0.85;
}

.claims-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.claim-v {
  display: inline-block;
  padding: 1px 8px;
  font-family: var(--code-font-family);
  font-size: 0.7em;
  font-weight: 600;
  letter-spacing: 0.03em;
  border-radius: 999px;
  flex: none;
}

.v-true { background: rgba(105, 219, 124, 0.16); color: #69db7c; }
.v-false { background: rgba(255, 107, 107, 0.16); color: #ff6b6b; }
.v-partial { background: rgba(255, 212, 59, 0.16); color: #ffd43b; }
.v-unverifiable { background: rgba(173, 181, 189, 0.16); color: #adb5bd; }
.v-no-demostrable { background: rgba(255, 169, 77, 0.16); color: #ffa94d; }

.claims-section {
  margin-bottom: var(--spacer-3);
}

.claims-section-title {
  font-size: 0.95em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.8;
  margin: 0 0 var(--spacer) 0;
  padding-bottom: var(--spacer);
  border-bottom: 1px solid var(--border-color);
}

.claim {
  padding: 12px 0;
  border-bottom: 1px solid var(--border-color);
}

.claim-head {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.claim-text {
  font-size: 0.92em;
  line-height: 1.5;
  color: var(--heading-color);
  flex: 1;
}

.claim-source {
  display: block;
  margin-top: 6px;
  font-size: 0.78em;
  opacity: 0.8;
  line-height: 1.5;
  padding-left: 0;
}

.claim-source a {
  color: var(--link-color);
  text-decoration: none;
}

.claim-source a:hover {
  text-decoration: underline;
}

.claims-note {
  margin-top: var(--spacer-2);
  font-size: 0.82em;
  opacity: 0.7;
  line-height: 1.6;
  border-top: 1px solid var(--border-color);
  padding-top: var(--spacer);
}
</style>

<div class="claims">

<p class="claims-eyebrow"><span class="claims-dot"></span>Verificación de datos · muchotexto.net</p>

<p class="claims-intro">Publicamos el registro de verificación que sostiene nuestros artículos: qué afirmación confirmamos, cuál era falsa o imprecisa y contra qué fuente. No es un resumen de todo lo que escribimos, sino de los datos duros que corregimos y confirmamos. Es la transparencia editorial hecha producto.</p>

<p class="claims-intro">40 registros revisados al 16-nov-2026: 37 claims y 3 correcciones. El estado indica la veracidad; la fuente y la nota indican la calidad de la evidencia.</p>

<div class="claims-legend">
  <span class="claims-legend-item"><span class="claim-v v-true">TRUE</span> confirmado con fuente</span>
  <span class="claims-legend-item"><span class="claim-v v-false">FALSE</span> era falso, corregido</span>
  <span class="claims-legend-item"><span class="claim-v v-partial">PARTIALLY</span> impreciso, matizado</span>
  <span class="claims-legend-item"><span class="claim-v v-unverifiable">UNVERIFIABLE</span> sin fuente sólida</span>
  <span class="claims-legend-item"><span class="claim-v v-no-demostrable">NO DEMOSTRABLE</span> ausencia no comprobada</span>
</div>

<section class="claims-section">
<h2 class="claims-section-title">Energía y data centers</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La matriz eléctrica paraguaya es casi totalmente renovable: en 2025, Itaipú aportó 87,6%, Yacyretá 10,5% y Acaray 1,9% del consumo nacional."</span></div>
  <span class="claim-source">Fuente: ANDE (14-ene-2026), distribución del consumo de 29.419 GWh. · <a href="https://www.ande.gov.py/interna.php?id=14877">ANDE</a> · <a href="/articulos/2026/08/04/energia-renovable-cambio-climatico-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARTIALLY</span><span class="claim-text">"Paraguay tiene la tarifa industrial más barata de Sudamérica."</span></div>
  <span class="claim-source">Es la más baja entre 13 países según CIER 2025 (residencial USD 46/MWh, industrial USD 35/MWh), pero "la más barata" sin comparar Argentina y Bolivia es impreciso. · <a href="/calculadora-energetica/">Calculadora</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"ANDE reportó 943,8 MW reservados por 41 suministros (13,5% de los 7.000 MW de Itaipú); un listado posterior al Congreso muestra 32 suministros y 975.667 kW."</span></div>
  <span class="claim-source">Fuente: ABC Color (15-mar-2026) y ANDE, listado GCIE remitido al Congreso. Los universos no coinciden: 41 suministros/943,8 MW frente a 32/975,7 MW. · <a href="https://www.abc.com.py/economia/2026/03/15/ande-41-empresas-consumen-el-135-de-nuestra-energia-de-itaipu/">ABC Color</a> · <a href="https://silpy.congreso.gov.py/web/descarga/respuestapedidoinforme-169763?preview=">ANDE/SILPy</a> · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El consumo nacional de electricidad fue de 29,4 TWh en 2025 (29.419 GWh)."</span></div>
  <span class="claim-source">Fuente: ANDE (14-ene-2026): “el consumo total llegó a 29.419 GWh”. · <a href="https://www.ande.gov.py/interna.php?id=14877">ANDE</a> · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La demanda eléctrica creció 18,5% en 2024, 12,5% en 2025 y 17,9% acumulado a 8 meses de 2026."</span></div>
  <span class="claim-source">Fuente: ANDE. El 21% era un parcial del primer trimestre de 2026, no un cierre anual. · <a href="https://www.ande.gov.py/interna.php?id=15615">ANDE</a> · <a href="/dashboard-energetico/">Dashboard</a> · <a href="/articulos/2026/08/12/mesa-energetica-pen-2050-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"HIVE Digital opera 300 MW en Paraguay (minería ASIC) y desarrolla 100 MW de infraestructura HPC/AI (Tier III, 2027)."</span></div>
  <span class="claim-source">Fuente: HIVE Digital Technologies, comunicado del 18-mar-2026: “300 MW... operational in Paraguay, with another 100 MW in development”. · <a href="https://www.hivedigitaltechnologies.com/news/hive-digital-technologies-reaches-ai-cloud-milestone-in-paraguay-powers-columbia-university-llm-research-from-new-york-to-asuncion/">HIVE</a> · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Un data center emplea 20-50 personas por cada 100 MW (referencia de industria)."</span></div>
  <span class="claim-source">Fuente: referencia de industria (sin cifra oficial por empresa) · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Los data centers consumieron el 23% de la electricidad metrada de Irlanda en 2025 (22% en 2024 y 21% en 2023)."</span></div>
  <span class="claim-source">Fuente: CSO Ireland, “Data Centres Metered Electricity Consumption 2025” (7-jul-2026). · <a href="https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2025/keyfindings/">CSO</a> · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El MOU nuclear firmado con EE.UU. el 4 de agosto de 2026 no es un Acuerdo 123: no es vinculante, no transfiere tecnología ni compromete proveedor, sitio, capacidad o plazos."</span></div>
  <span class="claim-source">Fuente: U.S. State Department — <a href="https://www.state.gov/releases/office-of-the-spokesperson/2026/08/secretary-of-state-marco-rubio-and-paraguayan-foreign-minister-ruben-ramirez-lezcano-at-the-signing-of-a-memorandum-of-understanding-for-strategic-civil-nuclear-cooperation/">Remarks</a> · <a href="/articulos/2026/09/23/energia-nuclear-paraguay-eeuu/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"Los USD 665 millones de Atome eran inversión proyectada, no dinero desembolsado; la empresa notificó la terminación de su PPA el 1-oct-2026, efectiva a fines de 2026."</span></div>
  <span class="claim-source">Fuente: ATOME PLC · <a href="https://www.prnewswire.com/news-releases/atome-plc-notice-of-dispute-and-intent-to-submit-claim-to-arbitration-under-the-uk--paraguay-bilateral-investment-treaty-the-treaty-or-bit-302881982.html">Notice of Dispute</a> · <a href="/articulos/2026/10/02/atome-ande-salida-paraguay/">Artículo</a>. La notificación no equivale a extinción inmediata del contrato.</span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Tarifas ANDE</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La tarifa del Grupo Consumo Intensivo Especial es de 30 US$/MWh (Resolución 49238/2024, vigente hasta diciembre de 2027)."</span></div>
  <span class="claim-source">Fuente: Resolución ANDE 49238/2024 · <a href="https://www.ande.gov.py/interna.php?id=12464">Resolución</a> · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"Los decretos que extendían la tarifa de 30 a 15 años fueron derogados el 9 de junio de 2026."</span></div>
  <span class="claim-source">Fuente: Agencia IP (10-jun-2026) y ABC Color (9-jun-2026). El Ejecutivo dejó sin efecto los decretos 5306 y 5307, modificados por 5860 y 5861. · <a href="https://www.ip.gov.py/ip/2026/06/10/ejecutivo-derogo-decretos-emitidos-sobre-industrias-convergentes-y-fortalece-coordinacion-institucional/">Agencia IP</a> · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"El estudio Ceare proyecta la tarifa media de 49,2 a 68,6 US$/MWh al 2030 (+39,4%)."</span></div>
  <span class="claim-source">Fuente: Ceare (UBA, con apoyo del BID), presentado por ANDE; ABC Color (6-ago-2026). Es proyección, no tarifa aplicada. · <a href="https://www.abc.com.py/economia/2026/08/06/ande-estudio-internacional-proyecta-un-aumento-de-la-tarifa-de-hasta-456/">ABC Color</a> · <a href="https://www.ceare.org/documentos.php">CEARE</a> · <a href="/articulos/2026/08/20/estudio-ceare-tarifa-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Itaipú</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La negociación del Anexo C se suspendió en abril de 2025 y se reanudó en noviembre de 2025."</span></div>
  <span class="claim-source">Fuente: MRE Paraguay, suspensión del 1-abr-2025 y reanudación anunciada el 17-nov-2025. · <a href="https://www.mre.gov.py/paraguay-pide-aclaraciones-a-brasil-y-suspende-temporalmente-negociacion-del-anexo-c-del-tratado-de-itaipu/">MRE (suspensión)</a> · <a href="https://www.mre.gov.py/paraguay-recibe-informe-del-brasil-y-ambos-paises-avanzan-en-una-nueva-etapa-de-relacion/">MRE (reanudación)</a> · <a href="/articulos/2026/07/17/itaipu-2027-energia-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El acuerdo tarifario de Itaipú (USD 19,28/kW-mes) vence el 1 de enero de 2027."</span></div>
  <span class="claim-source">Fuente: MRE Paraguay (9-may-2024) y entendimiento Brasil-Paraguay (16-abr-2024): tarifa de USD 19,28/kW-mes para 2024, 2025 y 2026. · <a href="https://www.mre.gov.py/paraguay-y-brasil-llegaron-a-un-historico-acuerdo-sobre-la-tarifa-de-itaipu/">MRE</a> · <a href="https://concordia.itamaraty.gov.br/ApiConcordia/Acordo/integra-acordo-html/12813">Itamaraty</a> · <a href="/articulos/2026/07/17/itaipu-2027-energia-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Demografía y economía</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay tiene 6.460.159 habitantes (2026), con edad mediana de 29,4 años."</span></div>
  <span class="claim-source">Fuente: INE Paraguay, Revisión 2025. La edad mediana es el indicador oficial; “edad media” era una imprecisión. · <a href="https://www.ine.gov.py/noticias/2946/paraguay-sigue-teniendo-la-mayor-cantidad-de-su-poblacion-en-edad-productiva">INE</a> · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La fecundidad es de 1,90 hijos por mujer (2026) y caerá a 1,72 en 2050, por debajo del reemplazo."</span></div>
  <span class="claim-source">Fuente: INE, Proyecciones de la Población 2026 (Revisión 2025). El rango 1,7-1,8 estaba desactualizado. · <a href="https://www.ine.gov.py/Publicaciones/Biblioteca/documento/266/Triptico.pdf">INE</a> · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARTIALLY</span><span class="claim-text">"El bono demográfico se cierra alrededor de 2045."</span></div>
  <span class="claim-source">No es fecha oficial: INE habla de ~2070 y la UIP de 2030-2040. Se presenta como estimación divergente. · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El PIB per cápita de Paraguay ronda los USD 9.400 nominales (2026)."</span></div>
  <span class="claim-source">Fuente: IMF World Economic Outlook (oct-2026), proyección de PIB per cápita nominal: USD 9.370. · <a href="https://www.imf.org/en/Publications/WEO/weo-database/2026/October">IMF WEO</a> · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El índice de capital humano de Paraguay es 0,528 (el más bajo entre pares regionales)."</span></div>
  <span class="claim-source">Fuente: Banco Mundial, Human Capital Index 2020 (Uruguay ~0,60, Chile ~0,65, Costa Rica ~0,63). · <a href="https://api.worldbank.org/v2/country/PRY/indicator/HD.HCI.OVRL?format=json">Banco Mundial</a> · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La informalidad laboral fue de 60,1% en 2025, según el INE; la referencia comparable de 2024 fue 62,5%."</span></div>
  <span class="claim-source">Fuente: INE, Ocupación Informal 2022 y 2025. · <a href="https://www.ine.gov.py/noticias/2891/la-ocupacion-informal-fue-de-601-en-el-ano-2025">INE</a> · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"Paraguay es el 4.º exportador mundial de soja (no el 6.º; 6.º es como productor)."</span></div>
  <span class="claim-source">Fuente: USDA FAS, tabla 07 de oferta y distribución mundial de soja (abr-2026): Paraguay exporta 8,2 MMT, detrás de Brasil, EE.UU. y Argentina. Un informe de 2024 lo ubicaba tercero. · <a href="https://apps.fas.usda.gov/psdonline/reporthandler.ashx?fileName=Table+07%3A+Soybeans%3A+World+Supply+and+Distribution&format=html&reportId=706&templateId=8">USDA</a> · <a href="/articulos/2026/07/01/de-la-soja-al-silicio-matriz-exportadora-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Regulación</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay aprobó su primera ley integral de protección de datos (Ley 7593/2025), en vigencia desde el 27-nov-2027: 24 meses desde su publicación."</span></div>
  <span class="claim-source">Fuente: BACN · <a href="https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025-de-proteccion-de-datos-personales-en-la-republica-del-paraguay">Ley 7593/2025</a> · <a href="/articulos/2026/07/07/ley-proteccion-datos-paraguay-ia/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La Ley 7599/2025 y el Decreto 6034/2026 abren la generación privada de energía renovable."</span></div>
  <span class="claim-source">Fuente: BACN, Ley 7599/2025. · <a href="https://www.bacn.gov.py/leyes-paraguayas/12999/ley-n-7599-2025-de-modernizaci-n-del-r-gimen-que-regula-y-fomenta-la-generaci-n-de-energ-a-el-ctrica-a-partir-de-fuentes-de-energ-as-renovables-no-convencionales-no-hidr-ulicas">Ley 7599/2025</a> · <a href="/articulos/2026/05/27/apertura-sector-electrico-privado-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"No identificamos una norma específica para data centers en la revisión de Ley 294/1993, Ley 7599/2025, Ley 7547/2025 y Ley 3001/2006."</span></div>
  <span class="claim-source">Fuente: revisión propia de normas citadas en el artículo. La ausencia de una norma específica no se puede probar como un hecho positivo. · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La Ley 7547/2025 establece el nuevo régimen de maquila."</span></div>
  <span class="claim-source">Fuente: BACN — <a href="https://www.bacn.gov.py/leyes-paraguayas/12853/ley-n-75472025-del-regimen-de-maquila">Ley 7547/2025</a> · <a href="/articulos/2026/08/28/adata-minga-guazu-memorias-semiconductores/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Migración y residencia</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La Resolución MIC 0283/2026 reglamenta la Constancia de Inversionista Extranjero; la residencia permanente la concede Migraciones al amparo del artículo 46 de la Ley 6984/2022."</span></div>
  <span class="claim-source">Fuente: MIC — <a href="https://www.mic.gov.py/wp-content/uploads/2026/04/Res.-N-0283.2026_Constancia-de-Inversionista.pdf">Resolución 0283/2026</a> · BACN — <a href="https://www.bacn.gov.py/leyes-paraguayas/10973/ley-n-6984-de-migraciones">Ley 6984/2022</a> · <a href="/articulos/2026/09/25/paraguay-investor-pass-residencia-inversores/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Ueno y datos personales</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El BCP dispuso la resolución de ueno bank el 2-nov-2026 por una insuficiencia de solvencia por debajo del 50% del mínimo; la app y los servicios se suspendieron el 3-nov-2026."</span></div>
  <span class="claim-source">Fuente: BCP/ABC Color y Poder Judicial — <a href="https://www.pj.gov.py/notas/30918-corte-suprema-de-justicia-socializa-comunicacion-de-la-superintendencia-de-bancos-sobre-ueno-bank-sa">Poder Judicial</a> · <a href="/articulos/2026/11/13/que-datos-tuyos-tenia-ueno/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El FGD garantiza hasta 75 salarios mínimos por depositante y por entidad."</span></div>
  <span class="claim-source">Fuente: BCP · <a href="https://www.pj.gov.py/notas/30918-corte-suprema-de-justicia-socializa-comunicacion-de-la-superintendencia-de-bancos-sobre-ueno-bank-sa">Comunicación de la Superintendencia de Bancos</a> · <a href="/articulos/2026/11/13/que-datos-tuyos-tenia-ueno/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"El BCP pagó un anticipo de hasta 40 salarios mínimos a 1.812.348 personas: G. 3,99 billones, equivalentes a USD 644 millones según la conversión difundida por Última Hora."</span></div>
  <span class="claim-source">Fuente: BCP/Última Hora. El BCP confirma depositantes y monto en guaraníes; la equivalencia en dólares depende del tipo de cambio y la fecha. · <a href="https://www.ultimahora.com/primera-semana-del-colapso-de-ueno-el-fgd-desembolso-usd-644-millones-a-1-8-millones-de-afectados">Última Hora</a> · <a href="/articulos/2026/11/13/que-datos-tuyos-tenia-ueno/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La Ley 2334/2003 no menciona datos personales; la Ley 7593/2025 recién rige el 27-nov-2027 y no tiene una regla específica para resoluciones bancarias."</span></div>
  <span class="claim-source">Fuente: BACN — <a href="https://www.bacn.gov.py/leyes-paraguayas/2513/ley-n-2334">Ley 2334/2003</a> · <a href="https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025-de-proteccion-de-datos-personales-en-la-republica-del-paraguay">Ley 7593/2025</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-no-demostrable">NO DEMOSTRABLE</span><span class="claim-text">"No encontramos información pública que confirme ni descarte la venta o transferencia de las bases de datos de Ueno."</span></div>
  <span class="claim-source">Fuente: TEDIC y BCP. Es una ausencia de evidencia, no una prueba de que la operación no exista. · <a href="https://www.tedic.org/caso-ueno-biometria-datos-personales-y-la-deuda-del-estado-paraguayo/">TEDIC</a> · <a href="/articulos/2026/11/13/que-datos-tuyos-tenia-ueno/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Ciberseguridad</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"CERT-PY fue creado el 30 de noviembre de 2012 y depende del MITIC."</span></div>
  <span class="claim-source">Fuente: CERT-PY — <a href="https://www.cert.gov.py/">CERT-PY</a> · <a href="/articulos/2026/07/17/ciberseguridad-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El Decreto 3900/2025 aprobó la Estrategia Nacional de Ciberseguridad 2025-2028."</span></div>
  <span class="claim-source">Fuente: MITIC, “Poder Ejecutivo oficializa la Estrategia Nacional de Ciberseguridad 2025-2028” (23-may-2025). · <a href="https://mitic.gov.py/enc2025-2028/">MITIC</a> · <a href="/articulos/2026/07/17/ciberseguridad-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Tokenización agro y cripto</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"Agrotoken tokenizó 230.000 toneladas de soja, maíz y trigo."</span></div>
  <span class="claim-source">Fuente: Tanssi (9-jul-2024), que cita la cifra histórica de Agrotoken; la empresa reporta hoy más de 1M de toneladas en su plataforma. Falta un registro verificable de emisión. · <a href="https://www.tanssi.network/post/collaboration-tanssi-agrotoken">Tanssi</a> · <a href="/articulos/2026/05/18/tokenizacion-del-agro-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Los exploits en activos tokenizados sumaron USD 17,9M (2023), USD 6M (2024) y USD 14,6M (primer semestre 2025)."</span></div>
  <span class="claim-source">Fuente: CertiK, 2025 Skynet RWA Security Report (21-ago-2025). · <a href="https://www.certik.com/certik-report/intel3d/2025-skynet-rwa-security-report">CertiK</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARCIAL</span><span class="claim-text">"El colapso de UST/LUNA destruyó entre USD 40.000 y 45.000 millones de capitalización de mercado en una semana."</span></div>
  <span class="claim-source">Fuente: Bloomberg, Wikipedia. La magnitud es correcta, pero mide capitalización destruida, no pérdidas efectivas de inversores.</span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Correcciones</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-false">FALSE</span><span class="claim-text">"Paraguay es el 6.º exportador mundial de soja."</span></div>
  <span class="claim-source">Corregido: es el 4.º exportador mundial en la campaña 2025/26; 6.º es como productor. · <a href="https://apps.fas.usda.gov/psdonline/reporthandler.ashx?fileName=Table+07%3A+Soybeans%3A+World+Supply+and+Distribution&format=html&reportId=706&templateId=8">USDA</a> · <a href="/articulos/2026/07/01/de-la-soja-al-silicio-matriz-exportadora-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-false">FALSE</span><span class="claim-text">"La demanda eléctrica crece 12% anual."</span></div>
  <span class="claim-source">Corregido: el piso oficial reciente es 12,5% (2025); en 2024 fue 18,5% y a 8 meses de 2026, 17,9%. · <a href="https://www.ande.gov.py/interna.php?id=14877">ANDE</a> · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-false">FALSE</span><span class="claim-text">"El Anexo C de Itaipú vence el 1 de enero de 2027."</span></div>
  <span class="claim-source">Corregido: lo que vence es el acuerdo tarifario 2024-2026, no el Anexo C. Las negociaciones del Anexo C siguen abiertas. · <a href="https://concordia.itamaraty.gov.br/ApiConcordia/Acordo/integra-acordo-html/12813">Itamaraty</a> · <a href="/articulos/2026/07/17/itaipu-2027-energia-paraguay/">Artículo</a></span>
</div>
</section>

<p class="claims-note">Este registro se actualiza con cada fact-check y se contrasta contra fuentes primarias. Si detectás un dato que cambió, escribinos por la <a href="/contacto/">página de contacto</a>. Nuestra metodología completa está en <a href="/como-trabajamos/">cómo trabajamos</a>.</p>

</div>
