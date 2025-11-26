def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def sumar(lista):
    return sum(lista)
print(sumar([1,2,3,4,5,6,7,8,9,10]))

class medicamento():
   def __init__(self,nombre, precio, categoria, stock, codigo_de_barra):
       self.nombre = nombre
       self.precio = precio
       self.categoria = categoria
       self.stock = stock
       self.codigo_de_barra = codigo_de_barra

   def reponer(self):
       cantidad_reponer = int(input("Ingrese La cantidad a reponer: "))
       aux = self.stock
       self.stock = self.stock + cantidad_reponer
       return self.stock
   def vender(self):
       cantidad_producto = int(input("Ingrese cantidad a comprar: "))
       aux = self.stock
       self.stock = self.stock - cantidad_producto
       if self.stock < 0:
           print("No hay suficiente Cantidad")
           self.stock = aux
       return self.stock


   def esta_en_stock_critico(self):
       if self.stock<10:
           return True
       else:
           return False


ibuprofeno = medicamento("Ibuprofeno 600mg", 150.0, "aliviante", 80, 1120893645)
paracetamol = medicamento("Paracetamol 500mg", 120.0, "aliviante",100, 1207336271)
print(ibuprofeno.nombre,ibuprofeno.precio,ibuprofeno.categoria,ibuprofeno.stock,ibuprofeno.codigo_de_barra,ibuprofeno.esta_en_stock_critico())
print(paracetamol.nombre,paracetamol.precio,paracetamol.categoria,paracetamol.stock,paracetamol.codigo_de_barra,paracetamol.esta_en_stock_critico())
def comprar():
    seguimos = True
    while seguimos:
        eleccion = int(input("""Elija que producto quiere comprar:
              1. Ibuprofeno 600mg 
              2. Paracetamol 500mg
              3. Salir: """))
        if eleccion == 1:
            print(f"El stock Actual del Ibuprofeno es:",ibuprofeno.vender())
        elif eleccion == 2:
            print("El stock Actual del Paracetamol es:",paracetamol.vender())
        elif eleccion == 3:
            print("Saliendo del Programa...")
            seguimos = False
comprar()

def reponer():
    seguimos = True
    while seguimos:
        escoger_producto = (
            int(input("""Ingrese El producto al cual reponer su stock:
                                1. Ibuprofeno 600mg
                                2. Paracetamol 500mg: """)))
        if escoger_producto == 1:
            print("Cantidad Actual: ",ibuprofeno.reponer())
        elif escoger_producto == 2:
            print("Cantidad Actual: ",paracetamol.reponer())
reponer()
print(ibuprofeno.nombre,ibuprofeno.precio,ibuprofeno.categoria,ibuprofeno.stock,ibuprofeno.codigo_de_barra,ibuprofeno.esta_en_stock_critico())
print(paracetamol.nombre,paracetamol.precio,paracetamol.categoria,paracetamol.stock,paracetamol.codigo_de_barra,paracetamol.esta_en_stock_critico())
