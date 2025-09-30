def ejercicio1():
   matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
   for x in matriz1:
       filas_suma = 0
       print(x)
       for num in x:
           filas_suma += num
       print(f"La suma de esta fila es: {filas_suma}")
   for x in range(len(matriz1)):
       columnas_suma = 0
       for y in range(len(matriz1[x])):
           columnas_suma += matriz1[y][x]
           print(matriz1[y][x])
       print(f"La suma de esta Columna es: {columnas_suma}")

def ejercicio2():
   traspuesta = [[],
                 [],
                 [],
                 []]
   matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
   for fila in matriz:
       print("Matriz: ", fila)
   for x in range(len(matriz)):
       for y in range(len(matriz[x])):
           traspuesta[x].append(matriz[y][x])
       for traspuesta_final in traspuesta:
           print(matriz_traspuesta_final)
   

def ejercicio3():
   contar_num = 0
   matriz = [[1, 5, 3, 5],
             [8, 5, 9, 2],
             [4, 5, 6, 7]]
   num_ingresado = int(input("Ingrese un número para ver cuantas veces se repite en la matriz: "))
    for fila in matriz:
        print(fila)
        for numero in fila:
            if numero == num_ingresado:
                contador += 1
   print(f"El número ingresado aparece la cantidad de veces de: {contar_num}")

def ejercicio4():
    promedio = 0
    matriz = [[1, 5, 3, 5],
                [8, 5, 9, 2],
                [4, 5, 6, 7],
                [2, 9, 1, 4]]
    matriz_auxiliar = []
    for fila in matriz:
        print(fila)
        for elemento in fila:
            promedio += elemento
    promedio = promedio/16
    for fila in matriz:
        lista_auxiliar = []
        for elemento in fila:
            if elemento < promedio:
                lista_auxiliar.append(promedio)
            else:
                lista_auxiliar.append(elemento)
        matriz_auxiliar.append((lista_auxiliar))
    for x in matriz_auxiliar:
        print(x)

def menu():
    quiere_seguir = True
    while quiere_seguir:
        opc = int(input("""
        ------------------------------------
        1.Suma de filas y columnas
        2.Matriz Traspuesta
        3.Números repetidos de la matriz
        4.Promedio de la matriz
        0.Salir del programa
        ------------------------------------
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

menu()
