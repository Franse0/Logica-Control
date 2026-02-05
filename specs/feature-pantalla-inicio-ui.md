# Feature: Pantalla de Inicio con Logo de Logica Control

## Descripción de la Feature
Crear la interfaz gráfica de usuario (UI) inicial del sistema Logica Control usando Tkinter. Esta ventana será el punto de entrada visual de la aplicación, mostrando la identidad de marca "LOGICA CONTROL" y preparando la arquitectura modular para futuras pantallas (login, registro de socios, validación biométrica, etc.).

La ventana debe ser simple, profesional y centrada en pantalla, con branding claro del gimnasio. Sirve como base para toda la UI del sistema de control de acceso.

## Historia de Usuario
Como **operador del sistema**
Quiero **ver una ventana de inicio profesional al ejecutar la aplicación**
Para **tener claridad de que el sistema Logica Control está corriendo y listo para operar**

## Planteo del Problema
Actualmente `src/main.py` solo imprime mensajes en consola sin interfaz gráfica. El sistema de control de acceso necesita una UI visible y profesional que:
- Identifique claramente la aplicación en ejecución
- Prepare la estructura modular para pantallas futuras (validación biométrica, registro, reportes)
- Sea fácil de usar en entorno de gimnasio (recepción/torniquete)
- Siga principios de diseño UI/UX básicos (centrado, legible, responsivo)

## Planteo de Solución
Implementar una ventana principal Tkinter en `src/ui/main_window.py` que:
1. Muestre el branding "LOGICA CONTROL" centrado con tipografía grande
2. Incluya subtítulo descriptivo "Sistema de Control de Acceso para Gimnasios"
3. Configure ventana de 800x600 px centrada en pantalla
4. Use fondo claro (blanco/gris) para mejor legibilidad
5. Integre con `src/main.py` como entry point de la UI
6. Prepare arquitectura modular para agregar pantallas (frames/vistas) en el futuro

Esta solución es:
- **Mínima**: No sobre-ingeniería, solo lo necesario para la UI base
- **Modular**: Fácil extender con nuevas vistas (login, registro, validación)
- **Offline-first**: Tkinter es nativo de Python, sin dependencias externas

## Archivos Relevantes
Usar estos archivos para implementar la feature:

- `src/main.py` - Entry point actual de la aplicación. Actualmente imprime en consola. Debe importar y lanzar la ventana Tkinter.
- `src/ui/__init__.py` - Package UI existente pero vacío. Se usará para exportar la ventana principal.
- `requirements.txt` - Gestión de dependencias. Tkinter viene con Python, no requiere agregados.

### New Files
- `src/ui/main_window.py` - Módulo nuevo que contiene la clase `MainWindow` con toda la lógica de la ventana principal Tkinter (configuración, widgets, layout, centrado).

## Plan de Implementación
### Fase 1: Base
- Crear módulo `src/ui/main_window.py` con clase `MainWindow` que hereda de `tk.Tk`
- Configurar ventana: título, tamaño (800x600), no-redimensionable (opcional)
- Implementar método de centrado en pantalla usando geometría de Tkinter

### Fase 2: Implementación Core
- Diseñar layout con widgets Tkinter:
  - `tk.Label` para texto "LOGICA CONTROL" (fuente grande, bold)
  - `tk.Label` para subtítulo "Sistema de Control de Acceso para Gimnasios"
- Aplicar colores (fondo blanco/gris claro, texto oscuro para contraste)
- Usar `pack()` o `grid()` para centrar elementos verticalmente

### Fase 3: Integración
- Actualizar `src/main.py` para:
  - Importar `MainWindow` desde `src.ui.main_window`
  - Instanciar ventana después de print inicial
  - Llamar `mainloop()` para mantener ventana abierta
- Actualizar `src/ui/__init__.py` para exportar `MainWindow`
- Verificar que ejecutar `python src/main.py` lance la ventana correctamente

## Tareas Paso a Paso
IMPORTANTE: Ejecutar cada paso en orden, de arriba hacia abajo.

### 1) Crear módulo de ventana principal
- Crear archivo `src/ui/main_window.py`
- Importar `tkinter as tk`
- Definir clase `MainWindow(tk.Tk)` con constructor `__init__()`
- Configurar título de ventana: "Logica Control - Sistema de Acceso"
- Establecer tamaño: `800x600`
- Implementar método `center_window()` que calcula posición centrada usando `winfo_screenwidth()` y `winfo_screenheight()`
- Configurar color de fondo: `#f0f0f0` (gris claro)

### 2) Diseñar layout con branding
- Crear `tk.Label` para texto principal "LOGICA CONTROL":
  - Fuente: `("Arial", 48, "bold")`
  - Color texto: `#2c3e50` (azul oscuro profesional)
  - Padding superior para centrado visual
- Crear `tk.Label` para subtítulo "Sistema de Control de Acceso para Gimnasios":
  - Fuente: `("Arial", 16)`
  - Color texto: `#7f8c8d` (gris medio)
  - Padding entre título y subtítulo
- Usar `pack()` con `pady` para espaciado vertical

### 3) Integrar con entry point main.py
- Actualizar `src/main.py`:
  - Importar `from ui.main_window import MainWindow`
  - Después del print inicial, instanciar: `app = MainWindow()`
  - Llamar `app.mainloop()` al final de `main()`
  - Remover o comentar TODOs de UI ya implementados
- Actualizar `src/ui/__init__.py`:
  - Agregar `from .main_window import MainWindow`
  - Exportar en `__all__ = ["MainWindow"]`

### 4) Validación final
- Ejecutar todos los `Comandos de Validación` para asegurar cero regresiones.
- Verificar que la ventana se abre, está centrada y muestra el branding correctamente
- Confirmar que no hay errores en consola al ejecutar

## Estrategia de Testing
### Unit Tests
No aplican unit tests para esta feature (es UI pura sin lógica de negocio). La validación será manual.

### Integration Tests
- **Test manual 1**: Ejecutar `python src/main.py` desde raíz del proyecto → debe abrir ventana Tkinter
- **Test manual 2**: Verificar que ventana está centrada en pantalla
- **Test manual 3**: Verificar que texto "LOGICA CONTROL" es visible, grande y centrado
- **Test manual 4**: Verificar que subtítulo es legible y está debajo del título
- **Test manual 5**: Verificar que cerrar ventana termina la aplicación sin errores

### Edge Cases
- **Resolución de pantalla pequeña**: En pantallas < 800x600, la ventana debe ajustarse sin error (considerar `minsize()`)
- **Sistema sin display gráfico**: Si se ejecuta en servidor sin X11, debe fallar con mensaje claro (no aplicable para uso en gimnasio, pero documentar)
- **Múltiples monitores**: Ventana debe centrarse en monitor principal

## Criterios de Aceptación
- Al ejecutar `python src/main.py` se abre una ventana Tkinter sin errores
- La ventana tiene título "Logica Control - Sistema de Acceso"
- La ventana muestra "LOGICA CONTROL" centrado con fuente grande (48pt o similar)
- El subtítulo "Sistema de Control de Acceso para Gimnasios" es visible debajo del título
- La ventana tiene tamaño 800x600 pixels
- La ventana está centrada en la pantalla al abrirse
- El fondo de la ventana es claro (blanco o gris claro)
- El código de la ventana está en `src/ui/main_window.py` y es modular
- No hay excepciones ni errores en consola al ejecutar y cerrar la aplicación

## Comandos de Validación
Ejecutar cada comando para validar que la feature funciona correctamente con cero regresiones.

- `python src/main.py` - Debe abrir la ventana sin errores. Cerrar manualmente para verificar que termina limpiamente.
- `python -m py_compile src/ui/main_window.py` - Verificar sintaxis correcta del módulo nuevo
- `python -m py_compile src/main.py` - Verificar sintaxis correcta del entry point actualizado

## Notes
- **Tkinter viene con Python**: No requiere dependencias adicionales en `requirements.txt`
- **Diseño futuro**: Esta ventana es temporal. En el futuro podría convertirse en splash screen o menú principal con botones (login admin, modo validación biométrica, etc.)
- **Extensibilidad**: Para agregar nuevas pantallas, usar frames Tkinter o ventanas secundarias (`tk.Toplevel`). Considerar patrón MVC/MVP en el futuro.
- **Colores**: Se usan colores neutros profesionales. Futuros diseñadores pueden cambiar el esquema de colores según branding del gimnasio.
- **Accesibilidad**: Fuentes grandes y alto contraste para fácil lectura desde distancia (útil en torniquete/recepción).
