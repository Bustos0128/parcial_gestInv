class Bodega:
    def __init__(self, id_bodega, nombre, ubicacion, capacidad_maxima):
        self.id = id_bodega
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = {}  # Diccionario: {id_producto: cantidad}

    def agregar_producto(self, producto_id, cantidad):
        total_stock = sum(self.productos_almacenados.values())
        if total_stock + cantidad <= self.capacidad_maxima:
            self.productos_almacenados[producto_id] = self.productos_almacenados.get(producto_id, 0) + cantidad
            return f"Producto {producto_id} agregado a la bodega {self.nombre}."
        return "No hay suficiente espacio en la bodega."

    def retirar_producto(self, producto_id, cantidad):
        if producto_id in self.productos_almacenados:
            if self.productos_almacenados[producto_id] >= cantidad:
                self.productos_almacenados[producto_id] -= cantidad
                if self.productos_almacenados[producto_id] == 0:
                    del self.productos_almacenados[producto_id]
                return f"{cantidad} unidades de {producto_id} retiradas de la bodega {self.nombre}."
            return "Stock insuficiente en la bodega."
        return "Producto no encontrado en la bodega."

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "capacidad_max": self.capacidad_maxima,
            "productos_almacenados": self.productos_almacenados,
        }

    @classmethod
    def from_dict(cls, data):
        bodega = cls(
            data["id"],
            data["nombre"],
            data["ubicacion"],
            data["capacidad_max"]
        )
        bodega.productos_almacenados = data.get("productos_almacenados", {})
        return bodega



    def __str__(self):
        return f"Bodega: {self.nombre} - Ubicación: {self.ubicacion}, Capacidad: {self.capacidad_maxima}"
