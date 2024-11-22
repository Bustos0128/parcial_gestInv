# Requisitos del Sistema

## Requisitos Funcionales

1. **Gestión de Productos**:
   - Registrar productos con su nombre, descripción, precio, stock inicial y categoría.
   - Consultar información de los productos registrados.
   - Actualizar el stock de los productos.
   - Calcular el valor total del stock de un producto.

2. **Gestión de Categorías**:
   - Crear, consultar y eliminar categorías.
   - Asociar productos a categorías.
   - Consultar los productos dentro de cada categoría.

3. **Gestión de Proveedores**:
   - Registrar proveedores con su nombre, dirección, teléfono y los productos que suministran.
   - Consultar la información de proveedores y los productos asociados.
   - Eliminar productos de los proveedores.

4. **Gestión de Bodegas**:
   - Registrar bodegas con su nombre, ubicación y capacidad máxima.
   - Agregar productos a las bodegas y actualizar su cantidad.
   - Retirar productos de las bodegas.
   - Consultar la disponibilidad de productos en cada bodega.

5. **Generación de Reportes**:
   - Generar reportes de stock de productos, indicando la cantidad disponible en las bodegas.
   - Consultar la disponibilidad de productos en las bodegas.

## Requisitos Técnicos

1. **Lenguaje de Programación**:
   - Python 3.7 o superior.

2. **Bibliotecas**:
   - Tkinter: Para la interfaz gráfica de usuario.
   - JSON: Para almacenar y cargar datos desde archivos.
   - Otros paquetes listados en el archivo `requirements.txt`.

3. **Base de Datos**:
   - El sistema no requiere base de datos externa, ya que se utiliza almacenamiento en archivos JSON (`productos.json`, `categorias.json`, `proveedores.json`, `bodegas.json`) para gestionar los datos.

4. **Plataforma**:
   - El sistema debe ser compatible con sistemas operativos Windows, macOS y Linux.

## Requisitos de Hardware

1. **Requisitos Mínimos**:
   - Procesador: Intel Core i3 o equivalente.
   - Memoria RAM: 4 GB.
   - Espacio en disco: 50 MB.

2. **Requisitos Recomendados**:
   - Procesador: Intel Core i5 o equivalente.
   - Memoria RAM: 8 GB.
   - Espacio en disco: 100 MB.

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/Bustos0128/sistema_gestion_inventario.git
