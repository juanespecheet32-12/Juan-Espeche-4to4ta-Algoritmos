def ejercicio1():
    num = [10, 20, 30, 40, 50]
    acumulador = 0
    for x in num:
        acumulador += x
        print(acumulador)
    print("Entonces la suma total es:", acumulador)
def ejercicio2():
    cadena = input("Ingrese algo: ")
    cont_vocales = 0
    vocales = ("aeiouAEIOU")
    for vocal in cadena:
        if vocal in vocales:
            cont_vocales += 1
    print("Hay", cont_vocales, "vocales.")
def ejercicio3():
    num = int(input("Ingrese un numero entero: "))
    for x in range(1, 11):
        print(num * x)
def ejercicio4():
    num_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cant_numpares = []
    num_pares = (2, 4, 6, 8, 10)
    for par in num_enteros:
        if par in num_pares:
            cant_numpares.append(par)
    print("Hay", len(num_pares), "números pares en la lista.")
def ejercicio5():
    numero_filas = int(input("Ingrese un Número para las filas:"))
    for filas in range(1, numero_filas + 1):
        for x in range(1, filas + 1):
            print("*", end="")
        print(" ")
def menu():
    seguir = True
    while seguir:
        opc = int(input("""
        ---------------------------
        1.Numeros enteros
        2.Mayúsculas y minusculas
        3.Multiplicador de numeros
        4.Numeros pares
        0.Salir del programa
        ---------------------------
        Seleccione una funcion: """))
        if opc == 1:
            ejercicio1()
        elif opc == 2:
            ejercicio2()
        elif opc == 3:
            ejercicio3()
        elif opc == 4:
            ejercicio4()
        elif opc == 0:
            print("Saliendo del programa...")
            seguir = False
menu()