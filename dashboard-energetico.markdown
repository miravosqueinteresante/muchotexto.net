---
layout: page
title: "Dashboard energético de data centers y tarifas"
permalink: /dashboard-energetico/
description: "Potencia reservada, tarifa GCIE y consumo eléctrico de data centers en Paraguay. Datos verificados contra ANDE y el estudio Ceare."
last_modified_at: 2026-08-21
---

<style>
/* ponytail: page-level override for wider layout */
.dash-page .container {
  max-width: 1120px;
}

/* ---------- dashboard scoped styles ---------- */
.dash {
  font-family: var(--body-font-family);
  margin-bottom: var(--spacer-3);
}

.dash-eyebrow {
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

.dash-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  box-shadow: 0 0 0 3px rgba(34, 184, 207, 0.18);
  animation: dash-pulse 2.4s ease-in-out infinite;
}

@keyframes dash-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.35; }
}

.dash-intro {
  font-size: 0.92em;
  line-height: 1.6;
  opacity: 0.85;
  margin: 0 0 var(--spacer-2) 0;
}

.dash-kpis {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: var(--spacer-3);
}

@media (min-width: 40rem) {
  .dash-kpis {
    grid-template-columns: repeat(4, 1fr);
  }
}

.dash-kpi {
  background: var(--code-bg-color);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 14px 16px;
}

.dash-kpi-value {
  font-family: var(--code-font-family);
  font-size: 22px;
  font-weight: 600;
  color: var(--oc-cyan-4);
  line-height: 1.1;
}

.dash-kpi-label {
  font-size: 0.8em;
  font-weight: 600;
  color: var(--heading-color);
  margin-top: 4px;
}

.dash-kpi-note {
  font-size: 0.72em;
  opacity: 0.6;
  margin-top: 2px;
}

.dash-section {
  margin-bottom: var(--spacer-3);
}

.dash-section-title {
  font-size: 0.95em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.6;
  margin: 0 0 var(--spacer) 0;
  padding-bottom: var(--spacer);
  border-bottom: 1px solid var(--border-color);
}

.dash-bar {
  display: grid;
  grid-template-columns: 52px 1fr 92px;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.dash-bar-year {
  font-family: var(--code-font-family);
  font-size: 0.82em;
  color: var(--heading-color);
}

.dash-bar-track {
  height: 20px;
  background: var(--oc-gray-8);
  border: 1px solid var(--border-color);
  border-radius: 5px;
  overflow: hidden;
}

.dash-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--oc-cyan-6), var(--oc-cyan-4));
  border-radius: 4px 0 0 4px;
  min-width: 2px;
}

.dash-bar-value {
  font-family: var(--code-font-family);
  font-size: 0.8em;
  color: var(--oc-gray-3);
  text-align: right;
}

.dash-timeline {
  list-style: none;
  margin: 0;
  padding: 0;
  border-left: 2px solid var(--border-color);
  padding-left: 20px;
}

.dash-timeline li {
  position: relative;
  margin-bottom: 16px;
}

.dash-timeline li::before {
  content: "";
  position: absolute;
  left: -26px;
  top: 5px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  border: 2px solid var(--oc-gray-9);
}

.dash-tl-date {
  font-family: var(--code-font-family);
  font-size: 0.78em;
  color: var(--oc-cyan-4);
  font-weight: 600;
}

.dash-tl-text {
  font-size: 0.88em;
  line-height: 1.5;
  opacity: 0.85;
  margin-top: 2px;
}

.dash-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85em;
}

.dash-table th,
.dash-table td {
  text-align: left;
  padding: 8px 10px;
  border-bottom: 1px solid var(--border-color);
}

.dash-table th {
  font-size: 0.78em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.55;
  font-weight: 600;
}

.dash-table td:last-child {
  font-family: var(--code-font-family);
  color: var(--oc-cyan-4);
}

.dash-note {
  background: rgba(34, 184, 207, 0.06);
  border: 1px solid rgba(34, 184, 207, 0.18);
  border-radius: 8px;
  padding: 12px 14px;
  margin-top: var(--spacer);
}

.dash-note ul {
  margin: 0;
  padding-left: 18px;
  font-size: 0.82em;
  line-height: 1.6;
  opacity: 0.8;
}

.dash-disclaimer {
  margin-top: var(--spacer-2);
  font-size: 0.8em;
  opacity: 0.65;
  line-height: 1.6;
}
</style>

<div class="dash-page">
<div class="dash">

<p class="dash-eyebrow"><span class="dash-dot"></span>Datos verificados · actualizado 21 de agosto de 2026</p>

<p class="dash-intro">El pulso eléctrico de la economía de IA en Paraguay, en un solo lugar. Potencia reservada para data centers y criptominería, la tarifa del consumo intensivo y el consumo nacional que la sostiene. Cada cifra sale de <a href="/regulacion/">fuentes oficiales</a> verificadas, no de estimaciones propias.</p>

<div class="dash-kpis">
  {% for k in site.data.energia.kpis %}
  <div class="dash-kpi">
    <div class="dash-kpi-value">{{ k.value }}</div>
    <div class="dash-kpi-label">{{ k.label }}</div>
    <div class="dash-kpi-note">{{ k.note }}</div>
  </div>
  {% endfor %}
</div>

<section class="dash-section">
  <h2 class="dash-section-title">Potencia reservada para consumo intensivo</h2>
  <div class="dash-bar">
    <span class="dash-bar-year">2023</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: 13%"></div></div>
    <span class="dash-bar-value">125 MW</span>
  </div>
  <div class="dash-bar">
    <span class="dash-bar-year">2025</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: 87%"></div></div>
    <span class="dash-bar-value">822 MW</span>
  </div>
  <div class="dash-bar">
    <span class="dash-bar-year">2026</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: 100%"></div></div>
    <span class="dash-bar-value">943,8 MW</span>
  </div>
  <p class="dash-disclaimer">Serie GCIE, creada en 2022 (Resolución ANDE 46984). 943,8 MW de potencia reservada y contratada por 41 empresas a agosto de 2026 — no necesariamente operativa.</p>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Consumo nacional de electricidad</h2>
  {% assign max_gwh = 29419 %}
  {% for c in site.data.energia.consumo_nacional %}
  <div class="dash-bar">
    <span class="dash-bar-year">{{ c.year }}</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: {{ c.gwh | times: 100 | divided_by: 29419 }}%"></div></div>
    <span class="dash-bar-value">{{ c.gwh | divided_by: 1000.0 | round: 1 }} TWh</span>
  </div>
  {% endfor %}
  <p class="dash-disclaimer">Demanda del sistema con pérdidas (ANDE). Crecimiento reciente de la demanda: 5,7% (2022), 12,4% (2023), 18,5% (2024), 12,5% (2025), 21% (2026) — el piso oficial reciente es 12,5%.</p>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Tarifa GCIE — línea de tiempo</h2>
  <p class="dash-intro">La tarifa del <strong>Grupo Consumo Intensivo Especial</strong>: {{ site.data.energia.tarifa_gcie.tarifa }} ({{ site.data.energia.tarifa_gcie.resolucion }}), {{ site.data.energia.tarifa_gcie.vigencia }}.</p>
  <ul class="dash-timeline">
    {% for e in site.data.energia.tarifa_gcie.eventos %}
    <li>
      <div class="dash-tl-date">{{ e.fecha }}</div>
      <div class="dash-tl-text">{{ e.texto }}</div>
    </li>
    {% endfor %}
  </ul>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Proyección de tarifa — estudio Ceare</h2>
  <p class="dash-intro">{{ site.data.energia.proyeccion_tarifa.fuente }}. Es proyección/recomendación, no tarifa aplicada.</p>
  <table class="dash-table">
    <thead>
      <tr><th>Segmento</th><th>Actual</th><th>Proyectada 2030</th></tr>
    </thead>
    <tbody>
      {% for i in site.data.energia.proyeccion_tarifa.items %}
      <tr>
        <td>{{ i.label }}</td>
        <td>{{ i.actual }}</td>
        <td>{{ i.proyectada }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</section>

<div class="dash-note">
  <strong>Distinciones que importan:</strong>
  <ul>
    {% for d in site.data.energia.distincion %}
    <li>{{ d }}</li>
    {% endfor %}
  </ul>
</div>

<p class="dash-disclaimer">Este tablero se re-verifica contra fuentes oficiales cada 30 días (próxima revisión de la tarifa: 7 de septiembre de 2026). Es una instantánea estática, no un feed en tiempo real. Complementa el <a href="/radar-legislativo/">radar legislativo</a> (estado de las normas) y la <a href="/calculadora-energetica/">calculadora de costo energético</a> (comparación internacional).</p>

</div>
</div>
