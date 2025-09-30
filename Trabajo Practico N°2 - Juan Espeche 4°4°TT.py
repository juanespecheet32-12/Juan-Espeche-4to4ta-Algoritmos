import random
def ahorcado():
    intentos = 7
    palabras = ["pepino guau", "algoritmos", "computadora", "palabra", "loma de burro"]
    palabra_=[]
    palabra_elegida = random.choice(palabras)
    for x in range(len(palabra_elegida)):
        palabra_.append("_")
    print("¡Bienvenido al ahorcado!")
    print("Se ha seleccionado una palabra al azar.")
    while intentos>0:
        print(f"{palabra_} intentos restantes: {intentos}")
        letra_elegida = input("Ingrese cualquier letra para saber si esta en la palabra:")
        adivino = False
        for indice_letra in range (len(palabra_elegida)):
            for letra2 in letra_elegida:
                if letra2 == palabra_elegida[indice_letra]:
                    palabra_[indice_letra] = letra2
                    adivino = True
        if not adivino:
        intentos -= 1
        if not "_" in palabra_:
        print("Adivinaste toda la palabra sos muy bueno.")
        break
    if intentos<=0:
        print("Se te acabaron los intentos y no adivinaste toda la palabra. Perdiste.")
    

ahorcado()
