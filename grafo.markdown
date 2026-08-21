---
layout: page
title: "Grafo del Observatorio"
permalink: /grafo/
description: "Mapa de relaciones entre las 18 entidades del Observatorio de IA en Paraguay. Quién comparte artículos, leyes y normativas: ANDE, Itaipú, HIVE, Taiwán, TSMC y más."
last_modified_at: 2026-08-20
---

<style>
/* ponytail: page-level override for wider layout */
.grafo-page .container {
  max-width: 1120px;
}

/* ---------- grafo scoped styles ---------- */
.grafo {
  font-family: var(--body-font-family);
  margin-bottom: var(--spacer-3);
}

.grafo-eyebrow {
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

.grafo-dot-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  box-shadow: 0 0 0 3px rgba(34, 184, 207, 0.18);
  animation: grafo-pulse 2.4s ease-in-out infinite;
}

@keyframes grafo-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.35; }
}

.grafo-intro {
  font-size: 0.92em;
  line-height: 1.6;
  opacity: 0.85;
  margin: 0 0 var(--spacer-2) 0;
}

.grafo-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: var(--spacer);
  font-size: 0.8em;
  opacity: 0.8;
}

.grafo-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.grafo-dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex: none;
}

.c-gobierno { background: #22b8cf; fill: #22b8cf; }
.c-infraestructura { background: #4dabf7; fill: #4dabf7; }
.c-empresa { background: #69db7c; fill: #69db7c; }
.c-geopolitica { background: #ff6b6b; fill: #ff6b6b; }
.c-comunidad { background: #ffd43b; fill: #ffd43b; }
.c-academia { background: #b197fc; fill: #b197fc; }

.grafo-stage {
  background: var(--oc-gray-9);
  border: 1px solid var(--oc-gray-7);
  border-radius: 14px;
  padding: 16px;
  margin-bottom: var(--spacer-2);
}

.grafo-canvas {
  position: relative;
  width: 100%;
  max-width: 860px;
  aspect-ratio: 1200 / 800;
  margin: 0 auto;
}

.grafo-canvas svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
}

.grafo-guide {
  fill: none;
  stroke: var(--oc-gray-7);
  stroke-width: 1.5;
  opacity: 0.45;
}

.grafo-edge {
  stroke: var(--oc-gray-6);
  opacity: 0.18;
  transition: opacity 0.2s ease, stroke 0.2s ease;
}

.grafo-edge.is-active {
  stroke: var(--link-color);
  opacity: 0.95;
}

.grafo-edge.is-dim {
  opacity: 0.03;
}

.grafo-node-dot {
  stroke: #14171a;
  stroke-width: 2;
  cursor: pointer;
  transition: opacity 0.2s ease, stroke-width 0.2s ease;
}

.grafo-node-dot.is-active {
  stroke: #ffffff;
  stroke-width: 3.5;
}

.grafo-node-dot.is-neighbor {
  opacity: 1;
}

.grafo-node-dot.is-dim {
  opacity: 0.1;
}

.grafo-node-dot.is-isolated {
  opacity: 0.35;
  stroke-dasharray: 3 3;
}

.grafo-labels {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.grafo-label {
  position: absolute;
  pointer-events: auto;
  background: transparent;
  border: none;
  padding: 2px 6px;
  color: var(--oc-gray-3);
  font-family: var(--code-font-family);
  font-size: 11px;
  line-height: 1.25;
  max-width: 170px;
  cursor: pointer;
  transition: color 0.15s ease, opacity 0.15s ease;
}

.grafo-label.pos-right { transform: translate(14px, -50%); text-align: left; }
.grafo-label.pos-left { transform: translate(calc(-100% - 14px), -50%); text-align: right; }
.grafo-label.pos-top { transform: translate(-50%, calc(-100% - 10px)); text-align: center; }
.grafo-label.pos-bottom { transform: translate(-50%, 10px); text-align: center; }

.grafo-label:hover,
.grafo-label:focus {
  color: var(--oc-white);
  outline: none;
}

.grafo-label.is-active {
  color: var(--oc-white);
}

.grafo-label.is-dim {
  opacity: 0.25;
}

.grafo-active {
  display: block;
  width: fit-content;
  max-width: 100%;
  margin: 16px auto 0;
  padding: 8px 16px;
  background: var(--oc-gray-8);
  border: 1px solid var(--border-color);
  border-radius: 999px;
  color: var(--oc-gray-2);
  font-family: var(--code-font-family);
  font-size: 12px;
  line-height: 1.3;
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.grafo-active.is-empty {
  opacity: 0.6;
}

.grafo-active:not(.is-empty) {
  border-color: var(--link-color);
  color: var(--oc-gray-1);
}

.grafo-noscript {
  font-size: 0.85em;
  opacity: 0.7;
  text-align: center;
  padding: var(--spacer);
}

.grafo-list-title {
  font-size: 0.95em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.6;
  margin: 0 0 var(--spacer) 0;
}

.grafo-entities {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
}

@media (min-width: 40rem) {
  .grafo-entities {
    grid-template-columns: repeat(2, 1fr);
  }
}

.grafo-entity a {
  display: flex;
  align-items: baseline;
  gap: 8px;
  padding: 8px 10px;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  color: inherit;
  text-decoration: none;
  font-size: 0.85em;
  line-height: 1.4;
  transition: border-color 0.15s;
}

.grafo-entity a:hover {
  border-color: var(--link-color);
}

.grafo-entity .grafo-dot {
  align-self: center;
}

@media (max-width: 47.99rem) {
  .grafo-label { display: none; }
  .grafo-canvas { max-width: 100%; }
  .grafo-active { font-size: 11px; }
}
</style>

<div class="grafo-page">
{% include grafo-observatorio.html %}
</div>
