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
Para cualquier dato sobre Paraguay, el fact-checker DEBE consultar:
- Wikipedia en español (no solo en inglés): https://es.wikipedia.org/
- ANDE (portal y noticias): https://www.ande.gov.py/
- BACN (leyes): https://www.bacn.gov.py/
- MADES (clima/ambiente): http://www.mades.gov.py/
- ABC Color (secciones Tecnología, Economía, Nacionales): https://www.abc.com.py/
- La Nación: https://www.lanacion.com.py/
- Itaipú Binacional: https://www.itaipu.gov.py/
