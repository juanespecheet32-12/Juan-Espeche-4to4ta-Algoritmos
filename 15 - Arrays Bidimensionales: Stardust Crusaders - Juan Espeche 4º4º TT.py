def ejercicio1():
    matriz =[[1, 5, 3, 5],
             [8, 5, 9, 2],
             [4, 5, 6, 7],
             [1, 2, 3, 4]]
    suma_esquinas = 0
    num = len(matriz)
    suma_esquinas += matriz[0][0]
    suma_esquinas += matriz[0][num-1]
    suma_esquinas += matriz[num-1][num-1]
    suma_esquinas += matriz[num-1][0]
    print(suma_esquinas)

def ejercicio2():
    matriz = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
    diag_principal = 0
    diag_secundaria = 2
    suma_diagonal = 0
    suma_diagonal2 = 0
    for x in range(len(matriz)):
        suma_diagonal += matriz[x][diag_principal]
        suma_diagonal2 += matriz[x][diag_secundaria]
        diag_principal += 1
        diag_secundaria -= 1
    print(suma_diagonal , suma_diagonal2)

def ejercicio3():
    tamaño = int(input("Ingrese la dimensión de la matriz identidad: "))
    matriz = []
    for x in range(tamaño):
        fila_nueva = []
        for y in range(tamaño):
            if x == y:
                fila_nueva.append(1)
            else:
                fila_nueva.append(0)
        matriz.append(fila_nueva)
    for x in matriz:
        print(x)
      
def menu():
    quiere_seguir = True
    while quiere_seguir:
        opc = int(input("""
        -------------------Menú---------------------
        1.Suma de esquinas
        2.Suma de diagonales principal y secundaria
        3.Matriz Identidad
        0.Salir del programa
        --------------------------------------------
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
        else:
          print("Opción inválida. Intente de nuevo.")

menu()
