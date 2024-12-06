import tkinter as tk
from tkinter import messagebox
import random

class AdivinameApp:
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica y los elementos necesarios para el juego.
        """
        self.root = root
        self.root.title("ADIVÍNAME")  # Título de la ventana
        self.root.geometry("400x400")  # Tamaño de la ventana
        self.root.configure(bg="#2C2C2C")  # Fondo en negro oscuro

        # Inicialización del juego
        self.numero_a_adivinar = random.randint(1, 100)  # Generar número aleatorio
        self.intentos_restantes = 10  # Número máximo de intentos

        # Título del juego
        self.label_titulo = tk.Label(
            root,
            text="¡ADIVINA EL NÚMERO!",
            font=("Arial", 16, "bold"),
            bg="#2C2C2C",  # Fondo negro oscuro
            fg="#FFA500"  # Naranja brillante
        )
        self.label_titulo.pack(pady=10)

        # Campo para ingresar el número
        self.entry_numero = tk.Entry(
            root,
            font=("Arial", 18),  # Tamaño de fuente aumentado
            justify="center",
            bg="#F4F4F4",  # Gris claro
            fg="#000000",  # Negro
            width=10  # Ancho del campo incrementado
        )
        self.entry_numero.pack(pady=10)

        # Botón para realizar la adivinanza
        self.boton_adivinar = tk.Button(
            root,
            text="Adivinar",
            font=("Arial", 14),
            bg="#FFA500",  # Naranja
            fg="#000000",  # Negro
            command=self.verificar_numero
        )
        self.boton_adivinar.pack(pady=10)

        # Etiqueta para mostrar mensajes de retroalimentación
        self.label_mensaje = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            bg="#2C2C2C",  # Fondo negro oscuro
            fg="#FFFFFF"  # Blanco
        )
        self.label_mensaje.pack(pady=10)

        # Etiqueta para mostrar los intentos restantes
        self.label_intentos = tk.Label(
            root,
            text=f"Intentos restantes: {self.intentos_restantes}",
            font=("Arial", 12),
            bg="#2C2C2C",  # Fondo negro oscuro
            fg="#FFA500"  # Naranja brillante
        )
        self.label_intentos.pack(pady=10)

        # Botón para reiniciar el juego
        self.boton_reiniciar = tk.Button(
            root,
            text="Reiniciar",
            font=("Arial", 14),
            bg="#D3D3D3",  # Gris claro
            fg="#000000",  # Negro
            command=self.reiniciar_juego
        )
        self.boton_reiniciar.pack(pady=20)

    def verificar_numero(self):
        """
        Verifica si el número ingresado por el usuario es correcto, demasiado alto o demasiado bajo.
        """
        try:
            # Convertir la entrada del usuario en un número entero
            numero_ingresado = int(self.entry_numero.get())

            # Validar que el número esté dentro del rango permitido
            if numero_ingresado < 1 or numero_ingresado > 100:
                self.label_mensaje.config(text="¡Por favor, ingresa un número entre 1 y 100!")
                return

            # Comprobar si el número ingresado es igual al número a adivinar
            if numero_ingresado == self.numero_a_adivinar:
                messagebox.showinfo("¡Felicidades!", "¡Correcto! Has adivinado el número.")  # Mensaje de éxito
                self.reiniciar_juego()
            elif numero_ingresado < self.numero_a_adivinar:
                self.label_mensaje.config(text="Demasiado bajo. Intenta con un número más alto.")
            else:
                self.label_mensaje.config(text="Demasiado alto. Intenta con un número más bajo.")

            # Reducir los intentos restantes y actualizar la interfaz
            self.intentos_restantes -= 1
            self.label_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")

            # Comprobar si el jugador se quedó sin intentos
            if self.intentos_restantes == 0:
                messagebox.showwarning("Juego terminado", f"¡Has perdido! El número era {self.numero_a_adivinar}.")
                self.reiniciar_juego()
        except ValueError:
            # Mostrar un mensaje si el usuario no ingresa un número válido
            self.label_mensaje.config(text="Por favor, ingresa un número válido.")

    def reiniciar_juego(self):
        """
        Reinicia el juego generando un nuevo número y restableciendo los intentos.
        """
        self.numero_a_adivinar = random.randint(1, 100)  # Generar un nuevo número aleatorio
        self.intentos_restantes = 10  # Reiniciar los intentos
        self.label_mensaje.config(text="")  # Limpiar los mensajes de retroalimentación
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")  # Actualizar intentos restantes
        self.entry_numero.delete(0, tk.END)  # Limpiar el campo de entrada

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinameApp(root)
    root.mainloop()
