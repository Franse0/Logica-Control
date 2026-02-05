# Feature: Validación de Credenciales en Formulario de Login

## Descripción de la Feature
Agregar funcionalidad de validación de credenciales al formulario de login existente en la ventana principal de Logica Control. Esta feature implementa la lógica de autenticación básica usando credenciales hardcodeadas (`admin`/`admin123`) y muestra feedback visual al usuario (mensajes de éxito en verde y errores en rojo).

Esta es una implementación temporal para validar el flujo de login antes de integrar la base de datos. Permite probar la UX de autenticación y preparar la arquitectura para futura validación contra SQLite.

## Historia de Usuario
Como **operador del gimnasio (recepcionista o administrador)**
Quiero **ingresar mis credenciales en el formulario de login y recibir feedback inmediato**
Para **autenticarme en el sistema de control de acceso y acceder a las funcionalidades restringidas**

## Planteo del Problema
Actualmente el formulario de login (Issue #4) es solo visual - los campos de usuario y contraseña no tienen validación, y el botón "Iniciar Sesión" no ejecuta ninguna acción. El sistema necesita:
- Validar que los campos no estén vacíos antes de procesar
- Comparar credenciales ingresadas contra valores conocidos (hardcoded por ahora)
- Mostrar feedback claro al usuario sobre el resultado de la validación
- Preparar la base para futura autenticación con base de datos

Sin esta funcionalidad, el login es una UI muerta que no cumple su propósito de control de acceso.

## Planteo de Solución
Implementar un método `validate_login()` en la clase `MainWindow` que:
1. **Lee los valores** de `self.username_entry` y `self.password_entry` usando `.get()`
2. **Valida campos vacíos**: Si alguno está vacío, muestra mensaje "Complete todos los campos" en amarillo/naranja
3. **Valida credenciales hardcodeadas**: Compara contra `username == "admin"` y `password == "admin123"`
   - Si son correctas → Muestra mensaje "✅ Inicio de sesión exitoso" en verde
   - Si son incorrectas → Muestra mensaje "❌ Usuario o contraseña incorrectos" en rojo
4. **Muestra feedback** usando un `tk.Label` debajo del botón "Iniciar Sesión" que actualiza su texto y color dinámicamente

Esta solución es:
- **Mínima**: Solo la lógica necesaria para validar y dar feedback
- **Preparatoria**: Fácil refactorizar después para validar contra base de datos
- **Clara**: Feedback visual inmediato para el usuario

## Archivos Relevantes
Usar estos archivos para implementar la feature:

- `src/ui/main_window.py` - Ventana principal que contiene el formulario de login (Issue #4). Aquí se agregará el método `validate_login()` y el label de mensajes. Los campos `self.username_entry` y `self.password_entry` ya existen como atributos de instancia.

### New Files
Ninguno. Esta feature solo modifica código existente.

## Plan de Implementación
### Fase 1: Base
- Verificar que el formulario de login visual existe en `src/ui/main_window.py` (Issue #4)
- Si no existe, mergear o cherry-pick los cambios de la branch `feature-0004-agregar-login-formulario`
- Confirmar que existen los atributos `self.username_entry` y `self.password_entry`

### Fase 2: Implementación Core
- Crear método `validate_login(self)` en clase `MainWindow`:
  - Obtener valores de entrada con `.get()` y limpiar espacios con `.strip()`
  - Validar campos vacíos (ambos deben tener contenido)
  - Comparar credenciales contra hardcoded: `admin` / `admin123`
  - Llamar a método helper `show_message()` para actualizar el label de feedback
- Crear método helper `show_message(self, text, color)`:
  - Actualiza el texto del label con `self.message_label.config(text=text, fg=color)`
  - Colores: verde `#27ae60` para éxito, rojo `#e74c3c` para error, naranja `#e67e22` para advertencia
- Crear `self.message_label` en `create_widgets()`:
  - Label vacío inicialmente, debajo del botón de login
  - Background `#f0f0f0` (igual que ventana)
  - Font `("Arial", 12)`

### Fase 3: Integración
- Conectar botón "Iniciar Sesión" al método `validate_login()`:
  - Cambiar `command=lambda: None` por `command=self.validate_login`
- Verificar que ejecutar `python src/main.py` muestre el formulario funcional
- Probar los 3 flujos:
  1. Campos vacíos → mensaje de advertencia
  2. Credenciales incorrectas → mensaje de error rojo
  3. Credenciales correctas (`admin`/`admin123`) → mensaje de éxito verde

## Tareas Paso a Paso
IMPORTANTE: Ejecutar cada paso en orden, de arriba hacia abajo.

### 1) Verificar y preparar formulario base
- Confirmar que existe el formulario de login en `src/ui/main_window.py`
- Si no existe (branch actual no tiene Issue #4), mergear cambios de `feature-0004-agregar-login-formulario`
- Verificar atributos `self.username_entry` y `self.password_entry` en `create_widgets()`
- Leer el código completo de `main_window.py` para entender la estructura actual

### 2) Crear label de mensajes
- En método `create_widgets()`, después de crear `login_button`, agregar:
  - `self.message_label = tk.Label(login_frame, text="", font=("Arial", 12), bg="#f0f0f0")`
  - `self.message_label.pack(pady=(15, 0))` para posicionar debajo del botón
- El label inicia vacío (sin texto) y solo se actualiza al validar

### 3) Implementar método show_message
- Crear método `show_message(self, text: str, color: str)`:
  - Actualiza `self.message_label` con `self.message_label.config(text=text, fg=color)`
  - Parámetros:
    - `text`: mensaje a mostrar (ej. "✅ Inicio de sesión exitoso")
    - `color`: color hex (ej. `#27ae60` verde, `#e74c3c` rojo, `#e67e22` naranja)

### 4) Implementar método validate_login
- Crear método `validate_login(self)`:
  - Obtener valores: `username = self.username_entry.get().strip()`
  - Obtener valores: `password = self.password_entry.get().strip()`
  - **Validación 1 - Campos vacíos**:
    ```python
    if not username or not password:
        self.show_message("Complete todos los campos", "#e67e22")
        return
    ```
  - **Validación 2 - Credenciales hardcodeadas**:
    ```python
    if username == "admin" and password == "admin123":
        self.show_message("✅ Inicio de sesión exitoso", "#27ae60")
    else:
        self.show_message("❌ Usuario o contraseña incorrectos", "#e74c3c")
    ```

### 5) Conectar botón con validación
- En método `create_widgets()`, encontrar la línea del `login_button`
- Cambiar `command=lambda: None` por `command=self.validate_login`
- Verificar sintaxis correcta (el método se pasa sin paréntesis)

### 6) Validación final
- Ejecutar todos los `Comandos de Validación` para asegurar cero regresiones.
- Probar los 3 escenarios manualmente (ver sección Testing)

## Estrategia de Testing
### Unit Tests
No aplican unit tests para esta feature (lógica simple con hardcoded). La validación será manual/integración.

Futuras mejoras podrían incluir tests unitarios si se extrae la lógica de validación a un módulo separado (ej. `src/auth/validator.py`).

### Integration Tests
**Test manual 1 - Campos vacíos**:
- Ejecutar `python src/main.py`
- Dejar ambos campos vacíos
- Hacer clic en "Iniciar Sesión"
- ✅ Debe mostrar "Complete todos los campos" en naranja/amarillo

**Test manual 2 - Credenciales incorrectas**:
- Ingresar usuario: `test`, contraseña: `wrong`
- Hacer clic en "Iniciar Sesión"
- ✅ Debe mostrar "❌ Usuario o contraseña incorrectos" en rojo

**Test manual 3 - Credenciales correctas**:
- Ingresar usuario: `admin`, contraseña: `admin123`
- Hacer clic en "Iniciar Sesión"
- ✅ Debe mostrar "✅ Inicio de sesión exitoso" en verde

**Test manual 4 - Solo usuario vacío**:
- Ingresar contraseña: `admin123`, dejar usuario vacío
- Hacer clic en "Iniciar Sesión"
- ✅ Debe mostrar "Complete todos los campos"

**Test manual 5 - Solo contraseña vacía**:
- Ingresar usuario: `admin`, dejar contraseña vacía
- Hacer clic en "Iniciar Sesión"
- ✅ Debe mostrar "Complete todos los campos"

### Edge Cases
- **Espacios en blanco**: Credenciales con espacios al inicio/final (ej. `" admin "`) → Se manejan con `.strip()`
- **Case sensitivity**: Usuario `ADMIN` o `Admin` → No coincide (case-sensitive por diseño simple)
- **Campos con solo espacios**: Contraseña `"    "` → Se valida como vacío gracias a `.strip()`
- **Múltiples intentos fallidos**: No hay límite de reintentos por ahora (feature futura: rate limiting)
- **Enter key**: No está configurado, solo funciona el botón (feature futura: bind Enter key)

## Criterios de Aceptación
- Al hacer clic en "Iniciar Sesión" con campos vacíos, se muestra mensaje "Complete todos los campos" en color naranja/amarillo
- Al ingresar credenciales incorrectas, se muestra mensaje "❌ Usuario o contraseña incorrectos" en rojo
- Al ingresar `admin` / `admin123`, se muestra mensaje "✅ Inicio de sesión exitoso" en verde
- Los mensajes aparecen debajo del botón "Iniciar Sesión" en el mismo frame del login
- El label de mensajes no afecta el layout existente (no desconfigura el formulario)
- El método `validate_login()` existe en la clase `MainWindow`
- El botón está conectado al método con `command=self.validate_login`
- La aplicación corre sin errores: `python src/main.py`

## Comandos de Validación
Ejecutar cada comando para validar que la feature funciona correctamente con cero regresiones.

- `python -m py_compile src/ui/main_window.py` - Verificar sintaxis correcta del módulo modificado
- `python src/main.py` - Debe abrir la ventana con formulario funcional. Probar los 3 escenarios de testing manual descritos arriba.

## Notes
- **Credenciales hardcodeadas**: Esta es una implementación temporal. En Issue futuro se reemplazará con validación contra base de datos (`src/database/gimnasio.db` → tabla de usuarios/administradores).
- **Seguridad**: Las credenciales `admin`/`admin123` son débiles y solo para demo. En producción se usarán hashes (bcrypt/argon2) almacenados en BD.
- **UX futura**: Considerar agregar:
  - Bind de tecla Enter para validar (no requiere clic)
  - Indicador visual en campos inválidos (borde rojo)
  - Limpieza de campos después de login exitoso
  - Transición a siguiente pantalla (dashboard/menú principal) después de login exitoso
- **Arquitectura futura**: Extraer lógica de validación a módulo `src/auth/validator.py` para mejor testing y separación de responsabilidades (UI vs lógica de negocio).
- **Colores**: Se usan colores estándar de feedback:
  - Verde `#27ae60` → éxito
  - Rojo `#e74c3c` → error
  - Naranja `#e67e22` → advertencia
- **Emojis**: Se usan emojis `✅` y `❌` para reforzar el feedback visual. Son opcionales y pueden removerse si causan problemas de encoding en algunos sistemas Windows antiguos.
