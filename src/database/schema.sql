-- Tabla: Socios
CREATE TABLE IF NOT EXISTS socios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    dni TEXT UNIQUE NOT NULL,
    email TEXT,
    telefono TEXT,
    fecha_nacimiento DATE,
    foto_path TEXT,
    estado TEXT DEFAULT 'activo' CHECK(estado IN ('activo', 'inactivo', 'bloqueado')),
    fecha_alta DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: Planes de Gimnasio
CREATE TABLE IF NOT EXISTS planes_gimnasio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    duracion_dias INTEGER NOT NULL,
    estado TEXT DEFAULT 'activo' CHECK(estado IN ('activo', 'inactivo')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: Inscripción de Socio a Plan
CREATE TABLE IF NOT EXISTS socio_plan_inscripcion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    estado_pago TEXT DEFAULT 'pendiente' CHECK(estado_pago IN ('pagado', 'pendiente', 'vencido')),
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (socio_id) REFERENCES socios(id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES planes_gimnasio(id)
);

-- Tabla: Asistencia/Accesos de Socios
CREATE TABLE IF NOT EXISTS asistencia_socio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    resultado TEXT NOT NULL CHECK(resultado IN ('permitido', 'denegado')),
    motivo TEXT,
    dispositivo TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (socio_id) REFERENCES socios(id) ON DELETE CASCADE
);

-- Índices para mejorar rendimiento
CREATE INDEX IF NOT EXISTS idx_socios_dni ON socios(dni);
CREATE INDEX IF NOT EXISTS idx_socios_estado ON socios(estado);
CREATE INDEX IF NOT EXISTS idx_inscripcion_socio ON socio_plan_inscripcion(socio_id);
CREATE INDEX IF NOT EXISTS idx_inscripcion_fechas ON socio_plan_inscripcion(fecha_inicio, fecha_vencimiento);
CREATE INDEX IF NOT EXISTS idx_asistencia_socio ON asistencia_socio(socio_id);
CREATE INDEX IF NOT EXISTS idx_asistencia_fecha ON asistencia_socio(fecha_hora);
