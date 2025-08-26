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
    for nombre in nombres:
        if nombre in vocales:
            cant_vocales += 1
    print(f"Los nombres tienen {cant_vocales} vocales.")