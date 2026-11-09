import sqlite3

def conectar():
    """
    Abre la conexion con la base de datos inventario.db.
    Devuelve el objeto de conexion para usarlo en otras funciones.
    """
    return sqlite3.connect("inventario.db")

def crear_tabla():
    """
    Crea la tabla 'productos' si todavia no existe.
    Define las columnas id, nombre, descripcion, cantidad, precio y categoria.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    Guarda un nuevo producto en la base de datos.
    Recibe los datos y los pasa mediante una tupla para evitar errores.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    # Los datos se agrupan en una tupla
    datos = (nombre, descripcion, cantidad, precio, categoria)
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', datos)
    conexion.commit()
    conexion.close()

def visualizar_productos():
    """
    Trae todas las filas de la tabla productos.
    Devuelve una lista llena de tuplas con los datos de cada producto.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    lista = cursor.fetchall()
    conexion.close()
    return lista

def actualizar_producto(id_prod, nombre, descripcion, cantidad, precio, categoria):
    """
    Modifica los datos de un producto buscando por su ID.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    datos = (nombre, descripcion, cantidad, precio, categoria, id_prod)
    cursor.execute('''
        UPDATE productos 
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    ''', datos)
    conexion.commit()
    conexion.close()

def eliminar_producto(id_prod):
    """
    Borra definitivamente un producto de la tabla usando su ID.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    conexion.commit()
    conexion.close()

def buscar_producto_id(id_prod):
    """
    Busca un producto especifico por su numero de ID.
    Devuelve la tupla del producto o None si no lo encuentra.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def buscar_producto_nombre(nombre):
    """
    Busca productos que contengan el nombre ingresado (opcional del enunciado).
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def reporte_bajo_stock(limite):
    """
    Filtra los productos que tengan un stock menor o igual al limite especificado.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados