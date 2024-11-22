import json
from models.producto import Producto
from models.categoria import Categoria
from models.proveedor import Proveedor
from models.bodega import Bodega

class SistemaInventario:
    def __init__(self):
        self.categorias = self.cargar_categorias()
        self.proveedores = self.cargar_proveedores()
        self.bodegas = self.cargar_bodegas()
        self.productos = self.cargar_productos()
        
        
    #carga de datos
    def cargar_categorias(self):
        try:
            with open("data/categorias.json", "r") as file:
                categorias_data = json.load(file)
                categorias = [Categoria(cat['id'], cat['nombre'], cat['descripcion']) for cat in categorias_data]
                for categoria, cat_data in zip(categorias, categorias_data):
                    categoria.productos = cat_data['productos']
                return categorias
        except FileNotFoundError:
            return []
        
    def cargar_proveedores(self):
        try:
            with open("data/proveedores.json", "r") as file:
                proveedores_data = json.load(file)
                proveedores = [
                    Proveedor(pro["id"], pro["nombre"], pro["direccion"], pro["telefono"])
                    for pro in proveedores_data
                ]
                for proveedor, pro_data in zip(proveedores, proveedores_data):
                    proveedor.productos = pro_data.get("productos", [])
                return proveedores
        except FileNotFoundError:
            return []
    
    def cargar_bodegas(self):
        try:
            with open("data/bodegas.json", "r") as file:
                bodegas_data = json.load(file)
                return [Bodega.from_dict(b) for b in bodegas_data]
        except FileNotFoundError:
            return []
        
    def cargar_productos(self):
        try:
            with open("data/productos.json", "r") as file:
                productos_data = json.load(file)
                productos = [
                    Producto(
                        prod["id"], 
                        prod["nombre"], 
                        prod["descripcion"], 
                        prod["precio"], 
                        prod["stock_inicial"], 
                        self.obtener_categoria_por_id(prod["categoria"]),  # Buscar por ID de la categoría
                        self.obtener_proveedores_por_ids(prod["proveedores"]),  # Buscar proveedores por sus IDs
                        self.obtener_bodegas_por_ids(prod["bodegas"])  # Buscar bodegas por sus IDs
                    )
                    for prod in productos_data
                ]
                return productos
        except FileNotFoundError:
            return []

    # Métodos para obtener objetos de categoría, proveedor y bodega por ID
    def obtener_categoria_por_id(self, categoria_id):
        for categoria in self.categorias:
            if categoria.id == categoria_id:
                return categoria
        return None

    def obtener_proveedores_por_ids(self, proveedor_ids):
        proveedores = []
        for proveedor_id in proveedor_ids:
            proveedor = next((p for p in self.proveedores if p.id == proveedor_id), None)
            if proveedor:
                proveedores.append(proveedor)
        return proveedores

    def obtener_bodegas_por_ids(self, bodega_ids):
        bodegas = []
        for bodega_id in bodega_ids:
            bodega = next((b for b in self.bodegas if b.id == bodega_id), None)
            if bodega:
                bodegas.append(bodega)
        return bodegas

        
    #####metodos de guardar - recuerda convertirlos a dict
    def guardar_categorias(self):
        with open("data/categorias.json", "w") as file:
            categorias_dict = [categoria.to_dict() for categoria in self.categorias]
            json.dump(categorias_dict, file, indent=4)
    
    def guardar_proveedores(self):
        with open("data/proveedores.json", "w") as file:
            proveedores_dict = [proveedor.to_dict() for proveedor in self.proveedores]
            json.dump(proveedores_dict, file, indent=4)
    
    def guardar_bodegas(self):
        with open("data/bodegas.json", "w") as file:
            bodegas_dict = [bodega.to_dict() for bodega in self.bodegas]
            json.dump(bodegas_dict, file, indent=4)
            
    def guardar_productos(self):
        with open("data/productos.json", "w") as file:
            productos_dict = [producto.to_dict() for producto in self.productos]
            json.dump(productos_dict, file, indent=4)   
            
    ######generar IDs
    def generar_id_categoria(self):
        if not self.categorias:
            return "C001"
        ultimo_id = sorted([int(cat.id[1:]) for cat in self.categorias])[-1]
        return f"C{ultimo_id + 1:03}"
    
    def generar_id_proveedor(self):
        ids_validos = [
            int(pro.id[2:]) for pro in self.proveedores if pro.id.startswith('PR') and pro.id[2:].isdigit()
        ]
        
        if not ids_validos:  
            return "PR001"
        
        ultimo_id = max(ids_validos)
        return f"PR{ultimo_id + 1:03}"
    
    def generar_id_bodega(self):
        if not self.bodegas:
            return "B001"  # Si no hay bodegas, inicia desde B001
        ids_existentes = [int(bodega.id[1:]) for bodega in self.bodegas]  # Extraer la parte numérica de los IDs
        nuevo_id = max(ids_existentes) + 1  
        return f"B{nuevo_id:03}"  

    
    def generar_id_producto(self):
        if not self.productos:
            return "P001"
        ultimo_id = sorted([int(prod.id[1:]) for prod in self.productos])[-1]
        return f"P{ultimo_id + 1:03}"

            
    ##### Registrar entidades
    def registrar_producto(self, nombre, descripcion, precio, stock_inicial, categoria, proveedores=None, bodegas=None):
        nuevo_id = self.generar_id_producto()
        producto = Producto(nuevo_id, nombre, descripcion, precio, stock_inicial, categoria, proveedores or [], bodegas or [])
        self.productos.append(producto)
        self.guardar_productos()
        return producto
    
    def registrar_categoria(self, nombre, descripcion):
        if any(categoria.nombre == nombre for categoria in self.categorias):
            return None  # Ya existe
        
        nuevo_id = self.generar_id_categoria()
        categoria = Categoria(nuevo_id, nombre, descripcion)
        self.categorias.append(categoria)
        
        self.guardar_categorias()
        return categoria
    
    def registrar_proveedor(self, nombre, direccion, telefono):
        if any(proveedor.nombre == nombre for proveedor in self.proveedores):
            return None  # Ya existe el proveedor

        nuevo_id = self.generar_id_proveedor()
        
        proveedor = Proveedor(nuevo_id, nombre, direccion, telefono)
        self.proveedores.append(proveedor)
        
        self.guardar_proveedores()
        return proveedor
    
    def registrar_bodega(self, nombre, ubicacion, capacidad_maxima):
            nuevo_id = f"B{len(self.bodegas) + 1:03}"
            bodega = Bodega(nuevo_id, nombre, ubicacion, capacidad_maxima)
            self.bodegas.append(bodega)
            self.guardar_bodegas()
            return bodega

    #### Métodos de consulta
    def consultar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                return vars(producto)
        return None
    
    def consultar_categoria(self, nombre_categoria):
        for categoria in self.categorias:
            if categoria.nombre == nombre_categoria:
                return vars(categoria)
        return None

    def consultar_proveedor(self, nombre_proveedor):
        for proveedor in self.proveedores:
            if proveedor.nombre == nombre_proveedor:
                return vars(proveedor)
        return None
    
    def consultar_bodega(self, nombre_bodega):
        for bodega in self.bodegas:
            if bodega.nombre == nombre_bodega:
                return vars(bodega)
        return None
    
    def consultar_bodega(self, id_bodega):
        for bodega in self.bodegas:
            if bodega.id == id_bodega:
                return bodega
        return None

    #####metodos de obtener
    def obtener_bodegas(self):
        return self.bodegas  

    
    def obtener_proveedores(self):
        return self.proveedores  

    def obtener_categorias(self):
        return self.categorias  # Retorna la lista de categorías cargadas
    
    def obtener_categoria(self, nombre_categoria):
        for categoria in self.categorias:
            if categoria.nombre == nombre_categoria:
                return categoria
        return None

  
  
    

    