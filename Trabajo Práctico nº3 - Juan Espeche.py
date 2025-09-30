contactos = []
telefono = []

def anadir_contactos():
    seguimos = True
    while seguimos:
        try:
            nuevo_contacto = input("Ingrese el nombre del Contacto: ").strip()
            telefono_contacto = int(input("Ingrese el Número de teléfono del Contacto: "))
            contactos.append(nuevo_contacto)
            telefono.append(telefono_contacto)
            seguimos = False
        except ValueError:
            print("Dato Incorrecto, Inténtelo de nuevo")
            seguimos = True

def mostrar_contactos():
        if not contactos:
            print("No hay contactos para mostrar.\n")
        else:
            print("\nLista de contactos:")
            for x in range(len(contactos)):
                print(f"{x + 1}. {contactos[x]} - {telefono[x]}")

def buscar_contactos():
    buscar_contacto = input("Ingrese el contacto a buscar: ").strip()
    if buscar_contacto in contactos:
        indice = contactos.index(buscar_contacto)
        print(f"Contacto Encontrado: {contactos[indice]} - {telefono[indice]}\n")
    else:
        print("Contacto no Encontrado :/\n")

def menu():
    while True:
        print("""
        -------Menu--------
        1. Agregar contacto
        2. Mostrar todos los contactos
        3. Buscar contacto por nombre
        4. Salir
        -------------------""")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            anadir_contactos()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contactos()
        elif opcion == "4":
            print("Has salido del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
menu()
