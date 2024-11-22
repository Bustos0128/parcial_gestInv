# SEBASTIAN BUSTOS
# Sistema de Gestión de Inventario

Este proyecto es un sistema para gestionar productos, categorías, proveedores y bodegas. Permite realizar diversas operaciones, como el registro de productos, la actualización de stock, la gestión de bodegas y la generación de reportes relacionados con el estado del inventario. Además, cuenta con una interfaz gráfica desarrollada con Tkinter para facilitar la interacción con el usuario.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

### 1. `app/`
Contiene los módulos principales que implementan la lógica del sistema.

- **`sistema_inventario.py`**: Clase principal que gestiona los productos, categorías, proveedores y bodegas.
- **`gestion_stock.py`**: Lógica para agregar y retirar stock de productos en las bodegas.
- **`reportes.py`**: Generación de reportes de stock.

### 2. `gui/`
Contiene los archivos para la interfaz gráfica (Tkinter).

- **`main_window.py`**: Ventana principal del sistema.
- **`productos_gui.py`**: Interfaz para gestionar productos.
- **`categorias_gui.py`**: Interfaz para gestionar categorías.
- **`proveedores_gui.py`**: Interfaz para gestionar proveedores.
- **`bodegas_gui.py`**: Interfaz para gestionar bodegas.
- **`reportes_gui.py`**: Interfaz para mostrar los reportes generados.
- **`widgets.py`**: Widgets personalizados reutilizables.

### 3. `models/`
Contiene las clases o modelos que representan las entidades del dominio del sistema.

- **`producto.py`**: Clase para gestionar productos.
- **`categoria.py`**: Clase para gestionar categorías de productos.
- **`proveedor.py`**: Clase para gestionar proveedores de productos.
- **`bodega.py`**: Clase para gestionar las bodegas.

### 4. `data/`
Contiene los archivos de datos iniciales en formato JSON.

- **`categorias.json`**: Datos iniciales de categorías.
- **`productos.json`**: Datos iniciales de productos.
- **`proveedores.json`**: Datos iniciales de proveedores.
- **`bodegas.json`**: Datos iniciales de bodegas.

### 5. `utils/`
Contiene utilidades generales, como validaciones y carga de datos desde archivos.

- **`loaders.py`**: Funciones para cargar datos desde archivos JSON.
- **`validators.py`**: Funciones para validar los datos ingresados.

### 6. `docs/`
Contiene documentación adicional del proyecto.

- **`diagrama_clases.png`**: Diagrama UML de clases.
- **`requisitos.md`**: Descripción de los requisitos del sistema.

### 7. Archivos principales:

- **`main.py`**: Punto de entrada de la aplicación.
- **`requirements.txt`**: Librerías necesarias para ejecutar el proyecto.
- **`.gitignore`**: Archivos y directorios a ignorar por Git.
- **`README.md`**: Documentación del proyecto.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/Bustos0128/sistema_gestion_inventario.git
