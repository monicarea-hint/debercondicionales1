import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.gestion = GestionAlumnos()
        self.root = root
        self.root.title("Gestión de Calificaciones")
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        self.dni_label = tk.Label(frame, text="DNI:")
        self.dni_label.grid(row=0, column=0)
        self.dni_entry = tk.Entry(frame)
        self.dni_entry.grid(row=0, column=1)

        self.nombre_label = tk.Label(frame, text="Nombre:")
        self.nombre_label.grid(row=1, column=0)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=1, column=1)

        self.apellidos_label = tk.Label(frame, text="Apellidos:")
        self.apellidos_label.grid(row=2, column=0)
        self.apellidos_entry = tk.Entry(frame)
        self.apellidos_entry.grid(row=2, column=1)

        self.nota_label = tk.Label(frame, text="Nota:")
        self.nota_label.grid(row=3, column=0)
        self.nota_entry = tk.Entry(frame)
        self.nota_entry.grid(row=3, column=1)

        self.add_button = tk.Button(frame, text="Añadir Alumno", command=self.add_alumno)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.display_button = tk.Button(frame, text="Mostrar Alumnos", command=self.display_alumnos)
        self.display_button.grid(row=5, column=0, columnspan=2)

    def add_alumno(self):
        dni = self.dni_entry.get()
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        try:
            nota = float(self.nota_entry.get())
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número.")
            return

        mensaje = self.gestion.introducir_alumno(dni, apellidos, nombre, nota)
        messagebox.showinfo("Resultado", mensaje)

    def display_alumnos(self):
        alumnos = self.gestion.mostrar_alumnos()
        messagebox.showinfo("Lista de Alumnos", alumnos if alumnos else "No hay alumnos registrados.")

root = tk.Tk()
app = App(root)
root.mainloop()
