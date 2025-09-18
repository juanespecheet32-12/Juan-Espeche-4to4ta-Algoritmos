def ejercicio1():
    nombres = ["Juan", "Demian", "Travieso", "Bruno", "Agustin", "Alba", "Thiago", "Santiago", "Josué", "Leonel"]
    nombre_largo = ""
    for nombre in nombres:
        if nombre > nombre_largo:
            nombre_largo = nombre
    print(f"El nombre más largo de la lista es: {nombre_largo}")
def ejercicio2():
    nombres = ["Juan", "Demian", "Travieso", "Bruno", "Agustin", "Alba", "Thiago", "Santiago", "Josué", "Leonel"]
    cant_vocales = 0
    vocales = "aeiouAEIOU"
    for x in range(len(nombres)):
        nombre = nombres[x]
        for vocal in nombre:
            if vocal in vocales:
                cant_vocales += 1
    print(f"Los nombres tienen {cant_vocales} vocales.")
def ejercicio3():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30]
    lista_factor = []
    factor = 9
    for x in range(len(lista)):
        num = lista[x]
        lista_factor.append(factor * num)
    print(f"La lista queda: {lista_factor}")
def ejercicio4():
    print("¡Bienvenido al Balatro!")
    num_cartas = []
    palos = []
    seguir = True
    while seguir == True:
        menu = int(input(
            """
----------------------
1.Pedir cartas
2.Descartar cartas
3.Dejar de jugar
----------------------
Seleccione una opcion: """))
        if menu == 1:

