# Planificar Bug (Logica Control)

Creá un plan simple y claro para arreglar un bug en Logica Control. El plan debe quedar en `specs/*.md`.

## Instrucciones

- IMPORTANTE: Estás escribiendo un **plan**. No implementes el fix acá.
- Primero entendé el bug: cómo se reproduce, qué debería pasar y qué pasa realmente.
- Investigá el código lo justo y necesario para identificar causa probable y archivos involucrados.
- El plan debe ser ejecutable: pasos concretos + cómo validar.
- Reemplazá todos los `<placeholders>`.
- El último bloque siempre debe incluir `Comandos de Validación`.

## Formato de Plan

```md
# Bug: <título corto del bug>

## Descripción
<qué falla y a quién afecta>

## Comportamiento esperado
<qué debería pasar>

## Comportamiento actual
<qué pasa hoy>

## Pasos para reproducir
1) <paso>
2) <paso>
3) <resultado>

## Causa probable
<hipótesis concreta (1 o 2) basada en lo que viste en el código/logs>

## Archivos relevantes
- `<ruta/archivo>` - <por qué es relevante>
- `<ruta/archivo>` - <por qué es relevante>

## Plan de arreglo
### 1) <paso>
- <tarea concreta>
- <tarea concreta>

### 2) <paso>
- <tarea concreta>
- <tarea concreta>

### 3) Validación final
- Ejecutar todos los `Comandos de Validación`.

## Tests a agregar o ajustar
- <test unitario o integración que cubra el bug y evite regresión>

## Criterios de aceptación
- <criterio medible 1>
- <criterio medible 2>

## Comandos de Validación
- `<comando tests>`
- `<comando lint/format si aplica>`
- `<comando smoke/e2e si existe>`

## Notes
<notas opcionales: riesgos, compatibilidad, cosas a revisar después>
Bug

$ARGUMENTS

Reporte

Resumí el plan en 3 a 6 bullets.

Incluí la ruta del archivo creado en specs/*.md.