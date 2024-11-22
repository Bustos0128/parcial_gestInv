import tkinter as tk
from tkinter import messagebox
from app.sistema_inventario import SistemaInventario

class CategoriasGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)  
        self.title("Gestionar Categorías")
        self.geometry("600x400")

        self.sistema = SistemaInventario() 
        self.create_widgets()  

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestionar Categorías", font=("Arial", 18))
        self.label.pack(pady=10)

        self.nombre_label = tk.Label(self, text="Nombre Categoría:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        
        self.descripcion_label = tk.Label(self, text="Descripcion:")
        self.descripcion_label.pack()
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.pack(pady=5)
        

        # btn de agregar, ver categorías y eliminar
        self.agregar_button = tk.Button(self, text="Agregar Categoría", command=self.agregar_categoria)
        self.agregar_button.pack(pady=10)

        self.ver_button = tk.Button(self, text="Ver Categorías", command=self.ver_categorias)
        self.ver_button.pack(pady=10)
        
        self.eliminar_button = tk.Button(self, text="Eliminar Categoría", command=self.eliminar_categoria)
        self.eliminar_button.pack(pady=10)

    def agregar_categoria(self):
        categoria_nombre = self.nombre_entry.get()
        categoria_descripcion = self.descripcion_entry.get()
        
        #validaciones 
        if not categoria_nombre or not categoria_descripcion:
            messagebox.showwarning("!!!", "por favor ingresar un nombre y una descripcion para la categoria")
            return
        
        categorias = self.sistema.obtener_categorias()
        if any(categoria.nombre == categoria_nombre for categoria in categorias):
            messagebox.showwarning("!!!","el nombre de la categoria ya existe")
            return
        
        self.sistema.registrar_categoria(categoria_nombre, categoria_descripcion)
        messagebox.showinfo("Éxito", "Categoría agregada exitosamente")
        self.nombre_entry.delete(0, tk.END)         # Limpiar el campo de nombre
        self.descripcion_entry.delete(0, tk.END)    # Limpiar el campo de descripción
        
    def ver_categorias(self):
        categorias = self.sistema.obtener_categorias()
        
        categorias_text = ""
        for categoria in categorias:
            categorias_text += f"Nombre: {categoria.nombre}\nDescripción: {categoria.descripcion}\n\n"
        
        if categorias_text:
            messagebox.showinfo("Categorías Disponibles", categorias_text)
        else:
            messagebox.showinfo("Categorías Disponibles", "No hay categorías disponibles.")

    def eliminar_categoria(self):
        categoria_nombre = self.nombre_entry.get()

        if not categoria_nombre:
            messagebox.showwarning("Advertencia", "Por favor ingresa el nombre de la categoría a eliminar.")
            return

        categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
        if not categoria:
            messagebox.showerror("Error", f"No se encontró la categoría '{categoria_nombre}'.")
            return

        # Confirmar eliminación
        confirmar = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar la categoría '{categoria_nombre}' y todos sus productos?")
        if not confirmar:
            return

        # Eliminar la categoría
        self.sistema.categorias.remove(categoria)
        self.sistema.guardar_categorias()  # Guardar los cambios en el archivo JSON
        messagebox.showinfo("Éxito", f"La categoría '{categoria_nombre}' ha sido eliminada junto con sus productos.")

        # Limpiar el campo de entrada
        self.nombre_entry.delete(0, tk.END)
