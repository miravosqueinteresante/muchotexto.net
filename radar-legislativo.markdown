---
layout: page
title: "Radar legislativo de IA en Paraguay"
permalink: /radar-legislativo/
description: "Estado de leyes, decretos y proyectos de IA, energía y datos en Paraguay: vigentes, en trámite y pendientes. Actualizado con fuentes verificadas."
last_modified_at: 2026-08-28
---

<style>
/* ---------- radar scoped styles ---------- */
.radar-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: var(--spacer-2);
}

.radar-chip {
  font-family: var(--code-font-family);
  font-size: 0.8em;
  padding: 6px 12px;
  background: var(--code-bg-color);
  border: 1px solid var(--border-color);
  border-radius: 999px;
  color: var(--body-color);
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s;
}

.radar-chip:hover {
  border-color: var(--link-color);
  color: var(--link-color);
}

.radar-chip.is-active {
  border-color: var(--link-color);
  color: var(--link-color);
  background: rgba(var(--link-color-rgb), 0.12);
}

.radar-group {
  margin-bottom: var(--spacer-3);
}

.radar-group-title {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 var(--spacer) 0;
  padding-bottom: var(--spacer);
  font-size: 0.95em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--body-color);
  border-bottom: 1px solid var(--border-color);
}

.radar-count {
  font-family: var(--code-font-family);
  font-size: 0.8em;
  opacity: 0.55;
  font-weight: 400;
}

.radar-badge {
  display: inline-block;
  padding: 2px 10px;
  font-size: 0.72em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-radius: 999px;
}

.badge-vigente {
  background: rgba(105, 219, 124, 0.16);
  color: #69db7c;
}

.badge-proyecto {
  background: rgba(255, 212, 59, 0.16);
  color: #ffd43b;
}

.badge-en-tramite {
  background: rgba(77, 171, 247, 0.16);
  color: #4dabf7;
}

.badge-pendiente {
  background: rgba(173, 181, 189, 0.16);
  color: #adb5bd;
}

.radar-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: var(--spacer);
}

.radar-item {
  padding: 0 0 var(--spacer) 0;
  border-bottom: 1px solid var(--border-color);
}

.radar-item a,
.radar-item strong {
  color: var(--heading-color);
  font-size: 0.98em;
  font-weight: 600;
  text-decoration: none;
  line-height: 1.4;
}

.radar-item a:hover {
  color: var(--link-color);
  text-decoration: underline;
}

.radar-nota {
  margin: 6px 0 0 0;
  font-size: 0.85em;
  opacity: 0.75;
  line-height: 1.55;
}

.radar-note {
  margin-top: var(--spacer-2);
  font-size: 0.85em;
  opacity: 0.7;
  line-height: 1.6;
}
</style>

<p>El estado de las leyes, decretos y proyectos que definen la inteligencia artificial, la energía y los datos en Paraguay. Filtrá por estado o leé el <a href="/regulacion/">mapa regulatorio completo</a> organizado por tema.</p>

<div class="radar-filters">
  <button type="button" class="radar-chip is-active" data-filter="todas">Todas</button>
  <button type="button" class="radar-chip" data-filter="vigente">Vigentes</button>
  <button type="button" class="radar-chip" data-filter="proyecto">Proyectos</button>
  <button type="button" class="radar-chip" data-filter="en-tramite">En trámite</button>
  <button type="button" class="radar-chip" data-filter="pendiente">Pendientes</button>
</div>

<section class="radar-group" data-estado="vigente">
  <h3 class="radar-group-title"><span class="radar-badge badge-vigente">Vigente</span> <span class="radar-count">{{ site.data.leyes | where: "estado", "vigente" | size }} normas</span></h3>
  <ul class="radar-list">
    {% for ley in site.data.leyes %}{% if ley.estado == "vigente" %}
    <li class="radar-item">
      {% if ley.articulo %}<a href="{{ ley.articulo }}">{{ ley.nombre }}</a>{% else %}<strong>{{ ley.nombre }}</strong>{% endif %}
      <p class="radar-nota">{{ ley.nota }}</p>
    </li>
    {% endif %}{% endfor %}
  </ul>
</section>

<section class="radar-group" data-estado="proyecto">
  <h3 class="radar-group-title"><span class="radar-badge badge-proyecto">Proyecto de ley</span> <span class="radar-count">{{ site.data.leyes | where: "estado", "proyecto" | size }} proyectos</span></h3>
  <ul class="radar-list">
    {% for ley in site.data.leyes %}{% if ley.estado == "proyecto" %}
    <li class="radar-item">
      {% if ley.articulo %}<a href="{{ ley.articulo }}">{{ ley.nombre }}</a>{% else %}<strong>{{ ley.nombre }}</strong>{% endif %}
      <p class="radar-nota">{{ ley.nota }}</p>
    </li>
    {% endif %}{% endfor %}
  </ul>
</section>

<section class="radar-group" data-estado="en-tramite">
  <h3 class="radar-group-title"><span class="radar-badge badge-en-tramite">En trámite</span> <span class="radar-count">{{ site.data.leyes | where: "estado", "en-tramite" | size }} procesos</span></h3>
  <ul class="radar-list">
    {% for ley in site.data.leyes %}{% if ley.estado == "en-tramite" %}
    <li class="radar-item">
      {% if ley.articulo %}<a href="{{ ley.articulo }}">{{ ley.nombre }}</a>{% else %}<strong>{{ ley.nombre }}</strong>{% endif %}
      <p class="radar-nota">{{ ley.nota }}</p>
    </li>
    {% endif %}{% endfor %}
  </ul>
</section>

<section class="radar-group" data-estado="pendiente">
  <h3 class="radar-group-title"><span class="radar-badge badge-pendiente">Pendiente (sin norma)</span> <span class="radar-count">{{ site.data.leyes | where: "estado", "pendiente" | size }} vacíos</span></h3>
  <ul class="radar-list">
    {% for ley in site.data.leyes %}{% if ley.estado == "pendiente" %}
    <li class="radar-item">
      {% if ley.articulo %}<a href="{{ ley.articulo }}">{{ ley.nombre }}</a>{% else %}<strong>{{ ley.nombre }}</strong>{% endif %}
      <p class="radar-nota">{{ ley.nota }}</p>
    </li>
    {% endif %}{% endfor %}
  </ul>
</section>

<p class="radar-note">Esta vista por estado complementa el <a href="/regulacion/">mapa regulatorio</a> (organizado por tema) y la <a href="/cronologia/">cronología</a> (organizada por fecha). Se actualiza con cada investigación nueva y se re-verifica contra fuentes oficiales.</p>

<script>
(function () {
  var chips = document.querySelectorAll('.radar-chip');
  var groups = document.querySelectorAll('.radar-group');
  if (!chips.length || !groups.length) return;

  for (var i = 0; i < chips.length; i++) {
    chips[i].addEventListener('click', function () {
      for (var c = 0; c < chips.length; c++) chips[c].classList.remove('is-active');
      this.classList.add('is-active');
      var f = this.getAttribute('data-filter');
      for (var g = 0; g < groups.length; g++) {
        var show = f === 'todas' || groups[g].getAttribute('data-estado') === f;
        groups[g].style.display = show ? '' : 'none';
      }
    });
  }
})();
</script>
