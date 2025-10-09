def ejercicio1():
    productos = [
        {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
        {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
        {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
        {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
    ]
    for producto in productos:
        print(f"Nombre: {producto['nombre']}")
def ejercicio2():
    precio_total = 0
    productos = [
        {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
        {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
        {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
        {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
    ]
    for precios in productos:
        print(f"Precio: {precios['precio']}")

def ejercicio3():
    productos = [
        {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
        {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
        {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
        {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
    ]
    producto_nuevo = {"nombre": "Impresora", "precio": 500, "categoria": "Electrónica"}
    productos.append(producto_nuevo)
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Categoria: {producto['categoria']}")

def ejercicio4():
    productos = [
        {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
        {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
        {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
        {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
    ]
    productos[1]["precio"] = 75
    productos[2]["precio"] = 150
    for precios in productos:
        print(f"Precio: {precios['precio']}")

def ejercicio5():
    nota_max = 0
    estudiante = 0
    estudiantes = [
        {"nombre": "Ana", "edad": 21, "calificacion": 90},
        {"nombre": "Luis", "edad": 22, "calificacion": 95},
        {"nombre": "Marta", "edad": 20, "calificacion": 85}
    ]
    for nota in estudiantes:
        if nota['calificacion'] > nota_max:
            nota_max = nota['calificacion']
            estudiante = nota
    print(f"Alumno con mas nota: {estudiante}")

def ejercicio6():
    estudiantes = [
        {"nombre": "Ana", "edad": 21, "calificacion": 90},
        {"nombre": "Luis", "edad": 22, "calificacion": 95},
        {"nombre": "Marta", "edad": 20, "calificacion": 85}
    ]
    nombres = []
    for estudiante in estudiantes:
        nombres.append(estudiante['nombre'])
    print(nombres)

def ejercicio7():
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
        {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
    ]
    libro_quijote = libros.pop(1)
    print(f"La lista quedo {libros}")
    print(f"Libro eliminado: {libro_quijote}")
    libros.append(libro_quijote)
    print(f"""Se ha vuelto a añadir el libro
Entonces la lista queda: {libros}""")

def ejercicio8():
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
        {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
    ]
    for clave in range(len(libros)):
        libros[clave]["Disponible"] = "True"
    for libro in libros:
        print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Disponible: {libro['Disponible']}")

def menu():
    quiere_seguir = True
    while quiere_seguir:
        opc = int(input("""
        -------------------Menú---------------------
        1.Recorrido de diccionario
        2.Suma total de precios
        3.Nuevo producto a la lista
        4.Actualizacion del precio de la lista
        5.Algoritmo del estudiante con más nota
        6.Algoritmo de nombres de estudiantes
        7.Eliminación del libro de Don Quijote
        8.Creacion de nueva clave
        0.Salir del programa
        --------------------------------------------
        Seleccione un número: """))
        if opc == 0:
            print("Saliendo del programa...")
            quiere_seguir = False
        elif opc == 1:
            ejercicio1()
        elif opc == 2:
            ejercicio2()
        elif opc == 3:
            ejercicio3()
        elif opc == 4:
            ejercicio4()
        elif opc == 5:
            ejercicio5()
        elif opc == 6:
            ejercicio6()
        elif opc == 7:
            ejercicio7()
        elif opc == 8:
            ejercicio8()
        else:
          print("Opción inválida. Intente de nuevo.")

menu()
