import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app.sistema_inventario import SistemaInventario

class BodegasGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestionar Bodegas")
        self.geometry("600x400")

        self.sistema = SistemaInventario()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestionar Bodegas", font=("Arial", 18))
        self.label.pack(pady=10)

        self.nombre_label = tk.Label(self, text="Nombre de la Bodega:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        self.ubicacion_label = tk.Label(self, text="Ubicación de la Bodega:")
        self.ubicacion_label.pack()
        self.ubicacion_entry = tk.Entry(self)
        self.ubicacion_entry.pack(pady=5)

        self.capacidad_label = tk.Label(self, text="Capacidad Máxima de la Bodega:")
        self.capacidad_label.pack()
        self.capacidad_entry = tk.Entry(self)
        self.capacidad_entry.pack(pady=5)

        self.agregar_button = tk.Button(self, text="Agregar Bodega", command=self.agregar_bodega)
        self.agregar_button.pack(pady=10)

        self.ver_button = tk.Button(self, text="Ver Bodegas", command=self.ver_bodegas)
        self.ver_button.pack(pady=10)

    def agregar_bodega(self):
        nombre = self.nombre_entry.get()
        ubicacion = self.ubicacion_entry.get()
        capacidad = self.capacidad_entry.get()

        if nombre and ubicacion and capacidad:
            try:
                capacidad = int(capacidad)  # Convertir a entero para capacidad
                bodega = self.sistema.registrar_bodega(nombre, ubicacion, capacidad)
                if bodega:
                    messagebox.showinfo("Éxito", "Bodega agregada exitosamente")
                else:
                    messagebox.showwarning("Advertencia", "La bodega ya existe")
                # Limpiar entradas
                self.nombre_entry.delete(0, tk.END)
                self.ubicacion_entry.delete(0, tk.END)
                self.capacidad_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Advertencia", "La capacidad debe ser un número")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

    def ver_bodegas(self):
        bodegas = self.sistema.bodegas
        if bodegas:
            # Crear una nueva ventana para mostrar las bodegas
            ventana_bodegas = tk.Toplevel(self)
            ventana_bodegas.title("Lista de Bodegas")
            ventana_bodegas.geometry("700x400")

            # Crear un Treeview para mostrar los datos
            tree = ttk.Treeview(ventana_bodegas, columns=("ID", "Nombre", "Ubicación", "Capacidad"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Ubicación", text="Ubicación")
            tree.heading("Capacidad", text="Capacidad")
            tree.column("ID", width=50)
            tree.column("Nombre", width=200)
            tree.column("Ubicación", width=200)
            tree.column("Capacidad", width=100)
            tree.pack(fill=tk.BOTH, expand=True, pady=10)

            # Insertar los datos de las bodegas en el Treeview
            for bodega in bodegas:
                tree.insert("", "end", values=(bodega.id, bodega.nombre, bodega.ubicacion, bodega.capacidad_maxima))
        else:
            messagebox.showinfo("Sin datos", "No hay bodegas registradas.")
