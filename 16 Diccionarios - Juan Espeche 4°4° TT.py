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
    precios = {"precio_1": 250,
               "precio_2": 100,
               "precio_3": 500,
               "precio_4": 1000,
               "precio_5": 1500
               }
ejercicio6()