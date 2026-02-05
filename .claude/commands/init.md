---
name: init
description: Initialize project structure with minimal necessary files and folders
tags: [setup, initialization]
---

You are initializing the **Logica Control** project structure.

## Your Task

Create the minimal necessary structure for the Python application:

### 1. Project Structure

Create these directories:
```
src/
├── models/          # Data models (Socio, Plan, Asistencia)
├── database/        # Database setup and queries
├── ui/              # User interface (Tkinter)
└── utils/           # Utility functions

specs/               # Feature/bug plans (created by /feature and /bug)
data/                # SQLite database files (gitignored)
```

### 2. Configuration Files

Create `.gitignore`:
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# Environment variables
.env
.env.local

# Database
data/*.db
data/*.sqlite
data/*.sqlite3

# Logs
*.log
agents/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Biometric templates (sensitive)
templates/
```

Create `.env.example`:
```env
# API Keys
ANTHROPIC_API_KEY=your_api_key_here

# GitHub Configuration
GITHUB_PAT=your_github_token_here
GITHUB_REPO_OWNER=your_username
GITHUB_REPO_NAME=logica-control-python

# Database
DATABASE_PATH=data/gimnasio.db

# Hardware Configuration
FINGERPRINT_READER=DigitalPersona4500
RELAY_PORT=COM3

# Webhook Server (optional)
PORT=8001

# Application Settings
APP_NAME=Logica Control
APP_VERSION=1.0.0
DEBUG=false
```

Create `requirements.txt`:
```txt
# Core dependencies
pydantic>=2.0.0
python-dotenv>=1.0.0

# ADW dependencies (already installed)
fastapi>=0.104.0
uvicorn>=0.24.0

# Future dependencies (uncomment when needed)
# Pillow>=10.0.0              # For images/photos
# pyserial>=3.5               # For relay control
```

### 3. Database Schema

Create `src/database/schema.sql`:
```sql
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
```

### 4. Main Entry Point

Create `src/main.py`:
```python
"""
Logica Control - Sistema de Control de Acceso para Gimnasios
Entry point de la aplicación
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))


def main():
    """Main entry point"""
    print("=" * 50)
    print("Logica Control - Sistema de Acceso")
    print("=" * 50)
    print()
    print("Inicializando...")

    # TODO: Initialize database
    # TODO: Initialize UI
    # TODO: Initialize fingerprint reader

    print("✅ Sistema listo")


if __name__ == "__main__":
    main()
```

### 5. Database Setup Script

Create `src/database/setup_db.py`:
```python
"""
Database setup script - creates tables from schema.sql
"""

import sqlite3
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


def setup_database():
    """Create database and tables from schema"""
    # Get database path from env or use default
    db_path = os.getenv("DATABASE_PATH", "data/gimnasio.db")

    # Create data directory if it doesn't exist
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    # Read schema
    schema_file = Path(__file__).parent / "schema.sql"
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema = f.read()

    # Create database and execute schema
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

    print(f"✅ Database created at: {db_path}")
    print("✅ Tables created successfully")


if __name__ == "__main__":
    setup_database()
```

### 6. Empty __init__.py files

Create empty `__init__.py` in:
- `src/__init__.py`
- `src/models/__init__.py`
- `src/database/__init__.py`
- `src/ui/__init__.py`
- `src/utils/__init__.py`

## Output

After creating all files and directories, provide a summary:

```
✅ Project initialized successfully

Created directories:
- src/models/
- src/database/
- src/ui/
- src/utils/
- specs/
- data/

Created files:
- .gitignore
- .env.example
- requirements.txt
- src/database/schema.sql
- src/database/setup_db.py
- src/main.py
- All __init__.py files

Next steps:
1. Copy .env.example to .env and fill in your values
2. Run: python src/database/setup_db.py
3. Run: python src/main.py
```

## Important Notes

- Keep it minimal - only create what's listed above
- Don't create extra documentation or unnecessary files
- Don't create example models or UI code yet
- The structure is ready for development with /feature and /bug commands
