import tkinter as tk
from tkinter import messagebox
from models.producto import Producto
from app.sistema_inventario import SistemaInventario

class ProductosGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestionar Productos")
        self.geometry("600x400")

        self.sistema = SistemaInventario()  # Debes instanciar tu sistema de inventario
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Registrar Producto", font=("Arial", 18))
        self.label.pack(pady=10)

        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        self.descripcion_label = tk.Label(self, text="Descripción:")
        self.descripcion_label.pack()
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.pack(pady=5)

        self.precio_label = tk.Label(self, text="Precio:")
        self.precio_label.pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)

        self.stock_label = tk.Label(self, text="Stock Inicial:")
        self.stock_label.pack()
        self.stock_entry = tk.Entry(self)
        self.stock_entry.pack(pady=5)

        self.categoria_label = tk.Label(self, text="Categoría:")
        self.categoria_label.pack()
        self.categoria_entry = tk.Entry(self)
        self.categoria_entry.pack(pady=5)

        self.registrar_button = tk.Button(self, text="Registrar Producto", command=self.registrar_producto)
        self.registrar_button.pack(pady=20)

    def registrar_producto(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = float(self.precio_entry.get())
        stock_inicial = int(self.stock_entry.get())
        categoria = self.categoria_entry.get()

        if nombre and descripcion and precio and stock_inicial and categoria:
            categoria_obj = self.sistema.obtener_categoria(categoria)
            if categoria_obj:
                self.sistema.registrar_producto(nombre, descripcion, precio, stock_inicial, categoria_obj)
                messagebox.showinfo("Éxito", "Producto registrado exitosamente")
                self.destroy()  # Cierra la ventana actual
            else:
                messagebox.showwarning("Error", "Categoría no encontrada")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
