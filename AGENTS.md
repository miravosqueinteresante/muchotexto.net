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
2. Extraer todo claim en DOS capas:
   - **Claims factuales**: números, fechas, montos, nombres de empresas, leyes, porcentajes
   - **Claims interpretativos/atributivos**: toda oración donde una fuente es el sujeto de un verbo de afirmación (sostiene, concluye, propone, usa, cita, refiere, documenta, descarta). Para estos, abrir el texto COMPLETO de la fuente y comparar la conclusión atribuida con la conclusión real de la fuente.
3. Despachar agentes de búsqueda en paralelo para verificar cada categoría contra fuentes oficiales
4. Devolver un informe estructurado: TRUE / FALSE / PARTIALLY TRUE / UNVERIFIABLE
5. Señalar correcciones necesarias con fuentes

**Checklist de atribución (sujeto-verbo), obligatorio en el informe:**
- Toda oración "X concluye/afirma/usa/cita Y" debe verificar que X existe, que el verbo es correcto y que Y está realmente en la fuente de X.
- Un claim interpretativo NO se aprueba con TRUE solo porque la fuente existe y el título coincide: hay que leer el abstract/texto completo y comprobar que la conclusión atribuida es la que la fuente realmente tiene. (Error histórico: se aprobó un claim invirtiendo la conclusión del BID porque solo se verificó la existencia del estudio, no su contenido.)
- Si el claim es una comparación del AUTOR (no atribuida a la fuente), se acepta solo si el texto la presenta como propia del autor, no de la fuente.

**Regla de fuentes primarias locales:** pasar al fact-checker las rutas de las fuentes primarias ya descargadas (ej. `C:\Users\pc\AppData\Local\Temp\opencode\energia_site\*.txt`) con instrucción de leerlas completas antes de emitir veredicto sobre cualquier claim que las involucre. Un claim no se marca UNVERIFIABLE solo porque el agente no encontró la fuente en la web si esa fuente está disponible localmente.

### Paso 3: Corregir y commitear
1. Aplicar las correcciones indicadas por el agente.
2. **Grep global del dato corregido**: tras corregir un número, fecha, nombre o frase errónea, buscarlo en TODO el artículo (`grep`) para cazarlo en todas sus apariciones. No corregir solo la primera ocurrencia y dejar residuos.
3. **Spot-check del orquestador**: al recibir un informe limpio de FALSE, abrir 1-2 fuentes de alto riesgo (las que sostienen claims interpretativos) y verificar personalmente su contenido. No confiar ciegamente en el veredicto del subagente.
4. Solo commitear cuando el informe esté limpio de FALSE y el spot-check no detectó nada.

### Regla de escape
Si un dato es inverificable pero viene de una fuente primaria citada en el artículo y esa fuente es confiable (ABC Color, ANDE, DNCP, IPS, MITIC, BACN, etc.), se puede mantener con la atribución explícita.

## Política editorial de IA (alineada con como-trabajamos.markdown)

- La IA es asistente, nunca autor final. Toda publicación requiere supervisión editorial humana.
- **Artículos long-form**: si la IA intervino de forma significativa en investigación o redacción, el artículo lleva al pie la fórmula: "Artículo elaborado con la asistencia de inteligencia artificial y supervisado por el editor humano de muchotexto.net." Si el uso incidió en contenido factual, indicar qué parte del proceso fue asistido.
- Pulso y Editorial ya se marcan como generados por IA con el modelo nombrado.
- **Prohibido**: ingresar información confidencial, datos personales de fuentes o borradores de contenidos inéditos en herramientas de IA comerciales. Solo herramientas autorizadas (listadas en como-trabajamos.markdown).
- **Política de revisión**: revisar esta política cada 90 días o al incorporar un modelo/herramienta nueva.

**Recordatorio de mantenimiento:** próxima revisión de la política de IA: 13 de noviembre de 2026.

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
- **Consumo intensivo ANDE (ago 2026)**: 41 empresas registradas, 943,8 MW de potencia reservada contratada (~13,5% de la potencia de Itaipú que corresponde a Paraguay, 7.000 MW — NO de la energía anual). ANDE proyecta ingresos de ~USD 350M en 2026 (+18,6% interanual). Fuente: ABC Color Negocios, 3-ago-2026.

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
- **Ley 7599**: promulgada en diciembre de 2025 (NO 2024). Abre sector eléctrico a inversión privada. Decreto 6034 de mayo 2026: habilita 6 fuentes renovables (solar, eólica, biomasa, biogás, geotermia, almacenamiento) + las figuras de autogenerador, cogenerador, generador, exportador y gran consumidor. NO usar "prosumidor": el término no aparece en la ley ni en el decreto (verificado contra textos oficiales en energia.paraguay.gov.py).
- **NDC 3.0**: presentada noviembre 2025. Meta: 20% reducción bajo BAU para 2030/2035 (10% incondicional + 10% condicional, USD 24.000M financiamiento externo).
- **Demanda eléctrica**: crecimiento 12,5-21% anual (ANDE: +5,7% 2022, +12,4% 2023, +18,5% 2024, +12,5% 2025, +21% 2026). El mínimo oficial es 12,5%, no 12%. NO usar 5-8% como ritmo actual.

### Fuentes primarias paraguayas — verificación obligatoria
### Demografía y economía (datos verificados ago 2026)
Fuentes: INE Paraguay, Banco Mundial, BCP, ABC Color.

- **Población**: 6.460.159 (2026, INE Revisión 2025), proyección ~6,9M (2040, INE Revisión 2024), 7,1M recién en 2050. NO usar 7,2-7,5M para 2040. Edad media: 29,4 años.
- **Fecundidad**: 1,90 hijos por mujer (2026) → 1,72 (2050), INE Revisión 2024. Por debajo del nivel de reemplazo (2,1). NO usar 1,7-1,8 (dato desactualizado).
- **Bono demográfico**: sin fecha oficial consolidada. INE sitúa el cierre ~2070; UIP estima 2030-2040. Presentar como estimación divergente, nunca como fecha fija.
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
- **Proyección ~6,9M en 2040**: TRUE (INE Revisión 2024/2025). NO usar 7,2-7,5M: 7,1M recién en 2050.
- **Fecundidad 1,90 (2026) → 1,72 (2050)**: TRUE. Fuente: INE Revisión 2024. El rango 1,7-1,8 estaba desactualizado.
- **Urbanización 69% → ~80% en 2040**: TRUE. Fuente: Censo 2022, verificado en AGENTS.md.
- **Bono demográfico "2045"**: PARTIALLY TRUE. No es fecha oficial: INE habla de ~2070, UIP de 2030-2040. Presentar como estimación divergente citando ambas fuentes.
- **HCI Paraguay 0,528**: TRUE. Fuente: Banco Mundial 2020, verificado en AGENTS.md.
- **HCI Uruguay 0,603, Chile 0,652, Costa Rica 0,623**: PARTIALLY TRUE. Las cifras exactas del Banco Mundial 2020 son: Uruguay 0,60 (no 0,603), Chile 0,65 (no 0,652), Costa Rica 0,63 (no 0,623). El artículo usa cifras con 3 decimales que son estimaciones o de otra fuente/edición. Recomendación: usar "aproximadamente 0,60" o citar la fuente exacta.
- **PIB per cápita USD 9.400 (2026)**: TRUE. Fuente: BCP, verificado en AGENTS.md.
- **Proyección PIB per cápita 2040: USD 14.000-17.000**: TRUE. Fuente: verificado en AGENTS.md.
- **PIB per cápita proyectado Uruguay USD 30.000, Chile USD 28.000, Costa Rica USD 22.000**: UNVERIFIABLE con precisión. Son proyecciones a 15 años de fuentes diversas (FMI, bancos centrales, consultoras). El orden de magnitud es razonable pero no hay una fuente única que consolide estas tres cifras para 2040. Recomendación: atribuir a "proyecciones del FMI y bancos centrales" o citar fuente específica.
- **Soja y carne >40% de exportaciones totales**: PARTIALLY TRUE. Datos del BCP 2025: soja ~28%, carne ~12%, total ~40%. La cifra es correcta pero depende del año y los precios internacionales. En 2024 fue ligeramente superior al 40%, en 2023 fue inferior. Recomendación: usar "alrededor del 40%" o citar año.
- **Informalidad 60-64%**: TRUE. Fuente: INE 2025-2026, verificado en AGENTS.md.
- **Exportaciones de servicios bajo maquila crecieron sostenidamente**: UNVERIFIABLE sin serie temporal concreta. Afirmación cualitativa razonable pero sin cifra específica.

#### Energía
- **~44 TWh/año generación, ~29,4 TWh consumo**: TRUE. ANDE (14-01-2026): consumo nacional 2025 = 29.419 GWh (29,4 TWh), repartido Itaipú 25.768 GWh + Yacyretá 3.081 + Acaray 570. Generación disponible ~45,5 TWh. Excedente exportado ≈35% (~15 TWh). NO usar ~15-16 TWh como consumo.
- **Crecimiento demanda 12,5-21% anual**: TRUE. Fuente: ANDE (oficiales: 12,5% 2025, 18,5% 2024, 21% 2026). NO usar 12% como mínimo ni 5-8% (desactualizado).
- **943,8 MW (41 empresas) = 13,5% de Itaipú**: TRUE. Es 13,5% de la POTENCIA que corresponde a Paraguay de Itaipú (7.000 MW), NO de la energía anual. Potencia reservada contratada, no necesariamente operativa.
- **Superávit se agota 2035-2040**: PROYECCIÓN (no verificable como hecho). Es el resultado del modelo del propio artículo, no una proyección oficial.
- **Irradiación solar Chaco ~4,8-4,9 kWh/m²/día**: TRUE. Atlas Solar 2016 y estudio académico del Chaco (La Patria, datos NASA 1983-2005): promedio anual GHI 4,7-5,1 kWh/m²/día. En el norte del Chaco más cerca de 5,0-5,1. NO usar 5,5.
- **Ley 7599 (dic 2025) y Decreto 6034 (may 2026)**: TRUE. Fuente: BACN, verificado en AGENTS.md.
- **Potencial solar Chaco 1.000-5.000 MW**: PROYECCIÓN (no verificable). Estimación razonable basada en recurso solar disponible, pero no hay estudio oficial que la respalde.
- **99,9% renovable**: PARTIALLY TRUE. AGENTS.md registra 99,998% renovable en 2024. El artículo dice 99,9% — diferencia menor, aceptable.
- **Energía más barata de Sudamérica**: PARTIALLY TRUE. Paraguay tiene tarifas industriales entre las más bajas (USD 0,03-0,05/kWh), pero afirmar "la más barata" sin comparación exhaustiva con todos los países es impreciso. Competidores cercanos: Argentina (subsidiada), Bolivia.

#### Data centers y conectividad
- **Serie GCIE**: creado 2022 (Res. ANDE 46984). Potencia reservada: ~125 MW (2023) → ~822 MW (2025) → 943,8 MW (2026). NO decir "0 a 944 MW en tres años" ni "en 2022 no había data centers".
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
- **Proyectos de ley presentados 13 agosto 2026**: el Ejecutivo presentó DOS proyectos de ley en la primera reunión de la Mesa Nacional del Sector Eléctrico presidida por Peña (reunión interinstitucional, reunión "subeléctrica", duró ~2,5 horas). Textos puestos a disposición pública en la web para análisis. Vocero: Guillermo Grance. IMPORTANTE: son proyectos de ley en debate, NO instituciones creadas. Fuente: La Nación (13-ago-2026).
  - NOMBRE OFICIAL (verificado en el texto publicado en energia.paraguay.gov.py, "PRELIMINAR VMME"): "Ministerio de Energía, Minería e Hidrocarburos". La prensa (La Nación) lo llama "Ministerio de Minas y Energía". Recomendación: usar el nombre oficial del proyecto o aclarar la equivalencia.
- **Mesa Energética del MIC+UIP**: dentro del Consejo Asesor Empresarial del MIC, concluyó el 22 de julio de 2026 que "por primera vez en la historia tenemos más proyectos que energía disponible" (Ministro Marco Riquelme). Fuente: RCC (22-jul-2026), MIC.gov.py.
- **Consumo eléctrico**: 29.419 GWh en 2025 (29,4 TWh) según ANDE (14-01-2026): es el CONSUMO NACIONAL (demanda del sistema con pérdidas). El historial ANDE: 18.583 GWh (2021), 19.635 (2022), 22.079 (2023), 26.154 (2024), 29.419 (2025). NO usar ~15-16 TWh como consumo actual (era la cifra ~2019-2020). Excedente exportado ≈35% (~15 TWh).
  - Crecimiento histórico del consumo: ~3-5% CAGR (2019-2025).
  - Crecimiento reciente de demanda (era data centers): 12,5-21% anual. El piso oficial reciente es 12,5% (2025); usar "12-21%" es impreciso.
- **6.300 MW**: es la potencia disponible de Itaipú para Paraguay (10 turbinas x 700 MW con 10% de margen), NO exclusivamente la demanda de empresas interesadas. La prensa reporta este número como "demanda de empresas" pero casualmente coincide con la capacidad paraguaya de Itaipú. Fuente: Wikipedia ES ANDE, ABC Color.

### Tarifas ANDE — Consumo Intensivo Especial (verificado ago 2026)

Fuentes: Resolución ANDE 49238/2024, Pliego de Tarifas Nº 21, ABC Color, decretos presidenciales (5306, 5307, 5860, 5861).

- **Tarifa Grupo Consumo Intensivo Especial: 30 US$/MWh**: TRUE. Resolución 49238/2024, vigente hasta dic 2027.
- **Decretos de extensión a 15 años (5306, 5307, 5860, 5861, ene-abr 2026)**: TRUE. Extendían la tarifa de 30 a industrias convergentes y data centers.
- **Decretos derogados el 9 de junio de 2026**: TRUE. Presión sindical y técnica interna de ANDE.
- **Renuncia de Félix Sosa (presidente ANDE) el 27 de julio de 2026**: TRUE. Se negó a aplicar los decretos.
- **Nuevo titular Miguel Báez instruido a definir tarifa técnica única**: TRUE. Informe entregado 31 de julio, contenido no público.
- **Demanda de empresas interesadas: 6.300 MW**: Cifra reportada por prensa (ABC Color). Equivale a toda la potencia de Itaipú disponible para PY. VERIFICAR con fuente oficial cuando esté disponible.

### Tarifas y finanzas ANDE — estudio Ceare 2026-2030 (verificado 15-ago-2026)

Fuentes: ABC Color / Silvana Bogarín (9-ago-2026), estudio Ceare (UBA, con apoyo del BID, marco ICP/FMI-SRS), CIER 2025.

- **Costo medio de generación ANDE: serie US$24/MWh (2023) → US$26,39 (2025) → ~US$28 tras incrementos de binacionales**: TRUE. Itaipú pasó de 16,75 a 19,28 US$/kW-mes; Yacyretá de 22,60 a 28 US$. NO citar un solo número sin aclarar período.
- **Tarifa media ANDE 2024: US$49,49/MWh**: TRUE. NO confundir con tarifa GCIE (30) ni tarifa técnica (~44).
- **Proyección Ceare 2026-2030**: tarifa media 49,2→68,6 US$/MWh (+39,4%); alta/muy alta tensión 35,3→51,4 (+45,6%); baja tensión 55,8→77,8 (+39,4%). Nuestro techo de 45 US$ era corto como proyección. Es proyección/recomendación, NO tarifa aplicada.
- **Cripto GCIE**: creció el consumo 14,4% (2022-2025) con criptominería vs 6,9% sin ellas. Cargas GCIE: 854 MW (2025) y 803 MW (2026) —demanda efectiva, NO potencia reservada. Los 943,8 MW de AGENTS.md son potencia reservada/contratada. Distinguir siempre.
- **Pérdidas de distribución ANDE**: 23,4% (2023) → 21,9% (2024) → 20,03% (2025). Comparables: Celesc 8,9%, Cemig 14,7%, EPEC 13%.
- **Morosidad particulares (sin Estado)**: 14,02% (2018) → 28,95% pico (2023) → 22,04% (2024) → 18,79% (2025).
- **Finanzas ANDE**: insuficiencia de rentabilidad US$468,2M (2002) → US$1.800M (2025) / US$2.000M (2026); deuda LP US$343,46M (2010) → US$1.664,29M (2026e); inversión récord 2025 US$349,2M. Carta Orgánica (Ley 966/1964, arts. 85 y 88) exige rentabilidad 8-10% sobre inversión inmovilizada.
- **CIER 2025**: tarifa residencial PY US$46/MWh e industrial US$35/MWh — las más bajas de 13 países (residencial media regional; industrial menor a El Salvador 207 y Colombia 181). Respaldan "la más barata de Sudamérica" con fuente citable.
- **Acuerdo Operativo Itaipú 2007**: expira 31-dic-2026 (renovado 2024-2026 por entendimiento del 16-abr/9-may-2024). Beneficio ~US$200M/año; desde 2027 la ANDE contratará toda su necesidad de potencia y podrá vender sobrante en Brasil (aún no vendió 1 kWh). NO confundir con Anexo C (reanudado nov-2025) ni con acuerdo tarifario (19,28, vence 1-ene-2027).
- **Plan Maestro ANDE 2024-2043**: ~800 MW/año promedio de generación fotovoltaica. Primera licitación: planta solar Loma Plata (Chaco), anunciada mayo-2026. AGO-2026: ninguna planta utility-scale en operación — usar "la primera licitación se anunció en mayo de 2026", NO "no hay ningún proyecto".

**Recordatorio de mantenimiento:** re-verificar la tarifa de ANDE cada 30 días. Próxima verificación: 7 de septiembre de 2026. Si cambia, actualizar `_includes/calculadora-energetica.html` y `calculadora-energetica.markdown` en menos de 48h.

### Tarifas eléctricas internacionales para data centers (verificado ago 2026)

Fuentes: Eurostat (nrg_pc_205, abril 2026), fuentes de mercado (CBRE, JLL, DCP reports), AGENTS.md.

- **Irlanda (Dublín) 150–190 USD/MWh (rango PPA data center)**: TRUE. Rango de mercado para PPAs de gran escala. Eurostat confirma €255/MWh (~276 USD/MWh) para consumidores no-domésticos medianos (500–2.000 MWh/año) en S2 2025 — los data centers negocian por debajo de ese techo. Fuentes: Eurostat + fuente de mercado independiente.
- **Suecia (Luleå) 45–65 USD/MWh**: TRUE. Dos fuentes de mercado independientes coinciden.
- **Chile 85–100 USD/MWh**: TRUE. Una fuente de mercado.
- **Virginia, EE.UU. 95–130 USD/MWh**: TRUE. Una fuente de mercado (Dominion Energy, PJM).
- **Paraguay 30–45 USD/MWh**: Rango con fuente primaria verificada (ANDE, Res. 49238/2024) pero en revisión activa. Ver sección Tarifas ANDE arriba.

#### Graduados STEM
- **~400 graduados en informática por año**: TRUE (INE vía La Tribuna, 22-01-2026). NO usar "400-600" ni "600" como techo. Estimación sectorial: 20-50 empleos por 100 MW en data centers.
