# Feature: Formulario de Login en Pantalla Principal

## Descripción de la Feature
Agregar un formulario de login visual a la pantalla principal de Logica Control con campos de usuario y contraseña. Este formulario servirá como punto de entrada para futuras implementaciones de autenticación de usuarios administradores del sistema. En esta fase inicial, el formulario es solo visual (sin funcionalidad de backend) para establecer la estructura de UI.

## Historia de Usuario
Como administrador del sistema de control de acceso
Quiero ver un formulario de login en la pantalla principal
Para poder acceder al sistema de gestión de socios y configuración en el futuro

## Planteo del Problema
Actualmente la aplicación muestra solo el título "LOGICA CONTROL" y un subtítulo en la pantalla principal. No existe ningún mecanismo de autenticación o punto de entrada para administradores. Para poder implementar funcionalidades de gestión (alta de socios, configuración, reportes), primero necesitamos la UI de login que permita distinguir entre usuarios administradores y el modo de validación biométrica para socios.

## Planteo de Solución
Modificar `src/ui/main_window.py` para agregar debajo del título existente un formulario simple con:
- Label + Entry para usuario
- Label + Entry para contraseña (con máscara `show="*"`)
- Botón "Iniciar Sesión" (sin funcionalidad todavía)

Usaremos el layout manager `pack` de Tkinter para mantener consistencia con el código existente y lograr un diseño centrado y limpio. Los widgets tendrán padding apropiado para buena UX.

## Archivos Relevantes
Usar estos archivos para implementar la feature:

- `src/ui/main_window.py` - Ventana principal existente donde se agregará el formulario de login. Ya tiene el título "LOGICA CONTROL" y subtítulo, necesitamos agregar los widgets del formulario debajo del subtítulo existente.
- `src/main.py` - Entry point de la aplicación, no requiere cambios pero se usará para validar que la app corre correctamente.

## Plan de Implementación
### Fase 1: Base
No requiere cambios de estructura ni nuevos archivos. La implementación será directamente sobre el archivo existente `src/ui/main_window.py`.

### Fase 2: Implementación Core
Modificar el método `create_widgets()` de la clase `MainWindow` para agregar:
1. Frame contenedor para el formulario (para agrupar los widgets de login)
2. Labels y Entries para usuario y contraseña
3. Botón de inicio de sesión
4. Configuración de estilos: colores, fuentes, padding, ancho de inputs

### Fase 3: Integración
No hay integración con otros módulos en esta fase. El formulario es solo visual y no conecta con lógica de autenticación todavía.

## Tareas Paso a Paso
IMPORTANTE: Ejecutar cada paso en orden, de arriba hacia abajo.

### 1) Agregar frame contenedor para el formulario de login
- Crear un `tk.Frame` debajo del `subtitle_label` existente
- Configurar el frame con el mismo color de fondo `#f0f0f0`
- Usar `pack()` con padding vertical apropiado (ej. `pady=40`)

### 2) Agregar campo de usuario
- Crear `tk.Label` con texto "Usuario:"
- Configurar fuente legible (ej. Arial 14)
- Crear `tk.Entry` con ancho de 30 caracteres
- Usar `pack()` para posicionar label y entry con padding

### 3) Agregar campo de contraseña
- Crear `tk.Label` con texto "Contraseña:"
- Crear `tk.Entry` con ancho de 30 caracteres y `show="*"`
- Usar `pack()` para posicionar label y entry con padding

### 4) Agregar botón de inicio de sesión
- Crear `tk.Button` con texto "Iniciar Sesión"
- Configurar color de fondo destacado (ej. `#3498db` azul)
- Configurar color de texto blanco para contraste
- Configurar fuente bold y tamaño apropiado
- Agregar padding interno al botón (ej. `padx=40, pady=10`)
- Por ahora, el comando del botón puede ser vacío o un placeholder sin funcionalidad

### 5) Validación final
- Ejecutar `python src/main.py` y verificar que la aplicación inicia sin errores
- Verificar visualmente que todos los elementos se muestran correctamente
- Verificar que el campo de contraseña muestra asteriscos al escribir
- Verificar que el botón es clickeable (aunque no haga nada todavía)

## Estrategia de Testing
### Unit Tests
No aplica en esta fase. El formulario es solo UI sin lógica de negocio que testear.

### Integration Tests
No aplica en esta fase. No hay integración con backend o servicios.

### Edge Cases
- Campo de contraseña debe mostrar asteriscos correctamente
- Layout debe verse ordenado en resolución 800x600
- Ventana debe seguir centrada correctamente
- Colores y fuentes deben ser legibles y consistentes

## Criterios de Aceptación
- ✅ Se mantiene el título "LOGICA CONTROL" existente en la parte superior
- ✅ Se ven dos campos de entrada con sus labels ("Usuario:" y "Contraseña:")
- ✅ La contraseña se muestra con asteriscos al escribir
- ✅ El botón "Iniciar Sesión" es visible y clickeable
- ✅ El layout se ve ordenado, centrado y con espaciado apropiado
- ✅ Los inputs tienen un ancho mínimo de 30 caracteres
- ✅ La aplicación corre sin errores: `python src/main.py`

## Comandos de Validación
Ejecutar cada comando para validar que la feature funciona correctamente con cero regresiones.

- `python src/main.py` - La aplicación debe iniciar sin errores y mostrar la ventana con el formulario de login

## Notes
- Esta feature solo implementa la UI visual. La funcionalidad de autenticación (validación de credenciales, sesiones, etc.) será implementada en una feature futura.
- Se mantiene el uso de `pack()` como layout manager para consistencia con el código existente.
- Los colores y fuentes elegidos buscan mantener el estilo profesional y limpio que ya tiene la aplicación.
- El botón puede tener un comando dummy o vacío por ahora, será conectado a lógica real en futuras features.
