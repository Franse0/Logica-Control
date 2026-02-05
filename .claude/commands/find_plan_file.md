# Encontrar archivo de plan (Logica Control)

Tu tarea es encontrar la ruta exacta del archivo de plan que se creó en `specs/` (por ejemplo: `specs/feature-control-acceso-membresia.md`).

## Qué devolver

- Si lo encontrás: devolvé **solo** la ruta del archivo (una sola línea).
- Si no lo encontrás: devolvé `0`.

## Cómo buscar (orden recomendado)

1) Ver archivos nuevos o modificados:
- `git status`

2) Buscar cambios contra `main` (si aplica):
- `git diff --name-only main...HEAD`

3) Listar los planes disponibles:
- `ls -la specs/`

4) Si sabés parte del nombre, filtrar:
- `ls specs/ | grep <palabra>`

## Input
$ARGUMENTS

## Output
Devolver **solo** la ruta del archivo o `0`.
