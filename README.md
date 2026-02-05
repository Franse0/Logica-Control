# Lógica Control - Sistema de Control de Acceso para Gimnasios

## Descripción

Aplicación local de control de acceso para gimnasios mediante validación biométrica (huella dactilar).

---

## Funcionalidades

### Gestión de Socios
- Registro de nuevos socios con datos básicos
- Captura y almacenamiento de huellas dactilares
- Asignación de planes/membresías

### Control de Acceso
- Validación de huella en tiempo real
- Verificación de estado del socio y vigencia de membresía
- Activación de cerradura magnética/relé para permitir ingreso
- Registro de eventos de acceso

---

## Comportamiento Esperado

### Alta de Socio
1. Ingresar datos del socio
2. Capturar huella dactilar (template biométrico)
3. Asociar huella al socio

### Ingreso al Gimnasio
1. Socio coloca huella en lector biométrico (Digital Persona 4500)
2. Sistema identifica al socio
3. Sistema valida:
   - Estado del socio (activo/bloqueado)
   - Vigencia de membresía
   - Estado de pago
4. **Si todo está OK**: Abre puerta (activa relé/cerradura)
5. **Si hay problema**: Muestra advertencia y deniega acceso
6. Registra el evento (fecha/hora, socio, resultado)

---

## Modelo de Datos

- **Socio**: Datos personales y template biométrico
- **PlanesGimnasio**: Tipos de membresía disponibles
- **SocioPlanInscripcion**: Plan actual del socio, fechas de vigencia, estado de pago
- **AsistenciaSocio**: Historial de accesos

---

## Reglas de Acceso

**Acceso permitido cuando:**
- Socio está activo
- Membresía vigente
- Estado de pago al día

**Acceso denegado:** Cualquier otra situación genera advertencia
