---
layout: page
title: "Calculadora energética para data centers en Paraguay"
seo_title: "Calculadora energía data center Paraguay"
permalink: /calculadora-energetica/
description: "Calculá el costo eléctrico de un data center con la tarifa de IA de ANDE (Res. 52552/2026) y compará con Irlanda, Virginia, Suecia y Chile."
last_modified_at: 2026-11-21
---

{% assign t = site.data.energia.tarifa_ia %}
{% assign g = site.data.energia.tarifa_gcie %}

<style>
/* ---------- calculator scoped styles ---------- */
.calc-energetica {
  --calc-bg: var(--oc-gray-9);
  --calc-panel: rgba(33,37,41,0.7);
  --calc-panel-2: rgba(52,58,64,0.5);
  --calc-border: var(--oc-gray-7);
  --calc-border-soft: rgba(73,80,87,0.5);
  --calc-text: var(--oc-gray-3);
  --calc-muted: var(--oc-gray-5);
  --calc-muted-2: var(--oc-gray-6);

  font-family: var(--body-font-family);
  margin-bottom: var(--spacer-3);
}

.calc-energetica *,
.calc-energetica *::before,
.calc-energetica *::after {
  box-sizing: border-box;
}

.calc-energetica h2,
.calc-energetica h3,
.calc-energetica p {
  margin: 0;
}

/* eyebrow */
.calc-eyebrow {
  font-family: var(--code-font-family);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 var(--spacer) 0;
}

.calc-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 3px rgba(var(--accent-rgb), 0.18);
  animation: calc-pulse 2.4s ease-in-out infinite;
}

@keyframes calc-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.35; }
}

/* alert */
.calc-alert {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  background: linear-gradient(180deg, rgba(var(--accent-rgb), 0.09), rgba(var(--accent-rgb), 0.035));
  border: 1px solid rgba(var(--accent-rgb), 0.3);
  border-radius: 10px;
  padding: 14px 16px;
  margin-bottom: var(--spacer-2);
}

.calc-alert-icon {
  font-size: 16px;
  color: var(--accent);
  line-height: 1;
  margin-top: 1px;
  flex: none;
}

.calc-alert-title {
  font-weight: 600;
  font-size: 13px;
  color: var(--accent);
  margin-bottom: 5px;
}

.calc-alert-text {
  font-size: 11.5px;
  color: var(--oc-gray-3);
  line-height: 1.6;
}

.calc-alert-text b {
  color: var(--accent-hover);
}

.calc-alert-text a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid rgba(var(--accent-rgb), 0.35);
}

/* grid */
.calc-grid {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 18px;
}

/* panels */
.calc-panel {
  background: var(--calc-panel);
  border: 1px solid var(--calc-border-soft);
  border-radius: 14px;
  padding: 20px;
}

.calc-panel-title {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--calc-muted);
  margin: 0 0 var(--spacer-2) 0;
}

/* input field */
.calc-field {
  margin-bottom: 22px;
}

.calc-field-label {
  font-size: 13px;
  font-weight: 500;
  color: var(--calc-text);
  margin-bottom: 8px;
  display: block;
}

.calc-mw-display {
  font-family: var(--code-font-family);
  font-size: 30px;
  font-weight: 600;
  color: var(--accent);
  margin-bottom: 6px;
}

.calc-mw-display span {
  font-size: 13px;
  color: var(--calc-muted);
  font-weight: 400;
}

.calc-energetica input[type=range] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 4px;
  border-radius: 2px;
  background: var(--calc-border);
  cursor: pointer;
}

.calc-energetica input[type=range]:focus-visible {
  outline: 2px solid var(--link-color);
  outline-offset: 3px;
}

.calc-energetica input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid var(--oc-gray-9);
  box-shadow: 0 0 0 3px rgba(var(--accent-rgb), 0.22);
  cursor: pointer;
}

.calc-energetica input[type=range]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid var(--oc-gray-9);
  box-shadow: 0 0 0 3px rgba(var(--accent-rgb), 0.22);
  cursor: pointer;
}

.calc-range-marks {
  display: flex;
  justify-content: space-between;
  font-size: 10px;
  color: var(--calc-muted-2);
  font-family: var(--code-font-family);
  margin-top: 6px;
}

/* presets */
.calc-presets {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.calc-preset-btn {
  background: var(--calc-panel-2);
  border: 1px solid var(--calc-border-soft);
  color: var(--calc-muted);
  font-family: var(--code-font-family);
  font-size: 10.5px;
  padding: 5px 9px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.calc-preset-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.calc-preset-btn.active {
  background: rgba(var(--accent-rgb), 0.12);
  border-color: var(--accent);
  color: var(--accent);
}

/* assumption */
.calc-assumption {
  font-size: 11px;
  color: var(--calc-muted);
  line-height: 1.55;
  background: var(--calc-panel-2);
  border: 1px solid var(--calc-border-soft);
  border-radius: 8px;
  padding: 10px 12px;
  margin-top: 4px;
}

/* how-to box */
.calc-howto {
  margin-top: var(--spacer);
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(var(--accent-rgb), 0.06);
  border: 1px solid rgba(var(--accent-rgb), 0.15);
}

.calc-howto-title {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--accent);
  margin-bottom: 8px;
}

.calc-howto-list {
  margin: 0;
  padding-left: 18px;
  font-size: 11px;
  color: var(--calc-muted);
  line-height: 1.6;
}

.calc-howto-list li {
  margin-bottom: 2px;
}

/* headline */
.calc-headline {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  padding: 14px 16px;
  border-radius: 10px;
  background: var(--calc-panel-2);
  border: 1px solid var(--calc-border-soft);
  margin-bottom: 20px;
}

.calc-headline-item {
  display: flex;
  flex-direction: column;
}

.calc-hl-n {
  font-family: var(--code-font-family);
  font-size: 20px;
  font-weight: 600;
  color: var(--accent);
}

.calc-hl-l {
  font-size: 10.5px;
  color: var(--calc-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-top: 2px;
}

/* bars */
.calc-bars {
  display: flex;
  flex-direction: column;
  gap: 18px;
  margin-bottom: var(--spacer);
}

.calc-bar-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  margin-bottom: 6px;
  font-size: 13px;
}

.calc-bar-head-note {
  margin-bottom: 4px;
}

.calc-bar-market {
  font-weight: 500;
  color: var(--calc-text);
}

.calc-bar-rate {
  font-family: var(--code-font-family);
  font-size: 10.5px;
  color: var(--calc-muted);
  margin-left: auto;
}

.calc-bar-note {
  width: 100%;
  text-align: right;
  font-size: 10px;
  color: var(--calc-muted-2);
  line-height: 1.3;
}

.calc-bar-track {
  height: 30px;
  background: var(--calc-panel-2);
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  border: 1px solid var(--calc-border-soft);
}

.calc-bar-fill {
  height: 100%;
  border-radius: 6px 0 0 6px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 10px;
  transition: width 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
  min-width: 2px;
}

.calc-bar-fill span {
  font-family: var(--code-font-family);
  font-size: 11.5px;
  font-weight: 600;
  color: var(--oc-gray-9);
  white-space: nowrap;
}

.calc-bar-fill-outside span {
  color: var(--calc-text);
  padding-left: 8px;
}

/* toggle */
.calc-toggle {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 11px 12px;
  background: var(--calc-panel-2);
  border: 1px solid var(--calc-border-soft);
  border-radius: 8px;
  margin-bottom: var(--spacer-2);
  cursor: pointer;
}

.calc-toggle input {
  margin-top: 2px;
  accent-color: var(--oc-yellow-6);
  width: 15px;
  height: 15px;
  cursor: pointer;
  flex: none;
}

.calc-toggle-text {
  font-size: 11.5px;
  color: var(--calc-muted);
  line-height: 1.5;
}

.calc-toggle-text b {
  color: var(--oc-gray-2);
  font-weight: 500;
}

/* narrative */
.calc-narrative {
  margin-top: var(--spacer-2);
  font-size: 13px;
  line-height: 1.65;
  color: var(--oc-gray-3);
  border-top: 1px solid var(--calc-border-soft);
  padding-top: 16px;
}

.calc-narrative b {
  color: var(--accent);
}

/* panel note */
.calc-panel-note {
  margin-top: 18px;
  font-size: 11px;
  color: var(--calc-muted);
  line-height: 1.6;
  border-top: 1px solid var(--calc-border-soft);
  padding-top: 12px;
}

.calc-panel-note b {
  color: var(--oc-gray-2);
  font-weight: 500;
}

.calc-panel-note a {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.calc-updated {
  font-family: var(--code-font-family);
  font-size: 10px;
  color: var(--calc-muted-2);
  margin-top: 14px;
  text-align: center;
}

/* page content */
.calc-intro,
.calc-section {
  --calc-border-soft: rgba(73,80,87,0.5);
  --calc-muted: var(--oc-gray-5);
  --calc-muted-2: var(--oc-gray-6);
}

.calc-intro {
  font-size: 13px;
  line-height: 1.7;
  color: var(--oc-gray-3);
  margin-bottom: var(--spacer-2);
}

.calc-intro p {
  margin-bottom: 10px;
}

.calc-intro strong {
  color: var(--accent);
}

.calc-intro a {
  text-decoration: underline;
  text-underline-offset: 2px;
}

.calc-section {
  margin-top: var(--spacer-3);
}

.calc-section[id] {
  scroll-margin-top: 80px;
}

.calc-section h2 {
  font-size: 18px;
  line-height: 1.3;
  color: var(--oc-gray-1);
  margin-bottom: 10px;
}

.calc-section p,
.calc-section li {
  font-size: 13px;
  line-height: 1.7;
  color: var(--oc-gray-3);
}

.calc-section p a {
  text-decoration: underline;
  text-underline-offset: 2px;
}

.calc-section ul,
.calc-section ol {
  padding-left: 20px;
  margin-bottom: 12px;
}

.calc-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  margin: 10px 0 16px;
}

.calc-table caption {
  caption-side: top;
  text-align: left;
  font-size: 11px;
  color: var(--calc-muted);
  padding-bottom: 8px;
}

.calc-table th,
.calc-table td {
  border-bottom: 1px solid var(--calc-border-soft);
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}

.calc-table th {
  color: var(--calc-muted);
  font-weight: 600;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.calc-table td {
  color: var(--oc-gray-3);
}

.calc-faq details {
  border-bottom: 1px solid var(--calc-border-soft);
  padding: 10px 0;
}

.calc-faq summary {
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  color: var(--oc-gray-2);
}

.calc-faq p {
  margin-top: 8px;
}

.calc-sources {
  font-size: 11.5px;
  line-height: 1.65;
  color: var(--calc-muted);
}

.calc-sources p a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid rgba(var(--accent-rgb), 0.35);
}

/* responsive */
@media (prefers-reduced-motion: reduce) {
  .calc-dot {
    animation: none;
  }

  .calc-bar-fill {
    transition: none;
  }
}

@media (max-width: 860px) {
  .calc-grid {
    grid-template-columns: 1fr;
  }

  .calc-headline {
    flex-direction: column;
    gap: 12px;
  }

  .calc-table {
    font-size: 11px;
  }

  .calc-table th,
  .calc-table td {
    padding: 6px;
  }
}
</style>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Calculadora energética para data centers en Paraguay",
  "url": "https://muchotexto.net/calculadora-energetica/",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "isAccessibleForFree": true,
  "description": "Calcula el costo anual de electricidad de un data center en Paraguay con la tarifa de IA de ANDE (Res. 52552/2026) y lo compara con Irlanda, Virginia, Suecia y Chile."
}
</script>

<div class="calc-intro">
  <p><strong>Actualizado el 21 de noviembre de 2026.</strong> La Resolución 52552/2026 creó un régimen propio para IA, nube, hiperescala y HPC. La tarifa media es de <strong>{{ t.media_220 | replace: ".", "," }} US$/MWh</strong> en 220 kV y de <strong>{{ t.media_23 | replace: ".", "," }} US$/MWh</strong> en 23 kV.</p>
  <p>La calculadora compara el costo anual con Irlanda, Virginia, Suecia y Chile. El GCIE de {{ g.referencia }} US$/MWh quedó para criptominería: <a href="#cambios">ver qué cambió</a>.</p>
</div>

<div class="calc-energetica-page">
{% include calculadora-energetica.html %}
</div>

<section class="calc-section" id="cambios">
  <h2>Qué cambió con la Resolución 52552/2026</h2>
  <p>Hasta octubre de 2026, los data centers se cobijaban en el Grupo de Consumo Intensivo Especial (GCIE). La extensión de ese régimen por los decretos 5306, 5307, 5860 y 5861 había sido derogada el 9 de junio de 2026, y el Pliego de Tarifas N° 21 no tenía un grupo para IA, nube, hiperescala ni HPC. La Resolución 52552/2026 los separó en un grupo propio, con tarifas más altas y una actualización anual.</p>
  <table class="calc-table">
    <caption>Fuente: ANDE, Res. 52552/2026 (tecnología avanzada) y Res. 49238/2024 (GCIE).</caption>
    <thead>
      <tr><th>Concepto</th><th>GCIE (Res. 49238/2024)</th><th>Tecnología avanzada (Res. 52552/2026)</th></tr>
    </thead>
    <tbody>
      <tr><td>Aplica a</td><td>Criptominería y validación de blockchain</td><td>IA, nube, centros de datos de hiperescala y HPC</td></tr>
      <tr><td>Energía en 220 kV</td><td>{{ g.energia_220 }} US$/MWh según horario</td><td>{{ t.energia_220 }} US$/MWh según horario</td></tr>
      <tr><td>Energía en 23 kV</td><td>{{ g.energia_23 }} US$/MWh según modalidad y horario</td><td>{{ t.energia_23 }} US$/MWh según modalidad y horario</td></tr>
      <tr><td>Promedio 220 kV</td><td>—</td><td>{{ t.media_220 | replace: ".", "," }} US$/MWh</td></tr>
      <tr><td>Promedio 23 kV</td><td>—</td><td>{{ t.media_23 | replace: ".", "," }} US$/MWh</td></tr>
      <tr><td>Ajuste</td><td>Régimen temporal</td><td>CPI + PPI de EE.UU., piso de {{ t.ajuste_piso | replace: ".", "," }}% anual desde {{ t.primera_actualizacion }}</td></tr>
      <tr><td>Vigencia</td><td>Contratos hasta el año 2027</td><td>Sin fecha de finalización en la resolución</td></tr>
    </tbody>
  </table>
  <p>La resolución también creó requisitos de acreditación: declaración jurada de intención de obtener certificación Tier III o TIA-942 Rated 3, contrato con un cliente de clase mundial, estados financieros auditados, origen lícito de fondos y control efectivo del terreno. La ANDE reportó unas {{ t.solicitudes_mw_label }} MW de solicitudes, pero solo unos {{ t.disponible_mw }} MW disponibles; tras los {{ t.comprometido_mw }} MW comprometidos con Kuntur quedan aproximadamente {{ t.restante_mw }} MW. El detalle está en el <a href="/dashboard-energetico/">dashboard energético</a>, la <a href="/entidades/ande/">ficha de ANDE</a> y el <a href="/radar-legislativo/">radar legislativo</a>.</p>
</section>

<section class="calc-section" id="metodologia">
  <h2>Cómo se calcula y qué no incluye</h2>
  <p>La calculadora multiplica la capacidad instalada por 8.760 horas anuales y por la tarifa media de 220 kV. Es un ejercicio de orden de magnitud, no una factura:</p>
  <ul>
    <li><strong>Tarifa Paraguay:</strong> {{ t.media_220 | replace: ".", "," }} US$/MWh en 220 kV. El promedio combina energía ({{ t.energia_220 }} US$/MWh) y potencia reservada; no es una tarifa única.</li>
    <li><strong>23 kV:</strong> la media es {{ t.media_23 | replace: ".", "," }} US$/MWh, pero ese nivel tiene un tope de 6 MW en subestación y no se usa en el cálculo.</li>
    <li><strong>Comparación internacional:</strong> rangos de mercado para Suecia, Chile, Virginia e Irlanda. No son tarifas reguladas equivalentes ni incluyen impuestos.</li>
    <li><strong>Escenario Ceare:</strong> lleva la tarifa paraguaya a 51,4 US$/MWh, la referencia técnica para alta y muy alta tensión en 2030.</li>
  </ul>
  <p>El resultado no incluye conexión, transmisión, respaldo, impuestos, costo de capital ni depreciación. Tampoco modela punta y fuera de punta ni excesos de potencia: usa un perfil continuo. Para un proyecto real, la factura de ANDE depende del perfil horario, la potencia reservada y el nivel de tensión.</p>
  <p>El ecosistema completo de data centers, energía y regulación está en la <a href="/ia-en-paraguay/">página pilar del observatorio</a>.</p>
</section>

<section class="calc-section calc-faq">
  <h2>Preguntas frecuentes</h2>

  <details>
    <summary>¿Cuánto paga un data center de IA por electricidad en Paraguay?</summary>
    <p>La tarifa media es de {{ t.media_220 | replace: ".", "," }} US$/MWh en 220 kV y de {{ t.media_23 | replace: ".", "," }} US$/MWh en 23 kV. Son promedios que combinan energía y potencia reservada; la energía sola va de {{ t.energia_min | replace: ".", "," }} a {{ t.energia_max | replace: ".", "," }} US$/MWh según tensión y horario.</p>
  </details>

  <details>
    <summary>¿La tarifa de {{ g.referencia }} US$/MWh sigue vigente?</summary>
    <p>Para criptominería y validación de blockchain sigue el GCIE de la Resolución 49238/2024. Para IA, nube, hiperescala y HPC rige la Resolución 52552/2026, con un promedio de {{ t.media_220 | replace: ".", "," }} US$/MWh en 220 kV.</p>
  </details>

  <details>
    <summary>¿La tarifa queda fija durante los 15 años del contrato?</summary>
    <p>No. El contrato de Kuntur dura 15 años, pero la tarifa se ajusta cada año con un piso de {{ t.ajuste_piso | replace: ".", "," }}% desde {{ t.primera_actualizacion }} y se revisa cada dos años según el costo medio de generación de la ANDE.</p>
  </details>

  <details>
    <summary>¿Qué potencia tiene disponible la ANDE?</summary>
    <p>La ANDE reportó solicitudes por unas {{ t.solicitudes_mw_label }} MW, pero aclaró que no son pedidos firmes. Dispone de unos {{ t.disponible_mw }} MW; con los {{ t.comprometido_mw }} MW comprometidos con Kuntur quedan aproximadamente {{ t.restante_mw }} MW.</p>
  </details>

  <details>
    <summary>¿Qué pasa si un proyecto consume más potencia que la reservada?</summary>
    <p>Paga un recargo por exceso: 6 veces el precio de la potencia reservada en punta y 4 veces fuera de punta. En 220 kV equivale a 34,88 y 15,49 US$/kW-mes, respectivamente.</p>
  </details>

  <details>
    <summary>¿La calculadora incluye impuestos y costos de conexión?</summary>
    <p>No. Aísla el componente de energía y potencia. No incluye impuestos, transmisión, conexión, respaldo ni una cotización real de ANDE.</p>
  </details>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Cuánto paga un data center de IA por electricidad en Paraguay?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La tarifa media es de {{ t.media_220 | replace: ".", "," }} US$/MWh en 220 kV y de {{ t.media_23 | replace: ".", "," }} US$/MWh en 23 kV. Son promedios que combinan energía y potencia reservada; la energía sola va de {{ t.energia_min | replace: ".", "," }} a {{ t.energia_max | replace: ".", "," }} US$/MWh según tensión y horario."
      }
    },
    {
      "@type": "Question",
      "name": "¿La tarifa de {{ g.referencia }} US$/MWh sigue vigente?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Para criptominería y validación de blockchain sigue el GCIE de la Resolución 49238/2024. Para IA, nube, hiperescala y HPC rige la Resolución 52552/2026, con un promedio de {{ t.media_220 | replace: ".", "," }} US$/MWh en 220 kV."
      }
    },
    {
      "@type": "Question",
      "name": "¿La tarifa queda fija durante los 15 años del contrato?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. El contrato de Kuntur dura 15 años, pero la tarifa se ajusta cada año con un piso de {{ t.ajuste_piso | replace: ".", "," }}% desde {{ t.primera_actualizacion }} y se revisa cada dos años según el costo medio de generación de la ANDE."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué potencia tiene disponible la ANDE?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La ANDE reportó solicitudes por unas {{ t.solicitudes_mw_label }} MW, pero aclaró que no son pedidos firmes. Dispone de unos {{ t.disponible_mw }} MW; con los {{ t.comprometido_mw }} MW comprometidos con Kuntur quedan aproximadamente {{ t.restante_mw }} MW."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué pasa si un proyecto consume más potencia que la reservada?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Paga un recargo por exceso: 6 veces el precio de la potencia reservada en punta y 4 veces fuera de punta. En 220 kV equivale a 34,88 y 15,49 US$/kW-mes, respectivamente."
      }
    },
    {
      "@type": "Question",
      "name": "¿La calculadora incluye impuestos y costos de conexión?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Aísla el componente de energía y potencia. No incluye impuestos, transmisión, conexión, respaldo ni una cotización real de ANDE."
      }
    }
  ]
}
</script>

<section class="calc-section calc-sources">
  <h2>Fuentes</h2>
  <p>
    <a href="https://www.ande.gov.py/docs/tarifas/RP52552%20Grupo%20Consumo%20Ind.%20Elect.%20Tec.%20Avanzada.pdf">ANDE — Resolución P/N° 52552/2026</a>, Grupo de Consumo de Industrias Electrointensivas de Tecnología Avanzada (21-oct-2026).<br>
    <a href="https://www.abc.com.py/economia/2026/10/24/ande-crea-por-resolucion-tarifa-para-centros-de-ia-y-fija-requisitos-pero-su-disponibilidad-es-limitada/">ABC Color — "ANDE crea por resolución tarifa para centros de IA y fija requisitos, pero su disponibilidad es limitada"</a> (24-oct-2026).<br>
    <a href="https://www.abc.com.py/economia/2026/11/01/tarifa-para-centros-de-ia-ande-cobrara-entre-us-34-y-46-por-mwh-de-energia-mas-la-potencia-reservada/">ABC Color — "Tarifa para centros de IA: ANDE cobrará entre US$ 34 y 46 por MWh de energía, más la potencia reservada"</a> (1-nov-2026).<br>
    <a href="https://www.abc.com.py/economia/2026/11/01/tarifa-de-la-ande-para-centros-de-ia-subira-como-minimo-25-por-ano-desde-2028-y-se-revisara-cada-dos-anos/">ABC Color — "Tarifa de la ANDE para centros de IA subirá como mínimo 2,5% por año desde 2028 y se revisará cada dos años"</a> (1-nov-2026).<br>
    <a href="https://www.abc.com.py/economia/2026/11/04/piden-6000-mw-y-quedan-464-cuales-son-los-requisitos-de-ande-para-dar-energia-a-centros-de-ia/">ABC Color — "Piden 6.000 MW y quedan 464: cuáles son los requisitos de ANDE para dar energía a centros de IA"</a> (4-nov-2026).<br>
    <a href="https://www.abc.com.py/economia/2026/10/23/es-beneficioso-para-la-ande-centro-de-ia-pagara-entre-us-4891-y-5639-por-mwh-de-la-energia/">ABC Color — "¿Es beneficioso para la ANDE? Centro de IA pagará entre US$ 48,91 y 56,39 por MWh de la energía"</a> (23-oct-2026).<br>
    ANDE — <a href="https://www.ande.gov.py/docs/tarifas/RP49238%20Actualizacion%20de%20las%20Tarifas%20de%20Energia%20Electrica%20GCIE-2024.pdf">Resolución P/N° 49238/2024</a>, tarifas del GCIE.
  </p>
  <p><strong>Verificación:</strong> Paraguay, resolución oficial de ANDE y cobertura de ABC Color (24-oct y 1-nov-2026); Suecia, dos fuentes de mercado independientes; Chile y Virginia, una fuente de mercado cada una; Irlanda, Eurostat (nrg_pc_205, edición abril 2026; datos del 2.º semestre de 2025) y una fuente de mercado. Los rangos internacionales son referencias de mercado, no tarifas reguladas, y no incluyen impuestos ni condiciones contractuales locales.</p>
</section>
