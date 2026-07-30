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
