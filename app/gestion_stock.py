from models.producto import Producto
from models.bodega import Bodega

class GestionStock:
    @staticmethod
    def agregar_stock(producto, cantidad):
        if isinstance(producto, Producto):
            producto.stock += cantidad
            return f"Se han agregado {cantidad} unidades de {producto.nombre}."
        return "Producto no válido."
    
    @staticmethod
    def retirar_stock(producto, cantidad):
        if isinstance(producto, Producto):
            if producto.stock >= cantidad:
                producto.stock -= cantidad
                return f"Se han retirado {cantidad} unidades de {producto.nombre}."
            return "Stock insuficiente."
        return "Producto no válido."
    
    @staticmethod
    def valor_total_stock(productos):
        total = sum(p.precio * p.stock for p in productos)
        return total
