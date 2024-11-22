class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock_inicial, categoria, proveedores=None, bodegas=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria  
        self.proveedores = proveedores or []  
        self.bodegas = bodegas or []  
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock_inicial": self.stock,
            "categoria": self.categoria.id,  
            "proveedores": [proveedor.id for proveedor in self.proveedores],  
            "bodegas": [bodega.id for bodega in self.bodegas]  
        }
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion}, Stock: {self.stock}, Precio: {self.precio}"
