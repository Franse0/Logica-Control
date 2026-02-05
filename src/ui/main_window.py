"""
Módulo de ventana principal para Logica Control.

Este módulo contiene la clase MainWindow que implementa la interfaz
gráfica inicial del sistema de control de acceso.
"""

import tkinter as tk


class MainWindow(tk.Tk):
    """Ventana principal de la aplicación Logica Control."""

    def __init__(self):
        """Inicializa la ventana principal con configuración y widgets."""
        super().__init__()

        # Configuración básica de la ventana
        self.title("Logica Control - Sistema de Acceso")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Centrar ventana en pantalla
        self.center_window()

        # Crear widgets de branding
        self.create_widgets()

    def center_window(self):
        """Centra la ventana en la pantalla principal."""
        self.update_idletasks()

        # Obtener dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Obtener dimensiones de la ventana
        window_width = 800
        window_height = 600

        # Calcular posición centrada
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Aplicar geometría centrada
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self):
        """Crea y configura los widgets de la ventana."""
        # Label principal con nombre del sistema
        title_label = tk.Label(
            self,
            text="LOGICA CONTROL",
            font=("Arial", 48, "bold"),
            fg="#2c3e50",
            bg="#f0f0f0"
        )
        title_label.pack(pady=(150, 20))

        # Label de subtítulo descriptivo
        subtitle_label = tk.Label(
            self,
            text="Sistema de Control de Acceso para Gimnasios",
            font=("Arial", 16),
            fg="#7f8c8d",
            bg="#f0f0f0"
        )
        subtitle_label.pack(pady=(0, 20))
