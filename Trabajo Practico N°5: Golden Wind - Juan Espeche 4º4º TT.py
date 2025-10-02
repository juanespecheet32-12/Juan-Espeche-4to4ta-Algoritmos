def tateti(matriz):
    # Verificar filas y columnas
    for x in range(3):
        if matriz[x][0] == matriz[x][1] == matriz[x][2] != " ":
            print(f"Ganaron las {matriz[x][0]}")
            return True
        if matriz[0][x] == matriz[1][x] == matriz[2][x] != " ":
            print(f"Ganaron las {matriz[0][x]}")
            return True
    # Verificar diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " ":
        print(f"Ganaron las {matriz[0][0]}")
        return True
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        print(f"Ganaron las {matriz[0][2]}")
        return True
    else: 
      return False

matriz = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]
turno = 9
while not tateti(matriz) and turno > 0:
    cont = 0
    for fila in matriz:
        cont += 1
        print(fila, cont)
    print("  1 ", "  2 ", "  3 ")
    jugador = "O" if turno % 2 == 0 else "X"
    while True:
        try:
            filas = int(input("Ingrese la fila de tu turno (1-3): "))
            columnas = int(input("Ingrese la columna de tu turno (1-3): "))
            if 1 <= filas <= 3 and 1 <= columnas <= 3:
                if matriz[filas - 1][columnas - 1] == " ":
                    matriz[filas - 1][columnas - 1] = jugador
                    turno -= 1
                    break
                else:
                    print("Esa casilla ya está ocupada, elige otra.")
            else:
                print("Fila y columna deben estar entre 1 y 3.")
        except ValueError:
            print("Por favor ingresa números válidos.")
cont = 0
for fila in matriz:
    cont += 1
    print(fila, cont)
print("  1 ", "  2 ", "  3 ")
