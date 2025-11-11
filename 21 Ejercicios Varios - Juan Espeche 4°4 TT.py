def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def sumar(lista):
    return sum(lista)
print(sumar([1,2,3,4,5,6,7,8,9,10]))

class Medicamento:
    def __init__(self, nombre, categoria, stock, precio, codigo_de_barras):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precio = precio
        self.codigo_de_barras = codigo_de_barras

    def vender(self, stock):
        stock_codigo = int(input("Ingrese el codigo del stock: "))
        if stock_codigo == "010000111001":
            print("Haz seleccionado Ibuprofeno 400mg")
            stock_integrado = int(input("Ingrese el valor del stock: "))
            if stock_integrado > stock:
                print("El numero de stock es mayor al stock integrado. El stock no puede venderse")
            elif stock_integrado <= stock:
                stock_integrado = stock_integrado - stock
                print(f"Han comprado {stock} medicamento")
                print(f"Quedan {stock_integrado} medicamento")
            else:
                print("El medicamento no puede venderse. Nos quedamos sin stock.")
        else:
            print("EL medicamento no se encontró.")
        return stock

    def reponer_stock(self, stock):
        stock_codigo = int(input("Ingrese el codigo del stock: "))
        if stock_codigo == self.codigo_de_barras:
            print("Haz seleccionado Ibuprofeno 400")
            stock_agregado = int(input("Ingrese el valor del stock: "))
            if stock_agregado > 0:
                stock = stock + stock_agregado
                print(f"Haz repuesto {stock} Ibuprofenos.")
            elif stock_agregado < 0:
                print("ERROR. Haz ingresado algo mal.")
            else:
                print("ERROR. No puedes poner un numero nulo para su repuesto.")
        return stock

    def esta_en_stock_critico(self):
        if self.stock < 10:
            return True
        else:
            return False

Ibuprofeno400 = Medicamento(nombre="Ibuprofeno 400", categoria="analgesico", stock=10, precio=150, codigo_de_barras="010000111001")
print(Ibuprofeno400.nombre,Ibuprofeno400.categoria,Ibuprofeno400.stock,Ibuprofeno400.precio,Ibuprofeno400.codigo_de_barras)

