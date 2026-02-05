# Generar nombre de branch (Logica Control)

Generá un nombre de branch de Git, en base al tipo de trabajo y un título corto. Mantenelo simple y consistente.

## Formato

`<tipo>-<numero>-<titulo-corto>`

- `<tipo>`: `feature` | `bug` | `chore`
- `<numero>`: número del issue/tarea (si no hay, usar `0000`)
- `<titulo-corto>`: 3 a 6 palabras, en minúsculas, sin tildes, sin caracteres raros, separado por guiones.

## Reglas

- Todo en minúsculas.
- Reemplazar espacios por `-`.
- Quitar tildes y `ñ` → `n`.
- No usar puntos, comas, paréntesis, ni símbolos.
- Si queda muy largo, acortarlo manteniendo el significado.

## Ejemplos

- `feature-0123-control-acceso-membresia`
- `bug-0048-sync-offline-duplicados`
- `chore-0000-limpiar-logs-y-errores`

## Pasos en Git

1) Asegurarse de estar en `main` y actualizado:
- `git checkout main`
- `git pull`

2) Crear la branch:
- `git checkout -b <nombre-de-branch>`

## Input
$ARGUMENTS

## Output
Devolver **solo** el nombre de la branch (una sola línea).
