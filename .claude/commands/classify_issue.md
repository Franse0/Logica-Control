# Clasificar Issue (Logica Control)

Leé la descripción de una tarea/issue y devolvé qué tipo de trabajo es para elegir el command correcto.

## Tipos posibles

- `/feature` → funcionalidad nueva o mejora visible para el usuario.
- `/bug` → algo que hoy funciona mal (error, comportamiento incorrecto, regresión).
- `/chore` → mantenimiento/refactor/limpieza, sin cambio funcional esperado para el usuario final.
- `0` → no se puede clasificar con seguridad.

## Reglas simples

- Si habla de “agregar/permitir/implementar” algo nuevo → `/feature`
- Si habla de “error/falla/no funciona/incorrecto” → `/bug`
- Si habla de “refactor/limpiar/ordenar/actualizar deps” → `/chore`
- Si es ambiguo o mezcla demasiado → `0`

## Input
$ARGUMENTS

## Output
Devolver **solo** uno de estos valores, en una sola línea:
`/feature` o `/bug` o `/chore` o `0`
