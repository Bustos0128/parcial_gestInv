import tkinter as tk
from tkinter import messagebox
from app.sistema_inventario import SistemaInventario

from tkinter import ttk

class ProveedoresGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestionar Proveedores")
        self.geometry("600x400")

        self.sistema = SistemaInventario()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestionar Proveedores", font=("Arial", 18))
        self.label.pack(pady=10)

        self.nombre_label = tk.Label(self, text="Nombre del Proveedor:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        self.direccion_label = tk.Label(self, text="Dirección del Proveedor:")
        self.direccion_label.pack()
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.pack(pady=5)

        self.telefono_label = tk.Label(self, text="Teléfono del Proveedor:")
        self.telefono_label.pack()
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.pack(pady=5)

        self.agregar_button = tk.Button(self, text="Agregar Proveedor", command=self.agregar_proveedor)
        self.agregar_button.pack(pady=10)

        self.ver_button = tk.Button(self, text="Ver Proveedores", command=self.ver_proveedores)
        self.ver_button.pack(pady=10)

    def agregar_proveedor(self):
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()

        if nombre and direccion and telefono:
            proveedor = self.sistema.registrar_proveedor(nombre, direccion, telefono)
            if proveedor:
                messagebox.showinfo("Éxito", "Proveedor agregado exitosamente")
            else:
                messagebox.showwarning("Advertencia", "El proveedor ya existe")
            self.nombre_entry.delete(0, tk.END)
            self.direccion_entry.delete(0, tk.END)
            self.telefono_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

    def ver_proveedores(self):
        proveedores = self.sistema.proveedores
        if proveedores:
            # Crear una nueva ventana para mostrar los proveedores
            ventana_proveedores = tk.Toplevel(self)
            ventana_proveedores.title("Lista de Proveedores")
            ventana_proveedores.geometry("700x400")

            # Crear un Treeview para mostrar los datos
            tree = ttk.Treeview(ventana_proveedores, columns=("ID", "Nombre", "Dirección", "Teléfono"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Dirección", text="Dirección")
            tree.heading("Teléfono", text="Teléfono")
            tree.column("ID", width=50)
            tree.column("Nombre", width=200)
            tree.column("Dirección", width=250)
            tree.column("Teléfono", width=100)
            tree.pack(fill=tk.BOTH, expand=True, pady=10)

            # Insertar los datos de los proveedores en el Treeview
            for proveedor in proveedores:
                tree.insert("", "end", values=(proveedor.id, proveedor.nombre, proveedor.direccion, proveedor.telefono))
        else:
            messagebox.showinfo("Sin datos", "No hay proveedores registrados.")
