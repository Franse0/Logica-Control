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

        # Frame contenedor para el formulario de login
        login_frame = tk.Frame(self, bg="#f0f0f0")
        login_frame.pack(pady=40)

        # Campo de usuario
        username_label = tk.Label(
            login_frame,
            text="Usuario:",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        username_label.pack(pady=(0, 5))

        self.username_entry = tk.Entry(login_frame, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=(0, 15))

        # Campo de contraseña
        password_label = tk.Label(
            login_frame,
            text="Contraseña:",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        password_label.pack(pady=(0, 5))

        self.password_entry = tk.Entry(login_frame, width=30, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=(0, 20))

        # Botón de inicio de sesión
        login_button = tk.Button(
            login_frame,
            text="Iniciar Sesión",
            font=("Arial", 14, "bold"),
            bg="#3498db",
            fg="white",
            padx=40,
            pady=10,
            command=self.validate_login
        )
        login_button.pack(pady=(10, 0))

        # Label de mensajes de feedback
        self.message_label = tk.Label(login_frame, text="", font=("Arial", 12), bg="#f0f0f0")
        self.message_label.pack(pady=(15, 0))

    def show_message(self, text: str, color: str):
        """Muestra un mensaje de feedback al usuario.

        Args:
            text: Mensaje a mostrar
            color: Color del texto en formato hex (ej. #27ae60)
        """
        self.message_label.config(text=text, fg=color)

    def validate_login(self):
        """Valida las credenciales ingresadas en el formulario de login."""
        # Obtener valores de los campos de entrada
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Validación 1 - Campos vacíos
        if not username or not password:
            self.show_message("Complete todos los campos", "#e67e22")
            return

        # Validación 2 - Credenciales hardcodeadas
        if username == "admin" and password == "admin123":
            self.show_message("✅ Inicio de sesión exitoso", "#27ae60")
        else:
            self.show_message("❌ Usuario o contraseña incorrectos", "#e74c3c")
