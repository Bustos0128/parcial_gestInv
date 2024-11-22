import tkinter as tk
from tkinter import ttk
from gui.productos_gui import ProductosGUI
from gui.categorias_gui import CategoriasGUI
from gui.proveedores_gui import ProveedoresGUI
from gui.bodegas_gui import BodegasGUI
from gui.reportes_gui import ReportesGUI

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión de Inventario")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.menu_frame, text="Bienvenido al Sistema de Inventario", font=("Arial", 20))
        self.label.pack(pady=20)

        self.productos_button = tk.Button(self.menu_frame, text="Gestionar Productos", command=self.open_productos)
        self.productos_button.pack(pady=10)

        self.categorias_button = tk.Button(self.menu_frame, text="Gestionar Categorías", command=self.open_categorias)
        self.categorias_button.pack(pady=10)

        self.proveedores_button = tk.Button(self.menu_frame, text="Gestionar Proveedores", command=self.open_proveedores)
        self.proveedores_button.pack(pady=10)

        self.bodegas_button = tk.Button(self.menu_frame, text="Gestionar Bodegas", command=self.open_bodegas)
        self.bodegas_button.pack(pady=10)

        self.reportes_button = tk.Button(self.menu_frame, text="Ver Reportes", command=self.open_reportes)
        self.reportes_button.pack(pady=10)

    def open_productos(self):
        self.new_window(ProductosGUI)

    def open_categorias(self):
        self.new_window(CategoriasGUI)

    def open_proveedores(self):
        self.new_window(ProveedoresGUI)

    def open_bodegas(self):
        self.new_window(BodegasGUI)

    def open_reportes(self):
        self.new_window(ReportesGUI)

    def new_window(self, gui_class):
        new_window = gui_class(self)
        new_window.grab_set()  # Disable the main window while the new one is open
