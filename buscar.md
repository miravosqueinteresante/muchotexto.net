---
layout: page
title: Buscar
permalink: /buscar/
description: "Buscá en muchotexto.net artículos, editoriales y análisis sobre inteligencia artificial, tecnología y Paraguay."
sitemap: false
---

<div class="search-form">
  <input type="text" id="search-input" class="search-input" placeholder="Escribe para buscar..." autofocus>
</div>

<ul id="search-results" class="search-results"></ul>

<style>
.search-input {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  background: var(--code-bg-color);
  color: var(--body-color);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
}
.search-input:focus {
  border-color: var(--link-color);
}
.search-result-item {
  list-style: none;
  padding: 1rem 0;
  border-bottom: 1px solid var(--border-color);
}
.search-result-item:last-child {
  border-bottom: none;
}
.search-result-item a {
  font-size: 1.1rem;
  text-decoration: none;
}
.search-result-item .post-meta {
  font-size: 0.82em;
  color: var(--text-color-light);
  margin: 0.25rem 0;
}
.search-result-item .search-excerpt {
  font-size: 0.9rem;
  opacity: 0.85;
}
</style>

<script>
(function() {
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var posts = [];

  fetch('/search.json')
    .then(function(r) { return r.json(); })
    .then(function(data) {
      posts = data;
      input.addEventListener('input', function() {
        var q = input.value.trim().toLowerCase();
        if (!q) { results.innerHTML = ''; return; }
        var terms = q.split(/\s+/).filter(Boolean);
        var matched = [];
        for (var i = 0; i < posts.length; i++) {
          var p = posts[i];
          var text = (p.title + ' ' + p.excerpt + ' ' + (p.tags || []).join(' ')).toLowerCase();
          var ok = true;
          for (var t = 0; t < terms.length; t++) {
            if (text.indexOf(terms[t]) === -1) { ok = false; break; }
          }
          if (ok) matched.push(p);
          if (matched.length >= 20) break;
        }
        results.innerHTML = matched.length
          ? matched.map(function(p) {
              return '<li class="search-result-item">' +
                '<a href="' + p.url + '">' + p.title + '</a>' +
                '<div class="post-meta">' + (p.type == 'pagina' ? 'P\u00e1gina' : p.date) + '</div>' +
                '<div class="search-excerpt">' + p.excerpt + '</div>' +
                '</li>';
            }).join('')
          : '<li style="list-style:none;opacity:0.6">No se encontraron resultados</li>';
      });
    })
    .catch(function() {
      results.innerHTML = '<li style="list-style:none;opacity:0.6">Error al cargar los datos de búsqueda</li>';
    });
})();
</script>
