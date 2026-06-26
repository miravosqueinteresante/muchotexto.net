# Rediseño del prompt de editoriales — enfoque fáctico

**Fecha:** 2026-06-26
**Estado:** Aprobado

## Problema

Las editoriales generadas por `editorial_diario.py` sufren de:
1. Alucinaciones fácticas (inventan hechos no presentes en el Pulso)
2. Oraciones rotas por `add_internal_links()` insertando links en medio de frases
3. Tono sensacionalista y metáforas forzadas ("X es el espejo de Y")
4. Temperatura 0.8 promoviendo creatividad sobre precisión

## Diseño

### 1. Nuevo System Prompt

Reemplazo completo del prompt actual. El AI pasa de "editorialista filosófico" a "analista fáctico":

- **Tono:** directo, periodístico. La opinión surge de contrastar hechos, no de filosofar.
- **Extensión:** 500-700 palabras (antes 800-1200).
- **Reglas eliminadas:** instrucciones de "hook provocador", "pregunta provocadora", "dato impactante", reglas SEO de keywords.
- **Reglas mantenidas:** no inventar datos, no atribuir citas, solo usar información del Pulso.
- **Reglas nuevas:** no usar metáforas forzadas, no preguntas retóricas vacías, no interpretaciones sin base en datos.
- **Temperature:** 0.3 (antes 0.8)

### 2. Arreglo de `add_internal_links()`

**Bug actual:** usa `str.replace(matched_text, link)` que puede partir palabras al medio.

**Fix:** usar `re.sub()` con word boundaries (`\b`) para respetar límites de palabra. Además, verificar que el reemplazo no rompa la gramática circundante (la posición del match debe estar en un contexto de frase completa, no intra-palabra).

### 3. Corrección del mapeo de links

| Patrón problemático | Link viejo | Acción |
|---|---|---|
| `Mundial.*fútbol\|Albirroja.*Mundial` | `que-es-realmente-el-futbol` (ensayo filosófico) | Eliminar entrada — el link al Pulso del día ya existe en el footer del post |

Los demás mapeos en `ARTICULOS_LINKEABLES` se mantienen.

### 4. Post-procesamiento de validación (no bloqueante)

Función `validate_content()` que:
- Detecta frases contradictorias entre la editorial y el Pulso fuente
- Marca oraciones sin ningún dato del Pulso (posible alucinación)
- Loguea warnings sin bloquear la publicación
- Sirve como trazabilidad para debugging futuro

### 5. Corrección manual de la editorial del 26/jun

Arreglar los 3 errores detectados:
- Párrafo 1: link insertado partiendo la frase → reescribir sin el link roto
- Línea 23: "pelea por entrar al Mundial" → corregir a "avanza en el Mundial" (ya está jugando)
- Tono general: reducir metáforas forzadas

## Archivos a modificar

- `scripts/editorial_diario.py` — system prompt, temperature, add_internal_links, validate_content
- `_posts/2026-06-26-es-el-futbol-el-unico-pacto-nacional-editorial-26-de-junio-d-editoria.md` — corrección manual

## Verificación

- Build de Jekyll sin errores
- Editorial generada manualmente con el nuevo prompt para validar calidad
