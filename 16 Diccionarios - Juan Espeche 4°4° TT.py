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
    try:
        mundo = [{"paises": "argentina"}, {"paises": "mexico"}, {"paises": "estados unidos"},
                 {"paises": "brasil"}, {"paises": ""}
                 {"paises": "colombia"},
                 {"paises": "paraguay"},
                 {"paises": "bolivia"},
                 {"paises": "ecuador"}
                 ]
ejercicio4()