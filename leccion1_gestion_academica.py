import tkinter as tk
from tkinter import messagebox

# Clase que representa a un alumno con sus datos y métodos para calcular su calificación
class Alumno:
    def __init__(self, cc, apellidos, nombre, nota):
        self.cc = cc  # Cédula de ciudadanía (identificación única del alumno)
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()  # Calcula automáticamente la calificación

    def calcular_calificacion(self):
        """Calcula la calificación textual a partir de la nota numérica."""
        if self.nota < 5:
            return "SS"  # Suspenso
        elif self.nota < 7:
            return "AP"  # Aprobado bajo
        elif self.nota < 9:
            return "NT"  # Notable
        else:
            return "SB"  # Sobresaliente

    def actualizar_nota(self, nueva_nota):
        """Actualiza la nota y recalcula la calificación."""
        self.nota = nueva_nota
        self.calificacion = self.calcular_calificacion()

    def __str__(self):
        """Representación en texto del alumno."""
        return f"{self.cc} {self.apellidos}, {self.nombre} {self.nota:.2f} {self.calificacion}"


# Clase que gestiona el conjunto de alumnos
class GestionAlumnos:
    def __init__(self):
        self.alumnos = {}  # Diccionario donde la clave es la cc y el valor es un objeto Alumno

    def mostrar_alumnos(self):
        """Devuelve una cadena con todos los alumnos registrados."""
        return "\n".join(str(alumno) for alumno in self.alumnos.values())

    def introducir_alumno(self, cc, apellidos, nombre, nota):
        """Añade un alumno al sistema, verificando que no exista otro con la misma cc."""
        if cc in self.alumnos:
            return "El alumno ya existe."
        self.alumnos[cc] = Alumno(cc, apellidos, nombre, nota)
        return "Alumno añadido."

    def eliminar_alumno(self, cc):
        """Elimina un alumno basado en su cc."""
        if cc in self.alumnos:
            del self.alumnos[cc]
            return "Alumno eliminado."
        return "Alumno no encontrado."

    def consultar_alumno(self, cc):
        """Consulta la nota y calificación de un alumno usando su cc."""
        if cc in self.alumnos:
            alumno = self.alumnos[cc]
            return f"Nota: {alumno.nota:.2f}, Calificación: {alumno.calificacion}"
        return "Alumno no encontrado."

    def modificar_nota(self, cc, nueva_nota):
        """Modifica la nota de un alumno existente."""
        if cc in self.alumnos:
            self.alumnos[cc].actualizar_nota(nueva_nota)
            return "Nota actualizada."
        return "Alumno no encontrado."

    def mostrar_aprobados(self):
        """Devuelve una cadena con los alumnos aprobados (nota >= 7)."""
        aprobados = [alumno for alumno in self.alumnos.values() if alumno.nota >= 7]
        return "\n".join(str(alumno) for alumno in aprobados)

    def mostrar_reprobados(self):
        """Devuelve una cadena con los alumnos reprobados (nota < 7)."""
        reprobados = [alumno for alumno in self.alumnos.values() if alumno.nota < 7]
        return "\n".join(str(alumno) for alumno in reprobados)


# Interfaz gráfica usando tkinter
class GestionCalificacionesApp:
    def __init__(self, root):
        self.gestion = GestionAlumnos()  # Instancia del gestor de alumnos
        self.root = root
        self.root.title("Gestión de Calificaciones")
        self.root.geometry("500x700")
        self.root.configure(bg="#F8F4FF")  # Fondo color pastel lila
        self.create_widgets()

    def create_widgets(self):
        """Crea y organiza los widgets de la interfaz."""
        # Título
        title = tk.Label(
            self.root,
            text="Gestión de Calificaciones",
            font=("Arial", 18, "bold"),
            bg="#F8F4FF",
            fg="#6A1B9A",
        )
        title.pack(pady=10)

        # Frame para entrada de datos
        frame = tk.Frame(self.root, bg="#E3F2FD")  # Fondo pastel azul claro
        frame.pack(pady=10, padx=10, fill="x")

        # Campos de entrada
        tk.Label(frame, text="CC:", bg="#E3F2FD").grid(row=0, column=0, padx=5, pady=5)
        self.cc_entry = tk.Entry(frame)
        self.cc_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nombre:", bg="#E3F2FD").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Apellidos:", bg="#E3F2FD").grid(row=2, column=0, padx=5, pady=5)
        self.apellidos_entry = tk.Entry(frame)
        self.apellidos_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nota:", bg="#E3F2FD").grid(row=3, column=0, padx=5, pady=5)
        self.nota_entry = tk.Entry(frame)
        self.nota_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botón para añadir alumno
        self.add_button = tk.Button(
            frame,
            text="Añadir Alumno",
            bg="#C8E6C9",
            fg="#2E7D32",
            command=self.add_alumno,
        )
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Botones de acciones adicionales
        self.show_button = tk.Button(
            self.root,
            text="Mostrar Alumnos",
            bg="#FFECB3",
            fg="#FF6F00",
            command=self.show_alumnos,
        )
        self.show_button.pack(pady=5)

        self.aprobados_button = tk.Button(
            self.root,
            text="Mostrar Aprobados",
            bg="#B3E5FC",
            fg="#0277BD",
            command=self.show_aprobados,
        )
        self.aprobados_button.pack(pady=5)

        self.reprobados_button = tk.Button(
            self.root,
            text="Mostrar Reprobados",
            bg="#FFCDD2",
            fg="#D32F2F",
            command=self.show_reprobados,
        )
        self.reprobados_button.pack(pady=5)

        self.result_text = tk.Text(self.root, height=15, bg="#FFFDE7", wrap=tk.WORD)
        self.result_text.pack(padx=10, pady=10)

    def add_alumno(self):
        """Añade un alumno con los datos introducidos en los campos."""
        cc = self.cc_entry.get().strip()
        if not cc.isdigit():
            messagebox.showerror("Error", "La CC debe ser numérica.")
            return
        nombre = self.nombre_entry.get().strip()
        apellidos = self.apellidos_entry.get().strip()
        try:
            nota = float(self.nota_entry.get().strip())
            if not (0 <= nota <= 10):
                raise ValueError("La nota debe estar entre 0 y 10.")
        except ValueError as e:
            messagebox.showerror("Error", "La nota debe ser un número entre 0 y 10.")
            return

        message = self.gestion.introducir_alumno(cc, apellidos, nombre, nota)
        messagebox.showinfo("Resultado", message)

    def show_alumnos(self):
        """Muestra todos los alumnos registrados."""
        alumnos = self.gestion.mostrar_alumnos()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, alumnos if alumnos else "No hay alumnos registrados.")

    def show_aprobados(self):
        """Muestra los alumnos aprobados."""
        aprobados = self.gestion.mostrar_aprobados()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, aprobados if aprobados else "No hay alumnos aprobados.")

    def show_reprobados(self):
        """Muestra los alumnos reprobados."""
        reprobados = self.gestion.mostrar_reprobados()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, reprobados if reprobados else "No hay alumnos reprobados.")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GestionCalificacionesApp(root)
    root.mainloop()
