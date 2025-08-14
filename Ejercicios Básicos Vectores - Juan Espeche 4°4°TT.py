def ejercicio1():
    print("")
    print("Código:")
    numeros = []
    num1 = int(input("Ingrese un número para almacenarlo en la lista de números: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    num4 = int(input("Ingrese el cuarto número: "))
    num5 = int(input("Ingrese el quinto y último número: "))
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)
    numeros.append(num4)
    numeros.append(num5)
    print("Su lista quedo conformada con los siguientes números:")
    for x in range(0, len(numeros), 1):
        print(numeros[x])
def ejercicio2():
    print("")
    print("Código:")
    frutas = ["manzana", "banana", "pomelo", "naranja", "mandarina"]
    busqueda = str(input("Ingrese el nombre de una fruta para buscarla en la lista: "))
    if busqueda in frutas:
        print("Esta fruta se encuentra en la lista")
        print("La fruta está en el índice", frutas.index(busqueda))
    else:
        print("Esta fruta no se encuentra en la lista.")
    print("Fin de la función.")
def ejercicio3():
    print("")
    print("Código:")
    notas_estudiantes = [8, 9, 4, 7, 6, 10, 2, 9, 8, 7]
    suma_total = 0
    promedio = 10
    print("Hay 10 notas de alumnos y se va a calcular la suma total y su promedio entre ellas.")
    print("Las notas son:", notas_estudiantes)
    for x in notas_estudiantes:
        suma_total += x
    print("La suma total de todas las notas es", suma_total)
    print("El promedio de las notas es:", suma_total / promedio)
def ejercicio4():
    print("")
    print("Código:")
    temp = [21, 24, 40, 32, 29]
    temp_max = -1
    temp_min = 100
    for tempmax in temp:
        if tempmax > temp_max:
            temp_max = tempmax
    for tempmin in temp:
        if tempmin < temp_min:
            temp_min = tempmin
    print("Las temperaturas son las siguientes:")
    print(temp)
    print("La temperatura máxima es: ", temp_max)
    print("La temperatura mínima es: ", temp_min)
def ejercicio5():
    print("")
    print("Código:")
    numeros = [7, 2, 15, 9, 19, 17, 1, 27, 3, 6, 4]
    numeros.sort()
    print(f"La lista ordenada de numeros queda conformada asi: {numeros}")
def ejercicio6():
    print("")
    print("Código:")
    numeros = [6, 9, 15, 12, 21, 28, 48, 35, 84, 127, 90, 13, 22, 76, 88, 1]
    num_pares = []
    num_impares = []
    for numero in range(1, len(numeros), 1):
        if numero % 2 == 0:
            num_pares.append(numero)
        elif numero % 2 != 0:
            num_impares.append(numero)
    print(f"Los números pares de la lista son: {num_pares}")
    print(f"Los números impares de la lista son: {num_impares}")
def menu():
    quiere_seguir = True
    while quiere_seguir == True:
        opc = int(input("""
                ------------------------------------
                1.Carga y Recorrido Básico
                2.Búsqueda y Conteo
                3.Suma y Promedio
                4.Encontrar el Valor Máximo y Mínimo
                5.Ordenamiento
                6.Pares e Impares
                0.Salir del programa
                ------------------------------------
                Seleccione un número: """))
        if opc == 0:
            print("Saliendo del programa")
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
menu()