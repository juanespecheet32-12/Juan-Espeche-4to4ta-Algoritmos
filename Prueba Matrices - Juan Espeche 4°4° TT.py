def crearmazo():
    cartas = [[], [], [], []]
    palos = [["Corazones"],
             ["Picas"],
             ["Tréboles"],
             ["Diamantes"]]
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for h in range(len(cartas)):
        for y in range(1):
            cartas[h].append(palos[h])
            for x in range(0, 13):
                cartas[h].append(valores[x])
                if valores == 1:
                    valores[0] = "A"
                if valores == 11:
                    valores[10] = "J"
                if valores == 12:
                    valores[11] = "Q"
                if valores == 13:
                    valores[12] = "K"
    print(f"Tus cartas son: {cartas}")
    return cartas

def balatro():
    mazo = crearmazo()
    matriz52x2 = []
    chips = []

balatro()