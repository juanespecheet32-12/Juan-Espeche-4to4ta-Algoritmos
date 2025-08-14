def ejercicio1():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(num1 / num2)
    except ZeroDivisionError:
        print("¡El número no se puede dividir por cero!")
def ejercicio2():
    seguimos = True
    while seguimos == True:
        try:
            edad = int(input("Ingrese su edad: "))
            seguimos = False
        except ValueError:
            print("Error. Intente de nuevo: ")
def ejercicio3():
    seguimos = True
    while seguimos == True:
        try:
            nombres = ["Ana", "Pedro", "Sofía"]
            indice = int(input("Ingrese un índice de la lista: "))
            print(nombres[indice])
            seguimos = False
        except (IndexError, TypeError):
            print("Error. Su número esta fuera del rango de la lista o ingresó otro tipo de dato.")
def ejercicio4():
    seguimos = True
    while seguimos == True:
        try:
            num1 = int(input("Ingrese un número entero: "))
            num2 = int(input("Ingrese otro número entero: "))
            print(num1 + num2)
            seguimos = False
        except (TypeError, ValueError):
            print("Error. Lo que ingreso no es un número o intento sumar un número con otro dato.")
def ejercicio5():
    try:
        num1 = int(input("Ingrese un número para dividirlo: "))
        num2 = int(input("Ingrese su último número: "))
        print(num1 / num2)
    except (ValueError, ZeroDivisionError):
        print("Error. Ingreso un dato incorrecto o un valor nulo (0).")
        num1err = int(input("Ingrese otro número para que este se divida: "))
        num2err = int(input("Ingrese su último número: "))
    finally:
        print("Fin del programa de cálculo.")

opc = int(input("""
                -------------------------
                1.División
                2.Edad
                3.Lista de nombres
                4.Suma de números enteros
                5.División de dos números
                -------------------------
                Ingrese un número para que se ejecute una función:  """))
if opc == 1:
    ejercicio1()
elif opc == 2:
    ejercicio2()
elif opc == 3:
    ejercicio3()
elif opc == 4:
    ejercicio4()
elif opc == 5:
    ejercicio5()
elif opc == 0:
    print("Fin del programa. Chau Travieso uwu")