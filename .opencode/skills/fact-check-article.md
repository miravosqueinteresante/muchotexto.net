# Skill: Verificación de datos para artículos

## Cuándo usar

Siempre antes de commitear un artículo long-form en `_posts/`. También cuando el usuario pida "chequea este artículo", "verifica los datos", "fact-check", "comprobar con fuentes oficiales".

## Paso 0 (OBLIGATORIO): descargar las fuentes ANTES de despachar

**Nunca despachar un fact-checker sin haber descargado las fuentes citadas.** Un verificador que no abre la fuente marca falsos negativos (error histórico: Biggie/DATO, ABC Color 27-ago y LinkedIn "Full Digital" se marcaron UNVERIFIABLE cuando las fuentes citadas contenían la cita exacta).

```bash
python scripts/fetch_sources.py _posts/2026-09-XX-slug.md
```

Esto descarga el texto real de cada URL citada a `<out>/sources/NN.txt` y genera `<out>/sources/INDEX.md`. Al despachar cada agente, **pasarle la ruta de esa carpeta** con la instrucción de leer los `.txt` antes de emitir veredicto. Regla: un claim no se marca UNVERIFIABLE si su fuente citada está descargada y la contiene.

## Método

### Fase 1: Extracción

Leer el artículo línea por línea. Extraer todo claim factual en categorías:

1. **Jurídico**: números de ley, decretos, fechas de promulgación, artículos, reguladores
2. **Numérico**: MW, USD, GWh, porcentajes, empleos, km, m², habitantes
3. **Corporativo**: nombres de empresas, capacidades, fases, fechas de hitos, tipo de infraestructura
4. **Institucional**: nombres de funcionarios, cargos, declaraciones textuales
5. **Internacional**: datos de otros países, rankings, modelos de IA, inversiones
6. **Fuentes**: verificar que las URLs citadas en la sección Fuentes no den 404

### Fase 2: Despacho paralelo

Despachar un agente independiente por cada categoría. Cada agente debe:

- **Leer primero los `.txt` descargados** en `Paso 0` para los claims que tengan fuente en el artículo.
- Buscar fuentes oficiales adicionales solo para los claims SIN fuente descargada o que requieran segunda verificación.
- Cruzar claims contra fuentes primarias
- Devolver veredicto: TRUE / FALSE / PARTIALLY TRUE / UNVERIFIABLE
- Incluir URL de la fuente en cada veredicto

Fuentes prioritarias por país:
- **Paraguay**: BACN (leyes), DNCP (contrataciones), ANDE, IPS, INE, MITIC, Contraloría
- **Brasil**: gov.br, ANEEL, IBGE
- **Global**: Wikipedia, World Bank, IMF, Uptime Institute, CSO, SEC/EDGAR

### Fase 3: Informe

Emitir informe con tres secciones:

```
## Errores graves (FALSE)
- claim + fuente que lo refuta

## Discrepancias (PARTIALLY TRUE)
- claim + corrección necesaria

## No verificable (UNVERIFIABLE)
- claim + fuente sugerida para verificar
```

### Fase 4: Corrección

Aplicar todos los FALSE y PARTIALLY TRUE. Para UNVERIFIABLE, decidir si:
- Se mantiene con atribución explícita a la fuente
- Se elimina
- Se reformula en condicional ("según reportes", "estaría")

## Reglas duras

- **Nunca usar Wikipedia en español para definiciones sin verificar que la página existe.** La página `IA soberana` no existe en español, solo en inglés.
- **Nunca afirmar que una infraestructura "ya opera" si está en construcción.** Verificar estado operativo en fuente primaria de la empresa.
- **Nunca mezclar minería Bitcoin (ASIC) con cómputo GPU/AI.** Son infraestructuras distintas con empleo y cadena de valor distintos.
- **Verificar números de ley en BACN.** Un número de ley puede corresponder a una ley completamente distinta.
- **Cruzar claims de empleo sectorial** con IPS cuando sea posible; las cámaras inflan.
- **Benchmarks de industria (CAPEX, empleo/MW, m²/MW)**: verificar con al menos 2 fuentes independientes (Uptime Institute, CBRE, DCD, Cortex, Alpha Matica, Hamm Institute).
