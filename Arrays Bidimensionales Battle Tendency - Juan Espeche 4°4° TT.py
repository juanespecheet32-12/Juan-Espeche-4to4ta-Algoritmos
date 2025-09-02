def ejercicio1():
   suma_fila1 = 0
   suma_fila2 = 0
   suma_fila3 = 0
   suma_fila4 = 0
   suma_colum1 = 0
   suma_colum2 = 0
   suma_colum3 = 0
   suma_colum4 = 0
   matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
   for x in matriz[0]:
       suma_fila1 += x
   for y in matriz[1]:
       suma_fila2 += y
   for p in matriz[2]:
       suma_fila3 += p
   for h in matriz[3]:
       suma_fila4 += h
   suma_colum1 = suma_colum1 + matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0]
   suma_colum2 = suma_colum2 + matriz[0][1] + matriz[1][1] + matriz[2][1] + matriz[3][1]
   suma_colum3 = suma_colum3 + matriz[0][2] + matriz[1][2] + matriz[2][2] + matriz[3][2]
   suma_colum4 = suma_colum4 + matriz[0][3] + matriz[1][3] + matriz[2][3] + matriz[3][3]
   print(f"La suma de la primera fila es de: {suma_fila1}")
   print(f"La suma de la segunda fila es de: {suma_fila2}")
   print(f"La suma de la tercera fila es de: {suma_fila3}")
   print(f"La suma de la cuarta fila es de: {suma_fila4}")
   print(f"La suma de la primera columna es: {suma_colum1}")
   print(f"La suma de la segunda columna es: {suma_colum2}")
   print(f"La suma de la tercera columna es: {suma_colum3}")
   print(f"La suma de la cuarta columna es: {suma_colum4}")

def ejercicio2():
   traspuesta = [[],
                 [],
                 [],
                 []]
   matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
   for x in range(len(matriz)):
       for y in range(len(matriz[x])):
           traspuesta[x].append(matriz[y][x])
   for traspuestafinal in traspuesta:
       print(traspuestafinal)

def ejercicio3():
   contar_num = 0
   matriz = [[1, 5, 3, 5],
             [8, 5, 9, 2],
             [4, 5, 6, 7]]
   num_ingresado = int(input("Ingrese un número para ver cuantas veces se repite en la matriz: "))
   for x in range(len(matriz)):
       if num_ingresado in matriz[x]:
           contar_num += matriz[x].count(num_ingresado)
   print(f"El número ingresado aparece la cantidad de veces de: {contar_num}")

def ejercicio4():
    matriz = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    promedio = 0

def menu():
    quiere_seguir = True
    while quiere_seguir == True:
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