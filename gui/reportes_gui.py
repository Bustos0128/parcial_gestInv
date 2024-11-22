import tkinter as tk
from tkinter import messagebox
from app.reportes import Reportes
from app.sistema_inventario import SistemaInventario

class ReportesGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Reportes de Inventario")
        self.geometry("600x400")

        self.sistema = SistemaInventario()  
        self.reportes = Reportes()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Generar Reportes", font=("Arial", 18))
        self.label.pack(pady=10)

        self.stock_total_button = tk.Button(self, text="Stock Total", command=self.generar_stock_total)
        self.stock_total_button.pack(pady=10)

        self.stock_categoria_button = tk.Button(self, text="Stock por Categoría", command=self.generar_stock_categoria)
        self.stock_categoria_button.pack(pady=10)

        self.stock_proveedor_button = tk.Button(self, text="Stock por Proveedor", command=self.generar_stock_proveedor)
        self.stock_proveedor_button.pack(pady=10)

        self.stock_bodega_button = tk.Button(self, text="Stock por Bodega", command=self.generar_stock_bodega)
        self.stock_bodega_button.pack(pady=10)

    def generar_stock_total(self):
        total = self.reportes.stock_total(self.sistema.productos)
        messagebox.showinfo("Stock Total", f"El stock total es: {total}")

    def generar_stock_categoria(self):
        categorias = self.reportes.stock_por_categoria(self.sistema.productos)
        result = "\n".join([f"{categoria}: {cantidad}" for categoria, cantidad in categorias.items()])
        messagebox.showinfo("Stock por Categoría", result)

    def generar_stock_proveedor(self):
        proveedores = self.reportes.stock_por_proveedor(self.sistema.productos)
        result = "\n".join([f"{proveedor}: {cantidad}" for proveedor, cantidad in proveedores.items()])
        messagebox.showinfo("Stock por Proveedor", result)

    def generar_stock_bodega(self):
        bodegas = self.reportes.stock_por_bodega(self.sistema.productos, self.sistema.bodegas)
        result = "\n".join([f"{bodega}: {cantidad}" for bodega, cantidad in bodegas.items()])
        messagebox.showinfo("Stock por Bodega", result)
