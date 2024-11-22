class Reportes:
    def stock_total(self, productos):
        return sum([producto.stock for producto in productos])
    
    def stock_por_categoria(self, productos):
        categoria_stock = {}
        for producto in productos:
            if producto.categoria.nombre not in categoria_stock:
                categoria_stock[producto.categoria.nombre] = producto.stock
            else:
                categoria_stock[producto.categoria.nombre] += producto.stock
        return categoria_stock
    
    def stock_por_proveedor(self, productos):
        proveedor_stock = {}
        for producto in productos:
            for proveedor in producto.proveedores:
                if proveedor.nombre not in proveedor_stock:
                    proveedor_stock[proveedor.nombre] = producto.stock
                else:
                    proveedor_stock[proveedor.nombre] += producto.stock
        return proveedor_stock
    
    def stock_por_bodega(self, productos, bodegas):
        bodega_stock = {bodega.nombre: 0 for bodega in bodegas}
        for producto in productos:
            for bodega in producto.bodegas:
                bodega_stock[bodega.nombre] += producto.stock
        return bodega_stock
