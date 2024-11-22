class Proveedor:
    def __init__(self, id, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []  
    
    def agregar_producto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "productos": self.productos
        }
    
    def __str__(self):
        return f"{self.nombre} - {self.direccion} - {self.telefono}"
