import database  # Importamos nuestro propio modulo

def mostrar_menu():
    """
    Imprime las opciones disponibles en la terminal.
    """
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Registrar nuevo producto")
    print("2. Visualizar productos registrados")
    print("3. Actualizar producto por ID")
    print("4. Eliminar producto por ID")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")

def pedir_entero(mensaje):
    """
    Pide un numero entero y valida que no sea texto ni este vacio.
    """
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("Error: Ingresa un numero entero valido.")

def pedir_float(mensaje):
    """
    Pide un numero con decimales y valida que el formato sea correcto.
    """
    while True:
        valor = input(mensaje).strip()
        # Validamos que sea numerico aceptando un solo punto decimal
        if valor.replace(".", "", 1).isdigit() and valor.count(".") <= 1:
            return float(valor)
        print("Error: Ingresa un precio valido (ej: 1200 o 350.50).")

def pedir_texto(mensaje):
    """
    Pide una cadena de texto y asegura que no se presione enter en vacio.
    """
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: Este campo es obligatorio.")

# Al arrancar el programa creamos la base de datos y la tabla
database.crear_tabla()

# Bucle principal de la aplicacion
while True:
    mostrar_menu()
    opcion = input("Elegi una opcion (1-7): ").strip()

    if opcion == "1":
        print("\n[Nuevo Registro]")
        nombre = pedir_texto("Nombre del producto: ")
        descripcion = input("Descripcion (opcional): ").strip()
        cantidad = pedir_entero("Cantidad en stock: ")
        precio = pedir_float("Precio: ")
        categoria = pedir_texto("Categoria: ")

        database.registrar_producto(nombre, descripcion, cantidad, precio, categoria)
        print("¡Producto registrado exitosamente!")

    elif opcion == "2":
        print("\n[Productos Registrados]")
        productos = database.visualizar_productos()
        if not productos:
            print("El inventario esta vacio.")
        else:
            # Recorremos la lista de tuplas que nos dio la base de datos
            for prod in productos:
                # prod[0] es ID, prod[1] es nombre, prod[3] cantidad, prod[4] precio, prod[5] categoria
                print(f"ID: {prod[0]} | {prod[1]} ({prod[5]}) - Stock: {prod[3]} - Precio: ${prod[4]}")

    elif opcion == "3":
        print("\n[Actualizar Datos]")
        id_modificar = pedir_entero("Ingresa el ID del producto a modificar: ")
        existente = database.buscar_producto_id(id_modificar)

        if existente:
            print(f"Modificando el producto actual: {existente[1]}")
            nombre = pedir_texto("Nuevo Nombre: ")
            descripcion = input("Nueva Descripcion (opcional): ").strip()
            cantidad = pedir_entero("Nueva Cantidad: ")
            precio = pedir_float("Nuevo Precio: ")
            categoria = pedir_texto("Nueva Categoria: ")

            database.actualizar_producto(id_modificar, nombre, descripcion, cantidad, precio, categoria)
            print("¡Producto actualizado con exito!")
        else:
            print("No se encontro ningun producto con ese ID.")

    elif opcion == "4":
        print("\n[Eliminar Producto]")
        id_eliminar = pedir_entero("Ingresa el ID del producto a borrar: ")
        existente = database.buscar_producto_id(id_eliminar)

        if existente:
            confirmar = input(f"¿Seguro que queres eliminar '{existente[1]}'? (s/n): ").lower().strip()
            if confirmar == "s":
                database.eliminar_producto(id_eliminar)
                print("Producto eliminado correctamente.")
            else:
                print("Operacion cancelada.")
        else:
            print("No se encontro ningun producto con ese ID.")

    elif opcion == "5":
        print("\n[Menu de Busqueda]")
        print("1. Buscar por ID")
        print("2. Buscar por Nombre")
        sub_opcion = input("Elegi una opcion: ").strip()

        if sub_opcion == "1":
            id_buscar = pedir_entero("Ingresa el ID: ")
            prod = database.buscar_producto_id(id_buscar)
            if prod:
                print(f"\nResultado -> ID: {prod[0]} | {prod[1]} | Categoria: {prod[5]} | Stock: {prod[3]} | Precio: ${prod[4]} | Desc: {prod[2]}")
            else:
                print("No se encontraron resultados para ese ID.")
        elif sub_opcion == "2":
            nom_buscar = pedir_texto("Ingresa el nombre (o parte de el): ")
            resultados = database.buscar_producto_nombre(nom_buscar)
            if resultados:
                for prod in resultados:
                    print(f"ID: {prod[0]} | {prod[1]} - Stock: {prod[3]} - Precio: ${prod[4]}")
            else:
                print("No se encontraron productos con ese nombre.")
        else:
            print("Opcion de busqueda invalida.")

    elif opcion == "6":
        print("\n[Reporte de Bajo Stock]")
        limite = pedir_entero("Ingresa el limite de stock maximo: ")
        resultados = database.reporte_bajo_stock(limite)
        
        if resultados:
            print(f"\nProductos con stock menor o igual a {limite}:")
            for prod in resultados:
                print(f"ID: {prod[0]} | {prod[1]} - Stock actual: {prod[3]}")
        else:
            print(f"Todo en orden. Ningun producto tiene stock menor o igual a {limite}.")

    elif opcion == "7":
        print("\nSaliendo del programa... ¡Exitos en la entrega!")
        break
    else:
        print("Opcion invalida. Elegi un numero del 1 al 7.")