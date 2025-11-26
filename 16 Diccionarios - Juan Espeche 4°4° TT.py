def ejercicio1():
    informacion_personal = {"nombre": "Juan", "edad": 17, "ciudad": "Villa Urquiza", "profesion": "Estudiante"}
    for dato in informacion_personal.values():
        print(dato)

def ejercicio2():
    informacion_personal = {"nombre": "Juan", "edad": 17, "ciudad": "Villa Urquiza", "profesion": "Estudiante"}
    informacion_personal["ciudad"] = "Monroe 5700"
    informacion_personal["profesion"] = "Futuro Técnico"
    informacion_personal["teléfono"] = 1169421871
    informacion_personal["email"] = "juanespeche11@gmail.com"
    for x in informacion_personal.values():
        print(x)

def ejercicio3():
    calificaciones = {"Matemática": 8, "Lengua y Literatura": 10, "Historia": 9, "Teatro": 7, "Biologia": 8, }
    print(calificaciones["Lengua y Literatura"])

def ejercicio4():
    promedio = 0
    materias = 5
    calificaciones = {"Matemática": 8, "Lengua y Literatura": 10, "Historia": 9, "Teatro": 7, "Biologia": 8, }
    for calificacion in calificaciones.values():
        promedio += calificacion
    promedio = promedio / materias
    print(f"El promedio de las calificaciones del alumno es: {promedio}")

def ejercicio5():
    mundo = {"argentina": "buenos aires",
             "mexico": "ciudad de mexico",
             "estados unidos": "washington",
             "colombia": "bogota",
             "paraguay": "asunción",
             "ecuador": "quito",
             "bolivia": "sucre",
             "brasil": "brasilia"}
    while True:
        opc = str(input("Ingrese el nombre de un pais de américa que usted quiera: "))
        if opc in mundo:
            print(mundo[opc])
        else:
            print("Ha ingresado algo mal. Intente de nuevo.")

def ejercicio6():
    Carrito = 0
    Items_Tienda = {
        "manzana": 3.50,
        "leche": 1.20,
        "pan": 2.00,
        "huevos": 2.50,
        "arroz": 1.00,
        "cafe": 4.00,
        "queso": 5.00,
        "tomates": 2.30,
        "pollo": 7.00,
        "azucar": 1.50
    }
    seguimos = True
    while seguimos:
            print("""--------------Menú--------------
                  PRODUCTOS
                  Manzana: 3.50
                  Leche: 1.20
                  Pan: 2.00
                  Huevos": 2.50
                  Arroz": 1.00
                  Cafe": 4.00
                  Queso": 5.00
                  Tomates": 2.30
                  Pollo": 7.00
                  Azucar": 1.50
                  --------------------------------""")
            Producto = str(input("Elige el Producto que quieras llevar(Escriba 'salir' para Salir): ")).lower()
            if Producto == "salir":
                break
            Cantidad = int(input("Elige la cantidad que vas a llevar: "))
            Carrito += Items_Tienda[Producto] * Cantidad
            print("Total: ",Carrito)

def ejercicio7():
    informacion_personal = {
        "nombre": "Juan", 
        "edad": 17, 
        "ciudad": "Villa Urquiza", 
        "profesion": "Estudiante",
        "teléfono": 1169421871,
        "email": "juanespeche11@gmail.com"
    }
    del informacion_personal["teléfono"]
    print(informacion_personal)

def ejercicio8():
    dic1 = {
        "perro" : "animal",
        "gato" : "animal",
        "uno": 1,
        "dos": 2
    }
    esta = input("Ingrese la clave a buscar: ")
    if esta in dic1:
        print(dic1.get(esta), "True")
    else:
        print(dic1.get(esta), "False")

def ejercicio9():
    dic1 = {
        "uno" : 1,
        "dos" : 2
    }
    dic2 = {
        "dos" : 2,
        "tres" : 3
    }
    dic1.update(dic2)
    print(dic1)
