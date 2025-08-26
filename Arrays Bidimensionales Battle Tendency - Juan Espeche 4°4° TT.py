def ejercicio1():
    fila1 = 0
    fila2 = 0
    fila3 = 0
    fila4 = 0
    columna1 = 0
    columna2 = 0
    columna3 = 0
    columna4 = 0
    matriz = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    for x in matriz[0]:
        fila1 += x
    for y in matriz[1]:
        fila2 += y
    for j in matriz[2]:
        fila3 += j
    for h in matriz[3]:
        fila4 += h

    print(f"La suma de la primera fila es: {fila1}")
    print(f"La suma de la segunda fila es: {fila2}")
    print(f"La suma de la tercera fila es: {fila3}")
    print(f"La suma de la cuarta fila es: {fila4}")
ejercicio1()