---
layout: page
title: "Calculadora energ\u00e9tica \u2014 Data Centers"
permalink: /calculadora-energetica/
description: "Compar\u00e1 el costo de electricidad para un data center en Paraguay vs. Irlanda, Virginia, Suecia y Chile. Tarifas oficiales verificadas."
last_modified_at: 2026-08-08
---

<style>
/* ponytail: page-level override for wider layout */
.calc-energetica-page .container {
  max-width: 1120px;
}

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
  color: var(--oc-cyan-4);
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 var(--spacer) 0;
}

.calc-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  box-shadow: 0 0 0 3px rgba(34,184,207,0.18);
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
  background: linear-gradient(180deg, rgba(250,176,5,0.10), rgba(250,176,5,0.04));
  border: 1px solid rgba(250,176,5,0.35);
  border-radius: 10px;
  padding: 14px 16px;
  margin-bottom: var(--spacer-2);
}

.calc-alert-icon {
  font-size: 16px;
  color: var(--oc-yellow-4);
  line-height: 1;
  margin-top: 1px;
  flex: none;
}

.calc-alert-title {
  font-weight: 600;
  font-size: 13px;
  color: var(--oc-yellow-4);
  margin-bottom: 5px;
}

.calc-alert-text {
  font-size: 11.5px;
  color: var(--oc-gray-3);
  line-height: 1.6;
}

.calc-alert-text b {
  color: var(--oc-yellow-4);
}

.calc-alert-text a {
  color: var(--oc-cyan-4);
  text-decoration: none;
  border-bottom: 1px solid rgba(34,184,207,0.35);
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
  color: var(--oc-cyan-4);
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
  outline: none;
  cursor: pointer;
}

.calc-energetica input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  border: 2px solid var(--oc-gray-9);
  box-shadow: 0 0 0 3px rgba(34,184,207,0.22);
  cursor: pointer;
}

.calc-energetica input[type=range]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--oc-cyan-4);
  border: 2px solid var(--oc-gray-9);
  box-shadow: 0 0 0 3px rgba(34,184,207,0.22);
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
  border-color: var(--oc-cyan-4);
  color: var(--oc-cyan-4);
}

.calc-preset-btn.active {
  background: rgba(34,184,207,0.12);
  border-color: var(--oc-cyan-4);
  color: var(--oc-cyan-4);
}

/* assumption */
.calc-assumption {
  font-size: 11px;
  color: var(--calc-muted-2);
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
  background: rgba(34,184,207,0.06);
  border: 1px solid rgba(34,184,207,0.15);
}

.calc-howto-title {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--oc-cyan-4);
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
  color: var(--oc-cyan-4);
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
  color: var(--oc-cyan-4);
}

/* disclaimer */
.calc-disclaimer {
  margin-top: 18px;
  font-size: 10.5px;
  color: var(--calc-muted-2);
  line-height: 1.65;
  border-top: 1px solid var(--calc-border-soft);
  padding-top: 14px;
}

.calc-disclaimer b {
  color: var(--oc-gray-2);
  font-weight: 500;
}

.calc-updated {
  font-family: var(--code-font-family);
  font-size: 10px;
  color: var(--calc-muted-2);
  margin-top: 14px;
  text-align: center;
}

/* responsive */
@media (max-width: 860px) {
  .calc-energetica-page .container {
    max-width: 100%;
  }

  .calc-grid {
    grid-template-columns: 1fr;
  }

  .calc-headline {
    flex-direction: column;
    gap: 12px;
  }
}
</style>

<div class="calc-energetica-page">
{% include calculadora-energetica.html %}
</div>
