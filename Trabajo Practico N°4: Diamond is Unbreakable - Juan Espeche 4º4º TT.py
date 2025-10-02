import random
def matrices_y_tesoros():
  intentos = 5
  cofres = 3
  matriz = [["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""]]
  matriz_a_mostrar = [["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""],
                      ["","","","","","","","","",""]]
  for x in range(cofres):
        indice1 = random.randint(0,9)
        indice2 = random.randint(0,9)
        matriz[indice1][indice2] = "✓"

  while cofres > 0 and intentos != 0:
          print(f"Te quedan {intentos} intentos")
          for fila in matriz_a_mostrar:
                  print(fila)
          valor1 = int(input("Ingrese la fila en donde cree que esta: "))
          valor2 = int(input("Ingrese la columna en donde cree que esta: "))
          if matriz[valor1 - 1][valor2 - 1] == "✓":
                  matriz_a_mostrar[valor1 - 1][valor2 - 1] = "✓"
                  cofres -= 1
                  print(f"Acertaste! Te quedan {cofres} Cofres")
          else:
                  matriz_a_mostrar[valor1-1][valor2-1] = "X"
                  print(f"No acertaste. Te quedan {cofres} cofres")
                  intentos -= 1

  if intentos == 0:
          print(f"""Perdiste
          El mapa con los cofres era:
""")
          for fila in matriz:
                  print(fila)
  else:
          print("¡Ganaste! ¡Felicidades!")

matrices_y_tesoros():
