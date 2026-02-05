# Generar mensaje de commit (Logica Control)

Generá un mensaje de commit simple, consistente y útil.

## Formato

`<autor>: <tipo>: <mensaje>`

- `<autor>`: tu nombre o alias (ej. `fran`)
- `<tipo>`: `feature` | `bug` | `chore`
- `<mensaje>`: corto, claro, en presente (qué hace el cambio)

## Reglas

- Máximo 60 caracteres ideal (si pasa un poco, igual priorizá claridad).
- En presente: “agrega”, “corrige”, “ajusta”, “refactoriza”.
- Sin punto final.
- No repetir el tipo dentro del mensaje (ya está en el formato).
- Evitar detalles técnicos innecesarios; que sea entendible.

## Ejemplos

- `fran: feature: agrega validacion de membresia vigente`
- `fran: bug: corrige duplicados en sync offline`
- `fran: chore: refactoriza logs de acceso`

## Pasos en Git

1) Revisar cambios:
- `git diff HEAD`

2) Stagear:
- `git add -A`

3) Commitear:
- `git commit -m "<mensaje>"`

## Input
$ARGUMENTS

## Output
Devolver **solo** el mensaje de commit (una sola línea).
