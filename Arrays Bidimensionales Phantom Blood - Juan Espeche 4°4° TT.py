def ejercicio1():
    print("")
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    for x in matriz:
        print(x)
def ejercicio2():
    print("")
    suma_total = 0
    matriz = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
    for x in matriz[0]:
        suma_total += x
    for y in matriz[1]:
        suma_total += y
    for j in matriz[2]:
        suma_total += j
    print(f"La suma de todos los números de la matriz es: {suma_total}")
def ejercicio3():
    print("")
    indice = 0
    seguimos = True
    while seguimos == True:
        try:
            matriz = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]]
            opc = int(input("Ingrese el número de cualquier índice de la columna de la matriz: "))
            opc2 = int(input("Ingrese el número de cualquier índice de la fila de la matriz: "))
            print(f"El número encontrado con la fila y columna ingresada es: {matriz[opc][opc2]}")
            seguimos = False
        except (ValueError, IndexError):
            print("ERROR ERROR. Haz ingresado algo mal. ERROR ERROR")
def ejercicio4():
    matriz = [[0, 2, 6, 7],
              [3, 9, 1, 4],
              [9, 5, 0, 6,],
              [2, 7, 8, 80]]
    numero_mas_grande = 0
   for fila in matriz:
       print(fila)
       for numero in fila:
           if numero > numero_mas_grande:
               numero_mas_grande = numero
   print(f"El Número Más grande es {numero_mas_grande}")

def menu():
    quiere_seguir = True
    while quiere_seguir == True:
        opc = int(input("""
    ------------------------------------
    1.Matriz cuadriculada
    2.Suma de la matriz
    3.Búsqueda de número en la matriz
    4.Número más grande de la matriz
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

