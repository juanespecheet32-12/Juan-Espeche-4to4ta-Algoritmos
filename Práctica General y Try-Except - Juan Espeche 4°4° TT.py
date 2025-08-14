import time
import random
def ejercicio1():
    plata_usuario = 1000
    seguimos = True
    while seguimos == True:
        try:
            opc = int(input("""Elegí una Opción:
            1. Depositar Dinero
            2. Retirar Dinero
            3. Salir : """))
            if opc == 1:
                opc2 = int(input("Ingrese el Monto a Depositar: "))
                plata_usuario += opc2
                print("Su Monto bancario ahora es de", plata_usuario)
            elif opc == 2:
                opc3 = int(input("Ingrese el Monto a Retirar: "))
                if opc3 > plata_usuario:
                    print("El Monto Escrito es mayor al Saldo Disponible, Inténtelo de Nuevo: ")
                else:
                    print(f"Ha retirado ${opc3}")
                    plata_usuario = plata_usuario - opc3
                    print(f"Tiene en total el monto en su cuenta de {plata_usuario}")
            elif opc == 3:
                print("Saliendo del Programa...")
                time.sleep(1)
                seguimos = False
        except(ValueError, TypeError):
            print("Valor Incorrecto o Suma Inválida, Inténtelo de Nuevo: ")

def ejercicio2():
    IMC = 0
    seguimos = True
    try:
        peso = int(input("Ingrese su Peso: "))
        altura = float(input("Ingrese su Altura: "))
        IMC = peso / (altura * altura)
        print("Su Índice de Masa Corporal es:", IMC)
        seguimos = False

    except(ValueError, TypeError):
        print("Valor Incorrecto o Suma Inválida, Inténtelo de Nuevo: ")

def ejercicio3():
    vocales = ["a","e","i","o","u"]
    seguimos = True
    try:
        frase = input("Ingrese una Frase: ")
        if frase == "agusfortnite2008":
            print("Nooo todo menos esoo")
            seguimos = False
        else:
            for vocales_a_buscar in range(0, len(vocales) - 1):
                vocal_aleatoria = random.randint(0, 4)
                frase = frase.replace(vocales[vocales_a_buscar], vocales[vocal_aleatoria])
            print(frase)
    except ValueError:
        print("Valor Inválido, Inténtelo de Nuevo: ")

def ejercicio4():
    frase_invertida=""
    palabras_separadas = []
    seguimos = True
    while seguimos == True:
        frase = input("Ingrese una frase: ")
        palabras_separadas = frase.split()
        print(palabras_separadas)
        for x in range(0, len(palabras_separadas)):
            palabras_separadas[x] = palabras_separadas[x][::-1]
        frase_invertida += " ".join(palabras_separadas)
        print(frase_invertida)

def ejercicio5():
    nombres = ["Brunini", "Chechini", "Traviesini", "Juanini"]
    quiere_seguir = True
    while quiere_seguir == True:
        try:
            print("Tienes una lista de nombres ya definida.")
            opc = int(input("""¿Quieres agregar más nombres?
                1.Si
                2.No
                Opción: """))
            if opc == 1:
                opc2 = str(input("Qué nombre quieres agregar?: "))
                nombres.append(opc2)
                opc3 = int(input("Ingrese algun indice de la lista: "))
                print("Usted eligio el nombre:", nombres[opc3])
            elif opc == 2:
                print("Elegiste no agregar mas nombres.")
                print(f"Tu lista quedo conformada con los siguientes nombres: {nombres}")
                quiere_seguir = False
        except (ValueError, IndexError):
            print("Usted ha ingresado un dato incorrecto. Vuelva a intentarlo.")

def menu():
    quiere_seguir = True
    while quiere_seguir == True:
        opc = int(input("""
    ------------------------------------
    1.Cuenta Bancaria
    2.IMC
    3.Frases y Vocales
    4.Frase con palabra invertida
    5.Nombres
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
        elif opc == 5:
            ejercicio5()
menu()