"""
Logica Control - Sistema de Control de Acceso para Gimnasios
Entry point de la aplicación
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from ui.main_window import MainWindow

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
    # TODO: Initialize fingerprint reader

    print("✅ Sistema listo")

    # Iniciar interfaz gráfica
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
