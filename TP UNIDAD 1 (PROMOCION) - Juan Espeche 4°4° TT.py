def ejercicio1():
   edad=int(input("ingrese su edad:"))
   if edad > 18:
       print("es mayor de edad")
   else:
       print("es menor de edad ")

def ejercicio2():
   numero = int(input("ingrese un numero:"))
   if numero/2 == 0:
       print("es par")
   else:
       print("no es par")

def ejercicio3():
   contrasena = "pepeelperon37"
   opc = str(input("ingrese su contraseña:"))
   if opc == contrasena:
       print("La contraseña es correcta")
   else:
       print("la contraseña es incorrecta")

def ejercicio4():
 numero = int(input("ingrese un numero:"))
 if numero > 0:
     print("Es positivo.")
 elif numero < 0:
     print("El numero es negativo.")
 else:
     print("el numero es nulo.")

def ejercicio5():
   contrasena = "pepeelperon37"
   intento = True
   intentos = 5
   while intento != False:
       opc = str(input("ingrese su contraseña:"))
       if opc == contrasena:
           print("La contraseña es correcta")
           intento = False
       else:
           print("la contraseña es incorrecta")
           print(f"Tienes la cantidad de intentos de: {intentos}")
           intentos = intentos - 1

def ejercicio6():
   numero=int(input("ingrese un numero:"))
   multi = 10
   for num in range(0,multi):
       print(numero * multi)
       multi = multi - 1

def ejercicio7():
   frase = str(input("Ingrese una frase que quiera repetir: "))
   repeticion = int(input("Ingrese la cantidad de veces que quiera repetir la frase: "))
   while repeticion != 0:
       print(f"Frase: {frase}")
       repeticion = repeticion - 1

def ejercicio8():
   numeros = 0
   numero_sum = []
   while numeros < 100:
       numero = int(input("Ingrese numeros hasta que sea mayor a 100: "))
       numeros = numeros + numero
       numero_sum.append(numero)
   print(f"El numero es mayor que 100, la suma son estos numeros: {numero_sum}")

def menu():
   quiere_seguir = True
   while quiere_seguir == True:
       opc = int(input("""
       --------------------------------------------
       1.Mayor o menor de edad
       2.Par o Impar
       3.Contraseña
       4.Numero positivo o negativo
       5.Contraseña con 5 intentos
       6.Tabla de multiplicar de un numero
       7.Repeticion de una frase
       8.Suma de numeros hasta que sea mayor a 100
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
       elif opc == 4:
           ejercicio4()
       elif opc == 5:
           ejercicio5()
       elif opc == 6:
           ejercicio6()
       elif opc == 7:
           ejercicio7()
       elif opc == 8:
           ejercicio8()
menu()