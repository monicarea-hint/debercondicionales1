import tkinter as tk

# Clase principal de la calculadora
class Calculamon:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculamon")
        self.root.configure(bg="pink")  # Fondo rosa
        
        # Variable para almacenar la entrada del usuario
        self.input_text = tk.StringVar()
        
        # Crear la pantalla de la calculadora
        self.create_screen()
        
        # Crear botones
        self.create_buttons()

    def create_screen(self):
        # Pantalla para mostrar los números y resultados
        entry = tk.Entry(self.root, textvariable=self.input_text, font=("Arial", 20), bd=5, insertwidth=4, width=14,
                         justify='right', bg="white")
        entry.pack(pady=10)

    def create_buttons(self):
        # Marco para los botones
        frame = tk.Frame(self.root, bg="pink")
        frame.pack()

        # Botones numéricos
        numbers = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
        ]
        for (text, row, col) in numbers:
            self.create_button(frame, text, row, col, "lime", self.add_to_input)

        # Botones de operaciones
        operations = [
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
        ]
        for (text, row, col) in operations:
            self.create_button(frame, text, row, col, "lightgreen", self.add_to_input)

        # Botón de igual
        self.create_button(frame, '=', 4, 2, "cyan", self.calculate)

        # Botón de limpiar
        self.create_button(frame, 'C', 4, 0, "red", self.clear_input)

    def create_button(self, frame, text, row, col, color, command):
        # Crear un botón con las propiedades dadas
        button = tk.Button(frame, text=text, padx=20, pady=20, font=("Arial", 12), bg=color, command=lambda: command(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def add_to_input(self, value):
        # Agregar el valor del botón presionado al texto actual
        current_text = self.input_text.get()
        self.input_text.set(current_text + value)

    def calculate(self, _=None):
        try:
            # Evaluar la expresión matemática
            result = str(eval(self.input_text.get()))
            self.input_text.set(result)
        except ZeroDivisionError:
            self.input_text.set("Error: División por 0")
        except Exception:
            self.input_text.set("Error: Entrada inválida")

    def clear_input(self, _=None):
        # Limpiar la pantalla de entrada
        self.input_text.set("")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculamon(root)
    root.mainloop()
