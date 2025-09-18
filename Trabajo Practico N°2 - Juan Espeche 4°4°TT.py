import random
def ahorcado():
    intentos = 7
    palabras = ["pepino guau", "algoritmos", "computadora", "palabra", "loma de burro", "cartas"]
    guion = "_"
    palabra = ""
    palabra_seleccionada = palabras[random.randint(0, 5)]
    for x in range(len(palabra_seleccionada)):
        palabra = guion * x
    print("¡Bienvenido al ahorcado!")
    print("Se ha seleccionado una palabra al azar.")
    while intentos != 0 or palabra == palabra_seleccionada:
        opc = str(input(f"""
La palabra esta formada: {palabra}
Tienes {intentos} intentos.
Ingrese una letra para saber si esta en la palabra: """))
        if opc in palabra_seleccionada:
            palabra = palabra
            print("La letra se encontro en la palabra.")
        else:
            intentos = intentos - 1
            print(f"""No se encontro la letra en la palabra seleccionada. 
            Tienes {intentos} intentos.""")
ahorcado()