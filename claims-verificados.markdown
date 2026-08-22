---
layout: page
title: "Claims verificados del Observatorio de IA"
permalink: /claims-verificados/
description: "Base pública de verificación de datos de muchotexto.net: qué afirmaciones confirmamos, cuáles eran falsas o parciales y contra qué fuente. Transparencia editorial."
last_modified_at: 2026-08-21
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

.claims-section {
  margin-bottom: var(--spacer-3);
}

.claims-section-title {
  font-size: 0.95em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.6;
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
  opacity: 0.65;
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

<div class="claims-legend">
  <span class="claims-legend-item"><span class="claim-v v-true">TRUE</span> confirmado con fuente</span>
  <span class="claims-legend-item"><span class="claim-v v-false">FALSE</span> era falso, corregido</span>
  <span class="claims-legend-item"><span class="claim-v v-partial">PARTIALLY</span> impreciso, matizado</span>
  <span class="claims-legend-item"><span class="claim-v v-unverifiable">UNVERIFIABLE</span> sin fuente sólida</span>
</div>

<section class="claims-section">
<h2 class="claims-section-title">Energía y data centers</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay tiene la matriz eléctrica 99,998% renovable en 2024 (Itaipú 86%, Yacyretá 11%, Acaray 3%)."</span></div>
  <span class="claim-source">Fuente: Wikipedia (Electricity sector in Paraguay), ANDE · <a href="/articulos/2026/08/03/energia-renovable-cambio-climatico-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARTIALLY</span><span class="claim-text">"Paraguay tiene la tarifa industrial más barata de Sudamérica."</span></div>
  <span class="claim-source">Es la más baja entre 13 países según CIER 2025 (residencial USD 46/MWh, industrial USD 35/MWh), pero "la más barata" sin comparar Argentina y Bolivia es impreciso. · <a href="/calculadora-energetica/">Calculadora</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"943,8 MW de potencia reservada por 41 empresas equivalen a ~13,5% de la potencia que le corresponde a Paraguay de Itaipú (7.000 MW)."</span></div>
  <span class="claim-source">Fuente: ABC Color Negocios (3-ago-2026) · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El consumo nacional de electricidad fue de 29,4 TWh en 2025 (29.419 GWh)."</span></div>
  <span class="claim-source">Fuente: ANDE (14-ene-2026) · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La demanda eléctrica crece 12,5-21% anual (12,5% en 2025, 18,5% en 2024, 21% en 2026)."</span></div>
  <span class="claim-source">Fuente: ANDE. El piso oficial reciente es 12,5%, no 12%. · <a href="/articulos/2026/08/12/mesa-energetica-pen-2050-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"HIVE Digital opera 300 MW en Paraguay y construye 100 MW adicionales de cómputo GPU."</span></div>
  <span class="claim-source">Fuente: HIVE FY2026 Earnings · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Un data center emplea 20-50 personas por cada 100 MW (referencia de industria)."</span></div>
  <span class="claim-source">Fuente: referencia de industria (sin cifra oficial por empresa) · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Los data centers ya consumen el 23% de la electricidad de Irlanda en 2025 (20% en 2023)."</span></div>
  <span class="claim-source">Fuente: CRU Ireland · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Tarifas ANDE</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La tarifa del Grupo Consumo Intensivo Especial es de 30 US$/MWh (Resolución 49238/2024, vigente hasta diciembre de 2027)."</span></div>
  <span class="claim-source">Fuente: Resolución ANDE 49238/2024 · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Los decretos que extendían la tarifa de 30 a 15 años fueron derogados el 9 de junio de 2026."</span></div>
  <span class="claim-source">Fuente: ABC Color · <a href="/dashboard-energetico/">Dashboard</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El estudio Ceare proyecta la tarifa media de 49,2 a 68,6 US$/MWh al 2030 (+39,4%)."</span></div>
  <span class="claim-source">Fuente: estudio Ceare (UBA, con apoyo del BID). Es proyección, no tarifa aplicada. · <a href="/articulos/2026/08/20/estudio-ceare-tarifa-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Itaipú</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La negociación del Anexo C se suspendió en abril de 2025 y se reanudó en noviembre de 2025."</span></div>
  <span class="claim-source">Fuente: ABC Color, El Nacional, ANDE · <a href="/articulos/2026/07/17/itaipu-2027-energia-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El acuerdo tarifario de Itaipú (USD 19,28/kW-mes) vence el 1 de enero de 2027."</span></div>
  <span class="claim-source">Fuente: ANDE · <a href="/articulos/2026/07/17/itaipu-2027-energia-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Demografía y economía</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay tiene 6.460.159 habitantes (2026), con edad media de 29,4 años."</span></div>
  <span class="claim-source">Fuente: INE Paraguay, Revisión 2025 · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La fecundidad es de 1,90 hijos por mujer (2026) y caerá a 1,72 en 2050, por debajo del reemplazo."</span></div>
  <span class="claim-source">Fuente: INE Revisión 2024. El rango 1,7-1,8 estaba desactualizado. · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-partial">PARTIALLY</span><span class="claim-text">"El bono demográfico se cierra alrededor de 2045."</span></div>
  <span class="claim-source">No es fecha oficial: INE habla de ~2070 y la UIP de 2030-2040. Se presenta como estimación divergente. · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El PIB per cápita de Paraguay ronda los USD 9.400 nominales (2026)."</span></div>
  <span class="claim-source">Fuente: BCP. USD 5.900 era el dato 2022-2023, ya corregido. · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El índice de capital humano de Paraguay es 0,528 (el más bajo entre pares regionales)."</span></div>
  <span class="claim-source">Fuente: Banco Mundial 2020 (Uruguay ~0,60, Chile ~0,65, Costa Rica ~0,63) · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La informalidad laboral está entre 60% y 64% según trimestre y medición."</span></div>
  <span class="claim-source">Fuente: INE 2025-2026 · <a href="/articulos/2026/08/05/paraguay-2040-futuro-datos/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay es el 4.º exportador mundial de soja (no el 6.º; 6.º es como productor)."</span></div>
  <span class="claim-source">Fuente: MercoPress 2024, USDA 2026, WITS (Banco Mundial) · <a href="/articulos/2026/07/01/de-la-soja-al-silicio-matriz-exportadora-paraguay/">Artículo</a></span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Regulación</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay aprobó su primera ley integral de protección de datos (Ley 7593/2025), en vigencia desde noviembre de 2027."</span></div>
  <span class="claim-source">Fuente: BACN · <a href="/articulos/2026/07/07/ley-proteccion-datos-paraguay-ia/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"La Ley 7599/2025 y el Decreto 6034/2026 abren la generación privada de energía renovable."</span></div>
  <span class="claim-source">Fuente: BACN · <a href="/articulos/2026/05/27/apertura-sector-electrico-privado-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Paraguay no tiene una regulación específica para data centers."</span></div>
  <span class="claim-source">Fuente: verificado en AGENTS.md · <a href="/articulos/2026/08/04/impacto-local-data-center-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-unverifiable">UNVERIFIABLE</span><span class="claim-text">"La Ley 7547/2025 reforma la Ley de Maquila."</span></div>
  <span class="claim-source">BACN devuelve una ley no relacionada para esa URL. La existencia de la reforma se menciona en prensa, pero el número exacto no se pudo confirmar con fuente primaria.</span>
</div>
</section>

<section class="claims-section">
<h2 class="claims-section-title">Tokenización agro y cripto</h2>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Agrotoken tokenizó 230.000 toneladas de soja, maíz y trigo."</span></div>
  <span class="claim-source">Fuente: prensaeconomica.com.ar, bichosdecampo.com (2022-2025) · <a href="/articulos/2026/05/18/tokenizacion-del-agro-paraguay/">Artículo</a></span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"Los exploits en activos tokenizados sumaron USD 17,9M (2023), USD 6M (2024) y USD 14,6M (primer semestre 2025)."</span></div>
  <span class="claim-source">Fuente: CertiK 2025 Skynet RWA Security Report</span>
</div>

<div class="claim">
  <div class="claim-head"><span class="claim-v v-true">TRUE</span><span class="claim-text">"El colapso de UST/LUNA destruyó entre USD 40.000 y 45.000 millones en una semana."</span></div>
  <span class="claim-source">Fuente: Bloomberg, Wikipedia. La magnitud es correcta; algunos artículos decían "3 días" y las fuentes "una semana".</span>
</div>
</section>

<p class="claims-note">Este registro se alimenta de nuestra base interna de claims verificados (AGENTS.md) y se actualiza con cada fact-check. Si detectás un dato que cambió, escribinos por la <a href="/contacto/">página de contacto</a>. Nuestra metodología completa está en <a href="/como-trabajamos/">cómo trabajamos</a>.</p>

</div>
