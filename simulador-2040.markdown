---
layout: page
title: "Paraguay 2040 — Simulador de escenarios"
permalink: /simulador-2040/
description: "Simulador interactivo: cinco palancas estrategicas determinan el futuro de Paraguay a 2040. Data centers, energia, informalidad, talento y escenarios geopoliticos."
last_modified_at: 2026-08-07
---

<style>
/* ponytail: page-level override for the simulator's wider layout */
.sim-2040-page .container {
  max-width: 1120px;
}

/* ---------- simulator scoped styles ---------- */
.sim-2040 {
  --sim-bg: var(--oc-gray-9);
  --sim-panel: rgba(33,37,41,0.7);
  --sim-panel-2: rgba(52,58,64,0.5);
  --sim-border: var(--oc-gray-7);
  --sim-border-soft: rgba(73,80,87,0.5);
  --sim-text: var(--oc-gray-3);
  --sim-muted: var(--oc-gray-5);
  --sim-muted-2: var(--oc-gray-6);

  font-family: var(--body-font-family);
  margin-bottom: var(--spacer-3);
}

.sim-2040 *,
.sim-2040 *::before,
.sim-2040 *::after {
  box-sizing: border-box;
}

.sim-2040 h2,
.sim-2040 h3,
.sim-2040 p {
  margin: 0;
}

/* chips */
.sim-chips {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  margin-top: var(--spacer-2);
  margin-bottom: 22px;
}

.sim-chip {
  background: var(--sim-panel);
  border: 1px solid var(--sim-border-soft);
  border-radius: 10px;
  padding: 12px 14px;
}

.sim-chip-val {
  font-family: var(--code-font-family);
  font-size: 18px;
  font-weight: 600;
  color: var(--oc-gray-2);
  line-height: 1.1;
}

.sim-chip-lbl {
  font-size: 11px;
  color: var(--sim-muted);
  margin-top: 4px;
  line-height: 1.35;
}

/* main grid */
.sim-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 18px;
}

/* panels */
.sim-panel {
  background: var(--sim-panel);
  border: 1px solid var(--sim-border-soft);
  border-radius: 14px;
  padding: 20px;
}

.sim-panel-title {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--sim-muted);
  margin: 0 0 16px;
}

/* levers */
.sim-lever {
  margin-bottom: 18px;
}

.sim-lever:last-of-type {
  margin-bottom: 8px;
}

.sim-lever-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 4px;
}

.sim-lever-name {
  font-size: 13px;
  font-weight: 500;
  color: var(--sim-text);
}

.sim-lever-val {
  font-family: var(--code-font-family);
  font-size: 12px;
  color: var(--oc-cyan-4);
  min-width: 30px;
  text-align: right;
}

.sim-lever-desc {
  font-size: 11px;
  color: var(--sim-muted-2);
  margin-bottom: 8px;
  line-height: 1.4;
}

.sim-2040 input[type=range] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 4px;
  border-radius: 2px;
  background: var(--sim-border);
  outline: none;
  cursor: pointer;
}

.sim-2040 input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  border: 2px solid var(--oc-gray-9);
  box-shadow: 0 0 0 3px rgba(34,184,207,0.22);
  cursor: pointer;
}

.sim-2040 input[type=range]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  border: 2px solid var(--oc-gray-9);
  box-shadow: 0 0 0 3px rgba(34,184,207,0.22);
  cursor: pointer;
}

/* toggles */
.sim-toggle {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 11px 12px;
  background: var(--sim-panel-2);
  border: 1px solid var(--sim-border-soft);
  border-radius: 10px;
  margin-top: 6px;
  cursor: pointer;
  transition: border-color 0.2s ease;
}

.sim-toggle:hover {
  border-color: var(--oc-gray-6);
}

.sim-toggle input {
  margin-top: 2px;
  accent-color: var(--oc-red-6);
  width: 15px;
  height: 15px;
  cursor: pointer;
  flex: none;
}

.sim-toggle-text {
  font-size: 11.5px;
  color: var(--sim-muted);
  line-height: 1.45;
}

.sim-toggle-text b {
  color: var(--oc-gray-2);
  font-weight: 500;
}

/* readout */
.sim-readout {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 18px;
  padding: 14px 16px;
  border-radius: 10px;
  border: 1px solid var(--sim-border-soft);
  background: var(--sim-panel-2);
  transition: border-color 0.25s ease, background 0.25s ease;
}

.sim-readout-label {
  font-family: var(--code-font-family);
  font-size: 10.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sim-muted);
  margin-bottom: 3px;
}

.sim-readout-scenario {
  font-size: 16px;
  font-weight: 600;
  color: var(--oc-gray-2);
}

.sim-readout-metrics {
  display: flex;
  gap: 22px;
  font-family: var(--code-font-family);
}

.sim-metric-n {
  font-size: 18px;
  font-weight: 600;
  color: var(--oc-gray-2);
  display: block;
  line-height: 1.1;
}

.sim-metric-u {
  font-size: 10px;
  color: var(--sim-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* chart */
.sim-2040 canvas {
  width: 100%;
  display: block;
  border-radius: 4px;
}

.sim-legend {
  display: flex;
  gap: 18px;
  margin-top: 10px;
  font-size: 11px;
  color: var(--sim-muted);
  flex-wrap: wrap;
}

.sim-legend span {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.sim-legend i {
  width: 10px;
  height: 10px;
  border-radius: 2px;
  display: inline-block;
  flex: none;
}

/* narrative */
.sim-narrative {
  margin-top: 16px;
  font-size: 13px;
  line-height: 1.65;
  color: var(--oc-gray-3);
  border-top: 1px solid var(--sim-border-soft);
  padding-top: 14px;
}

/* disclaimer */
.sim-disclaimer {
  margin-top: 20px;
  font-size: 10.5px;
  color: var(--sim-muted-2);
  line-height: 1.6;
  border-top: 1px solid var(--sim-border-soft);
  padding-top: 12px;
}

/* responsive */
@media (max-width: 860px) {
  .sim-2040-page .container {
    max-width: 100%;
  }

  .sim-grid {
    grid-template-columns: 1fr;
  }

  .sim-chips {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .sim-chips {
    grid-template-columns: 1fr;
  }

  .sim-readout {
    flex-direction: column;
    align-items: flex-start;
  }

  .sim-readout-metrics {
    gap: 14px;
  }
}
</style>

<div class="sim-2040-page">
{% include simulador-2040.html %}
</div>
