<?xml version="1.0" encoding="UTF-8"?>
<audit version="0.0.38">
<site url="https://muchotexto.net" crawled="100" date="2026-09-03T00:48:44.696Z"/>
<score overall="76" grade="C">
 <cat name="Structured Data" score="48"/>
 <cat name="Performance" score="94"/>
 <cat name="Accessibility" score="96"/>
 <cat name="Core SEO" score="92"/>
 <cat name="Security" score="77"/>
 <cat name="Crawlability" score="97"/>
 <cat name="Images" score="94"/>
 <cat name="Content" score="94"/>
 <cat name="URL Structure" score="97"/>
 <cat name="Links" score="80"/>
 <cat name="E-E-A-T" score="86"/>
 <cat name="Analytics" score="100"/>
 <cat name="Internationalization" score="100"/>
 <cat name="Legal Compliance" score="100"/>
 <cat name="Local SEO" score="100"/>
 <cat name="Mobile" score="100"/>
 <cat name="Social Media" score="100"/>
</score>
<summary passed="10747" warnings="872" failed="82"/>
<issues>
 <category name="Crawlability" errors="0" warnings="100">
  <rule id="crawl/canonical-chain" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/crawl/canonical-chain">
   Page redirects before content is served
   Pages (5/99): /about, /calculadora-energetica, /casos-de-uso, /claims-verificados, /como-trabajamos
   Items (5/99):
    - /about/ (https://muchotexto.net/about (301) → https://muchotexto.net/about/ (200)) [finalUrl: https://muchotexto.net/about/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/about&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/about/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/about&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;http&quot;},{&quot;url&quot;:&quot;https://muchotexto.net/abo…]
    - /calculadora-energetica/ (https://muchotexto.net/calculadora-energetica (301) → https://muchotexto.net/calculadora-energetica/ (200)) [finalUrl: https://muchotexto.net/calculadora-energetica/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/calculadora-energetica&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/calculadora-energetica/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/calculadora-energetica&quot;,&quot;statusCode&quot;:30…]
    - /casos-de-uso/ (https://muchotexto.net/casos-de-uso (301) → https://muchotexto.net/casos-de-uso/ (200)) [finalUrl: https://muchotexto.net/casos-de-uso/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/casos-de-uso&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/casos-de-uso/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/casos-de-uso&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;http&quot;},{&quot;url&quot;:&quot;https…]
    - /claims-verificados/ (https://muchotexto.net/claims-verificados (301) → https://muchotexto.net/claims-verificados/ (200)) [finalUrl: https://muchotexto.net/claims-verificados/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/claims-verificados&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/claims-verificados/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/claims-verificados&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;ht…]
    - /contacto/ (https://muchotexto.net/contacto (301) → https://muchotexto.net/contacto/ (200)) [finalUrl: https://muchotexto.net/contacto/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/contacto&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/contacto/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/contacto&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;http&quot;},{&quot;url&quot;:&quot;https://muchotext…]
  </rule>
  <rule id="crawl/sitemap-coverage" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/crawl/sitemap-coverage">
   158 sitemap URL(s) were not crawled
   Items (5/158):
    - /articulos/2026/07/01/de-la-soja-al-silicio-matriz-exportadora-paraguay/
    - /pulso-paraguay/2026/07/01/salario-minimo-pulso-paraguay/
    - /editorial/2026/07/01/ajustes-economicos-y-clima-social-editorial-1-de-julio-de-20-editoria/
    - /pulso-paraguay/2026/07/02/libertad-ambulatoria-para-miguel-prieto-pulso-paraguay/
    - /editorial/2026/07/02/corrupcion-y-salud-dos-focos-de-incertidumbre-en-paraguay-ed-editoria/
  </rule>
 </category>
 <category name="Core SEO" errors="0" warnings="109">
  <rule id="core/meta-title" severity="error" status="warn" docs="https://docs.squirrelscan.com/rules/core/meta-title">
   Title too short; Title too long
   Pages (5/71): /about, /calculadora-energetica, /contacto, /dashboard-energetico, /entidades
   Items (5/71):
    - /about/ (Acerca de | muchotexto.net (26 chars))
    - /contacto/ (Contacto | muchotexto.net (25 chars))
    - /entidades/peter-thiel/ (Peter Thiel | muchotexto.net (28 chars))
    - /entidades/x8cloud/ (X8 Cloud | muchotexto.net (25 chars))
    - /calculadora-energetica/ (Calculadora de costo energético — Data Centers | m (63 chars))
  </rule>
  <rule id="core/h1" severity="error" status="warn" docs="https://docs.squirrelscan.com/rules/core/h1">
   Multiple H1 tags found (2)
   Pages (1): /
   Items (1):
    - / (Multiple H1 tags found (2))
  </rule>
  <rule id="core/meta-description" severity="error" status="warn" docs="https://docs.squirrelscan.com/rules/core/meta-description">
   Description too long; Description too short
   Pages (5/37): /, /calculadora-energetica, /claims-verificados, /entidades, /grafo
   Items (5/37):
    - / (Observatorio de inteligencia artificial en Paragua (189 chars))
    - /calculadora-energetica/ (Compará el costo anual de electricidad para un dat (195 chars))
    - /claims-verificados/ (Base pública de verificación de datos de muchotext (163 chars))
    - /grafo/ (Mapa de relaciones entre las 18 entidades del Obse (163 chars))
    - /entidades/ (Índice de entidades clave del Observatorio de IA e (178 chars))
  </rule>
 </category>
 <category name="Security" errors="0" warnings="103">
  <rule id="security/csp" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/security/csp">
   No Content-Security-Policy header
  </rule>
  <rule id="security/hsts" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/security/hsts">
   Missing Strict-Transport-Security header
  </rule>
  <rule id="security/x-frame-options" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/security/x-frame-options">
   No clickjacking protection
  </rule>
  <rule id="security/third-party-cookies" severity="info" status="warn" docs="https://docs.squirrelscan.com/rules/security/third-party-cookies">
   1 known tracking domain(s) detected
   Pages (5/100): /, /about, /calculadora-energetica, /casos-de-uso, /claims-verificados
   Items (1):
    - www.googletagmanager.com (script)
  </rule>
 </category>
 <category name="Links" errors="0" warnings="6">
  <rule id="links/broken-external-links" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/links/broken-external-links">
   28 broken external link(s): 1 with 999, 19 with 404, 1 with 401, 4 with 403, 1 with 400, 2 failed
   Items (5/28):
    - https://www.linkedin.com/in/cesar-sanchez-melgarejo/ (https://www.linkedin.com/in/cesar-sanchez-melgarejo/ (999)) [status: 999] (from: /, /about, /about, /calculadora-energetica, /calculadora-energetica; +195 more)
    - https://www.vouga.com.py/en/avances-en-la-regulaci%C3%B3n-fintech-en-el-paraguay-criptomonedas-y-cripto-activos/ (https://www.vouga.com.py/en/avances-en-la-regulaci%C3%B3n-fintech-en-el-paraguay-criptomonedas-y-cripto-activos/ (404)) [status: 404] (from: /articulos/2026/05/18/tokenizacion-del-agro-paraguay)
    - https://www.abc.com.py/internacionales/2026/05/07/china-insta-a-paraguay-a-romper-sus-relaciones-con-Taiw%C3%A1n-ante-el-viaje-de-pena-a-la-isla/ (https://www.abc.com.py/internacionales/2026/05/07/china-insta-a-paraguay-a-romper-sus-relaciones-con-Taiw%C3%A1n-ante-el-viaje-de-pena-a-la-isla/ (404)) [status: 404] (from: /articulos/2026/05/16/peter-thiel-paraguay-experimento)
    - https://www.abc.com.py/politica/2026/05/13/gobierno-compara-Itaip%C3%BA-con-el-proyecto-centro-ia-paraguay-Taiw%C3%A1n/ (https://www.abc.com.py/politica/2026/05/13/gobierno-compara-Itaip%C3%BA-con-el-proyecto-centro-ia-paraguay-Taiw%C3%A1n/ (404)) [status: 404] (from: /articulos/2026/05/16/peter-thiel-paraguay-experimento)
    - https://www.abc.com.py/economia/2026/03/16/solo-cuatro-criptomineras-consumen-mas-que-una-turbina-de-Itaip%C3%BA/ (https://www.abc.com.py/economia/2026/03/16/solo-cuatro-criptomineras-consumen-mas-que-una-turbina-de-Itaip%C3%BA/ (404)) [status: 404] (from: /articulos/2026/05/16/peter-thiel-paraguay-experimento, /articulos/2026/05/27/apertura-sector-electrico-privado-paraguay, /articulos/2026/05/27/ia-cuesta-mas-que-humanos-burbuja, /articulos/2026/05/27/ia-cuesta-mas-que-humanos-burbuja)
  </rule>
  <rule id="links/https-downgrade" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/links/https-downgrade">
   1 link(s) downgrade to HTTP
   Pages (1): /directorio
   Items (1):
    - http://www.mades.gov.py/
  </rule>
  <rule id="links/orphan-pages" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/links/orphan-pages">
   14 orphan page(s) with &lt;2 incoming links
   Items (5/14):
    - /pulso-paraguay/2026/06/16/crisis-en-neonatologia-del-ips-pulso-paraguay
    - /pulso-paraguay/2026/06/17/caso-maria-fernanda-pulso-paraguay
    - /pulso-paraguay/2026/06/18/vergonzoso-abandono-del-edificio-del-correo-paragu-pulso-paraguay
    - /pulso-paraguay/2026/06/19/juicio-por-el-caso-maria-fernanda-pulso-paraguay
    - /pulso-paraguay/2026/06/20/festejos-por-la-albirroja-pulso-paraguay
  </rule>
  <rule id="links/redirect-chains" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/links/redirect-chains">
   99 page(s) redirect to another URL; 99 link target(s) point to redirecting URLs
   Items (5/198):
    - /about (https://muchotexto.net/about (301) → https://muchotexto.net/about/ (200)) [targetUrl: https://muchotexto.net/about/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/about&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/about/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/about&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;http&quot;},{&quot;url&quot;:&quot;https://muchotexto.net/abo…]
    - /calculadora-energetica (https://muchotexto.net/calculadora-energetica (301) → https://muchotexto.net/calculadora-energetica/ (200)) [targetUrl: https://muchotexto.net/calculadora-energetica/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/calculadora-energetica&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/calculadora-energetica/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/calculadora-energetica&quot;,&quot;statusCode&quot;:30…]
    - /casos-de-uso (https://muchotexto.net/casos-de-uso (301) → https://muchotexto.net/casos-de-uso/ (200)) [targetUrl: https://muchotexto.net/casos-de-uso/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/casos-de-uso&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/casos-de-uso/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/casos-de-uso&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;http&quot;},{&quot;url&quot;:&quot;https…]
    - /claims-verificados (https://muchotexto.net/claims-verificados (301) → https://muchotexto.net/claims-verificados/ (200)) [targetUrl: https://muchotexto.net/claims-verificados/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/claims-verificados&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/claims-verificados/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/claims-verificados&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;ht…]
    - /contacto (https://muchotexto.net/contacto (301) → https://muchotexto.net/contacto/ (200)) [targetUrl: https://muchotexto.net/contacto/, chain: {&quot;sourceUrl&quot;:&quot;https://muchotexto.net/contacto&quot;,&quot;finalUrl&quot;:&quot;https://muchotexto.net/contacto/&quot;,&quot;hops&quot;:[{&quot;url&quot;:&quot;https://muchotexto.net/contacto&quot;,&quot;statusCode&quot;:301,&quot;type&quot;:&quot;http&quot;},{&quot;url&quot;:&quot;https://muchotext…]
  </rule>
  <rule id="links/weak-internal-links" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/links/weak-internal-links">
   14 page(s) have only 1 internal link
   Items (5/14):
    - /pulso-paraguay/2026/06/16/crisis-en-neonatologia-del-ips-pulso-paraguay
    - /pulso-paraguay/2026/06/17/caso-maria-fernanda-pulso-paraguay
    - /pulso-paraguay/2026/06/18/vergonzoso-abandono-del-edificio-del-correo-paragu-pulso-paraguay
    - /pulso-paraguay/2026/06/19/juicio-por-el-caso-maria-fernanda-pulso-paraguay
    - /pulso-paraguay/2026/06/20/festejos-por-la-albirroja-pulso-paraguay
  </rule>
 </category>
 <category name="Content" errors="0" warnings="89">
  <rule id="content/heading-hierarchy" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/content/heading-hierarchy">
   Skipped heading levels detected
   Pages (3): /entidades, /grafo, /radar-legislativo
   Items (1):
    - H1 -&gt; H3
  </rule>
  <rule id="content/keyword-stuffing" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/content/keyword-stuffing">
   N word(s) may be overused
   Pages (5/78): /, /about, /casos-de-uso, /claims-verificados, /cronologia
   Items (5/18):
    - paraguay (&quot;paraguay&quot; (3.6%)) [count: 14, density: 3.5989717223650386]
    - que (&quot;que&quot; (3.2%)) [count: 20, density: 3.1645569620253164]
    - con (&quot;con&quot; (3.0%)) [count: 19, density: 3.0063291139240507]
    - fuente (&quot;fuente&quot; (4.6%)) [count: 29, density: 4.625199362041467]
    - true (&quot;true&quot; (4.0%)) [count: 25, density: 3.9872408293460926]
  </rule>
  <rule id="content/word-count" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/content/word-count">
   Thin content: N words (min N)
   Pages (5/8): /entidades/amcham, /entidades/koga, /entidades/peter-thiel, /entidades/pti-py, /entidades/santiago-pena
   Items (5/8):
    - /entidades/amcham (Thin content: 222 words (min 300))
    - /entidades/koga (Thin content: 274 words (min 300))
    - /entidades/pti-py (Thin content: 254 words (min 300))
    - /entidades/peter-thiel (Thin content: 254 words (min 300))
    - /entidades/santiago-pena (Thin content: 240 words (min 300))
  </rule>
 </category>
 <category name="Structured Data" errors="82" warnings="0">
  <rule id="schema/json-ld-valid" severity="warning" status="fail" docs="https://docs.squirrelscan.com/rules/schema/json-ld-valid">
   Invalid JSON-LD syntax
   Pages (5/82): /, /about, /calculadora-energetica, /casos-de-uso, /claims-verificados
   Items (5/12):
    - parse-0 (Validation: WebSite.name is required)
    - WebSite:name (WebSite missing name) [message: Validation: WebSite.name is required, severity: missing, path: [&quot;name&quot;]]
    - parse-1 (Validation: Article.datePublished is required)
    - parse-2 (Validation: Article.author.name is required)
    - parse-3 (Validation: Article.publisher.name is required)
  </rule>
 </category>
 <category name="Images" errors="0" warnings="99">
  <rule id="images/responsive-size" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/images/responsive-size">
   1 small image(s) may be serving oversized files
   Pages (5/99): /about, /calculadora-energetica, /casos-de-uso, /claims-verificados, /como-trabajamos
   Items (1):
    - cesar-sanchez.webp (56x56, no srcset)
  </rule>
 </category>
 <category name="Performance" errors="0" warnings="211">
  <rule id="perf/ttfb" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/perf/ttfb">
   Slow server response (Nms)
   Pages (2): /articulos/2026/05/28/magnifica-humanitas-enciclica-ia, /pulso-paraguay/2026/05/28/manifestacion-por-ingresos-a-la-policia-pulso-paraguay
   Items (2):
    - /articulos/2026/05/28/magnifica-humanitas-enciclica-ia (Slow server response (686ms))
    - /pulso-paraguay/2026/05/28/manifestacion-por-ingresos-a-la-policia-pulso-paraguay (Slow server response (663ms))
  </rule>
  <rule id="perf/dom-size" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/perf/dom-size">
   Element with N children found
   Pages (5/10): /como-trabajamos, /glosario, /articulos/2026/05/18/tokenizacion-del-agro-paraguay, /articulos/2026/05/27/apertura-sector-electrico-privado-paraguay, /articulos/2026/05/27/ia-cuesta-mas-que-humanos-burbuja
   Items (5/10):
    - /como-trabajamos (Element with 62 children found)
    - /glosario (Element with 100 children found)
    - /articulos/2026/05/18/tokenizacion-del-agro-paraguay (Element with 90 children found)
    - /articulos/2026/05/27/apertura-sector-electrico-privado-paraguay (Element with 110 children found)
    - /articulos/2026/05/27/ia-cuesta-mas-que-humanos-burbuja (Element with 85 children found)
  </rule>
  <rule id="perf/critical-request-chains" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/perf/critical-request-chains">
   1 critical request chain(s) found
   Pages (5/100): /, /about, /calculadora-energetica, /casos-de-uso, /claims-verificados
   Items (1):
    - CSS: /assets/monophase/styles.css
  </rule>
  <rule id="perf/lazy-above-fold" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/perf/lazy-above-fold">
   1 above-fold image(s) with lazy loading
   Pages (5/99): /about, /calculadora-energetica, /casos-de-uso, /claims-verificados, /como-trabajamos
   Items (1):
    - /assets/images/cesar-sanchez.webp
  </rule>
 </category>
 <category name="Accessibility" errors="0" warnings="127">
  <rule id="a11y/color-contrast" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/a11y/color-contrast">
   3 potential color contrast issue(s)
   Pages (5/100): /, /about, /calculadora-energetica, /casos-de-uso, /claims-verificados
   Items (4):
    - Light gray text: 2 instance(s)
    - White text (verify background): 1 instance(s)
    - Very light text color: 3 instance(s)
    - Very light text color: 4 instance(s)
  </rule>
  <rule id="a11y/focus-visible" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/a11y/focus-visible">
   outline:none found - ensure alternative focus styles exist
   Pages (3): /calculadora-energetica, /grafo, /simulador-2040
  </rule>
  <rule id="a11y/heading-order" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/a11y/heading-order">
   1 heading level skip(s) detected
   Pages (4): /entidades, /grafo, /ia-en-paraguay, /radar-legislativo
   Items (1):
    - H3 after H1
  </rule>
  <rule id="a11y/identical-links-same-purpose" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/a11y/identical-links-same-purpose">
   N link text(s) lead to different destinations
   Pages (5/19): /claims-verificados, /contacto, /directorio, /articulos/2026/05/28/magnifica-humanitas-enciclica-ia, /editorial/2026/06/16/malestar-ciudadano-la-salud-publica-como-espejo-de-editorial
   Items (5/8):
    - &quot;artículo&quot; → 10 different URLs
    - &quot;césar sánchez&quot; → 2 different URLs
    - &quot;leer análisis completo&quot; → 2 different URLs
    - &quot;leer más&quot; → 8 different URLs
    - &quot;leer análisis&quot; → 6 different URLs
  </rule>
  <rule id="a11y/table-duplicate-name" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/a11y/table-duplicate-name">
   3 table(s) without accessible names
   Pages (1): /como-trabajamos
   Items (1):
    - /como-trabajamos (3 table(s) without accessible names)
  </rule>
 </category>
 <category name="URL Structure" errors="0" warnings="26">
  <rule id="url/length" severity="info" status="warn" docs="https://docs.squirrelscan.com/rules/url/length">
   URL is N characters (over N)
   Pages (5/26): /editorial/2026/06/16/malestar-ciudadano-la-salud-publica-como-espejo-de-editorial, /editorial/2026/06/17/entre-secretos-y-pantallas-el-dilema-de-la-transparencia-en-editorial, /editorial/2026/06/18/el-colapso-simbolico-de-lo-publico-en-paraguay-editorial-18-editorial, /editorial/2026/06/19/justicia-memoria-y-el-espejo-roto-de-nuestra-sociedad-editor-editoria, /editorial/2026/06/20/celebracion-e-identidad-nacional-que-nos-dice-el-futbol-sobr-editoria
   Items (5/26):
    - /pulso-paraguay/2026/05/26/investigacion-contra-precandidato-cartista-de-luqu-pulso-paraguay (URL is 115 characters (over 100))
    - /pulso-paraguay/2026/05/29/santiago-pena-y-la-denuncia-de-enriquecimiento-ili-pulso-paraguay (URL is 115 characters (over 100))
    - /pulso-paraguay/2026/05/28/manifestacion-por-ingresos-a-la-policia-pulso-paraguay (URL is 104 characters (over 100))
    - /pulso-paraguay/2026/06/01/la-albirroja-y-su-lista-de-convocados-para-el-mund-pulso-paraguay (URL is 115 characters (over 100))
    - /pulso-paraguay/2026/06/09/perdida-de-investidura-de-kattya-gonzalez-pulso-paraguay (URL is 106 characters (over 100))
  </rule>
 </category>
 <category name="E-E-A-T" errors="0" warnings="2">
  <rule id="eeat/author-byline" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/eeat/author-byline">
   No content pages have author attribution
  </rule>
  <rule id="eeat/content-dates" severity="warning" status="warn" docs="https://docs.squirrelscan.com/rules/eeat/content-dates">
   No content pages have datePublished
  </rule>
 </category>
</issues>
</audit>