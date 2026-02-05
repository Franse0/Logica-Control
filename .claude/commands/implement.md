# Implementar Plan (Logica Control)

Este command toma un plan ya escrito (por ejemplo, el archivo `specs/*.md`) y lo implementa con **testing incremental e iteración automática**.

## Instrucciones

### 1. Lectura del Plan
- Leé el plan completo antes de empezar.
- Identificá los pasos de implementación y los comandos de validación.

### 2. Implementación Incremental con Testing
Para cada paso del plan:

1. **Implementá el paso** según las instrucciones
2. **Verificá sintaxis**: Ejecutá `python -m py_compile` en los archivos modificados
3. **Probá que funcione**:
   - Si el plan incluye validaciones específicas para este paso, ejecútalas
   - Si no, ejecutá `python src/main.py` para verificar que no haya errores de runtime
4. **Si falla**:
   - Analizá el error
   - Corregí el problema
   - Volvé a probar (hasta 3 intentos)
   - Si después de 3 intentos sigue fallando, documentá el error y continuá
5. **Si funciona**: Continuá con el siguiente paso

### 3. Validación Final
Después de implementar todos los pasos:
- Ejecutá TODOS los "Comandos de Validación" del plan
- Si alguno falla, intentá corregirlo (hasta 2 iteraciones)
- Reportá qué funcionó y qué no

### 4. Reglas Importantes
- Mantené el cambio acotado a lo que pide el plan (no inventés scope)
- Si algo del plan no es posible, documentalo y proponé ajuste mínimo
- **NO continúes** con pasos siguientes si un paso crítico falló
- Priorizá que funcione sobre que esté perfecto

## Plan
$ARGUMENTS

## Reporte

Estructurá tu reporte así:

### ✅ Implementado Exitosamente
- [Bullet por cada paso que funcionó]

### ⚠️ Problemas Encontrados y Resueltos
- [Errores que encontraste y cómo los corregiste]

### ❌ Problemas Sin Resolver (si aplica)
- [Errores que no pudiste resolver después de intentar]

### 📊 Estadísticas
```bash
git diff --stat
```

### 🧪 Resultados de Validación
- Comando: `python src/main.py`
  - Resultado: [Exitoso / Falló]
  - Output: [output relevante si falló]
- [Otros comandos de validación...]
