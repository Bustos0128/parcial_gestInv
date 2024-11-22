class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = [] 
    
    def agregar_producto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
    
    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.descripcion}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "productos": self.productos
        }
