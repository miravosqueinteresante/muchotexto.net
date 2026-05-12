---
layout: page
title: Buscar
permalink: /buscar/
---

<div class="search-form">
  <input type="text" id="search-input" class="search-input" placeholder="Escribe para buscar..." autofocus>
</div>

<ul id="search-results" class="search-results"></ul>

<script src="https://unpkg.com/simple-jekyll-search@1.10.0/dest/simple-jekyll-search.min.js"></script>
<script>
var sjs = SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('search-results'),
  json: '{{ '/search.json' | relative_url }}',
  searchResultTemplate: '<li class="search-result-item"><a href="{url}">{title}</a><div class="post-meta">{date}</div><div class="search-excerpt">{excerpt}</div></li>',
  noResultsText: '<li style="list-style:none;opacity:0.6">No se encontraron resultados</li>',
  limit: 20,
  fuzzy: false
});
</script>
