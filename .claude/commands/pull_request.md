# Crear Pull Request (Logica Control)

Usá este command para crear un Pull Request en GitHub de forma consistente, incluyendo título, descripción y referencias (issue + plan + tracking).

## Variables

branch_name: $1
issue: $2
plan_file: $3
tracking_id: $4

## Instrucciones

- Generar el título del PR con este formato:
  `<tipo>: #<numero> - <titulo>`
  Donde `<tipo>` puede ser: `feature`, `bug`, `chore`.
- El cuerpo del PR debe incluir:
  - **Resumen** del contexto del issue
  - **Link** al archivo de plan (`plan_file`)
  - Referencia al issue: `Closes #<numero>`
  - **Tracking ID** (por ejemplo, `tracking_id`)
  - **Checklist** de lo realizado
  - **Cambios clave** (resumen de qué se modificó)
- Extraer `numero`, `tipo` y `titulo` desde el JSON del issue.

## Run

1) Ver resumen de cambios:
- `git diff origin/main...HEAD --stat`

2) Ver commits incluidos:
- `git log origin/main..HEAD --oneline`

3) Ver archivos cambiados:
- `git diff origin/main...HEAD --name-only`

4) Pushear la branch:
- `git push -u origin <branch_name>`

5) Crear el PR con GitHub CLI:
- Setear `GH_TOKEN` desde `GITHUB_PAT` si está disponible
- `gh pr create --title "<titulo_pr>" --body "<cuerpo_pr>" --base main`

6) Capturar la URL del PR desde la salida del comando.

## Output
Devolver **solo** la URL del PR creado (una sola línea).
