def crear_arreglo():
    cantidad_elementos = int(input("Cuántos elementos tendra el arreglo?: "))
    arreglo = []
    for x in range(cantidad_elementos):
        elemento = int(input(f"Ingrese el elemento {x+1}: "))
        arreglo.append(elemento)
    return arreglo
  
def ordenamiento_seleccion():
    try:
        indice = len(Arreglo)
        for i in range(indice):
            minimo = i
            for j in range(i + 1, n):
                if Arreglo[j] < Arreglo[minimo]:
                    minimo = j
            Arreglo[i], Arreglo[minimo] = Arreglo[minimo], Arreglo[i]
            print(Arreglo)
        return Arreglo
    except NameError:
        print("No se encontro ningún arreglo.")
      
def ordenamiento_insercion():
    try:
        for i in range(1, len(Arreglo)):
            key = Arreglo[i]
            j = i - 1
            while j >= 0 and key < Arreglo[j]:
                Arreglo[j + 1] = Arreglo[j]
                j -= 1
                print(Arreglo)
            Arreglo[j + 1] = key
        return Arreglo
    except NameError:
        print("No se encontro ningún arreglo.") 
      
def ordenamiento_burbuja():
    try:
        n = len(Arreglo)
        for i in range(n - 1):
            Hay_Cambio = False
            for j in range(0, n - i - 1):
                if Arreglo[j] > Arreglo[j + 1]:
                    Arreglo[j], Arreglo[j + 1] = Arreglo[j + 1], Arreglo[j]
                    Hay_Cambio = True
                    print(Arreglo)
            if not Hay_Cambio:
                break
        return Arreglo
    except NameError:
        print("No se encontro ningún arreglo.") 
      
def busqueda_binaria(buscar):
    try:
        ordenado = int(input("""La lista esta ordenada?
        1.Si
        2.No
        Elección: """))
        valor = buscar
        if ordenado == 1:
            izquierda = 0
            derecha = len(Arreglo) - 1
            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2 
                if Arreglo[medio] == valor:
                    print(f"El elemento {buscar} esta en la posicion {medio}")   
                    break
                elif Arreglo[medio] < valor:
                    izquierda = medio + 1 
                else: 
                    derecha = medio - 1 
            return -1
        elif ordenado == 2:
            print("Ordena la lista porque no se puede realizar la búsqueda.")
    except NameError:
        print("No se encontro ningún arreglo.") 
      
def busqueda_secuencial(buscar):
    try:
        valor_a_buscar = buscar
        for i in range(len(Arreglo)):
            if Arreglo[i] == valor_a_buscar:
                return i  
        return -1
    except NameError:
        print("No se encontro ningún arreglo.") 
while True:
    try:
        opcion = int(input("""
        -------------Menú-------------
        1.Crear arreglo
        2.Ordenar
        3.Buscar
        4.Salir
        ------------------------------
        Ingrese una opcion:"""
              ))
        if opcion == 1:
            Arreglo = crear_arreglo()
        elif opcion == 2:
            opcion = int(input("""
            ---------Ordenamiento---------
            1.Burbuja
            2.Insercion
            3.Seleccion
            ------------------------------
            Ingrese una opcion: """))
            if opcion == 1:
                print(F"El Arreglo ordenado es: {ordenamiento_burbuja()}")
            elif opcion == 2:
                print(F"El Arreglo ordenado es: {ordenamiento_insercion()}")
            elif opcion == 3:
                print(F"El Arreglo ordenado es: {ordenamiento_seleccion()}")
            else:
                print("Flaco ingresa bien que queres hacer.")
        elif opcion == 3:
            opcion = int(input("""
            ------Búsqueda------
            1.Binaria
            2.Secuencial
            --------------------
            Ingrese una opcion: """
              ))
            buscar = int(input("Ingrese el elemento a buscar: "))
            if opcion == 1:
                indice = busqueda_binaria(buscar)
                print(F"El elemento {buscar} esta en la posicion: {indice}")
            elif opcion == 2:
                indice = busqueda_secuencial(buscar)
                print(F"El elemento {buscar} esta en la posicion: {indice}")
            else:
                print("Dale loco ingresa bien lo que queres hacer.")
        elif opcion == 4:
           print("Saliendo del programa...")
           break
        else:
            pass
    except ValueError:
        print("Ingrese un valor válida.")
