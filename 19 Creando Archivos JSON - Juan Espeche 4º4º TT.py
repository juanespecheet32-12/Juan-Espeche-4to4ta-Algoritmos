def ejercicio1():
    informacion_personal = {"nombre": "Juan", "edad": 17, "ciudad": "Villa Urquiza", "profesion": "Estudiante"}
    for dato in informacion_personal.values():
        print(dato)
    with open(ej1, 'w', encoding='utf-8') as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej1}' creado con éxito!")
ejercicio1()

def ejercicio2():
    informacion_personal = {"nombre": "Juan", "edad": 17, "ciudad": "Villa Urquiza", "profesion": "Estudiante"}
    informacion_personal["ciudad"] = "Monroe 5700"
    informacion_personal["profesion"] = "Futuro Técnico"
    informacion_personal["teléfono"] = 1169421871
    informacion_personal["email"] = "juanespeche11@gmail.com"
    for x in informacion_personal.values():
        print(x)
    with open(ej2, 'w', encoding='utf-8') as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej2}' creado con éxito!")
ejercicio2()

def ejercicio3():
    calificaciones = {"Matemática": 8, 
                      "Lengua y Literatura": 10, 
                      "Historia": 9, 
                      "Teatro": 7, 
                      "Biologia": 8, }
    print(calificaciones["Lengua y Literatura"])
    with open(ej3, 'w', encoding='utf-8') as archivo:
        json.dump(calificaciones, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej3}' creado con éxito!")
ejercicio3()

def ejercicio4():
    promedio = 0
    materias = 5
    calificaciones = {"Matemática": 8, 
                      "Lengua y Literatura": 10, 
                      "Historia": 9, 
                      "Teatro": 7, 
                      "Biologia": 8, }
    for calificacion in calificaciones.values():
        promedio += calificacion
    promedio = promedio / materias
    print(f"El promedio de las calificaciones del alumno es: {promedio}")
    with open(ej4, 'w', encoding='utf-8') as archivo:
        json.dump(calificaciones, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej4}' creado con éxito!")
ejercicio4()

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
        with open(ej5, 'w', encoding='utf-8') as archivo:
        json.dump(mundo, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej5}' creado con éxito!")
ejercicio5()

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
    with open(ej6, 'w', encoding='utf-8') as archivo:
        json.dump(Items_Tienda, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej6}' creado con éxito!")
ejercicio6()

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
    with open(ej7, 'w', encoding='utf-8') as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej7}' creado con éxito!")
ejercicio7()

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
    with open(ej8, 'w', encoding='utf-8') as archivo:
        json.dump(dic1, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej8}' creado con éxito!")
ejercicio8()

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
    with open(ej1, 'w', encoding='utf-8') as archivo:
        json.dump(dic1, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej1}' creado con éxito!")
ejercicio9()
