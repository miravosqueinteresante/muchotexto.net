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

<p class="claims-intro">40 registros revisados al 16-nov-2026: 37 claims y 3 correcciones. El estado indica la veracidad; Evidencia A-E indica la calidad de la fuente.</p>

<div class="claims-legend">
  <span class="claims-legend-item"><span class="claim-v v-true">TRUE</span> confirmado con fuente</span>
  <span class="claims-legend-item"><span class="claim-v v-false">FALSE</span> era falso, corregido</span>
  <span class="claims-legend-item"><span class="claim-v v-partial">PARCIAL</span> impreciso, matizado</span>
  <span class="claims-legend-item"><span class="claim-v v-unverifiable">NO VERIFICABLE</span> sin fuente sólida</span>
  <span class="claims-legend-item"><span class="claim-v v-no-demostrable">NO DEMOSTRABLE</span> ausencia no comprobada</span>
</div>

<div class="claims-legend">
  <span class="claims-legend-item"><strong>A</strong> fuente oficial</span>
  <span class="claims-legend-item"><strong>B</strong> fuente corporativa</span>
  <span class="claims-legend-item"><strong>C</strong> técnica independiente</span>
  <span class="claims-legend-item"><strong>D</strong> fuente secundaria</span>
  <span class="claims-legend-item"><strong>E</strong> revisión propia / sin fuente externa</span>
</div>

{% assign secciones = "Energía y data centers|Tarifas ANDE|Itaipú|Demografía y economía|Regulación|Migración y residencia|Ueno y datos personales|Ciberseguridad|Tokenización agro y cripto|Correcciones" | split: "|" %}
{% for seccion in secciones %}
<section class="claims-section">
<h2 class="claims-section-title">{{ seccion }}</h2>
{% assign claims = site.data.claims | where: "seccion", seccion %}
{% for c in claims %}
<div class="claim">
  <div class="claim-head">
    {% case c.estado %}
      {% when 'confirmado' %}<span class="claim-v v-true">TRUE</span>
      {% when 'parcial' %}<span class="claim-v v-partial">PARCIAL</span>
      {% when 'incorrecto' %}<span class="claim-v v-false">FALSE</span>
      {% when 'no_verificable' %}<span class="claim-v v-unverifiable">NO VERIFICABLE</span>
      {% when 'no_demostrable' %}<span class="claim-v v-no-demostrable">NO DEMOSTRABLE</span>
    {% endcase %}
    <span class="claim-text">"{{ c.claim }}"</span>
  </div>
  <span class="claim-source">{{ c.id }} · Fuente: {{ c.fuente }} · Evidencia {{ c.evidencia }} · corte {{ c.fecha_corte }} · revisado {{ c.ultima_verificacion }}{% if c.nota %} · {{ c.nota }}{% endif %} · <a href="{% if c.url contains 'http' %}{{ c.url }}{% else %}{{ c.url | relative_url }}{% endif %}">Fuente</a>{% if c.articulo %} · <a href="{{ c.articulo | relative_url }}">Artículo</a>{% endif %}</span>
</div>
{% endfor %}
</section>
{% endfor %}

<p class="claims-note">Este registro se actualiza con cada fact-check y se contrasta contra fuentes primarias. Si detectás un dato que cambió, escribinos por la <a href="/contacto/">página de contacto</a>. Nuestra metodología completa está en <a href="/como-trabajamos/">cómo trabajamos</a>.</p>

</div>
