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
