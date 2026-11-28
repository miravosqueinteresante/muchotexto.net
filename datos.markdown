---
layout: page
title: "Datos verificados"
permalink: /datos/
description: "Capa de datos verificados de muchotexto.net: 224 indicadores de ANDE, Itaipu y Yacyreta con trazabilidad completa."
resumen: "224 indicadores de ANDE, Itaipu y Yacyreta con fuente, URL y fecha de extraccion."
last_modified_at: 2026-11-28
---

Este observatorio mantiene una capa de datos verificados con **224 indicadores** de tres entidades energéticas paraguayas: ANDE, Itaipú Binacional y Yacyretá. Cada indicador incluye fuente, URL de proveniencia, método de extracción y estado de verificación.

Los datos se sincronizan automáticamente desde el repositorio hermano [datos-publicos](https://github.com/miravosqueinteresante/datos-publicos) en cada build.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Datos verificados de energia en Paraguay",
  "description": "224 indicadores de ANDE, Itaipu y Yacyreta con trazabilidad completa: fuente, URL, fecha de extraccion y estado de verificacion.",
  "url": "https://muchotexto.net/datos/",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "creator": {
    "@type": "Organization",
    "@id": "https://muchotexto.net/#org",
    "name": "MuchoTexto"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://muchotexto.net/#org",
    "name": "MuchoTexto"
  },
  "inLanguage": "es-PY",
  "keywords": ["energia", "Paraguay", "ANDE", "Itaipu", "Yacyreta", "consumo electrico", "generacion", "tarifas"],
  "temporalCoverage": "2023/2026",
  "spatialCoverage": {
    "@type": "Place",
    "name": "Paraguay"
  },
  "distribution": [
    {
      "@type": "DataDownload",
      "encodingFormat": "application/json",
      "contentUrl": "https://muchotexto.net/_data/datos_publicos.json"
    }
  ],
  "variableMeasured": [
    "Consumo total (GWh)",
    "Generacion (GWh)",
    "Perdidas de distribucion (%)",
    "Clientes (cantidad)",
    "Tarifa (USD/MWh)",
    "Potencia reservada (MW)"
  ]
}
</script>
