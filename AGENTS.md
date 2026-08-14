# muchotexto.net — workflow editorial

## Antes de publicar un artículo (OBLIGATORIO)

Todo artículo long-form en `_posts/` debe pasar por verificación de datos antes del commit.

### Paso 1: Escribir el borrador
Redactar el artículo normalmente. Las fuentes deben citarse al pie.

### Paso 2: Verificar datos
```
fact-check-article _posts/NOMBRE-DEL-ARTICULO.md
```
O equivalentemente: "Chequea los datos de este artículo con fuentes oficiales".

El agente de verificación hará lo siguiente automáticamente:
1. Leer el artículo párrafo por párrafo
2. Extraer todo claim factual: números, fechas, montos, nombres de empresas, leyes, porcentajes
3. Despachar agentes de búsqueda en paralelo para verificar cada categoría contra fuentes oficiales
4. Devolver un informe estructurado: TRUE / FALSE / PARTIALLY TRUE / UNVERIFIABLE
5. Señalar correcciones necesarias con fuentes

### Paso 3: Corregir y commitear
Aplicar las correcciones indicadas por el agente. Solo commitear cuando el informe esté limpio de FALSE.

### Regla de escape
Si un dato es inverificable pero viene de una fuente primaria citada en el artículo y esa fuente es confiable (ABC Color, ANDE, DNCP, IPS, MITIC, BACN, etc.), se puede mantener con la atribución explícita.

## Categorías de error más frecuentes (verificar con especial atención)

- **Números de leyes**: verificar número y año en BACN (www.bacn.gov.py)
- **Capacidades en MW y tipo de infraestructura**: HIVE tiene 300 MW Bitcoin ASIC (Tier-I), NO GPU. El proyecto GPU de 100 MW está en construcción
- **Empleo en data centers**: 20-50 personas por 100 MW, no 60-100
- **CAPEX hardware IT**: 60-70% del total, no 40-50%
- **Certificaciones Tier III**: existen en Paraguay (Itaipú, Tigo, Telefónica)
- **Fechas de hitos corporativos**: verificar con comunicados oficiales de la empresa, no con prensa
- **Cifras de empleo**: cruzar datos de IPS con claims de cámaras sectoriales

## Claims verificados (referencia para futuros artículos)

### Agrotoken y tokenización agrícola global
- **Agrotoken**: 230.000 toneladas tokenizadas (soja, maíz, trigo). Fuente: prensaeconomica.com.ar, bichosdecampo.com (2022-2025)
- **JSOY (Justoken)**: ~USD 141,75M en activos (no USD 100M). Fuente: rwa.xyz (jul 2026)
- **JSOY_OIL**: ~USD 425,15M en activos (no USD 481M). Fuente: rwa.xyz (jul 2026)
- **AgriDigital (Australia)**: 5,2M toneladas/año y USD 1.000M es dato histórico (~2019). Datos 2022: 25M toneladas, USD 6.000M+. No usar como cifra actual sin aclarar.
- **Farmway + Georgia**: USD 100M, 500 hectáreas de almendros. TRUE. Fuente: Cointelegraph (sep 2025)
- **Agrocoin**: pérdidas de USD 20M NO verificadas. Existe advertencia de FCA pero sin cifra de pérdidas confirmada.

### Seguridad en RWA / cripto
- **CertiK RWA exploits**: USD 17,9M (2023), USD 6M (2024), USD 14,6M (1S 2025). Fuente: CertiK 2025 Skynet RWA Security Report
- **Olympix**: 90% de smart contracts explotados habían sido auditados. TRUE. Fuente: blog.olympix.ai (múltiples artículos 2025-2026)
- **USDR**: perdió ~50% de su valor en horas (oct 2023). TRUE. Fuente: CoinDesk, The Block, Decrypt
- **UST/LUNA**: ~USD 40.000-45.000M destruidos en una semana. TRUE (la magnitud es correcta; el artículo dice "3 días", las fuentes dicen "una semana"). Fuente: Bloomberg, Wikipedia
- **Mt. Gox**: ~USD 473M perdidos (el artículo dice USD 450M, aproximación razonable). Fuente: Wikipedia, Bloomberg
- **Zoth**: USD 8,4M perdidos por clave de administrador comprometida (mar 2025). TRUE. Fuente: Zoth security report, Halborn, QuillAudits

### Paraguay: datos demográficos y económicos
- **Teléfono móvil**: 94% de personas tiene móvil — VERIFICAR. DataReportal 2026: 134% de penetración (conexiones, no personas). INE Paraguay 2025: 99,3% de hogares tiene acceso a algún TIC.
- **Internet**: 84% — PARTIALLY TRUE. DataReportal 2026: 83,1%. INE 2025: 85,4% (población 10+ años).
- **Pago con QR**: 64% de paraguayos. TRUE. Fuente: Pay Meeting 2025 / CPMP
- **MITIC trámites en línea**: "más de 400" — NO VERIFICADO directamente
- **Cooperativas**: 600 activas / 1,8M socios / 51% PEA — PARTIALLY TRUE. DGRV dice "800+ cooperativas, 1,8M socios, 51% PEA". INCOOP 2023: 649 cooperativas, 1,96M socios.
- **Exportación de soja**: 4.º exportador mundial (NO 6.º). 6.º productor mundial. Fuente: MercoPress 2024, UNDP, USDA 2026, WITS World Bank
- **Distritos sin presencia bancaria**: "30% de distritos >2.000 hab." — NO VERIFICADO
- **Cobertura internet**: 74% rural / 86% urbana. TRUE. Fuente: Internet Society Pulse 2024, INE 2024 (73,7% / 86,2%)

### Regulación financiera comparada
- **FCA sandbox UK**: "75% completaron pruebas, 90% obtuvieron autorización" — NO VERIFICADO

### HIVE Digital Technologies (datos verificados con fuentes oficiales)
Fuentes: HIVE FY2026 Earnings Release (jun 2026), HIVE Operations Paraguay page, HIVE homepage, Columbia University/NIPS announcement (jun 2026).

- **Capacidad operativa**: 300 MW en Paraguay a julio 2026, distribuidos en:
  - Yguazú Fase 1: completada junio 2025 (no abril)
  - Yguazú Fase 2: completada principios de septiembre 2025
  - Valenzuela Fase 3: completada 10 de noviembre de 2025
  - NOTA: Los 100 MW de Valenzuela SON la Fase 3 de los 300 MW operativos. No confundir con la expansión GPU de 100 MW (ver abajo).
- **Expansión GPU 100 MW** (NO es "Fase 3"): subestación en construcción en Yguazú. Energización: septiembre 2026. Data center Tier-III: ready-for-service en H2 2027.
- **Total plan Paraguay**: 400 MW (~74% de huella renovable global de ~540 MW).
- **Modelo de negocio**: DUAL (no "migración"). FY2026: minería Bitcoin $278.3M (93.5% revenue) + HPC/AI cloud $19.5M (6.5%).
- **BUZZ AI Cloud**: lanzado 18 de marzo de 2026 en Asunción, en data center Tier III de Tigo Paraguay.
- **Inversión**: adquirió sitio Yguazú (Bitfarms) por USD 56M en enero 2025. Revenue FY2026: $297.8M (+158% YoY).
- **Ubicación**: Yguazú (no "Colonia Iguazú").
- **Empleo**: sin cifra oficial verificable. Referencia de industria: 20-50 personas por 100 MW.

### Data centers e impacto local (datos verificados ago 2026)
Fuentes: HIVE FY2026 Earnings, HIVE Paraguay operations page, JLARC 2024, Bitfarms SEC filings.

- **HIVE timeline**: adquisición Yguazú enero 2025, construcción 300 MW completada jun-nov 2025. NO usar "noviembre 2024" como fecha de inicio.
- **HIVE sede**: operativa en San Antonio, Texas. Listada en TSX (Canadá) y Nasdaq. No es "empresa canadiense" en sentido operativo.
- **HIVE empleo construcción**: 800-1.500 trabajadores temporales durante 6 meses (estimación sectorial, sin cifra oficial).
- **Bitfarms salida de Paraguay**: vendió Yguazú enero 2025, completó salida enero 2026 con venta de Paso Pe (70 MW, hasta USD 30M). NO decir "abandonó el país en enero 2025".
- **Subestación Yguazú**: 200 MW (sobredimensionada al doble de Fase 1). Ubicada en Yguazú, NO en Valenzuela.
- **Infraestructura de data centers**: privada y dedicada. Sin evidencia de beneficio a red eléctrica residencial o conectividad local en Yguazú/Valenzuela.
- **Loudoun County, Virginia**: 200+ DCs. USD 733M en impuestos a la propiedad (JLARC 2024). 38% del Fondo General. NO usar "45% de ingresos" ni "USD 600M".
- **Irlanda**: 23% consumo eléctrico de DCs en 2025 (20% en 2023). Moratoria CRU 2021-2025. NO usar "EirGrid impuso moratoria" ni "hogares rurales" (son urbanos).
- **Paraguay regulación DC**: sin regulación específica. Ley 294/1993 de EIA aplica genéricamente, nunca aplicada al sector. Sin cuotas de contratación local ni obligaciones de beneficio comunitario.
- **Consumo intensivo ANDE (ago 2026)**: 41 empresas registradas, 943,8 MW de demanda conjunta (~13,5% de la energía de Itaipú que corresponde a Paraguay). ANDE proyecta ingresos de ~USD 350M en 2026 (+18,6% interanual). Fuente: ABC Color Negocios, 3-ago-2026.

### Energía, clima y deforestación (datos verificados ago 2026)
Fuentes: Wikipedia (Electricity sector in Paraguay), Banco Mundial CCKP, Global Forest Watch, Itaipú Binacional, ANDE, ABC Color.

- **Matriz eléctrica**: 99,998% renovable en 2024. Composición: Itaipú 86%, Yacyretá 11%, Acaray 3%. Térmica: 0,002%.
- **Capacidad instalada**: ~8.760 MW disponibles para Paraguay. Itaipú 7.000 MW (80%), Yacyretá ~1.550 MW (18%), Acaray 210 MW (2%). NO usar cifras de Wikipedia en inglés para Yacyretá — la mitad paraguaya real es ~1.550-1.600 MW (fuente: ANDE/ABC Color 2025-2026), no 900 MW.
- **Concentración**: Itaipú + Yacyretá = 97% de la capacidad hidroeléctrica en una sola cuenca (Paraná).
- **Sequía 2019-2022**: Paraná en mínimo histórico de 77 años. Generación Itaipú cayó 35,6%: 103,1 TWh (2016) → 66,4 TWh (2021).
- **Embalse Itaipú**: capacidad de ~1 mes de caudal promedio. Esencialmente represa de pasada.
- **Deforestación 2000-2020**: 6,3M ha perdidas (25,8% de cobertura). Concentrada en Chaco (Boquerón, Alto Paraguay).
- **Emisiones electricidad**: ~0,01 MtCO2e/año. LULUCF (deforestación): 28-52 MtCO2e/año. Total país: 75-98 MtCO2e/año. Paraguay es EMISOR NETO.
- **Paraguay no tiene**: parques solares utility-scale, parques eólicos, biomasa eléctrica significativa. Cero diversificación renovable no hidro.
- **Ley 7599**: promulgada en diciembre de 2025 (NO 2024). Abre sector eléctrico a inversión privada. Decreto 6034 de mayo 2026: habilita 6 fuentes renovables (solar, eólica, biomasa, biogás, geotermia, almacenamiento) + autogenerador, cogenerador, exportador, prosumidor.
- **NDC 3.0**: presentada noviembre 2025. Meta: 20% reducción bajo BAU para 2030/2035 (10% incondicional + 10% condicional, USD 24.000M financiamiento externo).
- **Demanda eléctrica**: crecimiento 12-21% anual (ANDE, datos recientes). NO usar 5-8% (dato desactualizado).

### Fuentes primarias paraguayas — verificación obligatoria
### Demografía y economía (datos verificados ago 2026)
Fuentes: INE Paraguay, Banco Mundial, BCP, ABC Color.

- **Población**: ~6,5M (2026), proyección ~7,2-7,5M (2040). Edad media: 29,4 años.
- **Fecundidad**: 1,7-1,8 hijos por mujer (INE 2026). Por debajo del nivel de reemplazo (2,1). NO usar 1,9 (dato desactualizado).
- **Bono demográfico**: activo hasta ~2045. Ventana se cierra con envejecimiento poblacional.
- **Urbanización**: 69% (Censo 2022), proyectado ~78-80% (2040).
- **PIB per cápita**: ~USD 9.400 nominal (2026). Proyección 2040: USD 14.000-17.000. NO usar USD 5.900 (dato 2022-2023).
- **HCI (Capital Humano)**: 0,528 (Banco Mundial 2020). El más bajo entre pares regionales (Uruguay ~0,60, Chile ~0,65, Costa Rica ~0,63).
- **Informalidad laboral**: 60-64% según trimestre y medición (INE 2025-2026). NO usar una cifra fija sin especificar fuente y período.
- **Exportaciones**: soja y carne siguen dominando, servicios digitales en crecimiento bajo maquila.

### Itaipú — Anexo C y negociaciones (datos verificados ago 2026)
Fuentes: ABC Color, El Nacional, ANDE.

- **Suspensión**: 1 de abril de 2025 por escándalo de espionaje ABIN (Brasil espió a funcionarios paraguayos).
- **Reanudación**: noviembre 2025, tras entrega del informe confidencial brasileño. Confirmado por Félix Sosa (ANDE).
- **Estado actual (ago 2026)**: conversaciones reanudadas pero sin nuevo Anexo C firmado. Acuerdo tarifario 2024-2026 (USD 19,28/kW-mes) vence 1 de enero de 2027.
- **NO decir** "congelada desde abril 2025" ni "Anexo C vence en 2027". Lo congelado fue hasta noviembre 2025; lo que vence es el acuerdo tarifario, no el Anexo.

### Fibra óptica y conectividad (datos verificados ago 2026)
Fuentes: MITIC, BID, DPL News.

- **Red Nacional de Fibra Óptica**: financiada con préstamo BID de USD 130M (2019). Etapa 1 completada (~2020-2021): unificación de redes de Copaco, ANDE, Interior, Hacienda, MITIC. Etapa 2 en ejecución.
- **NO decir** "no está construido" ni usar USD 47,9M como presupuesto (esa cifra corresponde a otro componente).
- **Cables submarinos**: Paraguay no tiene acceso directo. Depende de fibra terrestre a través de Brasil y Argentina. Sin proyecto confirmado de conexión internacional propia.

Para cualquier dato sobre Paraguay, el fact-checker DEBE consultar:
- Wikipedia en español (no solo en inglés): https://es.wikipedia.org/
- ANDE (portal y noticias): https://www.ande.gov.py/
- BACN (leyes): https://www.bacn.gov.py/
- MADES (clima/ambiente): http://www.mades.gov.py/
- ABC Color (secciones Tecnología, Economía, Nacionales): https://www.abc.com.py/
- La Nación: https://www.lanacion.com.py/
- Itaipú Binacional: https://www.itaipu.gov.py/

### Claims verificados — Paraguay 2040 (ago 2026)

Fuentes: AGENTS.md (claims pre-verificados), ABC Color, ANDE, BCP, BACN, Banco Mundial.

#### Datos demográficos y económicos
- **Población 6,5M, edad media 29,4 años**: TRUE. Fuente: INE Paraguay, verificado en AGENTS.md.
- **Proyección 7,2-7,5M en 2040**: TRUE. Fuente: INE, verificado en AGENTS.md.
- **Fecundidad 1,7-1,8**: TRUE. Fuente: INE 2026, verificado en AGENTS.md.
- **Urbanización 69% → ~80% en 2040**: TRUE. Fuente: Censo 2022, verificado en AGENTS.md.
- **Bono demográfico hasta ~2045**: TRUE. Fuente: INE, verificado en AGENTS.md.
- **HCI Paraguay 0,528**: TRUE. Fuente: Banco Mundial 2020, verificado en AGENTS.md.
- **HCI Uruguay 0,603, Chile 0,652, Costa Rica 0,623**: PARTIALLY TRUE. Las cifras exactas del Banco Mundial 2020 son: Uruguay 0,60 (no 0,603), Chile 0,65 (no 0,652), Costa Rica 0,63 (no 0,623). El artículo usa cifras con 3 decimales que son estimaciones o de otra fuente/edición. Recomendación: usar "aproximadamente 0,60" o citar la fuente exacta.
- **PIB per cápita USD 9.400 (2026)**: TRUE. Fuente: BCP, verificado en AGENTS.md.
- **Proyección PIB per cápita 2040: USD 14.000-17.000**: TRUE. Fuente: verificado en AGENTS.md.
- **PIB per cápita proyectado Uruguay USD 30.000, Chile USD 28.000, Costa Rica USD 22.000**: UNVERIFIABLE con precisión. Son proyecciones a 15 años de fuentes diversas (FMI, bancos centrales, consultoras). El orden de magnitud es razonable pero no hay una fuente única que consolide estas tres cifras para 2040. Recomendación: atribuir a "proyecciones del FMI y bancos centrales" o citar fuente específica.
- **Soja y carne >40% de exportaciones totales**: PARTIALLY TRUE. Datos del BCP 2025: soja ~28%, carne ~12%, total ~40%. La cifra es correcta pero depende del año y los precios internacionales. En 2024 fue ligeramente superior al 40%, en 2023 fue inferior. Recomendación: usar "alrededor del 40%" o citar año.
- **Informalidad 60-64%**: TRUE. Fuente: INE 2025-2026, verificado en AGENTS.md.
- **Exportaciones de servicios bajo maquila crecieron sostenidamente**: UNVERIFIABLE sin serie temporal concreta. Afirmación cualitativa razonable pero sin cifra específica.

#### Energía
- **~44 TWh/año generación, ~15 TWh consumo**: PARTIALLY TRUE. La generación total de Paraguay es mayor: Itaipú solo genera ~67 TWh (mitad paraguaya ~33,5 TWh) + Yacyretá ~11 TWh + Acaray ~1 TWh = ~45,5 TWh disponibles para Paraguay. El consumo interno es ~15-16 TWh. Las cifras del artículo son aproximaciones razonables. Fuente: ANDE, Wikipedia ES, AGENTS.md.
- **Crecimiento demanda 12-21% anual**: TRUE. Fuente: ANDE, verificado en AGENTS.md. NO usar 5-8% (dato desactualizado).
- **944 MW (41 empresas) = 13,5% de Itaipú**: PARTIALLY TRUE. AGENTS.md registra 943,8 MW (no 944). El redondeo es menor, aceptable para periodismo.
- **Superávit se agota 2035-2040**: PROYECCIÓN (no verificable como hecho). Es el resultado del modelo del propio artículo, no una proyección oficial.
- **Irradiación solar Chaco 5,5 kWh/m²/día**: TRUE. Fuentes múltiples (NASA POWER, GHI maps, IRENA) confirman que el Chaco paraguayo recibe 5,0-5,8 kWh/m²/día de irradiación global horizontal. 5,5 es el punto medio razonable.
- **Ley 7599 (dic 2025) y Decreto 6034 (may 2026)**: TRUE. Fuente: BACN, verificado en AGENTS.md.
- **Potencial solar Chaco 1.000-5.000 MW**: PROYECCIÓN (no verificable). Estimación razonable basada en recurso solar disponible, pero no hay estudio oficial que la respalde.
- **99,9% renovable**: PARTIALLY TRUE. AGENTS.md registra 99,998% renovable en 2024. El artículo dice 99,9% — diferencia menor, aceptable.
- **Energía más barata de Sudamérica**: PARTIALLY TRUE. Paraguay tiene tarifas industriales entre las más bajas (USD 0,03-0,05/kWh), pero afirmar "la más barata" sin comparación exhaustiva con todos los países es impreciso. Competidores cercanos: Argentina (subsidiada), Bolivia.

#### Data centers y conectividad
- **0 MW en 2022 → 944 MW en 2026**: TRUE. Verificado en AGENTS.md.
- **HIVE: 300 MW operativos + 100 MW GPU en construcción**: TRUE. Fuente: HIVE FY2026 Earnings, verificado en AGENTS.md.
- **Yguazú Digital: 3 fases, 10 MW a 1.000 MW**: UNVERIFIABLE en detalle. El artículo de muchotexto.net sobre Yguazú Digital menciona estas fases. No se encontró fuente oficial primaria que confirme los 1.000 MW finales con ese desglose exacto. La prensa paraguaya (ABC Color, La Nación) maneja cifras variables.
- **BID USD 130M para fibra óptica**: TRUE. Fuente: MITIC, BID, verificado en AGENTS.md.
- **20-50 empleos por 100 MW en data centers**: TRUE. Fuente: verificado en AGENTS.md (referencia de industria).
- **Irlanda: ~80 data centers**: UNVERIFIABLE. La cifra exacta varía según fuente: desde 70 hasta 82 según qué se cuenta como "data center". AGENTS.md solo verifica el 23% de consumo. Recomendación: usar "más de 70" o citar fuente (Host in Ireland, CSO Ireland).
- **Loudoun County: 200+ DCs**: TRUE. Fuente: JLARC 2024, verificado en AGENTS.md.

#### Regulación y leyes
- **Anexo C: suspendido abr 2025, reanudado nov 2025**: TRUE. Verificado en AGENTS.md.
- **Acuerdo tarifario vence 1 ene 2027**: TRUE. Verificado en AGENTS.md.
- **Ley 7547/2025 reforma Ley de Maquila**: UNVERIFIABLE. BACN devuelve una ley no relacionada (Ley 1229 de 1998) para la URL de la Ley 7547. No se pudo confirmar con fuente primaria. La existencia de reformas a la Ley de Maquila es mencionada en prensa pero el número exacto 7547 requiere verificación.
- **Paraguay sin regulación específica para data centers**: TRUE. Verificado en AGENTS.md ("sin regulación específica. Ley 294/1993 de EIA aplica genéricamente, nunca aplicada al sector").

### Mesa Energética Nacional y gobernanza institucional (verificado ago 2026)

Fuentes: Presidencia.gov.py, MOPC, ABC Color, Última Hora, RDN, RCC, MIC.gov.py, Itaipú.gov.py.

- **Mesa Energética Nacional**: creada por decreto presidencial en 2012 como organismo asesor del Presidente. Fuente: Última Hora (6-ago-2026), Itaipú.gov.py.
- **Reactivación 2023**: el gobierno de Santiago Peña la reactivó en octubre de 2023 con el mandato de actualizar la política energética. Fuente: RDN (9-oct-2023), MOPC Twitter.
- **Política Energética Nacional al 2050**: aprobada por Decreto N.º 2553/24 el 19-20 de septiembre de 2024. Deroga el decreto 6.092/2016. Define 95 objetivos y 385 metas (dato del propio documento, verificado por el fact-checker con fuente del MOPC). Fuente: MOPC (20-sep-2024), Presidencia.gov.py (16 y 29-sep-2024).
  - NOTA: El documento dice "95 objetivos y 385 metas" pero el acceso al PDF completo no está disponible online. Atribuir a "según el MOPC" hasta verificación directa.
- **Meta institucional**: la PEN 2050 incluye la creación y puesta en funcionamiento de un Ministerio de Energía, Hidrocarburos y Minería. Plazo original: 2024. A agosto 2026 no se ha creado (solo existen proyectos de ley). Solo existe el Viceministerio de Minas y Energía (VMME) como dependencia del MOPC. Fuente: MOPC.gov.py.
- **Reconvocatoria 6 agosto 2026**: Peña convocó la Mesa Energética Nacional y dio 30 días para presentar propuestas en 4 ejes: institucionalidad, grandes proyectos de generación, mesa eléctrica público-privada y reglas para inversores. Fuente: ABC Color (8-ago-2026).
- **Proyectos de ley presentados 13 agosto 2026**: el Ejecutivo presentó DOS proyectos de ley —creación del Ministerio de Minas y Energía y creación de un ente regulador del sector eléctrico— en la primera reunión de la Mesa Nacional del Sector Eléctrico presidida por Peña (reunión interinstitucional, reunión "subeléctrica", duró ~2,5 horas). Textos puestos a disposición pública en la web para análisis. Vocero: Guillermo Grance. IMPORTANTE: son proyectos de ley en debate, NO instituciones creadas. Fuente: La Nación (13-ago-2026).
- **Mesa Energética del MIC+UIP**: dentro del Consejo Asesor Empresarial del MIC, concluyó el 22 de julio de 2026 que "por primera vez en la historia tenemos más proyectos que energía disponible" (Ministro Marco Riquelme). Fuente: RCC (22-jul-2026), MIC.gov.py.
- **Consumo eléctrico**: ~15-16 TWh de consumo interno (NO 29 TWh). La cifra de 29.419 GWh citada en algunos análisis sectoriales no corresponde al consumo interno sino a generación total o disponible (consumo + exportación + pérdidas). Fuentes: Wikipedia "Energy in Paraguay" (2019: 13.229 GWh), ANDE/AGENTS.md (2025: ~15-16 TWh). NO usar 29 TWh como consumo interno.
  - Crecimiento histórico del consumo: ~3-5% CAGR (2019-2025).
  - Crecimiento reciente de demanda (era data centers): 12-21% anual. Ambos datos son correctos en sus respectivos contextos.
- **6.300 MW**: es la potencia disponible de Itaipú para Paraguay (10 turbinas x 700 MW con 10% de margen), NO exclusivamente la demanda de empresas interesadas. La prensa reporta este número como "demanda de empresas" pero casualmente coincide con la capacidad paraguaya de Itaipú. Fuente: Wikipedia ES ANDE, ABC Color.

### Tarifas ANDE — Consumo Intensivo Especial (verificado ago 2026)

Fuentes: Resolución ANDE 49238/2024, Pliego de Tarifas Nº 21, ABC Color, decretos presidenciales (5306, 5307, 5860, 5861).

- **Tarifa Grupo Consumo Intensivo Especial: 30 US$/MWh**: TRUE. Resolución 49238/2024, vigente hasta dic 2027.
- **Decretos de extensión a 15 años (5306, 5307, 5860, 5861, ene-abr 2026)**: TRUE. Extendían la tarifa de 30 a industrias convergentes y data centers.
- **Decretos derogados el 9 de junio de 2026**: TRUE. Presión sindical y técnica interna de ANDE.
- **Renuncia de Félix Sosa (presidente ANDE) el 27 de julio de 2026**: TRUE. Se negó a aplicar los decretos.
- **Nuevo titular Miguel Báez instruido a definir tarifa técnica única**: TRUE. Informe entregado 31 de julio, contenido no público.
- **Demanda de empresas interesadas: 6.300 MW**: Cifra reportada por prensa (ABC Color). Equivale a toda la potencia de Itaipú disponible para PY. VERIFICAR con fuente oficial cuando esté disponible.

**Recordatorio de mantenimiento:** re-verificar la tarifa de ANDE cada 30 días. Próxima verificación: 7 de septiembre de 2026. Si cambia, actualizar `_includes/calculadora-energetica.html` y `calculadora-energetica.markdown` en menos de 48h.

### Tarifas eléctricas internacionales para data centers (verificado ago 2026)

Fuentes: Eurostat (nrg_pc_205, abril 2026), fuentes de mercado (CBRE, JLL, DCP reports), AGENTS.md.

- **Irlanda (Dublín) 150–190 USD/MWh (rango PPA data center)**: TRUE. Rango de mercado para PPAs de gran escala. Eurostat confirma €255/MWh (~276 USD/MWh) para consumidores no-domésticos medianos (500–2.000 MWh/año) en S2 2025 — los data centers negocian por debajo de ese techo. Fuentes: Eurostat + fuente de mercado independiente.
- **Suecia (Luleå) 45–65 USD/MWh**: TRUE. Dos fuentes de mercado independientes coinciden.
- **Chile 85–100 USD/MWh**: TRUE. Una fuente de mercado.
- **Virginia, EE.UU. 95–130 USD/MWh**: TRUE. Una fuente de mercado (Dominion Energy, PJM).
- **Paraguay 30–45 USD/MWh**: Rango con fuente primaria verificada (ANDE, Res. 49238/2024) pero en revisión activa. Ver sección Tarifas ANDE arriba.

#### Graduados STEM
- **Menos de 600 graduados en informática por año**: PARTIALLY TRUE. El artículo del propio observatorio ("Educación tech en Paraguay") menciona 400-600 graduados. Fuentes externas (CONACYT, ANEAES) no publican una cifra consolidada actualizada. La estimación es razonable pero no verificable con fuente oficial primaria. Recomendación: citar la fuente del observatorio y aclarar que es estimación.
